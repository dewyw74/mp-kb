---
title: "Reese Bass Design"
synthesis_method:
  - "Subtractive"
  - "Detuned oscillator pair"
tags:
  - "reese-bass"
  - "jungle"
  - "drum-and-bass"
  - "detuned-oscillators"
  - "sound-design"
---

# Reese Bass Design

The Reese bass — named for Kevin "Reese" Saunderson's use of the technique — is the foundational detuned-oscillator-pair bass sound underlying jungle, drum & bass, speed garage, and much of dubstep's mid-bass vocabulary. `knowledge_base/sound_design/presets/edm_bass_design.md`'s Reese/Growl archetype (Section 3) documents the neurofunk-specific aggressive evolution of this technique; this entry is the dedicated reference for the underlying Reese mechanism itself and its spread across genres beyond neurofunk.

## The Core Mechanism

1. **Two detuned sawtooth oscillators**: the classic Reese pair is two sawtooth oscillators tuned a few cents apart (not the wider 15-25 cent unison-stack detune used for supersaw width — Reese detuning is narrower and specifically tuned to produce a slow, audible phase-beating rather than a fast shimmer). The slower the beat rate relative to the note's sustain, the more the ear perceives a churning, "alive" low-end movement rather than simple thickness.
2. **Panning for stereo/mono balance**: the two detuned voices are sometimes panned hard left/right for width (speed garage, some dubstep contexts) and sometimes kept centered/mono (classic jungle, riddim-adjacent uses) — stereo placement is a genre-specific choice layered on top of the same underlying detuning mechanism, not part of the mechanism itself.
3. **Filter and movement**: a resonant lowpass or bandpass filter, often with slow phaser/chorus movement for a smoother, liquid-adjacent character, or fast envelope/LFO movement for a more aggressive neurofunk-style growl — the same detuned pair scales from smooth to violent purely through modulation intensity.
4. **Distortion staging**: light saturation for a warmer, classic jungle/DnB tone; heavy multi-stage distortion/waveshaping for neurofunk's aggressive growl evolution (see `edm_bass_design.md` Section 3 for the full neurofunk recipe).
5. **Sub layer underneath**: as with every bass archetype surveyed in `edm_bass_design.md`, a clean sine sub beneath the Reese pair provides the physical low-end weight the detuned/distorted layer alone can't reliably deliver (see `knowledge_base/sound_design/presets/sub_bass_design.md`).

## Genre Grounding

- `knowledge_base/genres/edm/jungle.md` documents "Reese bass synthesis (detuned sawtooth oscillators, phase-modulated) for darker jungle," built from a "detuned saw pair" with "slow phaser/chorus on Reese bass for movement and width," and explicitly instructs keeping "sub-bass mono and separate from mid-bass/Reese content so both translate on club soundsystems without phase cancellation."
- `knowledge_base/genres/edm/speed_garage.md` documents the Reese bassline as "the genre's core identifying element," built from "detuned, layered sawtooth oscillators" imported directly from jungle/drum and bass, warning explicitly against "writing a thin, single-oscillator sub bass instead of a properly layered, detuned Reese bass, which loses the genre's core low-end identity" — the thick, slightly dissonant beating between detuned layers named as "the genre's signature low-end character."
- `knowledge_base/genres/edm/neurofunk.md` documents "a distorted, resonant, heavily modulated 'growl' or 'reese' bass built from layered detuned oscillators run through aggressive filtering, distortion, and often FM or wavetable modulation for a snarling, almost vocal-like rhythmic character" — the most extreme, heavily processed evolution of the same detuned-pair mechanism.
- `knowledge_base/genres/edm/slap_house.md` documents "a warm Reese-bassline-style sub-bass tone" as the genre's defining bass element, showing the technique's reach into modern mainstream house production well outside its jungle/DnB origin.
- `knowledge_base/genres/edm/dubstep.md` (via `edm_bass_design.md`'s wobble archetype) documents "a Reese-style pair (two sawtooths tuned a few cents apart, one panned hard left/right) beneath the main stack for extra thickness," used as a layering technique within a larger wobble-bass patch rather than the sole bass source.

## Common Mistakes

**Confusing Reese detuning with wide unison-stack detuning.** The two produce different perceptual results — Reese's narrow, slow-beating detune is deliberately audible as churning movement, while a wide unison stack (7+ voices, wider spread) is designed for shimmer and width rather than a distinct two-voice beat.

**Building a single-oscillator sub in place of a properly layered, detuned pair.** Per `speed_garage.md`'s explicit warning, this loses the genre-defining low-end character entirely — the detuned beating is the point, not an incidental texture.

## Cross-References

- `knowledge_base/sound_design/presets/edm_bass_design.md` — Section 3's neurofunk/DnB Reese-growl archetype recipe this entry's foundational mechanism supports.
- `knowledge_base/sound_design/presets/growl_and_wobble_bass_design.md` — the wavetable-modulation movement technique often layered onto a Reese pair in modern riddim-adjacent patches.
- `knowledge_base/sound_design/presets/sub_bass_design.md` — the clean sub layer every Reese bass patch needs beneath the detuned mid-bass.
- `knowledge_base/genres/edm/jungle.md`, `knowledge_base/genres/edm/speed_garage.md`, `knowledge_base/genres/edm/neurofunk.md`, `knowledge_base/genres/edm/slap_house.md`, `knowledge_base/genres/edm/dubstep.md` — genre sources grounding this entry.
