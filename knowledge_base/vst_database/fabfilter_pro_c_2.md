---
plugin_name: "Pro-C 2"
developer: "FabFilter"
category: "compressor"
type: "VCA-style digital compressor with multiple character algorithms"
cpu_usage: "low"
best_genres:
  - house
  - trance
  - hip_hop
  - pop
  - trap
strengths:
  - "Selectable compression 'style' algorithms (Clean, Classic, Opto, Vocal, Mastering, Bus, Punch) let one plugin cover a wide range of compressor character without switching tools."
  - "Clear, real-time gain-reduction and level metering makes it easy to dial in exact attack/release behavior by eye as well as by ear."
  - "Low CPU usage, making it practical to instantiate on many channels including for parallel compression setups."
  - "Range control lets gain reduction be capped at a maximum amount, useful for sidechain-ducking and parallel compression where an extreme setting shouldn't fully silence the source."
weaknesses:
  - "Its clean, precise digital character means it doesn't add the analog-style harmonic coloration that some hardware-emulation compressors (SSL bus comp emulations, 1176-style plugins) provide as part of their sound."
  - "The style-algorithm selector adds a decision point that a simpler, single-character compressor doesn't require — useful flexibility, but another choice to make correctly."
alternatives:
  - "Waves CLA-76 (1176-style character)"
  - "Ableton Compressor / Glue Compressor (stock)"
  - "Xfer OTT (for multiband/parallel character)"
recommended_settings:
  - "Sidechain pumping: Punch or Classic style, fast attack (0-1ms), release synced to a 16th or 8th note, ratio 4:1-10:1, sidechain input from the kick — see `knowledge_base/mixing/compression/sidechain_pumping.md`."
  - "Parallel compression (drum bus): Bus or Classic style, low threshold, high ratio (8:1+), Range control capped so the compressed signal stays usable when blended back in — see `knowledge_base/mixing/compression/parallel_compression.md`."
common_uses:
  - "Sidechain ducking/pumping compression"
  - "Parallel (New York-style) compression on drum and vocal buses"
  - "General-purpose vocal and instrument dynamics control"
tags: ["fabfilter", "pro-c-2", "compressor", "sidechain", "parallel-compression", "mixing"]
---

# Pro-C 2

Pro-C 2 (FabFilter) is a digital compressor offering several selectable "style" algorithms — Clean, Classic, Opto, Vocal, Mastering, Bus, and Punch — each modeling a different compression character, from transparent and precise to more colored, program-dependent behavior reminiscent of specific hardware compressor types. Its clear metering and low CPU cost have made it a common default choice for both surgical dynamics control and more deliberately audible compression effects like sidechain pumping.

## Sound Character and Strengths

The style selector is Pro-C 2's defining feature — rather than choosing between several separate compressor plugins for different jobs, one plugin instance can be set to Opto-style smooth leveling for a bass part, Punch-style transient-preserving compression for drums, or Bus-style glue compression for a mix bus, each with genuinely different response character rather than just different default parameter values. Its Range control (capping maximum gain reduction) is particularly useful for the sidechain-pumping and parallel-compression techniques documented elsewhere in this knowledge base, where an aggressive ratio/threshold shouldn't be allowed to fully silence the source signal.

## Weaknesses

Pro-C 2's precision is also its main limitation relative to hardware-emulation compressors: it doesn't add the harmonic saturation or the specific nonlinear behavior that plugins explicitly modeling an SSL bus compressor or a 1176 provide as part of their character. For mixes that want that specific coloration as an aesthetic choice, a dedicated hardware-emulation plugin is a better fit even though Pro-C 2 can approximate the gain-reduction behavior.

## Common Mistakes

Leaving the style selector on its default (usually Clean) regardless of the task — the style choice materially changes the compressor's behavior, and picking Punch for a sidechain pump or Opto for a vocal bus (rather than defaulting to Clean for everything) makes a real audible difference.

## Cross-References

- `knowledge_base/mixing/compression/sidechain_pumping.md`, `knowledge_base/mixing/compression/parallel_compression.md` — the two techniques this plugin's Range control and style algorithms directly support
- `knowledge_base/vst_database/fabfilter_pro_q_3.md` — commonly paired in a mix chain
- `knowledge_base/vst_database/xfer_ott.md` — a multiband alternative when single-band compression isn't precise enough for the target frequency range
