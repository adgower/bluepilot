<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent owner-v2 review

Scope: local source review only. No device access, CAN access, installation, or transmission. Reviewed the candidate design, host owner integration, Panda tick/FDCAN integration, Ford safety changes, and test harness source. No files in the candidate were edited. Tests were inspected rather than independently rerun.

## Actionable finding

[P1] Graceful pandad shutdown cancels the MCU cleanup reservation.

Location: openpilot/selfdrive/pandad/pandad.cc:464-468 (interacting with panda/board/main.c:118 and set_safety_mode at main.c:31-78).

The experiment explicitly requires an onroad, disengaged host. Those are exactly the conditions under which pandad_run sets NO_OUTPUT before joining its send thread on graceful shutdown. If SIGTERM/normal service shutdown happens after the high TXBAR request and before the 120..<245 ms cleanup tick, this changes current_safety_mode and calls can_init_all. The cleanup tick then refuses to call ford_ss_release_due because the mode is no longer FORD. Neutral will never be generated. This makes an ordinary host interruption cancel the reserved release even without hardware faults or an explicit operator safety-mode change.

The design lists safety reconfiguration as a residual limitation, but this reconfiguration is an automatic consequence of the host interruption that the integration is intended to tolerate. Resolve the shutdown path for an outstanding experiment or explicitly narrow the host-interruption claim and require review of that behavior before enabling source activation. Avoid treating a timer sleep alone as proof of delivery; the MCU transaction needs an observable terminal state or another explicitly reviewed policy.

Required regression: exercise the actual pandad graceful-exit policy during stage 2, including the boundary between command generation and USB transport. The MCU-only reconfiguration test currently confirms cancellation but does not expose its connection to ordinary pandad shutdown.

## Other observations

- Actual safety reconfiguration, relay malfunction, queue overflow, CAN reset/reinitialization, and bus faults remain real release-failure paths. The design already discloses these; they are not additional findings here.
- The host command is spent before transport, preventing automatic host retries. The MCU cleanup capability is confined to the reserved neutral shape and passed through the normal safety hook.
- Source activation is currently hard-disabled, so the finding is a blocker for a future enabled candidate rather than a presently reachable vehicle action.
- The 125-phase harness calls helper functions directly. It does not compile/run the real tick handler, FDCAN ISR, USB transport, or pandad shutdown, and therefore does not establish integration behavior or physical timing/delivery.

## Follow-up review of revised candidate

The revised shutdown path calls quiesce under the same mutex as command issuance, joins the sole transport thread, and only then grants 300 ms before NO_OUTPUT. This resolves the original graceful-exit ordering finding within the documented nominal MCU scheduling assumptions. It is scheduling grace, not a hard release-delivery guarantee; source activation remains disabled.

The revised FDCAN hooks now receive the actual output bus, preventing stock frames forwarded from bus 0 to bus 2 from being mistaken for the injected transaction. That correction addresses the forwarding identity issue.

Remaining actionable integration finding [P1/P2 depending on intended status-change guarantee]: automatic offroad/ignition reconfiguration still cancels cleanup.

Location: openpilot/selfdrive/pandad/pandad.cc:249-251, send_panda_states().

After high is requested, a deviceState.started transition to false or ignition health transition to false causes send_panda_states to immediately call set_safety_model(NO_OUTPUT). This occurs inside the normal main loop, before the new shutdown quiesce/join/grace logic. It cancels the pending neutral through the same current_safety_mode gate and CAN reset described above. The revised shutdown fix therefore does not cover these ordinary host/status transitions. Defer that automatic reconfiguration for a pending transaction under an explicitly reviewed policy, or narrow the design claim that status changes do not cancel cleanup and explicitly disclose offroad/ignition transitions as cancellation conditions. Test the real host policy transition during stage 2, rather than only a direct set_safety_hooks test.

No other new actionable defect identified in this follow-up source inspection. No device/network operations or candidate edits. Tests not independently rerun.
