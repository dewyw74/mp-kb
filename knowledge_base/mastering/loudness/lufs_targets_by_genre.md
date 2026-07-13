---
technique_name: LUFS Loudness Targets by Genre
category: loudness
problem_solved: "Choosing a mastering loudness target that's wrong for the genre — too loud crushes the dynamic contrast a genre depends on; too quiet undersells the impact a genre's context (club, festival, radio) demands"
parameters:
  quietest_tier: "-18 to -13 LUFS integrated — post-rock, progressive rock, ambient, world/classical/acoustic traditions, blues rock"
  moderate_tier: "-12 to -9 LUFS integrated — most mainstream pop, hip-hop, house, melodic EDM, indie/alternative rock"
  loud_tier: "-9 to -6 LUFS integrated — trap, K-pop, pop punk, breakbeat, most club-oriented EDM"
  loudest_tier: "-7 to -4 LUFS integrated — speedcore, hardstyle, riddim, big room house, neurofunk, other peak-time festival/club subgenres"
signal_chain_position: "Final limiter stage, after all mix-bus processing; the target should be decided from the genre's context (club PA, radio, streaming, concert hall) before any limiting is applied, not arrived at by simply pushing a limiter until it "feels loud enough""
genre_applicability:
  - post_rock
  - progressive_rock
  - ambient
  - blues_rock
  - flamenco
  - indian_classical
  - pop
  - hip_hop
  - trap
  - k_pop
  - speedcore
  - hardstyle
  - riddim
  - big_room_house
related_techniques:
  - dynamic_range_as_expressive_device
  - compression_and_clipping_as_aesthetic
  - streaming_platform_normalization
tags: ["lufs", "loudness-target", "mastering", "genre-convention", "club-vs-radio"]
---

# LUFS Loudness Targets by Genre

Across this knowledge base's genre entries, mastering loudness targets span an enormous range — from around -18 LUFS integrated for post-rock to -4 LUFS for speedcore — and the variation isn't arbitrary. It tracks a genre's actual listening context (concert hall vs. club PA vs. earbuds), the structural role dynamic contrast plays in the music, and how much a genre treats extreme loudness itself as part of its identity rather than a delivery-format concession.

## The Quiet End: Where Dynamic Range Is the Point

Genres built around a structural contrast between quiet and loud sections cluster at the bottom of the loudness range, because mastering them any louder would physically remove the contrast the music is built on. `post_rock.md` states this as close to a hard rule as any genre file in the knowledge base gets: "Maximum dynamic range preservation is essential — the genre's entire expressive power depends on the contrast between near-silent openings and overwhelming climaxes, so mastering must avoid compressing that range away." `progressive_rock.md` uses almost identical language: "Wide dynamic range preservation is essential and non-negotiable — the genre's structural identity depends on audible contrast between quiet and loud sections; heavy limiting actively damages the music's intent." World-music and classical-adjacent traditions sit in this same low-loudness tier for a related but distinct reason — they're mastered to represent a real acoustic performance space rather than a commercial delivery format, as seen in `flamenco.md`'s "-16 to -13 LUFS integrated, essential to conveying flamenco's intense emotional and rhythmic contrasts" and `indian_classical.md`'s "-16 to -13 LUFS integrated, essential to the tradition's alap-to-jhala structural and emotional arc."

## The Moderate Middle: Streaming-Competitive but Not Maximal

The bulk of mainstream, radio- and streaming-oriented genres sit in a -12 to -9 LUFS band, loud enough to be competitive on modern playback platforms without sacrificing all dynamic movement. `pop.md` targets "-9 to -7 LUFS integrated for streaming-competitive masters," explicitly framing the choice around "prioritizing loudness competitiveness on streaming platforms while still preserving enough dynamic contrast between verse and chorus to keep the arrangement's lift audible." `melodic_house.md` sits at a similar "-9 to -7 LUFS integrated, with moderate-to-high dynamic range deliberately preserved — especially around the melodic break — so the contrast between sparse and full sections reads clearly rather than being crushed flat." Genres in this tier are making a deliberate compromise: loud enough to compete, not so loud that the arrangement's own internal dynamic story gets erased.

## The Loud Tier: Club and Chart Competitiveness

