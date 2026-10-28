<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Owner-integrated transaction review v2

Local-only request: resolve competing publishers, host-dependent timing and release after host interruption. No installation or device/CAN access.

Design:
- pandad's existing can_send_thread owns the experiment. No new sendcan publisher and no second Panda connection. In explicit test mode, normal subscriber commands are suppressed and exactly one press command is passed through the existing transport. Existing PandaSafety configures the opt-in only for reviewed Ford/base-param10. Source activation remains hard-disabled for review.
- MCU safety accepts one press per boot, reserves a neutral frame, and rejects host release/retries. A press older than50ms is dropped before the FDCAN hardware request. Release time starts at the FDCAN TXBAR request, not host arm/log/echo time.
- Existing8Hz MCU tick queues a single neutral release once>=120ms elapsed. Nominal firmware scheduling interval120..<245ms, subject to interrupt latency and hardware availability. All packet generation uses the normal CAN safety entry; a private internal cleanup grant authorizes only that stored neutral frame. No all-output mode or stock-frame suppression.
- Host crash, USB disconnect, missing echo, unsafe raw-CAN observations or stale host state do not cancel an already-started MCU cleanup. No host retries. A hardware power loss/reset, safety reconfiguration (including immediate ignition-off/offroad NO_OUTPUT), bus fault or queue failure can still prevent delivery. These are explicit residual limits, not guarantees of remote state.
- Queueing and TXBAR are not wire acknowledgment, and receiver acceptance remains unproven. Tick and queue timing must be validated on a representative bench before vehicle enablement.

Deliverables: source patches for parent/Panda/opendbc, pure host-owner tests, MCU harness tests with fake queues/tick/hardware clocks, normal-mode regression tests, failure matrix and independent review. No flasher or executable live activation path.

Graceful shutdown: quiesce the mutex-protected owner, join its sole transport thread, allow300ms MCU scheduling grace after its last possible write, then retain normal NO_OUTPUT shutdown. This is a nominal scheduling allowance, not delivery acknowledgment. Ignition-off/offroad still selects NO_OUTPUT immediately; safety shutdown takes precedence over experimental cleanup. Full pandad and embedded firmware builds are not validated by native helper tests.
