<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Allocator budget, clearance and integral recovery: local resolution

October 25, 2026. **The constrained bounded-precharge path passes its local integration contracts. Full BP early coasting/release is deliberately disabled, and highway comfort is not proven.** Nothing on the Comma or either paired branch was changed; 1.20/0.97 is preserved.

## What was resolved

1. **Budget bypass/rearming:** nominal brake admission runs independently of the BP proposal. A weak required brake is staged as precharge only within the original signed-demand-area/deadline budget, then commits to actual braking. Micro-crossings cannot restart the budget. A committed brake cannot downgrade to precharge. Rearming requires fresh measured clearance and a continuous eligible positive-intent dwell; override and invalid context interrupt that dwell. Even latched nominal demand with positive net demand has an absolute deadline.
2. **Clearance phase error:** a precharge request is active brake actuation. The old extracted allocator left the observer timing a release while still requesting precharge. The candidate treats brake OR precharge as actuation; the existing release clock starts after both are withdrawn. All torque/sample/freshness/timeout conditions remain unchanged.
3. **Integral recovery:** a precharge-only stage formerly looked like blocked propulsion to the PID, giving different integral behavior from nominal actual braking. Separate phase metadata now preserves signed brake-stage integration without falsifying the actual brake bit. Normal release and propulsion-ramp feedback immediately resume the existing antiwindup policy. No extra recovery hold or recorded-I reset.

See `DESIGN.md` for the exact contract and `allocator.py`, `integral.py`, `experiment.py` for executable local overlays.

## Why this is narrower than the earlier BP comparison

The candidate does not use BP's earlier -0.06 release threshold or its full follow-mode coasting strategy. It keeps nominal release decisions. It also adapts the -0.12 precharge-entry threshold: an already-required weak nominal brake becomes bounded precharge even before that threshold, so the nominal demand cannot disappear behind a higher BP threshold. Strong demand retains nominal actual braking.

This is an entry-stage allocation change, not a claim that the complete BluePilot extension has been ported or the highway accel/brake cycle has been fixed. The early-coasting branch remains deferred because counterfactual release/response evidence is insufficient.

## Rejected approaches retained as evidence

The first authority-aware variant froze positive I growth during all actual braking. Switching fell, but braking time rose sharply: on one route at 60–65 mph, 66.936 seconds became 179.479 seconds. It rectified the feedback/error history and held braking instead of delivering a comfort improvement. A further recovery hold also altered the maneuver integral history. Both are rejected; source snapshots are in `broad-authority-pass/`.

A strict BP-threshold entry implementation barely exercised precharge because nominal actual braking often committed before BP's precharge threshold was reached. `strict-threshold-pass/` retains that result. The accepted entry policy stages existing weak nominal demand within the independent budget rather than changing release or weakening sustained-demand safeguards.

## RED/GREEN evidence

- Old threshold-only allocator fails all five initial independent-budget/rearming tests.
- Old allocator/old integral policy fail the precharge-as-actuation and signed-precharge-integration regressions.
- Additional regression catches downgrading a committed actual brake back to precharge.
- Retained-torque recovery, interrupted clean dwell and positive-net latched-demand tests caught separate rearming/deadline gaps; final implementation closes them.
- A seeded 5,000-step randomized policy check verifies every precharge-only decision has live finite budget, nominal demand, valid eligibility and an active owner.

Final focused suite: **20 tests pass**. Existing actual-controller Ford suite: **157 tests and 20 subtests pass**, with original assertions intact. An initial missing-module run and a test-helper argument error are not counted as behavioral RED evidence.

## Full causal controller replay

Final variant: `combined_bounded_precharge`. All **137 cached longitudinal segments / 401,970 consumer callbacks** are replayed through actual LongControl and CarController. Persistent integral state, actual consumed plan/state matching and causal returned feedback/publication timing are retained. Input caches are SHA-256 checked. The known consumer pose/IPC reconstruction limitation remains.

The invariant and wire proofs require:

- no added fault, loss of active state or changed pedal/owner behavior;
- exact baseline integral, producer acceleration, gas and brake-acceleration histories;
- selected brake OR precharge equals baseline brake demand;
- every changed ACC packet changes only the actual-deceleration bit from 1 to 0 while retaining precharge 1 and inactive gas;
- no changed actual-brake bit during strong consumed planner deceleration at or below -0.5 m/s².

Final verification: **zero added faults, zero integral/producer-request delta and zero strong-deceleration command regressions**. All selected brake/precharge actuation unions, gas and brake-acceleration histories exactly match the current-stack baseline. Only `AccBrkDecel_B_Rq` changes, in 1,879 callbacks across 189 bounded entry episodes / 37.657 seconds. The observed longest stage is 0.324494 seconds including callback quantization. Actual-deceleration-bit transitions across matched five-mph bands change 992→971 and rapid reversals 218→224; these are request-bit metrics, not a demonstrated physical improvement. Propulsion-inactive time is unchanged.

Final counts and native verification are in `RESULT.json`, `invariants.json`, `wire-proof.json` and the native receipts. Candidate output is compared with the current-stack baseline on the same recordings, not presented as reproduction of all historical source versions.

The recent 76 segments retain zero reconstructed coordination faults. The two older baseline reconstructed release faults remain unchanged; this work does not claim all historical ControlsMismatch episodes are fixed.

Precharge has a 300 ms **decision** deadline, with consumer-delivery quantization visible in observed durations (one callback may persist beyond 300 ms). This does not enlarge the original release timeout or promise a physical speed-error bound.

## Native replay provenance

Native debug safety hooks cover all final route inputs/messages without forcing permission or changing RX/non-ACC traffic/timer progression. The budgeted predecessor received a full fresh 137-segment run. Final guard hardening was replayed again through the coupled controller; changed routes received fresh native replay, and only byte-identical route streams reuse prior native results. The final native identity/coverage receipts distinguish these cases: 79 changed-route segments were rerun, 58 exact-wire-identical segments reuse the preceding full native run, and the final absolute-deadline guard revision has byte-identical output across all six routes. Verified final coverage totals 32,171,016 RX / 951,332 TX per variant, with zero added rejection, no relay malfunction and no forced permission. Existing recorded/baseline rejections remain visible; zero added rejection is not zero total rejection.

This is not sanitizer, ARM, hardware delivery, actual vehicle response or road-comfort proof.

## Interpretation and remaining work

Unlike the prior prototypes, the accepted local version contains the budget, release-phase and software-integral integration errors without buying a lower switching score through disengagement or more braking. However, recorded torque still belongs to the original actual-brake commands. The physical ECU response to replacing the brief entry with precharge-only is counterfactual; unchanged software trajectories do not prove unchanged or improved vehicle motion.

The candidate is **not installed or integrated into the paired branches**. Before normal integration, research-only metadata must become coherent, versioned paired IPC fields, including the consumed target and precharge/phase/budget context. Then normal parent/child build, ARM and staging checks are still required. There is no new UI toggle or on-device feature from this task.

Keep full early coasting and the broader highway-pulsing improvement open on the roadmap. This result establishes a locally validated bounded-precharge foundation, not a claim that Alpha now matches OEM ACC.
