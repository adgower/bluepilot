<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local high-speed calibrated wheel-target/unwind prototype

The prototype now admits a bounded trim during genuine, current wheel/body excess even while steering demand is withdrawing, and releases as the measured wheel closes toward its calibrated target. It is a research-only feedback-policy probe, not a new learned calibration, direct wheel-degrees-to-CAN conversion, or an installed change.

The saved lane-edge fixture receives20additional trim frames (about1second at nominal20Hz) in its final2.8seconds, from route1079.480720–1080.427611s. Maximum total extra reduction is0.002754742rad. The trim withdraws before the final two already-under-target frames. The earlier rearm-only prototype changed none of this final window. This demonstrates coverage of the intended condition on frozen inputs; it does **not** demonstrate improved physical path or that the lane-edge event is fixed.

## Design and boundaries

- New policy blends in70–75mph, full above75mph, retaining the inherited gentle-curve/request-acceleration eligibility. Calibrated expected wheel target, current wheel excess/direction, valid source timestamps, and current/sustained body excess must all pass the installed guards. The old fixed-peak exclusion alone can be bypassed.
- Five distinct advancing wheel source stamps and advancing control stamps are required, each no more than40ms old. A causal wheel-error slope predicts150ms ahead. Prediction may reduce or release trim, never increase it beyond current measured excess. Both current and projected error must exceed0.5°.
- No integral, accumulated gain or calibration update. Ratio/stiffness/roll/offset are checked inputs; native fixed pinion model and owner1.20/0.97 are untouched. The model-predicted near-edge path is a separate unresolved issue.
- Total reduction remains capped at15%/0.01rad relative to the independent RollAwareMapping reference, with inherited onset persistence/ramp, shadow intent and final native range/slew. No stacking of independent trims.
- An independently advanced installed strategy preserves original onset/latch history below70mph. Handoff rejoins that strategy through native bounds; a theoretical slew-limited handoff tail may cross70mph. Default-off is byte-identical. Recorded lower-speed parity must be checked separately rather than assumed from the blend.

See [DESIGN.md](DESIGN.md) and [prototype.py](../../navigator-reference/PRIVATE_ARTIFACTS.md). Engineering thresholds are hypotheses, not fitted handling parameters or statistical confidence bounds.

## Test-first and review evidence

[Final tests](../../navigator-reference/PRIVATE_ARTIFACTS.md):110passed, comprising73unchanged installed-reference cases and37prototype cases, including12,000transition/abort frames with native slew checks. New behavioral tests were observed failing for mirrored sustained unwind admission and early closing release, duplicate physical sample admission, boundary warmup contamination, and explicit disable being overwritten. The true under-target fixture keeps body excess positive, exercising the wheel guard independently.

[Review](REVIEW.md) identified and resolved source freshness and fixture-sign defects. The first replay exposed a lower-speed boundary state difference; mirrored tests reproduced it, and an independent installed state now prevents that contamination. Follow-up review caught an enable configuration copied over an explicit disable; enable is now synchronized and excluded from state copying, with a red/green regression. Narrow final review independently confirmed the fix. The first partial replay/scenes are retained in explicitly`*-boundary-obsolete`directories and are not acceptance evidence.

## Recorded scenes

[Scene audit](../../navigator-reference/PRIVATE_ARTIFACTS.md), final source hash`138ff7376794573dc1e9033e2cd50ef2bbc97bbc8e2f25746f0e33fc1938cf7f`:

| Saved route | Changed strategy frames | Added trim | Withdrew installed trim |
|---|---:|---:|---:|
|highspeed-session-03|263|163|100|
|highspeed-session-04|196|128|68|
|prior roll-session-01|104|71|33|

All additional-trim frames have current positive calibrated wheel/body excess, with no native handoff tails in these scenes. Maximum body source age among added frames is73.25ms; the stricter40ms requirement applies separately to wheel/control sources. There are zero scene changes at or below70mph, driver/inactive changes, or added trim into the saved under-target exits. All14retained earlier measured-under-response counterexamples still receive zero final extra correction. Some changes withdraw the installed trim during predicted closing; changed-frame counts must not be described as all additional reduction.

The installed-reference reconstruction matches actual active/no-driver packets within half a wire step on the two new high-speed sessions. The prior roll route was recorded on older RollAwareMapping source; its installed-high-speed reference is itself a counterfactual and is not claimed identical to that recording.

## Acceptance status

Exact recorded RX/TX timing passes for both new high-speed drives:234/170encoded steering packets differ (404total), with0additional native rejections across16,801,474physicalRX and286,463configuredTXpackets. Both variants retain the same32baseline rejections across allTXtypes (18/14per session), with0RXinvalids. Path bits/checksum alone are substituted in RAM; there is no control-permission override or physical transport. See each session's`recorded-native-results.json`under[scenes](../../navigator-reference/PRIVATE_ARTIFACTS.md). The [incident command CSV](../../navigator-reference/PRIVATE_ARTIFACTS.md) preserves aligned measured/requested wheel and installed/proposed path fields.

Full32-session/637-segment native replay **passes**:3,704,143controller updates per variant;503recorded-context and558separately labelled causal-fixture changed updates. There are0changes at/below70mph (including40–50mph),0handoff updates in this corpus, and default-off whole-stream byte parity passes at every update. Each variant generates2,399,383TXframes:11,829precede Ford configuration and2,387,554are accepted after configuration, with0configured native rejects. All variants have32startup invalid-safety ticks; this is not a claim of continuous RX-validity from startup. All28prior-route installed-reference stream hashes match the preceding accepted source; all32executed source snapshots agree, protected hashes/pairedHEADs remain unchanged, and both paired tracked checkouts stay clean. See[acceptance.json](../../navigator-reference/PRIVATE_ARTIFACTS.md),[full replay](../../navigator-reference/PRIVATE_ARTIFACTS.md)and[verification.json](../../navigator-reference/PRIVATE_ARTIFACTS.md). Legacy routes apply the paired pinion configuration consistently in generated replay; this is distinct from exact recorded-param/timing substitution on the two new routes. The native library is an unsanitized Mac debug build. Controller-update-time replay, send-time strategy reconstruction and actual recorded packet substitution are different harnesses; their frame counts need not match.

## Limits and next step

Frozen-input replay does not predict altered wheel/body response, lane position or driver action. Learned wheel geometry and calibrated pose yaw remain uncertain and correlated. No independent surveyed lane/tire clearance, EPS internal target, ARM/H7 or physical bus proof is established. Requested model path remains near the lane edge in this incident; this steering-policy probe does not center that path or certify clearance.

No SSH/device access, CAN transmission, ECU query, integration, commit/push, install, firmware or settings operation occurred. Paired source/HEADs and protected steering settings remain unchanged. After local acceptance, retain this as an unintegrated candidate with explicit physical-validation and path-position limitations; do not infer installation readiness or fixed oversteer from native replay alone.
