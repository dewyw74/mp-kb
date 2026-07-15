from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

from kb_utils import KB_ROOT, ROOT, markdown_files, read_frontmatter, title_from_frontmatter


EMBEDDINGS_PATH = KB_ROOT / "embeddings.json"
MODEL_NAME = "all-MiniLM-L6-v2"


def body_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return text
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "\n".join(lines[index + 1 :]).strip()
    return text


def main() -> int:
    from sentence_transformers import SentenceTransformer

    files = markdown_files()
    docs: list[dict[str, Any]] = []
    texts: list[str] = []

    for path in files:
        data = read_frontmatter(path)
        rel = path.relative_to(ROOT).as_posix()
        kb_rel = path.relative_to(KB_ROOT)
        category = kb_rel.parts[0] if kb_rel.parts else ""
        title = title_from_frontmatter(data)

        text = f"{title}\n\n{body_text(path)}"
        texts.append(text)
        docs.append({"path": rel, "title": title, "category": category})

    print(f"Loading embedding model {MODEL_NAME}...")
    model = SentenceTransformer(MODEL_NAME)

    print(f"Embedding {len(texts)} documents...")
    vectors = model.encode(texts, show_progress_bar=True, normalize_embeddings=True)

    for doc, vector in zip(docs, vectors):
        doc["embedding"] = [round(float(x), 6) for x in vector]

    payload = {
        "generated_by": "tools/build_embeddings_index.py",
        "model": MODEL_NAME,
        "entry_count": len(docs),
        "entries": docs,
    }

    EMBEDDINGS_PATH.write_text(
        json.dumps(payload, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Wrote {EMBEDDINGS_PATH.relative_to(ROOT)} with {len(docs)} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
