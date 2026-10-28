<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# 2023 Lincoln Navigator automatic start/stop — evidence and testing handoff

Prepared 2026-10-16, America/Chicago. Audience: an LLM assisting the vehicle owner with further investigation and potentially a separately authorized test.

## Read this first

Latest local revision: [owner-integrated candidate v2](review-candidate-v2/README.md) supersedes the v1 publisher/timing/release implementation discussion below. It integrates into pandad's existing writer, moves reserved neutral scheduling to the MCU, adds queue expiry and graceful-exit ordering, and preserves immediate ignition-off/offroad NO_OUTPUT. Source activation stays disabled; full binary/firmware builds, wire timing and receiver acceptance remain unverified. See its patches, native validation log and independent review. Current human authorization includes preparing local source changes only; no deployment or experimental transmission is authorized.

The goal is to toggle **automatic engine stop at traffic lights**, equivalent to the physical disable button. This is NOT the ignition/start button, remote start, a request to stop a running engine, or an emissions/configuration coding change.

**Current authorization is documentation and offline analysis only.** The owner repeatedly required no device changes and no experimental CAN messages. This handoff does not authorize execution, safety/firmware changes, diagnostic transmissions, deployment or active tests. A future agent must obtain explicit scope from the human before those actions. Merely receiving this document is not execution approval.

No experimental CAN injection has been performed. A later locally authorized review candidate now exists under review-candidate/README.md: a debug-gated safety patch, dry-run CLI and dormant adapter. Its --execute path is blocked; single-writer integration and release/receiver guarantees remain unresolved. Earlier statements below describe the original research snapshot unless explicitly updated. No firmware/safety/vehicle-setting changes were made for this investigation. Earlier in the conversation, the owner manually started the existing CAN-to-ZMQ bridge for passive Cabana recording. Later analyses were entirely local. A previous source-verification session used read-only SSH.

**Current finding:** raw byte0 bit0 of CAN ID0x461 is strongly correlated with physical start/stop button presses. Bits2–1 behave as a two-bit publication sequence in the capture. Current Ford safety source blocks host transmission of0x461. PCM consumption, validity checks and acceptance of a parallel publisher are unproven. The proposed parked test is **not ready to execute**.

## 1. What the next agent should do

1. Read the conclusions and corrections below before assuming an implementation exists.
2. Reproduce or inspect the local evidence. Completion: identify exact input recording, code versions, candidate/status bit extraction and analysis limitations.
3. Resolve receiver identity/acceptance and coexistence using authoritative message documentation or a representative isolated bench. Completion: produce evidence for receiver behavior, not a simulated assumption.
4. If proposing a vehicle experiment, present the exact bounded implementation, firmware/safety implications, interruption/release behavior, success criteria and remaining risks for human review before deployment or transmission.
5. Preserve all existing checkouts, vehicle configuration, fault evidence and genuine publisher traffic. Work in an isolated local checkout for any later code work.

The safest active environment is a representative isolated automotive bench operated by someone equipped for that work. It must reproduce the relevant modules/network; a fabricated receiver model is not a PCM substitute. A supervised parked vehicle test is a later decision, not implied by this handoff.

## 2. Environment and provenance

These are snapshots observed during this conversation, not a promise of current state. Reverify before any later action.

| Item | Observed value |
| --- | --- |
| Vehicle | Owner's2023 Lincoln Navigator; VIN/build-specific applicability not independently verified |
| Device | Owner's comma4, reachable at comma@<private host> during prior inspection |
| Device repository | /data/openpilot |
| Branch | codex/navigator-tracking-release |
| Parent commit | 9da98d0c91f0559efa976e3ffb221f2584fd0b88 |
| opendbc child | 18175406d0cc5af8233afde70a5d121aedf8de44 |
| Origin | https://github.com/adgower/openpilot.git |
| Matching Mac checkout | ${USER_HOME}/Apps/openpilot/.navigator-master-integration-20261014 |
| Saved CarParams | FORD_EXPEDITION_MK4; flags15; Ford safetyParam10; networkLocation=fwdCamera |
| Analysis/report directory | ${USER_HOME}/Apps/bluepilot/docs/research/navigator-startstop-2026-10-16 |

