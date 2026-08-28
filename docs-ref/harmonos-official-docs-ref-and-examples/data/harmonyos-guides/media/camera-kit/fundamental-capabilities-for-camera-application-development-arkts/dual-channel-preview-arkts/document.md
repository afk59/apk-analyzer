# Dual-Channel Preview (ArkTS)

Before developing a camera application, you must [request required permissions](../../requesting-camera-development-permissions/document.md).

Dual-channel preview means that an application can use two preview streams at the same time. One preview stream is used for display on the screen, and the other is used for other operations such as image processing, so as to improve the processing efficiency.

The camera application controls the camera device to implement basic operations such as image display (preview), photo saving (photo capture), and video recording. The camera development model is the Surface model, in which the application transfers data through Surface. It obtains the photo capture stream data through the Surface of [ImageReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagereceiver), and the preview stream data through the Surface of **XComponent**.

To implement dual preview, you can refer to [Photo Capture](../photo-capture-arkts/document.md) first. In dual preview, replace the photo capture stream with another preview stream, create another **previewOutput** through the Surface of [ImageReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagereceiver), and the rest of the process is the same as photo capture.

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera) for the API reference.

#### Constraints

-   Currently, streams cannot be dynamically added. In other words, you cannot call [addOutput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session#addoutput11) to add streams without calling [session.stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session#stop11) first.
-   After an ImageReceiver object processes image data obtained, it must release the image buffer so that the buffer queue of the surface properly rotates.

#### API Calling Process

The figure below shows the recommended API calling process of the dual-channel preview solution.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/II91fXTeRiCh-TlHcbCxhQ/en-us_image_0000002537925112.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=212D2E42EE72A4D48C85ACA9BB6482C0924D55E6004EA58FD9C91C3778FF3550)

#### How to Develop

-   For the first preview stream used for image processing, create an ImageReceiver object, obtain the surface ID to create the first preview stream, register an image listener, and process each frame of image data in the preview stream as required.
-   For the second preview stream used for image display, create an **XComponent**, obtain the surface ID to create the second preview stream, and render the preview stream data in the component.
-   To enable both preview streams to obtain data, configure a camera session for both preview streams, and start the session.

The examples in each of the following steps are code snippets. You can click the link at the bottom right of the sample code to obtain the complete sample codes.

## First Preview Stream Used for Image Processing

1.  Import dependencies, including dependencies related to image and camera framework.
    
    import { image } from '@kit.ImageKit';
    import { camera } from '@kit.CameraKit';
    import { display } from '@kit.ArkUI';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Obtain the surface ID for the first preview stream. Specifically, create an ImageReceiver object, and obtain the surface ID through the object.
    
    async init(size: Size, format = image.ImageFormat.JPEG, capacity = 8) {
      const receiver = image.createImageReceiver(size, format, capacity);
      const surfaceId = await receiver.getReceivingSurfaceId();
      this.onImageArrival(receiver);
      return surfaceId;
    }
    
