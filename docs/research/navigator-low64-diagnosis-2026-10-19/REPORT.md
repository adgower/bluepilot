<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local15mph and64mph mechanism investigation — October19,2026

**Two software constraints are reproduced: the15mph sustained-error correction is admitted but immediately exhausts its shared transient budget; the64mph policy deliberately blocks additional reduction during an unwind. The new70mph+wheel-target policy leaves this64mph behavior unchanged.** These explain missing correction, not a complete physical root cause or a proved handling fix.

No SSH/device access, production source changes, parameter writes, branch integration, installation or CAN transmission occurred. Owner1.20/0.97,geometry,pinion/native safety and exact paired source remain unchanged.

## Reproduction and evidence limits

Sources are the immutable103-segment download in the [drive review](../navigator-post-wheel-target-drives-2026-10-19/REPORT.md). Full causal warmup was retained for sessions04,05and11, not just the flagged seconds. The actual installed classes and original atomic control/model/calibration/motion events were executed at recorded send times. Python function-return probes inspect only the low-speed baseline and installed high-speed branch actually supplying output below70mph.

All replay arrays match the previous uninstrumented whole-session arrays exactly. Active packets match recorded wire encoding within half a0.0005rad step. [Verification](../../navigator-reference/PRIVATE_ARTIFACTS.md) confirms9diagnostic assertions plus exact source HEADs and clean paired working trees. This is a focused diagnosis, not a new full-corpus policy acceptance run. No controller change is being claimed.

Fast reproducer after cached traces exist:

```sh
python3 docs/research/navigator-low64-diagnosis-2026-10-19/reproduce_blockers.py
```

Outputs31valid low-speed frames/0extra correction,14body-confirmed high-speed frames/0extra reduction and BOTH_SAVED_BLOCKERS_REPRODUCED. `--require-correction` deliberately fails on these recorded blockers; it is not a physical closed-loop success criterion. Fresh actual-policy replay is `trace.py wheel-session-11` (project venv; other labels04/05). [Layer summaries](../../navigator-reference/PRIVATE_ARTIFACTS.md) and per-session episode CSVs preserve the probes.

##15mph: admission succeeds, budget removes the term

At13:14:14.70–<private clock time>.20CDT,14.8–15.0mph, previous clean analysis shows46.5%body response and46.5%learned-model wheel response, median21.7°wheel shortfall. Fixed native pinion response is57.2%of request, illustrating that fixed pinion and learned/calibrated wheel models are different. Both remain below target; body-yaw disagreement alone cannot explain this episode.

The precise command sequence is:

| CDT | Admission | Extra path angle | Cumulative budget use |
| --- | --- | ---: | ---: |
|<private clock time>|steady|0.001495895rad|0.000071712rad·s|
|<private clock time>|steady|0.002886224rad|0.000217961rad·s|
|<private clock time>|steady|0.000648809rad|0.000250000rad·s|
|Following31episode frames|ramp_limit_reached|0|budget spent|

Three20Hz command frames (about0.15s exposure,0.10s between first/last) use the entire0.00025rad·s budget. In all31subsequent episode frames, context/feedback are valid, the persistence test admits a positive upstream correction, and the budget wrapper returns zero because remaining area is zero. This is not failure to activate the setting, a stale input, a native range/slew ceiling, or a transport rejection in this window.

The term before budget limiting reaches its existing0.0075rad ceiling; at a representative0.11945rad feedforward that is only6.3%extra command. It cannot be interpreted as enough effort to recover the entire observed54%response deficit. A recorded command-area budget is neither EPS torque authority nor a physical response model.

### Why rearming alone does not solve this recording

BudgetedTrackingPrototype marks ramp_episode during a catch-up prediction exception, and later steady terms also spend that same budget until a continuous valid quiet dwell clears it. The first flag is set near13:11:43.779 at10.5mph even though no correction is then delivered. The installed implementation never rearms in this route; longest qualifying dwell is0.851s versus required1s. A0.1°wheel step at16mph changes measured curvature by0.0000278/m, exceeding the adjacent slope allowance0.00000956/m and clearing that dwell.

