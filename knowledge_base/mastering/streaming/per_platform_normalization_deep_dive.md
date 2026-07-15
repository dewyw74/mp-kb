---
technique_name: Per-Platform Loudness Normalization Deep Dive
category: loudness
problem_solved: "Treating 'streaming normalization' as one uniform -14 LUFS rule produces a mismatched master — Spotify, Apple Music, YouTube, and Tidal each implement distinct targets, distinct turn-up-vs-turn-down-only behavior, and distinct user-adjustable ranges, so a master optimized for one platform's specifics can arrive quieter, louder, or less true-peak-safe than intended on another"
parameters:
  spotify_target: "-14 LUFS integrated (default 'Normal' setting), turn-down-only from a louder master but Spotify's own documentation and community testing show a small amount of upward gain is possible for quieter masters within headroom limits; Premium users can additionally select Loud or Quiet, and free users can only toggle Normal on/off"
  apple_music_target: "Approximately -16 LUFS via Sound Check — a full 2 LUFS quieter than the Spotify/YouTube/Tidal convention; behaves as a ceiling rather than a two-way match, since tracks quieter than -16 LUFS are not boosted, only louder tracks are turned down"
  youtube_target: "-14 LUFS integrated with a -1dBTP true-peak target on the video platform; YouTube Music's own in-app normalization is documented as only reducing loudness above roughly -7 LUFS, a much looser ceiling than -14"
  tidal_target: "-14 LUFS integrated with a -1dBTP true-peak target, applied per-album so gain compensation stays consistent across a release rather than per-track"
  practical_delivery_target: "Mastering to approximately -14 LUFS integrated with true peak at or below -1dBTP satisfies Spotify, YouTube, and Tidal without leaving perceptible loudness on the table on any of the three; Apple Music's quieter -16 LUFS ceiling means a -14 LUFS master still gets turned down slightly there, which is expected and not a defect"
signal_chain_position: "Final limiter/true-peak stage, chosen with the specific destination platform(s) in mind rather than a single generic 'streaming' assumption"
genre_applicability:
  - pop
  - hip_hop
  - k_pop
  - teen_pop
  - tropical_house
  - west_coast_hip_hop
  - east_coast_hip_hop
related_techniques:
  - platform_normalization_behavior
  - lufs_targets_by_genre
  - dynamic_range_as_expressive_device
tags: ["streaming", "normalization", "lufs", "spotify", "apple-music", "youtube", "tidal", "platform-delivery"]
---

# Per-Platform Loudness Normalization Deep Dive

`platform_normalization_behavior.md` establishes the general principle that streaming platforms normalize playback to a target loudness, making a purely-maximum-loudness mastering strategy self-defeating. That entry treats "roughly -14 LUFS" as a single representative number. In practice the major platforms don't share one implementation — they differ in target level, in whether normalization only turns tracks down or can also turn them up, and in how much control they hand the listener. This entry goes platform-by-platform.

## Spotify: -14 LUFS, Mostly Turn-Down, User-Adjustable

Spotify's default "Normal" playback setting normalizes to -14 LUFS integrated. Premium users can additionally choose Loud or Quiet reference levels, while free users can only toggle Spotify's normalization on or off rather than choosing among levels. Spotify also normalizes at the album level rather than the individual track, so gain compensation stays consistent across an album's sequencing instead of jumping between tracks. A master delivered significantly louder than -14 LUFS gets turned down on playback with no perceptual benefit — the exact "self-defeating" scenario `platform_normalization_behavior.md` describes — while a quieter, more dynamic master closer to -14 LUFS reaches the listener with more of its original dynamic range intact.

## Apple Music: -16 LUFS via Sound Check, a Ceiling Rather Than a Match

Apple Music's Sound Check feature targets a noticeably quieter reference point, roughly -16 LUFS integrated — about 2 LUFS below the Spotify/YouTube/Tidal convention. Sound Check's behavior is asymmetric: it reduces the level of tracks louder than its target, but does not boost tracks that are already quieter than -16 LUFS. That makes Apple's normalization function more like a loudness ceiling than a two-way loudness match, and it means a master built to exactly hit Spotify's -14 LUFS target will still be turned down somewhat under Apple's Sound Check — expected behavior, not something to chase closer with extra loudness, since going louder just increases how much Apple turns the track back down.

## YouTube: -14 LUFS on Video, a Much Looser Ceiling on YouTube Music

The YouTube video platform targets -14 LUFS integrated with a -1dBTP true-peak ceiling, matching the Spotify/Tidal convention closely. YouTube Music, however, is documented as only reducing loudness once a track exceeds roughly -7 LUFS — a far looser ceiling than -14 LUFS. This is a meaningful distinction for genres delivered primarily through YouTube Music rather than the general video platform: a master mastered hot enough to sit near a genre's loudest documented tier (see `lufs_targets_by_genre.md`'s loudest tier, e.g. speedcore's -6 to -4 LUFS or hardstyle's -6 to -5 LUFS) may not get turned down by YouTube Music at all, unlike on Spotify, Apple Music, or Tidal.

## Tidal: -14 LUFS, Album-Based, True-Peak Aware

