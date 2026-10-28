<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Local signed-coast regression repair — October 27, 2026

**The final local prototype removes the previous candidate's added timeout and weaker-braking regressions across the full saved longitudinal corpus. It does not establish that the vehicle's highway pulsing is cured.** No paired-source, Comma, settings, firmware or CAN-transmission changes occurred. Owner 1.20/0.97 remains unchanged.

## What was repaired

The rejected pulse candidate combined true coast with a broad engine-ramp integral freeze. That changed integral history before coast was needed, delayed brake release, weakened later braking and added a release-timeout. The first repair restored the ordinary installed integral rule but still let true coast bypass release ownership: no brake/precharge bit meant the observer could remain already clear, so the following propulsion ramp differed from the precharge reference. That intermediate version still had 91 weaker encoded strong-target samples and is rejected (`repair.py`, revision 2).

The final `repair2.py` separates the modes:

- Ordinary ramps retain the installed numerical anti-windup predicate. No phase-wide freeze, I reset, reference-I copy, integral repayment or baseline-output oracle.
- Only an already-qualified, bounded weak precharge proposal can become true coast, after fresh observed clearance and valid owner/pose/target context. The installed weak-admission policy is retained. The same sampled-demand account, 0.01 allowance, 0.3-second deadline, debt retention, strong-demand bypass and earned rearm remain authoritative.
- True coast reports actual gas withdrawal and false brake/precharge bits. A new local revision-3 feedback contract distinguishes it from ordinary release using `release` phase, nominal/reference brake intent, finite trial age and remaining budget. The legacy-named precharge age/budget fields represent the bounded weak-allocation trial in this revision; they are not claims of physical precharge. Unsupported peers cannot admit the trial and fall back to nominal behavior.
- Only that explicit fresh bounded mode receives the installed signed-braking integral role. This keeps producer history equal without falsifying actual command bits.
- True coast arms a **logical clearance obligation**, not a physical brake command. The observer keeps `allow=false`, preserves owner/clock/freshness/reversal checks and clears qualification samples during coast. It cannot enter from an existing pending ordinary release. Continuation requires the same owner, current valid scope, fresh received torque at most 4 Nm, and the existing unspent trial. When coast ends, the inherited three new distinct clear readings spanning at least 40 ms are required before propulsion. The ordinary release timeout is unchanged; it is not suppressed or extended.

The transport experiment is implemented with isolated local hooks. It is **not a production protocol migration** and has not been ported into the paired branches.

## Full controller and producer replay

Reference source: openpilot `df788e02719c05595dab2f980e6fd9fb9e464006`, opendbc `1d29e6e78abcbf5c6a80eb397d80b349c6cca960`. The retained baseline artifacts were reused only after SHA-256 verification and imported-runtime-source equality; this is disclosed in `baseline-reuse.json`, not described as a fresh reference execution.

Fresh final candidate: **237 segments / 14 routes / 685,504 consumer callbacks**. One old 12-segment route has missing active-prefix atomic inputs and remains diagnostic-only; the other 225 segments have complete active atomic inputs. Candidate and reference both close the software producer/consumer feedback loop. Vehicle, ECU, lead and driver response remain frozen; exact hidden consumer receive-drain order is not logged. Prior recorded-feedback reproduction of the newest route matched all 107,945 producer steps, while coupled reconstruction itself is not asserted to exactly reproduce every installed feedback sample.

| Gate, final candidate versus current-source reference | Result |
|---|---:|
| Added or changed fault history | 0 |
| Lost or gained active callbacks | 0 / 0 |
| Different raw requests / I / gas at consumer callbacks | 0 / 0 / 0 |
| Weaker raw / encoded strong-target requests | 0 / 0 |
| Extra full-brake callbacks or full-brake exposure | 0 |
| Full-brake changes | 1,936 → 1,936 |
| Full-brake exposure | 3,144.149 → 3,144.149 s |
| Combined brake/precharge exposure | 3,232.285 → 3,219.652 s |
| Disabled-owner wire changes | 0 |
| New gas-under-brake/precharge or retained-torque conflicts | 0 |

Every recomputed producer step was audited independently: **1,311,408 steps**, with zero raw, I, freeze-decision, PID-phase or rolling-demand-reduction differences. The two older reference release-timeout histories remain identical; this is not a claim that all historical mismatch causes are eliminated. The latest drive has no candidate timeout, unlike the rejected pulse prototype.

All **627 changed ACC packets only clear the precharge-request bit 1→0**; every other bit is preserved. An independent packer-generated mask verifies the changed field. There is no weaker encoded braking or added propulsion hidden in the packet change.

[Full comparison](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Every-producer audit](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Changed-packet audit](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Named regressions and remaining pulsing

The protected city fixture retains 17 brake-bit changes and the existing release behavior. The newest approximately 59 / 68 / 59 mph windows retain **17 / 14 / 12** full-brake changes and identical propulsion. The high-RPM restart window retains raw demand, I, gas and brake timing. No zero-change window is credited after lost activity: active rows are identical throughout.

This repair therefore removes the *prototype-induced* regressions and substitutes short true-coast intervals for some weak precharge requests. **Gas-withdrawal cycling and full-brake switching in the main highway windows remain unchanged.** The reduced precharge request may change physical response, but the replay cannot prove comfort, hydraulic pressure, fuel, RPM or stopping-distance improvement. Do not advertise this as a solved highway-pulsing tune.

## Tests and independent review

The initial protocol-role tests failed on the installed behavior; the clearance-ownership tests failed on the first repair. Final tests: **32 pass**, covering versioned cereal/JSON round trip, unsupported peer fallback, ordinary ramp preservation, signed coast, debt, strong takeover, deadlines, stale/reversed torque, owner/clock changes, no pending-wait forgiveness and three distinct post-coast clear readings. A transport fixture initially omitted the producer timestamp; the failure is retained and the fixture corrected without changing runtime code.

Independent read-only review found no blocker in the final local clearance path. It noted the disabled-helper fabricated-context case is unreachable through the wrapper scope and that production negotiation is not implemented. The final full replay is the behavioral regression evidence; unit tests and review alone are insufficient.

## Native saved-traffic replay

Fresh native debug-hook replay completes **237 segments / 14 routes / 685,398 replacement ACC slots** with original received CAN, original non-ACC transmissions and timers retained. It adds **zero TX rejections and zero relay faults**, with no forced controls permission. This is unsanitized local native replay; no UBSan, ARM, hardware or road proof is claimed.

[Native summary](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Native source/header/binary provenance](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Workspace preservation

The paired sources remain clean and unchanged. No SSH or device interaction occurred. Local workspace pressure was handled only on task-generated caches: byte-identical archived pickle outputs were hard-linked, their paths/hashes preserved and made read-only; an unused decoded cache was compressed with exact decompression SHA verification. All original drive logs and their durable private archive remain untouched. `restore_cache.py` restores the exact decoded cache if an older analysis needs it; archived replay reproduction should use a fresh output directory.

Remaining work before any production integration: implement the revision-3 transport deliberately on both sides, retain mixed-peer fallback and clearance tests, and validate actual changed precharge/coast response. Do not change timeout policy, enlarge allowance or erase I to claim smoothing.
