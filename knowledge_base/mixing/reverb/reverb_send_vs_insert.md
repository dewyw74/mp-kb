---
technique_name: Reverb Send vs Insert Routing
category: reverb
problem_solved: "Placing reverb as an insert per-track wastes CPU, forces every processed element into the same fixed wet/dry ratio, and makes it impossible to blend multiple sources into a shared, cohesive sense of space or ride the wet level dynamically"
parameters:
  send_routing: "Aux/bus reverb fed by post-fader sends from multiple source tracks, with the reverb itself living on its own return channel — the standard approach for anything that needs level automation or a shared space across elements"
  insert_routing: "Reverb placed directly on a single channel's insert chain, used more rarely and mainly when a fixed, non-automated, 100%-committed spatial character is wanted on one specific element"
  multiple_sends: "Running two or more distinct reverb sends (e.g. a short room and a long hall) simultaneously so different elements can draw different amounts of each character"
signal_chain_position: "Aux send from source track(s) to a dedicated reverb return bus, as opposed to inline on the channel strip itself"
genre_applicability:
  - ambient
  - darkwave
  - cloud_rap
  - shoegaze
  - progressive_house
  - symphonic_black_metal
related_techniques:
  - reverb_automation
  - room_plate_hall_selection
tags: ["reverb-send", "aux-bus", "signal-routing", "parallel-reverb"]
---

# Reverb Send vs Insert Routing

Nearly every reverb mention in the genre corpus that specifies routing at all describes reverb as a **send**, not an insert — fed from one or more source tracks into a shared aux/return bus. This isn't incidental: send routing is what makes reverb automation, multi-element blending, and CPU-efficient large-scale space all possible, and several genre entries treat the send itself (not just the reverb algorithm behind it) as a compositional tool.

## Reverb as the Primary Instrument, Not a Channel Insert

`ambient.md` states the philosophy most explicitly: "Reverb is often the primary instrument, not an effect — use multiple reverb sends of different character (short room for intimacy, long hall/shimmer for scale) blended per layer." This is only possible with send routing — an insert-based reverb is locked to one channel's fixed wet/dry balance, while multiple sends let each layer draw a different proportion of two or more simultaneously-running reverb characters. `darkwave.md` treats its sends as similarly non-optional: "Large reverb sends on vocals and snare are essential rather than optional," language that frames the send level itself as a defining mix decision rather than a background polish step. `cloud_rap.md` pushes the same approach further across the whole arrangement: "Heavy reverb sends on nearly every element" as a core textural signature of the genre.

## Multiple Simultaneous Sends for Layered Space

`symphonic_black_metal.md` documents the clearest case for running more than one reverb send at once, specifically to keep two genre-conflicting spatial characters from collapsing into one undifferentiated wash: "Layer distinct reverb sends — a black-metal-style cavernous vocal reverb and a separate orchestral hall reverb — to preserve each layer's genre-appropriate space without collapsing into a single undifferentiated wash." This is a send-routing problem specifically — achieving it with inserts would require either compromising both elements' spatial character toward a single shared setting, or duplicating a reverb plugin instance per track (defeating the CPU and cohesion benefits sends exist to provide).

## Send Level as an Automatable, Ridable Parameter

Because a send's level lives on the source channel's mixer strip (or a dedicated send fader) rather than buried inside an insert plugin's own wet/dry knob, it's the parameter genre entries describe riding and automating throughout a song — see `reverb_automation.md` for the extensive build/throw examples this enables. `shoegaze.md` adds a routing wrinkle worth noting: sends aren't always dry-in, wet-out — "Reverb sends often processed in stereo with modulation (chorus on the reverb return) to widen and blur the wash further," meaning the reverb *return* channel itself can carry its own additional insert processing (chorus, EQ, saturation) after the reverb, independent of the dry source.

## Conditional/Sidechain-Aware Send Routing

`progressive_house.md` documents a more advanced send-routing technique that specifically depends on reverb living on its own bus rather than an insert: "Using sidechain-triggered reverb ducking (reverb return only ducks against the kick, not the dry signal) to keep pads spacious without pump conflict." This only works because the reverb return is a separate channel that can carry its own sidechain compressor, ducking independently from the dry pad signal underneath it — an insert-based reverb baked into the pad channel itself couldn't be ducked without also ducking the dry pad.

## Common Mistakes

**Inserting reverb per-track when multiple elements need to share a cohesive sense of space.** `ambient.md`'s "primary instrument" framing depends on several layers drawing from the *same* reverb bus (or a shared pair of buses) so they read as occupying one consistent room — inserting separate reverb instances per track tends to produce a mix where every element sounds like it's in a different-sized space.

**Missing the option to process the reverb return itself.** As `shoegaze.md` shows, a reverb send isn't a dead end — the return channel can carry its own chorus, EQ, or compression, giving control over the wet signal's character independent of the dry source's own processing.

**Automating a reverb plugin's internal parameters instead of the send level.** For section-to-section changes (see `reverb_automation.md`), riding the send fader is simpler, more CPU-friendly, and avoids the audible glitches that can come from automating a reverb algorithm's own decay/size parameters mid-tail.

## Cross-References

- `knowledge_base/genres/electronic/ambient.md` — reverb sends as the genre's primary compositional instrument
- `knowledge_base/genres/electronic/darkwave.md` and `knowledge_base/genres/hiphop/cloud_rap.md` — large/heavy reverb sends treated as essential rather than optional
- `knowledge_base/genres/metal/symphonic_black_metal.md` — layering two distinct reverb sends to preserve two genre-conflicting spatial characters at once
- `knowledge_base/genres/rock/shoegaze.md` — processing the reverb return itself (chorus/modulation) rather than treating the send as a dead end
- `knowledge_base/genres/edm/progressive_house.md` — sidechain-ducking a reverb return independently from its dry source, only possible with send routing
- `knowledge_base/mixing/reverb/reverb_automation.md` — the automation techniques that send-based routing specifically enables
