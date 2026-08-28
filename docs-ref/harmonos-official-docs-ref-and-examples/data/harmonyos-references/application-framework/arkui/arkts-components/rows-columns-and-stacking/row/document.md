# Row

The **Row** component lays out child components horizontally.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/H5tu_GbqTS6RXfTDcWPHEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBA0F653261B172C30E9F7189B53C248388EBE36F3D1B72FC4BEDFEDF6D89D9D)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

If no width or height is set for the **Row** component, the component automatically adapts to the size of its child components in the main axis and cross axis respectively.

#### Child Components

Supported

#### APIs

#### \[h2\]Row

Row(options?: RowOptions)

Creates a horizontal linear layout container. You can set the spacing between child components.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/p43DtK5OQ-meHp0m1A6dDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83B0426C1B046AC44663C956C2270E65D6EE3A3EBAC217F0BAC0002B278DE554)

Excessive component nesting (either too deep a hierarchy or too many nested components) incurs significant performance overhead. For performance purposes, you are advised to remove redundant nodes to simplify the component tree, use layout boundaries to reduce redundant layout calculations, properly apply rendering control syntax and layout component methods to minimize unnecessary re-renders and computations. For details about the best practices, see [Layout Optimization](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-improve-layout-performance).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options18+ | [RowOptions](#rowoptions18) | No | Spacing between elements in the horizontal layout. The value can be of the number or string type. |

#### \[h2\]Row18+

Row(options?: RowOptions | RowOptionsV2)

Creates a horizontal linear layout container. You can set the spacing between child components.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RowOptions](#rowoptions18) | [RowOptionsV2](#rowoptionsv218) | No | Spacing between elements in a horizontal layout. The value can be of the number, string, or Resource type. |

#### RowOptions18+

Sets the spacing between child components of the **Row** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/oIbi4e86RYmBZFLqCsr9yA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CC96B30E91185566F9AF664492D6BED4958B2B2FA61077768DE0EA1CBD753D4)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| space7+ | string | number | No | Yes | 
Spacing between child components.

Since API version 9, this parameter does not take effect when it is set to a negative number or when **justifyContent** is set to **FlexAlign.SpaceBetween**, **FlexAlign.SpaceAround** or **FlexAlign.SpaceEvenly**.

Default value: **0**, in vp

Invalid values are treated as the default value.

**NOTE**

The value of **space** can be a number greater than or equal to 0 or a string that can be converted to a number.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### RowOptionsV218+

Sets the spacing between child components of the **Row** component. The spacing type **SpaceType** can be number, string, or Resource.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| space | [SpaceType](../column/document.md#spacetype18) | No | Yes | 
Spacing between child components.

This parameter does not take effect if the value specified is a negative number, or if **justifyContent** is set to **FlexAlign.SpaceBetween**, **FlexAlign.SpaceAround**, or **FlexAlign.SpaceEvenly**.

Default value: **0**, in vp

Invalid values are treated as the default value.

**NOTE**

The value of **space** can be a number greater than or equal to 0, a string that can be converted to a number, or a Resource type that can be converted to a number.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]alignItems

alignItems(value: VerticalAlign)

