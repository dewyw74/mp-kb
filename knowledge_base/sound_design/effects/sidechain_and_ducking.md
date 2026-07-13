---
title: "Sidechain Compression and Gated Ducking as a Sound-Design Tool"
effect_type:
  - "Sidechain compression"
  - "Sidechain EQ / multiband ducking"
  - "Gate-based ducking"
  - "Envelope-follower modulation"
tags:
  - "sidechain"
  - "ducking"
  - "pumping"
  - "gate"
  - "envelope-follower"
  - "pad-design"
  - "bass-design"
  - "rhythmic-modulation"
  - "house"
  - "techno"
  - "dubstep"
  - "riddim"
---

# Sidechain Compression and Gated Ducking as a Sound-Design Tool

## Scope: this is not mix-bus sidechain

`mixing_agent` owns mix-bus-level sidechain compression — tuning threshold/ratio/attack/release on a kick-into-bass or kick-into-mix-bus chain so the low end stays uncluttered and the overall mix reads as cohesive and glued. That is a corrective/cohesion tool applied at mixdown.

This entry covers a different use of the same mechanism: sidechaining and ducking **designed into a specific patch as a compositional and sonic feature**, decided at the sound-design stage, before the part ever reaches a mix bus. The "pumping pad" in a house or EDM track isn't glue — it's the pad's defining timbral character, as load-bearing to that patch's identity as its oscillator or filter choice. If a technique changes what a part *sounds like* and is part of the patch, it belongs here. If it changes how already-designed parts *sit together*, it belongs to `mixing_agent`.

## Sidechain compression as a creative parameter, not a corrective one

Mechanically, sidechain compression is unchanged from its mixing use: a trigger source (almost always the kick) feeds a compressor's sidechain input, and the compressor ducks a target signal (pad, bass, lead) in response. What changes is the intent behind each parameter:

- **Threshold** — set low enough that *every* kick hit triggers a duck, because the rhythmic pulse itself is the desired effect, not an occasional safety net against masking.
- **Ratio** — pushed higher (8:1 and beyond, sometimes into limiting territory) specifically to create an audible, rhythmic gap rather than a few dB of gentle level correction.
- **Attack** — set fast enough to carve a hard, percussive dip at the start of the duck; the transient of the dip is part of the groove.
- **Release** — the parameter that actually *composes* the pumping feel. A release tuned to the track's tempo (synced to a 16th, 8th, or quarter note) makes the pad "breathe" in time with the beat; a release shorter than the beat interval creates a double-pump or stutter; a release that never fully recovers before the next kick creates a permanently ducked, rhythmically-gated texture rather than a single pump per beat.

The deciding factor for whether this is sound design or mixing: is the ducking amount/shape being chosen to make the *part* sound the way it's supposed to sound, or to make it *fit* around other parts that are already mixed? The former is this entry's territory.

## The classic "pumping pad" technique

The genre files in this knowledge base treat kick-triggered pad/bass ducking as a genre-defining sonic signature, not an afterthought:

- `knowledge_base/genres/edm/house.md` names it explicitly as a production identity marker: "Sidechain the kick into bass and pads for the essential 'pumping' house groove feel — it's as much a genre signature as a technical tool," and lists it under both `sound_design.processing` and `mixing.compression` as "the 'pumping' house groove feel."
- `knowledge_base/genres/edm/melodic_techno.md` uses the same mechanism but tuned for restraint: "Moderate sidechain compression to maintain groove cohesion without ducking the melodic content too aggressively" — the pump is present but subordinate to the arpeggio/lead material it shares space with.
- `knowledge_base/genres/edm/dub_techno.md` is the useful counter-example: it calls for ducking "kept subtle to preserve the genre's spacious, unhurried feel," and states plainly that "aggressive pumping compression works against the aesthetic." The absence (or extreme subtlety) of the pump is itself a deliberate sound-design choice for that genre — proof that "how much pump" is a genre-character decision, not a default setting.

Patch-design implication: when a pad is meant to pump, design the pad's own envelope and sustain character around the duck from the start (see the "designing for an external trigger" section below) rather than bolting a compressor onto a pad that was voiced to sit at a constant level.

