---
plugin_name: "LFO Tool"
developer: "Xfer Records"
category: "modulation"
type: "graphical LFO/envelope-shaping and sidechain-emulation utility"
cpu_usage: "low"
best_genres:
  - dubstep
  - future_bass
  - progressive_house
  - trance
  - brostep
strengths:
  - "A drawable point-plus-tension-curve editor lets a producer sculpt an exact custom modulation shape rather than being limited to fixed LFO waveforms (sine, triangle, square), which is essential for the precisely-shaped pumping and wobble curves common in EDM production."
  - "Functions as both a retriggering LFO and a one-shot envelope shaper (Note Retrig vs. Envelope Mode), covering both continuous rhythmic modulation and single-event dynamic shaping from one plugin."
  - "Built-in sidechain-pumping curve presets replicate the classic sidechain-compression 'duck' shape without needing a real sidechain-compressor signal routing setup, useful when the source DAW or workflow makes true sidechain routing inconvenient."
  - "12 switchable LFO graphs per preset, changeable via MIDI notes or automation, allow a single instance to alternate between multiple pre-drawn modulation shapes within a track rather than requiring multiple plugin instances."
  - "Includes a built-in multi-mode filter section, so the shaped LFO can drive filter cutoff movement directly inside the same plugin rather than needing a separate filter with modulation routed to it."
weaknesses:
  - "It shapes amplitude/filter movement on the channel it's inserted on — it doesn't replace a true sidechain compressor when the goal is genuinely dynamic, signal-dependent ducking that responds to the actual level of a triggering track rather than a fixed, pre-drawn curve."
  - "Its value is centered on rhythmic, tempo-synced modulation; it's not built for the kind of slow, evolving, non-rhythmic modulation an LFO with long free-running rates inside a synth's own modulation matrix might provide."
alternatives:
  - "A DAW's native sidechain compressor (e.g. Ableton Compressor's sidechain input) for genuinely signal-dependent ducking rather than a fixed drawn curve"
  - "A synth's internal LFO/modulation matrix (per `knowledge_base/sound_design/synthesis/lfo_and_modulation_routing_design.md`) when the modulation needs to be routed to a synthesis parameter inside the patch itself rather than applied as a channel effect"
  - "Xfer OTT (`xfer_ott.md`) for multiband dynamic density rather than drawn amplitude/filter modulation"
recommended_settings:
  - "Classic sidechain pump on a pad or bass bus: a fast-attack, medium-decay ducking curve drawn or selected from the sidechain presets, retriggered every beat, per the sidechain-pumping technique in `knowledge_base/mixing/compression/sidechain_pumping.md`."
  - "Dubstep/brostep wobble bass: a custom-drawn rhythmic curve routed to the filter section's cutoff, tempo-synced to a subdivision matching the wobble rhythm, per the growl/wobble design approach in `knowledge_base/sound_design/presets/growl_and_wobble_bass_design.md`."
  - "Trance-gate rhythmic chop on a pad or synth: a hard on/off drawn curve with steep transitions, Note Retrig mode, synced to a 1/16 or 1/8 grid, per `knowledge_base/sound_design/effects/rhythmic_gating_and_trance_gate_automation.md`."
common_uses:
  - "Emulating sidechain-compression pumping without a true sidechain routing setup"
  - "Drawing exact custom rhythmic modulation curves for wobble bass, trance-gating, tremolo, and auto-pan effects"
  - "Driving the plugin's built-in filter section with a custom-shaped LFO for rhythmic filter movement"
tags: ["xfer", "lfo-tool", "modulation", "sidechain", "edm", "utility"]
---

# LFO Tool

LFO Tool (Xfer Records) is a graphical modulation-shaping utility built around a drawable point-and-tension-curve editor, letting a producer sculpt an exact custom LFO or envelope shape rather than choosing from fixed waveforms. It functions equally as a retriggering LFO for continuous rhythmic modulation and as a one-shot envelope shaper for single-event dynamics, and includes a built-in multi-mode filter section so the drawn modulation can drive cutoff movement directly. It's a distinct utility from Xfer's other KB entries (Serum for synthesis, OTT for multiband dynamics) — LFO Tool's role is precise, visually-drawn amplitude and filter modulation rather than sound generation or density processing.

## Sound Character and Strengths

LFO Tool's core strength is precision: where a synth's built-in LFO offers a handful of fixed waveform shapes, LFO Tool's point-plus-tension-curve editor lets a producer draw the exact attack, hold, and decay shape a part needs, which is directly relevant to the sidechain-pumping technique documented in `knowledge_base/mixing/compression/sidechain_pumping.md` — its built-in sidechain-curve presets replicate the classic ducking shape without requiring an actual sidechain-compressor signal chain. Its dual identity as both a retriggering LFO (Note Retrig mode) and a one-shot envelope shaper (Envelope Mode) means it covers both the continuous rhythmic modulation used for wobble bass and trance-gating, and the single-event dynamic shaping more typical of an ADSR envelope, from one plugin. The 12 switchable graphs per preset, changeable via MIDI or automation, let a single instance alternate between several pre-drawn modulation shapes across a track's sections.

## Weaknesses

LFO Tool shapes a channel's own amplitude or filter movement using a pre-drawn curve — it does not perform true sidechain compression, where the ducking amount responds dynamically to the actual level of a separate triggering track. When genuinely signal-dependent ducking is needed (the ducking amount should vary with how hard the kick actually hits, not follow a fixed drawn shape every time), a real sidechain compressor per `knowledge_base/mixing/compression/sidechain_pumping.md` is the correct tool, not LFO Tool's curve emulation. Its focus on rhythmic, tempo-synced modulation also makes it less suited to slow, evolving, non-rhythmic modulation, which is better handled inside a synth's own modulation matrix per `knowledge_base/sound_design/synthesis/lfo_and_modulation_routing_design.md`.

## Common Mistakes

Using LFO Tool's sidechain-emulation presets as a permanent substitute for real sidechain compression on a bass or pad that needs to duck in response to a live, dynamically varying kick pattern — the drawn-curve approach in `knowledge_base/mixing/compression/sidechain_pumping.md`'s emulation category is a convenient stand-in when true sidechain routing isn't practical, not a strictly equivalent replacement for genuine signal-dependent ducking.

## Cross-References

- `knowledge_base/mixing/compression/sidechain_pumping.md` — the sidechain-ducking technique LFO Tool's presets emulate via a drawn curve rather than true signal-dependent compression
- `knowledge_base/sound_design/effects/sidechain_and_ducking.md` — sound-design-stage framing of ducking/pumping as a rhythmic device, directly relevant to LFO Tool's rhythmic modulation use cases
- `knowledge_base/sound_design/presets/growl_and_wobble_bass_design.md` — the wobble-bass design context LFO Tool's filter-routed rhythmic curves are commonly used for
- `knowledge_base/sound_design/effects/rhythmic_gating_and_trance_gate_automation.md` — the trance-gate technique LFO Tool's hard on/off drawn curves directly implement
- `knowledge_base/sound_design/synthesis/lfo_and_modulation_routing_design.md` — general LFO/modulation routing philosophy, contrasted with LFO Tool's channel-effect (rather than in-synth) approach
- `knowledge_base/vst_database/xfer_ott.md` — a related Xfer plugin for multiband dynamic density rather than drawn modulation
