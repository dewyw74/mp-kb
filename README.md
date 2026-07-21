# AI Music Producer Encyclopedia

A modular expert knowledge system that turns Claude Code into an expert music producer, composer, sound designer, MIDI programmer, mixing engineer, mastering engineer, and DAW specialist — covering composition, theory, genre analysis, arrangement, sound design, MIDI programming, recording, mixing, mastering, Ableton Live and FL Studio workflows, VST/plugin selection, and production automation.

The long-term goal is a private AI music producer operating system: a knowledge base Claude Code can search and reason over, paired with specialized subagents for each production discipline.

## Architecture

```
knowledge_base/
  genres/{electronic,rock,metal,hiphop,pop,jazz,classical,edm,cinematic,world_music}/
  music_theory/{scales,chords,harmony,melody,rhythm}/
  production/{arrangement,songwriting,workflow,templates}/
  sound_design/{synthesis,sampling,effects,presets}/
  mixing/{eq,compression,reverb,delay,stereo}/
  mastering/{loudness,dynamics,streaming}/
  midi/{patterns,controllers,programming}/
  daw/{ableton,fl_studio,logic_pro,pro_tools,cubase,studio_one,reaper,workflow}/
  vst_database/
  reference/           # external resource pointers (not deep technique docs, no schema)
schemas/            # JSON Schema contracts for each entry type's frontmatter
mcp_server/          # local MCP server: semantic KB search + WAV/AIFF mix/master analysis (Phase 6)
automation/          # future prompts/, workflows/, pipelines/
.claude/agents/       # Claude Code specialist subagents
.codex/agents/        # Codex specialist subagents
tools/                # validation, index-generation, embeddings-build, and mix-analysis CLI utilities
```

Each `knowledge_base/` category has its own `README.md` explaining what belongs there and which schema its entries conform to.

## How content is structured

Every knowledge base entry is a Markdown file with YAML frontmatter:

- **Frontmatter** holds structured, machine-parseable metadata (BPM, key, tags, category-specific fields) and must conform to the relevant file in `schemas/`.
- **Body** holds the prose — history, technique explanations, professional tips — organized under the section headings implied by the schema.

This keeps entries human-readable and hand-editable while still being searchable/parseable by tooling in later phases.

Four schemas currently defined:
| Schema | Covers |
|---|---|
| `schemas/genre_schema.json` | `knowledge_base/genres/**` |
| `schemas/plugin_schema.json` | `knowledge_base/vst_database/` |
| `schemas/mixing_schema.json` | `knowledge_base/mixing/**`, `knowledge_base/mastering/**` |
| `schemas/workflow_schema.json` | `knowledge_base/daw/**`, `knowledge_base/production/workflow/` |

Categories without a dedicated schema yet (`music_theory/`, `sound_design/`, `midi/`, `production/{arrangement,songwriting,templates}/`) use plain frontmatter (`title`, `tags` minimum) until a schema is added in a later phase — see each category's own README.

`reference/` is a special case: plain frontmatter (`title`, `tags`, `source_url`), but deliberately outside the citation-grounding rule the rest of the knowledge base follows, since its entries point to external resources rather than documenting this project's own researched or genre-grounded technique — see `knowledge_base/reference/README.md`.

## Tooling

Run these from the project root:

```powershell
python tools\validate_kb.py
python tools\generate_index.py
```

`validate_kb.py` checks Markdown frontmatter against the appropriate schema where one exists, and applies lightweight required-field checks for categories without dedicated schemas yet.

`generate_index.py` writes `knowledge_base/index.json`, a machine-readable catalog of the knowledge base for search, RAG, and future automation.

```powershell
$env:GROQ_API_KEY = "..."
python tools\draft_genre_with_groq.py "Genre Name" --parent-genre Rock
```

`draft_genre_with_groq.py` uses a Groq API key (free tier; set `GROQ_API_KEY` in the environment, never commit it) to generate a first-pass genre entry matching `schemas/genre_schema.json` and an existing entry's structure/depth. Output lands in `drafts/genres/` (gitignored), marked unreviewed — fact-check and edit it, then manually move it into `knowledge_base/genres/<family>/` and run `validate_kb.py` before it counts as real KB content.

## MCP Server

`mcp_server/server.py` is a local MCP server exposing semantic search over the knowledge base, registered project-wide via `.mcp.json`. Install dependencies with `pip install -r requirements.txt` (pulls in `mcp[cli]` and `sentence-transformers`; the embedding model is fully local/offline — no API key, no per-query cost).

