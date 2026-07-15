---
technique_name: "Limiting vs. Compression — Where the Functional Line Sits"
category: compression
problem_solved: "Treating a limiter and a compressor as interchangeable tools for 'making things louder or more even,' when genre practice documented across this knowledge base shows they're reached for at functionally different points in a chain — a compressor shapes dynamics and tone as a musical decision, a limiter enforces a hard ceiling — and using the wrong one, or the right one at the wrong intensity, either fails to control peaks or destroys the exact character the genre depends on"
parameters:
  compressor_ratio: "Typically well below 10:1, with the gain-reduction curve still shaping tone, sustain, and punch as a deliberate musical decision rather than an absolute cutoff"
  limiter_ratio: "Effectively infinity:1 (brickwall) above the threshold — no signal is allowed through above the ceiling at all, as opposed to a compressor's proportional reduction"
  where_each_sits: "Compression is used throughout the mix on individual elements and buses for tonal/dynamic shaping; limiting is normally reserved for the final safety ceiling before export, with a narrow set of genres deliberately moving a limiter earlier in the chain as a distortion/evenness effect"
  genre_specific_intensity: "Ranges from near-absent (ambient, glitch, post_rock-family genres avoiding limiting almost entirely to preserve dynamic contrast) to used-as-a-distortion-effect (industrial, death_metal's drum bus limiting for relentless evenness) to loudness-war-standard (contemporary_country, country_pop)"
signal_chain_position: "Compression: anywhere in the signal chain, on individual channels, buses, or the master. Limiting: almost always the last stage before the true-peak ceiling/export, with the documented genre exception of limiters used mid-chain as a deliberate distortion/evenness effect"
genre_applicability:
  - death_metal
  - heavy_metal
  - honky_tonk
  - bluegrass_gospel
  - outlaw_country
  - country_pop
  - contemporary_country
  - ambient
  - glitch
  - coldwave
  - industrial
  - breakbeat
related_techniques:
  - parallel_compression
  - drum_bus_compression
tags: ["limiting", "compression", "brickwall", "ceiling", "mastering", "dynamics"]
---

# Limiting vs. Compression — Where the Functional Line Sits

Technically, a limiter is just a compressor with a very high ratio (effectively infinity:1) and usually a very fast attack — the two tools sit on a continuum rather than being fundamentally different circuits. But genre practice documented across this knowledge base treats them as functionally distinct: compression is reached for continuously, throughout a mix, as a tone- and dynamics-shaping decision, while limiting is almost always reserved as the very last stage — the hard ceiling nothing is allowed to cross — with only a handful of genres deliberately breaking that convention.

## The Ceiling Job: Limiting as a Mastering-Stage Decision, Not a Mixing Tool

A large share of the genre corpus discusses "heavy limiting" as a single mastering-stage decision, distinct from any of the compression choices made earlier in the mix. `honky_tonk.md`'s mastering guidance: "avoid modern heavy limiting, which contradicts the genre's raw, dancehall character." `bluegrass_gospel.md`: "heavy limiting would be especially destructive to unaccompanied harmony singing." `outlaw_country.md`: "avoid modern heavy limiting, which would erase the genre's raw, live-band character." On the opposite end of the same axis, `country_pop.md` treats heavy limiting as the whole point: "Heavy limiting is used to crush the dynamic range, ensuring the track explodes out of radio speakers," and `contemporary_country.md` states it even more directly: "Masters are pushed to extreme levels (-7 to -9 LUFS) using heavy limiting and clipping." In every one of these citations, limiting is discussed as a mastering-stage yes/no decision about the finished mix's ceiling — never as a per-channel mixing tool the way compression is.

## Where Compression Stops and Limiting Begins on a Drum Bus

`death_metal.md` documents a genre exception to the "limiting only at the end" convention: "Extreme drum compression. Limiters are used on the drum bus to keep the blast beats perfectly even and relentless." That's a limiter placed mid-chain, on a drum bus, not at final mastering — because the genre's actual goal (perfectly even blast beats, not just an overall loudness ceiling) needs a hard, uncompromising cap on every single hit, not the proportional shaping a compressor provides. `heavy_metal.md` makes the contrast explicit by staying on the compression side of the line for a related but different goal: "Slower attack compression on the drum bus to let the transients smack" — heavy_metal wants the transient to survive and land, death_metal wants every transient forced to the exact same ceiling regardless of what it costs the transient's natural character.

## Genres That Avoid Limiting Almost Entirely

