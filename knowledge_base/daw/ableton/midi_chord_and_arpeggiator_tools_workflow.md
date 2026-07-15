---
workflow_name: "Ableton Chord, Arpeggiator, and Scale MIDI Tools Workflow"
daw: "ableton"
category: "midi"
goal: "Chain Ableton's Chord and Arpeggiator MIDI effect devices (with an optional Scale device to lock output to a key) inside a MIDI Effect Rack to generate harmonic ideas quickly from single held notes, then print the generated result to a real, editable MIDI clip for further hand-editing."
steps:
  - "Insert a MIDI Effect Rack on the target MIDI track, then add Chord as the first chain device and Arpeggiator as the second, so every incoming note is first turned into a chord and the arpeggiator then breaks that chord apart rhythmically."
  - "Program up to six Chord shifts — each a semitone offset from -36 to +36 with its own relative velocity — to build the target voicing, e.g. +4 and +7 for a major triad or +3 and +7 for minor, instead of manually stacking chord notes in the piano roll."
  - "Add a Scale device either before Chord (to constrain raw input notes to the track's key) or after Arpeggiator (to correct any out-of-key notes the chord shifts introduced), choosing one of Scale's built-in scales or defining a custom one."
  - "Set Arpeggiator's Style (Up, Down, Up/Down, Chord Trigger, Random, Random Other, Random Once, and others) and Rate — synced to a tempo-relative beat division or free-running in milliseconds — to match the target rhythmic pattern, auditioning several styles against the track's tempo before settling on one."
  - "Play single held notes or simple root-motion progressions into the chain and audition the generated harmonic and rhythmic result in real time, using the rack as a fast harmonic-idea generator rather than programming finished chord voicings by hand first."
  - "Once a result sounds right, create a new MIDI track and set its input to 'MIDI From' the original track, choosing the Post FX input option so the track receives the Chord/Arpeggiator/Scale chain's processed output rather than the raw notes."
  - "Arm the new track to record, play back (or re-play) the original held notes, and record a pass — this prints the live-generated chord and arpeggio notes into a standalone, ordinary MIDI clip rather than leaving the result dependent on the live device chain."
  - "Hand-edit the printed clip's note timing, velocity, and pitch in the piano roll — adjusting micro-timing, removing a repeated note, or adding a passing tone — since raw device output is a strong starting point, not a finished part."
  - "Mute or remove the original MIDI Effect Rack chain once the printed clip is confirmed correct, so the track no longer depends on live device processing for playback."
  - "Save a useful Chord/Arpeggiator/Scale combination as a MIDI Effect Rack in the User Library (per `knowledge_base/daw/ableton/racks_macros_and_performance_controls.md`) with macros mapped to the most-adjusted parameters, for reuse as a fast harmonic-idea starting point in future sessions."
related_plugins:
  - "Ableton Chord"
  - "Ableton Arpeggiator"
  - "Ableton Scale"
  - "Ableton MIDI Effect Rack"
tags:
  - "ableton"
  - "midi"
  - "chord-device"
  - "arpeggiator"
  - "scale-device"
  - "harmony"
  - "printing-midi"
  - "midi-effects"
---

# Ableton Chord, Arpeggiator, and Scale MIDI Tools Workflow

Ableton's Chord, Arpeggiator, and Scale MIDI effect devices turn a single held note into a full harmonic and rhythmic idea before a single note gets hand-programmed. Chained together in a MIDI Effect Rack, they're a fast way to generate chord voicings and arpeggiated patterns for further editing rather than a replacement for `knowledge_base/midi/patterns/chord_and_stab_pattern_programming.md` and `knowledge_base/midi/patterns/melody_and_arpeggio_pattern_programming.md`'s hand-programming guidance — this workflow covers generating a first pass quickly, then printing it so it can be edited the same way any other MIDI clip would be.

## Chaining Chord Before Arpeggiator

Order matters: Chord assembles a chord from each incoming note plus up to six additional user-defined "shifts" (pitch offsets of 1-36 semitones, each with its own relative velocity), and Arpeggiator then creates a rhythmical pattern from whatever notes it receives. Placing Chord first means Arpeggiator receives a full chord to arpeggiate rather than a single note, producing the layered, moving harmonic texture associated with trance and progressive builds (per `knowledge_base/sound_design/presets/arp_and_sequence_patch_design.md`'s genre grounding) rather than a simple single-note arpeggio. Reversing the order — Arpeggiator first, Chord second — produces a different, denser result where each arpeggiated note is itself turned into a chord; both orders are valid starting points, but Chord-then-Arpeggiator is the more common default for a single evolving harmonic line.

## Locking Output to a Key with Scale

The Scale device constrains incoming MIDI notes to a chosen scale, remapping any out-of-scale note to the nearest in-scale pitch. Placed before the Chord/Arpeggiator chain, it keeps raw input notes honest to the track's key even when played imprecisely on a controller; placed after, it catches any out-of-key notes the Chord device's semitone shifts introduced. Choosing the right scale here connects directly to `knowledge_base/music_theory/scales/modes_in_popular_music.md` and the genre's documented `common_scales` field (natural minor and harmonic minor for trance, per `knowledge_base/genres/edm/trance.md`) — Scale is only as musically useful as the scale choice fed into it.

## Auditioning and Iterating Quickly

The point of this chain is speed: hold a single note or play a slow root-motion progression and let Chord, Arpeggiator, and Scale generate the harmonic and rhythmic detail live, auditioning different Arpeggiator styles (Up, Down, Chord Trigger, Random, Random Other, Random Once) and Rate settings against the track's tempo. This is a sketching tool — the goal is finding a voicing and rhythmic pattern that works, not producing a final, note-perfect part directly from the device chain.

## Printing the Result to a MIDI Clip

Once a result sounds right, it needs to be captured as real notes so it can be hand-edited and doesn't remain dependent on live device processing. Create a new MIDI track, set its input to the source track with the Post FX option selected (so it receives the processed output of the Chord/Arpeggiator/Scale chain rather than the unprocessed input notes), arm it, and record a pass. This prints the generated chord and arpeggio notes into an ordinary MIDI clip that behaves exactly like any hand-programmed part — editable in the piano roll, quantizable, and independent of the original device chain once the source rack is muted or removed.

## Hand-Editing After Printing

Treat the printed clip as a strong first draft. Adjust individual note timing for feel, thin out or add notes the generator produced too evenly, and vary velocity per `knowledge_base/midi/programming/velocity_editing_and_dynamics.md` where the raw output is too mechanically even. This hand-editing pass is where a device-generated idea becomes a finished, intentional part rather than an obviously algorithmic one.

## Common mistakes

Skipping the print/record step and leaving a part dependent on a live MIDI Effect Rack, which breaks the moment the rack is edited, moved, or disabled, and makes the part impossible to hand-edit note by note. Recording with the new track's input still set to receive raw input rather than Post FX, which captures the un-processed notes instead of the generated result. Never adjusting the printed clip afterward, leaving a part that sounds identifiably generated rather than musically shaped. Placing Scale after a Chord device whose shifts were specifically chosen for out-of-key color, which can strip out an intentional chromatic note the Chord device was set up to add.
