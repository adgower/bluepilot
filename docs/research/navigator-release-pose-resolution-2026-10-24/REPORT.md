<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local pose and brake-release work — October 24, 2026

**Pose expiry recovery passes the local final replay. Brake-release timeouts are not yet resolved.** A narrow OEM-motivated quiet-resume prototype is implemented and native-checked, but unchanged recorded torque still produces all four original release timeouts. They have not been hidden, rearmed or delayed. No Comma contact, device mutation, paired-source edit, push, OS/firmware update, active ECU query or CAN transmission occurred. Owner **1.20/0.97 retained**.

## Final evidence

-35 focused contracts pass, including actual copied `Car.controls_update` → actual controller execution with mocked IPC, source-copy preservation, stale/future/reversed/unhealthy inputs, single-drain race, inactive reset and quiet-bit-only tests.
-226 retained Ford/native guard tests pass;79skipped,12,028subtests pass. These are retained guard checks, not a complete production integration suite.
-Final v4 actual-controller replay processes247,765callbacks across four moving saved Alpha sessions. The one recorded62mph pose fault no longer initiates; no added fault initiation. All four original release timeouts retain their exact reproduced times. No changed vehicle-response or recomputed parent/plant simulation is claimed.
-Final native replay covers19,834,859raw RX packets **per variant** and247,734ACC TX slots. Baseline/candidate share six TX rejections; zero added candidate rejections, zero relay faults, no forced controls permission. Thirty-one earlier callback slots are outside logged Ford11 replay eligibility. This is **ACC TX only**, with raw buses0–3 and timer/tick input; not full lateral/forwarding/heartbeat/hardware validation.
-The release-resolution gate is intentionally **RED**: `check_replays.py --require-release-resolved`. See release-gate-red.log. Passing guard tests must not be represented as resolved release behavior.

## 1. Pose failure: expiry-boundary coherent refresh

Recorded cause near62mph: the consumed command's source pose was100.120004ms old at the controller, although valid at production; the newer motion publication arrived0.133ms after that command was published and3.346ms before consumption. A fresh calibrated source30.552118ms old was available to the consumer. Increasing the100ms limit or changing the source timestamp would hide the problem.

`pose_refresh.py` now attempts a **copied-command refresh only when the original source would exceed100ms**, plus the necessary monotonic-consumption exception after a previous refresh. Ordinary healthy commands remain on their existing path. It retains:

-Original enabled/active/PID/moving scope, producer validity, request epoch/sequence and producer timestamp.
-The original100ms source-age limit at consumption; no timestamp restamping.
-A coherent orientation/angular-velocity/source tuple built with the existing calibration composition.
-Lateral navigatorCalibration and requested actuator fields unchanged.
-True producer-source reversal, future/invalid/stale sources, bad calibration/topic/sensor health and already-invalid producer context cannot be rescued.
-A previously measured refreshed source can be reused only while still fresh; it is never extrapolated or restamped.

Independent subscriber lag is distinguished from a newer unhealthy publication; a lagging subscriber cannot invalidate a newer producer. The subscriber is drained once, then `FrozenInputs` freezes data, validity and publication times before the existing calibration helper runs. The helper's own update becomes a no-op on that snapshot. A review caught and fixed the former second-drain race, and a specific racing-input contract covers it.

The in-memory `Car.controls_update` seam applies the copied pose before the real controller. Live subscriber construction, lifecycle wiring and live apply-clock placement remain future production integration work; the application clock must correspond to the validated post-drain snapshot. No paired source was changed and no live integration/build/ARM result is claimed.

### Rejected attempts retained

-Wholesale consumer refresh introduced spurious faults when its independent subscription lagged the producer or had a sample too new for the original command identity. Rejected.
-An80ms early-refresh policy passed the two newest recordings but changed grade decisions and introduced a new release timeout at812.896s in an older session. Rejected after broader replay.
-Final v4 uses expiry recovery and passes all four saved sessions without that added fault. Earlier attempt results are not validation of the final policy.

The final new-drive comparison shows exactly one changed source-pose tuple, at the recorded expiry race. The parent in the recording subsequently disables longitudinal control because the original vehicle already faulted; frozen replay cannot demonstrate uninterrupted counterfactual parent/vehicle operation. It establishes prevention of the fault initiation and local interface behavior, not road readiness.

## 2. Release investigation: telemetry remains genuinely non-clear

