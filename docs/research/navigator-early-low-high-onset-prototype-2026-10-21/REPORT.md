<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Earlier low-speed and 70–75 mph onset prototype — October 21, 2026

Local experimental candidate; no paired integration, build, publication or device changes. Owner1.20/0.97 and installed pair db584234805cf2039ee976d856a29b655188ad2a /8ccc6cf0ee123afddddbf6e0a0ea3d3316669a5e remain unchanged.

## Behavior

`prototype.py` adds five-frame independently validated rising-demand admission only between20 and25mph. The added term shares the existing0.00025rad·s ramp allowance, is capped at the smaller of0.0015rad or5% feedforward, lasts at most0.25s, and fades out by25mph. It validates original intent against the original atomic wheel target, requires wheel/body under-response and rejects evidence already outside the existing curvature deviation band. Current safety clipping remains authoritative.

Between70 and75mph, independently validated withdrawing-demand evidence can credit the existing onset confirmation in both blended branches. Current body margin, wheel predictive closure, release rules, caps and rate limits remain in force. There is no roll feedforward extension. Whole installed-policy output is selected outside the two new bands; boundary slew and residual handling are tested separately.

## Saved episode result

Final frozen candidate original-send reconstruction is in `saved-scene-final/`. Before the low-speed clamp binds, two commands change at219.185s and219.234s, about0.35s before the first clipped command. Maximum path-angle difference is0.001383rad. All29commands in the severe clipped window remain unchanged. This is an earlier-entry hypothesis, not a resolution of the entire35–41% response episode.

At74mph, the first56-frame pre-input window changes9 floating commands (maximum0.000801rad); the second changes32 (maximum0.001945rad). This is a counterfactual command comparison on frozen measured motion, not a prediction of achieved response or lane clearance. Both human inputs remain annotated as avoidance of tire debris. No outer boundary handoff was pending in the focused saved scene.

## Verification

- Behavioral baseline:10failed/26passed before implementation.
- Final focused behavior/fault/cadence suite:90passed. A separate60ms cadence regression reproduced nominal-time budget excess before repair; measured-time accounting fixes it.
- Independent read-only review: no remaining material findings after repair; see `REVIEW.md`.
- Active abort/reversal matrix:112cases pass, zero relative neutral-command tail.
- Shadow-intent parity:17,000updates pass.
- Full60recording/878segment controller/native replay: **accepted locally**,5,063,641controller updates and201,206,149physical RX frames per native variant. Exact rejection lists match: five shared existing events per context, zero added events. Candidate changes412recorded-context updates (42low,370high) and630causal-fixture updates (61low,569high). Whole disabled streams and output outside20–25/70–75mph are identical.966transition cases/309,120frames pass range, slew, exposure and settling checks. Final manifest/source audit passes; see `acceptance.json`.
- Native safety library reused only after matching its prior accepted hash; no fresh native build is claimed. Paired production source and native safety source are unchanged.

## Clamp and parking

See [software versus parking](CLAMP-AND-PARKING.md). The observed clip is application software, with separate Panda checks; these traces do not establish the vehicle EPS maximum. OEM parking instructions establish a stationary parking workflow, not unrestricted authority through the current on-road command interface. No limits or steering modes were widened.

## Remaining limits

Replay can detect command regressions, budget/guard failures and added native rejections. It cannot prove physical benefit, EPS acceptance under all conditions, road safety, or85mph stability. The severe low-speed deviation clip remains unresolved by this bounded candidate. No installation is authorized or implied by this report.
