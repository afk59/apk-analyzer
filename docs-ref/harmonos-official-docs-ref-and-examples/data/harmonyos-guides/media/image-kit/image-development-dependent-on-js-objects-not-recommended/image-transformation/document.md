# Image Transformation

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/CzH5I_LiQf-NdQ9hJBD64g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062042Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B95D8AEC58451612DC0D40FF3193AD896D69910A9F78C7870928A15E7A2A36D4)

This guide uses the APIs provided by the [Image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image) module, which supports basic functionalities such as image encoding/decoding, image receiver operations, and image data processing. These APIs are introduced prior to API version 11, and no additional features will be included in later versions. Therefore, these APIs are not recommended.

You can also use the C APIs provided by the [Image\_NativeModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-nativemodule) module, which includes all the foundational features of the Image module while adding new capabilities like multi-image encoding/decoding. For details about the development guide, see [Using Image\_NativeModule to Decode Images (C/C++)](../../image-development-c-c/image-decoding/using-image-nativemodule-to-decode-images/document.md). These APIs are available since API version 12 and are expected to keep evolving. You are encouraged to use them.

You are not advised to use both sets of C APIs in your code. It may cause compatibility issues in some scenarios.

This topic describes how to use native image APIs to implement image transformation.

#### How to Develop

**Adding Dependencies**

Open the **src/main/cpp/CMakeLists.txt** file of the native project, add **libace\_napi.z.so** and **libpixelmap\_ndk.z.so** (on both of which the image APIs depend) and **libhilog\_ndk.z.so** (on which the log APIs depend) to the **target\_link\_libraries** dependency.

target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so libpixelmap\_ndk.z.so)

**Adding API Mappings**

Open the **src/main/cpp/hello.cpp** file and add the following API mappings to the **Init** function:

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {
        { "testGetImageInfo", nullptr, TestGetImageInfo, nullptr, nullptr, nullptr, napi\_default, nullptr },
        { "testAccessPixels", nullptr, TestAccessPixels, nullptr, nullptr, nullptr, napi\_default, nullptr },
        { "testUnAccessPixels", nullptr, TestUnAccessPixels, nullptr, nullptr, nullptr, napi\_default, nullptr },
    };

    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

**Calling the Native APIs**

For details about the APIs, see [Image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image).

Obtain the JS resource object from the **hello.cpp** file and convert it to a native resource object. Then you can call native APIs. The sample code is as follows:

Open **src/main/cpp/hello.cpp**, and add the reference file.

#include<multimedia/image\_framework/image\_pixel\_map\_napi.h>

1.  Obtain the **PixelMap** information and store the information to the OhosPixelMapInfo struct.
    
    static napi\_value TestGetImageInfo(napi\_env env, napi\_callback\_info info)
     {
         napi\_value result = nullptr;
         napi\_get\_undefined(env, &result);
    
         napi\_value thisVar = nullptr;
         napi\_value argValue\[1\] = {0};
         size\_t argCount = 1;
    
         napi\_get\_cb\_info(env, info, &argCount, argValue, &thisVar, nullptr);
         
         OHOS::Media::OhosPixelMapInfo pixelMapInfo;
         OHOS::Media::OH\_GetImageInfo(env, argValue\[0\], &pixelMapInfo);
         return result;
     }
    
2.  Obtain the memory address of a PixelMap object and lock the memory.
    
    static napi\_value TestAccessPixels(napi\_env env, napi\_callback\_info info)
    {
        napi\_value result = nullptr;
        napi\_get\_undefined(env, &result);
    
        napi\_value thisVar = nullptr;
        napi\_value argValue\[1\] = {0};
        size\_t argCount = 1;
    
        napi\_get\_cb\_info(env, info, &argCount, argValue, &thisVar, nullptr);
    
        void\* addrPtr = nullptr;
        OHOS::Media::OH\_AccessPixels(env, argValue\[0\], &addrPtr);
        return result;
    }
    
3.  Unlock the memory of the PixelMap object.
    
    static napi\_value TestUnAccessPixels(napi\_env env, napi\_callback\_info info)
    {
        napi\_value result = nullptr;
        napi\_get\_undefined(env, &result);
    
        napi\_value thisVar = nullptr;
        napi\_value argValue\[1\] = {0};
        size\_t argCount = 1;
    
        napi\_get\_cb\_info(env, info, &argCount, argValue, &thisVar, nullptr);
    
        OHOS::Media::OH\_UnAccessPixels(env, argValue\[0\]);
        return result;
    }
    

**Calling APIs on the JS Side**

1.  Open src\\main\\cpp\\types\*libentry\\index.d.ts\* (where **libentry** varies according to the project name), and import the following files:
    
    import { image } from '@kit.ImageKit';
    export const add:(a: number, b: number) => image.PixelMap;
    export const transform: (a: image.PixelMap) => image.PixelMap;
    export const testGetImageInfo: (a: image.PixelMap) => image.PixelMap;
    export const testAccessPixels: (a: image.PixelMap) => image.PixelMap;
    export const testUnAccessPixels: (a: image.PixelMap) => image.PixelMap;
    
2.  Open **src\\main\\ets\\pages\\index.ets**, import **libentry.so** (where **libentry** varies according to the project name), call the native APIs, and pass in the JS resource object. The sample code is as follows:
    
    import testNapi from 'libentry.so';
    import { image } from '@kit.ImageKit';
    
    @Entry
    @Component
    struct Index {
    @State message: string = 'IMAGE';
    @State \_PixelMap : image.PixelMap | undefined = undefined;
    
    build() {
        Row() {
        Column() {
            Button(this.message)
            .fontSize(50)
            .fontWeight(FontWeight.Bold)
            .onClick(() => {
                const color : ArrayBuffer = new ArrayBuffer(96);
                let opts: image.InitializationOptions = { alphaType: 0, editable: true, pixelFormat: 4, scaleMode: 1, size: { height: 4, width: 6 } };
                image.createPixelMap(color, opts)
                .then( (pixelmap : image.PixelMap) => {
                    this.\_PixelMap = pixelmap;
                    testNapi.testGetImageInfo(this.\_PixelMap);
                    console.info("Test GetImageInfo success");
    
                    testNapi.testAccessPixels(this.\_PixelMap);
                    console.info("Test AccessPixels success");
    
                    testNapi.testUnAccessPixels(this.\_PixelMap);
                    console.info("Test UnAccessPixels success");
                })
            })
        }
        .width('100%')
        }
        .height('100%')
    }
    }
