# Rect

The **Rect** component is used to draw a rectangle.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/QCRfoRWBRcuRkS_XL6ZMAw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D2CE8FA7C9FA97842C26A221A961D56F9218B24299C966971CE10EA61A70BA1)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

This component supports dynamic constructor parameter updates using the [updateConstructorParams](../../../arkts-api/ui/arkui/attributeupdater/document.md#properties) API of the [AttributeUpdater](../../../arkts-api/ui/arkui/attributeupdater/document.md) class since API version 20.

#### Child Components

None

#### APIs

Rect(options?: RectOptions | RoundedRectOptions)

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RectOptions](#rectoptions18) | [RoundedRectOptions](#roundedrectoptions18) | No | 
Options of the rectangle.

The **undefined** and **null** values are treated as invalid and will not take effect.

 |

#### RectOptions18+

Describes the options of the rectangle.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/alqeqnwIT-Kpccu2MtjiAw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD383EF88DCBC044BAACDC1936FC5FFF032ABF80C5457E8964548176E99E1E40)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width7+ | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 
Width. The value must be greater than or equal to 0.

Default value: **0**

Default unit: vp

The **undefined**, **null**, **NaN**, and **Infinity** values are invalid and treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| height7+ | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Height. The value must be greater than or equal to 0.

Default value: **0**

Default unit: vp

The **undefined**, **null**, **NaN**, and **Infinity** values are invalid and treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| radius7+ | [Length](../../common-definitions/basic-types/document.md#length) | Array<any> | No | Yes | 

Radius of the rounded corner. You can set separate radii for the four rounded corners. The value must be greater than or equal to 0.

This attribute takes precedence over **radiusWidth** and **radiusHeight** when used together.

Default value: **0**

Default unit: vp

The **undefined**, **null**, **NaN**, and **Infinity** values are invalid and treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### RoundedRectOptions18+

Describes the options of the rounded rectangle.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/IYjWUfgHQMeuFw9cRa5Hcw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39C061887DD325A9F8D1B29AE22A9A6D0F22CB7438D781849666640BC86BCF59)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width7+ | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 
Width. The value must be greater than or equal to 0.

Default value: **0**

Default unit: vp

Invalid values are treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| height7+ | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Height. The value must be greater than or equal to 0.

Default value: **0**

Default unit: vp

Invalid values are treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| radiusWidth7+ | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Width of the rounded corner. The value must be greater than or equal to 0.

Default value: **0**

Default unit: vp

Invalid values are treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| radiusHeight7+ | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Height of the rounded corner. The value must be greater than or equal to 0.

Default value: **0**

Default unit: vp

Invalid values are treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]radiusWidth

radiusWidth(value: Length)

Sets the width of the rounded corner. The width and height are the same when only the width is set. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier). Invalid values are treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Width of the rounded corner. The value must be greater than or equal to 0.

Default value: **0**

Default unit: vp

The **undefined** value is invalid and treated as the default value.

 |

#### \[h2\]radiusHeight

radiusHeight(value: Length)

Sets the height of the rounded corner. The width and height are the same when only the height is set. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier). Invalid values are treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Height of the rounded corner. The value must be greater than or equal to 0.

Default value: **0**

Default unit: vp

The **undefined** value is invalid and treated as the default value.

 |

#### \[h2\]radius

radius(value: Length | Array<any>)

Sets the radius of the rounded corner. The value must be greater than or equal to 0. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier). Invalid values are treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Array<any> | Yes | 
Radius of the rounded corner. You can set separate radii for the four rounded corners.

Default value: **0**

Default unit: vp

Invalid values **undefined** and **null** are treated as **\[\[0, 0\], \[0, 0\], \[0, 0\], \[0, 0\]\]**.

 |

#### \[h2\]fill

fill(value: ResourceColor)

Sets the color of the fill area. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier). Invalid values are treated as the default value. If this attribute and the universal attribute **foregroundColor** are both set, whichever is set later takes effect.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Color of the fill area.