We replayed the previously saved **ResolutionAwareRearm** research class, unchanged, in the exact selected baseline slots. It successfully clears the earlier flag once at route198.931s. However, a **new catch-up exception at13:14:07.480** sets ramp_episode again. The subsequent steady correction is still charged to the same small budget and exhausts it in the same three frames. All8,394recorded candidate commands remain unchanged. Thus resolution-aware rearm is a real signal-handling improvement but **not a fix for this15mph episode**. No gain/budget was increased and no candidate was installed.

### Lag and model checks

Delaying requested wheel angle by0.291s changes median error21.65°→20.47°; at0.6s it is still18.90°. The main deficit is not ordinary delay alone. A later short reversal at13:14:19is different: its20.65°error falls to0.78°at0.6s lag. Do not pool that reversal with sustained deficit or derive an inverse gain from either ratio.

**Next design target:** distinguish bounded continuing steady-error correction from the transient rising/catch-up exception budget. Preserve the current caps, fresh-context and motion checks, same-direction observed response, catch-up withdrawal, driver override,25mph fade and independent total-exposure/repeated-cycle limits. Simply refilling the existing budget, removing its bound, or multiplying gain by100/46 is unsupported. Whether additional bounded command actually improves wheel tracking still needs an explicit local candidate, adversarial/full replay and later physical validation.

##64mph: an unwind latch blocks reduction, not a stuck command

Three saved windows reproduce the same mechanism:

| CDT | Window | Body / calibrated wheel response | Blocking frames |
| --- | ---: | ---: | ---: |
|<private clock time>|0.75s|156%/155%|14body-confirmed unwind-latch frames;1body-history frame|
|<private clock time>|1.15s|161%/174%|20unwind-latch frames;3near-neutral/direction frames|
|<private clock time>|0.55s|149%/146%|9unwind-latch frames;2eligible but not past persistence|

Existing HighSpeedReduction latches after demand falls below90%of the admitted bend peak (or raw demand below80%). It then requires five confirmations above102%of the **old peak** to rearm. During a continuing unwind those confirmations cannot occur, even with current wheel excess and sustained body confirmation. The recorded reason is unwind_rising_confirmation.

This is intentional withdrawal protection, not a coding exception or setting failure. In the09:08:57episode the retained peak is0.000976567/m while current request falls roughly0.000834→0.000349/m. The guard is asking for renewed rising demand, so it does not address residual wheel excess under a falling target.

Importantly, **the command already unwinds**: absolute path command falls from0.03339rad to0.01417rad over the flagged window; there is no extra final correction residual or release_pending tail in these three windows. Requested wheel angle and recorded wheel angle both decrease, but the wheel trails the target. Existing map contribution fades toward zero. Native range/slew clipping is not the limiting mechanism in the traced windows. This is not a command stuck at the old peak.

The wheel-target/unwind policy recently installed retains the old branch at/below70mph. Its fresh calibrated wheel-history/predictive-release behavior blends in70–75mph. Therefore it **cannot correct these64mph examples**; unchanged behavior here is expected.

### Delay explains part, not all, of the ratio

| Episode | Current-target wheel error |0.291s-old target |0.6s-old target |
| --- | ---: | ---: | ---: |
|<private clock time>|1.89°|1.07°|0.87°|
|<private clock time>|1.85°|1.05°|0.42°|
|<private clock time>|1.84°|0.94°|0.79°|

These are lag-sensitivity checks on frozen recordings, not a fitted delay setting. Much of the instantaneous over-response comes from a falling target and finite unwind response. Residual wheel/body agreement warrants further bounded feedback investigation, but not a blanket64mph gain reduction. Near-neutral target, sign reversal and already-under-target exit must remain withdrawal cases.

**Next design target:** evaluate whether the current calibrated wheel-target reduction/release approach can safely cover60–70mph, rather than defeating the old unwind latch or keeping old trim latched. Admission must require fresh advancing wheel/body/atomic-target evidence; closing prediction can only withdraw, reduction caps/native envelopes remain, and the40–50mph reference path stays untouched. First test these three scenes and existing under-response/abort cases, then full-corpus parity and native safety. This scope extension is not implemented in this investigation.

## Status and limits

Mechanisms are identified and reproduced locally. Existing rearm research fails to change the new15mph episode. No new control candidate, branch commit, publication or device change was made. No physical root cause (EPS/internal target, path execution, calibration truth or actuator authority) is established by frozen-input replay. No special high-speed reproduction drive is needed for the next local design stage.
