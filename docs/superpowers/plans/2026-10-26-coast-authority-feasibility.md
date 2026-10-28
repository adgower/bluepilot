<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Coast Authority Feasibility Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Determine whether saved OEM/Alpha data supports conservative, causal coast decisions before implementing a new coordinated controller policy.

**Architecture:** Read immutable response-model archives and hash-bound cases, reconstruct coast regimes, and measure support/error/interval coverage by route, mode, gear, grade and speed. Evaluate paired coast/brake command projections without changing the controller. A failed feasibility gate stops policy work; a pass supplies measured bounds for the conditional policy stage of the approved design.

**Tech Stack:** Python 3.12 from the existing paired checkout `.venv`, NumPy/SciPy, pytest, JSON and existing private NPZ/pickle fixtures; no dependency installation.

**Spec:** `docs/superpowers/specs/2026-10-26-coordinated-coast-integral-design.md` (approved by owner 2026-10-26).

## Global Constraints

- Preserve steering, 1.20/0.97, Navigator geometry and the selected narrow low-speed guard.
- Baseline parent `2ca969e45afee229d7ec5c03c8768e137410c8d1`; child `bcd706d02fd6b8159b1eadcb6b2a56b504f69567`.
- No push, SSH/device staging, install, settings change, reboot, firmware or CAN transmission.
- Reuse existing route split roles; previously inspected routes are development/regression evidence, not new blind validation.
- Never interpret inactive gas=-5 as delivered acceleration or a forecast as physical brake clearance.
- Stage A is research only; do not edit paired runtime or change/retrain the archived model to manufacture support.
- Preserve existing dirty research checkout; write only new allowlisted research files and scoped roadmap updates.

## Review Focus

- Inactive sentinel versus valid zero/negative engine requests must remain distinct.
- Future state, torque, grade, gear or lead samples must never enter causal decision inputs.
- Low-count strata or missing lead context must not silently become supported clear-road operation.
- Whole-route roles and original model hashes must survive every analysis step.
- Overlapping uncertainty or zero interventions must be reported as inconclusive, not a pulsing improvement.

---

## Files and evidence

New research directory `docs/research/navigator-coast-authority-feasibility-2026-10-26/` (called `P` below):
- `contracts.py`: pure mode classification, causal lookup, strata and interval comparison.
- `test_contracts.py`: synthetic boundary and leakage regressions.
- `evaluate.py`: hash verification, immutable model predictions, calibration/support report and projection screening.
- `RESULTS.json`, `REPORT.md`, `VERIFICATION.json`, test logs: reproducible outputs, provenance and limitations.

Read-only dependencies:
- `docs/research/navigator-coast-release-response-model-2026-10-24/{features.py,response_model.py,probability.py,case-manifest.json,split-manifest.json,model-archive.json}`.
- `.navigator-response-models/20261024-coast-release-v1/` immutable archive.
- Original private case/aligned caches identified by manifests; inspect availability and hashes before loading.
- Integrated 162-segment replay manifest and recorded projection fixtures from the rejected point-forecast experiment; never overwrite either.

## Task 1: Causal audit contracts

**Interfaces:** `classify_mode(brake: bool, precharge: bool, gas: float) -> str`; `at_or_before(rows, now_ns: int, max_age_ns: int) -> tuple | None`; `strict_interval_advantage(coast: tuple[float,float], brake: tuple[float,float], target: float) -> bool`.

- [x] Verify paired pins/clean state, model/case manifests and archive hashes; record unavailable inputs without substituting other drives. CodeGraph unavailable in this harness; use exact known source files.
- [x] Write failing tests: brake dominates precharge; inactive -5 differs from valid0/negative request; nonfinite input rejected; causal lookup rejects future/stale samples; interval overlap returns false; disjoint intervals do not imply advantage if the coast interval has worse worst-case target error.
```python
def test_command_and_interval_contracts():
    assert classify_mode(False, False, -5.0) == 'inactive_propulsion'
    assert classify_mode(False, False, 0.0) == 'valid_engine_request'
    assert classify_mode(False, False, -0.1) == 'valid_engine_request'
    assert not strict_interval_advantage((-0.2, 0.2), (-0.1, 0.1), 0.0)
    assert strict_interval_advantage((-0.01, 0.01), (0.2, 0.3), 0.0)
    assert at_or_before([(101, True, {})], 100, 150) is None
```

`at_or_before` consumes sorted `(timestamp_ns, valid, payload)` records; selects the latest record at/before now and returns it only if valid and within age. It must not skip an invalid latest record to reuse an older valid one.

