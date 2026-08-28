# How do I resolve the "byteCodeHar not supported when useNormalizedOHMUrl is not true." error?

**Symptom**

The "byteCodeHar not supported when useNormalizedOHMUrl is not true." error is reported during compilation.

**Possible Causes**

The **byteCodeHar** field in the **build-profile.json5** file of the HAR module is set to **true**, but the **useNormalizedOHMUrl** field in the project-level **build-profile.json5** file is not set to **true**, which means bytecode HARs are not supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/Z-lQmAdvTbCHXlv3LmbxKQ/en-us_image_0000002194318416.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F94DDB00DBA87BB1D2BCDE3B5861704D79A70DE4111C22C41A18709A652795F)

**Solution**

When the **byteCodeHar** field in the **build-profile.json5** file of the HAR module is set to **true**, set the **useNormalizedOHMUrl** field in the project-level **build-profile.json5** file to **true**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/-fW_8eLnRNOEEyDxvutiYQ/en-us_image_0000002308297297.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67788D2CF8BF28011A3C8BBD249CBB6DC7FC217AA00AD295484C02A0AC240FAD)

**Reference**

[strictMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile-app#section13181758123312)
