# daw/

DAW-specific workflow entries — `ableton/` (primary DAW), `fl_studio/` (secondary), `logic_pro/`, `pro_tools/`, `cubase/`, `studio_one/`, `reaper/` (alternative DAWs), `workflow/` (cross-DAW process guidance, `daw: "generic"`). Entries conform to `schemas/workflow_schema.json`, whose `daw` field enum must be one of these exact values.

Consumed primarily by `daw_agent`, which defaults to Ableton Live unless the user names a different DAW.
