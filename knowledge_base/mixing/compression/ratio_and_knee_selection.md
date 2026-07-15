---
technique_name: "Ratio and Knee Selection"
category: compression
problem_solved: "A compressor's gain reduction being either too obtrusive (flattening dynamics a genre depends on) or too weak (failing to control peaks/level that need active management), because the ratio was set from a generic default rather than from what the source and genre actually call for"
parameters:
  low_ratio: "1.5:1 to 2:1 — used for transparent glue where the compressor's job is to unify level without being heard as compression at all"
  moderate_ratio: "2:1 to 3:1 — used for controlled punch/consistency on a bus or element where some audible gain reduction is acceptable but flattening dynamics is not the goal"
  higher_ratio: "4:1 and up — reserved in this corpus for peak control on individual elements (vocals) or for deliberately aggressive/effect-style processing (sidechain ducking, parallel compression), not for general-purpose glue"
  knee: "Soft knee gradually increases the compression ratio around the threshold for a smoother, less audible onset of gain reduction; hard knee applies the full ratio abruptly once the threshold is crossed, for more decisive, obviously-engaged control — general audio-engineering theory, not a term used explicitly in this knowledge base's genre files"
signal_chain_position: "A parameter choice within any compressor insert — individual element, bus, or master"
genre_applicability:
  - modal_jazz
  - ambient
  - bluegrass
  - stoner_metal
  - post_grunge
related_techniques:
  - attack_and_release_time_science
  - bus_glue_compression
  - sidechain_pumping
  - parallel_compression
tags: ["ratio", "knee", "soft-knee", "hard-knee", "compression", "dynamics-control"]
---

# Ratio and Knee Selection

Ratio decides how hard a compressor reacts once a signal crosses its threshold — a low ratio nudges level down gently, a high ratio clamps it firmly. Across this knowledge base's genre files, ratio choice tracks a consistent pattern: genres and elements where the point is invisible glue specify low ratios, while genres and elements where the point is active peak control or a deliberately audible effect specify higher ones.

## Low Ratios for Transparent Glue

`modal_jazz.md` makes the clearest case for restraint: "Very light bus compression if any — the genre's dynamic subtlety (soft passages building to intense but still acoustic peaks) is part of its expressive vocabulary and should not be flattened," and its production notes specify "careful stereo bus glue compression (very low ratio, slow attack) to unify a multi-mic acoustic ensemble without killing dynamics." `ambient.md` lands in a similar range for a different reason — sustained tone rather than acoustic dynamics: "Light bus compression (1.5:1-2:1, slow attack/release) for glue; avoid pumping — ambient relies on sustained, unbroken tone." `bluegrass.md` doesn't give a number but states the same intent in plain language: "Use extremely transparent optical compression or fast FET compression just to catch the harsh transients of the banjo and mandolin. Do not squash the mix." All three treat a low ratio as the mechanism for compressing without the compression being audible as compression.

## Moderate Ratios for Controlled Punch

`stoner_metal.md` and `post_grunge.md` both specify a 2:1 ratio on a drum bus — high enough to add consistency and punch, low enough to leave the kit's transient character intact. `stoner_metal.md`: "Gentle bus compression on drums (2:1 ratio, 30 ms attack) to glue the kit." `post_grunge.md`: "Bus compression on drums (2:1 ratio, medium attack), parallel compression on guitars for thickness, vocal compression with fast attack and medium release to control peaks," restated later as "Compression uses a 2:1 ratio on the drum bus with medium attack to preserve transients." The ratio here sits a step above the transparent-glue range used in `modal_jazz.md` and `ambient.md` — these are rock/metal drum busses that need audible punch and consistency, not acoustic-ensemble subtlety, but they still stop well short of aggressive peak-limiting ratios.

## Higher Ratios for Peak Control, Not Glue

