<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Downhill cycle and rolling restart investigation — October 26, 2026

## Outcome

The new drives can be reproduced by the installed controller locally. This provides an exact software regression for the downhill switching and identifies a low-speed anti-windup eligibility gap during the rolling restart. A narrow research prototype reduces the stored correction in the isolated restart, but **is not ready for integration**: broader controller replay finds a small later strong-deceleration command-history regression. Neither paired branch nor the Comma was changed.

The OEM/Alpha shift comparison also revises the initial protocol hypothesis: the inactive acceleration-prediction field is not sufficient to explain the unusual high RPM. Other Alpha starts using the same fields request second gear at ordinary low speeds. The exceptional event is a late **reported target-gear selection**, rather than an extraordinary target-to-actual shift-completion delay.

## Recorded baseline reproduction

Extracted atomic state/control/plan/PID/pose/torque streams from the two active new-tune routes (25 segments). Full chronological reconstruction uses the real LongControl, CarController, pose refresh, measured torque and causally published returned feedback. Every one of 70,291 callbacks matches recorded brake, gas, fault and reason; all 131,258 recomputed producer acceleration/integral updates agree within 1e−5. No baseline faults. No recorded integral reseeding, synthetic clearance, future torque or forced permission is used.

This verifies the software inputs/decisions in these recordings. Replayed vehicle motion, gear and torque response remain frozen; changed commands cannot establish changed physical response.

## Why precharge does not rescue the downhill cycle

In the 15-second 62–64 mph episode near <private clock time> CDT:

- All 751 reconstructed callbacks are active and pedal-free. There are 20 actual-brake on/off changes, about 9.914 seconds commanding actual braking and 11.653 seconds with propulsion inactive.
- The allocator reports `budget_reference` on 739 callbacks and `reference_coast` on 12. It is budget-locked for about 98.4% of the interval. Its episode started before this window and its finite budget was already spent. No precharge-only stage is admitted.
- A proper half-second positive, nominally unbraked, measured-clear recovery finally rearms it about 14.77 seconds into the window. This is expected budget/rearm behavior, not a missing toggle or incompatible schema.
- Ten brake-OFF intervals follow. Five never regain positive propulsion before the next brake request; others clear and start the bounded propulsion ramp, then re-enter braking before recovery is complete. Representative observed-clear waits are about 0.18–0.22 seconds; useful OFF intervals are mostly under 1.1 seconds.
- The underlying release policy alternates between nonpositive-intent braking and its qualified positive release as the raw integral-driven request crosses the pitch-adjusted decision boundary. The producer integrates signed error during actual braking, freezes some unattainable positive error during release/ramp, and resumes integration when returned limited-state changes.

Simply making the precharge budget repeatedly rearm would remove the finite-demand protection that was deliberately introduced. It would not establish an appropriate physical engine-braking/coast response.

### Rejected diagnostic shortcuts

Turning the integral gain off for a whole route adds release-timeout faults before the selected windows; its apparent zero switching is partly lost engagement and cannot count as improvement.

Holding the integral only inside the selected window (with identical prior state) reduces 20 changes to five but raises actual-brake command time from 9.914 to 14.037 seconds in the first route. The second route adds a release-timeout fault and loses most active exposure. Both are rejected. Broad integral freezing is not a pulsing fix.

The narrow low-speed prototype described below also leaves the principal highway episode at 20 changes. It addresses a different software gap.

## High-RPM event: late target selection, with counterexamples

Twenty-one qualifying first→second target transitions were found in saved data: four OEM, eleven older Alpha and six new Alpha. Driver pedals are absent around target selection; command ownership, valid CAN and source freshness are checked. This is observational data, not matched load/grade/traffic testing.

- Four OEM examples target second at about 8.75–9.13 mph, with peaks of 2,100–2,636 RPM. Target-to-reported-actual delay is about 1.74–2.22 seconds.
- Five ordinary new Alpha examples target second near 9.05–9.81 mph and peak at 2,472–2,602 RPM. Their delay is about 1.74–2.10 seconds.
- The exceptional new restart targets second at **20.69 mph**, peaks at 3,946 RPM, and reports actual second 2.24 seconds after target selection. Another ordinary new Alpha event is also a rolling restart, with minimum preceding speed about 3.61 mph; a complete stop versus rolling start alone does not explain the exception.

