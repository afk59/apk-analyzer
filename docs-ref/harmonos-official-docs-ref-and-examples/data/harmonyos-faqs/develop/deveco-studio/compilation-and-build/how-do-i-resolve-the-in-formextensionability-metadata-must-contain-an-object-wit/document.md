# How do I resolve the "In FormExtensionAbility, metadata must contain an object with its name set to 'ohos.extension.form' and resource set to a second-level resource reference." error?

**Symptom**

The "In FormExtensionAbility, metadata must contain an object with its name set to 'ohos.extension.form' and resource set to a second-level resource reference." error is reported during compilation.

**Possible Causes**

The **metadata** field in the ExtensionAbility of the form type in the **module.json5** file does not contain an object with the name **ohos.extension.form** or does not include the **resource** field.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/DkgCZxFwT7-7YQ0JLfuNXQ/en-us_image_0000002229758517.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=768673962BC24897EC02522AD923F70180297B01C4E9595C8FF9B2B8EB46F2B4)

**Solution**

Make sure the **metadata** field contains an object with the name **ohos.extension.form** and a valid **resource** field. For details about the configuration instructions, see [Configuring ArkTS Widget Configuration Files](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-ui-widget-configuration).
