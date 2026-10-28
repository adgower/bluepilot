<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local turn-entry and 60–85mph investigation — October17,2026

## Main findings

**The saved drive strongly matches the reported inside-of-bend oversteer near85mph.** The matching section is logged at about82–83mph on October17,<private clock time>–<private clock time>:47CDT. Signals are off, lane-change state is off, and the driver steering input occurs afterward at22:42:49.113. The vehicle turns more than requested while the model-estimated inner lane line approaches the modeled vehicle origin. Model lane estimates support the user's report; they are not surveyed lane position, tire clearance or video confirmation.

The earlier all-speed review missed this section because its unchanged0.001/m meaningful-curvature threshold excluded it. That threshold was inadequate for investigating gentle high-speed bends. This investigation retains valid-data/driver/lane-change exclusions but screens by requested lateral acceleration and absolute response error. The earlier favorable50–65stronger-turn result still holds for that subset; it is not a clean bill of health for gentle bends or higher speeds.

**The24–30mph entry problem is real and distinct:** the command is delivered, but wheel/body response falls behind the growing request. The selected29mph approach is not primarily being held back by the final software slew limiter. Old same-revision recordings include a comparable29mph entry with the same delayed-response pattern.

No Comma connection, source/settings/service change, ECU query, firmware action or CAN transmission occurred in this investigation. Only preserved Mac recordings and local source were read. Owner1.20/0.97 and current installation remain unchanged. No controller prototype was implemented or installed.

## The reported fast bend

[Detailed results](../../navigator-reference/PRIVATE_ARTIFACTS.md), [wheel/model cross-check](../../navigator-reference/PRIVATE_ARTIFACTS.md), [anonymous trace](../../navigator-reference/PRIVATE_ARTIFACTS.md).

| Recorded evidence | Result |
|---|---|
| Clean scene |<private clock time>–<private clock time>.476CDT,6.5s |
| Recorded speed range |81.78–83.01mph |
| Body yaw response/request median |134.4% |
| Excess acceleration toward requested turn |Median0.3635m/s² |
| Measured wheel angle / requested angle medians |7.3° /4.99° |
| Median simultaneous wheel-minus-target error |+2.41° |
| Inner-line estimate at modeled origin |Approximately1.58m away before bend→0.41m near end |
| Lane-center proxy shift |Approximately1.09m toward the inside boundary |
| Lane confidence used for these distance summaries |Both inner-line probabilities>=0.7; confidence falls later |
| Blinkers / lane-change state |Both off throughout selected scene |
| New roll-mapping term |Exactly0 |
| Reconstructed mapped versus no-map path command |Identical throughout selected scene |

This is more than an unstable percentage on near-zero input: the selected scene requests roughly1m/s² of lateral acceleration and has a substantial absolute excess. The large model is asking for less wheel angle than the measured angle. A learned-parameter wheel model also predicts excess curvature (median143% of request versus about136% body response at its own sample times), making a body-yaw-only artifact a weaker explanation. Wheel and body estimates are not independent ground truth. Recomputing the application's desired angle from each atomic calibration packet agrees with its recorded target within2.4e-7deg. The new target-stamping code is not producing an inconsistent angle target in this scene.

The actual lane crossing and precise road curvature cannot be reconstructed conclusively from these model outputs. No retained road-camera video was inspected. The data nevertheless corroborates the reported inward drift and excess response before driver correction. It does not support blaming an intentional lane change or earlier driver steering for the start of this scene.

### Why the new roll option did not correct it

The installed mapping weight fades out65–70mph and is zero at/above70mph. Its reconstructed final output equals the independent baseline in the fast scene. This is an unaddressed upper-speed baseline tracking issue, not observed active roll-mapping overcorrection there.

Above70mph, the fork converts requested curvature to path angle through its existing speed/curvature gain. It does not directly regulate the difference between the application-level desired wheel angle and the measured wheel angle. The deviation guard remains, but it is not a general wheel-angle tracking loop. The model may change its future demand as lane position evolves, which does not identify a unique feedforward gain from this one scene.

At this speed, the gentle branch is1.425 and the high-curvature branch with the owner's0.97 is1.38225. The scene's effective baseline factor is about1.4107 because the branches blend by curvature. Therefore0.97 is not a blanket3% reduction of all high-speed steering. This source fact identifies the conversion path; it does not validate dividing its gain by the observed response ratio.

### All60–85mph bands, including gentle turns

These are all eligible turns with requested lateral acceleration>=0.25m/s², not steady-only measurements. They include changing requests and cannot be compared directly to the previous steady-only table. The gentle subset has abs(requested curvature)<=0.001/m—the part the previous scanner excluded.

| mph | Eligible turn exposure | Median body/request, all | Gentle-turn exposure | Gentle-turn median |
|---|---:|---:|---:|---:|
|60–65 |203.35s |107.0% |133.20s |114.8% |
|65–70 |22.15s |110.0% |17.45s |113.4% |
|70–75 |4.00s |134.3% |4.00s |134.3% |
|75–80 |0.15s |Insufficient |0.15s |Insufficient |
|80–85 |9.40s |136.6% |9.40s |136.6% |

The80–85 result is mostly one bend, not broad independent coverage. The70–75 exposure is also sparse. Above the old curvature cutoff, the new60–65all-phase response median remains98.2%, while its gentle subset is114.8%. Thus speed alone is not an adequate calibration dimension; bend demand, roll, direction, timing and mapping activation also matter.