Default value: [Color](../../common-definitions/enums/document.md#color).Black

The **undefined**, **null**, **NaN**, and **Infinity** values are invalid and treated as the default value.

 |

#### \[h2\]fillOpacity

fillOpacity(value: number | string | Resource)

Sets the opacity of the fill area. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Opacity of the fill area.

**NOTE**

For the number type, the value range is \[0.0, 1.0\]. A value less than 0.0 is treated as **0.0**. A value greater than 1.0 is treated as **1.0**. Any other value is treated as **1.0**.

For the string type, the value is a character string of the number type. The value range is the same as that of the number type.

For the Resource type, the value is a character string from the system resource or application resource. The value range is the same as that of the number type.

Invalid value **NaN** is treated as **0.0**, while invalid values **undefined**, **null**, and **Infinity** are treated as **1.0**.

Default value: **1.0**

 |

#### \[h2\]stroke

stroke(value: ResourceColor)

Sets the stroke color. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier). If this attribute is not set, the default stroke opacity is **0**, meaning no stroke is displayed.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Stroke color.

Default value: [Color](../../common-definitions/enums/document.md#color).Transparent

Invalid values **undefined** and **null** values are treated as the default value, and invalid values **NaN** and **Infinity** are treated as [Color](../../common-definitions/enums/document.md#color).Black.

 |

#### \[h2\]strokeDashArray

strokeDashArray(value: Array<any>)

Sets the stroke dashes. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier). The value must be greater than or equal to 0. Invalid values are treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Array<any> | Yes | 
Array defining the dash pattern for the rectangular outline. Elements alternate between dash length and gap length.

Default value: **\[\]** (empty array)

Default unit: vp

The **undefined** and **null** values are invalid and treated as the default value.

**NOTE**

Empty array: solid line

Even-numbered array: Elements cycle sequentially, for example, \[a, b, c, d\] represents: dash a -> gap b -> dash c -> gap d -> dash a -> ...

Odd-numbered array: Elements are duplicated to create an even-numbered array, for example, \[a, b, c\] becomes \[a, b, c, a, b, c\], representing: dash a -> gap b -> dash c -> gap a -> dash b -> gap c -> dash a -> ...

 |

#### \[h2\]strokeDashOffset

strokeDashOffset(value: number | string)

Sets the offset of the start point for drawing the stroke. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier). Invalid values are treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | Yes | 
Offset of the start point for drawing the stroke.

Default value: **0**

Default unit: vp

Invalid values **undefined** and **null** are treated as the default value. If set to **NaN** or **Infinity**, **strokeDashArray** has no effect.

 |

#### \[h2\]strokeLineCap

strokeLineCap(value: LineCapStyle)

Sets the cap style of the stroke. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [LineCapStyle](../../common-definitions/enums/document.md#linecapstyle) | Yes | 
Cap style of the stroke.

Default value: **LineCapStyle.Butt**

The **undefined**, **null**, **NaN**, and **Infinity** values are invalid and treated as the default value.

 |

#### \[h2\]strokeLineJoin

strokeLineJoin(value: LineJoinStyle)

Sets the join style of the stroke. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [LineJoinStyle](../../common-definitions/enums/document.md#linejoinstyle) | Yes | 
Join style of the stroke.

Default value: **LineJoinStyle.Miter**

The **undefined**, **null**, **NaN**, and **Infinity** values are invalid and treated as the default value.

 |

#### \[h2\]strokeMiterLimit

strokeMiterLimit(value: number | string)

Sets the limit on the ratio of the miter length to the value of stroke width used to draw a miter join. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier). The miter length indicates the distance from the outer tip to the inner corner of the miter. The border width is the value of **strokeWidth**. This attribute works only when **strokeLineJoin** is set to **LineJoinStyle.Miter**.

The value must be greater than or equal to 1.0. If the value is in the \[0, 1) range, the value **1.0** will be used. In other cases, the default value will be used.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | Yes | 
Limit on the ratio of the miter length to the value of **strokeWidth** used to draw a miter join.

Default value: **4**

Invalid values **undefined**, **null**, and **NaN** are treated as the default value. If set to **Infinity**, **stroke** has no effect.

 |

#### \[h2\]strokeOpacity

strokeOpacity(value: number | string | Resource)

Sets the stroke opacity. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier). The value range is \[0.0, 1.0\]. If the set value is less than 0.0, **0.0** will be used. If the set value is greater than 1.0, **1.0** will be used.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Stroke opacity.

