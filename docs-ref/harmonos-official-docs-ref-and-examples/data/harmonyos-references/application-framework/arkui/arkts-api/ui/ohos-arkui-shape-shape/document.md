# @ohos.arkui.shape (Shape)

The **shape** module provides [clipShape](../../../arkts-components/universal-attributes/visual-effects/shape-clipping/document.md#clipshape12) and [maskShape](../../../arkts-components/universal-attributes/visual-effects/shape-clipping/document.md#maskshape12) APIs to allow you to pass in various shapes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/5DuZUOvIQ6OCaBHjH3cMtg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E34C61090CF6D815654A04D36E06DB11201BC85AF0AA4CFC04336040A0C72F4B)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { CircleShape, EllipseShape, PathShape, RectShape } from "@kit.ArkUI";

#### CircleShape

Represents a circle shape used in the **clipShape** and **maskShape** APIs.

This API inherits from [BaseShape](#baseshape).

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor

constructor(options?: ShapeSize)

A constructor used to create a **CircleShape** object.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ShapeSize](#shapesize) | No | Size of the shape. |

#### EllipseShape

Represents an ellipse shape used in the **clipShape** and **maskShape** APIs.

This API inherits from [BaseShape](#baseshape).

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor

constructor(options?: ShapeSize)

A constructor used to create an **EllipseShape** object.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ShapeSize](#shapesize) | No | Size of the shape. |

#### PathShape

Represents a path used in the **clipShape** and **maskShape** APIs.

This API inherits from [CommonShapeMethod](#commonshapemethod).

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor

constructor(options?: PathShapeOptions)

A constructor used to create a **PathShape** object.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [PathShapeOptions](#pathshapeoptions) | No | Path parameters. |

#### \[h2\]commands

commands(commands: string): PathShape

Sets the path drawing commands.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| commands | string | Yes | Path drawing commands. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PathShape](#pathshape) | **PathShape** object. |

#### RectShape

Represents a rectangle shape used in the **clipShape** and **maskShape** APIs.

This API inherits from [BaseShape](#baseshape).

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor

constructor(options?: RectShapeOptions | RoundRectShapeOptions)

A constructor used to create a **RectShape** object.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [RectShapeOptions](#rectshapeoptions) | [RoundRectShapeOptions](#roundrectshapeoptions) | No | Rectangle parameters. |

#### \[h2\]radiusWidth

radiusWidth(rWidth: number | string): RectShape

Sets the radius width of the rectangle border corners.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rWidth | number | string | Yes | 
Radius width of the rectangle border corners.

When the parameter type is number, the valid value range is \[0, +∞). When the parameter type is string, the value must conform to the [Length](../../../arkts-components/common-definitions/basic-types/document.md#length) type specification.

Unit: vp.

If the value is invalid, 0 vp is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [RectShape](#rectshape) | **RectShape** object. |

#### \[h2\]radiusHeight

radiusHeight(rHeight: number | string): RectShape

Sets the radius height of the rectangle border corners.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rHeight | number | string | Yes | 
Radius height of the rectangle border corners.

When the parameter type is number, the valid value range is \[0, +∞). When the parameter type is string, the value must conform to the [Length](../../../arkts-components/common-definitions/basic-types/document.md#length) type specification.

Unit: vp.

If the value is invalid, 0 vp is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [RectShape](#rectshape) | **RectShape** object. |

#### \[h2\]radius

radius(radius: number | string | Array<number | string>): RectShape

Sets the radius of the rectangle border corners.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| radius | number | string | Array<number | string> | Yes | 
Radius of the rectangle border corners. When an array is provided, it should contain exactly four elements, corresponding to the radius of the upper left, upper right, lower left, and lower right corners of the rectangle, respectively. If more than four elements are contained, only the first four are accepted.

When the parameter type is number, the valid value range is \[0, +∞). When the parameter type is string, the value must conform to the [Length](../../../arkts-components/common-definitions/basic-types/document.md#length) type specification.

Unit: vp.

If the value is invalid, 0 vp is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [RectShape](#rectshape) | **RectShape** object. |

#### ShapeSize

Describes the size of a shape.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | number | string | No | Yes | 
Width of the shape.

When the parameter type is number, the valid value range is \[0, +∞). When the parameter type is string, the value must conform to the [Length](../../../arkts-components/common-definitions/basic-types/document.md#length) type specification.

Unit: vp.

If the value is invalid, 0 vp is used.

 |
| height | number | string | No | Yes | 

Height of the shape.

When the parameter type is number, the valid value range is \[0, +∞). When the parameter type is string, the value must conform to the [Length](../../../arkts-components/common-definitions/basic-types/document.md#length) type specification.

Unit: vp.

If the value is invalid, 0 vp is used.

 |

#### PathShapeOptions

Represents the parameter of the constructor used to create a **PathShape** object.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| commands | string | No | Yes | Path drawing commands. For details, see [commands](../../../arkts-components/graphic-drawing/path/document.md#commands). |

#### RectShapeOptions

Represents the parameter of the constructor used to create a **RectShape** object.

This API inherits from [ShapeSize](#shapesize).

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| radius | number | string | Array<number | string> | No | Yes | 
Radius of the rectangle border corners.

When the parameter type is number, the valid value range is \[0, +∞). When the parameter type is string, the value must conform to the [Length](../../../arkts-components/common-definitions/basic-types/document.md#length) type specification.

Unit: vp.

If the value is invalid, 0 vp is used.

 |

#### RoundRectShapeOptions

Represents the parameter of the constructor used to create a **RectShape** object with rounded corners.

This API inherits from [ShapeSize](#shapesize).

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| radiusWidth | number | string | No | Yes | 
Radius width of the rectangle border corners.

When the parameter type is number, the valid value range is \[0, +∞). When the parameter type is string, the value must conform to the [Length](../../../arkts-components/common-definitions/basic-types/document.md#length) type specification.

Unit: vp.

If the value is invalid, 0 vp is used.

 |
| radiusHeight | number | string | No | Yes | 

Radius height of the rectangle border corners.

When the parameter type is number, the valid value range is \[0, +∞). When the parameter type is string, the value must conform to the [Length](../../../arkts-components/common-definitions/basic-types/document.md#length) type specification.

Unit: vp.

If the value is invalid, 0 vp is used.

 |

#### BaseShape

This API inherits from [CommonShapeMethod](#commonshapemethod).

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]width

width(width: Length): T

Sets the width of a shape.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | [Length](../../../arkts-components/common-definitions/basic-types/document.md#length) | Yes | 
Width of the shape.

Unit: vp.

If the value is invalid, 0 vp is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### \[h2\]height

height(height: Length): T

Sets the height of a shape.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| height | [Length](../../../arkts-components/common-definitions/basic-types/document.md#length) | Yes | 
Height of the shape.

Unit: vp.

If the value is invalid, 0 vp is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### \[h2\]size

size(size: SizeOptions): T

Sets the size of a shape.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | [SizeOptions](../../../arkts-components/common-definitions/basic-types/document.md#sizeoptions) | Yes | Size of the shape. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### CommonShapeMethod

Implements the common shape methods.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]offset

offset(offset: Position): T

Sets the coordinate offset relative to the component's layout position.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| offset | [Position](../../../arkts-components/common-definitions/basic-types/document.md#position) | Yes | Coordinate offset relative to the component's layout position. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### \[h2\]fill

fill(color: ResourceColor): T

Sets the fill color of this shape, which determines its opacity, with black representing full transparency and white representing full opacity.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | Yes | Fill color of the shape, which represents the opacity of the fill area. The black color indicates full transparency, while white indicates full opacity. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### \[h2\]position

position(position: Position): T

Sets the position of the shape.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| position | [Position](../../../arkts-components/common-definitions/basic-types/document.md#position) | Yes | Position of the shape. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### Example

This example demonstrates how to use [clipShape](../../../arkts-components/universal-attributes/visual-effects/shape-clipping/document.md#clipshape12) and [maskShape](../../../arkts-components/universal-attributes/visual-effects/shape-clipping/document.md#maskshape12) to clip and mask images into different shapes.

import { CircleShape, EllipseShape, PathShape, RectShape } from '@kit.ArkUI';

@Entry
@Component
struct ShapeExample {
  build() {
    Column({ space: 15 }) {
      Text('CircleShape, position').fontSize(20).width('75%').fontColor('#DCDCDC')
      // Replace $r('app.media.startIcon') with the resource file you use.
      Image($r('app.media.startIcon'))
        .clipShape(new CircleShape({ width: '280px', height: '280px' }).position({ x: '20px', y: '20px' }))
        .width('500px').height('280px')

      Text('EllipseShape, offset').fontSize(20).width('75%').fontColor('#DCDCDC')
      // Replace $r('app.media.startIcon') with the resource file you use.
      Image($r('app.media.startIcon'))
        .clipShape(new EllipseShape({ width: '350px', height: '280px' }).offset({ x: '10px', y: '10px' }))
        .width('500px').height('280px')

      Text('PathShape, fill').fontSize(20).width('75%').fontColor('#DCDCDC')
      // Replace $r('app.media.startIcon') with the resource file you use.
      Image($r('app.media.startIcon'))
        .maskShape(new PathShape().commands('M100 0 L200 240 L0 240 Z').fill(Color.Red))
        .width('500px').height('280px')
    
      Text('RectShape, width, height, fill').fontSize(20).width('75%').fontColor('#DCDCDC')
      // Replace $r('app.media.startIcon') with the resource file you use.
      Image($r('app.media.startIcon'))
        .maskShape(new RectShape().width('350px').height('280px').fill(Color.Red))
        .width('500px').height('280px')
    }
    .width('100%')
    .margin({ top: 15 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/Cyg8dreMRzix9OwnqxMz7A/en-us_image_0000002537765320.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2653F0B6C71544BF37259DF2488F75A693289795EA8F1931BD62EDC82365AB41)
