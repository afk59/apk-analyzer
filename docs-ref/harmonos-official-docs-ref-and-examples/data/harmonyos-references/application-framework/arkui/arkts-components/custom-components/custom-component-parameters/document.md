# Custom Component Parameters

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/Do4JG1LERV67Blh25ock3Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A810B0B9FD899DA7CDB69DEE9F46E624A1135E85811F6C231647D825AAB5FC71)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### ComponentOptions

Defines the custom component parameters used to configure whether component freezing is supported.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/Jc-2OY3_RRO00gbIlWLxVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FAC476BB4310748CE10D984499894A68780208CF4130145700DB51266802644C)

Since API version 11, this parameter can be used to configure component freezing for [@Component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-create-custom-components#component). For implementation examples, see [Freezing a Custom Component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-custom-components-freeze).

Since API version 12, this parameter can be used to configure component freezing for [@ComponentV2](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-create-custom-components#componentv2). For implementation examples, see [Freezing a Custom Component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-custom-components-freezev2).

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| freezeWhenInactive | boolean | No | No | Whether to enable component freezing. The value **true** means to enable component freezing, and **false** means the opposite. If **ComponentOptions** is not specified, the default value **false** is used. |