```powershell
pip install -r requirements.txt
python tools\build_embeddings_index.py
```

`build_embeddings_index.py` embeds every KB entry's title + body with a local `sentence-transformers` model (`all-MiniLM-L6-v2`) and writes `knowledge_base/embeddings.json`. Re-run it whenever KB content changes — it's committed to git and regenerated the same way as `index.json`.

The server exposes five tools: `search_kb(query, category?, limit?)` for cosine-similarity semantic search (ranked results with a snippet), `get_kb_entry(path)` to fetch a full file's content, `analyze_mix(file_path, genre?)` for objective analysis of a single mix/master file, `analyze_mix_batch(file_paths, genre?)` to compare multiple files side by side (e.g. all stems in a folder, or a mix vs. a reference track — pass a single folder path to auto-expand it), and `separate_stems(file_path, output_dir?, model?)` to split a full mix into stems (vocals/drums/bass/other, via a local Demucs model) — the only tool that writes new audio files rather than just reporting metrics. All three audio tools support WAV/AIFF natively; MP3/M4A/FLAC/OGG/WMA/AAC are transcoded via an `ffmpeg` subprocess first (`ffmpeg` must be on `PATH` — WAV/AIFF work without it). LUFS integrated, true-peak (dBTP), and crest factor are compared against this KB's documented genre targets (`knowledge_base/mastering/loudness/`, `mastering/dynamics/`); stereo correlation and spectral-band energy are reported too, but as general audio-engineering diagnostics only, since the KB has no numeric target for either. `analyze_mix`/`analyze_mix_batch` are also available via a standalone CLI: `python tools\analyze_mix.py path\to\mix.wav` (single file) or `python tools\analyze_mix.py path\to\stems\` (folder, prints a comparison table). `separate_stems` has its own CLI: `python tools\separate_stems.py path\to\mix.wav` — writes stems to a `<mix>_stems\` folder by default, requires `torch`/`torchaudio`/`demucs` (a much larger install than this project's other dependencies; the first call for a given model also needs internet once, to download its weights, then runs fully offline). All 7 specialist subagents are wired to prefer `search_kb` over Grep/Glob when the MCP tool is available (falling back to Grep/Glob otherwise); `mastering_agent` and `mixing_agent` also have `analyze_mix`.

## Specialist subagents

Seven subagents live in `.claude/agents/` for Claude Code and `.codex/agents/` for Codex. Each searches its corresponding `knowledge_base/` subfolder before answering:

| Agent | Domain | Reads |
|---|---|---|
| `producer_agent` | Full-song planning: genre direction, arrangement, instrumentation, workflow | `genres/`, `production/` |
| `composer_agent` | Melody, chords, scales, harmony | `music_theory/` |
| `sound_design_agent` | Synth patches, synthesis method choice, effects chains | `sound_design/` |
| `mixing_agent` | Frequency/dynamics/stereo diagnosis, EQ/compression settings | `mixing/` |
| `mastering_agent` | Loudness, dynamics, tonal balance, streaming targets | `mastering/` |
| `midi_agent` | Piano roll programming, controller mapping, groove/velocity | `midi/` |
| `daw_agent` | Ableton Live (primary) and FL Studio (secondary), plus Logic Pro, Pro Tools, Cubase, Studio One, Reaper (alternative DAWs) | `daw/` |

`CLAUDE.md` defines the behavior rules Claude Code follows for any music production question asked directly (without going through a subagent).

## Roadmap

- [x] **Phase 1** — Folder structure, schemas, root docs, and the 7 specialist subagents.
- [x] **Phase 2** — Build 500 core genre profiles. Complete: 500/500 WebSearch-verified entries across all families — the essential genre baseline.
- [x] **Phase 2 tooling baseline** — Add frontmatter validation and generated knowledge-base index.
- [x] **Phase 3** — Add production techniques (mixing/mastering/sound-design entries at scale). Substantially complete: 196 entries across mixing (70), mastering (40), and sound_design (86).
- [x] **Phase 4** — Add the VST/plugin database. Complete: 64 entries (up from 29), covering synths/samplers, EQ/compression/dynamics, reverb/delay/saturation, vocal/pitch/mastering-limiters, multiband compression, metering/analysis, and drum romplers.
- [x] **Phase 5** — Add Ableton and FL Studio workflow entries at scale. Complete: 101 entries (up from 14) — 44 Ableton, 40 FL Studio, and a cross-DAW `daw/workflow/` folder (17 entries) covering session/live-performance, live looping, automation/modulation, templates, recording/comping, mixing, mastering, sampling, mix troubleshooting, vocal chain (tuning through full signal chain), drum-bus compression, orchestral MIDI programming, keyboard/pad performance setup, sound-design automation, granular/resampling, sidechain routing, stem-export/collaboration handoff, DI/reamping, MIDI chord/arpeggiator tools, vinyl mastering export prep, and genre-specific arrangement (EDM/trap/house-techno/dubstep/lofi/DnB/trance/ambient) workflows.
- [x] **Phase 6** — MCP server integration, vector DB / RAG retrieval, automated stem/mix analysis. Complete: MCP server (`mcp_server/server.py`) with local-embedding semantic search (`sentence-transformers`, no API key/cost) shipped and wired into all 7 subagents. Mix/master analysis shipped: `analyze_mix` computes LUFS/true-peak/crest-factor (compared against this KB's documented genre targets) plus stereo-correlation and spectral-band diagnostics (general audio-engineering readings, no KB-documented target exists for either); `analyze_mix_batch` compares multiple files side by side (stems, or a mix vs. a reference track). Both support WAV/AIFF natively and MP3/M4A/FLAC/OGG/WMA/AAC via ffmpeg. Wired into `mastering_agent`/`mixing_agent` and available as a standalone CLI (`tools/analyze_mix.py`). Still deferred as a future extension: analyzing individual tracks *within* a multitrack session file rather than pre-bounced stems.
- [x] **Stem separation** — `separate_stems` (MCP tool + `tools/separate_stems.py` CLI) splits a full mix into stems (vocals/drums/bass/other, or 6-stem with guitar/piano via `model="htdemucs_6s"`) using a local Demucs model (`mcp_server/stem_separation.py`), reusing `analyze_mix`'s WAV/AIFF-native + ffmpeg-transcoded format support. The first tool in this project that writes new audio files rather than only reporting metrics; adds `torch`/`torchaudio`/`demucs` as new dependencies (a much larger install than the rest of this project's stack).
- [ ] **Optional** — Expand genre coverage from the 500-genre essential baseline toward 6,000+ genres/subgenres (long-tail micro-genres, regional scenes, fusion styles). A stretch goal, not a blocker for Phases 5-6.
- [~] **Optional** — Extend DAW coverage beyond Ableton (primary) and FL Studio (secondary) to alternative DAWs: Logic Pro, Pro Tools, Cubase, Studio One, Reaper (picked per 2026 usage-survey data — Pro Tools leads professional studios, Logic/Studio One/Reaper/Cubase form the next tier). In progress: schema (`workflow_schema.json`'s `daw` enum extended to 8 values) and `knowledge_base/daw/{logic_pro,pro_tools,cubase,studio_one,reaper}/` folders built; `daw_agent` (Claude Code and Codex) updated to cover all five with Ableton/FL Studio still primary/secondary. First content round complete: 20 entries (4 per DAW) covering project setup/routing, each DAW's signature differentiator feature (Logic's Smart Controls/Drummer and Flex Time/Pitch, Pro Tools' Playlist comping and clip gain/Elastic Audio, Cubase's VST Expression/Expression Maps and Chord Track, Studio One's ARA/Melodyne integration and Scratch Pads, Reaper's flexible routing and ReaScript), and mixing/automation basics. Second content round complete: 20 more entries (4 per DAW, 40 total per DAW folder set) covering sidechain/ducking routing, vocal chain and tuning pipelines (Logic's Pitch Correction plugin, Pro Tools' Melodyne/ARA2, Cubase's VariAudio, Studio One's chain-order philosophy), stem export/session interchange (Pro Tools' AAF/OMF, Logic's Bounce in Place, Reaper's Region Render Matrix), and each DAW's remaining differentiators (Logic's groove templates, Pro Tools' HEAT saturation, Cubase's MIDI Remote and Control Room, Studio One's Project Page mastering and Impact XT, Reaper's JSFX scripting and sample-to-ReaSamplomatic workflow) — core-to-intermediate coverage, still short of Ableton/FL Studio depth (~40-44 entries each vs. 8 per alternative DAW).