`post_grunge.md` uses a noticeably higher ratio on its lead vocal within the same track: "a fast-attack vocal compressor (3:1) to control peaks while retaining dynamics." The jump from 2:1 on the drum bus to 3:1 on the vocal isn't arbitrary — the drum bus's job is glue across a full kit, while the vocal compressor's job is actively catching peaks on a single, more dynamically erratic source. This corpus's other documented high-ratio use cases live outside pure bus-glue territory entirely: `knowledge_base/mixing/compression/sidechain_pumping.md` specifies "4:1 to 10:1 (often deliberately extreme for an audible pump)" because the pump is meant to be heard, and `knowledge_base/mixing/compression/parallel_compression.md` specifies "6:1 to 20:1... deliberately aggressive since it's blended rather than applied directly." Read together with the glue-oriented genre files above, a pattern emerges: ratio tracks audibility intent, not genre intensity alone — even an aggressive metal drum bus (`stoner_metal.md`) stays at a gentle 2:1 when the job is glue, while a pop vocal or a sidechain duck reaches for far higher ratios because being heard is the point.

## Knee: General Theory, Lightly Grounded in This Corpus

None of the surveyed genre files name knee curve (hard vs soft) explicitly by that term, so this section leans on general audio-engineering theory rather than knowledge-base citations. A hard knee applies a compressor's full ratio the instant the signal crosses threshold, producing a more decisive, sometimes more audible onset of gain reduction — useful when a compressor's engagement is meant to be a clear, defined event (peak-limiting, aggressive bus glue). A soft knee ramps the ratio up gradually across a range straddling the threshold, so gain reduction begins subtly before the signal has fully crossed it and increases smoothly rather than snapping on — the mechanism behind why opto and vari-mu topologies (see `knowledge_base/mixing/compression/compressor_topology_comparison.md`) read as inherently more "musical" than fast VCA/FET circuits, since their natural knee behavior tends toward soft regardless of the ratio dialed in. Given the low-ratio, glue-oriented settings `modal_jazz.md` and `ambient.md` describe, a soft knee is the theoretically consistent choice for that use case even though neither file names the parameter directly — the entire goal in both citations is gain reduction that isn't perceived as a discrete event.

## Common Mistakes

**Defaulting to a "safe" moderate ratio regardless of the job.** `modal_jazz.md`'s "very low ratio" glue compression and `post_grunge.md`'s higher-ratio vocal peak control are solving different problems — a one-size ratio setting used everywhere in a mix will either over-flatten the glue application or under-control the peak-limiting one.

**Treating a high ratio as inherently "more compressed" without considering knee and attack together.** A high-ratio compressor with a slow attack and soft knee can sound gentler than a low-ratio compressor with a fast attack and hard knee — ratio alone doesn't determine audibility, which is why `stoner_metal.md` and `post_grunge.md` pair their moderate ratios with a specific attack time rather than leaving it unstated.

**Assuming acoustic-ensemble genres want the same glue ratio as rock/metal drum busses.** `modal_jazz.md`'s "very low ratio" is meaningfully lower than `stoner_metal.md` and `post_grunge.md`'s 2:1 — applying a rock drum bus's ratio to a jazz ensemble risks exactly the dynamic flattening `modal_jazz.md` warns against.

## Cross-References

- `knowledge_base/genres/jazz/modal_jazz.md` — very-low-ratio, slow-attack bus glue as a deliberate dynamics-preservation choice
- `knowledge_base/genres/electronic/ambient.md` — a specific 1.5:1-2:1 range chosen to avoid audible pumping on sustained tone
- `knowledge_base/genres/country/bluegrass.md` — transparent, non-squashing compression stated in plain language rather than a ratio number
- `knowledge_base/genres/metal/stoner_metal.md` — a 2:1 drum-bus ratio for punch without flattening
- `knowledge_base/genres/rock/post_grunge.md` — a 2:1 drum-bus ratio contrasted with a 3:1 vocal ratio within the same track
- `knowledge_base/mixing/compression/sidechain_pumping.md` — a deliberately aggressive 4:1-10:1 ratio range, used for the opposite reason (audible effect, not invisible glue)
- `knowledge_base/mixing/compression/parallel_compression.md` — a 6:1-20:1 aggressive-ratio range used specifically because it's blended rather than applied directly
- `knowledge_base/mixing/compression/compressor_topology_comparison.md` — how opto/vari-mu circuits' natural soft-knee behavior relates to the low-ratio glue use cases documented here
