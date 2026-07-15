---
workflow_name: "FL Studio Mastering Export Prep for Vinyl"
daw: "fl_studio"
category: "mastering"
goal: "Take a completed general master-bus chain and prepare a separate, vinyl-specific export in FL Studio — summing bass to mono below roughly 150-250Hz, restraining harsh high-frequency content, leaving extra dynamic-range headroom, and exporting at settings appropriate for a vinyl-cutting engineer handoff — rather than sending a standard streaming master to the lathe unchanged."
steps:
  - "Start from a completed general master-bus chain per `knowledge_base/daw/fl_studio/master_bus_chain_and_export_workflow.md`, then branch a separate vinyl-specific signal path rather than modifying the streaming master in place."
  - "Insert Fruity Stereo Shaper (or Maximus, using its low-band mono merge) after the existing EQ/dynamics stages, switch on its Bands display, and set the Low Band frequency cutoff to roughly 150-250Hz."
  - "Collapse that low band's stereo width to mono, leaving stereo information intact above the cutoff frequency, since wide stereo bass is what causes a cutting stylus to over-excurse or a playback stylus to mistrack."
  - "Confirm the mono-summed low end still sounds full and doesn't phase-cancel by checking the vinyl-chain bounce in mono via a utility mono button, per `knowledge_base/mastering/stereo/final_mono_and_translation_check.md`."
  - "Identify and restrain harsh or sibilant high-frequency content (roughly 5-10kHz and up) with light de-essing or a gentle high-shelf pull-back, since hot, unrestrained top end risks cutting-stage distortion and playback mistracking, especially toward a record's inner grooves."
  - "Back off the limiter's gain-reduction depth from the streaming master's setting, deliberately leaving more visible headroom and dynamic range than a loudness-competitive streaming master would carry."
  - "Re-check the resulting loudness against `knowledge_base/mastering/streaming/mastering_for_vinyl_vs_digital.md`'s vinyl-vs-streaming contrast rather than the streaming targets in `knowledge_base/mastering/loudness/lufs_targets_by_genre.md` — a vinyl pre-master intentionally runs quieter and more dynamic."
  - "Export via File > Export > Wave file at 24-bit and the project's working sample rate, leaving dithering off since the cutting engineer performs their own final conversion."
  - "Label and deliver the vinyl pre-master separately from the streaming master, and confirm target side length and running order with the cutting engineer before finalizing, since side length directly limits achievable loudness and bass level."
related_plugins:
  - "FL Studio Mixer"
  - "Fruity Stereo Shaper"
  - "Maximus"
  - "youlean_loudness_meter_2"
  - "voxengo_span"
tags:
  - "fl-studio"
  - "mastering"
  - "vinyl"
  - "mono-bass"
  - "export"
  - "workflow"
---

# FL Studio Mastering Export Prep for Vinyl

`knowledge_base/daw/fl_studio/master_bus_chain_and_export_workflow.md` covers building a general EQ/dynamics/limiter master-bus chain and exporting it for streaming or digital delivery. This entry picks up after that chain already exists and covers what changes specifically for a vinyl-cutting handoff: mono-summed bass, high-frequency restraint, extra dynamic headroom, and export settings suited to a cutting engineer rather than a streaming platform. None of the general master-bus chain content is repeated here — the assumption is a working streaming-oriented master already exists, and this workflow branches a separate, vinyl-specific version of it.

## Why vinyl needs a separate export, not a reused one

A vinyl cutting lathe is a physical, mechanical process rather than a digital normalization algorithm, and its constraints don't map onto streaming-mastering decisions at all. `knowledge_base/mastering/streaming/mastering_for_vinyl_vs_digital.md` lays out the core contrast: streaming mastering answers to a platform's loudness-normalization target, while vinyl mastering answers to a cutting stylus's physical tracking limits. A hot, hard-limited, wide-stereo-bass streaming master is exactly the combination of properties that causes problems on a lathe, which is why this workflow branches a separate signal path rather than reusing the streaming chain's output directly.

## Mono-summing the bass

