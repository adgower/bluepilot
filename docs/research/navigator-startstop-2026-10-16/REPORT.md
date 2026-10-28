<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator automatic start/stop: recording and transmission feasibility

2026-10-16. Read-only device inspection; no device writes, firmware changes, service interruption or experimental CAN transmission.

## Conclusion

The recording strongly supports 0x461 byte 0 bit 0 as a physical-button-related indication. It does not establish that injecting that bit can command the vehicle. The exact installed Ford safety source rejects host transmission of 0x461. A Python controller change alone cannot implement this under that safety configuration.

## Provenance

SSH read-only inspection: /data/openpilot parent 9da98d0c91f0559efa976e3ffb221f2584fd0b88, opendbc child 18175406d0cc5af8233afde70a5d121aedf8de44; both status outputs clean. SHA256 hashes of installed ford.h, carcontroller.py and fordcan.py match the local checkout ${USER_HOME}/Apps/openpilot/.navigator-master-integration-20261014. Saved CarParams: FORD_EXPEDITION_MK4, flags 15, Ford safetyParam 10, fwdCamera. Saved parameters and matching source do not prove the currently flashed MCU firmware or current runtime safety mode.

## Recording evidence

Input ${USER_HOME}/cabana_live_stream/2026-10-16--15-49-00--{54,55,56,57,59,60,63,64}/rlog, where available. Times below are monotonic offsets from first event in segment 0 and approximate the UI timeline; UI initial batch timing and pauses may introduce offsets. Analysis artifacts: frames.json and analyze_frames.py.

504 frames at bus 0, 504 matching-sequence frames at returned bus 130, ID 0x461, eight bytes. Every observed byte 1 through 7 is zero; byte 0 ranges from 0 to 7. Thus only low three bits vary in this sample. Bit 0 follows brief presses and sustained holds. Bits 1–2 cycle during idle; they overlap DBC-defined drive-mode fields. Do not assume they can be zeroed or label them a validated protocol counter.

Sustained presses: bit high 3819.502–3821.402 s (1.900 s), 3826.632–3828.742 s (2.110 s), 3833.652–3835.662 s (2.010 s). Independent 0x166 StopStrtDrvMde_D_Indic changes at 3821.482, 3828.782 and 3835.682 s, 80/40/20 ms after falling edges. State sequence disabled -> enabled -> disabled -> enabled. Earlier brief pulses and four toggles around 3602–3611 s provide repeated corroboration. Correlation does not establish the physical button producer or receiver command semantics.

Named DBC request candidates 0x326 byte0bit3 and 0x105 byte2bit7 remain constant during both test intervals. The 0x461 candidate bit is undefined by this DBC; the gateway message name is not reliable semantic documentation for that bit. No application checksum byte varies in these observed frames, but absence of a changing checksum here does not prove absence of all validity checks or network conditions.

## Transmission and forwarding

See CODE_REVIEW.md for exact source citations. ford.h:457–480 omits 0x461 from every transmit list. safety.h:230–252 requires a permitted address, bus and length. Generic forwarding allows 0 -> 2 and 2 -> 0 for this ID. panda.cc:268–269 adds 128 for returned frames, while fdcan.h marks outgoing frames returned and forwards received traffic with can_send(..., true). Bus 130 is therefore returned TX on physical bus 2; it is not an independent physical source. This supports the source-side receive on bus 0 and forwarding toward the camera, not proof that the command consumer is downstream of Panda.

Compiled a fresh local plain debug safety harness from this exact child source to ${PRIVATE_CACHE} Ford safety model 6 / param 10 initialized successfully. 16 transmit checks: bus 0 and 2, controls_allowed false and true, four observed eight-byte payloads 00/01/03/04 followed by seven zero bytes: all rejected. Forward hook tests returned bus 2 for source bus 0 and bus 0 for source bus 2. This is host-native safety evidence, not an injected vehicle test; no sanitizer or on-device firmware validation claimed.

## What remains before control is demonstrated

1. Identify the switch/gateway origin and command consumer, including whether the relevant request is merely mirrored across the camera connector. The consumer may sit on the same network as the genuine publisher, outside Panda's forwarding control.
2. Validate all remaining payload fields, timing and behavior under unrelated drive-mode controls. The current log cannot justify replacing the original message or constructing a mostly-zero command.
3. If justified, prepare an isolated, narrowly constrained safety/controller implementation and offline tests. Do not use all-output safety or bypass the global transmit checks. Preserve original vehicle traffic and account for conflicting same-ID publishers.
4. Separately authorize a supervised stationary vehicle test, verify actual firmware/runtime configuration, and use independent 0x166 state feedback as the acceptance criterion. There is no evidence yet that transmission will toggle the feature.

The present result is feasibility research, not approval for deployment or on-road use.
