<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator persistent-error prototype — local only

Completed the authorized offline prototype and full saved-input native safety replay. No Comma access, installation, settings changes, active ECU queries or transmission. Existing source checkouts remain clean. User1.20/0.97 factors and installed low-speed feedforward are preserved.

## Design

`persistent_error.py` subclasses the prior report-local bounded P prototype, retaining its update sequence and original range/rate bounds. DefaultOFF. Expedition identity and both pinion/low-speed flags required. Correct only5–25mph, full weight through15mph, smoothly zero by25mph. It uses fixed-model pinion curvature, not biased raw yaw or learned ratio/offset.

Admission requires11 consecutive20Hz eligible samples (0.5s span), same request direction, absolute request>.001/m, request range≤25% of median absolute request and speed range<0.5m/s. Measured curvature must have the request sign (zero allowed) and magnitude<70% of requested for six consecutive stable observations. First possible admission is update16 (0.75s since initial eligible sample). Invalid CAN/steering fault, driver input, inactivity, reversal, unsupported configuration or speed exclusion resets admission. Recovered response or unstable demand clears hold and correction/filter while retaining the rolling sample window.

Admitted feedback retains Kp0.5,0.30s filter, cap min(0.015rad,25% of feedforward), before original DBC range and speed-dependent slew limits. No integrator, extra global lag, EPS-bit override, request pulse or safety-limit expansion. Thresholds are experimental sensitivity choices, not identified vehicle calibration.

The strategy receives CarState/CarControl, not model lane-change state. It does not replicate the earlier diagnostic classifier's separate model lane-change gate or timestamp-age gate. Driver input is excluded; freshness must be provided by the calling pipeline. Therefore prior classifier frame counts are not interchangeable with this causal controller's counts. A deployable design would require a deliberate plan for stale data and lane-change context.

## Verification

-24 behavioral tests passed; meaningful RED against immediate ungated feedback had5 failing/5 passing tests, followed by GREEN and added boundary/regression coverage.
- Ford controller/native safety suite:213 passed,79 skipped,12,063 subtests passed. Skips are recorded, not passing coverage.
- Five complete cached drives,72 segments:410,939 controller updates;16,377,999 physical RX frames per independent hook. Native debug library and prototype hash recorded in `provenance.json`.
-244,093 generated TX total;1,843 before Ford configuration excluded from acceptance claims. All242,250 configured generated TX accepted; zero rejections and zero invalid required RX. Recorded controls permissions used without forcing them allowed.
- DefaultOFF entire generated stream byte-identical. Candidate changed310 generated-update streams, all below25mph. All50,567 generated messages at≥25mph and12,425 at≥45mph byte-identical to current installed-strategy baseline under recorded inputs.
- Latest persistent event105.43–107.43s:35/40 angle commands changed, maximum encoded difference0.015rad. Later510.48–512.48s catch-up event:0/40 changed. These are encoded command comparisons, not measured corrected response or admission percentages.

`summary.json`, `full-replay.json`, full log and command comparisons preserve evidence. Existing range/rate history is retained: instantaneous synthetic speed jumps can briefly retain corrected output history above the fade cutoff even though the added term is zero. Recorded high-speed parity does not establish universal parity for arbitrary state jumps.

## Limits and next decision

96 hypothetical independent-feedback gain/lag/delay scenarios retain identical45mph commands. Assumed50% steady response improves only to about60%; worst unit-gain peak remains1.1907×reference (about19% overshoot). These are uncalibrated toy plants, without full planner feedback, and do not prove actual vehicle improvement or safe deployment. Persistent gating reduces when correction is attempted; it does not establish the cause of15mph weakness or solve every delayed-response case. No road fix, EPS authority map or deployment readiness claimed.

Before device testing: address stale/lane-change context, inspect overshoot sensitivity and justify admission/caps with additional clean recorded response. Keep the current installed candidate unchanged meanwhile.

The [Start/Stop evidence package](../navigator-autostop-button-evidence-2026-10-14/README.md) separately preserves passive status observations and missing-request limitations for later work.

## Reproduction

Use `${USER_HOME}/Apps/openpilot/.navigator-master-integration-20261014/.venv/bin/python` with `run_tests.py`, `full_replay.py` and `synthetic_screen.py` here. Native Ford wrapper is the prior report's `run_ford_tests.py`, run from pinned `opendbc_repo`. Private cached input paths are in extraction/replay scripts; portable manifests identify segments by anonymous labels and hashes. Both report-local prototype modules are dependencies; pinned source parent76d78d46fc8713f2f6b1147af02e5aed07bf15a1 / childf50241ca59d866af275ff6c34fb407b93094e892. No source selector was edited.
