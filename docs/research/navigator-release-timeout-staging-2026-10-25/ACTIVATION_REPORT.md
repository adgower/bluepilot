<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Brake-release timeout activation — October 25, 2026

Active pair: parent `ead00c30e0f3e174130f475847b1f4a2a76e8902` / child `d4a201251d184a446cb2db383f4bd024c93e75cb`. Whole previous installation retained at `/data/openpilot.pre-release-timeout-<private timestamp identifier>`. Atomic exchange and automatic rollback guards were used; ignition-off acceptance passed with 192 Panda samples and no blocked transmissions or unexpected stopped processes. Alpha remains ON; selected settings and fresh learned calibration hashes are preserved. Steering remains 1.20/0.97. No OS/firmware update or device reboot occurred; the app service was restarted for activation.

The pre-activation ARM build and tests had passed. Before switching, the 253 model assets and exact clean paired source were reverified. A fresh 69-parameter Mac recovery snapshot preserves learned LiveParametersV2, LiveTorqueParameters and LiveDelay updates since the original staging backup; these were not overwritten with older values.

Owner confirmed the home screen responds and ignition ON in stationary Park; powered Park acceptance passed. Moving behavior and longitudinal maneuver completion are not yet proven for this revision. The change addresses the two progressing-release watchdog expirations; separate pose faults and highway pulsing remain separate work.

## Powered acceptance and final audit

55-second activated-stack passive check passed: 1,101 big-model samples at 20.0006 Hz, zero dropped frames, 551 healthy Ford-mode Panda samples (parameter 11), no controls permission, RX errors, blocked TX, transport faults or coordination faults. All 1,101 observed coordination requests had valid pose; all producer observation ages were below 28.6 ms. Assistance stayed disengaged and vehicle stationary in Park. Latest exact paired source, source cleanliness, retained owner settings, active service and clean rollback tree were verified. Firmware/launchers and AGNOS 20.1 slot _b are unchanged.

Learned LiveParametersV2, LiveTorqueParameters, LiveDelay and CarParamsPersistent hashes updated naturally after ignition ON; no learned parameter was manually written. Fresh pre-activation copies remain backed up on Mac and device. The source switch preserved the fresh pre-activation learned hashes during ignition-off acceptance.

Activation and requested parked checks are complete. The next evidence is a controlled maneuver-test retry; neither complete moving maneuver coverage nor a highway-pulsing improvement is established by these parked checks.
