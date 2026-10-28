<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator upstream readiness: local evidence audit

Audit date: October 19, 2026. Local source and existing reports only. No SSH, ECU queries, CAN traffic, branch changes, fetch, push, or PR creation. No owner VIN or device identifiers included. Historical device observations below are not a fresh vehicle inventory.

## Conclusion

The project has substantial personal-fork operating evidence, but does not yet establish natural Navigator identification or compatibility with the unmodified upstream Ford controller. The smallest support proposal should separate native identity, firmware matching and justified geometry from all experimental angle-control, pinion, safety, gain, MADS and longitudinal work. An identification-only change may be a useful first step, but must not claim working stock support without the missing compatibility evidence.

## Existing evidence and limitations

| Area | Evidence available | What remains unresolved |
|---|---|---|
| Vehicle | Research consistently identifies a 2023 Navigator; OEM comparison refers to the owner's Reserve; project geometry is short-wheelbase | Privately confirm model year, Reserve trim, drivetrain, SWB rather than L, market, and factory driver-assistance package from build documentation; reports are not authoritative build records |
| Geometry | Existing commit `a6dd3a44` is recorded as tape-measured wheelbase 3.1115 m, door-sticker-inferred historical base mass 2742 kg, community-reported steering ratio 19.6 | Wheelbase measurement is materially better grounded than ratio. Preserve this provenance; obtain OEM geometry/ratio confirmation if feasible. Door-sticker mass inference is not a certified curb-weight measurement; current normalized upstream does not need the old mass field |
| Identity | October 14 launch script forced `FINGERPRINT=FORD_EXPEDITION_MK4`; decoded CarParams says `fingerprintSource: fixed` | No natural match proved; cached runtime selection cannot establish which firmware matcher would select Navigator |
| Network | Historical cache: CANFD flag, forward-camera network location, Ford safetyParam 2, stock ACC (`openpilotLongitudinalControl=false`) | These are selected configuration values, not independent proof of harness wiring or live firmware. Need actual harness model, installation topology, and camera-module/hardware applicability |
| Firmware | Five decoded cached manufacturer-software replies from request `22 F1 88`, listed below | Exact bytes including NUL padding, ECU enum, address/subaddress, request, bus and multiplexing must be extracted from original CarParams/log artifacts before adding fingerprints. The prose table intentionally strips padding and cannot be pasted into fingerprints.py |
| Cache provenance | October 14 passive SSH audit read CarParams variants and hashes; startup clock jumps explain misleading July mtimes | Acquisition date and association to the current vehicle were not established in that audit; do not describe these as fresh ECU responses. Correlate with a verified vehicle route/initData privately |
| Routes | Historical local reports contain multiple drive analyses, native replay, manifests and source revisions; later roadmap records 32 sessions/637 segments and 3,704,143 updates per variant | Large personal replay volume does not replace a small reproducible upstream route. Select a complete raw route with CAN, carParams/carFw, relevant state, original source provenance and deliberate sharing permission; compact exports may omit needed fields |
| Running software | October 18 installation report records paired parent `50baa6fd6acf9d37b7e0768e5736efab2a357ddc` and child `0e65f296260ec16da3c3b814c10ac5f36f8b2e4c`, ARM build and stationary acceptance | Historical parked acceptance does not prove stock upstream steering or road improvement. No fresh device state was read for this audit |

### Cached firmware inventory

Read from saved data October 14, not actively queried then:

| Cache ECU label | Address | Display identifier (padding removed) |
|---|---|---|
| fwdCamera | 0x706 | RJ6T-14H102-BAH |
| eps | 0x730 | NL14-14D003-AE |
| abs | 0x760 | PL14-2D053-AB |
| fwdRadar | 0x764 | ML3T-14D049-AL |
| engine | 0x7E0 | PL7A-14C204-DE |

Saved bus 0/bus 1 records mostly marked obdMultiplexing true do not prove live routing. Additional `22 F1 10` entries use ambiguous labels and are not established Ford ECU identities. Saved As-Built blocks are unrelated to the minimal support task unless a maintainer identifies a concrete requirement. APA 2.0 hardware/retrofit research is separate.

## Current local checkout versus historical upstream

Fresh local check: `${USER_HOME}/Apps/opendbc` is on `master` at `3e92d112129507debe45364891954db70238997a`, tracking `origin/master` from `https://github.com/adgower/opendbc.git`. Its only short-status entry is untracked `.navigator-master-integration-20261014/`; it must be preserved. No public upstream remote is configured in this checkout.

This checkout's Ford values have no Navigator definition and still use old mass-bearing CarSpecs. Its Expedition values are mass 2000, wheelbase 3.69 and steering ratio 17.0. These are observations about a stale local fork, not current commaai master and not authoritative Expedition specifications. Do not base a public PR on this working tree or modify the Expedition platform globally to fit Navigator.

The October 14 upstream comparison pinned public opendbc `b3bd79a659dae961af169a3baac723961f720133` and openpilot `690fa743b945973d594f2dfa143eee4fabc98a70`. Those are historical snapshots; refresh the actual upstream PR base before implementation. Existing Ford docs already group Lincoln Aviator with Explorer in this stale snapshot: platform sharing and a Lincoln display name are different decisions from whether Navigator's dimensions justify a distinct platform.

## Personal dependencies to exclude from the first PR

The fork runs custom angle steering and engagement ordering, fixed pinion-derived feedback with paired Panda geometry/safety, owner 1.20/0.97 calibration, opt-in low/high-speed tracking and calibrated wheel-target/unwind policies, plus parent settings/registry/UI plumbing. Some protocol and control changes may be valuable independently, but the evidence above does not prove the Navigator works correctly with those removed. Earlier logs also show raw-yaw versus calibrated/model discrepancy; this needs explicit stock-controller assessment rather than assuming firmware identification solves it. Keep these investigations separate from firmware matching and native identity.

