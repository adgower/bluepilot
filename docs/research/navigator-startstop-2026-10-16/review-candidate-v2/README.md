<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator start/stop: local owner-integrated review candidate v2

Prepared 2026-10-16. **Disabled source-review candidate, not an executable vehicle test.** No device access, installation, firmware flashing or CAN transmission occurred in this revision. V1 remains preserved in `../review-candidate` for history; do not combine its host sender with v2.

## What changed

- The existing pandad `can_send_thread` owns the one-shot transaction through its existing Panda handle. No second `sendcan` publisher or direct competing Panda connection. Normal host commands are intercepted only after Panda reports the exact experimental safety configuration; initial fingerprinting traffic is not intercepted prematurely.
- Host requires fresh parked inputs and five seconds of continuous eligibility, with a fifteen-second arming deadline. A command spends its budget before transport; no automatic retry. Source activation is hard-disabled regardless of environment variables. There is no live CLI.
- MCU requires the exact debug build gates and Ford parameter `0x400A`, rechecks parked inputs immediately before the FDCAN hardware request, and drops a press queued longer than 50 ms. One host press attempt per MCU boot; changing safety mode cannot rearm it. Host release commands cannot consume the MCU cleanup capability.
- MCU reserves its own neutral frame and schedules it from the existing 8 Hz tick after at least 120 ms from TXBAR. All 125 simulated millisecond tick phases scheduled cleanup in 120–244 ms. This is a scheduling result, **not a wire pulse-duration guarantee**. Delayed interrupts and CAN arbitration/queues can extend it.
- Cleanup does not need host state, USB, returned echoes or a host release. Raw-CAN unsafe/stale observations after the press cannot cancel that reserved neutral frame. It still uses normal safety dispatch; no all-output mode or general safety bypass.
- Graceful exit first quiesces the mutex-protected owner, joins the sole writer, then allows 300 ms scheduling grace before normal NO_OUTPUT. A transport stall can still block the join. Forwarding checks use the actual output bus so stock bus-0 traffic forwarded to bus 2 is not treated as the host experiment.

## Remaining boundaries

| Event or uncertainty | Behavior / evidence limit |
| --- | --- |
| Host disappears after hardware TX request | MCU cleanup scheduler is independent; verified in native harness, not hardware |
| SIGTERM / ordinary exit | Quiesce → join → 300 ms grace → NO_OUTPUT; source review and owner unit checks only |
| Ignition-off, offroad or another safety-mode change | Existing immediate NO_OUTPUT takes precedence and can cancel cleanup; deliberately preserved |
| Power loss, MCU reset, relay fault, bus fault, full queue, unacknowledged frame | Delivery can fail; one cleanup allocation, no retransmission protocol or receiver acknowledgment |
| TXBAR / returned CAN echo | Hardware request indication only, not proof of acknowledgment or PCM acceptance |
| Genuine 0x461 continues | Not suppressed or replaced; parallel frames and sequence interpretation remain unproven at the receiver |
| Bits 2–1 | Sequence-like in capture, but not an authoritative counter specification; reused stock shape is experimental |
| PCM/gateway response | No acceptance proof. Neither local simulation nor physical network reachability establishes it |
| Full builds | Full pandad binary and H7 firmware compilation/linking have not been validated; native helpers are not substitutes |

The publisher ownership, host-dependent release scheduler, queue-age handling and ordinary-exit ordering now have a concrete local implementation. This does **not** make the parked test ready to execute. Full integration builds and representative bench evidence are still required to assess this implementation, including actual TX/cleanup timing and fault behavior. Deployment or transmission needs a separate human instruction.

## Files and exact bases

Patches are independent and apply at each repository root:

- `parent.patch`: parent `9da98d0c91f0559efa976e3ffb221f2584fd0b88`.
- `panda.patch`: Panda `a59195163c32a3a375ea6c86715dc08fd0984c1b`.
- `opendbc.patch`: opendbc `18175406d0cc5af8233afde70a5d121aedf8de44`.
- `DESIGN.md`: transaction contract and limits.
- `INDEPENDENT_REVIEW.md`: independent source review, including the shutdown finding and scope correction.
- `test_owner.cc`, `test_mcu.c`, `test_mcu_failures.c`, `validate.py`, `validation.log`: native-only verification.

Working mixed snapshot: `${PRIVATE_CACHE}`. It contains the parent paths plus `panda/` and `opendbc_repo/` at those bases. Durable patches above preserve the proposed changes if the temporary snapshot disappears. Apply only to isolated matching source copies; existing source checkouts were not edited.

Reproduce native checks with a Python environment containing this opendbc revision's test dependencies:

```sh
python validate.py ${PRIVATE_CACHE}
```

Validation compiles host-native C/C++ helpers and safety libraries into a temporary directory, then runs Ford regressions with the experimental build define absent and present (normal safety configurations). It has no device connection or CAN send path. See `validation.log` for exact results. The patch files and tests should be reviewed together; build-system activation, hardware enablement, installation and a live execution tool are intentionally absent.
