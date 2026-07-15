---
technique_name: "Loudness Metering Workflow During Mastering"
category: "loudness"
problem_solved: "Not having a repeatable process for actually reaching a target_loudness figure — mastering 'by ear' toward a vague sense of loudness, or checking a meter only once at the end, produces inconsistent results and misses problems (hot transients, section-level imbalance, unsafe true peak) that a structured metering workflow catches while there's still time to fix them"
parameters:
  metering_plugin: "A LUFS-capable metering plugin showing momentary, short-term, and integrated readouts simultaneously, placed on the master bus after all mix-bus processing but before (or wrapped around) the final limiter"
  gain_automation: "Coarse gain staged first to bring the short-term reading into the genre's target_loudness neighborhood, with the final limiter doing comparatively little work rather than carrying the entire loudness gain alone"
  true_peak_margin: "A true-peak-aware limiter ceiling (commonly -1dBTP or lower per true_peak_and_intersample_peaks.md) set independently of and in addition to the integrated LUFS target"
  reference_comparison: "Level-matched A/B comparison against a genre-appropriate commercial reference track, so the target isn't just a meter reading but a perceptual check against material the genre's own listeners already consider well-mastered"
signal_chain_position: "Continuous monitoring across the entire mastering-stage signal chain, from initial gain staging through the final limiter, not a single end-of-chain check"
genre_applicability:
  - post_rock
  - pop
  - trap
  - riddim
  - dark_ambient
related_techniques:
  - lufs_short_term_vs_integrated_vs_momentary
  - true_peak_and_intersample_peaks
  - lufs_targets_by_genre
tags: ["metering", "workflow", "gain-staging", "reference-track", "true-peak-limiter"]
---

# Loudness Metering Workflow During Mastering

The step-by-step process of actually reaching a target loudness during mastering is general mastering-engineering workflow rather than something this knowledge base's genre files document directly — genre entries state the destination (`target_loudness`, `dynamics`, `frequency_balance`) but not the metering-and-gain-staging process used to get there, since that process is largely genre-independent even though the destination numbers vary enormously by genre. This entry is honest about that: the workflow described below is general audio-engineering practice, not a synthesis of genre-file citations. What the genre corpus *does* provide is the concrete set of numeric targets an engineer is actually metering toward — the destination the workflow below is built to reach — and those numbers are worth anchoring the abstract workflow to real, cited figures.

## Step 1: Meter Placement and What to Watch

A LUFS-capable metering plugin is placed on the master bus, ideally showing momentary, short-term, and integrated readouts at once (see `lufs_short_term_vs_integrated_vs_momentary.md` for what each window is built to catch). The integrated reading only becomes meaningful once a meaningful portion of the track has played, so early in a mastering pass an engineer is mostly watching short-term and momentary behavior — how loud a given section or hit reads right now — rather than the integrated figure, which only converges to a stable, trustworthy number toward the end of playback.

## Step 2: Gain Staging Before Leaning on the Limiter

Rather than relying entirely on a brickwall limiter to carry a track from its mixed level up to the genre's target loudness, the more controlled approach is to first apply broad gain staging (a simple level increase, plus any needed mix-bus EQ/compression/glue) to bring the track's short-term reading into the general neighborhood of the target, so the final limiter is doing comparatively little work — shaving peaks and adding a modest amount of extra density — rather than being pushed hard enough to become the dominant factor in the track's sound. This distinction matters because how much work the limiter is doing is closely tied to the perceived-loudness/crest-factor concerns raised in `perceived_loudness_vs_peak_level.md`: a limiter doing a little work on a well-gain-staged track produces a very different result than a limiter doing a lot of work compensating for a track that was left too quiet going in.

## Step 3: Watching the Genre's Actual Target Numbers

