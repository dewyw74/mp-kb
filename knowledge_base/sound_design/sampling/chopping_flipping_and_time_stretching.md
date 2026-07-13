---
title: "Sample Chopping, Flipping, and Time-Stretching Techniques"
technique: "Sample chopping and manipulation"
tags:
  - "sample-chopping"
  - "flip"
  - "time-stretching"
  - "pitch-shifting"
  - "chopped-and-screwed"
  - "sampling"
---

# Sample Chopping, Flipping, and Time-Stretching Techniques

Sample chopping — cutting a source recording into small segments and rearranging, pitching, or re-triggering them — is documented across this knowledge base as hip-hop's foundational sound-design technique, and the specific manipulation applied to those chops (pitch, tempo, screwed/slowed processing) is itself a genre-defining decision, not just an implementation detail.

## Chopping as the Foundational Technique

`hip_hop.md` names chopping as the genre's originating sound-design method: "Sample-based production (chopping and looping breaks via turntables or later the MPC/sampler workflow) is hip-hop's foundational sound-design technique." The same file documents its modern evolution: "Chopping and pitching samples digitally (in-DAW time-stretching) for modern flip techniques beyond classic hardware sampler limitations" — the core technique (cut a source into pieces, rearrange and pitch them) is constant from the turntable/MPC era through modern DAW-based sampling, even as the tools changed.

## The Chopped-and-Screwed Family

`phonk.md` documents an entire sound-design identity built around one specific manipulation of the chopping technique: "Chopped and screwed technique — slowing tempo and lowering pitch of a sampled source — is the genre's foundational and most identifiable production device." The file is explicit that this isn't an occasional effect but the genre's core sonic signature, applied specifically to vocal samples for "a gritty, nostalgic, menacing atmosphere." `cloud_rap.md` cites the same lineage from a different angle — "Codeine/lean-influenced slowed-down aesthetic (via chopped and screwed)" — tracing the technique's origin to Houston's DJ Screw and its specific cultural association with a slowed, hazy listening experience, distinct from phonk's darker menace despite using the same underlying pitch-down/tempo-down technique.

## Chopping Melodic Loops vs. Chopping for Rhythm

`hip_hop.md` and `boom_bap.md` both describe chopping sampled piano/keys loops specifically for melodic/textural material: "Sampled piano/electric piano loops (often chopped and pitched) are a foundational textural element across hip-hop's history" (`hip_hop.md`), and "Sampled jazz or soul piano/electric piano loops (often chopped) are a foundational textural element" (`boom_bap.md`). This is a distinct application from breakbeat chopping (documented in `knowledge_base/midi/patterns/drum_pattern_programming.md` for jungle) — melodic-source chopping targets a harmonic/textural loop, re-cutting it to fit a new tempo or to isolate a usable phrase, while breakbeat chopping targets a rhythmic source and re-arranges its hits into a new drum pattern.

## Pitch and Time as Independent Manipulation Axes

`phonk.md`'s processing notes make explicit that pitch-shifting and time-stretching are applied together but are conceptually separate operations: "Heavy pitch-shifting and time-stretching on vocal samples" — a chop can be slowed without being pitched down (time-stretched), pitched down without being slowed (pitch-shifted), or both simultaneously (the classic "chopped and screwed" combination, which is really tempo-reduction with pitch following proportionally, as opposed to independent time-stretch/pitch-shift processing that keeps one axis fixed).

## Common Mistakes

**Treating "chopped and screwed" as a single generic effect rather than the specific slowed-tempo-plus-lowered-pitch combination it names.** Independently pitch-shifting a sample without also slowing it produces a different, thinner-sounding result than the genuine chopped-and-screwed technique.

**Chopping a melodic loop without regard to its harmonic phrase boundaries.** `boom_bap.md`'s and `hip_hop.md`'s melodic sample chopping depends on cutting at musically sensible points (phrase or bar boundaries) so the resulting loop remains harmonically coherent when repeated — cutting mid-phrase produces an audibly awkward loop point.

## Cross-References

- `knowledge_base/genres/hiphop/hip_hop.md`, `knowledge_base/genres/hiphop/boom_bap.md` — melodic sample chopping as foundational hip-hop sound design
- `knowledge_base/genres/hiphop/phonk.md`, `knowledge_base/genres/hiphop/cloud_rap.md` — the chopped-and-screwed slowed/pitched-down technique family
- `knowledge_base/midi/patterns/drum_pattern_programming.md` — the related but distinct breakbeat-chopping technique for rhythmic (rather than melodic) source material
- `knowledge_base/sound_design/synthesis/granular_synthesis.md` — a related but distinct sample-manipulation approach (granular re-synthesis rather than discrete chop-and-rearrange)
