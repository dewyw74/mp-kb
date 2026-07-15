---
plugin_name: "Melodyne"
developer: "Celemony"
category: "pitch correction"
type: "graphical, audio-to-MIDI-style pitch and time editor"
cpu_usage: "medium"
best_genres:
  - country_pop
  - contemporary_country
  - pop
  - choral_music
  - trap_soul
strengths:
  - "DNA (Direct Note Access) lets individual notes be edited within polyphonic material — chords on a piano or guitar, or a full mix — not just monophonic vocal or instrument lines, which no real-time pitch corrector can do."
  - "Presents pitch as an editable, note-by-note 'blob' display resembling a piano roll rather than a real-time-knob interface, making it a fundamentally visual, after-the-fact editing workflow rather than a performance effect."
  - "Separate Melodic, Percussive, Universal, and Polyphonic algorithms are each tuned to a different source type (sung/spoken monophonic material, drums/percussion, general mixed content, and chords/polyphonic instruments respectively), improving detection accuracy over a one-size-fits-all pitch tracker."
  - "Multitrack Note Editing and correction/timing/level macros let a producer apply consistent pitch and timing fixes across many tracks (e.g., a full harmony stack) from a single editing window rather than processing each take in isolation."
weaknesses:
  - "The graphical, note-by-note editing workflow is inherently slower than a real-time knob-based corrector — it isn't suited to fixing pitch on the fly during tracking or live performance the way Auto-Tune's Auto Mode is."
  - "Higher CPU and workflow overhead than a lightweight real-time corrector, since Melodyne must analyze and render a detailed pitch/time model of the audio before editing becomes possible, rather than processing in a continuous real-time stream."
alternatives:
  - "Antares Auto-Tune Pro (real-time, knob-driven correction and the deliberately audible hard-tune effect — see `knowledge_base/vst_database/antares_auto_tune_pro.md`)"
  - "iZotope Nectar (bundles Melodyne Essential alongside its own real-time pitch correction module — see `knowledge_base/vst_database/izotope_nectar.md`)"
  - "Waves Tune"
recommended_settings:
  - "Corrective-only pop/country vocal polish: Melodic algorithm, correct pitch center note-by-note toward the nearest scale tone while leaving each note's original pitch drift/vibrato curve intact, per `contemporary_country.md`'s documented two-stage chain: \"Use Melodyne for precise pitch correction, followed by Auto-Tune for absolute polish.\""
  - "Choral/group-vocal or harmony-stack cleanup: Multitrack Note Editing across all stacked takes at once, using the correction macros to apply consistent tuning across the full harmony stack rather than editing each take separately."
  - "Chord/harmonic reshaping on a polyphonic instrument sample or recorded guitar/piano part: Polyphonic algorithm with DNA, transposing individual notes within the chord rather than pitch-shifting the whole chord uniformly."
common_uses:
  - "Precise, note-by-note corrective pitch editing on a lead vocal, positioned as a first-pass fix before a stylistic pass with Auto-Tune"
  - "DNA-based editing of individual notes within polyphonic/chordal material that a monophonic real-time corrector can't address"
  - "Multitrack timing and pitch cleanup across a full harmony/backing-vocal stack from one editing window"
tags: ["celemony", "melodyne", "pitch-correction", "dna", "vocal-processing", "audio-to-midi"]
---

# Melodyne

Melodyne (Celemony) is the other major pitch-correction tool this knowledge base's genre corpus names alongside Auto-Tune, but it solves the same underlying problem — a vocal or instrument note sitting off pitch — with a fundamentally different workflow. Where Auto-Tune Pro's Auto Mode is a real-time, knob-driven processor built for tracking and live use, Melodyne presents recorded audio as an editable, note-by-note graphical display resembling a piano roll or MIDI editor, and lets each note's pitch, timing, formant, and (with DNA) even its position within a chord be adjusted individually after the fact. Celemony's DNA (Direct Note Access) technology, which won a Technical Grammy, is the plugin's defining capability: it can isolate and edit individual notes inside genuinely polyphonic material — a piano chord, a guitar strum, a full mix — not just a single monophonic voice or instrument line.

