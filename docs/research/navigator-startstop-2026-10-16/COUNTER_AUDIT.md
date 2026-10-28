<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Independent offline 0x461 counter audit

Only local saved rlogs were read. No SSH, device connection, CAN transmission, or source changes.

## Data and independently reproduced result

Parsed `~/cabana_live_stream/2026-10-16--15-49-00--{0..64}/rlog` with installed checkout cereal schema. Bus 0, ID 0x461: 1,314 frames; span from first to last 3,896.282 s. First frame is recording-relative 1.571 s. Each payload is 8 bytes. Only byte 0 varies (0..7); all remaining bytes are zero in this experiment.

Define `q=(payload[0] >> 1) & 3` and `button=payload[0] & 1`.

All 1,292 adjacent pairs separated by <=2s satisfy `q_next=(q+1)%4` with zero exceptions. This includes edge-triggered intervals substantially shorter than one second. Gap minimum 58.294 ms, median 999.953 ms, maximum 1,012.108 ms. Of the rounded-to-0.1s gaps, 1,251 are 1.0s and 41 are shorter. This strongly supports a per-observed-publication sequence, rather than a simple independent one-second wall-time phase.

The earlier validation excluded 21 gaps >2s. Nineteen are 6.491–6.510s and also advance by +1, always byte 0 `06` to `00`. Thus 1,311 of all 1,313 adjacent pairs are +1 mod4. The remaining two gaps are 2,455.180s and 50.979s, both delta3. Those gaps cannot establish reset behavior or continuity; missing publications, module sleep/wake, reconnects or restart are unresolved.

Early sample recording-relative times/payload first byte: 1.571/00, 2.571/02, 3.571/04, 4.570/06, 5.570/00, 6.571/02, 7.570/04, 8.570/06, 15.061/00. Other bus0 messages are present in the 8.570–15.061 interval (981 CAN frames), so the first long 0x461 gap is not a complete absence of all bus0 capture. Capture losses or source/network gating remain possible.

## DBC mapping caution

In current local `ford_lincoln_base_pt.dbc` line 2602:

- `SelDrvMdeSwtch_No_Actl : 2|2@0+` maps Motorola start bit2 length2 to raw byte0 bits2–1. This is the sequence-like field observed above.
- `SelDrvMdeSwtch_D_Stat : 4|2@0+` maps raw bits4–3, both zero here.
- `SelDrvMdeCnt_D_Stat : 7|3@0+` maps raw bits7–5, all zero here. The DBC field whose name contains `Cnt` is NOT the observed cycling field.
- Raw bit0 is not defined in that message by this DBC.
- Message transmitter is GWM; the three listed receivers are ABS_ESC. This DBC does not document a PCM receiver for this message.

Interpretation: strong statistical evidence for a two-bit rolling sequence on publication; no authoritative proof of receiver validation, reset/initialization rules, duplicated-frame tolerance, sequence-loss tolerance, checksum, or button semantics. A DBC signal name cannot resolve semantics without the accompanying signal specification.

## Limitations in previous validation

1. Its `((b[0]>>1)-(a[0]>>1))%4` correctly extracts the modulo difference of bits1–2 even though it lacks an explicit `&3`; higher bits cancel modulo4. It is not a computation bug.
2. Excluding all >2s gaps obscures the 19 additional +1 transitions and prevents evaluating likely sleep/wake behavior. Large gaps cannot be treated as known counter resets.
3. The preservation test proves only arithmetic bit preservation, not a valid message, checksum validity, application acceptance, or safe vehicle behavior.
4. Synthetic last-value/sampled receivers are explicitly illustrative. Genuine low frames cut synthetic holds only under those assumed receiver models. No actual PCM algorithm was emulated, and real receiver could use edge detection, latch/debounce, source gating, counter validation or another rule.
5. A non-advancing inserted frame creates an observed duplicate sequence value; an advancing insertion duplicates the following genuine sequence value. This is a sequence inconsistency, but receiver rejection is unproven.
6. All other bytes fixed zero means these samples provide essentially no ability to identify CRC/checksum dependencies over diverse payloads. Absence of a changing extra checksum byte is not evidence that the PCM accepts arbitrary bit0 changes.

Analysis scripts used: `${PRIVATE_CACHE}`, `${PRIVATE_CACHE}`. These are read-only local log readers.
