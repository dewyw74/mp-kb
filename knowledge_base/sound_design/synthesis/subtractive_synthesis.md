---
title: "Subtractive Synthesis"
synthesis_method: "subtractive"
tags:
  - "subtractive"
  - "oscillators"
  - "filters"
  - "envelopes"
  - "lfo"
  - "bass-design"
  - "lead-design"
  - "edm"
  - "analog"
  - "virtual-analog"
---

## What Subtractive Synthesis Is

Subtractive synthesis builds sound by generating a harmonically rich raw waveform and then *removing* (subtracting) frequency content from it with a filter, rather than building a tone up from scratch (as in additive or FM synthesis). It is the oldest and most intuitive electronic synthesis method — the architecture of the Minimoog, Roland Juno/Jupiter, and TB-303 — and remains the dominant sound-design approach for EDM bass and lead sounds because it maps directly onto physically intuitive controls (brightness, punch, movement) that are fast to program under time pressure.

The signal chain is linear and always flows in this order:

**Oscillator(s) → Filter → Amplifier**, with **Envelope Generators** and **LFOs** modulating the filter, amplifier, and/or oscillator pitch along the way.

1. **Oscillator stage** — generates one or more raw waveforms (saw, square, pulse, triangle, sine), each with a fixed, waveform-defined harmonic spectrum.
2. **Filter stage** — attenuates part of that spectrum (most commonly the highs), shaping tone and carving space in a mix.
3. **Amplifier stage** — controls the sound's volume over time, typically driven by an ADSR envelope.

Everything else in a subtractive patch — envelopes, LFOs, unison, effects — exists to make those three stages move and breathe instead of sitting static.

## Oscillator Waveforms and Harmonic Content

Each waveform has a fixed harmonic signature that determines what the filter has to work with:

