# genres/

One markdown file per genre or subgenre, filed under its parent-genre subfolder (`electronic/`, `rock/`, `metal/`, `hiphop/`, `pop/`, `jazz/`, `classical/`, `edm/`, `cinematic/`, `world_music/`). A genre that spans categories (e.g. a hip-hop/electronic hybrid) lives under its dominant parent and cross-links via `related_genres` in frontmatter.

Each file's frontmatter must conform to `schemas/genre_schema.json`. The markdown body follows the section order: History → Music Theory → Arrangement → Instruments → Sound Design → MIDI Programming → Mixing → Mastering → Reference Artists → Production Notes.

Consumed primarily by `producer_agent` and, for theory-specific questions, `composer_agent`.

Filename convention: `snake_case_genre_name.md` (e.g. `synthwave.md`, `progressive_house.md`).
