# Using Image\_NativeModule to Encode Pictures

With Image\_NativeModule, you can create and release ImagePacker instances and encode picture objects.

#### How to Develop

## Adding a Link Library

Open the **src/main/cpp/CMakeLists.txt** file of the native project, add **libimage\_packer.so** and **libhilog\_ndk.z.so** (on which the log APIs depend) to the **target\_link\_libraries** dependency.

target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so libimage\_source.so libimage\_packer.so libpixelmap.so)

## Calling the Native APIs

For details about the APIs, see [Image\_NativeModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-nativemodule).

Create a native C++ application in DevEco Studio. The project created by default contains the **index.ets** file, and a **hello.cpp** or **napi\_init.cpp** file is generated in the **entry\\src\\main\\cpp** directory. In this example, the generated file is **hello.cpp**. Implement the C APIs in **hello.cpp**. Refer to the sample code below.

**Example of Using the Encoding APIs**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/uonl1g_7QOi2iKZ48jn62g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD1D45978B4C6C5242D516082DC094C517FB2E6DAA137AC98BCA36C05577EC7F)

According to the MIME protocol, the standard encoding format is image/jpeg. When the APIs provided by the image module are used for encoding, **image\_MimeType** of the encoding parameters must be set to **image/jpeg**. The file name extension of the encoded image file can be .jpg or .jpeg, and the file can be used on platforms that support image/jpeg decoding.

Certain APIs are supported only in API version 20 or later. You should select an appropriate API version during development.

1.  Import the required header files.
    
    #include <hilog/log.h>
    #include <multimedia/image\_framework/image/image\_native.h>
    #include <multimedia/image\_framework/image/image\_packer\_native.h>
    #include <multimedia/image\_framework/image/image\_source\_native.h>
    #include <multimedia/image\_framework/image/picture\_native.h>
    #include <multimedia/image\_framework/image/pixelmap\_native.h>
    
2.  Modify the log macro definition as required.
    
    #undef LOG\_DOMAIN
    #undef LOG\_TAG
    #define LOG\_DOMAIN 0x3200
    #define LOG\_TAG "IMAGE\_SAMPLE"
    
3.  Define constants used for image processing.
    
    #define AUTO 0
    #define SDR 1
    const int MAX\_SIZE = 1024;
    const int MAX\_FORMAT\_LENGTH = 20;
    
4.  Define the ImagePictureNative class.
    
    class ImagePictureNative {
    public:
        Image\_ErrorCode errorCode = IMAGE\_SUCCESS;
        OH\_DecodingOptionsForPicture \*options = nullptr;
        OH\_ImagePackerNative \*imagePacker = nullptr;
        OH\_PackingOptions \*packerOptions = nullptr;
        OH\_PictureNative \*picture = nullptr;
        OH\_ImageSourceNative \*source = nullptr;
        ImagePictureNative() {}
        ~ImagePictureNative() {}
    };
    
5.  Create an instance of ImagePictureNative.
    
    static ImagePictureNative \*g\_thisPicture = new ImagePictureNative();
    
6.  Create the **GetJsResult** function to process the NAPI return value.
    
    // Process the NAPI return value.
    napi\_value GetJsResult(napi\_env env, int result)
    {
        napi\_value resultNapi = nullptr;
        napi\_create\_int32(env, result, &resultNapi);
        return resultNapi;
    }
    
