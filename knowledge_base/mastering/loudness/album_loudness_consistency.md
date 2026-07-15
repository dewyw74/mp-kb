---
technique_name: "Album/EP Loudness Consistency Across Tracks"
category: "loudness"
problem_solved: "Mastering each track on a release to the same genre-appropriate target_loudness number in isolation, then discovering on playback that the album/EP doesn't feel consistently leveled — a quieter or more dynamic track feels like a jarring dip, or a louder track feels like an unwelcome jump, between songs"
parameters:
  per_track_vs_per_release: "A genre file's target_loudness is a single-track convention; album-level consistency is a separate practice layered on top of it, comparing tracks against each other rather than each against the genre norm alone"
  reference_matching: "Gain-staging each track against a shared reference track (or against the other tracks on the same release) during mastering, rather than mastering each track to a fixed LUFS number in total isolation"
  logging: "Recording each track's integrated LUFS and true-peak reading as it's finalized, so the whole release's numbers can be reviewed together before final delivery rather than discovered to be inconsistent after the fact"
signal_chain_position: "A release-level review pass across all final masters, done after individual track mastering but before final delivery"
genre_applicability:
  - post_rock
  - trance
  - k_pop
  - scandipop
related_techniques:
  - lufs_targets_by_genre
  - lufs_short_term_vs_integrated_vs_momentary
  - perceived_loudness_vs_peak_level
tags: ["album-consistency", "ep", "reference-matching", "gain-staging", "lufs"]
---

# Album/EP Loudness Consistency Across Tracks

Grounding for this entry is honestly thinner than the other loudness entries in this knowledge base: every genre file here documents a single-track `target_loudness` convention, because genre files describe how one song in a given style is typically mastered, not how a multi-track release is sequenced and leveled as a whole. Album- and EP-level consistency is a real, well-established mastering practice, but it isn't something the genre corpus was built to capture directly. What the corpus *does* offer is a set of within-song loudness-contrast examples that are structurally analogous to the album-consistency problem — a single track intentionally varying perceived loudness section-to-section is a smaller-scale version of the same core question an album faces track-to-track: should this quieter (or louder) moment read as a deliberate contrast, or as an inconsistency to fix?

## The Practice, in General Terms

Album/EP loudness consistency means a listener moving from track to track on a release doesn't experience unintended jumps or dips in perceived loudness — variation that isn't a deliberate artistic choice by the artist/engineer, but simply an artifact of each track having been mastered independently to its own local target. In practice this is usually handled by gain-staging each finished master against a shared reference (either the loudest or most representative track on the release, or an external reference track in the same genre), and by logging each track's integrated LUFS and true-peak figures so the full set can be reviewed together — checking, for example, that no track sits more than roughly 1-2 LU away from the release's chosen central loudness without a specific reason — before final delivery. This is general mastering-engineering practice rather than something documented in this knowledge base's genre files, since it operates at the release level, above what any single genre entry describes.

## Why Genre `target_loudness` Ranges Already Anticipate Some of This

It's worth noting that every genre file's `target_loudness` in this knowledge base is already expressed as a range rather than a single fixed number — `pop.md`'s "-9 to -7 LUFS integrated," `trap.md`'s "-8 to -6 LUFS integrated," `post_rock.md`'s "-14 to -10 LUFS integrated." That range gives an engineer room to land each individual track at a slightly different point depending on its own internal dynamics and content, while still keeping every track on a release within the same genre-appropriate band — which is a first, coarse layer of album consistency built into genre convention itself, even without a dedicated album-level pass.

## The Closest Genre-File Analogue: Within-Song Section Contrast

Several genre files describe a track deliberately varying its own perceived loudness by section, which is the same underlying design question an album faces between tracks, just compressed to song-length rather than album-length. `trance.md` documents an explicit two-tier structure within a single track: "Peak sections are mastered for maximum club and festival impact, typically -8 to -6 LUFS integrated, while breakdowns retain more relative dynamic headroom to preserve the emotional contrast that is central to the genre's storytelling arc." `k_pop.md` frames its own section variation the same way: "Compressed for streaming/radio competitiveness while preserving the genre's dramatic section-to-section contrast." `scandipop.md` states it in almost the same terms: "Deliberate dynamic contrast preserved between minor-key verse restraint and euphoric chorus lift, even within an overall loud, radio-competitive master." `post_rock.md`'s entire mastering philosophy — preserving "the contrast between near-silent openings and overwhelming climaxes" — is the most extreme version of this same idea, taken to a whole-song scale.

## What the Analogy Does and Doesn't Establish

The parallel is useful but limited: within a single track, a documented loudness dip or peak (a breakdown, a verse) is almost always a *deliberate* arrangement device the mastering engineer is protecting, not an accident to be smoothed out — the whole point of `trance.md` and `post_rock.md`'s guidance is to preserve that contrast, not eliminate it. Album-level inconsistency is usually the opposite problem: an *unintended* loudness mismatch between tracks that a listener experiences as jarring rather than as a deliberate artistic choice. The practices are related (both involve deciding what loudness variation is meaningful vs. what should be evened out) but the correct response is often reversed — protect the contrast within a song, but generally normalize unintended contrast between songs on the same release, unless the artist has specifically sequenced the album to have its own dynamic arc (a quiet opener building into a loud centerpiece, for instance, which would make the album-level and within-song cases converge).

## Common Mistakes

**Mastering each track on a release in total isolation with no final cross-track comparison.** Even if every track lands within its genre's documented `target_loudness` range, they can still land at different enough points within that range to create an audible inconsistency across the release.

**Treating album consistency as "make every track the same LUFS."** As the within-song contrast examples above show, deliberate loudness variation is often the correct choice at the song level — the same logic can apply at the album level for a release with an intentional sequencing arc, so consistency should mean "no *unintentional* jumps," not "every track identical."

**Not logging per-track LUFS/true-peak figures during mastering.** Without a simple log of each finished track's numbers, inconsistency across a release is easy to miss until a full-album playback review, by which point re-mastering a track to fit is more disruptive than catching it during the original pass.

## Cross-References

- `knowledge_base/genres/edm/trance.md` — explicit two-tier (breakdown vs. peak) loudness structure within a single track, the closest genre-file analogue to album-level variation
- `knowledge_base/genres/pop/k_pop.md` and `knowledge_base/genres/pop/scandipop.md` — deliberate verse/chorus loudness contrast within a single master
- `knowledge_base/genres/rock/post_rock.md` — the most extreme single-track version of intentional loudness variation, at whole-song scale
- `knowledge_base/mastering/loudness/lufs_targets_by_genre.md` — the range-based (not fixed-number) target_loudness convention that gives album tracks some built-in consistency margin
- `knowledge_base/mastering/loudness/lufs_short_term_vs_integrated_vs_momentary.md` — the metering windows used to check both within-song and (by extension) cross-track loudness consistency
