# Using Image\_NativeModule to Decode Pictures

This topic describes how to create an ImageSource instance, decode it to obtain Picture object, and release the ImageSource instance.

#### How to Develop

## Adding a Link Library

Open the **src/main/cpp/CMakeLists.txt** file of the native project, add **libimage\_source.so** and **libhilog\_ndk.z.so** (on which the log APIs depend) to the **target\_link\_libraries** dependency.

target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so libimage\_source.so)

## Calling the Native APIs

For details about the APIs, see [Image\_NativeModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-nativemodule).

Create a native C++ application in DevEco Studio. The project created by default contains the **index.ets** file, and a **hello.cpp** or **napi\_init.cpp** file is generated in the **entry\\src\\main\\cpp** directory. In this example, the generated file is **hello.cpp**. Implement the C APIs in **hello.cpp**. Refer to the sample code below.

**Example of Using the Decoding APIs**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/mPUt4R2jQFWhPH8LyQN9Dw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00AB0DF1AE4ECAF43A177E9C3EB9E2DF49DBE6C6F2EE3E0ECDFCFD98CF016779)

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
    
3.  Define the ImagePictureNative class.
    
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
    
4.  Create an ImagePictureNative instance.
    
    static ImagePictureNative \*g\_thisPicture = new ImagePictureNative();
    
5.  Define the ImageAuxiliaryPictureNative class.
    
    class ImageAuxiliaryPictureNative {
    public:
        Image\_ErrorCode errorCode = IMAGE\_SUCCESS;
        Image\_AuxiliaryPictureType type = AUXILIARY\_PICTURE\_TYPE\_GAINMAP;
        OH\_AuxiliaryPictureNative \*auxiliaryPicture = nullptr;
        size\_t buffSize = 640 \* 480 \* 4; // Size of the auxiliary picture (width \* height \* number of bytes per pixel).
        ImageAuxiliaryPictureNative() {}
        ~ImageAuxiliaryPictureNative() {}
    };
    
6.  Create an ImageAuxiliaryPictureNative instance.
    
    static ImageAuxiliaryPictureNative \*g\_thisAuxiliaryPicture  = new ImageAuxiliaryPictureNative();
    
7.  Create the **GetJsResult** function to process the NAPI return value.
    
    // Process the NAPI return value.
    napi\_value GetJsResult(napi\_env env, int result)
    {
        napi\_value resultNapi = nullptr;
        napi\_create\_int32(env, result, &resultNapi);
        return resultNapi;
    }
    
