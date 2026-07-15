---
workflow_name: "FL Studio Chord, Arpeggiator, and Scale Helper Tools"
daw: "fl_studio"
category: "midi"
goal: "Use FL Studio's Piano Roll Chord Stamp tool, Chord Panel, Scale Highlighting, and both the Channel-level and Piano Roll-level Arpeggiator to generate harmonic ideas quickly, then print (convert/flatten) the result into standard editable Piano Roll notes for further hand-editing."
steps:
  - "Set the project's key/scale and enable Piano Roll menu > Helpers > Scale Highlighting so every stamped or typed note can be checked against the target scale before it's committed."
  - "Select the Stamp tool in the Piano Roll toolbar, choose a chord stamp (major, minor, diminished, augmented, 7th, 9th, 11th, 13th, sus2, sus4, add9, and similar), and click into the Piano Roll to place chords, using top-down (melody-led) or bottom-up (harmony-led) voice-leading mode depending on whether a melody note or the chord root should drive the voicing."
  - "Use the toolbar's Chord Panel to detect and audition chords in real time from MIDI input, the typing keyboard, or an existing note selection before committing a progression to the Piano Roll."
  - "Apply the Piano Roll's own Arpeggiator (Piano roll menu > Arpeggiate, or Alt+A) to a set of stamped chord notes, choosing an arpeggio score/pattern — this writes fully editable, hard-coded notes directly into the Piano Roll rather than a live-only performance effect, making it the fastest 'print' path for an arpeggiated idea."
  - "For quick real-time auditioning instead, open a Channel's Miscellaneous settings and use its built-in Arpeggiator (Direction, Range, Time, Gate, Chord) to hear an arpeggiated pattern live while composing, without committing to notes yet."
  - "Because the Channel-level Arpeggiator is a real-time performance effect and does not leave editable note data behind, flatten a chosen pattern into notes by recording a live pass into the Piano Roll with the arp running, or via Edison's 'Convert to score and dump to piano roll' function."
  - "Hand-edit the printed notes once they exist as standard Piano Roll data — adjust voicings, add or remove passing tones, and set velocity and timing per `knowledge_base/midi/programming/velocity_editing_and_dynamics.md` and `knowledge_base/midi/programming/humanization_and_groove_timing.md`."
  - "Cross-check chosen voicings against `knowledge_base/music_theory/chords/extended_jazz_chords.md` when a richer, jazz-informed harmonic color is the goal rather than plain triads."
  - "Save a useful chord/arp result as a reusable Piano Roll score or Channel preset rather than rebuilding the same idea from scratch in later projects."
related_plugins:
  - "FL Studio Piano Roll"
  - "FL Studio Chord Stamp Tool"
  - "FL Studio Chord Panel"
  - "FL Studio Piano Roll Arpeggiator"
  - "FL Studio Channel Arpeggiator"
  - "FL Studio Scale Highlighting"
  - "Edison"
tags:
  - "fl-studio"
  - "midi"
  - "chords"
  - "arpeggiator"
  - "scale-helper"
  - "piano-roll"
  - "workflow"
---

# FL Studio Chord, Arpeggiator, and Scale Helper Tools

FL Studio splits chord and arpeggio generation across several distinct tools rather than one unified device, and the practical distinction that matters most is which of them produce live, real-time performance data versus which write permanent, editable notes directly into the Piano Roll. This entry covers the Piano Roll's Stamp tool, Chord Panel, and Scale Highlighting for fast harmonic idea generation, the Channel-level and Piano Roll-level Arpeggiators for turning a chord into a moving pattern, and the workflow for "printing" whichever version was only a live effect into standard notes that can be hand-edited afterward.

## Scale Highlighting as a guardrail, not a lock

Piano Roll menu > Helpers > Scale Highlighting colors in-key notes once a root and scale are set, giving a visual guide while stamping or typing notes without physically restricting input the way a hard scale-lock would. Set this before reaching for the Stamp tool or Chord Panel so every chord placed afterward is visibly checked against the target key as it goes in, rather than requiring a separate pass to catch out-of-key notes later.

## The Chord Stamp tool

