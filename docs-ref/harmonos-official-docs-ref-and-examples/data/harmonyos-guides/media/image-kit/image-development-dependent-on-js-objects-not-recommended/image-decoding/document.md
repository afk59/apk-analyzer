# Image Decoding

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/CaVxya_kTT-J4w6lBKdtTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062042Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45BE155F980270F78EA21AA510F94A61EF1C9E5C2AE517BD1FC685D83F1FD2AA)

This guide uses the APIs provided by the [Image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image) module, which supports basic functionalities such as image encoding/decoding, image receiver operations, and image data processing. These APIs are introduced prior to API version 11, and no additional features will be included in later versions. Therefore, these APIs are not recommended.

You can also use the C APIs provided by the [Image\_NativeModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-nativemodule) module, which includes all the foundational features of the Image module while adding new capabilities like multi-image encoding/decoding. For details about the development guide, see [Using Image\_NativeModule to Decode Images (C/C++)](../../image-development-c-c/image-decoding/using-image-nativemodule-to-decode-images/document.md). These APIs are available since API version 12 and are expected to keep evolving. You are encouraged to use them.

You are not advised to use both sets of C APIs in your code. It may cause compatibility issues in some scenarios.

Image decoding refers to the process of decoding an image in a supported format into a PixelMap for image display or [processing](../../image-development-arkts/image-editing-and-processing/using-pixelmap-to-transform-images/document.md). Currently, the following image formats are supported: JPEG, PNG, GIF, WebP, BMP, SVG, ICO, DNG, and HEIC (support may vary across different hardware devices).

#### How to Develop

For details about the APIs related to image decoding, see the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-source-mdk-h).

## Adding Dependencies

Open the **src/main/cpp/CMakeLists.txt** file of the native project, add **libace\_napi.z.so**, **libpixelmap\_ndk.z.so**, **libimage\_source\_ndk.z.so**, **librawfile.z.so**, and **libhilog\_ndk.z.so** (on which the native log APIs depend) to the **target\_link\_libraries** dependency.

target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so libpixelmap\_ndk.z.so libimage\_source\_ndk.z.so librawfile.z.so)

## Adding API Mappings

Open the **src/main/cpp/hello.cpp** file, and add the mapping of the **getSyncPixelMap** function to the **Init** function. The **getSyncPixelMap** function is used to generate a PixelMap in synchronous mode. The code is as follows:

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {
        { "getSyncPixelMap", nullptr, getSyncPixelMap, nullptr, nullptr, nullptr, napi\_default, nullptr },
    };

    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

## Calling APIs on the JS Side

1.  Open src\\main\\cpp\\types\*libentry\\index.d.ts\* (where **libentry** varies according to the project name), and import the following files:
    
    import { image } from '@kit.ImageKit';
    import { resourceManager } from '@kit.LocalizationKit';
    
    // Synchronous call. The input parameters are the resource manager and image resource name, and a PixelMap is returned.
    export const getSyncPixelMap: (resMgr: resourceManager.ResourceManager, src: string) => image.PixelMap;
    
2.  Prepare an image resource file, named **example.jpg** in this example, and import it to \*src\\main\\resources\\rawfile\*.
    
3.  Open **src\\main\\ets\\pages\\index.ets**, import **libentry.so** (where **libentry** varies according to the project name), call the native APIs, and pass the JS resource object. The following is an example:
    
    import testNapi from 'libentry.so';
    import { image } from '@kit.ImageKit';
    import { common } from '@kit.AbilityKit';
    @Entry
    @Component
    struct Index {
      @State pixelMap : PixelMap | undefined = undefined;
      aboutToAppear() {
         // Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
         let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
         // Call the custom getSyncPixelMap function to obtain a PixelMap.
         this.pixelMap = testNapi.getSyncPixelMap(context.resourceManager, "example.jpg");
      }
    
      build() {
         Row() {
            Column() {
            Image(this.pixelMap)
               .width(100)
               .height(100)
            }
            .width('100%')
         }
         .height('100%')
      }
    }
    

## Calling the Native APIs

For details about the APIs, see [Image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image).

Obtain the JS resource object from the **hello.cpp** file and convert it to a native resource object. Then you can call native APIs.

**Adding Reference Files**

// Include the image framework, raw file, raw file management, and log print header files.
#include <cstdlib>
#include <cstring>
#include <multimedia/image\_framework/image\_source\_mdk.h>
#include <multimedia/image\_framework/image\_pixel\_map\_mdk.h>
#include <rawfile/raw\_file.h>
#include <rawfile/raw\_file\_manager.h>
#include <hilog/log.h>

