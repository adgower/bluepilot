<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Controls Mismatch timing prototype — October 23, 2026

**Local prototype complete; final replay and local checks passed. No device access, push, commit or activation.**

Baseline pair: parent `fe08ede1af29a9c37b0c8b3550ce66cbd9392348`, child `d2e8d0404143da0f2685c2ff4932b9b9f702951f`. Parent working changes are limited to coordination transport, producer publication and isolated regression tests. The child is unchanged and clean. Owner **1.20/0.97**, geometry, steering and native safety remain unchanged.

## Cause and repair

At the saved 64.2 mph failure, the main producer used an 81.5211 ms-old motion sample. Another 22.846956 ms elapsed before the real consumer callback, reaching **104.368056 ms** and correctly tripping the existing 100 ms guard. A newer healthy motion publication existed before request creation but was absent from that producer snapshot. Publication chronology cannot establish exact original IPC receipt.

The opt-in coordinator now has its own two-topic subscriber, drained with `update(0)` immediately before publication. Motion and calibration are selected independently by the newest publication time across main and late caches. A dedicated `PoseCalibrator` rebuilds orientation, angular velocity, source time and validity together.

The original motion timestamp, command timestamp, sequence, epoch, requested acceleration, ownership and reference withdrawal are retained. Main producer invalidity remains authoritative. Newly published invalid, reversed, future or stale data still faults; the **100 ms limit is unchanged**. Missing late data can use the primary cache. There is no global main-subscriber late poll, timestamp restamping, forced validity or native permission override.

Default-off creates no added subscriber. Inactive, stop and creep paths retain existing publication behavior. Lateral targets, lateral calibration and the child controller are unchanged. This addresses a false timing fault; it does not address Alpha ride quality, model speed selection or fuel use.

## Completed evidence

| Check | Result |
|---|---|
| Focused contracts | 37 pose cases plus 7 coordination cases pass; production publish/schema and actual Card/CarInterface/Ford consumer exercised |
| Independent review | Older-cache rollback found, reproduced failing, repaired; final review found no remaining implementation blocker |
| Exact saved fault | Baseline rejects 104.368056 ms; prototype uses the actual newer source at 44.72413 ms and does not fault |
| Real local IPC | Production nonblocking poll consumes a pending newer motion message; original source time retained |
| Final new-drive native replay | 33 segments, one baseline pose fault, zero prototype faults; 7,766,004 RX and 229,676 TX per variant; zero added rejection or relay fault |
| Unchanged exclusions | 36,755 inactive/stop/creep packets exact in new-drive replay |
| Parent tests | 1,029 passed, 87 skipped, one expected failure, 281 passing subtests |
| Unchanged child tests | 4,485 passed, 1,690 skipped, 24,693 passing subtests |
| Builds | Minimal/full Mac and standalone Panda builds passed; full Mac build repeated on final reviewed source |
| Lint | Changed files pass Ruff and `git diff --check` |

Fourteen button/permission rejections occur in recorded, regenerated baseline and prototype streams alike; **zero added rejection** does not mean zero existing recorded rejection. No native controls permission was forced. The new-drive replay reconstructs actual consumer callback time and consumed epoch/sequence from logged feedback, while sensor inputs remain past-only and native hooks retain original wire/log chronology. Earlier send-log-time harness attempts are preserved and explicitly excluded as timing-fix evidence; see [clock note](CLOCK_NOTE.md) and [new-drive summary](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The exact fault reproduction uses a fresh controller to isolate the pose guard; it does not restore all historical controller state. The separate full-drive replay preserves state across each session. Logged ownership after the original fault is not extended.

Retained longitudinal frozen/model/observed/native/response checks also pass: 65,736 slots per stream; default-off exact ACC parity, identical non-ACC hashes, and 36,086 inactive/stop/creep exclusions unchanged. The changed-command/old-observed-feedback stress still faults and is not treated as a valid physical response. Generic response simulations are not ride or fuel proof. Two retained longitudinal native replays each process 5.26 million RX frames with no added rejection.

**Final historical replay passed:** all 1,048 segments / 73 routes, 240,099,844 physical RX frames and 3,894,845 generated TX frames per recorded-context variant. Recorded-context reference and prototype share 402 rejections; zero added rejection, protected-scope change or phase/counter mismatch. See [full summary](../../navigator-reference/PRIVATE_ARTIFACTS.md). This broad regression protects the unchanged controller and safety behavior; it does not exercise the added parent IPC poll. Targeted producer/IPC and new-drive checks above cover that path.

The historical replay retains 402 shared regenerated-frame rejections: 356 button and 46 steering messages. Its receipts also preserve 833 generated frames before Ford configuration (excluded from TX-hook evaluation), 72 shared invalid-configuration ticks, and 11,481 baseline-versus-recorded active-angle reconstruction mismatches out of 475,702 comparisons. This is a comparative regression result, not an exact reconstruction of every original on-road command. These differences are not introduced by the timing prototype; no safety permission was forced.

## Scope and next gate

This is a local exploratory prototype, not an installed fix. Saved chronology tests conservative past-publication availability, not exact historical IPC arrival. Mac IPC timing is not ARM scheduling proof. Device engagement and release under real load remain separate ARM, parked and road validation gates.

The full parent suite initially encountered sandbox-only temporary-directory failures; the complete rerun with local fixture access passed. Partial broad runs were stopped and retained when review required production source changes; the final frozen-source run completed successfully and is the one used for completion. See [review](REVIEW.md), [frozen source hashes](../../navigator-reference/PRIVATE_ARTIFACTS.md) and [preservation receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md).

Alpha smoothness remains unresolved and OEM ACC remains the comparison baseline. No Comma settings, parameters, learned calibration, firmware or OS were touched.
