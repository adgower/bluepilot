<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# MADS / always-on steering exploration — 2026-10-14

Read-only research for a future vanilla-openpilot Navigator feature. No implementation, device changes, or new replay. MADS is a candidate, not part of the installed Navigator trial.

## The upstream name Alex may remember

The strongest matching proposal is comma's **Always on steering**, [PR38583](https://github.com/commaai/openpilot/pull/38583), by sshane. Live API: closed, **not merged**, exact head `ecc11b57d1df7bec8dbfe08bc881f918d8df9883`. It was explicitly exploratory and closed by inactivity automation; live API `closed_at` is `<private wall-clock timestamp>`. Cached web HTML still showing draft/open is stale; live API state takes precedence. Its patch adds `IsAosEnabled`, a Comma-four toggle, separate lateral/longitudinal selfdrive-state fields, and event-design notes. It leaves `lat_active` initialized false without a complete lateral state machine. This is architectural exploration, not a ready feature or a feature subsequently reverted. [patch](https://github.com/commaai/openpilot/pull/38583.patch), [live metadata](https://api.github.com/repos/commaai/openpilot/pulls/38583).

Other primary-source candidates:

| Proposal | Verified current status | Relevance |
| --- | --- | --- |
| [PR38391 — try MADS](https://github.com/commaai/openpilot/pull/38391) | Closed, unmerged; head `048661da1bf019f6dd36ec46b9a27d8e75213c41` | More complete prototype: parameter, alternativeExperience, lateral-only state, controls mismatch handling, UI and dependencies; explicitly Hyundai Sonata-only. Not a Ford-ready port. |
| [PR35165 — Always on lateral](https://github.com/commaai/openpilot/pull/35165) | Closed, unmerged; head `392da26e2b0d0563a1947e5210738fddee19101b` | Older naming candidate. No verified upstream deployment or reversal. |
| [PR37747 — reserved controls_allowed fields for forks](https://github.com/commaai/openpilot/pull/37747) | Merged 2026-04-04, merge `f170440f4ac49d4804eaa9079adf30fa291e49e7` | Infrastructure for forks, not upstream MADS behavior. |

An API merge_commit_sha alone does not prove merger; the `merged`/`merged_at` fields establish these statuses. Search did not establish an upstream proposal literally named ALKA. These named matches are stronger evidence than guessing that acronym.

## Current sunnypilot versus historical docs

The [official current README](https://github.com/sunnypilot/sunnypilot) directs users to docs.sunnypilot.ai, which currently redirects to community.sunnypilot.ai/docs and could not be read through the web tool. Do not silently substitute archived 2024 instructions for current configuration.

Current BluePilot local source names MADS **Modular Assistive Driving System**. Earlier official sunnypilot [archived README](https://github.com/sunnypilot/sunnypilot-archive) expands it as Modified Assistive Driving Safety and describes independent lane centering/cruise. Those old driver instructions are historical evidence only. Current local implementation is a better source for the BluePilot behavior under consideration.

## BluePilot local Ford path inspected

- `sunnypilot/mads/mads.py` reads `Mads`, `MadsMainCruiseAllowed`, steering-on-brake mode and unified-engagement settings. It owns lateral enable/disable events separately from stock cruise, respecting main-cruise availability for Ford. Cancel transitions can remove longitudinal operation while lateral remains requested. Brake behavior has explicit pause versus disengage modes; longitudinal auto-resume is not implied by lateral resume.
- `sunnypilot/mads/state.py` has a separate enabled/paused/soft-disabling/overriding state machine and retains immediate/soft fault handling.
- `opendbc_repo/opendbc/sunnypilot/car/ford/mads.py` decodes the Ford `Steering_Data_FD1.TjaButtnOnOffPress` button.
- `opendbc_repo/opendbc/safety/modes/ford.h` reads the same button bit. Common `safety_mads.h` and `safety.h` maintain lateral requested/allowed state, brake-mode behavior, main-off disengagement and heartbeat mismatch protections.

These are inspected local source paths, not proof of current remote BluePilot release status or installed Navigator functionality. Relevant primary upstream design sources: [sunnypilot MADS](https://github.com/sunnypilot/sunnypilot/tree/master/sunnypilot/mads), [sunnypilot opendbc](https://github.com/sunnypilot/opendbc).

## Candidate scope for the stock-openpilot branch

A scoped Ford/Navigator MADS port is feasible research, but neither exploratory upstream PR is a drop-in solution. Required layers include: Ford main/LKAS/cancel button semantics; independent lateral state and fault/driver-monitoring handling; explicit brake pause/disengage behavior; controls/pandad state and heartbeat; matching Panda permission logic and firmware; Comma-four indicators/settings; and engagement transition tests/replay with the already installed angle/pinion controls. Preserve longitudinal disengagement and explicit longitudinal re-engagement behavior.

Crucially, the current Navigator trial's ordinary `controls_allowed` drops on brake/cancel. Changing only Python `latActive` would produce safety rejections; changing only Panda permission would leave application-state inconsistencies. MADS does not improve steering gain, solve low-speed tracking, or add longitudinal actuation by itself. Existing human-turn override and paired pinion limits still apply.

Recommended first step: write a precise button/brake/fault behavior table, then prototype locally with MADS off by default, keeping owner 1.20/0.97 and trial gain behavior fixed. Evaluate transitions and recorded safety replay before any deployment. User preference between pause-on-brake and explicit disengage-on-brake is a real behavior choice to settle before implementation.
