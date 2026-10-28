<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# October 17 evidence refresh and 50–70 mph audit

## Result

All currently available new recordings were downloaded: **six sessions / 129 segments / 1,119,859,843 bytes**. A final read-only remote inventory check exactly matched the downloaded segment names. All 515 retained raw segment hashes were reverified. The expanded evidence corpus is **27 sessions / 515 segments**. Six freshly extracted/normalized sessions add **66.86 minutes of eligible active-control exposure** across all speeds. Raw logs and GPS-bearing extraction caches are preserved privately in `${USER_HOME}/CommaBackups/<private timestamp identifier>-new-drive-evidence`. Normalized analysis files omit GPS/device identities.

The existing device remains clean at parent9da98d0c9/child18175406 with1.20/0.97. No setting/source writes, restarts, updates, firmware actions or ECU queries occurred. This is recorded-data analysis, not an installation or a new native safety replay.

**Highway evidence is much stronger, but it does not justify a blanket steering boost or an inverse-percentage gain reduction.** The observed steady-request body response remains modestly above request; wheel/roll/model and directional consistency deserve investigation. Your new drives also close the previously missing opposite-direction steady evidence at40–50mph.

## New sessions

Times use stable recorded clock offsets, displayed in America/Chicago (CDT). Every new session advertises the existing9da98d0c9 revision. Recorded startup dirty flags can be true; revision labels alone do not establish exact recorded source identity.

| Anonymous session | Start CDT | Duration | Segments | Maximum recorded mph |
| --- | --- | ---: | ---: | ---: |
| oct17-session-01 | <private clock time> | 11.6 min | 12 | 72.7 |
| oct17-session-02 | <private clock time> | 12.0 min | 12 | 64.7 |
| oct17-session-03 | <private clock time> | 23.2 min | 24 | 63.6 |
| oct17-session-04 | <private clock time> | 21.4 min | 22 | 65.6 |
| oct17-session-05 | <private clock time> | 31.2 min | 32 | 72.7 |
| oct17-session-06 | <private clock time> | 26.1 min | 27 | 79.7 |

## 50–70 mph: saved baseline and expanded evidence

Definitions and thresholds were reused unchanged: fresh/valid active mode1, no recent driver steering/brake/fault/lane-change exclusions; meaningful requested curvature above0.001/m; steady-request phase based on a past-only one-second window with ≤10% curvature range, same turn sign and ≤3mph speed spread.5%/20% sensitivity is retained. “Steady request” does not prove settled response, a flat road or independent trials. All medians below are observational body yaw/request ratios, not controller gains or lane-position errors.

| Band | Previous steady exposure | Expanded steady exposure | Expanded median response | Negative / positive request exposure |
| --- | ---: | ---: | ---: | ---: |
| 50–55 mph | 7.95 s | 20.40 s | 109.7% | 6.90 / 13.50 s |
| 55–60 mph | 13.10 s | 49.35 s | 113.8% | 29.10 / 20.25 s |
| 60–65 mph | 30.45 s | 81.25 s | 112.2% | 31.55 / 49.70 s |
| 65–70 mph | 4.60 s | 11.20 s | 111.2% | 5.25 / 5.95 s |

Combined50–70steady exposure grows **56.10→162.20s**, with median response **112.1%** in the expanded set. Both turn signs are represented. This is improved evidence coverage, not a before/after improvement in steering: no controller revision was installed between these cohorts.

### Command, wheel and roll cross-check

| Steady band | Wire/feedforward median | Learned wheel/request without roll | Learned wheel/request with roll | Body/request |
| --- | ---: | ---: | ---: | ---: |
| 50–55 mph | 100.0% | 103.4% | 111.7% | 109.7% |
| 55–60 mph | 100.0% | 103.2% | 115.5% | 113.8% |
| 60–65 mph | 100.0% | 97.9% | 113.6% | 112.2% |
| 65–70 mph | 100.0% | 95.6% | 114.1% | 111.2% |

The mapped command is generally delivered, while recorded roll/model effects account for a substantial part of wheel/body differences. OEM yaw broadly corroborates body response. Recorded roll and learned parameters are estimates, not independent road-bank truth or proof that roll causes every error. A static speed multiplier could hide road/direction/timing effects. Normalized-grid command comparisons are diagnostic, not actual-send limiter telemetry.

### Prospective check of the55–60model

The saved-only55–60mph transfer model passed its original prediction/support checks. It was then **frozen**, not retrained, for the newly downloaded sessions.62new qualifying episodes give pooled normalized prediction RMSE0.0825 (gate0.25), with every new session below that error gate. However, the last session has only one qualifying55–60episode and residual/input dependence0.4075, above the unchanged0.35 per-route gate. The expanded assessment therefore withholds calibration support despite close pooled prediction. Speed and roll also correlate with that episode’s residual; this is a diagnostic pattern, not causal identification or a steering-fault alert.

