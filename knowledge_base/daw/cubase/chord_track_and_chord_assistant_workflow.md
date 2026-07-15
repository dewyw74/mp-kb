---
workflow_name: "Cubase Chord Track and Chord Assistant Workflow"
daw: "cubase"
category: "harmony"
goal: "Compose and reharmonize harmony-first in Cubase using the Chord Track, Chord Assistant, and Chord Pads — sketching and auditioning progressions before instrumental parts exist, and driving other tracks' harmony from a single source of truth."
steps:
  - "Add a Chord Track (Project > Add Track > Chord) near the top of the project so it's visible as the harmonic reference for the rest of the arrangement."
  - "Enter chords directly on the Chord Track by drawing chord events and setting root, type, and (optionally) bass note/tension per event, sketching a progression before any instrument part is recorded."
  - "Open the Chord Assistant and use its Circle of Fifths view to audition chords related to a chosen origin chord — clicking a chord plays it, and the three most recently clicked chords are shown in bold for quick comparison."
  - "Assign promising Chord Assistant suggestions to Chord Pads directly from the assistant (right-click > Assign to First Unassigned Pad, or double-click) rather than manually rebuilding each chord in the pad grid."
  - "Play Chord Pads live from a MIDI controller or the on-screen pad grid to perform a progression in real time, using them as a harmony-sketching instrument rather than only a fixed data source."
  - "Set a Chord Voicing Style per player (Piano Player, Guitar Player, and other available player types each carry their own voicing library) so pad playback reflects how that instrument type would actually voice the chord, rather than one generic voicing for every instrument."
  - "Enable Adaptive Voicing when triggering chord changes from the pads so Cubase favors the smallest pitch movement between consecutive chords, approximating how a competent player would voice-lead rather than jumping to the nearest root-position shape every time."
  - "Record-enable instrument tracks set to follow the Chord Track so each track's player-specific voicing responds to the same chord data, letting one Chord Track drive harmonically consistent parts across multiple instruments."
  - "Edit chord events on the Chord Track directly once a progression is set (changing root, type, or voicing per event) to reharmonize the whole arrangement from one place instead of re-editing every dependent instrument part by hand."
  - "Treat the Chord Track as a compositional sketchpad, not just a passive analysis layer — build a progression there first, audition it against Chord Pads and player voicings, and only then commit to fully performed or programmed parts once the harmony is settled."
related_plugins:
  - "Cubase Chord Track"
  - "Cubase Chord Pads"
  - "Cubase Chord Assistant"
  - "HALion Sonic"
tags:
  - "cubase"
  - "harmony"
  - "chord-track"
  - "chord-pads"
  - "chord-assistant"
  - "voicing"
  - "composition"
  - "reharmonization"
---

# Cubase Chord Track and Chord Assistant Workflow

The Chord Track, Chord Pads, and Chord Assistant form Cubase's harmony-first composition toolchain — a way to sketch, audition, and reharmonize progressions before committing to fully performed instrument parts. Rather than working out a chord progression note-by-note in a piano roll, this workflow treats harmony as its own editable layer that other tracks can be made to follow, which is particularly useful for fast idea generation, exploring reharmonizations, and keeping a multi-instrument arrangement harmonically consistent from one source of truth.

## Chord Track: harmony as its own layer

The Chord Track (Project > Add Track > Chord) holds chord events — root, chord type, and optional bass note or tension — independent of any specific instrument's MIDI data. Chords can be drawn directly on the track to sketch a progression before any part exists, giving a harmonic skeleton the rest of the arrangement can be built against. Editing a chord event later changes the harmonic context for anything following the Chord Track, which is what makes reharmonization fast: change the chord once on the track rather than re-editing every dependent instrument part by hand.

## Chord Assistant: guided reharmonization

The Chord Assistant surfaces chord suggestions related to a chosen origin chord through a Circle of Fifths view. Clicking a suggested chord plays it immediately, and the three most recently auditioned chords are shown in bold, making it fast to compare several reharmonization options against the current progression by ear rather than by music-theory lookup alone. Suggestions can be assigned straight onto an unassigned Chord Pad via right-click, so a promising chord found through the assistant becomes immediately playable rather than needing to be rebuilt manually.

## Chord Pads: performing harmony

Chord Pads present a grid of assignable chords that can be triggered live from a MIDI controller or the on-screen grid, turning harmony into something played rather than only entered as data. Each pad's playback goes through a Chord Voicing Style tied to a specific player type (Piano Player and Guitar Player are the documented player types with their own voicing libraries), so the same underlying chord is voiced the way that instrument would actually play it — a guitarist's chord shapes differ meaningfully from a pianist's spread voicings, and the pad system reflects that rather than outputting one generic voicing regardless of instrument.

## Adaptive Voicing

When Adaptive Voicing is active, triggering a chord change from the pads makes Cubase favor the smallest pitch movement needed to move from the previous chord to the new one, rather than jumping to a fixed root-position voicing every time. This approximates the voice-leading instinct of a competent player moving between chords smoothly, and is worth enabling by default for pad-performed progressions where jarring register jumps between chords would otherwise be distracting.

## Driving other tracks from the Chord Track

Instrument tracks can be set to follow the Chord Track, so record-enabling a track and playing its assigned player/voicing responds to the same chord data the Chord Track holds. This is the mechanism that lets one harmonic sketch drive multiple instruments consistently — a bass part, a pad part, and a comping guitar part can all reference the same Chord Track and stay harmonically aligned even as the progression is edited.

## Common mistakes

Building a progression note-by-note directly in each instrument's piano roll instead of sketching it on the Chord Track first, which makes later reharmonization require editing every part individually rather than one shared source. Leaving every pad on a generic or default voicing instead of setting a Chord Voicing Style appropriate to the instrument being auditioned, producing pad playback that doesn't represent how the part will actually sound once performed on its real instrument. Ignoring Adaptive Voicing for pad-performed progressions and getting large, unmusical register jumps between consecutive chords.

Related reading: `knowledge_base/music_theory/chords/extended_jazz_chords.md` and `knowledge_base/music_theory/chords/quartal_harmony_and_fourths_voicings.md` for the underlying harmonic vocabulary a Chord Track progression might draw from, and `knowledge_base/daw/workflow/midi_chord_and_scale_constraint_philosophy.md` for the cross-DAW philosophy of constraining MIDI input to a chosen harmony that this Cubase-specific tool implements.
