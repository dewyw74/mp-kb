---
plugin_name: "Saturator"
developer: "Ableton"
category: "saturation"
type: "waveshaping saturation/distortion device (stock Ableton Live, multiple curve types)"
cpu_usage: "low"
best_genres:
  - house
  - hip_hop
  - boom_bap
  - techno
strengths:
  - "Included with every edition of Ableton Live, with a visual waveshaping curve display showing exactly how the selected curve reshapes the signal."
  - "Multiple selectable waveshaping curve types (analog clip, digital clip, warm, and several others) covering a real range of saturation character within one free, native device."
  - "A built-in pre/post filter (DC filter and a shaping filter) lets the saturation stage's frequency range be controlled directly, avoiding uncontrolled full-range distortion."
  - "Very low CPU cost, practical to place on many channels without performance concerns."
weaknesses:
  - "Doesn't carry the specific, widely-referenced hardware-emulation lineage of a plugin like Soundtoys Decapitator (`soundtoys_decapitator.md`) — its curves are Ableton-native designs rather than modeled on named classic analog units."
  - "Fewer distinctly different 'models' than Decapitator's five hardware-emulated circuits, though its curve types still cover a meaningful tonal range."
alternatives:
  - "Soundtoys Decapitator (see `soundtoys_decapitator.md`) — hardware-emulation-specific character, five selectable circuit models"
  - "Xfer OTT (see `xfer_ott.md`) — for density via multiband compression rather than waveshaping saturation"
recommended_settings:
  - "Subtle mix-bus warmth: Warm or Analog Clip curve type, low drive, applied gently across a mix or drum bus per `knowledge_base/mixing/saturation/harmonic_saturation_and_distortion.md`'s vintage-warmth guidance."
  - "Aggressive drum bus character: Digital Clip or a harder curve type, higher drive, with the built-in shaping filter narrowed to target the frequency range that most needs grit rather than distorting the full spectrum."
common_uses:
  - "General-purpose mix-bus, drum-bus, and individual-channel saturation and harmonic density"
  - "Frequency-targeted distortion using the built-in shaping filter to distort a specific range rather than the whole signal"
  - "A free, always-available saturation option inside Ableton before reaching for a third-party plugin like Decapitator"
tags: ["saturator", "ableton", "stock-device", "saturation", "distortion", "mixing"]
---

# Saturator (Ableton Live)

Saturator is Ableton Live's first-party waveshaping saturation and distortion device, included with every edition of Live and offering multiple selectable curve types alongside a visual display showing exactly how each curve reshapes the incoming waveform. It's the native-Ableton implementation of the mix-stage saturation technique documented in `knowledge_base/mixing/saturation/harmonic_saturation_and_distortion.md`, covering both the subtle-warmth and aggressive-character ends of that spectrum within one free device.

## Sound Character and Strengths

Saturator's curve-type selector gives it real tonal range for a native, no-cost device — different curves produce meaningfully different harmonic character, from gentler analog-modeled warmth to harder digital clipping. Its built-in shaping filter (letting the saturation stage's frequency range be constrained rather than applied full-range) is a genuinely useful feature not every dedicated saturation plugin offers as directly — it allows, for instance, saturating only the low-mid character of a bass sound while leaving its top end untouched, without needing a separate multiband/EQ split.

## Weaknesses

Saturator's curves are Ableton-native designs rather than modeled on a specific, widely-referenced piece of analog hardware — a producer specifically chasing "the sound of" a named classic saturation unit (the way Decapitator's five models each target a specific analog lineage) won't find that same hardware-emulation specificity here. Its curve-type variety, while real, is narrower than Decapitator's distinct circuit models.

## Choosing Saturator Over a Third-Party Saturation Plugin

For general-purpose warmth, density, and character work — the majority of saturation use cases documented in `knowledge_base/mixing/saturation/harmonic_saturation_and_distortion.md` — Saturator's built-in curve types and shaping filter are fully capable and cost nothing extra. Reach for Decapitator specifically when a track's character depends on a recognizable, specific hardware-emulated saturation sound rather than saturation in general.

## Common Mistakes

**Applying saturation full-range when only a specific frequency band needs the added harmonic content.** Saturator's built-in shaping filter exists precisely to avoid this — skipping it and saturating the entire signal risks distorting frequency content (like a sub-bass fundamental) that should stay clean.

## Cross-References

- `knowledge_base/mixing/saturation/harmonic_saturation_and_distortion.md` — the general mix-stage saturation technique this device implements natively in Ableton
- `knowledge_base/vst_database/soundtoys_decapitator.md` — the hardware-emulation-specific third-party alternative
- `knowledge_base/vst_database/ableton_compressor_and_glue_compressor.md` — commonly paired with Saturator in a bus-processing chain for combined density and glue
