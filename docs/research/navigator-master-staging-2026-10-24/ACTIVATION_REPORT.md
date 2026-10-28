<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Latest master activation

Parent `74eaa6a60d344f141d06da16f4dbe10d3de49c0e` / child `3a5fe9fe5a296d44b7f898b580c2d3afafe6bfd1` is active. Ignition-off acceptance passed: 199 samples, no unexpected stopped processes, blocked-TX counter stable at zero. Owner confirmed normal home screen response. Powered stationary Park acceptance and final audit passed. No road readiness is claimed.

Alpha stayed ON. All selected settings and the fresh snapshot's calibration hashes were preserved, including owner factors **1.20/0.97**. Current learned values were captured before activation rather than replacing them with an older backup. Fresh private Mac snapshot: 64 parameter files; original full device/Mac archive retained.

Whole previous install: `/data/openpilot.pre-master-refresh-<private timestamp identifier>`. Atomic exchange and automatic rollback retained. Exact tested-model identity is bound to both powered-start receipts; all 253 hydrated tracked LFS assets are protected. Review finding reproduced by six failing identity tests, corrected; 43 guard tests pass.

AGNOS remains 20.1, slot B, and installed signed firmware/launchers are preserved. No OS/firmware update or active vehicle ECU query was requested. Parked checks only subscribe to normal stack telemetry.

Evidence: `activation-status.json`, `activation-preparation.json`, `activation-backup-verification.json`, `activation-helper-manifest.json`, `activate.log`, `activation-guard-tests.log`. Powered results and final audit are complete.

## Powered acceptance — passed

The 55-second passive Alpha-on Park capture observed 1,101 big-model samples at **20.002 Hz**, mean execution **38.77 ms**, with **zero dropped frames**. All required telemetry was alive/valid; no CAN, steering, ACC or coordination faults occurred. Panda remained Ford safety parameter 11, controls disallowed, RX-invalid and TX-blocked counters zero throughout 550 samples. All 1,101 coordination pose samples were valid; maximum observed producer age was 25.93 ms. Assistance remained disengaged and the vehicle stationary in Park.

Final audit verified exact clean active/rollback pairs, all 253 tracked LFS assets, source/firmware/launcher hashes, owner settings, Alpha ON, 1.20/0.97, AGNOS 20.1 slot B and active service. Calibration was preserved through the swap. After ignition ON, normal runtime learned-value changes were observed in LiveParametersV2, LiveTorqueParameters, LiveDelay and CarParamsPersistent; none was manually reset or overwritten.

The new master update is active. Parked startup/cadence and inactive coordination transport are validated; moving steering, braking/release reliability and Alpha comfort remain unproven by these checks. Existing brake-release cases are not claimed fixed.

Final evidence: `coordination-alpha-powered-parked-check.json`, `coordination-alpha-powered-parked-samples.json`, `activation-powered-parked-check.log`, `final-activation-audit.json`, `activation-status.json`.
