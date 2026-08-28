# What should I do if "compatibleSdkVersion and releaseType of the app do not match the apiVersion and releaseType on the device." is displayed during HAP installation?

**Symptom**

The error message "compatibleSdkVersion and releaseType of the app do not match the apiVersion and releaseType on the device." is displayed during HAP installation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/vjU5e39bTT-08ps3q5jnmg/en-us_image_0000002247307937.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84A69456B6B294609A75A31BBE62DEDA4AC39EED67E45F5B07C9531D463DC36B)

**Solution**

This issue occurs because the minimum compatible SDK version configured in your project is later than the device image version.

You can run the **hdc shell param get const.ohos.apiversion** command to query the API version of the current device and compare it with the API version of the **compatibleSdkVersion** field configured in the project-level **build-profile.json5** file. If the versions do not match, adopt the following solutions:

Solution 1: Upgrade the device image version to match the version required by your project. You can do this through the system settings on the device.

Solution 2: Decrease the API version of your project. Click in the upper right corner ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/3W6TKaYtQqCYwBpb035iDg/en-us_image_0000002489396138.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C69E1F2845FFA23C2EC1835794281D1BB003E1C860307164FB73AB7305BE4B92) of DevEco Studio and select a lower version for Compatible SDK.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/LkY75IQwTqy_9WAdH9qkHA/en-us_image_0000002521676021.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72D37430A12628C9FD4734ECE7174ECF7F02C1B24B3A9C2E6D9461FCE3F581B3)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/9eWxKVzKSIiUX2kDU04dOA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF44BFD783BC945DFE39B304C53402FCD20ACF7C4FC495104BA31788C4ABFD92)

-   If "\[Fail\]ExecuteCommand need connect-key? please confirm a device by help info" is returned after the command is executed, multiple debugging devices may be connected or the Emulator and real device are used at the same time.
    -   If both the Emulator and real device are connected, disconnect the Emulator.
    -   If multiple devices are connected, you need to use the **\-t** parameter to specify the identifier of the target device each time when executing the command. You can run the **hdc list targets** command to query the connected devices, and then run the **hdc -t _connect-key_ shell param get const.ohos.apiversion** command to specify the target device to be connected. **connect-key** is the device identifier, that is, the information returned by the **hdc list targets** command.
