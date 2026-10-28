<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Wheel/body disagreement and slow-unwind blockers: local resolution

The two local admission/release blockers have a corrected prototype in [highspeed.py](../../../navigator-reference/PRIVATE_ARTIFACTS.md), with a real-event adapter in [motion_context.py](../../../navigator-reference/PRIVATE_ARTIFACTS.md). The prior experiment is preserved in `../navigator-highspeed-correction-prototype-2026-10-17`. Installed paired source and Comma are unchanged. No device connection, ECU query, CAN transmission, firmware operation or publication was used.

## Findings

**Wheel angle excess is insufficient by itself.** The old candidate reduced commands on 14 individual samples whose measured body response was below 90% of instantaneous request. [Original-source diagnosis](../../../navigator-reference/PRIVATE_ARTIFACTS.md) still finds 14 below 90% using source timestamps directly; matching demand to the motion sample time retains 11. Thus double past alignment contributed but does not explain the full discrepancy.

[Wheel/model/body audit](../../../navigator-reference/PRIVATE_ARTIFACTS.md) finds all 14 measurements reach at least 90% of the frozen sample's target within 300 ms. The median absolute wheel/body gap is about 0.63 of the reported yaw std. This supports a transient/measurement/model ambiguity and does not establish a fixed yaw offset or a replacement steering gain. Future samples in this audit are **diagnostic only**; the controller consumes only messages already received. No constant yaw correction, steer-ratio recalibration, mass/wheelbase change or owner-gain change was made.

**The old unwind window forgot its peak.** A 1% per 50 ms decline never retreated 10% within its sliding six-frame window, so the correction could remain eligible throughout a much larger cumulative withdrawal. Fixed-peak latching addresses this; simply freezing the peak of all pre-entry demand was too restrictive and could disable a subsequent rising bend. The final peak is established after actual correction admission, uses a causal 3-sample median, and permits tightly confirmed new rising demand to rearm.

## Corrections

- Require fresh calibrated body yaw to confirm **both current and sustained** excess, in addition to the existing wheel-angle excess and coherent atomic calibration. Source, received and consumed timestamps remain distinct. At least 3 unique samples spanning 80 ms are needed; body age ≤ 100 ms, history ≤ 300 ms. Valid motion/envelope/calibration flags and finite bounded std are required. The 0.1 m/s²/10% excess margins and 0.03 rad/s std sanity ceiling are engineering guards, not confidence claims.
- Invalid calibration immediately invalidates cached yaw. Restoring valid calibration cannot revive an old transformed sample; a fresh motion sample and history generation are required. Source/arrival ordering and duplicate/out-of-order data are checked.
- Retain the admitted bend's peak. More than 10% retreat of causal median demand latches correction off; more than 20% raw retreat aborts immediately. For monotonic decline, median detection can lag by one 50 ms frame, rather than forgetting cumulative withdrawal indefinitely.
- A lower plateau cannot rearm. Valid neutral/speed/direction/disengagement evidence can start a new episode; alternatively, 5 consecutive wheel/body-confirmed requests above 102% of the frozen peak establish new rising demand. Normal onset persistence restarts and final output must join reference before rearming. Invalid reset-triggering samples cannot clear the latch.
- Preserve owner **1.20/0.97**, fixed pinion model, reference low-speed/roll-aware behavior, default-off identity, 15%/0.01 rad reduction caps and native final slew/range. Missing or uncertain evidence falls back to the installed strategy. This remains a reduction-only high-speed gentle-curve experiment.

## Retained counterexamples and reported bend

[Independent guard audit](../../../navigator-reference/PRIVATE_ARTIFACTS.md), [scene results](../../../navigator-reference/PRIVATE_ARTIFACTS.md), [body cross-check](../../../navigator-reference/PRIVATE_ARTIFACTS.md):

- **All 14 original disagreement samples now have zero final added correction.** There are zero new normalized body-under 90% samples among changed qualifying frames in the latest retained route. Direct arithmetic on the already-arrived calibrated yaw likewise finds zero changed active frames with negative current body excess.
- The reported 83 mph bend 1011–1017.5 s still triggers: **31 of 130 frames change**, versus 117 in the wheel-only prototype. Among changed frames, command reduction p10/p50/p90 is **1.40%/4.36%/12.51%**. Across all 130 frames it is **0%/0%/5.88%**; maximum residual 0.0063 rad. Do not present the changed-frame median as an improvement over the whole bend.
- Across the route there are 139 changed active strategy frames;125 of 3,343 qualifying gentle-curve frames change. Reference reconstruction retains 100% half-wire-step fidelity across 17,439 activeframes. All 1,567 active 40–50 mph scene frames remain unchanged.

