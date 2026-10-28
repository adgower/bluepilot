<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Wheel unwind and requested path near the lane-edge intervention

The recordings support the owner's report that steering can carry too much turn around80–85mph. The reported15:19:59CDT episode contains both measured wheel excess relative to its calibrated target and a model-predicted path already biased toward the nearby lane line. However, the final approach does **not** contain an extra software correction holding the transmitted command after demand falls. These are separate findings; neither proves the sole physical cause of the lane-edge event.

Scope: saved logs and installed source only. No SSH, ECU query, CAN transmission, paired-source edit, parameter write or device change. Preserve1.20/0.97 and current geometry/fixed pinion/safety. Scripts and diagnostics here are research artifacts, not a new control implementation.

## Requested → transmitted → wheel

The controlling fixture is `highspeed-session-04`, input at route1081.027305s,<private clock time>.361105CDT. The owner reports apparent oversteer past the lane line plus possible roadside metal avoidance. A tire crossing, object identity and controller causation are not independently proved.

Exact send-time reconstruction in the final2.8s covers56steering frames. Every frame follows the existing baseline formula `path_angle = 1.425 × speed × requested_curvature`, within the0.00025rad half wire step. The unquantized reconstructed formula error is below1e-12rad. There is zero extra high-speed residual and no pending software release. Thus, no software release tail or limiter hold is demonstrated in this window. Transmitted packets are not proof of the EPS's internal applied target.

| Before recorded pressure | Speed | Requested wheel | Measured wheel | Transmitted path |
|---|---:|---:|---:|---:|
|3.05s|84.0mph|2.27°|3.0°|−0.0260rad|
|2.05s|83.6mph|1.91°|3.5°|−0.0225rad|
|1.05s|83.0mph|1.28°|3.1°|−0.0175rad|
|0.25s|82.5mph|0.67°|0.3°|−0.0145rad|

The wheel initially retains/increases turn while request falls, then unwinds below the target before the recorded pressure flag. A single constant delay is therefore not an adequate description of the entire episode. That last unwind cannot be assumed entirely autonomous: the pressure flag is a threshold/debounce signal, not a hands-off detector. Ford uses >1Nm with a five-update debounce. In the analyzed5.8s ending0.2s before the flag, median absolute column torque is0.125Nm and maximum0.6875Nm; low-level human input cannot be excluded.

