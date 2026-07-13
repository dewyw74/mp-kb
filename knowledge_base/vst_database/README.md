# vst_database/

One markdown file per plugin, frontmatter conforming to `schemas/plugin_schema.json`. Flat directory (no subfolders) — filter by `category`/`tags` in frontmatter rather than folder structure, since plugins often serve multiple categories.

Consumed by `sound_design_agent` (instruments/synths) and `mixing_agent`/`mastering_agent` (processors).

Filename convention: `developer_plugin_name.md` (e.g. `xfer_serum.md`, `fabfilter_pro_q3.md`).
