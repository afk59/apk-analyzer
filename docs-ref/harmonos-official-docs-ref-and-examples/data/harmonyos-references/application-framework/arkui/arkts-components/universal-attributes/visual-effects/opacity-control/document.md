# Opacity Control

You can set the opacity of a component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/tQtkxQzpSsaZPPvDZu_Rcw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98FEB1DFA87D635CC427CC989257ED0F355A8716E7DBB35F3123934730344A38)

The initial APIs of this module are supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### opacity

opacity(value: number | Resource): T

Sets the opacity of the component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [Resource](../../../common-definitions/basic-types/document.md#resource) | Yes | 
Component opacity. Value range: 0 to 1. Values less than 0 are treated as 0. Values greater than 1 are treated as 1. **1**: fully opaque. **0**: fully transparent (where the component is hidden but occupies layout space).

Default value: **1**.

**NOTE**

Child components inherit parent opacity and combine with their own opacity. Example: Parent opacity 0.1 x Child opacity 0.8 = Effective opacity 0.08.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### opacity18+

opacity(opacity: Optional<number | Resource>): T

Sets the opacity of the component. Compared with [opacity](#opacity), this API supports the **undefined** type for the **opacity** parameter.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| opacity | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<number | [Resource](../../../common-definitions/basic-types/document.md#resource)\> | Yes | 
Component opacity. Value range: 0 to 1. Values less than 0 are treated as 0. Values greater than 1 are treated as 1. **1**: fully opaque. **0**: fully transparent (where the component is hidden but occupies layout space).

Default value: **1**.

**NOTE**

Child components inherit parent opacity and combine with their own opacity. Example: Parent opacity 0.1 x Child opacity 0.8 = Effective opacity 0.08.

When **opacity** is **undefined**, the component reverts to the default opacity of **1**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Example

This example shows how to set the opacity of a component using [opacity](#opacity).

// xxx.ets
@Entry
@Component
struct OpacityExample {
  build() {
    Column({ space: 5 }) {
      Text('opacity(1)').fontSize(9).width('90%').fontColor(0xCCCCCC)
      Text().width('90%').height(50).opacity(1).backgroundColor(0xAFEEEE)
      Text('opacity(0.7)').fontSize(9).width('90%').fontColor(0xCCCCCC)
      Text().width('90%').height(50).opacity(0.7).backgroundColor(0xAFEEEE)
      Text('opacity(0.4)').fontSize(9).width('90%').fontColor(0xCCCCCC)
      Text().width('90%').height(50).opacity(0.4).backgroundColor(0xAFEEEE)
      Text('opacity(0.1)').fontSize(9).width('90%').fontColor(0xCCCCCC)
      Text().width('90%').height(50).opacity(0.1).backgroundColor(0xAFEEEE)
      Text('opacity(0)').fontSize(9).width('90%').fontColor(0xCCCCCC)
      Text().width('90%').height(50).opacity(0).backgroundColor(0xAFEEEE)
    }
    .width('100%')
    .padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/td6Y_TRRTtq5mV9F40HCYg/en-us_image_0000002537765418.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A04BA8AE33F7B01E6E280FC00FC0EF0468DFF705969F172E3DD760FDA0B5783E)
