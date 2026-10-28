<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Downhill-compensation and BluePilot allocation: separate local comparisons

October 25, 2026. **Neither standalone variant is ready for integration or installation.** The experiments change brake decisions substantially, but do not establish reduced physical pulsing. Comma, paired source and 1.20/0.97 remain unchanged.

## Source and variants

Current BluePilot source was verified through BrowserOS neo at repository head `54acf36b6c8dabf1693f4002e1e88b41c928eb79`. Its Ford controller and longitudinal extension exactly match the cached upstream files examined earlier; the README is not evidence of a newly added fix. Hashes and pinned URLs are in `fork-provenance.json`; retained source is in `sources/`.

| Variant | Isolated change | Retained behavior |
|---|---|---|
| A: downhill compensation off | Clamp negative **effective** pitch contribution to zero before brake/precharge decision | Current grade mapping and validity checks, planner, integral, measured torque-clearance observer and gas ramp |
| B: extracted BP allocation | Brake engages below -0.14 and releases above -0.06 m/s²; independent precharge engages below -0.12 and releases above -0.06 | Current pitch mapping, planner, integral, actual-brake/propulsion exclusion and received-torque clearance |
| Additional conservative B ablation | Same allocation, with propulsion withdrawn during precharge-only | Same guards; truthful limited-authority feedback |

B uses persistent independent hysteresis. This is an **adapted component experiment**, not an exact complete BluePilot port: BP's follow-path local brake/precharge flags are reinitialized each update, while its ordinary brake flag is persistent. BP's lead gas caps, braking rate limiter, speed/lead eligibility gates and no-lead zero-braking-target branch are deliberately excluded to isolate allocation. B is applied without those gates; its low-speed results must not be presented as complete BluePilot behavior. Precharge-only in primary B can retain valid propulsion only when the existing received-torque observer permits it, like the relevant BP distinction. The conservative ablation is reported separately.

No observer reset, timeout extension, fake torque, forced permission or recorded-integral oracle is introduced. The precharge bit becomes independently encodable only in the private in-memory Ford CAN module; the paired module is unchanged.

## OEM reference

Reused the original verified OEM command/RX caches from the prior 96-segment OEM/Alpha dataset. OEM-owned recordings are an observational reference, not replayed as if they were Alpha engagements.

Across eligible OEM samples:

- 1,609 precharge-only samples / 32.194 seconds;
- 1,605 have a valid propulsion request, including 123 positive requests;
- 965 also report brake torque above 4 Nm;
- all 8,667 actual-braking samples have propulsion inactive.

This confirms that precharge and actual braking are distinct factory request states. It does not prove that permitting propulsion during precharge is appropriate under the Navigator's current observer contract, nor that these reported torque estimates are direct hydraulic measurements. Native safety acceptance also does not settle this physical coordination question.

## Fixed-request decision comparison

To isolate the decision change from integral drift and disengagement, `decision_only.py` applies each raw threshold policy to the same original baseline brake-acceleration request and effective pitch. Moving healthy PID samples only; all other existing guards are excluded from this **diagnostic** comparison.

| Raw threshold policy | Brake-on time | Transitions within five-mph bands |
|---|---:|---:|
| Original 0.0 / +0.3 thresholds | 2,186.611 s | 298 |
| Downhill off | 1,398.343 s | 288 |
| BP-derived allocation | 651.865 s | 340 |

A reduces raw threshold brake-on time by about 36%; B by about 70%, while B increases raw threshold transitions by about 14%. These are neither actual installed brake times nor ride-comfort improvements. In particular, do not compare these transition counts directly with the earlier coupled-controller count of 992: the latter includes current admission/release/feedback behavior. Fewer brake requests can also mean delayed necessary braking or increased precharge effort.

## Full causal controller comparison

Each primary variant ran all **137 cached Alpha segments / 401,970 consumer callbacks** through actual LongControl and CarController with persistent integral state and causal returned candidate feedback. Original consumed planner/state, driver actions and received torque remain frozen. A conservative allocation ablation also ran the full corpus.

| Result | Baseline | A: downhill off | B: adapted allocation |
|---|---:|---:|---:|
| Fault episodes in recent 76 segments | 0 | 10 | 9 |
| Fault episodes across all 137 segments | 2 | 17 | 20 |
| Lost healthy active time versus baseline | — | 2,949.564 s | 2,592.969 s |
| Moving positive-propulsion samples with received torque above 4 Nm | — | 0 | 0 |

Both variants encounter release timeouts and then lose substantial engagement. Therefore their smaller brake counts in the coupled comparison **must not be credited as smoother driving**. Per-band common-active statistics, lost exposure, precharge exposure and strong-demand command differences are retained in the comparison/availability JSON files.

Primary B has about 27.46 seconds of active precharge-only commands, including about 16.27 seconds with valid propulsion. The conservative ablation has no valid precharge-only propulsion but still loses about 2,579.69 seconds of healthy active exposure. Simply withdrawing gas during precharge does not solve integration.

