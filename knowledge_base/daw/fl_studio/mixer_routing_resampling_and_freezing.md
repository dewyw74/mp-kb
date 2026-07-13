---
workflow_name: "FL Studio Mixer Routing, Resampling, and Freezing"
daw: "fl_studio"
category: "routing"
goal: "Route Channel Rack instruments into FL Studio's Mixer correctly, and use freezing, resampling, and rendering to manage CPU load and print processed audio without losing the ability to edit the underlying pattern."
steps:
  - "Route every Channel Rack instrument to its own Mixer insert track rather than leaving everything on Master."
  - "Group related inserts (drums, bass, chords) into a Mixer track group or send them to a shared bus insert for group processing."
  - "Use Sends for shared reverb/delay returns instead of duplicating the same effect on every insert."
  - "Freeze a CPU-heavy insert (right-click > Freeze) when working on a large session, and unfreeze before making further pattern or plugin edits."
  - "Use 'Render as audio clip' or the Edison plugin to print a channel or bus to audio when the part is finished being edited as MIDI."
  - "Route printed/frozen audio back onto its own Playlist track so the original pattern remains available if the print needs to be redone."
  - "Reserve resampling (bouncing a chain of effects onto a single audio channel) for sound-design passes that need to be locked in before further layering."
related_plugins:
  - "FL Studio Mixer"
  - "Edison"
  - "FL Studio Fruity Wrapper"
  - "Fruity Send"
tags:
  - "fl-studio"
  - "mixer"
  - "routing"
  - "freezing"
  - "resampling"
  - "rendering"
  - "workflow"
---

# FL Studio Mixer Routing, Resampling, and Freezing

FL Studio separates the Channel Rack (instruments and patterns) from the Mixer (signal routing and processing) more explicitly than some DAWs, which makes correct insert routing the foundation for everything downstream — sends, freezing, and rendering all depend on each instrument already sitting on its own Mixer track rather than dumping straight to Master.

## Goal

The goal mirrors `knowledge_base/daw/ableton/routing_resampling_and_freezing.md`: keep every element on a dedicated signal path so it can be processed, grouped, frozen, or printed independently, while preserving the option to go back and re-edit the source pattern or plugin chain if needed.

## 1. Route every instrument to its own insert

By default, new Channel Rack instruments can end up routed to Master. Assign each instrument (or closely related instrument, like a layered kick) to its own numbered Mixer insert immediately after creating it. This is the single most important habit for keeping a session mixable — grouping, freezing, and sends all assume this one-instrument-per-insert baseline.

## 2. Group and bus related inserts

Use Mixer track grouping (selecting multiple inserts and linking them) or route several inserts to a shared bus insert for elements that should be processed and level-controlled together — drum bus, bass bus, chord/pad bus. This keeps fader and effect-chain edits from having to be duplicated across every individual channel in a group.

## 3. Use sends instead of duplicating effects

Route reverb and delay through a dedicated Send track (Fruity Send) rather than instantiating the same reverb plugin on every insert that needs it. This keeps CPU load down and, more importantly, gives every sent element a shared, cohesive sense of space rather than several unrelated reverb tails.

## 4. Freeze CPU-heavy inserts

Right-click an insert and choose Freeze to render its current output to audio temporarily, unloading its plugins from CPU while the rest of the session keeps working. This is a reversible, editing-time optimization, not a final print — unfreezing restores full plugin access. Use it on synth-heavy or effect-heavy inserts once their sound is stable, and unfreeze before making further sound-design changes.

## 5. Render or resample for a final print

When a part is genuinely finished being edited as MIDI or as a live plugin chain, use 'Render as audio clip' (or manually resample through Edison) to print it to a static audio file. Unlike freezing, this is meant as a deliberate, semi-permanent commit — do it for elements that won't need further pattern-level editing, and always route the printed audio to its own Playlist track so the original pattern/instrument chain stays intact as a fallback.

## Common mistakes

Leaving multiple instruments routed to the same Mixer insert, which makes later grouping, freezing, or per-element automation impossible without re-routing everything first. Freezing an insert and then forgetting it's frozen, then wondering why plugin parameter changes aren't taking effect — always unfreeze before further sound-design work.

## Alternatives

For very small or CPU-light projects, skip freezing entirely and rely on FL Studio's native performance mode / low-latency monitoring instead. For sound-design-heavy work where a resampled texture will be chopped, reversed, or granularly processed afterward, resample early and treat the result as new raw material rather than waiting until mixdown.
