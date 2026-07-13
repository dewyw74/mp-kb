---
technique_name: Humanization and Groove Timing (Piano-Roll Implementation)
category: programming
problem_solved: "Translating a genre's swing/groove requirement into concrete piano-roll settings — swing percentage, millisecond timing offsets, and which parts stay quantized versus which get micro-timing looseness"
genre_applicability:
  - french_house
  - progressive_trance
  - speedcore
  - modal_jazz
  - jazz_fusion
  - swing
  - jungle
related_techniques:
  - drum_pattern_programming
  - velocity_editing_and_dynamics
  - bass_and_808_pattern_programming
tags: ["humanization", "swing", "quantization", "groove-template", "midi-programming", "micro-timing"]
---

# Humanization and Groove Timing (Piano-Roll Implementation)

`knowledge_base/music_theory/rhythm/swing_and_quantization_feel.md` documents *why* genres choose rigid quantization or loose human timing as an aesthetic decision. This entry covers the complementary *how*: the concrete piano-roll numbers — swing percentages, millisecond offsets, and which parts get touched at all — that genre files specify for actually implementing that decision.

## Named Swing Percentages

Several genre files give an exact swing-quantization range rather than a vague "add some swing" instruction. `french_house.md`: "quantized tightly but often programmed with a swing percentage (54-58%) borrowed from the source disco breaks," with the drum programming instructions repeating the range as "swing quantization (55-60%)" when programming new parts from scratch to match sampled material. `swing.md` gives a wider, tempo-dependent range for its eighth-note feel: "apply a triplet-based swing feel (roughly 58-67% swing depending on tempo) to all eighth-note subdivisions." Note the pattern across both: swing percentage isn't a fixed universal number even within "genres that swing" — it moves with tempo and with how much triplet feel the genre wants, and higher percentages produce a more pronounced triplet lilt.

## Millisecond-Level Timing Offsets

`swing.md` specifies a technique distinct from swing percentage — deliberately staggering when different instrument sections start a note, to emulate ensemble imprecision: "stagger section entrances by a few milliseconds to emulate live ensemble imprecision." This is a small, targeted offset (a few ms, not a swing-grid setting) applied at entrances specifically, not as a blanket humanization pass across every note. `ambient.md` (cited in the music_theory swing entry) gives a comparable but larger and more general offset for a completely non-metric context: "loose timing (10-30ms random offset) since there is no strict grid to lock to."

## Genre-Specific Humanization Amount, Graded

Several jazz-family genres form a useful graded sequence for how much timing looseness to apply, from none to extensive:

- **Zero, by design:** `speedcore.md` — "None — speedcore is fully quantized by design; the mechanical relentlessness of the kick is central to the genre's identity, and any human timing looseness would undercut it."
- **Light, contrasted against harder styles:** `progressive_trance.md` — "Light timing humanization on percussion/groove elements is common and desirable here, in contrast to the strictly-quantized aesthetic of harder trance styles," with "subtle, humanized velocity variation across percussion layers for a more organic, less mechanically uniform groove than uplifting trance."
- **Moderate, closer to the grid than its predecessor styles:** `jazz_fusion.md` — "fusion is tighter and more precisely arranged than earlier swing-based jazz, so timing should be closer to the grid than modal jazz or bebop, while still avoiding fully mechanical quantization on solo lines."
- **Significant, including fully unquantized passages:** `modal_jazz.md` — "Significant micro-timing looseness needed — swung eighth feel varies by performer, and rubato passages (especially intros) should not be quantized at all."

Reading these together gives a practical dial rather than a binary choice: speedcore (0%) → progressive trance (light, percussion only) → jazz fusion (moderate, tighter than its jazz ancestors) → modal jazz (significant, with fully rubato sections). The right amount for a new track should be placed on this spectrum by finding the nearest documented genre neighbor, not chosen arbitrarily.

## Selective Humanization: Not Every Element Gets the Same Treatment

`trap.md` and `drill.md` both apply humanization asymmetrically within a single track: "808 and hi-hat programming stays tightly quantized for a driving, mechanical-precise feel; vocal delivery carries the human/expressive element" (`trap.md`); "Programming stays tightly quantized for rhythmic precision; the vocal delivery's aggressive cadence carries the human/expressive element" (`drill.md`). `hip_hop.md` documents this as a genre-wide spectrum rather than a fixed rule: "Humanization ranges from tightly quantized (modern trap-influenced) to intentionally loose and swung (boom-bap-influenced), depending on subgenre" — meaning the same parent genre spans both ends of the dial depending on which subgenre's sound is being targeted.

## Preserving Existing Humanization Rather Than Adding It

`jungle.md` documents a case where the correct action is to *not* apply a humanization pass at all, because the source material already carries real timing feel: "the genre's swing and feel come from the original drummer's performance preserved (and re-arranged) in the chops rather than from synthetic humanization." The genre's common-mistakes entry warns specifically against undoing this by "over-quantizing chopped breaks until they lose the original drummer's human swing."

## Common Mistakes

**Using a single default swing percentage across all "swung" genres.** `french_house.md`'s 54-60% and `swing.md`'s 58-67% are both "swing," but applying one genre's number to the other produces a groove that reads as subtly wrong even though swing is technically present.

**Applying a track-wide humanization percentage instead of the graded, element-specific approach `trap.md`/`drill.md`/`hip_hop.md` document.** Quantizing the drums while leaving the vocal free (or vice versa) is often the correct move, not an inconsistency to fix.

**Re-quantizing sample-sourced material that's already carrying real performance timing.** As with velocity, `jungle.md`'s breakbeat chops depend on the original drummer's micro-timing surviving into the final arrangement.

## Cross-References

- `knowledge_base/music_theory/rhythm/swing_and_quantization_feel.md` — the aesthetic "why" behind these genres' quantization/swing choices; this entry covers the implementation "how"
- `knowledge_base/genres/edm/french_house.md`, `knowledge_base/genres/jazz/swing.md` — named swing-percentage ranges
- `knowledge_base/genres/edm/speedcore.md`, `knowledge_base/genres/edm/progressive_trance.md`, `knowledge_base/genres/jazz/jazz_fusion.md`, `knowledge_base/genres/jazz/modal_jazz.md` — graded humanization intensity from none to extensive
- `knowledge_base/genres/hiphop/trap.md`, `knowledge_base/genres/hiphop/drill.md`, `knowledge_base/genres/hiphop/hip_hop.md` — selective, per-element humanization within one track
- `knowledge_base/genres/edm/jungle.md` — preserving source-material timing rather than applying synthetic humanization
- `knowledge_base/midi/programming/velocity_editing_and_dynamics.md` — the companion dimension (velocity) that's often graded alongside timing
