<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Controlled stationary start/stop acceptance test — preparation only

Date: 2026-10-16
Status: NOT READY TO EXECUTE. Procedure for review; no sender, safety changes, deployment or CAN transmission authorized or performed.

Offline follow-up: [OFFLINE_VALIDATION.md](OFFLINE_VALIDATION.md) found counter-like sequencing conflicts and stock frames interrupting hypothetical press intervals. The parallel one-shot approach has not passed readiness gates; do not execute this procedure without resolving them.

## Question and evidence standard

Does a bounded software-generated press/release of the candidate 0x461 byte0 bit0 on vehicle-side logical bus0 cause the independently observed start/stop mode in 0x166 to change without a physical button press?

A Panda TX echo or lack of a TX rejection proves neither PCM receipt nor acceptance. A correlated0x166 change and consistent physical dashboard/button indication support functional acceptance of this input through the vehicle network; they do not independently prove which ECU consumed0x461 directly. Stationary acceptance is not approval for an on-road feature.

## Recorded basis

See REPORT.md, WIRING_FINDINGS.md and frames.json. Physical presses correlate with bit0 pulses; sustained holds last1.90–2.11s, with mode changes20–80ms after falling edges. These are observations, not a validated sender timing specification. The low three bits vary; the other seven bytes were zero in the sampled frames. Do not generalize those zeros or reconstruct unspecified fields from scratch. Wiring supports a shared vehicle-side FD-CAN path; PCM acceptance remains the experiment's question.

## Gates before any vehicle execution

All gates must be completed in a separate authorized implementation/testing stage; preparing this document does not authorize them.

1. Reconfirm exact parent/submodule revisions, actual running Panda firmware identity and safety mode/parameters, hardware bus mapping, and vehicle configuration. Saved CarParams and matching source hashes alone are insufficient. No concurrent updater or software deployment.
2. Prepare an isolated reviewed sender and narrowly constrained Ford safety support. The current allowlist rejects0x461. Do not enable all-output/ELM327/unrestricted safety, disable standard controls protections, or bypass TX checks. No diagnostic or safety-mode changes to get around the allowlist.
3. Establish how to retain every unrelated field, fresh stock context and any required counter/validity behavior. Existing drive-mode fields and the cycling first-byte pattern are unresolved. A known recorded payload is a fixture, not permission to replay it unchanged onto the car. If this cannot be justified, stop and use a representative isolated bench before vehicle injection.
4. Specify and review a finite sender schedule before deployment: exact permitted payload transformation, current vehicle-side bus0 only, maximum press interval, release behavior, frame count/rate limits and response deadline. Do not invent these while the vehicle test is running. Select a single previously observed brief pulse as the proposed initial duration; it must first pass offline analysis of timing, stock interleaving and receiver-sampling uncertainty. The long holds are not a requirement for the first trial.
5. Account for the genuine gateway publisher explicitly. Do not disconnect it, suppress its original traffic, overwrite other drive-mode fields, or use repeated/higher-rate frames to overpower it. If safely bounded coexistence cannot be demonstrated offline/bench, do not proceed with the vehicle trial.
6. Independent recorder starts before sender arming and captures physical RX, attempted TX, returned/rejected frames,0x166 status, speed, gear, ignition and relevant health. Use the matching schema, retain raw bytes, and record monotonic timestamps. Observe existing fault indicators; no clearing of DTCs. Active diagnostic requests are outside the initial test unless separately approved.
7. Physical operator and laptop observer review the exact trial. Explicit authorization is required before deployment, firmware changes or any experimental transmission. Authorization to prepare is not authorization to execute.

## Offline verification required for a future sender

These are planned checks, not checks run in this preparation task.

- Replay recorded idle, brief-press and long-hold fixtures. Confirm raw extraction and independent0x166 enum decoding, including unknown/unavailable values.
- Verify modifications affect only the reviewed bit and any separately proven-required validity fields; retain every unrelated field. Reject wrong length, unexpected frame variants and stale stock input.
- Prove no transmission before explicit arming. Reject nonzero speed, non-Park, unknown state, stale/missing vehicle data, ignition changes, unexpected active assistance and recording failure.
- Enforce ID0x461, bus0, validated length and finite limits in the intended safety/sender boundary. Confirm bus2 and other IDs remain blocked, and existing Ford safety tests still pass.
- Simulate normal gateway interleaving, delayed/duplicate input, lost status, repeated arm requests, interruption during press and process exit. No duplicate trial or automatic retry.
- Define tested interruption semantics. A held-level protocol may require a bounded release frame; do not promise that process termination alone guarantees release. Any release must remain subject to safety checks and the reviewed finite budget. Avoid leaving a latched high state or a sender loop.
- Verify two independent controls: a hard expiry enforced by the sender and a direct operator stop. Prove expiry does not depend on UI responsiveness or continued SSH connectivity.
- If observations imply a counter/checksum or routing behavior the implementation cannot explain, fail the readiness gate.

