---
title: "Sample Library Curation Workflow"
technique: "Organizing, sourcing, and selecting from large sample and sample-library collections"
tags:
  - "sample-library"
  - "curation"
  - "sample-packs"
  - "sampling"
  - "workflow"
  - "orchestral-mockup"
---

# Sample Library Curation Workflow

Before a sample can be chopped, layered, or resampled, it has to be found, evaluated, and organized — and this knowledge base's genre files describe several genuinely different curation workflows depending on whether the source is a crate of records, a commercial sample pack, a scripted orchestral library, or a stash of ripped media. Genre files consulted for grounding: `knowledge_base/genres/hiphop/boom_bap.md`, `east_coast_hip_hop.md`, `jazz_rap.md`, `knowledge_base/genres/electronic/vaporwave.md`, `knowledge_base/genres/cinematic/trailer_music.md`, `knowledge_base/genres/pop/space_age_pop.md`, `knowledge_base/genres/r_and_b/modern_soul.md`.

## Curating a Sample-Pack Collection for a Target Aesthetic

Modern producers working in sample-descended genres frequently rely on cleared, purpose-built sample packs rather than sourcing directly from uncleared recordings, which turns curation into a search-and-evaluate task rather than a crate-digging one:

- `boom_bap.md` and `east_coast_hip_hop.md` both describe this directly: "Digging through royalty-free or cleared sample packs inspired by classic soul/funk/jazz breaks for modern boom-bap revival production." The curation task here is selecting packs and individual one-shots/loops that convincingly match a specific historical sonic reference (soul/funk/jazz breaks) while remaining legally usable — a different skill from digging through actual vintage vinyl, but aimed at the same sonic target.
- `jazz_rap.md` documents a related but distinct fallback: "Use high-quality jazz sample libraries or live jazz musicians recorded specifically for chopping, when direct sampling isn't cleared for use" — curation here means auditioning library material specifically for its chop-ability (phrasing, isolation of instruments, clean note attacks) rather than for how it sounds as a finished performance.

## Curating Ripped/Found Media into a Custom Sample Chain

`vaporwave.md` documents an idiosyncratic curation source distinct from either vinyl digging or commercial packs: "Building custom sample chains in a DAW's sampler (Ableton Simpler/Sampler, Native Instruments Kontakt) from ripped corporate VHS/CD-ROM audio for period-accurate source material." The curation task is sourcing (finding period-specific corporate/media audio — elevator music, software startup chimes, in-store radio rips) and then organizing the selected fragments into a sampler instrument, rather than selecting from a pre-organized commercial library — the raw material itself carries the genre's cultural-reference meaning, so curation choices are inseparable from the genre's aesthetic statement.

## Curating Orchestral Sample Libraries by Velocity and Articulation Coverage

A different curation axis appears across the cinematic and orchestral genre files: for scripted/mockup libraries, curation isn't about finding the right *source recording* but about choosing the right *library and articulation/velocity range* for the musical context:

- `trailer_music.md` documents an extreme, purpose-driven selection rule: "Trailer music uses the top velocity layers of orchestral sample libraries almost exclusively" — for maximum-impact material, the curation decision is deliberately narrowing to only the loudest, most aggressive velocity layers a library offers rather than using its full expressive range.
- This contrasts with genres needing the opposite: full-range, true-legato libraries for expressive, dynamically varied writing (see `multisampling_and_velocity_layers.md` for the construction side of this — how those velocity layers and articulations are built into a library in the first place).

## Curating a Collection as a Standalone Creative Identity

`modern_soul.md` and `space_age_pop.md` both describe curation as the primary creative act of a genre, rather than a preparatory step before production:

- `modern_soul.md` is explicit that "the genre remains defined by its curatorial function" — DJs and reissue labels "sourcing and licensing original mid-1970s-to-1980s American soul masters rather than 'producing' new modern soul material." Selection and sequencing *is* the genre's output.
- `space_age_pop.md` references "the Ultra Lounge compilation series (Capitol Records, from 1996) as a curated modern entry point into the genre's classic 1950s-60s recordings" — a professionally curated compilation functioning as a reference library for anyone wanting to study or draw on the genre's original recorded palette.

## A Practical Curation Workflow

Synthesizing the above into a repeatable process:

1. **Define the sonic target first** — a specific era/genre reference (boom bap's soul/funk break), a cultural-reference palette (vaporwave's corporate media), or a performance-intensity band (trailer music's top-velocity hits) — before auditioning any material, so evaluation has a clear pass/fail criterion.
2. **Source appropriately for the legal and aesthetic context** — cleared sample packs or newly recorded material when commercial release is the goal (`jazz_rap.md`, `boom_bap.md`), original/vintage recordings when the raw grain itself is the point (`vaporwave.md`, `modern_soul.md`). See `sample_clearance_and_legal_considerations.md` for the legal side of this decision.
3. **Organize by usable unit, not just by source file** — tag or file individual chops, one-shots, and loops by usable musical role (bassline-ready loop, isolated drum hit, texture bed) rather than leaving them as undifferentiated raw recordings, so later chopping/layering work (`chopping_flipping_and_time_stretching.md`, `layering_samples_for_hybrid_sounds.md`) can pull from an already-evaluated pool.
4. **Re-audition against the target regularly** — a library or pack that sounded right in isolation can still fail to match the track's evolving sonic identity; genres built on curation as their creative core (`modern_soul.md`) treat this as an ongoing editorial process, not a one-time setup step.

## Common Mistakes

**Treating sample-pack search as interchangeable with genuine crate-digging.** `boom_bap.md`'s modern-revival workflow explicitly substitutes cleared packs for original digging, but the curation goal (matching a specific historical sonic reference) stays the target — picking generic-sounding packs without auditioning against that reference produces a track that doesn't actually land the genre's sound.

**Using a library's default/middle velocity layers when the genre calls for a narrower, purpose-specific slice.** `trailer_music.md`'s top-velocity-only rule is a curation decision, not a performance one — pulling from the wrong part of a library's velocity range undermines the intended impact regardless of how the material is played.

**Skipping organization and re-auditioning raw source material from scratch every session.** Genres whose entire identity rests on curation (`modern_soul.md`) treat organizing and re-evaluating a collection as core, ongoing work rather than a one-time setup task to get past quickly.

## Cross-References

- `knowledge_base/sound_design/sampling/vinyl_and_tape_sample_sourcing.md` — the specific physical-media sourcing lineage (crate-digging vinyl/tape) this entry's sample-pack curation workflow often substitutes for.
- `knowledge_base/sound_design/sampling/sample_clearance_and_legal_considerations.md` — the legal considerations that shape sourcing decisions between cleared packs, original recordings, and re-played material.
- `knowledge_base/sound_design/sampling/multisampling_and_velocity_layers.md` — how the velocity/articulation coverage referenced in the orchestral curation section above is actually built into a sample library.
- `knowledge_base/genres/hiphop/boom_bap.md`, `east_coast_hip_hop.md`, `jazz_rap.md` — cleared sample-pack curation for classic soul/funk/jazz sonic targets.
- `knowledge_base/genres/electronic/vaporwave.md` — curating ripped media into a custom sample chain.
- `knowledge_base/genres/cinematic/trailer_music.md` — velocity-layer-specific orchestral library curation.
- `knowledge_base/genres/r_and_b/modern_soul.md`, `knowledge_base/genres/pop/space_age_pop.md` — curation as a genre's primary creative output.
