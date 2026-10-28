<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator start/stop local review candidate

**Review only — no installation or transmission authorized or performed.** Snapshot base: opendbc18175406d0cc5af8233afde70a5d121aedf8de44 paired with openpilot9da98d0c91f0559efa976e3ffb221f2584fd0b88. Existing source checkouts and device remain unchanged. Implementation was made in a separate git-initialized source snapshot at ${PRIVATE_CACHE} not on the installed branch. The durable files here are the review deliverable; the temporary checkout may be cleaned up later.

## Contents

- safety.patch: two-file patch against that exact opendbc base.
- review_startstop/oneshot.py: pure one-pair state machine, local JSONL dry-run CLI, and source-review-only adapter accepting a caller-owned publisher.
- review_startstop/test_candidate.py: host C safety behavior tests.
- review_startstop/test_tool.py: pure core, CLI and fully mocked transport tests; no real sockets.
- review_startstop/example.jsonl: synthetic parked fixture, not a recorded vehicle health claim.
- validate.py: compiles normal/experimental host harnesses and runs candidate and existing Ford tests in an already-patched isolated checkout. No automatic patching, dependency installation or hardware access.
- INITIAL_REVIEW.md: initial independent review and intermediate findings. Resolution status below supersedes that historical snapshot.

## Safety patch behavior

All three gates are required: ALLOW_DEBUG, FORD_STARTSTOP_TEST compiler define, and explicit safety parameter0x400A. The extra0x4000 parameter bit is locally assigned for this isolated experiment, not an upstream allocation. No car interface or manager code sets it; no build/install/flash path is added.

A build with either compile gate absent has no experimental behavior. With both defines and the parameter bit, this is a separate **stationary test mode**, not normal driving Ford safety. Only the exact base parameter0x400A can transmit. The test TX list replaces normal TX permissions with0x461/bus0/eight bytes only. No steering/cruise/longitudinal command is permitted in this mode. Other parameter variants with the opt-in bit fail closed for transmission. Normal configurations retain existing RX/TX/forwarding behavior; experimental mode changes RX monitoring and forwarding consequences and must never be used for driving.

Seven raw input IDs must be seen on bus0/eight bytes:0x415,0x202,0x213,0x176,0x165,0x166,0x461. Test RX configuration does not claim OEM checksums/counters for all seven; helper checks speed0x415 checksum/quality and zero speed, second speed0x202 quality/zero, standstill/parking-brake value1, Park request, cruise-state3, known start/stop status and released stock shape. Other validity semantics are unverified. Inputs require age<=200ms except stock0x461<=1.2s. No assertion of comprehensive vehicle health is made.

Press starts only with mode0(enabled), controls not allowed, expected stock bits and released physical candidate. Shape is deliberately restricted to observed first-byte values0/2/4/6 and seven zero bytes; broader drive-mode states are rejected. This restriction is not an OEM encoder specification. The payload copies current stock sequence bits; sequence duplicates are expected and their acceptance is unknown.

At most one high then one low frame per safety initialization; release must be100–200ms after accepted press. Wrong experiment payload/timing or observed unsafe input after press consumes the trial. The firmware does not generate a release autonomously. Mode reinitialization resets the budget; this is not a persistent vehicle-session/global lockout. Normal host TX attempts are rejected before the test helper and do not consume its pair budget.

## Tool behavior

Default CLI reads synthetic/local JSONL and writes only local audit output. Example from this folder, using the configured Python runtime:

```bash
python3 review_startstop/oneshot.py --input review_startstop/example.jsonl --log ${PRIVATE_CACHE}
```

The audit path must be new; existing files are not overwritten. The example emits exactly two local intents120ms apart. Intent output is not transmitted.

**--execute is unconditionally rejected before transport or audit creation**, even with the confirmation phrase. No single flag enables live mode. Do not remove that block as an implied approval step.

The dormant live adapter is present for review and mock tests only. It accepts a caller-owned existing sendcan publisher; it never constructs a second one. This matters because msgq_init_publisher changes the queue writer UID and the old publisher subsequently fails (matching parent msgq_repo/msgq/msgq.cc:157–170,235–240). A future adapter integration must preserve single-writer ownership, serialize normal controller output, and coordinate test-mode configuration without manager races. None of that integration or configuration is implemented here.

Adapter policy: five seconds of valid observed stationary conditions; exact single Panda reporting Ford/test parameter; known enabled initial status; released/fresh stock; fresh carState/pandaStates/selfdriveState/CAN; one trial; finite15s arm window. Release targets120ms after the first timely matching returned-TX echo(src128); tool refuses release later than180ms relative to that observation. A missing/stale echo aborts without retries. CAN event timestamps are publication/batch timestamps, not a precision firmware TX clock. Timing still needs real isolated transport validation before enablement.

Audit output records attempts before publish and separately labels publish as NOT acceptance, then observes candidate/status frames for five seconds. Full independent raw recording and operator observations are still required for a future experiment. It does not claim functional success or auto-restore state.

## Review findings and remaining blockers

Resolved locally:
- Timer previously started before publisher construction/audit. Publisher creation was removed; future release scheduling uses first matching TX echo rather than arm time.
- Missing prearm data now resets the stable interval; future timestamps abort.
- Dry-run regression from a copied adapter block fixed; actual CLI subprocess test added.
- A competing sendcan publisher would displace the normal writer. Adapter now requires the existing writer from its owner; CLI live execution stays blocked.

Still unresolved, deliberately not represented as safe/ready:
- Process crash, blocking audit I/O, unsafe/stale inputs, lost echo or firmware rejection can prevent release. This patch limits accepted host frames/timing; **it cannot guarantee remote asserted duration or successful cleanup**. Stock traffic recovery is not proven PCM behavior. No unsafe-state release override or automatic retry is provided.
- Consumer identity, sequence duplicate tolerance, validity/debounce and coexistence remain unproven.
- Single-writer integration, actual firmware identity/configuration ownership and continuous independent recording are not implemented/validated on the device.
- Park request is a raw requested range, not independent proof of mechanical engagement. Physical operator, parking brake and other environment checks remain essential.
- Ignition is checked in the dormant host adapter, not in the MCU helper. No engine-running state is independently established by the patch.

These are blockers to enabling the adapter for a vehicle trial. This package is a concrete source candidate for review, not a deployable vehicle feature or a claim of safe active testing.

## Local validation evidence

Initial safety tests failed before the patch. Initial tool test failed before implementation. Final candidate suite:38 tests passed, including a fully mocked two-request adapter path and a CLI proof that --execute cannot reach transport. Existing Ford suite passed against both normal and experimental host builds with the test parameter OFF:130 passed,79 skipped,12,008 subtests passed in each run. No sanitizer, embedded build, flash, real messaging socket, device runtime, PCM acceptance or road validation claimed.

To reproduce against an isolated opendbc checkout already containing safety.patch:

```bash
/path/to/matching/python validate.py /path/to/isolated/patched/opendbc
```

Use the matching Python dependencies from the parent checkout. Temporary native libraries are built locally; the review bundle contains source only.

See ../LLM_HANDOFF.md for recordings, wiring, source hashes, authorization history and prior research. No device command, firmware installer or active transmission command is included in this README.
