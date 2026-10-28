<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent review and fixes

Reviewer `/root/review_calibration_integration` reviewed the staged source, timing/baseline state and integration tests without vehicle access or full replay.

1. **P1: unknown opt-in parameter could crash card startup.** The initial staged card read the new key while the registered header was still a separate package artifact. Fixed by including the actual staged `common/params_keys.h` change and by `roll_mapping_opt_in` safely returning false for older native registries raising `UnknownKeyName`. Focused tests cover unknown/default/enabled reads. The actual staged Params C ABI library was subsequently rebuilt, and a real temporary Params store verifies default false plus enable/disable round trips. Original paired library is untouched.
2. **P2: initial IPC stale-release assertion was too broad.** An immediate second call could fail the cadence gate, and clearing the internal term did not establish final release. Replaced with controlled 50ms card calls, first establishing nonzero final mapping difference, then expiring source/state/computation timestamps with fresh receiver context, asserting snapshot rejection/internal zero and final baseline rejoin. The revised pipeline screen passes.
3. No additional concrete core-source issue was reported after registration/timing/release review. Reviewer independently ran the then-current15 integration tests; main agent ran the expanded54 focused tests and broader screens.

Native replay, C++ generation/compilation and pipeline/Params runtime receipts are separate from this review. No full vehicle application build, ECU, firmware, hardware or road validation is implied.
