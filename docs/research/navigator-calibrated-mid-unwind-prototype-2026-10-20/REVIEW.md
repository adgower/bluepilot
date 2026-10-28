<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent prototype review

The requesting-code-review workflow dispatched a reviewer with bounded artifact context and no device/source-write authorization.

Initial material findings, reproduced in failing tests and repaired:

1. Mid-speed effort added after the deviation projection. Added exclusion when native deviation clipping binds and a cap from remaining transformed deviation headroom.
2. Calibrated ratio rejection of zero demand bypassed inherited quiet dwell, preventing low-budget replenishment. Valid quiet now passes through both inherited dwell guards; invalid evidence explicitly clears quiet progress.
3. A one-frame target mismatch could readmit the mid term before the duration deadline. Active episodes now latch abort, with no area reset.
4. Follow-up review found the equivalent duplicate-motion-source gap. Added a single-frame regression and abort latch; demand withdrawal and predicted catch-up received equivalent tests.

Final independent review: no remaining material findings; reviewer independently ran78focused tests, all passing. This review addresses the local prototype, not integration, hardware or physical handling readiness.

The author also reproduced and bounded a draft issue where calibrated regular feedback could continue indefinitely under steady demand. All such regular effort now spends the existing finite transient allowance. Superseded scene outputs from before that repair are retained in `scenes-before-exposure-guard` and excluded from acceptance.
