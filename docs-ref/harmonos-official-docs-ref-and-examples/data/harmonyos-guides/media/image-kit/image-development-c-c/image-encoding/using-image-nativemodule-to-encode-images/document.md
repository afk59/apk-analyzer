# Using Image\_NativeModule to Encode Images

You can use the **ImagePacker** class to create and release ImagePacker instances.

#### How to Develop

## Adding a Link Library

Open the **src/main/cpp/CMakeLists.txt** file of the native project, add **libimage\_packer.so** and **libhilog\_ndk.z.so** (on which the log APIs depend) to the **target\_link\_libraries** dependency.

target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so libimage\_source.so libimage\_packer.so libpixelmap.so)

## Calling the Native APIs

For details about the APIs, see [Image\_NativeModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-nativemodule).

Create a native C++ application in DevEco Studio. The project created by default contains the **index.ets** file, and a **hello.cpp** or **napi\_init.cpp** file is generated in the **entry\\src\\main\\cpp** directory. In this example, the generated file is **hello.cpp**. Implement the C APIs in **hello.cpp**. Refer to the sample code below.

**Example of Using the Encoding APIs**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/tVRq8MsbT2y66uRdWOIXaA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C115B9D182C801734CB9652971CABC583AD09875C1EBA459A0CF01B930849A74)

-   According to the MIME protocol, the standard encoding format is image/jpeg. When the APIs provided by the image module are used for encoding, **image\_MimeType** of the encoding parameters must be set to **image/jpeg**. The file name extension of the encoded image file can be .jpg or .jpeg, and the file can be used on platforms that support image/jpeg decoding.
    
