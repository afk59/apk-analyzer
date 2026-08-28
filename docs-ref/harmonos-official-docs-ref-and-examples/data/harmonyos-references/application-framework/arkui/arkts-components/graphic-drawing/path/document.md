# Path

The **Path** component is used to draw a custom closed shape based on a specified drawing path.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/wq-DXS2LSqSKef2j1iS28g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB19F62BC730066BBB225B4025AA704FD973574B469D807A5ACCEBFE367F2B4F)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

This component supports dynamic constructor parameter updates using the [updateConstructorParams](../../../arkts-api/ui/arkui/attributeupdater/document.md#properties) API of the [AttributeUpdater](../../../arkts-api/ui/arkui/attributeupdater/document.md) class since API version 20.

#### Child Components

None

#### APIs

Path(options?: PathOptions)

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [PathOptions](#pathoptions18) | No | 
Options of the path.

The **undefined** and **null** values are treated as invalid and will not take effect.

 |

#### PathOptions18+

Describes the options of the path.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/Bol-1mVdRV66O6fs-j1FBg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08A0EEE495AF7DF52D505286D78103562C73FADF9EC069DB17206161E3BDF0CB)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width7+ | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 
Width of the rectangle where the path is located.

If the value is invalid or the default value is used, the width required for the content is used.

Default unit: vp

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| height7+ | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Height of the rectangle where the path is located.

If the value is invalid or the default value is used, the height required for the content is used.

Default unit: vp

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| [commands7+](#commands) | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Command string for drawing the path.

If the value is invalid or the default value is used, the width and height required for the content are used. The default value is an empty string.

An invalid value is handled as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]commands

commands(value: [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr))

Sets a string of path commands that comply with the [SVG path syntax](#svg-path-syntax). The unit is px. For details about how to convert pixel units, see [Pixel Units](../../common-definitions/pixel-units/document.md).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 
Path for drawing a line.

The default value is an empty string.

Default unit: px

The **undefined** and **null** values are invalid and treated as the default value.

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

**NaN** is treated as **0.0**, while **undefined**, **null**, and **Infinity** are treated as **1.0**.

Default value: **1.0**.

 |

#### \[h2\]stroke

stroke(value: ResourceColor)

Sets the stroke color. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier). If this attribute is not set, the default stroke color is opaque black.

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
Array defining the dash pattern for the path outline. Elements alternate between dash length and gap length.

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

Sets the offset of the start point for drawing the stroke. A positive value shifts the start point to the left. This attribute can be dynamically set using [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier). An invalid value is handled as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | Yes | 
Line dash offset.

Default value: **0**

Default unit: vp

The **undefined** and **null** values are treated as the default value. If set to **NaN** or **Infinity**, **strokeDashArray** has no effect.

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

The **undefined**, **null**, and **NaN** values are treated as the default value. If set to **Infinity**, **stroke** has no effect.

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

Default value: **1**

**NaN** is treated as **0.0**, while **undefined**, **null**, and **Infinity** are treated as **1.0**.

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

#### SVG Path Syntax

The table below lists the supported SVG path commands.

| Command | Name | Parameter | Description |
| :-- | :-- | :-- | :-- |
| M | moveto | 
**x**: X-coordinate of the start point.

**y**: Y-coordinate of the start point.

 | Starts a new subpath at the specified point (x, y). This point becomes the new current point. |
| L | lineto | 

**x**: X-coordinate of the end point of the line.

**y**: Y-coordinate of the end point of the line.

 | Draws a straight line from the current point to (x, y). This end point becomes the new current point. For example, **L 50 50** draws a line to (50, 50). |
| H | horizontal lineto | **x**: X-coordinate of the end point of the horizontal line. | Draws a horizontal line to the given X coordinate. Equivalent to an **L** command with the current Y coordinate. For example, **H 50** draws a horizontal line from the current point to (50, current y). |
| V | vertical lineto | **y**: Y-coordinate of the end point of the vertical line. | Draws a vertical line to the given Y coordinate. Equivalent to an **L** command with the current X coordinate. For example, given a current point of (100, 100), the command **V 50** draws a vertical line to the point (100, 50) and then sets (100, 50) as the new current point. |
| C | curveto | 

**x1**: X-coordinate of the first control point.

**y1**: Y-coordinate of the first control point.

**x2**: X-coordinate of the second control point.

**y2**: Y-coordinate of the second control point.

**x**: X-coordinate of the end point.

**y**: Y-coordinate of the end point.

 | Draws a cubic Bezier curve from the current point to the point specified by the given (x, y) coordinates, with (x1, y1) as the control point of the curve start point and (x2, y2) as the control point of the curve end point. For example, **C100 100 250 100 250 200** draws a cubic Bezier curve from the current point to (250, 200), with (250, 200) as the start point of a new subpath. |
| S | smooth curveto | 

**x2**: X-coordinate of the second control point.

**y2**: Y-coordinate of the second control point.

**x**: X-coordinate of the end point.

**y**: Y-coordinate of the end point.

 | Draws a cubic Bezier curve from the current point to the point specified by the given (x, y) coordinates, with (x2, y2) as the control point of the curve end point. If the previous command is **C** or **S**, the control point is the mapping of the control point of the curve end point in the previous command relative to the start point. For example, in **C100 100 250 100 250 200 S400 300 400 200**, the control point of the start point of the second Bezier curve is (250, 300). If there is no previous command or the previous command is not **C** or **S**, the first control point coincides with the current point. |
| Q | quadratic Bezier curve | 

**x1**: X-coordinate of the first control point.

**y1**: Y-coordinate of the first control point.

**x**: X-coordinate of the end point.

**y**: Y-coordinate of the end point.

 | Draws a quadratic Bezier curve from the current point to the point specified by the given (x, y) coordinates, with (x1, y1) as the control point. For example, **Q400 50 600 300** draws a quadratic Bezier curve from the current point to the point specified by the given (600, 300) coordinates, with the point specified by the given (600, 300) coordinates as the start point of a new subpath. |
| T | smooth quadratic Bezier curveto | 

**x**: X-coordinate of the end point.

**y**: Y-coordinate of the end point.

 | Draws a quadratic Bezier curve from the current point to the point specified by the given (x, y) coordinates. If the previous command is **Q** or **T**, the control point is the mapping of the control point of the curve end point in the previous command relative to the start point. For example, in **Q400 50 600 300 T1000 300**, the control point of the second Bezier curve is (800, 350). If there is no previous command or the previous command is not **Q** or **T**, the first control point coincides with the current point. |
| A | elliptical Arc | 

**rx**: radius of the ellipse on the x-axis.

**ry**: radius of the ellipse on the y-axis.

**x-axis-rotation**: rotation angle of the ellipse relative to the coordinate system.

**large-arc-flag**: whether to draw a large arc (1) or a small arc (0).

**sweep-flag**: whether to draw clockwise (1) or counterclockwise (0).

**x**: X-coordinate of the end point.

**y**: Y-coordinate of the end point.

 | Draws an elliptical arc from the current point to the point specified by the given (x, y) coordinates. The size and direction of the ellipse are defined by two radii (rx, ry) and **x-axis-rotation**, indicating how the entire ellipse is rotated relative to the current coordinate system (in degrees). **large-arc-flag** and **sweep-flag** define how the arc is drawn. |
| Z | closepath | none | Closes the current subpath by connecting the current path back to the initial point of the current subpath. |

For example, the command string **commands('M0 20 L50 50 L50 100 Z')** defines a triangle: It starts at (0, 20), draws a line to (50, 50), then to (50, 100), and finally closes the path back to (0, 20).

#### Examples

## Example 1: Drawing Rectangles

This example demonstrates how to use **commands**, **fillOpacity**, and **stroke** to draw a closed shape with the specified path, opacity, and stroke color.

// xxx.ets
@Entry
@Component
struct PathExample {
  build() {
    Column({ space: 10 }) {
      Text('Straight line')
        .fontSize(11)
        .fontColor(0xCCCCCC)
        .width('90%')
      // Draw a straight line whose length is 600 px and width is 3 vp.
      Path()
        .width('600px')
        .height('10px')
        .commands('M0 0 L600 0')
        .stroke(Color.Black)
        .strokeWidth(3)

      Text('Straight line graph')
        .fontSize(11)
        .fontColor(0xCCCCCC)
        .width('90%')
      // Draw a straight line.
      Flex({ justifyContent: FlexAlign.SpaceBetween }) {
        Path()
          .width('210px')
          .height('310px')
          .commands('M100 0 L200 240 L0 240 Z')
          .fillOpacity(0)
          .stroke(Color.Black)
          .strokeWidth(3)
        Path()
          .width('210px')
          .height('310px')
          .commands('M0 0 H200 V200 H0 Z')
          .fillOpacity(0)
          .stroke(Color.Black)
          .strokeWidth(3)
        Path()
          .width('210px')
          .height('310px')
          .commands('M100 0 L0 100 L50 200 L150 200 L200 100 Z')
          .fillOpacity(0)
          .stroke(Color.Black)
          .strokeWidth(3)
      }.width('95%')

      Text('Curve graphics').fontSize(11).fontColor(0xCCCCCC).width('90%')
      // Draw an arc.
      Flex({ justifyContent: FlexAlign.SpaceBetween }) {
        Path()
          .width('250px')
          .height('310px')
          .commands("M0 300 S100 0 240 300 Z")
          .fillOpacity(0)
          .stroke(Color.Black)
          .strokeWidth(3)
        Path()
          .width('210px')
          .height('310px')
          .commands('M0 150 C0 100 140 0 200 150 L100 300 Z')
          .fillOpacity(0)
          .stroke(Color.Black)
          .strokeWidth(3)
        Path()
          .width('210px')
          .height('310px')
          .commands('M0 100 A30 20 20 0 0 200 100 Z')
          .fillOpacity(0)
          .stroke(Color.Black)
          .strokeWidth(3)
      }.width('95%')
    }.width('100%')
    .margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/5jdGaK_ERvaLjWJy1fFNtg/en-us_image_0000002568685601.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83BFCCF392CBF1B3A5C18B19ECEBCC81A09979449E16084EC7BD62DE8B58B320)

## Example 2: Drawing a Path Using Different Parameter Types

This example demonstrates how to draw a path using different length types of the **width**, **height**, and **commands** attributes.

// xxx.ets
@Entry
@Component
struct PathTypeExample {
  build() {
    Column({ space: 10 }) {
      // Use the string type for the width, height, and commands attributes to draw a line.
      Path({ width: '600px', height: '10px' })
        .commands('M0 0 L600 0')
        .fillOpacity(0)
        .stroke(Color.Black)
        .strokeWidth(3)
      // Use the number type for the width and height attributes to draw a rectangle.
      Path({ width: 200, height: 100 })
        .commands('M200 0 H400 V200 H200 Z')
        .fillOpacity(0)
        .stroke(Color.Black)
        .strokeWidth(3)
      // Use the Resource type (customized by yourself) for the width, height, and commands attributes to draw an arc.
      Path({ width: $r('app.string.PathWidth'), height: $r('app.string.PathHeight') }) // In this example, PathWidth and PathHeight are both defined as 200.
        .commands($r('app.string.PathCommands')) // In this example, PathCommands is defined as "M150 300 Q300 0 450 300 Z".
        .fillOpacity(0)
        .stroke(Color.Black)
        .strokeWidth(3)
    }.width('100%')
    .margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/aN5_mMhUQWaub4UrQG57bA/en-us_image_0000002568765611.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E1811F4058EA10F3E3F0C04763D93030343E1664CACBAF7C7898BEA9134D90F)

## Example 3: Dynamically Setting Attributes of the Path Component Using attributeModifier

This example shows how to use **attributeModifier** to dynamically set the **commands**, **fill**, **fillOpacity**, **stroke**, **strokeDashArray**, **strokeDashOffset**, **strokeLineCap**, **strokeLineJoin**, **strokeMiterLimit**, **strokeOpacity**, **strokeWidth**, and **antiAlias** attributes of the **Path** component.

// xxx.ets
class MyPathModifier implements AttributeModifier<PathAttribute> {
  applyNormalAttribute(instance: PathAttribute): void {
    // Use the string type for the commands attribute to draw a triangle with the following information: fill color: #707070, fill opacity: 0.5, stroke color: #2787D9, stroke dash array: \[20\], offset to left: 15, cap style: semi-circle, line join: miter; miter limit: 5; stroke opacity: 0.5; stroke width: 10; anti-aliasing enabled.
    instance.commands('M100 0 L200 240 L0 240 Z')
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
struct PathModifierDemo {
  @State modifier: MyPathModifier = new MyPathModifier()

  build() {
    Column() {
      Path()
        .attributeModifier(this.modifier)
        .offset({ x: 20, y: 20 })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/f2QxR7bMQequpk6JwNO5wA/en-us_image_0000002537765886.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E2057C10FE2922827856EA1D3F6B21C487D009374CC697F8FD766C5C6549F8E)
