---
plugin_name: "Serum 1 (Classic)"
developer: "Xfer Records"
category: "synth"
type: "wavetable synth"
cpu_usage: "medium"
best_genres:
  - dubstep
  - brostep
  - future_bass
  - trance
  - uplifting_trance
  - hardstyle
  - bass_house
  - psytrance
  - riddim
strengths:
  - "Deep, visual wavetable editor with built-in wavetable drawing, warping, and importing tools, making custom wavetable design fast and intuitive."
  - "Extremely flexible modulation matrix with generous modulation slots and real-time visual feedback on every parameter."
  - "Strong built-in effects chain (distortion, flanger, phaser, compressor, EQ, delay, reverb, hyper/unison) that covers most bass and lead sound-design needs without leaving the plugin."
  - "Huge third-party preset and wavetable ecosystem, making it a fast starting point even without deep sound-design knowledge."
weaknesses:
  - "CPU load climbs quickly with high unison counts, multiple oscillators, and the built-in effects chain fully engaged — large multi-instance sessions need freezing or bouncing."
  - "The wavetable editor's power can become a time sink; a simpler subtractive synth is often faster for straightforward pad or lead sounds."
alternatives:
  - "Vital"
  - "Massive"
  - "Serum 2 (successor, see `xfer_serum_2.md`)"
recommended_settings:
  - "Modern EDM bass: 2 oscillators with unison 4-8 voices, heavy wavetable position modulation via an envelope for movement, distortion pre-filter for grit, and the built-in compressor on the master chain for glue."
  - "Supersaw-style leads: single sawtooth wavetable, unison voices 8-16, wide unison detune, and a slow filter envelope for evolving brightness."
common_uses:
  - "808/bass sound design via wavetable position modulation and FM"
  - "Supersaw and unison leads for trance and hardstyle"
  - "Dubstep/riddim growl and wobble bass via LFO-modulated wavetable scanning"
  - "General-purpose EDM pad and pluck design"
tags: ["serum", "xfer", "wavetable-synth", "edm", "bass-design", "lead-design"]
---

# Serum 1 (Classic)

This entry covers the original Serum (referred to here as "Serum 1" to distinguish it from its 2024 successor Serum 2, documented separately in `knowledge_base/vst_database/xfer_serum_2.md`). Xfer continues to sell and support Serum 1 alongside Serum 2 as of this writing, and its smaller CPU footprint and simpler, well-understood interface still make it the right choice for many producers and sessions — it has not been discontinued or made obsolete by the newer version.

Serum is a wavetable synthesizer built around a visual, hands-on approach to wavetable editing — its waveform display doubles as an editing surface, letting a producer draw, warp, and import wavetables directly rather than relying only on preset table selection. This directness is why it became the default modern-EDM sound-design tool across a wide swath of the genres documented in this knowledge base: dubstep and riddim growls, future bass leads, trance supersaws, and hardstyle screeches are all built on the same core workflow of modulating wavetable position and filter cutoff against a strong envelope or LFO.

## Sound Character and Strengths

Serum's two-oscillator architecture, each with independent wavetable selection, unison, and warp modes, makes layered, wide, evolving sounds fast to build. The modulation matrix is unusually deep for a synth this approachable — most parameters accept multiple modulation sources with visual feedback showing exactly how each source is affecting the destination in real time, which shortens the sound-design feedback loop considerably. The built-in effects rack (filter, distortion, flanger/phaser, EQ, compressor, delay, reverb) is strong enough that many patches never need an external effects chain at all.

## Weaknesses

Serum's flexibility comes with a CPU cost — high unison counts across two oscillators plus the internal effects chain add up fast, and large trance or hardstyle projects with a dozen Serum instances often need judicious freezing (see `knowledge_base/daw/ableton/routing_resampling_and_freezing.md` and `knowledge_base/daw/fl_studio/mixer_routing_resampling_and_freezing.md`). Its wavetable-editing depth is also a double-edged sword for speed: a producer who just needs a simple pluck or pad is sometimes faster off in a more constrained subtractive synth.

## Common Mistakes

Leaving unison voice count and warp settings at preset defaults instead of adjusting them to the target genre's character — a trance supersaw and a dubstep growl both start from the same oscillator engine but need very different unison width, warp mode, and modulation depth to read as genre-appropriate.

## Third-Party Wavetable and Preset Ecosystem

Serum's decade-plus market presence has produced one of the largest third-party content ecosystems of any synth documented in this knowledge base. Sample/preset marketplaces (Splice, ADSR Sounds, and Cymatics among the widely-used general platforms) host large numbers of Serum-format preset banks and custom wavetable packs spanning most EDM subgenres, and it's common practice for sound-design-focused producers and labels to sell genre-specific Serum patch banks (bass, lead, pluck collections aimed at a specific subgenre's character) as standalone products. This entry deliberately doesn't name or evaluate specific commercial packs, since pack quality and relevance change quickly and any specific recommendation would date fast — the practical takeaway is that a producer working in a well-established EDM subgenre (dubstep, trance, hardstyle, future bass) can very often find a purpose-built third-party wavetable or preset pack for that exact subgenre's character, rather than needing to build every patch from scratch using the from-scratch techniques in `knowledge_base/sound_design/synthesis/serum_wavetable_editor_workflow.md`.

## Cross-References

- `knowledge_base/sound_design/synthesis/wavetable_synthesis.md` — general wavetable synthesis technique, of which Serum is the primary example instrument
- `knowledge_base/sound_design/synthesis/serum_wavetable_editor_workflow.md` — the specific drawing/warping/importing UI workflow this entry's editor description summarizes
- `knowledge_base/sound_design/presets/supersaw_lead_design.md`, `knowledge_base/sound_design/presets/edm_bass_design.md`, `knowledge_base/sound_design/presets/pad_design_archetypes_and_patch_recipes.md` — genre-specific patch recipes built on Serum
- `knowledge_base/genres/edm/dubstep.md`, `knowledge_base/genres/edm/trance.md`, `knowledge_base/genres/edm/hardstyle.md` — genre files citing Serum as a primary sound-design tool
- `knowledge_base/vst_database/xfer_serum_2.md` — the newer, actively-developed successor; see that entry for what's changed and when to prefer it over Serum 1