This is deliberately narrower mitigation: it gives up intervention coverage when body confirmation or unwind state is uncertain. It does **not** prove that the reported lane incursion is fixed or that reducing a command byX% improves tracking byX%. The saved vehicle response is never rescaled or replaced.

## Tests, review and full replay

[Focused test log](../../../navigator-reference/PRIVATE_ARTIFACTS.md): **82 passed**, including mirrored bends, 12,000 transition/abort sweep frames, the original slow 1%/frame decline and 0.2%/0.5% declines, lower-plateau and above-peak rearm, one-frame jitter, invalid reset evidence, real calibration/motion events, cached invalidation/recovery, future/duplicate/out-of-order motion, unique-history span and driver/fault/stale-data releases. The original and review regressions were observed failing before their fixes. [Review record](REVIEW.md) documents both findings and their resolution; final source review found no remaining concrete blocker.

**Full source-verified replay completed: 28 sessions / 540 segments.** [Final verification](../../../navigator-reference/PRIVATE_ARTIFACTS.md), [route results](../../../navigator-reference/PRIVATE_ARTIFACTS.md), [source snapshot](../../../navigator-reference/PRIVATE_ARTIFACTS.md), [exact recorded native check](../../../navigator-reference/PRIVATE_ARTIFACTS.md), [four-instance independence proof](../../../navigator-reference/PRIVATE_ARTIFACTS.md).

- 124,787,149 physical recorded RX frames and 3,134,371 controller updates. Every input segment matches its retained SHA256 manifest. Every worker finishes with identical unchanged source hashes and paired HEADs.
- Original atomic-packet reference/candidate and separately labelled past-only synthetic calibration reference/candidate each generate 2,014,555 TX frames: **2,004,203 configured frames accepted, zero rejected**, plus 10,352 pre-Ford unhooked frames. All relevant physical RX checks pass. 28 startup invalid-safety ticks per variant are retained explicitly; no permission override was used.
- Default-off is byte-identical across the entire corpus. **All generated updates below 60 mph and 40–50 mph are identical** to installed reference in both input variants. No owner factor or baseline branch source changed.
- Older 27 routes remain unchanged with original packets lacking usable atomic calibration. Causal-fixture candidates change 493 updates; original-packet candidates change 121 updates, all on the latest route. These are generated-controller event-time comparisons, distinct from actual-send-time scene counts.
- 1,253,772 angle-frame rows across the two input variants pass the final bounded-reduction envelope checks, accounting for wire quantization; zero empty slew/envelope intersections.
- Exact original timing native replay covers 5,881,370 physical RX and 99,445 configured original TX per variant, with 490 pre-Ford TX unhooked. Candidate changes **110 encoded steering packets**, including **28 in the 83 mph bend** (31 unquantized strategy changes include sub-wire-step changes). No additional rejection. Both variants reproduce the same **seven existing rejects: six cancel 0x83 and one steering 0x3d6 at 1397.208088 s after braking with controls not allowed**. They are separate from this guard fix and have not been erased by the generated-controller zero-reject result.

[Slow-unwind traces](../../../navigator-reference/PRIVATE_ARTIFACTS.md) additionally show first latch at frame 54/2.70 s for 0.2% per frame decline, frame 23/1.15 s for 0.5%, and frame 12/0.60 s for 1%. This is cumulative 10% withdrawal plus the explicit causal median lag; the previous rolling gate could continue while these declines accumulated. Lower plateaus cannot restart correction. These are deterministic guard inputs, not predicted vehicle dynamics.

## Scope after local acceptance

The local wheel-only admission and forgetting-peak defects are addressed without changing sensor calibration or the live device. Physical tracking and latent true yaw remain unvalidated. The seven historical recorded native permission/cancel rejections are separate existing behavior. Production branch integration/build and hardware/closed-loop acceptance are separate from this research package; no install or road-readiness claim is made.

No special 85 mph reproduction drive is needed for the next local stage. Continue ordinary supervised evidence collection only under the existing plan if desired; this package has not been activated. The 24–30 mph entry delay and previous low-speed evidence tasks remain independent.

## Reproduce

Use `${USER_HOME}/Apps/openpilot/.navigator-master-integration-20261014/.venv/bin/python` in this directory:

1. `python -m pytest -c /dev/null -p no:cacheprovider -q test_highspeed.py test_motion_context.py`
2. `python scene_replay.py`, then `python body_crosscheck.py` and `python gate_audit.py`.
3. `python parallel_replay.py` and `python replay_recorded_native.py`.
4. `python summarize.py`.

Raw recordings stay in private backups; no location data is included. Native checks use the existing unmodified Mac debug library, independent hook state and original physical RX. No controls-permission override. They do not reproduce H7/USB/forwarding/physical timing or establish sanitizer/vehicle acceptance.
