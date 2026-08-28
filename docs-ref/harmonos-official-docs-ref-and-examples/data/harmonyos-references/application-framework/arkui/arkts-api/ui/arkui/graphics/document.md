# Graphics

The **Graphics** module provides APIs for defining attributes of a custom node.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/pU_3PP56QWGna4GPPgY7ww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=455475B83F0B29DCD0838B4AF83F1A797BD302F8121ED61CE37148312DF846CC)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { DrawContext, Size, Offset, Position, Pivot, Scale, Translation, Matrix4, Rotation, Frame, LengthMetricsUnit } from "@kit.ArkUI";

#### Size

Returns the width and height of the component. The default unit is vp, but APIs that use the Size type may specify a different unit, in which case the unit specified by the API takes precedence.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | number | No | No | 
Width of the component.

Unit: vp.

Value range: \[0, +∞).

 |
| height | number | No | No | 

Height of the component.

Unit: vp.

Value range: \[0, +∞).

 |

#### Position

type Position = Vector2

Sets or returns the position of the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Vector2](#vector2) | 
A vector that contains two values: x and y.

Unit: vp.

 |

#### PositionT12+

type PositionT<T> = Vector2T<T>

Sets or returns the position of the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Vector2T<T>](#vector2tt12) | 
A vector that contains two values: x and y.

Unit: vp.

 |

#### Frame

Sets or returns the layout size and position of the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | 
Horizontal position.

Unit: vp.

Value range: (-∞, +∞).

 |
| y | number | No | No | 

Vertical position.

Unit: vp.

Value range: (-∞, +∞).

 |
| width | number | No | No | 

Component width.

Unit: vp.

Value range: \[0, +∞).

 |
| height | number | No | No | 

Component height.

Unit: vp.

Value range: \[0, +∞).

 |

#### Pivot

type Pivot = Vector2

Sets the pivot of the component. As the rotation or scaling center of the component, the pivot affects the rotation and scaling effects.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Vector2](#vector2) | X and Y coordinates of the pivot. The value is a floating point number in the range \[0.0, 1.0\], and the default value is **0.5**. |

#### Scale

type Scale = Vector2

Sets the scale factor of the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Vector2](#vector2) | Scale factor along the x- and y-axis. The value is a floating point number, and the default value is **1.0**. |

#### Translation

type Translation = Vector2

Sets the translation amount of the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Vector2](#vector2) | 
Translation amount along the x- and y-axis.

Unit: px

 |

#### Rotation

type Rotation = Vector3

Sets the rotation angle of the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Vector3](#vector3) | 
Rotation angle around the x-, y-, and z-axes.

Unit: degree

 |

#### Offset

type Offset = Vector2

Sets the offset of the component or effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Vector2](#vector2) | 
Offset along the x- and y-axis.

Unit: vp.

 |

#### Matrix4

type Matrix4 = \[number,number,number,number,number,number,number,number,number,number,number,number,number,number,number,number\]

Sets a 4x4 matrix.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| 
\[number,number,number,number,

number,number,number,number,

number,number,number,number,

number,number,number,number\]

 | 

A 16-element array representing a 4x4 matrix.

Value range of each number: (-∞, +∞)

 |

The **Matrix4** type is used to set transformation information for components. The following is an example:

const transform: Matrix4 = \[
  1, 0, 45, 0,
  0, 1,  0, 0,
  0, 0,  1, 0,
  0, 0,  0, 1
\]

#### Vector2

Defines a vector that contains the x and y coordinate values.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | 
X coordinate value of the vector.

Value range: (-∞, +∞).

 |
| y | number | No | No | 

Y coordinate value of the vector.

Value range: (-∞, +∞).

 |

#### Vector3

Represents a vector including three values: x, y, and z.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | 
Rotation angle along the x-axis.

Value range: (-∞, +∞).

 |
| y | number | No | No | 

Rotation angle along the y-axis.

Value range: (-∞, +∞).

 |
| z | number | No | No | 

Rotation angle along the z-axis.

Value range: (-∞, +∞).

 |

#### Vector2T<T>12+

Represents a vector of the T type that contains two values: x and y.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | T | No | No | X coordinate value of the vector. |
| y | T | No | No | Y coordinate value of the vector. |

#### DrawContext

Graphics drawing context, which provides the canvas width and height required for drawing.

#### \[h2\]size

get size(): Size

Obtains the width and height of the canvas.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [Size](#size) | Width and height of the canvas. |

#### \[h2\]sizeInPixel12+

get sizeInPixel(): Size

Obtains the width and height of the canvas in px.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [Size](#size) | Width and height of the canvas, in px. |

#### \[h2\]canvas

get canvas(): drawing.Canvas

Obtains the canvas used for drawing.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [drawing.Canvas](../../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-drawing-drawing-module/class-canvas/document.md) | Canvas for drawing. |

**Example**

import { RenderNode, FrameNode, NodeController, DrawContext } from "@kit.ArkUI";

class MyRenderNode extends RenderNode {
  flag: boolean = false;

  draw(context: DrawContext) {
    const size = context.size;
    const canvas = context.canvas;
    const sizeInPixel = context.sizeInPixel;
  }
}

const renderNode = new MyRenderNode();
renderNode.frame = { x: 0, y: 0, width: 100, height: 100 };
renderNode.backgroundColor = 0xff519db4;

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/u9YOPOp-RoGSzPXhXzyESQ/en-us_image_0000002568685077.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC520847097B98AC2A2521332D1F05BACFC27FA0DE63914DACB9606E0930EAB8)

#### Edges<T>12+

Describes the edges.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | T | No | No | Left edge. |
| top | T | No | No | Top edge. |
| right | T | No | No | Right edge. |
| bottom | T | No | No | Bottom edge. |

#### LengthUnit12+

Enumerates length units.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| PX | 0 | Length in px. |
| VP | 1 | Length in vp. |
| FP | 2 | Length in fp. |
| PERCENT | 3 | Length in percentage. |
| LPX | 4 | Length in lpx. |

#### SizeT<T>12+

Sets the width and height attributes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | T | No | No | Width. |
| height | T | No | No | Height. |

#### LengthMetricsUnit12+

Enumerates length units.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | Length in vp. |
| PX | 1 | Length in px. |

#### LengthMetrics12+

Defines the length attribute. When the length unit is PERCENT, the value **1** indicates 100%.

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | number | No | No | Value of the length property. |
| unit | [LengthUnit](#lengthunit12) | No | No | Unit of the length property. The default value is VP. |

#### \[h2\]constructor12+

constructor(value: number, unit?: LengthUnit)

A constructor used to create a **LengthMetrics** instance. If the **unit** parameter is omitted or explicitly set to **undefined**, the default unit VP is used. If it is set to a value that is not of the LengthUnit type, the default value 0 VP is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value of the length property.

Value range: (-∞, +∞).

 |
| unit | [LengthUnit](#lengthunit12) | No | Unit of the length property. |

#### \[h2\]px12+

static px(value: number): LengthMetrics

Creates a length property in px.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value of the length property.

Value range: (-∞, +∞).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [LengthMetrics](#lengthmetrics12) | Instance of the **LengthMetrics** class. |

#### \[h2\]vp12+

static vp(value: number): LengthMetrics

Creates a length property in vp.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value of the length property.

Value range: (-∞, +∞).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [LengthMetrics](#lengthmetrics12) | Instance of the **LengthMetrics** class. |

#### \[h2\]fp12+

static fp(value: number): LengthMetrics

Creates a length property in fp.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value of the length property.

Value range: (-∞, +∞).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [LengthMetrics](#lengthmetrics12) | Instance of the **LengthMetrics** class. |

#### \[h2\]percent12+

static percent(value: number): LengthMetrics

Creates a length property in percent. The value **1** indicates 100%.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value of the length property.

Value range: \[0, 1\].

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [LengthMetrics](#lengthmetrics12) | Instance of the **LengthMetrics** class. |

#### \[h2\]lpx12+

static lpx(value: number): LengthMetrics

Creates a length property in lpx.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value of the length property.

Value range: (-∞, +∞).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [LengthMetrics](#lengthmetrics12) | Instance of the **LengthMetrics** class. |

#### \[h2\]resource12+

static resource(value: Resource): LengthMetrics

Represents the length of a resource of the Resource type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Resource | Yes | Value of the length property. |

**Return value**

| Type | Description |
| :-- | :-- |
| [LengthMetrics](#lengthmetrics12) | Instance of the **LengthMetrics** class. |

**Example**

Use LengthMetrics to set the padding and margin attributes of Row.

import { LengthMetrics, LengthUnit } from '@kit.ArkUI';

@Entry
@Component
struct SizeExample {
  build() {
    Column({ space: 10 }) {
      Text('margin and padding:')
        .fontSize(12)
        .fontColor(0xCCCCCC)
        .width('90%')
      Row() {
        Row() {
          Row()
            .size({ width: '100%', height: '100%' })
            .backgroundColor('#ffd5d5d5')
        }
        .width(80)
        .height(80)
        .padding({
          top: new LengthMetrics(20, LengthUnit.VP),
          bottom: LengthMetrics.px(15),
          start: LengthMetrics.vp(10),
          end: LengthMetrics.fp(20)
        })
        .margin({
          top: LengthMetrics.percent(0.1),
          bottom: LengthMetrics.lpx(20),
          start: LengthMetrics.resource($r('app.float.row\_margin\_start')),
          end: LengthMetrics.vp(10)
        })
        .backgroundColor(Color.White)
      }
      .backgroundColor("#ff2787d9")
    }
    .width('100%')
    .margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/YFoLZLDqTCuTVSQ7Fvrl-w/en-us_image_0000002568765087.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03CE0111E9AD600254B8BC678F1AB70C00008F0D9DE6A563479F958D5539B8F7)

#### ColorMetrics12+

Used to mix colors.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]numeric12+

static numeric(value: number): ColorMetrics

Instantiates the **ColorMetrics** class using a color in HEX format.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Color in HEX format.

RGB and ARGB color values are supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ColorMetrics](#colormetrics12) | Instance of the **ColorMetrics** class. |

#### \[h2\]rgba12+

static rgba(red: number, green: number, blue: number, alpha?: number): ColorMetrics

Instantiates the **ColorMetrics** class using colors in RGB or RGBA format.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| red | number | Yes | Red component of the color. The value is an integer ranging from 0 to 255. |
| green | number | Yes | Green component of the color. The value is an integer ranging from 0 to 255. |
| blue | number | Yes | Blue component of the color. The value is an integer ranging from 0 to 255. |
| alpha | number | No | 
Alpha component of the color. The value is a floating point number ranging from 0.0 to 1.0. The default value is **1.0** (fully opaque).

Note: If alpha is less than 0, the color is fully transparent. If alpha is greater than 1, the color is opaque.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ColorMetrics](#colormetrics12) | Instance of the **ColorMetrics** class. |

#### \[h2\]colorWithSpace20+

static colorWithSpace(colorSpace: ColorSpace, red: number, green: number, blue: number, alpha?: number): ColorMetrics

Creates a **ColorMetrics** instance using specified [ColorSpace](../../../../arkts-components/common-definitions/enums/document.md#colorspace20) and RGBA values. Only certain attributes support color configuration in the display-p3 color space.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colorSpace | [ColorSpace](../../../../arkts-components/common-definitions/enums/document.md#colorspace20) | Yes | Color space used to specify the color. If ColorSpace.DISPLAY\_P3 is used, the [setWindowColorSpace](../../../window-manager/ohos-window-window/interface-window/document.md#setwindowcolorspace9-1) API must be called to set the current window to the wide color gamut mode. |
| red | number | Yes | Red component of the color. The value is a floating point number ranging from 0 to 1. |
| green | number | Yes | Green component of the color. The value is a floating point number ranging from 0 to 1. |
| blue | number | Yes | Blue component of the color. The value is a floating point number ranging from 0 to 1. |
| alpha | number | No | Alpha component of the color. The value is a floating point number ranging from 0.0 to 1.0. The default value is **1.0** (fully opaque). |

**Return value**

| Type | Description |
| :-- | :-- |
| [ColorMetrics](#colormetrics12) | Instance of the **ColorMetrics** class. |

#### \[h2\]resourceColor12+

static resourceColor(color: ResourceColor): ColorMetrics

Instantiates the **ColorMetrics** class using a color in resource reference format.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [ResourceColor](../../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | Yes | Color in resource reference format. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ColorMetrics](#colormetrics12) | Instance of the **ColorMetrics** class. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [System Resource Error Codes](../../../../error-codes/ui/system-resource-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible cause:1.The type of the input color parameter is not ResourceColor;2.The format of the input color string is not RGB or RGBA. |
| 180003 | Failed to obtain the color resource. |

#### \[h2\]blendColor12+

blendColor(overlayColor: ColorMetrics): ColorMetrics

Blends a specified color (**overlayColor**) with the current color and returns the resulting color.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| overlayColor | [ColorMetrics](#colormetrics12) | Yes | Color to overlay. The alpha value determines the blending strength: **1.0** indicates complete opacity (fully covers the base color), and **0.0** indicates complete transparency (returns the original color). |

**Return value**

| Type | Description |
| :-- | :-- |
| [ColorMetrics](#colormetrics12) | New color object with red, green, blue, and alpha channels representing the blended result of the current color and overlay color. |

**Blending formula**:

The resulting alpha is fully opaque. The RGB values are calculated using the following formula:

result\_rgb = overlay\_rgb\*(overlay\_alpha) + (1 - overlay\_alpha) \* base\_rgb

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. The type of the input parameter is not ColorMetrics. |

#### \[h2\]color12+

get color(): string

Obtains the color of **ColorMetrics**. The return value is a string indicating an RGBA color value.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| string | String indicating an RGBA color value. Example: **'rgba(255, 100, 255, 0.5)'** |

#### \[h2\]red12+

get red(): number

Obtains the red component of the ColorMetrics color.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Red component of the color. The value is an integer ranging from 0 to 255. |

#### \[h2\]green12+

get green(): number

Obtains the green component of the ColorMetrics color.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Green component of the color. The value is an integer ranging from 0 to 255. |

#### \[h2\]blue12+

get blue(): number

Obtains the blue component of the ColorMetrics color.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Blue component of the color. The value is an integer ranging from 0 to 255. |

#### \[h2\]alpha12+

get alpha(): number

Obtains the alpha component of the ColorMetrics color.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Alpha component of the color. The value is an integer ranging from 0 to 255. |

**Example**

import { ColorMetrics } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

function getBlendColor(baseColor: ResourceColor): ColorMetrics {
  let sourceColor: ColorMetrics;
  try {
    // When resourceColor and blendColor of ColorMetrics are used, add exception handling.
    // Error codes 401 and 180003 of the ArkUI subsystem may be returned.
    // 61 157 180
    sourceColor = ColorMetrics.resourceColor(baseColor).blendColor(ColorMetrics.resourceColor("#083d9db4"));
    console.info(\`current color is ${sourceColor.color} r:${sourceColor.red} g:${sourceColor.green} b:${sourceColor.blue} a :${sourceColor.alpha}\`);
  } catch (error) {
    console.error("getBlendColor failed, code = " + (error as BusinessError).code + ", message = " +
    (error as BusinessError).message);
    sourceColor = ColorMetrics.resourceColor("#19000000");
  }
  return sourceColor;
}

@Entry
@Component
struct ColorMetricsSample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button("ColorMetrics blendColor")
        .width('80%')
        .align(Alignment.Center)
        .height(50)
        .backgroundColor(getBlendColor("#ff3d9db4").color)
        .margin(10)
      Button("ColorMetrics numeric")
        .width('80%')
        .align(Alignment.Center)
        .height(50)
        .backgroundColor(ColorMetrics.numeric(0xff707070).color)
        .margin(10)
      Button("ColorMetrics rgba")
        .width('80%')
        .align(Alignment.Center)
        .height(50)
        .backgroundColor(ColorMetrics.rgba(0, 74, 175, 255).color)
        .margin(10)
      Button("ColorMetrics colorWithSpace")
        .width('80%')
        .align(Alignment.Center)
        .height(50)
        .backgroundColor(ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0.4392, 0.4392, 0.4392).color)
        .margin(10)
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/lpxBtfULQk6atRRvKZE9rQ/en-us_image_0000002537765362.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40451EDEA45E81AD7E2799BD92921BCDD1557F40B517BDDF67F7F14D0F251829)

#### Corners<T>12+

Describes the four corners.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| topLeft | T | No | No | Radius of the upper left corner. |
| topRight | T | No | No | Radius of the upper right corner. |
| bottomLeft | T | No | No | Radius of the lower left corner. |
| bottomRight | T | No | No | Radius of the lower right corner. |

#### CornerRadius12+

type CornerRadius = Corners<Vector2>

Sets the semi-axis lengths for the x-axis and y-axis of the rounded corners.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Corners](#cornerst12)<[Vector2](#vector2)\> | Semi-axis lengths for the x-axis and y-axis of the rounded corners. |

#### BorderRadiuses12+

type BorderRadiuses = Corners<number>

Sets the uniform radius of the four corners.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Corners](#cornerst12)<number> | Uniform radius of the four corners. |

#### Rect12+

type Rect = common2D.Rect

Describes a rectangle.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [common2D.Rect](../../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#rect) | Rectangle. |

#### RoundRect12+

Describes a rectangle with rounded corners.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| rect | [Rect](#rect12) | No | No | Attributes of the rectangle. |
| corners | [CornerRadius](#cornerradius12) | No | No | Attributes of rounded corners. |

#### Circle12+

Describes a circle.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| centerX | number | No | No | X-coordinate of the center of the circle, in px. |
| centerY | number | No | No | Y-coordinate of the center of the circle, in px. |
| radius | number | No | No | 
Radius of the circle, in px.

Value range: \[0, +∞).

 |

#### CommandPath12+

Describes the command for drawing a path.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| [commands](../../../../arkts-components/graphic-drawing/path/document.md#commands) | string | No | No | 
Commands for drawing a path. For details about how to convert pixel units, see [Pixel Units](../../../../arkts-components/common-definitions/pixel-units/document.md).

Unit: px

 |

#### ShapeMask12+

Describes the shape mask.

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fillColor | number | No | No | 
Describes the fill color of the mask, in ARGB format. The default value is **0XFF000000**.

A color with only the transparency is generated based on the transparency and brightness of **fillColor**. The higher the brightness, the more transparent the color. Then, the color is blended with the color of **RenderNode** using the [BlendMode.SRC\_IN](../../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-drawing-drawing-module/enums/document.md#blendmode) API to generate the final color.

 |
| strokeColor | number | No | No | 

Sets the stroke color for the mask, in ARGB format. The default value is **0XFF000000**.

A color with only the transparency is generated based on the transparency and brightness of **strokeColor**. The higher the brightness, the more transparent the color. Then, the color is blended with the color of **RenderNode** using the [BlendMode.SRC\_IN](../../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-drawing-drawing-module/enums/document.md#blendmode) API to generate the final color.

 |
| strokeWidth | number | No | No | Sets the stroke width for the mask, in px. The default value is **0**. |

#### \[h2\]constructor12+

constructor()

A constructor used to create a **ShapeMask** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]setRectShape12+

setRectShape(rect: Rect): void

Sets a rectangle mask.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rect | [Rect](#rect12) | Yes | Shape of the rectangle. |

**Example**

import { RenderNode, FrameNode, NodeController, ShapeMask } from '@kit.ArkUI';

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const mask = new ShapeMask();
    mask.setRectShape({
      left: 0,
      right: uiContext.vp2px(150),
      top: 0,
      bottom: uiContext.vp2px(150)
    });
    mask.fillColor = 0X55FF0000;

    const renderNode = new RenderNode();
    renderNode.frame = {
      x: 0,
      y: 0,
      width: 150,
      height: 150
    };
    renderNode.backgroundColor = 0XFF00FF00;
    renderNode.shapeMask = mask;

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/TGUZxZj_T9mBevlH-226ng/en-us_image_0000002537925302.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2655DA06542157F80641CB0E641BA7C260B22DBDF14C3B2954A7EBAB90AC710E)

#### \[h2\]setRoundRectShape12+

setRoundRectShape(roundRect: RoundRect): void

Sets the mask in the shape of a rectangle with rounded corners.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| roundRect | [RoundRect](#roundrect12) | Yes | Shape of the rectangle with rounded corners. |

**Example**

import { RenderNode, FrameNode, NodeController, ShapeMask,RoundRect} from '@kit.ArkUI';

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const mask = new ShapeMask();
    const roundRect: RoundRect = {
      rect: { left: 0, top: 0, right: uiContext.vp2px(150), bottom: uiContext.vp2px(150) },
      corners: {
        topLeft: { x: 32, y: 32 },
        topRight: { x: 32, y: 32 },
        bottomLeft: { x: 32, y: 32 },
        bottomRight: { x: 32, y: 32 }
      }
    }
    mask.setRoundRectShape(roundRect);
    mask.fillColor = 0X55FF0000;

    const renderNode = new RenderNode();
    renderNode.frame = { x: 0, y: 0, width: 150, height: 150 };
    renderNode.backgroundColor = 0XFF00FF00;
    renderNode.shapeMask = mask;

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/mSp83GpKRJaraIDZEyXTxw/en-us_image_0000002568685079.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D8D24237B4E8EAD2ED3181F5E771B9311D2D1AFD10E28E432F93E5D8136D3A2)

#### \[h2\]setCircleShape12+

setCircleShape(circle: Circle): void

Sets a round mask.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| circle | [Circle](#circle12) | Yes | Round shape. |

**Example**

import { RenderNode, FrameNode, NodeController, ShapeMask } from '@kit.ArkUI';

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const mask = new ShapeMask();
    mask.setCircleShape({ centerY: uiContext.vp2px(75), centerX: uiContext.vp2px(75), radius: uiContext.vp2px(75) });
    mask.fillColor = 0X55FF0000;

    const renderNode = new RenderNode();
    renderNode.frame = {
      x: 0,
      y: 0,
      width: 150,
      height: 150
    };
    renderNode.backgroundColor = 0XFF00FF00;
    renderNode.shapeMask = mask;

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/dstvsmiKQ76nYWxpyNkE1Q/en-us_image_0000002568765089.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E32900C7476D61AD8576DE9B08D92A1BB0FCA10790396010783A0CD0B62D3E5E)

#### \[h2\]setOvalShape12+

setOvalShape(oval: Rect): void

Sets an oval mask.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| oval | [Rect](#rect12) | Yes | Oval shape. |

**Example**

import { RenderNode, FrameNode, NodeController, ShapeMask } from '@kit.ArkUI';

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const mask = new ShapeMask();
    mask.setOvalShape({ left: 0, right: uiContext.vp2px(150), top: 0, bottom: uiContext.vp2px(100) });
    mask.fillColor = 0X55FF0000;

    const renderNode = new RenderNode();
    renderNode.frame = { x: 0, y: 0, width: 150, height: 150 };
    renderNode.backgroundColor = 0XFF00FF00;
    renderNode.shapeMask = mask;

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/yPo2szR1QHqmtaK17WwfDw/en-us_image_0000002537765364.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7364727DE10112BC396AED33DA82FF249002D44F88EB40188FDF5E2826F12F28)

#### \[h2\]setCommandPath12+

setCommandPath(path: CommandPath): void

Sets the command for drawing a path.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | [CommandPath](#commandpath12) | Yes | Command for drawing a path. |

**Example**

import { RenderNode, FrameNode, NodeController, ShapeMask } from '@kit.ArkUI';

const mask = new ShapeMask();
mask.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });
mask.fillColor = 0X55FF0000;

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0XFF00FF00;
renderNode.shapeMask = mask;

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/plGGOmpPSl-wWsF8unozcQ/en-us_image_0000002537925304.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E4C48E73A377201A2BF11CBAD98C8F601B9D921845819E48961DD8DDC652AEA)

#### ShapeClip12+

Sets the clipping shape.

#### \[h2\]constructor12+

constructor()

A constructor used to create a **ShapeClip** object.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

#### \[h2\]setRectShape12+

setRectShape(rect: Rect): void

Sets a rectangle for shape clipping.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rect | [Rect](#rect12) | Yes | Shape of the rectangle. |

**Example**

import { RenderNode, FrameNode, NodeController, ShapeClip } from '@kit.ArkUI';

const clip = new ShapeClip();
clip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0xff519db4;
renderNode.shapeClip = clip;
const shapeClip = renderNode.shapeClip;

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
        .borderWidth(1)
        .margin({ bottom: 20 })
      Button("setRectShape")
        .onClick(() => {
          shapeClip.setRectShape({
            left: 0,
            right: 150,
            top: 0,
            bottom: 150
          });
          renderNode.shapeClip = shapeClip;
        })
    }.margin(20)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/pe6LKvb_TnKI6q3I2zG4KQ/en-us_image_0000002568685081.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4870F9EB90EDB4077EEC0E34FCF7799F4C0ECC3CEBB1F84000FE272DFEA308E8)

#### \[h2\]setRoundRectShape12+

setRoundRectShape(roundRect: RoundRect): void

Sets a rounded rectangle for shape clipping.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| roundRect | [RoundRect](#roundrect12) | Yes | Shape of the rectangle with rounded corners. |

**Example**

import { RenderNode, FrameNode, NodeController, ShapeClip } from '@kit.ArkUI';

const clip = new ShapeClip();
clip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0XFF00FF00;
renderNode.shapeClip = clip;

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
        .borderWidth(1)
      Button("setRoundRectShape")
        .onClick(() => {
          renderNode.shapeClip.setRoundRectShape({
            rect: {
              left: 0,
              top: 0,
              right: this.getUIContext().vp2px(150),
              bottom: this.getUIContext().vp2px(150)
            },
            corners: {
              topLeft: { x: 32, y: 32 },
              topRight: { x: 32, y: 32 },
              bottomLeft: { x: 32, y: 32 },
              bottomRight: { x: 32, y: 32 }
            }
          });
        })
    }
  }
}

#### \[h2\]setCircleShape12+

setCircleShape(circle: Circle): void

Sets a circle for shape clipping.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| circle | [Circle](#circle12) | Yes | Round shape. |

**Example**

import { RenderNode, FrameNode, NodeController, ShapeClip } from '@kit.ArkUI';

const clip = new ShapeClip();
clip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0XFF00FF00;
renderNode.shapeClip = clip;

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
        .borderWidth(1)
      Button("setCircleShape")
        .onClick(() => {
          renderNode.shapeClip.setCircleShape({ centerY: 75, centerX: 75, radius: 75 });

        })
    }
  }
}

#### \[h2\]setOvalShape12+

setOvalShape(oval: Rect): void

Sets an oval shape for shape clipping.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| oval | [Rect](#rect12) | Yes | Oval shape. |

**Example**

import { RenderNode, FrameNode, NodeController, ShapeClip } from '@kit.ArkUI';

const clip = new ShapeClip();
clip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0XFF00FF00;
renderNode.shapeClip = clip;

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
        .borderWidth(1)
      Button("setOvalShape")
        .onClick(() => {
          renderNode.shapeClip.setOvalShape({
            left: 0,
            right: this.getUIContext().vp2px(150),
            top: 0,
            bottom: this.getUIContext().vp2px(100)
          });
        })
    }
  }
}

#### \[h2\]setCommandPath12+

setCommandPath(path: CommandPath): void

Sets the command for drawing a path.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | [CommandPath](#commandpath12) | Yes | Command for drawing a path. |

**Example**

import { RenderNode, FrameNode, NodeController, ShapeClip } from '@kit.ArkUI';

const clip = new ShapeClip();
clip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0XFF00FF00;
renderNode.shapeClip = clip;

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.myNodeController)
        .borderWidth(1)
      Button("setCommandPath")
        .onClick(() => {
          renderNode.shapeClip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });
        })
    }
  }
}

#### edgeColors12+

edgeColors(all: number): Edges<number>

Generates an **edgeColors** object with the specified edge color for all edges.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| all | number | Yes | 
Edge color, in ARGB format, for example, **0xffff00ff**.

Value range: \[0, 0xffffffff\]

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [Edges](#edgest12)<number> | **edgeColors** object whose edge colors are all at the specified value. |

**Example**

import { RenderNode, FrameNode, NodeController, edgeColors } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = { x: 0, y: 0, width: 150, height: 150 };
renderNode.backgroundColor = 0xffd5d5d5;
renderNode.borderWidth = { left: 8, top: 8, right: 8, bottom: 8 };
renderNode.borderColor = edgeColors(0xff519db4);

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }.margin(30)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/qs-MnEMcQzCPcG47Dk1KCg/en-us_image_0000002568765091.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=258DAC7084B072F4A0E51DDB37DEA0DD2DD77CFCA1B6C98E0E36024148652918)

#### edgeWidths12+

edgeWidths(all: number): Edges<number>

Generates an **edgeWidths** object with the specified edge width for all edges.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| all | number | Yes | 
Edge width, in vp.

Value range: \[0, +∞).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [Edges](#edgest12)<number> | **edgeWidths** object whose edge widths are all at the specified value. |

**Example**

import { RenderNode, FrameNode, NodeController, edgeWidths } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0xffd5d5d5;
renderNode.borderWidth = edgeWidths(8);
renderNode.borderColor = {
  left: 0xff519db4,
  top: 0xff519db4,
  right: 0xff519db4,
  bottom: 0xff519db4
};

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }.margin(30)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/9yM1cwODRzqHd8kCBHzZqA/en-us_image_0000002537765366.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA23BA88A16B9DA6BCDF4FB03BF7705DE65ED06975C36935C7FE1C699526D6CE)

#### borderStyles12+

borderStyles(all: BorderStyle): Edges<BorderStyle>

Generates a border style object with the specified border style color for all borders.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| all | [BorderStyle](../../../../arkts-components/common-definitions/enums/document.md#borderstyle) | Yes | Border style. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Edges](#edgest12)<[BorderStyle](../../../../arkts-components/common-definitions/enums/document.md#borderstyle)\> | **borderStyles** object whose borders are all in the specified style. |

**Example**

import { RenderNode, FrameNode, NodeController, borderStyles } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0xffd5d5d5;
renderNode.borderWidth = {
  left: 8,
  top: 8,
  right: 8,
  bottom: 8
};
renderNode.borderColor = {
  left: 0xff519db4,
  top: 0xff519db4,
  right: 0xff519db4,
  bottom: 0xff519db4
};
renderNode.borderStyle = borderStyles(BorderStyle.Dotted);

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }.margin(30)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/RTc6bGZsTxCzbUjM7kiR0w/en-us_image_0000002537925306.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08EED57B1D75265C4B796639DE4AADC0002B090F1E93EB07A4289AD945728566)

#### borderRadiuses12+

borderRadiuses(all: number): BorderRadiuses

Generates a **borderRadiuses** object with the specified radius for all border corners.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| all | number | Yes | 
Radius of border corners.

Unit: vp.

Value range: \[0, +∞).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [BorderRadiuses](#borderradiuses12) | **borderRadiuses** object whose border corners all have the specified radius. |

**Example**

import { RenderNode, FrameNode, NodeController, borderRadiuses } from '@kit.ArkUI';

const renderNode = new RenderNode();
renderNode.frame = {
  x: 0,
  y: 0,
  width: 150,
  height: 150
};
renderNode.backgroundColor = 0xff519db4;
renderNode.borderRadius = borderRadiuses(32);

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new FrameNode(uiContext);

    const rootRenderNode = this.rootNode.getRenderNode();
    if (rootRenderNode !== null) {
      rootRenderNode.appendChild(renderNode);
    }

    return this.rootNode;
  }
}

@Entry
@Component
struct Index {
  private myNodeController: MyNodeController = new MyNodeController();

  build() {
    Row() {
      NodeContainer(this.myNodeController)
    }.margin(20)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/pqaYV_UcQ3enQjdHbmVGTg/en-us_image_0000002568685083.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A54D960CFA85C0AA942D5F37F09BAAF1213D587AB6DDF0FD84D5208AF85C84A0)
