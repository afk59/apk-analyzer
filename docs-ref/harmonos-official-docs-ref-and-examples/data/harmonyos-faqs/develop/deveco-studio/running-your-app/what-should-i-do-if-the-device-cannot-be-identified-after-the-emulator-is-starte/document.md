# What should I do if the device cannot be identified after the Emulator is started?

**Symptom**

Scenario 1: During debugging, if HAP fails to be installed and "Device not found or connected" is reported, check whether the device is correctly connected.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/W0UzfRFLRdmCH_83kU5pRA/en-us_image_0000002229603797.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E3171DCA709A30DFF29AE6BEB453BC2B3D2D1DB7A6D70E0CDE7F322D1DF2071)

Scenario 2: DevEco Studio cannot identify the connected device and "No device" is reported.

**Possible Causes**

The hdc process or Emulator is abnormal.

**Solution**

1.  Run the following command to stop the hdc process, and then reconnect to the device:
    
    hdc kill
    
2.  If the issue persists, restart the Emulator, and try again.
