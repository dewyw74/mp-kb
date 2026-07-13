---
title: "Serum 2 Hybrid Wavetable/Sample-Layer Bass — Full Patch Walkthrough"
synthesis_method:
  - "Wavetable"
  - "Sample-based"
  - "FM"
tags:
  - "serum-2"
  - "hybrid-synthesis"
  - "growl-bass"
  - "riddim"
  - "preset-recipe"
  - "semi-modular"
---

# Serum 2 Hybrid Wavetable/Sample-Layer Bass — Full Patch Walkthrough

`knowledge_base/vst_database/xfer_serum_2.md` names "modern growl/riddim bass: combine a wavetable oscillator with a sample-playback layer routed through the expanded modulation matrix for hybrid formant-and-wavetable movement" as a recommended use case, but doesn't walk through the build step by step. This entry fills that gap, extending the wobble/growl and riddim gate bass archetypes already documented in `knowledge_base/sound_design/presets/edm_bass_design.md` with the specific hybrid technique Serum 2's semi-modular architecture makes newly possible in a single instance.

## Why This Patch Needs Serum 2, Not Serum 1

Serum 1's fixed signal chain (oscillators into filter into effects, in a set order) can layer a wavetable oscillator with a sample-based one only by routing them to separate, parallel paths that don't meaningfully modulate each other — genuine cross-modulation between a wavetable source and a sample-playback source isn't available. Serum 2's semi-modular routing lets one oscillator's output feed another's modulation input directly, which is what makes the "hybrid formant-and-wavetable movement" `xfer_serum_2.md` describes actually achievable: the sample layer's amplitude or spectral content can modulate the wavetable oscillator's position or filter cutoff in real time, producing movement neither layer could generate alone.

## Sound Sources

**Layer 1 — Wavetable oscillator:** A standard growl-bass wavetable (per `knowledge_base/sound_design/presets/edm_bass_design.md`'s wobble/growl archetype), providing the patch's pitched, tonally stable foundation. Set unison to a moderate 2-4 voices — wider than this competes for space with the sample layer's own harmonic content.

**Layer 2 — Sample-playback oscillator:** A short vocal or formant-rich sample (a vowel sound, a breathy vocal one-shot, or a recorded acoustic transient) loaded into Serum 2's sample-based oscillator slot. This layer is the source of the "formant" character `xfer_serum_2.md` names — its job is contributing harmonic/formant complexity the wavetable layer alone can't produce, not carrying the bass's fundamental pitch (that's the wavetable layer's job).

**Layer 3 — Sub reinforcement:** Per the governing principle in `knowledge_base/sound_design/presets/edm_bass_design.md` ("layer a clean sine sub beneath the modulated/distorted mid-bass character"), add a simple, undistorted sine sub tracking the wavetable layer's root note, mono and centered, untouched by any of the cross-modulation routing below.

## Cross-Modulation Routing (the Serum 2-Specific Step)

Using Serum 2's semi-modular routing, feed the sample-playback oscillator's amplitude envelope (or a spectral/formant-tracking modulation source, if the specific sample-oscillator implementation exposes one) into the wavetable oscillator's position modulation input. This produces wavetable position movement that's driven by the sample's own timbral evolution rather than a generic LFO — the wavetable layer's tone shifts in sync with the sample layer's natural envelope/formant movement, producing the "hybrid formant-and-wavetable movement" character rather than two independently-modulated layers that happen to play together.

## Distortion and Filter Chain (Non-Default Ordering)

`xfer_serum_2.md` specifically calls out "chaining distortion into a resonant filter in a non-default order" as part of this patch's technique. Rather than Serum 1's fixed post-oscillator-filter-then-effects order, route distortion so it processes only the combined/cross-modulated signal after the wavetable-position modulation has already been applied, then follow with the resonant filter — this means the filter is shaping an already-distorted, already-cross-modulated signal, producing a more complex harmonic result than distortion-then-filter-then-done would.

## Rhythmic Character (Riddim Variant)

For a riddim-style version of this patch (per `knowledge_base/sound_design/presets/edm_bass_design.md`'s riddim gate bass archetype), gate the combined wavetable/sample layer's amplitude with a step-sequenced or tightly-quantized LFO locked to a half-time groove, keeping pitch static and varying gate timing, filter movement, and distortion amount for pattern variation — the same rhythmic/timbral-not-melodic principle as the Serum 1 riddim archetype, now applied to a richer, cross-modulated sound source.

## Common Mistakes

**Building this patch as two independently-modulated layers rather than using the actual cross-modulation routing.** Per `xfer_serum_2.md`'s own guidance, simply stacking a wavetable oscillator and a sample oscillator side by side (each with its own separate LFO) is achievable in Serum 1 too — it doesn't use Serum 2's actual architectural advantage and doesn't justify the higher CPU cost.

**Letting the sample layer's pitch drift from the wavetable layer's root.** Unless a deliberately dissonant or atonal texture is the goal, the sample layer should be pitched (or its pitch tracking disabled and its role kept purely textural/formant) so it reinforces rather than clashes with the wavetable layer's fundamental.

**Skipping the clean sub layer because the patch already feels "full" from the two modulated layers.** Per `edm_bass_design.md`, the sub's job (translating physical low-end weight on a soundsystem) is independent of how rich the mid-bass content is — a hybrid patch needs the sub just as much as a simpler single-oscillator growl bass does.

## Cross-References

- `knowledge_base/vst_database/xfer_serum_2.md` — the source recommendation this entry walks through in full
- `knowledge_base/sound_design/presets/edm_bass_design.md` — the wobble/growl and riddim gate bass archetypes this hybrid patch extends
- `knowledge_base/sound_design/synthesis/wavetable_synthesis.md`, `knowledge_base/sound_design/synthesis/fm_synthesis.md` — the underlying synthesis techniques combined in this patch
- `knowledge_base/genres/edm/riddim.md` — the rhythmic-gating genre context relevant to the riddim variant
