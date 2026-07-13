---
plugin_name: "Compressor and Glue Compressor"
developer: "Ableton"
category: "compressor"
type: "VCA-style digital compressor, two variants (stock Ableton Live devices)"
cpu_usage: "low"
best_genres:
  - house
  - trance
  - hip_hop
  - techno
strengths:
  - "Both included with every edition of Ableton Live, with clear gain-reduction metering and full automation/macro integration as first-party devices."
  - "Compressor offers a full standard parameter set (threshold, ratio, attack, release, knee) plus a sidechain input, covering general-purpose dynamics control and sidechain-ducking needs directly."
  - "Glue Compressor is modeled on classic bus-compressor behavior (program-dependent auto-release, a characterful, cohesive 'glue' effect) and is purpose-built for bus/group compression rather than single-channel dynamics work."
  - "Very low CPU cost for both, making them practical defaults across many channels and buses in a single session."
weaknesses:
  - "Neither offers the selectable multi-character 'style' modeling of a plugin like FabFilter Pro-C 2 (Clean, Opto, Vocal, Bus, Punch, etc., see `fabfilter_pro_c_2.md`) — Compressor and Glue Compressor each have one fixed character rather than several selectable behaviors in one device."
  - "No true multiband capability in either stock device — multiband compression needs Ableton's separate Multiband Dynamics device or a third-party tool."
alternatives:
  - "FabFilter Pro-C 2 (multiple selectable compression styles, see `fabfilter_pro_c_2.md`)"
  - "Ableton Multiband Dynamics (for frequency-specific compression, see `knowledge_base/mastering/dynamics/multiband_compression_and_limiter_chain_ordering.md` and `knowledge_base/mixing/compression/multiband_compression_for_mix_element_control.md`)"
recommended_settings:
  - "Sidechain pumping: Compressor with fast attack (0-1ms), release synced to a 16th or 8th note, ratio 4:1-10:1, sidechain input from the kick — direct implementation of `knowledge_base/mixing/compression/sidechain_pumping.md`."
  - "Drum bus glue: Glue Compressor with a moderate ratio (2:1-4:1), auto-release engaged, and the Peak/RMS switch set to RMS for a smoother, more programme-averaged gain-reduction response suited to bus-wide cohesion."
common_uses:
  - "Sidechain ducking/pumping compression (Compressor, via its dedicated sidechain input)"
  - "Bus and group glue compression for cohesion across drum buses, mix buses, or the master (Glue Compressor)"
  - "General-purpose single-channel dynamics control (Compressor)"
tags: ["compressor", "glue-compressor", "ableton", "stock-device", "compression", "sidechain"]
---

# Compressor and Glue Compressor (Ableton Live)

Ableton Live ships with two first-party compressors serving distinct roles: Compressor, a general-purpose VCA-style dynamics processor with a full standard parameter set and a dedicated sidechain input, and Glue Compressor, modeled on classic analog bus-compressor behavior and purpose-built for bus/group-wide cohesion rather than single-channel dynamics correction. Both are included with every edition of Live and carry very low CPU cost.

## Compressor: General-Purpose Dynamics and Sidechain Ducking

Compressor's dedicated sidechain input makes it the direct Ableton-native implementation of the sidechain-pumping technique documented in `knowledge_base/mixing/compression/sidechain_pumping.md` — routing a kick or 808 into the sidechain input and setting fast attack with a tempo-synced release produces the genre-standard pumping duck without needing a third-party plugin. Its full standard parameter set (threshold, ratio, attack, release, knee) also makes it a fully capable general-purpose compressor for individual-channel dynamics control beyond sidechain use cases.

## Glue Compressor: Bus-Wide Cohesion

Glue Compressor's auto-release behavior and program-dependent response are modeled on the classic analog bus-compressor character that gives "glue" compression its name — gently gluing a group of tracks (a drum bus, a full mix bus) into a more cohesive-sounding whole rather than correcting any single element's dynamics. This is the direct implementation of the density/cohesion side of the parallel-compression and general bus-compression principles documented in `knowledge_base/mixing/compression/parallel_compression.md`, when used as a light, subtle bus treatment rather than pushed to an aggressive setting.

## Weaknesses

Neither device offers the selectable multi-character modeling that a plugin like FabFilter Pro-C 2 provides in one instance (Clean, Opto, Vocal, Bus, Punch, and other style algorithms) — Compressor and Glue Compressor each have one fixed underlying character, so achieving a genuinely different compression behavior means switching devices rather than switching a style parameter. Neither is multiband either; true frequency-specific compression needs Ableton's separate Multiband Dynamics device.

## Choosing Between the Two

Compressor is the right tool for single-channel dynamics control and any sidechain-ducking task. Glue Compressor is the right tool specifically for gluing a group of already-mixed elements together — reaching for Glue Compressor on a single, isolated channel (rather than a bus) or for Compressor on a full mix bus where cohesion (not individual-signal correction) is the actual goal both miss each device's intended role.

## Common Mistakes

**Using Glue Compressor for single-channel corrective compression, or Compressor for bus-wide glue.** Each device's auto-release/program-dependent behavior (Glue) versus full manual parameter control (Compressor) is tuned for its intended role — swapping them doesn't produce an equivalent result.

**Reaching for a third-party multiband compressor when Ableton's own Multiband Dynamics device (not covered in this entry, but bundled with Live) already covers the need.** Check the native option before adding third-party plugin overhead for a capability Live already includes.

## Cross-References

- `knowledge_base/mixing/compression/sidechain_pumping.md` — the technique Compressor's sidechain input directly implements
- `knowledge_base/mixing/compression/parallel_compression.md` — the density/cohesion principle Glue Compressor applies at the bus level
- `knowledge_base/vst_database/fabfilter_pro_c_2.md` — the multi-character alternative for tasks needing more than one fixed compression style