Other50–70bands fail existing route/episode support or model-consistency checks. Expanded current-only whole-route CV also fails or lacks support; no new validated gain map is produced. More highway miles alone are not the primary next step: inspect model/roll/directional propagation and residual scenes before changing command scaling.

## One new highway under-response fixture: engagement transition

Only one new ≥30mph below70%-response window lasting at least0.5s appears in the existing scanner: **October17,<private clock time>:12p.m.CDT**, session05, ~61mph, duration1.05s and median response55.7%. Request rises about42.9%; the window has no steady-request samples.

Actual-send-time reconstruction shows assistance was inactive/mode0 immediately before elapsed835s. On engagement, the unchanged high-speed command slew limit ramps path angle by0.009rad per20Hz frame; feedforward is reached around835.3s. All160saved sends in elapsed832–840s match reconstruction within half a0.0005rad wire step. The historical Panda TX-blocked counter stays at5 through the scene. Body response subsequently catches up; a fixed+1s comparison brings the earlier window near112% of request. This is an engagement/rising-demand transient with an initial rate-limited command, not clean evidence for increasing the steady highway gain. The rate limit was not changed. [Trace and source](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The85retained new discrepancy fixtures include overlapping five-mph and custom bands, so their counts are not independent episodes. Several brief >130% windows accompany request withdrawal. They are diagnostic selections, not lane departures or proof of persistent oversteer.

## What the new data adds at other speeds

| Band | Previous steady-request exposure | Expanded steady-request exposure | Expanded median response | Updated evidence status |
| --- | ---: | ---: | ---: | --- |
| 30–35 mph | 10.90 s | 11.10 s | 101.3% | Near target in this subset; independent-route consistency still fails |
| 35–40 mph | 1.30 s | 5.00 s | 112.9% | Still sparse sustained evidence |
| 40–45 mph | 1.35 s | 9.40 s | 122.6% | Both turn signs now present; roll/model comparison remains material |
| 45–50 mph | 6.35 s | 27.35 s | 114.6% | Both turn signs now present; three qualifying transfer-fit sessions |

The full40–50steady cohort previously had zero negative-sign exposure; it now includes both signs in each five-mph band. That closes the specific direction-coverage gap, not calibration validation.40–45has9.4s of steady exposure and45–50has27.35s. Whole-drive validation still rejects or lacks a consistent model.45mph remains fully in scope; subjective feel is not proof of optimal tracking.

Below25mph, the new logs reinforce the unresolved shortfall. Expanded13–17meaningful demand totals51.25s with median response43.9%, but relatively steady-request support is almost absent. New examples include ~13mph at1:46:24p.m. with about39% response over3.25s. They are changing-demand/intervention-prone diagnostic scenes, not validated steady gain experiments. Saved fixtures remain useful for local controller/admission research; no further low-speed prototype was installed.

The newest session reaches **79.68mph**, extending the prior74mph maximum. New75–80travel totals only6.2s and contains no eligible meaningful bends or qualifying transfer-fit episodes.80–85and higher have no recorded coverage. Recording a speed on a straight section does not validate turning response there; no dedicated85mph collection is requested.

## Remaining collection and next investigation

- Continue ordinary **35–50mph** collection, especially sustained gentle35–45bends and additional independent45–50examples. Both directions on a familiar route where practical remain useful.35–40still has only5s of relatively steady request;45–50has only three qualifying transfer-fit sessions, short of the current-only CV’s four-route minimum. More data may expose model mismatch rather than make a gate pass.
- No additional special50–65highway mileage is needed before investigating the current residuals.65–70steady exposure remains thinner at11.2s; ordinary future drives can add it naturally.
- Next local technical question: how learned ratio/offset and roll/model effects reach the application-side angle map/feedback, and why some whole-drive residual patterns persist. Keep native safety interpretation separate. Do not invert112% into a universal gain.
- Normal supervision/braking/intervention take priority. Useful4–12s episodes should occur naturally; no forced exact-speed holds or delayed intervention. After parking, approximate problem times help locate scenes.

## Evidence and limits

`saved/` is the requested frozen saved-drive50–70audit. `expanded/` includes all27sessions and23band definitions, with old source-diverse training kept separate from current-revision whole-session holdout and current-only CV. `new-session-summary.json` records every new session/range, including travel versus eligible/meaningful exposure. `new-discrepancy-windows.json` preserves all selected weak/high-response scenes. `prospective-55-60.json` proves the saved historical model stayed frozen. `verification.json` records all515raw hashes,27normalized inputs and6new extraction bindings, phase/direction reconciliation and the61mph onset reconstruction.

No new gain recommendation, automatic calibration, paired-source change or road-validation claim is made. The earlier386segment native replay remains its own evidence; these129new logs were analyzed, **not added to a newly run native safety replay**. Raw/private GPS caches remain outside the report folder.
