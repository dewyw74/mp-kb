---
plugin_name: "Analog"
developer: "Ableton"
category: "synth"
type: "virtual analog subtractive synth (stock Ableton Live instrument, modeled dual-oscillator architecture)"
cpu_usage: "low-medium"
best_genres:
  - house
  - techno
  - synth_pop
  - synthwave
  - trance
strengths:
  - "Component-modeled analog circuit behavior (oscillator drift, filter saturation, envelope character) in the spirit of u-he Diva's modeling approach, but included free with Ableton Live Suite."
  - "Two independently configurable oscillator/filter/envelope/amp signal paths that can run in parallel or series, giving it more internal routing flexibility than a single-signal-path subtractive synth."
  - "Native Instrument Rack/macro integration as a first-party device, same as Wavetable and Operator."
  - "Lower CPU cost than Diva for comparable modeled-analog patch complexity, useful in dense Ableton sessions."
weaknesses:
  - "Doesn't match Diva's per-component model-switching depth (multiple selectable vintage-synth-specific filter/oscillator models) — Analog offers one consistent modeled character rather than several selectable vintage circuit emulations."
  - "Smaller third-party preset ecosystem than dedicated third-party analog-modeled synths, tied as it is to the Ableton platform."
alternatives:
  - "u-he Diva (see `u-he_diva.md`) — deeper per-component vintage-circuit modeling, higher CPU cost"
  - "Ableton Drift (see `ableton_drift.md`) — a lighter-weight, newer alternative for simpler analog-style patches"
recommended_settings:
  - "Warm analog bass: single oscillator per signal path, moderate filter resonance, fast filter envelope for pluck-like attack, both signal paths detuned slightly against each other for width without a separate unison control."
  - "Classic house/techno stab: both signal paths active with contrasting filter settings (one bright/short, one warm/sustained), blended for a layered analog stab character."
common_uses:
  - "Warm, modeled-analog bass and lead design inside Ableton Live without leaving the DAW's own device set"
  - "Two-signal-path layered patches (bright plus warm, short plus sustained) using the dual signal-path architecture"
  - "General-purpose subtractive synthesis where Diva's deeper modeling isn't needed but a more characterful result than Wavetable's cleaner digital tone is wanted"
tags: ["analog", "ableton", "stock-device", "virtual-analog", "subtractive-synth"]
---

# Analog (Ableton Live)

Analog is Ableton Live's first-party virtual analog subtractive synthesizer, modeling component-level analog circuit behavior — oscillator drift, filter saturation, envelope character — in a similar spirit to u-he Diva's modeling approach, but included with Live Suite at no additional third-party cost. Its defining architectural feature is two independently configurable signal paths (each with its own oscillator, filter, envelope, and amp stage) that can be routed in parallel or series, giving it more internal signal-flow flexibility than a conventional single-path subtractive synth.

## Sound Character and Strengths

Analog's modeled circuit behavior gives it a warmer, more characterful tone than Ableton's cleaner, more digitally precise Wavetable instrument (`knowledge_base/vst_database/ableton_wavetable.md`), positioning it as the native-Ableton analog-modeled option in the same conceptual space as u-he Diva. Its dual signal-path architecture is genuinely useful for layered patches — two contrasting filter/envelope settings can be blended within one instance rather than requiring two separate synth instances layered in an Instrument Rack.

## Weaknesses

Analog offers one consistent modeled analog character rather than Diva's per-component switchable models (multiple selectable vintage filter/oscillator emulations within one instrument) — a producer chasing a specific named vintage synth's exact character is better served by Diva's more granular model selection. Its preset ecosystem is also smaller than a dedicated third-party analog synth's, being tied to the Ableton platform.

## Choosing Analog Over Diva or Wavetable

Reach for Analog when a modeled-analog warmth is wanted without Diva's higher CPU cost or deeper per-component model-switching complexity — for most house, techno, and synth-pop bass/lead work, Analog's single consistent character is sufficient. Reach for Diva specifically when a patch needs to target a particular vintage synth's exact modeled circuit behavior, and reach for Wavetable when the task calls for cleaner, more precisely evolving digital tone rather than analog warmth.

## Common Mistakes

**Expecting Diva-level per-component model switching from Analog.** Analog's modeling is consistent and unified rather than offering several selectable vintage-circuit emulations — approaching it expecting that flexibility will lead to disappointment; it's a different, simpler tool by design.

## Cross-References

- `knowledge_base/sound_design/synthesis/subtractive_synthesis.md` — general subtractive synthesis technique, of which Analog is a native-Ableton example instrument
- `knowledge_base/vst_database/u-he_diva.md` — the deeper, per-component-modeled alternative for targeting specific vintage synth character
- `knowledge_base/vst_database/ableton_wavetable.md`, `knowledge_base/vst_database/ableton_drift.md` — Ableton's complementary stock synths for wavetable and lightweight subtractive/wavetable-hybrid patches respectively
