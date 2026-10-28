<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Navigator 75 mph boundary correction

The local fix passes the full replay audit. The exact 75.111 mph discrepancy is resolved, and commands match the installed reference at or above 75 mph throughout the saved corpus. Nothing was integrated into the paired branches or changed on the Comma.

## Cause and correction

The previous 60–70 mph extension changed stored reduction history. Equal formulas above 75 mph therefore did not guarantee equal output. One recorded-context generated command encoded 0.0280 rad instead of the installed reference’s 0.0285 rad.

The new candidate continuously advances an independent copy of the installed controller. It preserves the previous prototype below 70 mph and fades back to that independent installed output from 70 to 75 mph. Final native slew remains enforced; any required handoff tail is explicitly reported. Neither controller overwrites the other’s internal history.

| Exact boundary frame, 75.111 mph at 1049.346243136 s | Before | After |
|---|---:|---:|
| Installed reference | 0.0285 rad | 0.0285 rad |
| Candidate | 0.0280 rad | 0.0285 rad |
| Wire difference | 0.0005 rad | 0 |

## Validation

- **122 focused tests pass.** The previous implementation failed four initial speed-crossing cases. Crossings now cover both directions and signs, invalid evidence, generation changes, override, disable/re-enable and reversal.
- **480 transition/abort cases, 172,800 frames pass** actual-output range, sign, cap, slew and settlement checks.
- **43 routes, 740 segments:** 4,289,417 controller updates per variant. There are 355 recorded-context and 783 separately labelled synthetic-fixture updates changed versus installed policy.
- **Zero changes at or above 75 mph** in either context. Default-off byte parity and unchanged below-5 / 25–60 mph behavior pass, including 40–50 mph.
- Native hooks accept 2,761,407 generated TX frames per variant, with two shared baseline cancel-message rejections per variant and **zero additional rejections**. RX-invalid parity, complete rejection receipts and source hashes pass.
- **All 13 original send-time native scenes pass**, with 235 encoded candidate-versus-installed packet changes and no added rejection. The separate 404 historical-recording-versus-installed-reference packet differences remain explicitly accounted for.
- All 13 send-time scenes preserve the prior prototype’s returned commands through 70 mph, including the saved 15 mph and 64 mph episodes. Differences from that prototype stay within the 70–75 mph fade.

Independent review caught and resolved stale diagnostics that described hidden extension output instead of the returned command. [Review](REVIEW.md), [design](DESIGN.md), [prototype](../../navigator-reference/PRIVATE_ARTIFACTS.md).

[Full acceptance](../../navigator-reference/PRIVATE_ARTIFACTS.md), [boundary receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md), [continuity receipt](../../navigator-reference/PRIVATE_ARTIFACTS.md), [protected source](../../navigator-reference/PRIVATE_ARTIFACTS.md).

The paired source stays clean at the original heads. **1.20/0.97**, geometry, pinion selection and native safety limits remain unchanged. No SSH, device settings, installation or firmware work occurred. Frozen-input replay establishes command behavior and native admission; it does not establish physical tracking improvement or closed-loop stability. This remains a report-local prototype requiring integration and hardware validation before release.
