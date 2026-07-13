---
technique_name: Stereo Width and Mono-Compatibility Strategy
category: stereo
problem_solved: "Deciding what should be wide versus centered/mono in a mix — getting this backward (wide bass/kick, narrow hooks) undermines both club/system translation and the sense of scale a genre depends on"
parameters:
  mono_core: "Kick, bass/sub, and lead vocal are the most consistently centered/mono elements across genres, for phase coherence and club/system translation"
  wide_candidates: "Pads, harmonies, doubled rhythm guitars, hi-hats/percussion, and atmospheric elements are the most consistently widened elements"
  double_tracking: "Recording or duplicating a part twice and hard-panning left/right (rather than using a stereo effect on a single track) is the most cited method for genuine, phase-stable width on guitars"
signal_chain_position: "Panning and width decisions made per-element before bus processing; mono-compatibility should be checked (sum to mono and listen) especially on any element carrying low-frequency content"
genre_applicability:
  - house
  - jungle
  - metal
  - shoegaze
  - post_rock
  - psychedelic_rock
  - garage_rock
  - delta_blues
  - space_rock
  - southern_rock
  - idm
  - vaporwave
related_techniques:
  - reverb_types_and_selection
  - delay_types_and_sync
tags: ["stereo-imaging", "mono-compatibility", "double-tracking", "panning", "width"]
---

# Stereo Width and Mono-Compatibility Strategy

Stereo imaging decisions across this knowledge base follow one near-universal rule even in genres that otherwise disagree on almost everything else: low-frequency and rhythm-critical elements (kick, bass, lead vocal) stay centered or mono, while harmonic and textural elements (pads, harmonies, doubled guitars, percussion) get spread wide. The genres differ enormously in *how wide* "wide" gets and in how much width the overall aesthetic wants, but the core split — narrow foundation, wide texture — recurs constantly.

## The Consistent Core: Centered Low End

`house.md` states the principle plainly: "Kick and bass centered and mono/near-mono for club translation; hats, percussion, and chord stabs spread wider for groove texture." This isn't an aesthetic preference so much as a technical necessity — `jungle.md`'s frequency-balance notes make explicit why sub-frequency content specifically needs to stay mono: bass and sub content panned wide risks phase cancellation when a system sums to mono (common on club systems, Bluetooth speakers, and broadcast), which can partially or fully cancel the low end. This same "centered bass/kick, wide everything else" split appears independently across otherwise unrelated genres — `metal.md` ("bass, kick, and lead vocal centered"), `nu_metal.md` ("Guitars and bass often centered/tight for groove impact; turntable/sample elements and vocal layers given width for texture"), and `darksynth.md` ("Bass and kick kept centered/mono for maximum impact").

## Double-Tracking as the Preferred Width Method for Guitars

Where a genre wants a guitar wall of sound, the consistently cited method is double-tracking — recording (or programming) the same part twice with natural performance variation, then hard-panning the two takes left and right — rather than applying a stereo widener effect to a single track. `metal.md`'s production notes are explicit: "Double-track rhythm guitars and pan hard left/right for the genre's characteristic wide, powerful wall of sound." `grunge.md` and `metalcore.md` both document the identical technique. The reason double-tracking is preferred over a synthetic widener is phase stability: two genuinely independent performances (or takes) panned apart don't have the same phase-cancellation risk in mono as an artificially decorrelated single source can, and the natural micro-timing differences between two real takes read as a fuller, more organic width than most algorithmic wideners produce.

## Extreme Width as a Genre-Defining Signature

Several genres treat width itself — not just as a mixing choice but as a core sonic identity — far beyond the "narrow core, wide texture" default. `shoegaze.md` states this most directly: "Extremely wide — multiple guitar layers are hard-panned and stacked to create an immersive, enveloping stereo field; this width is one of the genre's core sonic signatures." `space_rock.md` extends the same idea to a genre built around "vastness and motion": "synth sweeps, phased guitars, and layered textures are spread and automated across the stereo field." `psychedelic_rock.md` goes further still, using panning itself as an expressive, moving device rather than a static placement decision: "hard-panned elements, phasing/flanging sweeps across the stereo field, and panning automation used as an expressive device rather than just a placement tool." `post_rock.md` shows width used dynamically as part of a track's structural arc: "Very wide, especially at climaxes... quiet sections can be comparatively narrower and more intimate before widening as the piece builds" — width itself becomes a build/release tool, not a fixed setting for the whole track.

## Deliberately Narrow: Mono as an Aesthetic Choice

A number of genre entries specify narrow or near-mono imaging as a deliberate aesthetic decision rather than a limitation. `delta_blues.md` states it plainly: "Mono or near-mono, single-source recording aesthetic." `garage_rock.md` frames this historically: "Often fairly narrow/mono-leaning, especially in period-authentic productions reflecting the era's mono or simple stereo recording setups." `vaporwave.md` uses narrowness as a specific nostalgia device: "Often narrower and less 'hi-fi wide' than modern productions, intentionally emulating consumer cassette/VHS stereo limitations; occasional mono-summed sections for authenticity" — here mono isn't a technical constraint being worked around but an intentionally chosen texture in its own right, in the same way a genre might intentionally use tape saturation or bit-reduction.

## Unconventional and Rule-Breaking Width

`idm.md` is worth flagging as a genre that deliberately violates the "narrow core, wide texture" convention as a stylistic device: "Extremely wide and unconventional; hard-panned granular fragments, mono-to-stereo glitch effects, and unpredictable stereo movement are common techniques." This is a reminder that the centered-bass/wide-texture split documented above is a strong default, not an inviolable rule — genres built around disorientation or unpredictability can and do treat stereo placement itself as a compositional variable rather than a fixed mixing convention.

## Common Mistakes

**Panning bass or kick content away from center.** This is the most consistently flagged error across genre files, because of the mono-compatibility and phase-cancellation risk documented under `jungle.md`'s frequency-balance guidance — any element carrying significant sub-100Hz content should default to centered/mono unless a genre (like `idm.md`) specifically calls for breaking that rule as a deliberate effect.

**Using a stereo widener plugin instead of double-tracking for guitar walls.** As documented under `metal.md`, `grunge.md`, and `metalcore.md`, genuine double-tracked performances panned hard left/right produce more natural, phase-stable width than algorithmic widening on a single source, which can introduce mono-compatibility problems of its own.

**Treating width as a fixed, track-long setting rather than a dynamic tool.** `post_rock.md`'s climax-vs-quiet-section width contrast shows that stereo width can and should move over the course of a track in genres built around dynamic build/release, rather than being set once during initial mixing and left static.

## Cross-References

- `knowledge_base/genres/edm/house.md` and `knowledge_base/genres/edm/jungle.md` — centered kick/bass for club/mono-system translation
- `knowledge_base/genres/metal/metal.md`, `knowledge_base/genres/rock/grunge.md`, `knowledge_base/genres/metal/metalcore.md` — double-tracked, hard-panned guitars as the preferred width method
- `knowledge_base/genres/rock/shoegaze.md`, `knowledge_base/genres/rock/space_rock.md`, `knowledge_base/genres/rock/psychedelic_rock.md` — extreme width as a core genre signature
- `knowledge_base/genres/rock/post_rock.md` — width used dynamically across a track's build/release arc
- `knowledge_base/genres/rock/delta_blues.md`, `knowledge_base/genres/rock/garage_rock.md`, `knowledge_base/genres/electronic/vaporwave.md` — narrow/mono imaging as a deliberate aesthetic choice
- `knowledge_base/genres/electronic/idm.md` — deliberately unconventional, rule-breaking stereo placement as a compositional device
