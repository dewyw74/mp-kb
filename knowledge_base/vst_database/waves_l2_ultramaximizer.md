---
plugin_name: "L2 Ultramaximizer"
developer: "Waves"
category: "limiter"
type: "wideband peak limiter and maximizer with dithering"
cpu_usage: "low"
best_genres:
  - contemporary_country
  - country_pop
  - pop
  - trap
  - hip_hop
strengths:
  - "A wideband brickwall limiter with a simple threshold/ceiling/output workflow made it fast to push a master to a hard, competitive loudness level with minimal setup — a large part of why it became a default tool during the CD-era loudness war."
  - "IDR (Increased Digital Resolution) dithering, built into the same plugin as the limiting stage, lets a high-bit-depth master be reduced to a target bit depth (e.g., 24-bit to 16-bit for CD) while preserving more perceived dynamic range than an undithered bit-depth reduction would."
  - "Very low CPU cost, reflecting its late-1990s origin — practical to run without meaningfully taxing a session even by modern standards."
  - "Simple enough interface (threshold, ceiling/output level, release, dithering options) that it remains a fast, low-friction way to hear how hard a mix can be pushed before audible artifacts appear, independent of whether that aggressive setting is the final choice."
weaknesses:
  - "Wideband design processes the entire frequency spectrum with the same gain-reduction behavior, so a loud low-end transient (a kick or 808) triggers gain reduction across the whole signal, including highs and mids that didn't need it — the L3 Multimaximizer's multiband design exists specifically to address this limitation."
  - "No true-peak/ISP-aware limiting mode — L2 was designed before inter-sample peak management was standard practice in mastering limiters, so a master that reads safe on L2's meters can still overshoot 0dBTP after lossy encoding (see `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md`)."
  - "Historically associated with the loudness-war-era practice of maximizing level at the expense of dynamic range, which is directly counter to genres in this knowledge base that treat dynamic-range preservation as essential (post_rock, progressive_rock, ambient)."
alternatives:
  - "FabFilter Pro-L 2 (true-peak-aware, multiple selectable limiting styles — see `knowledge_base/vst_database/fabfilter_pro_l_2.md`)"
  - "Waves L3 Multimaximizer (multiband version of the same IDR/threshold/ceiling design, addressing the wideband limitation)"
  - "iZotope Ozone's maximizer module (bundled within a full mastering-suite workflow — see `knowledge_base/vst_database/izotope_ozone.md`)"
recommended_settings:
  - "CD-era-style loud master (contemporary_country, country_pop's documented -7 to -9 LUFS competitive targets): moderate-to-aggressive threshold reduction, output ceiling left with a small safety margin below 0dBFS, IDR dithering enabled if delivering at a reduced bit depth."
  - "Historical/reference use — understanding loudness-war-era mastering: push threshold hard enough to produce audible pumping and transient smearing deliberately, as a reference for what `knowledge_base/mastering/dynamics/brickwall_limiting_artifacts.md`'s pumping and transient-smearing checks are listening for, then compare against a true-peak-aware modern limiter at matched loudness."
common_uses:
  - "Fast, simple wideband loudness maximization on a master bus"
  - "Bit-depth reduction with IDR dithering when delivering at a lower bit depth than the mix was produced at"
  - "Historical reference point for loudness-war-era brickwall limiting practice"
tags: ["waves", "l2", "ultramaximizer", "limiter", "loudness-war", "dithering", "mastering"]
---

# L2 Ultramaximizer

The L2 Ultramaximizer (Waves) is a wideband brickwall peak limiter with built-in IDR dithering, and one of the plugins most directly associated with the CD-era "loudness war" documented in `knowledge_base/mastering/loudness/loudness_war_history_and_reaction.md`. Alongside its predecessor L1, the L2 became a standard tool for pushing masters to competitive loudness levels through the 1990s and 2000s, before true-peak-aware limiting and streaming-platform loudness normalization changed the competitive incentives around maximum-loudness mastering. Its successor, the L3 Multimaximizer, addressed the L2's core limitation — wideband-only gain reduction — by splitting the signal into up to five separately limited frequency bands, but the L2's simpler wideband design remains the historically significant reference point and is still in active use for fast, straightforward loudness maximization.

