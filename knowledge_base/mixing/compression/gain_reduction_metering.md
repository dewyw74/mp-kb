---
technique_name: "Reading a Compressor's Gain-Reduction Meter"
category: compression
problem_solved: "Setting a compressor by ear or genre convention alone with no way to verify how much work it's actually doing, leading either to under-compression that doesn't reach the genre's target consistency, or over-compression that isn't obvious until the transient/dynamic damage is already audible in the mix"
parameters:
  light_glue_range: "Roughly 2-4dB of gain reduction for transparent bus glue or gentle vocal riding, per classic_rock.md's drum-bus figure and vocal_trance.md's vocal-compression figure — both land in the same range despite being applied to very different sources"
  heavy_range: "Multiple dB, often sustained and deep, for genres that treat heavy compression/limiting as a deliberate character rather than a transparent finishing touch (death_metal's drum-bus limiting, contemporary_country's loudness-war mastering)"
  near_zero_range: "Minimal-to-no sustained gain reduction, reserved for catching only occasional peaks, in genres where dynamic range preservation is the explicit goal (ambient and similar)"
  what_to_watch: "The meter's overall movement pattern — how often it moves, how far, how quickly it returns to zero — rather than only its peak value; a meter resting at -4dB most of the time describes a far more compressed result than one that occasionally flickers to -4dB and springs back immediately"
signal_chain_position: "Read directly on the compressor's own gain-reduction meter/display during mixing or mastering, rather than via a separate metering insert"
genre_applicability:
  - classic_rock
  - vocal_trance
  - post_grunge
  - heavy_metal
  - death_metal
  - ambient
  - contemporary_country
related_techniques:
  - limiting_vs_compression
  - parallel_compression
tags: ["gain-reduction", "GR-meter", "metering", "compression"]
---

# Reading a Compressor's Gain-Reduction Meter

**A note on grounding for this entry:** most genre files describe compressor settings in terms of ratio, attack, and a qualitative label ("moderate," "heavy," "transparent") rather than a specific gain-reduction meter reading. Only two files in the corpus give a literal dB-of-reduction figure. This entry uses those two citations as calibration anchors, then reasons from the ratio/attack descriptions genre files do give — and from what those settings would typically produce on a meter — to build out the rest of the picture. Grounding here is moderate: real, but requiring more inference than most technique entries in this category.

## The Two Documented Numeric Anchors

`classic_rock.md`'s mixing section gives an explicit figure for drum-bus glue compression: "Moderate bus compression for glue (2-4 dB gain reduction), individual compression on vocals and bass for consistency." `vocal_trance.md` gives an almost identical figure for a completely different source — a lead vocal: "Vocal-focused compression (often 2-4dB of gentle riding plus parallel compression) keeps the vocal consistently present against a loud, dense trance backing track." Both land in the same 2-4dB range despite the different source material, which is worth noting as a rough shared reference point for what "moderate/glue-level" compression tends to read as on a GR meter in this knowledge base's genre practice — though with only two data points, it shouldn't be generalized into a universal number that applies regardless of source or genre.

## Translating Ratio and Attack Descriptions Into an Expected GR Range

`post_grunge.md`'s drum bus setting — "2:1 ratio, medium attack" — and its vocal compressor — "fast-attack vocal compressor (3:1) to control peaks while retaining dynamics" — describe compressors configured for transparent, moderate control on genre-typical source material. Settings in that range generally produce a GR reading in the same low-single-digit-dB territory as `classic_rock.md`'s and `vocal_trance.md`'s explicitly stated 2-4dB, even though `post_grunge.md` itself doesn't cite a meter number directly. `heavy_metal.md`'s "slower attack compression on the drum bus to let the transients smack" is worth reading specifically as a setting built to keep the meter from registering strong gain reduction on the initial transient at all — the slow attack lets the hit pass essentially unprocessed, with gain reduction only showing up once the compressor catches up to the sustain portion.

## When the Meter Should Be Showing Much More

`death_metal.md`'s description of drum-bus limiting — "Limiters are used on the drum bus to keep the blast beats perfectly even and relentless" — describes a goal that, translated to a meter reading, means the GR display sitting deep and largely constant rather than lightly flickering; "relentless" is really a description of what a heavily and continuously worked gain-reduction meter looks like, even though the genre file doesn't state a number. `contemporary_country.md`'s mastering approach — "Masters are pushed to extreme levels (-7 to -9 LUFS) using heavy limiting and clipping" — implies a comparable "meter parked deep, most of the time" reading at the mastering stage, for a loudness-competitiveness reason rather than a rhythmic-evenness one.

## When the Meter Should Barely Move

`ambient.md` describes the opposite target explicitly: "Preserve wide dynamic range; minimal limiting, no brickwall squashing — the genre's power comes from headroom and space," with its mastering notes adding that "limiting is used sparingly, mostly to catch stray peaks from reverb tails rather than to raise perceived loudness." Read as a meter description, this means a GR display sitting at 0dB the large majority of the time, only flickering briefly on an occasional, isolated peak — any more consistent movement than that would already be over-processing relative to the genre's stated goal.

## Watching the Pattern, Not Just the Peak Value

A GR meter's peak reading alone doesn't distinguish between two very different-sounding results: a compressor that occasionally spikes to -4dB and immediately springs back (audible only as a brief, controlled catch on the loudest hits) versus one that sits at -4dB continuously (audible as a constantly-engaged, more heavily-processed character throughout). The genre citations above only ever describe outcomes — "moderate glue," "relentless," "sparingly, mostly to catch stray peaks" — which are really descriptions of a GR meter's *pattern* over time, not a single instantaneous number. Reading a meter well means watching how often and how long it's engaged, not just how deep it reads at its worst moment.

## Common Mistakes

**Chasing a specific dB number without regard for source or genre context.** 2-4dB of reduction on a drum bus (`classic_rock.md`) reads completely differently in practice than 2-4dB on an already-quiet vocal (`vocal_trance.md`) — the number alone doesn't tell you whether the result is appropriate for the material.

**Judging a compressor only by its peak GR reading rather than how much of the time it's actively reducing gain.** A meter that spikes briefly is a very different (and often more transparent) result than one sitting at the same peak value continuously, even though both would report an identical "worst-case" number.

**Assuming heavy, constant visible gain reduction is inherently a mixing mistake.** `death_metal.md` and `contemporary_country.md` both document a GR meter parked deep and constant as exactly the genre-appropriate target, not a sign of over-compression to correct.

## Cross-References

- `knowledge_base/genres/rock/classic_rock.md` and `knowledge_base/genres/edm/vocal_trance.md` — the two explicit 2-4dB gain-reduction figures this entry anchors on
- `knowledge_base/genres/rock/post_grunge.md` — ratio/attack settings implying a comparable moderate GR range without stating a meter number directly
- `knowledge_base/genres/metal/heavy_metal.md` and `knowledge_base/genres/metal/death_metal.md` — attack time controlling whether GR registers on the transient or only the sustain, and how deep/constant the meter reads for a "relentless" genre target
- `knowledge_base/genres/electronic/ambient.md` — the near-zero, peaks-only GR pattern appropriate to dynamic-range-preserving genres
- `knowledge_base/genres/country/contemporary_country.md` — a deep, constant GR pattern appropriate to loudness-war mastering
- `knowledge_base/mixing/compression/limiting_vs_compression.md` — the related question of when gain reduction should come from a proportional compressor versus a hard-ceiling limiter
- `knowledge_base/mixing/compression/parallel_compression.md` — a technique where the parallel bus's compressor is deliberately set to show much heavier GR than would ever be used on a direct chain
