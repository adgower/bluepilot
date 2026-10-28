<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator 20–40 mph understeer and wandering — local investigation

2026-10-14. Used the 45 already-copied rlog segments from three drives. No SSH/device access, parameter writes, ECU queries, deploy, or controller-source changes in this investigation. Both isolated implementation repositories remain clean at the previous pinion-option commits. Factors 1.20/0.97 remain intact.

## Conclusion and repair target

The data separates two problems:

1. **Biased feedback sometimes alters steering correction direction.** The local pinion option removes the extra command sign crossings induced by the yaw-based deviation clamp in these recordings. It is a plausible improvement for some wandering, not proof that all felt wandering is explained.
2. **Low-speed command-to-response conversion undertracks even without clipping.** The primary remaining repair target is the Navigator-specific curvature-to-path-angle map in `opendbc/car/ford/lateral_angle.py`. Correcting feedback alone does not repair this map. Increasing the existing tighter-turn factor alone misses most newer low-speed commands.

A deployable numerical calibration is not established. Do not infer a multiplier by taking the reciprocal of observed actual/requested curvature: changing commands changes the subsequent planner, vehicle, and feedback response.

## Reproduction and discrimination

`extract_full.py` processes complete local logs chronologically, retains the latest recorded state, and executes the actual LateralAngle strategy at its 20 Hz cadence. It captures planner action, carControl curvature and desired steering angle, actual wheel angle, calibrated motion, saturation reporting, and controller limiter stages. `summarize_full.py` and `verify.py` reproduce and verify the observational shortfall. This is a deterministic recorded-input diagnostic, not a closed-loop symptom reproduction or a fix-verdict test.

Latest drive, stronger turn at 107.5–112.7 seconds:

- Approximately 27.7 mph.
- Independent motion/requested curvature median ratio **0.606**.
- Calculated desired steering wheel angle median **−14.53°**, actual median **−10.0°**. Median paired absolute tracking error **4.18°**; the difference between separate medians is not the paired median.
- Upstream angle-saturation flag true for **75.96%** of these frames. This flag is an angle tracking-error indicator; it is not proof of an EPS torque limit.
- Planner model action and carControl curvature have zero median difference. The request reaches the downstream conversion.
- **Zero deviation clipping and zero path-angle limiting** in this window. Pinion substitution has no meaningful command change here.
- Exploratory motion offsets of 0.2/0.5/1 seconds do not recover the request ratio; this argues against a simple timing shift explaining this example. It is not a full identification of actuator dynamics.

The gentler ~28 mph example has motion/request ratio ~0.75 in the full trace, versus ~0.72 using prior nearest matched/downsampled inputs. Selection and timestamp differences account for the small variation. It mostly uses the gentle arm and has very little clipping; pinion changes only a small part of its commands.

Across all valid/no-driver selected frames in the complete logs, path-angle limiting was zero in every 20–30, 30–40, and 40–50 mph bin. That includes both rate and DBC range effects. Some deviation clipping remains separately. Median actual/request ratios aggregated over bends are exploratory because route, turn direction, acceleration, roll, demand changes, and near-zero signals differ. The earlier route provides 24.2 seconds of selected 30–40 mph data; the newer routes provide only 0.15 and 5.9 seconds. This is not strong matched evidence for every speed throughout 20–40 mph.

## Why the existing tuning misses part of the issue

Below 13.5 m/s (~30.2 mph), gentle-curvature gain is **1.0**; tight-curvature gain is **1.30 × 1.20 = 1.56**. The 0.97 factor sets the high-speed tighter-turn endpoint. The newer drives use the gentle arm for **77.08%** and **75.09%** of selected 20–30 mph frames. The earlier route has more tight turns and uses it for 48.15%.

The gain blends across |curvature|=0.0007–0.001 /m. Because the gain multiplies curvature, the incremental sensitivity is not merely the interpolated gain: at the blend center below ~30 mph, d(command/speed)/d(curvature) is **2.867**, versus 1.0 on the gentle arm. This follows directly from the source math. It amplifies small changes near that transition, making this a plausible contributor to inconsistent correction strength. It does not demonstrate closed-loop instability.

