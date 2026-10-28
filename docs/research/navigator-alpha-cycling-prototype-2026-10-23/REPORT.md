<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local Alpha cycling prototype — October 23, 2026

## Outcome

A **report-local bounded brake-admission prototype is implemented**, but it is a **partial reduction, not a resolved cycling fix or an installation candidate**. It reduces reconstructed eligible brake edges from213 to 179 (**16.0%**) across the drive. The worst highway window remains31 edges/20 seconds versus 33 baseline: plainly insufficient. Do not widen the suppression bounds merely to improve that count; a real new weak grade brake can be delayed by this experiment.

No paired branch integration, commit, push, device access or device/setting changes. Parent `ffebc43497f8015c37be5927800832f2719c7dca` / child `0ac9618972dd580281c5e933c7990f186522fbd4` and owner steering 1.20/0.97 are retained. This task used saved logs only.

## Mechanism investigated

The installed new release/handoff prevents simultaneous active braking and valid propulsion, but its brake decision can still switch around pitch-adjusted zero. Brake entry withdraws propulsion and clears its ramp history. Clearing the bit triggers fresh qualification and bounded ramp rise. Repeated short intervals therefore alternate brake/coast/partial propulsion. The drive contains positive raw controller demand alongside negative net pitch-adjusted demand.

The conservative prototype admits existing holds, stopping/low speed, negative/raw near-zero intent and stronger negative grade demand unchanged. It qualifies only a *new*, weak negative net entry while raw intent is positive and speed>=3m/s. [Design and exact boundaries](DESIGN.md), [prototype module](../../navigator-reference/PRIVATE_ARTIFACTS.md), [reviewable local patch](../../navigator-reference/PRIVATE_ARTIFACTS.md), [staged source](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The initial timer-only hypothesis allowed negative-biased grade pulses to evade admission indefinitely by resetting the timer. Independent review exposed it; a failing adversarial test was added, then signed demand-area debt retained across weak positive crossings fixed that specific escape. Budget/sampling and new weak-grade delay limits remain explicit. The initial version and red logs are retained; no claim that grade behavior is physically validated.

## Replay fidelity and results

Fresh full-rate inputs from all 23 Alpha segments:328,469 state/control/ACC-slot events, each raw segment hash checked. No 20 Hz extraction used to reconstruct controller inputs. [Input receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Baseline reconstruction on65,736 actual ACC slots matches63,132 recorded messages (**96.04%**). Brake/precharge differs on 40 slots; propulsion differs on 2,568. Reconstructed eligible edges 213 versus 209 recorded. Frame phase, internal receive ordering and controller-call time are not logged exactly. Consequently this is a frozen-input comparison of two reconstructions, not an exact production replay or a prediction of new vehicle acceleration.

| Reconstructed window | Baseline edges | Candidate edges | Positive-propulsion share, baseline→candidate |
|---|---:|---:|---:|
| <private clock time>–<private clock time> CDT, about69mph | 33 | 31 | 43.8%→54.8% |
| <private clock time>–<private clock time> CDT, overlapping, about70.5mph | 24 | 22 | 47.4%→56.0% |
| <private clock time>–<private clock time> CDT, about22mph | 24 | 18 | 31.7%→41.5% |
| Full drive, active/pedal-free/>5mph | 213 | 179 | Not an OEM comfort score |

1,370ACC slots change; only propulsion and brake/precharge bits differ. **All braking-acceleration wire values identical.** Zero changed inactive, stopping or below 3 m/s slots in this fixed-input drive comparison. Non-ACC message stream hashes match within the reconstructed ACC-slot update calls; production non-ACC updates between those calls were not replayed. Zero active brake+valid-propulsion overlap. [Comparison](../../navigator-reference/PRIVATE_ARTIFACTS.md), [baseline](../../navigator-reference/PRIVATE_ARTIFACTS.md), [candidate](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Historical isolated Alpha segment:2,983 slots; eligible edges 3→3, zero overlap, non-ACC hashes equal. Unknown prior controller state, initialized to default, makes this a compatibility comparison rather than reproduction of that old drive. [Historical baseline](../../navigator-reference/PRIVATE_ARTIFACTS.md), [historical candidate](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Native RX/TX validation

The first RX replay incorrectly initialized Ford mode from recording start, while the device log was initially in diagnostic/ELM mode. It latched a relay fault and rejected *every* recorded/baseline/candidate TX. That run is invalid and retained in `rx-invalid-startup.json`; equal rejection counts are not success evidence.

Corrected replay starts from the first logged Panda Ford11 configuration, excluding pre-configuration frames. **5,260,361 RX frames  / 65,728 ACC TX slots per variant**: recorded, reconstructed baseline and candidate each have the same 3 ACC rejections, no added candidate rejection, no final relay fault. Permission comes from RX; it is not forced. The three rejected commands occur during driver-brake transitions while recorded longActive stilltrue and native permissionfalse. The broader on-road 8 counter increments are not all explained: only ACC TX is exercised here, not lateral/other messages.

This is fresh Mac debug native safety hooks (no sanitizer), raw bus0–3 RX, timer/tick, and ACC-only TX. No hardware, full lateral/forwarding/heartbeat replay or physical grade/comfort validation. [Native receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md), [executable replay](../../navigator-reference/PRIVATE_ARTIFACTS.md).

## Software verification

- 11 new admission contracts pass, with baseline/adversarial failures observed before the corresponding changes. Includes exact debt/grade thresholds, irregular cadence, persistent/alternating grade, invalid recovery, existing holds and stop/low-speed bypass.
- 33 retained child/actual parent coordination, handoff, release and stopping→PID-cap tests pass against the in-memory candidate. Covers the previously resolved restart deadlock.
- Full retained Ford/native suites: **886 passed, 79 skipped, 12,083 subtests passed**. The 32 child coordination tests overlap this suite; the 33-test focused run adds one actual parent restart regression.
- Exported staged source separately replayed over all 65,736 slots: ACC stream hash, non-ACC hash and comparison counts exactly match the in-memory prototype. [Final verification receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md).
- No paired builds/ARM/device tests: no production integration was made or authorized here.

## Remaining blocker and next local direction

Most remaining candidate brake entries are **persistent weak negative net** or the new demand-budget limit, not a one-frame artifact. In the whole drive, candidate brake-on events include 62 persistent-net entries and 19 budget admissions; only 12 are immediate raw-deceleration/stronger-grade admissions. Removing those entries indiscriminately could suppress real grade braking. The conservative bound therefore does not solve the main highway issue.

Next local work should separate the calibrated body-pitch contribution, steady grade, longitudinal feedback/integral offset and actuator release/resumption delay using this saved drive's command/ECU-response chronology. The repeated ramp reset is visible, but response changes under a modified controller require a justified closed-loop response model or later carefully scoped physical validation, not only frozen-input edge counts. Do not simultaneously increase PID gains or relax braking while this ambiguity remains.

Current recommendation remains OEM ACC for ordinary driving. The device was not contacted or changed during this prototype task; Alpha remains whatever the owner last selected. No new road trial requested.