## A Loudness-War-Era Tool, Documented Directly in This Knowledge Base's Mastering Corpus

`knowledge_base/mastering/loudness/loudness_war_history_and_reaction.md` documents the broader historical pattern this plugin was built for and helped drive: "CD-era loudness increases accelerated through the 1990s-2000s as digital limiting made squeezing more perceived loudness out of a fixed 0dBFS ceiling technically easy." Two genre files in this knowledge base name the resulting competitive loudness pressure directly in language that describes exactly the kind of processing an L2-style wideband limiter is built to deliver: `contemporary_country.md` states "Masters are pushed to extreme levels (-7 to -9 LUFS) using heavy limiting and clipping. The goal is to sound massive and punchy on the radio, sacrificing the natural dynamic range of the acoustic instruments for sheer commercial power," and `country_pop.md` documents the identical competitive pressure: "the masters are incredibly loud (-7 to -9 LUFS). Heavy limiting is used to crush the dynamic range, ensuring the track explodes out of radio speakers." Neither genre file names the L2 by product name, but the -7 to -9 LUFS wideband-limiting behavior they describe is precisely the sound this class of limiter produces, and the L2 specifically is the tool most identified with that mastering era.

## Sound Character and Strengths

The L2's threshold/ceiling/release workflow is deliberately simple compared to a modern multi-algorithm limiter like Pro-L 2 — there's no style selector, just a threshold that determines how much gain reduction is applied and an output ceiling that sets the hard maximum level. IDR dithering, built into the same plugin, remains a genuinely useful feature independent of the limiter's loudness-war reputation: reducing a 24-bit master to a 16-bit delivery format with IDR's noise-shaped dither preserves more perceived dynamic range than a plain truncation would.

## Weaknesses

Because the L2 is a purely wideband limiter, a single loud low-frequency transient (a kick drum, an 808 hit) triggers gain reduction across the entire frequency spectrum simultaneously, pulling down the highs and mids along with the low end that actually triggered it — this is the specific limitation the L3's multiband design was built to solve, and it's a real audible difference on bass-heavy modern genres. The L2 also predates true-peak/ISP-aware limiting as standard mastering practice (per `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md`), so a master that reads safe on the L2's own sample-peak meters can still produce inter-sample overshoots after lossy encoding or platform transcoding — a true-peak meter needs to be checked separately when using this plugin for a genuinely modern streaming-delivery master.

## Common Mistakes

Applying L2-style aggressive wideband limiting to a genre that explicitly documents dynamic-range preservation as essential — per `knowledge_base/mastering/loudness/loudness_war_history_and_reaction.md`'s "Reaction" section, genres like post_rock, progressive_rock, and ambient treat exactly this kind of heavy limiting as actively damaging to the music's intent, the direct opposite of what contemporary_country and country_pop's competitive loudness pressure calls for. Trusting the L2's sample-peak-only metering as sufficient for a final streaming master without a separate true-peak check, given the plugin predates true-peak-aware limiter design.

## Cross-References

- `knowledge_base/mastering/loudness/loudness_war_history_and_reaction.md` — the historical context this plugin is most directly associated with, including the Death Magnetic flashpoint and the standardization-driven reaction against loudness-war mastering
- `knowledge_base/mastering/dynamics/limiter_types_and_algorithms.md` — the mechanical distinction between wideband, brickwall, and true-peak-aware limiter types this entry's weaknesses section draws on
- `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md` — the true-peak/ISP concern this plugin's design predates and doesn't address natively
- `knowledge_base/mastering/dynamics/brickwall_limiting_artifacts.md` — the pumping and transient-smearing artifacts this class of aggressive wideband limiting is prone to producing
- `knowledge_base/genres/country/contemporary_country.md`, `knowledge_base/genres/country/country_pop.md` — the genre files documenting the -7 to -9 LUFS competitive loudness pressure this plugin was historically used to achieve
- `knowledge_base/vst_database/fabfilter_pro_l_2.md` — a modern, true-peak-aware, multi-style alternative for the same final-limiting-stage role
