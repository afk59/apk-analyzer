# How do I implement the onPreviewFrame callback function for photo preview?

Use the dual-channel preview to implement the **onPreviewFrame** callback function, and set **previewOutput2** to receive continuous data. Refer to the sample code below, which stores the first three frames of data.

this.previewOutput = this.cameraManager!.createPreviewOutput(previewProfilesArray\[5\], surfaceId);
let size: image.Size = {
  width: 640,
  height: 480
}
let receiver: image.ImageReceiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
receiver.on('imageArrival', () => {
  receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
    if (err || nextImage === undefined) {
      console.error('readNextImage failed');
      return;
    }
    nextImage.getComponent(image.ComponentType.JPEG, (err: BusinessError, imgComponent: image.Component) => {
      if (err || imgComponent === undefined) {
        console.error('getComponent failed');
      }
      if (imgComponent && imgComponent.byteBuffer as ArrayBuffer && this.count<3) {
        this.count = this.count + 1
        let path: string = context.filesDir + "/image.yuv";
        let file = fileIo.openSync(path, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
        let opt: WriteOptions = {
          // 2048 extra bytes of data
          length: imgComponent.byteBuffer.byteLength - 2048
        }
        fileIo.write(file.fd, imgComponent.byteBuffer, opt).then((writeLen) => {
          console.info("write data to file succeed and size is:" + writeLen);
          fileIo.closeSync(file);
        }).catch((err: BusinessError) => {
          console.info("write data to file failed with error message: " + err.message + ", error code: " + err.code);
        });
      }
      nextImage.release();
    })
  })
})
let ImageReceiverSurfaceId: string = await receiver.getReceivingSurfaceId();
this.previewOutput2 = this.cameraManager!.createPreviewOutput(previewProfilesArray\[5\], ImageReceiverSurfaceId);
