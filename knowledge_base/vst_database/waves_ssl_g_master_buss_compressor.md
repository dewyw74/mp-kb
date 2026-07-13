---
plugin_name: "SSL G-Master Buss Compressor"
developer: "Waves"
category: "compressor"
type: "bus compressor (emulation of the SSL 4000 G console's stereo buss compressor)"
cpu_usage: "low"
best_genres:
  - house
  - hip_hop
  - pop
  - rock
strengths:
  - "Modeled directly on the SSL 4000 G console's stereo buss compressor, one of the most widely referenced 'glue' compression sounds in mixing history — a genuine industry-standard reference point, not just a generic bus compressor."
  - "Simple, fast parameter set (attack, release, ratio, threshold, makeup gain, plus a characterful auto-fade/release behavior) makes it quick to dial in a cohesive bus-glue sound without extensive tweaking."
  - "Distinct sonic character (a specific, well-known coloration and 'punch' on transients) beyond just gain-reduction math, which is the actual reason producers reach for this specific emulation rather than a generic compressor set to similar numeric parameters."
  - "Very low CPU cost, practical for mix-bus, drum-bus, and master-bus use without performance concerns."
weaknesses:
  - "Single fixed character — unlike FabFilter Pro-C 2's selectable style algorithms (`fabfilter_pro_c_2.md`), this plugin emulates one specific hardware unit's behavior rather than offering multiple selectable compression characters in one instance."
  - "As a hardware emulation, its appeal is largely about matching a specific, well-known sonic signature — for fully transparent, surgical compression with no added character, a cleaner digital compressor (Ableton's own Compressor/Glue Compressor, or FabFilter Pro-C 2's Clean mode) is a better fit."
alternatives:
  - "Ableton Glue Compressor (see `ableton_compressor_and_glue_compressor.md`) — also modeled on classic bus-compressor behavior, included natively with Live at no additional cost"
  - "FabFilter Pro-C 2 (see `fabfilter_pro_c_2.md`) — for selectable-character compression rather than one fixed hardware emulation"
recommended_settings:
  - "Mix-bus/master-bus glue: moderate ratio (2:1-4:1), slower attack to let transients through, auto-release engaged, applied gently (2-4dB gain reduction) for cohesion rather than obvious pumping — the classic 'SSL bus comp' glue application."
  - "Drum bus punch: faster attack settings and a higher ratio for a more audible, characterful compression effect on a drum group specifically, leaning into the plugin's distinct transient coloration rather than aiming for transparency."
common_uses:
  - "Mix-bus and master-bus glue compression"
  - "Drum bus cohesion and characterful punch"
  - "General-purpose bus compression wherever the specific SSL console-emulated character is the desired sonic signature"
tags: ["ssl", "waves", "bus-compressor", "glue-compression", "console-emulation", "mixing"]
---

# SSL G-Master Buss Compressor

The SSL G-Master Buss Compressor (Waves) is a software emulation of the stereo buss compressor built into the SSL 4000 G recording console — one of the most referenced and imitated compression sounds in mixing history. Where `knowledge_base/vst_database/fabfilter_pro_c_2.md` offers several selectable compression-style algorithms in one plugin, this plugin instead commits to emulating one specific, well-known piece of hardware's behavior, and its popularity comes directly from producers wanting that particular, recognizable sonic signature rather than a generic compression curve.

## Sound Character and Strengths

The plugin's appeal is inseparable from its hardware-emulation lineage — its specific coloration and transient "punch" character on a bus is a known, widely-referenced sound that a generic compressor set to matching numeric parameters (threshold, ratio, attack, release) doesn't automatically reproduce, since much of an analog console compressor's character comes from circuit-level behavior beyond the basic gain-reduction math. Its parameter set is intentionally simple — this is a fast, opinionated tool for bus glue, not a deep multi-parameter dynamics processor, and that simplicity is part of why it remains a fast, reliable choice for mix-bus and master-bus cohesion.

## Weaknesses

Because it emulates one specific hardware unit, it offers a single fixed character rather than the multiple selectable compression styles a plugin like FabFilter Pro-C 2 provides in one instance — achieving a genuinely different compression character means reaching for a different plugin, not switching a style parameter. For fully transparent, surgical compression with no added coloration, a cleaner digital compressor (Ableton's stock Compressor, or Pro-C 2's Clean mode) is a better fit than a plugin whose entire value proposition is its specific added character.

## Relationship to Ableton's Own Glue Compressor

`knowledge_base/vst_database/ableton_compressor_and_glue_compressor.md` documents Ableton's own Glue Compressor as similarly modeled on classic analog bus-compressor behavior, included natively with Live at no additional cost. The SSL G-Master Buss Compressor's specific appeal over Ableton's native option is its direct lineage to one particular, widely-referenced console — a producer specifically chasing "the SSL sound" as a known reference point reaches for this plugin, while a producer wanting general bus-glue cohesion without needing that specific reference can get comparable practical results from Ableton's included Glue Compressor.

## Common Mistakes

**Using this plugin as a general-purpose single-channel compressor rather than for bus-wide glue.** Its character and simple parameter set are tuned for gluing a group of already-mixed elements together, not for surgical, single-source dynamics correction — per `knowledge_base/mixing/compression/parallel_compression.md`'s general density/cohesion principles, this is a bus tool first.

**Pushing gain reduction far beyond the gentle 2-4dB range typical of subtle glue applications and expecting a transparent result.** This plugin's character becomes increasingly audible and colored as gain reduction increases — appropriate when that audible character is the goal, counterproductive when transparency is.

## Cross-References

- `knowledge_base/vst_database/ableton_compressor_and_glue_compressor.md` — Ableton's native, similarly bus-compressor-modeled alternative
- `knowledge_base/vst_database/fabfilter_pro_c_2.md` — the selectable-multi-character alternative for tasks needing more than one fixed compression style
- `knowledge_base/mixing/compression/parallel_compression.md` — the general bus-glue/density principle this plugin is most commonly used to implement