-   Some APIs (such as [OH\_ImagePackerNative\_GetSupportedFormats](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-packer-native-h#oh_imagepackernative_getsupportedformats)) are supported only in API version 20 or later. You need to select a proper API version during development.
    

1.  Import the required header files.
    
    #include <string>
    #include <hilog/log.h>
    #include <multimedia/image\_framework/image/image\_source\_native.h>
    #include "napi/native\_api.h"
    #include <multimedia/image\_framework/image/image\_common.h>
    #include <multimedia/image\_framework/image/pixelmap\_native.h>
    #include <set>
    #include <multimedia/image\_framework/image/image\_packer\_native.h>
    
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
    
5.  Define a global variable to record the encoding formats supported.
    
    static std::set<std::string> g\_encodeSupportedFormats;
    
6.  Create the **GetJsResult** function to process the NAPI return value.
    
    // Process the NAPI return value.
    napi\_value GetJsResult(napi\_env env, int result)
    {
        napi\_value resultNapi = nullptr;
        napi\_create\_int32(env, result, &resultNapi);
        return resultNapi;
    }
    
7.  After an ImagePacker instance is created and encoding parameters are specified, the ImageSource or PixelMap object is encoded to a file or buffer.
    
    // Obtain the encoding capability range.
    Image\_ErrorCode GetEncodeSupportedFormats()
    {
        Image\_MimeType\* mimeType = nullptr;
        size\_t length = 0;
        Image\_ErrorCode errCode = OH\_ImagePackerNative\_GetSupportedFormats(&mimeType, &length);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImagePackerNative\_GetSupportedFormats failed,"
                                  "errCode: %{public}d.", errCode);
            return errCode;
        }
        for (size\_t count = 0; count < length; count++) {
            if (mimeType\[count\].data != nullptr) {
                g\_encodeSupportedFormats.insert(std::string(mimeType\[count\].data));
                OH\_LOG\_INFO(LOG\_APP, "Encode supportedFormats: %{public}s", mimeType\[count\].data);
            }
        }
        return IMAGE\_SUCCESS;
    }
    
    Image\_MimeType GetMimeTypeIfEncodable(const char \*format)
    {
        auto it = g\_encodeSupportedFormats.find(format);
        if (it == g\_encodeSupportedFormats.end()) {
            return {const\_cast<char \*>(""), 0};
        }
        return {const\_cast<char \*>(format), strlen(format)};
    }
    
    Image\_ErrorCode packToFileFromImageSourceTest(int fd, OH\_ImageSourceNative\* imageSource)
    {
        // Create an ImagePacker instance.
        OH\_ImagePackerNative \*testPacker = nullptr;
        Image\_ErrorCode errCode = OH\_ImagePackerNative\_Create(&testPacker);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromImageSourceTest OH\_ImagePackerNative\_Create failed,"
                                  "errCode: %{public}d.", errCode);
            return errCode;
        }
        
        // Obtain the encoding capability range.
        errCode = GetEncodeSupportedFormats();
        if (errCode != IMAGE\_SUCCESS) {
            OH\_ImagePackerNative\_Release(testPacker);
            return errCode;
        }
        
        // Specify encoding parameters and encode the ImageSource into a file.
        OH\_PackingOptions \*option = nullptr;
        OH\_PackingOptions\_Create(&option);
        Image\_MimeType image\_MimeType = GetMimeTypeIfEncodable(MIME\_TYPE\_JPEG);
        if (image\_MimeType.data == nullptr || image\_MimeType.size == 0) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromImageSourceTest GetMimeTypeIfEncodable failed,"
                         "format can't support encode.");
            return IMAGE\_BAD\_PARAMETER;
        }
        OH\_PackingOptions\_SetMimeType(option, &image\_MimeType);
        // HDR encoding is possible only when the device supports HDR encoding, the image resource is an HDR image, and the format of the image resource is JPEG.
        OH\_PackingOptions\_SetDesiredDynamicRange(option, IMAGE\_PACKER\_DYNAMIC\_RANGE\_AUTO);
        // Set the encoding quality (default: 0; recommended ≥ 80).
        uint32\_t quality = 90;
        OH\_PackingOptions\_SetQuality(option, quality);
        errCode = OH\_ImagePackerNative\_PackToFileFromImageSource(testPacker, option, imageSource, fd);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromImageSourceTest OH\_ImagePackerNative\_PackToFileFromImageSource failed,"
                                  "errCode: %{public}d.", errCode);
            return errCode;
        }
    
        // Release the ImagePacker instance.
        errCode = OH\_ImagePackerNative\_Release(testPacker);
        testPacker = nullptr;
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromImageSourceTest OH\_ImagePackerNative\_Release failed,"
                         "errCode: %{public}d.", errCode);
            return errCode;
        }
        
        // Release the PackingOptions instance.
        errCode = OH\_PackingOptions\_Release(option);
        option = nullptr;
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromImageSourceTest OH\_PackingOptions\_Release failed,"
                         "errCode: %{public}d.", errCode);
            return errCode;
        }
        return IMAGE\_SUCCESS;
    }
    
    Image\_ErrorCode packToFileFromPixelmapTest(int fd, OH\_PixelmapNative \*pixelmap)
    {
        // Create an ImagePacker instance.
        OH\_ImagePackerNative \*testPacker = nullptr;
        Image\_ErrorCode errCode = OH\_ImagePackerNative\_Create(&testPacker);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromPixelmapTest CreatePacker OH\_ImagePackerNative\_Create failed,"
                         "errCode: %{public}d.", errCode);
            return errCode;
        }
    
        // Specify encoding parameters and encode the PixelMap into a file.
        OH\_PackingOptions \*option = nullptr;
        OH\_PackingOptions\_Create(&option);
        char type\[\] = "image/jpeg";
        Image\_MimeType image\_MimeType = {type, strlen(type)};
        OH\_PackingOptions\_SetMimeType(option, &image\_MimeType);
        // Set the encoding quality (default: 0; recommended ≥ 80).
        uint32\_t quality = 90;
        OH\_PackingOptions\_SetQuality(option, quality);
        errCode = OH\_ImagePackerNative\_PackToFileFromPixelmap(testPacker, option, pixelmap, fd);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromPixelmapTest OH\_ImagePackerNative\_PackToFileFromPixelmap failed,"
                                  "errCode: %{public}d.", errCode);
            return errCode;
        }
    
        // Release the ImagePacker instance.
        errCode = OH\_ImagePackerNative\_Release(testPacker);
        testPacker = nullptr;
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromPixelmapTest ReleasePacker OH\_ImagePackerNative\_Release failed,"
                                  "errCode: %{public}d.", errCode);
            return errCode;
        }
        
        // Release the PackingOptions instance.
        errCode = OH\_PackingOptions\_Release(option);
        option = nullptr;
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromPixelmapTest OH\_PackingOptions\_Release failed,"
                                  "errCode: %{public}d.", errCode);
            return errCode;
        }
        
        return IMAGE\_SUCCESS;
    }
    
    napi\_value PackToFileFromImageSourceTestJs(napi\_env env, napi\_callback\_info info)
    {
        napi\_value argv\[1\] = {0};
        size\_t argc = 1;
        if (napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr) != napi\_ok) {
            OH\_LOG\_ERROR(LOG\_APP, "PackToFileFromImageSourceTestJs napi\_get\_cb\_info failed.");
            return nullptr;
        }
        
        int fd;
        napi\_get\_value\_int32(env, argv\[0\], &fd);
        
        Image\_ErrorCode errCode = packToFileFromImageSourceTest(fd, g\_thisImageSource->source);
        if (errCode == IMAGE\_SUCCESS) {
            OH\_LOG\_INFO(LOG\_APP, "ImagePackerNativeCTest PackToFileFromImageSourceTestJs successfully.");
        }
        return GetJsResult(env, errCode);
    }
    
    napi\_value PackToFileFromPixelmapTestJs(napi\_env env, napi\_callback\_info info)
    {
        napi\_value argv\[1\] = {0};
        size\_t argc = 1;
        if (napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr) != napi\_ok) {
            OH\_LOG\_ERROR(LOG\_APP, "PackToFileFromImageSourceTestJs napi\_get\_cb\_info failed.");
            return nullptr;
        }
        
        int fd;
        napi\_get\_value\_int32(env, argv\[0\], &fd);
        
        Image\_ErrorCode errCode = packToFileFromPixelmapTest(fd, g\_thisImageSource->resPixMap);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "packToFileFromPixelmapTest failed,"
                         "errCode: %{public}d.", errCode);
            return GetJsResult(env, errCode);
        } else {
            OH\_LOG\_INFO(LOG\_APP, "PackToFileFromPixelmapTestJs successfully.");
        }
        return GetJsResult(env, errCode);
    }