Changing 1.20 to 1.25 yields at most **4.17%** more tighter-turn command at low speed, and **0%** more gentle-arm command. It therefore cannot address the identified broad low-speed calibration issue by itself.

## Wandering evidence and its limits

Held-input pinion replay at the full extracted controller cadence produces:

| Drive / speed | Request sign crossings | Current command crossings | Pinion command crossings |
|---|---:|---:|---:|
| Earlier / 20–30 mph | 59 | 73 | 59 |
| Newer 1 / 20–30 mph | 60 | 62 | 60 |
| Newer 2 / 20–30 mph | 30 | 36 | 30 |
| Newer 2 / 30–40 mph | 1 | 3 | 1 |

Pinion eliminates the extra net command crossings in these selections. The direction counts use the controller's floating-point path-angle output and are sensitive to near-zero values and encoding. They do not measure lane departure, oscillation frequency, or felt steering-wheel motion. Raw controller sign crossings alone cannot establish the user's exact wandering episode, since that episode was not identified. Path-angle radians are also not steering-wheel radians.

## Source-level explanation

`openpilot/selfdrive/controls/controlsd.py` computes a desired curvature and, through LatControlAngle, a desired wheel angle using learned ratio, stiffness, roll, and angle offset. The angle controller reports tracking error/saturation but does not add a PID correction.

The fork's Ford CarController angle path consumes `actuators.curvature` and uses LateralAngle's **curvature × speed × gain** map. It does **not** consume `actuators.steeringAngleDeg` to generate the wire command. Measured curvature currently acts as a deviation bound and shadow safety feedback; it is not a continuous tracking-error correction. This establishes the missing software correction path, not the design of the proprietary PSCM's internal control loop. Existing saved PSCM status did not indicate a continuously reached limit in selected low-speed turns.

## Concrete next local change to evaluate

Keep the pinion option and paired safety code as the feedback correction, preserving its OFF baseline and existing safety limits. Separately prototype a **Navigator-only low-speed response calibration**:

1. Give gentle corrections their own low-speed calibration rather than leaving their gain at 1.0 while only boosting the tight-turn arm. Keep the owner's 1.20/0.97 constants intact; expose any additional calibration separately so its effect is auditable.
2. Smooth and broaden the narrow curvature-dependent transition, checking its *incremental* gain as well as its endpoint gains. Avoid a schedule that alternates weak and disproportionately strong corrections around one curvature threshold.
3. Calibrate tighter-turn response separately: the strong turn already uses gain 1.56 and still undertracks. A gentle-arm change alone will not repair it. Compare a speed/curvature feedforward calibration with a bounded tracking-error correction, using independently calibrated motion to cross-check learned wheel-angle estimates. Do not introduce an unvalidated integrator or use the biased CAN yaw for error correction.
4. Fade additional low-speed calibration to zero by the satisfactory ~45 mph region, and verify byte-identical commands there. Preserve override behavior and native safety checks. Replay every candidate's RX/TX; discard candidates with incompatible safety behavior rather than widening safeguards.
5. Evaluate steady turns of both signs and correction reversals, not just aggregate ratios. Saved inputs can verify command changes and safety compatibility. Only subsequent vehicle response evidence can determine whether a candidate fixes understeer without increasing wandering.

The source location and the kinds of changes needed are now clear. The best final gains, transition width, and any tracking-correction terms remain unproven; these recordings are insufficient to certify them as a handling fix. No further controller modification was made under this investigation-only request.

## Artifacts

- `analysis.json`: matched prior samples, selected-window timing offsets, exact command-map sensitivity.
- `full-trace.json`: anonymous numeric signals from all 45 local segments, with no location/VIN fields.
- `full-summary.json`: full-trace bins and selected examples.
- `pinion-reversals.json`: held-input pinion direction comparison.
- `extract_full.py`, `analyze.py`, `summarize_full.py`, `pinion_reversals.py`, `verify.py`: rerunnable local diagnostic.

Verification: `verify.py` passed. It verifies the observed diagnostic claims, not a proposed road fix. Previous pinion native safety replay is documented separately in `navigator-pinion-implementation-2026-10-14/REPORT.md`.
