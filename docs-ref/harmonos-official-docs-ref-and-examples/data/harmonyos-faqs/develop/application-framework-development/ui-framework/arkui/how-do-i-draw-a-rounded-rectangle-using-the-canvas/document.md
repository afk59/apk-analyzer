# How do I draw a rounded rectangle using the canvas?

Use the **arc** method of the [CanvasRenderingContext2D](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-canvasrenderingcontext2d) object to draw arc paths and use the **lineTo** method to draw straight lines. The sample code is as follows:

@Entry
@Component
struct CanvasDrawRoundedRectangle {
  private readonly settings: RenderingContextSettings = new RenderingContextSettings(true);
  private readonly ctx: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  drawRoundRect(x: number, y: number, width: number, height: number, radius: number, strokeColor?: string,
    fillColor?: string, lineDash?: Array<number>) {
    if (width < 2 \* radius || height < 2 \* radius) {
      radius = Math.min(width, height) / 2;
    }
    strokeColor = strokeColor || '#333';
    lineDash = lineDash || \[\];
    this.ctx.beginPath();
    this.ctx.setLineDash(lineDash);
    // Draw the first arc path
    this.ctx.arc(x + radius, y + radius, radius, Math.PI, Math.PI \* 3 / 2);
    // Draw the first straight path
    this.ctx.lineTo(width - radius + x, y);
    // Draw the second arc path
    this.ctx.arc(width - radius + x, radius + y, radius, Math.PI \* 3 / 2, Math.PI \* 2);
    // Draw the second straight path
    this.ctx.lineTo(width + x, height + y - radius);
    // Draw the third arc path
    this.ctx.arc(width - radius + x, height - radius + y, radius, 0, Math.PI / 2);
    // Draw the third straight path
    this.ctx.lineTo(radius + x, height + y);
    // Draw the fourth arc path
    this.ctx.arc(radius + x, height - radius + y, radius, Math.PI / 2, Math.PI);
    // Draw the fourth straight path
    this.ctx.lineTo(x, y + radius);
    // Set brush color
    this.ctx.strokeStyle = strokeColor;
    // Stroke drawing
    this.ctx.stroke();
    if (fillColor) {
      this.ctx.fillStyle = fillColor;
      this.ctx.fill();
    }
    this.ctx.closePath();
  }

  build() {
    Row() {
      Column() {
        Canvas(this.ctx)
          .width('100%')
          .height('100%')
          .onReady(() => {
            this.drawRoundRect(50, 50, 100, 100, 10);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

The figure below shows the implementation effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/4QG1OY8HQl2ZX8huoDOtFw/en-us_image_0000002229758593.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062555Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F85A435639ABC81237F03818538CE5257F3D81332D211D12FE17FCDF2DCE35B)