8.  Create and configure decoding options, and call the decoding API to decode the image and obtain an auxiliary image.
    
    // Release the image source.
    napi\_value ReleasePictureSource(napi\_env env, napi\_callback\_info info)
    {
        if (g\_thisPicture->source != nullptr) {
            g\_thisPicture->errorCode = OH\_ImageSourceNative\_Release(g\_thisPicture->source);
            g\_thisPicture->source = nullptr;
            return GetJsResult(env, g\_thisPicture->errorCode);
        }
        
        if (g\_thisPicture->picture != nullptr) {
            g\_thisPicture->errorCode = OH\_PictureNative\_Release(g\_thisPicture->picture);
            g\_thisPicture->picture = nullptr;
            return GetJsResult(env, g\_thisPicture->errorCode);
        }
        
        OH\_LOG\_DEBUG(LOG\_APP, "ReleasePictureSource source is null !");
        return GetJsResult(env, g\_thisPicture->errorCode);
    }
    
    // Create decoding parameters.
    napi\_value CreateDecodingOptions(napi\_env env, napi\_callback\_info info)
    {
        g\_thisPicture->errorCode = OH\_DecodingOptionsForPicture\_Create(&g\_thisPicture->options);
    
        if (g\_thisPicture->errorCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_DecodingOptionsForPicture\_Create failed, errCode: %{public}d.",
                         g\_thisPicture->errorCode);
            return GetJsResult(env, g\_thisPicture->errorCode);
        } else {
            OH\_LOG\_DEBUG(LOG\_APP, "OH\_DecodingOptionsForPicture\_Create success !");
        }
    
        return GetJsResult(env, g\_thisPicture->errorCode);
    }
    
    // Configure decoding parameters, which are passed from the application layer.
    napi\_value SetDesiredAuxiliaryPictures(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
        if (napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr) != napi\_ok || argc < 1 || args\[0\] == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "napi\_get\_cb\_info failed !");
            return GetJsResult(env, IMAGE\_BAD\_PARAMETER);
        }
    
        uint32\_t length = 0;
        napi\_get\_array\_length(env, args\[0\], &length);
        if (length <= 0) {
            OH\_LOG\_ERROR(LOG\_APP, "napi\_get\_array\_length failed !");
            return GetJsResult(env, IMAGE\_UNKNOWN\_ERROR);
        }
        Image\_AuxiliaryPictureType typeList\[length\];
        for (int index = 0; index < length; index++) {
            napi\_value element;
            uint32\_t ulType = 0;
            napi\_get\_element(env, args\[0\], index, &element);
            napi\_get\_value\_uint32(env, element, &ulType);
            typeList\[index\] = static\_cast<Image\_AuxiliaryPictureType>(ulType);
            OH\_LOG\_DEBUG(LOG\_APP, "ulType is :%{public}d", ulType);
        }
        
        // Call OH\_DecodingOptionsForPicture\_Create to create DecodingOptions.
        CreateDecodingOptions(env, info);
        g\_thisPicture->errorCode =
            OH\_DecodingOptionsForPicture\_SetDesiredAuxiliaryPictures(g\_thisPicture->options, typeList, length);
        if (g\_thisPicture->errorCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_DecodingOptionsForPicture\_SetDesiredAuxiliaryPictures failed,errCode: %{public}d.",
                         g\_thisPicture->errorCode);
            return GetJsResult(env, g\_thisPicture->errorCode);
        } else {
            OH\_LOG\_DEBUG(LOG\_APP, "OH\_DecodingOptionsForPicture\_SetDesiredAuxiliaryPictures success !");
        }
    
        return GetJsResult(env, g\_thisPicture->errorCode);
    }
    
    // Decode data.
    napi\_value CreatePictureByImageSource(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = {nullptr};
    
        if (napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr) != napi\_ok || argc < 1 || args\[0\] == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "CreatePicture\_ napi\_get\_cb\_info failed !");
            return GetJsResult(env, IMAGE\_BAD\_PARAMETER);
        }
        
        char filePath\[MAX\_SIZE\];
        size\_t pathSize;
        napi\_get\_value\_string\_utf8(env, args\[0\], filePath, MAX\_SIZE, &pathSize);
    
        g\_thisPicture->errorCode = OH\_ImageSourceNative\_CreateFromUri(filePath, pathSize, &g\_thisPicture->source);
        if (g\_thisPicture->errorCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageSourceNative\_CreateFromUri failed, errCode: %{public}d.",
                         g\_thisPicture->errorCode);
            return GetJsResult(env, g\_thisPicture->errorCode);
        } else {
            OH\_LOG\_DEBUG(LOG\_APP, "OH\_ImageSourceNative\_CreateFromUri success !");
        }
        
        // Create decoding options and then decode the video. The API for creating the decoding options is implemented in SetDesiredAuxiliaryPictures.
        g\_thisPicture->errorCode =
            OH\_ImageSourceNative\_CreatePicture(g\_thisPicture->source, g\_thisPicture->options, &g\_thisPicture->picture);
        
        // Release the decoding options.
        OH\_DecodingOptionsForPicture\_Release(g\_thisPicture->options);
        g\_thisPicture->options = nullptr;
        
        g\_thisAuxiliaryPicture ->errorCode = OH\_PictureNative\_GetAuxiliaryPicture(g\_thisPicture->picture,
            g\_thisAuxiliaryPicture ->type, &g\_thisAuxiliaryPicture ->auxiliaryPicture);
        if (g\_thisAuxiliaryPicture ->errorCode == IMAGE\_SUCCESS) {
            uint8\_t\* buff = new uint8\_t\[g\_thisAuxiliaryPicture ->buffSize\];
            OH\_AuxiliaryPictureNative\_ReadPixels(g\_thisAuxiliaryPicture ->auxiliaryPicture, buff,
                &g\_thisAuxiliaryPicture ->buffSize);
            OH\_AuxiliaryPictureNative\_Release(g\_thisAuxiliaryPicture ->auxiliaryPicture);
            g\_thisAuxiliaryPicture ->auxiliaryPicture = nullptr;
            delete \[\]buff;
        }
        
        if (g\_thisPicture->errorCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "ImageSourceNative\_CreatePicture failed, errCode: %{public}d.",
                         g\_thisPicture->errorCode);
            return GetJsResult(env, g\_thisPicture->errorCode);
        } else {
            OH\_LOG\_DEBUG(LOG\_APP, "ImageSourceNative\_CreatePicture success !");
        }
        
        return GetJsResult(env, g\_thisPicture->errorCode);
    }
