# Emulator Error Codes

When an error occurs during emulator running, you can submit error details. On the extensions menu bar, open the bug report page.

-   On the left pane, check the screenshot of the device captured when the error occurs.
-   Under **Issue description**, enter details about the bug to help locate and solve the issue more quickly.
-   Under **Context of Log Files**, view the collected logs.
-   In the lower right corner of the page, select the checkbox to agree to the User Agreement and click **Save** to store the bug log locally.

Sign in to the [HUAWEI Developers](https://developer.huawei.com/consumer/en/support/feedback/#/add/90011/HAOS0001?level2=90047) website to submit the error. During submission, upload the saved bug log to the attachments section.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/c159PhXASN-CqW6Ggm9Lpg/en-us_image_0000002501068632.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6847ABA2B3383A2F2E0EBB7C3C721738415EFB3BC3513BD604A6AA8D76D0AC5D "Click to enlarge")

#### 00801001 Hyper-V Is Not Enabled

**Error Message**

Hyper-V Not Enabled.

**Symptom**

"Hyper-V Not Enabled" is reported when the emulator is started.

**Possible Causes**

-   Run the emulator in a virtual Windows environment, such as a cloud desktop. Currently, the emulator cannot run on a VM.
-   If Hyper-V is not enabled on Windows, perform the following steps.

**Solution**

1.  Check whether the CPU model supports virtualization. If not, the emulator cannot be used.
2.  If the CPU supports virtualization, choose **Control Panel** > **Programs** > **Programs and Features** > **Turn Windows features on or off** (for Windows 11, go to **System** > **Optional features** > **Related settings** > **More Windows features**). Check whether **Hyper-V**, **Windows Hypervisor Platform**, and **Virtual Machine Platform** are listed.
    
    -   If no, Hyper-V is not preinstalled in the system. Install Hyper-V that matches the system version.
    -   If yes, select the three features, click **OK**, and restart the computer.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/D6-Tyk3qQgm_XrPv_dNOjQ/en-us_image_0000002501068624.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C03C710CFE2D73CC4C0AD9B99903E545639F375B13462EB37BD413AD20E04F1 "Click to enlarge")
    
3.  If the error persists, open the CLI as an administrator, run the following command, and restart the computer.
    
    bcdedit /set hypervisorlaunchtype auto
    
4.  If the issue persists, choose **Task Manager** > **Performance**. If **Virtualization** is disabled or not enabled, it is disabled in the BIOS. In this case, go to the BIOS settings page based on the mainboard model of the computer and enable the virtualization feature.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/8KxKUC6cSaihtIc6ajCQug/en-us_image_0000002501068628.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56CA2C0A8CCB8DF0CF68D8C93E125B01CA998A71E6CB98BD0E2BA901B02BF4C2 "Click to enlarge")
    

For details about how to install Hyper-V, see [Install Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/Install-Hyper-V?f=255&amp;MSPPError=-2147217396&amp;tabs=powershell&amp;pivots=windows) and [System requirements for Hyper-V on Windows and Windows Server](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/host-hardware-requirements?pivots=windows).

#### 00801002 Insufficient Disk Space

**Error Message**

The available disk space is less than the amount of space required to run the emulator.

**Symptom**

The error message "The available disk space is less than the amount of space required to run the emulator" is displayed.

**Possible Causes**

The disk space of the emulator does not meet its startup requirements.

**Solution**

1.  Free up the disk space or change the disk location where the emulator resides.
2.  If the operating system is macOS and the displayed available disk space is larger than the space required by the emulator, open Disk Utility and check the amount of space available. Determine if there is reclaimable space causing the actual available space to be far less than the displayed available space. If so, try clearing unnecessary APFS snapshots and local cache files from Disk Utility.

#### 00801003 Image File Path Is Changed

**Error Message**

The Image path has changed. Please clear image data before start.

**Symptom**

The error message "The Image path has changed. Please clear image data before start" is displayed.

**Possible Causes**

The path for storing the image file is changed.

**Solution**

Click **OK** to clear the image data, and then start the emulator. If you do not want to clear the image data, click **Cancel**, change the image path to the original one, and start the emulator.

#### 00801004 CPU Does Not Support AES Instructions

**Error Message**

Emulator cannot start on this computer because its CPU does not support AES instructions.

**Symptom**

The error message "Emulator cannot start on this computer because its CPU does not support AES instructions" is displayed.

**Possible Causes**

The current CPU does not support AES instructions.

**Solution**

The current computer does not support the Emulator. You are advised to replace the computer with one that supports the Emulator. For details, see [Working Environment](../overview/working-environment/document.md).

#### 00801005 Insufficient Allocable Memory

**Error Message**

Emulator failed to start due to insufficient memory.

**Symptom**

The error message "Emulator failed to start due to insufficient memory" is displayed.

**Possible Causes**

The idle memory of the system does not meet the memory requirements for starting the Emulator.

**Solution**

