# DrawingRenderingContext

After the **DrawingRenderingContext** object is bound to the **Canvas** component, you can draw shapes, texts, and images on the **Canvas** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/IXheP_URRVaSN9b8Twi5pw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34CA838620DA6789E6AC32C01B892046DC10ACA6771A5AD550265628EB7C8EEC)

The initial APIs of this module are supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### constructor

constructor(unit?: LengthMetricsUnit)

Creates a **Canvas** object for drawing operations using the drawing API. Configuration of the unit mode for the **DrawingRenderingContext** object is supported.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| unit | [LengthMetricsUnit](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetricsunit12) | No | 
Unit mode of the **DrawingRenderingContext** object. The value cannot be changed once set. The configuration method is the same as that of [CanvasRenderingContext2D](../canvasrenderingcontext2d/document.md).

Invalid values **undefined**, **NaN** and **Infinity** are treated as the default value.

Default value: **DEFAULT**.

 |

#### size

get size(): Size

Obtains the size of the **DrawingRenderingContext** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [Size](#size-1) | Size of the **DrawingRenderingContext** object. |

#### canvas

get canvas(): DrawingCanvas

Obtains the canvas object for drawing content.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [DrawingCanvas](#drawingcanvas12) | Canvas object for drawing content. |

#### invalidate

invalidate(): void

Invalidates the component and triggers re-rendering of the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### DrawingCanvas12+

type DrawingCanvas = Canvas

Draws content on the **DrawingRenderingContext**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Canvas](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-drawing-drawing-module/class-canvas/document.md) | Canvas object. |

#### Size

Provides size information of the **DrawingRenderingContext** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | number | No | No | 
Width of the **DrawingRenderingContext** object, which corresponds to the width of the associated **Canvas** component.

The unit can be vp or px.

Default unit: vp

 |
| height | number | No | No | 

Height of the **DrawingRenderingContext** object, which corresponds to the height of the associated **Canvas** component.

The unit can be vp or px.

Default unit: vp

 |

#### Example

## Example 1: Drawing Shapes

This example demonstrates how to draw shapes using APIs in **DrawingRenderingContext**.

import { common2D, drawing } from '@kit.ArkGraphics2D';

// xxx.ets
@Entry
@Component
struct CanvasExample {
  private context: DrawingRenderingContext = new DrawingRenderingContext();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('50%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          let brush = new drawing.Brush();
          // Draw a circle with center at (200, 200) and radius of 100, filled with RGBA(39, 135, 217, 255).
          brush.setColor({
            alpha: 255,
            red: 39,
            green: 135,
            blue: 217
          });
          this.context.canvas.attachBrush(brush);
          this.context.canvas.drawCircle(200, 200, 100);
          this.context.canvas.detachBrush();
          this.context.invalidate();
        })
      Button("Clear")
        .width('120')
        .height('50')
        .onClick(() => {
          let color: common2D.Color = {
            alpha: 0,
            red: 0,
            green: 0,
            blue: 0
          };
          // Fill the canvas using RGBA(0, 0, 0, 0).
          this.context.canvas.clear(color);
          this.context.invalidate();
        })
    }
    .width('100%')
    .height('100%')
  }
}

Figure 1 Circle with center at (200, 200) and radius of 100, filled with RGBA(39, 135, 217, 255)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/HuSB8bqGSSGW30gNL4b8Xg/en-us_image_0000002568765565.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44ADEC80B7CC4F2094B18813E53379B8C9DD75A2EF0E1A391FE3558CA41B9864)

Figure 2 Clearing the canvas with the Clear button

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/hXlM_O5HRaaHrOfAEwYvMA/en-us_image_0000002537765840.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AED928BF2AE7E19E571A7D835953649CEE45603600299878456EC544DA113D61)

## Example 2: Drawing Text

This example demonstrates how to draw custom text using [drawTextBlob](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-drawing-drawing-module/class-canvas/document.md#drawtextblob), with custom fonts loaded via [makeFromRawFile](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-drawing-drawing-module/class-typeface/document.md#makefromrawfile18) (available since API version 18). When the drawing API is used, custom fonts from the **rawfile** directory can be loaded directly with drawing.Typeface.[makeFromRawFile](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-drawing-drawing-module/class-typeface/document.md#makefromrawfile18), eliminating the need to pre-register fonts through this.uiContext.getFont().[registerFont](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-font/document.md#registerfont) or fontCollection.[loadFontSync](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#loadfontsync).

import { drawing } from '@kit.ArkGraphics2D';

// xxx.ets
@Entry
@Component
struct CanvasExample {
  private context: DrawingRenderingContext = new DrawingRenderingContext();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('50%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          let font = new drawing.Font();
          font.setSize(50);
          // Load the custom font file HarmonyOS\_Sans\_Bold.ttf from the rawfile directory.
          const myTypeFace = drawing.Typeface.makeFromRawFile($rawfile('HarmonyOS\_Sans\_Bold.ttf'));
          font.setTypeface(myTypeFace);
          const textBlob =
            drawing.TextBlob.makeFromString("Hello World", font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
          this.context.canvas.drawTextBlob(textBlob, 60, 100);
          this.context.invalidate();
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/KImVM3XcQimet45ESvzNxA/en-us_image_0000002537925780.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7855FC8165979ABB609473CD9C282CD8D3AD5CA1FD21DF9B9FA5FF3CDAF5AA20)
