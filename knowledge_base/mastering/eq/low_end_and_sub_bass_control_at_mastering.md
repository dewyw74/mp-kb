---
technique_name: "Low-End and Sub-Bass Control at the Mastering Stage"
category: "eq"
problem_solved: "A master's low end either lacks the weight a genre's convention demands, or is so extended/uncontrolled that it eats headroom, causes limiter pumping, or fails to translate to club and consumer playback systems — and the correct target varies enormously by genre rather than following a single 'more sub is better' or 'less is safer' rule"
parameters:
  club_soundsystem_control: "Deep, controlled sub-bass kept mono/near-mono and separated in level from low-mid content, prioritized in genres built for club and soundsystem playback"
  smile_curve_extension: "Deliberately massive, extended sub-bass (frequently 808-driven) as a genre-defining tonal feature rather than a problem to tame, in modern pop/hip-hop/R&B smile-curve genres"
  masking_avoidance: "Low-mid content deliberately kept lean or scooped relative to sub-bass so the two don't mask each other, especially where sub-bass and low-mid instruments (bass guitar, wobble bass) must remain distinct"
  restraint_by_period_or_genre_convention: "Some genres deliberately limit sub-bass extension relative to modern norms, either as a period-authentic choice (vinyl-era genres) or a genre-identity choice (treble-forward genres inverting the usual low-end emphasis)"
signal_chain_position: "Broad low-frequency shelving/filtering as part of the master-bus tonal-balance EQ stage, coordinated with multiband compression and the limiter's low-band behavior"
genre_applicability:
  - jungle
  - techno
  - house
  - dubstep
  - bassline
  - dark_pop
  - alternative_r_and_b
  - contemporary_r_and_b
  - drone_metal
  - black_metal
related_techniques:
  - genre_tonal_balance_targets
  - final_mono_and_translation_check
  - stereo_widening_at_mastering
tags: ["eq", "sub-bass", "low-end", "mono", "mastering", "club-translation"]
---

# Low-End and Sub-Bass Control at the Mastering Stage

Genre files across the corpus treat mastering-stage low-end control as one of the most genre-dependent decisions a mastering engineer makes — the "correct" amount of sub-bass extension, and how tightly it needs to be controlled versus allowed to dominate, varies from genres that build their entire identity around it to genres that deliberately invert the convention.

## Club and Soundsystem Genres: Controlled, Mono, and Separated From the Low-Mids

`jungle.md` documents a precise, structural approach: "Deep, controlled sub-bass; forward upper-midrange presence on break hits for clarity on club systems; low-mid kept relatively lean to avoid masking the sub" — the low-mid range is deliberately thinned specifically so it doesn't compete with and mask the sub-bass underneath it. `techno.md` reinforces the mono-compatibility side of the same discipline: "Mono-summed low end for club-system translation and DJ mix compatibility." `house.md` frames its target as moderate rather than maximal: "controlled sub bass (club-system-focused, not festival-sub-heavy)," explicitly distinguishing its low-end goals from festival/EDM genres that push sub-bass further. `dubstep.md` documents the same controlled-but-deep approach while separating sub-bass from its genre-defining midrange element: "Deep, controlled sub-bass; a clear, present low-mid for wobble bass definition" — here the low-mid isn't scooped the way jungle's is, because wobble bass itself needs to live there. `bassline.md` states the underlying risk directly: "the low end preserved and controlled rather than over-limited into mush, since the bassline's rhythmic definition depends on transient clarity" — a warning that low-end control isn't just about tonal balance but about not destroying rhythmic information through over-limiting.

## Smile-Curve Genres: Sub-Bass as a Deliberate Feature, Not a Risk to Manage

`dark_pop.md` treats extended low end as a headline feature rather than a hazard: "Deep, weighty low end (808/sub-bass) balanced against a present, close-mic'd vocal, with restrained, non-fatiguing high end." `alternative_r_and_b.md` and `contemporary_r_and_b.md` both describe similarly weighted low ends, with `contemporary_r_and_b.md` adding the control caveat: "The low end (kick and sub-bass) is powerful but tightly controlled to avoid muddying the mix." The distinction from the club-genre approach above is one of degree and context rather than philosophy — these genres still control the low end carefully, they just start from a target that's already bigger.

## The Inverted Case: Genres That Deliberately Minimize Sub-Bass

`drone_metal.md` documents the most extreme low-end-forward target in the corpus — "Extremely low-end and sub-bass focused, with high frequencies comparatively minimal — the opposite emphasis of black metal's treble-forward mastering" — and in doing so names its own direct opposite. `black_metal.md` confirms that inverse explicitly: "Harsh, cold, and treble-heavy. A deliberate lack of warm low-mids and sub-bass." Mastering low-end control for black metal isn't about taming excess sub-bass — there's deliberately very little of it to begin with — while drone metal's mastering job is almost entirely about managing and supporting a sub-bass-dominant signal without letting a limiter choke it.

## Common Mistakes

**Applying a uniform sub-bass target across genres regardless of convention.** A jungle or techno master's "controlled, club-focused" sub-bass would read as underweight on a dark-pop or contemporary R&B master, and a dark-pop-weight sub-bass would overwhelm a jungle mix's carefully separated low-mid/sub relationship.

**Letting low-mid content mask the sub-bass rather than deliberately separating them.** As `jungle.md` demonstrates, some genres solve this by thinning the low-mids specifically to give the sub-bass room, rather than trying to EQ the sub-bass itself to "cut through."

**Forgetting that low-end control also protects transient/rhythmic information, not just tonal balance.** `bassline.md`'s warning about over-limiting turning the low end to "mush" is a dynamics problem as much as an EQ one — low-end EQ decisions at mastering need to be made in coordination with the limiter's behavior on that band, not in isolation.

## Cross-References

- `knowledge_base/mastering/eq/genre_tonal_balance_targets.md` — the broader tonal-balance framework this low-end-specific guidance sits inside
- `knowledge_base/mastering/stereo/final_mono_and_translation_check.md` — the mono-fold verification step for the mono-centered low-end convention documented here
- `knowledge_base/genres/edm/jungle.md`, `knowledge_base/genres/edm/techno.md`, `knowledge_base/genres/edm/house.md`, `knowledge_base/genres/edm/dubstep.md`, `knowledge_base/genres/edm/bassline.md` — direct sources for club/soundsystem low-end control convention
- `knowledge_base/genres/pop/dark_pop.md`, `knowledge_base/genres/r_and_b/alternative_r_and_b.md`, `knowledge_base/genres/r_and_b/contemporary_r_and_b.md` — direct sources for smile-curve sub-bass-as-feature convention
- `knowledge_base/genres/metal/drone_metal.md`, `knowledge_base/genres/metal/black_metal.md` — direct sources for the sub-bass-forward vs. treble-forward inverted extremes
