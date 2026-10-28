<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Chestnut eGPU and big-model compatibility for BluePilot

**Research snapshot:** 2026-08-20 (America/Chicago)
**Latest refresh:** 2026-08-25 (America/Chicago)
**Scope:** comma.ai/openpilot, sunnypilot, and BluePilot primary sources only
**BluePilot code inspected:** `upstream/bp-7.0` at `e1d051d7ba270261b4455068bd68f1a58db15a4a` and `upstream/bp-dev` at `8eea9eb68e0c4126ee1c52f251e274d5865b6743`

## Executive answer

Chestnut support is not just “turn on the USB GPU flag.” BluePilot 7 already contains comma's earlier generic USB-GPU path, but it predates the production Chestnut firmware/updater, Chestnut-qualified detection, the 1B model artifact and release pipeline, Chestnut telemetry and failure handling, and sunnypilot's automatic big-model catalog/default selection.

The good news is that the architecture is now upstream-shaped:

- comma has shipped the production Chestnut stack on the dedicated [`release-chestnut`](https://github.com/commaai/openpilot/tree/release-chestnut) branch. Its August 17 tip is openpilot v0.11.2. The launch calls the model 1B parameters; the release notes give the more exact 880M figure, while retaining the 30x-parameter/100x-FLOP comparison with the on-device model. [comma Chestnut launch](https://blog.comma.ai/chestnut/), [release history](https://github.com/commaai/openpilot/commits/release-chestnut/), [v0.11.2 release notes](https://github.com/commaai/openpilot/blob/release-chestnut/RELEASES.md)
- sunnypilot merged its core adaptation as [PR #1894](https://github.com/sunnypilot/sunnypilot/pull/1894) on August 17, then merged model-build, artifact-fetch, default-model, and SunnyLink follow-ups in [#1922](https://github.com/sunnypilot/sunnypilot/pull/1922), [#1928](https://github.com/sunnypilot/sunnypilot/pull/1928), [#1929](https://github.com/sunnypilot/sunnypilot/pull/1929), and [#1931](https://github.com/sunnypilot/sunnypilot/pull/1931).
- it is **merged to sunnypilot `master`, but not yet in a tagged sunnypilot release**. The latest published release is [v2026.002.002](https://github.com/sunnypilot/sunnypilot/releases/tag/v2026.002.002), dated August 6, before the August 17 Chestnut merge.

The safest BluePilot route is therefore: integrate current/forthcoming sunnypilot into **`bp-dev`**, validate on comma four + Chestnut, and only then merge the result into `bp-7.0`. A hand-picked patch directly on `bp-7.0` is possible, but it is the higher-risk route because the production feature spans hardware management, schemas, build behavior, model runtime, model distribution, release tooling, and sunnypilot-specific selection logic.

## What Chestnut actually is

Chestnut is a USB-to-PCIe compute dock for **comma four**. The ready-to-drive kit currently includes Chestnut, an AMD Radeon RX 9060 8GB, a 3 m USB3 cable, vehicle power, and mounting hardware; the bare dock can use a user-supplied GPU and power supply. Both variants use the same open-source custom firmware. [comma shop and setup guide](https://comma.ai/shop/chestnut), [firmware repository](https://github.com/tinygrad/asm2464pd-firmware/)

The official product/software boundary is important:

- comma explicitly documents the in-car openpilot setup for comma four, not comma 3X. [launch post](https://blog.comma.ai/chestnut/), [product page](https://comma.ai/shop/chestnut)
- the production runtime is AMD-specific today: openpilot compiles the big path with tinygrad's `USB+AMD:LLVM` device and runs policy inference on `AMD`, while keeping camera warp work on QCOM. [openpilot model build source](https://github.com/commaai/openpilot/blob/master/openpilot/selfdrive/modeld/SConscript), [openpilot model runtime source](https://github.com/commaai/openpilot/blob/master/openpilot/selfdrive/modeld/modeld.py)
- the first official model is a new 1B-parameter “Chestnut class,” and comma says future autonomy effort will focus primarily on that larger class. [launch post](https://blog.comma.ai/chestnut/)
- the official `release-chestnut` software baseline selects **AGNOS 19.6**. BluePilot's AGNOS 18.5 is therefore outside the supported software path even if its Python changes are backported. [release-chestnut launcher](https://github.com/commaai/openpilot/blob/release-chestnut/launch_env.sh), [AGNOS 19.6 PR #38611](https://github.com/commaai/openpilot/pull/38611)

## The production openpilot stack

The openpilot work landed as a sequence, not one isolated commit:

0. **Base USB-GPU architecture.** [PR #37906](https://github.com/commaai/openpilot/pull/37906) introduced boot-time big-model compilation, separate QCOM/AMD device placement, chunked big artifacts, runtime/status params, the eGPU UI indicator, and release-build handling. [#38123](https://github.com/commaai/openpilot/pull/38123) preserved realtime pinning, while [#38273](https://github.com/commaai/openpilot/pull/38273) changed model loading to stream pickle protocol-5 out-of-band buffers instead of materializing all weights in RAM.

1. **Device identity and firmware lifecycle.** openpilot centralized Chestnut USB IDs/firmware identity, added production and ROM recovery flashing, added a newer USB VID, and fixed upgrades from older firmware. [new USB VID #38517](https://github.com/commaai/openpilot/commit/04847f3805fee671a1762d25cf72e26ab0ffead0), [production updater #38546](https://github.com/commaai/openpilot/commit/dd2214a78ccd932100d5987ef73196a7609645ca), [old-firmware flash fix #38639](https://github.com/commaai/openpilot/commit/5e3d17c72cf2cd90a57d1cd31771c3aacfc9f79b)

   The current source requires firmware/product string `custom ed4e39b7-CLEAN`, accepts runtime IDs `ADD1:0001` and `3801:0001`, and knows the ASM2464 ROM IDs used for recovery. Older launch-branch firmware hashes are superseded by this current value. [current USB definitions](https://github.com/commaai/openpilot/blob/master/openpilot/common/hardware/usb.py), [current detector](https://github.com/commaai/openpilot/blob/master/openpilot/selfdrive/modeld/helpers.py)

2. **Cold-start/link qualification.** Chestnut may enumerate before its PCIe link is usable, so build probing waits for link-up; later work sped that probe up. [probe-before-build #38540](https://github.com/commaai/openpilot/commit/a7f32be2fd7edd433b654138d21e558e0fce7da9), [faster probe #38596](https://github.com/commaai/openpilot/commit/855c99bf923aaf10b72e9938bc52dfe61f17cc65)

3. **Big-model build and release artifacts.** Release tooling gained Chestnut build scripts and a dedicated release branch, while source/build logic handled the big model and Git LFS edge cases. [release build scripts #38638](https://github.com/commaai/openpilot/commit/391132465d6d216e455d5bf81de695a244d3eef6), [release branch](https://github.com/commaai/openpilot/commit/7a76a50c4fb6619923fe826be2a14d51af342c08), [LFS guard revert #38670](https://github.com/commaai/openpilot/commit/03711a13b0a7740f28ac480b42da67a86ed1d1dd)

4. **Runtime observability and failure handling.** openpilot logs Chestnut state/metrics, samples ASM telemetry at 10 Hz, drops non-finite eGPU output, fails fast instead of hanging if telemetry wedges, and retains the small model for atomic runtime fallback. [state and metrics #38527](https://github.com/commaai/openpilot/commit/d86686fffda05d558a4c103ca835bb3da231b7a3), [more metrics #38550](https://github.com/commaai/openpilot/commit/5406aba1a25830a4c02d651e8706695bd14c6f68), [10 Hz ASM #38609](https://github.com/commaai/openpilot/commit/ad5afe222d543c59522906f0d2eae438d321bdb1), [non-finite guard #38556](https://github.com/commaai/openpilot/pull/38556), [hang hardening #38565](https://github.com/commaai/openpilot/commit/b755d32276a4934690e9e6f6f5824888245d582f), [current model runtime](https://github.com/commaai/openpilot/blob/master/openpilot/selfdrive/modeld/modeld.py)

5. **Release/channel guardrails.** Hardware detection can raise an offroad warning when the installed branch lacks the big model, and comma documented Chestnut-specific branches while the release path stabilized. [branch alert #38636](https://github.com/commaai/openpilot/commit/28560d6cf1b44f2f01c1dc0e6855a1fb64fd1e11), [branch documentation](https://github.com/commaai/openpilot/commit/6ad35321133fd0a7979dd85415be110d80ba582a)

6. **Operating-system baseline.** openpilot advanced through AGNOS 19 and then AGNOS 19.6; the shipped `release-chestnut` branch pins 19.6. [AGNOS 19 PR #38520](https://github.com/commaai/openpilot/pull/38520), [AGNOS 19.6 PR #38611](https://github.com/commaai/openpilot/pull/38611), [release-chestnut launcher](https://github.com/commaai/openpilot/blob/release-chestnut/launch_env.sh)

The shipped openpilot path is therefore a coherent tuple—comma four, Chestnut firmware, tested AMD GPU, big-model artifact, openpilot branch, and AGNOS—not a model-file swap.

## What sunnypilot has done

### Core runtime port

[sunnypilot PR #1894](https://github.com/sunnypilot/sunnypilot/pull/1894) merged 49 commits across 15 files (+424/-567) from `egpu-support` into `master`. It combines current openpilot Chestnut plumbing with sunnypilot's alternate `modeld_v2` and model publishing system.

The material sunnypilot behavior now is:

- `modeld_v2` calls the same production `usbgpu_present()` detector, runs the model on AMD while preserving QCOM camera warp, publishes `modelV2.big`, publishes `chestnutState`, exposes `UsbGpuLoading`/`UsbGpuActive`, and imposes a 60-second model-load timeout. [current `modeld_v2`](https://github.com/sunnypilot/sunnypilot/blob/b742557d62175872ea91723eb73a22b0849b8ae2/openpilot/sunnypilot/modeld_v2/modeld.py)
- compilation/build helpers wait for Chestnut PCIe link-up before compiling a USB model. [current compiler](https://github.com/sunnypilot/sunnypilot/blob/b742557d62175872ea91723eb73a22b0849b8ae2/openpilot/sunnypilot/modeld_v2/compile_modeld.py)
- the model fetcher automatically switches between the normal catalog and a separate USB-GPU catalog, with separate cache keys. [current fetcher](https://github.com/sunnypilot/sunnypilot/blob/b742557d62175872ea91723eb73a22b0849b8ae2/openpilot/sunnypilot/models/fetcher.py)
- the current USB-GPU catalog is `driving_models_usbgpu_v21.json`. It contains three 20 Hz, tinygrad, generation-12 choices—Lebowski, Tee Time, and TTTTFBRLM—each as 38 integrity-checked chunks. All three are currently marked `environment: development`, another reason not to describe this as a tagged stable sunnypilot release yet. [USB-GPU model catalog](https://raw.githubusercontent.com/sunnypilot/sunnypilot-models/refs/heads/gh-pages/docs/driving_models_usbgpu_v21.json)

### Follow-up work after the core merge

- [#1922](https://github.com/sunnypilot/sunnypilot/pull/1922) created a dedicated big-model CI runner/build path.
- [#1928](https://github.com/sunnypilot/sunnypilot/pull/1928) fixed CI so Git LFS fetches the actual ONNX rather than leaving a pointer.
- [#1929](https://github.com/sunnypilot/sunnypilot/pull/1929) added separate small/big defaults: `CD210` and `Lebowski`.
- [#1931](https://github.com/sunnypilot/sunnypilot/pull/1931) made SunnyLink advertise the correct default based on live USB-GPU presence.
- [#1927](https://github.com/sunnypilot/sunnypilot/pull/1927), a model-panel cache/navigation cleanup, was still open in the inspected snapshot; it is useful UI cleanup but is not the core Chestnut runtime.

### Readiness evidence and limits

PR #1894 was approved and merged with 19 of 20 checks passing. Its process replay reported 0 changed, 66 passed, and 0 errors, while its UI preview explicitly reported differences for MICI and big UI. That is useful regression evidence but is not the same as a documented comma-four/Chestnut road test. Also, current sunnypilot `modeld_v2` has non-finite-output and load-timeout guards, but unlike stock openpilot it does not visibly instantiate a small model for in-process eGPU fallback; a runtime failure raises and relies on process/system safety behavior. That difference needs deliberate device testing. [PR #1894 conversation/check evidence](https://github.com/sunnypilot/sunnypilot/pull/1894), [sunnypilot `modeld_v2`](https://github.com/sunnypilot/sunnypilot/blob/b742557d62175872ea91723eb73a22b0849b8ae2/openpilot/sunnypilot/modeld_v2/modeld.py), [stock openpilot runtime](https://github.com/commaai/openpilot/blob/master/openpilot/selfdrive/modeld/modeld.py)

There were no open sunnypilot PRs matching “chestnut” in the inspected snapshot; the only direct match was the merged #1894. However, the latest tagged sunnypilot release still predates it, and the model pipeline continued changing through #1931. Therefore the accurate status is **merged on master and still settling, not yet shipped in a tagged sunnypilot release**. [sunnypilot Chestnut PR search](https://github.com/sunnypilot/sunnypilot/pulls?q=is%3Apr+chestnut), [latest release](https://github.com/sunnypilot/sunnypilot/releases/latest), [master head](https://github.com/sunnypilot/sunnypilot/tree/master)

## Where BluePilot 7 is today

BluePilot `bp-7.0` identifies itself as sunnypilot `2026.002.000`, based on the June 10 sunnypilot sync, and its device launcher selects AGNOS 18.5. That is one major compatibility gap from the official Chestnut release's AGNOS 19.6. [BluePilot sunnypilot version](https://github.com/BluePilotDev/bluepilot/blob/e1d051d7ba270261b4455068bd68f1a58db15a4a/sunnypilot/common/version.h), [June sync commit](https://github.com/BluePilotDev/bluepilot/commit/668542771), [BluePilot AGNOS selection](https://github.com/BluePilotDev/bluepilot/blob/e1d051d7ba270261b4455068bd68f1a58db15a4a/launch_env.sh), [official Chestnut AGNOS selection](https://github.com/commaai/openpilot/blob/release-chestnut/launch_env.sh)

It already has an **experimental predecessor** of the final path:

- stock modeld can detect a hard-coded `0xADD1:0x0001` USB GPU, build a `big_` model, and run it through tinygrad. [BluePilot helper](https://github.com/BluePilotDev/bluepilot/blob/e1d051d7ba270261b4455068bd68f1a58db15a4a/selfdrive/modeld/helpers.py), [BluePilot stock model build](https://github.com/BluePilotDev/bluepilot/blob/e1d051d7ba270261b4455068bd68f1a58db15a4a/selfdrive/modeld/SConscript), [BluePilot stock runtime](https://github.com/BluePilotDev/bluepilot/blob/e1d051d7ba270261b4455068bd68f1a58db15a4a/selfdrive/modeld/modeld.py)
- the MICI home screen already has connected/compiled eGPU indicators. [BluePilot MICI home](https://github.com/BluePilotDev/bluepilot/blob/e1d051d7ba270261b4455068bd68f1a58db15a4a/selfdrive/ui/mici/layouts/home.py)

But it is not production Chestnut-compatible yet:

- detection is only the old hard-coded USB ID; it does not validate the production firmware product string or use the current Chestnut ID sets. [old BluePilot detector](https://github.com/BluePilotDev/bluepilot/blob/e1d051d7ba270261b4455068bd68f1a58db15a4a/selfdrive/modeld/helpers.py), [current upstream detector](https://github.com/sunnypilot/sunnypilot/blob/b742557d62175872ea91723eb73a22b0849b8ae2/openpilot/selfdrive/modeld/helpers.py)
- BluePilot `hardwared` has no Chestnut offroad updater/recovery flow or branch/model alert. [BluePilot hardwared](https://github.com/BluePilotDev/bluepilot/blob/e1d051d7ba270261b4455068bd68f1a58db15a4a/system/hardware/hardwared.py), [current upstream-derived hardwared](https://github.com/sunnypilot/sunnypilot/blob/b742557d62175872ea91723eb73a22b0849b8ae2/openpilot/system/hardware/hardwared.py)
- BluePilot's sunnypilot model catalog is still the single `driving_models_v17.json`; it cannot switch to the dedicated USB-GPU v21 catalog. [BluePilot fetcher](https://github.com/BluePilotDev/bluepilot/blob/e1d051d7ba270261b4455068bd68f1a58db15a4a/sunnypilot/models/fetcher.py), [current sunnypilot fetcher](https://github.com/sunnypilot/sunnypilot/blob/b742557d62175872ea91723eb73a22b0849b8ae2/openpilot/sunnypilot/models/fetcher.py)
- BluePilot's `modeld_v2` only enables AMD when a `USBGPU` environment variable is manually present. It lacks automatic Chestnut detection, active/loading params, 60-second load protection, `modelV2.big`, and Chestnut telemetry. [BluePilot `modeld_v2`](https://github.com/BluePilotDev/bluepilot/blob/e1d051d7ba270261b4455068bd68f1a58db15a4a/sunnypilot/modeld_v2/modeld.py), [current sunnypilot `modeld_v2`](https://github.com/sunnypilot/sunnypilot/blob/b742557d62175872ea91723eb73a22b0849b8ae2/openpilot/sunnypilot/modeld_v2/modeld.py)
- BluePilot has only one default model name (`CD210`), not the USB-aware `Lebowski` default and SunnyLink resolver. [BluePilot default](https://github.com/BluePilotDev/bluepilot/blob/e1d051d7ba270261b4455068bd68f1a58db15a4a/sunnypilot/models/model_name.py), [sunnypilot #1929](https://github.com/sunnypilot/sunnypilot/pull/1929), [sunnypilot #1931](https://github.com/sunnypilot/sunnypilot/pull/1931)
- its old big artifact contract is split into `big_driving_vision.onnx` (296,203,378 bytes) and `big_driving_on_policy.onnx` (14,061,419 bytes), roughly 310 MB combined. Current openpilot uses one `big_driving_supercombo.onnx` shown by GitHub as 1.64 GB (1,757,355,221 bytes). The compiler/model contract is therefore materially different, not just a new model name. [BluePilot big vision](https://github.com/BluePilotDev/bluepilot/blob/e1d051d7ba270261b4455068bd68f1a58db15a4a/selfdrive/modeld/models/big_driving_vision.onnx), [BluePilot big policy](https://github.com/BluePilotDev/bluepilot/blob/e1d051d7ba270261b4455068bd68f1a58db15a4a/selfdrive/modeld/models/big_driving_on_policy.onnx), [current big supercombo](https://github.com/commaai/openpilot/blob/master/openpilot/selfdrive/modeld/models/big_driving_supercombo.onnx)

The relevant BluePilot model/hardware files show no fork-specific changes after the June upstream sync, which is encouraging for a future upstream merge. The complication is broader: current sunnypilot has since adopted the `openpilot/` source-root layout and many additional upstream changes, so importing current master is a real upstream synchronization, not a tiny isolated cherry-pick. [BluePilot June sync](https://github.com/BluePilotDev/bluepilot/commit/668542771), [current sunnypilot tree](https://github.com/sunnypilot/sunnypilot/tree/b742557d62175872ea91723eb73a22b0849b8ae2)

## Recommended integration strategy

### Preferred: upstream-first integration on `bp-dev`

1. **Wait for or select a fixed sunnypilot baseline.** Best is the first tagged sunnypilot release containing #1894, #1922, #1928, #1929, and #1931. If experimentation cannot wait, pin exact `master` SHA `b742557d62175872ea91723eb73a22b0849b8ae2` rather than following a moving branch. [sunnypilot master snapshot](https://github.com/sunnypilot/sunnypilot/commit/b742557d62175872ea91723eb73a22b0849b8ae2)

2. **Integrate into a branch based on BluePilot `bp-dev`, not directly into `bp-7.0`.** `bp-dev` is where BluePilot's current development already lives; the release branch should receive the result after device validation. [BluePilot `bp-dev`](https://github.com/BluePilotDev/bluepilot/tree/bp-dev), [BluePilot `bp-7.0`](https://github.com/BluePilotDev/bluepilot/tree/bp-7.0)

3. **Treat the sunnypilot sync as the source of truth.** Preserve BluePilot's documented three-layer extension seams, then reapply only BluePilot-specific wiring/comments where the new upstream layout conflicts. Do not independently reinvent the model catalog or `modeld_v2` Chestnut path after sunnypilot has already done that work.

4. **Audit the end-to-end contract, not only compilation.** The minimum coherent surface is:

   - Chestnut USB IDs, product-string qualification, ROM recovery, firmware payload and flasher;
   - AGNOS 19.6 and its GPU/USB firmware/runtime prerequisites;
   - `hardwared` updater and offroad alert;
   - cereal/service/device-state Chestnut telemetry;
   - stock modeld helper/build/runtime changes;
   - sunnypilot `modeld_v2` runtime;
   - model manager's USB-GPU catalog and separate caches;
   - `CD210`/`Lebowski` default resolver and SunnyLink metadata;
   - release/model CI only if BluePilot will publish its own compiled model artifacts.

5. **Keep BluePilot control changes out of the first bring-up.** Chestnut changes inference compute/model output, not Ford angle-mode tuning. Validate the same Ford car/controller behavior with the small model first, then switch only the compute/model dimension.

   In particular, freeze the user's current `FordHighSpeedFactor_ang=1.25` and `FordLowSpeedFactor_ang=1.29` for the initial A/B. A larger model can produce a different path even with identical controller factors, so compare small versus big on the same routes before retuning either factor; changing model and tuning together would make the result uninterpretable.

### Faster but riskier: bounded backport to the old layout

A backport can avoid the repository-root migration, but it must port the whole contract above. PR #1894 alone is insufficient because its follow-up PRs fixed artifact generation, LFS retrieval, defaults, and SunnyLink resolution. The old BluePilot stock model path also expects split `big_driving_vision`/`big_driving_on_policy` inputs, while the current upstream release path uses a big `driving_supercombo`; mixing the old compiler assumptions with the new artifact is unsafe. [BluePilot build source](https://github.com/BluePilotDev/bluepilot/blob/e1d051d7ba270261b4455068bd68f1a58db15a4a/selfdrive/modeld/SConscript), [current upstream build source](https://github.com/sunnypilot/sunnypilot/blob/b742557d62175872ea91723eb73a22b0849b8ae2/openpilot/selfdrive/modeld/SConscript)

Use this route only for an explicitly experimental branch, never as a quick edit to the release branch.

## Validation gate before calling it compatible

The following evidence should be required on a comma four with the intended Chestnut/GPU/power setup:

1. **Offroad hardware lifecycle**

   - cold boot with Chestnut unpowered, late-powered, and already powered;
   - production and ROM USB IDs detected;
   - firmware mismatch flashed offroad, then exact current product string verified;
   - PCIe link-up probe succeeds across repeated 12 V power cycles;
   - branch/model-missing alert appears and clears correctly.

2. **Model distribution**

   - normal device receives the normal catalog;
   - Chestnut receives `driving_models_usbgpu_v21.json` and a separate cache;
   - Lebowski's 38 chunks download, hash-verify, survive reboot, and are not accidentally removed by cache cleanup;
   - unplugging Chestnut returns model selection/catalog state to the supported small-model path while offroad.

3. **Runtime**

   - `modeld_tinygrad` starts within the 60-second limit;
   - `UsbGpuLoading`, `UsbGpuActive`, `modelV2.big`, and `chestnutState` transition correctly;
   - model frequency, dropped frames, execution latency, thermals, GPU power, and GPU memory stay within upstream behavior;
   - stock modeld's small-model fallback works on an induced eGPU failure;
   - sunnypilot `modeld_v2` failure/restart behavior is explicitly tested and does not leave controls consuming stale model output.

4. **BluePilot/Ford regression**

   - stock small model on comma four;
   - Chestnut big model on comma four;
   - BluePilot angle mode and curvature mode with identical vehicle/tuning configuration;
   - on-policy/off-policy/split-model choices that remain supported by the new catalog;
   - C3X/MICI builds and UI remain functional even though Chestnut is officially a comma-four product.

5. **Build/release**

   - full C4 release build from a clean checkout with real LFS model assets;
   - relevant unit tests plus sunnypilot process replay;
   - device cold-build and warm-build;
   - exact branch, commit, AGNOS, Chestnut firmware, tinygrad commit, model ref/hash, and GPU recorded in the test report.

## Decision

The project is ready for a **BluePilot integration spike**, but not for declaring `bp-7.0` Chestnut-compatible today. The right next engineering step is an isolated `bp-dev` upstream-sync branch pinned to a fixed sunnypilot commit (or preferably the first tagged Chestnut release), followed by source-level conflict mapping and device bring-up. No production code, checkout, or working branch was changed during this research. A read-only tracking ref, `research/sunnypilot-master`, was fetched at `b742557d62175872ea91723eb73a22b0849b8ae2` so the comparison is reproducible; the report itself is the only working-tree file added.

## Refresh — 2026-08-25 (America/Chicago)

This is a live primary-source refresh of the 2026-08-20 snapshot above. Repository pages were checked on 2026-08-25 through GitHub; no device, release build, artifact download, or road test was performed. Consequently, the facts below establish source/release state, not working hardware compatibility.

### Exact current heads and releases

- comma `master` is [`084747c75d2cbd23af65ab7a9e770bbd7b98bac9`](https://github.com/commaai/openpilot/commit/084747c75d2cbd23af65ab7a9e770bbd7b98bac9), dated August 21. The inspected head change is UI-only; it does not replace the Chestnut production work recorded above. [`master`](https://github.com/commaai/openpilot/tree/master)
- The dedicated comma production branch remains [`release-chestnut`](https://github.com/commaai/openpilot/tree/release-chestnut) at [`473eba53f280743d09c5bebc2d0613ea46883e02`](https://github.com/commaai/openpilot/commit/473eba53f280743d09c5bebc2d0613ea46883e02), labelled **openpilot v0.11.2**, dated August 17. It is one commit ahead of `master` and intentionally does not track subsequent master history. Important qualification: GitHub's public Releases page still lists v0.11.1 as its latest public release, so this is a frozen dedicated release branch, not a newly published general release. It remains the clearest source-level Chestnut tuple, including the already-documented AGNOS 19.6 requirement. [release history](https://github.com/commaai/openpilot/commits/release-chestnut/), [public releases](https://github.com/commaai/openpilot/releases)
- sunnypilot `master` has advanced from the former comparison snapshot [`b742557d62175872ea91723eb73a22b0849b8ae2`](https://github.com/sunnypilot/sunnypilot/commit/b742557d62175872ea91723eb73a22b0849b8ae2) to [`25c25047b890337059f3a6727c1525c49dca2b10`](https://github.com/sunnypilot/sunnypilot/commit/25c25047b890337059f3a6727c1525c49dca2b10), dated August 25 (the comparison reports 38 intervening commits). A staging tag, [`staging/2026.003.000/2026.08.25-4792`](https://github.com/sunnypilot/sunnypilot/releases/tag/staging%2F2026.003.000%2F2026.08.25-4792), points to that head, but the latest formal release remains [`v2026.002.002`](https://github.com/sunnypilot/sunnypilot/releases/tag/v2026.002.002), [`c440933a65fa2c669a9926c8112ae352d3600f07`](https://github.com/sunnypilot/sunnypilot/commit/c440933a65fa2c669a9926c8112ae352d3600f07), released August 7. Thus **the Chestnut work is staging/master-only, not a tagged formal sunnypilot release**. [`master`](https://github.com/sunnypilot/sunnypilot/tree/master), [releases](https://github.com/sunnypilot/sunnypilot/releases)
- BluePilot `bp-dev` is [`5f17cf389b1a48b09185a732564db11bd6477b58`](https://github.com/BluePilotDev/bluepilot/commit/5f17cf389b1a48b09185a732564db11bd6477b58), August 24; `bp-7.0` remains [`e1d051d7ba270261b4455068bd68f1a58db15a4a`](https://github.com/BluePilotDev/bluepilot/commit/e1d051d7ba270261b4455068bd68f1a58db15a4a), August 16. `bp-7.0` is 10 commits ahead and 16 behind `bp-dev`. [`bp-dev`](https://github.com/BluePilotDev/bluepilot/tree/bp-dev), [`bp-7.0`](https://github.com/BluePilotDev/bluepilot/tree/bp-7.0)

### What changed since `b742557`

sunnypilot is now actively closing the integration seams that were still hypothetical in the earlier snapshot:

- [`#1935`](https://github.com/sunnypilot/sunnypilot/pull/1935) adds Chestnut prebuilt CI branches and [`#1936`](https://github.com/sunnypilot/sunnypilot/pull/1936) carries Chestnut offroad-warning branch metadata. [`#1943`](https://github.com/sunnypilot/sunnypilot/pull/1943) adds a big-model list when Chestnut is present, and [`#1948`](https://github.com/sunnypilot/sunnypilot/pull/1948) relaxes device detection. These are material end-to-end follow-ups beyond the former resolver-only baseline.
- [`#1957`](https://github.com/sunnypilot/sunnypilot/commit/2ba91d2be5cc91813762ffe6af3243728e7799ed) adds a tinygrad-reference check to `prepare_chestnut` and speeds its prebuilt stages; [`19f83b2`](https://github.com/sunnypilot/sunnypilot/commit/19f83b274fceeaa56ec5090d0497046d604be027) makes the Chestnut prebuilt publish environment match. These are useful release/CI hardening signals, but do not prove BluePilot can publish or consume the artifacts.
- [`#1959`](https://github.com/sunnypilot/sunnypilot/commit/cefe5737b9b201af26eafc0c4d426e7e15ecdd4c) fixes the current model not updating when Chestnut status changes; [`#1960`](https://github.com/sunnypilot/sunnypilot/commit/25c25047b890337059f3a6727c1525c49dca2b10) persists model selection per catalog across that transition. Together they reduce a real plug/unplug/catalog-selection gap in the model-manager path.
- [`#1934`](https://github.com/sunnypilot/sunnypilot/commit/45814e331381c2c132912fae0807cfb783bec0a2) adds `modeld_v2` spatial features, and [`#1958`](https://github.com/sunnypilot/sunnypilot/commit/760c19d3f91f79e404f36b020c5df027a5291e48) hardens model-cache size calculation when files disappear. They are current runtime/catalog churn adjacent to, rather than a replacement for, the core Chestnut port.

The current open-PR searches return **zero** sunnypilot PRs matching `chestnut`, `modeld_v2`, or `catalog`; the matching work is merged/closed. This does not mean the repository has no other open PRs. [Chestnut](https://github.com/sunnypilot/sunnypilot/pulls?q=is%3Apr+chestnut+is%3Aopen), [modeld_v2](https://github.com/sunnypilot/sunnypilot/pulls?q=is%3Apr+modeld_v2+is%3Aopen), [catalog](https://github.com/sunnypilot/sunnypilot/pulls?q=is%3Apr+catalog+is%3Aopen)

One important runtime difference remains at current sunnypilot master `25c2504`. Stock openpilot loads a small model if the big model fails or exceeds its startup timeout, and it switches to that already-loaded small model after an eGPU runtime exception. sunnypilot's alternate `modeld_v2` still raises `RuntimeError` after a 60-second eGPU load failure and does not instantiate an in-process small-model fallback. BluePilot should therefore bring up the stock modeld path first or add and validate equivalent fallback behavior before treating `modeld_v2` as release-ready. [stock fallback](https://github.com/sunnypilot/sunnypilot/blob/25c25047b890337059f3a6727c1525c49dca2b10/openpilot/selfdrive/modeld/modeld.py), [current `modeld_v2`](https://github.com/sunnypilot/sunnypilot/blob/25c25047b890337059f3a6727c1525c49dca2b10/openpilot/sunnypilot/modeld_v2/modeld.py)

### BluePilot status and revised readiness call

No BluePilot pull request—open or closed—matches `chestnut`, and the August 20–25 `bp-dev` history contains unrelated `.gitattributes`, comm-issue, and Ford reverse-to-drive changes rather than an upstream Chestnut import. [BluePilot Chestnut PR search](https://github.com/BluePilotDev/bluepilot/pulls?q=is%3Apr+chestnut), [recent `bp-dev` history](https://github.com/BluePilotDev/bluepilot/commits/bp-dev?since=2026-08-20&until=2026-08-26) Therefore no production Chestnut support has landed in either `bp-dev` or `bp-7.0` as of this refresh; the old experimental USB-GPU precursor and all gaps documented above remain the applicable BluePilot evidence.

The integration recommendation is now stronger but unchanged in direction: baseline an experimental BluePilot sync on **current sunnypilot `25c2504` or a future tag that contains it**, rather than the stale `b742557` snapshot. Include the post-snapshot `prepare_chestnut`/prebuilt CI work and the catalog-transition fixes in the conflict map. Do not label it compatible until the device validation gate above has been executed on a comma four, actual Chestnut firmware, supported AMD GPU/power setup, and AGNOS 19.6-equivalent base.

### Evidence limits

GitHub branch comparisons are time-sensitive and report source topology, not binary provenance. The release page verifies that sunnypilot has not tagged the master changes, but it cannot prove a downstream installer has not carried an equivalent patch. Likewise, text/PR searches can establish that no PR title/body matches `chestnut`; they cannot rule out an unlabelled or private downstream implementation. This refresh did not inspect private CI logs, artifacts, USB firmware on hardware, LFS contents, or an on-road safety outcome.

## Refresh — 2026-08-27 (America/Chicago)

This refresh used BrowserClaw against GitHub primary sources and then the locally refreshed read-only refs for sunnypilot and BluePilot. The openpilot fetch remained stalled, so openpilot statements below are live GitHub evidence rather than local-ref evidence. No branch or checkout was changed. This remains source/release evidence only; it is not a device, artifact, build, or road-test result.

### Heads, channels, and BluePilot delta

- comma `master` is [`4a13639cfd122ccb9113a4d6ce225dcbd8e61914`](https://github.com/commaai/openpilot/commit/4a13639cfd122ccb9113a4d6ce225dcbd8e61914), August 27, `reduce chestnut states` ([#38705](https://github.com/commaai/openpilot/pull/38705)). The public formal GitHub release is still [`v0.11.1`](https://github.com/commaai/openpilot/releases/tag/v0.11.1), published June 5; `release-chestnut` remains [`473eba53f280743d09c5bebc2d0613ea46883e02`](https://github.com/commaai/openpilot/commit/473eba53f280743d09c5bebc2d0613ea46883e02). Thus the Chestnut line is still ahead of comma's latest formal GitHub release.
- sunnypilot `master` is [`4075befc5e5fea9a4fc1e68eaa23ca5bbd01824f`](https://github.com/sunnypilot/sunnypilot/commit/4075befc5e5fea9a4fc1e68eaa23ca5bbd01824f), August 27. The refreshed local `research/sunnypilot-master` ref resolves to that exact SHA. Its latest formal release is still [`v2026.002.002`](https://github.com/sunnypilot/sunnypilot/releases/tag/v2026.002.002), published August 7. The current staging tag [`staging/2026.003.000/2026.08.27-4808`](https://github.com/sunnypilot/sunnypilot/releases/tag/staging%2F2026.003.000%2F2026.08.27-4808) resolves to [`9f43d2477d29198f21e528c50cc2a7b20ba82f23`](https://github.com/sunnypilot/sunnypilot/commit/9f43d2477d29198f21e528c50cc2a7b20ba82f23), immediately before the master head; the Chestnut-specific build heads are [`dev-chestnut` `8cc25a2b8b240ba71ca4e56c324ad35fd1cd9c47`](https://github.com/sunnypilot/sunnypilot/commit/8cc25a2b8b240ba71ca4e56c324ad35fd1cd9c47) and [`staging-chestnut` `9e963772ee6e413ac4cd5dd1d37e13aa0dcf0329`](https://github.com/sunnypilot/sunnypilot/commit/9e963772ee6e413ac4cd5dd1d37e13aa0dcf0329). They are staging/build channels, not formal releases.
- Ref refresh confirms BluePilot `upstream/bp-dev` remains [`5f17cf389b1a48b09185a732564db11bd6477b58`](https://github.com/BluePilotDev/bluepilot/commit/5f17cf389b1a48b09185a732564db11bd6477b58), August 24, and `upstream/bp-7.0` remains [`e1d051d7ba270261b4455068bd68f1a58db15a4a`](https://github.com/BluePilotDev/bluepilot/commit/e1d051d7ba270261b4455068bd68f1a58db15a4a), August 16. Neither branch has a commit since August 25, and GitHub searches still show no BluePilot Chestnut PR/commit. No BluePilot production-support delta has landed.

### Material changes since August 25

- comma merged [#38700](https://github.com/commaai/openpilot/pull/38700) ([`d40df6f`](https://github.com/commaai/openpilot/commit/d40df6f829c18bf17ae2e4a825220778e2780e98)): invalid/non-finite big-model output now reaches the stock modeld fallback path. It then merged [#38703](https://github.com/commaai/openpilot/pull/38703) ([`5cfdb2f`](https://github.com/commaai/openpilot/commit/5cfdb2f4dac82ba89ebf310db13ff08d49cf4916)) to rename eGPU/`usbgpu` interfaces to Chestnut, [#38704](https://github.com/commaai/openpilot/pull/38704) ([`fa75fdd`](https://github.com/commaai/openpilot/commit/fa75fdd852d29eedf454afdcfa76c34451ada8e9)) for telemetry/GPU-work overlap, and [#38705](https://github.com/commaai/openpilot/pull/38705) for unified status presentation. [#38706](https://github.com/commaai/openpilot/pull/38706), Chestnut offroad alerts, remains open in this snapshot.
- sunnypilot merged [#1966](https://github.com/sunnypilot/sunnypilot/pull/1966), [`da28afc`](https://github.com/sunnypilot/sunnypilot/commit/da28afca91a1ec0e5919a483d99508512886105c), a ref-based dual-slot QCOM/USB-GPU model backend. Its UI now exposes Chestnut presence via [#1968](https://github.com/sunnypilot/sunnypilot/pull/1968), [`1d4558c`](https://github.com/sunnypilot/sunnypilot/commit/1d4558c067bde1cfab37c6f865eb9ddf8f1098d7), and uses full big-model failure detection for those indicators in [#1969](https://github.com/sunnypilot/sunnypilot/pull/1969), [`15f201c`](https://github.com/sunnypilot/sunnypilot/commit/15f201caeddcf331ab4ff5f2b909ba0f28c3eeee). The broader Model Selector work in [#1953](https://github.com/sunnypilot/sunnypilot/pull/1953), [`2d6cc4c`](https://github.com/sunnypilot/sunnypilot/commit/2d6cc4c065c4d1833dc267fff60ebae48b444817), now represents the small/big slots explicitly. This is important model-management progress, but it does not by itself make BluePilot compatible.

### `modeld_v2` fallback answer

**No:** current SunnyPilot `modeld_v2` still does not have stock-style, in-process small-model fallback. At current master, it creates one eGPU model when Chestnut is present, waits 60 seconds, then raises `RuntimeError` if the load did not produce a model; its non-finite output handling drops the frame. It does not create a small `ModelState` alongside the big model or switch to one after a big-model exception. [current SunnyPilot `modeld_v2`](https://github.com/sunnypilot/sunnypilot/blob/4075befc5e5fea9a4fc1e68eaa23ca5bbd01824f/openpilot/sunnypilot/modeld_v2/modeld.py)

This contrasts with stock comma modeld: it preloads `small_model` whenever Chestnut is selected, uses it if big-model startup fails, and swaps to it after a runtime big-model exception. [current stock `modeld`](https://github.com/commaai/openpilot/blob/4a13639cfd122ccb9113a4d6ce225dcbd8e61914/openpilot/selfdrive/modeld/modeld.py) SunnyPilot [#1965](https://github.com/sunnypilot/sunnypilot/pull/1965) is open and provides retry-only protection for AMD-over-USB contention; its author explicitly records that the earlier built-in fallback was removed during review. It therefore cannot be counted as equivalent fallback behavior.

### Updated decision

Upstream capability is advancing rapidly, but the compatibility conclusion is unchanged and sharper: BluePilot has **no new Chestnut integration**; SunnyPilot staging now has a stronger two-slot catalog/build/UI path; and the alternate `modeld_v2` safety behavior still lags stock modeld's in-process fallback. A BluePilot spike should pin a selected SunnyPilot staging/build SHA, port the entire hardware/runtime/catalog/CI contract, and explicitly validate both big-model failure and the desired small-model recovery before any compatibility claim. Keep the existing comma-four, AGNOS, firmware, artifact, C3X/MICI, and Ford-regression gates above.

## Refresh — 2026-08-28 (America/Chicago)

This is a live GitHub-primary-source refresh. It does not change any branch or production code, and it remains source/release evidence rather than a hardware, artifact, build, or road-test result.

### Exact heads and release channels

- comma `master` is [`30f358eb59c191cb6ca98b4ee79e17e5b9b82b63`](https://github.com/commaai/openpilot/commit/30f358eb59c191cb6ca98b4ee79e17e5b9b82b63), August 28; its head is unrelated Cabana work. `nightly` is [`3e30ed40eb4895c746a86af8e744b40b97d4c5ed`](https://github.com/commaai/openpilot/commit/3e30ed40eb4895c746a86af8e744b40b97d4c5ed), and the fixed `release-chestnut` branch remains [`473eba53f280743d09c5bebc2d0613ea46883e02`](https://github.com/commaai/openpilot/commit/473eba53f280743d09c5bebc2d0613ea46883e02). The latest formal GitHub release is still [`v0.11.1`](https://github.com/commaai/openpilot/releases/tag/v0.11.1), published June 5.
- sunnypilot `master` remains [`4075befc5e5fea9a4fc1e68eaa23ca5bbd01824f`](https://github.com/sunnypilot/sunnypilot/commit/4075befc5e5fea9a4fc1e68eaa23ca5bbd01824f), August 27. `staging-chestnut` has advanced to [`6abbc1745df9737f149cce17feccabe0e2b0be45`](https://github.com/sunnypilot/sunnypilot/commit/6abbc1745df9737f149cce17feccabe0e2b0be45), while `dev-chestnut` remains [`8cc25a2b8b240ba71ca4e56c324ad35fd1cd9c47`](https://github.com/sunnypilot/sunnypilot/commit/8cc25a2b8b240ba71ca4e56c324ad35fd1cd9c47). The latest formal release is still [`v2026.002.002`](https://github.com/sunnypilot/sunnypilot/releases/tag/v2026.002.002), published August 7; the Chestnut branches are staging/build channels, not formal releases.
- BluePilot `bp-dev` remains [`5f17cf389b1a48b09185a732564db11bd6477b58`](https://github.com/BluePilotDev/bluepilot/commit/5f17cf389b1a48b09185a732564db11bd6477b58) and `bp-7.0` [`e1d051d7ba270261b4455068bd68f1a58db15a4a`](https://github.com/BluePilotDev/bluepilot/commit/e1d051d7ba270261b4455068bd68f1a58db15a4a). BluePilot has no GitHub releases and no matching Chestnut commits or PRs. [commit search](https://github.com/BluePilotDev/bluepilot/search?q=chestnut&type=commits), [PR search](https://github.com/BluePilotDev/bluepilot/search?q=chestnut&type=pullrequests)

### Openpilot’s naming/state cleanup and follow-ups

[#38703](https://github.com/commaai/openpilot/pull/38703), merged as [`5cfdb2f`](https://github.com/commaai/openpilot/commit/5cfdb2f4dac82ba89ebf310db13ff08d49cf4916), made the code-facing term **Chestnut** rather than the generic eGPU/`usbgpu`. In particular it renamed:

- params `UsbGpuActive`/`UsbGpuLoading` to `ChestnutActive`/`ChestnutLoading`;
- model helpers `usbgpu_present()`/`usbgpu_compiled()` to `chestnut_present()`/`chestnut_compiled()`, their Boolean argument and JSON device key to `chestnut`, and the build lock to `.chestnut.lock`;
- modeld's `USBGPU`/`ModelState.usbgpu`/UI-state fields to `CHESTNUT`/`ModelState.chestnut`/`chestnut_*` while retaining the same AMD big-model contract and preloaded-small-model fallback; and
- MICI asset and renderer names from `egpu*.png`/`_egpu_*` to `chestnut*.png`/`_chestnut_*`.

The exact file-level patch is the authoritative inventory. [#38703 changed files](https://github.com/commaai/openpilot/pull/38703/files)

[#38706](https://github.com/commaai/openpilot/pull/38706), `add chestnut offroad alerts`, is **still open** as of this refresh, so it cannot be treated as mainline support. A post-August-27 mainline follow-up did land: [#38711](https://github.com/commaai/openpilot/pull/38711), [`4cdc160`](https://github.com/commaai/openpilot/commit/4cdc16031ffd8bd44cb1d3f2fd2bfd49effd66ce), logs Chestnut supply fault. The mainline history also retains the immediately preceding state reduction ([#38705](https://github.com/commaai/openpilot/pull/38705)) and telemetry/GPU-work consolidation ([#38704](https://github.com/commaai/openpilot/pull/38704)).

### SunnyPilot status: not yet a naming/fallback parity port

SunnyPilot has absorbed the **user-facing model-state direction**—its merged [#1953](https://github.com/sunnypilot/sunnypilot/pull/1953) reports distinct small/big slots and a big-to-small failover state in the picker—but `master` has not absorbed stock openpilot's code/API naming cleanup into the alternate runtime. Current [`modeld_v2`](https://github.com/sunnypilot/sunnypilot/blob/4075befc5e5fea9a4fc1e68eaa23ca5bbd01824f/openpilot/sunnypilot/modeld_v2/modeld.py) still imports `usbgpu_present`, constructs `ModelState(..., usbgpu=True)`, and writes `UsbGpuLoading`/`UsbGpuActive`.

The open upstream-sync [#1973](https://github.com/sunnypilot/sunnypilot/pull/1973) is the pending bridge. It is currently clean/mergeable and carries the rename through 40 changed files, including SunnyPilot's build workflows, `modeld_v2`, model-manager source names and cache keys, UI state, SunnyLink telemetry, and a migration from `ModelManager_ActiveBundleUSBGPU` to `ModelManager_ActiveBundleChestnut`. It targets comma ref `4a13639`, so it includes #38703/#38705 but predates the still-open #38706 and merged #38711. Until #1973 merges, Sunny `master` is not source-name/state parity with #38703; after it merges, downstreams must port the migration and Sunny-specific rename work as one contract rather than cherry-picking only the stock openpilot files.

SunnyPilot [#1965](https://github.com/sunnypilot/sunnypilot/pull/1965) remains **open**, not merged. It retries only `am_usb` lock-contention failures (up to five retries) and explicitly says its earlier built-in fallback was removed in review. The current source still raises after a failed or timed-out eGPU load and does not instantiate a small `ModelState` alongside the big model. #1973 gives SunnyPilot's **default/stock modeld runner** the upstream fallback, but its own model-picker text and `modeld_v2` patch confirm that a custom big model still has no automatic fallback. The public PR search produces no new actual `modeld_v2` small-model fallback implementation; #1965 is the matching result and documents that the proper fallback is still being developed. [fallback PR search](https://github.com/sunnypilot/sunnypilot/search?q=small+model+fallback&type=pullrequests), [failure evidence #1963](https://github.com/sunnypilot/sunnypilot/issues/1963)

### Conclusion

There is no new BluePilot Chestnut delivery. The practical integration delta has increased: port the upstream Chestnut naming/state contract deliberately, rather than mixing `Chestnut*` stock params with SunnyPilot `UsbGpu*` `modeld_v2` behavior; preserve the stock in-process small-model fallback as an explicit safety requirement; and do not treat #38706 or #1965 as shipped capabilities until their merge state changes and the device gate is executed.
