---
technique_name: "Genre-Specific Tonal Balance Targets at Mastering"
category: "eq"
problem_solved: "Applying a generic, one-size-fits-all mastering EQ curve to every mix, when the correct tonal target — 'smile curve' hype, warm/natural restraint, or aggressive midrange presence — varies enormously and systematically by genre"
parameters:
  smile_curve_genres: "Pop, EDM, and modern trap/hip-hop favor a 'smile' EQ curve — boosted sub/low end and boosted highs with a comparatively recessed midrange — for a big, exciting, hyped-up commercial sound"
  warm_natural_genres: "Jazz, classical, acoustic, and vintage-leaning genres favor a warm, natural balance that explicitly avoids 'loudness-war brightness,' preserving instrument timbre over commercial hype"
  midrange_forward_genres: "Metal, punk, and vocal/dialogue-critical genres (video game score) favor a present, sometimes aggressive midrange, since that's where riff articulation, vocal intelligibility, or gameplay-cue clarity actually lives"
  context_dependent_genres: "Some genres (film score, video game score) explicitly subordinate their tonal target to an external context — the final film mix or the gameplay audio it must not compete with — rather than following an internal genre convention at all"
signal_chain_position: "Broad tonal-balance EQ, typically the first processing stage on the master bus, before multiband compression and the final limiter"
genre_applicability:
  - contemporary_country
  - country_pop
  - trailer_music
  - bossa_nova
  - baroque
  - heavy_metal
  - sludge_metal
  - video_game_score
  - film_score
related_techniques:
  - lufs_targets_by_genre
  - matching_master_transparency_to_source_character
  - multiband_compression_and_limiter_chain_ordering
tags: ["eq", "tonal-balance", "smile-curve", "mastering", "genre-convention", "frequency-balance"]
---

# Genre-Specific Tonal Balance Targets at Mastering

Across this knowledge base's genre entries, mastering-stage tonal balance (documented in each genre file's `frequency_balance` field) splits into a handful of recurring philosophies rather than one universal "good" curve — and picking the wrong one for a given genre produces a technically clean master that still sounds wrong to anyone familiar with that genre's conventions.

## The Smile Curve: Hyped Lows and Highs, Recessed Mids

Modern commercial pop, country-pop, and trailer/epic cinematic genres lean hard into a scooped-midrange "smile" curve. `contemporary_country.md` describes it plainly as "Massive, sub-heavy low end and sparkling, hyped highs. The classic 'smile' EQ curve of modern pop," and `country_pop.md` echoes it almost verbatim as "the classic pop 'smile' curve — booming, tight lows and sparkling, hyped highs." Trailer music pushes the same philosophy to its most extreme form: `trailer_music.md` calls for "massive, cinematic sub-bass and aggressive, bright, tearing high frequencies... the ultimate 'smile' EQ curve." This curve isn't a mistake to be corrected — it's the genre-correct target, since these genres are built for club PAs, earbuds, phone speakers, and trailer-house theater systems where hyped lows and highs read as "big" and "exciting" rather than harsh.

## Warm and Natural: Restraint as the Genre-Correct Choice

At the opposite end, jazz, classical, and vintage-leaning acoustic genres treat brightness itself as the mistake. `bossa_nova.md` calls for a balance "avoiding modern loudness-war brightness entirely, as it directly conflicts with the genre's hushed character," and `baroque.md` describes frequency balance as "warm and natural, avoiding excessive brightness that would misrepresent period instrument timbre (gut strings, harpsichord, natural brass)." Several country entries in this knowledge base similarly call for "a natural, non-aggressive top end." The common thread: these genres are mastered to represent a real acoustic performance rather than a commercial delivery format, so a smile-curve approach would actively misrepresent the source material's actual timbre.

## Midrange-Forward: Where the Genre's Identity Actually Lives

A third group deliberately keeps the midrange present rather than recessing it, because the midrange is where the genre's defining character sits. Metal genres consistently call for preserved or boosted midrange — `heavy_metal.md` calls for "thick, heavy low-mids (the 'chug' frequency) with a biting, aggressive high-midrange presence for the guitar attack and cymbals," and `sludge_metal.md` goes further, insisting the midrange stay "dense (not scooped)... a deliberate contrast with thrash or death metal mixing conventions." The reasoning is structural, not just stylistic: riff articulation and cymbal attack live in that midrange-to-high-mid range, and scooping it the way a pop smile-curve would actively removes the genre's core sonic identity.

## Context-Dependent: No Internal Genre Convention at All

Cinematic genres built to sit underneath other audio break the "pick a genre curve" model entirely. `video_game_score.md` states its frequency balance must stay "balanced and clear — extreme sub-bass or piercing highs can interfere with critical gameplay audio cues," and film score entries describe a target "tailored to complement, not compete with, the dialogue and sound-design frequency ranges in the final film mix." For these genres, the correct mastering EQ target isn't derivable from the genre alone — it depends on the specific mix context (a game's sound design, a film's dialogue) the music will sit inside.

## Common Mistakes

**Applying a smile-curve master to acoustic, jazz, or classical material because it "sounds more exciting."** This actively works against genres where warm, natural, unhyped tonal balance is the entire point — a jazz trio master with a scooped midrange and boosted highs reads as amateurish to genre-literate listeners, not polished.

**Scooping the midrange on metal or punk masters out of habit, borrowed from pop/EDM conventions.** As `sludge_metal.md` and its neighboring metal entries make clear, the midrange carries the riff and vocal presence that defines these genres — removing it removes the genre's identity, not just "harshness."

**Choosing a fixed tonal target for context-dependent cinematic genres without checking the context they'll sit inside.** A video game score or film score mastered in isolation to sound maximally impressive on its own can actively conflict with the dialogue or gameplay-cue frequencies it needs to leave room for.

## Cross-References

- `knowledge_base/mastering/loudness/lufs_targets_by_genre.md` — the parallel genre-driven convention for loudness targets, following the same "context and identity, not a universal default" logic applied to tonal balance here
- `knowledge_base/mastering/dynamics/matching_master_transparency_to_source_character.md` — the related principle of matching mastering processing to what the source material actually is, rather than a fixed recipe
- `knowledge_base/mastering/dynamics/multiband_compression_and_limiter_chain_ordering.md` — the processing stage that follows this broad tonal-balance EQ in the standard mastering chain order
- `knowledge_base/genres/metal/heavy_metal.md` and `knowledge_base/genres/metal/sludge_metal.md` — direct sources for the midrange-forward, deliberately non-scooped mastering philosophy
- `knowledge_base/genres/cinematic/video_game_score.md` and `knowledge_base/genres/cinematic/film_score.md` — direct sources for context-dependent tonal balance with no internal genre convention
- `knowledge_base/genres/country/contemporary_country.md`, `knowledge_base/genres/country/country_pop.md`, and `knowledge_base/genres/cinematic/trailer_music.md` — direct sources for the smile-curve philosophy
- `knowledge_base/genres/jazz/bossa_nova.md` and `knowledge_base/genres/classical/baroque.md` — direct sources for the warm/natural, brightness-averse philosophy
