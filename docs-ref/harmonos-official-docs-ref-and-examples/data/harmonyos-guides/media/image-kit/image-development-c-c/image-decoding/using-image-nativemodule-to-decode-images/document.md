# Using Image\_NativeModule to Decode Images

This topic describes how to create an ImageSource object, obtain the width and height of the PixelMap, and release the ImageSource object.

Starting from API version 22, thumbnail decoding is provided for images in various professional camera formats. The formats supported are CR2, CR3, ARW, NEF, RAF, NRW, ORF, RW2, PEF, and SRW.

#### How to Develop

## Adding a Link Library

Open the **src/main/cpp/CMakeLists.txt** file of the native project, add **libimage\_source.so**, **libpixelmap.so**, and **libhilog\_ndk.z.so** (on which the log APIs depend) to the **target\_link\_libraries** dependency.

target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so libimage\_source.so libpixelmap.so)

## Calling the Native APIs

For details about the APIs, see [Image\_NativeModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-nativemodule).

Create a native C++ application in DevEco Studio. The project created by default contains the **index.ets** file, and a **hello.cpp** or **napi\_init.cpp** file is generated in the **entry\\src\\main\\cpp** directory. In this example, the generated file is **hello.cpp**. Implement the C APIs in **hello.cpp**. Refer to the sample code below.

**Example of Using the Decoding APIs**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/R3-korE_QYCCkzI5QVoY_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14CB90CDA8241EF3B60F5DB18C91981F1FA81C466B85DDA20347BE628DEC5E09)

Some APIs (such as [OH\_ImageSourceNative\_GetSupportedFormats](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_getsupportedformats)) are supported only in API version 20 or later. You need to select a proper API version during development.

1.  Import the required header files.
    
    #include <string>
    #include <hilog/log.h>
    #include <multimedia/image\_framework/image/image\_source\_native.h>
    #include "napi/native\_api.h"
    #include <multimedia/image\_framework/image/image\_common.h>
    #include <multimedia/image\_framework/image/pixelmap\_native.h>
    
2.  Modify the log macro definition as required.
    
    #undef LOG\_DOMAIN
    #undef LOG\_TAG
    #define LOG\_DOMAIN 0x3200
    #define LOG\_TAG "IMAGE\_SAMPLE"
    
3.  Define the ImageSourceNative class.
    
    class ImageSourceNative {
    public:
        OH\_ImageSource\_Info \*imageInfo;
        OH\_ImageSourceNative \*source = nullptr;
        OH\_PixelmapNative \*resPixMap = nullptr;
        OH\_Pixelmap\_ImageInfo \*pixelmapImageInfo = nullptr;
        uint32\_t frameCnt = 0;
        ImageSourceNative() {}
        ~ImageSourceNative() {}
    };
    
4.  Create an instance of ImageSourceNative.
    
    static ImageSourceNative \*g\_thisImageSource = new ImageSourceNative();
    
5.  Create the **GetJsResult** function to process the NAPI return value.
    
    // Process the NAPI return value.
    napi\_value GetJsResult(napi\_env env, int result)
    {
        napi\_value resultNapi = nullptr;
        napi\_create\_int32(env, result, &resultNapi);
        return resultNapi;
    }
    
6.  Define constants.
    
    const int MAX\_STRING\_LENGTH = 1024;
    
