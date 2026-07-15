---
workflow_name: "Pro Tools Session Setup and Routing Workflow"
daw: "pro_tools"
category: "routing"
goal: "Build a Pro Tools session's I/O, bus, and Aux-track structure correctly from the start, and choose the right grouping mechanism — Mix Groups, VCA Master tracks, or Routing Folder Tracks — for large-scale mix management instead of defaulting to a single Ableton/FL-style group-track model."
steps:
  - "Open the I/O Setup window before recording begins and label input, output, and bus paths with meaningful names (Kick, OH L/R, Drum Bus, Reverb Send) rather than leaving default Avid-numbered paths."
  - "Create internal buses in I/O Setup for every submix and effects-return path the session will need, since a bus in Pro Tools is a routing path, not a track."
  - "Create an Aux track for each submix or effects return, and set its input to the matching bus so it becomes the audible destination for everything routed to that bus."
  - "Route instrument and audio tracks' outputs to the appropriate submix bus (drums, bass, music, vocals) rather than sending every track directly to the Master fader."
  - "Decide per mix task whether a Mix Group (linked fader/mute/solo control, no audio path), a VCA Master track (linked gain control with no audio passing through it), or a Routing Folder Track (organizational folder plus its own Aux-style I/O and inserts) is the right tool, since Pro Tools treats these as three distinct mechanisms rather than one group-track type."
  - "Build VCA Master tracks over an existing Mix Group when the goal is riding the combined level of many tracks — drums, a stem, a whole orchestral section — while preserving every member track's own automation and relative balance underneath."
  - "Use VCA Spill to temporarily reveal only the member tracks under a VCA fader when detailed work on individual members is needed, then collapse back to the VCA view."
  - "Reserve Routing Folder Tracks for cases that need both organizational collapsing and shared insert processing (a shared bus compressor or EQ) on the folder's own signal path, since a VCA has no insert points and cannot process audio."
  - "Route all submix Aux tracks to the Master fader last, and confirm the Master fader's output path matches the session's actual monitoring and print path before any mix pass begins."
  - "Save the finished I/O map, bus layout, and group/VCA structure as a session template once it works, so future sessions of the same type start from a validated routing setup."
related_plugins:
  - "Pro Tools I/O Setup"
  - "Pro Tools Aux Track"
  - "Pro Tools VCA Master Track"
  - "Pro Tools Mix Group"
  - "Pro Tools Routing Folder Track"
  - "Avid Channel Strip"
tags:
  - "pro-tools"
  - "routing"
  - "vca"
  - "aux-tracks"
  - "mix-groups"
  - "session-setup"
  - "bus-structure"
---

# Pro Tools Session Setup and Routing Workflow

Pro Tools separates concerns that Ableton and FL Studio combine into a single Group Track: routing audio through a submix, linking fader/mute/solo control across tracks, riding combined gain without touching an audio path, and organizing tracks visually in the track list are four distinct mechanisms in Pro Tools rather than one. Getting a session's I/O, bus, and grouping structure right at setup time — before tracking or mixing begins — avoids a rebuild later and is the foundation every other Pro Tools workflow in this knowledge base assumes is already in place.

## I/O Setup and Buses

The I/O Setup window is Pro Tools' virtual patch bay: it is where physical inputs/outputs and internal bus paths get labeled and mapped before they're usable on a track. A bus in Pro Tools is a routing path, not a track — it carries signal internally the way a physical cable would, but it has no fader, no meter, and no way to hear it directly. To make a bus audible or processable, an Aux track has to be created with its input set to that bus; the Aux track is the destination that actually receives, displays, and can process what the bus carries. Labeling buses clearly at the I/O Setup stage (Drum Bus, Vox Reverb Send, Print Bus) pays off constantly during mixing, since every send and output selector in the session pulls its names from this window.

## Aux Tracks as Submixes

Route drums, bass, music, and vocal tracks to their own submix bus, each received by a dedicated Aux track, rather than sending every track straight to Master. This mirrors the functional group-bus structure documented in `knowledge_base/daw/ableton/mixing_bus_routing_and_gain_staging_workflow.md`, but the mechanism is different: in Ableton a Group Track is simultaneously the routing destination, the shared processing point, and the fader-link point. In Pro Tools those jobs live on separate track types, so an Aux track's job is specifically to be a submix's audible destination and processing point — it is not, by itself, a grouping or gain-riding mechanism.

## Mix Groups vs. VCA Master Tracks

A Mix Group links selected tracks' faders, mutes, and solos so that moving one moves all of them proportionally — no audio passes through a Mix Group, it is purely a control link. A VCA Master track is best understood as a master fader for an existing Mix Group: it adds one more fader that scales every member track's own fader by the same amount, while each member's individual automation underneath stays fully intact and editable. Because a VCA carries no audio, it has no inserts and cannot apply shared EQ or compression to the group — for that, route the members to a shared Aux/submix bus instead, or use a Routing Folder Track. VCA Spill temporarily shows only the tracks assigned to a given VCA so they can be worked on individually without hunting through the full track list, then folds back into the VCA view when detailed work is done.

## Routing Folder Tracks

A Basic Folder Track is purely organizational — it has no signal path of its own and only affects how tracks are displayed and collapsed in the Edit and Mix windows. A Routing Folder Track combines that same organizational folding with an Aux track's I/O, inserts, and sends, so it can both collapse a set of tracks out of view and act as their shared submix destination with its own processing. Choose a Routing Folder Track over a VCA specifically when the group needs shared inserted processing (a bus compressor gluing a drum group, a shared reverb send point) in addition to linked level control; choose a VCA when the goal is pure, transparent gain riding across many tracks — especially tracks routed to different outputs, since VCAs (unlike Aux-based submixes) can group tracks regardless of where their audio is actually routed.

## Common mistakes

Treating a VCA Master track as if it were a group bus and expecting to insert an EQ or compressor on it — VCAs carry no audio and cannot host processing; the plugin has to go on a Mix Group's member tracks, a Routing Folder Track, or a shared Aux submix instead. Routing every track directly to Master and skipping submix Aux tracks entirely, which removes the ability to process or level-check a functional group (drums, vocals) before it reaches the master bus. Leaving I/O Setup paths unlabeled, which makes every send and output menu in a larger session much harder to navigate correctly under time pressure. Building a VCA without an underlying Mix Group, which works for level but loses the option to move mute/solo state together with the fader.
