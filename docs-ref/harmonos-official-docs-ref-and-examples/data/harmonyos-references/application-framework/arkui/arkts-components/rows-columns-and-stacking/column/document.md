# Column

The **Column** component lays out child components vertically.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/nAwzk27SQ3WjKgc4QcmAvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67E865ACFC653938704C718F871BB50CBBB7495BFA17ADD31DEE05700FBBEE1A)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

If no height or width is set for the **Column** component, the component automatically adapts to the size of its child components in the main axis and cross axis respectively.

#### Child Components

Supported

#### APIs

#### \[h2\]Column

Column(options?: ColumnOptions)

Creates a vertical linear layout container. You can set the spacing between child components.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/sDgZUSnLRAK457QuuPgKUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BD2FB7ECED67A37E141D724324335C44EF8BC3274351BE402CA2F3E613E6461)

Excessive component nesting (either too deep a hierarchy or too many nested components) incurs significant performance overhead. For performance purposes, you are advised to remove redundant nodes to simplify the component tree, use layout boundaries to reduce redundant layout calculations, properly apply rendering control syntax and layout component methods to minimize unnecessary re-renders and computations. For details about the best practices, see [Layout Optimization](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-improve-layout-performance).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options18+ | [ColumnOptions](#columnoptions18) | No | Vertical spacing between two adjacent child components. The value can be of the number or string type. |

#### \[h2\]Column18+

Column(options?: ColumnOptions | ColumnOptionsV2)

Creates a vertical linear layout container. You can set the spacing between child components.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ColumnOptions](#columnoptions18) | [ColumnOptionsV2](#columnoptionsv218) | No | Vertical spacing between two adjacent child components. The value can be of the number, string, or Resource type. |

#### ColumnOptions18+

Sets the spacing between child components of the **Column** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/x4utZpwMS7WfTvxrkXpfWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6128ED328CE906A4C31A56EF720ECDDAAAC8BA01A40120757C6ACF911E77B536)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| space7+ | string | number | No | Yes | 
Vertical spacing between two adjacent child components.

