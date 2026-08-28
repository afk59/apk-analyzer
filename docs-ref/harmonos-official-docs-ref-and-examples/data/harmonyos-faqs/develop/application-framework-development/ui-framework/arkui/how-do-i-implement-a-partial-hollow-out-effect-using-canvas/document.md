# How do I implement a partial hollow-out effect using Canvas?

1.  Use [Canvas](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-components-canvas-canvas) to draw a hollow circle.
2.  Use the **Stack** component to overlay the area that needs to be transparently displayed.

Refer to the code snippet below.

@Entry
@Component
struct HollowOutWithCanvas {
  @State circleCenterX: number = 0;
  @State circleCenterY: number = 0;
  @State circleRadius: number = 1000;
  private contextSettings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.contextSettings);

  build() {
    Row() {
      Column() {
        Stack() {
          Image($r('app.media.startIcon'))
            .height(300)
          // Use Canvas to draw masks to cover images, cameras, etc
          Canvas(this.context)
            .width('100%')
            .height('100%')
            .backgroundColor('#00000000')
            .onReady(() => {
              this.circleCenterX = this.context.width / 2;
              this.circleCenterY = this.context.height / 2;
              this.context.fillStyle = 'rgba(0,0,0,0.67)';
              if (this.circleRadius > this.circleCenterX) {
                this.circleRadius = this.circleCenterX / 2;
              }
              // Draw a circular path for semi transparent filling
              this.context.beginPath();
              this.context.moveTo(0, 0);
              this.context.lineTo(0, this.context.height);
              this.context.lineTo(this.context.width, this.context.height);
              this.context.lineTo(this.context.width, 0);
              this.context.lineTo(0, 0);
              this.context.arc(this.circleCenterX, this.circleCenterY, this.circleRadius, 0, Math.PI \* 2);
              this.context.fill();
              this.context.closePath();
            })
        }
        .width('1456px')
        .height('1456px')
      }
      .width('100%')
    }
    .height('100%')
  }
}
