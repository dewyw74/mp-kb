---
technique_name: "Bus / Group Glue Compression"
category: compression
problem_solved: "A collection of individually well-mixed elements (a choir, a horn section, a pad/synth layer, or the entire mix bus) still sounding like separate parts rather than one cohesive group, because nothing is gently linking their dynamics together"
parameters:
  ratio: "Typically low (1.5:1 to 2.5:1) when the goal is transparent cohesion; higher when glue is meant to be an audible genre signature rather than an invisible finishing touch"
  attack: "Slow-to-medium in most cited cases, so the compressor reacts to the group's overall level movement rather than grabbing individual transients within it"
  gain_reduction_depth: "Light — typically 1-3dB of gain reduction is enough for cohesion; deeper reduction starts to sound like the group is being actively compressed rather than gently unified"
  scope: "Applied to a bus carrying multiple related elements (a section, a group, or the full mix) rather than a single element — the whole point is linking multiple sources' dynamics together"
signal_chain_position: "Insert on a group bus (backing vocals, horns, pads, percussion section) or the full mix bus, downstream of individual-element processing"
genre_applicability:
  - modal_jazz
  - choral_music
  - kizomba
  - zouk
  - latin_jazz
  - disco
  - trance
  - techno
  - liquid_dnb
  - quiet_storm
  - chicago_house
related_techniques:
  - parallel_compression
  - serial_multi_stage_compression
  - compressor_topology_comparison
tags: ["glue-compression", "bus-compression", "cohesion", "group-bus", "mix-bus"]
---

# Bus / Group Glue Compression

