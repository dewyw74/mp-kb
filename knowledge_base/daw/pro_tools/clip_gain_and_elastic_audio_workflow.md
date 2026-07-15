---
workflow_name: "Pro Tools Clip Gain and Elastic Audio Workflow"
daw: "pro_tools"
category: "editing"
goal: "Use Pro Tools' pre-fader clip gain for level-riding at the clip level before any processing sees the signal, and use the correct Elastic Audio algorithm for time and pitch manipulation depending on the source material."
steps:
  - "Level individual clips with Clip Gain before adding any insert processing, since clip gain is applied pre-insert and pre-fader — closer to trimming a source recording than to riding a fader downstream of it."
  - "Use the Clip Gain Line (breakpoint editing directly on the clip, similar to drawing volume automation) for detailed within-clip rides, and the Clip Gain value/knob for a fast overall level trim on a whole clip."
  - "Reach for clip gain instead of track volume automation whenever the goal is consistent input level into a compressor or other dynamics processor, since clip gain changes what the plugin actually sees rather than just changing output level after the fact."
  - "Remember that clip gain settings are stored per clip and per playlist, so each Playlist on a track can carry its own independent clip gain pass, unlike track volume automation which is shared across all playlists on that track."
  - "Enable Elastic Audio on a track (or apply it per-clip) only when time or pitch manipulation is actually needed, since it adds processing overhead and, for some algorithms, audible character to the signal."
  - "Choose Polyphonic for complex mixed or layered material (full mixes, stereo group stems, chords) where no single algorithm is tuned to the specific source."
  - "Choose Rhythmic for percussive, transient-heavy material (drums, loops) where preserving transient integrity under time-stretching matters more than pitch accuracy."
  - "Choose Monophonic for single-note-at-a-time sources (lead vocal, bass, solo instrument) to get the cleanest pitch-shifting and time-stretching with the fewest artifacts."
  - "Choose Varispeed when pitch should move together with tempo, the way a physical tape or turntable speed change would behave, rather than independently."
  - "Reserve X-Form for final, high-stakes time/pitch moves where the highest fidelity matters more than real-time preview, since X-Form is an offline, rendered algorithm rather than a real-time one."
related_plugins:
  - "Pro Tools Clip Gain"
  - "Pro Tools Elastic Audio (Polyphonic)"
  - "Pro Tools Elastic Audio (Rhythmic)"
  - "Pro Tools Elastic Audio (Monophonic)"
  - "Pro Tools Elastic Audio (Varispeed)"
  - "Pro Tools Elastic Audio (X-Form)"
  - "Celemony Melodyne"
tags:
  - "pro-tools"
  - "clip-gain"
  - "elastic-audio"
  - "editing"
  - "time-stretching"
  - "pitch-shifting"
  - "gain-riding"
---

# Pro Tools Clip Gain and Elastic Audio Workflow

Clip gain and Elastic Audio solve two different problems that are easy to conflate with track-level tools: clip gain is a pre-fader, clip-level way to ride level before anything else touches the signal, and Elastic Audio is Pro Tools' family of time-and-pitch manipulation algorithms, each tuned to a different kind of source material. Both operate at the clip rather than the track level, which is what makes them distinct from the track volume automation and tempo-track tools covered elsewhere in the DAW knowledge base.

## Clip Gain vs. Track Volume Automation

The defining difference is signal-flow position: clip gain is applied pre-insert and pre-fader, much like trimming the gain knob on an analog preamp before the signal reaches any processing, while track volume automation is post-insert and post-fader, changing the level of a signal that has already been shaped by EQ, compression, or other inserts. This matters most wherever a compressor or other level-dependent processor sits on the track's inserts: using clip gain to even out a vocal or dialogue track before it hits the compressor gives that compressor a consistent input level to react to, producing more even gain-reduction behavior than compensating for the same unevenness with post-fader automation ever could. Clip gain settings also live with the clip and the playlist rather than the track as a whole, so different Playlists on the same track (see `knowledge_base/daw/pro_tools/playlist_based_comping_workflow.md`) can carry entirely independent clip gain passes, while track volume automation is shared across every playlist on that track.

## Clip Gain Line and Quick Trims

Two levels of clip gain control cover most riding tasks. The Clip Gain Line lets breakpoints be drawn directly on the waveform, functioning much like a miniature automation lane scoped to a single clip — useful for smoothing an uneven vocal phrase or taming one hot syllable without touching anything outside that clip's boundaries. For simpler needs, a whole clip's gain can be trimmed as a single value, which is the faster move when an entire take or comped section just needs to sit a few dB higher or lower relative to its neighbors before further processing.

## The Five Elastic Audio Algorithms

Elastic Audio offers five distinct algorithms, and picking the right one for the source material is the difference between transparent results and audible artifacts:

- **Polyphonic** — general-purpose, tuned for complex or layered material such as full mixes, stereo stems, or chordal parts; a reasonable balance of quality and speed when nothing more specialized fits.
- **Rhythmic** — tuned for percussive, transient-driven material (drums, loops); prioritizes preserving transient sharpness under time-stretching over pitch accuracy.
- **Monophonic** — tuned for single-note-at-a-time sources (lead vocal, bass, solo instrument); gives the cleanest pitch-shift and time-stretch results specifically because the algorithm can assume one pitch is sounding at a time.
- **Varispeed** — links pitch and tempo together the way a physical tape or turntable speed change would, for when that coupled behavior is the intended effect rather than something to be avoided.
- **X-Form** — the highest-fidelity option, but offline/rendered rather than real-time; it requires the audio to be processed before playback, so it's the right choice for a final, committed move rather than for auditioning options quickly.

## Common mistakes

Riding level with track volume automation when the real goal is even compressor input — this leaves the compressor reacting to the original uneven level and produces inconsistent gain reduction across the phrase, which clip gain applied first would have avoided entirely. Leaving Elastic Audio set to Polyphonic out of habit on a solo vocal or bass part, where Monophonic would produce noticeably cleaner pitch and time results. Using Rhythmic on a melodic, pitched part or Monophonic on a full drum loop — matching the algorithm to the wrong kind of source is the most common cause of audible Elastic Audio artifacts. Committing to X-Form for quick auditioning passes, where the rendering step slows down experimentation compared to a real-time algorithm, and saving X-Form only for the final pass once the edit is locked.
