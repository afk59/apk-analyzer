# Polyline

The **Polyline** component is used to draw a polyline.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/fOdnmVsRRou3YMOQ3RAsKQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94CAE3120F8488CE52FA0C2B504AB6DA963B2352C2C6191C8D64C9138BA26EA1)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

This component supports dynamic constructor parameter updates using the [updateConstructorParams](../../../arkts-api/ui/arkui/attributeupdater/document.md#properties) API of the [AttributeUpdater](../../../arkts-api/ui/arkui/attributeupdater/document.md) class since API version 20.

#### Child Components

None

#### APIs

Polyline(options?: PolylineOptions)

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [PolylineOptions](#polylineoptions18) | No | 
Options of the polyline.

The **undefined** and **null** values are treated as invalid and will not take effect.

 |

#### PolylineOptions18+

Describes the options of the polyline.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/KYBkqDAsQaaz5tCvWrvCVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20990FBB568FD11F48219A479F4B4B6D8110900DC6587C577FF600510A87B86F)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width7+ | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 
Width. The value must be greater than or equal to 0.

Default value: **0**.

Default unit: vp

The **undefined**, **null**, **NaN**, and **Infinity** values are invalid and treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| height7+ | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Height. The value must be greater than or equal to 0.

Default value: **0**.

Default unit: vp

The **undefined**, **null**, **NaN**, and **Infinity** values are invalid and treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]points

points(value: Array<any>)

Sets the list of coordinates through which the polyline passes. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Array<any> | Yes | 
List of coordinates that the polyline passes through. A two-dimensional array is passed, and each subarray indicates the \[x, y\] coordinates of a vertex.

Default value: **\[\]** (empty array)

Default unit: vp

The **undefined** and **null** values are invalid and treated as the default value.

 |

#### \[h2\]fill

fill(value: ResourceColor)

Sets the color of the fill area. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier). If this attribute and the universal attribute **foregroundColor** are both set, whichever is set later takes effect.

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

For the number type, the value range is \[0.0, 1.0\]. A value less than 0.0 is treated as **0.0**. A value greater than 1.0 is treated as **1.0**. Any other invalid value is treated as **1.0**.

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

Sets the stroke dashes. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier). Line segments may overlap when they intersect. The value must be greater than or equal to 0. Invalid values are treated as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Array<any> | Yes | 
Array defining the dash pattern for the polyline outline. Elements alternate between dash length and gap length.

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

Sets the offset of the start point for drawing the stroke. A positive value shifts the start point to the left. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | Yes | 
Offset of the start point for drawing the stroke.

Default value: **0**.

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

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | Yes | 
Limit on the ratio of the miter length to the value of **strokeWidth** used to draw a miter join.

Default value: **4**

The value must be greater than or equal to 1.0. If the value is within the \[0, 1) range, **1.0** is used.

Invalid values **undefined**, **null**, and **NaN** are treated as the default value. If set to **Infinity**, **stroke** has no effect.

 |

#### \[h2\]strokeOpacity

strokeOpacity(value: number | string | Resource)

Sets the stroke opacity. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Stroke opacity. The value range is \[0.0, 1.0\].