This parameter has no effect if the value specified is a negative number, or if [justifyContent](#justifycontent8) is set to **FlexAlign.SpaceBetween**, **FlexAlign.SpaceAround**, or **FlexAlign.SpaceEvenly**

Default value: **0**

Invalid values are treated as the default value.

Unit: vp

**NOTE**

The value of **space** can be a number greater than or equal to 0 or a string that can be converted to a number.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### ColumnOptionsV218+

Sets the spacing between child components of the **Column** component. The spacing type **SpaceType** can be number, string, or Resource.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| space | [SpaceType](#spacetype18) | No | Yes | 
Vertical spacing between two adjacent child components.

This parameter has no effect if the value specified is a negative number, or if **justifyContent** is set to **FlexAlign.SpaceBetween**, **FlexAlign.SpaceAround**, or **FlexAlign.SpaceEvenly**.

Default value: **0**, in vp

Invalid values are treated as the default value.

**NOTE**

The value of **space** can be a number greater than or equal to 0, a string that can be converted to a number, or a Resource type that can be converted to a number.

 |

#### SpaceType18+

type SpaceType = string | number | Resource

Describes the supported data types for the **space** parameter in the constructors of the **Column** component. The type is a union of the following types.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| number | Represents a numeric value. It can take any numerical value. |
| string | Represents a string value. It can take any string value. |
| [Resource](../../common-definitions/basic-types/document.md#resource) | Represents a resource reference type. It can take values from system resources or application resources. |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]alignItems

alignItems(value: HorizontalAlign)

Alignment mode of the child components in the horizontal direction.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [HorizontalAlign](../../common-definitions/enums/document.md#horizontalalign) | Yes | 
Alignment mode of child components in the horizontal direction.

Default value: **HorizontalAlign.Center**

 |

#### \[h2\]justifyContent8+

justifyContent(value: FlexAlign)

Alignment mode of the child components in the vertical direction.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [FlexAlign](../../common-definitions/enums/document.md#flexalign) | Yes | 
Alignment mode of child components in the vertical direction.

Default value: **FlexAlign.Start**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/CEAhQoxcRdGzp-XTNq0Y-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6C98F0171B38EF04D76DE3568B0045986CCC488DA0B7DCA64C93004B65E24A3)

During the column layout, if [flexShrink](../../universal-attributes/layout-and-borders/flex-layout/document.md#flexshrink) is not set for a child component, the child component is not compressed by default. This can result in the total main axis size of all child components exceeding the container's main axis size, which makes **FlexAlign.Center** and **FlexAlign.End** ineffective.

#### \[h2\]reverse12+

reverse(isReversed: Optional<boolean>)

Sets whether to reverse the vertical arrangement of child components.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isReversed | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to reverse the vertical arrangement of child components.

Default value: **true**. **true**: Child components are arranged in reverse order vertically. **false**: Child components are arranged in normal order vertically.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/kjGbyDi9ShSQamFWKgBnDg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2DAFD164C6F298D2DA7524327C283C8800081B8B38C25FD70A66A76C44F3B6E)

If the **reverse** attribute is not set, the arrangement on the main axis remains in the normal order. If the attribute is set to **undefined**, it defaults to **true**, which reverses the arrangement on the main axis.

The **direction** attribute only changes the cross axis direction of the column and does not impact the main axis direction. Therefore, it is independent of the **reverse** attribute.

#### Events

The [universal events](../../universal-events/document.md) are supported.

#### Example

## Example 1: Setting the Layout Attributes of the Column Component

This example demonstrates how to set the layout attributes of the **Column** component, such as the spacing and alignment mode and its effect.

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
struct ColumnExample {
  build() {
    Scroll() {
      Column({ space: 5 }) {
        // Set the vertical spacing between two adjacent child components to 5.
        Text('space').width('90%')
        Column({ space: 5 }) {
          Column().width('100%').height(30).backgroundColor(0xAFEEEE)
          Column().width('100%').height(30).backgroundColor(0x00FFFF)
        }.width('90%').height(100).border({ width: 1 })

        // Set the spacing between child elements using the Resource type.
        Text('Resource space').width('90%')
        Column({ space: $r('app.string.stringSpace') }) {
          Column().width('100%').height(30).backgroundColor(0xAFEEEE)
          Column().width('100%').height(30).backgroundColor(0x00FFFF)
        }.width('90%').height(100).border({ width: 1 })

        // Set the alignment mode of the child components in the horizontal direction.
        Text('alignItems(Start)').width('90%')
        Column() {
          Column().width('50%').height(30).backgroundColor(0xAFEEEE)
          Column().width('50%').height(30).backgroundColor(0x00FFFF)
        }.alignItems(HorizontalAlign.Start).width('90%').border({ width: 1 })

        Text('alignItems(End)').width('90%')
        Column() {
          Column().width('50%').height(30).backgroundColor(0xAFEEEE)
          Column().width('50%').height(30).backgroundColor(0x00FFFF)
        }.alignItems(HorizontalAlign.End).width('90%').border({ width: 1 })

        Text('alignItems(Center)').width('90%')
        Column() {
          Column().width('50%').height(30).backgroundColor(0xAFEEEE)
          Column().width('50%').height(30).backgroundColor(0x00FFFF)
        }.alignItems(HorizontalAlign.Center).width('90%').border({ width: 1 })

        // Set the alignment mode of the child components in the vertical direction.
        Text('justifyContent(Center)').width('90%')
        Column() {
          Column().width('90%').height(30).backgroundColor(0xAFEEEE)
          Column().width('90%').height(30).backgroundColor(0x00FFFF)
        }.height(100).border({ width: 1 }).justifyContent(FlexAlign.Center)

        Text('justifyContent(End)').width('90%')
        Column() {
          Column().width('90%').height(30).backgroundColor(0xAFEEEE)
          Column().width('90%').height(30).backgroundColor(0x00FFFF)
        }.height(100).border({ width: 1 }).justifyContent(FlexAlign.End)
      }.width('100%').padding({ top: 5 })
    }.width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/9PmZdaiLTBaqyP_qW5oouQ/en-us_image_0000002537925440.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B629BCF824D092AF5C34013ADDF513A9D049D86A1CA2F6F0DA5037B821861343)

## Example 2: Configuring the Reverse Attribute

This example demonstrates how to set the **reverse** attribute of the **Column** component and its effect.

@Entry
@Component
struct ColumnReverseSample {
  build() {
    Column() {
      Text("1")
        .width(50)
        .height(100)
        .backgroundColor(0xAFEEEE)

      Text("2")
        .width(50)
        .height(100)
        .backgroundColor(0x00FFFF)
    }
    .height(300)
    .width(100)
    .border({ width: 1 })
    .reverse(true)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/SHugyhv5T8en47x-0fqXFA/en-us_image_0000002568685217.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062237Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9ADE15380F6645D5C7425243F28A06938144F23D87482B2984D3A424D35CEE25)
