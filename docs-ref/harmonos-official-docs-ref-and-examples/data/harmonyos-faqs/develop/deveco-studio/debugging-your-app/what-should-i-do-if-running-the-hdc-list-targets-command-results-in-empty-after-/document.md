# What should I do if running the "hdc list targets" command results in "\[Empty\]" after a real device is connected?

**Symptom**

After the **hdc list targets** command is executed, the command output is **\[Empty\]**, indicating that the device cannot be identified.

**Possible Causes**

| 
Item

 | 

Symptom

 |
| :-- | :-- |
| 

Hardware Connection

 | 

The USB port is abnormal, the data cable is damaged, or the docking station is interfered.

 |
| 

Driver Issue

 | 

The HDC driver is not installed, the driver version conflicts, or an exception occurs during Zadig installation.

 |
| 

Environment Conflict

 | 

The port is occupied (for example, ADB and HDC share port 8710), or the TCP mode fails to be switched.

 |
| 

System Compatibility

 | 

The device system does not match the hdc tool version, or the image burning is abnormal.

 |

**Solution**

1\. Check the device connection.

1.  Windows
    
    Check whether the target device is displayed in **Device Manager**.
    
    If **HDC Device** or **HDC Interface** is displayed, the connection is normal.
    
    **HDC Interface** usually indicates that the device has composite ports.
    
    If the **HDC Device** is not displayed, the device cannot be identified. You can use any of the following methods to resolve the problem:
    
    -   Change the USB port.
    -   Use another USB cable.
    -   Connect the device to another computer.
    -   Burn the corresponding image again.
    
    Reinstall the driver if it is damaged.
    
    Reinstalling the driver:
    
    Open [Zadig](https://zadig.akeo.ie/) ([Zadig Repository](https://github.com/pbatard/libwdi/releases)) and insert the device. In **Options**, click **List All Devices**, select **HDC Device** from the drop-down list, and click **Reinstall Driver**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/IpsmSYr-QDuzvwjIRjFUng/en-us_image_0000002229758201.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D2AE7275F1DEF84CC1D12FDA66398880219E76A3C19DD33CD4B29C2EC5B670A "Click to enlarge")
    
2.  Linux
    
    Run the **lsusb** command to check whether **HDC Device** or **HDC Interface** exists. If the command does not exist, run the **apt-get install usbutils** command to install usbutils.
    
3.  macOS
    
    Check whether the macOS can identify the USB device connected to the Mac in **System Information** or **System Overview**.
    
    (1) Press and hold the **Option** key on the keyboard, and click **Menu**.
    
    (2) Choose **System Information** or **System Overview**.
    
    (3) Select **USB** on the left.
    
    (4) Check whether **HDC Device** or **HDC Interface** is displayed in the device tree. If not, perform the following steps to check whether the USB connection is normal.
    

| 
Check Item

 | 

Normal Status

 | 

Exception Handling

 |
| :-- | :-- | :-- |
| 

USB port

 | 

Connect the device using a USB port.

 | 

If the device cannot be identified using a docking station, replace the docking station or try to connect the device using a USB port.

 |
| 

USB cable

Device status

 | 

Use the USB cable delivered with the device.

The device is powered on. In **Settings** > **System** > **Developer options**, **USB debugging** is enabled.

 | 

If a third-party cable is used, ensure that the cable meets the USB2.0 standard.

If **USB debugging** is not enabled, remove and insert the USB port, restart the device, or restore the device to its factory settings.

 |

2\. Clear device alarms.

1.  Run **regedit** to open the Registry Editor, and click **Computer\\HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\{88bae032-5a81-49f0-bc3d-a4ff138216d6}**.
2.  In the list on the right, right-click **UpperFilters** and choose **Edit** to clear all character data. (You are advised to back up the data before clearing the data.) Refresh the screen, remove and insert the device, or restart the PC.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/wSFw64HdRW-GFlYK34oqJw/en-us_image_0000002194158332.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9034C2E5AFA2FB7EB6DA9CEECD731B33A6046C37773F28D66915C1729BC83ED9 "Click to enlarge")
    

3\. Change the TCP mode to the USB mode.

4\. If "\[Fail\]Failed to communicate with daemon" is displayed when the device is connected, the possible causes are:

1.  The hdc does not match the device. If the latest image is burnt to the device, the hdc must be of the latest version.
2.  The port is occupied. hdc and hdc\_std cannot run at the same time because they use the same port. Ensure that either hdc or hdc\_std is running.
3.  The adb conflicts with the hdc. You can run any of the following commands:
    
    **adb kill-server**
    
    **hdc kill**
    
    **hdc start**
