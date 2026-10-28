<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Rising-demand Navigator correction — local prototype

The prototype starts the added command about0.95s earlier on the saved weak15mph turn. Full replay of six complete drives/89 segments finds no additional native safety rejections, defaultOFF parity and recorded≥25/45mph command parity. It is not a zero-rejection replay: one identical rejection remains in the installed baseline and candidate near28mph. A synthetic aborted-turn residual tradeoff also remains. No Comma access, source/settings change, service action, ECU query or CAN transmission occurred.

## Why change admission

The installed correction waits for a nearly steady request and projects absolute wheel-response growth toward the current request. During a ramping turn, both desired and actual curvature can rise while actual/request stays weak; absolute growth is not necessarily catch-up. On the saved turn the installed visible term began889.727s, only0.331s before detected driver input at890.058s.

`ramp_tracking.py` is a report-local subclass of the pinned installed controller. It preserves the installed feedforward, fixed pinion model,1.20/0.97, original range/slew/shadow/human-override sequence and private CP model. No installed selector or branch is edited.

## Experimental design

Existing observation/freshness/driver/fault/profile/flag eligibility, observed response floor10% and5–25mph speed fade remain. Full speed weight through15mph, zero added term at25mph. Explicit per-frame state/control/model context and model lane-change/blinker guards remain.40–60ms steering cadence and actual timestamps are retained.

Admission keeps the11-sample nominal0.5s window and six-observation hold. It accepts either the prior steady-demand condition or a bounded same-direction rising request at nearly constant speed. Rising rate is limited to2 times the window's median request per second both over the complete window and at every adjacent actual-time interval. Backsteps are tolerated only up to2% of current request per sample. A large jump cannot masquerade as a smooth ramp.

Release uses the measured/requested response fraction and its positive recovery slope projected1s ahead. A weak, roughly constant fraction under increasing demand can qualify; a fraction recovering toward70% vetoes the extra term. This is an experimental gate, not a fitted predictor of the Navigator.

For a rising request growing>5% over the window, halve the computed feedback term: effective Kp0.125 and cap min(0.00375rad,6.25% of feedforward), versus installed steady Kp0.25/cap min(0.0075rad,12.5%). The existing filter remains0.30s. No integral, yaw-sensor switch, EPS-bit override, reset pulse or safety-limit expansion.

## Saved-turn timing

Past logged inputs at actual outgoing20Hz timestamps reconstruct first additional term:

|Evidence|Installed correction|Local candidate|
|---|---:|---:|
|First extra term, recording seconds|889.727|888.780|
|Lead before detected driver input|0.331s|1.278s|

That is0.947s earlier under recorded feedback. An anonymous saved-turn fixture drives the actual correction code; its earlier-admission regression fails with the installed class substituted and passes with the new candidate. This is command timing, not earlier physical response, fewer interventions or a road-improvement estimate. Logged state is held fixed in the comparison; no changed vehicle/planner feedback is predicted.

## Full native safety replay

Baseline is the currently installed ReleaseTrackingPrototype with correctionON. Candidate is the new local RampTrackingPrototype ON. Separately, candidate defaultOFF is compared against installed feedforward with trackingOFF. Both safety hooks have independent native state, consume recorded physical RX and permissions, and never force controls allowed. All89 raw files are hash/size checked against saved manifests.

|Result|Count|
|---|---:|
|Complete drives / segments|6 /89|
|Controller updates per version|507,964|
|Physical RX frames per safety instance|20,227,501|
|Generated TX|301,709|
|TX before Ford configuration, excluded|2,212|
|Configured candidate TX accepted|299,496|
|Configured TX rejected, baseline / candidate|1 /1|
|Additional candidate rejections|0|
|Relevant required RX invalid|0|
|Generated updates changed vs installed, all below25mph|192|
|Compared messages at≥25mph / changed updates|55,301 /0|
|Compared messages at≥45mph / changed updates|12,425 /0|
|DefaultOFF parity against trackingOFF feedforward|All updates|

The common rejection is0x3d6 near547.984s in the latest drive,28.44mph, active mode1, controls allowed/RX valid. All generated streams≥25mph are identical, so its payload is identical in both arms and the new added term is zero there. Timing is close to the previously unexplained hardware counter increment near548.016s. This strengthens an existing-baseline/replay issue for separate diagnosis; it does not establish the exact hardware rejection cause or justify widening safety limits. Do not call this a clean zero-rejection pass.

As before, zero extra term at25mph does not discard inherited slew history. Artificial instantaneous speed/demand jumps can briefly retain prior-output differences; dedicated tests preserve the slew bound and convergence. Recorded≥25/45mph parity is the concrete result, not a universal arbitrary-jump equivalence guarantee.

## Behavioral and sensitivity tests

36 behavioral/regression tests pass, including the inherited guard/cap/defaultOFF/high-speed cases, smooth signed ramps, fractional catch-up, silent actuator exclusion, single-jump rejection, ramp-specific cap and saved-turn admission. RED evidence is retained for rising timing, smaller cap, abrupt-jump guard and saved-turn behavior. Ford/controller/native suite213 passed,79 skipped,12,063 subtests passed; it validates the unchanged Ford framework, while report-local tests cover the new module.

Original96 step scenarios retain no unit-gain peak above the global requested magnitude and identical45mph commands. Expanded210 gain/time-constant/delay stress scenarios remain bounded as before. These simple plants are not identified from the vehicle and omit the outer planner/road/friction/authority model.

An additional300 ramp/hold/unwind/reverse/abort/noisy-request cases compares the installed correctionON against the candidateON. All45mph commands match. The worst tested unit-gain aborted-turn residual increases by1.327 percentage points of peak requested curvature: baseline0.9394→candidate0.9527 of that peak, after demand has already dropped. Remaining below the global peak request does not make extra turn-exit steering acceptable. Earlier admission has a material delay/residual tradeoff; tests do not establish that this candidate is ready for installation or safe in all closed-loop conditions.

The first exploratory candidate had~4.93 points extra residual against a feedforward-only reference; a smaller rising cap and per-step bounds reduced the risk. Final300-case results use the installed correction as reference; these comparisons are not interchangeable. Constants are sensitivity choices, not optimized or road-calibrated values.

## Review, reproducibility and next decision

Independent source review found a missing per-sample ramp-rate bound; added a failing jump regression, fixed it, and reran the full replay. Re-review found no further blocking source defect, while explicitly retaining the residual-turn-exit limitation. Reviewer did not rerun the final suite/replay; fresh logs and verification are recorded separately.

`summary.json`, `full-replay.json`, `verification.txt`, `provenance.json`, `input-manifest.json`, `test-green.txt`, sensitivity JSON and the saved fixture provide inspectable proof. Use the pinned Mac `.venv/bin/python` for `run_tests.py`, `full_replay.py` and the screen scripts. All work is local. Both installed-source checkout trees remain clean at parent74f66e7a0bf1dc0718431532948ece2c4fb0041c / child1b965caadd4a6aea4d09985532bf7cca6c0873ca.

Next: investigate the common28mph rejection separately and further assess ramp-release residual behavior before considering deployment. No road benefit or deployment readiness claimed. The Comma retains the installed correction and settings unchanged.
