<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Highway coast/brake prototype — October 26 CDT / October 27 UTC, 2026

**Investigation and the full controller replay are complete. Neither local prototype is ready for integration.** The latest explicit-coast version removes the first version's added timeouts, but its small reduction in switching comes with longer braking exposure and weaker later strong-braking requests. Paired branches and the Comma remain unchanged.

## Reproduction and cause

The installed pair (`1dbbc0189` / `beb10c25`) reproduces all 54,969 recorded software-feedback callbacks on the new moving drive. Recomputed producer acceleration matches every recorded sample within 1e-5 m/s² (maximum approximately 1.19e-7). This establishes the new-window baseline before changing the allocator.

The trace records actual consumer-refreshed pitch, mapped gravity, planner target, integral, net decision demand and mode. It does not estimate consumer pitch from producer orientation.

1. Small net-demand crossings repeatedly enter braking. For example, near 74 mph, raw positive demand 0.130 plus mapped gravity -0.168 gives net -0.038 m/s² and enters braking. A later raw 0.197 / net +0.075 qualifies release. The original planner target stays positive throughout that 15-second window.
2. The precharge allocator is already `budget_reference` in these windows. Its decision deadline has expired; it is not rearming between brief crossings. That prevents its short precharge trial from smoothing subsequent entries. A locked allocator is evidence of a spent decision allowance, not permission to reset it on every crossing.
3. Brake release withdraws propulsion until received pressure/torque clears, then restarts the engine-request ramp. This changes when anti-windup freezes the integral. A local admission change therefore changes later raw demand even after that admission episode ends.

The replay proves this software chain on frozen recorded inputs. It does **not** prove that pitch variation is surveyed road grade, that it is the sole physical cause, or how torque would respond to different commands.

