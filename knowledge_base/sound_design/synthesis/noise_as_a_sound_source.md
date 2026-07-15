---
title: "Noise as a Sound Source"
synthesis_method: "noise-oscillator"
tags:
  - "noise-oscillator"
  - "white-noise"
  - "pink-noise"
  - "filtered-noise"
  - "noise-synthesis"
  - "percussion-synthesis"
---

## Noise as a Sound Source, Not Just an Effect

This file covers noise generators used as a primary or contributing **oscillator** in a synth patch — a sound-generation source that a filter, envelope, and the rest of a synthesis chain shapes into a finished tone — as distinct from noise used as a mix-stage *effect* (vinyl crackle, tape hiss, riser sweeps layered for atmosphere over an otherwise-finished mix, which belong more to production/mixing technique than synthesis). The distinction matters because a noise oscillator inside a synth voice is typically shaped by the same envelope, filter, and modulation chain as any other oscillator in that patch — it's a raw material for synthesis, not a decorative layer added afterward.

## White Noise vs. Pink Noise vs. Filtered Noise

- **White noise** contains equal energy at every frequency across the audible spectrum, perceived as bright and hissy since the ear's sensitivity and the frequency spacing of octaves both weight higher frequencies more heavily in equal-Hz-width noise. It's the standard starting point for a noise oscillator before any filtering.
- **Pink noise** has equal energy per *octave* rather than per Hz, rolling off at roughly -3dB/octave relative to white noise — this matches the ear's natural perception more closely and sounds notably darker, warmer, and less harsh than white noise at the source, before any filtering is applied.
- **Filtered noise** — white or pink noise passed through a resonant filter (see `filter_type_comparison.md`) — is how most practical noise-oscillator sound design actually happens: a bandpass or lowpass filter carves the raw noise down to a specific frequency region, and modulating that filter's cutoff over time (an envelope, an LFO) shapes the noise into anything from a percussive hi-hat transient to a slowly evolving atmospheric texture.

## Noise for Percussion Synthesis

Because noise contains energy across the full spectrum with no fixed pitch, it's the standard raw material for synthesizing unpitched or semi-pitched percussion — hi-hats, cymbals, snares, claps — where a filtered/enveloped noise burst substitutes for (or layers with) a sampled drum hit. `knowledge_base/genres/edm/techno.md` documents "White/pink noise (percussion, hats, texture)" directly among its oscillator/sound sources, and `knowledge_base/genres/edm/speedcore.md`, `knowledge_base/genres/edm/gabber.md`, and `knowledge_base/genres/edm/industrial_techno.md` all similarly document white/pink noise used for risers, texture, and percussion body. `knowledge_base/genres/edm/goa_trance.md` documents "Resonant filtered noise for percussion/FX texture" specifically, naming the filtered-noise-as-percussion-source technique directly.

## Noise as a Structural/Textural Synth Voice

Beyond percussion, several genres document noise functioning as a genuine melodic-adjacent or textural synth voice in its own right, not merely a transient or effect:

- **Minimal techno** — `knowledge_base/genres/edm/minimal_techno.md` documents a track built from "a single filtered noise loop, a subtly modulated drone, or a tiny repeating percussive blip" as its core synth texture, and its intro section is described as beginning with "a filtered noise loop — looping for an extended period (32-64+ bars) before anything else enters," treating filtered noise as a legitimate, sustained lead voice rather than a supporting texture.
- **Ambient** — `knowledge_base/genres/electronic/ambient.md` documents builds that are "additive, not dynamic-driven: new layers (a second pad, a filtered noise bed, a granular texture) enter roughly every 30-60 seconds," using filtered noise as one of several equal-weight textural layers in the arrangement.
- **Noise music** — `knowledge_base/genres/electronic/noise_music.md` uses noise as its entire sonic foundation rather than a contributing element: "Sub-bass and low-frequency noise mass (rumble, filtered noise) provide physical weight, generated from noise sources and heavily distorted signal chains rather than a bass instrument or synth part," with guitars and keys, when present, used "purely as a feedback/noise source" or "only as a drone/noise source." The genre file also documents "Granular and spectral (FFT) processing of noise sources" for evolving textures beyond what static filtered noise alone reaches, and "Circuit-bent and homemade electronic instruments" as a source of DIY, non-standardized noise generation true to the genre's roots.
- **Industrial and power electronics** — `knowledge_base/genres/electronic/industrial.md` documents "Noise (white/pink)" directly among its core oscillator types (alongside sawtooth and ring-modulated tones), and `knowledge_base/genres/electronic/power_electronics.md` documents "Analog noise/tone generators" and "Feedback circuits (audio and homemade)" as its primary synth-type palette — noise here functions as the genre's actual lead instrument, not a texture layered under other elements.
- **Bass and lead texture in bass-heavy electronic genres** — `knowledge_base/genres/hiphop/industrial_hip_hop.md` documents "Noise oscillators for texture" and `knowledge_base/genres/electronic/deconstructed_club.md` documents "Noise sources shaped into aggressive percussive hits," and `knowledge_base/genres/electronic/idm.md` documents "noise sources shaped into pitched material" — the last a particularly notable technique, since it describes filtering/shaping noise tightly enough (narrow bandpass, resonant filtering near self-oscillation) to produce a perceivable pitch from an inherently unpitched source.

## Practical Noise Sound Design

- **Choose white vs. pink deliberately as a starting tonal-balance decision**: white noise for bright hi-hat/cymbal synthesis or aggressive risers, pink noise for warmer, darker textural beds and atmospheric layers.
- **Filter type matters as much as noise color**: a narrow bandpass filter on noise (especially pushed toward self-oscillation/high resonance, per `filter_type_comparison.md`) can extract a semi-pitched tone from noise, the mechanism behind `idm.md`'s "noise sources shaped into pitched material."
- **Envelope shape defines the percussive character**: a very fast attack and short decay on filtered noise produces a hi-hat/snap transient; a slow attack and long decay produces a riser or swell; a sustained/looping envelope (minimal_techno.md's filtered noise loop) turns noise into a genuine background texture layer.
- **Combine with granular/spectral processing for evolving noise textures**: `noise_music.md`'s citation of granular and FFT processing of noise sources is directly relevant beyond noise music itself — any genre wanting continuously evolving atmospheric noise beds (dark ambient, drone, cinematic sci-fi textures) benefits from the same granular-on-noise approach (see `granular_synthesis.md`).

## Cross-References

- `knowledge_base/sound_design/synthesis/filter_type_comparison.md` — the filtering techniques (bandpass, resonant, comb) most directly responsible for shaping raw noise into a usable tone.
- `knowledge_base/sound_design/synthesis/granular_synthesis.md` — granular processing of noise sources for evolving textures, per `noise_music.md`.
- `knowledge_base/genres/edm/minimal_techno.md` — filtered noise loop as a primary, sustained synth voice.
- `knowledge_base/genres/electronic/noise_music.md`, `knowledge_base/genres/electronic/industrial.md`, `knowledge_base/genres/electronic/power_electronics.md` — noise as the primary sound source rather than a contributing texture.
- `knowledge_base/genres/electronic/idm.md` — noise shaped into pitched material via tight resonant filtering.
- `knowledge_base/genres/edm/goa_trance.md`, `knowledge_base/genres/edm/techno.md` — filtered noise for percussion synthesis.
