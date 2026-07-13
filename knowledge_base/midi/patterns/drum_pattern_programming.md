---
technique_name: Drum Pattern Programming
category: patterns
problem_solved: "Deciding which drum elements carry a genre's rhythmic signature (hi-hats, ghost notes, breakbeat chops, polyrhythmic percussion) versus which stay as simple timekeeping"
genre_applicability:
  - trap
  - drill
  - boom_bap
  - hard_bop
  - jazz_fusion
  - afro_house
  - jungle
  - french_house
  - progressive_trance
related_techniques:
  - bass_and_808_pattern_programming
  - velocity_editing_and_dynamics
  - humanization_and_groove_timing
tags: ["drums", "hi-hats", "ghost-notes", "breakbeat", "polyrhythm", "midi-programming"]
---

# Drum Pattern Programming

Every genre in this knowledge base has a drum element that carries most of its rhythmic identity — but which element that is varies enormously, and programming the wrong one as the "featured" part is a common way to miss a genre's groove even with technically correct note placement.

## Hi-Hats as the Signature Element

Trap-descended genres put their rhythmic identity almost entirely in the hi-hat part rather than the kick/snare. `trap.md` states this plainly: "Hi-hats are the genre's signature rhythmic element — rapid rolls, triplet subdivisions, and velocity-varied accents create the 'trap hi-hat' feel; kick/808 and snare/clap placement is sparse and syncopated by comparison." The file's professional tips reinforce the priority order: "Build the beat around the 808 and hi-hat relationship first — melody is secondary atmosphere in most trap production," and "Use hi-hat roll variation (triplets, 32nd notes, velocity accents) as the primary source of rhythmic interest and groove." `hip_hop.md` generalizes this across the wider genre: "hi-hats carry much of the rhythmic character through rolls, triplets, and velocity variation."

## Ghost Notes and Press Rolls

`hard_bop.md` documents ghost notes as a deliberate expressive device rather than a mixing accident: "Program a harder-hitting backbeat feel with syncopated, propulsive bass-drum accents (not just ride-cymbal timekeeping)... use ghost notes and press rolls to capture the genre's assertive, gospel-influenced drive." `jazz_fusion.md` uses ghost notes on the bass rather than drums for the same rhythmic-filling function: "syncopated, funk-derived electric bass lines with ghost notes and 16th-note subdivisions." `jungle.md` applies a related idea to re-triggered breakbeat chops: "deliberate accents added on re-triggered ghost notes for extra swing." Across all three, the ghost note's job is the same — filling rhythmic space with low-velocity hits that a listener feels more than consciously hears, distinct from the strong, clearly-accented main hits.

## Polyrhythmic and Interlocking Percussion

`afro_house.md` describes drum programming as a layered, interlocking system rather than a single pattern: "layered hand percussion — congas, bongos, shakers, log drums (kalimba-adjacent tuned percussion), and tribal toms — programmed in interlocking polyrhythmic patterns," built up incrementally from "layered hand percussion... establishing a polyrhythmic groove before the kick and bassline enter." `jazz_fusion.md` applies a related but distinct polyrhythmic approach to odd meters: "odd-meter patterns (7/8, 5/4) should be programmed with clear internal subdivision groupings (e.g. 2+2+3) rather than treated as an undifferentiated bar length" — the programming technique here is making the meter's internal grouping audible through accent placement, not just getting the note count right.

## Breakbeat Chops as "Already-Human" Drum Programming

Jungle's drum programming inverts the usual workflow: instead of programming a pattern from scratch and then humanizing it, the source material (a sampled breakbeat) is already a human performance, and the programming task is chopping and re-arranging it while preserving that feel. `jungle.md`: "The breakbeat source material is already human-played, so the genre's swing and feel come from the original drummer's performance preserved (and re-arranged) in the chops rather than from synthetic humanization." The file's named common mistake is "over-quantizing chopped breaks until they lose the original drummer's human swing, which flattens the genre's essential groove" — a case where quantization actively destroys feel that was already present in the source, rather than a case of adding feel to a rigid grid.

## Swung Foundational Patterns

`boom_bap.md` ties its entire groove identity to one specific kick/snare relationship: "The genre's namesake kick-and-snare pattern (a heavy 'boom' kick on 1, a strong 'bap' snare, both swung and sitting slightly behind the beat) defines its laid-back, head-nodding groove — quantizing this too rigidly removes the essential feel." `french_house.md` documents a similarly specific four-on-the-floor recipe: "Four-on-the-floor kick with open hats on the off-beat 8ths, claps/snares on 2 and 4, and swung 16th-note shaker/hat patterns lifted in feel from chopped funk breakbeats."

## Common Mistakes

**Programming the kick/snare as the featured rhythmic element in a hi-hat-driven genre.** Trap's rhythmic interest lives in the hi-hat rolls and velocity accents; a technically correct but static hi-hat pattern under an elaborate kick/snare arrangement inverts the genre's actual priority.

**Quantizing away ghost notes or breakbeat-source swing.** Both `hard_bop.md`'s ghost-note guidance and `jungle.md`'s breakbeat-chop guidance depend on preserving low-velocity, slightly-off-grid hits — over-quantizing removes the exact texture the technique exists to create.

**Flattening polyrhythmic layers into a single quantization grid.** `afro_house.md`'s interlocking percussion and `jazz_fusion.md`'s grouped odd-meter accents both require each layer/grouping to keep its own internal logic rather than being forced onto one uniform subdivision.

## Cross-References

- `knowledge_base/genres/hiphop/trap.md`, `knowledge_base/genres/hiphop/hip_hop.md` — hi-hats as the primary rhythmic-interest element
- `knowledge_base/genres/jazz/hard_bop.md`, `knowledge_base/genres/jazz/jazz_fusion.md` — ghost notes and grouped odd-meter accents
- `knowledge_base/genres/world_music/afrobeat.md`, `knowledge_base/genres/edm/afro_house.md` — layered, interlocking polyrhythmic percussion
- `knowledge_base/genres/edm/jungle.md` — breakbeat chops as already-humanized source material
- `knowledge_base/genres/hiphop/boom_bap.md`, `knowledge_base/genres/edm/french_house.md` — swung foundational kick/snare/hat recipes
- `knowledge_base/midi/patterns/bass_and_808_pattern_programming.md` — how the bass locks against these drum patterns
