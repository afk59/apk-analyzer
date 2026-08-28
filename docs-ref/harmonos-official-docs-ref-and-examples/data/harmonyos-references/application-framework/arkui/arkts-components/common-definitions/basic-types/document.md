# Basic Types

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/_3-OQx6lROuBpKyVcRPXSg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E487EA0FF3D9BD3425839D1E72EA589CC9585F261EE39528AFA33290F29A196)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Resource

The **Resource** type is used to reference resources for setting component attributes. Resource files must be stored and managed in specific subdirectories. For examples of resource directories, see [Resource Categories](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access#resource-categories).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

You can use $r or $rawfile to create a **Resource** object, but its attribute values cannot be changed.

-   $r('belonging.type.name')
    
    **belonging**: group to which the resource belongs, which can be **'sys'** or **'app'**.
    
    **type**: resource type, which can be '**boolean'**, **'color'**, **'float'**, **'intarray'**, **'integer'**, **'pattern'**, '**plural'**, **'strarray'**, **'string'**, or **'media'**.
    
    **name**: resource name, which is determined during resource definition.
    
-   $rawfile('filename')
    
    **filename**: name of the file in the **resources/rawfile** directory of the project.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/k8O8y625TX6-6JGAOR4uFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF21809B3BAE2CA65797D333A0373D5559C8F2EF73DD73997D5D977AABBB4DC8)

When referencing a resource type, ensure that the data type in the resource type object is the same as the type of the attribute method that uses the resource type as the parameter. For example, if an attribute method supports setting string | Resource, the data type must be string when Resource is used.

When referencing a resource type, ensure that the resource type object is used in the supported mode. Otherwise, the attribute effect of the resource type as a parameter is the same as that of not setting the attribute.

#### Length

The **Length** type is used to represent a size unit.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| string | 
String type. Specify the length [unit](../pixel-units/document.md) explicitly, for example, **'10px'**, or provide the length in percentage, for example, **'100%'**.

**NOTE**

If the unit is not specified, the default unit vp is used, in which case '10' is equivalent to 10 vp.

 |
