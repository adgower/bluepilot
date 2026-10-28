<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Activation helper review

Read-only review on 2026-10-27. No critical or important findings in the requested helper adaptation. This is source review, not device activation or powered acceptance evidence.

Reviewed `prepare_activation.py`, `activate.py`, `install_guard.py`, `card-startup-check.py`, `run_activation.py`, `download_activation_backup.py`, `accept_offroad.py`, and `activation-config.json`, against the previously used coordinated-coast staging helpers and the supplied activation requirements.

The config binds the requested transition from parent `df788e02719c05595dab2f980e6fd9fb9e464006` / child `1d29e6e78abcbf5c6a80eb397d80b349c6cca960` to parent `e05e42f43d2907a4f02915a924cfd95a46197e79` / child `5097b993965b2b65ea3fcca7e3769cfa9403d49c`. The swap, recovery, guard, backup-download, dispatch, and passive-acceptance implementations are byte-identical to the corresponding previously used helpers. Preparation adds completed/native evidence identity, clean candidate manifests, inactive validation unit, private backup, disk, offroad/noOutput, and fresh parameter snapshot checks. The Card constructor assertion changes only the imported high-speed implementation to `MidrangeAdmission`.

The installer checks fresh private Mac backup hashes before stopping the service, rechecks install identities and preservation after stopping, retains the whole original tree, and handles failure both before and after moving the original tree into its retained location. Failure recovery restores migration keys and the original install, verifies preferences/calibration before restarting, and deliberately keeps the service stopped if offroad or preservation conditions no longer hold. No reviewed helper adds OS/firmware update commands or custom CAN/ECU queries.

Validation performed locally: all seven Python helper sources compiled without executing them; the fully substituted remote preparation program, including `install_guard.py`, also compiled. AST inspection confirmed newline constants are LF (10), including generated inventory writes and backup receipt writes; remote source/tab escaping is syntactically valid. Reviewed the supplied `VERIFICATION.json` identity and inactive-state evidence; its ARM/native results remain staging evidence.

At review time `activation-helper-manifest.json` had not yet been created. `run_activation.py:3` fails closed until it exists; generate it from the final reviewed helper/config bytes before dispatch. Fresh backup preparation and verification remain operational prerequisites checked by the installer, not outcomes established by this review.

No SSH, source/helper edits, activation, parameter changes, or vehicle I/O were performed for this review. Only this review file was written.
