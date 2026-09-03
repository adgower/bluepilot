# Personal Chestnut integration provenance

## Status

`codex/chestnut-personal-2` is a personal development integration for a comma
four with the official Chestnut/GPU/power kit. It is **development-only and
not installable**. Host tests and a host build establish source reproducibility;
they do not establish CI, an installable upstream artifact, device behavior,
or vehicle safety.

The pre-provenance verified integration HEAD is
`d3fdabbd7a310fc2a8b99604b9930e9b4637eeac` (`test: make messaging retry
process spawn-safe`). This document is committed immediately after that HEAD.
A Git commit cannot embed its own SHA, so the documentation commit and the
published remote HEAD must be verified through Git history after publication,
for example with `git rev-parse codex/chestnut-personal-2` and
`git log --first-parent d3fdabbd..codex/chestnut-personal-2`.

## Reproducible source tuple

| Component | Verified value |
| --- | --- |
| Branch | `codex/chestnut-personal-2` |
| SunnyPilot source | `e87dbbaba710bbfe7661d9ff064d46170cac9442` |
| Incorporated OpenPilot | `6249f4d5b0e63c05f08bce12ca3afebda9f764a3` |
| AGNOS | 19.7; `agnos.json` SHA-256 `ce7eeb20a915a16ec2f4363fdeace6e4cbb2918f3ee929cc7388e4a601657d74` |
| Chestnut firmware | `ed4e39b7`; `firmware_wrapped.bin` SHA-256 `9520fde0bf43d499c07abd0a09b74e94d8a7cc3d610f577b7a4e218ab8a378e9` |
| Small model | `CD210`, ref `5b6436a90cf6902b8aaa71c2b6f3d7164d8ae391`, SHA-256 `c5be11d2fb1115be953c541f30c50f7c71a00bc4a0e128e19aa11b60689317fc` |
| Big model | `BMRLNAP Model v4`, ref `f877d7a0ccc3cce943c76e285214c020cd65c899`, SHA-256 `2c814f08a2c51323b87839fbf8d2c2a9853a2b5536271b3d67f7b7a2de7f9374` |
| BluePilot merge source | `501a7c0e911245044196fcc90cb077a69fa0749b` (PR #195) |
| Original personal rollback | `1f4ec37186e6d9f7a3679790b1a75b026e008c26` |
| Flattened opendbc provenance | `f95f996f`; this is source provenance, not a live submodule |
| msgq | `e7396e76dadbb49e374d4b664ff6bbb43a39bcb0` |
| neural network data | `03cac2d30e111e0689c0429cb8c1fe6cb5a905af` |
| panda | `74a0adced421e8b7acd728d0f9988ce225423f13` |
| rednose | `28d4a7f69e80e1c3e0d24ca0733d7daeaeade3d0` |
| teleoprtc | `1aa8fc433bef1519a95c0700c96258c3be6dfb34` |
| tinygrad | `e837e367aac9e1a66e689f4f32ce20ca9367df13` |

No opendbc submodule is declared or initialized. Git LFS pull and fsck are
green, and all six declared submodule pins above are exact.

## Integration and behavior boundary

Sunny owns Chestnut detection, firmware qualification, hardware state, AGNOS,
model catalogs/downloads, and model runtimes. BluePilot consumes the canonical
Chestnut state and leaves Ford controls on ordinary model/planner messages.
The small and Chestnut model slots remain separate and the legacy USB-GPU key
is only a one-way migration source.

No Ford retune is included: angle-mode high remains `1.25` and low remains
`1.29`. The literal one-comment opendbc plan gate was impossible after the
nested Sunny layout. Its provenance-aware replacement classified 189 paths
against `501a7c0e`: candidate-to-original Ford production/safety content is
only PR #195; inherited non-Ford opendbc content maps to `1f4ec371`; four
exact nested imports are reversible; 27 paths are whitespace-only; one
test-only dampening assertion correction is inherited; and `mads.h` has one
MISRA comment. This is a classification/audit result, not a new Ford behavior
claim.

## Host verification evidence

Task 4 completed `git lfs pull` and `git lfs fsck` successfully. The complete
Sunny model suites ran as follows (both exit 0):

```bash
PATH="$PWD/.venv/bin:$PATH" pytest -q openpilot/sunnypilot/models/tests
# 53 passed, 1 skipped in 11.49s

PATH="$PWD/.venv/bin:$PATH" pytest -q openpilot/sunnypilot/modeld_v2/tests
# 100 passed, 1 skipped in 5.47s
```

Six submodule pins are listed in the source tuple. The initial collection
attempts required standard ignored host build products; the final commands
above are the binding results.

After the test-only spawn-safe commit `d3fdabbd`, Task 5's exact stock-launcher
Step 1 command passed cleanly:

```bash
PATH="$PWD/.venv/bin:$PATH" pytest -q openpilot/cereal/messaging/tests openpilot/common/tests/test_params.py openpilot/sunnypilot/system/tests/test_params_migration.py openpilot/system/manager/test/test_manager.py
# exit 0; 363 passed, 1 skipped in 3.66s; no warnings

PATH="$PWD/.venv/bin:$PATH" python -m compileall -q bluepilot openpilot/selfdrive/ui/bp openpilot/sunnypilot
# exit 0; no output or import-compilation errors
```

The backend boolean checks were run through their direct-script entrypoints,
rather than relying on their earlier pytest collection behavior:

```bash
PATH="$PWD/.venv/bin:$PATH" python bluepilot/backend/test_backend_import.py
# exit 0; all eight import groups successful

PATH="$PWD/.venv/bin:$PATH" python bluepilot/backend/test_modules_only.py
# exit 0; Tests passed: 5; Tests failed: 0

PATH="$PWD/.venv/bin:$PATH" python /tmp/task5-fix1-portal-smoke.py
# GET http://127.0.0.1:57042/api/status -> 200
# PORTAL_SMOKE_PASS child_exit=0; process exit 0
```

The last command is a bounded, disposable `/tmp` harness, not a committed
repository test or durable repository artifact. It used the real HTTP server
and handler, a disposable Params root, a loopback ephemeral port, and only the
safe `GET /api/status` endpoint.

Focused Ford behavior was verified with:

```bash
PATH="$PWD/.venv/bin:$PATH" pytest -q \
  opendbc_repo/opendbc/sunnypilot/car/ford/tests/test_carstate_ext.py \
  opendbc_repo/opendbc/sunnypilot/car/ford/tests/test_lateral_angle_ext.py \
  opendbc_repo/opendbc/sunnypilot/car/ford/tests/test_lane_center_trim.py \
  opendbc_repo/opendbc/sunnypilot/car/ford/tests/test_vin_fingerprint.py \
  opendbc_repo/opendbc/car/ford/tests/test_ford.py
# exit 0; 56 passed, 16 subtests passed, 0 failed, 0 skipped in 0.84s
```

The full Ford safety suite is an inherited failure set. The following raw
capture blocks were each executed as a separate shell in the stated worktree.
They redirect both pytest streams first, save pytest's immediate exit code to a
sidecar before any normalization, then propagate that expected nonzero code to
the invoking shell:

```bash
PATH="$PWD/.venv/bin:$PATH" pytest -q -rfE opendbc_repo/opendbc/safety/tests/test_ford.py > /tmp/task5-fix1-original-safety-raw.txt 2>&1
pytest_exit=$?
printf '%s\n' "$pytest_exit" > /tmp/task5-fix1-original-safety-exit.txt
exit "$pytest_exit"
```

Executed in `/Users/alex/Apps/bluepilot-chestnut-personal`: exit `1`; `22759
failed, 474 passed, 285 skipped, 1756 subtests passed in 240.42s (0:04:00)`.

```bash
PATH="$PWD/.venv/bin:$PATH" pytest -q -rfE opendbc_repo/opendbc/safety/tests/test_ford.py > /tmp/task5-fix1-candidate-safety-raw.txt 2>&1
pytest_exit=$?
printf '%s\n' "$pytest_exit" > /tmp/task5-fix1-candidate-safety-exit.txt
exit "$pytest_exit"
```

Executed in `/Users/alex/Apps/bluepilot-chestnut-personal-2`: exit `1`;
`22759 failed, 474 passed, 285 skipped, 1756 subtests passed in 252.29s
(0:04:12)`.

```bash
sed -E 's/ in [0-9.]+s( \([0-9:]+\))?//' /tmp/task5-fix1-original-safety-raw.txt > /tmp/task5-fix1-original-safety-normalized.txt
sed -E 's/ in [0-9.]+s( \([0-9:]+\))?//' /tmp/task5-fix1-candidate-safety-raw.txt > /tmp/task5-fix1-candidate-safety-normalized.txt
diff -u /tmp/task5-fix1-original-safety-normalized.txt /tmp/task5-fix1-candidate-safety-normalized.txt
# exit 0; no output
```

The elapsed-time-only normalized failure text was byte-identical. This passes
the differential regression gate only; it is not an absolute Ford safety pass.
The `/tmp` capture and comparison files are ephemeral evidence, not durable
repository artifacts.

Task 6 ran exactly:

```bash
PATH="$PWD/.venv/bin:$PATH" scons -j4
```

SCons exited 0 and printed `scons: done building targets.` The complete log
contained 27 warning matches: one PWD diagnostic, 23 third-party acados Python
`SyntaxWarning`s, one CasADi supported-version warning, and two linker
warnings. These warnings are recorded, not waived. The build produced only
ignored/generated artifacts; no tracked source changes resulted.

## Closed installer gate and rollback

The live upstream snapshot was refreshed through BrowserOS neo on 2026-09-03:

- OpenPilot `master` is `3a13b67b6f92c0716616342f285165a215ab7900`.
- SunnyPilot `master` remains
  `e87dbbaba710bbfe7661d9ff064d46170cac9442`. PR #1974 is merged and PR
  #1965 remains open.
- SunnyPilot `staging-chestnut` remains
  `35ddbb199887b4048323c809ecff052e627a3bf5` and records source
  `47db84ebfb47f82bfe3ebb3d78cb13d4bc9a91a3`; `dev-chestnut` is
  `99114d2135f5ebfa3059601bef90cbd7d5f8d567` and records the same source.
- BluePilot `bp-dev` remains
  `501a7c0e911245044196fcc90cb077a69fa0749b`; `bp-7.0` remains
  `e1d051d7ba270261b4455068bd68f1a58db15a4a`.
- SunnyPilot PR #1986 is open. Its head
  `5b7ddce980a40cf025a6f34959c36b4b1454dd59` is one workflow-only commit on
  top of `e87dbbab` and changes three workflow YAML files to replace Hugging
  Face OAuth with a token.
- PR-head workflow run `33720345491` completed successfully: `build_big_model`,
  artifact creation, `upload_defaults`, and `Upload model to HF` all passed.
  Its `model-BMRLNAP-Model-v4-32` artifact is 734,268,714 bytes with digest
  `sha256:3c8c139b6df2014dcbac32b6ca3ea326808f13ceb216d62ebdc44c70d34ea7d6`.
  The workflow published `models/defaults/big/default_models.json` at
  `2026-09-03T06:00:38Z` and the
  `model-BMRLNAP-Model-v4-5b7ddce9-32` folder; all 18 chunk objects are
  publicly listed by the Hugging Face tree API. The generated default metadata
  records ref `5b7ddce9` because the workflow checkout was shallow.
- The public Chestnut runtime catalog
  `sunnypilot-models/gh-pages/docs/driving_models_chestnut_v23.json` still
  lists `BMRLNAP Model v4` dated 2026-08-30, ref `f877d7a0`, with 17 chunk
  hashes at the older `recompiled24` path. The earlier exact-`master` run
  `33706185619` had uploaded the byte-identical
  `model-BMRLNAP-Model-v4-e87dbbab-28` folder before it failed at the metadata
  upload step.

The successful PR-head run demonstrates that the artifact-publishing blocker
is fixed on the unmerged workflow branch and that its chunk objects are public.
It does not open the installer gate: PR #1986 is not merged, the runtime catalog
still points to its prior model tuple, and the staged source `47db84eb` still
does not match this branch's incorporated Sunny source `e87dbbab`. Do not
install this branch or treat it as a Sunny release artifact until one coherent,
reviewed source/staging/build/model tuple satisfies the complete gate.

The rollback heads are original personal `1f4ec371` and the BluePilot merge
source `501a7c0e`; the normal production rollback target remains the reviewed
`bp-dev` installer path. Device installation stays closed until a matching
reviewed Sunny artifact and all offroad, stationary, fallback, rollback, and
controlled vehicle-validation gates are completed. Host/build evidence is not
device or vehicle validation.

## Deliberately excluded work

No later OpenPilot changes, BluePilot-specific detector, parallel fallback,
or Ford steering/longitudinal/safety-limit change is included. Future upstream
work must arrive through a reviewed SunnyPilot sync rather than bypassing the
three-layer integration boundary.
