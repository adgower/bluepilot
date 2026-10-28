<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator fork versus current upstream master — 2026-10-14

Read-only source/API comparison. No checkout, device OS, firmware, model, or steering changes. Exact references matter: public master was queried through `git/ref/heads/master`, not inferred from global commit search or an unrelated local checkout.

## Exact versions

| Item | Navigator installation / local trial | Public upstream master |
| --- | --- | --- |
| openpilot | Installed Git baseline `f35e6e5eb11ca9cddad3ed945d44d8f191679240` plus documented trial source overlay; local packaged trial `c1bf21f3d` | `690fa743b945973d594f2dfa143eee4fabc98a70`, <private wall-clock timestamp>, UI raylib keyboard check |
| Upstream-related fork ancestor | `20a7bd00b4e50d70f35fcf439e34c4dfcd9f9d06` | API comparison reports diverged: 183 upstream commits ahead, 1 commit behind this fork ancestor |
| opendbc gitlink | Installed baseline `eb70bef4f56d2e9e91cb5a0a8374890a6acfaf51`; local trial `6c17a0afc5abc0ca9f46a1afb823e0238b402f5e` | `b3bd79a659dae961af169a3baac723961f720133` |
| Required AGNOS in launch_env | 19.7 | **19.9** |

Parent agent's fresh SSH observation independently confirmed installed `/VERSION` **19.7**, Ubuntu 24.04.4, kernel 4.9.103, updates paused and prebuilt present. Both Navigator trial settings are enabled, and the controller hash matches the deployment manifest. Installed source expects Chestnut firmware `ed4e39b7`; this is a source expectation, not a fresh physical firmware read. Exact current upstream [USB source](https://github.com/commaai/openpilot/blob/690fa743b945973d594f2dfa143eee4fabc98a70/openpilot/common/hardware/usb.py) expects **`8516b768`**. Git metadata alone does not identify installed source because our trial is an overlay. See deployment report for source hashes.

Primary sources: [live master ref](https://api.github.com/repos/commaai/openpilot/git/ref/heads/master), [exact commit](https://github.com/commaai/openpilot/commit/690fa743b945973d594f2dfa143eee4fabc98a70), [ancestry comparison](https://github.com/commaai/openpilot/compare/20a7bd00b4e50d70f35fcf439e34c4dfcd9f9d06...690fa743b945973d594f2dfa143eee4fabc98a70), [exact dependency](https://github.com/commaai/openpilot/tree/690fa743b945973d594f2dfa143eee4fabc98a70/opendbc_repo).

## AGNOS update implication

The exact-head [launch_env](https://github.com/commaai/openpilot/blob/690fa743b945973d594f2dfa143eee4fabc98a70/launch_env.sh) defaults `AGNOS_VERSION` to 19.9. [launch_chffrplus](https://github.com/commaai/openpilot/blob/690fa743b945973d594f2dfa143eee4fabc98a70/launch_chffrplus.sh) compares `/VERSION` to that value, verifies the manifest, and enters the OS updater when mismatched. Pinning the environment to 19.7 to bypass that flow does not establish runtime compatibility.

Canonical manifest: [openpilot/common/hardware/comma/agnos.json](https://github.com/commaai/openpilot/blob/690fa743b945973d594f2dfa143eee4fabc98a70/openpilot/common/hardware/comma/agnos.json). It contains A/B xbl, xbl_config, abl, aop, devcfg, boot, and system images. System expanded size is 4,718,592,000 bytes; manifest hash `9aebca09b9d142718e71efbfe44b723010eec6e70067c043c63186067291739d`, raw-image hash `80d9373348ddff2a5d1f534fab3420383939c96f3eba60baab6b15339fc602c7`. This identifies requested software, not a download, flash, or OS backup. Both [AGNOS19.8 #38935](https://github.com/commaai/openpilot/pull/38935) and [19.9 #39026](https://github.com/commaai/openpilot/pull/39026) occurred since the fork base.

## Material upstream changes since this fork base

- **Vehicle model/mass:** [Remove car mass #39072](https://github.com/commaai/openpilot/commit/2713630e7950a61dc072467b5394a1043e34547f) changes parameter representation in the estimator and opendbc vehicle model. The port must adapt our fixed pinion guard and verify Python/Panda agreement; mixing normalized stiffness with old mass without conversion breaks that agreement. The original Panda formula can remain algebraically equivalent if conversion is handled correctly. This is not a free steering improvement.
- **Chestnut model distribution/build:** [precompiled eGPU model #38930](https://github.com/commaai/openpilot/pull/38930), [LFS instead of chunking #38941](https://github.com/commaai/openpilot/pull/38941), [precompiled camera warps #38991](https://github.com/commaai/openpilot/pull/38991), and [faster Chestnut build #38656](https://github.com/commaai/openpilot/pull/38656). Model files and runtime dependencies must match the new source; copying only Python is insufficient.
- **Chestnut operation:** [100W default GPU power limit #38992](https://github.com/commaai/openpilot/pull/38992), [wait for enumeration #39011](https://github.com/commaai/openpilot/pull/39011), [timeout fix #39012](https://github.com/commaai/openpilot/pull/39012), fallback checks/drop handling, firmware bump [#39050](https://github.com/commaai/openpilot/pull/39050), and [flash before onroad #39078](https://github.com/commaai/openpilot/pull/39078). New hardware behavior warrants parked validation and rollback planning independently of steering replay.
- **Chestnut CI/distribution:** nightly-chestnut and nightly-chestnut-dev builds, onroad CI, telemetry and fallback tests were added. Upstream coverage is not Navigator-specific proof.
- **UI/runtime and schema:** comparison includes MICI replay/UI changes, `log.capnp`, locationd `car_kf.py` and `paramsd.py`, launch/hardware path changes, package/compiler updates and updater fixes. Preserve the two Comma-four trial controls through UI rebase, rebuild generated/native artifacts, and recheck replay schema compatibility.
- **Panda/opendbc:** the dependency gitlink changes substantially. This report records the exact target but does not claim a complete child-repository safety audit; that is mandatory before porting our pinion geometry and angle checks. Our custom firmware is not proven compatible with that child simply by upstream tests.

## Recommended local upgrade sequence

Create an isolated upgrade candidate at the exact upstream target and port the current paired opendbc/firmware changes with the original 1.20/0.97 map and trial-off path preserved. Reconcile the changed vehicle model before enabling pinion. Validate static/build/schema behavior, full old/new-route safety replay, and >=45mph byte comparisons. Separately establish AGNOS19.9/model/Chestnut prerequisites and a concrete rollback plan. Keep MADS, auto-calibration and new longitudinal candidates out of the initial base-upgrade comparison so any regression has a narrow cause.

Current conclusion: the running device is on AGNOS19.7 and the requested latest master requires19.9; latest-master adoption is a coordinated source/dependency/model/OS upgrade, not a safe assumption that an ordinary pull preserves this installed trial.
