<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Paired longitudinal installation — October 23, 2026

## Current status

Exact published pair activated: openpilot `ffebc43497f8015c37be5927800832f2719c7dca`, opendbc `0ac9618972dd580281c5e933c7990f186522fbd4`. Ignition-off and powered Park acceptance passed. Owner confirmed responsive home screen. Alpha remains **off**, preserving OEM ACC configuration.

## Verified evidence

- Remote heads: [publication.json](../../navigator-reference/PRIVATE_ARTIFACTS.md).
- Private backup: `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-longitudinal`; 843,605,227-byte archive checksum and 135 manifest members verified, nested source archives read through EOF. [Receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md).
- Fresh isolated ARM build and native replay passed in 1,150.9 seconds; 944 native test cases, 79 skips; 14 parent smoke tests. Active source, settings, manager and service unchanged during validation. [Acceptance](../../navigator-reference/PRIVATE_ARTIFACTS.md), [evidence](../../navigator-reference/PRIVATE_ARTIFACTS.md).
- Candidate Git object stores made independent before activation. Firmware and launchers preserved. Full original source retained at `/data/navigator-previous-longitudinal-<private timestamp identifier>`.
- Atomic source exchange and ignition-off startup passed. 201 passive samples; zero blocked TX, no unexpected stopped processes. All selected preferences and five learned/calibration parameter hashes preserved. Owner factors **1.20/0.97** unchanged. [Activation log](../../navigator-reference/PRIVATE_ARTIFACTS.md).
- AGNOS **20.1/B** retained; no OS update, firmware flashing or manual ECU/CAN requests.

## Remaining acceptance and trial boundary

The 55-second passive powered Park check passed with assistance disengaged: no vehicle/Panda faults, zero invalid RX and blocked TX, no unexpected stopped processes, calibrated state, and large model 20.0006 Hz with zero dropped frames. Exact installed pair clean; all Navigator preferences and initial speed setting preserved. [Powered receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md). Alpha-specific testing requires the driver enabling the normal longitudinal Alpha option while parked, understanding its UI warning, and separate powered acceptance. OEM ACC drives do not exercise the new longitudinal handoff.

Offline/parked checks do not establish physical braking release, grade rollback, restart comfort, fuel savings, shaking resolution or highway safety. Start any later longitudinal trial at low speed under the existing [test plan](../navigator-longitudinal-handoff-2026-10-23/TEST_DRIVE_PLAN.md); do not begin with the previous 80–85 mph shaking condition.

## Alpha acceptance after owner UI enablement

Owner enabled Alpha while in Park and disengaged. Separate 55-second passive acceptance **passed**: live openpilot longitudinal enabled, Ford safety parameter11, Alpha preference true; radar and longitudinal planner alive/valid, all radar error flags false, no vehicle/Panda faults, zero invalid RX/blocked TX, assistance inactive, exact paired source clean and retained Navigator settings unchanged. Model about20Hz with zero dropped frames. No lead present in this parked sample; actual lead response, braking, restart and comfort remain road-unverified. [Alpha receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Initial validator failed because radarErrors is a boolean-field structure rather than a list; all fields were false. Corrected the validator only and reran the complete sample successfully. Original failure log retained. No installed source or settings changed during checks.
