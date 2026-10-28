<!-- Public reference export: local identifiers/paths/times may be redacted; supporting private artifacts are intentionally omitted. -->
# Comma four migration recovery assessment

Reviewed October 14, 2026 on the Mac. Research only: no SSH, device probes, OS commands, firmware utilities, resets or flashes were run for this report. Candidate source is openpilot `6ae31161b73de2ce5043f708569759ac5f55f283`; installed AGNOS 19.7/slot A and Chestnut `ed4e39b7` are supplied by the separate inventory, not reverified here.

## Decision

Staging an inert checkout separately is compatible with the current no-update instruction. Activating it is not: the candidate requires AGNOS 19.9 and Chestnut `8516b768`, and its normal startup includes automatic OS/Panda/Chestnut update paths. Do not invoke its launcher, manager, hardwared, pandad, AGNOS updater or firmware scripts during staging. Do not replace `/data/openpilot`, `/data/pythonpath`, service targets or boot links yet. The application update pause is not an OS/firmware interlock. [Launcher](https://github.com/adgower/openpilot/blob/6ae31161b73de2ce5043f708569759ac5f55f283/launch_chffrplus.sh), [OS requirement](https://github.com/adgower/openpilot/blob/6ae31161b73de2ce5043f708569759ac5f55f283/launch_env.sh), [Chestnut requirement](https://github.com/adgower/openpilot/blob/6ae31161b73de2ce5043f708569759ac5f55f283/openpilot/common/hardware/usb.py).

There are documented recovery mechanisms, but no proven one-step return to the complete current OS/application/firmware combination. An application backup preserves settings and source, not an AGNOS or firmware snapshot.

## OS recovery choices

| Choice | What the evidence supports | Limits and prerequisites |
| --- | --- | --- |
| Restore preserved application/configuration | Appropriate first response to a candidate source/build problem while SSH and the OS remain usable. | Restoring source does not reverse OS or firmware. Old source can itself request its expected OS/firmware on startup. Check compatibility before launching restored source. |
| A/B slot fallback | Candidate updater selects the opposite slot, marks it unbootable before writing, verifies images and later switches active slot. Its seven manifest partitions all have A/B copies. | This establishes update design, not tested rollback. Slot A being active does not prove slot B is healthy, or that old slot A remains bootable after later updates. Shared `/data` and external firmware are not rolled back by choosing a slot. No slot switches were tested. |
| On-device factory reset | Comma four reset UI removes `/data` content and reformats userdata, then reboots. | Destructive to settings, source, calibration and local backups. It is not an OS downgrade. Copy private backups off the device first. |
| Official web reflash | Official AGNOS builder points users to [flash.comma.ai](https://flash.comma.ai/) for factory recovery. The official wizard supports Comma four using WebUSB and offers Chrome when WebUSB is absent. | Requires physical access, Mac-compatible Chrome/WebUSB, internet, a working USB data cable for port 1, and a second connection powering port 2. It erases user data and installs official release images, not Alex's pinned fork or necessarily AGNOS 19.7. Hardware recognition/flashing have not been tested on this Mac/device. |

A subtle hazard: the AGNOS script's `--verify` option is **not read-only**. On success it calls `swap`, clears stored partition hash markers and sets the active slot. `--swap` can download and flash first; invoking the script without those switches also flashes. Do not use any of these as an inventory check. [Pinned updater](https://github.com/adgower/openpilot/blob/6ae31161b73de2ce5043f708569759ac5f55f283/openpilot/common/hardware/comma/agnos.py), [pinned manifest](https://github.com/adgower/openpilot/blob/6ae31161b73de2ce5043f708569759ac5f55f283/openpilot/common/hardware/comma/agnos.json).

The factory reset is explicitly an erase action, and directs users to the web flasher for deeper reset. [Pinned Comma four reset implementation](https://github.com/adgower/openpilot/blob/6ae31161b73de2ce5043f708569759ac5f55f283/openpilot/system/ui/mici_reset.py).

## Official Mac recovery evidence

The official web-flasher source was fetched read-only into `${PRIVATE_CACHE}`, pinned at `7dddd54b0d8d493d57486596affaacabac740630`. The current wizard gives a Comma four-specific sequence: disconnect, connect port 1 to the computer, then port 2 to the computer or a power brick; the blank screen is expected. Its Windows driver step is Windows-only, and its Linux driver-unbind step applies to Comma 3/3X. There is no Windows computer requirement for this path. Actual WebUSB permission and Comma detection remain untested. Use the live wizard and its port illustration when recovery is authorized, rather than applying old Comma 3/3X instructions. [Wizard source](https://github.com/commaai/flash/blob/7dddd54b0d8d493d57486596affaacabac740630/src/app/Flash.jsx).

The flasher repairs partition tables, erases storage while preserving GPT/MBR and `persist`, installs system images and resets. Preserving `persist` does **not** preserve `/data` or Alex's settings. Its Comma four image manifest comes from `release-mici`; factory recovery is not a pinned 19.7 downgrade service. [Erase/install implementation](https://github.com/commaai/flash/blob/7dddd54b0d8d493d57486596affaacabac740630/src/utils/manager.js), [manifest selection](https://github.com/commaai/flash/blob/7dddd54b0d8d493d57486596affaacabac740630/src/config.js).

The [official AGNOS builder README](https://github.com/commaai/agnos-builder) also documents developer flashing and an Apple Silicon `libusb` workaround. That is an alternate developer path, not a prerequisite for Chrome's WebUSB recovery. Building a kernel on macOS adds a case-sensitive-filesystem requirement; factory web recovery does not require building a kernel.

## Panda recovery

The pinned `pandad` wrapper resets the internal Panda, checks bootstub/app health and version, and invokes the internal recovery/DFU path to reflash bootstub and app if unhealthy or mismatched. Its source documents this as a recovery mechanism; no DFU entry or flash was tested here. A mismatched candidate can flash simply by starting this process. Preserve both source revisions and their firmware/build provenance. Application rollback can require matching Panda firmware, so a folder restore must not be described as a complete hardware rollback. [Pinned Panda wrapper](https://github.com/adgower/openpilot/blob/6ae31161b73de2ce5043f708569759ac5f55f283/openpilot/selfdrive/pandad/pandad.py).

## Chestnut recovery

The candidate `hardwared` automatically initiates a Chestnut firmware flash while offroad when its product/version mismatches. Its flasher preserves the first 256 bytes of device configuration in `/data/chestnut_config/<hostname>.bin`, verifies sector/page writes and final image, and includes a ROM-bootloader recovery path. Crucially, ROM recovery refuses to proceed without a valid **256-byte configuration backup** at that path. The hostname-dependent name must be retained or deliberately reconciled if factory recovery changes the hostname. [Automatic flash trigger](https://github.com/adgower/openpilot/blob/6ae31161b73de2ce5043f708569759ac5f55f283/openpilot/system/hardware/hardwared.py), [pinned flasher and ROM recovery](https://github.com/adgower/openpilot/blob/6ae31161b73de2ce5043f708569759ac5f55f283/openpilot/system/hardware/chestnut/flash.py).

Inventory and copy any existing `/data/chestnut_config` files to the private Mac backup before an update. Checking/copying existing files is different from creating a hardware configuration dump: do not execute the flasher to generate one under today's no-update authorization. If none exists, record that limitation; the candidate creates one before normal programming, but that does not establish pre-migration recovery now. Its firmware can activate after a power cycle; restoring old source is not proof of a successful downgrade to `ed4e39b7`. Chestnut's configuration backup is not a full old-firmware dump. No standalone official Mac Chestnut factory-recovery procedure was established in this review.

The coordinating inventory reported this directory absent in the previous backup. Unless the fresh inventory finds it, **Chestnut ROM recovery has a concrete missing prerequisite**. The normal flash path reads the 256 bytes three times for stability, creates the backup exclusively with mode 0600 and fsyncs it before its first sector erase/program. That sequencing reduces risk during a future authorized normal flash; it is not proof that a backup already exists or is recoverable on the Mac. A separate future preparation option is a narrowly reviewed configuration-dump-only routine with no erase/program/activation calls. Even its USB register access, driver unbinding and runtime-power-management changes would be hardware operations requiring a new explicit scope; do not silently classify them as passive inventory. For today's staging, leave firmware untouched and record the missing backup rather than execute the bundled flasher.

## Before approving activation

- Keep the verified application/parameter backup on the Mac, independent of userdata; preserve existing Chestnut configuration backup and hostname if present.
- Have physical access, Chrome, data-capable USB cable and separate power connection available. Confirm the live flasher loads without connecting or flashing; physical recovery has not yet been rehearsed.
- Keep the staged branch inert and verify exact parent/child revisions, model assets and source constants offline. The 1.20/0.97 values are source constants, not a replacement for preserving parameters/calibration.
- Treat AGNOS update, Panda update and Chestnut update as separate changes with separate post-update verification. The current authorization permits none of them.
- Do not promise A/B rollback, firmware downgrade or factory restore of the personal configuration. Supported mechanisms exist, while end-to-end recovery of this particular hardware/software combination remains untested.

The official [device connection documentation](https://docs.comma.ai/how-to/connect-to-comma/) describes Comma four serial access through an internal debug connector with dedicated debug hardware forthcoming; an ordinary Mac USB cable must not be presented as guaranteed serial-console access. Web recovery does not require buying that debug connector.