Genre files give the engineer concrete numeric checkpoints to meter against, even though they don't describe the metering process itself. A post-rock master should see its integrated reading settle somewhere in `post_rock.md`'s documented "-14 to -10 LUFS integrated" range, and the engineer watching the short-term meter during the track's quiet opening and its climax should see those two sections read very differently from each other — if they don't, the earlier gain-staging or limiting has already erased the contrast `post_rock.md`'s mastering guidance is built to protect. A trap master watching for `trap.md`'s "-8 to -6 LUFS integrated" should expect the short-term meter to sit in a comparatively narrower band than post-rock's, since trap's own dynamics description calls for being "fairly compressed... while preserving 808 punch" rather than wide structural contrast. A riddim master targeting `riddim.md`'s "-6 to -5 LUFS integrated" should expect the meter (and the ear) to confirm the "very low dynamic range" the genre file describes as deliberate. In each case, the genre file supplies the number the workflow is metering toward; the workflow itself supplies the process for getting there without breaking something else along the way.

## Step 4: True-Peak Limiting as a Separate, Simultaneous Check

Independent of the integrated LUFS target, the final limiter's ceiling needs to be set in true-peak (oversampling) mode rather than plain sample-peak mode, with headroom commonly at -1dBTP or lower, per `true_peak_and_intersample_peaks.md`. This check runs in parallel with the loudness-target check, not after it — a track can be mid-way through gain staging toward its LUFS target while the true-peak ceiling is already fixed at the final limiter, so the two checks are both live throughout the later part of a mastering pass rather than sequential steps.

## Step 5: Reference-Track Comparison

A level-matched comparison against a commercial reference track in the same genre is a standard workflow check precisely because a meter reading alone doesn't confirm the master actually sounds right for the style — it confirms the number is correct, not the perceptual result. Level-matching (turning both the in-progress master and the reference to the same perceived loudness before comparing, usually via the reference's own LUFS reading) is important here, since comparing an unmatched-level reference against a work-in-progress master will make whichever one is louder seem better by default, independent of actual tonal or dynamic quality — a well-known trap in critical listening generally, not specific to mastering.

## Step 6: Momentary Spikes on Transient-Heavy Material

For genres with prominent transient content — `trap.md`'s 808s and hi-hats, `jungle.md`'s chopped breaks — the momentary meter needs specific attention during the pass, since a limiter tuned primarily to hit an integrated target can still be crushing individual hits in a way the integrated or even short-term reading won't clearly show. Watching for unexpected momentary spikes (or unexpected momentary flatness, which can indicate a transient has already been over-limited) during playback of the track's busiest sections is a targeted check on top of the broader integrated/short-term monitoring described above.

## Common Mistakes

**Checking the loudness meter only once, after the full mastering chain is applied.** This turns metering into a pass/fail check at the end rather than a diagnostic tool used throughout the pass — by the time a problem shows up on a single end-of-chain check, it's often already baked into decisions made several steps earlier.

**Relying on the limiter alone to reach the target loudness.** Leaning entirely on the limiter rather than gain-staging first tends to produce a denser, more limiting-dominated result than necessary to hit the same integrated number — see `perceived_loudness_vs_peak_level.md` for why that difference is audible even at a matched LUFS figure.

**Comparing against a reference track without level-matching first.** An unmatched-level comparison biases the ear toward whichever track is louder in the moment, regardless of which one is actually better mastered — level-match before doing any A/B judgment.

## Cross-References

- `knowledge_base/mastering/loudness/lufs_short_term_vs_integrated_vs_momentary.md` — the three metering windows this workflow watches simultaneously
- `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md` — the true-peak-specific check that runs alongside the integrated-loudness workflow described here
- `knowledge_base/mastering/loudness/perceived_loudness_vs_peak_level.md` — why gain-staging-first vs. limiter-only approaches to reaching the same LUFS number sound different
- `knowledge_base/genres/rock/post_rock.md`, `knowledge_base/genres/hiphop/trap.md`, `knowledge_base/genres/edm/riddim.md` — concrete target_loudness figures used above as workflow checkpoints
- `knowledge_base/mastering/loudness/lufs_targets_by_genre.md` — the full set of genre-specific numeric targets this workflow is generically built to reach
