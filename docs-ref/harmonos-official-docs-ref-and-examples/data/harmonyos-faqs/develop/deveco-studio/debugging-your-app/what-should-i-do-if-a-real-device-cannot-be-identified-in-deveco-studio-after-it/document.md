# What should I do if a real device cannot be identified in DevEco Studio after it is connected?

**Symptom**

During debugging, the HAP fails to be installed and the error message "Device not founded or connected" is displayed. Alternatively, "No device" is displayed in the DevEco Studio device list.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/mhKkFhycTa6N_dnb3Ctk_w/en-us_image_0000002370362990.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CEF04A616B060E4A582B67D083FAC730C743122944224F150120F4A7D203BDA9 "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/sCHpc3W1SWmTcpgExcrOkA/en-us_image_0000002403922581.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0BFC36023699BF66B8123F06372852563202E3E51C2B4C29CC58F900210B8935 "Click to enlarge")

**Possible Causes**

1.  **Developer options** is disabled on the device.
2.  The device system does not match the DevEco Studio version.
3.  The USB cable in use is a charging cable, not a data cable.
4.  The current USB data port is damaged.
5.  The hdc process or device is abnormal.
6.  Scenario 1: After USB debugging is disabled, the USB cable is disconnected, and USB debugging is enabled again, no device could be recognized.
    
    Scenario 2: After wireless debugging is enabled, connect to the device for wireless debugging. Then, disable wireless debugging and enable USB debugging, no device could be recognized.
    
7.  The connected device is not supported.

**Solution**

1.  Enable [Developer options](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-developer-mode) on the device, and enable USB debugging or wireless debugging.
2.  Make sure the versions that match. For details, see [Version Overview](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/overview-511-beta1).
    
3.  Use a USB 2.0 cable to directly connect to the device, without using a docking station.
4.  Connect the device to a different USB port. Make sure the port drivers are properly installed and up to date.
5.  Run the following command to stop the hdc process, and then reconnect to the device:
    
    hdc kill
    
    If the issue persists, restart the device and try again.
    
6.  Restart the device, connect the device using a USB cable, and enable USB debugging.
