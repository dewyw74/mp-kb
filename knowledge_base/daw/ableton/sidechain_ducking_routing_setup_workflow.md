---
workflow_name: "Ableton Sidechain Ducking: Mechanical Routing Setup"
daw: "ableton"
category: "routing"
goal: "Set up sidechain compression routing in Ableton Live mechanically — enabling the Compressor device's sidechain section, using its Audio From dropdowns to select a trigger track and tap point, and building a filtered sidechain trigger with a duplicate track and EQ so ducking is keyed off a specific frequency range rather than a track's full signal."
steps:
  - "Insert Ableton Compressor on the track or group that should duck (bass, pads, synths) rather than on the trigger track (kick, 808) itself."
  - "Click the Sidechain arrow/chevron on the Compressor device to expand its sidechain section, which is collapsed and hidden by default."
  - "Enable the Sidechain toggle within that expanded section to activate external-input triggering, since Compressor otherwise reacts only to its own track's input."
  - "In the Audio From section's top dropdown, select the track (or bus) that should trigger the ducking — typically the kick or 808 track — from the list of available tracks in the Set."
  - "In the Audio From section's second dropdown, choose the tap point: Pre-FX to trigger from that track's raw input signal before its own device chain processes it, or Post-FX to trigger from its fully processed output; Pre-FX is the more common choice so the sidechain isn't affected by the trigger track's own compression or EQ."
  - "Set Compressor's Attack fast (0-1ms) so it catches the kick's transient instantly, and Release tempo-synced to a 16th or 8th note so the ducked element recovers before the next hit, per the musical settings documented in `knowledge_base/mixing/compression/sidechain_pumping.md`."
  - "To trigger the duck from a specific frequency range rather than the kick's full spectrum, duplicate the kick track (or route a copy to a dedicated trigger track) and insert EQ Eight on the duplicate, filtering it to isolate the frequency range that should do the triggering (for example, high-passing away the sub to trigger only from the kick's beater transient)."
  - "Mute the duplicated/filtered trigger track's audio output (or set it to no output) so it doesn't add an audible extra copy of the kick to the mix — its only job is feeding the sidechain input, not being heard directly."
  - "Select the filtered duplicate track (not the original kick) in Compressor's Audio From dropdown, so the ducking compressor reacts specifically to the EQ'd trigger signal rather than the kick's unfiltered full-range output."
  - "Confirm the duck is audible and rhythmically locked to the trigger by soloing the ducked track against the trigger track, then reference `knowledge_base/mixing/compression/sidechain_pumping.md` for how aggressive the duck should read for the target genre before finalizing ratio and threshold."
related_plugins:
  - "Ableton Compressor"
  - "Ableton EQ Eight"
  - "Ableton Utility"
tags:
  - "ableton"
  - "routing"
  - "sidechain"
  - "ducking"
  - "compressor"
  - "audio-from"
  - "sidechain-eq"
---

# Ableton Sidechain Ducking: Mechanical Routing Setup

`knowledge_base/mixing/compression/sidechain_pumping.md` documents the musical side of sidechain ducking — why genres use it, how aggressive the pump should read, and the ratio/attack/release settings that produce a tight, tempo-locked duck versus a subtle, masking-avoidance-only duck. This entry covers the other half: the literal, mechanical steps to route a sidechain trigger into a compressor in Ableton Live, including the Compressor device's own Sidechain "Audio From" controls and a filtered-trigger setup for keying the duck off a specific frequency range rather than a track's full signal.

## Enabling Compressor's Sidechain Section

Ableton's stock Compressor device has a dedicated sidechain input, but its controls are hidden by default: expand them by clicking the Sidechain arrow/chevron on the device, then enable the Sidechain toggle inside that expanded section. Until that toggle is on, Compressor only reacts to its own track's input signal, regardless of what's selected in the Audio From dropdowns below it — this is the step most commonly missed when a sidechain setup "isn't working."

## The Audio From Dropdowns: Track and Tap Point

Once sidechain is enabled, two dropdowns under Audio From determine the trigger source. The top dropdown selects which track or bus in the Set should trigger the compressor — the kick or 808 track, most commonly. The second dropdown selects the tap point on that source: Pre-FX routes from the trigger track's raw input, before any of its own devices process it, while Post-FX routes from its fully processed output. Pre-FX is the more common choice specifically because it keeps the sidechain trigger signal independent of whatever compression, EQ, or saturation is happening on the trigger track's own chain — a producer tweaking the kick's own processing later shouldn't have to also re-tune every sidechain relationship keyed off it.

## Filtering the Trigger With a Duplicate Track

Compressor's sidechain input reacts to the full-range signal selected in Audio From — there's no built-in EQ on the sidechain input itself. To trigger specifically off a frequency range (for example, ducking bass only when the kick's beater transient is present, ignoring the kick's own sub content so the two don't fight over which one "wins" the low end), build a filtered duplicate: duplicate the kick track, insert EQ Eight on the duplicate and shape it to isolate the target range, then mute that duplicate's audible output so it exists purely as a sidechain trigger feed rather than an audible extra copy of the kick. Select this filtered duplicate — not the original kick track — in the ducking compressor's Audio From dropdown. This duplicate-and-filter approach is the standard Ableton-native way to get frequency-specific sidechain triggering, since the routing itself only offers track/tap-point selection, not built-in frequency filtering.

## Handing Off to the Musical Settings

Once the trigger is correctly routed — enabled, source selected, tap point chosen, and filtered if the frequency-specific approach is being used — the remaining decisions (attack, release, ratio, threshold, and how aggressive the resulting pump should sound) are musical rather than routing decisions, and are documented in full in `knowledge_base/mixing/compression/sidechain_pumping.md`. A fast attack (0-1ms) and a release tempo-synced to a 16th or 8th note are the standard starting point for a tight, rhythmic duck; that entry's genre-by-genre guidance determines how far to push ratio and threshold beyond that starting point.

## Common mistakes

Setting the Audio From track and tap point correctly but forgetting to enable the Sidechain toggle itself, leaving the compressor still reacting only to its own track's input. Leaving a filtered duplicate trigger track's audio output unmuted, adding an unintended extra copy of the kick to the mix. Selecting Post-FX as the tap point without a specific reason, making the sidechain relationship dependent on the trigger track's own device chain in a way that complicates later mix changes. Trying to achieve frequency-specific triggering by adjusting the ducking compressor's own settings, when Compressor's sidechain input has no built-in EQ — the duplicate-and-filter trigger track is the actual mechanism for that in Ableton.

## Cross-References

- `knowledge_base/mixing/compression/sidechain_pumping.md` — the musical settings (ratio, attack, release) and genre-specific intensity this routing setup feeds into
- `knowledge_base/daw/ableton/mixing_bus_routing_and_gain_staging_workflow.md` — the broader group-bus structure a sidechain-ducked bass or pad bus typically sits within
