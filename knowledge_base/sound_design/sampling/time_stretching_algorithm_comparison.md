---
title: "Time-Stretching Algorithms Compared"
technique: "Choosing between elastic/formant-preserving and simple resampling time-stretch methods"
tags:
  - "time-stretching"
  - "pitch-shifting"
  - "formant-preserving"
  - "elastic-audio"
  - "sampling"
  - "algorithm-comparison"
---

# Time-Stretching Algorithms Compared

`knowledge_base/sound_design/sampling/chopping_flipping_and_time_stretching.md` establishes that pitch and time are independent manipulation axes and that genre context determines whether stretch artifacts should be embraced or avoided. This entry goes one level deeper: comparing the specific *algorithms* available for time-stretching and pitch-shifting — elastic/formant-preserving methods vs. simple resampling (speed-linked pitch change) vs. the grainy character of early hardware — and what each one actually does mechanically to produce its characteristic artifacts. Genre files consulted for grounding: `knowledge_base/genres/edm/happy_hardcore.md`, `electro_swing.md`, `tech_house.md`, plus `knowledge_base/sound_design/sampling/sampling_and_resampling.md`'s existing jungle/S1000 grounding.

## Simple Resampling: Speed and Pitch Linked

The most basic time-stretch/pitch-shift method is simple resampling — literally playing a sample back faster or slower, which changes both speed and pitch together in direct proportion, exactly like speeding up or slowing down a physical tape or turntable. There is no independent axis here: doubling playback speed also raises pitch by an octave. `happy_hardcore.md`'s sound-design notes name this method directly by contrast with a formant-preserving alternative: "Formant-preserving or classic resampling pitch-shift on vocal chops to keep them intelligible at high pitch" — "classic resampling" is this method, offered as one of two named options specifically because it produces a different, more overtly "sped-up" character than a formant-preserving algorithm. Chopped-and-screwed (per `chopping_flipping_and_time_stretching.md`) is the same mechanism applied in the opposite direction — slowing playback lowers pitch proportionally.

## Elastic/Formant-Preserving Algorithms: Independent Time and Pitch Axes

Modern "elastic audio" or "complex" time-stretch algorithms (Ableton's Complex/Complex Pro warp modes, dedicated tools like zplane's Élastique) decouple time and pitch, letting either be changed independently of the other. Mechanically, these algorithms analyze the audio's transient and pitch content, then reconstruct it at the new tempo or pitch using overlapping, time-adjusted grains or phase-vocoder-style spectral processing (the same underlying grain mechanics documented in `granular_resynthesis_vs_discrete_chopping.md`) rather than simply replaying the waveform faster or slower.

- `electro_swing.md` documents this algorithm family used specifically for transparency: "Using high-quality time-stretch/pitch-shift algorithms (elastic audio, warp modes) to cleanly fit vintage samples to a modern tempo grid with minimal artifacting" — the explicit goal here is inaudibility, fitting a vintage swing/jazz sample to a new tempo without the listener noticing the sample has been stretched at all.
- `tech_house.md` documents the formant-preserving side of the same algorithm family applied creatively rather than just transparently: "Formant-shifting and time-stretching vocal chops (e.g. in Serato Sample, Ableton's Warp modes) to create original-sounding hooks from source vocal material" — here the algorithm's formant control is used deliberately to change a vocal's character while keeping it intelligible, rather than purely to hide the stretch.

## Formant Preservation Specifically

Formant preservation is a specific feature within elastic/complex algorithms, not synonymous with the whole category: it keeps a voice's resonant timbral character (the vowel-shaping frequencies determined by vocal-tract size) stable even as pitch changes, so a vocal pitched up several semitones doesn't automatically sound smaller/younger ("chipmunked") the way simple resampling or a non-formant-aware pitch-shift would. `happy_hardcore.md`'s "formant-preserving or classic resampling" framing treats these as genuinely alternative choices with different results — formant-preserving pitch-shift for intelligibility at extreme pitch, classic resampling for a rougher, more overtly processed character — not one being simply a "better" version of the other.

