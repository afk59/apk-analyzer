# What should I do if "Duplicated files found in module entry. This may cause unexpected errors at runtime." is reported during compilation and build?

**Symptom**

The error "Duplicated files found in module entry. This may cause unexpected errors at runtime." is reported during compilation and build.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/pRtJr1A_SjmBRu7cSc5Dcw/en-us_image_0000002229603833.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CBE00476031EF9712A73EA0B9D866706639C8C843D6C47AF32DE8AFF85E1237 "Click to enlarge")

**Solution**

This error message indicates that .so packages with the same name are collected from different packages, resulting in .so package conflicts. You can set the **enableOverride** field to the module-level **build-profile.json5** file and set this field to **true**. For details, see [Module-level build-profile.json5 File](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-build-profile).

"buildOption": {
  "nativeLib": {
    "filter": {
      "enableOverride": true
    }
  }
},