[First transitions with actual consumer inputs](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Local prototypes

Both variants retain the planner, acceleration/brake packet encoding, strong-demand fallback, measured clearance and timeout rules. They extend weak-entry qualification from net greater than -0.05 to greater than -0.14 m/s² only when a fresh valid planner target is nonnegative, raw demand exceeds +0.02, speed is at least 3 m/s, the driving/pose/CAN context is valid, and fresh received brake torque is at most 4 Nm. Existing entry-area 0.01 m/s and 0.3-second deadline remain. These are decision-demand bounds, not proven physical speed-loss bounds or a global per-route budget.

- **Variant 1: defer weak entry while retaining existing propulsion behavior.** In the new 62–64 mph window, changes fall 12→8. Full replay adds release timeouts at 40.85 and 56.18 mph and weaker subsequent braking. Rejected.
- **Variant 2: explicit coast during the newly expanded weak-entry interval.** Withdraws propulsion and reports the actual software limitation, so positive integral growth can freeze. No fabricated brake bits, torque, unlimited authority or baseline-output oracle. This clears both newly added timeouts, but still changes later integral history and fails braking-performance regressions. Rejected.

These are separate research files loaded into the unchanged installed controller classes for offline replay. They are not commits in the paired branches.

## Full controller replay

All **216 segments /13 routes /625,238 callbacks** processed for installed reference and both candidates: the previous complete 197-segment corpus plus the latest 19-segment drive. One older 12-segment route has five missing active prefix inputs and is diagnostic-only. The remaining 204 segments have complete active atomic input coverage. Input hashes and source bindings were verified.

Variant 2, using only complete-active-input routes:

| Check | Result |
|---|---:|
| Added fault sequences | 0 |
| Lost/gained active callbacks | 0 /0 |
| Gas while commanding brake/precharge | 0 |
| Moving gas with retained received brake torque | 0 |
| Disabled-owner wire changes | 0 |
| Brake-request changes | 1,655→1,649 |
| Brake-command exposure | 2,783.745→2,834.924 seconds (**+51.179**) |
| Weaker raw strong-target requests | **2,586** |
| Weaker encoded strong-target requests | **2,071 /35,375 checked** |
| Maximum weaker encoded demand | **0.039 m/s²** |

The two preexisting reference release timeouts remain at the same timestamps; one belongs to the diagnostic-only route. Zero added timeouts is not a claim that all controls-mismatch causes are resolved. Changes in command counts/exposure are not a comfort or collision-risk score.

### Named regressions, variant 2

| Fixture | Brake changes, reference→candidate | Brake exposure, seconds |
|---|---:|---:|
| New 58–62 mph /15 seconds | 14→14 | 7.703→7.741 |
| New 62–64 mph /15 seconds | 12→10 | 4.500→5.922 |
| New ~74 mph /15 seconds | 10→10 | 3.564→3.466 |
| Earlier 63 mph /15 seconds | 20→20 | 9.914→9.587 |
| Earlier city ~25 mph | 17→17 | 21.533→21.347 |
| Earlier highway response window 1 | 22→21 | 14.325→14.577 |
| Earlier highway response window 2 | 12→12 | 12.340→12.203 |

The two high-RPM rolling windows and normal stopped-launch window retain their brake-change counts/exposure. Actual RPM, shifting and vehicle response remain frozen: no RPM or restart improvement is established by this prototype.

[Full comparison](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Rejected first variant](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Verified controller summary](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Remaining blocker: integral/authority continuity

The explicit coast state initially leaves I lower than reference. It can still become higher later when the engine ramp reaches the slightly lower candidate request sooner. In the first retained regression, candidate I starts about 0.000797 below reference. A producer update then unfreezes candidate growth while the reference remains frozen, even though both report `limited=true`. The existing numerical-authority margin is 0.011 m/s²; the two requests cross that margin at different times. Candidate I overtakes reference by approximately 0.000382. Other routes develop larger differences, including later weaker strong-braking requests.

This is not an omitted release-timeout exception. It is a feedback/state-history interaction. A brief coast-entry delay alone cannot promise subsequent command recovery. The replay explicitly rejects the resulting variations rather than resetting I, copying reference I, inventing a repayment oracle or weakening clearance rules.

[First exact producer crossover](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Per-route first crossover and braking regression](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [First variant's added timeouts](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Next design boundary

The next candidate needs a single owner-consistent coast/precharge/brake allocation state and an explicit definition of delivered propulsion authority for integral recovery. Independently adding an admission delay ahead of the already locked precharge allocator leaves two budgets and ambiguous recovery timing. Keep the first producer crossover above as a failing regression, along with the city, rolling, strong-braking and timeout fixtures. Do not simply enlarge the coast band, forgive a spent allowance at every crossing, suppress the timeout or claim a vehicle response improvement from this replay.

No device changes, SSH, installation, branch integration, push, reboot, CAN transmission or OS/firmware action occurred. Steering code and owner 1.20/0.97 remain unchanged. The native safety replay and final verification receipts are recorded separately below.

## Native safety and verification

Fresh native replay of variant 2 completed **216 segments /13 routes**, replacing **625,140 ACC send slots** while retaining original received CAN, non-ACC sends and timers. It added **zero transmit rejections and zero relay faults**, with no forced permission. The existing rejection counts remain equal between reference and candidate. Header/binary hashes and paired source status were verified.

**13 focused prototype tests and 202 installed longitudinal contract tests (plus 20 subtests) passed.** The normal sanitizer-backed native test initially failed to load its UBSan dynamic library because of macOS platform policy. The same contract suite was repeated successfully with an explicitly compiled unsanitized native library; the full native replay also uses unsanitized debug hooks. No sanitizer, ARM build, hardware or physical-response proof is claimed.

This native protocol pass does not override the failed braking-performance gates. Final decision: **retain as a rejected local research prototype; do not integrate or install.**

[Final verification](PUBLIC_VERIFICATION.json) · [Native replay](../../navigator-reference/PRIVATE_ARTIFACTS.md) · [Native source provenance](../../navigator-reference/PRIVATE_ARTIFACTS.md)
