# What should I do if the password of the keystore file is incorrect?

**Symptom**

The message "Init keystore failed: keystore password was incorrect" is displayed during application packaging and signing.

**Possible Causes**

The password of the keystore file is incorrect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/t40Ejr-jTRi-oSXIjU5xWA/en-us_image_0000002487813226.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6FEF551F6230AC83343ACF461C17EC56FF6260BA36AB19B5707471587FCD6D5B)

**Solution**

Use the correct password of the keystore file. To verify the password, perform the following steps:

Open the **Terminal** window in DevEco Studio and run the **keytool -list -keystore ${Store file} -storepass ${Store password}** command.

-   Correct password

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/L1vrXLjCQLqQ-UwhFNzWIw/en-us_image_0000002376396373.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E549BE82090D15793507F7D1202CE81BDDD9AA4AE642877C74B33A84BAEAA40)

-   Incorrect password

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/lEnq45RQTk2xAH_NAUON_Q/en-us_image_0000002342678234.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6FA99E9B43A2D99985EAD7E2DC64B991D15FBAB2FA8C26F76CECC5F9ADBAE4E8)