Default value: opacityset by the [stroke](#stroke) API.

If the set value is less than 0.0, **0.0** will be used. If the set value is greater than 1.0, **1.0** will be used.

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

## Example 1: Drawing a Polyline

This example demonstrates how to use **points**, **fillOpacity**, **stroke**, **strokeLineJoin**, and **strokeLineCap** to draw a polyline with specific coordinates, opacity, stroke colors, corner styles, and endpoint styles.

// xxx.ets
@Entry
@Component
struct PolylineExample {
  build() {
    Column({ space: 10 }) {
      // Draw a polyline in a 100 × 100 rectangle. The start point is (0, 0), the end point is (100, 100), and the passing point is (20,60).
      Polyline({ width: 100, height: 100 })
        .points(\[\[0, 0\], \[20, 60\], \[100, 100\]\])
        .fillOpacity(0)
        .stroke(Color.Blue)
        .strokeWidth(3)
      // Draw a polyline in a 100 × 100 rectangle. The start point is (20, 0), the end point is (100, 90), and the passing point is (0,100).
      Polyline()
        .width(100)
        .height(100)
        .fillOpacity(0)
        .stroke(Color.Red)
        .strokeWidth(8)
        .points(\[\[20, 0\], \[0, 100\], \[100, 90\]\])
        // Set the join style of the stroke to a rounded corner.
        .strokeLineJoin(LineJoinStyle.Round)
        // Set the cap style of the stroke to a half circle.
        .strokeLineCap(LineCapStyle.Round)
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/67i13f3PQcCzAjn5fRzbLw/en-us_image_0000002537765882.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1819698A79259B3B5F12275ACAE23E109A1BAA6D525A45E1F9634F2CB1D6251)

## Example 2: Drawing a Polyline with Different Parameter Types for Width and Height

This example demonstrates how to draw a polyline using different length types of the **width** and **height** attributes.

// xxx.ets
@Entry
@Component
struct PolylineTypeExample {
  build() {
    Column({ space: 10 }) {
      // Draw a polyline in a 100 × 100 rectangle. The start point is (0, 0), the end point is (100, 100), and the passing point is (20,60).
      Polyline({ width: '100', height: '100' }) // Use the string type.
        .points(\[\[0, 0\], \[20, 60\], \[100, 100\]\])
        .fillOpacity(0)
        .stroke(Color.Blue)
        .strokeWidth(3)
      Polyline({ width: 100, height: 100 }) // Use the number type.
        .points(\[\[0, 0\], \[20, 60\], \[100, 100\]\])
        .fillOpacity(0)
        .stroke(Color.Blue)
        .strokeWidth(3)
      Polyline({ width: $r('app.string.PolylineWidth'), height: $r('app.string.PolylineHeight') }) // Use the Resource type, which needs to be customized.
        .points(\[\[0, 0\], \[20, 60\], \[100, 100\]\])
        .fillOpacity(0)
        .stroke(Color.Blue)
        .strokeWidth(3)
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/atNqFLuDTreSNMb3-c9JGg/en-us_image_0000002537925822.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=46E26C1EE944E93247AC317D22E59C909C90D2079D4D009D8165445F6C1F1973)

## Example 3: Dynamically Setting Attributes of the Polyline Component Using attributeModifier

This example shows how to use **attributeModifier** to dynamically set the **points**, **fill**, **fillOpacity**, **stroke**, **strokeDashArray**, **strokeDashOffset**, **strokeLineCap**, **strokeLineJoin**, **strokeMiterLimit**, **strokeOpacity**, **strokeWidth**, and **antiAlias** attributes of the **Polyline** component.

// xxx.ets
class MyPolylineModifier implements AttributeModifier<PolylineAttribute> {
  applyNormalAttribute(instance: PolylineAttribute): void {
    // Line starting at (0, 0), passing through (50, 100), and ending at (100, 0). Fill color: #707070; fill opacity: 0.5; stroke color: #2787D9; stroke dash array: \[20\]; offset to left: 15; cap style: semi-circle; join style: miter; miter limit: 5; stroke opacity: 0.5; stroke width: 10; anti-aliasing enabled.
    instance.points(\[\[0, 0\], \[50, 100\], \[100, 0\]\])
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
struct PolylineModifierDemo {
  @State modifier: MyPolylineModifier = new MyPolylineModifier()

  build() {
    Column() {
      Polyline()
        .width(100)
        .height(100)
        .attributeModifier(this.modifier)
        .offset({ x: 20, y: 20 })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/nRH6OTr6TAeHiRjY_sLxsw/en-us_image_0000002568685599.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D747C7C5DBC0D997A9FFC9B95009EEDE322BE2625B0214092461580141D1A485)
