<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Joint planner, integral and actuator investigation

October 24, 2026. Local saved-data work only. No Comma contact, ECU queries, CAN transmission, source integration or installation.

## Result

A coupled software replay now reproduces the latest installed drive exactly at the tested longitudinal seams. The integral interacts with brake release and planner target changes, but **neither integral prototype passes the broader replay acceptance**. Disabling the integral is also unsuitable: fewer switches coincide with substantially more brake-command time and another simulated timeout. Do not install these experiments as a pulsing fix.

The useful next direction is the Ford actuator/coast/release response, using original OEM and Alpha commands. A preliminary response model is not accurate enough to support closed-loop comfort claims or reliable simulated pressure clearance. This is a concrete model-validation failure, not a request for more uncomfortable Alpha highway drives.

Paired source remains parent `74eaa6a60d344f141d06da16f4dbe10d3de49c0e` / child `3a5fe9fe5a296d44b7f898b580c2d3afafe6bfd1`, with steering constants 1.20/0.97 unchanged.

## Inputs and baseline fidelity

Freshly re-read and hash-checked 61 saved rlog segments from the latest Alpha session and two preceding sessions. Extracted full-rate serialized vehicle state, control, pose and calibration, consumed planner references, PID telemetry and received brake/propulsion torque. Raw route identities and payloads remain private.

The steering provenance packet already contains `navigatorCalibration.stateMonoTime`. That identifies the exact vehicle-state message used by each producer. `controlsState.longitudinalPlanMonoTime` identifies its consumed planner message; `ufAccelCmd` matches that planner target during PID. Publication ordering pairs PID telemetry immediately before its CarControl.

| Verification | Result |
|---|---|
| Actual LongControl, one-step replay using recorded prior integral | All 353,281 checked updates match acceleration and integral within 1e-5 |
| Latest-drive full-history coupled LongControl + CarController | All 135,449 recomputed producer outputs/integrals match within 1e-5 |
| Latest-drive returned software feedback | All 67,687 callbacks match brake, gas, fault and reason; gas tolerance 1e-5 |
| Active latest-drive producers missing atomic inputs | 0 |
| Older active producers missing atomic inputs | 5 at the recording boundary in older session 01 |

The full-history replay does **not** reseed the integral each cycle. Its own emitted controller feedback feeds subsequent producer updates, becoming available only at the recorded output publication time. Planner targets, driver inputs, vehicle motion, pressure/torque and pose remain recorded/frozen.

Historical drives used older installations. Running the current paired stack with its own feedback against those historical physical responses is a stress counterfactual, not exact reproduction of the historical installation. Current-stack baseline itself produces different release-fault episodes there. Those differences are retained and must not be described as newly observed road faults.

Code: `extract_joint.py`, `validate_inputs.py`, `joint_replay.py`. Coverage: `coverage.json`. Previous cached Alpha audit reaches about 73.8 mph, with no valid Alpha exposure at 75–85 mph. Five-mph bins organize evidence; they are not separate tunes.

## What the combined trace shows

1. The actual LongControl request equals the planner feedforward plus integral, subject to the existing limits. The replay does not reveal a hidden fixed 62 mph limit or lost acceleration request in that path. It preserves model/radar/stop targets; it does not force cruise speed past model slowing.
2. Existing anti-windup requires `target >= 0`, even when the **resulting controller request is positive and is being withheld**. If the planner target crosses slightly negative while accumulated correction keeps the controller request positive, that condition permits more positive integral growth. The latest drive contains 1,565 such updates, and both older sessions contain the pattern too (1,506 and 1,840 updates). These are approximately 100 Hz control updates, not that many distinct incidents.
3. That growth cannot simply be classified as unnecessary. Suppressing it wholesale can prevent enough correction to complete release, keeping brake requests active longer. Some correction is compensating the actuator/reference behavior rather than merely adding noise.
4. Observed brake release is not instantaneous. For uncensored latest-drive releases in the 50–70 mph bins, median decision-to-received distinct-sample clearance is approximately 147–158 ms. The 60–65 mph observed maximum is about 361 ms. Other attempts are censored by command reapplication, override or disengagement. The existing original-drive 47.7 mph timeout remains in the exact baseline.

These timings include CAN scheduling and filtering; they are not isolated ECU response delays. Reapplication censors a release attempt. Clearance analysis uses distinct samples spanning at least 40 ms and at least three samples, rather than assuming three consecutive raw packets necessarily span 40 ms.

Received propulsion torque, an inactive propulsion request and a valid negative acceleration request are different signals. Prior OEM evidence already shows that negative requested acceleration may coexist with positive engine torque. A sign-only assumption that negative demand necessarily requires friction braking is not supported. See the existing `navigator-coast-transitions-prototype-2026-10-23/REPORT.md` OEM comparison.

## Prototypes and outcomes

All adaptations are research-only Python policy seams over the actual controllers. Neither changes model targets, the grade map, integral gain, steering, physical clearance thresholds or the one-second timeout.

### Output-aware integral freezing

Removed the planner-target sign requirement while retaining the existing fresh/valid feedback, positive controller demand, limited output, no actual-brake, phase, speed and positive-error conditions.

