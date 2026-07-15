---
workflow_name: "Studio One Chord Track and ARA Melodyne Integration"
daw: "studio_one"
category: "harmony"
goal: "Use Studio One's Chord Track to drive harmony-first composition across MIDI and audio, and use Studio One's native ARA integration with Melodyne to edit pitch and timing inside the DAW without bouncing or rendering audio first."
steps:
  - "Add a Chord Track above the arrangement and either draw chords by hand with the pencil tool or drag an existing Keys/MIDI clip onto it so Studio One detects the chords automatically."
  - "Enable Follow Chords in the Inspector on each track that should transpose when the Chord Track changes, since Follow Chords is opt-in per track, not global."
  - "Write or arrange the Chord Track first when composing harmony-first, then build basslines, pads, and comping parts as MIDI parts that follow it."
  - "Use the Chord Track's Nashville Number / Roman numeral display when transposing a section to a new key so the harmonic function stays visible independent of the actual pitches."
  - "Treat Chord Track transformation of audio clips as a prototyping tool, not a final-take tool — PreSonus documents extreme chord-driven audio transposition as capable of producing audible artifacts."
  - "For vocal or monophonic instrument pitch editing, double-click the audio event to insert Melodyne via ARA directly on the event rather than loading Melodyne as a channel insert."
  - "Let Melodyne analyze the audio and edit pitch, timing, formant, and (on polyphonic material) individual notes within the ARA-hosted view, with all edits and referenced audio saved inside the Studio One Song file."
  - "Use Melodyne's algorithm choice (Melodic, Percussive, Universal, Polyphonic — see `knowledge_base/vst_database/celemony_melodyne.md`) appropriate to the source material for accurate note detection."
  - "Keep ARA-based Melodyne edits non-destructive during comping and arrangement passes; only render/bounce once pitch and timing edits are finalized."
  - "Cross-check Melodyne-corrected vocal or lead lines against the Chord Track when Follow Chords is active, since a Melodyne pitch edit changes the note independent of chord-track transposition logic."
related_plugins:
  - "Studio One Chord Track"
  - "Celemony Melodyne (ARA) — see `knowledge_base/vst_database/celemony_melodyne.md`"
  - "Studio One Harmonic Editing"
tags:
  - "studio_one"
  - "chord-track"
  - "ara"
  - "melodyne"
  - "harmony"
  - "pitch-editing"
  - "composition"
---

# Studio One Chord Track and ARA Melodyne Integration

Studio One has two harmony-adjacent features that are genuine differentiators for the DAW: the Chord Track, a project-wide harmonic reference that MIDI and audio tracks can follow, and native ARA integration with Celemony Melodyne, which lets Melodyne edit audio in place on an event rather than as an external round-trip process. Both are documented, current Studio One features (not third-party add-ons), and both change how harmony and pitch editing fit into the arrangement workflow compared to a DAW without them.

## What the Chord Track actually does

The Chord Track analyzes MIDI and audio content dragged onto it and displays the detected chords as a timeline of chord symbols running alongside the arrangement. Chords can also be drawn directly with the pencil tool, or extracted from an existing MIDI or audio part. Individual tracks do not follow the Chord Track automatically — each track has a Follow Chords option in the Inspector that must be enabled per track, which is what lets a producer keep some parts locked to their original notes (a fixed bass hook, a sample) while other parts (pads, comping guitar, harmony fills) transpose automatically when the Chord Track changes.

Because Follow Chords rewrites notes relative to the Chord Track rather than baking a transposition permanently into the clip, the whole system is non-destructive: switching the Chord Track off returns every following clip to its original notes.

## Harmony-first composition workflow

Writing the Chord Track before the parts that follow it inverts the usual "record parts, then figure out the harmony" order. A songwriter can block out a full harmonic structure — verse chords, chorus chords, a key change into the bridge — before a single note of bass, pad, or comping part exists, then build or drag in MIDI content that automatically conforms. This is a genuinely different composition path from building harmony bottom-up out of recorded or programmed parts, and it pairs naturally with the KB's general chord-progression material in `knowledge_base/music_theory/harmony/` and `knowledge_base/music_theory/chords/` — the Chord Track is a DAW-native place to audition those progressions against real arrangement material before committing.

## Audio and the Chord Track — a documented limit

Studio One's Chord Track can also affect audio tracks through Harmonic Editing, including polyphonic audio, not just MIDI. PreSonus documentation frames this audio-side capability as best suited to prototyping — sketching how a chord change might sound against an existing recording — because pushing audio through extreme chord transformations can introduce audible artifacts. Treat Chord-Track-driven audio transposition as an idea tool, not a mix-ready processing chain.

## ARA and native Melodyne integration

Audio Random Access (ARA) is the technology, jointly developed by Celemony and PreSonus, that lets Melodyne exchange detailed audio analysis data with the host DAW instead of operating as an opaque plugin. Studio One was the first DAW to ship ARA support, alongside Melodyne's own ARA-enabled versions, in 2011. When Melodyne is inserted via ARA — by double-clicking an audio event and choosing Melodyne rather than loading it as a channel-strip insert — it behaves like an alternative to the sample editor or piano roll: editing happens directly on the event in place, with no bounce, render, or external round-trip required before pitch and timing changes can be heard and refined. All audio data Melodyne needs is stored inside the Studio One Song project itself, so ARA edits travel with the session on save and archive without special handling.

Loading Melodyne as a plain channel-strip insert instead of via ARA skips this integration entirely — it functions as an ordinary real-time effect with none of the in-place, note-level editing. The ARA path is what makes Melodyne's DNA (Direct Note Access) editing and multitrack note editing (see `knowledge_base/vst_database/celemony_melodyne.md`) usable without breaking arrangement flow.

## Common mistakes

Forgetting to enable Follow Chords on a track and then wondering why it did not transpose with a Chord Track change is the most common Chord Track mistake — the feature is per-track and opt-in, not global. A related mistake is applying large chord-track transformations directly to finished vocal or lead audio and treating the result as final, when PreSonus's own guidance frames that use case as prototyping only. On the Melodyne side, the recurring mistake is inserting Melodyne as a normal channel insert instead of via ARA (double-click on the event), which silently loses the in-place, non-destructive, note-level editing that is the actual reason to reach for Melodyne inside Studio One rather than round-tripping to a separate audio editor.

## Cross-references

- `knowledge_base/vst_database/celemony_melodyne.md` — Melodyne's DNA technology, algorithm choices, and its documented corrective role alongside Auto-Tune
- `knowledge_base/music_theory/harmony/` — chord function, cadences, and modal interchange material to compose against the Chord Track
- `knowledge_base/music_theory/chords/` — extended and quartal chord voicings that can be drawn directly into the Chord Track
