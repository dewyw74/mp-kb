---
plugin_name: "Battery 4"
developer: "Native Instruments"
category: "sampler"
type: "cell-based drum sampler/rompler"
cpu_usage: "medium"
best_genres:
  - boom_bap
  - trap
  - hip_hop
  - metal
  - drum_and_bass
strengths:
  - "Cell-based, drag-and-drop architecture where each individual drum hit lives in its own cell with a dedicated envelope, filter, and compressor — the direct software equivalent of the MPC/SP-1200-style hit-per-pad kit-building workflow this knowledge base documents as foundational to hip-hop drum programming."
  - "Seven sample-playback modes (including classic sampler and groove-box emulation modes) plus Time Machine Pro time-stretching give each cell more flexibility than a simple one-shot trigger, without requiring a full multisampling workflow."
  - "Built-in per-cell and per-group effects (SOLID EQ, SOLID BUS COMP, Transient Master, tape saturation, lo-fi, convolution reverb) mean a full drum-kit processing chain can be built inside the sampler rather than requiring a separate effects rack on every pad."
  - "Color-coded cells and instant cell rendering make assembling a kit from disparate sources — the exact 'pull a kick from one break, a snare from another' workflow documented for boom bap and east coast hip-hop — fast to execute and visually easy to track."
weaknesses:
  - "As a dedicated drum sampler, Battery doesn't cover melodic/pitched sampling or the deep scripting depth of a general-purpose sampler like Kontakt — it's purpose-built for one-shot and short-loop drum/percussion material, not orchestral or pitched-instrument libraries."
  - "Running many cells each with their own filter, compressor, and effects chain active simultaneously carries a real CPU cost in a large kit, more than a lighter native DAW sampler handling the same number of simple one-shots."
alternatives:
  - "Ableton Simpler and Sampler (see `ableton_simpler_and_sampler.md` — lighter-weight, natively integrated option for simpler one-shot kits)"
  - "Native Instruments Kontakt (see `native_instruments_kontakt.md` — for melodic/pitched sampling and deep scripting beyond drum-focused work)"
recommended_settings:
  - "Boom bap/east coast kit assembly: source individual kick, snare, and hat hits from separate chopped breaks, map each to its own cell, apply a shared processing chain (bit-reduction, filtering, tape saturation) across all cells for cohesion per the documented 'dusty' kit-unification technique."
  - "Trap/hip-hop 808 and percussion layering: dedicated cells for layered clap/snare stacks and hi-hat rolls, per-cell compression for consistent transient punch, Time Machine Pro for pitch-independent length adjustment on looped percussion elements."
common_uses:
  - "Building cohesive playable drum kits from chopped breaks and one-shots for boom bap and east coast hip-hop production"
  - "Layered, per-cell-processed drum programming for trap and modern hip-hop"
  - "Fast-tempo, mechanically precise programmed drum kits for metal and drum and bass where live-drummer limitations aren't a factor"
tags: ["native-instruments", "battery", "sampler", "drum-sampler", "rompler", "hip-hop"]
---

# Battery 4

Battery 4 (Native Instruments) is a cell-based drum sampler where each individual sound — kick, snare, hat, percussion hit, or short loop — lives in its own cell with a dedicated envelope, filter, compressor, and up to eight modulation paths, all navigated through a color-coded, drag-and-drop grid. It's the modern software realization of the pad-per-sound drum-machine/sampler workflow that hardware samplers like the Akai MPC series and SP-1200 established, and it fills a genuine gap in this knowledge base's vst_database: a dedicated drum sampler/rompler sitting alongside the general-purpose Kontakt and the native Ableton Simpler/Sampler.

## Sound Character and Strengths

`knowledge_base/sound_design/sampling/sample_based_drum_kit_construction.md` documents the MPC-style workflow this knowledge base treats as foundational to hip-hop drum programming — isolating individual hits from one or more source breaks and mapping each to its own trigger, "turning several source recordings into one unified, playable kit rather than leaving each break as an unsliced loop." Battery's cell architecture is the direct software continuation of that exact workflow: each cell functions as a pad, each with its own processing, and the color-coded grid makes tracking which cell holds which source hit straightforward even in a kit assembled from several unrelated break sources. Its per-cell effects (EQ, bus compression, transient shaping, tape saturation, lo-fi degradation, convolution reverb) also directly support the "shared processing chain to unify hits from disparate sources" technique that same file documents as essential to a cohesive-sounding finished kit.

## Weaknesses

Battery is a drum-focused sampler, not a general-purpose one — it doesn't offer Kontakt's scripting depth or its strength with melodic/pitched sample libraries (orchestral, acoustic instrument content), so a producer needing both drum programming and deep pitched-instrument sampling in one session will likely still need Kontakt or a similar tool alongside it. A large kit with many cells each running their own filter, compressor, and effects simultaneously also adds up in CPU cost faster than an equivalent set of simple one-shot triggers in a lighter native sampler.

## Common Mistakes

Loading a full kit's worth of cells with heavy per-cell processing (compression, saturation, convolution reverb) active on every single cell simultaneously, rather than applying shared processing at the group or master-bus level where the goal is kit-wide cohesion — per `sample_based_drum_kit_construction.md`'s documented approach, a *shared* processing chain across hits from different sources is what makes a kit read as one instrument, and duplicating that chain per-cell instead of at the group level wastes CPU without improving cohesion.

## Cross-References

- `knowledge_base/sound_design/sampling/sample_based_drum_kit_construction.md` — documents the MPC-style hit-per-pad kit-building workflow Battery's cell architecture directly implements in software
- `knowledge_base/sound_design/sampling/circuit_bent_and_hardware_sampler_texture.md` — the shared processing-chain technique for unifying hits drawn from disparate sources into one cohesive kit
- `knowledge_base/vst_database/native_instruments_kontakt.md` — the general-purpose, melodic/pitched-sampling counterpart for tasks outside Battery's drum-focused scope
- `knowledge_base/vst_database/ableton_simpler_and_sampler.md` — the lighter-weight, natively integrated alternative for simpler one-shot drum kits
