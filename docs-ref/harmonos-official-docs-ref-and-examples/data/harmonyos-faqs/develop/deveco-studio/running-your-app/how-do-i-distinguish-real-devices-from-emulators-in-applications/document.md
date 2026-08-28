# How do I distinguish real devices from emulators in applications?

**Symptom**

When debugging applications, you may need to distinguish real devices from emulators. In this case, you can check specific system attributes or environment variables.

**Solution**

In applications, you can use the **productModel** attribute of the [@ohos.deviceInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references-V5/js-apis-device-info-V5) module to distinguish real devices from emulators. For emulators, the value of **productModel** is **emulator**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/7FdrPtnsQYCMDDwC0LmOtg/en-us_image_0000002229603717.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37646AA44E4A60F4903F4B6331836773B12233BA677B58AE74EC061B0A356004 "Click to enlarge")