3.  Obtain the image or PixelMap formats of the preview stream received by ImageReceiver. For details about the image format, see the **format** parameter in [Image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-image). For details about the [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) format, see [PixelMapFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-e#pixelmapformat7).
    
    // Mappings between image formats and PixelMap formats.
    let formatToPixelMapFormatMap = new Map<number, image.PixelMapFormat>(\[
      \[12, image.PixelMapFormat.RGBA\_8888\],
      \[25, image.PixelMapFormat.NV21\],
      \[35, image.PixelMapFormat.YCBCR\_P010\],
      \[36, image.PixelMapFormat.YCRCB\_P010\]
    \]);
    // Mapping of the size of a single pixel for each PixelMapFormat.
    let pixelMapFormatToSizeMap = new Map<image.PixelMapFormat, number>(\[
      \[image.PixelMapFormat.RGBA\_8888, 4\],
      \[image.PixelMapFormat.NV21, 1.5\],
      \[image.PixelMapFormat.YCBCR\_P010, 3\],
      \[image.PixelMapFormat.YCRCB\_P010, 3\]
    \]);
    
4.  Register a listener to process each frame of image data in the preview stream. Specifically, use the **imageArrival** event in the ImageReceiver object to obtain the image data returned by the bottom layer. For details, see [Image API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagereceiver).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/vbloAdB_RNOz4BLLGhQ_Kg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDAD09945BC5C425DAAE36143BBA5E127B2E29981E730573061FC8F429E553D5)
    
    -   When you create a [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) instance using the [createPixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-f#imagecreatepixelmap8) API, the properties such as **Size** and **srcPixelFormat** must match **Size** and **Format** configured in preview output stream's preview profile. For details about the image pixel format of ImageReceiver, see [PixelMapFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-e#pixelmapformat7). For details about the output format the preview profile, see [CameraFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-e#cameraformat).
    -   Due to the variability across different devices, you must obtain the preview profiles supported by the current device by calling [getSupportedOutputCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#getsupportedoutputcapability11) before creating a preview output stream. Then based on actual service requirements, select a suitable preview profile that meets the required [CameraFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-e#cameraformat) and [Size](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-i#size).
    -   The actual format of the preview stream image data received by ImageReceiver is determined by the **format** parameter in the preview profile that you select based on service requirements when creating the preview output stream. For details, see [Enabling a Preview Stream to Obtain Data](#enabling-a-preview-stream-to-obtain-data).
    
    onImageArrival(receiver: image.ImageReceiver): void {
      receiver.on('imageArrival', () => {
        Logger.info(TAG, 'image arrival');
        receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
          if (err || nextImage === undefined) {
            Logger.error(TAG, 'readNextImage failed');
            return;
          }
          nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError, imgComponent: image.Component) => {
            if (err || imgComponent === undefined) {
              Logger.error(TAG, 'getComponent failed');
            }
            if (imgComponent.byteBuffer) {
              // ...
            } else {
              Logger.error(TAG, 'byteBuffer is null');
            }
            // ...
          });
        });
      });
    }
    
    The following methods are available for parsing the image buffer data by using [image.Component](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-i#component9).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/S0EhgYW5SMe6PNCLMJEAkQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=215D62B3603D836FD9F48B1AAE7DB20B742FF012E54D0C08AEB3D746E173981C)
    
    Check whether the width of the image is the same as **rowStride**. If they are different, perform the following operations.
    
    Method 1: Remove the stride data from **imgComponent.byteBuffer**, obtain a new buffer by means of copy, and process the buffer by calling the API that does not support stride.
    
    async getPixelMap(imgComponent: image.Component, width: number, height: number, stride: number) {
      if (stride === width) {
        return await image.createPixelMap(imgComponent.byteBuffer, {
          size: { height: height, width: width },
          srcPixelFormat: image.PixelMapFormat.NV21,
        });
      }
      const dstBufferSize = width \* height \* 1.5;
      const dstArr = new Uint8Array(dstBufferSize);
      for (let j = 0; j < height \* 1.5; j++) {
        const srcBuf = new Uint8Array(imgComponent.byteBuffer, j \* stride, width);
        dstArr.set(srcBuf, j \* width);
      }
      return await image.createPixelMap(dstArr.buffer, {
        size: { height: height, width: width },
        srcPixelFormat: image.PixelMapFormat.NV21,
      });
    }
    
    Method 2: Create a PixelMap based on the value of stride \* height, and call **cropSync** of the PixelMap to crop redundant pixels.
    
    // Create a PixelMap, with width set to the value of stride.
    let pixelMap = await image.createPixelMap(imgComponent.byteBuffer, {
      size:{height: height, width: stride}, srcPixelFormat: pixelMapFormat});
    // Crop extra pixels.
    pixelMap.cropSync({size:{width:width, height:height}, x:0, y:0});
    
    Method 3: Pass **imgComponent.byteBuffer** and **stride** to the API that supports stride.
    

## Second Preview Stream Used for Image Display

To obtain the surface ID of the second preview stream, you must first create an **XComponent** for displaying the preview stream. For details about how to obtain the surface ID, see [getXComponentSurfaceId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent#getxcomponentsurfaceid9). The **XComponent** capability is provided by the UI. For details, see [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent).

XComponent({
  type: XComponentType.SURFACE,
  controller: this.previewVM.xComponentController
})
  .size({ height: '100%', width: '100%' })
  .onLoad(async () => {
    // ...
    this.previewVM.surfaceId = this.previewVM.xComponentController.getXComponentSurfaceId();
    this.previewVM.setPreviewSize();
    this.previewVM.xComponentController.setXComponentSurfaceRotation({ lock: true });
    // ...
  })

## Enabling a Preview Stream to Obtain Data

Create two preview outputs with two surface IDs, add the outputs to a camera session, and start the camera session to obtain the preview stream data.

async createOutput(config: CreateOutputConfig) {
  const cameraOutputCap = config.cameraManager.getSupportedOutputCapability(config.device, config.sceneMode);
  const displayRatio = config.profile.size.width / config.profile.size.height;
  const profileWidth = config.profile.size.width;
  const previewProfile = cameraOutputCap.previewProfiles
    .sort((a, b) => Math.abs(a.size.width - profileWidth) - Math.abs(b.size.width - profileWidth))
    .find(pf => {
      const pfDisplayRatio = pf.size.width / pf.size.height;
      return pf.format === config.profile.format &&
        Math.abs(pfDisplayRatio - displayRatio) <= CameraConstant.PROFILE\_DIFFERENCE;
    });
  if (!previewProfile) {
    Logger.error(TAG\_LOG, 'Failed to get preview profile');
    return;
  }
  this.output = config.cameraManager.createPreviewOutput(previewProfile, config.surfaceId);
  this.addOutputListener(this.output);
  return this.output;
}

#### Complete Sample Code

import { image } from '@kit.ImageKit';
import { camera } from '@kit.CameraKit';
import { display } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { Logger } from 'commons';
import OutputManager, { CreateOutputConfig } from './OutputManager';
import CameraConstant from '../constants/CameraConstants';

const TAG = 'ImageReceiverManager';

export class ImageReceiverManager implements OutputManager {
  public output?: camera.PreviewOutput;
  public isActive: boolean = true;
  public callback: (px: PixelMap) => void;
  private position: camera.CameraPosition = camera.CameraPosition.CAMERA\_POSITION\_BACK;

  constructor(cb: (px: PixelMap) => void) {
    this.callback = cb;
  }

  async createOutput(config: CreateOutputConfig) {
    const cameraOutputCap = config.cameraManager.getSupportedOutputCapability(config.device, config.sceneMode);
    const displayRatio = config.profile.size.width / config.profile.size.height;
    const profileWidth = config.profile.size.width;
    const previewProfile = cameraOutputCap.previewProfiles
      .sort((a, b) => Math.abs(a.size.width - profileWidth) - Math.abs(b.size.width - profileWidth))
      .find(pf => {
        const pfDisplayRatio = pf.size.width / pf.size.height;
        return pf.format === config.profile.format &&
          Math.abs(pfDisplayRatio - displayRatio) <= CameraConstant.PROFILE\_DIFFERENCE;
      });
    if (!previewProfile) {
      Logger.error(TAG, 'Failed to get preview profile');
      return;
    }
    const surfaceId = await this.init(config.profile.size);
    this.output = config.cameraManager.createPreviewOutput(previewProfile, surfaceId);
    this.position = config.device.cameraPosition;
    return this.output;
  }

  async release() {
    await this.output?.release();
    this.output = undefined;
  }

  async init(size: Size, format = image.ImageFormat.JPEG, capacity = 8) {
    const receiver = image.createImageReceiver(size, format, capacity);
    const surfaceId = await receiver.getReceivingSurfaceId();
    this.onImageArrival(receiver);
    return surfaceId;
  }

  async getPixelMap(imgComponent: image.Component, width: number, height: number, stride: number) {
    if (stride === width) {
      return await image.createPixelMap(imgComponent.byteBuffer, {
        size: { height: height, width: width },
        srcPixelFormat: image.PixelMapFormat.NV21,
      });
    }
    const dstBufferSize = width \* height \* 1.5;
    const dstArr = new Uint8Array(dstBufferSize);
    for (let j = 0; j < height \* 1.5; j++) {
      const srcBuf = new Uint8Array(imgComponent.byteBuffer, j \* stride, width);
      dstArr.set(srcBuf, j \* width);
    }
    return await image.createPixelMap(dstArr.buffer, {
      size: { height: height, width: width },
      srcPixelFormat: image.PixelMapFormat.NV21,
    });
  }

  onImageArrival(receiver: image.ImageReceiver): void {
    receiver.on('imageArrival', () => {
      Logger.info(TAG, 'image arrival');
      receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
        if (err || nextImage === undefined) {
          Logger.error(TAG, 'readNextImage failed');
          return;
        }
        nextImage.getComponent(image.ComponentType.JPEG, async (err: BusinessError, imgComponent: image.Component) => {
          if (err || imgComponent === undefined) {
            Logger.error(TAG, 'getComponent failed');
          }
          if (imgComponent.byteBuffer) {
            const width = nextImage.size.width;
            const height = nextImage.size.height;
            const stride = imgComponent.rowStride;
            Logger.info(TAG, \`getComponent with width:${width} height:${height} stride:${stride}\`);
            const pixelMap = await this.getPixelMap(imgComponent, width, height, stride);
            const displayRotation = display.getDefaultDisplaySync().rotation \* camera.ImageRotation.ROTATION\_90;
            const rotation = this.output!.getPreviewRotation(displayRotation);
            if (this.position === camera.CameraPosition.CAMERA\_POSITION\_FRONT) {
              if (displayRotation === 90 || displayRotation === 270) {
                await pixelMap.rotate((rotation + 180) % 360);
              } else {
                await pixelMap.rotate(rotation);
              }
              await pixelMap.flip(true, false);
            } else {
              await pixelMap.rotate(rotation);
            }
            this.callback(pixelMap);
          } else {
            Logger.error(TAG, 'byteBuffer is null');
          }
          nextImage.release().then(() => {Logger.info(TAG, 'image release done');}).catch((error: BusinessError) => {
            Logger.error(TAG, \`Release failed! Code ${error.code},message is ${error.message}\`);
          });
          Logger.info(TAG, 'image process done');
        });
      });
    });
  }
}
