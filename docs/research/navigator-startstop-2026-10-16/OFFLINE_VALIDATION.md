<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Offline payload, timing and coexistence validation

2026-10-16. **Result: vehicle-test readiness fails for the proposed parallel one-shot sender.** Payload bit preservation passes, but coexistence and receiver timing/counter behavior remain unresolved. No device connection, change, CAN transmission or safety modification was performed. No runnable sender was created.

## Reproduction and scope

Analysis source: [offline_validate.py](../../navigator-reference/PRIVATE_ARTIFACTS.md). Results: [offline_validation.json](../../navigator-reference/PRIVATE_ARTIFACTS.md). Run from the matching openpilot checkout with its Python environment and PYTHONPATH=.:opendbc_repo, passing the absolute analysis script path. It reads only local recordings and writes its analysis JSON beside itself.

Read65 existing segments0–64 from ${USER_HOME}/cabana_live_stream/2026-10-16--15-49-00--N/rlog without parse errors. Found1,314 eight-byte0x461 physical-RX frames on bus0, spanning about00:01.57–<private clock time>. Other buses are excluded to avoid double-counting returned transmissions. Missing/unobserved stock intervals are not interpreted as evidence about the PCM. This is one parked recording, not all vehicle operating states.

## Payload preservation — narrow check passes

All sampled first bytes are0–7; other seven bytes are zero. Tested a pure in-memory bit0 replacement on all256 possible first-byte values and two target states, using deliberately nonzero other bytes:512 preservation/round-trip assertions passed. Five wrong lengths were rejected. The operation preserves bits1–7 and all other bytes by construction. This verifies byte manipulation only, not whether unchanged validity fields remain valid after changing bit0. No checksum receiver model or OEM rule is available.

## Timing — correlations confirmed, sender specification not proven

Found12 complete high pulses. All12 had an independent0x166 mode change20–112ms after the falling edge, within the selected500ms correlation window. Nine short pulses lasted approximately101–169ms; three holds lasted1.900,2.110 and2.011s. Mode changes alternate. This corroborates the observed input relationship; it does not establish PCM debounce, permissible injection duration or whether a request is consumed through another intermediate module.

Median0x461 interval is0.999953s. Among1,292 successive pairs separated by at most2s, the value(byte0>>1)&3 advances exactly+1 modulo4 in every pair:1,268 same-button-state pairs and24 edge pairs.21 larger gaps are excluded. This is strong empirical evidence of a per-frame counter-like field; its receiver enforcement is not known. The DBC calls overlapping bits a drive-mode switch field, not a confirmed rolling counter. Do not silently relabel the dictionary or assume an enforcement rule from the observed sequence.

## Coexistence — two independent problems

### Stock traffic interrupts a software hold

Used actual quiet released-state stock frames from segment63 and inserted hypothetical single high and low events in memory. Swept100 starting phases across one second, at nominal pulse durations120ms and2s. Original stock messages remained unmodified.

Under a hypothetical last-received-value receiver, a released stock frame ends the synthetic high interval. The120ms pulse survived approximately9.53–120ms across sampled phases; the nominal2s hold survived approximately9.53–999.53ms. This phase sweep is a discrete sensitivity study, not a lower bound: starting even closer to a stock frame could yield a shorter interval. It does not model equal-timestamp CAN arbitration, errors or actual PCM scheduling.

Illustrative sampled receivers with10/100/500/1,000ms periods and100 sampling phases produce differing detection counts. For a120ms nominal pulse, detections ranged95–100/100 at10ms,9–100 at100ms,2–25 at500ms and1–13 at1,000ms. These are deterministic phase counts for hypothetical receivers, **not acceptance probabilities or measured PCM sample periods**. They demonstrate why the recording cannot validate one proposed injection timing.

### Inserting frames changes the counter-like sequence

Copying the freshest stock frame and changing only bit0 repeats the counter-like value. Advancing it instead consumes the next value that the unchanged gateway publisher will also send. Exhaustively illustrated all four prior values: for prior value2 and expected stock next3, preserving yields2,2,3; incrementing yields2,3,3. Either single-insert strategy introduces a repeated value somewhere relative to the observed+1 sequence. In the two-event hypothetical schedules, both press/release copies produce two repeated-value transitions.

This does not prove the PCM validates these bits or would reject a duplicate. It demonstrates that a claim of full stock-compatible sequencing would be unsupported. Do not compensate by flooding, hiding gateway originals, replaying a drive-mode action or inventing new counter semantics. The camera harness cannot replace the gateway's messages already delivered on the shared vehicle segment.

## Decision and remaining work

The current safety allowlist still rejects0x461; no change was made. Even if permission were added, a fixed parallel press/release sender has not passed coexistence validation. **Do not execute the parked test on the strength of these results.**

The unresolved gates are model-correct definitions for0x461's candidate and cycling fields, whether PCM actually consumes this gatewayed ID, validity/edge semantics and competing-publisher behavior. Those require receiver documentation or a representative isolated bench with the relevant gateway/controller setup. A simulation that assumes receiver behavior cannot prove it. More button presses alone will not resolve those gates. No production feature or safety patch is justified by this offline result alone.
