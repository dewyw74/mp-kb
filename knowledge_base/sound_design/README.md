# sound_design/

Synthesis and sound-shaping reference — `synthesis/` (methods: subtractive, FM, wavetable, granular), `sampling/`, `effects/` (processing techniques, distinct from mixing-stage effects), `presets/` (documented patch recipes).

No dedicated schema yet; use YAML frontmatter until a `sound_design_schema.json` is added in a later phase. Minimum fields by subfolder:

- `synthesis/` and `presets/`: `title`, `synthesis_method`, `tags`
- `effects/`: `title`, `effect_type`, `tags`
- `sampling/`: `title`, `technique`, `tags`

Consumed primarily by `sound_design_agent`.
