<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Response-aware coast/brake prototype — October 26, 2026

**Implemented and evaluated a local research allocator, but found no qualifying coast/brake decision to activate. City and highway pulsing remain unresolved.** This is a useful negative experiment, not a controller improvement ready to integrate. The Comma and paired source were left unchanged; 1.20/0.97 remain intact.

## New recordings and symptoms

Read-only SSH acquisition downloaded **two new drives / 21 completed segments / 182,360,561 compressed bytes**, with before/after hashes, source, settings and protected-file checks. Comma Lab started an import but became unavailable; its partial job was not used as authoritative evidence. The SSH download contains all newly identified completed logs relative to prior acquisition receipts, with no open segment deferred. Source remains installed parent `5b301a944` / child `884c9f491`.

The new recordings confirm repeated brake requests at city and highway speeds. In a selected 20-second window, speed is **57.8–60.7 mph**, gear remains 10, software brake requests change **23 times**, received actual brake torque ranges **0–232 Nm**, and planner target acceleration ranges approximately **−0.022 to +0.223 m/s²**. Another 57.1–62.1 mph window has 13 changes and received brake torque 0–300 Nm. These are observed CAN and planner signals, not direct measurements of ride comfort or proof of a specific friction-brake force.

New active driving reaches about 65.3 and 66.3 mph. These trips add no 75–85 mph road evidence. The saved state/event streams contain **no controlsMismatch observation or coordination fault** in either new drive. `health-summary.json` retains this check separately from prototype replay.

## High-RPM event preserved

A matching event occurs about **7 min 42 s into `response-road-session-01`**. Decoded RPM is above 3,200 for 3.73 seconds and peaks at **4,136**, at roughly **16.6–22.7 mph**, while Alpha is active and the driver accelerator pedal is not pressed. Actual gear reports 1; target gear changes from 1 to 2 at about 463.877 seconds, and actual gear reports 2 at 466.144 seconds. This reported transition interval is about 2.27 seconds; it is not proof that the transmission mechanically stayed in first throughout every instant of the shift.

After a slowdown to about 4 mph, the software propulsion request ramps to about 1.8 m/s² while planner demand is around 1.1–1.2 m/s², then tapers. The high-RPM interval itself contains no requested brake/precharge. Precharge and braking appear afterward around 23 mph despite slight positive planner targets, and later another brake entry occurs during the next upshift. Thus this episode includes both acceleration/handoff behavior and subsequent braking, but is not simply repeated brake application during the RPM peak.

**RPM quality is unresolved:** decoded `EngAoutNActl_D_QF` remains 0, labeled Faulty by the current DBC, across OEM and Alpha evidence. The changing RPM and gear signals preserve the owner's matching symptom; they do not certify engine RPM, establish a transmission fault or prove a fix. `high-rpm-timeline.json` preserves the command/gear timeline.

The passive OEM comparison reveals a specific protocol hypothesis:

- Current Alpha sends `AccPrpl_A_Pred = −5` and `AccVeh_V_Trg = 145 km/h` throughout the compared first-gear samples. Local `fordcan.py` and `carcontroller.py` confirm these constant choices.
- OEM ACC varies both fields in its sampled first-gear operation; its target-speed range is 0–55 km/h in the two OEM routes with comparable low-speed samples. OEM peak gas-request magnitude can exceed Alpha's, so these recordings do not support a simple “Alpha's peak throttle is always higher” explanation.

This is an **association and reverse-engineering lead**, not evidence that either field causes late upshifts or highway pulsing. Route, lead, grade, speed and request history differ. Do not change those CAN fields based on this contrast alone. Next local work can compare their OEM timing with actual/target gear and delivered torque, including the new event. No transmission command or ECU query was sent.

## Prototype and response model

Created separate empirical **200 ms response envelopes** for inactive propulsion, valid near-zero engine requests, valid negative-engine requests, and braking. The inactive −5 gas value remains a mode marker; it is never numerically averaged with real engine requests. Positive propulsion and precharge are not relabeled as coast evidence. RPM is excluded as unqualified, rather than accepting its zero flag as valid.

