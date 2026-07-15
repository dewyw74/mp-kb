---
technique_name: "Inter-Track Gain and Level Staging Across an Album"
category: "other"
problem_solved: "Tracks mastered individually to their own genre-correct loudness target end up jarringly inconsistent in perceived level when sequenced together on one album or EP — a listener has to reach for the volume knob between songs, which breaks the listening experience regardless of how well each individual track was mastered"
parameters:
  genre_convention_sets_the_starting_gap: "Because target_loudness varies enormously by genre (from roughly -20 LUFS for the quietest ambient/dynamics-preserving genres to roughly -6 LUFS for the loudest festival/EDM genres), an album mixing genres or moods internally needs deliberate inter-track gain staging to avoid that entire documented range showing up as audible level jumps"
  relative_not_absolute_matching: "Inter-track gain staging is a relative decision (how does track 3 feel against track 2 and track 4) rather than a simple rule of forcing every track to an identical LUFS number, since a deliberately quieter interlude or a deliberately loud climax may be the intended effect"
  streaming_normalization_context: "Modern streaming-platform loudness normalization reduces (but does not eliminate) the practical impact of inter-track level inconsistency, since platforms typically normalize at the album or release level differently than at the single-track level depending on the service"
signal_chain_position: "Final gain-staging pass across the full album/EP running order, performed after each track's individual mastering chain is complete, immediately before delivery"
genre_applicability:
  - dark_ambient
  - complextro
  - glitch
  - reggaeton
  - post_rock
related_techniques:
  - album_track_ordering_and_flow
  - silence_gaps_and_crossfades_between_tracks
  - genre_tonal_balance_targets
tags: ["sequencing", "gain-staging", "loudness-consistency", "lufs", "other"]
---

# Inter-Track Gain and Level Staging Across an Album

Like album track ordering, this is a topic individual genre files weren't written to address directly — no entry in this corpus discusses sequencing multiple tracks together. What the corpus does provide is something genuinely useful for this specific problem: dozens of genre files document a precise `target_loudness` figure, and comparing those figures across genres shows exactly how wide a gap inter-track gain staging has to manage whenever a release isn't drawn from a single tightly-conventional genre.

## The Documented Loudness Range Inter-Track Staging Has to Bridge

At the quiet end, `dark_ambient.md` documents mastering "to a quieter integrated loudness (-20 to -14 LUFS) than most electronic genres, with minimal limiting" — a direct quote from the dynamics preservation entry in this knowledge base. At the loud end, `complextro.md` documents masters that "typically run dense and loud, around -7 to -6 LUFS integrated, comparable to mainstream festival EDM." `reggaeton.md` is mastered "extremely loud to compete in clubs and on streaming playlists," while `glitch.md` deliberately masters quieter than most electronic material — "a target of roughly -12 to -9 LUFS integrated" — specifically to preserve dynamic detail. `post_rock.md` doesn't state a single LUFS figure but documents why any figure alone would be misleading for this genre: dynamic range preservation is "essential — the genre's entire expressive power depends on the contrast between near-silent openings and overwhelming climaxes." That range — roughly -20 LUFS at the quietest documented genre target to roughly -6 LUFS at the loudest — is the practical scale inter-track gain staging has to manage whenever a release spans genres or moods this different.

## Why This Isn't Just "Normalize Everything to the Same Number"

The post_rock and dark_ambient citations above point to the actual complication: for genres (and individual tracks within a genre-consistent album) where dynamic range and contrast are the compositional point, forcing every track to an identical integrated LUFS reading can flatten exactly the peak-to-quiet relationship the sequencing is supposed to showcase. A quieter interlude track between two louder pieces, or a climactic closing track intentionally mastered louder than what precedes it, are legitimate sequencing decisions — inter-track gain staging in cases like this means judging the *relative* perceived-loudness relationship between adjacent tracks by ear, not mechanically matching every track's meter reading.

## The Streaming Normalization Wrinkle

Because most listening now happens through platforms that apply their own loudness normalization, extreme inter-track loudness gaps are partially (not fully) smoothed out automatically once a release reaches a streaming service — but that normalization typically doesn't apply within an album consistently across every playback context (offline downloads, DJ software, some car-integration systems bypass it), so gain staging the actual delivered files still matters rather than being fully outsourced to the platform.

## Common Mistakes

**Mastering every track on a mixed-genre or mixed-mood release to its own individually "correct" genre LUFS target without checking the sequence as a whole.** A dark-ambient-adjacent interlude mastered to -18 LUFS immediately followed by a complextro-leaning track mastered to -6 LUFS produces exactly the jarring, reach-for-the-volume-knob experience this entry exists to prevent, even though each individual master might be genre-correct in isolation.

**Force-normalizing every track to an identical LUFS reading regardless of intended dynamic relationship.** As `post_rock.md`'s contrast-dependent structure illustrates at the single-track level, the same principle applies across a sequence — a deliberately quieter or louder track relative to its neighbors may be the intended effect, not an inconsistency to correct.

**Assuming streaming normalization makes inter-track gain staging unnecessary.** Normalization behavior varies by platform and playback context, and doesn't apply uniformly to every way a release might be consumed (download, DJ set, offline playback) — the delivered files still need to make sense on their own.

## Cross-References

- `knowledge_base/mastering/sequencing/album_track_ordering_and_flow.md` — the ordering decision that inter-track gain staging is applied on top of
- `knowledge_base/mastering/loudness/lufs_targets_by_genre.md` — the fuller genre-by-genre loudness target reference this entry draws its range from
- `knowledge_base/mastering/dynamics/dynamic_range_as_expressive_device.md` — the dynamics-preservation principle that complicates simple LUFS-matching across a sequence
- `knowledge_base/genres/electronic/dark_ambient.md`, `knowledge_base/genres/edm/complextro.md`, `knowledge_base/genres/world_music/reggaeton.md`, `knowledge_base/genres/electronic/glitch.md`, `knowledge_base/genres/rock/post_rock.md` — direct sources for the documented loudness-target range this entry compares