- [x] Run isolated pytest with `-o addopts='' --confcutdir=P`; retain behavioral RED log.
- [x] Implement only pure contracts. Conservative advantage means the greatest absolute target error anywhere in the coast interval is strictly less than the smallest absolute target error anywhere in the brake interval. Nonfinite/reversed intervals return false.
- [x] Run tests and retain GREEN. Do not encode vehicle permission in any result.

## Task 2: Original-command support and uncertainty audit

**Interfaces:** `evaluate_original(manifest_path: Path, archive_path: Path) -> dict`; uses Task1 classification. Produces route/split/horizon/stratum case counts, support rates, acceleration interval widths and coverage, bias, MAE/RMSE, and absolute-error quantiles.

- [x] Add failing tests for role preservation, source-hash mismatch, count conservation across disjoint speed bins, missing gear/grade and sparse strata.
- [x] Evaluate unchanged archived model on original cases at0.2,0.4,1.0s. Keep train/calibration/test reports separate; call test-role data previously inspected evaluation, not blind validation.
- [x] Use5mph bins0–85, observed gear identifiers plus missing/unknown, and gravity bands `<-0.1`, `[-0.1,0.1]`, `>0.1`m/s². These are diagnostic strata, not runtime tuning or physical slope truth. Report horizons and counts even when empty.
- [x] Report stationary original command prefixes separately from transitions. Do not equate initial command-mode support with full-horizon mode support. Retain all calibrated intervals, including poorly covered/sparse bins; do not narrow or recalibrate them in this task.
- [x] Verify per-route/bin count reconciliation and rerun tests; record model and input hashes before/after to prove immutability.

## Task 3: Conservative paired-command feasibility screen

**Interfaces:** `screen_projections(projection_paths: list[Path]) -> dict`; reads existing projection schema and applies Task1 interval comparison to each valid paired coast/brake acceleration forecast.

- [x] Add failing tests for missing comparison arms, unsupported forecasts, mismatched initial histories/horizons, nonfinite intervals and missing/stale lead context.
- [x] Reproduce the previous54-snapshot overlap result using the original fixture identifiers and unchanged archive. Report any reconstruction mismatch rather than silently using a different cohort.
- [x] Locate the downhill62–64mph fixture and21.39mph first divergence in existing cases/projections. Report explicit availability/support gaps; do not claim a matched forecast where no causal projection exists.
- [x] Screen paired commands only when identical initial state/history and declared hypothetical command prefixes are available. No future recorded physical inputs enter candidate prefixes. Report support, conservative advantage and exclusions separately from road performance.
- [x] For follow-context screening, join only valid backward-looking radar messages <=150ms old, preserving actual leadOne.present. Missing context is unavailable. A forecast screen cannot by itself certify safe following margins.
- [x] Feasibility result must be `not_identifiable` if no conservative supported comparison survives; `research_support_found` otherwise, with exact query IDs and limitations. The latter is not permission to integrate or install, nor a physical performance guarantee.

## Task 4: Evidence review and conditional next stage

- [x] Run all new tests; verify no paired source changes, exact pins and unchanged1.20/0.97.
- [x] Obtain one fresh read-only whole-result review (native execution workflow) focused on causal leakage, uncertainty, cohort identity, missingness and overstated conclusions.
- [x] Write results and scoped roadmap update. Keep raw/source-rich traces private and report inspected-route limitations and75–85mph evidence gap.
- [x] If `not_identifiable`, finish StageA with the precise missing support/data requirement; do not implement the selector/back-calculation experiment.
- [x] Not applicable (StageA gate failed): if `research_support_found`, use the measured bounds to write the conditional research-policy execution steps: baseline/consumer-only/integral-only/coordinated ablations, full downstream integral/strong-braking comparison, unchanged clearance/budgets, then full162-segment/native/build checks only if early gates pass. Do not invent those bounds before StageA.
- [x] Research docs/scripts remain separate from paired runtime. Any local research commit uses an explicit allowlist only; no broad staging of the dirty root. No publishing/device operation.

## Self-review

The approved design is intentionally divided at its feasibility gate. StageA tasks cover source provenance, causal mode distinctions, uncertainty/support, conservative comparisons and truthful stopping conditions. StageB remains conditional because authority representation, numeric bounds and feedback policy depend on StageA measurements; this plan does not pretend those values are known. No controller implementation is authorized by a positive forecast score alone.

## Execution result

Completed2026-10-26 using native execution. StageA result:not_identifiable; StageB correctly not implemented. See [report](../../research/navigator-coast-authority-feasibility-2026-10-26/REPORT.md).52tests and independent result review passed; paired runtime/Comma unchanged.