## Environment and roles

Vehicle stationary outdoors in a clear, level location; transmission Park, parking brake applied, vehicle secured, normal ignition/engine-running state. The trial concerns disabling automatic stop at traffic lights, not starting or stopping ignition. No engine-off/auto-stop trial, shifting, acceleration, steering control, or road movement.

The physical operator remains in the driver's seat and watches vehicle indications. A second observer operates the laptop and recording. Do not reach for the laptop while responsible for vehicle controls. Stop for any person entering the work area, unexpected movement, state uncertainty, warning or abnormal vehicle behavior.

## Baseline immediately before the one-shot trial

1. Record software/firmware identity, safety configuration and operator time marker.
2. Observe at least30s of stable stationary vehicle state with sender disarmed. Verify normal CAN flow and recording health, no relevant new warnings, known0x166 enum, and no unrelated drive-mode operation.
3. With sender still disarmed, use the physical button once if necessary to establish start/stop ENABLED (0x166 mode0). Confirm both CAN status and the corresponding vehicle indication. Then wait at least10s without touching the switch or other controls. If the state cannot be established or disagrees between observations, stop.
4. Confirm active driver-assistance control is not engaged, gear/speed/ignition are known and stable, and the physical button is released. The initial active trial requests disabled, never an automatic enabling request.
5. Read back the reviewed finite schedule, limits and expiration. Confirm no other sender is running. Arm exactly one trial only when all gates pass.

## Single trial

1. Announce/mark T0. Operator does not touch the physical button.
2. Execute exactly one reviewed bounded press/release schedule; no continuous broadcast or repeat.
3. Recorder captures the candidate, stock publisher interleaving, attempted/returned/rejected TX and0x166. Sender finishes and disarms independently of whether a response arrives.
4. Observe for5s after the planned release as an initial analysis window. This is a conservative experimental deadline, not an OEM response specification. Record state and physical indications. No response does not trigger a retry.
5. Continue passive recording for at least30s to check stability and warning changes. Confirm sender is stopped/disarmed. Any restoration of initial state uses the physical button after the trial and is separately marked; never automatically send another toggle.

## Abort criteria

Abort before arming for any unmet gate, uncertain vehicle/network state or missing recorder. During the trial abort under the prevalidated interruption/release policy for vehicle movement, loss of Park, new warnings, driver-assistance activation, CAN errors/abnormal traffic, stale stock/status data, unexpected payload or controls, an unrequested second toggle, or any operator concern. Do not chase an abnormal response with more frames. Leave the vehicle secured and preserve evidence; do not reboot, reflash or clear faults as an improvised recovery step.

## Classify the outcome

| Evidence | Conclusion |
| --- | --- |
| No allowed TX / explicit rejection | Test did not reach the intended transport path; says nothing about PCM acceptance. |
| Allowed TX/echo, no independent state change | Acceptance not demonstrated. Wrong semantics, routing, timing, interleaving or receiver filtering remain possible; not proof that control is impossible. |
| Exactly one enabled->disabled status change, matching vehicle indication, no physical press, clean bounded TX record | Provisional functional acceptance of the injected input path. Preserve exact timing and payloads; no automatic repeat or on-road rollout. |
| Multiple toggles, warnings, conflicts or inconsistent indications | Failed/unsafe result. Stop; analyze offline. |
| Missing/incomplete logs or ambiguous physical input | Inconclusive; do not claim acceptance. |

A second confirmation trial or any test of software enabling requires review of the first result and separate authorization. Success does not resolve long-term coexistence, ignition-cycle behavior or normal driving safety.

## Deliverables after any future authorized execution

Unmodified raw recording, sender/safety source revision, firmware identity, exact schedule and all attempted/accepted/rejected TX, before/after status and vehicle observations, recorded stop/disarm evidence and outcome classification. Keep personal identifiers private. No deployment or road-validation claims based on this single stationary experiment.
