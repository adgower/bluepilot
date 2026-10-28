<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Calibration update repair — October 23, 2026

**Local repair and full requested replay passed. Nothing on the Comma changed.** The existing paired checkout contains one production change in `openpilot/selfdrive/controls/controlsd.py`, plus regression tests. Parent base e9ddc7668; child d2e8d040 remains clean and unchanged. No push, commit, install, device access, parameter write, OS/firmware update or CAN transmission. Owner1.20/0.97 and all child steering/geometry/safety sources preserved. [Patch](../../navigator-reference/PRIVATE_ARTIFACTS.md), [source hashes](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Repair and engagement proof

The producer now rebuilds calibrated orientation and validity when calibration changes and a motion sample has been seen, as well as on motion updates. Calibration is applied before the rebuild. The original deviceMotion timestamp is retained, and the controller's100ms age limit, finite/health checks, reversed-time rejection and real-fault latching remain unchanged. The disabled coordination path retains its original update cadence.

RED: tests reproduced both invalidity on unchanged calibration-only publication and stale orientation after changed calibration. GREEN:26focused engagement/coordination tests pass, including19new continuity cases. These exercise actual update, PoseCalibrator, publish, Cap'n Proto transport, Car.controls_update/CarInterface/controller, valid moving engagement, independent calibration/motion cadence, simultaneous inputs, missing initial motion, nonfinite/unhealthy/invalid/uncalibrated inputs, stale/future/reversed samples and parent fault latch through actual owner disable/rearm. Transport tests run in a subprocess to avoid contaminating later replay-fork tests. [RED](../../navigator-reference/PRIVATE_ARTIFACTS.md), [final GREEN](../../navigator-reference/PRIVATE_ARTIFACTS.md), [JUnit](../../navigator-reference/PRIVATE_ARTIFACTS.md), [independent review](REVIEW.md).

## Saved sensor replay

All18new and32retained Alpha acquisition files rehashed successfully. Replayed94,980producer updates across the three failed sessions through the real update/publish path. Under publication-time ordering, installed code produces6,990invalid-pose requests; repaired code277, retaining genuine invalid inputs and adding no new invalidity.6,713calibration-only gaps removed. Motion timestamp selection is identical between old/repaired producer. Disabled producer output is byte-identical across every replayed control.

Logger publication order is not exact consumer batching: consumed motion timestamps match the recording on93,360/94,980controls. Therefore each of the five first-fault snapshots is additionally rebuilt from its **exact recorded consumed motion timestamp** and past calibration. All five now yield valid pose with timestamp preserved and no controller fault. That isolated controller check uses fresh synthetic zero-torque feedback, explicitly not physical release proof. [Sensor replay](../../navigator-reference/PRIVATE_ARTIFACTS.md), [input hashes](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Full longitudinal/native regression

Six retained full-stream variants rerun,65,736slots each. Default-off ACC exact parity and all non-ACC hashes retained;36,086inactive/stop/creep excluded packets unchanged. All six streams match their prior integrated hashes. Recomputed-parent/model case:221→65eligible brake edges and zero modeled faults, retaining1,561positive-integral inhibits; frozen/model213→77. These are retained model results, not a new physical smoothness claim.

The changed-command/original-observed-feedback stress case retains27,549faulted slots, unchanged from its prior integrated result. Original actuator feedback belongs to original commands; this incompatible counterfactual is not presented as a successful vehicle-response replay or as evidence to suppress the observed-release fault.

288retained response-uncertainty cases /1,152,000controller updates: zero modeled fault frames,172improved acceleration-RMSE cases and none worse by>10percent, identical to prior integration. These generic lag/coast/release assumptions do not identify real vehicle dynamics, perception, fuel use or road readiness. [Full-stream comparison](../../navigator-reference/PRIVATE_ARTIFACTS.md), [scenario results](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Two native raw-RX/timer ACC replays (frozen and recomputed-parent): each5,260,361RX and65,728ACC slots per variant; three shared recorded/baseline/candidate pedal-boundary rejects, zero added candidate rejects, zero final relay fault and no forced permission. [Frozen](../../navigator-reference/PRIVATE_ARTIFACTS.md), [parent](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Fresh failed-drive native replay

Replayed3,968,773raw RX and108,771all-TX frames across the three new sessions with native safety hooks. Recorded, baseline and repaired variants share10cancel-button rejections (0x83, buses0/2) after cruise already disengaged; no ACC or lateral message rejection in this replay, zero added repaired rejection and no relay fault. Repaired producer inputs eliminate the five baseline controller fault slots while retaining actual recorded owner/demand and exact consumed motion timestamp. All non-ACC messages remain recorded bytes; active requests rebuilt42/65/31per session. No post-fault continued engagement or alternate vehicle response is invented. [Native candidate replay](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The live Panda counters had14Ford increments; native replay reproduces10as cancellation pairs. The remaining four are not exactly reconstructed from logged RX/TX ordering. Do not claim all hardware rejects resolved or zero recorded rejects; later device/parked/road validation must inspect them. The calibration repair does not loosen cancellation, steering, acceleration or safety checks.

## Build, tests and environment

Full parent suite:1,029passed,87skipped,1expected failure and281passing subtests. Ford/native:915passed,79skipped and12,083passing subtests. Focused26tests above overlap other suites; counts must not be summed as independent cases. Ruff, Python compilation and minimal Mac build pass. ARM/Chestnut build and candidate parked/road checks have **not** run for this repair.

The first sandboxed parent run failed because per-test `.comma…` directories under the home folder were blocked; a minimal diagnostic confirms PermissionError, and the full suite passed after permitted private filesystem/IPC access. The first build lacked the checkout's compiler-tool PATH; the retry with existing `.venv/bin` passed. A separate optional type-check attempt found no installed `ty` executable; no type-check pass is claimed. Helper development had a bytes-vs-builder capture error; corrected to match real card output, then the final real-card test and full parent suite passed. Initial failures are retained as logs, not counted as candidate code failures or passing proof.

## Broad lateral corpus / release boundary

The freshly executed retained71-session/1,015-segment native lateral corpus completed in1800.4seconds with no errors, no additional native rejection or RX difference, no protected-band scope change, and no phase/counter mismatch. It compares recorded and causal-fixture variants, native RX/rejections, protected-band/slew/budget/abort behavior and callback phase/counter alignment; it is not a new lateral tune. Current production patch leaves child code unchanged. Fresh AST comparison verifies the replay candidate matches current child semantics except class name/module docstring. [Equivalence](../../navigator-reference/PRIVATE_ARTIFACTS.md). The corpus retains historical reference/candidate rejections; this is a no-added-rejection comparison, not a zero-total-rejection claim. Exact variant totals and232,333,840physical RX frames are in the final receipt.

This remains a **local-only** patch. [Final receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md), [full lateral result](../../navigator-reference/PRIVATE_ARTIFACTS.md). No publication or activation authorized by this request. Keep Alpha off on the installed version until a separately authorized candidate ARM build, backup/install and powered Park acceptance. A subsequent short controlled trial/log review is still needed to establish physical engagement, smoothness, grade/release and restart behavior.
