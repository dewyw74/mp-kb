---
technique_name: "Multiband Mastering Compression and Limiter Chain Ordering"
category: "dynamics"
problem_solved: "A single-band (full-range) compressor or limiter reacting to whichever frequency range is loudest at a given moment (usually bass), causing pumping or unwanted gain reduction across the whole spectrum rather than the specific problem range"
parameters:
  crossover_points: "Commonly split around 100-150Hz (low/low-mid boundary) and 2-5kHz (mid/high boundary) as genre-agnostic starting points, refined per-track based on where the source material's frequency-dependent dynamic problems actually sit"
  band_count: "3-band splits are the most common mastering-stage default; more bands add precision but also more interaction complexity between bands"
  chain_ordering: "EQ (broad tonal balance) before multiband compression (frequency-specific dynamics control) before the final limiter (overall loudness/ceiling), as the standard default order"
signal_chain_position: "Master bus, positioned after broad tonal-balance EQ and before the final brickwall limiter"
genre_applicability:
  - hip_hop
  - trap
  - pop
  - edm_trap
  - house
related_techniques:
  - dynamic_range_as_expressive_device
  - compression_and_clipping_as_aesthetic
  - true_peak_and_intersample_peaks
tags: ["multiband-compression", "mastering-chain", "limiter", "gain-staging", "mastering"]
---

# Multiband Mastering Compression and Limiter Chain Ordering

A full-range (single-band) compressor or limiter on a master bus reacts to the entire signal's combined level at once, which means a loud sub-bass hit can trigger gain reduction that also ducks an unrelated vocal or cymbal sitting in a completely different frequency range at that same instant. Multiband compression splits the signal into separate frequency bands (commonly 3, sometimes more) so each band's dynamics can be controlled independently — the bass can be tightened without the highs pumping in sympathy, and vice versa.

## Why Frequency-Independent Dynamics Control Matters at Mastering

A mastering-stage master already has all its elements summed into one stereo file — there's no going back to adjust an individual channel's compression the way there was during mixing. If the combined mix has a bass-heavy section triggering excessive full-range gain reduction, single-band compression or limiting can only respond to the whole signal at once, over-compressing frequency content that wasn't actually the source of the problem. Multiband processing at the mastering stage recovers some of that per-element control after the fact, at the frequency-band level rather than the individual-instrument level.

## Standard Chain Ordering

The conventional default order places broad tonal-balance EQ first (correcting overall frequency balance issues visible across the whole mix), multiband compression second (addressing frequency-specific dynamic problems — often a bass-heavy section pumping, or harsh high-frequency peaks needing targeted taming), and the final brickwall limiter last (setting overall loudness and, per `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md`, true-peak headroom). This ordering exists because each stage assumes the previous stage's problem has already been addressed — the limiter shouldn't be doing a multiband compressor's frequency-specific job, and the multiband compressor shouldn't be doing a broad EQ's overall tonal-balance job.

## Setting Crossover Points From the Actual Problem, Not a Fixed Recipe

While 100-150Hz and 2-5kHz are common starting-point crossover frequencies, the correct crossover placement for a given master should be set based on where that specific mix's frequency-dependent dynamics problem actually occurs — a trap master with an aggressive 808 that's triggering broadband gain reduction needs its low crossover placed to isolate exactly the 808's fundamental range, which varies by the specific bass patch and key used, rather than applied as a fixed universal number.

## Relationship to Aesthetic Compression/Clipping

`knowledge_base/mastering/dynamics/compression_and_clipping_as_aesthetic.md` documents genres (industrial, power electronics, speedcore, hardstyle) that treat heavy compression and clipping as a deliberate sonic identity rather than a corrective, transparent process. Multiband mastering compression as documented in this entry is the more common, corrective counterpart to that aesthetic use — the goal here is controlling problematic frequency-specific dynamics transparently, not generating audible distortion or pumping as the point of the processing.

## Common Mistakes

**Placing the limiter before multiband compression in the chain.** This asks the limiter to absorb frequency-specific dynamic problems it isn't designed to address cleanly, typically producing audible pumping or distortion that targeted multiband compression earlier in the chain would have prevented.

**Using generic crossover points without checking where the specific mix's actual problem frequency sits.** The 100-150Hz/2-5kHz starting points are defaults, not a substitute for identifying the actual frequency range causing broadband gain-reduction problems on a given master.

**Reaching for multiband compression as a substitute for fixing a mix-stage problem at its source.** Per the general principle in `knowledge_base/mixing/eq/subtractive_eq.md`, mastering-stage multiband processing is a corrective layer for problems that survive from the mix — it's more effective (and less likely to introduce audible artifacts) to fix a severely unbalanced element during mixing than to rely entirely on mastering-stage multiband compression to compensate.

## Cross-References

- `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md` — the final limiter stage that follows multiband compression in the standard chain order
- `knowledge_base/mastering/dynamics/compression_and_clipping_as_aesthetic.md` — the aesthetic/deliberate counterpart to this entry's corrective/transparent use case
- `knowledge_base/mastering/dynamics/dynamic_range_as_expressive_device.md` — the broader dynamic-range philosophy this chain-ordering technique serves
- `knowledge_base/mixing/compression/sidechain_pumping.md` — a mix-stage frequency-specific dynamics technique conceptually related to multiband mastering compression
