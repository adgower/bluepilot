<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Pre-install parity assessment — 2026-10-14

Candidate: openpilot `6ae31161b73de2ce5043f708569759ac5f55f283`, paired opendbc `c09baff5c2cdd7c887e25c2d88b671f403e1ed9d`. Compared with the saved October 14 device inventory and deployment/replay evidence; no fresh device connection was made for this assessment.

## Confirmed preserved in candidate

- Owner 1.20/0.97 angle constants; path-angle steering and engagement ordering.
- Forced FORD_EXPEDITION_MK4 identity, Navigator SWB 3.1115 m wheelbase, steering ratio 19.6 and equivalent normalized dynamics.
- Paired pinion option and unchanged low-speed trial, 30–45 mph fade, startup wiring and both settings UI paths.
- Recorded-input controller replay: identical complete generated CAN on three saved drives / 45 segments; 12,425 >=45 mph messages with zero trial differences. This compares the controller under recorded inputs, not the updated full driving stack.
- DisableUpdates, both Ford preferences and DisengageOnAccelerator are persistent registered keys. The updater exits when DisableUpdates is true. Normal manager transition clearing does not target these persistent keys. Existing preference storage must be retained; fresh storage defaults the Ford options off.
- Startup reads the two Ford preferences when constructing the vehicle interface. Old runtime flags/CarParams must not be transplanted; option bits changed to avoid an upstream collision.

## Known settings to verify before and after migration

DisableUpdates=1; FordPrefSteerAngleCurvature=1; FordPrefLowSpeedGain=1; AlphaLongitudinalEnabled=0; ExperimentalMode absent/off; ExperimentalModeConfirmed=1; OpenpilotEnabledToggle=1; DisengageOnAccelerator=0. Preserve a fresh private full parameter backup, calibration and current source independently of selected-key restoration. The earlier inventory does not identify every setting ever changed. Validate parameter schema migration rather than blindly restoring old serialized runtime/learned data.

## Differences and evidence limits

The candidate is a pinned October 14 upstream master snapshot, not a continuously refreshed latest branch. AGNOS changes from the inventoried 19.7 to 19.9; upstream models, Chestnut firmware expectations and other upstream code differ. The old prebuilt marker and staging symlink are not portable configuration to carry forward. New models/planning/estimation can produce different requested steering even when controller replay is identical. Full Mac builds/tests do not establish AGNOS/Chestnut runtime, offline startup or road parity. Application/source backup is not a demonstrated OS downgrade path.

No known custom steering feature was dropped. An unconditional no-regression/no-configuration-loss guarantee is not supported by current evidence. Keep the working installation until a backed-up, parked target verification is available. Neither MADS nor the separate longitudinal candidate was on the verified device baseline or added here.

## Next preparation and deployment gates

1. Publish paired branches and verify a clean clone resolves both exact SHAs after proceeding with the acknowledged upstream/runtime differences.
2. Prepare the supported AGNOS/model/firmware procedure and establish recovery feasibility before altering OS or firmware. Do not assume copying the old application back restores the OS.
3. While parked with stable power/network, take and verify a fresh private full source/parameter backup and recheck the actual installed state.
4. Preserve selected preferences and calibration with schema-aware handling. Do not factory reset, remove the update pause, restore old prebuilt hacks, or enable experimental/alpha longitudinal as part of this migration.
5. Verify target build, exact source/child SHA, OS/firmware/models, trial preferences, ordinary and offline startup, and vehicle recognition before driving. Treat a later cautious road evaluation as separate evidence.

This assessment is read-only with respect to the Comma; no publication or installation was performed.
