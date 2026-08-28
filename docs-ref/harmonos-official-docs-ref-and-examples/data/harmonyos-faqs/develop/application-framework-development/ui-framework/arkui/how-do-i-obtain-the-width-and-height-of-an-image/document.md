# How do I obtain the width and height of an image?

Use the [onComplete](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-image#oncomplete) event of the **Image** component, which is triggered when an image is successfully loaded or decoded and returns the size of the loaded image. The code snippet is as follows:

Image($r('app.media.startIcon'))
  .width(200)
  .height(200)
  .objectFit(ImageFit.Contain)
  .onComplete((event) => {
    let imageWidth = event?.width;
    let imageHeight = event?.height;
    console.info('imageWidth:'+imageWidth,'imageHeight:'+imageHeight);
  })

**Reference**

[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)
