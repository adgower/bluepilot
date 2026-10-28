<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# High-speed gentle-bend correction: local prototype

Local experimental implementation: [highspeed.py](../../navigator-reference/PRIVATE_ARTIFACTS.md), [design](DESIGN.md), [independent review](REVIEW.md). The installed paired branches and Comma are unchanged. No network/device access, firmware operation, active ECU queries or CAN transmission were used.

## What changed locally

Added a composition wrapper around the exact installed roll-aware strategy. Only coherent, fresh, sustained high-speed wheel-angle excess in a gentle curve can request a reduction. Speed weighting starts at 60 mph and reaches full weight at 70 mph; gentle-turn demand uses lateral acceleration, avoiding the old curvature floor that missed the reported bend. Reduction is limited to 15% of installed command magnitude and 0.01 rad, with slow onset and unchanged native final slew/range constraints. It never amplifies or reverses the installed command. The original shadow curvature remains intent, not a claim that the reduced output equals requested motion.

The owner's **1.20/0.97**, fixed pinion model, existing low-speed steering and reference roll mapping remain unchanged. Disabled behavior is exact reference behavior. No production factory, parameter registry, UI or paired branch is modified. A future integration would need the explicit event-validity contract and normal build/hardware validation; this local wrapper is not an installable release.

## Recorded 83 mph bend and gentle curves

[Scene results](../../navigator-reference/PRIVATE_ARTIFACTS.md) compare commands at actual recorded steering-send timestamps using original atomic calibration packets. No target, state, measured yaw or body response is synthesized for this scene pass. The predeclared reported bend is elapsed **1011–1017.5 seconds**, no signal/lane change/driver input during the selected interval.

- Reference strategy matches **all 17,439 active/no-driver recorded frames within half wire step** (0.00025 rad); selected bend also passes that fidelity check.
- Candidate changes **117 of 130 frames** in the reported bend; command reduction fraction p10/p50/p90 is approximately **0.65% / 15% / 15%**. Maximum final residual magnitude is **0.006751 rad**. These percentages describe command change, not improvement in tracking.
- **1,567 active frames at 40–50 mph are unchanged** in this send-time scene comparison.
- Across the latest route's eligible high-speed gentle-curve screen there are **3,343 active frames**, **989 changed**. The screen uses requested acceleration >=0.25 m/s² and abs curvature <=0.001/m, not a high-curvature cutoff.

[Body cross-check](../../navigator-reference/PRIVATE_ARTIFACTS.md) retains the measured calibrated body response. Among fresh eligible changed samples, median body/request ratios by band are approximately **1.180 at60–65**, **1.172 at65–70**, **1.366 at70–75**, **1.369 at80–85**. There are no changed qualifying75–80 samples in this route, so that range has no direct scene efficacy evidence.

There are **14 individual changed samples with measured body response below90% of demand** despite wheel excess (11 at60–65,2 at65–70,1 at80–85). Their command reductions range from nearly zero to4.54%; they are short transient/model-alignment counterexamples, not evidence to discard. The wheel-only guard is therefore not a perfect classifier of body over-response. More held-out/transient validation is needed before promoting this experiment.

The earlier observed ~134% body response in the reported bend remains unchanged in the recording. No replay method here can prove that a15% command reduction would yield15% less vehicle response, correct lane position, or prevent a departure. No new high-speed reproduction drive is needed for the next local review.

## Focused tests and review

`green.txt` records **39 passing tests** with no warnings. Coverage includes mirrored turns, no excess/undershoot, default-off parity,15–59.9mph parity, invalid/stale/future/mismatched context, faults, lane change, driver takeover, invalid state envelopes after activation, reversal, meaningful withdrawal, residual join/re-arm, small jitter and slow unwind. Three deterministic transition/abort sweeps cover12,000frames. Owner factors and fixed pinion VM are explicitly checked.

Important qualification: withdrawal means >10% retreat within six frames. A slower continuous unwind can remain eligible while wheel excess persists. The report does not claim universal unwind suppression. All such trial output remains reduction-only and bounded; characterizing this is separate from proving better physical turn release.

