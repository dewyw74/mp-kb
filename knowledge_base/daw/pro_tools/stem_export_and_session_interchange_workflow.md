---
workflow_name: "Pro Tools Stem Export and Session Interchange Workflow"
daw: "pro_tools"
category: "collaboration"
goal: "Export stems correctly using Track Bounce or Bounce to Disk, and hand a session off to another studio, mixer, or picture editor using AAF (preferred) or OMF interchange, since Pro Tools sits at the center of professional post-production and score handoffs where these formats are the actual working standard rather than a fallback option."
steps:
  - "Distinguish Export from Bounce before choosing a method: Export saves selected clips/files largely as-is, bypassing real-time processing, while Bounce prints audio from a chosen output through the full signal chain, including every insert and send — use Bounce for anything that must sound like the current mix."
  - "For multiple simultaneous stems, use Track Bounce (right-click a track, routing folder, or Aux name) rather than Bounce to Disk, since Bounce to Disk only renders one stem mix at a time while Track Bounce can render every selected stem together in one pass."
  - "Route each stem group (drums, bass, music, vocals) through its own submix Aux or Routing Folder Track, per `knowledge_base/daw/pro_tools/session_setup_and_routing_workflow.md`, before bouncing, so each stem actually represents the intended group rather than a re-derived rough mix."
  - "Name exported stem files and folders with a consistent, parseable convention (artist/project, song title, key, tempo, or the studio's house convention) so a receiving engineer can identify contents without opening every file."
  - "For picture or score handoff, use File > Export Selected Tracks as AAF/OMF, having pre-selected only the tracks that should travel — unselected tracks are silently excluded from the export."
  - "Prefer AAF over OMF whenever the receiving system supports it: AAF carries track names and volume/automation data that OMF forces the receiving engineer to manually rebuild, and OMF is additionally capped at a 2GB file size that can silently fail on long or high-sample-rate sequences."
  - "In the Publishing Options dialog, name the sequence clearly and add any handoff notes, then choose 'Breakout to Mono' when the receiving system expects each channel on its own mono track rather than interleaved stereo clips."
  - "Send a flat reference video (commonly H.264, with timecode and clip-name burn-in) alongside any AAF/OMF for picture-locked work, since the interchange file alone does not prove picture sync — the receiving mixer confirms nothing drifted by lining the import up against this reference."
  - "When importing a received AAF/OMF or session, use File > Import > Session Data and set Audio Media Options to 'Copy from Source Media' rather than 'Link to Source Media,' so the new session becomes self-contained instead of depending on the sender's original file locations."
  - "Archive or version the exported stems and interchange files per the general conventions in `knowledge_base/daw/workflow/stem_export_and_session_versioning_conventions_philosophy.md` before deleting any intermediate bounces."
related_plugins:
  - "Pro Tools Track Bounce"
  - "Pro Tools Bounce to Disk"
  - "Pro Tools Export Selected Tracks as AAF/OMF"
  - "Pro Tools Import Session Data"
tags:
  - "pro-tools"
  - "stem-export"
  - "aaf"
  - "omf"
  - "session-interchange"
  - "collaboration"
  - "post-production"
  - "bounce"
---

# Pro Tools Stem Export and Session Interchange Workflow

Pro Tools is the format professional studios, post houses, and film/score mixers standardize around, which makes stem export and session interchange a genuinely different-stakes workflow here than in a producer-to-producer DAW handoff. Two separate jobs sit under this umbrella: rendering audio stems out of a session (Bounce vs. Export, single-stem vs. multi-stem), and moving an entire session's track/edit/automation structure to another system via AAF or OMF. Getting both right is what makes a Pro Tools handoff arrive usable rather than needing to be manually rebuilt on the other end. See `knowledge_base/daw/ableton/stem_export_and_collaboration_handoff_workflow.md` for the same problem solved with Ableton's simpler, non-interchange-format toolset.

## Bounce vs. Export, and Track Bounce for Multi-Stem Work

Export extracts clips or files close to their raw, unprocessed state, while Bounce prints audio from a chosen output through the complete signal path — every insert, every send, every bus — which is why Bounce is the correct choice whenever the output has to actually sound like the current mix. Bounce to Disk historically forced one stem at a time; Track Bounce, run from a track, routing folder, or Aux's right-click menu, renders every selected stem group together in a single pass, which is the practical method for delivering a full stem set (drums, bass, music, vocals) without repeating the bounce process per group.

## AAF vs. OMF for Session Interchange

AAF is the modern interchange standard and is preferred wherever the receiving system supports it, because it carries track names and volume/automation data that OMF simply drops, forcing a receiving engineer to manually rebuild that information. OMF also caps out at 2GB, which can silently fail to export a long-form or high-sample-rate session. An OMF showing up today more often reflects an older system or exporting out of habit than a deliberate choice. File > Export Selected Tracks as AAF/OMF only exports tracks that are actively selected in the Edit window — a track left unselected is silently excluded, which is a common cause of an incomplete-seeming handoff.

## Publishing Options and the Reference Video

The Publishing Options dialog that appears after choosing AAF/OMF export is where the sequence gets named and annotated, and where 'Breakout to Mono' should be enabled if the destination expects individual mono channels rather than interleaved stereo clips. The interchange file by itself does not prove picture sync stayed intact — for any picture-locked handoff, a flat reference video (H.264 with timecode and clip-name burn-in is standard) travels alongside the AAF/OMF so the receiving mixer can visually confirm nothing drifted on import.

## Common mistakes

Exporting an AAF/OMF without checking which tracks are actually selected, silently dropping tracks the sender assumed were included. Choosing OMF by default instead of AAF and losing track names and automation data that then has to be manually rebuilt on the receiving end. Using Bounce to Disk one stem at a time when Track Bounce could have rendered the full stem set in a single pass. Sending an AAF/OMF for picture work with no reference video, leaving the receiving mixer with no way to confirm sync. Importing a received session with 'Link to Source Media' left on, leaving the new session dependent on file paths that may not exist on the receiving system.
