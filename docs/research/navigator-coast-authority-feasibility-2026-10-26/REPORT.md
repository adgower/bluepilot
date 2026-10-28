<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Coast authority feasibility — 2026-10-26

**Result: not identifiable with the unchanged archived model. No new controller prototype was built or installed.** The approved design's Stage A stop gate applies; this is a completed feasibility investigation, not a highway pulsing fix.

## What the audit establishes

Audited 17,943 source cases from 8 routes (7 with usable cases), across 0.2, 0.4 and 1.0 second horizons: 53,829 case/horizon evaluations. Source case hashes, original extracted-array hashes and archive hashes were verified. Every original case's 154 model inputs was reconstructed exactly from its aligned initial context and command prefix. Route train/calibration/test roles were retained. Previously inspected test-role routes remain development evaluation rather than fresh blind validation.

The original 54 paired coast/brake forecast queries were rebuilt at identical fixture indexes with the same archived model; all stored values match within 1e-12, boolean fields exactly. **43 point forecasts favor coast; zero conservative interval comparisons establish an advantage**, even before adding following-context requirements. This reproduces the earlier uncertainty result rather than selecting a new cohort that looks better.

The old query extraction has no radarState stream: all 54 queries lack the independently received following context required by the new design. This is an additional gap, not the reason the uncertainty gate fails. Recovering radar alone cannot turn those zero conservative advantages into evidence for coast.

## Why “supported” was not sufficient

The archived model's global distance/initial-mode rule calls all 54 comparisons supported. That does not certify coverage for the specific mode, gear and grade.

At 60–70 mph, the **training** split has only the following stable 200 ms command-prefix cases:

| Regime | Training cases |
|---|---:|
| Inactive propulsion, no brake/precharge | 8 |
| Valid negative engine request, no brake/precharge | 2 |
| Near-zero engine request, no brake/precharge | 1 |

All 11 come from one highway route and observed gear identifier 10; the 2 negative-request examples are in the level-gravity diagnostic band. They are not 11 independent road trials. Initial command mode must not be mistaken for a full-horizon steady coast episode or a known controller engineRamp phase.

The current model does not expose enough conditional evidence to distinguish a slight coast/brake choice at highway speed. This is consistent with broad acceleration intervals. At 200 ms, median interval widths are approximately 1.09 m/s² in both previously inspected test-role routes. On original commanded responses, acceleration RMSE is about 0.256 m/s² for OEM and 0.253 m/s² for Alpha; empirical interval coverage is 95.7% and 96.4%, below the nominal 98% residual interval construction. These are descriptive, correlated-case results, not statistical confidence guarantees or validated counterfactual intervals. Reported coverage is for original commands; it does not establish intervention accuracy.

Full joint speed/gear/gravity/prefix tables, sparse flags, support counts, bias, MAE/RMSE, absolute-error quantiles and interval coverage/width are in `original-audit.json`. Train scores must not be promoted over the poorer test-role results.

## Fixture availability and timing

- The newer 62–64 mph downhill trace and independently joined radar context exist, but that route has no aligned response-model/case cache and no matched paired forecast in this archive. Its controller trace is not automatically a usable physical-response model fixture.
- The older 21.39 mph first-divergence comparison is present. The first original fixed-state projection timestamp is about 1.220 ms after the coupled-controller first-divergence timestamp. It is a nearby diagnostic comparison, **not** exact controller-clock/history reproduction.
- The retained full 162-segment replay remains the committed baseline reference. No candidate controller was changed, so no fresh candidate native replay, ARM build or road test was performed for this analysis. The prior low-speed guard remains the exact local pair.

## Concrete next work

First re-extract received engine torque, actual/arbitrated brake torque, RPM/gear, grade/pose and radar from the **existing saved newer routes**, including the downhill regression. Preserve chronological ages and full command history. Determine whether those routes contain enough naturally occurring valid coast episodes in the relevant gear/grade regimes before proposing new data collection. Keep new development routes separate from evaluation and keep the current archived model immutable.

A future separately versioned model may use additional whole training routes and mode-conditioned uncertainty, but must not move inspected evaluation rows into training while continuing to describe them as held out. A successful point fit or nominal support flag is insufficient. Until conservative coast authority is established, do not implement the mode selector or integral back-calculation, extend precharge, weaken braking, substitute forecast clearance, or tune gains against this 15-second recording.

No new drive is required merely to perform that next extraction. Whether targeted additional coast data is needed remains unanswered by the present immutable-model audit. Physical ride comfort, safe following gaps and 75–85 mph response remain unproven.

## Verification and preservation

Contract tests cover sentinel separation, causal lookup and invalid-latest fallback, overlapping/nonfinite/reversed intervals, mismatched histories/horizons, missing/closing lead context, urgent demand, missing roles/hash mismatches, sparse bins and full-prefix transitions. Behavioral RED then GREEN logs are retained. Final counts are in `VERIFICATION.json`.

Source pair remains parent `2ca969e45afee229d7ec5c03c8768e137410c8d1` / child `bcd706d02fd6b8159b1eadcb6b2a56b504f69567`, with 1.20/0.97 unchanged. No paired runtime edit, publishing, device access, setting change, reboot, firmware update or CAN transmission occurred. Research-root pre-existing changes were preserved.

Run with the paired checkout's `.venv/bin/python`:

```sh
python -m pytest -c /dev/null -p no:cacheprovider -o addopts='' -q --confcutdir=docs/research/navigator-coast-authority-feasibility-2026-10-26 docs/research/navigator-coast-authority-feasibility-2026-10-26/test_contracts.py
python docs/research/navigator-coast-authority-feasibility-2026-10-26/evaluate.py
python docs/research/navigator-coast-authority-feasibility-2026-10-26/evaluate.py --screen-only
```

Raw source-rich cases remain private. The new scripts read existing artifacts and write only the new audit directory. `RESULTS.json`, `fixture-availability.json`, `projection-screen.json`, `original-audit.json`, testlogs and the independent review preserve results and limits.