## Grainy, Low-Fidelity Hardware Character as a Third Option

Per `sampling_and_resampling.md`'s existing grounding, early hardware sampler stretch algorithms (Akai S1000/S950-era) produce a distinctly grainy, lower-fidelity stretch character that jungle production specifically continues to seek out deliberately, and Ableton's own Simpler offers a comparable spectrum of playback-mode fidelity from clean to intentionally lower-quality. This sits alongside — not strictly below — the elastic and simple-resampling categories above: it's a deliberately chosen lower-fidelity option, not simply a technical limitation to be avoided by using a "better" mode. See `circuit_bent_and_hardware_sampler_texture.md` for the related bit-depth/sample-rate side of vintage hardware character.

## Choosing an Algorithm: A Practical Comparison

| Method | Time/pitch coupling | Formant behavior | Best for |
|---|---|---|---|
| Simple resampling | Linked (speed change = pitch change) | Shifts with pitch (no preservation) | Chopped-and-screwed effect, deliberately "sped up/slowed down" character (`happy_hardcore.md`) |
| Elastic/complex, formant-preserving | Independent | Preserved (vocal stays natural-sounding) | Extreme pitch-shifted vocal chops that must stay intelligible (`happy_hardcore.md`) |
| Elastic/complex, formant-shifting | Independent | Deliberately shifted for character | Creating original-sounding hooks from familiar vocal source material (`tech_house.md`) |
| Elastic/complex, transparent mode | Independent | Not a factor (non-vocal content) | Fitting a sample to a new tempo with minimal audible artifacting (`electro_swing.md`) |
| Grainy hardware-style algorithms | Typically linked or low-quality independent stretch | N/A | Deliberately embracing lo-fi, "broken" stretch texture (jungle, per `sampling_and_resampling.md`) |

## Common Mistakes

**Assuming "formant-preserving" and "elastic/complex" are the same setting.** Per `happy_hardcore.md`'s framing, formant preservation is a specific behavior within a capable algorithm — an elastic algorithm can still be set to shift formants deliberately (`tech_house.md`) rather than preserve them, so the choice needs to be made explicitly rather than assumed from the algorithm family alone.

**Using a transparent elastic algorithm when the classic-resampling character is actually the desired effect.** Chopped-and-screwed and happy hardcore's genre-signature pitched-up chops both depend on the linked time/pitch character simple resampling produces — a transparent elastic stretch that preserves pitch independent of tempo removes exactly the effect being sought.

**Defaulting to the highest-quality/most transparent algorithm setting regardless of genre.** `sampling_and_resampling.md`'s jungle grounding and this entry's grainy-hardware-character option both show that a lower-fidelity stretch is sometimes the deliberately correct choice, not a fallback for when better options aren't available.

## Cross-References

- `knowledge_base/sound_design/sampling/chopping_flipping_and_time_stretching.md` — the general pitch/time manipulation axes and chopped-and-screwed technique this entry's algorithm comparison supports.
- `knowledge_base/sound_design/sampling/sampling_and_resampling.md` — the original jungle/S1000 grainy-stretch grounding and DAW-level warp-mode workflow notes this entry builds on.
- `knowledge_base/sound_design/sampling/granular_resynthesis_vs_discrete_chopping.md` — the grain-level mechanics underlying elastic/complex time-stretch algorithms.
- `knowledge_base/sound_design/sampling/circuit_bent_and_hardware_sampler_texture.md` — the related bit-depth/sample-rate character of vintage hardware samplers, distinct from but often paired with grainy stretch character.
- `knowledge_base/genres/edm/happy_hardcore.md` — formant-preserving vs. classic resampling pitch-shift as an explicit genre-relevant algorithm choice.
- `knowledge_base/genres/electronic/electro_swing.md` — elastic audio/warp modes used for transparent, minimal-artifact tempo-fitting.
- `knowledge_base/genres/edm/tech_house.md` — formant-shifting time-stretch used creatively to generate original vocal-chop hooks.
