<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Why the 23–29 mph shortfalls and 64 mph unwind remain

October 20, 2026. Local diagnosis only; no SSH, device/settings changes, CAN transmission or production-controller edits. Owner **1.20/0.97** and paired branches remain unchanged.

**The failures have different software causes. Around 23 mph, the fixed pinion feedback vetoes a deficit confirmed by the calibrated wheel target and body motion. At 26–29 mph, the corrective feedback is outside its intended speed range. At 64 mph, repeated speed weighting, interrupted confirmation and wire quantization leave very little additional command reaching the vehicle. Response delay also inflates an instantaneous body-response percentage, but the measured wheel unwind error remains.** These findings explain missing or small correction; they do not establish the complete physical cause or validate a replacement tune.

## Reproduction and scope

Sources: the hash-verified [26-segment acquisition and all-range review](../navigator-post-sustained-drives-2026-10-20/REPORT.md). Full-session causal warmup was retained for both moving sessions, rather than restarting controller history at an incident. Original model, calibration, motion, control/state events and send times drive the actual installed strategy factory. Return probes identify the low-speed branch actually supplying output below 60 mph and the selected high-speed extension.

The instrumented full-session command arrays are **exactly equal** to the previous uninstrumented arrays: 23,001 evaluated sends, including 11,057 active/no-driver frames. The current parent/child remain clean at `0171b897289be53fd62f330935c55825b86c3c3a` / `4167433e5c575f620a9dedf8144a0bc7cba14291`. See [verification](../../navigator-reference/PRIVATE_ARTIFACTS.md). This is an observational mechanism replay, not a new full-corpus safety acceptance run or a vehicle-motion simulation.

Fast saved symptom witness:

```sh
python3 docs/research/navigator-shortfall-unwind-diagnosis-2026-10-20/reproduce.py
```

It reproduces three pre-intervention deficits and unresolved matched unwind. `--expect-tracked` intentionally exits 1 for those saved observations. No command-only change can make frozen recorded vehicle motion into proof of improved handling.

## 23 mph: two feedback definitions disagree, and the old one wins admission

At approximately **<private clock time>–<private clock time> CDT**, before the steering input at <private clock time>, the focused 163.1–165.9 s window contains 2.5 clean turning seconds. Measured response is about 62% of requested body turning. On the actual selected controller frames:

| Feedback definition | Median response relative to its request |
|---|---:|
| Fixed pinion model used by the original low-speed admission | 81.7% |
| Measured wheel angle relative to calibrated, offset-corrected wheel target | 60.1% |
| Wheel curvature reconstructed using the current learned model and roll | 60.4% |
| Calibrated body yaw relative to requested turning | 60.6% |

These rows summarize the same active, no-driver/no-brake/no-signal controller window; the first has a different model definition. Clean 20 Hz metrics and controller-frame metrics have slightly different timestamps, so the body medians differ slightly.

The fixed native pinion model uses the original base ratio and raw steering angle, whereas the application target uses the learned model, offset and roll. The two numbers cannot be compared as interchangeable tracking percentages. This mismatch matters directly because ordinary low-speed admission requires measured curvature below 70% and predicts catch-up from that fixed-model response.

Of 55 controller frames in the window, **44 return `catchup_veto` and 11 remain `waiting`**. The new sustained observer independently confirms the calibrated wheel/body deficit on six frames (164.143, 164.194, 164.593, 164.644, 164.694 and 165.494 s). Every one is nevertheless blocked by the original `catchup_veto`, with `hold_frames=0`. The sustained term explicitly requires the original admission and hold to pass, so adding the allowance did not remove this older gate.

This is **not budget exhaustion or failure to rearm**: ramp area and sustained area are both zero. No curvature-deviation clipping, DBC range clipping or final path-angle slew binding occurs in this window. Inputs pass basic calibrated-evidence validity. Some other frames legitimately fail the new observer's own persistence/recovery checks; fixing the fixed-model gate would not imply unrestricted activation.

Even an admitted term is nearly faded out here: the below-25 speed weight is only approximately **0.026–0.111** across this window. The 0.0025 rad sustained cap therefore becomes at most roughly 0.00028 rad before other caps. This is an additional effectiveness limit, not justification to raise the cap blindly.

### Implication

Use a single, explicitly validated application-frame definition for the experimental admission/recovery evidence, with independent wheel/body agreement. Keep native fixed-pinion safety/shadow feedback separate. Do not globally change the base steering ratio, override the owner factors, or disable predictive withdrawal. A local candidate must demonstrate that persistent deficits admit while genuine catch-up and aborted turns still release.

## 26–29 mph: the below-25 correction cannot address these turns

| Saved window | Clean body response | Other evidence |
|---|---:|---|
| Session 02, 161–167.1 s, approximately 26 mph | 65.4%, 3.25 s | Correction speed weight zero; curvature-deviation clip also binds during part of the rising request |
| Session 03, 254–262.3 s, approximately 29 mph | 83.5%, 8.3 s | Calibrated wheel response about83.3%; no deviation/range/final-slew clipping in this window |

The below-25 feedback is exactly zero at these speeds. Existing broader low-speed **feedforward** remains present; the assertion here concerns the additional error correction, not all low-speed steering code.

At 26 mph, the existing deviation envelope restricts requested curvature to measured fixed-pinion curvature ±0.002/m once speed exceeds 9 m/s (about20.1 mph). In the 161–167.1 s controller window it clips 31 of120 active/no-driver frames. The final saved request reaches about0.01748/m while the bounded request is about0.01430/m. This explains part of the rising-turn shortfall; it does not explain the entire physical under-response. Do not widen or bypass this envelope as a diagnostic shortcut.

