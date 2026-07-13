---
title: "Modulation Effects for Sound Design: Chorus, Flanger, and Phaser"
effect_type:
  - "Chorus"
  - "Flanger"
  - "Phaser"
  - "Ensemble/unison detune (chorus-adjacent)"
tags:
  - "chorus"
  - "flanger"
  - "phaser"
  - "modulation-effects"
  - "sound-design"
  - "width"
---

# Modulation Effects for Sound Design: Chorus, Flanger, and Phaser

Chorus, flanger, and phaser are all built on the same underlying mechanism — a delayed and pitch/phase-modulated copy of the source signal mixed back with the original — but the delay time and modulation depth used produce distinctly different effects, and this knowledge base's genre files reach for each one for a different specific sound-design purpose.

## Chorus for Width and Ensemble Character

Chorus uses a short, modulated delay (typically a few milliseconds to tens of milliseconds) to simulate multiple slightly-detuned voices playing the same part, and it appears across genre files most often as a width and thickness tool for leads, pads, and guitars. It's functionally related to (but distinct from) unison/detune settings on a synth oscillator itself — `knowledge_base/vst_database/lennardigital_sylenth1.md` documents a "wide chorus/unison spread" approach for trance leads that combines both techniques, using oscillator-level unison for the core width and chorus as an additional processing layer on top.

## Flanger for Sweeping, Metallic Movement

Flanger uses a shorter delay time than chorus (often under 20ms) with feedback, producing the characteristic sweeping, metallic, "jet engine" comb-filtering sound as the delay time modulates. It reads as a much more identifiable, foregrounded effect than chorus — appropriate for transitional moments (a riser or a build section) or as a deliberate texture on a specific element, rather than as an always-on width tool the way chorus is typically used.

## Phaser for Subtler Sweeping Movement

Phaser produces a related but gentler sweeping effect through phase-cancellation notches rather than a true delay line, generally reading as smoother and less metallic than a flanger. It's a common choice for adding movement to a static pad or bass sound without the more aggressive, obviously-processed character a flanger brings — useful when the goal is "keep this sound interesting over time" rather than "make this sound obviously effected."

## Choosing Between the Three

The practical selection principle across this knowledge base's sound-design guidance is intensity and foregrounding: chorus for a subtle, always-on width/thickness treatment that shouldn't call attention to itself; phaser for gentle, ongoing movement that adds interest without becoming the focal point; flanger for a deliberate, audible sweeping effect used as a specific texture or transitional device rather than a constant treatment. Applying flanger's intensity where chorus's subtlety was needed (or vice versa) is one of the more common modulation-effect mismatches.

## Common Mistakes

**Defaulting to chorus on every lead or pad without considering whether oscillator-level unison already provides sufficient width.** Stacking heavy oscillator unison and heavy chorus can produce excessive, phasey width rather than the intended thickening — per `knowledge_base/vst_database/lennardigital_sylenth1.md`, these two width sources should be balanced against each other, not both pushed to maximum independently.

**Using flanger for a subtle, always-on treatment.** Flanger's audible sweep makes it a poor choice for width tasks chorus handles more transparently — reserve it for moments where the sweeping effect itself is the intended musical gesture.

## Cross-References

- `knowledge_base/mixing/stereo/stereo_widening_techniques.md` — mix-stage stereo widening, complementary to but distinct from these sound-design-stage modulation effects
- `knowledge_base/vst_database/lennardigital_sylenth1.md` — documents chorus combined with oscillator unison for trance lead width
- `knowledge_base/sound_design/synthesis/subtractive_synthesis.md` — the oscillator-level unison/detune technique these effects are often layered on top of