7.  Create an ImageSource instance.
    
    // Return the error code.
    napi\_value ReturnErrorCode(napi\_env env, Image\_ErrorCode errCode, std::string funcName)
    {
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "%{public}s failed, errCode: %{public}d.", funcName.c\_str(), errCode);
            return GetJsResult(env, errCode);
        }
        return GetJsResult(env, errCode);
    }
    
    // Obtain the decoding capability range.
    napi\_value GetSupportedFormats(napi\_env env, napi\_callback\_info info)
    {
        Image\_MimeType\* mimeType = nullptr;
        size\_t length = 10;
        Image\_ErrorCode errCode = OH\_ImageSourceNative\_GetSupportedFormats(&mimeType, &length);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageSourceNative\_GetSupportedFormats failed, "
                         "errCode: %{public}d.", errCode);
            return GetJsResult(env, errCode);
        }
        for (size\_t count = 0; count < length; count++) {
            OH\_LOG\_INFO(LOG\_APP, "Decode supportedFormats: %{public}s", mimeType\[count\].data);
        }
        return GetJsResult(env, errCode);
    }
    
    // Create an ImageSource instance.
    napi\_value CreateImageSource(napi\_env env, napi\_callback\_info info)
    {
        napi\_value argValue\[1\] = {nullptr};
        size\_t argCount = 1;
        if (napi\_get\_cb\_info(env, info, &argCount, argValue, nullptr, nullptr) != napi\_ok || argCount < 1 ||
            argValue\[0\] == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "CreateImageSource napi\_get\_cb\_info failed!");
            return GetJsResult(env, IMAGE\_BAD\_PARAMETER);
        }
    
        char name\[MAX\_STRING\_LENGTH\];
        size\_t nameSize = MAX\_STRING\_LENGTH;
        napi\_get\_value\_string\_utf8(env, argValue\[0\], name, MAX\_STRING\_LENGTH, &nameSize);
    
        Image\_ErrorCode errCode = OH\_ImageSourceNative\_CreateFromUri(name, nameSize, &g\_thisImageSource->source);
        return ReturnErrorCode(env, errCode, "OH\_ImageSourceNative\_CreateFromUri");
    }
    
