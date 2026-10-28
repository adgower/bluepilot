<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local candidate review

Read only; no device, CAN, or messaging connection was made. Candidate inspected in ${PRIVATE_CACHE} Findings concern the optional live adapter; pure tests do not exercise it.

1. **[P1] Release timing starts before publisher construction and press publication** — review_startstop/oneshot.py:121-132. Trial.step marks `started` and stage 1 before synchronous audit I/O, PubMaster construction, and send. If construction/logging/send delays the first publication by 40ms, the planned release at core elapsed 120ms occurs only 80ms after the press; firmware rejects it (<100ms) and permanently consumes the trial. Longer delay can suppress release entirely. Establish the publisher before arming and base scheduling on a verified transport event; add injected-clock/transport tests covering delayed construction and send. This still cannot establish actual firmware acceptance without an acknowledgment mechanism.

2. **[P1] Interruption or health loss after a press has no bounded release guarantee** — review_startstop/oneshot.py:94-96,148-151 and ford_startstop_test.h:58-59,68-79. A keyboard interrupt, audit write failure, stale health, or unsafe RX after an accepted press exits without release. In several cases firmware itself permanently forbids the neutral release. The header’s 100–200ms check constrains an optional second TX; it does not bound how long the remote input remains asserted. The final log acknowledges dependence on unverified stock traffic. Keep the live adapter unavailable until passive evidence establishes neutral stock recovery under the relevant fault cases, or design/review a bounded release mechanism. No software-only host test proves the receiver clears this input.

3. **[P2] Missing/invalid inputs do not reset the five-second stable arm window** — review_startstop/oneshot.py:94-98,113-120. During initial arm, invalid/unseen input causes `continue` while preserving stable_since. For example, one eligible sample at t=0, invalid input through t=4.99, then one eligible sample at t=5 causes an immediate press, without five seconds of uninterrupted eligible observation. Reset stable_since before the prepress continue and test invalid-then-restored health.

Additional completeness issue: PLAN.md says the live adapter is deliberately absent and imports/sockets never occur, but oneshot.py includes executable live publishing. The module also points operators to a nonexistent README.md. Update the review plan/documentation to match final scope before presenting it for approval.

No broad normal-mode regression identified by inspection: new routing is compile gated; normal lists are unchanged. This is not runtime or receiver validation.

## Follow-up review

CLI execution is now hard disabled before messaging import/socket setup. The pre-arm invalid-input reset is implemented. Physical TX echo scheduling improves the dormant live adapter, but receiver/process-interruption guarantees remain appropriately unresolved.

**[P1] Default dry-run now crashes on the second record.** `dry_run` contains a copied live-echo wait block referring to `press_echo_time`, `now`, and `press_publish_time`, none of which exist in that function. Reproduced locally using two valid JSONL samples at t=1 and 1.12: `NameError: name 'press_echo_time' is not defined`. Remove that live-only block and add an end-to-end dry-run CLI pair test; pure Trial tests and mocked live tests miss this regression.

The dormant adapter still performs synchronous audit I/O between release eligibility evaluation and publishing. A sufficiently slow write can carry a release beyond the firmware's upper 200ms bound; echo timestamp is also the aggregate CAN publication timestamp rather than the firmware TX acceptance timer. These remain live-readiness concerns, not blockers to a properly disabled review-only/offline artifact.
