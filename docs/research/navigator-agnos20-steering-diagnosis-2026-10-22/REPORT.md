<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local steering diagnosis — October 22, 2026

No Comma access or changes. No paired-branch controller edits. Owner 1.20/0.97 unchanged. This is a diagnosis of recorded inputs, commands and measured response, not a validated correction or full safety replay.

## Selector correction discovered during prototype

The above75mph final selection passes through `unchanged.stock.upper_reference`, not `unchanged.upper_reference`. The earlier diagnostic frequencies for the adjacent upper policy were not final-selected reason counts and are withdrawn below. Recorded command matching, observed physical response and actual final trim measurements remain separate evidence. See the [continuity prototype](../navigator-observer-continuity-prototype-2026-10-22/DESIGN.md).

## Main findings

**The highway correction is intermittent, not completely disabled. The 23–24 mph issue combines a software command clamp with correction admission/episode limits. Neither is explained by an AGNOS process failure.**

### 70–79 mph: why excess turning can remain

The production factory was replayed using original control packets and calibration provenance, original motion/model events, and recorded send times. In the focused 71.8–79.5 mph bend, all 284 eligible meaningful send frames reproduce the recorded path-angle command within half a wire quantization step (0.00025 rad). This makes the focused command diagnosis useful without inventing a new calibration packet.

Above75mph, the newest EarlyLowHighOnset policy intentionally selects its `unchanged` predecessor, rather than the new70–75mph onset policy. The predecessor still has calibrated wheel-target trim; this is not a return to unmodified upstream steering. The roll-aware mapping correction is also zero at these speeds by design, so it is not actively injecting the observed high-speed excess.

In the selected75+mph part of this bend:

- 248 eligible send frames, all matching the recorded command within half a wire step.
- Actual command trim is present on73frames, about29.4%, in seven bursts of0.05–0.95s. It is zero on175frames. Across all248frames the median trim is0%,90th percentile6.45%,maximum14.41% of the independent reference path angle. These are command reductions, not predicted road improvement.
- Adjacent-policy diagnostics reported45 `unwind_rising_confirmation` frames and48wheel `fresh_wheel_history` frames, but these are not final-selected above75mph reason frequencies. Do not use them as causal attribution of the final output. The actual selected older wheel-target class also clears wheel history on upstream eligibility withdrawal; prototype tests now exercise that selected layer.
- The wheel observer clears its history whenever upstream eligibility is lost. Once fresh body/wheel confirmation returns it rebuilds five observations, and final trim also requires persistence. This creates repeated delayed admission in the recorded bend. Not every withdrawal is erroneous: absence of current excess, direction/driver/fault/invalid-context guards must remain effective.

The previous review measured123.1% body and133.7% wheel response across14.35 clean seconds in the broader bend. The new trace establishes intermittent trim and its gates, not that changing those gates will produce a specific physical response.

### 23–24 mph: why more gain alone is insufficient

Two replayed pre-input shortfall windows reproduce every eligible send command within half a wire step:

|Window, session10 relative seconds|Eligible send frames|Curvature-clipped frames|Early correction nonzero|Regular/sustained correction nonzero|
|---|---:|---:|---:|---:|
|478–484|54|28|0|0 /0|
|509–513|37|27|0|0 /0|

The early correction declines with `command_deviation_limited` on28/27frames and `episode_spent` on26/10frames, respectively. The application first clips the desired curvature to fixed pinion curvature ±0.002/m above9m/s (about20.1mph). EarlyLow explicitly refuses further early effort when its original intent differs from this bounded command. This is application clipping, not a measured physical EPS torque/angle limit.

The regular calibrated observer also evaluates a wheel target from the curvature passed into correction. During clipping that curvature differs from the original requested curvature used to stamp the atomic wheel target. The target-consistency check can therefore reject an otherwise intact original calibration packet.27/23clipped frames in these windows simultaneously report `invalid_calibrated_feedback`. This is a request-versus-bounded-command mismatch in observer semantics, not evidence that the body yaw sensor or saved calibration has failed.

