# PixelMap Operation

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/-6MPKN9_S4CKi5CZOoP35g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062042Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C81DB8C6DBFE073FDB6107A13AC0A75C1B5698C33EAF6BCBB790F2FAF83A6D11)

This guide uses the APIs provided by the [Image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image) module, which supports basic functionalities such as image encoding/decoding, image receiver operations, and image data processing. These APIs are introduced prior to API version 11, and no additional features will be included in later versions. Therefore, these APIs are not recommended.

You can also use the C APIs provided by the [Image\_NativeModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-nativemodule) module, which includes all the foundational features of the Image module while adding new capabilities like multi-image encoding/decoding. For details about the development guide, see [Using Image\_NativeModule to Decode Images (C/C++)](../../image-development-c-c/image-decoding/using-image-nativemodule-to-decode-images/document.md). These APIs are available since API version 12 and are expected to keep evolving. You are encouraged to use them.

You are not advised to use both sets of C APIs in your code. It may cause compatibility issues in some scenarios.

This topic describes how to use native image APIs to perform PixelMap operations.

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
        { "createPixelMapTest", nullptr, CreatePixelMapTest, nullptr, nullptr, nullptr, napi\_default, nullptr },
        { "createAlphaPixelMap", nullptr, CreateAlphaPixelMap, nullptr, nullptr, nullptr, napi\_default, nullptr },
        { "transform", nullptr, Transform, nullptr, nullptr, nullptr, napi\_default, nullptr },
    };

    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

**Calling the Native APIs**

For details about the APIs, see [Image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image).

Obtain the JS resource object from the **hello.cpp** file and convert it to a native resource object. Then you can call native APIs.

**Adding Reference Files**

#include <multimedia/image\_framework/image\_mdk\_common.h>
#include <multimedia/image\_framework/image\_pixel\_map\_mdk.h>
#include <stdlib.h>

1.  Create a PixelMap object.
    
    napi\_value CreatePixelMapTest(napi\_env env, napi\_callback\_info info) {
        napi\_value udfVar = nullptr;
        napi\_value pixelMap = nullptr;
    
        struct OhosPixelMapCreateOps createOps;
        createOps.width = 4;
        createOps.height = 6;
        createOps.pixelFormat = 4;
        createOps.alphaType = 0;
        size\_t bufferSize = createOps.width \* createOps.height \* 4;
        void \*buff = malloc(bufferSize);
        if (buff == nullptr) {
            return udfVar;
        }
    
        char \*cc = (char \*)buff;
        for (int i = 0; i < 96; i++) {
            \*(cc++) = (char)i;
        }
        int32\_t res = OH\_PixelMap\_CreatePixelMap(env, createOps, (uint8\_t \*)buff, bufferSize, &pixelMap);
        free(buff);
        if (res != IMAGE\_RESULT\_SUCCESS || pixelMap == nullptr) {
            return udfVar;
        }
        return pixelMap;
    }
    
2.  Create a PixelMap object that contains only alpha channel information.
    
    napi\_value CreateAlphaPixelMap(napi\_env env, napi\_callback\_info info) {
        napi\_value udfVar = nullptr;
        napi\_value thisVar = nullptr;
        napi\_value argValue\[1\] = {0};
        size\_t argCount = 1;
    
        napi\_value alphaPixelMap = nullptr;
    
        napi\_get\_undefined(env, &udfVar);
    
        if (napi\_get\_cb\_info(env, info, &argCount, argValue, &thisVar, nullptr) != napi\_ok || argCount < 1 ||
            argValue\[0\] == nullptr) {
            return udfVar;
        }
        int32\_t res = OH\_PixelMap\_CreateAlphaPixelMap(env, argValue\[0\], &alphaPixelMap);
        if (res != IMAGE\_RESULT\_SUCCESS || alphaPixelMap == nullptr) {
            return udfVar;
        }
        return alphaPixelMap;
    }
    
