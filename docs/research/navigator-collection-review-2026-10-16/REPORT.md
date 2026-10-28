<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Test-drive collection assessment — October 16, 2026

The new drive materially improves low-speed evidence coverage, but does not establish a calibration or a steering improvement. The 15 mph deficit remains visible. No device settings or steering code were changed; 1.20/0.97 are preserved.

## What was reviewed

Read-only SSH found two sessions newer than the fixed 335-segment analysis corpus. All 51 new rlogs (409,758,697 bytes) were downloaded and SHA-256 verified against device hashes; both sessions have complete, contiguous segment numbering. Private raw recordings and extracted caches are preserved in `${USER_HOME}/CommaBackups/<private timestamp identifier>-collection-review`. Public-facing analysis files use anonymous labels and omit GPS/device identities.

- Collection session 01: October 16, **<private clock time>–<private clock time> CDT**, 23 segments, 22.3 minutes. Maximum speed zero; this is stationary recording, not a calibration drive.
- Collection session 02: October 16, **<private clock time>–<private clock time> CDT**, 28 segments, 27.2 minutes. Includes multiple moving/stopped stretches; maximum speed **38.8 mph**. Stretches within this session are not counted as separate independent held-out drives.

Stable recorded clock offsets provide the times above. Both sessions advertise parent revision `9da98d0c91f0559efa976e3ffb221f2584fd0b88`; recorded startup dirty flags are true, so commit metadata alone does not prove exact recorded source contents. A separate current SSH check found parent `9da98d0c9` and child `18175406` clean for tracked files, with factors 1.20/0.97. Recorded preferences retain angle, low-speed and persistent-tracking options enabled, updates paused and alpha longitudinal disabled. No source/parameter writes, restart, ECU queries or firmware actions were performed.

## Coverage against the plan

All values below are from the moving session. Travel includes manual/inactive time. Eligible means the existing, unchanged freshness, validity, driver/brake, gear, lane-keeping and active-wire-mode criteria pass. Meaningful turning additionally requires absolute requested curvature above 0.001/m. These are sample exposure counts, not independent trials. Plan bands overlap other reporting bands; do not sum overlapping bands.

| Plan band | Travel | Lateral active | Fully eligible | Meaningful turning | Qualifying calibration episodes |
| --- | ---: | ---: | ---: | ---: | ---: |
| 13–17 mph | 93.75 s | 42.90 s | 31.05 s | **19.60 s** | **1 × 12.0 s** |
| 18–22 mph | 60.90 s | 34.50 s | 34.20 s | 12.10 s | **1 × 9.85 s** |
| 23–27 mph | 53.20 s | 30.80 s | 29.90 s | 5.10 s | 0 |
| 40–50 mph | 0 | 0 | 0 | 0 | 0 |

This closes the specific gap of having **no current-version uninterrupted 13–17 mph episode**. It does not close the repeatability gap. The strongest new episode is mostly one command direction (11 s positive, 1 s negative); aggregate meaningful demand includes both signs (13.1/6.5 s), but that is not equivalent to long independent turns in both directions.

The existing selector splits continuous eligible runs into up-to-12-second blocks, requires at least four seconds, input variation, and no more than 3 mph speed spread. At 13–17 mph, 18 additional candidate blocks/runs were shorter than four seconds. At 18–22 mph, 21 were short and one failed speed drift. At 23–27 mph, 28 were short and one failed speed drift. These exclusions are analysis criteria, not instructions to delay braking/intervention or hold speed unnaturally.

## What the steering did

Meaningful eligible sample medians of body yaw / requested yaw were **41.2% at 13–17 mph**, **58.7% at 18–22 mph**, and **78.5% at 23–27 mph**. These are contemporaneous observational tracking ratios, not fitted actuator gains, matched-road improvement percentages, lane-position errors or multipliers to invert.

The most useful new diagnostic fixture starts **<private clock time> CDT**, elapsed 1532 s:

- A 12-second qualifying episode stays between **13.94 and 15.48 mph**, with substantial transmitted-command variation.
- Within it, an approximately **9.85-second** clean meaningful window remains below 70% response, with median speed about **14.5 mph** and body response about **40.7%**. Request changes substantially across this window, so it is not a constant-demand steady-state experiment.
- For the corresponding 9.85 s sample mask, diagnostic stationary-debiased OEM yaw gives about **44.9%** of request, with median absolute CAN/body yaw difference **0.00143 rad/s**. The second signal corroborates low response; stationary debiasing is diagnostic only, not a new sensor setting or ground truth.
- Learned steering ratio is about **22.58** and angle offset about **−1.58°** in this window. Neither was changed.