8.  After creating an ImageSource instance, obtain and modify property values, create a PixelMap object by using decoding parameters, and obtain the number of image frames.
    
    -   Create a PixelMap object.
        
        // Create a PixelMap object based on image decoding parameters.
        napi\_value CreatePixelMap(napi\_env env, napi\_callback\_info info)
        {
            // nullptr cannot be passed in to ops. If ops does not need to be set, you do not need to create a PixelMap object.
            OH\_DecodingOptions \*ops = nullptr;
            OH\_DecodingOptions\_Create(&ops);
            // If \*\*IMAGE\_DYNAMIC\_RANGE\_AUTO\*\* is passed in, the system decodes the image based on the image format and the device capabilities. If the image is HDR and the device supports HDR decoding, the image is decoded into an HDR PixelMap.
            OH\_DecodingOptions\_SetDesiredDynamicRange(ops, IMAGE\_DYNAMIC\_RANGE\_AUTO);
            
            OH\_PixelmapNative\_Release(g\_thisImageSource->resPixMap);
            g\_thisImageSource->resPixMap = nullptr;
            
            Image\_ErrorCode errCode = OH\_ImageSourceNative\_CreatePixelmap(g\_thisImageSource->source,
                                                                          ops, &g\_thisImageSource->resPixMap);
            OH\_DecodingOptions\_Release(ops);
            ops = nullptr;
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageSourceNative\_CreatePixelmap failed, errCode: %{public}d.", errCode);
                return GetJsResult(env, errCode);
            }
        
            // Check whether the PixelMap is the HDR content.
            OH\_PixelmapImageInfo\_Create(&g\_thisImageSource->pixelmapImageInfo);
            OH\_PixelmapNative\_GetImageInfo(g\_thisImageSource->resPixMap, g\_thisImageSource->pixelmapImageInfo);
            bool pixelmapIsHdr;
            OH\_PixelmapImageInfo\_GetDynamicRange(g\_thisImageSource->pixelmapImageInfo, &pixelmapIsHdr);
            if (pixelmapIsHdr) {
                OH\_LOG\_INFO(LOG\_APP, "The pixelMap's dynamicRange is HDR.");
            }
            OH\_PixelmapImageInfo\_Release(g\_thisImageSource->pixelmapImageInfo);
            g\_thisImageSource->pixelmapImageInfo = nullptr;
            return GetJsResult(env, errCode);
        }
        
    -   Create a structure object that defines the image information and obtain the image information.
        
        // Create a structure object that defines the image information and obtain the image information.
        napi\_value GetImageInfo(napi\_env env, napi\_callback\_info info)
        {
            OH\_ImageSourceInfo\_Create(&g\_thisImageSource->imageInfo);
            Image\_ErrorCode errCode = OH\_ImageSourceNative\_GetImageInfo(g\_thisImageSource->source,
                                                                        0, g\_thisImageSource->imageInfo);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageSourceInfo\_Create failed, errCode: %{public}d.", errCode);
                return GetJsResult(env, errCode);
            }
            
            uint32\_t width;
            uint32\_t height;
            OH\_ImageSourceInfo\_GetWidth(g\_thisImageSource->imageInfo, &width);
            OH\_ImageSourceInfo\_GetHeight(g\_thisImageSource->imageInfo, &height);
            OH\_LOG\_INFO(LOG\_APP, "OH\_ImageSourceNative\_GetImageInfo success,"
                       "width: %{public}d, height: %{public}d.", width, height);
            OH\_ImageSourceInfo\_Release(g\_thisImageSource->imageInfo);
            g\_thisImageSource->imageInfo = nullptr;
            return GetJsResult(env, width); // Return the width of the obtained info.
        }
        
    -   Read and edit Exif data.
        
        // Obtain the value of a specified property.
        napi\_value GetImageProperty(napi\_env env, napi\_callback\_info info)
        {
            napi\_value argValue\[1\] = {nullptr};
            size\_t argCount = 1;
            if (napi\_get\_cb\_info(env, info, &argCount, argValue, nullptr, nullptr) != napi\_ok || argCount < 1 ||
                argValue\[0\] == nullptr) {
                OH\_LOG\_ERROR(LOG\_APP, "GetImageProperty napi\_get\_cb\_info failed!");
                return GetJsResult(env, IMAGE\_BAD\_PARAMETER);
            }
            // Modify the values of the specified properties.
            char key\[MAX\_STRING\_LENGTH\];
            size\_t keySize = MAX\_STRING\_LENGTH;
            napi\_get\_value\_string\_utf8(env, argValue\[0\], (char \*)key, sizeof(key), &keySize);
            Image\_String getKey;
            getKey.data = key;
            getKey.size = keySize;
            Image\_String getValue;
            OH\_LOG\_INFO(LOG\_APP, "OH\_ImageSourceNative\_GetImageProperty key: %{public}s.", getKey.data);
            Image\_ErrorCode errCode = OH\_ImageSourceNative\_GetImagePropertyWithNull(g\_thisImageSource->source,
                                                                                    &getKey, &getValue);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageSourceNative\_GetImageProperty failed, errCode: %{public}d.", errCode);
                return GetJsResult(env, errCode);
            }
            napi\_value resultNapi = nullptr;
            napi\_create\_string\_utf8(env, getValue.data, getValue.size, &resultNapi);
            free(getValue.data);
            getValue.data = nullptr;
            return resultNapi;
        }
        
        // Modify the value of a specified property.
        napi\_value ModifyImageProperty(napi\_env env, napi\_callback\_info info)
        {
            napi\_value argValue\[2\] = {nullptr};
            size\_t argCount = 2;
            const size\_t minCount = 2;
            if (napi\_get\_cb\_info(env, info, &argCount, argValue, nullptr, nullptr) != napi\_ok || argCount < minCount ||
                argValue\[0\] == nullptr || argValue\[1\] == nullptr) {
                OH\_LOG\_ERROR(LOG\_APP, "ModifyImageProperty napi\_get\_cb\_info failed!");
                return GetJsResult(env, IMAGE\_BAD\_PARAMETER);
            }
        
            // Obtain the key to be modified.
            char key\[MAX\_STRING\_LENGTH\];
            size\_t keySize = MAX\_STRING\_LENGTH;
            napi\_get\_value\_string\_utf8(env, argValue\[0\], (char \*)key, sizeof(key), &keySize);
            Image\_String setKey;
            setKey.data = key;
            setKey.size = keySize;
            OH\_LOG\_INFO(LOG\_APP, "ModifyImageProperty key: %{public}s.", setKey.data);
            
            // Obtain the value to be modified.
            char value\[MAX\_STRING\_LENGTH\];
            size\_t valueSize;
            napi\_get\_value\_string\_utf8(env, argValue\[1\], (char \*)value, MAX\_STRING\_LENGTH, &valueSize);
            Image\_String setValue;
            setValue.data = value;
            setValue.size = valueSize;
            OH\_LOG\_INFO(LOG\_APP, "ModifyImageProperty value: %{public}s.", setValue.data);
        
            Image\_ErrorCode errCode = OH\_ImageSourceNative\_ModifyImageProperty(g\_thisImageSource->source, &setKey, &setValue);
            return ReturnErrorCode(env, errCode, "OH\_ImageSourceNative\_ModifyImageProperty");
        }
        
    -   Obtain the number of frames.
        
        // Obtain the number of image frames.
        napi\_value GetFrameCount(napi\_env env, napi\_callback\_info info)
        {
            Image\_ErrorCode errCode = OH\_ImageSourceNative\_GetFrameCount(g\_thisImageSource->source,
                                                                         &g\_thisImageSource->frameCnt);
            if (errCode != IMAGE\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageSourceNative\_GetFrameCount failed, errCode: %{public}d.", errCode);
                return GetJsResult(env, errCode);
            }
            return GetJsResult(env, g\_thisImageSource->frameCnt); // Return the number of obtained image frames.
        }
        
    -   Create a PixelMap list based on image decoding parameters.
        
        // Create a PixelMap list based on image decoding parameters.
        napi\_value CreatePixelmapList(napi\_env env, napi\_callback\_info info)
        {
            OH\_DecodingOptions \*opts = nullptr;
            OH\_DecodingOptions\_Create(&opts);
            OH\_PixelmapNative\*\* resVecPixMap = new OH\_PixelmapNative\* \[g\_thisImageSource->frameCnt\];
            size\_t outSize = g\_thisImageSource->frameCnt;
            Image\_ErrorCode errCode = OH\_ImageSourceNative\_CreatePixelmapList(g\_thisImageSource->source,
                                                                              opts, resVecPixMap, outSize);
            OH\_DecodingOptions\_Release(opts);
            opts = nullptr;
            delete\[\] resVecPixMap;
            return ReturnErrorCode(env, errCode, "OH\_ImageSourceNative\_CreatePixelmapList");
        }
        
    -   Obtain the image delay time list.
        
        // Obtain the image delay time list.
        napi\_value GetDelayTimeList(napi\_env env, napi\_callback\_info info)
        {
            int32\_t \*delayTimeList = new int32\_t\[g\_thisImageSource->frameCnt\];
            size\_t size = g\_thisImageSource->frameCnt;
            OH\_LOG\_INFO(LOG\_APP, "GetDelayTimeList size: %{public}zu.", size);
            Image\_ErrorCode errCode = OH\_ImageSourceNative\_GetDelayTimeList(g\_thisImageSource->source, delayTimeList, size);
            delete\[\] delayTimeList;
            return ReturnErrorCode(env, errCode, "OH\_ImageSourceNative\_GetDelayTimeList");
        }
        
9.  Release the ImageSource instance.
    
    // Release the instance.
    napi\_value ReleaseImageSource(napi\_env env, napi\_callback\_info info)
    {
        Image\_ErrorCode errCode = OH\_ImageSourceNative\_Release(g\_thisImageSource->source);
        g\_thisImageSource->source = nullptr;
        OH\_PixelmapNative\_Release(g\_thisImageSource->resPixMap);
        g\_thisImageSource->resPixMap = nullptr;
        return ReturnErrorCode(env, errCode, "OH\_ImageSourceNative\_Release");
    }
