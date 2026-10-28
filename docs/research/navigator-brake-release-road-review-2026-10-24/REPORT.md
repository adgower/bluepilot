<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Brake-release road review — October 24, 2026

The latest change is not sufficient to prefer Alpha over OEM ACC. New recordings establish a repeatable software propulsion interruption near 6.7 mph, substantial remaining brake-command cycling, and two release-observer timeouts. No controller/tuning/settings/source/OS/firmware changes, CAN transmission or ECU queries were made in this investigation.

## Data and reproduction

55 newly completed segments / four sessions (481,255,652 bytes) downloaded and SHA-256 checked, with remote recheck and unchanged source/settings/service during acquisition. Two sessions are stationary setup; the two moving sessions span <private clock time>–<private clock time> and <private clock time>–<private clock time> America/Chicago, about 39.8 minutes of recorded longActive. Maximum actual speed 65.7 mph; no 80–85 mph evidence here. First setup session predates activation; both moving sessions record the intended parent `064e086d2` / child `50719b1e` behavior.

`replay_controller.py --assert-no-release-timeout` is intentionally RED: it reproduces both release timeouts. At 136,308 recorded consumer callback slots, all **four checked fields** (brake, gas, fault, reason; gas tolerance `1e-5`) match. This reconstructs latest-published carState and decoded torque, disables lateral activity, substitutes vEgoRaw=vEgo, sets flags15 and frame=slot*2. It is not complete-feedback-byte equality, exact consumed-state reconstruction, a native safety replay or physical vehicle simulation. The minimized observer fixtures reproduce the same timeouts with 51/52 samples. Paired production checkouts remain clean at their original hashes.

## 1. Restart pause: a specific 3 m/s state-boundary defect

Nine selected automatic launches show a previously positive propulsion request becoming the inactive sentinel at the **3 m/s (6.71 mph)** crossing. Brake command is false and decoded torque is zero at each crossing. ECU-reported gear remains first from0.5 seconds before through1.5 seconds after each crossing. Eight cases reach10mph with uninterrupted automatic activity; the ninth remains automatic through its observation window. This selected cohort does not establish universal launch performance.

The source mechanism is direct: below3m/s, ReleaseBarrier resets its moving clearance obligation each update. Entering the moving band requires new post-start torque samples even after a run of clear feedback below the boundary. That withdraws propulsion and resets Handoff.last_valid; restoration then starts at zero and rises at0.5 m/s³.

Example09:46:24.501: sent request1.769 m/s² → inactive while torque0; one second later sent request0.461 m/s² versus requested2.0 m/s². The recording shows speed flattening near8mph and estimated acceleration dropping alongside the command discontinuity. This is associated observed motion; it is not a counterfactual measurement of how the vehicle would behave after repair.

[Private/local visualization omitted](../../navigator-reference/PRIVATE_ARTIFACTS.md)

`restart_boundary_diagnostic.py` is intentionally RED (the initial pytest run took 0.25 seconds): steady0.7 m/s² demand, flat supplied pitch and repeated fresh zero-torque feedback reach healthy propulsion below the boundary, then a speed-only crossing returns gas=-5 with wait_observed_clear. No vehicle, shift event or planner change is required to produce this command discontinuity.

**Concrete next local design:** retain fresh, measured clear qualification across a speed-only transition; maintain continuity of an already valid propulsion request. Actual new braking, non-clear/stale/invalid torque, override, owner reset and urgent braking must still withdraw/requalify. Keep below-boundary outputs and native limits unchanged. This is a state-continuity repair, not a request to raise launch gains or permit propulsion without measured clearance.

Initial launch reaction time to a green light is not identified. The launch timing artifact starts at the last qualifying positive-planner PID run (>=150 ms) before3mph, not first lead departure, first demand or green light. In those selected cases, positive propulsion follows that selected reference by0.18–0.54s; eight observed runs reach10mph roughly6.0–6.6s later. Long red-light waits and earlier negative planner demand must not be counted as actuation delay. Two-second withholding totals are window sums, not necessarily a single continuous pause.

## 2. Pulsing remains on downhill and near-level proxies

The full-rate scan finds **39 brake-command transitions /20 seconds at59.7 mph**, with raw controller demand positive above 0.02 m/s² for 94.8% of that window. The second moving session has a22-transition20s window near44.3 mph. These count requested on/off edges, not39 independently verified physical brake applications or direct comfort scores.

[Private/local visualization omitted](../../navigator-reference/PRIVATE_ARTIFACTS.md)

Grade-dependent brake decisions and request withdrawal repeatedly switch around near-zero demand. The selected worst window has 45 net decision zero crossings; replacing supplied pitch by that window's median leaves 22. This is retrospective sensitivity with lookahead, **not** a proposed real-time filter or evidence of a deployable smoothing improvement. Planner/controller demand also varies, so pitch is not the only contributor.

Twenty-Hz context summaries show braking-command fractions around 52–56% in downhill-proxy samples and 21–32% in near-level-proxy samples; coasting states are present but intermittent. These proxies use calibrated pose plus the existing relative reference offset, not surveyed grade. Actual acceleration estimates and reported brake torque vary too. The recordings support the reported pulsing and flat-ish occurrence, but do not establish comfort/fuel improvement relative to unmatched older OEM routes.

**Next local design:** a coherent coast/precharge/brake allocator with a stable, causal decision reference and bumpless transitions. Preserve urgent/planned braking and fresh-feedback guards. The earlier short-edge admission change does not address sustained switching or the restart state reset. A separate precharge bit alone was already insufficient in prior frozen-input research; do not equate fewer bits with better physical response.

