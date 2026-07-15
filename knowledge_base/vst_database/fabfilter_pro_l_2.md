---
plugin_name: "Pro-L 2"
developer: "FabFilter"
category: "limiter"
type: "true-peak mastering limiter"
cpu_usage: "medium"
best_genres:
  - pop
  - house
  - techno
  - hip_hop
  - trap
strengths:
  - "Four selectable limiting-style algorithms (Transparent, Dynamic, Punchy, Modern — plus Aggressive, Bus, and Safe variants) each shape gain reduction differently, covering everything from clean mastering transparency to EDM/rock loudness to drum-bus-specific limiting from one plugin."
  - "Dedicated true-peak limiting mode detects and controls inter-sample overshoots directly, rather than requiring a separate oversampling/ISP-safety plugin downstream of the limiter."
  - "Extensive, standards-compliant loudness metering (including LUFS integrated/short-term/momentary) is built into the same plugin doing the limiting, so a mastering engineer can watch the loudness target and the limiting behavior in one window."
  - "Up to 32x linear-phase oversampling gives high internal sound quality even at aggressive gain-reduction settings, and the Safe algorithm specifically prioritizes avoiding audible distortion over maximum loudness when transparency matters more than level."
weaknesses:
  - "Heavier CPU load than a simple single-algorithm brickwall limiter, since Pro-L 2 runs its loudness metering, multiple selectable algorithms, and high oversampling ratios within one plugin instance."
  - "The style-algorithm choice is a real decision with audible consequences, not a cosmetic preset name — picking the wrong style (e.g., a mastering-transparent style on a genre that wants aggressive, in-your-face limiting, or vice versa) works against the genre's documented character."
alternatives:
  - "Waves L2 Ultramaximizer (a simpler, historically significant wideband limiter without Pro-L 2's multiple selectable algorithms — see `knowledge_base/vst_database/waves_l2_ultramaximizer.md`)"
  - "iZotope Ozone's built-in maximizer module (bundled within a full mastering-suite workflow rather than a standalone limiter — see `knowledge_base/vst_database/izotope_ozone.md`)"
  - "Ableton's stock Limiter (simpler, no selectable style algorithms or true-peak mode)"
recommended_settings:
  - "Transparent mastering pass on a dynamic-range-preserving genre (post_rock, progressive_rock, ambient): Transparent or Safe style, true-peak mode enabled, ceiling at -1dBTP or lower per `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md`, gain reduction kept light enough that `knowledge_base/mastering/dynamics/brickwall_limiting_artifacts.md`'s pumping/smearing checks come back clean."
  - "Loud-tier EDM/pop master (house, trance, trap): Punchy or Modern style for transient-preserving loudness, true-peak ceiling still set to -1dBTP regardless of how aggressive the integrated LUFS target is, per `true_peak_and_intersample_peaks.md`'s point that true-peak headroom and integrated loudness are independent decisions."
  - "Drum bus or individual-track limiting at the mix stage (not mastering): Bus style, which FabFilter designed specifically for this narrower, per-track use case rather than full-mix mastering."
common_uses:
  - "Final-stage mastering limiter setting the last-word ceiling on a track's output level"
  - "True-peak-aware loudness maximization for streaming-platform-safe delivery"
  - "Drum-bus or individual-track limiting at the mix stage using the Bus algorithm"
tags: ["fabfilter", "pro-l-2", "limiter", "true-peak", "mastering", "loudness"]
---

# Pro-L 2

Pro-L 2 (FabFilter) is a true-peak-aware mastering limiter offering multiple selectable limiting-style algorithms, standards-compliant loudness metering, and up to 32x linear-phase oversampling, positioned as the final-stage tool in a mastering chain that FabFilter's other plugins (Pro-Q 3 for EQ, Pro-C 2 for compression, already documented in this knowledge base) handle earlier. It's the natural limiter counterpart to those two entries, sharing FabFilter's low-CPU, precisely-metered design philosophy while addressing the specific mechanical concerns — brickwall ceiling behavior, lookahead, and true-peak/ISP overshoot — covered in `knowledge_base/mastering/dynamics/limiter_types_and_algorithms.md`.

## Sound Character and Strengths

Pro-L 2's style algorithms are its defining feature, functioning the same way Pro-C 2's compression styles do: rather than one fixed limiting character, the same plugin instance can be set to Transparent or Safe for a mastering pass on a dynamic-range-preserving genre, or Punchy/Modern/Aggressive for a loud-tier EDM or pop master that wants maximum perceived impact. This maps directly onto the limiter-aggressiveness tiers documented in `knowledge_base/mastering/dynamics/limiter_types_and_algorithms.md` — genres like post_rock and ambient that explicitly warn against heavy brickwall limiting are served by the gentler styles, while genres in the "loudest tier" (per `knowledge_base/mastering/loudness/lufs_targets_by_genre.md`) are better matched to the more aggressive ones. Its true-peak limiting mode directly implements the guidance in `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md`: rather than requiring a separate oversampling safety check downstream, Pro-L 2 detects inter-sample overshoots — including ones already present in the input signal, not just ones its own gain reduction might introduce — and attenuates them as part of the same limiting pass.

## Weaknesses

Running loudness metering, multiple algorithm options, and high-ratio oversampling in one plugin instance costs more CPU than a minimal single-algorithm limiter, which matters in large sessions running many mastering-chain instances at once. The style selector is also a genuine decision point rather than a set-and-forget default — using Aggressive or Modern on a genre whose own documentation calls for restraint (per `knowledge_base/mastering/dynamics/brickwall_limiting_artifacts.md`'s citations of `coldwave.md` and `arena_rock.md` warning against heavy brickwall limiting) works directly against that genre's intended dynamic character.

## Common Mistakes

Leaving the true-peak mode disabled because the integrated LUFS target already reads correctly on a standard meter — per `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md`, integrated loudness and true-peak safety are independent measurements, and a track can hit its LUFS target while still overshooting 0dBTP after lossy encoding or platform transcoding if true-peak mode isn't engaged. Defaulting to one style algorithm regardless of genre, the same mistake Pro-C 2's entry documents for its own style selector — the choice materially changes the limiter's audible character and needs to match what the genre's dynamics documentation actually calls for.

## Cross-References

- `knowledge_base/mastering/dynamics/limiter_types_and_algorithms.md` — the mechanical breakdown of brickwall, lookahead, and true-peak-aware limiting this plugin implements
- `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md` — the true-peak/ISP concern Pro-L 2's dedicated true-peak mode directly addresses
- `knowledge_base/mastering/dynamics/brickwall_limiting_artifacts.md` — the pumping/transient-smearing artifacts to check for regardless of which style algorithm is chosen
- `knowledge_base/mastering/dynamics/clipping_vs_limiting.md` — the mechanical distinction between this plugin's gain-reduction-based limiting and clipping-based loudness tools used in the loudest-tier genres
- `knowledge_base/vst_database/fabfilter_pro_q_3.md`, `knowledge_base/vst_database/fabfilter_pro_c_2.md` — the EQ and compression stages typically preceding this plugin in a FabFilter-based mastering chain
- `knowledge_base/vst_database/waves_l2_ultramaximizer.md` — an older, simpler wideband limiter historically central to loudness-war-era mastering