Glue compression links the dynamics of multiple related sources — a choir, a percussion section, a synth-pad layer, or an entire mix — so they move together rather than independently, reading as one cohesive group instead of a stack of separately-processed parts. This entry covers that group/mix-bus-wide use specifically, distinct from drum-bus compression aimed at a single kit (documented separately in this knowledge base's drum-bus compression entry). Genre files describe glue compression across a wide range of intensities, from barely-perceptible cohesion on acoustic ensembles to a genre-defining heavy squash, and the amount of gain reduction used tracks what each genre actually wants listeners to hear.

## Group Bus Glue Beyond Drums

`choral_music.md` documents glue compression applied to an entire vocal section rather than a drum kit: "Use very transparent, slow-acting optical compression (like an LA-2A) on the choir bus to gently glue the voices together without crushing their natural dynamic breathing." `modal_jazz.md` applies the same idea to a full acoustic ensemble captured on multiple microphones: "Careful stereo bus glue compression (very low ratio, slow attack) to unify a multi-mic acoustic ensemble without killing dynamics." `latin_jazz.md` scopes it to a percussion section specifically: "Apply bus compression to the full percussion section for club/dance-floor translation without losing individual instrument transient character." `kizomba.md` and `zouk.md` both apply light glue compression to a pad/synth group rather than an acoustic section — `kizomba.md`: "light bus compression across pads for cohesion," `zouk.md`: "light bus compression across pads and synths for glue." Across all five, the target is a specific group of related elements, not the full mix — the compressor's job is making that one group sound like it's breathing together.

## Full Mix-Bus Glue as a Genre Signature

Several genres push glue compression further, applying it across the entire mix and treating the resulting cohesion — sometimes with audible gain reduction — as part of the genre's identity rather than an invisible finishing step. `disco.md` states this most directly: "Heavy mix-bus compression to 'glue' the massive orchestra, rhythm section, and vocalists together, keeping the track punching relentlessly." `trance.md` applies the same full-mix scope specifically at a track's most dense moments: "Bus compression/glue on the full mix during peak sections," with its mixing section adding that "bus compression glues the full-density drop sections together." `techno.md` frames mix-wide glue as inseparable from the genre's groove: "Bus compression and saturation for cohesive, punchy groove glue," with sidechain ducking handling the rhythmic pump separately from this broader glue role. In all three, glue compression isn't hiding — it's part of what makes the genre's mix-bus sound the way it does.

## Gentle, Transparent Glue vs Audible, Heavy Glue

Set side by side, the corpus shows a clear spectrum rather than one universal "bus compression" setting. `liquid_dnb.md` sits at the gentle end deliberately: "Gentle bus glue compression preserves musical dynamics rather than flattening them; individual break hits compressed lightly for clarity, not extreme punch." `quiet_storm.md` makes the same choice even more explicit as a stated production principle: "Apply light, transparent bus compression to preserve natural vocal dynamics rather than a modern loudness-focused chain." At the opposite end, genres chasing maximum perceived density push glue compression hard enough that the compression itself becomes audible — `disco.md`'s "keeping the track punching relentlessly" and `trance.md`'s peak-section glue both treat noticeable gain movement as a feature, not something to hide. The technique is the same signal-chain move in every case (a compressor across a group bus, unifying dynamics); what differs is how much gain reduction each genre wants a listener to actually perceive.

## When Glue Comes From Something Other Than a Compressor

`chicago_house.md` is a useful counter-citation: "Light compression by modern standards; glue comes from tape/analog mixer saturation rather than heavy bus compression." This is a reminder that "glue" describes a perceptual result — elements sounding like they belong together — not a specific processor. Chicago house gets there through analog saturation's harmonic and dynamic side effects rather than a dedicated compressor doing the unifying work, which is worth knowing before reaching for a compressor as the automatic answer whenever a mix or group needs to sound more cohesive.

## Common Mistakes

**Applying heavy, audible glue compression to material where transparency is the point.** `modal_jazz.md`'s "very low ratio... without killing dynamics" and `choral_music.md`'s "without crushing their natural dynamic breathing" both exist because these genres' expressive range depends on dynamics glue compression could easily flatten — the disco- or trance-style heavy glue described above would actively work against what these acoustic/ensemble genres are trying to preserve.

**Treating group-bus glue and drum-bus compression as the same technique.** The citations here are about linking a section, group, or full mix's dynamics together — a genuinely different job from compressing a single drum kit's internal balance, even though both frequently get called "glue compression" informally.

**Assuming a compressor is always the source of cohesion.** `chicago_house.md`'s reliance on tape/analog mixer saturation rather than heavy bus compression shows that the perceptual goal (elements sounding unified) doesn't always require the tool most associated with it — sometimes saturation, sometimes an even lighter compressor than expected, gets there instead.

**Using the same gain-reduction depth on every genre without checking whether audible glue is wanted or unwanted.** `liquid_dnb.md` and `quiet_storm.md`'s "gentle"/"light, transparent" instructions and `disco.md`/`trance.md`'s "relentless"/full-density-section heavy glue are not interchangeable defaults — copying one genre's gain-reduction depth onto another risks either under-gluing a dance mix that wants audible cohesion or over-flattening an acoustic mix that doesn't.

## Cross-References

- `knowledge_base/genres/classical/choral_music.md` — transparent LA-2A glue compression on a choir bus
- `knowledge_base/genres/jazz/modal_jazz.md` — very-low-ratio stereo bus glue unifying a multi-mic acoustic ensemble
- `knowledge_base/genres/jazz/latin_jazz.md` — bus compression scoped to a full percussion section
- `knowledge_base/genres/world_music/kizomba.md` and `knowledge_base/genres/world_music/zouk.md` — light bus compression across a pad/synth group for cohesion
- `knowledge_base/genres/r_and_b/disco.md` — heavy mix-bus glue as an audible genre signature
- `knowledge_base/genres/edm/trance.md` — full-mix bus glue concentrated at a track's peak/drop sections
- `knowledge_base/genres/edm/techno.md` — mix-wide bus compression and saturation as inseparable from the genre's groove identity
- `knowledge_base/genres/edm/liquid_dnb.md` and `knowledge_base/genres/r_and_b/quiet_storm.md` — deliberately gentle, transparent glue compression
- `knowledge_base/genres/edm/chicago_house.md` — glue achieved through analog/tape saturation rather than heavy bus compression
- `knowledge_base/mixing/compression/parallel_compression.md` — a related density-adding technique often used alongside bus glue compression rather than as a substitute for it
- `knowledge_base/mixing/compression/serial_multi_stage_compression.md` — documents bus glue compression's role as the final stage in several multi-stage compressor chains