## Sidechain EQ: ducking frequency bands instead of full-band level

A full-band sidechain compressor ducks the whole target signal every time it triggers. Sidechain EQ (multiband/frequency-selective ducking) instead carves out only the band that conflicts with or should rhythmically echo the trigger, leaving the rest of the target signal untouched — a more surgical, creative-effect version of the same idea:

- Duck only the low-mid band of a pad on the kick, leaving its high shimmer/air content constant — the pad still "breathes" rhythmically but doesn't lose its perceived brightness or width on every hit.
- `knowledge_base/genres/edm/dubstep.md` documents a related technique in its modern production notes: "Using sidechain-triggered reverb ducking to keep pads spacious in breakdowns without clouding the drop's low end" — here the *reverb send* specifically is the ducked signal, not the dry pad, so the pad stays present while its tail clears out of the way rhythmically.
- Practically: split the target into bands (a multiband dynamics processor, or parallel EQ'd sends each compressed independently) and apply different sidechain amounts/timings per band for a more three-dimensional pumping effect than a single full-band duck can produce.

## Gate-based ducking: the riddim/dubstep-adjacent alternative

Sidechain compression reacts to signal level; a gate (or LFO/step-sequenced amplitude modulation) instead switches or scales a signal's level against a fixed, programmed rhythmic pattern, independent of an audio trigger's dynamics. This is the mechanism behind riddim's core sound:

- `knowledge_base/genres/edm/riddim.md` describes this directly as the genre's defining sound-design skill: "Tightly quantized LFO or step-sequenced modulation on filter cutoff and/or amplitude, precisely locked to the half-time groove — this rhythmic precision is the genre's defining sound design skill," calling the mechanism itself "the core 'riddim' mechanism."
- The same file also documents true kick-triggered sidechain layered *on top of* the gate pattern as a further refinement: "Using sidechain/ducking from the kick into the bass pattern itself to add extra rhythmic punctuation within the wobble" — gate and sidechain aren't mutually exclusive; riddim's modern production technique stacks both, gate for the core pattern, sidechain for extra accenting.
- Gate-based ducking is preferable to audio-triggered sidechain when the rhythmic pattern needs to be independent of an actual kick transient (e.g., a pattern faster or more complex than the kick, or a pattern that needs to run even in sections where the kick drops out) — the trade-off is that a gate needs to be manually synced/programmed, where sidechain compression tracks a live trigger automatically.
- See `knowledge_base/sound_design/presets/edm_bass_design.md` for a full patch recipe built around gate-based amplitude/filter modulation for riddim-style bass.

## Designing a patch around an external trigger from the start

The strongest version of this technique treats the duck as part of the patch's envelope design, not an effect added afterward:

1. **Give the pad a naturally slow attack.** A pad voiced with a 200-500ms amp attack has almost no transient of its own — its perceived "hit" timing is entirely handed over to whatever ducks it. Combined with sidechain ducking synced to the kick, the pad's audible swell happens *in the gap* between kicks, and the next kick cuts it off right as it reaches full level — producing a rhythmic pulse that the pad's own envelope couldn't create alone.
2. **Voice the sustain to be tolerant of being cut short.** Since the duck (not the patch's own release) will define the audible note length in practice, sustain-heavy, evolving pad content (slow filter LFO, unison drift, long reverb tails) reads better than content that needs to fully resolve to sound "finished."
3. **Decide the release-vs-tempo relationship deliberately**, per the parameter discussion above — full recovery before the next hit (single clean pump), partial recovery (permanently gated, more aggressive texture), or recovery timed to a subdivision different from the trigger (polyrhythmic pumping).
4. **Route the reverb/delay send through its own ducking stage** if the dry signal and its tail need different rhythmic behavior (see the dubstep sidechain-triggered reverb ducking example above) — this keeps the tail from smearing into the next transient without flattening the dry pad's own duck curve.

Once the patch is built this way, handing it to `mixing_agent` is still appropriate for anything beyond the patch itself: bus-level glue compression, deciding how this already-pumping pad sits in level against the rest of the arrangement, or correcting masking against other elements it wasn't designed against. The pump itself, tuned as part of the patch, should not be re-tuned at mixdown as if it were a mix problem.
