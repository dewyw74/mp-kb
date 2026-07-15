---
technique_name: Drum Bus Compression
category: compression
problem_solved: "Individually well-processed drum elements (kick, snare, overheads, room) still sounding disconnected or thin once summed, because gluing them into one cohesive-sounding group requires dynamics control applied to the summed bus itself, not just to the individual channels feeding it"
parameters:
  ratio: "Light-to-moderate for glue (roughly 2:1 to 4:1) in most rock/pop contexts; pushed to extreme, limiter-style ratios in some metal subgenres for a relentlessly even, machine-like feel"
  attack: "Ranges from medium (letting the initial transient smack through before gain reduction engages) to fast/extreme (evenness-over-punch, used deliberately in genres built on sustained, relentless drum patterns)"
  release: "Medium, tuned to recover between hits without audible pumping at the track's tempo"
  gain_reduction_amount: "Roughly 2-4dB for transparent glue-style bus compression; runs much deeper when the compression is being used for an aggressive, deliberately-crushed genre character"
signal_chain_position: "Compressor inserted on the summed drum bus/group — post-fader on the individual kick/snare/overhead/room channels, pre-master-bus — often paired with a separate parallel-compression send from the same bus"
genre_applicability:
  - classic_rock
  - post_grunge
  - heavy_metal
  - death_metal
  - jungle
  - bassline
  - jump_up
  - contemporary_r_and_b
  - big_beat
related_techniques:
  - parallel_compression
  - transient_shaping_for_punch_and_glue
  - multiband_compression_and_limiter_chain_ordering
tags: ["drum-bus", "glue-compression", "drum-group", "bus-compression"]
---

# Drum Bus Compression

Drum bus compression is dynamics processing applied directly to the summed kick/snare/overhead/room group — distinct from the mastering-stage, whole-mix glue covered in `bus_glue_compression.md`, and distinct from parallel compression, where the aggressive compressor sits on a separate blended send rather than the main signal path. The direct compressor on the bus is doing a specific job: taking a group of individually-tracked or individually-programmed elements and making them read as one cohesive-sounding drum kit once they hit tape (or the export) together.

## Moderate Glue: The Classic-Rock/Post-Grunge Default

`classic_rock.md` documents transparent, moderate settings as the default: "Moderate bus compression for glue (2-4 dB gain reduction), individual compression on vocals and bass for consistency; drums often compressed in parallel for punch without killing transients." `post_grunge.md` gives an almost identical figure with more specificity: "Bus compression on drums (2:1 ratio, medium attack)," restated later as "Compression uses a 2:1 ratio on the drum bus with medium attack to preserve transients." Both files land on a light ratio and a medium attack specifically to add cohesion without erasing the individual hits' character.

## Attack Time Is the Real Character Decision

The single biggest variable separating a "glued but still punchy" drum bus from a "crushed and relentless" one is attack time, not ratio. `heavy_metal.md` favors "slower attack compression on the drum bus to let the transients smack" — the compressor only grabs the sustain, leaving the kick and snare's initial hit untouched. `death_metal.md` goes the opposite direction entirely: "Extreme drum compression. Limiters are used on the drum bus to keep the blast beats perfectly even and relentless." At blast-beat tempos, evenness across hundreds of nearly-identical hits per minute becomes more important than any individual hit's transient snap, so the genre reaches for a fast, limiter-grade setting that would sound over-processed in almost any other context.

## Reassembling Chopped or Sequenced Material Into One Group

Drum bus compression isn't limited to live-tracked kits. `jungle.md` documents it as the final step in reassembling heavily chopped breakbeat material: "Individual break hits are often compressed hard for punch before re-assembly; bus compression across the drum group glues re-triggered slices back into a cohesive-sounding break." The individual-hit compression and the bus compression are doing different jobs in sequence — one shapes each slice, the other makes the reassembled sequence of slices sound like a single performance again. `bassline.md` and `jump_up.md` apply the same logic to sequenced/programmed EDM drums: "bus compression on the drum group keeps the groove tight and club-ready" and "drum bus compression for punch and glue" respectively, alongside separate sidechain and bass-bus processing handling other parts of the mix.

## Bus Compression Alongside Parallel Compression, Not Instead Of

`classic_rock.md`'s citation above pairs direct drum bus compression with parallel-compressed drums in the same sentence — the two are complementary layers rather than alternatives. The direct bus compressor handles overall glue and consistency at a moderate setting; the parallel send (see `knowledge_base/mixing/compression/parallel_compression.md`) can be pushed far more aggressively underneath it because it's blended rather than replacing the dry signal. Reaching for only one of the two techniques when a genre's reference sound calls for both typically leaves a drum bus sounding either glued-but-flat or punchy-but-disconnected.

## When Drum Bus Compression Becomes an Aesthetic, Not Just Glue

`big_beat.md` treats heavy drum bus compression as part of the genre's identity rather than a transparent finishing touch: "Heavy compression and saturation across drum bus and master for a loud, dense, rock-adjacent sound." `contemporary_r_and_b.md` sits closer to the transparent-glue end but still names it as a distinct, deliberate stage: "Glue compression on the drum bus," separate from the heavy vocal compression and sidechained bass processing happening elsewhere in the same chain.

## Common Mistakes

**Using the same attack/ratio settings regardless of genre.** `heavy_metal.md`'s slow-attack, transient-preserving approach and `death_metal.md`'s fast, limiter-grade approach solve for opposite goals (punch vs. relentless evenness) — copying one genre's settings into the other's context produces a drum bus that undermines the track's actual identity.

**Relying on bus compression alone to fix poorly balanced individual drum channels.** Per `jungle.md`'s two-stage approach, individual-hit shaping and bus-level glue are different jobs; a bus compressor asked to compensate for badly-leveled individual channels will either pump audibly or fail to actually glue the group.

**Treating direct bus compression and parallel compression as redundant.** `classic_rock.md` uses both simultaneously for a reason — dropping one because "we already have compression on the drum bus" loses either the transparent glue or the added punch/density the other provides.

## Cross-References

- `knowledge_base/genres/rock/classic_rock.md` — moderate glue-style bus compression combined with parallel compression on the same drum bus
- `knowledge_base/genres/rock/post_grunge.md` — specific 2:1, medium-attack drum bus settings
- `knowledge_base/genres/metal/heavy_metal.md` and `knowledge_base/genres/metal/death_metal.md` — attack time as the deciding factor between transient-preserving glue and relentless, limiter-grade evenness
- `knowledge_base/genres/edm/jungle.md` — bus compression reassembling individually-compressed chopped breakbeat hits into a cohesive group
- `knowledge_base/genres/edm/bassline.md` and `knowledge_base/genres/edm/jump_up.md` — drum bus compression on sequenced/programmed EDM drum groups
- `knowledge_base/genres/electronic/big_beat.md` and `knowledge_base/genres/r_and_b/contemporary_r_and_b.md` — drum bus compression ranging from aesthetic density to transparent glue
- `knowledge_base/mixing/compression/parallel_compression.md` — the complementary parallel-bus technique frequently paired with direct drum bus compression
