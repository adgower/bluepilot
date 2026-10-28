<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator paired candidate: isolated device build and offline replay

Status: device build, native tests and full offline replay passed. The candidate is staged, not activated.

## Exact source and boundary

- Candidate parent `0cc74c94f3c6dafa3790c303be9ef345878bd792`, opendbc `d64ffcfa4e4a7556151962ca304d223a0a323375`, paired branch `codex/navigator-tracking-release`.
- Separate device directory `/data/navigator-validation/<private timestamp identifier>-0cc74c94f/source`.
- Active parent remains `74f66e7a0bf1dc0718431532948ece2c4fb0041c`, opendbc `1b965caadd4a6aea4d09985532bf7cca6c0873ca` at `/data/openpilot`.
- Preserve owner 1.20/0.97, all live settings, active service and firmware. No activation, reboot, ECU queries or live CAN transmission is part of this job.

Source was cloned into new repositories with read-only borrowed objects, then checked out at the candidate commits. All 262 LFS files were hydrated only after matching their committed object hashes and sizes. The uploaded archive SHA-256 was `ecd1487780a9cd2cb9edaa756136311f194176f9a1892ffb48288b39559e2351` (737,515,520 bytes), including all 89 saved segments. Later isolated-runner compatibility revisions are separate from the candidate source.

## Execution isolation

A dedicated transient unit `navigator-validation-<private timestamp identifier>-0cc74c94f.service` owns only validation processes. Runtime properties checked: `KillMode=control-group`, `SendSIGKILL=yes`, `TimeoutStopUSec=10s`; active watcher PID 70578 at build start. Root watcher performs read-only live snapshots and resource/offroad monitoring. Candidate processes run as comma with zero effective capabilities and kernel-verified no-new-privileges, at nice 10 / I/O priority 7.

Private mount/network namespaces make the active data tree read-only to the job while its stage remains writable. Parameters, cache, home, logs, tmp and shared memory are private. USB is hidden; existing SPI/GPIO/serial/Panda nodes are replaced with `/dev/null`. The fresh network namespace has only down loopback/default tunnel interfaces and unreachable routes. Native safety replay uses a newly compiled in-memory C library; it does not instantiate vehicle interfaces or publish CAN.

The first probes stopped before compilation due to unsupported PID namespaces and kernel-specific network/proc fields. A dedicated systemd cgroup replaces PID-namespace teardown; down default tunnels and unreachable kernel routes are explicitly checked, and `prctl(PR_GET_NO_NEW_PRIVS)` replaces the absent proc status field. Active source, selected settings, manager/service identity and all parameter hashes were unchanged after stopped probes. The final isolation probe passed before build started.

Watchdog stops only this job if `IsOffroad` is no longer 1, available memory falls below 450 MiB or data free space falls below 2.5 GB. It does not stop or restart the installed application.

## Checks and limitations

Full device `scons -j1` passed (including Qualcomm model compilation and staged Panda images). Native device tests passed: **277 passed, 79 skipped, 12,063 subtests passed** in 95.46 seconds. The test-only pytest dependencies are private staged pure-Python copies from the local validation environment; installed Python packages were not changed. An initial wrapper used an invalid capnp import and was corrected before replay. A redundant rebuild retry was stopped and the original successful full-build receipt/log retained (the private top-level `evidence/build.log` is that canceled retry; the successful original is `evidence/attempt-replay-import/build.log`); replay uses the built staged Python bindings and its separately compiled native safety library.

The complete six-drive / 89-segment ARM-native replay passed and its full result JSON is exactly equal to the Mac reference, including per-drive command hashes, counters, rejection records and comparison results:

- 20,227,501 physical RX frames processed in memory.
- 322,306 configured candidate TX accepted, **zero rejected**; baseline reproduces one rejection.
- All 89 input hashes verified before replay.
- Option OFF is byte-identical to the feedforward reference at every generated update.
- Generated actuation packets from recorded inputs at ≥25 and ≥45 mph are byte-identical to baseline. Metadata traffic intentionally differs; whole-stream baseline parity is not claimed.
- Replay-only retry completed in 2,047.50 seconds including the native tests. Minimum available memory was 1,895,702,528 bytes; minimum data free space was 9,461,530,624 bytes. Original full-build minimum available memory was 1,431,687,168 bytes. No resource threshold was hit.

[Summary](../../navigator-reference/PRIVATE_ARTIFACTS.md), [full replay](../../navigator-reference/PRIVATE_ARTIFACTS.md), [build receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md), [successful full-build log](../../navigator-reference/PRIVATE_ARTIFACTS.md), [source verification](../../navigator-reference/PRIVATE_ARTIFACTS.md), [preservation receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md), and isolation receipts accompany this report. The native ARM safety library uses `ALLOW_DEBUG` without sanitizer, matching the reference safety-build mode; its binary hash naturally differs from the Mac library.

## Installed state after validation

Both active repositories remain clean at their original commits. Active path, selected options, controller/geometry source and Panda-image hashes, manager process identity and existing service start identity compare equal. Of 66 parameter-file hashes, only normal running-service counters `LastAthenaPingTime` and `UptimeOffroad` changed. No settings/calibration changes were observed. Staged child has no tracked changes; all 262 hydrated LFS files retain their expected hashes. Parent Git status lists those hydrated files because the new clone does not inherit the installed repo's LFS clean-filter configuration; there are no other tracked-source differences.

A final 15-second passive check on the original installed software passed: 151 Panda samples remained `noOutput`, ignition off, controls disallowed, no RX-invalid/fault/heartbeat-lost reports; historical TX-blocked count stayed at 6. Owner factors are 1.20/0.97; no expected running process was unexpectedly stopped. Powered stationary validation was not performed (vehicle stayed off).

The transient validation unit ended `inactive`, `Result=success`, `ExecMainStatus=0`, with no remaining main process. The stage is retained. Private detailed evidence, logs and passive snapshots are saved at `${USER_HOME}/CommaBackups/20261015T0827-staged-build-offline-replay`; raw drive logs remain private on the device stage. Final helper checksums match the retrieved device scripts.

Even a successful offline replay cannot establish live EPS behavior, metadata arrival timing on the physical bus, vehicle response or safe road handling. No candidate hardware actuation is authorized by this validation request.
