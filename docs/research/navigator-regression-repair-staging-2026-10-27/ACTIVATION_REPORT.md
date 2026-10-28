<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Regression repair activation — October 27, 2026

**New pair activated; ignition-off acceptance passed. Powered stationary acceptance is pending the owner’s ignition transition.**

Active parent `e05e42f43d2907a4f02915a924cfd95a46197e79` pins child `5097b993965b2b65ea3fcca7e3769cfa9403d49c` on `codex/navigator-tracking-release`. The entire prior `df788e02719c05595dab2f980e6fd9fb9e464006` / `1d29e6e78abcbf5c6a80eb397d80b349c6cca960` install is retained at `/data/openpilot.pre-regression-repair-<private timestamp identifier>`. The switch used `rename_exchange` with guarded rollback; the source directories were exchanged whole, preserving previous compiled binaries.

Owner explicitly authorized installation and confirmed parked/ignitionOFF/stable power/Wi-Fi/screen/recovery cables. Fresh current68parameter snapshot on device and private Mac was verified before switching. Current learned calibration differs from the original pre-drive backup and was carried forward unchanged. All selected settings and protected learned hashes matched the fresh activation snapshot after startup. Alpha remains ON;1.20/0.97, current steering opt-ins, geometry, launchers, signed firmware and AGNOS20.1slotB were preserved. No OS/firmware update, custom CAN transmission or active ECU query was performed.

Before switching: retained staging evidence hashes checked;18installer guards passed; isolated pure Card constructor check covered all8tracking/roll/high combinations and selected `MidrangeAdmission` for all opt-ins. Independent review found no critical/important defect. This adapts the assertion to the new class without changing runtime code. Fresh device/Mac activation params and exact helper hashes were required by dispatch.

Ignition-off acceptance:201passive Panda samples, noOutput/no ignition/no controls allowed, blocked-TX value0stable, no unexpected stopped process. Exact active pair, clean source, firmware/launcher hashes, every selected preference and protected learned hash passed. The recorded original blocked counter was historical9before switching; the restarted stack reset it to0. No road/physical comfort result is inferred.

See `activation-status.json`, `final-preservation-checks.json`, `activation-helper-manifest.json`, `activation-backup-verification.json`, `activation-card-startup.log` and `ACTIVATION_REVIEW.md`.

One initial local guard-test invocation loaded the unrelated BluePilot root conftest; correcting the standalone test boundary yielded18passes. PWD/environment warnings during the swap were nonfatal and are retained in the console log. All production source bytes remained the staged/tested revisions.

The owner has been asked to confirm home-screen response and turn ignition ON while stationary in Park with assistance disengaged for passive new-stack checks. No powered or road acceptance is claimed yet. The two historical release-timeout replay faults and physical pulsing/tracking benefit remain open.
