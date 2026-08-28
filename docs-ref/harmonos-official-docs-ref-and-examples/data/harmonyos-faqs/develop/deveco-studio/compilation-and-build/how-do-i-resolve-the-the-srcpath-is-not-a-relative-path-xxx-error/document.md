# How do I resolve the "The srcPath is not a relative path: xxx" error?

**Symptom**

The value of **srcPath** must be a relative path.

**Possible Causes**

When the **includeNode** API is used in the **hvigorconfig.ts** file, **srcPath** must be a relative path.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/nCBT3scWR7670VZPd-sOZg/en-us_image_0000002229604333.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=011736B61546049CE5788481C9305CB5238E2B07269C9533744DEC8435D6CBD4)

**Solution**

Open the **hvigorconfig.ts** file, locate the **includeNode** API used to add the target module, and ensure that **srcPath** is specified as a relative path.

**Reference**

[Hvigor Script Files](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-life-cycle#section810245135914)
