<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Rolling-restart integral recovery prototype — October 26, 2026

**Implemented two local prototypes and rejected the bounded candidate after full replay. Do not integrate or install it.** The bounded version reduces excess demand in the two high-RPM windows and preserves the named city-braking regression exactly, but introduces weaker strong-demand braking fields and a simulated release-timeout in another saved route. Native packet acceptance does not clear those controller failures. The paired branches and Comma remain unchanged, including 1.20/0.97.

## What was prototyped

The installed-reference coordination function is taken from exact child `884c9f49167a8baffdb643559b5d341815172836`. The current local child `bcd706d0` already contains the earlier, uninstalled broad below-3 m/s guard. This experiment replaces that broad guard **only inside a local offline import seam**, rather than stacking the new policy on it or crediting its differences as improvements. Runtime differences between installed/current local source were inspected: the child difference is that broad integral guard; parent differences are its pin, documentation and tests.

The new stateful guard qualifies a moving slowdown followed by a rolling restart:

- Active, valid CAN state, no driver pedals and consistent owner/sequence/clock history.
- Previous movement at or above 4 m/s, followed by a fresh low-speed brake/precharge/reference-brake episode.
- No actual stop or cruise-standstill indication. Full-stop launches clear the moving history.
- Fresh owned allocator-protocol feedback in a limited engine-ramp phase at 0.3–3 m/s, with positive numerical gas authority and unmet positive demand. Inactive −5 is never used as an acceleration bound.
- Hold only positive native integral growth. Signed negative-error recovery and actual brake/precharge paths retain the installed behavior.

The first version held eligible positive growth for at most three seconds. It preserved the city fixture but prolonged braking elsewhere and failed the encoded-braking gate. It was rejected.

The second version additionally limits **cumulative positive integral growth omitted during one approach to 0.25 m/s²**. This is a declared research choice, not a proved physical tolerance. A one-step copy of the current production Python PID computes the exact growth that would otherwise occur under current limits. It is not a parallel reference history, forecast of vehicle response, output substitute, integral reset or reseed. A whole update is held only if its cost fits the remaining allowance; otherwise the approach is spent. Actual stop, disable, epoch/clock discontinuity or renewed normal motion clears qualification appropriately.

Maximum observed omitted growth in any approach is **0.24913 m/s²**. This budget does **not** bound total candidate-versus-baseline integral or command divergence: later feedback, saturation and brake-mode histories can diverge. No withheld integral is repaid artificially. Once authority returns or the bound/deadline is reached, the installed signed PID recovery continues.

No planner, propulsion/brake ramp, received-pressure clearance, deadline, safety limit, predicted-acceleration field, target-speed field, steering or geometry value was changed.

## Focused results

These are **frozen recorded motion/torque/planner/driver-response replays**, not predictions of changed RPM, gear shifting or physical comfort.

| Fixture | Installed reference | Bounded rolling candidate |
|---|---:|---:|
| Earlier high-RPM window: low-speed peak integral | 0.772 | 0.472 |
| Earlier high-RPM window: peak raw request, m/s² | 2.000 | 1.708 |
| Latest high-RPM window: low-speed peak integral | 0.827 | 0.593 |
| Latest high-RPM window: peak raw request, m/s² | 2.000 | 1.765 |
| Normal stopped-launch window: peak raw request, m/s² | 1.440 | 1.440 |
| Named city window: brake changes | **17** | **17** |
| Named city window: brake-command exposure | **21.533 s** | **21.533 s** |
| Original 63 mph highway window: brake changes | **20** | **20** |

The **entire named city route is byte-for-byte identical** in longitudinal wire output, not merely equal on switch count. The normal same-drive stopped-launch window is also unchanged. The two newer selected highway windows remain 22 and 12 changes respectively in this controller reconstruction; their original logged-send counts were 23 and 13, which are kept separate from reconstructed clocks/history.

The high-RPM windows do not demonstrate an overall smoother handoff. In the earlier window, braking exposure grows **1.940 → 2.677 s**; in the latest it grows **1.100 → 3.001 s**. The RPM and actual gear streams are frozen and unchanged, so the lower software request is not evidence of a lower road RPM peak or earlier real shift.

Exposure integrates the prior command over its interval until the next callback (left-held command timing). This differs slightly from older reports' right-endpoint summaries; both sides here use the same corrected calculation.

## Full controller replay: failed gates

Processed **197 segments / 12 routes / 570,269 callbacks**, comparing actual LongControl and CarController with causal returned software feedback. Baseline and candidate source fingerprints are bound before execution and rechecked after completion. The encoded brake-acceleration field is compared on **every common active strong-target row**, independent of whether the candidate raw request increased. Unit regressions cover equal/lower producer raw hiding a weaker encoded request.

Results:

- **32,122 changed longitudinal packets**; no disabled-owner wire changes.
- No commanded gas under brake/precharge, no checked moving-PID gas under retained pressure, and no newly introduced positive-gas/valid-fresh-retained-torque rows in the checked corpus.
- **19 weaker encoded brake-acceleration fields during common active target demand ≤ −0.5 m/s²**, all with a brake bit. Each difference is one encoded increment, about **0.0039 m/s²**. There are also 110 weaker raw requests in that stronger-demand cohort. A past tolerance acceptance for another candidate is not silently reused here.
- Added simulated **`release_timeout_disengage` at approximately 61.23 mph**, 555.912 seconds into retained `alpha-comfort-session-01`.
- That fault changes subsequent engagement history: **8,969 callbacks lose simulated longitudinal activity** versus the reference. These are replay rows following one fault, not 8,969 observed road incidents.
- On the common active/pedal-free comparison cohort, brake changes are 1,376 → 1,357 while brake exposure grows **2,475.352 → 2,516.158 s**. Fewer changes is not a demonstrated coasting improvement, especially when a fault also removes activity.

The last rolling hold before the added fault occurs roughly **317 seconds earlier**. That is why a local omitted-growth budget does not certify later recovery behavior. The changed history reaches a different release/pressure wait while the recorded reference torque continues rising or remaining nonzero. This is a **simulated fault under frozen reference response**, not proof the changed vehicle would reproduce it. It is nevertheless a failed gate; no clearance rule or timeout was weakened to hide it.

The earlier unbounded version is retained as preliminary failed evidence. Its run preceded the tightened missing-input handling and its numbers are not presented as a controlled one-parameter ablation against the bounded run. Both versions are rejected; there was no tolerance sweep to force a passing fixture.

## Data limitations and replay corrections

Eleven routes, **185 segments / 534,518 callbacks**, have no active atomic-input gaps under the audit. One retained 12-segment `highway-pulsing-session-01` contains **five active prefix updates** without complete logged producer inputs and is restricted to diagnostic evidence. The full corpus is processed, but is not described as perfectly reconstructed PID history.

Inactive missing-input updates now explicitly reset PID/output/state to off, consistent with production. Active missing-input updates retain the recorded payload only as disclosed diagnostic fallback and clear rolling qualification; they never seed the integral from a logged future value. Invalid atomic transport disables the rolling intervention while the installed reference path remains explicit. All 19 weaker encoded fields and the added fault occur in the **input-complete** `alpha-comfort-session-01` route, so excluding the diagnostic prefix cannot clear the rejection.

The outgoing control's phase is intentionally the **pre-update** LoC phase: production `controlsd.py` assigns it before `LoC.update`. The logged controlsState/producer phase is post-update. The two meanings are documented instead of changing production ordering to make a phase gate pass.

Exact hidden CAN receive-drain ordering is not recorded. Packet timestamps, validity, torque ages, owner context and source intervals are retained; no synthetic pressure clearance, heartbeat, permission or vehicle response is introduced.

## Full native RX/TX replay: no added hook rejection

A fresh native C build from exact local child `bcd706d0` processed the **same 197 segments / 12 routes** using recorded RX, original non-ACC TX, timers and replacement ACC frames at actual logged send slots:

- **45,641,383 received frames**; zero native RX rejections in the recorded streams.
- **777,090 original non-ACC TX frames** retained.
- **570,178 reconstructed ACC replacement slots**; one original ACC slot outside reconstruction remains unchanged. These are send-slot counts, not an assertion of one-to-one coverage of every software callback.
- **134 retained TX rejections in each variant**, **zero added candidate TX rejections**, zero relay faults.
- No forced controls permission, injected heartbeat, forwarding injection, hardware connection or changed ECU response.

The build uses debug hooks without sanitizers. This proves only relative recorded-stream hook compatibility at the checked send slots. It does not prove successful engagement, brake clearance on changed dynamics, stopping distance, RPM, shifting or comfort. Native acceptance does not offset the failed software braking/fault gates.

No ARM/device build or road test was performed.

## Tests, review and disposition

**46 focused tests pass**, including real production-PID stopped/rolling behavior, signed recovery, sentinel handling, pressure/brake-phase exclusion, stale/invalid feedback, owner/epoch/sequence/clock resets, exact deadline, omitted-growth budget, and the independent encoded-braking checks. RED/GREEN logs are retained. Independent review confirmed the native one-step budget accounting and resolved the braking, missing-input and phase-reporting issues; it supports rejecting the candidate.

**Do not integrate either prototype.** The useful progress is that narrow rolling qualification preserves the named city/full-stop fixtures and reduces excess stored request; what remains unresolved is recovery across later brake/propulsion decisions with a truthful changed response. The next local design must address that long-running feedback interaction, not relax pressure clearance or infer physical success from lower request peaks.

The earlier broad below-6.7 mph guard remains in the local pair unchanged and uninstalled; this experiment neither deploys nor silently reverts it. Local parent remains `2ca969e45afee229d7ec5c03c8768e137410c8d1`, child `bcd706d02fd6b8159b1eadcb6b2a56b504f69567`. No device access, settings change, publishing, activation, reboot, OS/firmware update or CAN transmission occurred. Steering 1.20/0.97 and geometry remain unchanged.

`DESIGN.md`, `policy.py`, RED/GREEN tests, exact-source replay receipts, `comparison-installed_state-rolling.json`, `gate-summary.json`, `release-fault-context.json`, native source/coverage receipts and final verification preserve the evidence. Raw recordings and full source-rich traces remain private local caches.