Set Fruity Stereo Shaper's Low Band frequency cutoff to roughly 150-250Hz (the range documented in `knowledge_base/mastering/format/vinyl_mastering_considerations.md` and confirmed by current vinyl-mastering references) and collapse that band's stereo width to mono, leaving everything above the cutoff untouched. Maximus works as an alternative if a multiband tool is already in the chain, since its low-band handling can also be merged to mono. Wide, out-of-phase stereo bass forces the cutting head into excessive lateral excursion and, in the worst case, can cause the playback stylus to skip or jump a groove — this is a hard mechanical constraint, not a stylistic preference, and it applies regardless of how well the same wide-stereo low end translates on streaming playback systems. After summing, check the result in mono via a utility mono button to confirm the low end still sounds full rather than thinning out from unexpected cancellation.

## Restraining harsh high-frequency content

Dense or sibilant high-frequency content — roughly 5-10kHz and up — is a known source of cutting-stage distortion and playback mistracking, and the risk is worst toward a record's inner grooves, where groove speed (and therefore high-frequency tracking accuracy) is lowest. A light touch of de-essing on vocal-heavy masters, or a gentle high-shelf pull-back on the vinyl chain specifically, reduces this risk without needing to dull the track's overall brightness on the streaming version. This is a vinyl-only adjustment — the streaming master's top end doesn't need to change at all.

## Leaving more dynamic range than a streaming master

Back the limiter's gain-reduction depth off from whatever the streaming master used, deliberately leaving more headroom and a wider dynamic range on the vinyl chain. `knowledge_base/mastering/streaming/mastering_for_vinyl_vs_digital.md` notes that vinyl "generally tolerates and rewards wider dynamic range than a hot streaming master," partly because heavily-limited, near-zero-headroom masters translate poorly to a lathe's cutting and tracking constraints in the first place. Judge the result against that vinyl-vs-streaming contrast rather than against `knowledge_base/mastering/loudness/lufs_targets_by_genre.md`'s streaming-oriented numbers — hitting a streaming LUFS target on the vinyl chain defeats the purpose of building a separate export.

## Export settings for the cutting-engineer handoff

Export via File > Export > Wave file at 24-bit and the project's working sample rate rather than downsampling to a final 16-bit/44.1kHz consumer file — the cutting engineer needs headroom for their own processing and will handle any final format conversion on their end. Leave dithering off for the same reason: dithering belongs on the final bit-depth-reduction step, and that step happens at the cutting facility, not in this export.

## Side length and running order

Because a vinyl side has a fixed physical groove area, program length directly trades off against achievable loudness and bass level — a longer side forces a quieter, less bass-extended cut. Confirm target side length and running order with the cutting engineer before finalizing gain-reduction depth on the vinyl chain, per the side-length/loudness tradeoff in `knowledge_base/mastering/format/vinyl_mastering_considerations.md`; a mastering level appropriate for a short single is not automatically appropriate for a full album side.

## Common mistakes

Sending the streaming master directly to a cutting engineer unchanged, carrying wide stereo bass and near-zero headroom that are exactly the properties vinyl's physical constraints push against. Mono-summing the entire mix instead of just the low band, which discards stereo width the format can actually support above the bass-summing cutoff. Chasing the same LUFS target used for the streaming master on the vinyl chain, which fights against the extra headroom vinyl needs rather than serving it. Finalizing the vinyl chain's loudness before confirming side length with the cutting engineer, risking a mismatch between the mastering level chosen and what the actual side can physically accommodate.

## Cross-references

- `knowledge_base/daw/fl_studio/master_bus_chain_and_export_workflow.md` — the general master-bus chain and export workflow this entry picks up after
- `knowledge_base/mastering/format/vinyl_mastering_considerations.md` — the bass mono-summing threshold, RIAA curve context, and side-length/loudness tradeoff underlying this workflow
- `knowledge_base/mastering/streaming/mastering_for_vinyl_vs_digital.md` — the direct contrast between vinyl's physical cutting constraints and streaming's normalization-driven mastering logic
- `knowledge_base/mastering/stereo/final_mono_and_translation_check.md` — the mono-compatibility check applied here to the summed low band
