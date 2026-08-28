# Information Display APIs

Provides APIs for displaying information in [Gauge](../gauge/document.md) and [DataPanel](../datapanel/document.md) components.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/4aXO0Ss8Sa2XUtyZxPOO0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B18787F92AFDE013A8267DA9454EFBEE02D4B832A5922C5A001FF2FB2EA6D02)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### MultiShadowOptions

Defines shadow style properties.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| radius | number | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 
Shadow blur radius.

The default value varies by API version.

API version 10 and earlier versions: **5**

Since API version 11: **20**

Unit: vp.

The value of the number type must be greater than 0.

**NOTE**

A value less than or equal to 0 is handled as the default value.

 |
| offsetX | number | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 

X-axis offset.

There is no value range restriction for the number type.

Default value: **5**

Unit: vp.

 |
| offsetY | number | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 

Y-axis offset.

There is no value range restriction for the number type.

Default value: **5**

Unit: vp.

 |