- **Sawtooth** — contains all harmonics (fundamental + every integer multiple), amplitude falling off at roughly -6dB/octave. The brightest, most harmonically dense waveform; the default choice for EDM leads, basses, and stabs because a lowpass filter can carve almost any timbre out of it. Layering 2-7 detuned saws is the basis of the "supersaw" (see Unison/Detune below).
- **Square** — contains only odd harmonics (1st, 3rd, 5th...), giving a hollow, woody, "clarinet-like" tone. Common for basses that need to sit narrower in the spectrum than a saw, and for retro/8-bit leads.
- **Pulse** — a square wave with adjustable duty cycle (width) rather than fixed 50%. Narrowing the pulse width thins the harmonic content and produces a nasal, reedy character; modulating pulse width with a slow LFO (PWM) creates a chorus-like animated texture without adding a second voice — useful for basses and pads that need movement without stacking oscillators.
- **Triangle** — only odd harmonics like a square, but they fall off much faster (-12dB/octave vs square's -6dB), giving a soft, flute-like, nearly-sine tone with just a touch of edge. Useful as a sub-bass alternative to sine when a hint of harmonic content is wanted for translation on small speakers.
- **Sine** — the fundamental only, no harmonics. The standard choice for sub-bass (felt more than heard) and for kick-drum tone generation, since it adds low-end weight without competing for midrange space with anything else in the mix.

Most EDM basses layer a sine or triangle sub underneath a saw/square mid layer — the sub carries weight below roughly 80-100Hz where filtering and distortion would just make mud, and the upper layer carries the harmonic/timbral character that a filter and distortion can act on.

## Filter Types and Slopes

The filter is subtractive synthesis's defining stage — it's the "subtractive" in the name.

- **Lowpass (LP)** — passes frequencies below the cutoff, attenuates above it. The overwhelmingly dominant filter type in EDM sound design: it's what makes a bright saw sound warm, what creates the classic "filter opens on the build" riser effect, and what shapes the wobble in dubstep bass.
- **Highpass (HP)** — passes frequencies above the cutoff, attenuates below it. Used to thin out pads/leads in breakdowns, remove unwanted low-end rumble from non-bass elements, and automate elements "opening up" from thin to full during a build.
- **Bandpass (BP)** — passes a band around the cutoff, attenuating both above and below. Produces telephone/vowel-like, honky textures; useful for growl/formant-style dubstep bass and for making an element cut through a dense mix in a narrow frequency window.
- **Notch (band-reject)** — the inverse of bandpass; removes a narrow band while passing everything else. Less common melodically, more common for surgical resonance removal or phaser-like sweeping effects.

**Slope** describes how steeply the filter attenuates content past the cutoff, measured in dB per octave:

- **12dB/octave (2-pole)** — a gentler slope; more of the original harmonic content bleeds through above the cutoff, giving a smoother, more "vowel-y," less clinical sound. Classic Roland/Juno character.
- **24dB/octave (4-pole)** — a steeper slope (the Moog ladder-filter standard); much more decisive removal of content above cutoff, giving a punchier, more surgical, more modern EDM sound. Most contemporary EDM basses and leads default to 24dB for a tighter, more controlled low end.

Some synths (Diva, Serum) offer selectable slopes or emulate specific vintage filter circuits (Moog ladder, Oberheim SEM, Roland TB-303) — each has a distinct resonance and saturation character worth auditioning per sound.

## Resonance and Self-Oscillation

Resonance boosts the frequencies right at the cutoff point before they're attenuated, creating an emphasized peak. At low-to-moderate settings it adds character and "aggression" or "squelch" to a filter sweep — the acid-house TB-303 sound is essentially a saw/square oscillator through a resonant lowpass filter with the cutoff and resonance both under heavy modulation. At extreme settings, resonance becomes strong enough that the filter begins **self-oscillating** — generating an audible sine-like tone of its own even with no oscillator input — which can be tuned and played as a pure, filter-only sound source. In EDM practice, resonance is one of the primary "movement" parameters automated across a filter sweep in builds and risers: rising cutoff + moderate resonance is the standard riser recipe.

## Envelope Generators (ADSR)

An ADSR envelope generates a control signal over time in four stages, typically applied to the amplifier (shaping volume) and, separately, to the filter cutoff (shaping tone over time):

- **Attack** — time to reach full level from note-on. Fast attack (0-5ms) gives punchy, percussive plucks and basses; slow attack (100ms+) gives swells and pads that fade in.
- **Decay** — time to fall from the attack peak to the sustain level. Short decay on a bass or pluck creates the characteristic "thump then drop away" shape that leaves room for the next note.
- **Sustain** — the level held for as long as the note/key is held (not a time value). Zero sustain on a plucked bass or pluck lead means the sound is entirely shaped by attack+decay regardless of how long the note is held — critical for tight, rhythmic EDM basslines that need to stop dead before the next 16th note.
- **Release** — time to fall to silence after note-off. Short release avoids muddying fast basslines; longer release lets pads and leads tail off naturally into reverb.

A second (or third) envelope routed to filter cutoff — separate from the amplitude envelope — is what gives a subtractive bass or pluck its characteristic "pluck" transient: a fast-attack, short-decay envelope opening the filter briefly at the start of each note before it closes back down, producing the classic "wow" pitch-and-brightness pop heard on nearly every EDM pluck and many basses.

## LFO Modulation Targets

A Low-Frequency Oscillator (typically sub-20Hz, often tempo-synced in EDM) provides cyclical, ongoing modulation rather than the one-shot-per-note behavior of an envelope. Common EDM targets:

- **Filter cutoff** — the wobble-bass mechanism: an LFO (sine, triangle, or a custom/drawn shape) sweeping cutoff at a tempo-synced rate (1/4, 1/8, 1/16, triplet subdivisions) is the entire basis of dubstep and riddim wobble/growl bass, and is widely used more subtly on pads and leads for slow evolving movement.
- **Pitch** — vibrato when subtle; dramatic siren/growl effects when deep and fast, common in aggressive bass design (brostep, hardstyle screech leads).
- **Pulse width** (on pulse waveforms) — PWM chorus-like movement without extra voices.
- **Amplitude** — tremolo effects, rhythmic gating.
- **Pan** — auto-panning for width and movement on pads/plucks.

## Unison and Detune

Stacking multiple copies of an oscillator, each slightly detuned in pitch and spread across the stereo field, is the single most important width/thickness technique in EDM subtractive sound design — the "supersaw" popularized by the Roland JP-8000 and used throughout trance, big room house, and electro house leads and chords. Typical parameters:

- **Voice count**: 3-8 voices per note is standard; more voices thicken the sound but increase CPU load and can mush the transient.
- **Detune amount**: small values (a few cents) give subtle chorus-like thickening; larger values (10-30+ cents) give the wide, aggressive supersaw wash associated with trance/hardstyle/big-room leads.
- **Stereo spread**: voices panned across the stereo field (not just detuned) is what creates width rather than just beating/chorusing in mono — critical since the kick and bass typically stay centered/mono for club translation while leads and pads spread wide.
- **Trade-off**: heavy unison thickens a sound but reduces low-end mono-compatibility and definition; basses are usually kept to 1-2 voices (or unison disabled entirely) and summed to mono below ~100-150Hz, while leads, plucks, and pads carry the wide unison stacking.

## Subtractive Synthesis in EDM Sound Design

**Basses.** The core EDM bass design pattern is a sine/triangle sub layer (mono, minimal filtering, carries low-end weight) blended with a saw/square mid layer that a resonant lowpass filter and distortion/waveshaping act on for character and cut-through. Dubstep and riddim wobble/growl basses drive this further by putting the mid layer's filter cutoff under fast, tempo-synced LFO modulation — the wobble itself *is* the subtractive filter sweep. Reese-style bass (two detuned saws beating against each other, filtered and distorted) underlies drum & bass and much dark bass music.

**Leads.** Bright saw or detuned-saw-stack ("supersaw") oscillators through a resonant lowpass filter, often with a secondary filter envelope for movement and a fast LFO or pitch-bend for aggression, are the default EDM lead architecture — used across trance, big room house, electro house, and hardstyle (rawstyle screech leads push resonance and distortion further, often blending in FM/wavetable elements).

**Plucks.** Short amplitude envelope (fast attack, short decay, zero sustain) combined with a separate filter envelope of similar shape produces the characteristic "pop" pluck transient common in progressive house, melodic techno arpeggios, and trance/tech-house stabs; light unison (2-3 voices) adds body without blurring the transient.

**Kicks and percussion.** Sine oscillators pitch-modulated by a fast-decaying envelope (pitch drops from a few hundred Hz down to the fundamental in milliseconds) is the standard subtractive approach to synthesized kick drum design, often layered with sampled/synthesized transient click and distortion for punch.

## Recommended Synths

- **u-he Diva** — the reference standard for authentic vintage filter/oscillator emulation (Moog ladder, Oberheim SEM, Roland Juno/Jupiter models selectable per-module); CPU-heavy but the gold standard for warm, analog-accurate subtractive basses and leads.
- **Ableton Analog** — a lightweight, stock virtual-analog subtractive synth built into Live; excellent for fast sketching of classic two-oscillator subtractive patches (basses, leads, plucks) without leaving the DAW.
- **Xfer Serum** — primarily a wavetable synth, but its filter section (multiple selectable models including analog-modeled options) and basic-waveform oscillator options make it fully capable of standard subtractive patches; widely used across modern EDM specifically because wavetable and subtractive techniques can be combined in the same patch (e.g., a wavetable oscillator through an aggressively resonant subtractive-style filter for hybrid growl basses).
- **Vital** — a free/donation wavetable synth with a subtractive-style filter section (multiple filter models, including analog-modeled lowpass/highpass/bandpass/notch) comparable in flexibility to Serum; a strong no-cost option for learning filter/envelope/LFO subtractive fundamentals.
- **Roland TB-303 hardware/emulations** (e.g., Audiorealism ABL3, TAL-U-No-LX for Juno-style) — for acid house/acid techno-specific resonant filter squelch.

## Cross-References

- `knowledge_base/genres/edm/dubstep.md` — wobble/growl bass built entirely on LFO-modulated resonant lowpass filtering, the clearest single-genre case study for subtractive filter modulation.
- `knowledge_base/genres/edm/techno.md` — analog and virtual-analog subtractive synthesis (TB-303/SH-101/Juno/Jupiter-style) for basses, stabs, and percussion.
- `knowledge_base/genres/edm/trance.md` — virtual-analog subtractive supersaw leads (JP-8000-style detuned sawtooth stacks) as the genre's defining melodic sound.
- `knowledge_base/genres/edm/hardstyle.md` — subtractive lead design and filter-swept, pitch-enveloped kick synthesis.
- `knowledge_base/genres/edm/melodic_techno.md` — subtractive arpeggios and basslines layered with wavetable/FM pads for evolving texture.
