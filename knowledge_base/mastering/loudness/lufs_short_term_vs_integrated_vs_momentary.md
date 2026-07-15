---
technique_name: "Momentary, Short-Term, and Integrated LUFS Metering"
category: "loudness"
problem_solved: "Watching only one loudness metering window during mastering — typically whatever number a plugin's main readout defaults to — misses problems the other two windows are specifically designed to catch: a single hot transient, a chorus that reads louder than the rest of the mix, or a final delivery number that doesn't match the genre's documented target"
parameters:
  momentary: "~400ms sliding window, ungated — the fastest-responding of the three, built to catch a single hit, stinger, or transient spike rather than a sustained section"
  short_term: "~3 second sliding window, ungated — built to track a section's (verse, chorus, drop, breakdown) sustained perceived loudness as it plays, faster than integrated but slower/more stable than momentary"
  integrated: "Whole-program average per ITU-R BS.1770 / EBU R128, gated (silence below -70 LUFS excluded, plus a relative gate dropping content 10 LU below the running integrated value) — this is the single number genre files document as target_loudness"
signal_chain_position: "Final mastering-stage metering, read continuously alongside the limiter rather than checked only once at the end of the chain"
genre_applicability:
  - pop
  - trance
  - k_pop
  - post_rock
  - trap
  - dark_ambient
related_techniques:
  - lufs_targets_by_genre
  - loudness_metering_workflow
  - perceived_loudness_vs_peak_level
tags: ["lufs", "metering", "momentary", "short-term", "integrated", "ebu-r128", "bs1770"]
---

# Momentary, Short-Term, and Integrated LUFS Metering

ITU-R BS.1770 and EBU R128 define three loudness measurement windows, not one, and they're not interchangeable readings of the same thing at different smoothing amounts — they're built to answer three different questions during mastering. Momentary loudness integrates over a ~400ms sliding window and isn't gated, making it the fastest-responding of the three and the one built to catch a single transient or hit. Short-term loudness integrates over a ~3 second sliding window, also ungated, tracking a section's loudness as it actually plays. Integrated loudness is the whole-program average, gated so that silence and unusually quiet passages don't drag the number down — this is the single figure every genre file in this knowledge base documents under `target_loudness`. None of the genre entries in this corpus discuss metering windows explicitly by name (they document the final `target_loudness` number, not the metering process used to reach it), so the window definitions above are general BS.1770/R128 specification, verified independently rather than pulled from a genre-file citation — but the genre files' loudness targets are still the concrete, citable anchor for what an engineer is watching the integrated window converge toward.

## Integrated LUFS Is the Number Genre Files Actually Document

Every `target_loudness` figure in this knowledge base's genre files is an integrated-loudness number, and the range across genres is wide enough that the integrated window is doing real discriminating work, not just providing a vague "how loud is this" figure. `post_rock.md` targets "-14 to -10 LUFS integrated," `pop.md` targets "-9 to -7 LUFS integrated," `k_pop.md` targets "-8 to -6 LUFS integrated," and `riddim.md` targets "-6 to -5 LUFS integrated." An engineer mastering any of these genres is ultimately watching the integrated meter converge on that specific documented figure over the length of the whole track — but getting there without checking the other two windows along the way risks missing exactly the kind of problem those windows exist to catch.

## Where Short-Term Loudness Matters: Section-to-Section Contrast

