"""Draft a first-pass genre entry via the Groq API for human/Claude review.

Usage:
    python tools/draft_genre_with_groq.py "Genre Name" --parent-genre Rock [--subgenre-of "Parent Subgenre"]

Requires GROQ_API_KEY to be set in the environment. Never commit an API key.
PowerShell:  $env:GROQ_API_KEY = "..."
bash:        export GROQ_API_KEY="..."

Output is NOT written into knowledge_base/ directly. It lands in drafts/genres/
(gitignored) with a DRAFT marker, and must be fact-checked, edited, and manually
moved into knowledge_base/genres/<family>/ before it's real KB content. Run
tools/validate_kb.py after moving it to confirm the frontmatter is schema-valid.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.dont_write_bytecode = True

from kb_utils import ROOT, SCHEMA_ROOT

GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
DEFAULT_MODEL = "openai/gpt-oss-120b"
DEFAULT_REASONING_EFFORT = "high"
DEFAULT_TEMPERATURE = 0.6  # Groq's reasoning-model guidance: 0.5-0.7, lower values risk repetition/incoherence
# Default max_completion_tokens (1024) is too low once reasoning_effort=high is in play —
# the hidden reasoning trace alone can consume most or all of that budget, leaving the
# visible answer truncated or empty. This document is long (frontmatter + 10 prose sections).
DEFAULT_MAX_COMPLETION_TOKENS = 12000
DEFAULT_EXAMPLE = ROOT / "knowledge_base" / "genres" / "rock" / "heartland_rock.md"
DEFAULT_OUTPUT_DIR = ROOT / "drafts" / "genres"

# GPT-OSS models support reasoning_effort; other Groq models don't and error if it's sent.
REASONING_MODEL_PREFIXES = ("openai/gpt-oss",)

SYSTEM_PROMPT = """You write genre profile entries for a music-production knowledge base. \
Match the frontmatter schema and the example entry's structure, depth, and specificity exactly. \
Be concrete: use real artist names, real song titles, precise BPM ranges and LUFS targets. \
Never write generic filler that could apply to any genre — do not repeat the same stock phrase \
("focus on creating a heavy sound", "clear and defined sound", etc.) across different sections; \
each section should say something specific to this genre's actual sonic identity. \
If you are not confident a specific claim (a fact, an artist attribution, a technical number) is \
accurate, mark it inline with an HTML comment immediately after it: <!-- UNVERIFIED: why -->. \
Output ONLY the markdown file content (frontmatter between --- delimiters, then the body \
sections), no other commentary before or after."""


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def build_user_prompt(genre_name: str, parent_genre: str, subgenre_of: str | None, example_text: str, schema_text: str) -> str:
    parts = [
        f"Write a genre profile entry for: {genre_name}",
        f"parent_genre: {parent_genre}",
    ]
    if subgenre_of:
        parts.append(f"subgenre_of: {subgenre_of}")
    parts.append("\n--- FRONTMATTER SCHEMA (schemas/genre_schema.json) ---\n" + schema_text)
    parts.append(
        "\n--- EXAMPLE ENTRY (match this structure, section order, and level of detail) ---\n"
        + example_text
    )
    return "\n".join(parts)


def call_groq(
    api_key: str,
    model: str,
    system_prompt: str,
    user_prompt: str,
    temperature: float,
    reasoning_effort: str | None,
    max_completion_tokens: int,
) -> str:
    # Groq's reasoning-model guidance: avoid a separate system role, put all
    # instructions in the user message. Applying this generally is harmless
    # for non-reasoning models too.
    combined_prompt = f"{system_prompt}\n\n{user_prompt}"

    body_dict: dict = {
        "model": model,
        "messages": [{"role": "user", "content": combined_prompt}],
        "temperature": temperature,
        "max_completion_tokens": max_completion_tokens,
    }

    if reasoning_effort and model.startswith(REASONING_MODEL_PREFIXES):
        body_dict["reasoning_effort"] = reasoning_effort
        body_dict["include_reasoning"] = False

    payload = json.dumps(body_dict).encode("utf-8")

    request = urllib.request.Request(
        GROQ_ENDPOINT,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "music-kb-draft-genre-script/1.0",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Groq API error {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"Could not reach Groq API: {exc.reason}") from exc

    try:
        choice = body["choices"][0]
        content = choice["message"]["content"]
    except (KeyError, IndexError) as exc:
        raise SystemExit(f"Unexpected Groq API response shape: {body}") from exc

    if not content.strip():
        finish_reason = choice.get("finish_reason", "unknown")
        raise SystemExit(
            f"Groq returned empty content (finish_reason={finish_reason!r}). "
            "Likely hit max_completion_tokens before the reasoning trace finished — "
            "try a higher --max-completion-tokens or a lower --reasoning-effort."
        )

    return content


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("genre_name", help="Genre/subgenre name to draft, e.g. \"Dungeon Synth\"")
    parser.add_argument("--parent-genre", required=True, help="Top-level family, e.g. Rock, EDM, Jazz")
    parser.add_argument("--subgenre-of", default=None, help="Immediate parent subgenre, if any")
    parser.add_argument("--example", type=Path, default=DEFAULT_EXAMPLE, help="Template genre file to few-shot from")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Groq model id (default: {DEFAULT_MODEL})")
    parser.add_argument(
        "--reasoning-effort",
        default=DEFAULT_REASONING_EFFORT,
        choices=["low", "medium", "high"],
        help=f"Reasoning effort for GPT-OSS models only, ignored otherwise (default: {DEFAULT_REASONING_EFFORT})",
    )
    parser.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE, help=f"Sampling temperature (default: {DEFAULT_TEMPERATURE})")
    parser.add_argument(
        "--max-completion-tokens",
        type=int,
        default=DEFAULT_MAX_COMPLETION_TOKENS,
        help=f"Response token budget, must cover hidden reasoning + visible answer (default: {DEFAULT_MAX_COMPLETION_TOKENS})",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Where to write the draft (default: drafts/genres/)")
    args = parser.parse_args()

    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print(
            "GROQ_API_KEY is not set.\n"
            "  PowerShell:  $env:GROQ_API_KEY = \"your-key\"\n"
            "  bash:        export GROQ_API_KEY=\"your-key\"",
            file=sys.stderr,
        )
        return 1

    if not args.example.exists():
        print(f"Example file not found: {args.example}", file=sys.stderr)
        return 1

    schema_path = SCHEMA_ROOT / "genre_schema.json"
    example_text = args.example.read_text(encoding="utf-8")
    schema_text = schema_path.read_text(encoding="utf-8")

    user_prompt = build_user_prompt(
        args.genre_name, args.parent_genre, args.subgenre_of, example_text, schema_text
    )

    print(f"Requesting draft for '{args.genre_name}' from Groq ({args.model}, reasoning_effort={args.reasoning_effort})...")
    draft_body = call_groq(
        api_key,
        args.model,
        SYSTEM_PROMPT,
        user_prompt,
        args.temperature,
        args.reasoning_effort,
        args.max_completion_tokens,
    )

    slug = slugify(args.genre_name)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    out_path = args.output_dir / f"{slug}.md"

    marker = (
        f"<!-- DRAFT: AI-generated via Groq (model: {args.model}), UNREVIEWED. "
        "Fact-check before use. Move into knowledge_base/genres/<family>/ only "
        "after review, and run tools/validate_kb.py to confirm schema validity. -->\n\n"
    )
    out_path.write_text(marker + draft_body, encoding="utf-8")

    print(f"Draft written to: {out_path.relative_to(ROOT)}")
    print("This is UNREVIEWED AI output. Fact-check it before moving it into knowledge_base/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
