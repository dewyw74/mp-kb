---
plugin_name: "Auto Filter"
developer: "Ableton"
category: "other"
type: "modulatable filter effect (stock Ableton Live, multiple filter types with built-in LFO/envelope-follower modulation)"
cpu_usage: "low"
best_genres:
  - house
  - french_house
  - dubstep
  - progressive_trance
strengths:
  - "Multiple filter type/slope options (lowpass, highpass, bandpass, notch, and morph variants) in one device, covering most filter-shape needs without switching plugins."
  - "Built-in LFO and envelope-follower modulation sources routed directly to cutoff/resonance, implementing filter-sweep automation (per `knowledge_base/genres/edm/french_house.md`'s filter-sweep-as-arrangement technique) without needing a separate modulation device."
  - "Included with every edition of Ableton Live, with native Rack/macro and Arrangement View automation integration."
  - "Very low CPU cost, making it practical to place on many channels for filter-movement effects across a session."
weaknesses:
  - "As an insert effect, it filters an already-recorded or already-synthesized signal — it doesn't replace a synth's own internal filter for sound-design-stage patch building the way Wavetable's or Analog's filter sections do."
  - "Its envelope-follower mode, while useful, is a simpler implementation than a dedicated sidechain-triggered dynamic EQ or filter plugin might offer for complex program-dependent filtering."
alternatives:
  - "A synth's own internal filter (Wavetable, Analog, Operator — see their respective entries) for sound-design-stage filtering rather than post-hoc insert filtering"
  - "Ableton EQ Eight (see `ableton_eq_eight.md`) for static, non-modulated filtering needs"
recommended_settings:
  - "French house filter-sweep intro/build: lowpass filter type, cutoff swept from closed to fully open via a slow manual automation ramp (8-16 bars) rather than the built-in LFO, per `knowledge_base/genres/edm/french_house.md`'s filter-sweep-as-arrangement guidance."
  - "Dubstep/riddim rhythmic gating: bandpass or lowpass filter type with the built-in LFO synced to a tempo subdivision and set to a fast, tempo-locked rate, implementing the rhythmic-gating technique from `knowledge_base/sound_design/effects/rhythmic_gating_and_trance_gate_automation.md` directly on an already-recorded or sampled source."
common_uses:
  - "Filter-sweep builds and breakdowns on sampled loops or full mix buses"
  - "Rhythmic, LFO-synced filter gating as an insert effect on samples or sustained pads"
  - "Envelope-follower-driven filtering that reacts to a signal's own dynamics"
tags: ["auto-filter", "ableton", "stock-device", "filter", "modulation"]
---

# Auto Filter (Ableton Live)

Auto Filter is Ableton Live's first-party modulatable filter effect, offering multiple filter types (lowpass, highpass, bandpass, notch, and morph variants) alongside built-in LFO and envelope-follower modulation sources routed directly to cutoff and resonance. Unlike a synth's internal filter section, Auto Filter is an insert effect — it filters whatever signal is already present on a track, whether that's a synth, a sample, or a full mix bus, making it the tool for post-hoc filter movement rather than sound-design-stage patch building.

## Sound Character and Strengths

Auto Filter's built-in modulation sources are what make it more than a static filter — the LFO can be tempo-synced for rhythmic gating effects (directly implementing the technique documented in `knowledge_base/sound_design/effects/rhythmic_gating_and_trance_gate_automation.md` on any track, not just a synth patch with its own internal gate), and the envelope follower lets the filter react to the input signal's own dynamics rather than an independent modulation source. Its multiple filter-type options and inclusion with every edition of Live make it a practical, no-cost default for filter-sweep and filter-movement needs across a session.

## Weaknesses

Because it's an insert effect applied after a signal already exists, Auto Filter doesn't replace a synth's own internal filter for building a patch's fundamental character — that sound-design-stage filtering belongs inside the synth itself (Wavetable's, Analog's, or Operator's filter sections). Its envelope-follower mode is also a simpler tool than a dedicated program-dependent dynamic EQ or filter plugin might offer for more complex sidechain-triggered filtering scenarios.

## Common Uses Across This Knowledge Base's Genre Guidance

`knowledge_base/genres/edm/french_house.md` documents filter-sweep automation as "the arrangement, not decoration" — Auto Filter on a sampled loop, swept open over many bars via manual automation, is the direct implementation of that technique. `knowledge_base/sound_design/effects/rhythmic_gating_and_trance_gate_automation.md`'s riddim-style gating technique can be applied to any track (not just inside a synth) using Auto Filter's tempo-synced LFO mode.

## Common Mistakes

**Using Auto Filter's built-in LFO for a slow, arrangement-scale filter sweep instead of manual automation.** For long, multi-bar sweeps like French house's intro build, manually drawn automation gives more precise control over the sweep's exact timing and curve than a free-running or even tempo-synced LFO.

## Cross-References

- `knowledge_base/genres/edm/french_house.md` — the filter-sweep-as-arrangement technique this device directly implements
- `knowledge_base/sound_design/effects/rhythmic_gating_and_trance_gate_automation.md` — the rhythmic gating technique Auto Filter's tempo-synced LFO mode can apply to any track
- `knowledge_base/vst_database/ableton_wavetable.md`, `knowledge_base/vst_database/ableton_analog.md` — where sound-design-stage (rather than insert-effect-stage) filtering belongs