The Navigator is represented by an Expedition platform selection in saved parameters. Matching source and saved CarParams do not prove the currently running Panda safety mode or the flashed MCU firmware identity.

Installed source hashes matched this local checkout when checked:

| Source under /data/openpilot | SHA256 |
| --- | --- |
| opendbc_repo/opendbc/safety/modes/ford.h | bd912f0f60bf4f7b632ad2e5e369317ce6e6e2199eef14f904a660ef80928e80 |
| opendbc_repo/opendbc/car/ford/carcontroller.py | 0570911df69167805833196f4feba13efaa840ed9f7e2a385649fcb882ebe5b4 |
| opendbc_repo/opendbc/car/ford/fordcan.py | 5ae496e81d234e671d66dd8d37080bd8414489351d99504b84117f22af9285ef |

Both inspected parent/child status outputs were clean at that point. Separately, ${USER_HOME}/Apps/bluepilot is a dirty bp-dev checkout with unrelated README.md changes and untracked research/roadmap material. Do not reset, switch, clean or overwrite it. This investigation added local research artifacts only.

## 3. Raw recordings and reproduction

Cabana recorded locally on the Mac:

`${USER_HOME}/cabana_live_stream/2026-10-16--15-49-00--N/rlog`

Offline validation read existing segments N=0 through64 with no parse errors. These are uncompressed Cap'n Proto event streams read with the matching checkout's cereal schema. Analysis uses physical RX bus0, avoiding returned bus130 duplicates.

The recording timestamp origin is the first event's logMonoTime in segment0:7727.078886387 seconds. Reported elapsed times are each event's monotonic timestamp minus that origin. Approximate UI time can differ with buffering/playback/pauses. Segment numbers are logger wall-clock buckets, not an exact substitute for message-relative times. Pausing Cabana's display did not stop its raw recording.

Local-only reproduction, from the matching checkout:

```bash
cd ${USER_HOME}/Apps/openpilot/.navigator-master-integration-20261014
PYTHONPATH=.:opendbc_repo ./.venv/bin/python \
  ${USER_HOME}/Apps/bluepilot/docs/research/navigator-startstop-2026-10-16/offline_validate.py
```

This script reads local logs, runs pure byte/receiver-model checks, and writes offline_validation.json beside itself. It contains no CAN/SSH APIs. It is not a sender. It scans available segments0–64 at execution time, so preserve/hash a fixed input copy for a future formal reproduction. The earlier frames.json analyzes a smaller selected segment set and is superseded for aggregate statistics by offline_validation.json and COUNTER_AUDIT.md.

The independent counter audit used read-only scripts `${PRIVATE_CACHE}` and `${PRIVATE_CACHE}`; preserve local copies if still available. Temporary files are not guaranteed to survive cleanup. The report records their results.

## 4. Candidate message and independent state

### Candidate:0x461 / decimal1121 / eight bytes

- Seen physically received on logical bus0.
- DBC name: AllTerrainControlData_FD1.
- Raw byte0 bit0 follows physical button holds. It is **not defined by this DBC**.
- Empirical sequence q=(byte0>>1)&3; raw button-related candidate b=byte0&1.
- Captured byte0 is2*q+b; the other seven bytes were zero in this parked sample. This describes observations, not a complete transmit encoding.
- Released first bytes cycle00,02,04,06; held first bytes cycle01,03,05,07. Phase continues through button transitions.
- No meaningful application checksum rule was recovered. Constant-zero remaining bytes do not prove absence of validity checks.

DBC source under the matching checkout: opendbc_repo/opendbc/dbc/ford_lincoln_base_pt.dbc:2602–2605:

```text
BO_ 1121 AllTerrainControlData_FD1: 8 GWM
 SG_ SelDrvMdeSwtch_No_Actl : 2|2@0+ (1,0) [0|3] "unitless" ABS_ESC
 SG_ SelDrvMdeSwtch_D_Stat : 4|2@0+ (1,0) [0|3] "SED" ABS_ESC
 SG_ SelDrvMdeCnt_D_Stat : 7|3@0+ (1,0) [0|7] "Counts" ABS_ESC
```

Motorola mapping matters: the cycling field is bits2–1, named SelDrvMdeSwtch_No_Actl. The field actually named Cnt occupies bits7–5 and stayed zero. The DBC lists GWM and named-field receiver ABS_ESC, not a verified PCM consumer for unnamed bit0. FrameGatewayNetwork=HS2_CAN at line5439 is provenance/routing metadata, not a PCM acceptance rule. The dictionary includes older/multiple-platform fields and is not a VIN-specific2023 protocol specification.

### Independent status:0x166 / decimal358

DBC name Stop_Start. Raw status extraction:

`mode=(payload[1]>>4)&3`

Signal StopStrtDrvMde_D_Indic, Motorola13|2:

| Value | DBC meaning |
| --- | --- |
| 0 | StopStart_Selected — enabled |
| 1 | StopStart_Deselected — disabled |
| 2 | StartStop_IndirectDeselect |
| 3 | NotUsed |

This is a two-bit enum; never silently treat any nonzero value as a confirmed disabled state. Status source is dictionary-labeled PCM_HEV, with GWM recipient; actual nonhybrid platform applicability comes from observed correlation, not the suffix alone.

A related indicator is StopStrtStdby_D_Indic in byte6 bits7–5. It alternated5/0 in these trials. Its DBC labels describe telltales, so do not substitute it for the explicit mode enum or engine-running status.

Other DBC-named request candidates remained constant during both examined trials:0x326 byte0bit3=0 and0x105 byte2bit7=1. Their names do not establish use on this vehicle.

## 5. Physical-button experiments and timing

Twelve complete candidate high pulses were found; each was followed by an independent mode change within500ms of its falling edge. Observed delays ranged approximately20–112ms. This is correlation, not a receiver specification or proof of injection acceptance.

Four repeated brief toggles:

| Elapsed time, approximate | Mode after change |
| --- | --- |
| <private clock time> | enabled |
| <private clock time> | disabled |
| <private clock time> | enabled |
| <private clock time> | disabled |

Owner then intentionally held the physical button, reporting the experiment interval1:03:30–<private clock time>:

| Candidate high interval | High duration | Independent mode change |
| --- | --- | --- |
| <private clock time>–<private clock time> | 1.900s | <private clock time> enabled |
| <private clock time>–<private clock time> | 2.110s | <private clock time> disabled |
| <private clock time>–<private clock time> | 2.011s | <private clock time> enabled |

The earlier owner instruction said hold about1s; recorded highs were about2s. Treat measured CAN durations as evidence, not the intended duration. Nine brief highs lasted approximately101–169ms. Final state after the held-button trial was enabled; do not carry forward the earlier statement that it was off.

## 6. Counter-like behavior and coexistence

Total physical bus0 frames analyzed:1,314. All1,292 adjacent pairs within2s satisfy q_next=(q+1)%4. This includes additional button-edge frames separated by as little as58.294ms. Median interval999.953ms. Nineteen further6.491–6.510s gaps also advance+1, always first byte06->00. Across all1,313 adjacent pairs,1,311 advance+1; two much longer gaps have delta3. Modulo aliasing prevents inferring exact missing-message counts or reset rules from those gaps.

This supports a publication sequence, not a free-running one-second phase or a count incremented only on button presses. It does not prove who generates q or whether the PCM validates it.

