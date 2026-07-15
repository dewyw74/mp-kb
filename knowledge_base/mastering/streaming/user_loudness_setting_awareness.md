---
technique_name: Mastering With Awareness of User-Adjustable Loudness Settings
category: loudness
problem_solved: "Treating platform loudness normalization as a fixed, invisible background process ignores that listeners themselves can adjust or disable it (Spotify's Loud/Normal/Quiet modes, Apple Music's Sound Check toggle) — but this doesn't change the core mastering implication, since normalization (whatever level it lands on) only matches perceived level, it never restores dynamic range a limiter already removed, so a master's internal dynamics/limiting choices remain fully audible regardless of which loudness setting a given listener has selected"
parameters:
  spotify_user_settings: "Premium users can choose Loud, Normal (default, -14 LUFS), or Quiet reference levels; free users can only toggle the default Normal normalization on or off — in every case the underlying track's own dynamic content, not just its level, is unaffected by which setting is active"
  apple_music_user_setting: "Sound Check (targeting roughly -16 LUFS) can be toggled on or off per-device in system or app settings, and does not sync automatically across a listener's devices — a listener may be hearing a mastering-intended level on one device and a normalized level on another"
  normalization_is_gain_only: "Loudness normalization applies a static or slowly-varying gain offset to match a target level; it is not a dynamics processor and does not compress, expand, or otherwise reshape the waveform it's adjusting — whatever dynamic range and limiting character the mastering engineer built into the file survives the gain change untouched"
  practical_implication: "Because normalization only shifts level, two masters that reach the same listener loudness after normalization can sound completely different in dynamic character — one squashed flat by heavy limiting, one preserving wide contrast — and a listener will hear that difference regardless of whether their loudness setting happens to be Loud, Normal, Quiet, or normalization is off entirely"
signal_chain_position: "Final limiter/dynamics decisions at mastering, made on the understanding that the resulting dynamic character persists through any platform-side or user-side loudness adjustment downstream"
genre_applicability:
  - post_rock
  - ambient
  - pop
  - hip_hop
  - k_pop
related_techniques:
  - dynamic_range_as_expressive_device
  - platform_normalization_behavior
  - lufs_targets_by_genre
tags: ["user-settings", "sound-check", "loudness-normalization", "dynamics", "streaming"]
---

# Mastering With Awareness of User-Adjustable Loudness Settings

`platform_normalization_behavior.md` establishes that streaming platforms normalize playback to a target loudness and that chasing maximum loudness past that target is self-defeating. What that entry doesn't cover is that normalization itself is often user-adjustable rather than a single fixed background process — and, more importantly, that the specific loudness setting a listener has active doesn't change the core argument at all, because normalization only ever adjusts level, never dynamics.

## How Listeners Can Adjust Normalization Themselves

Spotify Premium users can choose among Loud, Normal (the -14 LUFS default), or Quiet reference levels, while free users only get an on/off toggle for the default Normal behavior. Apple Music's Sound Check (targeting roughly -16 LUFS) can be switched on or off per device in system or app settings, and critically does not sync automatically across a listener's devices — someone could be hearing an un-normalized, mastering-intended level on their laptop and a normalized level on their phone without changing any setting on either device intentionally. This means a mastering engineer cannot assume any single, universal normalized-listening condition for every listener; some fraction of any platform's audience is hearing a track closer to its raw, un-normalized level, and some fraction is hearing a track normalized to whatever level (potentially several different levels, depending on platform and setting) that listener has chosen or defaulted to.

## The Key Synthesis: Normalization Is a Level Match, Not a Dynamics Change

This is the practical point that makes user-setting variability less concerning than it might first appear. Loudness normalization applies a gain offset — turning a track up or down to hit a target level — and nothing more. It does not compress the file, expand it, or otherwise reshape its waveform. Whatever dynamic range, transient character, and limiting decisions a mastering engineer built into a file survive every normalization pass completely intact; only the overall level moves. This means the entire argument in `dynamic_range_as_expressive_device.md` about limiting decisions mattering — that a heavily brickwalled master destroys a genre's quiet-to-loud structural contrast while a lightly-limited one preserves it — remains true *after* normalization has been applied, regardless of which specific loudness setting (Loud, Normal, Quiet, Sound Check on or off) a given listener happens to have selected. The peak-loudness competition between tracks is what normalization neutralizes; the internal dynamic story a mastering engineer chose to tell is not touched by it at all.

## Why This Reinforces Rather Than Complicates the "Self-Defeating" Argument

