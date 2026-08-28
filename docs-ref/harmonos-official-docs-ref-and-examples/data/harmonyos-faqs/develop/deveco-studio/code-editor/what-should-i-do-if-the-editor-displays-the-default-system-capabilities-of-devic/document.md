# What should I do if the editor displays "The default system capabilities of devices wearable do not include SystemCapability.ArkUI.ArkUI.Circle" when using the ArcList component on DevEco Studio?

**Symptom**

When the **ArcList** component is used, the editor reports the following error.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/hA6q3eVFQiOS_ij4cI5FwA/en-us_image_0000002459313966.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AFE5ADA1EED5F527D7B01BE5F16DBD5C004360283EDB8FDE70AD750CC00A68D6)

**Solution**

1.  Go to the [download center](https://developer.huawei.com/consumer/en/download/) to update DevEco Studio to 6.0.1 Release or later.
2.  If you still need to use the current version, add the **syscap.json** configuration file to the **src/main** directory. For details, see the [SysCap development guide](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#how-to-develop).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/YJpDiIlTSkmeY-i-rMc_lg/en-us_image_0000002460277990.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA717C7F3E2C121073ED423486B894CCF2D92CB67256F284BED6A399F6B694F4)