7.  After an ImagePacker instance is created and encoding parameters are specified, the Picture object is encoded to a file or buffer.
    
    // Set packing parameters.
    void SetPackOptions(OH\_PackingOptions \*packerOptions,
                        Image\_MimeType format,
                        uint32\_t quality,
                        bool needsPackProperties,
                        int32\_t desiredDynamicRange)
    {
        OH\_PackingOptions\_SetMimeType(packerOptions, &format);
        OH\_PackingOptions\_SetQuality(packerOptions, quality);
        OH\_PackingOptions\_SetNeedsPackProperties(packerOptions, needsPackProperties);
        OH\_PackingOptions\_SetDesiredDynamicRange(packerOptions, desiredDynamicRange);
    }
    
    // PackToData.
    napi\_value PackToDataFromPicture(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
        if (napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr) != napi\_ok) {
            OH\_LOG\_ERROR(LOG\_APP, "napi\_get\_cb\_info failed!");
            return GetJsResult(env, g\_thisPicture->errorCode);
        }
        
        size\_t outDataSize = 10000 \* 10000;
        uint8\_t \*outData = new uint8\_t\[outDataSize\];
    
        if (g\_thisPicture->packerOptions == nullptr) {
            g\_thisPicture->errorCode = OH\_PackingOptions\_Create(&g\_thisPicture->packerOptions);
        }
        if (g\_thisPicture->imagePacker == nullptr) {
            g\_thisPicture->errorCode = OH\_ImagePackerNative\_Create(&g\_thisPicture->imagePacker);
        }
        
        char strFormat\[MAX\_FORMAT\_LENGTH\];
        size\_t strFormatSize;
        napi\_get\_value\_string\_utf8(env, args\[0\], strFormat, MAX\_FORMAT\_LENGTH, &strFormatSize);
        OH\_LOG\_DEBUG(LOG\_APP, "PackToDataFromPicture format: %{public}s", strFormat);
    
        Image\_MimeType format;
        format.size = strFormatSize;
        format.data = const\_cast<char \*>(strFormat);
        uint32\_t quality = 95;
        bool needsPackProperties = true;
        int32\_t desiredDynamicRange = AUTO;
        SetPackOptions(g\_thisPicture->packerOptions, format, quality, needsPackProperties, desiredDynamicRange);
        // Ensure that the Picture object has been created.
        g\_thisPicture->errorCode = OH\_ImagePackerNative\_PackToDataFromPicture(
            g\_thisPicture->imagePacker, g\_thisPicture->packerOptions, g\_thisPicture->picture, outData, &outDataSize);
        
        // Release imagePacker and packerOptions.
        OH\_PackingOptions\_Release(g\_thisPicture->packerOptions);
        g\_thisPicture->packerOptions = nullptr;
        OH\_ImagePackerNative\_Release(g\_thisPicture->imagePacker);
        g\_thisPicture->imagePacker = nullptr;
        
        if (g\_thisPicture->errorCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImagePackerNative\_PackToDataFromPicture failed, errCode: %{public}d.",
                         g\_thisPicture->errorCode);
            delete\[\] outData;
            return GetJsResult(env, g\_thisPicture->errorCode);
        } else {
            OH\_LOG\_DEBUG(LOG\_APP, "OH\_ImagePackerNative\_PackToDataFromPicture success !");
        }
        delete\[\] outData;
        return GetJsResult(env, g\_thisPicture->errorCode);
    }
    
    // PackToFile.
    napi\_value PackToFileFromPicture(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 2;
        napi\_value args\[2\] = {nullptr};
        if (napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr) != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "napi\_get\_cb\_info failed!");
            return GetJsResult(env, g\_thisPicture->errorCode);
        }
        uint32\_t fd = 0;
        napi\_get\_value\_uint32(env, args\[0\], &fd);
    
        if (g\_thisPicture->packerOptions == nullptr) {
            g\_thisPicture->errorCode = OH\_PackingOptions\_Create(&g\_thisPicture->packerOptions);
        }
        if (g\_thisPicture->imagePacker == nullptr) {
            g\_thisPicture->errorCode = OH\_ImagePackerNative\_Create(&g\_thisPicture->imagePacker);
        }
        
        char strFormat\[MAX\_FORMAT\_LENGTH\];
        size\_t strFormatSize;
        napi\_get\_value\_string\_utf8(env, args\[1\], strFormat, MAX\_FORMAT\_LENGTH, &strFormatSize);
        OH\_LOG\_INFO(LOG\_APP, "PackToFileFromPicture format: %{public}s", strFormat);
    
        Image\_MimeType format;
        format.size = strFormatSize;
        format.data = const\_cast<char \*>(strFormat);
        uint32\_t quality = 95;
        bool needsPackProperties = false;
        int32\_t desiredDynamicRange = SDR;
        SetPackOptions(g\_thisPicture->packerOptions, format, quality, needsPackProperties, desiredDynamicRange);
        // Ensure that the Picture object has been created.
        g\_thisPicture->errorCode = OH\_ImagePackerNative\_PackToFileFromPicture(
            g\_thisPicture->imagePacker, g\_thisPicture->packerOptions, g\_thisPicture->picture, fd);
        
        // Release imagePacker and packerOptions.
        OH\_PackingOptions\_Release(g\_thisPicture->packerOptions);
        g\_thisPicture->packerOptions = nullptr;
        OH\_ImagePackerNative\_Release(g\_thisPicture->imagePacker);
        g\_thisPicture->imagePacker = nullptr;
        
        if (g\_thisPicture->errorCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImagePackerNative\_PackToFileFromPicture failed,"
                         "errCode: %{public}d.", g\_thisPicture->errorCode);
            return GetJsResult(env, g\_thisPicture->errorCode);
        } else {
            OH\_LOG\_DEBUG(LOG\_APP, "OH\_ImagePackerNative\_PackToFileFromPicture success !");
        }
    
        return GetJsResult(env, g\_thisPicture->errorCode);
    }