1.  Open **Task Manager** and choose the **Details** tab, right-click the table header and choose **Select columns** and select **Commit size**. Click the **Commit size** column to sort the processes, and close some processes with high commit size.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/Qhw_MUEcSh6fuGnqSyWPOA/en-us_image_0000002501068640.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FFDBAA6CFE3BD5788CF105A71B9580D4EBF37B6D6D9175586E7B12795B38FD1A)
    
2.  Choose **Task Manager** > **Performance** > **Memory** and ensure that the remaining committed memory size is greater than the RAM size set for the Emulator.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/9eCs02ioTtGhpz91N6F7SQ/en-us_image_0000002501068618.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11A1DECC1DDE29BE55B01E5DDAEC53F0D5C76E7651FD4FEF2BFFC5A0DF4F9C3A "Click to enlarge")
    

#### 00801006 Windows System Version Out of Date

**Error Message**

To avoid emulator malfunctions and unexpected computer restarts, update your PC to Windows 10 (OS build 18363 or later) and then try again.

**Symptom**

The error message "To avoid emulator malfunctions and unexpected computer restarts, update your PC to Windows 10 (OS build 18363 or later) and then try again" is displayed.

**Possible Causes**

The current Windows version is outdated.

**Solution**

Upgrade the Windows version as instructed.

#### 00801007 Disk Space of the Emulator Is Insufficient

**Error Message**

The remaining disk space of the emulator is insufficient. Please clear the emulator data and then restart the emulator.

**Symptom**

The error message "The remaining disk space of the emulator is insufficient. Please clear the emulator data and then restart the emulator" is displayed.

**Possible Causes**

The disk space of the emulator is insufficient.

**Solution**

Clear the emulator data and restart the emulator.

#### 00801008 Image File Missing

**Error Message**

The system-image file is missing.

**Symptom**

The emulator fails to be started, and the error message "The system-image file is missing" is displayed.

**Possible Causes**

The image file is damaged or lost.

**Solution**

Use either of the following methods to solve the problem:

-   Choose **Tools** > **Device Manager** on the menu bar. On the **Local Emulator** tab, click **New Emulator** in the lower right corner. On the virtual device configuration page, update the emulator image files.
-   Delete the created emulator and create a new one.

#### 00801009 Unsupported Image Version

**Error Message**

The current emulator image version is too low.

**Symptom**

The error message "The current emulator image version is too low" is displayed.

**Possible Causes**

The current image version is outdated.

**Solution**

Open the device management page, update the image, and create an emulator.

#### 00801010 Image Version Mismatch

**Error Message**

The Image version has changed. Please clear image data before start.

**Symptom**

The error message "The Image version has changed. Please clear image data before start" is displayed.

**Possible Causes**

The image version is changed.

**Solution**

Click **OK** to clear the image data and start the emulator. If the image data of the old version still exists on the local PC, click **Cancel** to replace the image data with that of the old version and start the emulator.

#### 00801011 Outdated macOS Version

**Error Message**

To avoid emulator malfunctions and unexpected computer restarts, update your Mac to 12.5 or later.

**Symptom**

The error message "To avoid emulator malfunctions and unexpected computer restarts, update your Mac to 12.5 or later" is displayed.

**Possible Causes**

The current macOS version is outdated.

**Solution**

Upgrade the macOS version to the prompted version or later.

#### 00801012 Emulator Configuration File Is Damaged or Abnormal

**Error Message**

The emulator configuration file is damaged or abnormal.

**Symptom**

The error message "The emulator configuration file is damaged or abnormal" is displayed.

**Possible Causes**

The configuration file of the local emulator is damaged or abnormal.

**Solution**

-   In the **Local Emulator** window, click **Wipe User Data** to clear the emulator data, and then restart the emulator.
-   Create an emulator and start it.

#### 00801013 Outdated Graphics Driver Version

**Error Message**

The graphics card in use does not support OpenGL 4.1 or later. Update the graphics card driver or use another graphics card.

**Symptom**

The error message "The graphics card in use does not support OpenGL 4.1 or later. Update the graphics card driver or use another graphics card" is displayed.

**Possible Causes**

The graphics driver is outdated, or does not support OpenGL 4.1 or later.

**Solution**

Upgrade the graphics driver. If the graphics card does not support OpenGL, replace the graphics card. For details, see [Working Environment](../overview/working-environment/document.md).

#### 00801014 SDK Path Is Changed

**Error Message**

Sdk Path has been changed.

**Symptom**

The emulator fails to be started, and the error message "Sdk Path has been changed" is displayed.

**Possible Causes**

The SDK path is changed when the emulator is started.

**Solution**

Use either of the following methods to solve the problem:

-   In the **Local Emulator** window, click **Wipe User Data** to clear the emulator data, and then restart the emulator.
-   Create an emulator and start it.

#### 00801015 Local Emulator Does Not Exist

**Error Message**

No local emulator found.

**Symptom**

The emulator fails to be started, and the error message "No local emulator found" is displayed.

**Possible Causes**

The local emulator file is missing or damaged.

**Solution**

Delete the emulator and create a new one.

