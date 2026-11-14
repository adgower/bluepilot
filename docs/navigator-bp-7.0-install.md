# Install BluePilot 7.0 on the 2022 Lincoln Navigator

This branch is for the standard-wheelbase Navigator with the existing comma harness. It identifies the car from its firmware and uses BluePilot 7.0's Angle mode with Alex’s full Navigator wheel-target tune. It works with the device's normal driving model. No Chestnut setup is required. This port has had source review only. Its first device build and parked identification check are pending.

## Install while parked

1. Photograph your current BluePilot settings and save any recordings you want to keep. You'll reinstall from a different GitHub fork, so use the custom install screen. Keep the comma powered and connected to Wi-Fi during installation.
2. Open **Settings → Software → Uninstall** on a comma 3X. On a comma 4, open **Settings → Device → Uninstall sunnypilot**. Confirm and let the comma restart.
3. Choose **Custom Software** on the setup screen. On a comma 4, use **Slide to install custom software**, then follow the prompts to **Choose software**. Enter this address exactly:

   ```text
   installer.comma.ai/adgower/bp-7.0-navigator
   ```

   The installer uses the branch mirrored under Alex’s `openpilot` repository. The code is BluePilot 7.0.

4. Wait for the download, first build, and any reboots to finish. Leave the device powered until the normal BluePilot home screen appears.

## If this Navigator branch is already installed

While parked, use the device’s software updater to check for and install an update on the current branch. After it restarts, follow the settings below.

## Set up Angle mode

1. **Clear the old Expedition override if you see it.** On a comma 3X, open **Settings → Vehicle**. Tap **REMOVE** if Expedition was manually selected and the row is blue. If you see **SELECT**, leave it alone. If you reinstall on a comma 4, start with the fresh settings and skip importing an old backup that contains the Expedition override.
2. On a comma 3X, open **Settings → BluePilot → Lateral Tuning → Primary Control Variable** and select **Angle**. On a comma 4, open **Settings → BluePilot** and select **angle** under **Primary Control Variable**.
3. Turn on **Use Pinion Yaw Sensor**. On a comma 3X, open **Settings → BluePilot → Vehicle**. On a comma 4, open **Settings → BluePilot → vehicle**. This switch selects the full Navigator tune when Angle is active.
4. Leave **Disable BP Lateral Control** off. The full tune uses Alex’s **1.20 low-speed / 0.97 high-speed** factors internally, so you can skip the adjustment sliders. Keep **Alpha Longitudinal** off for the first check so the Navigator handles adaptive cruise.
5. Reboot while parked. The pinion setting takes effect at startup. Once the comma has valid calibration, the tune can use the steering wheel reading, the comma’s built-in motion sensors, and the selected driving model’s path. There is no Chestnut step.

## Check before using assistance

1. Start the Navigator and leave it in Park. Wait for vehicle detection. On a comma 3X, return to **Settings → Vehicle** and look for a green **LINCOLN_NAVIGATOR_MK4** row. Green indicates automatic detection. A blue row indicates a manual selection.
2. If there's no detected Navigator, the device still reports Expedition, or there is a persistent warning, leave assistance disengaged. Share a photo of the alert and the route timestamp with Alex so he can check the firmware response. A fresh ignition cycle and reboot while parked can help after clearing a manual override.
3. A successful parked check confirms that the software booted and saw the right car. Use the branch initially as an evaluation build and take over immediately if steering behavior is unexpected.

## Go back to regular BluePilot 7.0

To try the built-in BluePilot Angle controller first, turn **Use Pinion Yaw Sensor** off and reboot while parked.

To reinstall regular BluePilot 7.0, repeat the uninstall and Custom Software steps and enter `installer.comma.ai/BluePilotDev/bp-7.0`. Reapply your previous settings from the photos. The regular branch may still need the Expedition selection you were using before.
