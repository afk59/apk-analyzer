# Using ImageReceiver to Receive Images

You can use the **ImageReceiver** class to obtain the surface ID of a component, read the latest image or the next image, and release ImageReceiver instances.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/_OcYMclESYq4GdmrsdV3_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=226EA66F34F3F7B79F7A46E2B71CC5AAA0DA8359F7F6F69E599F8D1490556CDC)

The ImageReceiver works as a consumer and needs a matching producer to provide data to work properly. Typical producers are the camera's photo or preview streams. The ImageReceiver merely serves as the recipient and consumer of images. The properties set in ImageReceiver, such as size and format, do not actually take effect. The parameters passed when creating the ImageReceiver object do not have a practical impact. Image properties need to be configured on the sending side (the producer), such as when setting up the [profile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-i#profile) for a [camera preview stream](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#createpreviewoutput).

The ImageReceiver can receive images from the camera's preview stream, allowing for [dual-channel preview](../../../../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/dual-channel-preview-arkts/document.md).

Read [Image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagereceiver) for APIs related to ImageReceiver.

#### How to Develop

Create an ImageReceiver object, obtain the surface ID to create a preview stream, register image listeners, and process each frame of the image in the preview stream as required.

1.  Import the required modules.
    
    import image from '@ohos.multimedia.image'
    import { camera } from '@kit.CameraKit';
    import { BusinessError } from '@ohos.base'
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Create an ImageReceiver object, through which you can obtain the surface ID of the preview stream.
    
    async function initImageReceiver(): Promise<void> {
      // Create an ImageReceiver object. The parameters in createImageReceiver do not have any impact on the received data.
      let size: image.Size = { width: imageWidth, height: imageHeight };
      let imageReceiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
      // Obtain the preview stream surface ID.
      let imageReceiverSurfaceId = await imageReceiver.getReceivingSurfaceId();
      console.info(\`initImageReceiver imageReceiverSurfaceId:${imageReceiverSurfaceId}\`);
    }
    
3.  Register a listener to process each frame of image data in the preview stream. The image data is returned from the underlying layer through the imageArrival event in ImageReceiver. For details about the APIs, see [ImageReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagereceiver).
    
    function onImageArrival(receiver: image.ImageReceiver) {
      // Subscribe to the imageArrival event.
      receiver.on('imageArrival', () => {
        // Obtain an image.
        receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
          if (err || nextImage === undefined) {
            console.error('readNextImage failed');
            return;
          }
          // Parse the image.
          nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError,
            imgComponent: image.Component) => {
            if (err || imgComponent === undefined) {
              console.error('getComponent failed');
            }
            if (imgComponent.byteBuffer) {
              // For details, see the description of parsing the image buffer data below. This example uses method 1.
              let width = nextImage.size.width; // Obtain the image width.
              let height = nextImage.size.height; // Obtain the image height.
              let stride = imgComponent.rowStride; // Obtain the image stride.
              console.debug(\`getComponent with width:${width} height:${height} stride:${stride}\`);
              // The value of stride is the same as that of width.
              if (stride == width) {
                let pixelMap = await image.createPixelMap(imgComponent.byteBuffer, {
                  size: { height: height, width: width },
                  srcPixelFormat: 8,
                })
              } else {
                // The value of stride is different from that of width.
                const dstBufferSize = width \* height \* 1.5;
                const dstArr = new Uint8Array(dstBufferSize);
                for (let j = 0; j < height \* 1.5; j++) {
                  // Different devices have different memory capacities. If the memory is insufficient, it might not be able to complete the write operation.
                  const srcBuf = new Uint8Array(imgComponent.byteBuffer, j \* stride, width);
                  dstArr.set(srcBuf, j \* width);
                }
                let pixelMap = await image.createPixelMap(dstArr.buffer, {
                  size: { height: height, width: width },
                  srcPixelFormat: 8,
                })
              }
            } else {
              console.error('byteBuffer is null');
            }
            // Release the resource when the buffer is not in use.
            // If an asynchronous operation is performed on the buffer, call nextImage.release() to release the resource after the asynchronous operation is complete.
            nextImage.release();
          })
        })
      })
    }
    

The following methods are available for parsing the image buffer data by using [image.Component](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-i#component9).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/OjFsMEs4QFS2uWGRyWAjGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F5D9A0C6D1A90319C1C412B8FFEAAC0893A4376300A870739580CA7D75012FC)

Check whether the image width matches the row stride. If they do not match, you can preprocess the data using either of the two methods outlined below.

Method 1: Remove the stride data from **imgComponent.byteBuffer**, obtain a new buffer by means of copy, and process the buffer by calling the API that does not support stride.

// The value of stride is different from that of width.
const dstBufferSize = width \* height \* 1.5
const dstArr = new Uint8Array(dstBufferSize)
for (let j = 0; j < height \* 1.5; j++) {
  const srcBuf = new Uint8Array(imgComponent.byteBuffer, j \* stride, width)
  dstArr.set(srcBuf, j \* width)
}
let pixelMap = await image.createPixelMap(dstArr.buffer, {
  size: { height: height, width: width },
  srcPixelFormat: 8,
})

Method 2: Create a PixelMap based on the value of stride \* height, and call **cropSync** of the PixelMap to crop redundant pixels.

// Create a PixelMap, with width set to the value of stride.
let pixelMap = await image.createPixelMap(imgComponent.byteBuffer, {
  size:{height: height, width: stride}, srcPixelFormat: 8});
// Crop extra pixels.
pixelMap.cropSync({size:{width:width, height:height}, x:0, y:0});
