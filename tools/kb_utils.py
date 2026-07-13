from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
KB_ROOT = ROOT / "knowledge_base"
SCHEMA_ROOT = ROOT / "schemas"


class FrontmatterError(ValueError):
    pass


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in KB_ROOT.rglob("*.md")
        if path.name.lower() != "readme.md"
    )


def read_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise FrontmatterError("missing opening frontmatter delimiter")

    end = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = index
            break

    if end is None:
        raise FrontmatterError("missing closing frontmatter delimiter")

    return parse_yaml_subset(lines[1:end])


def parse_yaml_subset(lines: list[str]) -> dict[str, Any]:
    root: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(-1, root)]
    last_key_at_indent: dict[int, str] = {}

    for line_index, raw in enumerate(lines):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue

        indent = len(raw) - len(raw.lstrip(" "))
        line = raw.strip()

        while stack and indent <= stack[-1][0]:
            stack.pop()

        parent = stack[-1][1]

        if line.startswith("- "):
            item = parse_scalar(line[2:].strip())
            if not isinstance(parent, list):
                raise FrontmatterError(f"list item without list parent: {raw}")
            parent.append(item)
            continue

        if ":" not in line:
            raise FrontmatterError(f"unsupported frontmatter line: {raw}")

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if not isinstance(parent, dict):
            raise FrontmatterError(f"mapping entry inside non-mapping parent: {raw}")

        if value:
            parent[key] = parse_scalar(value)
            last_key_at_indent[indent] = key
            continue

        next_container = infer_container(lines, line_index)
        parent[key] = next_container
        last_key_at_indent[indent] = key
        stack.append((indent, next_container))

    return root


def infer_container(lines: list[str], current_index: int) -> dict[str, Any] | list[Any]:
    current_raw = lines[current_index]
    current_indent = len(current_raw) - len(current_raw.lstrip(" "))
    for raw in lines[current_index + 1 :]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        if indent <= current_indent:
            return {}
        return [] if raw.strip().startswith("- ") else {}
    return {}


def parse_scalar(value: str) -> Any:
    if value in {"true", "True"}:
        return True
    if value in {"false", "False"}:
        return False
    if value in {"null", "Null", "~"}:
        return None
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(part.strip()) for part in inner.split(",")]
    return value


def schema_for_path(path: Path) -> Path | None:
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith("knowledge_base/genres/"):
        return SCHEMA_ROOT / "genre_schema.json"
    if rel.startswith("knowledge_base/vst_database/"):
        return SCHEMA_ROOT / "plugin_schema.json"
    if rel.startswith("knowledge_base/mixing/") or rel.startswith(
        "knowledge_base/mastering/"
    ):
        return SCHEMA_ROOT / "mixing_schema.json"
    if rel.startswith("knowledge_base/daw/") or rel.startswith(
        "knowledge_base/production/workflow/"
    ):
        return SCHEMA_ROOT / "workflow_schema.json"
    return None


def lightweight_required_fields(path: Path) -> list[str]:
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith("knowledge_base/sound_design/synthesis/") or rel.startswith(
        "knowledge_base/sound_design/presets/"
    ):
        return ["title", "synthesis_method", "tags"]
    if rel.startswith("knowledge_base/sound_design/effects/"):
        return ["title", "effect_type", "tags"]
    if rel.startswith("knowledge_base/sound_design/sampling/"):
        return ["title", "technique", "tags"]
    if rel.startswith("knowledge_base/music_theory/"):
        return ["title", "tags"]
    if rel.startswith("knowledge_base/midi/"):
        return ["title", "tags"]
    if rel.startswith("knowledge_base/production/"):
        return ["title", "tags"]
    return []


def load_schema(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_against_schema(data: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in schema.get("required", []):
        if field not in data:
            errors.append(f"missing required field: {field}")

    properties = schema.get("properties", {})
    for field, value in data.items():
        field_schema = properties.get(field)
        if not field_schema:
            continue
        errors.extend(validate_value(field, value, field_schema))
    return errors


def validate_value(name: str, value: Any, schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    expected = schema.get("type")
    if expected and not type_matches(value, expected):
        errors.append(f"{name}: expected {expected}, got {type(value).__name__}")
        return errors

    if "enum" in schema and value not in schema["enum"]:
        choices = ", ".join(str(choice) for choice in schema["enum"])
        errors.append(f"{name}: expected one of [{choices}], got {value!r}")

    if expected == "object" and isinstance(value, dict):
        child_properties = schema.get("properties", {})
        for child_name, child_value in value.items():
            child_schema = child_properties.get(child_name)
            if child_schema:
                errors.extend(
                    validate_value(f"{name}.{child_name}", child_value, child_schema)
                )

    if expected == "array" and isinstance(value, list):
        item_schema = schema.get("items", {})
        for index, item in enumerate(value):
            errors.extend(validate_value(f"{name}[{index}]", item, item_schema))

    return errors


def type_matches(value: Any, expected: str) -> bool:
    if expected == "string":
        return isinstance(value, str)
    if expected == "array":
        return isinstance(value, list)
    if expected == "object":
        return isinstance(value, dict)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return True


def title_from_frontmatter(data: dict[str, Any]) -> str:
    return (
        data.get("genre_name")
        or data.get("workflow_name")
        or data.get("technique_name")
        or data.get("plugin_name")
        or data.get("title")
        or "Untitled"
    )


def slug_from_path(path: Path) -> str:
    return re.sub(r"[^a-z0-9_]+", "_", path.stem.lower()).strip("_")
