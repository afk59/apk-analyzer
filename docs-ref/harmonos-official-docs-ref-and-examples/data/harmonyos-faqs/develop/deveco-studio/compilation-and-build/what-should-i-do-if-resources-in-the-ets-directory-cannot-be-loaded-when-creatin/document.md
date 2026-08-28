# What should I do if resources in the ets directory cannot be loaded when creating a new project or module?

**Symptom**

When creating a new project, local images in the **src/main/ets** directory cannot be loaded using **ImageBitmap** or other components.

**Possible Causes**

If a new project is created using DevEco Studio 6.0.0 Beta2 or later, image resources in the **src/main** directory of the module are not packaged by default. For details, see **[copyCodeResource](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-build-profile#table1476161719356)**.

**Solution**

1\. Place the resource files in the **ets** directory to the **resources** directory and reference the files in **$r** mode. For details, see the following:

// xxx.ets
@Entry
@Component
struct VideoPlayer {
  private controller: VideoController = new VideoController()
  private previewUris: Resource = $r('app.media.preview')
  private innerResource: Resource = $rawfile('videoTest.mp4')

  build() {
    Column() {
      Video({
        src: this.innerResource,
        previewUri: this.previewUris,
        controller: this.controller
      })
        .onUpdate((event) => { // Triggered when the playback progress changes.
          console.info("Video update.");
        })
        .onPrepared((event) => { // Triggered when video preparation is complete.
          console.info("Video prepared.");
        })
        .onError(() => { // Triggered when the video playback fails.
          console.error("Video error.");
        })
        .onStop(() => { // Triggered when the video playback stops.
          console.info("Video stopped.");
        })
    }
  }
}

2\. If the component does not support the **$r** writing method, you can obtain and use resources in the **resources** directory through the **resourceManager** resource APIs. For details, see the following:

// xxx.ets
@Entry
@Component
struct ImageExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // Replace "common/images/example.jpg" with the image resource file you use.
  // private img: ImageBitmap = new ImageBitmap("common/images/example.jpg"); // This relative path writing will make it impossible to record pictures in the new template
     private img: ImageBitmap = new ImageBitmap(this.getUIContext().getHostContext()?.resourceManager
    .getDrawableDescriptorByName("example")
    .getPixelMap()); // You can refer to the interface for using resourceManager

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 200)
          this.img.close()
        })
    }
    .width('100%')
    .height('100%')
  }
}
