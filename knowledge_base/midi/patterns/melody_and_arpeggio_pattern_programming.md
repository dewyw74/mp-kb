---
technique_name: Melody and Arpeggio Pattern Programming
category: patterns
problem_solved: "Choosing melodic density and development style — short repeated loops vs. developing phrases vs. block-harmonized ensemble writing — to match a genre's function for the melodic part"
genre_applicability:
  - trap
  - drill
  - progressive_trance
  - modal_jazz
  - swing
  - jazz_fusion
  - lo_fi_hip_hop
related_techniques:
  - bass_and_808_pattern_programming
  - drum_pattern_programming
  - humanization_and_groove_timing
tags: ["melody", "arpeggio", "midi-programming", "patterns", "call-and-response"]
---

# Melody and Arpeggio Pattern Programming

Melodic MIDI parts across this knowledge base fall into two broad functions: a short, repeated atmospheric loop that stays out of the vocal or lead's way, or a developing melodic line that carries the track's primary interest. Genre determines which one to program, and mixing the two up produces melodies that either compete with a vocal that needs space, or feel too static for a genre that expects development.

## Minimal, Repeated Loops as Atmosphere

Trap and drill treat melody as a stable backdrop rather than a featured part. `trap.md`: "Short, dark, repeated melodic loops (often just 2-4 notes) provide a stable, moody harmonic bed beneath dense vocal rhythmic activity." `drill.md` uses nearly identical language: "Minimal, dark, repeated melodic phrases (often just 2-3 notes) provide atmosphere without competing with the 808/vocal rhythmic focus." `lo_fi_hip_hop.md` applies the same restraint for a different reason — sustained listenability rather than vocal space: "Short, repeated, jazz-harmony-informed melodic loops with subtle variation over time, designed for extended, non-intrusive listening." In all three cases, the note count staying low (2-4 notes) is the actual technique — the loop's job is harmonic/atmospheric bed, not melodic statement.

## Repeating Motif Plus Timbral Automation

`progressive_trance.md` documents a distinct middle-ground approach: keep the note pattern short and repetitive, but generate interest by automating the sound rather than writing new melodic material. "Short, repeating motifs rather than long developing melodic phrases; interest comes from filter and timbral automation applied to a repeating pattern rather than new melodic material." The instrument list backs this up: "Filtered pads, subtle plucks, and short arpeggiated motifs rather than wide supersaw leads; timbral evolution (filter sweeps, unison width changes) substitutes for melodic development." This is a genuinely different technique from trap's minimal loop — the note pattern itself may not change for many bars, but the arrangement still needs to feel like it's developing, so that development gets encoded as CC/automation data (filter cutoff, unison detune) layered on top of the static MIDI pattern.

## Scalar, Space-Driven Development

`modal_jazz.md` documents the opposite extreme from trap's tight repetition — melody built from open scalar motion with deliberate space between phrases: "Sketch improvised lines using scalar/modal motion (stepwise Dorian or Mixolydian runs) with long note values and space between phrases rather than dense sixteenth-note bebop runs; motivic repetition and development read as more idiomatic than constant new material." The key programming instruction is the contrast with bebop density — modal jazz specifically avoids the "dense sixteenth-note run" approach in favor of longer note values and more rest.

## Block-Harmonized Ensemble Writing

`swing.md` documents a melodic programming technique specific to big-band arranging rather than a single melodic line at all: "Sketch horn-section melodies as harmonized block chords moving in parallel motion (typical of big-band brass/reed writing); use call-and-response between a 'brass' MIDI channel and a 'reed' MIDI channel to capture the antiphonal arranging style." This means the "melody" is programmed across multiple MIDI channels/tracks simultaneously, each doubling the same line a third or sixth apart, rather than as a single monophonic part. `jazz_fusion.md` describes a related unison technique used for a different effect — tightness and power rather than harmonic richness: "Sketch tight unison lines (guitar/synth/horn doubling) with angular intervallic leaps and syncopated rhythmic placement."

## Common Mistakes

**Writing a developing melodic line where the genre calls for a static loop.** Trap and drill's 2-4 note loops exist specifically to stay out of the vocal's way — a melodically active lead competes for the same rhythmic/attention space the vocal needs.

**Mistaking progressive trance's static pattern for a lack of development.** The motif genuinely doesn't change much, but the automation (filter, unison width) carries the arrangement's sense of movement — skipping that automation while keeping the repetitive MIDI pattern produces a genuinely static, undeveloping section.

**Programming modal jazz melody with bebop-density note values.** `modal_jazz.md` explicitly contrasts its long-note, spacious phrasing against "dense sixteenth-note bebop runs" — using bebop's note density defeats the genre's characteristic floating, open feel.

## Cross-References

- `knowledge_base/genres/hiphop/trap.md`, `knowledge_base/genres/hiphop/drill.md`, `knowledge_base/genres/hiphop/lo_fi_hip_hop.md` — short, repeated melodic loops as atmospheric bed
- `knowledge_base/genres/edm/progressive_trance.md` — repeating motif with development carried by automation, not new notes
- `knowledge_base/genres/jazz/modal_jazz.md` — scalar, space-driven melodic development contrasted with bebop density
- `knowledge_base/genres/jazz/swing.md` — block-harmonized, multi-channel call-and-response ensemble writing
- `knowledge_base/genres/jazz/jazz_fusion.md` — tight unison doubling across instrument channels
- `knowledge_base/midi/patterns/bass_and_808_pattern_programming.md` — the complementary role of an intentionally simple bass under an active melody, or vice versa
