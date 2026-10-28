<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Master sync deployment — October 20, 2026

Status: published and installed; ignition-off acceptance passed. Powered stationary acceptance passed.

Parent `db584234805cf2039ee976d856a29b655188ad2a` merges upstream `1ace967a7e27d2537a956c683978f646d6b6d739`; child `8ccc6cf0ee123afddddbf6e0a0ea3d3316669a5e` remains unchanged. Existing adgower origins and branch `codex/navigator-tracking-release` verified after publication.

Fresh private backup: device `/data/navigator-backups/<private timestamp identifier>-pre-master-sync`, Mac `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-master-sync`. Archive checksum, manifest and nested source archives verified; 843,669,817 bytes, 147 manifest members, 68 parameters. Whole previous installation will be retained on activation. Private backup material is outside this report.

Preserve owner 1.20/0.97, custom steering options, learned calibration, stock ACC/Alpha off, AGNOS 19.9, signed firmware and launchers. Removed ExperimentalMode is archived raw and excluded from new typed Params access; rollback restores migration keys exactly. InitialCruiseSpeedKph adopts upstream 40 only if previously absent, otherwise preserves the owner's value.

Fresh validation covers isolated full ARM compilation, Ford/controller/native/context tests, actual Card startup, IPC/stale snapshot handling, scheduler stalls and cruise/Mici/default-key tests. Prior child transition/abort matrices are carried by exact receipt hashes and 85 protected source-file identities; they are not freshly rerun. This does not establish road tracking or high-speed stability.

Independent installer review found skipped JUnit cases could pass the parent gate. Regression reproduced the defect; updated gate rejects skipped/failing/error cases and all nine helper tests pass. Exact remote helper update recorded in helper-patch-receipt.json. No other material installer finding identified.

Activation and powered stationary acceptance passed. No OS/firmware update, ECU request or manual CAN command is part of this deployment.

## Fresh device validation results

Full ARM build passed. Native suite: 750 passed, 79 skipped, 12,063 subtests. Initial runtime check stopped because the isolated Params mock lacked upstream return_default; a failing regression confirmed the issue, then the corrected mock passed. Original failure receipts remain. A separate supervised runtime-only followup passed eight Card selection combinations, actual IPC/calibration/stale withdrawal, fake-clock stalls and default keys. Parent tests: 14 passed, six parameterized base classes skipped by upstream design; all concrete cruise variants and three UI cases executed. Exact base-class skips are allowlisted; other skips or absent executed module coverage fail acceptance. Eleven helper tests pass. Active source/settings/manager/service preserved in both supervision receipts. Total supervised validation 1,627 seconds; no repeated large child matrices.

## Activation

Guarded atomic exchange completed. Target parent db584234805cf2039ee976d856a29b655188ad2a / child 8ccc6cf0ee123afddddbf6e0a0ea3d3316669a5e are active. Both repositories clean; protected source/settings and five learned parameter hashes equal backup. Existing steering opt-ins and 1.20/0.97 preserved; Alpha remains off and update pause remains enabled. InitialCruiseSpeedKph initialized to the upstream default. Twenty-second offroad acceptance: 201 samples, no unexpected stopped processes. Previous complete installation retained at /data/navigator-previous-master-sync-<private timestamp identifier>. AGNOS 19.9, signed firmware and launchers preserved. No manual CAN or ECU requests issued. Powered stationary acceptance subsequently passed; parked results do not establish road tracking.

## Powered stationary acceptance

User confirmed ignition on, stationary in Park, assistance disengaged. Passive 55.01-second check passed: all 12 topics alive/valid; zero CAN-invalid, timeout, steering or vehicle fault samples; no unexpected stopped processes, Panda faults, SPI errors or Chestnut supply faults. Ford safety parameter 10; controls disallowed throughout, zero RX-invalid/blocked-TX counters. Big model 20.001 Hz, 1,101 samples, zero frame drops, mean execution 39.90 ms. All 1,101 calibration snapshots had valid provenance and matching targets. Exact installed pair clean.

Update pause and five steering preferences remain enabled; Alpha longitudinal remains off, stock ACC retained, initial speed default 40 kph. Learned steering ratio 21.9478855, mean angle offset -1.8609586 degrees and delay 0.2846166 seconds retained, as are geometry/profile/flags/safety, CalibrationParams hash and torque payload. Normal torque-cache event timestamp changed; payload equal. No settings restored or changed by these read-only checks. Owner 1.20/0.97 remains protected in unchanged steering source.

Installation gates complete. Road tracking after the master merge remains unvalidated; no new steering tune was installed. Use ordinary supervised driving and review logs afterwards.