Each response case uses a stable command prefix, matching forward actual/target gear and engaged clutch, fresh received torque/status/state, no driver pedals, valid causal pose context and bounded pitch-proxy variation. Labels are velocity-derived response over that prefix. Candidate inputs are initial observations only. Coast-like cases require received actual/arbitrated brakes and brake/precharge status clear over the prefix. Brake cases retain their initial pressure and lag rather than assuming instantaneous response.

Prediction uses the same mode and gear and nearby speed, raw pitch-gravity proxy, initial acceleration, actual wheel torque and brake torque; valid engine-request levels are matched separately. A query excludes its entire own route. Correlated slices are collapsed by contiguous episode; support requires at least three distinct episodes across at least two other routes. Empirical 1st/99th episode-response percentiles plus a 0.15 m/s² floor are **descriptive envelopes**, not calibrated confidence bounds or validated counterfactual predictions.

Three versions are retained rather than overwriting evidence:

| Version | Response cases | Source scope | Evaluation |
|---|---:|---|---|
| v1 | 874 | Recovered OEM highway routes, newer Alpha and city routes | Route-excluded development scores; actual controller shadow replay |
| v2 | 941 | Adds 16 segments from original OEM city routes | Same fixed screen, no threshold search |
| v3 | 2,036 | Adds 61 older Alpha segments; **147 total source segments / 14 routes** | Same fixed screen; new 21 segments excluded from fitting |

Original archived models and their old split files remain immutable. Previously inspected OEM calibration/test and Alpha calibration/test routes are explicitly repurposed as development data for these new versions, with whole-route exclusion in retrospective scoring. They are not still described as independent test data. The two latest drives are not added to model fitting; they were already inspected for symptoms before their descriptive model scores were computed, so they are not a blind road-validation trial.

The proposed allocator has fresh owner/pose/lead/pressure gates, strong-demand/stop/FCW bypasses, and a finite 200 ms / 0.01 m/s demand-area lease that cannot release an already committed brake. It is a **new experimental lease**, not a silent extension or rearming of the installed precharge budget. It cannot apply without a qualified model. Current envelopes fail the declared screen for route support, coverage and useful width. The actual adapter therefore always runs and returns the original allocation unchanged.

The negative/near-zero engine alternatives are separate diagnostics on unchanged traces. They explicitly set `apply=False`; they are not wired into feedback, integral, gas or brake commands. Both the engine alternatives and inactive-coast selector remain research only.

## City and highway replay findings

The v3 causal entry screen covers the city/highway routes with newly recovered physical context, including the three older Alpha routes. It finds **364 pre-brake entry opportunities**, of which 200 pass the context/pressure/demand guards:

| Alternative | Queries | Observational support | Paired brake support | Qualifying proposals |
|---|---:|---:|---:|---:|
| Inactive propulsion | 200 | 0 | 0 | **0** |
| Valid near-zero engine request | 200 | 46 | 43 | **0** |
| Valid negative engine request | 39 | 9 | 9 | **0** |

These counts are descriptive neighbor matches, not proof of accurate physical predictions. The other three maneuver replay routes still lack the recovered physical-context arrays needed by this screen and are explicitly marked skipped; they are included in the full wire-preservation replay. The installed-source city traces are screened separately, without counting them twice in these totals; they also produce no qualifying proposal. None of the versions' tolerances was adjusted to make a city or highway fixture pass.

Inactive coast evidence remains particularly sparse: v3 has just 28 nonoverlapping 200 ms slices. Near-zero and negative requests add examples, but their uncertainty overlaps braking. New-drive evaluation also fails to establish a precise response model: depending on route/mode, supported-case mean absolute errors are roughly 0.13–0.22 m/s², with median descriptive interval widths about 0.70–0.96 m/s². This does not justify withholding an existing brake request.

