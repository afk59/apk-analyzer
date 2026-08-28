# How do I resolve the "The type of target device does not match the device type configured by module: xxx" error?

**Symptom**

The "The type of target device does not match the device type configured by module: xxx" error is reported during compilation.

**Possible Causes**

The type of the specified target device does not match the device type configured for the module.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/4a6q0ZWYThurF_Ly6Tdwyw/en-us_image_0000002194158392.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8944EBEE56D497BFB9067CF0611A90621405E6B49DC85998E8C7A39C5EE0BB9)

**Solution**

1.  Make sure the device types specified under **targets** in the **build-profile.json5** file in the module directory contain the required device type.
2.  Make sure the **deviceTypes** field configured in **src/main/module.json5** in the module directory contains the required device type.
3.  Check whether the **hvigorfile.ts** or [Hvigor Script Files](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-life-cycle#section810245135914) contains any code that might modify the **deviceTypes** settings of the module. If such code exists, ensure that the final settings include the required device type.
