# Blank

The **Blank** component is a spacer in the layout, automatically filling the remaining space along the main axis of its parent container. It works only when the parent component is [Row](../../rows-columns-and-stacking/row/document.md), [Column](../../rows-columns-and-stacking/column/document.md), or [Flex](../../rows-columns-and-stacking/flex/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/X2gun6fWSO2mUrDWahNSnQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91F289CADF86F4A5ADA296F1AC27979CD6193B19B8835C3A278B2BB9E3FA76D7)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

Blank(min?: number | string)

Creates a **Blank** component.

Since API version 10:

-   When the **Blank** component is used within a [Row](../../rows-columns-and-stacking/row/document.md), [Column](../../rows-columns-and-stacking/column/document.md), or [Flex](../../rows-columns-and-stacking/flex/document.md) container, it will automatically stretch or shrink along the main axis if it does not have a main axis size specified. If the **Blank** component has a main axis size specified or if the container is set to adapt to the size of its child nodes, the component will not automatically stretch or shrink.
-   Relationship between **size** and **min** of the **Blank** component on the main axis: max(min, size).
-   If the **Blank** component has a cross axis size specified, it will not fill up the parent container on the cross axis. If it does not have a cross axis size specified, it will fill up the parent container on the cross axis, following the **ItemAlign.Stretch** mode, the default setting of **alignSelf**.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| min | number | string | No | 
Minimum size of the **Blank** component in the container along the main axis.

Default value: **0**

If the type is number, the default unit is vp. If the type is string, the [pixel unit](../../common-definitions/pixel-units/document.md) can be explicitly specified, for example, '**10px'**. If the unit is not specified, the default unit vp is used, in which case **'10'** is equivalent to **10vp**.

Invalid values are treated as the default value.

**NOTE**

This parameter cannot be set in percentage. If the value is negative, the default value is used. If the minimum size is larger than the available space of the container, it is used as the component size, and the component extends beyond the container.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]color

color(value: ResourceColor)

Sets the fill color of the **Blank** component. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Color to fill the blank.

Default value: **Color.Transparent**

Invalid values are treated as the default value.

 |

#### Events

The [universal events](../../universal-events/document.md) are supported.

#### Example

## Example 1: Filling Remaining Space

This example shows how the **Blank** component fills the remaining space in landscape and portrait modes.

// xxx.ets
@Entry
@Component
struct BlankExample {
  build() {
    Column() {
      Row() {
        Text('Bluetooth').fontSize(18)
        Blank()
        Toggle({ type: ToggleType.Switch }).margin({ top: 14, bottom: 14, left: 6, right: 6 })
      }.width('100%').backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 })
    }.backgroundColor(0xEFEFEF).padding(20)
  }
}

Portrait mode

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/-7qQU6kRT3iUaU-HNsQMSg/en-us_image_0000002537925736.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A3423BECC50BE2A6620D89A095617DBFF2C10CDF791F05D69EFA408919C21ED2)

Landscape mode

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/-qydjnbER72MPSRvQUd4Rw/en-us_image_0000002568685513.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05DB1BB892A0788F852B9194F032E7D91F1611EF097ECBE78FFD147CD0F046C2)

## Example 2: Filling a Fixed Width

This example shows the effect of using the **min** parameter of the **Blank** component when its parent component does not have a width set.

// xxx.ets
@Entry
@Component
struct BlankExample {
  build() {
    Column({ space: 20 }) {
      // If the width of the parent container is not set, the Blank component becomes invalid. In this case, you can set min to specify the minimum width.
      Row() {
        Text('Bluetooth').fontSize(18)
        Blank().color(Color.Yellow)
        Toggle({ type: ToggleType.Switch }).margin({ top: 14, bottom: 14, left: 6, right: 6 })
      }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 })

      Row() {
        Text('Bluetooth').fontSize(18)
        // Set the minimum width to 160.
        Blank('160').color(Color.Yellow)
        Toggle({ type: ToggleType.Switch }).margin({ top: 14, bottom: 14, left: 6, right: 6 })
      }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 })

    }.backgroundColor(0xEFEFEF).padding(20).width('100%')
  }
}

If the width of the parent container is not set, set **min** to specify the minimum width of the **Blank** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/6ej8rq5bQe-mpGh69cea5w/en-us_image_0000002568765523.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E36E24201758BEE52C32F2E55B155F1DDC2D0C0DD28F42CB05B301CA05FB7411)
