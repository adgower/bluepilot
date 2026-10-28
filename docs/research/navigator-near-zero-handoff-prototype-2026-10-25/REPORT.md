<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Near-zero handoff and integral-recovery prototype — October 25, 2026

## Result

**Built and tested locally; rejected as an overall pulsing fix.** The bounded state machine and feedback-aware integral experiment are implemented. They retain measured clearance and add no replay faults or native packet rejections, but they do not materially reduce the observed highway cycling. Some speed bands have additional brake transitions or slightly more commanded brake time. Do not integrate, push or install this version as a comfort improvement.

The Comma was not contacted. Neither paired checkout was edited; clean parent `ead00c30e` / child `d4a20125` and steering 1.20/0.97 remain unchanged.

## What was prototyped

`policy.py` wraps the installed weak-brake qualifier with an explicit coast trial. New intervention is limited to moving PID operation through 70 mph, no stop/FCW/lead, fresh independent radar and actual/arbitrated brake-torque data, mild requested/grade-compensated demand and small measured tracking error. State includes a causal error filter, short trial deadline, physical speed-tracking budget and recovery latch. The budget is 0.04 m/s absolute speed error against the integrated planner target; the maximum trial is 300 ms. Micro positive crossings do not rearm it; sustained positive, measured tracking recovery is required.

The release-aware version may withdraw a weak brake bit while received actual/arbitrated torque is already at most 4 Nm even when the measured observer is still qualifying clearance. It cannot authorize propulsion: the existing observer must independently receive the original distinct-sample clearance sequence. Retained pressure still withholds gas, stalled release still faults, and the current progressing-release two-second bound remains. Strong braking demand and invalid context fall back immediately. No planner target, grade offset, PID gain, native safety limit, longitudinal upper acceleration cap or steering setting is changed.

`experiment.py` overlays the actual CarController in memory. A permitted coast sends a valid request bounded at zero/nonpositive demand through the existing handoff limiter. The existing limited/brake/fault feedback flags stay honest, and an explicit reason identifies the experimental state. The producer's optional integral settling holds only tiny errors while this marked feedback is fresh, valid and in the current owner epoch. Normal release/ramp anti-windup and integration resume outside that state. Admission-only and combined versions were replayed separately.

No forecaster output establishes torque clearance or actuator feedback. No global camera/vehicle calibration was reset. Valid zero propulsion is an ECU input, not proof of neutral or fuel cut.

## Defects found and corrected in the spike

The first acceleration-instant version admitted too little useful behavior and failed broad comparison. The second version replaced rectified noisy acceleration-error accumulation with the bounded speed-error reference while retaining the maximum trial time. A RED regression then demonstrated that an expired trial could fall into another legacy qualification delay. The corrected deadline/failed-tracking exit applies the underlying requested brake decision at that exit, while locked fallback otherwise retains the original qualifier. This avoids repeating the earlier rejected prototype's blanket raw-brake fallback during lockout.

The actual-controller hard-bound test initially used inconsistent floating-point versus integer-nanosecond synthetic timestamps and hit the existing strict future-sample guard. The harness was corrected to use one integer-nanosecond clock; the production freshness check was not weakened. Another retained test expected the underlying qualifier's public `budget` attribute, which the wrapper now exposes without changing that budget.

First/second/entry-only source snapshots and uniquely named replay traces are retained. They are intermediate experiments, not the final result.

## Validation

- **18 focused tests passed**: debt/deadline/rearming, measured speed error, owner reset, stop/FCW/lead/stale/missing-radar fallback, out-of-scope speeds through 85 mph, marker freshness and integral recovery, and actual-controller retained-pressure/clearance/time-bound contracts.
- **157 existing longitudinal tests and 20 subtests passed** with the candidate controller substituted into the module used by the tests. Plain native debug hooks were loaded for existing permission tests.
- **137 saved segments / 401,970 consumer callbacks** in chronological producer/consumer replay, with the candidate's own feedback affecting subsequent integral updates. Original state, torque, driver actions, planner targets and pose remain fixed.
- **Fresh native RX/original non-ACC TX/timer replay on the 76 newly extracted segments:** 17,832,115 RX and 521,403 TX events per variant, zero added candidate rejection, no relay fault, no forced controls permission. Existing recorded/permission-boundary rejections are retained. This is a plain Mac debug build; sanitizer, actual firmware execution, forwarding/heartbeat injection and hardware validation are not claimed.
- The 61 older segments have exact baseline wire-byte identity. They lack the independent arbitration/radar context required for new admission, so this establishes fallback preservation, not active coast-state validation there.
- The full new maneuver route is also wire-identical. The deliberate maneuver planner reports a lead, so the new trial does not interfere with those tests. This preserves the successful timeout correction; it does not physically test the proposed coast input.

