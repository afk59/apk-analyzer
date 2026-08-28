# How do I resolve the "useNormalizedOHMUrl can be true only when Compatible SDK Version is 5.0.0 (12) or later" error?

**Symptom**

The "useNormalizedOHMUrl can be true only when Compatible SDK Version is 5.0.0 (12) or later" error is reported during compilation.

**Possible Causes**

This is because **useNormalizedOHMurl** is incorrectly set to **true** when **compatibleSdkVersion** is earlier than 5.0.0(12).

**Solution**

Check the **compatibleSdkVersion** configuration in the project-level **build-profile.json5** file. If it is 4.1.0(11) or an earlier version, set [useNormalizedOHMUrl](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-build-profile-app#section13181758123312) to **false**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/pBk9oWHWRpi-qPvypM4Zpg/en-us_image_0000002363676020.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F113795D87E970A42247006FE6F92E3319EB9B7E1923DE664D21DCB5868BE3D2)