| number | Number type. The default unit is vp. |
| [Resource](#resource) | Size referenced from system or application resources. |

#### ResourceStr

The **ResourceStr** type is used to represent the types that can be used by input parameters of the string type.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| string | String type. |
| [Resource](#resource) | String referenced from system or application resources. |

#### Padding

The **Padding** type is used to describe the paddings in different directions of a component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| top | [Length](#length) | No | Yes | Height of the padding on the top of the component. |
| right | [Length](#length) | No | Yes | Width of the padding on the right of the component. |
| bottom | [Length](#length) | No | Yes | Height of the padding at the bottom of the component. |
| left | [Length](#length) | No | Yes | Width of the padding on the left of the component. |

#### LocalizedPadding12+

The **Padding** type is used to describe the paddings in different directions of a component.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| top | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | Height of the padding on the top of the component. |
| end | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | 
Width of the padding on the right of the component.

Width of the padding on the left of the component in RTL mode.

 |
| bottom | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | Height of the padding at the bottom of the component. |
| start | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | 

Width of the padding on the left of the component.

Width of the padding on the right of the component in RTL mode.

 |

#### Margin

The **Margin** type is used to describe the margins in different directions of a component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| top | [Length](#length) | No | Yes | Height of the margin above the component. |
| right | [Length](#length) | No | Yes | Width of the margin on the right of the component. |
| bottom | [Length](#length) | No | Yes | Height of the margin below the component. |
| left | [Length](#length) | No | Yes | Width of the margin on the left of the component. |

#### LocalizedMargin12+

The **Margin** type is used to describe the margins in different directions of a component.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| top | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | Height of the margin above the component. |
| end | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | 
Width of the margin on the right of the component.

Width of the margin on the left of the component in RTL mode.

 |
| bottom | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | Height of the margin below the component. |
| start | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | 

Width of the margin on the left of the component.

Width of the margin on the right of the component in RTL mode.

 |

#### EdgeWidths9+

The **EdgeWidths** type is used to describe the edge widths in different directions of a component.

To reference this object, at least one parameter must be passed.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| top | [Length](#length) | No | Yes | Width of the top edge of the component. |
| right | [Length](#length) | No | Yes | Width of the right edge of the component. |
| bottom | [Length](#length) | No | Yes | Width of the bottom edge of the component. |
| left | [Length](#length) | No | Yes | Width of the left edge of the component. |

#### LocalizedEdgeWidths12+

The **EdgeWidths** type is used to describe the edge widths in different directions of a component.

To reference this object, at least one parameter must be passed.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| top | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | Width of the top edge of the component. |
| end | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | 
Width of the right edge of the component.

Width of the left edge of the component in RTL mode.

 |
| bottom | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | Width of the bottom edge of the component. |
| start | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | 

Width of the left edge of the component.

Width of the right edge of the component in RTL mode.

 |

#### BorderRadiuses9+

The **BorderRadiuses** type is used to describe the corner radius of a component's border.

To reference this object, at least one parameter must be passed.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| topLeft | [Length](#length) | No | Yes | Radius of the upper left corner of the component. |
| topRight | [Length](#length) | No | Yes | Radius of the upper right corner of the component. |
| bottomLeft | [Length](#length) | No | Yes | Radius of the lower left corner of the component. |
| bottomRight | [Length](#length) | No | Yes | Radius of the lower right corner of the component. |

#### LocalizedBorderRadiuses12+

The **LocalizedBorderRadiuses** type is used to describe the corner radius of a component's border.

To reference this object, at least one parameter must be passed.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| topStart | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | 
Radius of the upper left corner of the component.

For right-to-left scripts, this indicates the radius of the upper left right of the component.

 |
| topEnd | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | 

Corner radius of the upper right corner of the component.

For right-to-left scripts, this indicates the corner radius of the upper left corner of the component.

 |
| bottomStart | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | 

Radius of the lower left corner of the component.

For right-to-left scripts, this indicates the corner radius of the lower right corner of the component.

 |
| bottomEnd | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | 

Radius of the lower right corner of the component.

For right-to-left scripts, this indicates the corner radius of the lower left corner of the component.

 |

#### EdgeColors9+

The **EdgeColors** type is used to describe the edge colors of a component.

To reference this object, at least one parameter must be passed.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| top | [ResourceColor](#resourcecolor) | No | Yes | Color of the top edge of the component. |
| right | [ResourceColor](#resourcecolor) | No | Yes | Color of the right edge of the component. |
| bottom | [ResourceColor](#resourcecolor) | No | Yes | Color of the bottom edge of the component. |
| left | [ResourceColor](#resourcecolor) | No | Yes | Color of the left edge of the component. |

#### LocalizedEdgeColors12+

The **EdgeColors** type is used to describe the edge colors of a component.

To reference this object, at least one parameter must be passed.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| top | [ResourceColor](#resourcecolor) | No | Yes | Color of the top edge of the component. |
| end | [ResourceColor](#resourcecolor) | No | Yes | 
Color of the right edge of the component.

For right-to-left scripts, this indicates the color of the left edge of the component.

 |
| bottom | [ResourceColor](#resourcecolor) | No | Yes | Color of the bottom edge of the component. |
| start | [ResourceColor](#resourcecolor) | No | Yes | 

Color of the left edge of the component.

Color of the right edge of the component in RTL mode.

 |

#### EdgeStyles9+

The **EdgeStyles** type is used to describe the edge styles of a component.

To reference this object, at least one parameter must be passed.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| top | [BorderStyle](../enums/document.md#borderstyle) | No | Yes | Style of the top edge of the component. |
| right | [BorderStyle](../enums/document.md#borderstyle) | No | Yes | Style of the right edge of the component. |
| bottom | [BorderStyle](../enums/document.md#borderstyle) | No | Yes | Style of the bottom edge of the component. |
| left | [BorderStyle](../enums/document.md#borderstyle) | No | Yes | Style of the left edge of the component. |

#### Offset

The **Offset** type is used to describe the offset coordinates of a component in the layout.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| dx | [Length](#length) | No | No | X coordinate of the offset. |
| dy | [Length](#length) | No | No | Y coordinate of the offset. |

#### RectResult10+

The **RectResult** type is used to describe the position, width, and height of a component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | X-coordinate. |
| y | number | No | No | Y-coordinate. |
| width | number | No | No | Content width. |
| height | number | No | No | Content height. |

#### ResourceColor

type ResourceColor = [Color](../enums/document.md#color) | number | string | [Resource](#resource)

The **ResourceColor** type is used to describe the color types of resources.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Color](../enums/document.md#color) | Color enums. |
| number | Color in hexadecimal notation. RGB and RGBA are supported. Examples: **0xffffff** and **0xffff0000**. If the number type is used, the format of the color value depends on the value. For example, 0x00ffffff is parsed as an RGB color value. |
| string | RGB or RGBA color. Example: **'#ffffff'**, **'#ff000000'**, **'rgb(255, 100, 255)'**, **'rgba(255, 100, 255, 0.5)'** |
| [Resource](#resource) | Color referenced from system or application resources. |

#### LengthConstrain

The **LengthConstrain** type is used to describe the maximum and minimum lengths of a component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| minLength | [Length](#length) | No | No | Minimum length of the component. |
| maxLength | [Length](#length) | No | No | Maximum length of the component. |

#### Font

The **Font** type is used to set the text style.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| size | [Length](#length) | No | Yes | 
Font size. If the value is of the number type, the unit fp is used. Percentage strings are not supported.

Default value: **16.0**

 |
| weight | [FontWeight](../enums/document.md#fontweight) | number | string | No | Yes | 

Font weight. For the number type, the value ranges from 100 to 900, at an interval of 100. A larger value indicates a thicker font.

Default value: **400** | **FontWeight.Normal**

 |
| family | string | [Resource](#resource) | No | Yes | Font family of the text. Use commas (,) to separate multiple fonts. The priority of the fonts is the sequence in which they are placed. An example value is **'Arial, HarmonyOS Sans'**. Currently, the HarmonyOS Sans font and custom font [loadFontSync](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#loadfontsync) are supported. |
| style | [FontStyle](../enums/document.md#fontstyle) | No | Yes | 

Font style.

Default value: **FontStyle.Normal**

 |

#### Area8+

Area type, which is used to store the area information of an element.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Description |
| :-- | :-- | :-- |
| width | [Length](#length) | 
Width of the target element.

Unit: vp

 |
| height | [Length](#length) | 

Height of the target element.

Unit: vp

 |
| position | [Position](#position) | Position of the upper left corner of the target element in the [component coordinate system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkui-glossary#component-coordinate-system) of the parent element. |
| globalPosition | [Position](#position) | Position of the upper left corner of the target element in the current window coordinate system. |

#### Position

The **Position** type is used to represent coordinates of a point.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | [Length](#length) | No | Yes | 
X-coordinate.

Unit: vp

 |
| y | [Length](#length) | No | Yes | 

Y-coordinate.

Unit: vp

 |

#### LocalizedPosition12+

The **LocalizedPosition** type is used to represent coordinates of a point.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | X-coordinate relative to the left for left-to-right (LTR) scripts; X-coordinate relative to the right for right-to-left (RTL) scripts. |
| top | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | Y-coordinate. |

#### Edges12+

The **Edges** type is used to describe the offset relative to the four edges. If both **top** and **bottom** are set, only **top** takes effect. If both **left** and **right** are set, only **left** takes effect.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| top | [Dimension](#dimension10) | No | Yes | Offset relative to the top edge. |
| bottom | [Dimension](#dimension10) | No | Yes | Offset relative to the bottom edge. |
| left | [Dimension](#dimension10) | No | Yes | Offset relative to the left edge. |
| right | [Dimension](#dimension10) | No | Yes | Offset relative to the right edge. |

#### LocalizedEdges12+

The **LocalizedEdges** type is used to describe the offset relative to the four edges. If both **top** and\*\* bottom \*\*are set, only **top** takes effect. If both **start** and **end** are set, only **start** takes effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| top | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | Offset relative to the top edge. |
| bottom | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | Offset relative to the bottom edge. |
| start | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | Offset relative to the left in LTR mode; offset relative to the right in RTL mode. |
| end | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | Offset relative to the right for in LTR mode; offset relative to the left in RTL mode. |

#### ConstraintSizeOptions

Describes the size constraints of a component during layout.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| minWidth | [Length](#length) | No | Yes | Minimum width of the component. |
| maxWidth | [Length](#length) | No | Yes | Maximum width of the component. |
| minHeight | [Length](#length) | No | Yes | Minimum height of the component. |
| maxHeight | [Length](#length) | No | Yes | Maximum height of the component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/rfaPAPHVRLGWPkOQbTPcxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2CAE95B68FA0C64EA8980C5B3B82CA5ADE88D64FB2AC950E4370FFFA619D41E)

In the [Row](../../rows-columns-and-stacking/row/document.md), [Column](../../rows-columns-and-stacking/column/document.md), and [RelativeContainer](../../rows-columns-and-stacking/relativecontainer/document.md) components, setting **width** and **height** to **auto** means that the size adapts to the size of their child components. In the [TextInput](../../text-and-input/textinput/document.md) component, setting **width** to **auto** means that the width adapts to the width of the text content.

#### SizeOptions

Describes the width and height of a component during layout.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | [Length](#length) | No | Yes | Width of the component. |
| height | [Length](#length) | No | Yes | Height of the component. |

#### BorderOptions

The **BorderOptions** type is used to provide border information.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | [EdgeWidths](#edgewidths9)9+ | [Length](#length) | [LocalizedEdgeWidths](#localizededgewidths12)12+ | No | Yes | 
Border width.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| color | [EdgeColors](#edgecolors9)9+ | [ResourceColor](#resourcecolor) | [LocalizedEdgeColors](#localizededgecolors12)12+ | No | Yes | 

Border color.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| radius | [BorderRadiuses](#borderradiuses9)9+ | [Length](#length) | [LocalizedBorderRadiuses](#localizedborderradiuses12)12+ | No | Yes | 

Border corner radius.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| style | [EdgeStyles](#edgestyles9)9+ | [BorderStyle](../enums/document.md#borderstyle) | No | Yes | 

Border style.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| dashGap12+ | [EdgeWidths](#edgewidths9) | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | [LocalizedEdgeWidths](#localizededgewidths12) | No | Yes | 

Gap between dashed line segments. It takes effect when the border style is set to dashed.

Percentage values are not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

**Widget capability**: This API cannot be used in ArkTS widgets.

 |
| dashWidth12+ | [EdgeWidths](#edgewidths9) | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | [LocalizedEdgeWidths](#localizededgewidths12) | No | Yes | 

Width of dashed line segments. It takes effect when the border style is set to dashed.

Percentage values are not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

**Widget capability**: This API cannot be used in ArkTS widgets.

 |

#### ColorFilter9+

The **ColorFilter** type is used to create a color filter with a 4 x 5 matrix.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| constructor | number\[\] | Yes | Constructor for creating a color filter with a 4\*5 matrix. The input parameter is \[m\*n\], which is the matrix value in row m and column n. The matrix is row-first. |

#### CustomBuilder8+

The **CustomBuilder** type is used to define custom UI descriptions in component attribute methods.

| Name | Type | Description |
| :-- | :-- | :-- |
| CustomBuilder | (() => any) | void | Builder used to generate a custom UI component when used with the [@Builder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder) decorator. |

#### MarkStyle10+

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Default Value | Description |
| :-- | :-- | :-- | :-- | :-- | :-- |
| strokeColor | [ResourceColor](#resourcecolor) | No | Yes | Color.White | Color of the check mark. |
| size | [Length](#length) | No | Yes | \- | 
Size of the check mark, in vp. The default size is the same as the width of the check box component.

Percentage values are not supported. If an invalid value is set, the default value is used.

 |
| strokeWidth | [Length](#length) | No | Yes | 2 | Stroke width of the check mark, in vp. Percentage values are not supported. If an invalid value is set, the default value is used. |

#### ModalTransition10+

The **ModalTransition** type is used to set the transition type for a full-screen modal.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| NONE | No transition animation for the modal. |
| DEFAULT | Slide-up and slide-down animation for the modal. |
| ALPHA | Opacity gradient animation for the modal. |

#### OutlineOptions11+

Outer outline options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | [Dimension](#dimension10) | [EdgeOutlineWidths](#edgeoutlinewidths11) | No | Yes | 
Width of the outline. Percentage values are not supported.

Default value: **0**.

**width** must be set to display the outline effect.

 |
| color | [ResourceColor](#resourcecolor) | [EdgeColors](#edgecolors9) | [LocalizedEdgeColors](#localizededgecolors12)12+ | No | Yes | 

Color of the outline.

Default value: **Color.Black**.

 |
| radius | [Dimension](#dimension10) | [OutlineRadiuses](#outlineradiuses11) | No | Yes | 

Radius of the outline corners. Percentage values are not supported.

Default value: **0**

Maximum effective value: Component width/2 + outlineWidth or component height/2 + outlineWidth

 |
| style | [OutlineStyle](../../universal-attributes/visual-effects/outline-styling/document.md#outlinestyle) | [EdgeOutlineStyles](#edgeoutlinestyles11) | No | Yes | 

Outline style.

Default value: **OutlineStyle.SOLID**

 |

#### EdgeOutlineWidths11+

To reference this object, at least one parameter must be passed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | [Dimension](#dimension10) | No | Yes | Thickness of the left outline. |
| right | [Dimension](#dimension10) | No | Yes | Thickness of the right outline. |
| top | [Dimension](#dimension10) | No | Yes | Width of the top outline. |
| bottom | [Dimension](#dimension10) | No | Yes | Thickness of the bottom outline. |

#### OutlineRadiuses11+

To reference this object, at least one parameter must be passed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| topLeft | [Dimension](#dimension10) | No | Yes | Radius of the upper left corner. |
| topRight | [Dimension](#dimension10) | No | Yes | Radius of the upper right corner. |
| bottomLeft | [Dimension](#dimension10) | No | Yes | Radius of the lower left corner. |
| bottomRight | [Dimension](#dimension10) | No | Yes | Radius of the lower right corner. |

#### EdgeOutlineStyles11+

To reference this object, at least one parameter must be passed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | [OutlineStyle](../../universal-attributes/visual-effects/outline-styling/document.md#outlinestyle) | No | Yes | Style of the left outline. |
| right | [OutlineStyle](../../universal-attributes/visual-effects/outline-styling/document.md#outlinestyle) | No | Yes | Style of the right outline. |
| top | [OutlineStyle](../../universal-attributes/visual-effects/outline-styling/document.md#outlinestyle) | No | Yes | Style of the top outline. |
| bottom | [OutlineStyle](../../universal-attributes/visual-effects/outline-styling/document.md#outlinestyle) | No | Yes | Style of the bottom outline. |

#### Dimension10+

The **Length** type is used to represent a size unit.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [PX](#px10) | Physical pixel unit type. The unit px must be included, for example, **'10px'**. |
| [VP](#vp10) | Pixel unit type specific to the screen density. The unit vp can be included or omitted, for example, **10** or **'10vp'**. |
| [FP](#fp10) | Font pixel unit type. The unit fp must be included, for example, **'10fp'**. |
| [LPX](#lpx10) | Logical pixel unit type. The unit lpx must be included, for example, **'10lpx'**. |
| [Percentage](#percentage10) | Percentage type. The unit % must be included, for example, **'10%'**. |
| [Resource](#resource) | Size referenced from system or application resources. |

#### PX10+

The **PX** type is used to represent a length in px.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| {number}px | Physical pixel unit type. The unit px must be included, for example, **'10px'**. |

#### VP10+

The **VP** type is used to represent a length in vp.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| {number}vp|number | Pixel unit type specific to the screen density. The unit vp can be included or omitted, for example, **10** or **'10vp'**. |

#### FP10+

The **FP** type is used to represent a length in fp.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| {number}fp | Font pixel unit type. The unit fp must be included, for example, **'10fp'**. |

#### LPX10+

The **LPX** type is used to represent a length in lpx.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| {number}lpx | Logical pixel unit type. The unit lpx must be included, for example, **'10lpx'**. |

#### Percentage10+

The **Percentage** type is used to represent a length in percentage.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| {number}% | Percentage type. The unit % must be included, for example, **'10%'**. |

#### Degree10+

The **Degree** type is used to represent a length in deg.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| {number}deg | Degree type. The unit deg must be included, for example, **'10deg'**. |

#### TouchPoint11+

The **TouchPoint** type is used to define the coordinates of the touch point.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Description |
| :-- | :-- | :-- |
| X | [Dimension](#dimension10) | X coordinate of the touch point. |
| Y | [Dimension](#dimension10) | Y coordinate of the touch point. |

#### VoidCallback12+

type VoidCallback: () => void;

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### Callback12+

Callback<T,V = void> = (data: T) => V;

The **Callback** type is used to represent the callback with parameters.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### DividerStyleOptions12+

The **DividerStyleOptions** type is used to provide the information about the divider.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| strokeWidth | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | Width of the divider. |
| color | [ResourceColor](#resourcecolor) | No | Yes | Color of the divider. |
| startMargin | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | Distance between the divider and the start edge of the menu. |
| endMargin | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)12+ | No | Yes | Distance between the divider and the end edge of the menu. |
| mode | [DividerMode](../enums/document.md#dividermode19)19+ | No | Yes | Mode of the divider. |

#### ChainWeightOptions14+

The **ChainWeightOptions** type is used to describe the layout weight of a component within a chain.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| horizontal | number | No | Yes | 
Layout weight of the component in the horizontal direction. It is effective when set to a value greater than 0.

Default value: **0**

Invalid values are treated as **0**.

 |
| vertical | number | No | Yes | 

Layout weight of the component in the vertical direction. It is effective when set to a value greater than 0.

Default value: **0**

Invalid values are treated as **0**.

 |

#### Configuration

The **Configuration** type is used to describe the color mode and font scale.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| colorMode | string | Yes | No | Color mode. |
| fontScale | number | Yes | No | Font scale. |

#### AccessibilityOptions14+

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| accessibilityPreferred | boolean | No | Yes | 
Whether to prioritize the accessibility text of child components during a deep traversal. The value **true** means to prioritize the accessibility text of child components.

If the accessibility text is empty, the text is selected. The combined text is set to the parent node whose accessibilityText and text are empty.

The value **false** means not to prioritize the accessibility text of child components.

Default value: **false**.

 |

#### ScrollBarMargin20+

Scroll bar margin.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 
Start margin of the scroll bar.

Default value: **0**, in vp

 |
| end | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 

Margin at the end of the scroll bar.

Default value: **0**, in vp

 |

#### ResponsiveFillType22+

type ResponsiveFillType = PresetFillType

Responsive layout padding mode, which is used for the WaterFlow, Grid, List, and Swiper components.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [PresetFillType](../enums/document.md#presetfilltype22) | Number of columns for different responsive breakpoint specifications. |

#### ItemFillPolicy22+

Defines a responsive layout policy applicable to the WaterFlow, Grid, List, and Swiper components.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fillType | [ResponsiveFillType](#responsivefilltype22) | No | Yes | Enumerates preset column layouts for different responsive breakpoints. The default value is **BREAKPOINT\_DEFAULT**. |

#### DirectionalEdgesT<T>12+

Edge width type, which is used to describe the width of the component edge in different directions. Globalization is supported.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start | T | No | No | Start edge. It is the left edge if the direction is left-to-right and the right edge if the direction is right-to-left. |
| end | T | No | No | End edge. It is the right edge if the direction is left-to-right and the left edge if the direction is right-to-left. |
| top | T | No | No | Top edge. |
| bottom | T | No | No | Bottom edge. |

#### Bias

Defines the offset of the component under the anchor constraints.

In the horizontal direction, the value of **Bias** is the ratio of the distance from the component to the left anchor Dstart to the total distance between the component and the horizontal anchors Dstart + Dend. In a mirrored language layout, Dstart is the distance from the component to the right anchor. The width of the component is represented by Dwidth.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/MSRLOhHeQEGf84NCxZ-MYw/en-us_image_0000002568685721.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55C3ECAEA2E8E14A8515EF026105BE49D31D4B2D6C506545D720A6275D39A32B)

Similarly, in the vertical direction, the value of **Bias** is the ratio of the distance from the component to the top anchor Dtop to the total distance between the component and the vertical anchors Dtop + Dbottom. The height of the component is represented by Dheight.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/3HCJgh6PR0GHa0ltPej5fQ/en-us_image_0000002568765731.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AFEB3F1A1C567167D40D4C220BB80EDCCF1126C535DA2BBA36DCD4053420B9A2)

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| horizontal | number | No | Yes | 
Bias value in the horizontal direction.

This parameter is valid only when the width attribute of the child component has a correct value and two horizontal anchors are available. The value must be greater than or equal to 0.

Default value: **0.5**

 |
| vertical | number | No | Yes | 

Returns the bias value in the vertical direction.

This parameter is valid only when the height attribute of the child component has a correct value and two vertical anchors are available. The value must be greater than or equal to 0.

Default value: **0.5**

 |

#### CacheCountInfo22+

Defines cache count information.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| minCount | number | No | No | 
Minimum number of caches. When the actual number of caches is less than the minimum number, caches are loaded in the idle slot between frames of the scrolling animation.

Value range: \[0, +∞). If the value is less than 0, the value 1 is used.

 |
| maxCount | number | No | No | 

Maximum number of caches. If the actual number of caches is greater than the value of this parameter, the cached content is reclaimed or released. When the UI is idle (no animation or user operation), caches are loaded to the maximum number.

Value range: \[minCount, +∞). If the value is less than minCount, the value of minCount is used.

 |