Do not compare a newer100Hzcontrol value to an older20Hzwire value and call the difference a release tail. The exact send-time audit avoids that artifact. See [incident-audit.json](../../navigator-reference/PRIVATE_ARTIFACTS.md), [timeline CSV](../../navigator-reference/PRIVATE_ARTIFACTS.md), and the retained [synchronized road video](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Measured excess is not confined to the pose-yaw channel

For the same pre-input5.8s window, median calibrated wheel-model/request curvature is162.1%, calibrated body-yaw/request curvature161.9%, and signed measured-wheel minus requested-wheel error1.52°. Comparing current response to demand0.25s earlier still gives154.4% wheel /152.5% body; even1s shift leaves roughly146.7%/147.9%. A simple lag correction does not remove the discrepancy in this window.

The wheel target reconstructs from the atomic learned ratio, stiffness, roll and offset to within about0.0000011° across all analyzed eligible high-speed samples. The logged target is internally consistent; it is not a degree/radian or stale-target arithmetic error in this analysis. This does not certify the learned parameters as physically correct.

The target decomposition is relevant: removing roll/offset from that target reduces median wheel excess from1.52° to0.39°. The combined target shift from roll/offset has median magnitude1.21°. These medians do not add exactly, and this is an algebraic sensitivity, **not** a causal allocation of physical error or proof that adding an offset to the OEM path field is valid. OEM path angle is not steering-wheel angle.

Body yaw is uncertain: median reported yaw std corresponds to roughly0.47m/s² at this speed, compared with median estimated excess0.31m/s². Learned wheel geometry and calibrated body estimates are also correlated through learning; they are not two independent ground truths. No inverse-response gain is justified from these ratios.

## Requested path position

The selected three raw segments contain3600`modelV2`messages and18001`carControl`messages, with no`lateralManeuverPlan`messages. In the pre-input window,98.62%of580active control samples match the latest logged model action curvature within1e-8/m. The90thpercentile difference is0; maximum2.49e-5/m. Small mismatches can reflect independent process receive snapshots. There is no evidence here of a large control-side stale request or alternate maneuver-plan override. See [request-source.json](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The model's predicted centerpoint path is inside its estimated lane curves at all examined0/10/30/50/80m horizons, but biased toward the near line:

| Horizon | Median offset toward left of estimated lane center | Median fraction of lane width from left |
|---|---:|---:|
|0m|0.79m|20%|
|30m|0.78m|21%|
|50m|0.70m|24%|
|80m|0.55m|29%|

At50m, minimum predicted centerpoint-to-left-line distance is0.51m in this window. This is **not vehicle/tire clearance**. Camera/body reference, model uncertainty, vehicle envelope and unsurveyed lane geometry prevent that conversion. The0m prediction describes estimated current position; future points are predictions, not executed trajectories. A near-edge path could contribute to perceived cutting-in, but may also be responding to the vehicle's already displaced position. Causation is unresolved. See [model-summary.json](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Is it just one85mph incident?

No. The other retained fast bends show similar excess, including opposite signed steering:

| Input association | Speed near input | Pre-input median body/request | Wheel-model/request | Signed wheel-target error |
|---|---:|---:|---:|---:|
|<private clock time>, brake/disengagement|83mph|131.9%|135.4%|1.79°|
|<private clock time>, steering pressure|81mph|138.3%|140.9%|1.44°|
|<private clock time>, owner-described lane edge/debris|82mph|161.9%|162.1%|1.52°|

These use up to5.8s ending0.2s before each input, with fresh valid active lane-keeping evidence; they are largely transient windows, not steady-state gain measurements. Individual frames are temporally correlated. Other input groups must not be classified as tracking failures without context.

Across the two faster sessions,70–75mph has5.4s of strict steady support,75–80has1.65s, and80–85has only0.35s; there is no eligible meaningful85–90mph support. The speed labels are approximate, and there is no demonstrated threshold that suddenly changes at85mph. In80–85mph unwind samples, median body response is160.0%/168.2% and learned-wheel response150.8%/152.0% across the two sessions. Route/bank/turn/direction differences confound a universal speed-dependent factor. See [analysis.json](../../navigator-reference/PRIVATE_ARTIFACTS.md) for all60–90mph bands/phases.

## Source implications and next work

1. Above60mph, gentle-curvature baseline feedforward settles at1.425. The owner's0.97 multiplier applies to the high-curvature arm; it is **not selected** in these gentle high-speed samples. There is no new gain step at85mph. Do not alter1.20/0.97 to address this evidence.
2. The existing roll-aware mapping fades out by70mph. Its offset-free roll/target transform is therefore not directly adding command here. The fixed-pinion baseline, learned wheel target and body calibration remain distinct models; their disagreement deserves explicit high-speed target tracking analysis.
3. The high-speed reduction is a guarded trim, not a full wheel-target tracker. Changing its rearm rule alone cannot fix the final approach, where demand is withdrawing and the trim is alreadyzero.
4. Prioritize a **local high-speed calibrated-target/unwind design study**, separating steady mapping bias from excess wheel retained during withdrawal. Preserve fixed native pinion geometry/safety, caps, driver withdrawal, lower speeds and the independent fallback. Test both turn signs, invalid/uncertain calibration, over/under-response, target reversal and already-under-target exit frames. In particular, do not continue a reduction into the last sample where the wheel has already unwound below target.
5. Keep requested-path position as a separate upstream question. Reducing steering globally may worsen lane tracking if the desired path itself is too near the edge; a steering-response fix cannot certify lane margin. Do not add a generic lane-center offset from these unsurveyed model lines.

No control fix is implemented or claimed by this investigation. Existing saved transient evidence supports further local work; ordinary future drives can fill steady70–85mph support when naturally available. No special85mph reproduction or unsafe maneuver is needed. A full637-segment safety replay is not rerun because paired/prototype steering behavior did not change; new diagnostic assertions and source/hash checks are recorded in `verification.json`.