Default value: opacity set by the [stroke](#stroke) API

Invalid value **NaN** is treated as **0.0**, while invalid values **undefined**, **null**, and **Infinity** are treated as **1.0**.

 |

#### \[h2\]strokeWidth

strokeWidth(value: Length)

Sets the stroke width. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier). If this attribute is of the string type, percentage values are not supported and will be treated as 1 px.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Stroke width. The value must be greater than or equal to 0.

Default value: **1**

Default unit: vp

Invalid values **undefined**, **null**, and **NaN** are treated as the default value, and invalid value **Infinity** is treated as **0**.

 |

#### \[h2\]antiAlias

antiAlias(value: boolean)

Sets whether to enable anti-aliasing. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether anti-aliasing is enabled.

**true**: enable anti-aliasing; **false**: disable anti-aliasing.

Default value: **true**

Invalid values **undefined** and **null** are treated as **false**.

 |

#### Examples

## Example 1: Drawing a Rectangle

This example demonstrates how to use **fill**, **fillOpacity**, **stroke**, and **radius** to draw rectangles with specific fill colors, opacity, stroke colors, and rounded corners.

// xxx.ets
@Entry
@Component
struct RectExample {
  build() {
    Column({ space: 10 }) {
      Text('normal').fontSize(11).fontColor(0xCCCCCC).width('90%')
      // Draw a 90% × 50 rectangle.
      Column({ space: 5 }) {
        Text('normal').fontSize(9).fontColor(0xCCCCCC).width('90%')
        // Draw a 90% × 50 rectangle.
        Rect({ width: '90%', height: 50 })
          .fill(Color.Pink)
        // Draw a 90% × 50 rectangle.
        Rect()
          .width('90%')
          .height(50)
          .fillOpacity(0)
          .stroke(Color.Red)
          .strokeWidth(3)

        Text('with rounded corners').fontSize(11).fontColor(0xCCCCCC).width('90%')
        // Draw a 90% × 80 rectangle, with the width and height of its rounded corners being 40 and 20, respectively.
        Rect({ width: '90%', height: 80 })
          .radiusHeight(20)
          .radiusWidth(40)
          .fill(Color.Pink)
        // Draw a 90% × 80 rectangle, with the width and height of its rounded corners being both 20.
        Rect({ width: '90%', height: 80 })
          .radius(20)
          .fill(Color.Pink)
          .stroke(Color.Transparent)
      }.width('100%').margin({ top: 10 })

      // Draw a 90% × 50 rectangle, with the width and height of its rounded corners as follows: 40 for the upper left rounded corner, 20 for the upper right rounded corner, 40 for the lower right rounded corner, and 20 for the lower left rounded corner.
      Rect({ width: '90%', height: 80 })
        .radius(\[\[40, 40\], \[20, 20\], \[40, 40\], \[20, 20\]\])
        .fill(Color.Pink)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/6AN8EShJSruPVwF3j8RRpw/en-us_image_0000002537925826.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BF01030790D16ABFE0C1E8875A785BDEADDC21C03C00ADDB16EBD1D6D011914)

## Example 2: Drawing a Gradient Rectangle

This example demonstrates how to use the universal attributes [linearGradient](../../universal-attributes/visual-effects/color-gradient/document.md#lineargradient18) and [clipShape](../../universal-attributes/visual-effects/shape-clipping/document.md#clipshape18) to draw a gradient rectangle.

The universal attributes **linearGradient** and **clipShape** are supported since API version 18.

// xxx.ets
@Entry
@Component
struct RectExample {
  build() {
    Column({ space: 10 }) {
      Column()
        .width(100)
        .height(100)
        .linearGradient({
          direction: GradientDirection.Right,
          colors: \[\[0xff0000, 0.0\], \[0x0000ff, 0.3\], \[0xffff00, 1.0\]\]
        })
        .clipShape(new Rect({ width: 100, height: 100, radius: 40 }))
      Rect()
        .width(100)
        .height(100)
        // Set the color of the fill area. To display the gradient color of the background, set .fillOpacity(0.0).
        .fill(Color.Pink)
        // Set the radius of the chamfer to 40.
        .radius(40)
        .stroke(Color.Black)
        // Set the gradient color. It takes effect only for a 100 × 100 rectangular area. The boundary of the gradient color does not contain chamfers.
        .linearGradient({
          direction: GradientDirection.Right,
          colors: \[\[0xff0000, 0.0\], \[0x0000ff, 0.3\], \[0xffff00, 1.0\]\]
        })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/Pu_6lymzQ7G2j21MiboG9g/en-us_image_0000002568685603.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=01B48DC94D6CA954A67F853F67D340FE7CE097A83D938C81610A89C517FE43B9)

## Example 3: Drawing a Rectangle with Different Parameter Types

This example demonstrates how to draw a rectangle using different parameter types for the **width**, **height**, **radius**, **radiusWidth**, and **radiusHeight** attributes.

// xxx.ets
@Entry
@Component
struct RectExample {
  build() {
    Column({ space: 10 }) {
      // Draw a 90% × 50 rectangle, with the radius of rounded corners being 5.
      Rect({ width: '90%', height: '50', radius: '5' }) // Use the string type.
        .fill(Color.Green)
      // Draw a 200 × 50 rectangle, with the radius of rounded corners being 5.
      Rect({ width: 200, height: 50, radius: 5 }) // Use the number type.
        .fillOpacity(0)
        .stroke(Color.Red)
        .strokeWidth(3)
      // Draw a 200 × 50 rectangle, with the width and height of its rounded corners being 80 and 20, respectively.
      Rect({
        width: $r('app.string.RectWidth'), // Use the Resource type, which needs to be customized.
        height: $r('app.string.RectHeight'),
        radius: $r('app.string.RectRadius')
      })
        .radiusWidth($r('app.string.RectRadiusWidth'))
        .radiusHeight($r('app.string.RectRadiusHeight'))
        .fill(Color.Green)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/_zMtxrynQ6Sk86567B_--g/en-us_image_0000002568765613.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=516BA3CCEAC72BB5CC1890001F6B2387EE159ABCB3C53D2AC0431FACE12F48C7)

## Example 4: Dynamically Setting Attributes of the Rect Component Using attributeModifier

This example shows how to use **attributeModifier** to dynamically set the **fill**, **fillOpacity**, **stroke**, **strokeDashArray**, **strokeDashOffset**, **strokeLineCap**, **strokeLineJoin**, **strokeMiterLimit**, **strokeOpacity**, **strokeWidth**, and **antiAlias** attributes of the **Rect** component.

// xxx.ets
class MyRectModifier implements AttributeModifier<RectAttribute> {
  applyNormalAttribute(instance: RectAttribute): void {
    // Fill color: #707070; fill opacity: 0.5; stroke color: #2787D9; stroke dash array: \[20\]; offset to left: 15; cap style: semi-circle; join style: miter; miter limit: 5; stroke opacity: 0.5; stroke width: 10; anti-aliasing enabled.
    instance.fill("#707070")
    instance.fillOpacity(0.5)
    instance.stroke("#2787D9")
    instance.strokeDashArray(\[20\])
    instance.strokeDashOffset("15")
    instance.strokeLineCap(LineCapStyle.Round)
    instance.strokeLineJoin(LineJoinStyle.Miter)
    instance.strokeMiterLimit(5)
    instance.strokeOpacity(0.5)
    instance.strokeWidth(10)
    instance.antiAlias(true)
  }
}

@Entry
@Component
struct RectModifierDemo {
  @State modifier: MyRectModifier = new MyRectModifier()

  build() {
    Column() {
      Rect()
        .width(200)
        .height(200)
        .attributeModifier(this.modifier)
        .offset({ x: 20, y: 20 })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/UIjS_KSZT8WCfXFJZEP63Q/en-us_image_0000002537765888.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B14C3225B6BBC5D2B8430FC8DB9B22845DFF92986AAC41DEEC5B5FE00A338617)