3.  Process the PixelMap object.
    
    napi\_value Transform(napi\_env env, napi\_callback\_info info) {
        napi\_value thisVar = nullptr;
        napi\_value argValue\[1\] = {0};
        size\_t argCount = 1;
    
        if (napi\_get\_cb\_info(env, info, &argCount, argValue, &thisVar, nullptr) != napi\_ok || argCount < 1 ||
            argValue\[0\] == nullptr) {
            return nullptr;
        }
        napi\_value result = nullptr;
        napi\_get\_undefined(env, &result);
        
        // Initialize a NativePixelMap object.
        NativePixelMap \*native = OH\_PixelMap\_InitNativePixelMap(env, argValue\[0\]);
        if (native == nullptr) {
            return result;
        }
    
        // Obtain image information.
        struct OhosPixelMapInfos pixelMapInfo;
        OH\_PixelMap\_GetImageInfo(native, &pixelMapInfo);
    
        // Obtain the number of bytes per row of the PixelMap object.
        int32\_t rowBytes;
        OH\_PixelMap\_GetBytesNumberPerRow(native, &rowBytes);
    
        // Check whether the PixelMap object is editable.
        int32\_t editable = 0;
        OH\_PixelMap\_GetIsEditable(native, &editable);
    
        // Check whether the PixelMap object supports alpha channels.
        int32\_t supportAlpha = 0;
        OH\_PixelMap\_IsSupportAlpha(native, &supportAlpha);
    
        // Set an alpha channel for the PixelMap object.
        int32\_t alphaAble = 0;
        OH\_PixelMap\_SetAlphaAble(native, alphaAble);
    
        // Obtain the pixel density of the PixelMap object.
        int32\_t densityG;
        OH\_PixelMap\_GetDensity(native, &densityG);
    
        // Set the pixel density for the PixelMap object.
        int32\_t densityS = 100;
        OH\_PixelMap\_SetDensity(native, densityS);
    
        // Set the opacity for the PixelMap object.
        float opacity = 0.5;
        OH\_PixelMap\_SetOpacity(native, opacity);
    
        // Scale the image.
        // scaleX: The width of the image after scaling is 0.5 of the original width.
        // scaleY: The height of the image after scaling is 0.5 of the original height.
        float scaleX = 0.5;
        float scaleY = 0.5;
        OH\_PixelMap\_Scale(native, scaleX, scaleY);
    
        // Translate the image.
        // translateX: Translate the image by 50 units downwards.
        // translateY: Translate the image by 50 units rightwards.
        float translateX = 50;
        float translateY = 50;
        OH\_PixelMap\_Translate(native, translateX, translateY);
    
        // Rate the image clockwise by 90°.
        float angle = 90;
        OH\_PixelMap\_Rotate(native, angle);
    
        // Flip the image.
        // flipX: whether to flip the image horizontally. The value 1 means to flip the image and 0 means the opposite.
        // flipY: whether to flip the image vertically. The value 1 means to flip the image and 0 means the opposite.
        int32\_t flipX = 0;
        int32\_t flipY = 1;
        OH\_PixelMap\_Flip(native, flipX, flipY);
    
        // Crop the image.
        // cropX: x-axis coordinate of the start point for cropping.
        // cropY: y-axis coordinate of the start point for cropping.
        // cropH: height after cropping (10), cropping from top to bottom.
        // cropW: width after cropping (10), cropping from left to right.
        int32\_t cropX = 1;
        int32\_t cropY = 1;
        int32\_t cropW = 10;
        int32\_t cropH = 10;
        OH\_PixelMap\_Crop(native, cropX, cropY, cropW, cropH);
    
        // Obtain the memory address of the PixelMap object and lock the memory.
        void \*pixelAddr = nullptr;
        OH\_PixelMap\_AccessPixels(native, &pixelAddr);
    
        // Unlock the memory of the PixelMap object.
        OH\_PixelMap\_UnAccessPixels(native);
    
        return result;
    }
    

**Calling APIs on the JS Side**

1.  Open src\\main\\cpp\\types\*libentry\\index.d.ts\* (where **libentry** varies according to the project name), and import the following files:
    
    import { image } from '@kit.ImageKit';
    
    export const createPixelMapTest: () => image.PixelMap;
    export const transform: (a: image.PixelMap) => void;
    
2.  Open **src\\main\\ets\\pages\\index.ets**, import **libentry.so** (where **libentry** varies according to the project name), call the native APIs, and pass in the JS resource object. The sample code is as follows:
    
    import testNapi from 'libentry.so';
    import { image } from '@kit.ImageKit';
    
    @Entry
    @Component
    struct Index {
    @State \_pixelMap : image.PixelMap | undefined = undefined;
    
    build() {
        Row() {
            Column() {
                Button("PixelMap")
                .width(100)
                .height(100)
                .onClick(() => {
                    console.info("com.example.native\_ndk\_api10 button click in");
                    this.\_pixelMap = testNapi.createPixelMapTest();
                    testNapi.transform(this.\_pixelMap);
                })
                Image(this.\_pixelMap)
                .width(500)
                .height(500)
                .objectFit(ImageFit.Cover)
                .border({width: 1, color: Color.Blue})
                }
                .width('100%')
            }
            .height('100%')
        }
    }
