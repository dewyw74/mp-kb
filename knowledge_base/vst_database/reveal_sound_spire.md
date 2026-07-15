---
plugin_name: "Spire"
developer: "Reveal Sound"
category: "synth"
type: "hybrid wavetable/waveshaping synth"
cpu_usage: "medium"
best_genres:
  - electro_house
  - uplifting_trance
  - trance
  - progressive_trance
  - big_room_house
strengths:
  - "Four 'polymorphic' oscillators, each blending a selected wavetable with adjustable wet-mix waveshaping ('polymorphing') rather than pure wavetable playback alone, giving leads and stabs a denser, more aggressive harmonic character than a clean wavetable readout."
  - "Seven oscillator modes (Classic, Noise, FM, HardFM, SawPWM, AMSync, Vowel) mean a single oscillator can cover subtractive, FM, and formant/vowel territory without reaching for a second synth."
  - "Deep modulation architecture — four envelopes, four LFOs, two step sequencers, and a full routing matrix — supports the same kind of evolving, rhythmically-locked movement trance and electro house leads rely on."
  - "Well established as a supersaw/virtual-analog-style lead and stab tool in the genre corpus, sitting alongside Sylenth1 and Serum as a standard choice for trance and electro house synth work."
weaknesses:
  - "Its factory-preset-driven reputation can encourage relying on stock patches rather than exploring the polymorphing oscillator engine's own sound-design depth, which is deeper than a quick preset-browsing session reveals."
  - "The seven-mode oscillator and full modulation matrix add a real learning curve compared to a simpler virtual-analog synth like Sylenth1, despite a broadly similar target use case."
alternatives:
  - "LennarDigital Sylenth1 (see `lennardigital_sylenth1.md` — simpler, lighter-CPU virtual-analog alternative for the same supersaw/trance lead role)"
  - "Xfer Serum 2 (see `xfer_serum_2.md` — deeper wavetable editing for from-scratch design)"
  - "Arturia Pigments (see `arturia_pigments.md` — broader multi-engine alternative)"
recommended_settings:
  - "Uplifting trance supersaw lead: Classic mode on 2-3 oscillators with wide unison detune and stereo spread, polymorph wet-mix pushed partway in for extra harmonic density, slow filter-cutoff automation across the buildup."
  - "Electro house stab: SawPWM or HardFM oscillator mode, fast attack/short decay amplitude envelope, resonant lowpass filter with envelope modulation for a percussive, aggressive stab character."
common_uses:
  - "Supersaw and virtual-analog-style leads for trance and progressive trance"
  - "Aggressive stabs and plucks for electro house and big room house"
  - "General-purpose wavetable/waveshaping sound design where FM, vowel, and classic oscillator modes need to coexist in one synth"
tags: ["reveal-sound", "spire", "synth", "wavetable", "trance", "electro-house"]
---

# Spire

Spire (Reveal Sound) is a hybrid wavetable and waveshaping synthesizer built around four "polymorphic" oscillators, each combining a chosen wavetable with an adjustable waveshaping stage the developer calls "polymorphing." It was Reveal Sound's first synthesizer and became a genre-standard EDM lead/stab tool, cited alongside Sylenth1 and Serum in the trance and electro house corners of this knowledge base.

## Sound Character and Strengths

Spire's polymorphing oscillators are the key differentiator from a straightforward wavetable synth: rather than just reading a table's waveform, each oscillator wet-mixes the selected wavetable against a waveshaping stage, which is part of why its leads and stabs read as denser and more harmonically saturated than a plain wavetable readout. `knowledge_base/genres/edm/electro_house.md` groups it with Sylenth1 as a virtual-analog/digital-subtractive option for that genre's lead tones, and `knowledge_base/genres/edm/uplifting_trance.md` and `knowledge_base/sound_design/presets/supersaw_lead_design.md` cite it directly as one of the standard supersaw-style software options alongside Serum and Sylenth1 for trance's signature stacked-sawtooth lead. Its seven oscillator modes give it functional overlap with FM and formant/vowel synthesis without needing a separate dedicated synth for those textures.

## Weaknesses

Spire ships with an unusually large factory preset library, and its reputation among many producers is built almost entirely on that library rather than its own sound-design engine — which means its actual synthesis depth (the polymorphing oscillator, the seven-mode oscillator architecture, the dual step sequencers) is easy to underuse. The tradeoff for that depth is a steeper learning curve than a simpler virtual-analog synth aimed at the same supersaw/lead use case.

## Common Mistakes

Treating Spire purely as a preset browser rather than using its oscillator-mode and polymorphing controls to build a patch from scratch — per `knowledge_base/sound_design/presets/supersaw_lead_design.md`'s general guidance on trance lead design, the genre's signature sound comes from deliberate unison/detune and filter-envelope choices, not just loading a factory patch unmodified.

## Cross-References

- `knowledge_base/genres/edm/electro_house.md` — cites Spire alongside Access Virus and Sylenth1 for virtual analog/digital subtractive lead tones
- `knowledge_base/genres/edm/uplifting_trance.md` — cites Spire as a software equivalent for the genre's supersaw lead sound
- `knowledge_base/sound_design/presets/supersaw_lead_design.md` — the supersaw lead design recipe citing Spire alongside Serum and Sylenth1
- `knowledge_base/vst_database/lennardigital_sylenth1.md` — the lighter-weight virtual-analog alternative most commonly compared against Spire