Sets the alignment mode of child components in the vertical direction.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [VerticalAlign](../../common-definitions/enums/document.md#verticalalign) | Yes | 
Alignment mode of child components in the vertical direction.

Default value: **VerticalAlign.Center**

 |

#### \[h2\]justifyContent8+

justifyContent(value: FlexAlign)

Sets the alignment mode of the child components in the horizontal direction.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [FlexAlign](../../common-definitions/enums/document.md#flexalign) | Yes | 
Alignment mode of child components in the horizontal direction.

Default value: **FlexAlign.Start**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/50OeyplwQ62i4Wx1pC0rjg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AFD2A00CBAC3509E09F8E05370EBF256559EEB9102C29EB622D442E2783D2E92)

During the row layout, if [flexShrink](../../universal-attributes/layout-and-borders/flex-layout/document.md#flexshrink) is not set for a child component, the child component is not compressed by default. This can result in the total main axis size of all child components exceeding the container's main axis size, which makes **FlexAlign.Center** and **FlexAlign.End** ineffective.

#### \[h2\]reverse12+

reverse(isReversed: Optional<boolean>)

Sets whether to reverse the horizontal arrangement of child components.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isReversed | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to reverse the horizontal arrangement of child components.

Default value: **true**. **true**: Child components are arranged in reverse order horizontally. **false**: Child components are arranged in normal order horizontally.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/4TrsjZ7eQryszwnvwxIWVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2EC01042C5F1463D4E81FA2E79AEF17D060F0368D9505419959826D30B7BBFD5)

If the **reverse** attribute is not set, the arrangement on the main axis remains in the normal order. If the attribute is set to **undefined**, it defaults to **true**, which reverses the arrangement on the main axis.

Keep in mind that the main axis arrangement direction is also affected by the **direction** attribute. If **reverse** is set to **true**, it effectively reverses the arrangement that results from the **direction** attribute settings.

#### Events

The [universal events](../../universal-events/document.md) are supported.

#### Example

## Example 1: Setting the Layout Attributes of the Row Component

This example demonstrates how to set the layout attributes of the **Row** component, such as the spacing and alignment mode and its effect.

// resources/base/element/string.json
{
  "string": \[
    {
      "name": "stringSpace",
      "value": "5"
    }
  \]
}

// xxx.ets
@Entry
@Component
struct RowExample {
  build() {
    Column({ space: 5 }) {
      // Set the horizontal spacing between two adjacent child components to 5.
      Text('space').width('90%')
      Row({ space: 5 }) {
        Row().width('30%').height(50).backgroundColor(0xAFEEEE)
        Row().width('30%').height(50).backgroundColor(0x00FFFF)
      }.width('90%').height(107).border({ width: 1 })

      // Set the spacing between child components using the Resource type.
      Text('Resource space').width('90%')
      Row({ space: $r('app.string.stringSpace') }) {
        Row().width('30%').height(50).backgroundColor(0xAFEEEE)
        Row().width('30%').height(50).backgroundColor(0x00FFFF)
      }.width('90%').height(107).border({ width: 1 })

      // Set the alignment mode of the child components in the vertical direction.
      Text('alignItems(Bottom)').width('90%')
      Row() {
        Row().width('30%').height(50).backgroundColor(0xAFEEEE)
        Row().width('30%').height(50).backgroundColor(0x00FFFF)
      }.width('90%').alignItems(VerticalAlign.Bottom).height('15%').border({ width: 1 })

      Text('alignItems(Center)').width('90%')
      Row() {
        Row().width('30%').height(50).backgroundColor(0xAFEEEE)
        Row().width('30%').height(50).backgroundColor(0x00FFFF)
      }.width('90%').alignItems(VerticalAlign.Center).height('15%').border({ width: 1 })

      // Set the alignment mode of the child components in the horizontal direction.
      Text('justifyContent(End)').width('90%')
      Row() {
        Row().width('30%').height(50).backgroundColor(0xAFEEEE)
        Row().width('30%').height(50).backgroundColor(0x00FFFF)
      }.width('90%').border({ width: 1 }).justifyContent(FlexAlign.End)

      Text('justifyContent(Center)').width('90%')
      Row() {
        Row().width('30%').height(50).backgroundColor(0xAFEEEE)
        Row().width('30%').height(50).backgroundColor(0x00FFFF)
      }.width('90%').border({ width: 1 }).justifyContent(FlexAlign.Center)
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/r53LQZO2SwG-TFM5bohA6w/en-us_image_0000002568765227.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E75B0E73FFBBA67AD54C979F94A87C2C06C7D6B661CC27656239956882D356AA)

## Example 2: Configuring the Reverse Attribute

This example demonstrates how to set the **reverse** attribute of the **Row** component and its effect.

@Entry
@Component
struct RowReverseSample {
  build() {
    Row() {
      Text("1")
        .width(100)
        .height(50)
        .backgroundColor(0xAFEEEE)

      Text("2")
        .width(100)
        .height(50)
        .backgroundColor(0x00FFFF)
    }
    .height(100)
    .width(300)
    .border({ width: 1 })
    .reverse(true)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/-hlE_LccTSS0L4uTmTB4qg/en-us_image_0000002537765502.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA64A1633D8C7177FFD876BA0E09FFBB8980A5C30A7AE5A22ACAF93C69F390F5)