Clean pre-input physical response remains about48–51% body /53–61% wheel in these windows; delaying the comparison reference explains some, not all. Steering saturation alerts occur nearby. The second window has no rejected echo; the first mode1 rejection is at the subsequent brake transition. These facts identify application-side lost authority/admission before input; they do not establish the vehicle would accept or achieve an unrestricted request.

## Does this support an80–85mph ping-pong feel?

It is plausible that excess turning followed by correction/release feels like repeated corrections. The recorded high-speed excess makes the concern worth treating seriously. **This dataset does not establish80–85mph oscillatory instability.** Maximum recorded speed is about80.0mph, there is only0.05s of clean lane-keeping at80+, and no clean meaningful80–85mph target sample or85mph evidence.

A local screening checks body-minus-request acceleration beyond±0.15m/s² with a corroborating opposite-signed wheel-target residual over0.5degree, persisting at least0.30s, in continuous clean70+mph periods. Broad periods do contain alternating signed errors, but also changing left/right requests and near-zero targets. The same-direction meaningful-demand screen found seven sustained bend islands across the three highway recordings and **zero** persistent error alternations inside those islands. The clearest79mph bend is prolonged excess turning rather than demonstrated left/right oscillation on a fixed bend.

This screening is descriptive, threshold-dependent and not an instability certification. It does not rule out straight-road wandering, an unsampled event, or what the driver felt. Lane-center estimates are model proxies, not measured vehicle edge clearance. Owner tentatively recalls obstacle avoidance without identifying an exact event; no input is labeled a confirmed tracking-failure takeover. No video was reviewed.

## Best next local design work

1. Highway: keep continuously fresh wheel-history observation separate from the decision to apply trim, so a temporarily unmet body-excess margin need not discard all valid wheel history. Require current independent body/wheel excess before applying anything. Evaluate admission/release hysteresis and the70/75mph handoff with fixed bounds, abort behavior and genuine turn reversal tests. Do not simply extend the70–75mph patch upward or increase gain.
2. Low speed: distinguish original requested path, feasible bounded command and measured motion explicitly. Validate original wheel/calibration evidence against original intent, then separately classify lack of command headroom. Evaluate earlier bounded admission/rearming only where headroom exists. This must not turn a target-consistency repair into a bypass of the deviation envelope or an unlimited error integrator. Fully clipped parts cannot be promised to achieve the original request under unchanged limits.
3. Keep1.20/0.97 intact and preserve unrelated speed output. A candidate would need new recorded-command replay, transition/reversal/driver-abort tests, native safety replay and build checks before any installation consideration. No candidate was implemented or full safety replay claimed here.

## Evidence and limits

Production strategy replay: session10 has15,240active/unpressed/mode1frames,99.9278%within half a wire step; session11 has23,627suchframes,99.8349%within half a wire step. There are11/39mismatchframes outside the focused eligible windows; their scheduling/input-order discrepancy is unresolved. Do not claim bit-identical full-route replay or use mismatch frames as proof of controller behavior. All91focused low-speed and284focused highway eligible sends match.

`replay.py` exercises the real current factory with frozen recorded inputs and no sockets. `summarize.py` reproduces the recorded clamp/admission/intermittent-trim facts. It is not a closed-loop physical test: changing a command on recorded motion cannot prove that the vehicle will follow differently. A physical-response regression seam is unavailable in this local frozen replay.

Source references:

- [Software curvature clamp](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Original target versus bounded command gate](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Calibrated feedback consistency](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Wheel history reset on eligibility withdrawal](../../navigator-reference/PRIVATE_ARTIFACTS.md)
- [Final policy selection outside70–75mph](../../navigator-reference/PRIVATE_ARTIFACTS.md)

Artifacts: [blocker summary](../../navigator-reference/PRIVATE_ARTIFACTS.md), [command replay10](../../navigator-reference/PRIVATE_ARTIFACTS.md), [command replay11](../../navigator-reference/PRIVATE_ARTIFACTS.md), [broad oscillation screen](../../navigator-reference/PRIVATE_ARTIFACTS.md), [same-direction screen](../../navigator-reference/PRIVATE_ARTIFACTS.md). Frozen source pair26b3416a6/fe59e503. No network/device mutations or branch changes.
