<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Coordinated coast/brake activation — October 27, 2026

Activated parent `df788e02719c05595dab2f980e6fd9fb9e464006` with opendbc `1d29e6e78abcbf5c6a80eb397d80b349c6cca960`.

Ignition-off acceptance passed. Powered stationary Park observation passed for 55 seconds: model 20.0005 Hz, zero dropped frames, 550 Panda samples, zero blocked commands, all required telemetry alive/valid, and assistance disengaged. Pose inputs were healthy in all 1,100 samples.

Final identity and preservation audit passed. Alpha and coordination remain ON; owner 1.20/0.97 settings preserved. AGNOS 20.1, firmware and launcher preserved. Latest learned parameters were backed up and not manually overwritten; normal learned changes after ignition-on are recorded in the final audit.

Full previous installation retained at `/data/openpilot.pre-coordinated-coast-<private timestamp identifier>`. Fresh 68-file parameter snapshot verified on Mac before activation. Existing ARM build and replay evidence remains in this directory. The initial powered-check SSH timeout was resolved by retrying; no further installation change was needed.

These checks establish parked operation only. Physical highway pulsing, braking comfort and rolling-restart improvement remain unproven on the road. The accepted replay benefit is modest; it does not establish that pulsing is fixed.

Evidence: `parked-powered.json`, `final-activation-audit.json`, `activation-console.log`, and `activation-backup-verification.json`.