## Minimum next evidence work

1. Recover original cached CarParams and complete raw route artifacts privately; extract exact five-ECU bytes and provenance. Do this before requesting new ECU collection.
2. Run the current upstream matcher offline against the exact saved firmware set, without any forced fingerprint. Record exact/fuzzy candidates, no-match/ambiguity result and which fields disambiguate Navigator from Expedition and other Ford platforms.
3. Confirm SWB/year/trim/drivetrain/package/harness and parameter sources; propose only the validated year/configuration, without assuming Navigator L or every model year is equivalent.
4. Replay a selected complete raw route against the stock upstream parsing/controller/safety path. Compare relevant CAN protocol, stock ACC, engagement/release, faults and steering response. Treat replay as compatibility screening; ask maintainers what normal supervised stock road evidence they require before changing device behavior.
5. Prepare one clean branch from fresh upstream. Likely minimal files are Ford vehicle definition/docs, firmware fingerprints and the repository's existing route/test registration when required. Use existing shared tests first. No new general-purpose framework or bulk historical reports in the public PR.

## Sources

- [Project roadmap and explicit NAV-11/NAV-12 separation](../../NAVIGATOR_ROADMAP.md)
- [Feature inventory and geometry provenance](navigator-branch-feature-list.md)
- [Passive cache and exact acquisition limitations](navigator-active-park-assist-2026-10-14.md)
- [Owner Reserve reference and limits of OEM research](navigator-ipma-oem-comparison-2026-10-14.md)
- [Historical source and upstream version comparison](navigator-upstream-master-comparison-2026-10-14.md)
- [Settings, forced identity and normalized-model migration](navigator-migration-settings-2026-10-14.md)
- [Raw-yaw versus steering-model discrepancy](navigator-steering-latest-2026-10-14/REPORT.md)
- [Historical paired integration and replay limits](navigator-master-integration-2026-10-14/REPORT.md)
- [Latest documented paired installation and parked checks](navigator-wheel-target-installation-2026-10-18/REPORT.md)

Structural CodeGraph tools were not exposed in this audit's tool inventory. No claim of a current graph query or graph validation is made. Inspected known source files directly; source findings are explicitly local, not current upstream.

## Public-source addendum: October 19 browser verification

Read current public master through BrowserOS Neo. These are moving-branch observations, not a pinned PR base:

- [Ford values.py](https://github.com/commaai/opendbc/blob/master/opendbc/car/ford/values.py) contains no Navigator definition/display name. Explorer still groups Lincoln Aviator; Expedition remains wheelbase 3.69, ratio 17.0. Current CarSpecs omit mass.
- [Ford interface.py](https://github.com/commaai/opendbc/blob/master/opendbc/car/ford/interface.py) uses shared Ford angle control, CANFD safety flag, center-to-front 0.44 × wheelbase, and blocks unsupported SecOC when camera-bus messages 0x3d6/0x186 are not 8 bytes. Confirm those packet lengths from the saved Navigator CAN; CANFD alone is not sufficient.
- [Ford carcontroller.py](https://github.com/commaai/opendbc/blob/master/opendbc/car/ford/carcontroller.py) sends curvature in CANFD mode 1, with path-angle/path-offset terms zero; current curvature is `-yawRate / max(vEgoRaw, 0.1)`, with a curvature-error clamp above 9 m/s. This differs materially from the personal angle/path-angle/pinion control path. Existing logs must establish stock-path suitability rather than conflating the two.

### What actual AI-related reviews establish

| Primary example | Observed contribution/review | Supported conclusion |
|---|---|---|
| [openpilot #38250](https://github.com/commaai/openpilot/pull/38250) | 17 additions/1 deletion across two files; wider degenerate-input guard and new tests; prose Summary/Change/Test; process replay 66 passes. [Adeeb's comment](https://github.com/commaai/openpilot/pull/38250#issuecomment-4871218169): “Closing. Indistinguishable from an LLM” | He explicitly rejected this contribution in those terms. Comment does not explain which prose, test or implementation feature caused that judgment |
| [openpilot #38255](https://github.com/commaai/openpilot/pull/38255) | Five files; timeout callback cleanup; issue reference, lint/test commands; process replay 66 passes, identical UI previews. [Adeeb's comment](https://github.com/commaai/openpilot/pull/38255#issuecomment-4871232700) uses the same closure wording | Passing checks did not secure acceptance. No basis to claim that tests themselves were the cause |
| [openpilot #38467](https://github.com/commaai/openpilot/pull/38467) | 12 additions/7 deletions, four files, concrete broken links after directory restructure; explicit Claude-assistance disclosure, mechanically verified targets, local lint/docs-build evidence. Adeeb merged August 7 and [commented thanks](https://github.com/commaai/openpilot/pull/38467#issuecomment-5220235517) | Direct counterexample to a blanket prohibition on disclosed AI assistance |

The closure quote above is repeated once because the wording was identical in both reviewed comments. These examples do not justify psychological claims about Adeeb or an invented policy that small diffs, automated tests, or AI assistance are categorically unwelcome. Practical recommendation (our inference): demonstrate a real owner problem and original vehicle evidence, personally understand every changed line, keep scope narrow, follow existing tests, and state exactly what was exercised. Avoid speculative drive-by fixes, excessive generated explanation, unsupported confidence and test-count marketing. AI concealment is not the strategy.
