<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# City coast/brake handoff prototype — October 26, 2026

**The first local prototype was implemented and rejected for integration.** It does not reduce the 17 city brake changes, does not reduce the named highway episode's 20 changes, and adds stronger-demand command regressions. Neither paired branch nor the Comma was changed. The earlier highway work is still part of the investigation, not superseded by the city episode.

## What causes the city switching

The target is the 37.5-second stretch at about <private clock time>–<private clock time> Central, median speed approximately 25.3 mph, MAX 35, with a lead ahead. Reconstructed all 17 software brake transitions from the installed baseline. Every transition occurs while the finite precharge allocator is in `budget_reference`; its finite entry assistance is already exhausted. The system therefore returns to nominal admission/release, rather than sustaining a coast decision.

The grade-adjusted request repeatedly crosses the brake admission/release boundary as the model target, integral and mapped pitch/grade term change. Most transition targets are small, including positive targets at several brake entries. While actual braking is commanded, signed integral continues adjusting the request. After the brake bit withdraws, received pressure still has to clear, then propulsion ramps. Two short unbraked intervals never deliver a valid propulsion request before braking resumes. Thus a brake-bit transition is not automatically a physical gas/brake cycle.

There are also 59 consumer trace rows in this window whose producer context has a negative planner target, positive wanted request and positive error while returned feedback is limited and not actual braking. The existing anti-windup exception permits integration when the planner target is negative. This suggested a targeted hypothesis, not proof that the old behavior is erroneous: signed brake recovery may need that correction. The failed prototype below is why this is not declared a fixed calibration bug.

## Prototype and preservation

`policy.py` tests a command-domain anti-windup extension only for moving PID at/above 3 m/s, negative planner target, positive unattainable request/error, and fresh current-owner protocol 1 feedback explicitly in `release` or `engineRamp`. Actual-brake/precharge control, signed negative-error recovery and the selected below 3 m/s guard remain on the original path. Inactive gas −5 is handled as a mode marker, never a numerical acceleration bound. No brake permission, pressure-clearance rule, planner target, gain, rate limit or coast budget changes.

This is an isolated research import seam used only by offline subprocesses. It is not ported into opendbc or openpilot. Forty focused tests passed after a genuine five-failure RED regression. Those passes prove the proposed contract, not that the proposal improves driving.

## Installed versus local baseline must stay separate

The recordings use installed parent `5b301a944` / child `884c9f491`. The current local pair `2ca969e45` / `bcd706d0` already contains the separate below-6.7mph guard. That prior change can affect later integral history, so comparing the new prototype directly with recorded output would mix two changes.

The installed-source integral function was loaded from the exact old child commit for diagnosis. Its 73,279 recomputed producer raw/integral updates across the 14 new segments agree with recorded values within 1e−5. Brake bits reproduce the city episode. There remain 36 gas/reason feedback differences following a one-callback early observed-clear decision, without a brake-bit difference. Restricting CAN lookup to the latest state publication did not remove it. The exact receive-drain boundary is not logged; no arbitrary timestamp shift, recorded-integral reseed or synthetic pressure clearance was introduced to force a match.

## City and highway results

All figures below are frozen-response controller replay, with recorded motion, torque, planner and driver response unchanged. They are not physical ride-comfort or stopping-distance measurements.

| Comparison in the city window | Brake changes | Brake-command exposure | Valid-propulsion-request exposure |
|---|---:|---:|---:|
| Installed baseline | 17 | 21.538 s | 14.594 s |
| Same handoff prototype on installed baseline | 17 | 22.671 s | 13.661 s |
| Current local pair, including earlier low-speed guard | 7 | 32.045 s | 5.041 s |
| Prototype added to current local pair | 7 | 32.142 s | 4.926 s |

The standalone experiment reduces peak stored integral (about 0.458 → 0.355), but **does not reduce the cycling and increases braking exposure**. It is not a smoother result. The local pair's seven rather than seventeen changes also cannot be called an improvement: it commands much more braking in this frozen trace. This is new evidence to resolve before staging the earlier low-speed candidate, not proof that it would produce those exact physical outcomes on the road. The local candidate is retained unchanged; it was not silently reverted.

In the named 15-second 63 mph highway regression, the prototype stays at **20→20 changes**, with only a small redistribution between braking and propulsion. Highway smoothing is therefore not proved improved by this policy.

## Broader controller replay and rejection gate

Compared the current local pair and prototype on **176 segments / 10 routes / 512,066 controller callbacks**: all 162 retained segments plus 14 new city segments. Both sides use the same state-publication visibility assumption and causal returned software feedback. A source audit found five active producer updates without complete atomic inputs at the start of one retained highway route; these use the recorded control payload fallback. The newer city routes and named highway fixture have no active missing-atomic updates. Do not describe the entire corpus as perfectly reconstructed initial state. All 441 encoded stronger-target regressions below occur in other routes with complete active atomic coverage, so they do not depend on that retained-prefix gap.

- Common active, pedal-free brake changes increase 1,193 → 1,196.
- **441 encoded total-brake acceleration values become less negative under target acceleration ≤ −0.5 m/s² while the brake bit is commanded.** Maximum difference 0.0312 m/s². Raw-request differences affect 1,406 such callbacks. This is a new command-history regression, not a measured stopping-distance result. The earlier accepted 27 one-increment differences for the low-speed guard do not authorize it.
- No changed disabled-owner wire packets, commanded gas under brake/precharge, or moving-PID gas with retained received torque in the checked replay.
- Two previously reconstructed retained release faults remain. One fault time shifts about 62 ms later, producing three additional active callbacks; this is disclosed rather than counted as smoothness or asserted hardware correctness.

A one-state-cycle CAN-availability sensitivity experiment on the two new routes plus the named highway route (29 segments / 83,201 callbacks) still fails: city 7 → 7, highway 22 → 22 under that hypothesis, and 44 encoded stronger-target regressions. Source CAN timestamps are unchanged; only availability is delayed. This is a timing sensitivity scenario, not proof that the actual hidden receiver delay equals one cycle.

**Do not integrate or install this prototype.** Native firmware replay, ARM build and hardware tests were not run after its controller/comfort gates failed. No existing native result from another candidate is borrowed for these changed packets.

## Where the previous highway investigation stands

The earlier recovery found 34 OEM highway coast episodes, 10 lasting at least 600 ms and eight in the negative-gravity-proxy band, with received torque/gear and fresh radar. Those remain useful inputs for a **separately versioned** response experiment, not a trained coast model or validated policy. RPM quality is still unresolved; old calibration/test roles were not moved or relabeled as new blind validation.

The city result reinforces the same architectural requirement as the highway work: a mode decision must distinguish engine-coast capability from friction braking, and coordinate integral recovery with actual delivered authority. Another integral hold or a larger precharge budget alone is not supported by this result. The next meaningful prototype needs that response-aware allocation model and must include both the city fixture and the existing highway regressions. No new road collection is requested by this experiment.

## Artifacts and scope

`fixtures.json`, `diagnosis.json`, installed replay receipts/mismatch detail, `policy.py`, focused RED/GREEN logs, full comparison JSON, standalone/sensitivity comparisons and private full traces preserve the evidence. New inputs were extracted from the hash-bound saved 14 segments; no device access occurred. Main paired code, calibration, wheelbase/mass, safety code and steering 1.20/0.97 remain unchanged.