The **v1 actual LongControl + CarController shadow replay** covers **197 segments / 12 routes / 570,269 callbacks**. Both sides use identical recorded state, planner, pose, torque and driver response. The adapter was bound to v1; v2/v3 are additional response/entry diagnostics, not a new counterfactual physical controller replay.

- **Zero changed longitudinal packets**, disabled-owner changes, lost/gained active rows or new fault histories.
- **Zero commanded gas under brake/precharge or moving-PID gas while retained received torque exceeds 4 Nm** in the checked corpus.
- Common active, pedal-free brake changes remain **1,370 → 1,370**. No smoothing is demonstrated.
- Named 63 mph highway episode remains **20 → 20**, with identical brake exposure.
- City fixture remains **7 → 7** for the current *local* pair, with identical exposure. The recorded/installed baseline had 17 changes. The seven-change local history includes the earlier **uninstalled below-6.7 mph guard**, which commands more braking in that frozen trace; it must not be credited as a smoother road result. That prior commit was not changed or installed.
- The new selected highway windows reconstruct 22 and 12 changes in the local frozen controller, versus 23 and 13 observed sent-command changes. Clock boundary/history and the uninstalled guard are kept explicit; the new candidate equals that local baseline exactly.

The older retained replay has five active producer-prefix updates with incomplete atomic inputs at the start of one route and uses its disclosed recorded-control fallback. Both new routes have zero active missing-atomic updates. Exact hidden CAN receive-drain order is not logged. This is frozen software replay, not changed vehicle dynamics, ECU response validation, stopping-distance proof or road comfort measurement. Native firmware replay and ARM builds were not run for this inactive, unqualified experiment; no old native result is borrowed as candidate validation.

## Decision and next local work

**Do not integrate or install this prototype.** Its tests prove the proposed contracts and fail-closed behavior; its response data do not establish a useful coast decision. This result does not prove that coasting cannot improve the vehicle, that every brake request is physically necessary, or that no better model can be built.

Keep the city 17-change fixture, original 63 mph fixture, two new highway windows and first-gear high-RPM event as separate regressions. The strongest new protocol lead is the OEM predicted-acceleration/target-speed relationship to shifting and delivered torque. Study that passively against matched OEM/Alpha histories before choosing new CAN semantics or another gain/integral adjustment. Remaining saved maneuver routes may also be re-extracted into the response corpus; no new drive is required merely for that work. Any future changed allocator still needs coupled feedback/command-history checks and hardware validation before road claims.

No paired integration, publishing, device setting change, source switch, install, reboot, OS/firmware update or CAN transmission occurred. Source pair remains `2ca969e45` / `bcd706d0`, and steering/geometry are unchanged.

## Reproduction and retained artifacts

Use the paired checkout's `.venv/bin/python`. `test_allocator.py` and `test_engine_coast.py` cover sentinel separation, uncertainty/support, full-route exclusion, episode independence, urgent/pressure/lead guards, clocks, bounded lease and shadow-only behavior. RED then GREEN logs are retained. `build_model.py` rebuilds v3 from hash-bound caches; `evaluate_new.py` scores the new routes without fitting them; `screen_engine_modes.py` reproduces the separate v3 entry diagnostic. `replay_policy.py` explicitly binds `v1-model-receipt.json` for the full controller shadow replay. `compare.py` fails closed on missing/extra routes and matches the declared 197-segment corpus.

`model-receipt.json`, preserved v1/v2 receipts, `new-model-evaluation.json`, `engine-mode-screen.json`, `comparison-local_state-response.json`, acquisition/extraction receipts, `input-audit.json`, `new-drive-review.json`, `new-highway-fixtures.json`, `high-rpm-timeline.json`, `first-gear-oem-alpha-contrast.json`, health checks and final verification preserve the evidence. Raw signals, route identities, motion and source-rich cases remain in private local caches. No publication was performed.