#### 00801016 No Matching Device Found Due to the HDC's Abnormal Running State

**Error Message**

Can't find device, may be Hdc is not normal running.

**Symptom**

The error message "Can't find device, may be Hdc is not normal running" is displayed.

**Possible Causes**

The HDC process is abnormal, or the emulator image does not match the DevEco Studio version.

**Solution**

1.  Run the following command to terminate the HDC process, and then try again. For more information about HDC, see [hdc](../../../system/debugging-tools/performance-analysis-kit/command-line-tools/hdc/document.md).
    
    hdc kill
    
2.  If the issue persists, restart DevEco Studio and the emulator, and try again.
3.  Choose **Tools** > **Device Manager** from the menu bar. On the **Local Emulator** tab, click **New Emulator** in the lower right corner. On the virtual device configuration page, update the emulator image.
4.  If the HDC environment variable has been configured, check whether it is correctly configured.

#### 00801017 Failed to Install and Parse the .so File

**Error Message**

The XXX ABI type is missing. Make sure it is configured for all .so files in the HAPs/HSPs.

**Symptom**

When you start debugging or run a C++ app or atomic service, the error message "The XXX ABI type is missing. Make sure it is configured for all .so files in the HAPs/HSPs" is displayed.

**Possible Causes**

The Application Binary Interface (ABI) supported by the device does not match that configured in the C++ project.

**Solution**

-   For details, see [9568347 Failed to Parse Native SO Files](../../../system/debugging-tools/debugging-commands/bundle-manager/document.md#section9568347-failed-to-parse-native-so-files).
-   If the project configuration cannot be modified, you can use the cloud debugging service and select a HarmonyOS NEXT device for development and debugging. For details, see [Cloud Debugging](https://developer.huawei.com/consumer/en/agconnect/cloud-adjust).

#### 00801018 Insufficient Emulator Memory

**Error Message**

The emulator RAM is insufficient.

**Symptom**

The default RAM of the emulator is 4 GB. When the emulator RAM is insufficient, an error message pops up, and the emulator may freeze or crash.

**Possible Causes**

The RAM allocated to the emulator is less than 500 MB.

**Solution**

You are advised to increase the emulator RAM when creating the emulator. For details, see [Creating an Emulator](../managing-the-emulator/creating-an-emulator/document.md#section1764055173710).

#### 00801019 Image File Verification Failure

**Error Message**

Failed to verify the image file.

**Symptom**

The emulator fails to be started, and the error message "Failed to verify the image file" is displayed.

**Possible Causes**

The emulator image file does not match the image signature file.

**Solution**

On the **Local Emulator** tab, click **New Emulator** in the lower right corner. On the virtual device configuration page, download the matching image file.

#### 00801020 Unsupported by ARM-based Windows

**Error Message**

Failed to start the Emulator. It does not work with Windows on Arm.

**Symptom**

The emulator fails to be started, and the error message "Failed to start the Emulator. It does not work with Windows on Arm" is displayed.

**Possible Causes**

The emulator does not work with Windows on ARM.

**Solution**

Change the system type and then use the emulator. For details about the running environment requirements, see [Working Environment](../overview/working-environment/document.md).

#### 00802001 Emulator Is Suspended

**Error Message**

Emulator Freeze.

**Symptom**

The emulator image system runs abnormally, and a crash report is displayed. **ErrorType** is **Emulator Freeze**.

**Possible Causes**

Unknown causes.

**Solution**

1.  On the displayed crash report dialog box, click **Save** to store the bug log locally. Then, sign in to the [HUAWEI Developers](https://developer.huawei.com/consumer/en/support/feedback/#/add/90011/HAOS0001?level2=90047) website to submit the error. During submission, upload the saved bug log to the attachments section.
2.  Restart the emulator.

#### 00802002 Emulator Does Not Respond

**Error Message**

Emulator Graphic Hung.

**Symptom**

The emulator does not respond, and a crash report is displayed. **ErrorType** is **Emulator Graphic Hung**.

**Possible Causes**

The graphics rendering process is abnormal.

**Solution**

1.  On the displayed crash report dialog box, click **Save** to store the bug log locally. Then, sign in to the [HUAWEI Developers](https://developer.huawei.com/consumer/en/support/feedback/#/add/90011/HAOS0001?level2=90047) website to submit the error. During submission, upload the saved bug log to the attachments section.
2.  Restart the emulator.

#### 00802003 Emulator Crashes

**Error Message**

Emulator Crash.

**Symptom**

The emulator crashes unexpectedly and a crash report is displayed. **ErrorType** is **Emulator Crash**.

**Possible Causes**

The emulator exits unexpectedly due to unknown causes.

**Solution**

1.  On the displayed crash report dialog box, click **Save** to store the bug log locally. Then, sign in to the [HUAWEI Developers](https://developer.huawei.com/consumer/en/support/feedback/#/add/90011/HAOS0001?level2=90047) website to submit the error. During submission, upload the saved bug log to the attachments section.
2.  Restart the emulator.
