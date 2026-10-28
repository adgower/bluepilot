<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator wait/catch-up prototype — 2026-10-15

Local experiment only. No SSH, device writes, settings changes, firmware changes or activation. The paired release checkouts remain unchanged. This evaluates command behavior against recorded inputs, not physical response to commands the vehicle has never received.

## Problem and chosen change

The prior drive assessment found a 21–22 mph shortfall near drive-02 elapsed 499 s (about <private clock time> CDT). Requested curvature oscillates while measured pinion curvature remains near −0.0025/m. The fractional recovery predictor can treat a smaller request denominator as evidence of catching up and repeatedly discard the wait/filter state.

`wait_catchup.py` preserves existing eligibility, persistence window, hold duration, proportional term, feedforward, limits and 25 mph fade. Its narrow exception requires **both fractional and measured recovery** before predicting catch-up from a small demand fluctuation. The instantaneous 70% response threshold still releases. Three consecutive demand declines exceeding 5% cumulatively retain the old predictive unwind release. This is an experimental distinction between jitter and unwind, not an identified EPS model.

Any term newly admitted by the exception starts the existing finite command-area episode: **0.00025 rad·s before final limits**. The budget is not increased, and reset, dropout, driver intervention or reversal cannot replenish it. Only the original full valid quiet/settled dwell can rearm it. This also means a brief exception can suppress later correction until a valid dwell occurs.

The candidate uses local multiple inheritance so the exact current budget/rearm/update implementation surrounds the modified admission method. This is an experiment seam, not proposed production architecture. Baseline is the current installed BudgetedTrackingPrototype with the same synchronized safety metadata, rather than the older release strategy or older metadata.

## Iterations and tests

- `red.txt`: original controller fails the request-dip/flat-response regression; three other targeted protections pass.
- First measured-recovery-only candidate (`wait_catchup_v1.py`) passed that regression but failed sustained-unwind predictive release (`unwind-red.txt`). Expanded simulated weak/slow plants also showed up to 0.004886 added peak excess normalized to peak demand. Rejected as a deployment candidate. `v1-full-replay.*` is an interrupted partial run, not a full validation result.
- Final candidate adds sustained-unwind release and charges newly admitted exceptions to the unchanged budget. `focused.txt`: 58 tests pass, including original admission/freshness/driver/lane/platform/flags/default-OFF/caps tests, new request-noise and unwind cases, both steering signs, and all inherited budget/rearm tests.
- `expanded-v2/final-command-screen.json`: 540 paired simulations at 15/22/45 mph, six demand patterns including noisy unwind, two assumed response gains, three lags and five delays; plus two saturation and ten forced-abort cases. Range/slew assertions pass, all trace endpoints settle, and no case adds peak response excess versus the installed controller in this tested grid. All 45 mph simulated traces match. Worst after-last-internal-term command tail remains 0.000740499 rad·s. These are hypothetical plants, not vehicle validation or a guarantee about untested conditions.

[Private/local visualization omitted](../../navigator-reference/PRIVATE_ARTIFACTS.md)

## Actual-send-time reconstruction

`reconstruct.py` replays all 55 latest route segments at recorded steering-send timestamps, with recorded state/control/model validity and context ages. The candidate and installed strategy see identical inputs. This complements the full generated-command replay, whose controller frame phase is reconstructed.

In the target window (498.7–500.511 s), the installed strategy produces six nonzero extra terms; the final candidate produces eight. Four candidate frames at 499.183–499.333 s continue correction where the installed strategy had withdrawn it: approximately 0.20 s, peaking at 0.0013444 rad (1.34 mrad) final path-angle difference. It then reaches its budget and stops; two later installed pulses are suppressed. This moves a small amount of correction earlier and makes that first burst continuous. It does **not** establish enough correction to solve the turn.

Across the latest route, the candidate uses the entire 0.00025 rad·s budget, with no reconstructed rearm. The installed controller's later single 11.8 mph pulse is consequently suppressed. No additional correction occurs at 13–17 mph in this recording. At every recorded sample ≥25 mph, candidate and installed path-angle outputs are identical, including the highway portion. The 1.20/0.97 base factors are unchanged.

The recorded wire messages belong to the installed strategy. Candidate-to-wire error is not a fit/improvement score: candidate commands were never driven, and the measured trajectory is held fixed. The original approximately 59% body-response shortfall cannot be converted into a predicted improvement percentage.

## Full cached native safety replay

See `full-replay.json`, `input-manifest.json`, `provenance.json` and `summary.json` for final counts and assertions. Scope: eight cached sessions, **160 segments** (144 moving-route segments plus 16 parked-session segments). Every input hash matches the earlier 89-segment and latest 71-segment receipts. Two independent native safety-library instances receive chronological physical RX and candidate/baseline generated TX. No forced controls permission, safety edits, networking, firmware or live ECU interaction.

**Completed and verified:** 36,949,571 physical RX frames and 927,410 controller updates; baseline and candidate each generate 580,109 frames. Each has 577,162 configured TX accepted and **zero rejected**. The remaining 2,947 generated frames occur outside Ford safety configuration and are reported separately, not counted as accepted. Critical RX validation rejection maps are empty. All eight sessions preserve default-OFF whole-stream parity and all generated bytes at ≥25/45 mph. Candidate differs on 182 controller updates across the full cache, three on the latest route.

This is generated-command hook replay. It does not resolve the earlier actual-device rejected-frame echoes at brake/cancel permission edges, or claim to reproduce USB arrival timing. The separate prior recorded-TX replay and its known rejections remain valid evidence; see the prior drive assessment.

`verification.txt` confirms all assertions, current clean paired heads 0cc74c94f3c6dafa3790c303be9ef345878bd792 / d64ffcfa4e4a7556151962ca304d223a0a323375, factors and data hashes. Candidate SHA-256: `9adbea31909884995469aa1e816d8085735e6eb552f5825a2fdba0ea6a218b12`. Native safety library SHA-256 is recorded in `provenance.json`. Python compilation/import checks passed; no new device build or physical validation was performed.

## Interpretation and next boundary

This is a bounded prototype for the observed false catch-up reset, not a completed low-speed steering fix. Existing feedforward, Navigator geometry, pinion selection and 1.20/0.97 remain intact; ≥25 mph recorded outputs and 45 mph simulation outputs are preservation checks. The small finite burst and lack of a quiet rearm in this recording limit benefit. Do not raise the budget based on this result alone. Physical handling, EPS response, bus timing and on-device execution of this new prototype remain unvalidated. No installation was performed or requested in this turn.

## Reproduce

Use `${USER_HOME}/Apps/openpilot/.navigator-master-integration-20261014/.venv/bin/python` to run `run_tests.py`, `expanded_screen.py --out expanded-v2`, `reconstruct.py`, `full_replay.py`, then `verify.py` from this directory. Run the scripts themselves by absolute path or from the Bluepilot root. All use cached files only. The frozen parent/child dependencies are recorded in `summary.json`; relocating caches requires explicit path edits. `verify.py` checks source factors, untouched paired checkouts, fixture parity, simulation assertions, complete coverage, baseline/candidate rejection equality and high-speed byte parity.