Several genres in the corpus document deliberately minimizing limiting because dynamic contrast is structurally part of the composition. `ambient.md`: "Preserve wide dynamic range; minimal limiting, no brickwall squashing — the genre's power comes from headroom and space," with its mastering notes adding "Limiting is used sparingly, mostly to catch stray peaks from reverb tails rather than to raise perceived loudness." `glitch.md` frames over-limiting as an outright genre-breaking mistake: "Over-limiting at mastering, which flattens the erratic dynamics that define the genre," alongside guidance that "heavy-handed limiting is avoided" since "sudden silence-to-noise jumps are a genre signature." `coldwave.md`: "avoid heavy brickwall limiting that would erase the drum machine's natural punch." `breakbeat.md` frames the same tradeoff in terms of the material limiting would destroy: "over-limiting flattens exactly the rhythmic detail that makes a well-chopped break compelling on a big sound system."

## When Limiting Becomes the Aesthetic Itself

`knowledge_base/mastering/dynamics/compression_and_clipping_as_aesthetic.md` documents a small group of genres — industrial and power electronics chief among them — where the line between compression and limiting collapses entirely on purpose. `industrial.md`, as quoted there, describes "extreme compression/limiting used as a distortion effect in its own right, not just for dynamic control." Read alongside `death_metal.md`'s mid-chain drum-bus limiter above, this shows the "limiting only at the very end, compression everywhere else" convention isn't a hard rule — it's the default that a specific, identifiable set of genres deliberately breaks for an artistic reason, not out of confusion about the tools.

## A Practical Rule for Choosing

If the goal is shaping tone, sustain, punch, or moment-to-moment level consistency across a performance — the kind of decision `classic_rock.md`'s 2-4dB bus glue or `post_grunge.md`'s 2:1 drum bus setting represent — reach for a compressor with a proportional ratio. If the goal is an absolute ceiling nothing may cross, whether that's a mastering-stage safety limit or, per the death_metal/industrial exception, a deliberately audible brickwall character, reach for a limiter. The genre files above consistently treat "how much limiting" as a separate decision from "how much compression," made at a different stage of the chain for a different reason.

## Common Mistakes

**Using a limiter to do a compressor's tone-shaping job.** A limiter's near-infinite ratio and fast attack will crush exactly the transient detail a genre like `heavy_metal.md` or `classic_rock.md` is trying to protect with a moderate compressor instead.

**Skipping a final limiter and relying on compression alone to manage the master's ceiling.** Compression's proportional gain reduction doesn't guarantee an absolute peak ceiling the way a limiter does — see `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md` for why a true-peak-aware limiter is still needed as the last stage even on a track mixed with light, transparent compression throughout.

**Assuming "heavy limiting" is always a mistake to avoid.** `death_metal.md` and `industrial.md` (via `compression_and_clipping_as_aesthetic.md`) document heavy limiting as a legitimate, deliberate genre choice — the mistake isn't heavy limiting itself, it's applying it to a genre like `honky_tonk.md` or `ambient.md` whose entire character depends on the opposite approach.

## Cross-References

- `knowledge_base/genres/metal/death_metal.md` and `knowledge_base/genres/metal/heavy_metal.md` — a limiter used mid-chain for relentless drum-bus evenness, contrasted with a compressor used to preserve transient smack
- `knowledge_base/genres/country/honky_tonk.md`, `knowledge_base/genres/country/bluegrass_gospel.md`, and `knowledge_base/genres/country/outlaw_country.md` — heavy limiting explicitly avoided at mastering to preserve raw dynamic character
- `knowledge_base/genres/country/country_pop.md` and `knowledge_base/genres/country/contemporary_country.md` — heavy limiting used deliberately for loudness-war radio competitiveness
- `knowledge_base/genres/electronic/ambient.md`, `knowledge_base/genres/electronic/glitch.md`, `knowledge_base/genres/electronic/coldwave.md`, and `knowledge_base/genres/electronic/breakbeat.md` — limiting minimized to preserve dynamic contrast or transient detail
- `knowledge_base/mastering/dynamics/compression_and_clipping_as_aesthetic.md` — the genres that collapse the compression/limiting distinction on purpose
- `knowledge_base/mastering/loudness/true_peak_and_intersample_peaks.md` — the final-limiter true-peak ceiling that applies regardless of how a mix was compressed upstream
- `knowledge_base/mastering/dynamics/multiband_compression_and_limiter_chain_ordering.md` — standard chain ordering placing the limiter last, after EQ and multiband compression
