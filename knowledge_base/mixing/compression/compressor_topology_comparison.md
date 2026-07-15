---
technique_name: "Compressor Topology Comparison: VCA vs FET vs Opto vs Vari-Mu"
category: compression
problem_solved: "Choosing a compressor by ratio/attack/release numbers alone and getting the wrong sonic character — a fast, aggressive FET-style grab where a slow, musical optical glue was needed, or a punchy VCA bus compressor where vintage tube warmth was the actual goal"
parameters:
  vca: "Fast, precise, consistent gain reduction across program material; typically fast attack (sub-ms to a few ms) and programmable release; the character behind SSL-style bus compressors and most modern 'clean' digital compressors"
  fet: "Extremely fast attack (as low as 20 microseconds on a real 1176), aggressive and somewhat colored/distorted at high ratios or fast settings; reacts to the input signal directly rather than a smoothed control voltage"
  opto: "Program-dependent, non-linear attack/release that slows down on longer or louder passages (an electro-optical cell's inherent lag); smooth, musical, hard to make sound harsh even when pushed"
  vari_mu: "Tube-based gain reduction with a soft, increasingly non-linear knee as more compression is applied; naturally gentle, 'glue'-oriented character even at higher ratios, historically exemplified by the Fairchild 670"
signal_chain_position: "Insert on an individual source (vocal, bass, guitar bus) or the full mix/master bus, chosen by desired character rather than by ratio/attack numbers alone"
genre_applicability:
  - bluegrass
  - soul
  - classic_country
  - choral_music
  - yacht_rock
  - funk
related_techniques:
  - parallel_compression
  - bus_glue_compression
  - attack_and_release_time_science
tags: ["compressor-topology", "vca", "fet", "opto", "vari-mu", "1176", "la-2a", "fairchild", "vintage-compression"]
---

# Compressor Topology Comparison: VCA vs FET vs Opto vs Vari-Mu

Genre files in this knowledge base rarely stop at "compress the vocal" — when a specific vintage character is part of the genre's sound, they name the actual circuit type or hardware unit the sound is modeled on. Read together, these citations sketch out why topology, not just ratio and attack/release numbers, is a real production decision: the same numeric settings dialed into a FET-style plugin and an opto-style plugin will not sound alike, because the two circuits derive their gain reduction differently.

## Optical (Opto) Compression: Slow, Musical, Program-Dependent

Opto compressors — the LA-2A is the reference unit — use an electro-optical cell whose response time depends on the signal driving it, producing a naturally slow, smooth, program-dependent attack and release rather than a fixed millisecond setting. `soul.md` reaches for exactly this on vocals: "Opto-compression (LA-2A) on vocals" paired with "Pultec-style passive EQ for warm lows and smooth highs." `classic_country.md` uses the same unit for a related reason: "Light optical compression (LA-2A) on vocals and bass to gently control dynamics without squashing the performance." `choral_music.md` extends opto compression to a full vocal group rather than a solo voice: "Use very transparent, slow-acting optical compression (like an LA-2A) on the choir bus to gently glue the voices together without crushing their natural dynamic breathing." Across all three, the common thread is control without audible intervention — opto is the choice when the goal is to tame dynamics while the performance still sounds unprocessed.

## FET Compression: Fast, Aggressive, Characterful

FET compressors — the 1176 is the archetype — respond almost instantly to the input signal, making them the choice when a fast transient genuinely needs catching rather than smoothing. `bluegrass.md` names the tradeoff directly: "Use extremely transparent optical compression or fast FET compression just to catch the harsh transients of the banjo and mandolin. Do not squash the mix." The genre file treats opto and FET as two valid answers to a related but distinct problem — opto for overall dynamic control, FET specifically when a sharp transient (banjo/mandolin pick attack) needs grabbing without slowing the compressor down to catch it. `yacht_rock.md` cites the FET topology for its historical association rather than a transient-control need: "Reference-quality vintage compressor/EQ emulations (LA-2A, 1176-style) for the smooth, glossy studio character central to the genre's mix aesthetic" — here the 1176 is invoked alongside the LA-2A as part of a period-correct studio chain, not because the source needs FET-specific fast transient control.

## Vari-Mu (Tube) Compression: The Fairchild Glue

