# Image Encoding

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/HWFxNYYASjSZcDlWluKtNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062042Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0908FB7273D9753E2CFD865C22157C08BF2EA5FEBB752A9E0A8FF9DA870D15DE)

This guide uses the APIs provided by the [Image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image) module, which supports basic functionalities such as image encoding/decoding, image receiver operations, and image data processing. These APIs are introduced prior to API version 11, and no additional features will be included in later versions. Therefore, these APIs are not recommended.

You can also use the C APIs provided by the [Image\_NativeModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-nativemodule) module, which includes all the foundational features of the Image module while adding new capabilities like multi-image encoding/decoding. For details about the development guide, see [Using Image\_NativeModule to Decode Images (C/C++)](../../image-development-c-c/image-decoding/using-image-nativemodule-to-decode-images/document.md). These APIs are available since API version 12 and are expected to keep evolving. You are encouraged to use them.

You are not advised to use both sets of C APIs in your code. It may cause compatibility issues in some scenarios.

You can call the native APIs provided by the ImagePacker module to encode images, that is, to compress a PixelMap object into an image in the desired format.

Currently, images can be encoded only into the JPEG, WebP, PNG, or HEIF format (depending on the hardware).

**Usage Scenario**

-   Image codec conversion
    
    Import an image source, and encapsulate it into the desired format.
    
-   Image editing
    
    Edit a PixelMap object, and export an image in the desired format.
    

#### How to Develop

Read the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-packer-mdk-h) for APIs related to image encoding.

Refer to the code snippet below to complete the entire image encoding process, including creating an encoder, initializing resources, performing encoding, and destroying the encoder.

During application development, you must call the APIs in the defined sequence. Otherwise, an exception or undefined behavior may occur.

The figure below shows the call relationship of image encoding.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/nC1Rg7E-Q-G5a2NgAdETpg/en-us_image_0000002568764911.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062042Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7561018AC88199F6836CAC687FC73AEBD622F5C597612A6A4AEB0E156F2E5A30)

## Linking the Dynamic Library in the CMake Script

target\_link\_libraries(entry PUBLIC libace\_napi.z.so)
target\_link\_libraries(entry PUBLIC libimage\_packer\_ndk.z.so)

## How to Develop

1.  Add the header file **image\_packer\_mdk.h**.
    
    // Add the header file image\_packer\_mdk.h.
    #include <multimedia/image\_framework/image\_packer\_mdk.h>
    
2.  Create an encoder instance.
    
    You must use napi\_env to create an encoder.
    
    // Use napi\_value to undertake the created encoder instance.
    napi\_value packer;
    // Use napi\_env to create an encoder. If result is IMAGE\_RESULT\_SUCCESS, the encoder is created.
    int32\_t result = OH\_ImagePacker\_Create(env, &packer);
    
3.  Initialize resources.
    
    Call **OH\_ImagePacker\_InitNative** to initialize the encoder instance.
    
    // Initialize the instance through napi\_env and the created encoder instance.
    ImagePacker\_Native\* nativePacker = OH\_ImagePacker\_InitNative(env, packer);
    
