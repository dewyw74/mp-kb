---
workflow_name: "Studio One Song Setup and Console Routing"
daw: "studio_one"
category: "routing"
goal: "Set up a new Studio One Song with correct Bus Channel and FX Channel routing, using Studio One's drag-and-drop workflow instead of menu-driven insertion to build a fast, uncluttered mixing structure in the Console."
steps:
  - "Create the Song and set sample rate/bit depth before importing audio, since Studio One does not resample on the fly during recording."
  - "Open the Console (F3) alongside the Arrange view rather than treating mixing as a separate later phase."
  - "Build group Bus Channels (drums, bass, vocals, music) by dragging tracks onto the Console's channel list or using Add Bus, then route source channels' outputs to the matching bus."
  - "Drag an effect or FX Chain directly from the Effects browser onto a channel's Insert slot to load it, instead of opening an insert menu and selecting from a list."
  - "Drag an effect from the browser onto a channel's Send slot to auto-create a new FX Channel of the same name, instantiate the effect on it, and wire up the send in one motion."
  - "Drag an existing Bus or FX Channel onto a track's Send slot to route to that channel instead of creating a duplicate."
  - "Drag the Inserts header (not an individual plugin) from one channel to another to copy the whole effects chain at once."
  - "Route each Bus Channel to Main, and confirm the Main output channel is the final stage before any mastering-style processing."
  - "Use Folder Tracks as effects-drop targets when a Bus selection is active, so dragging effects onto the folder loads them onto the associated Bus Channel."
  - "Save a Song as a template once the bus structure is finalized, so future Songs start with the same routing without rebuilding it by hand."
related_plugins:
  - "Studio One Console"
  - "Studio One Channel Strip"
  - "Studio One Console Shaper / CTC-1 Pro Console Shaper (Mix Engine FX)"
  - "PreSonus Fat Channel XT"
tags:
  - "studio_one"
  - "console"
  - "routing"
  - "bus-channel"
  - "fx-channel"
  - "drag-and-drop"
  - "mixing"
---

# Studio One Song Setup and Console Routing

Studio One's mixer is called the Console, and the fastest way to build routing inside it is not through insert menus but through drag-and-drop: dragging effects, instruments, files, and even whole channels directly onto their destination. This is a genuine, long-documented PreSonus design philosophy — Studio One's own manual and support documentation describe creating sends, building effects chains, and instantiating buses primarily as drag targets rather than dialog-driven choices. Setting a Song up with clean Bus Channel and FX Channel routing from the start, using this drag-and-drop workflow, keeps the Console readable as track count grows.

## The Console and channel types

The Console (opened with F3) holds four channel types: Audio and Instrument channels for sources, Bus Channels for grouping, and FX Channels for return-style processing. In modern Studio One versions Bus and FX Channels are functionally close — the practical differences are that FX Channels are solo-safe by default and are filtered separately in the channel list — but keeping the naming distinction (buses for grouping, FX channels for sends like reverb and delay) keeps a session's routing legible at a glance.

## Drag-and-drop as the core interaction model

Dragging is not a shortcut layered on top of a menu system in Studio One — it is the primary way routing gets built:

- Dragging an effect or FX Chain from the browser onto a channel's Insert section loads it there directly.
- Dragging an effect onto a channel's Send slot auto-creates a new FX Channel named after the effect, instantiates it, and creates the send — one drag replaces three separate manual steps.
- Dragging an existing Bus, FX Channel, Audio, or Instrument channel onto a Send slot routes to that existing channel instead of spawning a new one.
- Dragging the Inserts header (rather than a single plugin) copies an entire effects chain from one channel to another.
- Dragging effects onto a Folder Track routes them onto that folder's associated Bus Channel when a bus selection is active.

This matters for song setup specifically because a new Song's bus structure — drum bus, vocal bus, music bus, parallel-compression sends, reverb/delay returns — can be built in the time it takes to drag a handful of objects into place, rather than repeatedly opening insert-selection dialogs.

## Building the bus structure

A typical Song setup groups tracks into a small number of Bus Channels (drums, bass, vocals, other instruments) and routes each bus to Main. Bus Channels are useful for group dynamics processing and group fader control; FX Channels are the natural home for shared time-based effects (reverb, delay) fed by sends from multiple sources, keeping the CPU cost of a single reverb instance shared across many tracks instead of duplicated per-channel.

## Mix Engine FX for full-console character

Console Shaper and the newer CTC-1 Pro Console Shaper are Studio One-specific "Mix Engine FX" — a plugin category unique to Studio One that processes every channel routed through a bus or the Main output independently at the audio-engine level from a single plugin instance, rather than as one instance per channel. Loaded on a Bus Channel or Main, they emulate analog console behavior (input drive, channel noise, crosstalk) across the whole signal path. This is a routing-adjacent feature worth knowing during song setup because it changes where console character gets added: at the bus/Main stage, not per-channel inserts.

## Common mistakes

Building routing entirely through right-click/insert menus and ignoring drag-and-drop is the most common way to slow down Console setup in Studio One — the drag workflow exists specifically to collapse multi-step routing tasks into one action. A second mistake is creating a new FX Channel by dragging an effect onto a Send slot repeatedly for similar sends, which produces duplicate reverb/delay instances instead of dragging the already-created FX Channel onto subsequent tracks' Send slots. A third is confusing Bus Channels and FX Channels functionally — while they behave similarly in current versions, using FX Channels for group dynamics processing works against their solo-safe default and separate filtering, and defeats the organizational point of having two channel types.