static napi\_value getSyncPixelMap(napi\_env env, napi\_callback\_info info)
{
   size\_t argc = 2;
   napi\_value args\[2\] = {nullptr};

   napi\_get\_cb\_info(env, info, &argc, args , nullptr, nullptr);
   
   napi\_valuetype srcType;
   napi\_typeof(env, args\[0\], &srcType);

   // The input parameter args\[0\] indicates the resource manager, which is used to initialize the resource manager at the native layer.
   NativeResourceManager \*mNativeResMgr = OH\_ResourceManager\_InitNativeResourceManager(env, args\[0\]);
   
   size\_t strSize;
   char srcBuf\[2048\];
   // The input parameter args\[1\] indicates the file name.
   napi\_get\_value\_string\_utf8(env, args\[1\], srcBuf, sizeof(srcBuf), &strSize);

   // Use the resource manager to open the raw file.
   RawFile \* rawFile = OH\_ResourceManager\_OpenRawFile(mNativeResMgr, srcBuf);
   if (rawFile != NULL) {
      // Obtain the file size and read data.
      long len = OH\_ResourceManager\_GetRawFileSize(rawFile);
      uint8\_t \* data = static\_cast<uint8\_t \*>(malloc(len));
      int res = OH\_ResourceManager\_ReadRawFile(rawFile, data, len);

      OhosImageSource imageSource\_c;
      imageSource\_c.buffer = data;
      imageSource\_c.bufferSize = len;

      OhosImageSourceOps ops{};
      napi\_value imageSource;
      napi\_value pixelMap;

      // Create an ImageSource object using the read raw data.
      int32\_t ret = OH\_ImageSource\_Create(env, &imageSource\_c, &ops, &imageSource);

      // Initialize the ImageSource object at the native layer.
      ImageSourceNative \* imageSourceNative\_c = OH\_ImageSource\_InitNative(env, imageSource);
      OhosImageDecodingOps decodingOps{};
      // Create a PixelMap.
      OH\_ImageSource\_CreatePixelMap(imageSourceNative\_c, &decodingOps, &pixelMap);

      // The following APIs are used for the GIF format.
      // napi\_value pixelMapList;
      // OH\_ImageSource\_CreatePixelMapList(imageSourceNative\_c, &decodingOps, &pixelMapList);
      // OhosImageSourceDelayTimeList list{};
      // OH\_ImageSource\_GetDelayTime(imageSourceNative\_c, &list);
      // uint32\_t count;
      // OH\_ImageSource\_GetFrameCount(imageSourceNative\_c, &count);

      OhosImageSourceInfo info{};
      // Read the image width and height.
      OH\_ImageSource\_GetImageInfo(imageSourceNative\_c, 0, &info);
      OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00, "\[decode\]", "imageInfo width:%{public}d , height:%{public}d", info.size.width, info.size.height);
      
      // Read the ImageWidth configuration of the image source and print logs.
      OhosImageSourceProperty target;
      char exifKey\_c\[\] = "ImageWidth";
      target.size = strlen(exifKey\_c);
      target.value = exifKey\_c;

      OhosImageSourceProperty response{};
      response.size = 20;
      response.value = static\_cast<char \*>(malloc(20));
      OH\_ImageSource\_GetImageProperty(imageSourceNative\_c, &target, &response);
      OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00, "\[decode\]", "ImageProperty width after modify:%{public}s", response.value);

      // After the processing is complete, release resources at the native layer.
      OH\_ImageSource\_Release(imageSourceNative\_c);
      OH\_ResourceManager\_CloseRawFile(rawFile);
      return pixelMap;
   }
   OH\_ResourceManager\_ReleaseNativeResourceManager(mNativeResMgr);
   return nullptr;
}

The image framework supports incremental decoding. The method is as follows:

// Include the image framework, raw file, raw file management, and log print header files.
#include <cstdlib>
#include <cstring>
#include <multimedia/image\_framework/image\_source\_mdk.h>
#include <multimedia/image\_framework/image\_pixel\_map\_mdk.h>
#include <rawfile/raw\_file.h>
#include <rawfile/raw\_file\_manager.h>
#include <hilog/log.h>

