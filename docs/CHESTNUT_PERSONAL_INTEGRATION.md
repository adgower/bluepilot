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

Task 4 completed `git lfs pull` and `git lfs fsck` successfully. Sunny model
tests reported 53 passed, 1 skipped; `modeld_v2` reported 100 passed, 1
skipped. Six submodule pins are listed in the source tuple.

Task 5's exact Step 1 result after the test-only spawn-safe commit
`d3fdabbd` was 363 passed, 1 skipped, with no warnings. Backend direct scripts
passed (8 import groups and 5 module checks), and the real `GET /api/status`
portal smoke passed. Focused Ford verification reported 56 passed plus 16
subtests. The full Ford safety matrix is inherited and failing: 22,759 failed,
474 passed, 285 skipped, and 1,756 subtests. Its raw exit was 1 for both the
candidate and original `1f4ec371`; after elapsed-time-only normalization the
complete failure text was byte-identical. The differential gate passes; the
safety suite does not pass.

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

The current Sunny artifact snapshot remains unsuitable for installation:
development branch source `e87dbbab` does not match staging source `47db84eb`,
and workflow run `33706185619` failed at `Upload model to HF`. Do not install
this branch or treat it as a Sunny release artifact.

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
