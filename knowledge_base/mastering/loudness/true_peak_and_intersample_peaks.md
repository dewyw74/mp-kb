---
technique_name: "True Peak Headroom and Inter-Sample Peak Management"
category: "loudness"
problem_solved: "Masters that measure fine on a sample peak meter but clip audibly after lossy encoding or platform transcoding introduces inter-sample peaks above 0dBTP"
parameters:
  true_peak_ceiling: "Commonly -1dBTP or lower on the final limiter, independent of whatever integrated LUFS target the genre calls for"
  measurement_tool: "A true-peak (oversampling) meter, not a standard sample peak meter, since sample peak meters can't detect inter-sample overshoots"
  relationship_to_loudness: "True peak headroom and integrated LUFS target are separate, independently-set measurements — meeting one doesn't guarantee the other is safe"
signal_chain_position: "Final limiter on the master bus, as the last stage before export/delivery"
genre_applicability:
  - trap
  - dubstep
  - techno
  - pop
  - hard_techno
related_techniques:
  - dynamic_range_as_expressive_device
  - compression_and_clipping_as_aesthetic
  - platform_normalization_behavior
tags: ["true-peak", "intersample-peaks", "mastering", "limiting", "loudness", "streaming"]
---

# True Peak Headroom and Inter-Sample Peak Management

`knowledge_base/mastering/streaming/platform_normalization_behavior.md` documents true peak as a concern distinct from a genre's integrated loudness (LUFS) target — this entry expands specifically on why that distinction exists and how to manage it at the final limiting stage.

## Why Sample Peaks Aren't the Whole Story

A standard sample peak meter only measures the digital signal at each discrete sample point, but the actual analog waveform a D/A converter (or a lossy codec's decoder) reconstructs between samples can overshoot those measured points — an "inter-sample peak." A master that reads 0dBFS or just under on a sample peak meter can therefore still produce a reconstructed waveform that exceeds 0dBTP (true peak, i.e., dB True Peak) once actually played back or decoded, and that overshoot is where audible clipping and distortion artifacts get introduced even though the file "measured safe" on the wrong kind of meter.

## Why This Matters More After Transcoding

`knowledge_base/mastering/streaming/platform_normalization_behavior.md` states the core risk directly: "lossy encoding and platform-side transcoding can introduce inter-sample peaks that weren't present in the original file, and a master left with no headroom at all is more likely to produce audible clipping artifacts after that processing than one with a small margin retained." This is why the standard mastering guidance is to leave true-peak headroom (commonly -1dBTP or lower) as a fixed safety margin, applied on top of whatever integrated loudness target the genre calls for — a hard-techno master targeting an aggressively loud integrated LUFS still needs the same -1dBTP true-peak ceiling as a much quieter, dynamic-range-preserving master; the two measurements are independent.

## True Peak vs. Integrated Loudness Are Separate Decisions

The file's common-mistakes guidance names the specific failure mode directly: "Ignoring true-peak headroom because the integrated LUFS target is already met. These are separate measurements; a track can sit at an appropriate integrated loudness and still clip after transcoding if true peak was left at or near 0dBTP." This matters specifically because achieving an aggressive integrated loudness target (via heavy limiting) is one of the most common ways a master ends up with little or no true-peak headroom in the first place — the two problems are correlated in practice even though they're conceptually independent measurements.

## Setting the Final Limiter

In practice, this means the final brickwall limiter on a master bus should be configured with a true-peak-aware ceiling setting (most modern mastering limiters offer a "true peak" or "ISP" mode using internal oversampling) rather than a plain sample-peak ceiling, set to -1dBTP or lower rather than 0dBFS, regardless of how loud or quiet the genre's integrated LUFS target is.

## Common Mistakes

**Using a limiter's plain sample-peak ceiling instead of its true-peak/oversampling mode.** A limiter set to stop at exactly 0dBFS on sample peaks alone can still produce inter-sample overshoots above 0dBTP.

**Assuming a quieter, more dynamic master is automatically safe from this issue.** True-peak overshoot is primarily a function of how hard the limiter/clipper stage pushes near the ceiling, not directly of the integrated loudness target — a dynamic master pushed right up to 0dBFS on peaks can still have an inter-sample peak problem even at a modest integrated LUFS.

## Cross-References

- `knowledge_base/mastering/streaming/platform_normalization_behavior.md` — the source of the true-peak-as-separate-concern guidance this entry expands on
- `knowledge_base/mastering/dynamics/compression_and_clipping_as_aesthetic.md` — the limiting/clipping techniques whose final-stage settings need true-peak awareness
- `knowledge_base/mastering/loudness/lufs_targets_by_genre.md` — the integrated-loudness side of mastering decisions, independent of but commonly set alongside true-peak headroom
