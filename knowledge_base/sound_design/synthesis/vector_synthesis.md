---
title: "Vector Synthesis"
synthesis_method: "vector-synthesis"
tags:
  - "vector-synthesis"
  - "prophet-vs"
  - "joystick-morphing"
  - "cross-fade"
  - "wavestation"
  - "4-source-blend"
---

## What Vector Synthesis Is

Vector synthesis structures a sound around real-time, continuous cross-fading between multiple (conventionally four) independent sound sources, positioned conceptually at the four extreme points of an X/Y plane — commonly labeled A, B, C, and D at north, east, south, and west. A control source, most iconically a physical joystick, sets a position anywhere within that plane, and the synth continuously blends the four sources' relative volumes according to the joystick's X/Y coordinates: pushed toward one corner, that source dominates; centered, all four blend evenly; moved along an edge, the synth crossfades between just the two sources at that edge's endpoints. Moving the joystick in real time, or recording its motion as an automated "vector envelope," turns a static four-layer patch into a continuously morphing composite timbre — the sound literally moves through the sound-source space over the note's duration.

## History: The Prophet VS

Vector synthesis was introduced by Sequential Circuits' **Prophet VS**, released in 1986 — the first synthesizer to use vector synthesis, built around a joystick arranged in a diamond pattern for oscillator mixing. Each of the Prophet VS's voices mixed four 12-bit digital single-cycle waves, fed into analog CEM3379/3389 chips for filtering and amplification — a hybrid digital-oscillator, analog-filter architecture, with the four-source joystick blend as its defining innovation. Sequential Circuits folded only a year after the Prophet VS's release, but the vector-synthesis concept proved influential well beyond the instrument's short production run: Yamaha adopted a related four-source joystick-morphing approach in the SY22 and TG33, and Korg's **Wavestation** (1990) extended the idea further by combining vector-style four-source blending with wavetable-style "vector sequencing" — automating the joystick position to move through a programmed path over time, turning the crossfade itself into a rhythmic, sequenced compositional element rather than just a static performance control.

## How Vector Synthesis Differs From Wavetable Morphing

Vector synthesis and wavetable morphing (`wavetable_morphing_techniques.md`) both involve continuous movement between stored sound material, but the structure differs: wavetable morphing scans linearly through an ordered sequence of single-cycle waveform frames along one axis (position), while vector synthesis crossfades between up to four *independent, potentially unrelated* sound sources across a two-dimensional plane. A wavetable's frames are typically designed as a single coherent timbral progression; vector synthesis's four sources can be four entirely different oscillator types, samples, or waveforms with no inherent relationship, blended by X/Y position rather than scanned in sequence — this makes vector synthesis better suited to combining genuinely disparate timbral characters (a clean tone, a noisy tone, a metallic tone, a bass tone, say) under one continuous performance control, where wavetable morphing is better suited to smooth evolution within one coherent timbral family.

## Where Vector Synthesis Appears in the Genre Corpus

Vector synthesis by name does not turn up in the current `knowledge_base/genres/` corpus — it is a historically narrow technique (a roughly two-year commercial window for the Prophet VS itself, though its influence persists through the Wavestation lineage and modern software recreations) rather than a broadly documented production staple. This is consistent with vector synthesis's real-world footprint: it never achieved the ubiquity of subtractive, FM, or wavetable synthesis, remaining a specialist, historically-specific technique best understood through its direct lineage (Prophet VS to Wavestation to modern vector-capable software instruments like Arturia's Prophet VS V and Korg's Wavestation software recreation) rather than assumed to be documented in any particular genre's production conventions. Genres that plausibly draw on vector-synthesis-adjacent multi-source blending and morphing character — synthwave and other 1980s-revival electronic genres documented elsewhere in this knowledge base, for instance — describe their synth palettes in terms of specific instruments (Juno, Jupiter, DX7) and general wavetable/virtual-analog technique rather than naming vector synthesis or the Prophet VS specifically, so treat this as a real documentation gap rather than an assumption to present as sourced genre fact.

## Practical Vector Synthesis Sound Design

- **Choose four genuinely distinct sources**: vector synthesis's value is in blending timbrally different material (e.g., a clean sine/triangle pad, a bright detuned saw, a noise/texture layer, and a metallic FM or bell tone) rather than four similar variations — the more distinct the four corners, the more dramatic and useful the morphing range.
- **Automate the vector path, not just static position**: the Wavestation's "vector sequencing" innovation — programming the X/Y position to move through a defined path over time rather than staying fixed or only responding to live joystick input — is the technique's most compositionally powerful extension, effectively turning a four-layer patch into its own miniature arrangement.
- **Use vector position as a performance-expression control**: assigning the X/Y position to a mod wheel, macro knob, or MPE-style continuous controller (rather than only a physical joystick) brings vector synthesis's real-time morphing into a modern MIDI workflow without dedicated hardware.
- **Modern access points**: Arturia's Prophet-VS V and Korg's Wavestation software recreation are the direct software lineage; several modern wavetable synths (Vital, Serum) can approximate vector-style four-source blending by assigning multiple oscillators to a 2D X/Y macro control even without dedicated vector-synthesis architecture.

## Cross-References

- `knowledge_base/sound_design/synthesis/wavetable_morphing_techniques.md` — the related but structurally distinct technique of linear scanning through an ordered frame sequence, versus vector synthesis's 2D four-source blend.
- `knowledge_base/sound_design/synthesis/fm_synthesis.md` — the contemporaneous mid-1980s digital synthesis lineage (DX7, 1983) vector synthesis (Prophet VS, 1986) emerged alongside, both part of the same wave of hybrid digital/analog instrument design.
- `knowledge_base/sound_design/synthesis/phase_distortion_synthesis.md` — another mid-1980s digital synthesis method (Casio CZ, 1984-85) from the same historical period, similarly under-documented in the current genre corpus relative to its historical significance.
