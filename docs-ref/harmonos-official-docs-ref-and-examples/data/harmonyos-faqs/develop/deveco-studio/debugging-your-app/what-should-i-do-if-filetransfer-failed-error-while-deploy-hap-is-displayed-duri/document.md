# What should I do if "FileTransfer Failed: Error while Deploy Hap" is displayed during HAP installation on DevEco Studio?

**Symptom**

The error message "FileTransfer Failed: Error while Deploy Hap" is displayed during HAP installation on DevEco Studio.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/5XBSNwJnTiOpsGwLAnzV5Q/en-us_image_0000002215508376.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B39D565817AB090759BB2CE14F345E6979B5F5DEF1CD02DC65431B23D0BD1F5)

**Solution**

If a real device is used: Replace the data cable or the USB port on the PC and try again.

If the Emulator is used:

-   In the device list window of the local emulator, click **Wipe User Data** to clear the emulator data, start the emulator, and run the project again.
-   Open the command line tool, go to **sdk\\default\\openharmony\\toolchains** in the DevEco Studio installation directory, run the **hdc kill -r** command, and start the emulator and run the project again.
