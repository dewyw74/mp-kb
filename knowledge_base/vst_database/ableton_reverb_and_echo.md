---
plugin_name: "Reverb and Echo"
developer: "Ableton"
category: "reverb"
type: "Algorithmic reverb and tempo-syncable delay, two devices (stock Ableton Live)"
cpu_usage: "medium"
best_genres:
  - house
  - trance
  - hip_hop
  - dub_techno
strengths:
  - "Both included with every edition of Ableton Live, with full tempo-sync and automation/macro integration as first-party devices."
  - "Reverb offers selectable room-size character and a distinct early-reflection/diffuse-tail split with independent controls, covering the predelay and early-reflections technique documented in `knowledge_base/mixing/reverb/predelay_and_early_reflections.md` natively."
  - "Echo (Live's more advanced delay device, successor to the older Simple/Ping Pong Delay devices) supports tempo-synced subdivisions, stereo ping-pong routing, and built-in modulation/character controls (noise, wobble, filtering) in one device."
  - "Low-to-moderate CPU cost, practical as a send-bus effect across a full session."
weaknesses:
  - "Ableton's stock Reverb doesn't match a dedicated convolution reverb's ability to load real impulse responses of specific physical spaces — it's a purely algorithmic device."
  - "Echo's built-in character/modulation controls, while extensive, don't match a dedicated vintage-delay-modeling plugin's specific hardware-unit emulation depth."
alternatives:
  - "Valhalla VintageVerb (colored, era-specific reverb character, see `valhalla_vintageverb.md`)"
  - "A convolution reverb plugin (for real-space impulse-response-based reverb, not currently documented in this knowledge base's vst_database)"
recommended_settings:
  - "Genre-scale-matched reverb: set Reverb's room size and decay to match the target genre's scale per `knowledge_base/mixing/reverb/reverb_types_and_selection.md`, with predelay set per `knowledge_base/mixing/reverb/predelay_and_early_reflections.md` to preserve vocal/transient clarity."
  - "Ping-pong rhythmic delay: Echo with sync mode engaged, a 16th or 8th-note (straight or dotted) subdivision, stereo ping-pong routing enabled, and feedback set low for subtle width or higher for a more pronounced rhythmic repeat, per `knowledge_base/mixing/delay/ping_pong_and_multi_tap_delay_design.md`."
common_uses:
  - "Send-bus reverb for genre-scale-matched spatial treatment across vocals, leads, and pads"
  - "Tempo-synced rhythmic and ping-pong delay for width and hypnotic movement on leads/vocals"
  - "Short slap-back delay for vocal/lead thickness without a perceptible rhythmic echo"
tags: ["reverb", "echo", "ableton", "stock-device", "reverb", "delay"]
---

# Reverb and Echo (Ableton Live)

Ableton Live's first-party Reverb and Echo devices are the native Ableton implementation of most of the spatial and delay techniques documented in `knowledge_base/mixing/reverb/` and `knowledge_base/mixing/delay/`. Both are included with every edition of Live, carry low-to-moderate CPU cost, and integrate directly with Live's tempo sync, automation, and macro-mapping systems as first-party devices.

## Reverb: Algorithmic Space With Independent Early-Reflection Control

Ableton's Reverb device separates early reflections from the diffuse reverb tail with independent controls for each — a direct native implementation of the predelay and early-reflections technique documented in `knowledge_base/mixing/reverb/predelay_and_early_reflections.md`, where a gap between a dry source and its reverb tail (and the character of the reflections that arrive before that tail builds up) preserves transient/vocal clarity even at a large, genre-appropriate reverb size. Its selectable room-size and character options cover the scale-matching principle from `knowledge_base/mixing/reverb/reverb_types_and_selection.md` — from tight, small-room settings to large hall/cathedral-scale spaces — within one device.

## Echo: Tempo-Synced, Modulation-Capable Delay

Echo (Live's more advanced delay device) supports tempo-synced subdivisions and stereo ping-pong routing directly, implementing both the tempo-synced rhythmic delay technique in `knowledge_base/mixing/delay/delay_types_and_sync.md` and the ping-pong stereo-alternating technique in `knowledge_base/mixing/delay/ping_pong_and_multi_tap_delay_design.md` natively in one device, without needing a separate stereo-imaging plugin downstream. Its built-in character controls (noise, wobble, filtering on the repeats) let a delay's repeats degrade or color over successive echoes, a texture-design option beyond a purely clean, transparent delay line.

## Weaknesses

Neither device reaches into more specialized territory: Reverb is purely algorithmic rather than convolution-based, so it can't load an impulse response of an actual physical space the way a dedicated convolution reverb plugin can, and Echo's character/modulation controls, while genuinely useful, don't model a specific vintage hardware delay unit's exact circuit behavior the way a dedicated vintage-delay-emulation plugin would.

## Common Mistakes

**Reaching for a third-party reverb/delay plugin by default without checking whether Live's stock devices already cover the need.** Both stock devices cover the large majority of the genre-scale-matching, predelay, and tempo-sync techniques documented in this knowledge base's mixing guidance — third-party tools add real value for specific colored character (per `knowledge_base/vst_database/valhalla_vintageverb.md`) or convolution/real-space accuracy, not as a blanket upgrade.

## Cross-References

- `knowledge_base/mixing/reverb/reverb_types_and_selection.md`, `knowledge_base/mixing/reverb/predelay_and_early_reflections.md` — the general reverb techniques this device directly implements
- `knowledge_base/mixing/delay/delay_types_and_sync.md`, `knowledge_base/mixing/delay/ping_pong_and_multi_tap_delay_design.md` — the general delay techniques Echo directly implements
- `knowledge_base/vst_database/valhalla_vintageverb.md` — a colored, era-specific reverb alternative for when Reverb's more neutral algorithmic character isn't what a genre calls for
