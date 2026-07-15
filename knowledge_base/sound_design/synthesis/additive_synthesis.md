---
title: "Additive Synthesis"
synthesis_method: "additive"
tags:
  - "additive"
  - "sine-partials"
  - "harmonic-series"
  - "drawbar-organ"
  - "hammond"
  - "spectral"
  - "partials"
  - "organ-synthesis"
---

## What Additive Synthesis Is

Additive synthesis builds a timbre from the bottom up: a bank of individual sine-wave oscillators — the **partials** — is summed together, with each partial's frequency, amplitude, and phase set independently. Where subtractive synthesis starts from a harmonically dense waveform and carves content away with a filter, additive synthesis starts from silence and adds exactly the harmonic content the sound designer specifies, one sine wave at a time. It is, conceptually, the audio-rate application of Fourier's principle that any periodic waveform can be described as a sum of sine waves at the fundamental frequency and its integer multiples (harmonics) — additive synthesis simply runs that principle forward, constructing a waveform from a chosen harmonic recipe rather than analyzing one after the fact.

Because each partial is controlled independently, additive synthesis offers the most granular timbral control of any synthesis method — in principle, any static or slowly evolving spectrum is reachable — at the cost of being the most parameter-heavy: a rich, evolving tone can require independent envelopes on dozens of partials rather than the one or two envelopes a subtractive patch needs.

## The Hammond Organ: Additive Synthesis Before Synthesizers

The clearest and most historically important additive instrument predates the synthesizer entirely. Laurens Hammond's tonewheel organ, introduced in 1935, generated each pitch from a physically spinning metal tonewheel and electromagnetic pickup, then let the player mix the fundamental with eight fixed harmonic partials using sliding **drawbars** — pulling a drawbar out increases that partial's volume, directly analogous to raising a single sine oscillator's amplitude in a modern additive synth. The classic percussive "click" attack, Leslie rotating-speaker modulation, and the specific drawbar registrations associated with gospel, soul, and jazz organ playing are all additive synthesis techniques, just implemented mechanically and electromechanically rather than with software oscillators. `knowledge_base/genres/r_and_b/gospel.md` documents "the Hammond B3 Organ (with a Leslie rotating speaker)" as foundational to the genre, "played with extreme harmonic complexity" — a direct, still-current example of additive/drawbar synthesis as a working production tool rather than a historical curiosity.

## Spectral and Analysis-Resynthesis Approaches

A more modern, computationally intensive branch of additive synthesis derives its partial data from analysis of a real recorded sound (via FFT or similar spectral analysis) rather than a hand-set harmonic recipe, then resynthesizes or transforms that spectrum with banks of sine oscillators. `knowledge_base/genres/classical/spectral_music.md` documents this philosophy at the compositional level — treating "a 'sound' ... as a compositional object to be analyzed, decomposed into partials, and gradually reassembled or transformed," with instruments assigned to individual partials of an analyzed spectrum so the ensemble functions as a kind of live additive resynthesis engine (what the genre file calls "instrumental synthesis"). This is the same underlying idea as additive/spectral synthesis software (Reaktor's spectral tools, or dedicated resynthesis engines): decompose a sound into partials, then treat those partials as independently controllable material.

## Additive/Organ Synthesis in Drone and Ambient Contexts

`knowledge_base/genres/electronic/drone.md` lists "additive/organ synthesis" directly among its documented synth types, alongside physical modeling and granular synthesis, and specifically calls out "pipe organ or drawbar organ synths exploiting rich harmonic content" as a sustain-capable sound source well suited to the genre's demand for unbroken, evolving tone — additive/organ synthesis is favored here because a static or slowly shifting bank of harmonic partials can sustain indefinitely without the transient decay that would undercut drone's core aesthetic of continuous, unbroken sound. The same file notes the technique's harmonic output benefits from "harmonic/overtone EQ boosting to bring out specific partials" at the mixing stage — additive synthesis and EQ are working the same axis (individual harmonic balance), one at the synthesis stage and one after the fact.

## Additive Elements in Hybrid Textures

`knowledge_base/genres/cinematic/sci_fi_score.md` documents "granular and spectral synthesis for alien/otherworldly textures" alongside FM and analog-modeled pads — spectral synthesis (a close relative of additive synthesis, working from analyzed or synthesized partial data rather than a fixed oscillator waveform) contributes exactly the kind of inhuman, precisely-controlled evolving timbre that a filtered subtractive pad cannot easily reach, because its harmonic content is authored directly rather than shaped from a pre-existing spectrum.

## Practical Additive Sound Design

- **Building an organ-style patch**: set partials at simple integer harmonic ratios (1x, 2x, 3x, 4x...) matching a drawbar layout, and use fast percussive attack on the higher partials only (the Hammond's characteristic "click") for authentic touch response.
- **Building evolving pads/drones**: automate individual partial amplitudes on slow, independent envelopes or LFOs so the perceived timbre shifts continuously without ever repeating exactly — the technique `drone.md` and `ambient.md`-style genres rely on for long-form harmonic movement.
- **Inharmonic/bell-like additive patches**: detune partials away from strict integer ratios (the same principle FM uses via non-integer C:M ratios) for metallic, bell, or otherworldly timbres, useful for the "alien" sci-fi textures cited above.
- **CPU cost**: real additive synthesis with dozens of independently enveloped sine oscillators is CPU-expensive relative to a subtractive or wavetable oscillator; most modern "additive" synths (Native Instruments Razor, Camel Audio Alchemy's additive engine) manage this with resynthesis shortcuts or partial-count limits rather than true unlimited independent oscillator banks.

## Cross-References

- `knowledge_base/genres/r_and_b/gospel.md` — Hammond B3 drawbar organ as a working additive-synthesis instrument, foundational to the genre.
- `knowledge_base/genres/electronic/drone.md` — additive/organ synthesis and drawbar organ synths as a sustain-capable source for unbroken drone tone.
- `knowledge_base/genres/classical/spectral_music.md` — analysis-resynthesis philosophy of decomposing sound into partials, the compositional cousin of spectral/additive synthesis.
- `knowledge_base/genres/cinematic/sci_fi_score.md` — spectral synthesis for alien, otherworldly textures.
- `knowledge_base/sound_design/synthesis/subtractive_synthesis.md` — the structurally opposite approach: starting harmonically rich and removing content, versus additive's start-from-silence-and-add.
- `knowledge_base/sound_design/synthesis/fm_synthesis.md` — a different route to inharmonic/bell timbres (via modulation sidebands) compared to additive's direct authoring of inharmonic partials.
- `knowledge_base/sound_design/synthesis/granular_synthesis.md` — another way of building evolving, spectrally rich texture from many small sound units rather than sine partials.