Offline byte preservation:512 checks cover256 first bytes and two candidate bit states, with deliberately nonzero other bytes; unrelated fields preserved and round-trip restored. Five incorrect lengths rejected. This proves arithmetic only.

Offline coexistence models use real idle stock timing plus hypothetical inserted high/low frames. Copying the latest stock q repeats a value; advancing it consumes a value the genuine publisher also uses next. Original gateway frames continue; camera forwarding control cannot erase traffic already delivered on the shared vehicle network.

A hypothetical last-value receiver sees stock released frames interrupt inserted highs. In100 sampled starting phases, nominal120ms pulses survive about9.53–120ms; nominal2s pulses survive9.53–999.53ms. These are **conditional simulations**, not measured PCM response, lower bounds, acceptance probabilities or proof of rejection. No actual PCM emulator was available. Edge-latched/debounced/counter-gated receivers could behave differently. Do not extend a hold or flood frames to compensate.

## 7. Network topology and documentation

### Year-specific wiring evidence

Located Ford-attributed diagrams in a third-party2023 Navigator Black Label manual collection. They are reproduced primary technical content, not an authenticated VIN-filtered Ford session; integrity/build applicability remain unverified.

[Auto-Start-Stop wiring page](https://lemon-manuals.la/Lincoln/2023/Navigator%20Black%20Label/Repair%20and%20Diagnosis/Electrical/Wiring%20Diagrams/OEM%20Wiring%20Diagrams/Auto-Start-Stop%20System/)

- Figure1/GFDWR184841 is explicitly EXPEDITION; do not substitute it for Navigator.
- [Figure2/GFDWR184842](https://lemon-manuals.la/images25/GFDWR184842/) is explicitly NAVIGATOR. Start/Stop switch and indicator are inside ATCM.
- ConnectorC3393 pin3 HS2CAN+ circuitVDB25 GN-OG; pin2 HS2CAN- circuitVDB26 GY-BU; pin1 supply, pin4 ground. Documentation only; no physical probing/modification performed or authorized.

[2023 network diagram/module chart](https://lemon-manuals.la/Lincoln/2023/Navigator%20Black%20Label/Repair%20and%20Diagnosis%20%28Single%20Page%29/Accessories%20%26%20Equipment/Communication%20Devices/Controller%20Area%20Network%20%28Can%29%20Module%20Communications%20Network%20%28Description%20%26%20Operation%29/Description%20And%20Operation/Controller%20Area%20Network%20%28CAN%29%20Module%20Communications%20Network%20-%20System%20Operation%20and%20Component%20Description/System%20Diagram/)

Chart places ATCM on HS-CAN2; PCM, IPMA(front camera), GWM on FD-CAN. GWM connects both networks.

### Supported path inference

```text
Physical button -> ATCM -> HS2-CAN -> GWM -> vehicle-side FD-CAN
                                            |-> PCM
                                            |-> Panda logical bus0
                                                  | forwarding
                                                  v
                                              logical bus2 -> isolated IPMA camera
```

Linking numeric0x461 and its unnamed bit to the ATCM path is a synthesis of wiring, dictionary metadata and recording correlation—not a statement printed in the wiring diagram. PCM consuming this bit is still unproven.

In segment63,66 received0x461 bus0 payloads exactly match66 ordered returned bus130 payloads; echo delays0–9.60ms. Panda adds128 for returned TX frames, so130 means returned physical bus2. It is not an additional vehicle network and not proof of independent ECU acknowledgment.

If the documented harness/network applies, a bus0 transmission is already on the PCM's shared FD-CAN segment; reverse gateway routing is not required for physical reachability. Physical reachability still does not prove ID/bit acceptance. A camera-side bus2 transmission is not equivalent to direct vehicle-side delivery.

### Documentation search status

No public model-correct PCM receive specification for0x461 was found. Exact symbol searches found copied DBCs/generated summaries rather than new receiver definitions. Ford's publicly accessed2020–2023 gasoline OBD summary provides diagnostics, not this CAN receive rule:
https://www.fordservicecontent.com/Ford_Content/catalog/motorcraft/OBD_System_Operation_Update.pdf

An older2018 Ford summary describes FCIM button input and rising-edge toggling. That generic architecture is not the Navigator-specific ATCM diagram, and its edge description does not match the observed post-falling-edge status timing. Do not use it as the exact protocol.

Official service resources: https://www.motorcraft.com/us/en_us/home/technical-resources.html/1000

No subscription purchase or authenticated VIN-specific documentation access occurred. A service subscription is not established to include an engineering CAN matrix; do not promise it does. The needed artifact is a2023 Navigator ATCM/GWM/PCM communication matrix or receiver-interface definition for gatewayed0x461: unnamed bit0, bits2–1, delivery to PCM, duplicate/skip/reset/timeout handling, validity checks and debounce/edge behavior. No request was sent to Ford or others.

## 8. Source and safety constraints

All references below are relative to the matching checkout in section2; line numbers are snapshots and should be checked at that revision.

- opendbc_repo/opendbc/car/ford/fordcan.py:4–18: logical main=offset, radar=offset+1, camera=offset+2. Logical numbers are not Ford HS-network labels.
- opendbc_repo/opendbc/car/ford/carcontroller.py:75–85 and fordcan.py:295–343: existing cruise/TJA button implementation uses Steering_Data_FD1, ID0x83. It is not a start/stop API.
- opendbc_repo/opendbc/safety/modes/ford.h:457–480: all normal/debug Ford TX lists omit0x461.
- opendbc_repo/opendbc/safety/safety.h:230–252: exact ID/bus/length allowlist gates host TX.
- safety.h:255–287 and ford.h hooks: ordinary forwarding0<->2 permits this stock frame; forwarding permission differs from host TX permission.
- openpilot/selfdrive/pandad/panda.cc:268–269 and panda.h:24: returned TX adds128 to the bus label.
- panda/board/drivers/fdcan.h:131 and forwarding path: returned flag and forwarded stock send behavior.

Compiled a fresh local plain debug host harness from the exact child source at ${PRIVATE_CACHE} Ford safety model6/param10 initialized successfully. Sixteen checks across bus0/2, controls_allowed false/true, and four observed eight-byte payloads were all rejected. Forward hook mapped0->2 and2->0. This is host-native safety evidence, not flashed firmware identity or a vehicle test; no sanitizer validation claimed. Temporary harness may no longer exist.

A Python controller change alone cannot overcome this source's safety allowlist. Retain standard protections; unrestricted-output safety or bypassing checks is outside the proposed approach.

## 9. Unresolved questions that gate active testing

- Is0x461 bit0 a command the PCM consumes, a gateway mirror, or an indication consumed elsewhere?
- Is q a receiver-enforced sequence, and who owns it? Initialization, wrap/reset, duplicate and missed-frame tolerance are unknown.
- What is the relevant debounce/edge/timeout behavior? Correlation after release is not a receiver state-machine specification.
- Do other vehicle/drive-mode states change unobserved bits or validity requirements?
- Can a bounded parallel publisher coexist without repeated toggles, network errors, unrelated drive-mode requests or losing ordinary gateway traffic?
- Does actual running firmware match the reviewed safety source and saved configuration?

A controlled test must distinguish these uncertainties. A missing response cannot alone prove rejection or impossibility.

## 10. Future test criteria — not an executable procedure

Detailed review draft: PARKED_TEST_PLAN.md. It is explicitly NOT READY; OFFLINE_VALIDATION.md identifies failed readiness gates.

Any later separately authorized test should use a finite, reviewed press/release schedule, fresh verified payload context, tested hard expiry and interruption/release semantics, and independent recording. The initial vehicle experiment, if ever justified, would start enabled and request disabled once, with Park, parking brake, zero speed, outdoors, physical operator plus observer, no active assistance, and no engine-off/road/shifting experiment. No automatic retry or automatic software restoration.

Classify evidence:

| Observation | Permitted conclusion |
| --- | --- |
| TX blocked/rejected | Intended transport path was not exercised |
| TX echo with no status change | Acceptance not demonstrated; reason unresolved |
| Exactly one matching0x166 and physical-indication change with no physical press | Provisional functional acceptance of injected input path, not direct proof of which ECU consumes it |
| Multiple toggles/warnings/conflicts | Failed/unsafe trial; stop and preserve logs |
| Incomplete recording/ambiguous operator input | Inconclusive |

Success requires independent mode feedback and vehicle observation, not an echo. Preserve attempted/rejected/returned TX, stock traffic and timestamps. Do not clear faults, reboot or modify firmware as an improvised response. A stationary success does not prove road safety, ignition-cycle behavior, production readiness or reliable long-term coexistence.

## 11. Corrections that must survive handoff

1. Cabana Suppress Highlighted suppresses recent byte-change highlighting across messages; it does not hide rows, stop counters or target only the selected row. Suppress Signals can hide changes in DBC-defined bits. These UI settings do not alter saved raw evidence.
2. Cabana changes working directory at startup; the earlier relative --dbc path failed. Absolute DBC paths fixed path resolution. This was not evidence of an invalid DBC.
3. The bridge's Address already in use arose because an earlier remote bridge remained running after SSH interruption. No need to start competing bridges. Old PID26153 is historical, not current process identity.
4. Bus130 is returned TX on bus2, not a third physical source.
5. Navigator-specific wiring uses ATCM; generic FCIM descriptions and the Expedition figure are not its circuit.
6. The sequence-like bits are1–2; the DBC field named Cnt is bits5–7 and stayed zero.
7. Simulated stock interference is conditional on assumed receiver behavior, not demonstrated PCM rejection.
8. Latest held-button experiment ended enabled; initial states must be re-established, never assumed from older chat statements.

## 12. Evidence index

Later local-only implementation: review-candidate/README.md, safety.patch, validation.log and review_startstop/ source/tests. This does not authorize deployment or transmission. The original matching source checkouts remain clean; the patch was developed in an isolated snapshot.

All files are under ${USER_HOME}/Apps/bluepilot/docs/research/navigator-startstop-2026-10-16/:

| File | Purpose |
| --- | --- |
| LLM_HANDOFF.md | This consolidated context and authorization boundary |
| REPORT.md | Initial provenance, candidate frames and host safety results |
| CODE_REVIEW.md | Source-level TX, forwarding and Ford API citations |
| NETWORK_SOURCE.md | Additional local topology and DBC review |
| NETWORK_ACCEPTANCE.md | Earlier topology uncertainty; refined by WIRING_FINDINGS.md |
| WIRING_FINDINGS.md | Year-specific diagrams, supported shared-network inference |
| PCM_SPEC_SEARCH.md | Public search scope, no recovered PCM acceptance specification |
| COUNTER_AUDIT.md | Independent raw-log sequence audit and simulation caveats |
| OFFLINE_VALIDATION.md | Byte preservation, timings and conditional coexistence results |
| offline_validation.json | Machine-readable aggregate results and hypothetical model cases |
| offline_validate.py | Local-only reproducible aggregate analysis |
| frames.json / analyze_frames.py | Earlier smaller sample analysis |
| PARKED_TEST_PLAN.md | Unexecuted review draft, failed readiness gates |

Essential evidence is summarized here so this file can be shared alone. For reproducibility on another machine, also transfer the analysis scripts/results and a fixed copy of the raw recordings with checksums. Raw recordings contain more vehicle information than the summaries; share them only with the owner's intended recipient. Do not infer missing raw data from the tables or fabricate a PCM specification.
