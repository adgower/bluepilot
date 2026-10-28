<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Restart continuity staging and activation — October 24, 2026

Published exact parent `49be383b2913c5cd62372f7e94222ef75592c61f` and child `d459133a3453d523f1e64b7017a444d78d111f17` on both existing adgower `codex/navigator-tracking-release` branches. Remote refs verified before staging.

Fresh private device and Mac recovery backup verified: 843,630,641-byte archive, 147 manifest members, 69 parameters, nested source archives fully readable. Fresh pre-activation 69-parameter Mac snapshot additionally verified. No learned calibration hash changes before activation.

Full isolated ARM build passed. On ARM: 1,045 native Ford/controller/context tests passed, 79 skipped, 12,083 subtests passed; 75 actual production restart contracts passed; 14 parent smoke and one calibration/engagement regression passed. All isolation and preservation gates passed. Total isolated validation 1,150.9 seconds. The prior saved-road native comparison remains linked through the [integration report](../navigator-restart-continuity-integration-2026-10-24/REPORT.md); this ARM run is not new physical road evidence.

Final staging audit passed: both exact repositories clean, independent Git objects, firmware and launchers preserved, settings and 1.20/0.97 unchanged. Only uptime/Athena background parameters changed during validation.

After explicit activation authorization and verified ignition/Alpha off, an atomic whole-install exchange activated the candidate. The prior complete install is retained at `/data/openpilot.pre-restart-continuity-<private timestamp identifier>`. Ignition-off acceptance passed: 197 Panda samples, no blocked transmissions or unexpected stopped processes. Settings and binary calibration hashes preserved; no OS or firmware update. Owner then enabled Alpha and ignition. Passive stationary Park acceptance passed after startup settled. Initial capture included eight ELM327 identification samples, followed by 451 healthy Ford-mode samples and no faults or blocked transmissions; that initial capture failed the strict all-Ford-mode gate and is retained. An unchanged 55-second recheck passed. Final active/rollback source, settings, firmware, AGNOS 20.1 slot _b and service audit passed.

This change addresses qualified propulsion continuity across 3 m/s (6.7 mph). It does not resolve the separate release timeouts or highway pulsing. Physical comfort and moving engagement remain unproven for this pair.

Evidence: [ARM acceptance](../../navigator-reference/PRIVATE_ARTIFACTS.md), [activation](../../navigator-reference/PRIVATE_ARTIFACTS.md), [backup verification](../../navigator-reference/PRIVATE_ARTIFACTS.md), [staging audit](../../navigator-reference/PRIVATE_ARTIFACTS.md).
