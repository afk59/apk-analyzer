# How do I resolve the "The required attribute: module-name is missing" error?

**Symptom**

The "The required attribute: module-name is missing" error is reported during compilation.

**Possible Causes**

1.  The module name is missing in the **build-profile.json5** file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/KNhYfHeqQdy4aD7A9nYqvw/en-us_image_0000002229758649.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C914A4180EFAA146C8560E5849CBE84368C925FBB3527970DE353D7D54819B7)
    
2.  The module name is not set when the module is dynamically added to the **hvigorconfig.ts** file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/Qe-BocpuTYeFUEVw3aXedg/en-us_image_0000002194158776.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B07D6FB2A58E7BC60AE90F153BD0A8B36EADD7A7C9E9C0032D94AD23C15E7841)

**Solution**

1.  Open the **build-profile.json5** file in the root directory of the project, and ensure that the **name** field exists under **module** and is not empty.
2.  Open the **hvigorconfig.ts** file in the root directory of the project and ensure that the **name** parameter of **includeNode** exists and is not empty.

**Reference**

[Hvigor Script Files](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-life-cycle#section810245135914)