## 3. Both Controls Mismatch episodes are release timeouts

| Local consumer time | Speed | Torque at fault | Valid pose age |
|---|---:|---:|---:|
|<private clock time>|34.18 mph|72 Nm|53.76 ms|
|<private clock time>|45.97 mph|92 Nm|27.23 ms|

Both reproduce release_timeout_disengage with fresh torque and pose context. During their release waits, reported actual torque stays72–172 Nm and92–216 Nm; no sample reaches the current<=4 Nm clearance threshold. The observer therefore faults under its existing contract. Later repeated alert/state transitions belong to the second episode; they are not extra independent torque faults.

The fresh ABS 531 status probe finds ACC active-braking/precharge bits low for roughly 98% of distinct incoming frames in each wait; CMBB braking/precharge/disable/deny indicators are low throughout. Nevertheless the arbitrated brake-request channel remains positive (medians 136/162 Nm) and reported actual torque remains non-clear. Normal_Operation is the decoded engine ACC status. These fields are not interchangeable and do not independently measure hydraulic pressure or prove physical release.

At the fault instants, raw demand plus uncorrected supplied pitch gravity is approximately -0.033/-0.082 m/s², whereas the mapped decision reference is +0.117/+0.068 m/s². This highlights a reference/command-semantics question; the earlier relative 0.1499 offset fit does not identify the PCM's internal reference or prove why torque persists.

First<=4 Nm observations occur about 40.5/118.2 ms after fault withdrawal. Multiple fields change on withdrawal (enable/resume and brake-acceleration request); this cannot identify which change caused clearance or prove it would clear with continued ownership. Keep the existing measured-clearance/deadline protections while resolving request ownership and feedback semantics.

## 4. Ford protocol work: useful, but start with the existing interface

The current Ford path already sends acceleration requests to the vehicle controller, rather than raw throttle percentage. [Upstream fordcan](https://github.com/commaai/opendbc/blob/d22436e8ef5e7bdd029a3f8561ecd4354968f948/opendbc/car/ford/fordcan.py) encodes separate propulsion and brake acceleration fields, precharge/deceleration flags, resume/stop and target/predicted fields. Several unused fields have explicitly uncertain effects in the source. Their names are not proof that changing them will improve a Navigator.

Freshly decoded ABS/PCM/gear status was added for all 55 new and 35 saved OEM segments. Older OEM eligibility is confirmed openpilotLongitudinalControl=false, cruise enabled, no driver pedals, received camera-bus ACC active and fresh past-only state/control. The 36,522 eligible moving OEM samples all have fresh ABS status. OEM uses precharge-only with a valid propulsion request;51 samples have positive requested propulsion and reported torque>4 Nm in that state. This establishes an observed command combination, not safe permission for Alpha to ignore residual torque.

Current production create_acc_msg derives precharge and actual-deceleration flags from one boolean, so it cannot represent that OEM distinction. The prior report-local split-flag experiment demonstrated an encoding possibility but did not resolve cycling. Combined with the new release waits, this is a concrete protocol/allocator investigation target.

### Passive reverse-engineering priorities

1. Correlate ACCDATA propulsion/brake requests, precharge/deceleration, CMBB enable, resume/stop and target/predicted fields through OEM coast/brake/release/launch events.
2. Identify how ABS arbitrated brake request and actual torque relate to ACC/CMBB active/precharge/deny/stop state. Preserve sender/bus/chronology; avoid treating a status flag as pressure ground truth.
3. Relate requested/actual wheel propulsion torque, engine ACC status, creep, RPM and gear/engagement status. The nine boundary examples remain in first gear, so their software dropout is not explained by a recorded shift.
4. Compare brake-acceleration field values during OEM ownership-preserving release against Alpha release, with speed, grade proxy and prior braking matched. A directly validated pressure/ownership observation or bench/HIL evidence is needed before replacing physical-clearance semantics.

Primary upstream context: [Ford longitudinal worklist #1393](https://github.com/commaai/opendbc/issues/1393), [merged pitch-compensation PR1418](https://github.com/commaai/opendbc/pull/1418), and [open Maverick brake-usage report3518](https://github.com/commaai/opendbc/issues/3518). The latter is another owner's report, not a verified Navigator diagnosis. No new alternate throttle protocol or third-party cure was established.

## Priority and remaining evidence

First local improvement: repair the demonstrated6.7 mph state discontinuity with retained fresh clearance. In parallel, resolve release-command/feedback ownership and design stable coast/brake allocation before another Alpha installation. Do not tune overall acceleration higher to compensate for the software dropout. Existing data is sufficient to prototype the continuity repair; more uncontrolled Alpha drives are not needed for that diagnosis.

OEM ACC remains the preferred baseline while these defects remain. This investigation leaves Alpha and every other device setting untouched; owner 1.20/0.97 and paired production sources unchanged. No new implementation/build/ARM/native-safety/parked/road acceptance is claimed. The existing installed pair's earlier acceptance remains historical evidence only.

Independent review supports the boundary mechanism and two timeout reproductions, with explicit reconstruction, selected-cohort and physical-causality limits in REVIEW.md. Intentionally failing diagnostic oracles are kept as evidence, not hidden as passing tests. Protocol hashes, manifests, traces, JSON summaries and figures are linked in this directory; raw route identities/GNSS remain in private storage.
