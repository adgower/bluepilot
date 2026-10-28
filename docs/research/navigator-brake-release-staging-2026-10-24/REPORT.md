<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Brake-release staging — October 24, 2026

Authorized scope: publish exact paired branches, fresh backup, separate device staging, ARM build and passive parked acceptance. Candidate remains inactive; no service restart, reboot, OS/firmware update, preference write or CAN/ECU command is part of this task.

## Published pair and current installation

Both GitHub heads verified on `codex/navigator-tracking-release`: parent `064e086d2dc4e724df007fa66953d4f7e48f0141`, child `50719b1ef987d6582e85c417adb452f098b850cb`. The Comma remains on parent `fe08ede1af29a9c37b0c8b3550ce66cbd9392348`, child `d2e8d0404143da0f2685c2ff4932b9b9f702951f`, AGNOS20.1 slot_b.

## Backup and isolation

Fresh device backup `/data/navigator-backups/<private timestamp identifier>-pre-brake-release`; private verified Mac copy `${USER_HOME}/CommaBackups/<private timestamp identifier>-pre-brake-release`. Archive843,623,530bytes,147manifest members checked; both nested source archives read fully.69parameters captured with firmware, launchers and source hashes. Offroad preferences Alpha1, coordination1, DisableUpdates1 retained.

Candidate staged at `/data/navigator-validation/<private timestamp identifier>-064e086d2/source`.253LFS assets hydrated only after committed size/OID checks.83protected child files match both versions;3candidate paths match exact new commit. Independent review verified manifests against commit blobs and found no helper blocker.10local acceptance-helper tests passed.

The transient validation unit mounts active source read-only, uses private params/cache/log/home, blocks networking and listed vehicle interfaces, drops privileges and aborts for low memory/disk or loss of offroad state. Probe/build/replay phase receipts, exit codes and preservation hashes determine acceptance.

## Parked evidence

Ignition-off current-stack observation:55.01seconds,551Panda samples, no issues; historical blocked-TX count15 did not increase. This observes the currently installed stack, not candidate actuation. First offroad-helper invocation occurred before backup inventory existed and exited; log retained, successful run repeated after backup completion.

ARM acceptance passed: full aarch64 build, **1,010 native/Ford/context tests +12,083subtests**, **40 actual admission comparisons**,14parent smoke tests and1pose/engagement regression.79native and6parameterized-base smoke skips recorded. All phases exit0 in1,146.92seconds. Isolation and active-source/settings/manager/service preservation receipts pass; only volatile LastAthenaPingTime/UptimeOffroad hashes changed. Staging finalization passed: both staged repositories clean, Git objects self-contained and firmware/prebuilt marker retained after the full ARM build. Candidate remains inactive. Powered Park acceptance **passed**:55.009seconds,550Panda samples,5,499carState/5,498control samples, no faults or new blockedTX (current count0),20.0001Hz model with zero frame drop,1,100/1,100healthy pose inputs (max observed age38.60ms). Alpha0 and assistance disengaged confirmed. Final source/hash audit passed: active and staged paired trees clean, exact gitlinks and owner1.20/0.97 in both sources. Active source/firmware/launcher hashes and13owner setting values preserved; only owner-requested Alpha-off/ignition state differs. LiveParametersV2,LiveTorqueParameters,LiveDelay andCarParamsPersistent hashes changed across ignition startup; these learned/cache parameters were not manually written or restored. Candidate remains inactive. Physical brake-release resolution is unproven; recorded old-response timeout remains in local replay. Candidate hardware control behavior and road smoothness are not established by build/offline tests or observation of the old active installation.