A step louder, in the -9 to -6 LUFS range, sit genres whose primary listening context is a club system, a car stereo, or a hyper-competitive streaming chart environment where standing out matters more than preserving wide dynamic contrast. `trap.md` and `hip_hop.md` both land around "-9 to -7" to "-8 to -6 LUFS integrated... for streaming and club competitiveness." `k_pop.md` runs slightly louder still, "-8 to -6 LUFS integrated, compressed for streaming and radio competitiveness while still preserving the genre's dramatic section-to-section contrast" — note the qualifier: even at this louder tier, the genre file still calls out preserving *some* contrast as a priority, distinguishing it from the loudest tier below where dynamic contrast is explicitly deprioritized.

## The Loudest Tier: Loudness as the Genre's Actual Point

At the extreme end, several EDM subgenres treat maximal loudness not as a necessary compromise but as a direct expression of the genre's aesthetic identity — impact and physical weight matter more than preserved dynamic nuance. `speedcore.md` is the most extreme documented case: "-6 to -4 LUFS integrated (often louder/more clipped than conventional mastering targets by design)... clipping and brickwall limiting are treated as aesthetic tools rather than problems to avoid." `hardstyle.md` ("-6 to -5 LUFS integrated... reflecting the genre's maximal, aggressive festival aesthetic"), `riddim.md` ("-6 to -5 LUFS integrated... with very low dynamic range reflecting the genre's priority on maximum physical bass weight and loudness over dynamic nuance"), and `big_room_house.md` ("-6 to -5 LUFS integrated... heavily limited to prioritize maximum perceived impact on large festival PA systems") all sit in this same tier, unified by an explicit prioritization of impact over dynamic preservation. See `compression_and_clipping_as_aesthetic.md` for the deeper mixing/mastering-stage logic behind this choice.

## Reading a Genre File's Loudness Target Correctly

The number alone isn't the useful information — the reasoning attached to it is. A genre file's `target_loudness` field paired with its `dynamics` field tells you whether a given LUFS number reflects a hard structural requirement (post-rock, progressive rock — going louder actively breaks the music), a competitive-but-compromising choice (mainstream pop, hip-hop — loud enough to compete, but contrast still matters), or a genre where loudness itself is aesthetically central (speedcore, hardstyle — more compression is more "right," not a necessary evil).

## Common Mistakes

**Applying a single "competitive" loudness target across every genre.** A -9 LUFS master on a post-rock or progressive-rock track directly destroys the quiet-to-loud contrast those genres are structurally built around — the target has to come from the genre's own logic, not a generic streaming-loudness rule of thumb.

**Assuming louder is always "more professional."** In genres explicitly citing dynamic range preservation as essential (`post_rock.md`, `progressive_rock.md`, `blues_rock.md`, `world_music` entries), a quieter, more dynamic master is the technically correct choice, not an unfinished or underdeveloped one.

**Ignoring the difference between "loud because the genre demands club impact" and "loud because that's just what mastering does."** Compare `k_pop.md`'s "-8 to -6 LUFS... while still preserving the genre's dramatic section-to-section contrast" against `speedcore.md`'s explicit deprioritization of dynamic nuance — both are loud, but for different reasons, and the mastering approach (how hard to lean into limiting/clipping) should differ accordingly.

## Cross-References

- `knowledge_base/genres/rock/post_rock.md` and `knowledge_base/genres/rock/progressive_rock.md` — dynamic range preservation treated as non-negotiable
- `knowledge_base/genres/world_music/flamenco.md` and `knowledge_base/genres/world_music/indian_classical.md` — loudness targets reflecting acoustic/performative authenticity rather than commercial delivery
- `knowledge_base/genres/pop/pop.md` and `knowledge_base/genres/edm/melodic_house.md` — the moderate, streaming-competitive-but-still-dynamic middle tier
- `knowledge_base/genres/hiphop/trap.md`, `knowledge_base/genres/hiphop/hip_hop.md`, `knowledge_base/genres/pop/k_pop.md` — loud, club/streaming-competitive tier that still preserves some contrast
- `knowledge_base/genres/edm/speedcore.md`, `knowledge_base/genres/edm/hardstyle.md`, `knowledge_base/genres/edm/riddim.md`, `knowledge_base/genres/edm/big_room_house.md` — the loudest tier, where dynamic nuance is explicitly deprioritized in favor of impact
- `knowledge_base/mastering/dynamics/dynamic_range_as_expressive_device.md` and `knowledge_base/mastering/dynamics/compression_and_clipping_as_aesthetic.md` — the deeper logic behind why genres land where they do on this spectrum