### Why the timeouts need careful interpretation

The recorded ECU response belongs to the old commands. After an experiment withdraws its brake bit, the recording may still show torque from braking that the original controller continued requesting. The unchanged observer correctly refuses propulsion and eventually faults; the resulting loss of engagement then changes integral history and invalidates any naive comfort score.

First examples:

- A: route 01 relative 131.848 s / 59.31 mph, candidate brake off but baseline brake on, received torque 60 Nm;
- B: route 01 relative 174.511 s / 60.67 mph, candidate brake off but baseline brake on, received torque 52 Nm.

At newly faulted episode onsets, the baseline is still commanding actual braking in 12 of 16 A contexts and 13 of 19 B contexts. Other cases also involve changed timing/history; they are not automatically proved physical stalls. See `fault-contexts.json`.

**These replays do not prove BluePilot or downhill-off would produce those exact real-world timeouts.** They show the drop-in changes cannot pass the current software/recorded-response validation, and frozen torque cannot certify the counterfactual ECU release. This limitation must not be hidden by resetting clearance, changing recorded torque or allowing propulsion on a forecast.

## Existing contracts and focused checks

- Unmodified baseline: **157 tests and 20 subtests pass**.
- Each primary variant: **8 focused tests pass**, covering independent precharge encoding, retained actual-brake gas exclusion, received-torque clearance and stalled/progressing timeout behavior.
- A retained suite: 151 tests pass, **6 tests fail**; 12 subtests pass and **8 grade subcases fail**.
- B retained suite: 152 tests pass, **5 tests fail**; 16 subtests pass and **4 grade subcases fail**.

The failing assertions cover sustained grade-adjusted mild brake demand, bounded alternating negative exposure, delivery-interval fallback, and negative-net grade behavior, including low-speed cases. They express the existing policy assumption that sustained negative grade-adjusted demand must reach actual braking. A changes that input; B can keep the proposed brake false below its new threshold, so the existing admission budget never gets a brake entry to qualify. These are deliberate behavior conflicts, not Python crashes, and not by themselves proof the old policy is physically correct. They require an explicit revised braking/actual-speed-tracking contract backed by response evidence; the assertions were not silently rewritten to obtain a pass.

The experiments retain strong planner requests rather than BP's no-lead zero-braking branch, but changed feedback still shifts later integral state. Full comparison receipts retain those differences and cannot be replaced by a command-edge count.

## Native replay

Both primary variants each ran fresh plain-debug native safety hooks over all 137 segments: **32,171,016 RX / 951,332 TX per recorded/baseline/candidate variant**, zero added candidate rejection, no relay malfunction, no forced controls permission. Original non-ACC traffic and timer progression are retained. Existing original/baseline rejections remain visible. This is not zero total rejection, sanitizer, ARM, hardware, vehicle release or road-comfort proof.

Native acceptance and focused checks do not override retained contract failures, lost engagement or the physical-response limitation.

## PR #38367

[longitudinal: move cruise speed limit out of the MPC](https://github.com/commaai/openpilot/pull/38367) was merged July 22, 2026, at `736f3b1a00c23d286465eb14976c25068c82d025`. A live GitHub metadata/diff read and local `git merge-base --is-ancestor` confirm it is **already in the paired parent branch** `ead00c30e`.

The PR removed the artificial cruise-speed obstacle from the lead MPC, added a separate cruise acceleration candidate and selected among cruise/lead/model candidates. It modified planner and maneuver tests, not Ford actuator encoding or brake-release coordination. Later upstream changes are present in the current source, so the old PR should not be reapplied verbatim.

Current planner code independently computes cruise acceleration, gets lead-MPC and model acceleration candidates, applies the existing model acceleration boost, then selects the least acceleration candidate. Set cruise speed therefore competes with lead/model demands; it does not force the car to reach that speed. This architecture is relevant to investigating the earlier set-75/drive-62 report, but it does not establish that exact episode's cause or that the PR follows posted road limits. A diagnosis needs the selected source/candidate values at the episode. PR #38367 supplies no missing Ford coasting fix to cherry-pick.

## Decision and next design gate

Keep both comparisons local. Do not install either standalone change. The useful findings are that negative pitch can materially influence brake entry, independent precharge is factory-observed, and simply transplanting the thresholds bypasses assumptions in the current bounded admission/release path.

The next local design should put the allocator and the sustained-demand/actual-speed-error budget under one explicit contract, retaining truthful brake/precharge authority feedback and measured clearance. Reconcile the intentional grade-policy test changes using the supported ECU response semantics, then evaluate later integral recovery/lead braking as well as the immediate coast event. A validated dynamic response or later separately planned physical test is needed to establish counterfactual release/comfort; ordinary frozen-torque replay alone cannot do that. No device activation or new drive was requested by this comparison.

Evidence: `RESULT.json`, `availability.json`, `decision-only-summary.json`, `fault-contexts.json`, `oem-reference.json`, `pr38367.json`, native receipts and test logs. Exact paired/source preservation is recorded in `preservation.json`.
