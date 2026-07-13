from __future__ import annotations

import sys
from pathlib import Path

sys.dont_write_bytecode = True

from kb_utils import (
    ROOT,
    FrontmatterError,
    lightweight_required_fields,
    load_schema,
    markdown_files,
    read_frontmatter,
    schema_for_path,
    validate_against_schema,
)


def main() -> int:
    failures: list[tuple[Path, list[str]]] = []

    for path in markdown_files():
        errors: list[str] = []
        try:
            data = read_frontmatter(path)
        except FrontmatterError as exc:
            failures.append((path, [str(exc)]))
            continue

        schema_path = schema_for_path(path)
        if schema_path:
            errors.extend(validate_against_schema(data, load_schema(schema_path)))
        else:
            for field in lightweight_required_fields(path):
                if field not in data:
                    errors.append(f"missing required field: {field}")

        if errors:
            failures.append((path, errors))

    if failures:
        print(f"Knowledge-base validation failed: {len(failures)} file(s)")
        for path, errors in failures:
            rel = path.relative_to(ROOT)
            print(f"\n{rel}")
            for error in errors:
                print(f"  - {error}")
        return 1

    print(f"Knowledge-base validation passed: {len(markdown_files())} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
