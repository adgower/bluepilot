<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Calibrated feedback, bounded 25–30 mph effort and stronger unwind prototype

October 20, 2026. **Local prototype complete; research checks pass. Not integrated or ready to install.** No device access, transmission, production source edits, paired-branch commits or publication occurred. Owner1.20/0.97 and native safety code remain unchanged.

The candidate addresses the three mechanisms in the [preceding investigation](../navigator-shortfall-unwind-diagnosis-2026-10-20/REPORT.md). It produces finite command changes near23 and29mph and a more effective encoded highway trim. **The principal26mph episode still receives no additional command**, because the earlier mid episode has aborted without a qualifying quiet rearm, followed by native deviation clipping. No physical tracking improvement is established.

## What the report-local code does

[Prototype](../../navigator-reference/PRIVATE_ARTIFACTS.md), [design](DESIGN.md), [focused tests](../../navigator-reference/PRIVATE_ARTIFACTS.md).

**Calibrated low-speed feedback:** only experimental admission/recovery sees the better-tracking of calibrated wheel-target response and calibrated body response. Both must establish a deficit. Fixed pinion curvature, deviation/shadow intent and native safety models are unchanged. This removes the mismatch where fixed feedback reports about82% while calibrated wheel/body report about60%.

All regular effort under the new feedback definition spends the existing0.00025rad·s allowance; the separately confirmed sustained allowance retains0.0025rad·s and its one-second deadline. This avoids creating an unlimited steady correction. The existing below25mph fade still applies, so effective correction near23mph remains small. Valid quiet frames advance rearm even though zero curvature cannot supply a meaningful response ratio. Invalid evidence clears quiet progress.

**Bounded mid-speed correction:** acts strictly between25 and30mph, fading in25–26 and out29–30. Both calibrated responses must be below90%, with five distinct fresh observations, atomic target agreement and predictive catch-up/demand checks. The positive effort is capped by0.0025rad,5%of current path magnitude,0.0015rad·s total,0.75seconds from first delivery and remaining native deviation headroom. A binding deviation clip blocks it. Area is charged before final range/slew clipping and is not refunded.

An active mid episode aborts on invalid/duplicate target or motion evidence, catch-up/withdrawal, direction, generation or speed exit. Only a full second of continuously valid, distinct, quiet wheel/body evidence replenishes it. This prevents renewed pulses after a one-frame fault but can conservatively block a later turn when no quiet dwell qualifies.

**Highway unwind:** the wheel-based60–70mph fade is applied once rather than twice. Independent valid wheel history can accumulate across body-excess-margin crossings, while current wheel/body permission and predictive closing still gate every application. The existing15%/0.01rad reduction caps, onset/persistence, native limits and inherited release remain. A separately advanced current-policy instance supplies protected output at30–60mph and>=75mph; final native slew handles handoffs.

## Saved episode results

Same recorded inputs and frozen vehicle motion; path-angle command changes are not steering-wheel-angle or physical-response improvement estimates. Comparisons are against the current installed `SustainedErrorUnwind` policy.

| Episode | Frames examined | Changed float commands | Changed packed path signals | Maximum command difference |
|---|---:|---:|---:|---:|
|23mph deficit, session03,163.1–165.9s|55|6 larger|3|0.000271rad|
|26mph deficit, session02,161–167.1s|120|0|0|0|
|29mph deficit, session03,254–262.3s|165|15 larger|15|0.002363rad|
|64mph unwind, session02,213–216s|60|17 smaller|14|0.001200rad|
|62mph unwind, session02,258–263s|100|7 smaller|3|0.000346rad|
|61mph unwind, session03,335–341s|120|31 smaller|11|0.000286rad|
|Prior15mph deficit, wheel-session11,331.2–332.75s|31|1 smaller|1|0.002500rad|
|Prior83mph lane-edge, highspeed-session03,1011–1017.5s|130|0|0|0|

[Episode receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md).

At23mph the changed-command median is only about0.16%of the current path magnitude; the feedback mismatch is addressed, but the retained fade/persistence/exposure bounds leave very little actual extra command. This does not imply that a roughly40%physical shortfall has been corrected.

At29mph,15frames (about0.75s) get extra command, with a1.63%median change on those frames. The allowance then stops; it cannot cover the entire8-second deficit. The prototype is intentionally finite and is not an inverse-response gain fit.