A screen requiring at least0.5s, same-direction excess acceleration>0.2m/s² and response>120% finds eight windows: one around63.6mph, five fragments of the82–83mph bend, one around71mph and one around68mph. Fragments of one bend are not independent failures. [Complete windows](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The separate84mph peak near22:47:31 follows a signaled lane-change interval around22:47:22. At the peak, requested lateral acceleration is near zero. The report-matched no-signal bend is the earlier83mph section; the later nearly straight peak is not pooled into it or used for a meaningful response ratio.

## 24–30 mph: where the delay occurs

[Stage metrics and historical fixtures](../../navigator-reference/PRIVATE_ARTIFACTS.md), [prior send-time command reconstruction](../../navigator-reference/PRIVATE_ARTIFACTS.md), [prior limiter detail](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The frozen29mph shortfall reproduces15eligible samples/0.75s at62.6% median simultaneous body/request response with no driver input. Demand grows rather than settles. The episode progresses into a `turn exceeds limit` alert and sustained driver steering at22:33:39.891.

| Stage | Observation |
|---|---|
| Model→control curvature |Median absolute difference0.000218/m in the3.3s approach; a smaller gap than the ensuing wheel/body shortfall. Sampling and standard curvature limiting can contribute. |
| Command→recorded CAN path angle |Median error0.000112rad,95th percentile0.000236rad, within the0.00025rad half wire step |
| Final slew/deviation guards |Prior clean1.95s analysis: no soft-slew-bound frames; deviation guard binds only3/39frames |
| Desired→measured wheel angle |Median absolute gap6.81°,95th percentile18.30° in the3.3s approach |
| Late approach, before driver input |Target grows approximately25.3°→64.6° magnitude; measured wheel18.3°→45.9° |
| Late approach angle gap |Median11.16° over1.8s |
| Controller angle-saturation flag |1.7s of the3.3s approach |
| Roll mapping |Zero; this option does not cover24–30mph |

The late measured angle turns in the correct direction but does not keep up with the target's growth. Body yaw also falls behind. This localizes a substantial error downstream of target production/command delivery. It does not prove a hard EPS torque/rate limit: path angle is not a direct wheel-angle command, and the retained data do not identify internal EPS actuation limits or a unique closed-loop vehicle model.

The24mph rise/unwind scene has a smaller2.82° median absolute wheel-target error and later response above the withdrawing request. The29mph selected below70% window reaches about108% of its earlier request when body response is examined0.5s later, still before driver input. These shifted comparisons illustrate dynamic timing; they are not a calibrated constant0.5s delay or proof that extra lead/gain would be correct during turn exit.

### Repeatability in older saved drives

Eighteen prior-revision normalized sessions were hash-verified and screened with the existing24–30mph discrepancy definitions. Two>=0.5s under-response windows exist in two sessions:

- `collection-drive-02`, approximately29mph:55.4% simultaneous response,78.6% at+0.25s and107.1% at+0.5s. Assistance was active for the preceding2s with no driver steering. This is a useful corroborating turn-entry fixture.
- `oct17-session-05`, approximately27mph:9.8% simultaneous response and62.1% at+0.5s. Only7.5% of the preceding2s was assistance-active and driver input was present. Treat it as an engagement/transition case, not the same settled-control mechanism or evidence for one universal delay.

The older24–30scanner contains no>=0.5s above130% window under those eligibility rules. The latest drive does contain a brief unwind overshoot at29mph, so the absence in older scenes does not remove the exit-risk counterexample.

## Hypotheses and outcomes

1. **Entry-response lag:** supported by wheel/body falling behind rising targets, verified command delivery and one comparable old29mph scene. Exact actuator delay versus dynamic gain/internal EPS response remains unidentified.
2. **Planner/command blocking is the primary29mph cause:** not supported in the selected clean lead-in. Small model/control differences and brief deviation clipping exist; final slew and CAN quantization do not explain the large wheel-angle gap.
3. **New mapping actively overcorrects at83mph:** ruled out for the selected scene; its term is zero and final output equals baseline. The unvalidated upper-speed conversion/angle-target tracking remains the leading control-path concern.
4. **Intentional lane change or driver input initiates the fast event:** not supported for the matching bend. Blinkers/lane-change state are off and steering input follows the measured inward movement. A separate faster peak follows an actual lane-change interval and is treated separately.
5. **Pure yaw artifact or bad target snapshot:** weaker after wheel/body cross-check and exact target recomputation. Learned geometry/roll accuracy, actual bank and planning/model errors remain possible contributors; no independent road/lane ground truth is available.

## What to do next locally

Prioritize the reported high-speed inward-drift fixture before another device trial. Review calibrated target propagation and conversion jointly across speed, turn demand and roll; the current raw-curvature gates leave gentle bends weakly handled and the speed gate leaves70+unmapped. Extending the existing speed range alone is not validated by these results.

For24–30mph, the next design question is bounded turn-entry response compensation with prompt withdrawal/reversal/driver release—not a persistent percentage boost. Keep the24mph unwind counterexample, the29mph takeover and old29mph entry together. Do not relax native range/slew/deviation safeguards or change1.20/0.97 from this investigation.

Before any candidate is activated: local paired-source integration, full retained-data replay including these newly admitted gentle high-speed fixtures, abort/reversal/release tests, native safety and build checks, followed by separate device/hardware acceptance. No claimed replay can establish a new physical vehicle response without later validation. Existing saved data are sufficient for the next local stage; no high-speed reproduction run is needed.

## Reproducible witnesses and scope

`witness.py --expect-within30pct` deliberately fails on the frozen29mph recorded shortfall. `highspeed_witness.py --expect-no-excess` deliberately fails on the selected recorded excess-response/inward-lane-estimate proxy. Their normal modes assert the symptoms are preserved. These are red-capable recorded-data witnesses, not a simulator or a regression test showing that hypothetical controller code fixes physical steering. The actual lane crossing has no video/surveyed ground-truth replay in this retained dataset; that portion remains observational.
