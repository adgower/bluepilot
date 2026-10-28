<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Calibrated/mid/rearm installation — October20,2026

Installed; ignition-off and powered stationary acceptance passed. Ordinary supervised road evaluation pending.

## Pair, backup and preservation

Published exact pair, child first without force; remote heads verified:

- openpilot `f750d756caf772c36c01a97be4c03501de8851db`
- opendbc `de70d4f945b2bb1472e5207b92d2276137d8c5a1`

Fresh post-drive private backup `/data/navigator-backups/<private timestamp identifier>-pre-calibrated-rearm`; independent Mac copy `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-calibrated-rearm`. Archive 843,593,059bytes,66parameters; hash/size,143manifest members and both nested source archives verified. Whole previous install retained at `/data/navigator-previous-calibrated-rearm-<private timestamp identifier>`. Owner **1.20/0.97**,selected settings and all captured learned/calibration hashes matched during ignition-off acceptance. AGNOS remains19.9; exact installed firmware/launchers preserved. No OS/firmware update or manual ECU/CAN diagnostic query.

## Fresh validation and activation

The first attempt aborted safely when the vehicle went onroad. Its receipts are retained separately; no acceptance from it was used to activate. After user returned, fresh backup and full validation rerun completed with a fresh parked preservation snapshot. Same exact-pair stage `/data/navigator-validation/<private timestamp identifier>-f750d756c` retained262hash-verified LFS assets. Dedicated validation unit isolated vehicle devices/network/parameters/cache and kept active source read-only.

Fresh full ARM SCons build passes. Ford/native suite690passed/79skipped/12,063subtests; retained320case/115,200frame roll screen and480case/172,800frame sustained screen pass. New714case/228,480frame calibrated transition and128active-abort cases pass, as do all8actual Card preference combinations, controls/Card/Cap'nProto IPC,atomic calibration and stale withdrawal. Live source/settings/manager/service preservation matched across the successful run. [Validation acceptance](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Prepared self-contained Git objects,clean paired source,preserved launchers/firmware and compiled startup artifacts. Guarded whole-directory exchange retained previous binaries and provided automatic whole-pair rollback on ignition-off failure. Twenty-second passive ignition-off acceptance passed: NO_OUTPUT,no ignition/control permission,no sampled faults or blocked-TX increments. [Activation](../../navigator-reference/PRIVATE_ARTIFACTS.md),[preservation](../../navigator-reference/PRIVATE_ARTIFACTS.md),[backup](../../navigator-reference/PRIVATE_ARTIFACTS.md),[review](REVIEW.md).

Existing preference prerequisites already enable the new class; no extra toggle or parameter was added. Rollback should be parked with ignition off, preserving intervening settings; restore the whole pair rather than mixing source or restoring stale learned values.

Local/native/parked checks establish startup and bounded command behavior, not physical tracking improvement or closed-loop road stability. Use ordinary supervised driving after powered acceptance, taking over as needed; no deliberate high-speed or lane-edge reproduction is required.

## Powered stationary acceptance

Fresh55-second passive stationary Park check passes. Assistance stayed disengaged; source/settings/profile/geometry/native safety and core learned steer ratio,average offset,delay,extrinsics and torque payload preserved. Big-model inference and CAN/steering/Chestnut health pass. Normal upstream estimator startup differences are recorded without restoring stale caches. [Powered check](../../navigator-reference/PRIVATE_ARTIFACTS.md),[learned preservation](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Normal upstream powered initialization reset stiffness from1.048793to1.000000and refreshed the torque-cache outer timestamp. Core learned steer ratio,average offset,lateral delay,extrinsics and torque payload were retained; no stale cache was restored. Big model measured20.001fps with zero sampled reported drops.
