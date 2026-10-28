<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Coordinated coast/brake and integral recovery — local prototype

Authorization: user requested local prototyping, resolution of weaker braking and extra exposure, then full replay. No paired integration/device action. Preserve 1.20/0.97 and installed pair1dbbc0189/beb10c25.

Hypotheses ranked: (1) consuming the weak allocation deadline before any precharge decision loses useful allowance; (2) the added independent coast-admission state changes propulsion/anti-windup history; (3) the numerical engine-ramp authority margin creates delayed integral crossovers. Existing failing traces already establish (2)/(3).

Prototype approach: remove the rejected extra admission override. Make the existing single precharge allocator's deadline begin only when a nominal weak brake is pending, rather than on any negative net crossing during reference coast. Preserve its signed area, deadline, commitment, measured-clear recovery, owner/invalid-input and strong-braking fallbacks. Use truthful existing bounded-precharge feedback and its signed-braking integral role; do not create an integral debt, copy baseline I or run a baseline controller inside the candidate. This tests whether the existing correct brake/precharge role avoids the rejected true-coast integral divergence.

This is coast-ready precharge, not proven zero physical braking. Full brake and precharge still withdraw propulsion and wait for real clearance. Do not claim relief of gas withdrawal or physical highway pulsing from fewer full-brake bits alone.

1. Failing allocator-entry/deadline test plus integral-role equivalence test.
2. Small local allocator prototype and complete new-drive replay; inspect named windows and feedback correctness.
3. Full216segments /13routes against current installed reference, including first prior producer crossover and all city/restart/strong-braking fixtures. Exact raw/I/gas equality is the desired result; no new timeouts, retained-pressure gas or weaker braking. No extra full-brake exposure and no increase of combined brake/precharge exposure.
4. Native safety replay with original RX/timers/non-ACC TX, contract tests, source/hash validation and roadmap/report. Keep12segments with missing active prefix inputs diagnostic-only.

Alternative: widen admission and add integral repayment. Rejected because it repeats independently changing propulsion authority and requires a counterfactual recovery account. A broader delivered-authority/PID redesign remains a future option if the narrower coordinated signed-braking role fails. No installation is implied by successful replay.

## Final design refinement

The early-start-only variant is rejected: it ignores legacy admission deferral before nominal brake arrival. The zero-debt recovery-only intermediate variant also retains the old accounting of delivered full braking as debt; a focused test rejects that accounting.

Final coordinator3 retains the original negative-net start, including earlier legacy coast deferral. Its existing ledger charges negative demand during legacy deferred entry or prospective weak precharge, retains already accumulated debt during delivered braking, and accepts positive net credit. Delivered full/strong braking does not create additional omission debt. No new budget/debt account or I repayment is introduced. The wall-time trial deadline stays0.3s; the demand-area allowance stays0.01. A new trial requires the ledger to be exactly zero plus100ms of continuous eligible, measured-clear, nominal-off, positive raw/net/target context (instead of old500ms that could also erase an unpaid ledger). This is sampled decision-demand accounting, not a continuous physical speed-error bound.

Signed braking/precharge feedback retains the existing identical native integral role. Gas and combined brake/precharge requests should remain exactly equal to reference. Raw/I equality and no-extra-exposure gates remain mandatory in the full saved replay. Keep early/intermediate variants and their red tests labeled superseded rather than advertising their favorable isolated metrics.
