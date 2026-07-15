---
workflow_name: "Ableton Project Templates and Track Bus Conventions"
daw: "ableton"
category: "templates"
goal: "Use Ableton's specific template mechanics — Save Live Set as Default Set, the User Library Templates folder, track color-coding, and group-track/freeze conventions — to build fast-starting, consistently organized Live Sets, separate from the genre-agnostic template philosophy already documented for the KB generally."
steps:
  - "Build a Set with the track grouping, return-track setup, and master-chain utilities a genre family actually needs, per the philosophy in `knowledge_base/production/templates/reusable_session_and_template_design.md`."
  - "Use File > Save Live Set as Default Set to make the current Set load automatically every time a new Set is created with Ctrl/Cmd+N."
  - "For more than one template, save additional Sets into the User Library's Templates folder (Documents/Ableton/User Library/Templates on Windows, Music/Ableton/User Library/Templates on Mac) so each appears under the Templates label in Live's Browser."
  - "Right-click any Set in the Templates Browser section and choose Set Default Live Set to promote a specific genre template to the one that loads on Ctrl/Cmd+N, without needing to re-run Save Live Set as Default Set."
  - "Apply a consistent track color-coding scheme across every template (for example, warm colors for drums/percussion, cool colors for harmony/pads, a distinct color for returns and the reference track) so the same visual language holds across every project."
  - "Group related tracks (drums, bass, harmony, lead/vocal, returns) into Group Tracks in the template, collapsed by default, so Arrangement and Session View stay readable as more tracks are added during writing."
  - "Leave CPU-heavy placeholder devices unfrozen in the template itself, since freezing is a per-project action that should happen once real content and settings exist, not baked into a blank starting point."
  - "Re-save the default or Templates-folder Set whenever the actual working routing or master-chain conventions change, so the template keeps matching current practice rather than drifting out of date."
related_plugins:
  - "Ableton Save Live Set as Default Set"
  - "Ableton Templates (User Library)"
  - "Ableton Group Track"
  - "Ableton Track Color"
  - "Ableton Freeze Track"
tags:
  - "ableton"
  - "templates"
  - "default-set"
  - "track-color"
  - "group-tracks"
  - "workflow"
  - "organization"
---

# Ableton Project Templates and Track Bus Conventions

`knowledge_base/production/templates/reusable_session_and_template_design.md` covers what belongs in a template and why — permanent infrastructure like grouping and routing versus creative decisions like tempo and patches that a template should leave open. This entry covers the Ableton-specific mechanics for actually building, saving, and maintaining that template inside Live: the Default Set system, the Templates folder, and the track-organization conventions (color, grouping, freeze state) that make a template Set fast to work from once it's open.

## Default Set vs. the Templates folder

Live has two related but distinct template mechanisms. File > Save Live Set as Default Set captures the current Set as the one that loads automatically whenever a new Set is created with Ctrl/Cmd+N or File > New Live Set — this is the right mechanism for a single, all-purpose starting point. For more than one template (per the genre-family template guidance in `knowledge_base/production/templates/reusable_session_and_template_design.md`), save each variant into the User Library's Templates folder instead: any Set placed there appears under the Templates label in Live's Browser, and opening one generates a new Untitled Set with that configuration rather than opening the template file itself. A Set inside the Templates folder can also be promoted to the actual Default Set by right-clicking it in the Browser and choosing Set Default Live Set, which is the fastest way to switch which genre template Ctrl/Cmd+N loads without re-running the Save Live Set as Default Set command from scratch.

## Track color-coding conventions

A consistent color scheme across every template turns track color into information instead of decoration: assigning drums/percussion one color family, harmony/pad instruments another, lead/vocal a third, and returns and the reference track their own distinct colors means a producer can read a Set's structure at a glance, in Session View, Arrangement View, and the mixer, without reading every track name. This matters more as a project's track count grows past what fits on one screen — color becomes the fastest way to locate the right track under time pressure.

## Group tracks and default collapse state

Group Tracks bundle related tracks (drums, bass, harmony, lead/vocal, returns) into one collapsible row, matching the grouping structure documented in `knowledge_base/daw/ableton/session_to_arrangement_workflow.md`. Building these groups into the template itself, collapsed by default, keeps Session View and Arrangement View compact and readable from the very first minute of a new project, rather than requiring the producer to build and collapse groups partway through every new Set.

## Freeze state in a template

A template should not ship with tracks pre-frozen, since Freeze Track (per `knowledge_base/daw/ableton/routing_resampling_and_freezing.md`) is meant to commit a specific, finished patch or performance to reduce CPU load — a template's placeholder devices haven't been performed or finalized yet, so there's nothing meaningful to freeze. Freeze conventions belong in the template only as a documented practice (freeze once CPU-heavy parts are stable), not as a pre-applied state on empty tracks.

## Common mistakes

Saving a template once and never updating it as routing, master-chain, or color conventions actually change in practice — per `knowledge_base/production/templates/reusable_session_and_template_design.md`, an unmaintained template drifts into stale scaffolding that gets bypassed. Using Save Live Set as Default Set for multiple genre variants, which only supports one Set at a time — use the Templates folder instead once there's more than one starting point to maintain. Pre-freezing placeholder tracks in a template, which locks in a CPU-saving state for devices that haven't even been configured for the actual project yet.
