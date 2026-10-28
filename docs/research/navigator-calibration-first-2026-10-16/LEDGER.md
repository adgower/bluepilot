<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Execution ledger

- User approved calibration-first design and requested local implementation plus55/65/75/85mph audit.
- Existing dependency environment confirmed scipy1.18.1/numpy2.5.4. No CodeGraph tools are callable; specific previously identified files used as references.
- Paired parent9da98d0c9/child18175406 clean at start. Root BluePilot has pre-existing README changes and untracked research; preserve all.
- Implementation and outputs confined to this new folder and private caches. No source/controller changes or remote writes yet.

- Task1 red: 7 functional failures against unimplemented estimator (plus shape validation passes). First implementation exposed two contract issues: a conditional95% interval cannot guarantee coverage of a single noisy draw; held-out gain-shift detection needed a direct parameter-consistency check. Ruling: test interval precision/centering without claiming guaranteed coverage, and explicitly reject >25% held-out gain shifts. This preserves validation rather than widening acceptance to pass a test.

- Estimator and dataset gates implemented. Initial red8/1 and datasetred5/0; expanded contracts now include source-cache integrity and JSON serialization. Fixed a robust-point/OLS-bootstrap mismatch rather than treating its interval as robust uncertainty. Conditional gain and bias intervals now use the same robust estimator.
- Ruling: distinguish held-out prediction and steady gain support from separate delay/tau identification. A near-flat dynamics profile can support a stable predictive gain, but cannot justify choosing a new delay. Profile bounds are sensitivity ranges, not confidence intervals.
- Whole-route CV on older low-speed episodes added separately from latest-route validation; it cannot be presented as current-revision road proof.
- Independent reviewer foundP2 cache provenance issue; reproduce/red tests and fix underway. All335 signals regenerated unless exact raw/code/payload bindings already verified; normalization checks binding and embedded anonymous label at consumption.
- Naming ruling: controller_map_validated is scientific validation state, not a claim about user authorization. The user has authorized local implementation; this stage has no calibration application path.

- Final reviewer rechecked provenance/staging and per-held-out-route validation: no remaining material findings. Reviewed28core tests plus3tracking tests; full pipeline31pass.
- Exact end-to-end run complete: all335 raw hashes/19 bindings verified, all19 normalized routes,15speedbands, newest routes held out, alltests and final verification exit0.
- Low-speed newest episodes do not meet4s minimum; historical low-speed held-out folds fail/lack support. No map proposed. Broad60–70mph predictive model supports holdout observations, with unidentifiable separate dynamics; narrow65focus additionally fails one low-excitation route's normalized-error gate.55focus also fails route/residual/gain consistency.75band only observed72.5–74,85empty.
- Pair remains clean9da98d0c9/18175406; factors1.20/.97 unchanged. No networking/device writes in this implementation. Durable335raw/APFSclone and privatecache backup: ${USER_HOME}/CommaBackups/<private timestamp identifier>-calibration-first.