Several genre files describe explicit within-song loudness contrast between sections — a chorus, drop, or peak section that's deliberately louder than a verse or breakdown, distinct from and sitting on top of the track's overall integrated target. `k_pop.md` documents this as a genre priority: "Compressed for streaming/radio competitiveness while preserving the genre's dramatic section-to-section contrast." `pop.md` frames the same contrast around a specific arrangement moment: "prioritizing loudness competitiveness on streaming platforms while still preserving enough dynamic contrast between verse and chorus to keep the arrangement's lift audible." `trance.md` states it as an explicit two-tier loudness structure within a single track: "Peak sections are mastered for maximum club and festival impact, typically -8 to -6 LUFS integrated, while breakdowns retain more relative dynamic headroom to preserve the emotional contrast that is central to the genre's storytelling arc." A short-term meter (the ~3 second window) is the tool that actually shows this contrast happening in real time — watching only the final integrated number would tell you the track hit its overall target, but it wouldn't tell you whether the chorus got audibly hotter than the verse, or whether a limiter quietly ironed that contrast flat while the integrated average still landed correctly. This is the same structural concern `dynamic_range_as_expressive_device.md` raises about post-rock and ambient genres, applied to a faster, section-level timescale rather than a whole-song arc.

## Where Momentary Loudness Matters: Single-Hit and Transient Material

The 400ms momentary window responds fast enough to register a single sharp event — a snare hit, an 808 slide, a horror-score stinger — that would be smoothed away by even the 3-second short-term window, let alone the whole-program integrated average. `trap.md`'s target of "-8 to -6 LUFS integrated" is reached with, per its own dynamics note, mastering that stays "fairly compressed for streaming/club loudness competitiveness while preserving 808 punch and hi-hat clarity" — preserving that punch and clarity on individual hits is a momentary-timescale concern, not something the integrated number can verify on its own, since a limiter can crush individual transients while the long-term average still lands exactly on target. `jungle.md` makes the same point from the opposite direction, describing masters that "retain more dynamic range than modern EDM, generally sitting around -9 to -7 LUFS integrated, preserving the transient punch of chopped breaks that would otherwise be flattened by heavy limiting" — the whole reason jungle's chopped-break transients survive mastering is that the engineer is protecting momentary-timescale peaks from a limiter that would otherwise be tuned only to the integrated target.

## Reading All Three Windows Together

In practice, the three windows answer three different questions during a mastering pass: is this specific hit or transient still punchy (momentary), is this section reading at the perceived loudness the arrangement intends relative to the surrounding sections (short-term), and has the whole track converged on the genre's documented delivery target (integrated). A master can pass on integrated loudness alone and still have failed on either of the other two — a flattened chorus-to-verse contrast, or a squashed transient — which is why mastering engineers watch short-term and momentary readouts continuously during the pass rather than checking only the final integrated number once processing is done.

## Common Mistakes

**Treating the integrated number as the only thing worth watching.** A track can converge on its documented `target_loudness` while a limiter has quietly flattened the verse-to-chorus or breakdown-to-drop contrast the arrangement depends on — that failure only shows up on the short-term window, not the integrated one.

**Reading momentary spikes as a mixing problem rather than a mastering-stage limiter setting.** A hot momentary reading on a transient-heavy element (drum hits, 808 slides) is often a limiter attack/release setting that's crushing the transient rather than a level problem in the mix itself.

**Assuming a fast meter response (momentary) gives a more "accurate" loudness reading than the slower windows.** Each window is answering a different question, not offering competing levels of precision on the same question — momentary readings jump around by design and aren't meant to be read as the track's overall loudness.

## Cross-References

- `knowledge_base/mastering/loudness/lufs_targets_by_genre.md` — the integrated-loudness numbers this entry's momentary/short-term windows are checked against during mastering
- `knowledge_base/genres/pop/k_pop.md` and `knowledge_base/genres/pop/pop.md` — explicit section-to-section (verse/chorus) loudness contrast, the short-term window's primary use case
- `knowledge_base/genres/edm/trance.md` — an explicit two-tier loudness structure (breakdown vs. peak) within a single track
- `knowledge_base/genres/hiphop/trap.md` and `knowledge_base/genres/edm/jungle.md` — transient/hit-level punch preservation, the momentary window's primary use case
- `knowledge_base/mastering/dynamics/dynamic_range_as_expressive_device.md` — the whole-song-arc version of the same contrast-preservation concern this entry addresses at the section and hit level
