# What should I do if uninstalling an application on the local Emulator shows success, but it was not actually uninstalled?

**Symptom**

Uninstalling an application on the local Emulator shows success, but it was not actually uninstalled.

**Solution**

The application cannot be uninstalled if the Emulator disk space is full. The disk space may be insufficient when the **hdc file send local remote** command is frequently used to push files to the Emulator.

You can use the following two methods:

-   Method 1: Delete the files that are no longer used from the Emulator. You can run the **hdc shell \[COMMAND\]** command to delete related files. For details about hdc, see [hdc](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hdc).
-   Method 2: Delete the local Emulator and create a new one. If the local Emulator is used to push large files or applications, you are advised to increase the internal storage (ROM) when creating the Emulator.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/UUe4zMJ_S4SanwdmnEcsQw/en-us_image_0000002194318364.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F06C2E4601A000D7FE8719F170EBD7094E55C138E1EF013779B882E212AF5A7B "Click to enlarge")