The minimal actual-LongControl regression goes red on the installed policy and green with the experiment. The full coupled replay nevertheless rejects it as an overall fix:

| Latest-drive bin | Baseline rapid reversals → experiment | Baseline brake-command seconds → experiment |
|---|---:|---:|
| 50–55 mph | 7 → 6 | 28.7 → 35.5 |
| 55–60 mph | 23 → 27 | 61.4 → 100.1 |
| 60–65 mph | 31 → 16 | 53.7 → 71.5 |
| 65–70 mph | 10 → 18 | 50.0 → 58.2 |

These are software commands against frozen motion/pressure, not observed physical candidate braking. Disappearance of the original timeout in this counterfactual does not prove an ECU-release repair: changed release demands and brake holds alter whether the old pressure trace starts a timer.

### Release-request anchor

Allowed ordinary integral recovery up to the positive request that began an actuator-limited window, then froze further positive growth. The anchor resets with invalid/unlimited feedback, owner/context changes and inactivity; it is not an added acceleration command.

This passes focused recovery and physical-feedback guard tests, but the full coupled replay creates earlier release timeouts in the latest recording, around 59.5 and 66.0 mph. It is rejected. Reduced edge counts after a prototype disengages are **not** counted as a comfort improvement; comparisons use common healthy-active samples and availability failures remain separate.

### Integral-disabled diagnostic

Zero integral gain is an ablation, not an installation candidate. In the latest 55–60 mph bin it reduces rapid reversals 23→7 but increases brake-command time 61.4→108.2 seconds. In 60–65 mph, reversals fall 31→5 while brake-command time increases 53.7→110.6 seconds. It also produces another simulated release timeout. Thus fewer switches alone does not establish coasting, smoother physical control, faster acceleration or better efficiency.

## Actuator-response identification check

A simple autoregressive command-to-received-torque model was fitted on the first 65% of eligible latest-drive time and tested on the later 35%, separated by a two-second boundary gap. A second version separates braking, inactive-propulsion release, valid nonpositive propulsion/coast request and positive drive modes. One-second held-out rollouts use known **original** commands; they never consume future measured torque as a predictor.

| Held-out one-second rollout | Single model | Mode-separated model |
|---|---:|---:|
| Propulsion torque RMSE | 95.7 Nm | 90.7 Nm |
| Brake torque RMSE | 46.9 Nm | 45.3 Nm |
| Predicted-clear samples while received brake torque was >4 Nm | 25 | 37 |
| Predicted-held samples while received brake torque was <=4 Nm | 880 | 112 |

The mode-separated model is a useful reduction in false holds, but its **37 false-clear samples** remain unacceptable for a simulated clearance claim. These are sample counts, not 37 independent release incidents. The 4 Nm boundary is the existing observer's threshold, not a newly validated physical standard. This diagnostic is never substituted for actual received torque or used to grant propulsion.

Small one-step error (about 5.2 Nm for brake torque) hid much larger one-second drift. The simple models fail even with the original commands, before asking them to simulate candidate vehicle motion. A new-controller comfort claim from these models would therefore be unsupported. Only one session was used for this identification experiment; no cross-route generalization is claimed.

## Replay and contract checks

- **15 focused contracts pass.** Two original sign-boundary regressions were observed red before the experimental policy. Actual LongControl + CarController integration tests retain the one-second timeout under persistent pressure and require real distinct-sample clearance before positive propulsion. Anchor recovery/reset tests pass.
- Native hook replay covers all **61 saved segments**, including recorded RX, all original non-ACC TX and native timer progression. It replaces **179,133 ACC slots**, with **14,338,901 received and 429,929 transmitted packets per variant**. The anchored prototype adds **zero native rejections**, no relay faults and no forced controls permission. Existing rejections are retained, not described as zero absolute rejections.
- The native library was compiled from current source with the existing Ford parameter 11/debug path. As in the preceding investigation, macOS cannot load the UBSan runtime; the normal native build was used. No sanitizer coverage is claimed.
- Passing native packet checks does not validate ECU release, candidate availability, physical braking or comfort. The anchored experiment fails the software availability screen despite passing those packet checks.
- No ARM/product build or hardware test was requested or performed for these unintegrated research adapters. Paired source and device are unchanged.

## Decision and next work

**No candidate is selected for paired integration.** Keep the exact baseline and all counterexamples; do not lengthen the timeout or loosen physical clearance to make the prototypes pass.

The next useful work is a validated Ford command-to-torque/release model, checked against original OEM as well as Alpha traces, especially the distinction between an inactive request (-5), a valid coast/deceleration request, retained brake pressure and propulsion torque. Include release deadband/hold behavior and transport delay; validate multi-step response and rare release events on held-out routes before using a simulation to rank controller changes. Keep the real received-pressure guard authoritative regardless of simulation quality.

The evidence does not support another global integral/gain reduction, nor does it show that current data are exhausted. No extra uncomfortable Alpha high-speed drive is needed to reject the prototypes tested here. 75–85 mph remains a later validation gap.