Vari-mu compressors use a vacuum tube's variable transconductance to produce gain reduction, and the resulting knee gets progressively softer and more program-dependent as compression increases — the Fairchild 670 is the unit genre files reach for by name. `soul.md` cites it directly as part of classic soul's recording chain: "the 'sound design' comes from the recording process: the sound of the room, tape saturation, the bleed between microphones, and the specific use of analog gear like Fairchild compressors and Pultec EQs." Its mixing section frames the sonic goal explicitly: "Slower attack, musical compression (Fairchild, LA-2A). The goal is glue and warmth, not aggressive transient shaping." That last sentence is the clearest statement in the corpus of what vari-mu and opto topologies share and FET does not — both are reached for specifically when transient shaping is not the goal.

## VCA Compression: Precision Punch on Busses

VCA (voltage-controlled amplifier) compressors trade the program-dependent smoothing of opto/vari-mu circuits for precise, consistent, fully programmable gain reduction — the topology behind SSL-style bus compressors. `funk.md` names this explicitly for drums and bass: "VCA compression (like SSL channel strips) used for punch and 'smack' on drums and bass. Fast attack times to control the aggressive transients of slap bass." Where `soul.md` reaches for vari-mu/opto specifically to avoid aggressive transient shaping, `funk.md` reaches for VCA specifically because it wants that fast, controlled grab on slap bass's sharp transients — the two genres want opposite things from their compressor, and pick opposite topologies to get them.

## Choosing Topology by Genre Aesthetic, Not Just Source Material

Laid side by side, these citations show topology choice tracking two different variables: transient content (bluegrass picks FET specifically for banjo/mandolin transient control, funk picks VCA for slap-bass transients) and genre-era aesthetic (soul, classic country, choral music, and yacht rock all reach for opto or vari-mu specifically to invoke a vintage, musical, non-aggressive character regardless of what the source material's transients actually demand). A modern digital compressor set to the "same" ratio and attack/release numbers as an LA-2A will not automatically sound like one, because the numbers don't capture the program-dependent, non-linear behavior that defines the opto and vari-mu topologies in the first place.

## Common Mistakes

**Choosing a compressor by ratio/attack numbers while ignoring topology.** `soul.md`'s "goal is glue and warmth, not aggressive transient shaping" only works because opto/vari-mu circuits are inherently smooth — dialing a VCA or FET compressor to the same numeric attack/release settings won't reproduce that same non-linear, program-dependent gentleness.

**Reaching for FET on material that needs to stay unprocessed-sounding.** `bluegrass.md`'s guidance to "not squash the mix" pairs FET specifically with the transient-catching job it's good at, not as a general-purpose vocal or bus compressor — its speed and character work against the "musical, uncompressed-sounding" goal that opto/vari-mu serve in `soul.md` and `choral_music.md`.

**Assuming any "vintage-style" plugin is interchangeable with any other.** An LA-2A emulation and a Fairchild 670 emulation are both reached for in this corpus to avoid aggressive transient shaping, but they arrive at that smoothness through different circuits (opto cell vs vari-mu tube) with different sonic side effects — treating "vintage compressor" as one undifferentiated category loses the distinction genre files like `soul.md` are actually making.

## Cross-References

- `knowledge_base/genres/country/bluegrass.md` — optical vs FET compression as two answers to different transient-control needs
- `knowledge_base/genres/r_and_b/soul.md` — opto (LA-2A) and vari-mu (Fairchild) compression explicitly framed as glue-and-warmth, not transient-shaping tools
- `knowledge_base/genres/country/classic_country.md` — LA-2A opto compression for gentle, performance-preserving dynamic control
- `knowledge_base/genres/classical/choral_music.md` — LA-2A opto compression scaled up to a full choir bus for transparent glue
- `knowledge_base/genres/rock/yacht_rock.md` — LA-2A and 1176-style compression cited as period-correct studio character rather than transient-driven necessity
- `knowledge_base/genres/r_and_b/funk.md` — VCA/SSL-style compression chosen specifically for fast, punchy transient control on slap bass
- `knowledge_base/mixing/compression/parallel_compression.md` — a related technique where aggressive compressor settings (often FET/VCA-style) are deliberately used on a parallel bus rather than avoided
- `knowledge_base/mixing/compression/bus_glue_compression.md` — bus-wide glue compression, where opto/vari-mu topology choices most often appear in this corpus
