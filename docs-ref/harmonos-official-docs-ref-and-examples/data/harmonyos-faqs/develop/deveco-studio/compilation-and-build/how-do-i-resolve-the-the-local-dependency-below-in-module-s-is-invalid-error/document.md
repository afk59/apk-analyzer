# How do I resolve the "The local dependency below in module %s is invalid." error?

**Symptom**

The local dependency added to the module is invalid.

**Possible Causes**

When **harLocalDependencyCheck** is set to **true**, external dependencies outside of the module directory are added to the HAR module and the compilation error is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/CJB-wFoQQ-WMEKq428TAKg/en-us_image_0000002194158324.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D6181EDE974A69343F9ECF1631EFF569B327F2B6E7A587AD4E3A8EC177AB732)

**Solution**

Open the **oh-package.json5** file in the module directory and make sure the dependencies listed under **dependencies** and **dynamicDependencies** are located within the current module directory.
