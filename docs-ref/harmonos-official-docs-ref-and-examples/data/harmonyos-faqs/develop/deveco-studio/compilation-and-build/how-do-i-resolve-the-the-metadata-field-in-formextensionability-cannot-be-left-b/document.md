# How do I resolve the "The metadata field in FormExtensionAbility cannot be left blank or as an empty array." error?

**Symptom**

The "The metadata field in FormExtensionAbility cannot be left blank or as an empty array." error is reported during compilation.

**Possible Causes**

The **metadata** field in the ExtensionAbility of the form type in the **module.json5** file is either empty or set as an empty array.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/xlI1TSttS1Cc3msfnO-pIA/en-us_image_0000002194158712.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=17B63DA35129056F28AC417A209046661D79466079A5DAB8F6C693C96BF06E92)

**Solution**

Make sure the **metadata** field is not empty and is not set as an empty array. For details about the configuration instructions, see [Configuring ArkTS Widget Configuration Files](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-ui-widget-configuration).