4.  Perform encoding.
    
    The following input parameters are provided for the encoding APIs:
    
    -   ImagePacker\_Native instance obtained
        
    -   Image source (napi\_value), PixelMap object, or ImageSource object (when **CreatePixelMap** is not called yet) to be encoded
        
    -   Encoding parameters, including the encoding format and encoding quality
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/hRHfYA7sSOG7jjQF9Weotw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062042Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B18BE5021EE8C55B9EEC5D1AF69C31DF3DAB67B6F65B06E4CB0638716F248697)
        
        According to the MIME protocol, the standard encoding format is image/jpeg. When the APIs provided by the image module are used for encoding, **format** of the encoding parameters must be set to **image/jpeg**. The file name extension of the encoded image file can be .jpg or .jpeg, and the file can be used on platforms that support image/jpeg decoding.
        
    
    The encoding APIs can output data to the buffer (memory) or a file. They have the same input parameters, as described previously.
    
    You can select either of them as required.
    
    Output data to the buffer (memory).
    
    #include <cstdlib>
    #include <multimedia/image\_framework/image\_packer\_mdk.h>
    
    int32\_t packImageToData(napi\_env env, napi\_callback\_info info)
    {
        napi\_value source;
        // Use napi\_value to undertake the created encoder instance.
        napi\_value packer;
        // Use napi\_env to create an encoder. If result is IMAGE\_RESULT\_SUCCESS, the encoder is created.
        int32\_t errorCode = OH\_ImagePacker\_Create(env, &packer);
        if (errorCode != IMAGE\_RESULT\_SUCCESS) {
            return errorCode;
        }
        // Initialize the instance through napi\_env and the created encoder instance.
        ImagePacker\_Native\* nativePacker = OH\_ImagePacker\_InitNative(env, packer);
        // Encoding parameters.
        struct ImagePacker\_Opts\_ opts;
        // (Mandatory) Configure the encoding format.
        opts.format = "image/jpeg";
        // (Mandatory) Configure the encoding quality.
        opts.quality = 95;
        // Set the output buffer size, for example, to 4 KB.
        size\_t bufferSize = 4\*1024;
        // Apply for a buffer for image encoding.
        uint8\_t\* outData = (uint8\_t \*)(malloc(bufferSize));
        if (outData == NULL) {
            errorCode = OH\_ImagePacker\_Release(nativePacker);
            if (errorCode != IMAGE\_RESULT\_SUCCESS) {
                return errorCode;
            } else {
                nativePacker = NULL; // The encoder cannot be destroyed repeatedly.
            }
            return IMAGE\_RESULT\_MALLOC\_ABNORMAL;
        }
        // Start to encode the input source. If IMAGE\_RESULT\_SUCCESS is returned, the encoding is successful. In this case, bufferSize indicates the size of the buffer used for encoding.
        int32\_t result = OH\_ImagePacker\_PackToData(nativePacker, source, &opts, outData, &bufferSize);
        free(outData);
        outData = NULL;
        errorCode = OH\_ImagePacker\_Release(nativePacker);
        if (errorCode != IMAGE\_RESULT\_SUCCESS) {
            return errorCode;
        } else {
            nativePacker = NULL; // The encoder cannot be destroyed repeatedly.
        }
        return result;
    }
    
    Output data to a file.
    
    #include <fcntl.h>
    #include <unistd.h>
    #include <cstdlib>
    #include <multimedia/image\_framework/image\_packer\_mdk.h>
    
    int32\_t packImageToFile(napi\_env env, napi\_callback\_info info)
    {
        napi\_value source;
        // Use napi\_value to undertake the created encoder instance.
        napi\_value packer;
        // Use napi\_env to create an encoder. If result is IMAGE\_RESULT\_SUCCESS, the encoder is created.
        int32\_t errorCode = OH\_ImagePacker\_Create(env, &packer);
        if (errorCode != IMAGE\_RESULT\_SUCCESS) {
            return errorCode;
        }
        // Initialize the instance through napi\_env and the created encoder instance.
        ImagePacker\_Native\* nativePacker = OH\_ImagePacker\_InitNative(env, packer);
        // Encoding parameters.
        struct ImagePacker\_Opts\_ opts;
        // (Mandatory) Configure the encoding format.
        opts.format = "image/jpeg";
        // (Mandatory) Configure the encoding quality.
        opts.quality = 100;
        // Open the file to which the data will be written. (Ensure that the application has the permission to access the file path.)
        int fd = open("/data/test.jpg", O\_RDWR | O\_CREAT, S\_IRUSR | S\_IWUSR);
        int result;
        if (fd >= 0) {
            // Start to encode the input source. If IMAGE\_RESULT\_SUCCESS is returned, the encoding is successful.
            result = OH\_ImagePacker\_PackToFile(nativePacker, source, &opts, fd);
            // Close the file.
            close(fd);
        }
        errorCode = OH\_ImagePacker\_Release(nativePacker);
        if (errorCode != IMAGE\_RESULT\_SUCCESS) {
            return errorCode;
        } else {
            nativePacker = NULL; // The encoder cannot be destroyed repeatedly.
        }
        return result;
    }
