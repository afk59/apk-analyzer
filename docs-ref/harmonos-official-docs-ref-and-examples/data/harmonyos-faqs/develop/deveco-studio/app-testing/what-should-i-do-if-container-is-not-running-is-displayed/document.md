# What should I do if "container is not running" is displayed?

**Symptom**

When the **hdc -n shell param set persist.ace.testmode.enabled 1** command is executed on a HarmonyOS device, the error message "container is not running" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/cYrDFtvJRHmHXDQXSERvkQ/en-us_image_0000002194318268.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21388662F1535E8EE12396593AEEC9F5F85EAEEA770A103A3848B5427351A63D)

**Solution**

Run a test case in DevEco Studio. Push the package to the device. Then, run the **hdc -n shell param set persist.ace.testmode.enabled 1** command.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/oLdZ6LVwTgGe1IEIuQYfow/en-us_image_0000002194158644.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=120DB90601440684070C8B1ED0E29D4F236FE35A5A2E39B5C454C24A0F999497)
