from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

from kb_utils import KB_ROOT, ROOT, markdown_files, read_frontmatter, slug_from_path, title_from_frontmatter


INDEX_PATH = KB_ROOT / "index.json"


def main() -> int:
    entries: list[dict[str, Any]] = []

    for path in markdown_files():
        data = read_frontmatter(path)
        rel = path.relative_to(ROOT).as_posix()
        kb_rel = path.relative_to(KB_ROOT)
        category = kb_rel.parts[0] if kb_rel.parts else ""
        subcategory = kb_rel.parts[1] if len(kb_rel.parts) > 2 else None

        entry = {
            "id": slug_from_path(path),
            "title": title_from_frontmatter(data),
            "path": rel,
            "category": category,
            "subcategory": subcategory,
            "tags": data.get("tags", []),
            "schema_type": infer_schema_type(category, rel),
        }

        for key in [
            "genre_name",
            "parent_genre",
            "subgenre_of",
            "tempo_range",
            "common_keys",
            "related_genres",
            "synthesis_method",
            "workflow_name",
            "daw",
            "technique_name",
            "plugin_name",
            "developer",
        ]:
            if key in data:
                entry[key] = data[key]

        entries.append(entry)

    payload = {
        "generated_by": "tools/generate_index.py",
        "entry_count": len(entries),
        "entries": entries,
    }

    INDEX_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {INDEX_PATH.relative_to(ROOT)} with {len(entries)} entries")
    return 0


def infer_schema_type(category: str, rel: str) -> str:
    if category == "genres":
        return "genre"
    if category == "vst_database":
        return "plugin"
    if category in {"mixing", "mastering"}:
        return "mixing"
    if category == "daw" or rel.startswith("knowledge_base/production/workflow/"):
        return "workflow"
    return "plain_frontmatter"


if __name__ == "__main__":
    raise SystemExit(main())