The Stamp tool in the Piano Roll toolbar places a full chord voicing with a single click, from a library that covers major, minor, diminished, augmented, and extended qualities (7th, 9th, 11th, 13th) plus common alterations (sus2, sus4, add9). Two voice-leading modes change how the stamped chord is built around the clicked note: top-down mode treats the clicked note as part of the chord built underneath it, letting a melody note lead the voicing, while bottom-up mode is harmony-driven, with FL Studio choosing the chord shape based on where the click lands. Combined with Scale Highlighting, stamped chords land in-key by default and can be dragged to adjust voicing afterward exactly like any other Piano Roll note.

## The Chord Panel for real-time detection

The Chord Panel, accessible from the Piano Roll toolbar, detects and names chords in real time from MIDI input, the computer's typing keyboard, or a selection of existing notes. This is the fastest way to audition several chord options against a melody or a held drone before committing anything — play or select candidate voicings and read back what the panel identifies rather than working out chord names by ear or by counting intervals manually.

## Two different Arpeggiators, two different outputs

FL Studio's Channel-level Arpeggiator (in a Channel's Miscellaneous settings, available on every instrument channel including VST/AU plugins) is a real-time performance effect: Direction sets the arp's traversal pattern (up, down, up-down, and a randomized option), Range sets how many octaves it spans, Time sets speed, Gate sets note length, and Chord can trigger a full chord or scale shape from a single held note. It's the fastest way to hear an arpeggiated idea while composing, but it does not leave behind editable note data — it only changes what's heard on playback.

The Piano Roll's own Arpeggiator (Piano roll menu > Arpeggiate, or Alt+A) works differently: applied to a selection of stamped or typed chord notes, it hard-codes the resulting arpeggio directly into the Piano Roll as standard, individually editable notes. Because it writes real notes rather than performing a live effect, it's the more direct "print" path when the goal is an arpeggiated pattern that needs further hand-editing.

## Printing a Channel-level arp into editable notes

When a live Channel Arpeggiator pattern is the one worth keeping, it still needs to become real notes before it can be hand-edited. The two working approaches are recording a live pass into the Piano Roll while the arp plays (capturing the arp's output as a standard MIDI recording), or using Edison's "Convert to score and dump to piano roll" function on a recorded audio/MIDI capture of the arpeggiated output. Either way, the goal is the same: move from a parameter-driven live effect to static notes that can be freely edited, reordered, or partially deleted.

## Hand-editing after printing

Once a chord or arp idea exists as printed notes — whether from the Stamp tool, the Piano Roll Arpeggiator, or a flattened Channel-arp recording — treat it as ordinary Piano Roll data. Adjust individual voicings, thin out or add passing tones, and set velocity and timing per `knowledge_base/midi/programming/velocity_editing_and_dynamics.md` and `knowledge_base/midi/programming/humanization_and_groove_timing.md`, since printed arp/chord output typically arrives with uniform velocity and machine-perfect timing that benefits from the same humanization pass any other programmed part would get.

## Common mistakes

Treating the Channel-level Arpeggiator as if it were already editable note data, then being unable to make a precise voicing change without disabling it and starting the pattern over — flatten it into notes first. Skipping Scale Highlighting and stamping chords freehand, producing voicings that need to be manually corrected note-by-note afterward instead of landing in-key on the first pass. Leaving a printed arpeggio at uniform velocity and grid-perfect timing when the part calls for a more human feel, rather than running it through the same humanization pass any other programmed part would get.

## Cross-references

- `knowledge_base/music_theory/chords/extended_jazz_chords.md` — extended voicing vocabulary (7ths, 9ths, 11ths, 13ths) relevant when choosing stamp qualities for a richer harmonic color
- `knowledge_base/midi/patterns/chord_and_stab_pattern_programming.md` and `knowledge_base/midi/patterns/melody_and_arpeggio_pattern_programming.md` — genre-level guidance on how dense or sparse the printed result should actually be
- `knowledge_base/midi/programming/humanization_and_groove_timing.md` — the humanization pass printed arp/chord notes typically need
- `knowledge_base/daw/fl_studio/groove_and_humanization_workflow.md` — FL Studio-specific mechanics for the same humanization step
