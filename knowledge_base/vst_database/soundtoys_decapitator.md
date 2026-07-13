---
plugin_name: "Decapitator"
developer: "Soundtoys"
category: "saturation"
type: "analog-modeled saturation/distortion unit (5 selectable circuit models)"
cpu_usage: "low"
best_genres:
  - boom_bap
  - lo_fi_hip_hop
  - house
  - hip_hop
  - rock
strengths:
  - "Five selectable analog circuit models (labeled A through E, each modeled on a different class of vintage analog gear — tube preamp, transformer, and other classic saturation sources) give it more tonal variety than a single-character saturation plugin."
  - "A dedicated Punish mode pushes the saturation into a much more extreme, aggressive territory than the standard drive range, useful for the deliberately harsh/distorted character documented in `knowledge_base/sound_design/effects/distortion_and_saturation_sound_design.md`."
  - "Very low CPU cost, making it practical to instantiate on many individual channels as well as bus/master applications."
  - "Widely used both as a subtle, always-on warmth/density tool and as an aggressive, foregrounded distortion effect, covering both ends of the saturation-intensity spectrum documented in `knowledge_base/mixing/saturation/harmonic_saturation_and_distortion.md`."
weaknesses:
  - "As a single-effect saturation unit, it doesn't offer the layered generative sound-design role a synth's internal distortion/waveshaping stage provides (per `knowledge_base/sound_design/effects/distortion_and_saturation_sound_design.md`'s distinction between sound-design-stage and mix-stage saturation) — it's a mix/mastering-stage tool, not a patch-building one."
  - "Its five circuit models, while varied, are all analog-modeled/harmonic-saturation character — it doesn't cover the harsher, more digital bitcrush/sample-rate-reduction territory documented for hyperpop and vaporwave-style degradation."
alternatives:
  - "Xfer OTT (see `xfer_ott.md`) — for density via multiband upward/downward compression rather than harmonic saturation"
  - "A DAW's stock saturation device, where available, for a lighter-weight but less characterful alternative"
recommended_settings:
  - "Subtle mix-bus warmth: low drive amount, a transformer- or tube-modeled circuit setting, applied across a full mix bus or drum bus per the vintage-warmth guidance in `knowledge_base/mixing/saturation/harmonic_saturation_and_distortion.md`."
  - "Aggressive character distortion: higher drive amount or Punish mode engaged on an individual element (drum bus, bass, vocal) where audible grit and harmonic density is the deliberate goal, per the aggressive-distortion genre guidance in the same entry."
common_uses:
  - "Subtle, always-on harmonic warmth and density on mix buses, drum buses, and individual channels"
  - "Aggressive, foregrounded saturation/distortion as a deliberate character effect"
  - "Vintage-analog tonal coloring on otherwise clean digital source material"
tags: ["decapitator", "soundtoys", "saturation", "distortion", "analog-modeled", "mixing"]
---

# Decapitator

Decapitator (Soundtoys) is an analog-modeled saturation and distortion plugin offering five selectable circuit models, each based on a different class of classic analog hardware saturation source, plus a dedicated Punish mode for pushing well past subtle warmth into aggressive, foregrounded distortion territory. It's one of the most widely used dedicated saturation plugins in modern mixing precisely because its five-model selector covers both ends of the saturation-intensity spectrum documented in `knowledge_base/mixing/saturation/harmonic_saturation_and_distortion.md` — vintage warmth and deliberate genre-signature aggression — within one plugin.

## Sound Character and Strengths

Decapitator's five circuit models give it more tonal variety than a single-character saturation unit — a producer can select a specific analog-modeled flavor to match a track's intended vintage character rather than settling for one fixed saturation curve. Its Punish mode is a genuinely distinct, more extreme processing stage rather than just an extension of the drive knob's range, making the plugin useful across the full range from `knowledge_base/mixing/saturation/harmonic_saturation_and_distortion.md`'s "subtle, barely perceptible" end to its "extreme, audibly distorted, becomes the sound's defining character" end. Its very low CPU cost makes it practical to place on many channels at once, not just a single master-bus instance.

## Weaknesses

Decapitator is exclusively a mix/mastering-stage tool — it doesn't play the sound-design-stage, patch-building role that a synth's internal waveshaping/distortion stage provides (the generative distinction documented in `knowledge_base/sound_design/effects/distortion_and_saturation_sound_design.md`). Its character is also entirely analog-modeled harmonic saturation — none of its five models reach into the harsher, more digital bitcrush/sample-rate-reduction territory that genres like hyperpop or vaporwave call for; a separate bitcrush/digital-degradation tool is needed for that different character.

## Choosing Decapitator Over Sound-Design-Stage Distortion

Reach for Decapitator when the goal is adding density, warmth, or aggressive character to an already-recorded or already-programmed track (a mix-stage decision), not when building a synth patch's core harmonic content from scratch (a sound-design-stage decision best handled inside the synth itself, per `knowledge_base/sound_design/effects/distortion_and_saturation_sound_design.md`). The two are complementary rather than interchangeable — a bass patch can use internal waveshaping to generate its raw harmonic character and still receive further Decapitator treatment at the mix stage for additional density.

## Common Mistakes

**Reaching for Decapitator to build a bass patch's core distorted character instead of using the synth's own internal waveshaping.** Per `knowledge_base/sound_design/effects/distortion_and_saturation_sound_design.md`, generative, patch-defining distortion is more effective built into the synthesis chain itself — Decapitator is better suited to adding density on top of an already-designed sound.

**Using a single circuit model/setting across every application without matching it to the target character.** The five models genuinely differ in tonal result — picking one and using it universally wastes the plugin's main advantage over a simpler, single-character saturation tool.

## Cross-References

- `knowledge_base/mixing/saturation/harmonic_saturation_and_distortion.md` — the general mix-stage saturation technique this plugin directly implements, across its full subtle-to-extreme range
- `knowledge_base/sound_design/effects/distortion_and_saturation_sound_design.md` — the sound-design-stage counterpart, clarifying when to use synth-internal distortion instead of a mix-stage tool like this one
- `knowledge_base/vst_database/xfer_ott.md` — a related density-building mix-stage tool using a different underlying mechanism (multiband compression rather than harmonic saturation)
