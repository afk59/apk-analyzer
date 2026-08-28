# What should I do if "ArkTS:WARN: For details about ArkTS syntax errors" is reported during compilation and build?

**Symptom**

What should I do if ArkTS syntax alarms are reported during project building?

Error message:

1.  ERROR: ArkTS:ERROR File: C:/Users/... ,Use "let" instead of "var" (arkts-no-var)
2.  ERROR: ArkTS:ERROR File: D:/DTS/MyApplicationAPI12/... ,The "@Sendable" decorator can only be used on "class", "function" and "typeAlias" (arkts-sendable-decorator-limited)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/qFnTEZxlTwO-YvdKMUMJ9A/en-us_image_0000002429325678.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90D836E48E3BD274C0F7BB50B12544FD2C68C1C2687DB96D22CD890E2998E255)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/KaY5VTkeTeuiov32BduEXw/en-us_image_0000002429485750.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B060165D173D5639EF515E9882B92AD37DFB92EAF0F94AF12A787599CD4B0BCB)

**Solution**

This error indicates that the code contains elements that do not comply with the ArkTS syntax specifications. To address this, refer to the information in the error message to identify the specific issues, or search for corresponding explanations on this website based on the provided syntax rules (such as arkts-no-var and arkts-sendable-decorator-limited), and modify the code to conform to the ArkTS syntax specifications. For details about ArkTS, see [ArkTS](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts).
