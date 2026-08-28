# How do I save the video frame data received by ImageReceiver locally?

Refer to the sample code below, which stores the first three frames of data.

let size: image.Size = {
  width: 640,
  height: 480
}
let receiver: image.ImageReceiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
receiver.on('imageArrival', () => {
  console.info("imageArrival callback");
  receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
    if (err || nextImage === undefined) {
      console.error("receiveImage -error:" + err + " nextImage:" + nextImage);
      return;
    }
    nextImage.getComponent(image.ComponentType.JPEG, (err: BusinessError, imgComponent: image.Component) => {
      if (err || imgComponent === undefined) {
        console.error("receiveImage--getComponent -error:" + err + " imgComponent:" + imgComponent);
        return;
      }

      if (imgComponent.byteBuffer as ArrayBuffer) {
        let sourceOptions: image.SourceOptions = {
          sourceDensity: 120,
          sourcePixelFormat: 8,
          sourceSize: {
            height: 1080,
            width: 1920
          },
        }
        let imageResource = image.createImageSource(imgComponent.byteBuffer, sourceOptions);
        let imagePackerApi = image.createImagePacker();
        let packOpts: image.PackingOption = { format: "image/jpeg", quality: 90 };
        const filePath: string = context.getHostContext()!.cacheDir + "/image.jpg";
        let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
        imagePackerApi.packToFile(imageResource, file.fd, packOpts).then(() => {
          console.error('pack success: ' + filePath);
        }).catch((error: BusinessError) => {
          console.error('Failed to pack the image. And the error is: ' + error);
        })
        imageResource.createPixelMap({}).then((res) => {
          this.imgUrl = res;
        });
      } else {
        return;
      }
      nextImage.release();
    });
  });
});