static napi\_value getSyncPixelMap(napi\_env env, napi\_callback\_info info)
{
   size\_t argc = 2;
   napi\_value args\[2\] = {nullptr};

   napi\_get\_cb\_info(env, info, &argc, args , nullptr, nullptr);
   
   napi\_valuetype srcType;
   napi\_typeof(env, args\[0\], &srcType);

   // The input parameter args\[0\] indicates the resource manager, which is used to initialize the resource manager at the native layer.
   NativeResourceManager \* mNativeResMgr = OH\_ResourceManager\_InitNativeResourceManager(env, args\[0\]);
   
   size\_t strSize;
   char srcBuf\[2048\];
   // The input parameter args\[1\] indicates the file name.
   napi\_get\_value\_string\_utf8(env, args\[1\], srcBuf, sizeof(srcBuf), &strSize);

   // Use the resource manager to open the raw file.
   RawFile \* rawFile = OH\_ResourceManager\_OpenRawFile(mNativeResMgr, srcBuf);
   if (rawFile != NULL) {
      // Obtain the file size. If the file size is greater than 2048 bytes, incremental decoding is performed. Otherwise, full decoding is performed.
      long len = OH\_ResourceManager\_GetRawFileSize(rawFile);
      if (len > 2048) {
         uint8\_t \* data = static\_cast<uint8\_t \*>(malloc(len));
         // Read all data in the file.
         int res = OH\_ResourceManager\_ReadRawFile(rawFile, data, len);
         
         uint8\_t \* holderdata = static\_cast<uint8\_t \*>(malloc(len));

         OhosImageSource imageSource\_c;
         // A buffer of imageSource\_c is allocated, but no data is filled in.
         imageSource\_c.buffer = holderdata;
         imageSource\_c.bufferSize = len;
         OhosImageSourceOps ops{};
         napi\_value imageSource;
         // Initialize the incremental ImageSource object.
         OH\_ImageSource\_CreateIncremental(env, &imageSource\_c, &ops, &imageSource);

         // Initialize the ImageSource object at the native layer.
         ImageSourceNative \* imageSourceNative\_c = OH\_ImageSource\_InitNative(env, imageSource);

         // The following simulates segment loading. Segments are loaded twice. 2048 bytes of data are loaded for the first time, and the remaining data is loaded for the second time.
         OhosImageSourceUpdateData firstData{};
         firstData.buffer = data; // Image data.
         firstData.bufferSize = len; // Total size of the image data.
         firstData.isCompleted = false;
         firstData.offset = 0; // The first loading starts from the very beginning.
         firstData.updateLength = 2048; // 2048 bytes are loaded for the first time.
         OH\_ImageSource\_UpdateData(imageSourceNative\_c, &firstData);

         OhosImageSourceUpdateData secondData{};
         secondData.buffer = data;
         secondData.bufferSize = len;
         secondData.isCompleted = true; // Last loading, to indicating that loading is complete.
         secondData.offset = 2048; // 2048 bytes of data have been loaded. Offset the data to load for the second time.
         secondData.updateLength = len - 2048; // Load the remaining data for the second time.
         OH\_ImageSource\_UpdateData(imageSourceNative\_c, &secondData);

         napi\_value pixelMap;
         OhosImageDecodingOps decodingOps{};
         decodingOps.index = 0;
         // Create a PixelMap.
         OH\_ImageSource\_CreatePixelMap(imageSourceNative\_c, &decodingOps, &pixelMap);

         // After the processing is complete, release resources at the native layer.
         OH\_ImageSource\_Release(imageSourceNative\_c);
         OH\_ResourceManager\_CloseRawFile(rawFile);
         return pixelMap;
      }
      // Read all data in the raw file.
      uint8\_t \* data = static\_cast<uint8\_t \*>(malloc(len));
      int res = OH\_ResourceManager\_ReadRawFile(rawFile, data, len);

      OhosImageSource imageSource\_c;
      imageSource\_c.buffer = data;
      imageSource\_c.bufferSize = len;

      OhosImageSourceOps ops{};
      napi\_value imageSource;
      napi\_value pixelMap;

      // Create an ImageSource object using the read raw data.
      int32\_t ret = OH\_ImageSource\_Create(env, &imageSource\_c, &ops, &imageSource);

      // Initialize the ImageSource object at the native layer.
      ImageSourceNative \* imageSourceNative\_c = OH\_ImageSource\_InitNative(env, imageSource);
      OhosImageDecodingOps decodingOps{};

      // Create a PixelMap.
      OH\_ImageSource\_CreatePixelMap(imageSourceNative\_c, &decodingOps, &pixelMap);

      // After the processing is complete, release resources at the native layer.
      OH\_ImageSource\_Release(imageSourceNative\_c);
      OH\_ResourceManager\_CloseRawFile(rawFile);
      return pixelMap;
   }
   OH\_ResourceManager\_ReleaseNativeResourceManager(mNativeResMgr);
   return nullptr;
}