`platform_normalization_behavior.md` frames chasing maximum loudness past a platform's target as self-defeating because "the platform turns it back down," leaving the track with less dynamic range and more audible limiting artifacts for a loudness gain the listener won't perceive once normalized. User-adjustable settings extend that argument rather than undermining it: no matter which of Spotify's Loud/Normal/Quiet settings, or Apple Music's Sound Check on/off state, a given listener has active, the loudness-war trade-off (spending dynamic range for a competitive edge normalization removes) still nets out the same way — a loss with no corresponding gain in nearly every listening scenario a track might actually be heard in. The one partial exception is a listener who has normalization fully disabled and is therefore hearing the track's true, un-normalized level; even then, however, the mastering engineer's actual dynamics and limiting decisions are exactly what that listener hears, undiluted, making those decisions arguably more consequential in that scenario rather than less.

## Genres Where This Synthesis Point Is Clearest

The genres that lean hardest into dynamic-range preservation are the clearest illustration that mastering choices persist post-normalization, because their whole mastering philosophy depends on that persistence being true. `post_rock.md`: "Post-rock masters generally sit quieter and more dynamic than most rock, around -14 to -10 LUFS integrated, because the genre's entire expressive power depends on the contrast between near-silent openings and overwhelming climaxes — any mastering stage that compresses that range away undermines the music's core mechanism." That contrast is exactly the kind of internal dynamic content that survives every normalization pass unchanged — a normalized post-rock track's quiet section is still genuinely quiet relative to its climax, at whatever absolute level normalization lands it at. `ambient.md` makes the same point even more directly against the loudness-war impulse specifically: "Ambient masters resist the loudness-war impulse entirely. Dynamic range is the point — a wide LUFS range (typically mastering to -18 to -14 LUFS integrated) preserves the quiet-to-loud breathing that gives the genre its sense of scale. Limiting is used sparingly, mostly to catch stray peaks from reverb tails rather than to raise perceived loudness." Both genres are, in effect, betting their mastering approach on the fact articulated above — that a listener's loudness setting changes level, not dynamic character — and that bet is correct precisely because of how normalization actually works.

Set against this, the streaming-competitive genres `platform_normalization_behavior.md` already documents — `pop.md`'s "-9 to -7 LUFS integrated for streaming-competitive masters," `hip_hop.md`'s "-9 to -7 LUFS integrated for streaming and club competitiveness," `k_pop.md`'s "-8 to -6 LUFS integrated, compressed for streaming and radio competitiveness while still preserving the genre's dramatic section-to-section contrast" — show the same principle from the other direction: these genres accept some dynamic-range cost for streaming competitiveness, but even they explicitly hedge by preserving *some* contrast (k_pop.md's own language), because that contrast, not the peak loudness these genres are nominally chasing, is what a normalized listener actually experiences as the track's dynamic character.

## Common Mistakes

**Assuming normalization "fixes" or compensates for a heavily over-limited master.** Normalization changes level only; a flat, brickwalled master arrives at a listener's ears still flat and brickwalled, just at a different absolute volume — normalization cannot restore contrast a limiter already removed.

**Optimizing a master for a single assumed loudness-setting scenario.** Because Sound Check doesn't sync across devices and Spotify offers multiple user-selectable reference levels, a meaningful fraction of listeners are not hearing the platform's default normalized level at all — mastering decisions should hold up across that variability, not just at one assumed setting.

**Concluding that because normalization exists, mastering-stage dynamics decisions matter less.** The opposite is closer to true: because normalization only ever equalizes peak-loudness competition and never touches internal dynamic character, the dynamics and limiting choices made at mastering are the primary thing that actually differentiates how a track is experienced once every track a listener hears has been leveled to roughly the same loudness.

## Cross-References

- `knowledge_base/mastering/streaming/platform_normalization_behavior.md` — the base streaming-normalization principle and "chasing loudness past the target is self-defeating" argument this entry extends to user-adjustable settings specifically
- `knowledge_base/mastering/dynamics/dynamic_range_as_expressive_device.md` — the underlying claim (limiting decisions structurally matter) that this entry shows survives normalization regardless of listener setting
- `knowledge_base/genres/rock/post_rock.md` and `knowledge_base/genres/electronic/ambient.md` — genres whose entire mastering philosophy depends on internal dynamic contrast surviving normalization untouched
- `knowledge_base/genres/pop/pop.md`, `knowledge_base/genres/hiphop/hip_hop.md`, `knowledge_base/genres/pop/k_pop.md` — streaming-competitive genres that still explicitly preserve some contrast, consistent with contrast (not peak loudness) being what a normalized listener actually hears
- `knowledge_base/mastering/loudness/lufs_targets_by_genre.md` — the genre-loudness spectrum this entry's user-setting analysis sits alongside
