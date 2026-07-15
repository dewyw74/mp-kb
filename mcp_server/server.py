from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

# The embedding model is cached locally after the first `build_embeddings_index.py`
# run; force offline mode so the server never makes network calls (matches the
# "fully offline, no API dependency" design choice for this server).
os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

ROOT = Path(__file__).resolve().parents[1]
EMBEDDINGS_PATH = ROOT / "knowledge_base" / "embeddings.json"

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "music-kb",
    instructions=(
        "Semantic search over the AI Music Producer Encyclopedia knowledge base "
        "(genres, mixing, mastering, sound design, MIDI, DAW workflows, VST database, "
        "music theory, production). Use search_kb to find relevant entries by meaning "
        "(not just keyword match), then get_kb_entry to read a specific file in full."
    ),
)

_model = None
_entries: list[dict[str, Any]] | None = None


def _load() -> None:
    global _model, _entries
    if _entries is not None:
        return

    if not EMBEDDINGS_PATH.exists():
        raise RuntimeError(
            f"{EMBEDDINGS_PATH} not found. Run `python tools/build_embeddings_index.py` first."
        )

    payload = json.loads(EMBEDDINGS_PATH.read_text(encoding="utf-8"))
    _entries = payload["entries"]

    from sentence_transformers import SentenceTransformer

    _model = SentenceTransformer(payload["model"])


def _cosine_search(query: str, category: str | None, limit: int) -> list[dict[str, Any]]:
    _load()
    assert _model is not None and _entries is not None

    query_vec = _model.encode([query], normalize_embeddings=True)[0]

    candidates = _entries
    if category:
        candidates = [e for e in _entries if e["category"] == category]

    scored = []
    for entry in candidates:
        vec = entry["embedding"]
        score = sum(a * b for a, b in zip(query_vec, vec))
        scored.append((score, entry))

    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [
        {
            "path": entry["path"],
            "title": entry["title"],
            "category": entry["category"],
            "score": round(float(score), 4),
        }
        for score, entry in scored[:limit]
    ]


def _snippet(path: str, max_chars: int = 280) -> str:
    full = (ROOT / path).read_text(encoding="utf-8")
    lines = full.splitlines()
    if lines and lines[0].strip() == "---":
        for index, line in enumerate(lines[1:], start=1):
            if line.strip() == "---":
                body = "\n".join(lines[index + 1 :]).strip()
                break
        else:
            body = full
    else:
        body = full
    body = " ".join(body.split())
    return body[:max_chars] + ("..." if len(body) > max_chars else "")


@mcp.tool()
def search_kb(query: str, category: str | None = None, limit: int = 5) -> list[dict[str, Any]]:
    """Semantically search the music production knowledge base.

    Args:
        query: Natural-language search query (e.g. "sidechain compression for a kick drum").
        category: Optional top-level category filter (e.g. "mixing", "mastering", "genres",
            "sound_design", "midi", "daw", "vst_database", "music_theory", "production").
        limit: Maximum number of results to return (default 5).
    """
    results = _cosine_search(query, category, limit)
    for result in results:
        result["snippet"] = _snippet(result["path"])
    return results


@mcp.tool()
def get_kb_entry(path: str) -> str:
    """Return the full content (frontmatter + body) of a knowledge base file.

    Args:
        path: Repo-relative path as returned by search_kb (e.g.
            "knowledge_base/mixing/compression/sidechain_pumping.md").
    """
    target = (ROOT / path).resolve()
    if ROOT not in target.parents or not target.is_file():
        raise ValueError(f"invalid or out-of-repo path: {path}")
    return target.read_text(encoding="utf-8")


@mcp.tool()
def analyze_mix(file_path: str, genre: str | None = None) -> dict[str, Any]:
    """Analyze a mix or master file and report objective metrics.

    Natively supports WAV/AIFF; MP3/M4A/FLAC/OGG/WMA/AAC are transcoded via
    an ffmpeg subprocess first (requires ffmpeg on PATH — WAV/AIFF work
    without it).

    Computes LUFS integrated loudness, true-peak (dBTP), and crest factor (dB) —
    metrics this knowledge base documents genre-specific numeric targets for.
    Also computes stereo correlation and relative spectral-band energy as
    general audio-engineering diagnostics; the knowledge base has no numeric
    targets for those two, so they are NOT compared against a KB-documented
    value — interpret them using standard audio-engineering knowledge instead.

    Args:
        file_path: Path to a local audio file (WAV/AIFF native; MP3/M4A/FLAC/
            OGG/WMA/AAC via ffmpeg).
        genre: Optional genre name (e.g. "trap", "ambient") — if given, also
            returns relevant_kb_entries pointing at documented LUFS/dynamics
            targets for that genre, for comparison against the measured values.
    """
    from audio_analysis import analyze_audio_file

    result = analyze_audio_file(file_path)

    if genre:
        query = f"LUFS loudness dynamic range true peak target for {genre}"
        result["relevant_kb_entries"] = _cosine_search(query, "mastering", 3)

    return result


@mcp.tool()
def analyze_mix_batch(file_paths: list[str], genre: str | None = None) -> dict[str, Any]:
    """Analyze multiple audio files side by side (e.g. stems, or a mix vs. a
    reference track) and summarize them.

    Args:
        file_paths: Either a list of individual file paths, or a single-item
            list containing one folder path (all supported audio files
            directly inside that folder are analyzed, non-recursive).
        genre: Optional genre name — if given, also returns relevant_kb_entries
            (shared across the whole batch) pointing at documented LUFS/
            dynamics targets for that genre.

    Returns a "files" list (one entry per input, with an "error" field instead
    of metrics for any file that failed to analyze) and a "summary" with
    min/max/range for lufs_integrated, true_peak_dbtp, and crest_factor_db
    across the successfully analyzed files — useful for spotting inconsistent
    gain-staging across stems, or comparing a mix against a reference track.
    """
    from audio_analysis import analyze_multiple

    result = analyze_multiple(file_paths)

    if genre:
        query = f"LUFS loudness dynamic range true peak target for {genre}"
        result["relevant_kb_entries"] = _cosine_search(query, "mastering", 3)

    return result


if __name__ == "__main__":
    mcp.run()
