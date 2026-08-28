# How do I dynamically update the Canvas content?

In a declarative syntax, **Canvas** is driven by data to update the UI. You can use the @Watch decorator to listen for changes in data and bind a custom **draw()** method. When the data is updated, the method bound by @Watch will execute the drawing logic.

The code snippet is as follows:

@Entry
@Component
struct CanvasContentUpdate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  @State @Watch('draw')content: string = '';

  draw() {
    this.context.clearRect(0, 0, 200, 200); // Clean up canvas content
    this.context.fillText(this.content, 50, 50); // Refill
  }

  build() {
    Column() {
      Canvas(this.context)
        .width('100%')
        .height('25%')
        .backgroundColor('#F5DC62')
        .onReady(() => {
          //You can draw content here.
          this.context.font = '55px sans-serif';
          this.context.fillText(this.content, 50, 50);
        })
      TextInput({
        text:$$this.content
      })
    }
    .borderColor('#31525B')
    .borderWidth(12)
    .width('100%')
    .height('100%')
  }
}

**Reference**

[Drawing Custom Graphics Using the Canvas (Canvas)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-drawing-customization-on-canvas)