The comparison episode starts **<private clock time> CDT**, elapsed 1552.85 s, lasts 9.85 s and spans **18.14–21.00 mph**. Its meaningful-demand subset totals 5.25 s: body response median about **60.1%**, diagnostic OEM response **63.9%**. Different subsets and timestamps explain the difference from pooled band medians.

Eight eligible below-70% windows lasting at least 0.5 s were detected in the 13–17 mph band. This confirms useful sustained undertracking evidence, without proving its cause or that this revision improved/worsened it. Current logs were not compared as matched-road controlled trials with a previous revision.

## Calibration support check

The existing frozen historical training corpus was reused without changing its selection gates. These new recordings were held out as whole sessions; no new samples were used to select training parameters. Prior newest sessions remain excluded from training.

| Existing calibration band | Historical training episodes | New held-out episodes | Result |
| --- | ---: | ---: | --- |
| 13–17 mph | 10 | 1 | Too few held-out episodes and independent moving routes |
| 17–20 mph | 16 | 1 | Too few episodes/routes and insufficient held-out duration |
| 20–25 mph | 15 | 0 | No qualifying held-out episode |

The fit abstains before selecting a model. At minimum, the existing assessment requires two held-out routes, three held-out episodes and 10 seconds of scored episode span, plus input-direction/variation support; passing these entry gates still does not establish calibration. Historical route inconsistency remains a separate issue. No gain, bias, delay or controller-map recommendation is established by this assessment.

## Remaining collection checklist

- [x] Retrieve and verify the latest sessions and classify stationary versus moving data.
- [x] Obtain a current-version uninterrupted qualifying 13–17 mph episode.
- [x] Obtain some meaningful turning in both request directions near 15 mph.
- [ ] Repeat comparable gentle turns on **one or two more separate drives**, aiming for the original two-to-three-drive collection goal. A single additional drive can help satisfy route-count entry requirements; it does not guarantee validation.
- [ ] Capture additional qualifying turns near 15 mph, particularly the opposite direction to the strongest new episode. The current 13–17 mph holdout has one episode; the entry gate needs at least three across two routes.
- [ ] Add repeatable 18–22 mph coverage and steadier 20–25 / 23–27 mph transition turns where naturally available. No qualifying 20–25 mph episode was collected.
- [ ] Include a short normal **40–50 mph** reference section when appropriate; this drive never reached it. Existing older highway evidence is retained, but is not a new reference on this outing.
- [ ] Check cross-drive prediction, gain/bias/delay separation and turn-entry/exit behavior before proposing any smooth correction; preserve 1.20/0.97 and good 45 mph behavior.

Use the same practical plan: familiar low-traffic route, good visibility, gentle marked bends, normal supervision. Intervene/brake whenever needed. Do not force an exact speed, delay intervention to meet the four-second selector, or change engagement/settings to manufacture coverage. After parking, note approximate problem locations or times. No 75/85 mph collection is needed.

## Reproduction and limits

`analyze.py` reuses the prior normalizer, episode selector, discrepancy scanner and abstaining estimator. `coverage.json` contains per-session/per-band exposure, exclusions, episodes and discrepancy windows; `heldout-assessment.json` records the support failures; `window-detail.json` records the corroborating OEM comparison. `input-manifest.json` contains anonymous raw hashes and sizes. `provenance.json` binds the analysis inputs/code and private signal payloads.

No new controller/native replay or build was run because no controller or firmware source changed. No physical performance improvement, precise delay, exact corrective multiplier or general safe-operating envelope is claimed. The next useful evidence is repeated low-speed turns and transition/reference coverage, not more high-speed driving or a larger inverse-ratio factor.

Validation: all 51 raw hashes were rechecked after preservation; coverage/episode assertions passed. The unchanged offline estimator/dataset/cache/tracking suite passed **31 tests** (one warning) with repository-level conftest excluded. The initial broad pytest invocation failed on the unrelated Bluepilot native `params_pyx` import; isolated offline tests then passed. No native-controller validation is implied.