At26mph, a preceding25.6mph turn receives four bounded samples around148.09–148.24s, spending0.00034777rad·s before abort. There is no qualifying quiet rearm before the later turn around164–167s. That later turn is first excluded by target/admission and the aborted-episode latch, then also by the existing deviation clip. **The prototype does not resolve this principal26mph episode.** Relaxing rearm or the native envelope is not justified by this replay alone.

The earlier15mph fixture is almost unchanged: one frame ends the current allowance earlier by0.0025rad. This conservative command difference is retained explicitly; no claim of15mph parity or improved road handling is made.

Across both latest moving drives, the stronger highway policy changes62packed path signals relative to the current installation. Compared with the same preceding wheel-target baseline used in the investigation, current policy changes9highway samples and this prototype changes64. These are counts of encoded commands, **not percentages of tracking improvement**. [Encoding comparison](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Validation and actual limits of proof

- **78focused tests pass**, including both turn signs, default-off whole-stream examples, protected speeds, invalid/stale inputs, finite exposure, valid quiet rearm and single-frame abort/duplicate regressions.
- **714transition cases /228,480updates** pass range, slew, exposure and final-settling checks across10–85mph, both signs and fault/driver/unwind/reversal/speed transitions.
- **128active-correction abort/transition cases** pass. The maximum additional command tail relative to current policy after the subsequent neutral request is0.10seconds in these fixtures. This is not physical actuator-unwind timing.
- **46recordings /766segments:** full retained corpus replayed at original saved CAN/send times through three independent native safety states: original traffic, current-policy path replacements and prototype path replacements. Inputs are hash-verified.176,310,196physical RX packets and2,830,661recorded TX packets are processed per compared stream. No controls-permission override, forwarding or bus transmission is used.
- **Zero additional native rejections.** Current reference and candidate have exactly the same232recorded-timing rejections:208at0x83 and24at0x3d6. These are shared retained baseline cases, not zero rejects; individual causes were not all re-diagnosed here.774steering packets differ between candidate and current reference over the whole corpus.
- **Zero changed active/no-driver path frames below5mph,30–60mph or>=75mph** in this recorded-send-time corpus, including40–50mph and the saved83mph lane-edge episode. Generated discontinuous transitions are bounded separately; recorded equality is not a promise of instantaneous parity after every artificial jump.
- The executed-source snapshot stayed unchanged, and paired production source remains clean at parent`0171b897289be53fd62f330935c55825b86c3c3a` /child`4167433e5c575f620a9dedf8144a0bc7cba14291`. Owner factors remain1.20/0.97.

[Acceptance receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md), [full route results](../../navigator-reference/PRIVATE_ARTIFACTS.md), [transitions](../../navigator-reference/PRIVATE_ARTIFACTS.md), [active aborts](../../navigator-reference/PRIVATE_ARTIFACTS.md), [independent review](REVIEW.md).

This run validates original-send-time path replacements under native hooks. It is **not** the full generated CarController/atomic-context integration replay, native paired build, device/hardware test or closed-loop road comparison. Default-off whole-stream proof here is focused synthetic testing, not a claimed full-corpus default-off run. No alternate trajectory, lane clearance or model-based percentage handling benefit is inferred.

The first native-harness attempt had an import-path error before native validation could begin. It was stopped and repaired. Completed scene traces were reused only after their executed candidate/scene/production hashes matched; incomplete scenes were rerun. Final native results cover all46recordings under the corrected frozen snapshot. Superseded pre-exposure-guard scenes are excluded.

## Remaining blockers and next local work

1. Quantify why no valid quiet rearm occurs between the two saved25–26mph turns. Any resolution-aware rearm proposal must retain fresh independent wheel/body proof and total exposure accounting. Do not solve this by clearing budgets on a reset, signal, driver input or a new turn.
2. Assess the23mph effective fade and finite exposure against actual encoded commands. Admission now uses consistent evidence, but delivered effort is tiny; deciding a larger/sustained allowance requires explicit bounded tests and cannot be justified by dividing100by the observed response.
3. Retain the prior15mph earlier-release frame as a fixture. Check that later changes do not unintentionally trade that behavior for a moderate-speed improvement.
4. Before any integration/installation, run the exact candidate through the generated CarController/context replay and paired build checks, retain the shared rejected-packet cases, and then separately establish hardware and road behavior. This artifact is not installation-ready.
