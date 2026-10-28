<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Coasting and pose activation

The paired candidate is active on the Comma. Ignition-off acceptance passed; powered stationary Park acceptance also passed after owner confirmation.

- Parent: `2aa86b78d323a068d53a40edcbca5e23968b8108`
- Child: `3a5fe9fe5a296d44b7f898b580c2d3afafe6bfd1`
- Alpha remained ON throughout activation. The installer now verifies Alpha matches the fresh backup, rather than requiring OFF. Ignition-off, offroad, healthy Panda noOutput and disengagement guards remain enforced. Revised policy passed 18 local tests and independent review.
- Fresh private Mac backup verified all 69 parameter files. Settings, calibration hashes and owner factors `1.20/0.97` were preserved.
- Whole previous installation: `/data/openpilot.pre-coast-pose-<private timestamp identifier>`.
- Offroad acceptance: 195 samples; transmit-blocked count stable at zero; no unexpected stopped processes.
- AGNOS remains 20.1. No OS or firmware update was performed.

Evidence: `activation-status.json`, `activate.log`, `activation-backup-verification.json`, `install-guard-tests.log`.

Parked acceptance does not establish highway smoothness or physical brake-release behavior. Previously identified brake-release timeout cases remain unresolved by this candidate; road improvement is unproven.

## Powered stationary acceptance

The 55-second passive Alpha-on Park check completed successfully (`COORDINATION_ALPHA_POWERED_PARKED_ACCEPTANCE_PASS`). No assistance was engaged or active test requests transmitted. The final source/settings audit passed, including clean active and rollback trees, exact paired gitlink, 1.20/0.97, Alpha ON and AGNOS 20.1. Learned LiveTorqueParameters, LiveDelay and CarParamsPersistent changed after ignition-on through normal runtime; these were not manually overwritten.

Evidence: `coordination-alpha-powered-parked-check.json`, `coordination-alpha-powered-parked-samples.json`, `powered-parked-check.log`, `final-activation-audit.json`. Physical brake-release behavior, pulsing improvement and road reliability remain unproven.