Tidal's documented loudness target is -14 LUFS integrated with a -1dBTP true-peak target, and like Spotify, Tidal applies normalization at the album level so a release's internal sequencing and relative loudness between tracks is preserved rather than flattened track-by-track. Tidal's normalization is also turn-down-only in practice — it does not raise the level of a track that already sits below -14 LUFS.

## Why Genres With a Documented Streaming Target Care About This Distinction

Several genre files in this knowledge base tie their loudness target explicitly to competing on streaming platforms, and re-reading their mastering sections directly (rather than through `platform_normalization_behavior.md`'s existing citations) shows how tightly the -9 to -6 LUFS range clusters around the Spotify/YouTube/Tidal -14 LUFS convention specifically, not Apple's quieter -16 LUFS ceiling. `pop.md`: "Pop masters typically target -9 to -7 LUFS integrated, prioritizing loudness competitiveness on streaming platforms while still preserving enough dynamic contrast between verse and chorus to keep the arrangement's lift audible." `hip_hop.md`: "Masters typically target -9 to -7 LUFS integrated for streaming and club competitiveness, balancing a bright, vocal-forward top end against a deep, controlled low end designed to translate across club systems and headphones alike." `k_pop.md` runs louder still: "Masters typically target -8 to -6 LUFS integrated, compressed for streaming and radio competitiveness while still preserving the genre's dramatic section-to-section contrast." `teen_pop.md` frames the same choice around radio as much as streaming: "Masters run loud (-8 to -6 LUFS integrated) for radio and streaming competitiveness, while still preserving the energy jump from verse to chorus that the entire arrangement is built to deliver." All four of these targets sit meaningfully above every platform's actual normalization point — the loudness headroom isn't wasted, though, because on Apple Music's quieter -16 LUFS ceiling these masters get turned down further than they would on Spotify, which is a real practical difference between destinations that a single "-14 LUFS" mental model obscures.

`tropical_house.md` shows the deliberate opposite choice: "Masters sit around -10 to -8 LUFS integrated, more dynamic than club-focused EDM subgenres, reflecting the genre's radio and streaming-oriented listening context rather than club-system playback" — a target already close enough to the Spotify/YouTube/Tidal -14 LUFS convention that normalization turn-down is minimal, preserving more of the master's own dynamic range on arrival.

`west_coast_hip_hop.md` and `east_coast_hip_hop.md` both document the same era-driven loudness shift, worth re-quoting directly here since it's central to why "streaming-competitive" is a moving target rather than a fixed number: "Classic-style masters run at a moderate -11 to -9 LUFS integrated, while modern West Coast-influenced production trends closer to -9 to -7 LUFS for streaming competitiveness, generally preserving the region's warm, full, groove-focused frequency character" (West Coast), and the near-identical "Classic-style masters run at a moderate -11 to -9 LUFS integrated, while modern East Coast-influenced production trends closer to -9 to -7 LUFS for streaming competitiveness, generally preserving a warm, slightly darker frequency character relative to more polished mainstream pop-rap production" (East Coast). Both regional traditions moved their conventional target louder specifically in response to the platform landscape — which is itself a reason to treat any platform's current normalization number as subject to change rather than permanent.

## Common Mistakes

**Assuming one "-14 LUFS" number covers every major platform.** Apple Music's Sound Check target sits roughly 2 LUFS quieter than Spotify, YouTube, and Tidal's shared convention — a master that arrives correctly on three platforms still gets turned down further specifically on Apple Music, which is expected rather than a mastering failure.

**Not distinguishing YouTube's video platform from YouTube Music.** The video platform's -14 LUFS/-1dBTP target and YouTube Music's much looser roughly -7 LUFS ceiling are different systems; a master built assuming the stricter video-platform number will simply not be turned down at all on YouTube Music if it's delivered louder than -7 LUFS.

**Chasing loudness past a platform's ceiling in the belief that it helps competitiveness there.** As `platform_normalization_behavior.md` already establishes, exceeding a platform's target only spends dynamic range and headroom for a loudness gain the platform's normalization then removes — true independently on Spotify, Apple Music, YouTube, and Tidal, even though their specific numbers differ.

## Cross-References

- `knowledge_base/mastering/streaming/platform_normalization_behavior.md` — the general streaming-normalization principle and the "chasing maximum loudness is self-defeating" argument this entry differentiates and extends per-platform
- `knowledge_base/genres/pop/pop.md`, `knowledge_base/genres/hiphop/hip_hop.md`, `knowledge_base/genres/pop/k_pop.md`, `knowledge_base/genres/pop/teen_pop.md` — streaming-competitive loudness targets clustered around the Spotify/YouTube/Tidal -14 LUFS convention
- `knowledge_base/genres/edm/tropical_house.md` — a genre mastered close enough to the -14 LUFS convention that normalization turn-down is minimal by design
- `knowledge_base/genres/hiphop/west_coast_hip_hop.md` and `knowledge_base/genres/hiphop/east_coast_hip_hop.md` — the documented historical loudness-target shift toward streaming competitiveness
- `knowledge_base/mastering/loudness/lufs_targets_by_genre.md` — the full genre-loudness spectrum this entry's platform-specific targets sit alongside
- `knowledge_base/mastering/dynamics/dynamic_range_as_expressive_device.md` — why mastering louder than a platform's actual normalization point produces no perceptual gain