## The Corrective, Precision-Editing Counterpart to Auto-Tune's Real-Time Effect

`knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md` documents Melodyne consistently on the transparent/corrective side of the pitch-correction split, distinct from Auto-Tune's dual corrective-or-stylized role. `country_pop.md` names both tools together but implies distinct roles: "Melodyne and Auto-Tune used flawlessly to create perfectly pitched pop vocals." `contemporary_country.md` is the most explicit about the two-stage sequence this implies: "Vocal perfection is required. Use Melodyne for precise pitch correction, followed by Auto-Tune for absolute polish." Per `knowledge_base/mixing/vocal_processing/vocal_chain_signal_order.md`'s reading of this same citation, the ordering is deliberate — Melodyne's precise, note-by-note graphical correction happens first as a foundational fix, with Auto-Tune's faster, effect-oriented pass applied afterward, rather than the two tools being interchangeable or redundant. This reflects the genuine difference in what each tool is built for: Melodyne is an editing environment for getting pitch exactly right note by note, not a real-time performance effect.

## Sound Character and Strengths

Melodyne's "blob" display turns each detected note into an editable graphical object showing pitch, pitch drift, formant, and amplitude simultaneously, which makes it possible to correct a note's center pitch while choosing exactly how much of its natural vibrato or scoop to preserve — a level of individual-note control a real-time corrector's global Retune Speed/Flex-Tune settings can't replicate. DNA extends this same note-by-note editing into polyphonic material: a single note inside a recorded guitar or piano chord, or even within a stereo mix, can be isolated and retuned or time-shifted without re-recording, something no monophonic real-time pitch tracker (including Auto-Tune's standard algorithms) can do at all. The four source-specific algorithms (Melodic, Percussive, Universal, Polyphonic) mean Melodyne's pitch/time detection is tuned to what's actually being analyzed rather than applying one generic detection model to everything from a solo vocal to a full mix.

## Weaknesses

Melodyne's analysis-then-edit workflow is not a real-time effect — audio has to be processed into its internal pitch/time model before any editing can happen, and the editing itself is a deliberate, visual, note-by-note process rather than a fast knob turn. This makes it a poor fit for tracking or live use, where Auto-Tune Pro's Auto Mode is the appropriate tool, and it carries meaningfully more CPU and workflow overhead per vocal take than a lightweight real-time corrector.

## Common Mistakes

Reaching for Melodyne when the actual goal is Auto-Tune's audible hard-tune effect (or the reverse) — per `pitch_correction_philosophy.md`, these are documented as genuinely different roles in the genre corpus, not interchangeable tools for the same job. Trying to use Melodyne as a real-time tracking-stage corrector, when its analysis-based workflow is built for precise after-the-fact editing rather than a live signal chain.

## Cross-References

- `knowledge_base/mixing/vocal_processing/pitch_correction_philosophy.md` — the transparent-vs-stylized framework distinguishing Melodyne's corrective role from Auto-Tune's dual role
- `knowledge_base/mixing/vocal_processing/vocal_chain_signal_order.md` — the documented Melodyne-then-Auto-Tune sequencing in `contemporary_country.md`
- `knowledge_base/mixing/vocal_processing/doubling_and_harmony_stacking.md` — Multitrack Note Editing's use case for cleaning pitch/timing across a full harmony stack at once
- `knowledge_base/genres/country/country_pop.md`, `knowledge_base/genres/country/contemporary_country.md` — the primary genre citations for Melodyne's corrective, "flawless"-pitch use case
- `knowledge_base/vst_database/antares_auto_tune_pro.md` — the real-time, knob-driven counterpart, frequently used in sequence with Melodyne rather than as a substitute for it
- `knowledge_base/vst_database/izotope_nectar.md` — bundles a Melodyne Essential license as its included pitch-correction engine
