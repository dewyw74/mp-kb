---
title: "Arp and Sequence Patch Design"
synthesis_method:
  - "Subtractive"
  - "Wavetable"
tags:
  - "arpeggio"
  - "sequence"
  - "patch-design"
  - "trance"
  - "melodic-techno"
  - "sound-design"
---

# Arp and Sequence Patch Design

Arpeggiator and step-sequencer *pattern* programming (note order, gate length, octave range) is documented in `knowledge_base/midi/patterns/melody_and_arpeggio_pattern_programming.md`. This entry covers the separate discipline of designing the *synth patch itself* so it sounds good when arpeggiated — envelope shape, voice mode, and articulation choices that matter specifically because the same patch will play many fast, short, repeated notes rather than sustained chords or a single legato melody.

## What Makes a Patch "Arp-Ready"

1. **Fast, clean amplitude envelope**: a near-instant attack and a decay/release short enough that each stepped note has finished (or nearly finished) sounding before the next one triggers, so individual notes stay articulate rather than smearing into an indistinct wash. If the arpeggiator's step rate is fast, an envelope release longer than the step interval causes audible note-stacking that muddies the pattern rather than reinforcing it.
2. **Voice/glide mode**: polyphonic mode with no glide is standard for a clearly articulated arp where every note should read as a distinct event; monophonic mode with a short glide/portamento time can be used deliberately for a smoother, more "performed" arp line, but this is a specific stylistic choice, not a default.
3. **Filter envelope retrigger per step**: many arp-ready patches retrigger a filter envelope on every step (rather than leaving the filter static), so each note gets its own brief brightness "pop" — this is the same filter-envelope-plus-fast-decay mechanism documented in `knowledge_base/sound_design/presets/pluck_lead_design.md`, applied specifically to a sequenced/arpeggiated context.
4. **Waveform brightness**: because arp notes are heard individually and quickly rather than sustained, a brighter, more harmonically present oscillator (sawtooth, or a wavetable frame with more upper harmonic content) reads more clearly at speed than a rounder, darker tone that needs sustain time to be perceived fully.
5. **Velocity response**: since arpeggiators frequently vary step velocity for accent patterns, the patch's amp and filter envelopes should respond meaningfully to velocity — a patch with velocity mapped only to volume (not filter brightness) loses the accented, "alive" quality velocity-varied arp patterns are designed to produce.

## Genre Grounding

- `knowledge_base/genres/electronic/synth_pop.md` documents "driving 8th or 16th-note sequenced [bass] patterns, often arpeggiated across a I-V or root-fifth-octave shape; locked tightly to the grid to lean into the sequenced, machine-driven aesthetic" — a patch built for tight, mechanical articulation rather than expressive legato movement.
- `knowledge_base/genres/edm/trance.md` documents builds using "a rapidly arpeggiated synth line" as a tension-accumulation device, requiring a patch bright and articulate enough to read clearly at speed over 8-16 bars.
- `knowledge_base/genres/edm/melodic_techno.md` (per `knowledge_base/sound_design/presets/supersaw_lead_design.md`'s plucky-arp-lead archetype) treats the "arpeggiator/sequencer itself... as the primary melodic device," with the patch sitting "between a hard pluck and a legato pad" — a moderate-attack, subdued articulation deliberately less percussive than a trance arp, showing how the same arp-readiness principles scale from mechanically tight to atmospherically subdued depending on genre.
- `knowledge_base/genres/world_music/zouk.md` documents "bright plucked/arpeggiated synth lines" as a defining textural element, built from sawtooth/square oscillators for clarity at the genre's danceable tempo.
- `knowledge_base/genres/r_and_b/disco.md` documents late-1970s "Euro-disco" (Giorgio Moroder) "pioneer[ing] the heavy use of arpeggiated Moog synthesizers" — an early, foundational example of a monophonic analog patch designed specifically for arpeggiated sequencer performance.

## Common Mistakes

**Reusing a sustained pad or lead patch unmodified for an arpeggiated part.** A patch designed for legato sustain (slow attack, long release) turns into an indistinct wash when arpeggiated at speed — arp-readiness requires deliberately redesigning the envelope, not just feeding an existing patch into an arpeggiator.

**Ignoring velocity mapping.** An arp pattern programmed with deliberate velocity accents (per `knowledge_base/midi/patterns/melody_and_arpeggio_pattern_programming.md`) is wasted on a patch that doesn't translate velocity into audible timbral or dynamic variation.

## Cross-References

- `knowledge_base/midi/patterns/melody_and_arpeggio_pattern_programming.md` — arpeggiator/sequencer pattern programming (note order, gate length, octave range) this entry's patch-design guidance supports.
- `knowledge_base/sound_design/presets/pluck_lead_design.md` — the fast-envelope, filter-pop mechanism shared with arp-ready patch design.
- `knowledge_base/sound_design/presets/supersaw_lead_design.md` — melodic techno's plucky-arp-lead archetype, a genre-specific application of arp-readiness principles.
- `knowledge_base/genres/electronic/synth_pop.md`, `knowledge_base/genres/edm/trance.md`, `knowledge_base/genres/edm/melodic_techno.md`, `knowledge_base/genres/world_music/zouk.md`, `knowledge_base/genres/r_and_b/disco.md` — genre sources grounding this entry.
