---
plugin_name: "Diva"
developer: "u-he"
category: "synth"
type: "analog-modeled subtractive synth"
cpu_usage: "high"
best_genres:
  - trance
  - progressive_trance
  - techno
  - melodic_house
  - hard_trance
  - tech_trance
  - hardstyle
  - synthwave
  - outrun
strengths:
  - "Component-modeled analog circuit emulation (multiple selectable oscillator, filter, and envelope models drawn from classic synths like the Minimoog, Jupiter-8, and CS-80) gives it an unusually authentic analog character."
  - "Filter models in particular are widely regarded as some of the best analog emulations available, with real self-oscillation and drive behavior."
  - "Per-component model switching means a single instance can target the character of several different vintage synths without leaving the plugin."
weaknesses:
  - "CPU usage is high relative to most modern synths because of its component-level circuit modeling — large projects with many Diva instances need freezing or careful voice-count management."
  - "Its interface and workflow are less visually modern than wavetable synths like Serum/Vital, favoring knob-per-function analog-style layout over visual modulation routing."
alternatives:
  - "u-he Repro"
  - "Arturia analog synth emulations"
  - "Native Instruments Monark"
recommended_settings:
  - "Trance pluck/lead: Jupiter-8-style filter model, moderate resonance, fast envelope on filter cutoff, and light chorus for width without losing mono-compatible low end."
  - "Synthwave/outrun lead: CS-80-style oscillator model paired with a slow filter envelope and portamento for glide between notes."
common_uses:
  - "Warm analog-style leads and plucks for trance and progressive house"
  - "Synthwave and outrun lead and pad sounds"
  - "Techno and hard trance stabs using its self-oscillating filter models"
tags: ["diva", "u-he", "analog-modeled", "subtractive-synth", "trance", "synthwave"]
---

# Diva

Diva (u-he) is a subtractive synthesizer built around component-level modeling of specific classic analog synth circuits, letting each oscillator, filter, and envelope module be independently set to emulate a particular vintage instrument's behavior rather than offering one generic "analog-style" algorithm. This is why Diva shows up across this knowledge base wherever a genre wants a specifically vintage-analog character rather than the modern, digitally-precise tone associated with wavetable synths like Serum.

## Sound Character and Strengths

Diva's filter models are its most celebrated feature — several are modeled closely enough on specific classic synth filters (Minimoog-style ladder, Jupiter-8-style, CS-80-style) that they reproduce real self-oscillation and saturation behavior under drive, giving leads and basses a texture that's difficult to achieve with purely digital filter algorithms. Because oscillator, filter, and envelope models are independently selectable, a single Diva patch can mix and match circuit character in ways no single real vintage synth could.

## Weaknesses

That circuit-level modeling is computationally expensive — Diva is one of the heavier synths in common use, and CPU load becomes a real constraint in dense arrangements with several simultaneous instances. Its interface also assumes some familiarity with analog synth architecture (oscillator/filter/envelope-per-knob layout); it doesn't offer the visual modulation-routing convenience that Serum or Vital provide.

## Common Mistakes

Running many simultaneous Diva instances without freezing or bouncing, then encountering CPU dropouts partway through a mix session — apply the freezing workflow from `knowledge_base/daw/ableton/routing_resampling_and_freezing.md` or `knowledge_base/daw/fl_studio/mixer_routing_resampling_and_freezing.md` proactively on Diva-heavy projects rather than reactively.

## Cross-References

- `knowledge_base/sound_design/synthesis/subtractive_synthesis.md` — general subtractive synthesis technique, of which Diva is a primary example instrument
- `knowledge_base/genres/edm/trance.md`, `knowledge_base/genres/edm/hard_trance.md`, `knowledge_base/genres/electronic/synthwave.md`, `knowledge_base/genres/electronic/outrun.md` — genre files citing Diva as a primary lead/pluck sound-design tool
- `knowledge_base/vst_database/xfer_serum.md` — a useful contrast case: digital wavetable precision vs. Diva's modeled analog character