At 29 mph, the fixed model reports approximately95.7% response while the calibrated wheel model and body motion report about83–84%. The command reaches the intended current path-angle calculation without range or final slew saturation. These logs cannot establish whether the remaining mismatch is an application-to-EPS mapping error, a load-dependent actuator response or another plant effect. They do show why simply replenishing the 15 mph budget would not fix it.

### Implication

Treat 25–30 mph as a separately evidenced scope change. First distinguish bounded target from planner target and calibrate the application-frame tracking measurement. A candidate extending correction must remain within native deviation/range/slew and exposure limits, fade deliberately before protected ranges, and be tested on entry, sustained demand, reversal, driver input and aborted turns. A global gain increase is not supported by this evidence.

## 64 mph: most computed changes do not change the encoded command

Across both drives, the new policy differs from the preceding policy on **69 floating-point active command frames**. Packing both alternatives through the actual native Ford `CANPacker` changes the path-angle signal on only **nine frames**: eight in the first drive and one in the second. At20Hz, that is about0.45s of distinct command samples in this batch. Sixty of the69 computed changes produce the same encoded path-angle signal as the prior policy.

This corrects a limitation of reporting floating-point changes alone. The new policy did run; its additional wire effect was much smaller. Counterfactual encoding is not a controlled before/after vehicle experiment, and source reconstruction retains the previously documented single half-step tolerance outlier.

### Repeated speed weighting

For the wheel-based unwind extension, `ExtendedWheelTarget._fraction` computes:

- `blend = smoothstep((mph-60)/10)`;
- the wheel `scope` includes that same speed factor;
- the returned fraction multiplies the wheel fraction by `blend` again.

When the older bend latch returns zero during unwind, the wheel extension's speed factor is therefore **squared**. Ignoring other reductions, its nominal15% ceiling becomes:

| Speed | Single speed weight | Maximum wheel-extension fraction after both weights |
|---|---:|---:|
| 62 mph | 0.104 | 0.162% |
| 64 mph | 0.352 | 1.859% |
| 65 mph | 0.500 | 3.750% |

The final70–75mph handoff weight is1.0 here and is not the cause. Curvature/demand scope and wheel deadband can reduce the amount further. Repeated speed weighting is a confirmed attenuation mechanism, not a claim that removing a factor is already a safe fix.

### Confirmation frequently restarts

During clean60–65mph unwinding, the two drives contain198 and124 replay controller frames respectively (alignment differs by one frame from the normalized grid in the second drive):

| Mechanism | First drive | Second drive |
|---|---:|---:|
| Positive requested reduction fraction | 54 | 41 |
| Positive fraction while fewer than five confirmation frames accumulated | 25 | 21 |
| Nonzero final extension residual | 29 | 20 |
| Wheel reason `fresh_wheel_history` | 43 | 33 |

The wheel history is cleared whenever inherited admission rejects body excess, target direction, scope or current wheel excess. Fresh history then requires five samples spanning about0.2s. The update layer also requires five consecutive positive fractions and resets its counter on zero. During a changing exit, short threshold crossings repeatedly force fresh confirmation. The larger49 residual-frame count is still mainly sub-resolution when compared with the previous policy; only seven of these clean unwinding frames change the encoded path signal.

This does not justify treating missing/stale or disagreeing evidence as permission to steer. It suggests separating valid wheel-history collection from **current permission to apply correction**, so valid history need not be rebuilt solely because a conservative body margin briefly crosses zero. Invalid evidence, driver intervention and direction changes must still withdraw/reset as appropriate.

### Delay explains part of the percentage, not all of the wheel unwind

Instantaneous unwinding body response is127.0%/129.4% on the two drives. As a sensitivity check, comparing motion to a request0.262s earlier lowers the medians to112.7%/112.4%; using0.4s lowers them to109.2%/109.0%. These are diagnostic alignments, **not measured actuator-delay estimates or recommended parameter changes**. The target pipeline may already compensate for delay; this exercise does not identify the right control timing.

The wheel itself still exceeds the current calibrated target by a median **0.83°/0.75°** during clean unwind. Thus the residual is not solely a body-yaw artifact. Body yaw uncertainty is correlated and substantial relative to these small acceleration errors; it cannot establish a precise gain by itself. Range and final slew bounds do not bind in the three focused highway windows, so a bigger native slew limit is not supported here.

## What to prototype next, locally

1. **Measurement consistency first:** calibrated application-frame wheel/body evidence for the experimental low-speed admission and catch-up decision, retaining atomic-target checks and separate unchanged native safety feedback. Reproduce the six observer-confirmed/vetoed frames before considering extra exposure.
2. **Separate25–30mph experiment:** explicit bounded scope for observed turn-entry and sustained errors, with planner-versus-bounded-request diagnostics. Do not bypass the deviation clip or infer that the15mph allowance covers this range.
3. **Unwind effectiveness:** apply the intended speed fade once to a bounded wheel trim; collect fresh independent wheel history while all inputs are valid, requiring current wheel/body agreement for actuation. Preserve predictive release, persistence, exposure bounds, abort behavior and the protected high-speed handoff.
4. **Prove the encoded effect:** count actual packed path-angle changes as well as floating-point differences. Validate final residual, release duration and safety acceptance at transitions; frozen replay cannot prove road improvement.

No replacement controller was implemented or integrated in this diagnosis. Before any installation, a proposed candidate needs focused recorded/synthetic tests, full paired safety replay and build checks, including40–50mph parity and protected upper-speed behavior. Existing saved episodes are sufficient to begin that local prototype; no special drive is needed first.

[Detailed episode metrics](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Gate summary](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Verification](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Reproducer](../../navigator-reference/PRIVATE_ARTIFACTS.md)