## Coupled results

Only **11 callbacks** reached permitted valid coast across the two new normal-driving sessions; none were admitted in the maneuver session or older corpus. Altering even those few callbacks changed later integral history, reinforcing why an isolated brake-bit replay is insufficient.

Representative brake-transition counts in one normal-driving session:

| Speed | Baseline | Combined candidate |
|---|---:|---:|
| 35–40 mph | 21 | 23 |
| 40–45 mph | 44 | 46 |
| 50–55 mph | 47 | 47 |
| 55–60 mph | 37 | 37 |

In 50–55 mph, commanded brake time increases by about **0.585 seconds**. The other session's 50–65 mph transition counts remain unchanged; its 60–65 mph brake time falls by only **0.041 seconds**. The named bad highway windows remain in `named-episode-comparison.json`; the approximately 55 mph, 24-transition episode is not solved.

No candidate fault samples were added. The older reconstructed baseline's stalled-release fault around 69.7 mph remains at the same time, rather than being hidden to improve the score. Maneuver output remains unchanged.

The combined version still produces **513 callbacks with slightly weaker raw requested deceleration** when the planner target is at most -0.5 m/s²; the maximum difference is about **0.0005103 m/s²**. This is a small software-request shift, not demonstrated weaker physical braking or a stopping-distance change. It nevertheless fails the predeclared strict regression gate, and there is no meaningful comfort benefit to justify it. Admission-only removes that particular integral-regression count in the final release-aware comparison, but still has no useful highway switching reduction and adds transitions in the same lower bands.

## Baseline and interpretation limits

The baseline reproduces all recomputed producer outputs/integrals and feedback of new sessions 01 and 06 within the declared tolerances. In session 02, about 99.02% of recomputed outputs/integrals match within 1e-5; the saved pre-install pose fault is not reproduced by the reconstructed consumer visibility/timing. Candidate comparisons are against that same reconstructed baseline. They must not be presented as a physical repair of the recorded pose fault. Older recordings are current-stack stress counterfactuals, not exact reproductions of historical installations.

Recorded vehicle response cannot react to candidate commands. These results establish software behavior and reject regressions, not passenger comfort, fuel economy, following-distance performance or physical stopping behavior. Most of the troublesome cycle is outside the narrow qualified coast interval; simply granting a longer grace period is not justified by this experiment.

## Remaining blocker and next local direction

A small extra coast qualifier is insufficient. The existing grade-conditioned brake decision, actuator authority and integral history still govern the subsequent cycle. The next useful work is to resolve effective near-zero propulsion/coast/brake response and its timing against the measured ECU channels, then test a consistent mode-level controller with those dynamics. Blanket integral freezing, a larger gain, relaxed measured clearance or an arbitrarily longer coast grace period are not supported by these results. Existing saved data are sufficient to continue the local investigation; another uncomfortable drive is not needed just to repeat this failure.

## Files and reproduction

Design and plan: `DESIGN.md`, `PLAN.md`. Code: `policy.py`, `experiment.py`, `joint_replay.py`. Evidence: `RESULT.json`, `unique-tests.log`, `retained-tests.log`, `joint-comparison-combined_release.json`, `fallback-and-maneuver-identity.json`, `named-episode-comparison.json`, native results/provenance and private hash-bound manifests. Raw route identities and full payloads stay private.

Use the existing paired Python with this research directory as script location. Run focused tests with this directory as pytest confcutdir, `joint_replay.py` with `JOINT_VARIANT=baseline`, `admission_release` or `combined_release`; use `JOINT_MANIFEST=older-inputs.json JOINT_PREFIX=older-` for older data. Run `compare_joint.py` with `JOINT_CANDIDATE=combined_release`, and `native_replay.py` for the same candidate. Prototype overlays affect only their own process. No source integration, build/deploy, publication or device activation was performed.