The same inactive prediction/always-enabled resume fields coexist with ordinary Alpha shifts. Their OEM/Alpha difference remains a reverse-engineering lead, but setting prediction to OEM-like values cannot be credited as a demonstrated fix. Engine ACC status is normal in the exceptional window; the reported stop-mode request is inactive. No direct gear command is added or tested.

## Concrete low-speed control gap and local prototype

During the exceptional 3–6 mph reacceleration, feedback correctly advertises a valid `engineRamp` phase, limited propulsion, no brake/precharge and received torque at zero. The output request rises at the existing 0.5 m/s² per second limit. However, the existing integral anti-windup predicate requires speed >=3 m/s (6.71 mph), so positive tracking error keeps accumulating below that threshold.

Recorded examples: at about 3.7 mph the controller wants 1.74 m/s² while wire propulsion is 0.64; around 5.5 mph wanted reaches 1.99 while wire propulsion is 1.14 and stored integral is about 0.77. This is a real software mismatch between the delivered ramp and the integral eligibility window; it does not prove the stored correction caused the TCM's late shift selection.

Research-only `ramp_experiment.py` extends positive anti-windup only for speed strictly between zero and 3 m/s, PID state, fresh current-owner protocol-1 `engineRamp` feedback, no brake/precharge/reference-brake demand, and a valid nonnegative propulsion request below wanted demand. It preserves negative-error integration, target-negative recovery, malformed/stale/unknown metadata fallback and the original >=3 m/s predicate. It does not authorize propulsion, change clearance, alter ramp rate, modify planner/gains, or touch steering.

A genuine baseline regression fails the recorded low-speed case; all **41 focused tests pass** with the prototype. In an episode-isolation ablation with identical state/history before the restart, peak stored correction falls from about **0.772 to 0.199** and peak valid propulsion request from **1.823 to 1.398 m/s²**. There is no new propulsion blackout during the reacceleration through 6–8 mph. The absolute-time episode selector is diagnostic only, not a runtime feature. Physical acceleration, RPM and gear response are unchanged inputs in this replay and cannot be claimed improved.

## Broader replay and remaining blocker

The general metadata-based prototype, without an episode-specific selector, was replayed across **162 segments / 472,261 controller callbacks**: the 25 new active-drive segments plus the 137 retained segments. No added coordination faults, inactive-path changes, gas during commanded brake/precharge, or moving-PID gas with retained measured torque were found. Two reconstructed older baseline release faults remain identical.

The strict strong-deceleration history gate fails: 253 callbacks with consumed target <=−0.5 m/s² have slightly more positive raw requests. At 27 callbacks this changes encoded total-brake acceleration by **one 0.0039 m/s² wire increment**; gas and brake-bit selections at those samples are unchanged. Maximum raw delta is about 0.0005115 m/s². This is a small software command difference, not a measured braking-distance effect, but it does not satisfy the existing no-weaker-braking requirement.

The first positive integral crossover is localized in two retained routes. A lower request reaches the end of a later handoff earlier, clearing `limited` feedback one or two producer iterations before the reference. Positive integration then resumes on the candidate while the reference remains held. Another route crosses while candidate actual braking still integrates signed error but the reference is waiting for release. Thus direct low-speed scope does not guarantee identical later integral history.

**Do not integrate or install this version.** Native candidate CAN replay, paired build/ARM validation and device staging were not run after this history gate failed. The next correction needs a consistent recovery/handoff policy that avoids this later crossover; do not hide it with recorded-I reseeding, arbitrary extra braking or a blanket post-ramp hold. Separately, the downhill nominal mode selection needs its own response-aware design rather than treating the small precharge entry as a full coasting controller.

## Receipts and preservation

`VERIFICATION.json`, `cycle-diagnosis.json`, `shift-events.json`, `ramp-red.log`, `ramp-final-tests.log`, `ramp-comparison.json`, `strong-wire-regression.json`, `first-positive-integral-divergence.json`, `integral-ablation.json`, `window-hold-i-summary.json` and `ramp-highway-windows.json` retain results. The existing committed-baseline artifacts are reused for the 137 retained segments at the same exact paired source; their SHA-bound input caches are rechecked by the runner. Both paired repositories remain clean at parent `5b301a944` / child `884c9f491`, with 1.20/0.97 unchanged. No device connection or setting change occurred in this investigation. Raw recordings, full traces and source-rich extracted data remain private.
