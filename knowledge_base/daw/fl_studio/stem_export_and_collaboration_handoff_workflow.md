---
workflow_name: "FL Studio Stem Export and Collaboration Handoff"
daw: "fl_studio"
category: "templates"
goal: "Export sample-accurate, correctly-named multitrack stems from FL Studio using the 'Split Mixer Tracks' export option, so a collaborator or external mixing engineer receives a clean, aligned, clearly-labeled set of files rather than a single stereo bounce."
steps:
  - "Confirm every element that needs its own stem already sits on its own Mixer insert per `knowledge_base/daw/fl_studio/mixer_routing_resampling_and_freezing.md` — any two sounds sharing one insert will export as a single combined stem, not two separate files."
  - "Name every Mixer insert clearly by role before exporting (Kick, Snare, Bass, Lead_Vocal, BGVs, Synths, FX) per the naming convention in `knowledge_base/daw/fl_studio/project_templates_and_mixer_conventions.md`, since FL Studio uses these insert names directly in the exported stem filenames."
  - "Decide whether Master Effects (any processing on the Master insert itself) should be included in the stems or excluded, and disable Master Effects in the export settings when the recipient needs unmastered, individually processed stems rather than stems with the master chain baked in."
  - "Leave Insert Effects enabled in the export settings when each stem should carry its own bus-level processing (EQ, compression, saturation already dialed in on that insert), which is the normal choice for a collaborator who's continuing the mix rather than starting dynamics from scratch."
  - "Open File > Export > Wave file (or the target format), and check the 'Split Mixer Tracks' option in the export settings so every Mixer insert renders as its own file instead of a single summed stereo bounce."
  - "Set sample rate and bit depth to match the project's working settings (typically 24-bit, project sample rate) rather than a lower-fidelity consumer export setting, since stems are a mixing/collaboration deliverable, not a final listening file."
  - "Render the export and confirm the resulting files are sample-accurately aligned — because every stem is rendered from the same Playlist timeline in one export pass, all files start at the same sample position and will re-align automatically when imported together into another DAW."
  - "Rename or organize exported files with a consistent handoff convention (project name, stem role, version/date) if the raw insert-name-based filenames aren't already descriptive enough for the recipient, and include a reference mix/rough bounce alongside the stems so the collaborator has a target to check alignment and balance against."
related_plugins:
  - "FL Studio Mixer"
  - "FL Studio Playlist"
tags:
  - "fl-studio"
  - "stems"
  - "export"
  - "collaboration"
  - "multitrack"
  - "split-mixer-tracks"
  - "templates"
  - "workflow"
---

# FL Studio Stem Export and Collaboration Handoff

`knowledge_base/daw/fl_studio/master_bus_chain_and_export_workflow.md` covers exporting a single finished master file, and its Alternatives section already notes that a track headed to an outside mixing or mastering engineer should skip the limiter/loudness stages and export a clean, headroom-preserving bounce instead. This entry covers the adjacent but distinct case: exporting a full set of individual stems — one file per Mixer insert or group — for a collaborator who needs to work with the separate elements rather than a single stereo file, using FL Studio's "Split Mixer Tracks" export option.

## One insert, one stem

FL Studio's stem export works at the Mixer-insert level, not the Channel Rack instrument level — everything routed to a given insert exports as one combined file. If two hi-hats or two vocal takes are meant to become separate stems, they need to already be on separate inserts before export; consolidating them onto one insert for convenience during mixing means they'll export as a single, unsplittable stem later. This makes the routing discipline in `knowledge_base/daw/fl_studio/mixer_routing_resampling_and_freezing.md` — one instrument (or one intentional group) per insert — a direct prerequisite for a usable stem export, not just a mixing-session convenience.

## Naming inserts before exporting, not after

FL Studio names each exported stem file after its source Mixer insert, so insert names chosen during setup become the actual filenames a collaborator receives. Apply the naming convention `knowledge_base/daw/fl_studio/project_templates_and_mixer_conventions.md` already recommends for template setup — `Kick`, `Bass`, `Lead_Vocal`, `BGVs`, `Synths`, `FX` — before exporting rather than after, since generic default insert names (`Insert 3`, `Insert 7`) turn directly into equally unhelpful stem filenames that force the recipient to open and identify every file by ear.

## Choosing what processing rides along in the stems

Decide deliberately whether Insert Effects and Master Effects should be baked into the exported stems. Leaving Insert Effects enabled carries each stem's own bus-level EQ, compression, and saturation into the export — the right choice when a collaborator is continuing work on an already-shaped mix rather than starting dynamics from zero. Disabling Master Effects specifically keeps whatever's on the Master insert (a mix-bus compressor, a loudness-matching utility) out of every individual stem, which matters because baking master-bus processing into stems meant for further mixing effectively forces that processing onto every element permanently, with no way for the recipient to undo it.

## The Split Mixer Tracks export option

In the export dialog (File > Export > Wave file or the target format), check "Split Mixer Tracks" to render every Mixer insert as its own file in a single export pass, rather than the default single summed stereo bounce. Because every stem is rendered from the same Playlist timeline in that one pass, all resulting files share the same start position and sample-accurate alignment — reimporting the full set into another DAW (or handing them to a collaborator working in a different DAW entirely) reconstructs the mix's timing exactly, with no manual nudging required on the receiving end.

## Export settings and handoff hygiene

Render at 24-bit and the project's working sample rate rather than a lower-fidelity consumer setting, since stems are a mixing deliverable that may go through further processing, not a final listening file. Once exported, apply a consistent file-naming and organization convention beyond the raw insert names if the recipient needs more context (project title, stem role, date or version), and include a rough reference bounce of the full mix alongside the stems so the collaborator has something to check balance and alignment against as they work.

## Common mistakes

Leaving two or more sounds sharing a single Mixer insert and expecting them to export as separate stems — the split only happens at the insert level, so anything sharing an insert exports combined regardless of intent. Exporting with default, unnamed inserts and handing off a set of files labeled `Insert 1` through `Insert 12`, forcing the recipient to identify every stem by ear before they can start working. Leaving Master Effects enabled in the export and unknowingly baking mix-bus processing into every stem, which the recipient then can't remove. Skipping a reference mix in the handoff, leaving the collaborator with no quick way to confirm the received stems actually sum back into the intended balance.

## Cross-References

- `knowledge_base/daw/fl_studio/master_bus_chain_and_export_workflow.md` — exporting a single finished master file, as distinct from this entry's multitrack stem export
- `knowledge_base/daw/fl_studio/mixer_routing_resampling_and_freezing.md` — the one-instrument-per-insert routing discipline this workflow depends on
- `knowledge_base/daw/fl_studio/project_templates_and_mixer_conventions.md` — the Mixer insert naming convention that determines exported stem filenames
