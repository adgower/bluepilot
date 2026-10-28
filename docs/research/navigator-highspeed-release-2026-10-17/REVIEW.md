<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent read-only review

Reviewer `/root/review_highspeed_body_release` inspected the candidate, tests, real-event motion adapter and replay wiring. It did not edit files or contact the device.

Two concrete findings were reproduced red and resolved:

1. Invalid/recalibrating extrinsics could leave previously cached motion valid until the next deviceMotion. The adapter now revokes cached samples immediately; calibration recovery cannot revive them. Generation changes clear body history across invalid/recovered calibration. Tests use actual Cap'n Proto event builders and installed PoseCalibrator, including all motion/envelope validity flags.
2. Bend resets originally ran before input freshness/validity checks. An invalid zero-speed/neutral/sign-change tick could clear a real unwind latch. Resets and peak advancement now require fresh validated state/control/model/calibration evidence. Five invalid-reset variants and lower-plateau followups lock this down.

Additional tests cover source/arrival ordering, out-of-order source after activation, repeated source IDs,80 ms unique-history boundary, slow cumulative decline, small demand jitter, genuine rising-demand rearm and renewed body confirmation. A one-frame median lag in slow-withdrawal detection is explicit; large raw retreat aborts immediately.

Final source re-review found no remaining concrete blocker by inspection. Test/native replay results remain separate evidence, recorded in the report/verification artifacts. No physical vehicle readiness conclusion was requested or supplied by the reviewer.


## Final driver-slew delta

A separate adversarial regression found that returning immediately to a rapidly rising reference on ordinary steering pressure could exceed the final slew limit. The corrected branch matches installed RollAwareMapping: inactive/human-turn states use reference immediately; ordinary steering pressure withdraws extra correction and rejoins through the slew-limited release path. Both turn directions and takeover events in the transition sweeps are tested. The reviewer inspected the delta and found no concrete new blocker. Final tests and the entire corpus replay passed again after this source change; earlier evidence is archived separately.
