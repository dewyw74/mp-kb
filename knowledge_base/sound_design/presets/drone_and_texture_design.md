---
title: "Drone and Texture Design"
synthesis_method:
  - "Analog modular/subtractive"
  - "Granular"
  - "Additive/organ synthesis"
tags:
  - "drone"
  - "texture"
  - "sustained-sound"
  - "just-intonation"
  - "dark-ambient"
  - "sound-design"
---

# Drone and Texture Design

A drone is a sustained, typically beatless sound source — a single fundamental or a small cluster of tones held (or continuously regenerated) for extended durations, with movement, if any, living in slow timbral/textural change rather than rhythm or melody. This is distinct from pad design (`knowledge_base/sound_design/presets/pad_and_atmosphere_design.md`, `knowledge_base/sound_design/presets/pad_design_archetypes_and_patch_recipes.md`), which covers chord-voiced, typically harmonically-moving synth layers supporting other elements — a drone is frequently the *only* element present, is not necessarily built from a conventional chord voicing, and treats non-tonal noise/field-recording sources as first-class material rather than an occasional layer.

## Building a Drone

1. **Sustain-capable sources**: anything capable of genuinely continuous sound generation works — analog modular oscillators, sustain-pedal/drone-mode synth patches, feedback-driven electric guitar (often in alternate/drone tunings), bowed strings using extended technique (sul ponticello, harmonics), or drawbar/organ-style additive synthesis for rich harmonic drones. Percussive, transient-attack sources are essentially excluded by definition, since a drone's identity depends on unbroken sustain.
2. **Just-intonation tuning**: tuning drone layers to simple integer-ratio intervals (a perfect fifth at exactly 3:2, rather than the slightly-off equal-tempered fifth) produces a richer, more resonant beating pattern between overtones than equal temperament — a technique specific to drone work where the beating itself becomes part of the perceived texture.
3. **Slow chaos/random modulation**: rather than a fast rhythmic LFO, drone and dark-ambient texture design uses very slow, often randomized modulation sources (chaos LFOs, extremely long-period random walks) on filter cutoff, detune amount, or granular scan position — movement present but never resolving into a perceptible cycle.
4. **Granular processing for evolving texture**: feeding field recordings or short samples through a granular engine and freezing/slowly scanning through them produces genuinely non-repeating textural evolution — distinct from a looping oscillator or wavetable pad's more periodic movement (see `knowledge_base/sound_design/synthesis/granular_synthesis.md`).
5. **Feedback as a legitimate source**: guitar/amp feedback or synth self-oscillation is a traditional and structurally important drone source in its own right, not merely an accident to be avoided — relying solely on sustained synth pads misses a large part of the genre's sonic vocabulary.
6. **Extreme low-end and infrasound**: dark-ambient and horror-adjacent texture work frequently layers content below conscious hearing threshold (very low sub content) specifically to induce unease at a physical rather than melodic level.

## Genre Grounding

- `knowledge_base/genres/electronic/drone.md` (the genre) documents the technique set directly: analog modular oscillator drones, additive/organ synthesis, granular synthesis "for slowly shifting drone clouds," just-intonation tuning ("a perfect fifth at exactly 3:2... for a richer, more resonant beating pattern"), and feedback as "a legitimate and traditional sound source for drone," with pieces conventionally running 15-40+ minutes.
- `knowledge_base/genres/electronic/dark_ambient.md` documents "sub-bass drones and low rumble (often below 60 Hz)" as the genre's foundation, "analog modular for raw drones," "granular synthesis of noise and field recordings," "slow random/chaos LFOs," and "extreme detuning between voices for beating/dissonance" — a texture-first approach built on "static tone clusters, no functional progression."
- `knowledge_base/genres/electronic/space_ambient.md` (per `knowledge_base/sound_design/presets/pad_design_archetypes_and_patch_recipes.md`) documents "sine subs for foundation" beneath "detuned saw stacks for lush pad width," showing drone-adjacent sub layering used to support a more pad-like texture in a related but distinct genre.
- `knowledge_base/genres/cinematic/horror_score.md` documents "infrasound/very low frequency content (below conscious hearing) used to induce unease" and "detuned, dissonant stacks for cluster-like synth textures echoing orchestral tone clusters" as explicit sound-design techniques (see `knowledge_base/sound_design/presets/horror_and_tension_drone_design.md` for the dedicated tension-drone treatment).

## Common Mistakes

**Introducing too much event-based variation.** Per `drone.md`'s own guidance, adding frequent discrete events pulls a piece toward ambient (event-driven atmosphere) rather than true drone stasis — the genre's identity depends on sustained, largely unbroken continuity.

**Relying solely on sustained synth pads and ignoring feedback and acoustic extended-technique sources.** These are traditional, structurally significant drone sources in their own right, not a stylistic afterthought.

**Underestimating duration.** A 3-minute "drone" rarely achieves the immersive, time-dissolving effect the form depends on; drone pieces conventionally run far longer than a typical song section.

## Cross-References

- `knowledge_base/sound_design/presets/pad_and_atmosphere_design.md`, `knowledge_base/sound_design/presets/pad_design_archetypes_and_patch_recipes.md` — the chord-voiced, structurally-supporting pad counterpart this entry's standalone drone/texture approach is distinct from.
- `knowledge_base/sound_design/presets/horror_and_tension_drone_design.md` — the dissonance-specific application of drone/texture technique to horror and tension scoring.
- `knowledge_base/sound_design/synthesis/granular_synthesis.md` — the granular-processing technique underlying evolving drone textures.
- `knowledge_base/genres/electronic/drone.md`, `knowledge_base/genres/electronic/dark_ambient.md`, `knowledge_base/genres/electronic/space_ambient.md`, `knowledge_base/genres/cinematic/horror_score.md` — genre sources grounding this entry.
