<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Coasting and pose device staging — October 24, 2026

The exact tested pair is published and built in a separate Comma checkout. ARM and offline validation passed. **The candidate is inactive; the current installation remains active.** Final metadata preparation and preservation audit passed. Both staged repositories are clean, with self-contained Git objects.

## Published pair

- openpilot: `2aa86b78d323a068d53a40edcbca5e23968b8108`
- opendbc: `3a5fe9fe5a296d44b7f898b580c2d3afafe6bfd1`
- Both existing adgower `codex/navigator-tracking-release` remote refs match the local commits.

## Recovery backup

A fresh private source/settings recovery archive was created on the Comma and copied to `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-coast-pose`. The 843,633,456-byte archive, all 147 manifest members and both nested source archives were verified. It preserves 69 parameters, source snapshots, launchers and the installed signed Panda image. No settings were changed.

## Isolated ARM validation

The dedicated transient unit ran against a separate checkout with the live tree read-only, private parameters/cache/log/home, network interfaces down, vehicle devices blocked and privileges dropped. All probe/build/offline-test phases passed; total time was 1,132.9 seconds.

- Full ARM build passed.
- 1,094 native/Ford/context tests passed, 79 skipped, 12,083 subtests passed.
- All 75 retained restart/braking contracts passed. Three superseded admission expectations were updated to the already validated bounded-coasting contracts; original clearance and timeout assertions remain.
- Startup, scheduler/default and actual Controls/Card pipeline checks passed.
- 14 parent smoke tests passed; six documented parameterized base-class cases skipped.
- Calibration/engagement wrapper passed.

Coverage explicitly includes the new coasting class and both parent pose modules. Transfer/gate checks verify 86 protected child files, four candidate child files and seven candidate parent files. Live source, selected settings, manager PIDs and service timestamp stayed equal before/after validation; only background uptime/Athena parameter hashes changed.

This ARM run is build/unit/contract validation. The prior [local integration report](../navigator-coast-pose-integration-2026-10-24/REPORT.md) retains the four-drive saved-traffic replay; those raw drives were not rerun on ARM here. No physical comfort, moving engagement or new road acceptance is established.

## Current installation and scope

The live install remains parent `49be383b2` / child `d459133a`. Passive ignition-off observation passed over 55 seconds and 550 Panda samples, with no faults or new blocked transmissions; the historical blocked count was seven and stayed constant. This is evidence about the current install, not an active candidate hardware check.

Owner **1.20/0.97**, steering/geometry, settings, AGNOS 20.1 and boot slot `_b` are preserved. Quiet-release is excluded. The known brake-release timeouts and physical pulsing concerns remain; staging does not resolve them. No activation, service restart, OS/firmware update, active ECU queries or CAN transmission were performed.

Evidence: publication.json, backup-verification.json, validation-acceptance.json, evidence/preservation.json and parked-offroad.json. Final receipts: [inactive preparation](../../navigator-reference/PRIVATE_ARTIFACTS.md) and [preservation audit](../../navigator-reference/PRIVATE_ARTIFACTS.md). Selected preferences and binary calibration hashes match the fresh backup; firmware, launchers, OS/slot and live service remain unchanged. Only background Athena/uptime parameter hashes changed.
