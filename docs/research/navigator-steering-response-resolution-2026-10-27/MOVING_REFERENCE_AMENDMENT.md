<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Moving-reference response observability amendment

Design for review before further controller code. Current frozen focus remains3trials/0associations/3target-drift aborts; no full737selection.

## What the focused evidence establishes

The absolute0.5degraw-angle anchor check wrongly combines known live requested-curvature motion with unexplained calibration/reference drift. Exact atomic producer snapshots show:

|Trial|Raw angle change deg|Curvature-driven component deg|Fixed-start-curvature calibration/speed component deg|
|---|---:|---:|---:|
|1|−.79465|−.75526|−.03938|
|2|−.70801|−.74124|+.03323|
|3|+.51276|+.33496|+.17779|

The raw requested curvature moves only1.60–3.68%, within the same15%episode. A corrected reference contract must keep the live raw atomic request, actual selected feasible reference and a fixed-start-curvature calibration/speed basis separate. Only unexplained basis/provenance drift should trigger the0.5degassociation-consistency check; increasing its numerical threshold would not resolve the semantic error.

## Why basis compensation alone cannot authorize maintenance

The current response test compares directional actual-angle movement with net target displacement plus0.2deg. Under an unwinding request, an actuator that follows only the original feedforward can move toward target without responding to the new optional correction. A static gain or delayed baseline response can produce an apparent positive residual innovation. Stationary/wrong-direction controls are necessary but insufficient negative controls: the key control is a moving-reference actuator with **no response to the optional correction**.

For a linear target ramp`theta(t)=theta0−r*t`, a constant correction effect after the ramp can be exchanged with unknown delay: `g*theta(t−(tau+d))−q = g*theta(t−tau)` when`d=q/(g*r)`. Thus plausible different delay/actuation hypotheses can produce the same post-action observation. Pre-action history may narrow such hypotheses only under an identified/bounded response and disturbance model. Current angular quantization, atomic model consistency, body coherence and snapshot freshness do not supply that incremental gain/delay/confounding bound. Wheel/body ratios must not be promoted to one.

## Correct association interface

A genuine moving-reference association needs a justified envelope of baseline target-driven movement over the **entire target trajectory**, including its delayed effects, plus sensor/target/calibration uncertainty. New response is distinguishable only if observed directional innovation lies outside that envelope in the correction-consistent direction. The envelope must have an explicit source/model/provenance and validity domain. Merely subtracting instantaneous/net target movement or using reported yaw standard deviation as angle-response uncertainty is invalid.

No such envelope is present in the current stamped production tuple or identified by the saved replay. A research-only optional provider could supply a known envelope in synthetic models; absence/unsupported delay or calibration means WAIT(no association), bounded trial exposure, then RELEASE/LOCKOUT—not guessed maintenance. This would be an explicit missing contract, not an installable closed-loop solution. Native packet acceptance is not an actuation acknowledgment.

## Falsifiable next check and stop condition

Before another focused trial, test a live moving raw/selected target with(1)stationary output,(2)wrong-direction output,(3)baseline-feedforward-driven output ignoring optional trim, and(4)known genuinely correction-responsive lagged output. Raw-curvature episode identity remains original; no second action, gain/uncertainty relaxation or wholeFFhold is allowed. Unknown delay/input-driven motion must not acquire an association solely through reference movement. Reversal/unwind/rising target histories must be included.

If only an externally supplied, bounded synthetic response model separates(3)and(4), retain the architectural progress and report moving-reference response observability as the concrete blocker. Do not rerun737segments or tune an input-motion threshold to manufacture source maintenance. The existing235unit checks/finite supported stresses and focused native compatibility remain their exact completed evidence scopes.

## Revision contract accepted for staging

A separate `moving-reference-contract/` revision will fix the proven basis bug without claiming a supplied actuator model. `basis_angle` is the current atomic-calibration/speed model evaluated at the original trial curvature. Its0.5degconsistency guard is distinct from the live raw atomic target; ordinary requested-curvature movement is not a provenance failure. The entire post-generation target/nominal-command movement is retained, not merely net endpoint displacement. When that reference moves and no validated dual-prefix model is available, the transaction explicitly remains WAIT, then expires/releases/locks out. No one-sided heuristic is promoted to maintenance.

A real future provider must supply calibrated predictive envelopes for both the nominal and actually corrected **known causal command prefixes**, use only inputs preceding the observation by a justified source margin, require observations consistent with corrected-command response and inconsistent with nominal response, and reject overlapping/out-of-model/ambiguous cases. Relative innovation alone can be positive for stationary/wrong-direction observations under a rising nominal target; the initial analytic probe demonstrates that caveat and is not controller clearance. No provider is integrated in this revision.

`state_ns`in the frozen prototype is carState **publication** time, not ECUphysical sample or even exact last0x7eCANreceive time. The frozen focus's0associations must not be reinterpreted as proof of post-generated physical angle freshness. A stronger research association contract needs `AngleReceipt(received_ns,quality,value)`bound to the actual value used by the carState snapshot. It identifies a received ECUestimate, not its unknown internal sampling/filter delay. Missing/invalid receive identity cannot authorize a response association. Synthetic fixtures may supply their explicitly known observation time; original saved streams require separate raw0x7eextraction/binding. No such field is silently assumed to exist in production transport.
