<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# PCM message specification search and counter findings

2026-10-16. No device access, code/firmware modification or CAN transmission.

## Search result

No publicly accessible model-correct PCM receive specification for0x461 was located. This is a bounded negative search result, not proof that no such specification exists. No OEM receiver code, acceptance window, duplicate tolerance, timeout/reset rule or checksum rule for this frame was found. A Motorcraft service subscription is not established to include an engineering CAN matrix; do not purchase one on that assumption.

Searched public web for Ford0x461/1121 plus PCM/start-stop/counter, exact AllTerrainControlData_FD1 and SelDrvMdeSwtch_No_Actl names, and Ford service-content matches. GitHub connector searches of exact symbols returned copies of the same three-field dictionary or generated summaries, not a distinct PCM implementation. Scoped searches in commaai/opendbc and the Ford F150 CAN interface project did not yield a start/stop receiver specification. Irrelevant substring hits were discarded.

Primary source already available locally: exact child18175406d0cc5af8233afde70a5d121aedf8de44, opendbc/dbc/ford_lincoln_base_pt.dbc:2602–2605. [Pinned source](https://github.com/adgower/opendbc/blob/18175406d0cc5af8233afde70a5d121aedf8de44/opendbc/dbc/ford_lincoln_base_pt.dbc). It defines GWM as sender and ABS_ESC as recipient of the three named drive-mode fields. Bit0 is unnamed, so that metadata cannot establish its consumer. Its1121 attributes include HS2_CAN gateway metadata but no PCM acceptance specification. Local recent history has a spelling-label update and the earlier nested-path move, neither adding button/counter receiver rules.

Search hits reproducing the dictionary:
- https://github.com/AchterL/Bachelor_KI/blob/bdaf89d7303728267c79457595ea0d44c1036f6e/FileCarver/case/DATA/data/dbc/generated_dbc_file_53.dbc
- https://github.com/lowdown1983/m2-oem-database/blob/ba9a9503d9cdbaff1cf1736662cd1d46aacf1398/m2-oem-database/generated/wiki/vehicles.md
These are discovery leads only, not independent OEM validation. Generated/copy content is not a second confirmation of receiver semantics.

## What the cycling bits do in this capture

Independent raw-recording audit: [COUNTER_AUDIT.md](COUNTER_AUDIT.md). For q=(byte0>>1)&3, the observed publication sequence is0,1,2,3,0. All1,292 adjacent pairs within2s advance by exactly1 modulo4, including extra button-edge frames separated by about58ms. Including19 approximately6.5s gaps,1,311 of1,313 adjacent pairs advance by1. The two exceptions cross much longer gaps and have delta3. Because modulus4 aliases missing frames, gaps do not establish dropped-frame counts or reset behavior. The short edge-event intervals distinguish this sequence from a simple independent one-second clock.

Important distinction: the DBC names bits2–1 SelDrvMdeSwtch_No_Actl, not a counter. Its separately named SelDrvMdeCnt_D_Stat uses bits7–5 and remains zero. A per-publication sequence is an empirical interpretation for this Navigator capture, not a verified field definition across platforms.

Observed byte0 can be summarized as2*q+b with b=byte0&1, where b is the physical-button-related candidate. All other observed bits/bytes are zero in this sample. This compact expression describes captured bytes only; it is not a validated transmit encoder or instruction to zero other states. With button released, byte0 cycles00,02,04,06; with button held it cycles01,03,05,07. Phase continues across press/release rather than restarting at each press.

## Limits and correction to readiness language

Copying the latest q repeats it; incrementing q locally competes with the next genuine publisher value. Those conflicts are real properties of the observed sequence. Whether PCM cares about this q remains entirely unknown. The prior last-value/sampled receiver simulations are hypothetical sensitivity models; they do not prove actual PCM hold truncation or rejection. Therefore the current one-shot proposal remains **unvalidated**, not conclusively impossible.

The remaining exact question is: does this vehicle's PCM consume this bit in0x461, and if so does its receive implementation require q progression, accept repeats/skips, debounce b or use another translated request? Wiring and this DBC do not answer it. No passive analysis can substitute for a receiver definition or representative bench acceptance evidence.

## Useful request for an authoritative source

Request the2023 Navigator ATCM/GWM/PCM CAN communication matrix or receiver-interface definition for gatewayed AllTerrainControlData_FD1, CAN0x461(1121), including byte0bit0 and bits2–1, delivery to PCM on FD-CAN, sequence/duplicate/reset/timeout policy, validity checks and button-edge/debounce semantics. The distinction from diagnostic PID definitions and wiring diagrams is essential. No request was sent to Ford or any third party.
