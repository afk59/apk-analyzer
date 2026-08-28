# CanvasPattern

**CanvasPattern** represents an object, created by the [createPattern](../canvasrenderingcontext2d/document.md#createpattern) API, describing an image filling pattern based on the image and repetition mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/VpCFHBsJSY2p5VOtnhDIbQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09765AFD14BB22C1D401D3DB2274CCCDF3FF89A243ED9E74406BF8093E3D074F)

This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Methods

#### \[h2\]setTransform

setTransform(transform?: Matrix2D): void

Uses a **Matrix2D** object as a parameter to perform matrix transformation on the current **CanvasPattern** object.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| transform | [Matrix2D](../matrix2d/document.md) | No | 
Transformation matrix.

**undefined** and **null** are treated as invalid values, and no matrix transformation is performed.

Default value: no matrix transformation

 |

#### Example

This example demonstrates how to apply matrix transformations to a **CanvasPattern** object using the **setTransform** API.

// xxx.ets
@Entry
@Component
struct CanvasPatternPage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();
  private img: ImageBitmap = new ImageBitmap("common/pattern.jpg");
  private pattern: CanvasPattern | null = null;

  build() {
      Column() {
        Button("Click to set transform")
          .onClick(() => {
            this.matrix.scaleY = 1
            this.matrix.scaleX = 1
            this.matrix.translateX = 50
            this.matrix.translateY = 200
            if (this.pattern) {
              this.pattern.setTransform(this.matrix)
            }
            this.context.fillRect(0, 0, 480, 720)
          })
          .width("45%")
          .margin("5px")
        Canvas(this.context)
          .width('100%')
          .height('80%')
          .backgroundColor('#FFFFFF')
          .onReady(() => {
            this.pattern = this.context.createPattern(this.img, 'no-repeat')
            this.matrix.scaleY = 0.5
            this.matrix.scaleX = 0.5
            this.matrix.translateX = 50
            this.matrix.translateY = 50
            if (this.pattern) {
              this.context.fillStyle = this.pattern
              this.pattern.setTransform(this.matrix)
            }
            this.context.fillRect(0, 0, 480, 720)
          })
      }
      .width('100%')
      .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/r4y-d87rR8ijuiEbvbdZ4A/en-us_image_0000002568765527.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E188AEF9D1526F83EE2E689E81F3794D89B71C017E1CB298D5EB7A02FD894FBB)
