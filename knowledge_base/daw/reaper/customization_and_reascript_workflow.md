---
workflow_name: "Reaper Customization and ReaScript Workflow"
daw: "reaper"
category: "scripting"
goal: "Use Reaper's Actions list, custom keyboard shortcuts/toolbars, and ReaScript (EEL2, Lua, or Python) to automate repetitive tasks and extend Reaper beyond what stock menus and dialogs expose."
steps:
  - "Open the Actions list (default shortcut: ?) before building a custom shortcut or macro — check whether a built-in action already does what you want."
  - "Combine several existing actions into one repeatable command using a custom action (macro), built from the Actions list's 'New action...' > 'New custom action...' entry."
  - "Assign a keyboard shortcut, mouse modifier, MIDI/OSC trigger, or toolbar button to any action or custom action so it's triggered without opening the Actions list."
  - "For behavior no built-in action covers, write a ReaScript: choose EEL2 or Lua for something that works immediately with no extra install, or Python if you need to interoperate with external Python libraries."
  - "If using Python, install it separately and enable it under Options > Preferences > Plug-ins > ReaScript, matching Reaper's bitness (32-bit Reaper needs 32-bit Python, 64-bit needs 64-bit)."
  - "Create a new script via Actions list > 'New action...' > 'New ReaScript...', which opens Reaper's built-in code editor (or your preferred external editor) and saves a file with the matching .eel, .lua, or .py extension."
  - "Load an existing script file into the Actions list via 'New action...' > 'Load ReaScript...' rather than rewriting it from scratch."
  - "Run a script directly from the Actions list, or bind it to a shortcut/toolbar icon exactly like a native action."
  - "Install ReaPack (a community package manager) to browse, install, and auto-update third-party ReaScripts, JS effects, and themes instead of manually tracking script files."
  - "Add the SWS/S&M Extension for a large library of extra stock-style actions (region/marker management, auto-coloring, cycle actions) that cover many common customization needs without writing a script at all."
related_plugins:
  - "Reaper Actions List"
  - "ReaScript (EEL2 / Lua / Python)"
  - "SWS/S&M Extension"
  - "ReaPack"
tags:
  - "reaper"
  - "reascript"
  - "customization"
  - "actions-list"
  - "scripting"
  - "automation"
  - "workflow"
---

# Reaper Customization and ReaScript Workflow

Deep customization is Reaper's signature differentiator among DAWs: almost every command is exposed as an item in a single searchable Actions list, any of those actions (or a custom chain of them) can be bound to a shortcut or toolbar button, and where the built-in command set runs out, ReaScript lets a producer write actual code — in EEL2, Lua, or Python — to add new behavior. This turns Reaper from a fixed-feature application into a platform that reshapes itself around a specific workflow.

## The Actions List

The Actions list (opened with `?` by default) is the central command index for the entire application — thousands of built-in actions covering editing, transport, routing, rendering, and view management, all searchable by name. Before building anything custom, search here first; a large share of "I wish Reaper could..." requests turn out to already be a built-in action that simply isn't bound to a shortcut yet.

## Custom Actions (Macros)

A custom action chains multiple existing actions into a single command, run as one step and assignable to one shortcut. This is the lowest-effort form of customization: no scripting required, just selecting a sequence of actions (for example, "split items at edit cursor" followed by "trim content behind items") and saving the chain as a new named action that then behaves exactly like a native command, including its own keyboard shortcut and toolbar icon.

## ReaScript: Languages and Setup

ReaScript supports three languages with different tradeoffs. EEL2 is an in-house C/JavaScript-like language built into Reaper with no install step and strong runtime performance. Lua (5.4) is also built in, generally easier to learn than EEL2, and offers the same UI/graphics capabilities. Python must be installed separately and enabled under Options > Preferences > Plug-ins > ReaScript (matching Reaper's 32-bit/64-bit build to the Python install); it runs slower than EEL2 or Lua and lacks their native UI/graphics features, but it's the right choice when a script needs to lean on Python's wider library ecosystem.

## Writing, Loading, and Running Scripts

A new script is created from the Actions list via "New action..." > "New ReaScript...", which prompts for a save location and infers the language from the file extension (.eel, .lua, or .py) — this opens Reaper's built-in code editor by default. An existing script file is added the same way via "Load ReaScript...". Once a script is in the Actions list, it runs exactly like any native command: from the list itself, from a bound shortcut, or from a toolbar button, and it appears alongside built-in actions rather than in a separate scripting-only menu.

## Extending Further: ReaPack and SWS

ReaPack is a community package manager that installs and auto-updates third-party ReaScripts, JS effects, themes, and language packs from public repositories, removing the manual file-management step of tracking down and updating individual script files. The SWS/S&M Extension is a widely used free add-on that bundles hundreds of additional stock-style actions (region and marker management, auto-coloring, cycle actions, project organization tools) — much of what a producer might otherwise write a custom script for is already covered by SWS, so it's worth checking before writing one from scratch.

## Common mistakes

Writing a full ReaScript for something a custom action (macro) could already do with zero code — check the Actions list and custom-action chaining first. Choosing Python by default without needing its library ecosystem, which adds an install/configuration step and gives up EEL2/Lua's better in-app performance and UI support for no benefit. And skipping SWS/ReaPack entirely: a large share of "I need to script this" problems in Reaper are already solved by an existing SWS action or a published community script.
