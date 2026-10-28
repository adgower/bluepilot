<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# OEM predicted acceleration and target speed — October 26, 2026

**The fields differ from OEM, but saved drives do not establish that either causes the high RPM or pulsing. The clearest new finding is excess integral demand accumulated during rolling restarts below 6.7 mph.** That extra request is directly reconstructible from the recorded PID terms; its effect on the vehicle's shift schedule remains an association. No controller, paired branch or Comma changes were made.

## Evidence scope and method

Compared **168 saved segments / 16 routes**, including five OEM route records, older and newer Alpha records, and the two latest drives. Thirteen routes contain qualifying active observations: **40,548 OEM and 250,474 Alpha command observations** after command validity, fresh state/control/ownership, CAN validity and driver-pedal checks. Counts are correlated samples, not independent experiments. Three route records contain no qualifying active owner data and are retained explicitly.

The comparison keeps incoming factory bus-2 commands separate from outgoing Alpha bus-0 commands. State, gear, torque, status, plan and radar are aligned backward in time with their recorded validity and age; invalid latest observations never borrow an older valid value. Shift and launch cohorts break at ownership/pedal changes and clock gaps. OEM cruise setpoints were independently recovered from **35 hash-verified raw segments**, rather than guessing set speed from a CAN field name.

There are **321 upshift-target events**: 306 complete under the selection rules, ten retract/change and five censor. The low-speed cohort is **38 algorithm-selected first-positive-request episodes** in uninterrupted first-gear intervals, not every possible rolling restart. Ninety nonoverlapping 20-second highway windows meet the selected speed/gear/context rules; 84 are Alpha and six OEM. Data is inspected retrospective evidence, not a blind validation set.

## What the two OEM fields appear to represent

| Field | OEM observations | Alpha observations | Supported interpretation |
|---|---|---|---|
| `AccPrpl_A_Pred` | Varies with signed gas/brake acceleration requests; approximately 65–79% of observations in each active OEM route agree with the same-time positive-gas/otherwise-brake reference within 0.02 m/s² | Exactly −5 in all 250,474 qualifying active samples | Largely mirrors a current signed request in this corpus. The name does not establish a fixed advance forecast or its ECU purpose. |
| `AccVeh_V_Trg` | Varies around the vehicle's changing speed trajectory and often below the displayed cruise setpoint | Exactly 145 km/h in all qualifying active samples | More consistent with a varying near-term speed trajectory than a literal cruise-setpoint copy. Exact trajectory/horizon semantics remain unidentified. |

### Prediction is not a demonstrated one-second lookahead

Tested the OEM prediction against signed requests at −0.5, −0.25, −0.1, 0, +0.1, +0.25, +0.5 and +1 seconds. Among those diagnostic horizons, the same-time request gives the lowest mean absolute error in each of the four active OEM routes: approximately **0.042–0.063 m/s²**, compared with about **0.174–0.292 m/s²** at +1 second. This agrees with the existing packer's comment that OEM prediction appears to track the raw signed request.

Both selection formulas are retained: positive gas otherwise the brake-acceleration field, and any valid engine request otherwise brake acceleration. Inactive −5 gas is never treated as a real −5 m/s² request. Future values in these comparisons are retrospective outcomes only; no controller input or proposed field value uses future telemetry. Same uninterrupted owner blocks and endpoint availability are required.

This does **not** prove the prediction field is ignored, redundant in an ECU, or incapable of influencing torque/shifting. It only limits what can be inferred from its name and these recordings.

### Target speed is not simply the selected maximum

For moving OEM observations, the target-speed field is closer to measured speed than to the independently logged cruise setpoint in roughly **82–91%** of eligible samples per active OEM route. Median signed target-minus-speed differences are near zero, but median absolute differences are about **2.2–2.8 km/h**, so it is not an exact speed copy either. Retrospective comparisons against vehicle speed 0.5–2 seconds later generally fit better than same-time speed, with different preferred horizons across routes. Do not promote those descriptive comparisons into a causal forecast or fixed horizon.

Two samples in `oem-02` decode above 200 km/h, including 252, despite low vehicle speed. These remain visible in all-range statistics and are not treated as a valid high cruise setpoint or silently converted into a special code. Their meaning needs separate decoding verification. They do not justify copying those values.

Consequently, replacing Alpha's 145 with the driver's set speed would **not** reproduce the observed OEM trajectory. This finding does not establish that the existing constant is safe/optimal or explain the user's separate failure to reach the selected cruise maximum. Planner demand remains a separate control input.

## High-RPM result: delayed reported gear target and accumulated request

Among **completed first-to-second events**, the four OEM cases report a second-gear target at 8.78–9.18 mph. Thirty Alpha cases have a median target-change speed of **9.21 mph**, with two exceptions near **20.69 and 21.23 mph**. Those exceptions match decoded RPM peaks of **3,944 and 4,136**. Both began by resuming from a crawl; many full-stop launches with the identical Alpha field settings shift normally.

The latest high-RPM event reports target gear 2 at about 463.877 seconds and actual gear 2 at 466.144 seconds into the route. Its approximately **2.27-second target-to-actual interval** is within the **1.75–2.28-second range** seen among the selected completed Alpha first-to-second events. The unusual observation is the much later **target change**, rather than a uniquely long completion interval after that target. These are reported gear signals sampled/aligned at command times, not a measurement of the exact mechanical shift boundary or proof of which ECU scheduled it.

The three directly reconstructed recorded PID histories are particularly informative:

| Episode | Decoded RPM peak | Planner target around 6.7 mph | Stored integral around 6.7 mph | Raw controller request around 6.7 mph | Returned gas request / phase |
|---|---:|---:|---:|---:|---|
| Earlier rolling restart, `precharge-road-session-02` | 3,944 | 1.213 | **0.772** | **1.985** | 1.370 / engineRamp, limited |
| Latest rolling restart, `response-road-session-01` | 4,136 | 1.169 | **0.828** | **1.997** | 1.220 / engineRamp, limited |
| Normal full-stop launch in that same latest drive | 2,248 | 1.124 | **0.169** | **1.293** | 1.300 / drive, not limited |

Acceleration/request/integral values are m/s². These are **recorded producer values**, not substituted output from the uninstalled local low-speed guard. Source control, PID, state and plan validity is checked, and PID timing matches within two milliseconds. Returned feedback must be causally published, fresh and owned by the correct epoch/sequence.

Both problematic launches accumulate roughly 0.77–0.83 integral below the moving threshold while the software propulsion ramp is still limiting delivery. At the latest request peak, the vehicle is around 6.49 mph, planner target is about 1.174 and integral about 0.826, producing a raw request near 2.0. This establishes where the **extra software request** comes from. It does not prove that removing it would produce a particular RPM or shift response.

The installed `884c9f491` coordination source only applies its moving positive-demand anti-windup condition at speed ≥3 m/s (6.7 mph). The inspected local pair already contains a separate below-threshold engine-ramp guard, but it is **uninstalled** and has a documented later-city-braking exposure regression in frozen replay. This investigation neither changes nor clears that candidate. The useful next local step is to revisit bounded integral/release recovery with **both high-RPM starts, the normal same-drive start and the city 17-change regression**, rather than copying unknown CAN-field semantics.

The selected OEM launch cohort contains no matching decelerating rolling-resume case; three complete starts are from stopped and one is a rolling start with positive initial acceleration. Thus OEM-vs-Alpha RPM is not a matched experiment. Even among Alpha, two other selected decelerating rolling starts shift normally. Grade, request history, vehicle state and lead context remain possible contributors.

**RPM interpretation stays qualified:** `EngAoutNActl_D_QF` is decoded as zero across the relevant data. The current DBC labels it Faulty, but applicability/population on this vehicle is unresolved. RPM values support a match to the reported symptom; they do not certify a mechanical fault. Raw orientation is a pitch/gravity proxy, not surveyed road grade.

## Do these fields explain highway pulsing?

There is no observed Alpha variation in either field with which to estimate an independent effect. All qualifying Alpha records use −5 / 145, including normal first-to-second shifts, the two high-RPM cases, and 20-second highway windows ranging from **zero to 24 brake changes**. Constant settings do not explain the differences by themselves, but this does not rule out a context-dependent ECU effect.

The new 23-change highway episode remains in reported tenth gear. The sent brake bits and received brake torque pulse while the two fields stay constant. Locally, brake admission, release, grade adjustment, precharge and integral feedback are computed **before** `create_acc_msg` writes the prediction and speed fields. Neither field is an input to that software brake decision. Changing only their packed bytes in a frozen-response replay cannot establish a pulsing fix; any physical improvement would need a changed ECU response and resulting feedback that these recordings do not supply.

The window cohorts also demonstrate why simple owner comparisons would mislead: the low-switching windows can have different lead presence, demand, grade proxies, speed range, source revisions and total braking. Fewer brake changes is not automatically better coasting. No fitted owner/field regression is presented as a causal vehicle response model, because the Alpha field constants are perfectly confounded with controller ownership and correlated with other changed behavior.

The current evidence therefore supports continuing **request/integral/grade and coast–brake handoff work** as the direct software investigation. The OEM fields remain protocol hypotheses, not a demonstrated smoothness remedy.

## Native limit and feedback implications

The exact paired `ford.h` treats `AccPrpl_A_Pred` as a second gas channel. Its permitted active numerical range is **−0.5 to +2.0 m/s²**, plus inactive −5. Of the 40,548 qualifying OEM command samples, **6,193 prediction values** fall outside that range (5,587 below −0.5, 606 above +2). Copying the OEM field unmodified would therefore introduce known range rejections under the current hook; it is not an installable proposal.

A **64-case synthetic native TX unit probe** was compiled from the exact local child. It confirms the range/permission behavior and that the sampled target values 40 and 145 do not change hook acceptance. Permission is deliberately set in the isolated test library and is disclosed; this is **not** recorded safety replay, real engagement, device testing or ECU response validation. Debug hooks are built without sanitizers.

The probe also confirms that an in-range positive prediction can be accepted alongside a brake request when synthetic longitudinal permission is enabled. That does not prove physical simultaneous actuation, but it means a future prediction-field proposal cannot simply bypass the existing gas ramp, received-pressure barrier, cancellation and truthful feedback. The generic DBC receiver labels do not independently establish which Navigator gasoline drivetrain ECU consumes these fields. No safety limits were changed or weakened.

## Decision and artifacts

**No CAN-field change is justified for installation by this investigation.** Prioritize the recorded rolling-restart integral/ramp interaction and preserve the city/highway regressions. Retain prediction/target-speed research as a separate path requiring clearer semantics and response evidence. Saved-drive statistics cannot isolate the physical effect of fields that never vary independently in Alpha.

`inputs.json`, raw cruise extraction receipts, `analysis.json`, `recorded-launch-pid.json`, `predicted-field-limit-audit.json`, `native-field-probe.json`, contract RED/GREEN tests, independent review and final verification preserve the evidence. Raw recordings and source-rich timelines remain private local caches. No SSH, ECU query, CAN transmission, source integration, firmware/OS work or device mutation occurred in this turn. Local paired source remains `2ca969e45` / `bcd706d0`, with 1.20/0.97 and geometry unchanged.
