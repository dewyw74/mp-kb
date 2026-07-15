---
title: "String Machine Emulation Design"
synthesis_method:
  - "Subtractive (ensemble/chorus circuit)"
tags:
  - "string-machine"
  - "solina"
  - "ensemble"
  - "analog-strings"
  - "sound-design"
  - "new-wave"
---

# String Machine Emulation Design

A string machine (ARP Solina/String Ensemble, Roland RS/VP series, and similar late-1970s/early-1980s instruments) produces a distinctive analog "orchestral strings" character that is mechanically different from either a modern detuned-unison pad or a sampled orchestral string patch — the difference lives specifically in the ensemble/chorus circuit these instruments used, not just in oscillator choice.

## Building the Sound

1. **Oscillator source**: sawtooth (or a sawtooth-derived divide-down waveform, as the original hardware used organ-style top-octave-divider circuits rather than true polyphonic VCOs) is the standard starting waveform — bright and harmonically rich enough for the ensemble circuit to have material to work with.
2. **The ensemble/chorus circuit (the defining element)**: rather than stacking multiple detuned oscillator voices per note (the modern supersaw/unison approach), classic string machines run a single oscillator per note through a bucket-brigade-device-based ensemble/chorus circuit — several slightly delayed, independently modulated copies of the signal are summed together, producing a shimmering, slowly phasing width that is subtly different in character from oscillator-level unison detune. Modern emulation plugins (or a BBD-style chorus effect applied to a simple saw pad) reproduce this by running a plain, undetuned sawtooth pad through a multi-voice chorus/ensemble effect rather than detuning the oscillators themselves.
3. **Envelope**: a slow attack (strings "swelling" in) and a sustained, even level — no fast filter-envelope movement or percussive articulation; the instrument's identity is sustained harmonic pad content, not rhythmic interest.
4. **Minimal or no filter movement**: unlike a modern evolving pad, a string-machine patch typically keeps the filter static or only gently moving — the ensemble circuit itself provides all the perceived "movement" needed.

## Genre Grounding

- `knowledge_base/genres/electronic/coldwave.md` documents "Roland Jupiter-4/6, Korg Polysix, ARP Solina/String Ensemble, Yamaha CS-15" as core instruments "for pads and stabs," with string-machine pads standing in for orchestral strings entirely (no live orchestration typical of the genre).
- `knowledge_base/genres/electronic/synth_pop.md` documents "string machine or sampled/synthesized string pads for emotional lift in choruses and bridges," used in place of live orchestration.
- `knowledge_base/genres/electronic/new_wave.md` documents string machine pads providing "a light orchestral wash in bridges or choruses."
- `knowledge_base/genres/rock/soft_rock.md` documents "string-machine synths (Solina, ARP String Ensemble) and simple analog pads for warm orchestral-adjacent texture" as a defining production element.
- `knowledge_base/genres/rock/glam_rock.md` documents "string machine or real strings for dramatic chorus lifts," paired with piano glissando flourishes.
- `knowledge_base/genres/rock/dream_pop.md` documents "Roland Juno, Yamaha DX7 pad patches, string machines" as a core textural element, "frequently blended with or indistinguishable from heavily processed guitar."
- `knowledge_base/genres/edm/detroit_techno.md` documents "string-machine/ensemble synths (Roland RS/VP, Solina-style)" directly by name as part of the genre's synth palette.
- `knowledge_base/genres/edm/jungle.md` documents "string machine pads" as part of a sparse instrumental palette alongside stabbing sampled brass hits.

## Common Mistakes

**Substituting oscillator-level unison detune for the ensemble/chorus circuit.** A detuned-unison saw pad and a string-machine ensemble-chorused pad can sound superficially similar but are mechanically different — the BBD-chorus character (subtle pitch/time modulation on delayed copies) has a distinctive shimmer that plain detune doesn't reproduce; use a dedicated ensemble/chorus effect, not just wider unison.

**Adding fast filter-envelope movement to a string-machine patch.** This instrument family's identity is sustained, evenly-voiced pad content — percussive articulation or fast filter sweeps immediately break the vintage-ensemble character being emulated.

## Cross-References

- `knowledge_base/sound_design/presets/pad_design_archetypes_and_patch_recipes.md` — the modern detuned-unison pad archetypes this entry's ensemble-circuit technique is mechanically distinct from.
- `knowledge_base/sound_design/synthesis/subtractive_synthesis.md` — general unison/detune and oscillator fundamentals this entry's ensemble-circuit approach diverges from.
- `knowledge_base/genres/electronic/coldwave.md`, `knowledge_base/genres/electronic/synth_pop.md`, `knowledge_base/genres/electronic/new_wave.md`, `knowledge_base/genres/rock/soft_rock.md`, `knowledge_base/genres/rock/glam_rock.md`, `knowledge_base/genres/rock/dream_pop.md`, `knowledge_base/genres/edm/detroit_techno.md`, `knowledge_base/genres/edm/jungle.md` — genre sources grounding this entry.
