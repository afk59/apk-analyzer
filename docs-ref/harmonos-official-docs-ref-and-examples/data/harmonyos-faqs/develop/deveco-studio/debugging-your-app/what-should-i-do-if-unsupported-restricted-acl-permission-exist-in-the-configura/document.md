# What should I do if "Unsupported restricted ACL permission exist in the configuration" is displayed during automatic signing of a HarmonyOS application?

**Symptom**

When **Automatically generate signature** is selected in the HarmonyOS application project, the error message "Unsupported restricted ACL permission exist in the configuration" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/t-Qgv4WLS8Ou8VEFGdeqUw/en-us_image_0000002250504069.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80FE3E9D6C8A69439F7A50960A511159AE7D27BD5C84FC54CD5CF403CE50C517)

**Solution**

The DevEco Studio automatic signature supports only some ACL permissions. The current project uses ACL permissions that are not supported. You are advised to use manual signing.

**Reference**

[ACL Permissions Supported by Automatic Signing](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-signing#section5301916183411)

[Signing Your App/Service Manually](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-signing#section297715173233)
