<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Paired activation plan

User authorized backup, activation of the validated pair, preservation of settings/1.20/.97 and parked checks.

1. Verify offroad/ignition off, clean original pair, settings and passive health. Save fresh tracked-source/full-parameter backup on Mac, verify archives and hashes; preserve launcher, signed Panda image, parameter snapshot and original Git rollback refs on device.
2. Verify exact candidate and descendants; same native dependencies, OS and Panda safety source. Reuse already validated source/ARM build/replay evidence. Stop application only while ignition off. Import verified bundled commits, preserve old heads under new rollback branch names, fast-forward both current branches (no reset/clean/force).
3. Before startup, verify exact paired heads, clean source, geometry/1.20/.97, settings/calibration and signed Panda image. Exercise exact Car constructor with in-memory parameters/stubbed IPC to verify option selects BudgetedTrackingPrototype. No CAN I/O in validation.
4. Start normal app. Preserve original preferences, restoring only known startup-default ExperimentalMode initialization to its captured state if necessary. Verify exact source/runtime metadata, expected processes, offroad/noOutput/controls disallowed and unchanged calibration/source/image/settings. On failure, stop application and restore original pair from dedicated rollback refs if clean; verify before restart. Never reset/clean dirty source.
5. Ask user to turn ignition on while remaining in Park only after offroad acceptance passes. Run passive powered parked check for actual CarParams, model/Chestnut health, faults, no assistance engagement, and source/options. No active ECU requests, injected control/steering tests, OS or firmware updates. If ignition is unavailable, clearly mark powered parked acceptance pending and do not call ready for driving.
6. Save receipts/report/roadmap. Separate startup/offline/parked evidence from road steering response. Keep fresh rollback material.

Execution ledger:
- Started: source/state inspection and fresh Mac backup.
- Ruling: fast-forward existing clean active repositories rather than switching active path to borrowed-object stage. The stage borrows active Git objects; relocating it would make its alternates fragile. Existing compiled assets/dependency pins are unchanged. Cost if wrong: startup failure; guarded rollback and parked acceptance before road testing.

- Pre-activation review fixed rollback settings/calibration verification and added all-parameter hashing.
- First runtime attempt: source/constructor/startup passed, but overly strict calibration comparison rejected manager-cleared live CarParams and default/reset metadata. Guard stopped app and restored old source; persistent calibration and owner options still matched. Verified CarParams/IsDriverViewEnabled/DriverLockoutCount manager-reset definitions in params_keys.h. Ruling: classify these documented startup fields and BootCount as runtime state; never restore stale CarParams or driver lockout state. Preserve every persistent calibration/preference and record all differences. Retry switches back to existing candidate branch without advancing saved rollback refs.

- Completed: fresh backup verified, exact pair active with original rollback refs intact, offroad acceptance passed, powered parked acceptance passed55.01s. Owner preferences and decoded learned steering values retained. Road-response validation remains outside parked acceptance.
