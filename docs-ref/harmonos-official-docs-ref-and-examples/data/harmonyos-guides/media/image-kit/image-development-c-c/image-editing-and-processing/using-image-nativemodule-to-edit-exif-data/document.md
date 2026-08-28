# Using Image\_NativeModule to Edit Exif Data

Image Kit provides the capabilities of reading and editing Exchangeable Image File Format (Exif) data.

Exif is a file format dedicated for photos taken by digital cameras and is used to record attributes and shooting data of the photos. Currently, JPEG, PNG, HEIF, and WEBP23+ images that contain Exif data are supported.

Users may need to view or modify the Exif data of photos in the Gallery application. When the manual lens parameters of the camera are not automatically written as part of the Exif data or the shooting time is incorrect due to camera power-off, you can manually correct the Exif data.

Currently, HarmonyOS allows you to view and modify part of Exif data. For details, see [OHOS\_IMAGE\_PROPERTY\_XXX](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-common-h#variables).

#### How to Develop

## Adding a Link Library

Open the **src/main/cpp/CMakeLists.txt** file of the native project, add **libimage\_source.so** and **libhilog\_ndk.z.so** (on which the log APIs depend) to the **target\_link\_libraries** dependency.

target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so libimage\_source.so)

## Calling the Native APIs

For details about the C APIs for reading and editing Exif data, see [OH\_ImageSource\_GetImageProperty](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_getimageproperty) and [OH\_ImageSource\_ModifyImageProperty](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_modifyimageproperty).

Create a native C++ application in DevEco Studio. The project created by default contains the **index.ets** file, and a **hello.cpp** or **napi\_init.cpp** file is generated in the **entry\\src\\main\\cpp** directory. In this example, the generated file is **hello.cpp**. Implement the C APIs in **hello.cpp**. Refer to the sample code below.

**Example for Reading and Editing Exif Data**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/vpMMkURXRliYvSHeNATnOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7875841A1F6ED4F0EC3E93218C4575F0F2773ABF9156C1363559FC7C727BF78)

Certain APIs are supported only in API version 20 or later. You should select an appropriate API version during development.

1.  Import the required header files.
    
    #include <string>
    #include <hilog/log.h>
    #include <multimedia/image\_framework/image/image\_source\_native.h>
    #include "napi/native\_api.h"
    
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
    
5.  Create the GetJsResult function to process the NAPI return value.
    
    // Process the NAPI return value.
    napi\_value GetJsResult(napi\_env env, int result)
    {
        napi\_value resultNapi = nullptr;
        napi\_create\_int32(env, result, &resultNapi);
        return resultNapi;
    }
    
6.  After an ImageSource object is created, read and edit its Exif data.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/YfANzb2yQuyKxIrEmSqlUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7124882F4D8490C42F1B0D6437F9F119E1DE134BCF8D568D0AE8EC3AACCAB95)
    
    For details about how to create an ImageSource object, see [Image Decoding](../../image-decoding/using-image-nativemodule-to-decode-images/document.md).
    
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
        // Modify the value of a specified property key.
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
