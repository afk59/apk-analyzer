# What should I do if the hdc cannot connect to the MacBook (ARM chip)?

**Symptom**

After the **hdc list targets** command is executed on the MacBook (ARM chip) system, the result is **\[Empty\]**.

**Possible Causes**

1\. The USB device cannot be discovered on the MacBook (ARM chip) system.

2\. The hdc device can be queried by running the **system\_profiler SPUSBDataType** command. However, no authorization dialog box is displayed on the device side, which may be caused by the abnormal public key file on the computer.

**Solution**

1\. Check whether the macOS can identify the USB device connected to the Mac in **System Information** or **System Overview**.The specific steps are as follows:

-   Press and hold the **Option** key on the keyboard, and click the menu in the upper-left corner of the screen.
-   Choose **System Information** or **System Overview**.
-   Check whether **HDC Device** or **HDC Interface** exists in the device tree. If not, perform the following steps to check whether the USB connection is normal, or run the **system\_profiler SPUSBDataType** command to view the USB device information.

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

 | 

Use the USB cable delivered with the device.

 | 

If a third-party cable is used, ensure that the cable meets the USB2.0 standard.

 |
| 

Device status

 | 

The device is powered on. In **Settings** > **System** > **Developer options**, **USB debugging** is enabled.

 | 

If **USB debugging** is not enabled, remove and insert the USB port, restart the device, or restore the device to its factory settings.

 |

2\. Open the terminal window, run the **cd** command to go to the home directory of the current user, run the **rm -r .harmony** command to manually delete the public key storage directory, and run the **hdc kill -r** command to restart the server process to trigger authorization.
