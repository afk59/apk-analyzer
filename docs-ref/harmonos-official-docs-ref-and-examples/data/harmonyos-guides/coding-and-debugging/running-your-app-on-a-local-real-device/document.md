# Running Your App on a Local Real Device

Install and run your HarmonyOS app/atomic service on a local real device in either USB or wireless mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/WRtMAvi9T12HQf8WCpRNCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D9CCC77B12F5F51E96AD02BD905CAB6FFD9A2468FDFA397CA8CF3BB018F62E3)

Wearables (excluding lite wearables) support only wireless debugging.

#### Prerequisites

-   The device operating system is HarmonyOS NEXT Developer Beta1 or later.
-   On the HarmonyOS real device, check whether **Developer options** exists in **Settings** > **System**. If it does not exist, choose **Settings** > _Device name_, tap the software version number seven times in quick succession until a prompt like "Enable developer options" appears. Tap the confirm button and enter the PIN (if set). The device will automatically restart. Wait until the restart is complete.
-   The app/atomic service has been signed. For details, see [Signing Your App/Atomic Service](../configuring-a-debug-signature/document.md).

#### In USB Mode

1.  Use a USB cable to connect the real device to the computer.
2.  Choose **Settings** > **System** > **Developer options** and enable **USB debugging** (this option is available only when the device is connected through a USB cable).
3.  When a USB debugging authorization prompt appears on the real device, click **OK**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/ZBpvR1SLSymCebHW2OssIQ/en-us_image_0000002532750617.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B37D47480A9D66CE43998B19DC65F53A4E38E9AA54FC3DE8ACA734A943768556)
    
4.  On the menu bar, choose **Run** > **Run '**_module name_**'** or click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/PvVVDzGGQF2Nl0hMExrTUw/en-us_image_0000002501070592.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B96AD11C7D5BE4C10701784501ACB0036BC2EDBFBA406B330646231CAF5C5216), or press **Shift+F10** (**Control+R** on macOS).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/poXGwzQfQZmI1CSe8waT3A/en-us_image_0000002501070596.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5FBF4DED6CFDD5A187EB410E0BB66A289DB2661A7E2ED6658D6371B0EE932FF5)
    
5.  DevEco Studio will start to build and install the HAP on the device. The device will automatically run your app/atomic service once it is installed.

## Troubleshooting with the Device Connection Assistant

Since DevEco Studio 5.1.1 Beta1, if DevEco Studio cannot detect the device after it is connected, the message "No Devices" is displayed. You can use the device connection assistant for troubleshooting. Click the device drop-down menu and select **Troubleshoot Device Connections** to enable it. This initiates a three-step diagnostic process. Click **Next** after completing each step.

1.  **Connect your device via USB**. Click **Rescan Devices** to refresh the connected device list. Ensure your target device appears in the results.
2.  **Enable USB debugging**. Verify the OS version of your device. Enable **Developer options** and **USB debugging** on your device.
3.  **Restart the hdc service**. If DevEco Studio still cannot identify the device, click **Restart hdc Service**. This forces hdc to re-detect connected devices. If issues persist, see [What should I do if the device cannot be detected after being connected?](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs/faqs-app-debugging-3) or [What should I do if a device cannot be identified by hdc?](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs/faqs-performance-analysis-kit-32).

#### In Wireless Mode

1.  Connect the real device and the PC to the same WLAN.
2.  With **Developer options** enabled, turn on **Wireless debugging** or **Debug via WLAN** (for wearables) and obtain the IP address and port number of the real device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/wMAx5IIvT5OjMifsy2de4A/en-us_image_0000002500910752.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=490751CFD1CE29AE0C321C6BF0BDA8AD3D6FFC09EBB0C78346F4A05EB3EF101A "Click to enlarge")
    
3.  Connect the device in either of the following ways:
    
    -   On the menu bar of DevEco Studio, choose **Tools** > **IP Connection**, enter the IP address and port number of the device to connect, and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/0rYTXokdTk208djvQxZyXQ/en-us_image_0000002532750613.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BCA8451243CE533C46AC71B32B866D65B7C9F737E088AAFB95CA5D5FCD3843D7). After the connection is set up, the device's status will change to **online**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/nc3UnLeqTmW0bFC5uVbJNA/en-us_image_0000002500910750.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F187F11BE34073C0FE1E4F4B9F3CFC84166C6A7CB5909582F79A19A29BB8A267)
        
    -   Run the hdc command. For details about how to use the hdc tool, see [hdc](../../system/debugging-tools/performance-analysis-kit/command-line-tools/hdc/document.md).
        
        hdc tconn _device IP address:port number_
        
    
4.  On the menu bar, choose **Run** > **Run '**_module name_**'** or click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/GHfrKSiMTPGI3inpUMK0rw/en-us_image_0000002532750615.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F975CAC8FED56D53997C94BFA70A561E3295121C3453EFFBF7299427DEED7E5E), or press **Shift+F10** (**Control+R** on macOS).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/yITi0OacRH-fQ2L1bHAzhw/en-us_image_0000002501070594.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B778E009DD9DC52C087F3AB8EBB17921F2B6F154D422E25EE20488C36ECA2499)
    
5.  DevEco Studio will start to build and install the HAP on the device. The device will automatically run your app/atomic service once it is installed.
