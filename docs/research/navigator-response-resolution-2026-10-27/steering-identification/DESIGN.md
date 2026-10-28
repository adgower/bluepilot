<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Original steering request → reported ECU angle assessment

Status: dataset/design before fit. Offline only; no controller/reference mutation.

## Data feasibility and ownership

Use nine original post-regression signal captures (79 segments), plus the already-extracted original coordinated-coast session05 (21 segments) for independent calibration coverage. Sendcan0x3d6 path/mode are original published applied-command requests; they are not proof of ECU consumption. RawCS compensated pinion-angle is the response estimate, not independently measured physical steering truth. No yaw/body-derived wheel curvature is used as a label.

Available publication-level guards give installed08 ~791.8 seconds, including84.7 seconds35–50mph. They are provisional: existing JSON omits carState vehicleSensorsInvalid and actual last angle CAN-event age. Targeted original100segment extraction supplies receive-CAN0x7e time, StePinComp_An_Est and its QF(3), plus CS envelope/sensor-invalid flags. Exact decoder is checked against the installed DBC parser. The CAN event time is a host receive clock, not the unknown internal ECU measurement time.

Original valid atomic cc.steeringAngleDeg equals navigatorCalibration.targetAngleDeg in available qualified rows. This is a desired model-derived target BEFORE final Ford deviation/roll/trim mapping, not an identified physical feedforward gain. There is no certified path(rad)→pinion(deg) conversion; empirical inputs will retain actual path, path/v and path*v alongside original target prefixes. Owner1.20/.97 is unchanged and no gain is inferred from wheel/body ratios.

Whole-session split chosen from coverage before fit: train new01–04; calibrate prior coordinated-coast05; test new05/06 and installed08. New07/09 have no assisted moving examples and are not scored as easy stationary cases. New02 supplies most training35–45 coverage; quantify this concentration and unsupported cells.

## Qualification

Require mode1 original requests, active valid original CC with valid atomic target, drive gear, CAN validity/no steering faults, fresh CS/CC/calibration/Panda, healthy controlsAllowed, no driver steer pressure/raw torque above installed allowance, no pedals or turn signal, and preceding1s free of such intervention. Use raw angle QF3/envelope valid, exact past receive-CAN age, and no invalid sensor prefix. Exclude the declared planned-maneuver interval in08 conservatively. Every outcome is the recorded compensated-angle estimate. No future response threshold selects examples.

## Two distinct timing problems

1. Ordinary forecast: at origin t, only past state/commands/target through t−margin may predict ECUangle at t+h. No future commands are features.
2. Association-time retrodiction: at label/association time t, initial angle/rate are taken at t−H and its earlier history; the ENTIRE KNOWN original command/target/speed prefix [t−H,t−sourceMargin] is legitimate input. No angle after t−H is used in this response-kernel model, and no post-label command is used. This is not a future-input oracle relative to inference time. Evaluate source margins20 and50ms because internal sensor/transport delay is not certified.

Retrodiction is the primary moving-reference-association assessment. A separate recent-angle persistence/rate baseline may use data≤t−margin, but already absorbs intermediate response and is not an untrimmed counterfactual explanation.

## Transparent comparisons and uncertainty

Fit regularized linear finite-history response models for ΔECUangle, with initial angle/rate/speed plus:
- state persistence/rate baseline;
- initial state + original nominal atomic-target/speed prefix;
- the same inputs plus ORIGINAL actual applied-path prefix and speed-basis terms.

Train-only scaling/imputation, calibration-only regularization and residual bands, then whole held-out sessions. Report angle errors in degrees, QF/age and35–50/50–70/direction/turn-rate support. Nonoverlapping temporal-block uncertainty and training-session jackknife test whether added actual commands explain response beyond state/target correlation. Quantify command innovation after state/target and covariance/collinearity; do not call regression coefficients a causal actuator G or delay.

At an original held-out prefix, make an OFFLINE ≤5% toward-zero path perturbation, quantized within0.0005rad and never exceeding5%, leaving the initial state and original target fixed. Compare its model-predicted effect and jackknife direction to the empirical held-out residual envelope and0.1deg sensor resolution. This is an observability/sensitivity probe, not observed trim truth or a generated command used as plant data. If perturbation is outside conditional command support or uncertainty exceeds its predicted effect, moving-reference null versus responsive trim is unvalidated.

No current replay reference/candidate stream, synthetic body/wheel ratio, post-label command or modified physical response is admitted as training data. No new model is used in the controller. If uncertainty or confounding remains too large, freeze the quantitative blocker rather than fit more variants until an apparent G appears.