Independent review found and resolved dropped state-envelope validity and source-provenance weaknesses before the accepted full replay. Early pilot runs were exploratory and were superseded by the restarted, source-verified run.

## Full replay

**Completed:28 sessions /540 segments**, with the same unchanged source snapshot in every worker. [Final gate results](../../navigator-reference/PRIVATE_ARTIFACTS.md), [full route results](../../navigator-reference/PRIVATE_ARTIFACTS.md), [source hashes](../../navigator-reference/PRIVATE_ARTIFACTS.md).

- **124,787,149 recorded physical RX frames** and **3,134,371 controller updates** replayed. Every input segment is checked against its existing SHA256 manifest.
- Four independent native-hook/generated-controller variants: original atomic-packet reference/candidate, and past-only synthetic-calibration reference/candidate. Each generates2,014,555TXframes; **2,004,203 post-Ford frames accepted, zero rejected**, plus10,352pre-Ford frames explicitly unhooked. All recognized physical RX checks pass. Each variant has28startup safety-config-invalid ticks, one perroute; these are reported rather than hidden.
- **Default-off is byte-identical to installed strategy throughout. All generated updates below60mph, including40–50mph, are identical**, for both actual packets and synthetic fixtures.
- Older27routes have no usable atomic packet for this trial and remain byte-identical in the original-packet pass. Synthetic causal snapshots exercise those saved trajectories separately:6,557changed candidate updates across the full corpus, versus856changed updates on original packets (all in latest route). Neither is historical proof that the old producer emitted the packet.
- **1,253,772 angle-frame rows** across both input variants pass final reduction-envelope checks, with wire quantization accounted for. No infeasible final-slew/envelope intersection occurs. Exact floating bounds/reversal/abort behavior are independently covered by the focused tests.

### Exact recorded timing and seven shared historical rejections

[Recorded native replay](../../navigator-reference/PRIVATE_ARTIFACTS.md) additionally feeds every original physical RX and original TX at its recorded timestamp through two independent native-hook instances. The candidate changes only selected0x3d6path-angle bits and recalculates the Ford checksum; stock fields, counter, mode, shadow intent and all other messages are retained. **839 encoded steering packets change, including all117selected bend packets**; this differs from unquantized strategy-change counts because many small adjustments round to the same wire value.

Both variants process5,881,370physical RX and99,445configured TX, with490pre-Ford frames unhooked. **Zero candidate-specific native rejects.** Both reproduce the same **seven historical native rejections: six cancel0x83messages plus one active0x3d6steering message at1397.208088s after braking, controls not allowed**. They are not repaired by this high-speed experiment. The generated-controller replay's zero rejects must not be confused with a claim that the original recorded stream has none.

## Disposition and remaining work

Local prototype and full offline acceptance checks are complete. This is **not a validated tracking fix or an installable paired release**. Preserve the current device install. Before any integration proposal, investigate the14body-under-response transient samples and slow-unwind behavior, check held-out performance/corrected-command release timing, and define producer/state-validity handling for the new feedback wrapper. Production build, physical hardware validation and closed-loop performance remain separate.24–30mph entry delay and the original lower-speed evidence gaps remain open; this experiment does not address them.

## Reproduce locally

Use `${USER_HOME}/Apps/openpilot/.navigator-master-integration-20261014/.venv/bin/python` from this directory. Tests: `python -m pytest -c /dev/null -p no:cacheprovider -q test_highspeed.py`. Recorded-send comparison: `python scene_replay.py`; retained corpus/native replay: `python parallel_replay.py`; body audit: `python body_crosscheck.py`; final gates: `python summarize.py`. Input recordings remain in private backups; no GPS or routes are embedded in this report.

The native library is an existing Mac debug build, not a sanitizer or H7/USB/vehicle validation. Original legacy packets and separately labelled past-only synthetic calibration fixtures are distinct evidence. No safety limit or control-permission override is used.