All four waits reproduce for approximately one second without brake-bit assertion. Reported actual torque remains non-clear:

-Older episodes:72–172Nm and92–216Nm, with uncorrected request-plus-pitch net negative throughout each wait.
-New24.8mph episode: variable pitch/request reference, with positive and negative uncorrected net during the wait; reported torque remains non-clear,156Nm at fault.
-New20.5mph episode: uncorrected net is already positive throughout (+0.022 to+0.344m/s²), but reported torque remains236–744Nm. A single grade-offset explanation cannot resolve all four.

ACC/CMBB status and arbitrated request do not establish independently measured hydraulic clearance. Total reported torque cannot simply be ignored, nor is a higher clear threshold or longer timeout justified by these observations. Dropping multiple command fields at the original fault precedes eventual torque clearance, but does not identify which field caused it.

### Factory evidence and quiet-resume hypothesis

An initial broad camera-bus scan finds32falling brake-bit edges with brake enable retained and resume off. Restricting to the previously qualified OEM command dataset, excluding stopping, leaves **25matched non-stopping OEM release edges**; all25have resume off. This is a selected passive command sample, not a causal physical release experiment or proof of every OEM situation. The broader OEM scan also shows resume is usually off in other active states, so its name alone does not establish its exact ECU semantics.

Current custom/upstream packing sets `AccResumEnbl_B_Rq=1` whenever long_active is true, including release waits with inactive propulsion. OEM release brake-acceleration fields can remain negative; simply zeroing that field or forcing an invented positive release request is not supported.

`quiet_release.py` therefore prototypes only this narrow change:

-After a confirmed moving PID brake event, while owner/longitudinal remain active and the observer reports `wait_observed_clear`, brake bit is off, propulsion is the inactive sentinel and no fault exists, clear the resume bit.
-Keep collision/brake enable, brake acceleration, propulsion, stop fields, measured-clearance qualification and the original fault deadline unchanged.
-Clear qualification on inactivity, owner off, faults, stop/creep or confirmed clearance. Initial moving entry cannot qualify merely by waiting.
-OnlyACCDATA byte4 bit1 can change in this policy. Actual-controller metamorphic tests confirm all other parsed fields and feedback remain identical. The combined pose fix can separately change a packet at the recovered pose event; do not claim every combined-candidate packet differs by only one bit.

The latest final-wire replay clears resume in551/952targeted slots by drive. Native hooks accept this pattern without an added rejection. The CAN change does **not** alter the saved feedback, so all four original torque waits still time out. The independent observer remains active and withholds propulsion; no simulated clearance has been substituted into the recorded replay.

This is a supported **protocol hypothesis**, not a proven physical fix. It is possible the resume bit affects release, but its causal effect remains unmeasured. A successful no-fault software test obtained by replacing the torque stream with zero would not resolve that uncertainty.

## Remaining work before claiming resolution or installation readiness

The missing evidence is the ECU's actual response to an ownership-preserving release command with resume withdrawn, while retaining the same other request fields. A suitable controlled bench/HIL setup needs representative ABS/PCM behavior and independent brake/torque/ownership feedback. Stationary Park checks alone cannot establish loaded release at20–46mph. Another uncontrolled uncomfortable Alpha drive with the old command does not supply this counterfactual.

For future integration: preserve true non-clear/stale feedback failure, fresh distinct-sample clearance, original deadline, no propulsion before clearance, urgent braking/stop/restart and1.20/.97. Finish consumer lifecycle/clock integration, full parent/controller/transition/abort/default-off replay, build and hardware gates. No installation-ready or physical comfort improvement is claimed here. The earlier bounded-coast prototype remains local and still has residual pulsing.

## Artifacts

-`replay-gates.json`, `controller-replay-candidate_final_v4.json`, `old-controller-replay-candidate_final_v4.json`: final actual-controller results.
-`final-native-results.json`, `old-final-native-results.json`: final comparative native scope and shared rejections.
-`final-comparison.json`, `pose_refresh.py`, `quiet_release.py`, `test_pose.py`, `test_card.py`, `test_quiet_release.py`: local implementation and contracts.
-`release-probe.json`, `oem-release.json`, `resume-probe.json`: passive release evidence.
-`contracts.log`, `guard-tests.xml`, `release-gate-red.log`: pass/fail evidence retained honestly.

Raw route identities/GNSS remain in existing private saved-data storage. All work in this report is local.
