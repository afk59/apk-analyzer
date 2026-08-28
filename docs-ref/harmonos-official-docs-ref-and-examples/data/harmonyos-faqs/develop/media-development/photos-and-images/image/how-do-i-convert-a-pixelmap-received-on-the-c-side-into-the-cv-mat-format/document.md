# How do I convert a PixelMap received on the C++ side into the cv::Mat format?

**Solution**

You can use either of the following methods to convert a PixelMap into cv::Mat:

-   Convert the ArrayBuffer of the PixelMap into cv::Mat.
-   Use **OH\_PixelMap\_AccessPixels** to obtain the memory address of the PixelMap and convert the data in the memory address into cv::Mat.

In both methods, ensure that the format of the PixelMap is the same as that of Mat in OpenCV. Otherwise, color deviation occurs.

Refer to the code snippet below.

Parameters passed by ArkTS:

import cPixelMapToMat from 'libcpixelmaptomat.so';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct Index {
  @State pixelMap: image.PixelMap | undefined = undefined

  async arrayBufferToMat() {
    if (this.pixelMap == undefined || this.pixelMap){
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let resourceManager = context.resourceManager
      let imageArray = await resourceManager.getMediaContent($r('app.media.sample10'));
      let pixelBuffer = new Uint8Array(imageArray).buffer as Object as ArrayBuffer
      console.info("pixelBuffer length: " + pixelBuffer.byteLength);
      let imageResource = image.createImageSource(pixelBuffer);
      let opts: image.DecodingOptions = {
        editable: true,
        desiredPixelFormat: image.PixelMapFormat.RGBA\_8888
      }
      this.pixelMap = await imageResource.createPixelMap(opts);
    }

    const readBuffer: ArrayBuffer = new ArrayBuffer(this.pixelMap.getPixelBytesNumber()); // Obtain the array buffer of the pixelmap
    console.info("readBuffer length: " + readBuffer.byteLength);
    this.pixelMap.readPixelsToBuffer(readBuffer).then(() => {
      console.info("No Error!")
    }).catch((err: BusinessError) => {
      console.error("Error! " + err.message)
    })
    const dir = getContext(this).filesDir;
    console.info('save path: ' + dir);
    cPixelMapToMat.arrayBufferToMat(this.pixelMap, readBuffer, dir);
  }

  async accessToMat(){
    if (this.pixelMap == undefined || this.pixelMap) {
      let resourceManager = getContext(this).resourceManager
      let imageArray = await resourceManager.getMediaContent($r('app.media.sample14'));
      let pixelBuffer = new Uint8Array(imageArray).buffer as Object as ArrayBuffer
      console.info("pixelBuffer length: " + pixelBuffer.byteLength);
      let imageResource = image.createImageSource(pixelBuffer);
      let opts: image.DecodingOptions = {
        editable: true,
        desiredPixelFormat: image.PixelMapFormat.RGBA\_8888
      }
      this.pixelMap = await imageResource.createPixelMap(opts);
    }

    const dir = getContext(this).filesDir;
    console.info('save path: ' + dir);
    cPixelMapToMat.accessToMat(this.pixelMap, dir);
  }

  build() {
    Row() {
      Column() {
        Image(this.pixelMap)
          .width(200)
          .height(200)
        Button('ArrayBufferToMat')
          .onClick(() => {
            this.arrayBufferToMat();
          })

        Button('AccessToMat')
          .onClick(() => {
            this.accessToMat();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

Solution 1: Converting an ArrayBuffer into cv::Mat:

#include "napi/native\_api.h"
#include <multimedia/image\_framework/image\_mdk.h>
#include <multimedia/image\_framework/image\_mdk\_common.h>
#include <multimedia/image\_framework/image\_pixel\_map\_mdk.h>
#include <multimedia/image\_framework/image\_pixel\_map\_napi.h>
#include "hilog/log.h"
#include <opencv2/opencv.hpp>
#include <bits/alltypes.h>

static napi\_value ArrayBufferToMat(napi\_env env, napi\_callback\_info info) {
    size\_t argc = 3;
    napi\_value args\[3\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

    napi\_value error;
    napi\_create\_int32(env, -1, &error);

    // Initialize PixelMap object data 
    NativePixelMap \*native = OH\_PixelMap\_InitNativePixelMap(env, args\[0\]);
    if (native == nullptr) {
        return error;
    }
    // Obtaining Image Information
    struct OhosPixelMapInfos pixelMapInfos;
    if (OH\_PixelMap\_GetImageInfo(native, &pixelMapInfos) != IMAGE\_RESULT\_SUCCESS) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0xFF00, "Test", "Pure : -1");
        return error;
    }
    // Obtains the buffer
    napi\_value buffer = args\[1\];
    napi\_valuetype valueType;
    napi\_typeof(env, buffer, &valueType);
    if (valueType == napi\_object) {
        bool isArrayBuffer = false;
        napi\_is\_arraybuffer(env, buffer, &isArrayBuffer);
        if (!isArrayBuffer) {
            napi\_throw\_error(env, "EINVAL", "Error");
        }
    }

    void \*data = nullptr;
    size\_t byteLength = 0;
    napi\_get\_arraybuffer\_info(env, buffer, &data, &byteLength);
    int32\_t \*saveBuffer = (int32\_t \*)(data);

    // Convert to Mat
    cv::Mat originMat(pixelMapInfos.height, pixelMapInfos.width, CV\_8UC4, saveBuffer);
    if (!originMat.data) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0xFF00, "Read Image", "Pure : -1");
        return error;
    }

    // openCV defaults to BGRA or BGR. If the pixelmap is not created in one of these formats, a format conversion is required
    cv::Mat saveMat;
    cv::cvtColor(originMat, saveMat, cv::COLOR\_BGRA2RGBA);
    char pathArray\[1024\];
    size\_t length;
    napi\_get\_value\_string\_utf8(env, args\[2\], pathArray, 1024, &length);
    std::string path(pathArray);
    path += "/buffer.jpg";
    if (!cv::imwrite(path, saveMat)) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0xFF00, "Write Image", "Pure : -1");
        return error;
    }

    napi\_value res;
    napi\_create\_int32(env, 1, &res);
    return res;
}

Solution 2: Converting the data in the PixelMap memory address, which is obtained by calling **OH\_PixelMap\_AccessPixels**, into cv::Mat:

static napi\_value AccessToMat(napi\_env env, napi\_callback\_info info) {
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

    napi\_value error;
    napi\_create\_int32(env, -1, &error);

    NativePixelMap \*native = OH\_PixelMap\_InitNativePixelMap(env, args\[0\]);
    if (native == nullptr) {
        return error;
    }
    struct OhosPixelMapInfos pixelMapInfos;
    if (OH\_PixelMap\_GetImageInfo(native, &pixelMapInfos) != IMAGE\_RESULT\_SUCCESS) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0xFF00, "Test", "Pure : -1");
        return error;
    }

    void \*pixel;
    // Obtain the memory address of the NativePixelMap object and lock the memory
    OH\_PixelMap\_AccessPixels(native, &pixel);

    // Convert to Mat, pay attention to alignment, so rowSize needs to be passed in
    cv::Mat originMat(pixelMapInfos.height, pixelMapInfos.width, CV\_8UC4, pixel, pixelMapInfos.rowSize);
    if (!originMat.data) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0xFF00, "Read Image", "Pure : -1");
        return error;
    }

    // openCV defaults to BGRA or BGR. If the pixelmap is not created in one of these formats, a format conversion is required
    cv::Mat saveMat;
    cv::cvtColor(originMat, saveMat, cv::COLOR\_BGRA2RGBA);
    char pathArray\[1024\];
    size\_t length;
    napi\_get\_value\_string\_utf8(env, args\[1\], pathArray, 1024, &length);
    std::string path(pathArray);
    path += "/access.jpg";
    if (!cv::imwrite(path, saveMat)) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0xFF00, "Write Image", "Pure : -1");
        return error;
    }

    napi\_value res;
    napi\_create\_int32(env, 1, &res);
    return res;
}

In HarmonyOS development, the memory size needs to be specified for images that support hardware decoding. **OH\_PixelMap\_AccessPixels()** obtains the memory address of the image and locks the memory. However, the actual image size needs to be aligned with **lineStride**. Therefore, when constructing a Mat object, you must specify **lineStride**, that is, **rowSize**, for alignment. You can call **OH\_GetImageInfo** to obtain the image information, including the width, height, and row size.
