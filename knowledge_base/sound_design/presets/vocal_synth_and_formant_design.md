---
title: "Vocal Synth and Formant Design"
synthesis_method:
  - "Vocoder (carrier/modulator)"
  - "Formant filtering"
  - "Subtractive"
tags:
  - "vocoder"
  - "formant"
  - "talk-box"
  - "vocal-synthesis"
  - "sound-design"
---

# Vocal Synth and Formant Design

This entry covers building vocal-like synth tones through two related but mechanically distinct techniques: vocoding (imposing a real voice's spectral envelope onto a synth carrier) and formant filtering (shaping a synth's frequency content to mimic the resonant peaks of the human vocal tract without any live voice input at all). Both produce the "talking synth" or "vowel-morphing" character documented across electro, dubstep, and electroclash production.

## Building the Sound

1. **Vocoder mechanics**: a vocoder analyzes an input "modulator" signal (typically a spoken or sung vocal) across a bank of frequency bands, measures the amplitude in each band, and applies that same band-by-band amplitude envelope to a separate "carrier" signal (typically a harmonically rich synth — sawtooth or pulse waves work best, since they provide energy across many bands for the vocoder to shape). The result is a synth tone that "speaks" the modulator's words and prosody while retaining the carrier's pitch and timbre. `knowledge_base/genres/electronic/electro.md` documents this mechanism directly: "Vocoders process a vocal or synth 'modulator' signal through a synth 'carrier' signal to produce the robotic vocal sound."
2. **Formant filtering without a live modulator**: rather than analyzing a real voice, a formant filter uses a fixed or automated set of bandpass filters tuned to the resonant frequencies characteristic of vowel sounds (roughly 300-1000 Hz, 800-2500 Hz, and 2000-3500 Hz for the first three formants). Automating the filter frequencies to sweep between vowel positions (e.g., "ah" to "oo") produces a vowel-morphing effect on a synth voice with no vocal input at all — this is the mechanism behind formant-filtered growl bass documented in `knowledge_base/genres/edm/dubstep.md` and `knowledge_base/genres/edm/brostep.md`.
3. **Talk box (a physical, not digital, variant)**: a talk box routes a synth or guitar signal through a tube directly into a performer's mouth, using the performer's own vocal tract as a live, manually-controlled formant filter — producing an effect `knowledge_base/genres/r_and_b/electro_funk.md` describes as more expressive than any LFO, since it's shaped by real-time mouth articulation rather than automation.
4. **Carrier/source choice matters**: a bright, harmonically dense carrier (sawtooth, pulse, or a synth bass tone) gives a vocoder or formant filter more spectral material to shape into intelligible vowel content; a pure sine wave carrier produces a much weaker, less articulate vocal effect.

## Genre Grounding

- `knowledge_base/genres/electronic/electro.md` documents the Roland VP-330 as an "era-defining" vocoder unit turning spoken/rapped vocals into the genre's "characteristic robotic textures," used sparingly and rhythmically rather than as a full melodic vocal replacement.
- `knowledge_base/genres/r_and_b/electro_funk.md` documents the talk box (Electro-Harmonix Golden Throat) as "the genre's defining instrument," routing a Minimoog or Yamaha DX100 FM synth signal through a tube into the performer's mouth, functioning "as the lead vocalist" rather than a novelty effect.
- `knowledge_base/genres/electronic/electroclash.md` documents vocoders and pitch-shifters used "for ironic or confrontational vocal effect rather than polished robotic smoothness," a deliberately imperfect, "cheap electronics as punk statement" application distinct from electro's more functional robotic-vocal use.
- `knowledge_base/genres/edm/dubstep.md` and `knowledge_base/genres/edm/brostep.md` both document "bandpass/formant filtering for vowel-like growl bass movement" as a core wobble-bass sound-design technique — formant filtering applied to a bass patch rather than a vocal-replacement lead.
- `knowledge_base/genres/edm/colour_bass.md` names "formant filtering/vowel morphing" as "the genre's core sound-design signature, moving a patch between vowel-like melodic tones and growled aggression," with formant automation as the genre's primary expressive automation lane.
- `knowledge_base/genres/electronic/future_funk.md` documents "talkbox/vocoder textures pulled from or emulating disco-era synth work," referencing the Zapp/Roger Troutman funk-era lineage of the technique.

## Common Mistakes

**Using a pure sine or triangle carrier for a vocoder and expecting clear vowel articulation.** Vocoders need a harmonically rich carrier to have enough spectral material across all analysis bands to reproduce intelligible formant shapes.

**Confusing vocoding (requires a live modulator signal) with formant filtering (does not).** They produce related but mechanically different results — a formant-filtered bass patch has no "words," only vowel-like timbral movement, while a vocoder genuinely imposes another signal's spoken/sung content.

## Cross-References

- `knowledge_base/sound_design/presets/growl_and_wobble_bass_design.md` — wavetable-position modulation, a related but distinct movement mechanism often layered alongside formant filtering in growl bass.
- `knowledge_base/sound_design/synthesis/fm_synthesis.md` — FM's role in the metallic carrier tones common in vocoder/formant-filtered bass and lead patches.
- `knowledge_base/genres/electronic/electro.md`, `knowledge_base/genres/r_and_b/electro_funk.md`, `knowledge_base/genres/electronic/electroclash.md`, `knowledge_base/genres/edm/dubstep.md`, `knowledge_base/genres/edm/brostep.md`, `knowledge_base/genres/edm/colour_bass.md`, `knowledge_base/genres/electronic/future_funk.md` — genre sources grounding this entry.
