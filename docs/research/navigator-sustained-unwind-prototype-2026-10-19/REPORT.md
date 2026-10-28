<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Bounded sustained-error /60–70mph unwind prototype — October19,2026

Status: local prototype and layered replay validation complete. No additional native rejections; protected25–60mph/default-off parity passes. One75.1mph generated-timing boundary difference is documented below. This is not integration, device or physical-handling acceptance.

## What changed locally

This research-only prototype addresses the two mechanisms in the [preceding diagnosis](../navigator-low64-diagnosis-2026-10-19/REPORT.md). The production paired branches and Comma remain unchanged. Owner1.20/0.97,geometry,pinion/native safety,preferences and existing firmware are preserved.

**Low speed:** sustained confirmed error gets an independent finite allowance, rather than being shut off solely because the earlier transient/catch-up budget is spent. Additional path angle is capped at0.0025rad; independent exposure at0.0025rad·s and one second from first delivery. The sum of regular and extra correction remains inside the existing0.0075rad/12.5%-of-feedforward cap. Effort is charged before final native clipping, with no refund. Existing speed fade reaches zero by25mph.

Admission requires the existing demand persistence/recovery tests plus five distinct fresh wheel/body/control observations, same-direction response, calibrated target agreement, meaningful demand and wheel/body ratios below70%. Each sensor has a predictive catch-up veto. A0.5s demand window must have<=15%span and<=10%net rise. This is not a stall rescue or an inverse-response gain fit.

The new allowance requires a separate full second of continuously valid, quiet pinion **and body** curvature before rearming. Both range and adjacent-slope limits apply. Driver/inactive/fault/generation edges abort the allowance; resets or repeated turns do not refill it. The regular installed budget's dwell is unchanged.

**60–70mph:** the existing calibrated wheel-target reduction/predictive-withdrawal policy now blends60–70mph in this report-local copy, replacing its70–75mph blend. At/below60mph the high-speed branch retains its installed reference; at/above75mph its formula is unchanged. Reduction caps, neutral/sign and body/wheel confirmation, fresh atomic target, native slew/range and closing release remain. State-transition parity is checked separately; changing a blend boundary is not proof of whole-route identity.

## Saved episode results

These compare commands on the same recorded motion. They cannot estimate the alternate physical trajectory or prove improved steering.

| Saved episode | New command effect |
| --- | --- |
|<private clock time>:15CDT,~15mph|16of31flagged frames receive extra correction (0.80s), maximum0.0025rad. The allowance then withdraws at its one-second deadline. Previously all31frames had zero added term after transient-budget exhaustion.|
|<private clock time>:57CDT,~64mph|6of15frames receive additional reduction; peak0.000315rad.|
|<private clock time>:22CDT,~64mph|14of23frames receive additional reduction; peak0.000441rad.|
|<private clock time>:34CDT,~64mph|1of11frames receives additional reduction; peak0.000300rad.|

The low-speed increase is modest (about2%of representative0.12rad feedforward), not a claim that46%observed response becomes100%. The finite allowance intentionally stops before it can accumulate unbounded effort. The64mph effects are also small, often near the0.0005rad wire quantum; exact packet changes are evaluated separately. See [episode-results.json](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The two prior high-speed recordings show no added command changes at>=75mph in the original send-time scene replay, including the previously identified83mph/near-lane-edge scenes. The generated control-time full replay does show one recorded-context boundary frame at75.11mph (route1049.346s): reference0.0285rad versus candidate0.0280rad, a0.0005rad wire quantum of additional reduction. Formula equality above75mph does not imply identical onset history across the changed60–75mph transition. This isolated generated-timing difference must be retained as an integration review item; do not claim whole-corpus>=75mph byte parity. It is absent from the labelled synthetic-snapshot version of that route. [Boundary receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Tests and independent review

Four behavior tests fail against the installed policy and pass with the prototype. Initial scope/guard tests pass. Independent review identified three real gaps: invalid body samples could contribute to refill; body recovery was not independently predicted; and quiet pinion could refill despite nonquiet body motion. Each was reproduced in a failing regression before repair. All are resolved; final independent review finds no remaining material issue.

Combined candidate and inherited wheel-guard tests:95passed. Two inherited warmup/parity cases formerly expected identity at65mph; because65mph is intentionally in the new scope, their protected-range checks now target55mph, with new64mph behavior tests covering the changed scope. No physical-response expectation was used to excuse a failing native bound.

Transition/abort screen:480cases/172,800frames, both signs and15–85mph, covering hold/unwind/closing/reversal/driver/disengage/invalid/stale/duplicate/context/body/generation/speed exits. All final range/slew and envelope checks pass; all traces settle. Additional active-allowance abort/reversal tests retain native slew; a bounded command tail up to0.0025rad can remain during abrupt reversal and must rejoin the reference within the tested0.3s boundary. This is not claimed to be instantaneous withdrawal of physical steering. Budget and extra-term caps are asserted throughout. [Transition results](../../navigator-reference/PRIVATE_ARTIFACTS.md), [review](REVIEW.md), [design](DESIGN.md).

The first partial full replay used the pre-review candidate. It was stopped and retained under `replay-review-superseded`; those results are excluded. A fresh full replay uses source snapshots including both prototype modules. Likewise the old scene outputs are retained as superseded, not mixed with final results.

## Original-timing comparison and provenance

New October19recordings used the current installed wheel-target policy, but older high-speed recordings predate it. The original-timing harness therefore uses three independent native hook instances: original recorded traffic, installed-reference path replacements, and prototype path replacements. Only path-angle bits/checksum are replaced, in RAM, preserving recorded timing/RX/permission events. Older reference commands must not be asserted identical to their historical wire packets.

The prototype is compared with the installed reference for additional rejection behavior; the original recording remains separately reported. This is an unsanitized Mac debug-hook experiment, not bus/hardware proof or a control-permission override.

## Completion boundary

No production source edits, runtime selector,preference registration,paired branch commit,push,device access,OS/firmware change or install is part of this prototype. The report-local code is not vehicle-ready. Full replay acceptance and then separate integration/build/device/physical validation are distinct stages. Requested-path lane-edge behavior remains separate from actuator tracking; no special85mph reproduction drive is requested.

## Final replay acceptance

-43sessions/740segments:4,289,417controller updates per recorded/fixture variant.369recorded-context and796labelled synthetic-snapshot updates differ from the installed reference. Four independent native states process generated TX with original saved RX; each variant retains exactly2shared native rejects and no additional candidate rejection.
- Default-off whole-stream byte parity passes across all updates. Zero changes below5mph or25–60mph, including40–50mph, in recorded and fixture versions. One recorded-context75.11mph boundary update differs; zero fixture>=75mph differences.
-13original-send-time scenes:244encoded candidate-versus-installed-reference steering packet changes,0additional native rejects.404historical packets differ between original-recorded and installed-reference baselines, explicitly represented by a third native-hook stream. RX/timing/permission events are preserved; no permissive control override.
-95focused/guard tests and480transition cases/172,800frames pass. Paired source heads/files/native library are unchanged and clean, owner1.20/0.97preserved. [Acceptance receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md), [full route receipts](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Before any integration, retain or resolve the one generated75mph boundary difference explicitly and validate the runtime factory/context contract against the exact candidate. Device build/parked acceptance and physical tracking remain separate. No promise that a2%-scale finite extra command closes the observed54%low-speed response deficit. No new85mph test is requested.
