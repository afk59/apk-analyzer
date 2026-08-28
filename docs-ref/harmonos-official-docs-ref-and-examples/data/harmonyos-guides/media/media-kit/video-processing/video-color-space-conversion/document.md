# Video Color Space Conversion

With the [C APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-videoprocessing) provided by the VideoProcessing module, you can implement Color Space Conversions (CSCs) of HDR2SDR, HDR2HDR, and SDR2SDR.

A typical usage scenario is video editing and sharing.

-   **Video editing**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/T5pIpw9iT8eGcmsa8NCMew/en-us_image_0000002498405686.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E6B00B63FB9A24319373845473A9F046BDBD1B600B6514051FE56964C5E4B8A3 "Click to enlarge")
    
-   **Video sharing**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/hKzti2L4TtKXTjrelb76_w/en-us_image_0000002498565670.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C31DB7FFB84A043A46D15044FC64085B5242D0615DFBB2C4626484C91343298F "Click to enlarge")
    

#### Specifications

When the video CSC algorithm is SDR2SDR, the supported format combinations are as follows:

-   Format combination 1
    
    | 
    **Parameter**
    
     | 
    
    **Input**
    
     | 
    
    **Output**
    
     |
    | :-- | :-- | :-- |
    | 
    
    [ColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_colorspace)
    
     | 
    
    OH\_COLORSPACE\_BT601\_EBU\_LIMIT
    
     | 
    
    OH\_COLORSPACE\_BT709\_LIMIT
    
     |
    | 
    
    [MetadataType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_metadatatype)
    
     | 
    
    OH\_VIDEO\_NONE
    
     | 
    
    OH\_VIDEO\_NONE
    
     |
    | 
    
    [pixelFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-buffer-h#oh_nativebuffer_format)
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888
    
     |
    
-   Format combination 2
    
    | 
    **Parameter**
    
     | 
    
    **Input**
    
     | 
    
    **Output**
    
     |
    | :-- | :-- | :-- |
    | 
    
    [ColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_colorspace)
    
     | 
    
    OH\_COLORSPACE\_BT601\_SMPTE\_C\_LIMIT
    
     | 
    
    OH\_COLORSPACE\_BT709\_LIMIT
    
     |
    | 
    
    [MetadataType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_metadatatype)
    
     | 
    
    OH\_VIDEO\_NONE
    
     | 
    
    OH\_VIDEO\_NONE
    
     |
    | 
    
    [pixelFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-buffer-h#oh_nativebuffer_format)
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888
    
     |
    

When the video CSC algorithm is HDR2SDR, the supported format combinations are as follows:

-   Format combination 1
    
    | 
    **Parameter**
    
     | 
    
    **Input**
    
     | 
    
    **Output**
    
     |
    | :-- | :-- | :-- |
    | 
    
    [ColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_colorspace)
    
     | 
    
    OH\_COLORSPACE\_BT2020\_PQ\_LIMIT
    
     | 
    
    OH\_COLORSPACE\_BT709\_LIMIT
    
     |
    | 
    
    [MetadataType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_metadatatype)
    
     | 
    
    OH\_VIDEO\_HDR\_VIVID
    
     | 
    
    OH\_VIDEO\_NONE
    
     |
    | 
    
    [pixelFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-buffer-h#oh_nativebuffer_format)
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_888
    
     |
    
-   Format combination 2
    
    | 
    **Parameter**
    
     | 
    
    **Input**
    
     | 
    
    **Output**
    
     |
    | :-- | :-- | :-- |
    | 
    
    [ColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_colorspace)
    
     | 
    
    OH\_COLORSPACE\_BT2020\_HLG\_LIMIT
    
     | 
    
    OH\_COLORSPACE\_BT709\_LIMIT
    
     |
    | 
    
    [MetadataType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_metadatatype)
    
     | 
    
    OH\_VIDEO\_HDR\_VIVID
    
     | 
    
    OH\_VIDEO\_NONE
    
     |
    | 
    
    [pixelFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-buffer-h#oh_nativebuffer_format)
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888
    
     |
    
-   Format combination 3
    
    | 
    **Parameter**
    
     | 
    
    **Input**
    
     | 
    
    **Output**
    
     |
    | :-- | :-- | :-- |
    | 
    
    [ColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_colorspace)
    
     | 
    
    OH\_COLORSPACE\_BT2020\_HLG\_FULL
    
     | 
    
    OH\_COLORSPACE\_BT709\_LIMIT
    
     |
    | 
    
    [MetadataType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_metadatatype)
    
     | 
    
    OH\_VIDEO\_HDR\_VIVID
    
     | 
    
    OH\_VIDEO\_NONE
    
     |
    | 
    
    [pixelFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-buffer-h#oh_nativebuffer_format)
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888
    
     |
    
-   Format combination 4
    
    | 
    **Parameter**
    
     | 
    
    **Input**
    
     | 
    
    **Output**
    
     |
    | :-- | :-- | :-- |
    | 
    
    [ColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_colorspace)
    
     | 
    
    OH\_COLORSPACE\_BT2020\_HLG\_FULL
    
     | 
    
    OH\_COLORSPACE\_P3\_FULL
    
     |
    | 
    
    [MetadataType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_metadatatype)
    
     | 
    
    OH\_VIDEO\_HDR\_VIVID
    
     | 
    
    OH\_VIDEO\_NONE
    
     |
    | 
    
    [pixelFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-buffer-h#oh_nativebuffer_format)
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888
    
     |
    

When the video CSC algorithm is HDR2HDR, the supported format combinations are as follows:

-   Format combination 1
    
    | 
    **Parameter**
    
     | 
    
    **Input**
    
     | 
    
    **Output**
    
     |
    | :-- | :-- | :-- |
    | 
    
    [ColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_colorspace)
    
     | 
    
    OH\_COLORSPACE\_BT2020\_PQ\_LIMIT
    
     | 
    
    OH\_COLORSPACE\_BT2020\_HLG\_LIMIT
    
     |
    | 
    
    [MetadataType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_metadatatype)
    
     | 
    
    OH\_VIDEO\_HDR\_VIVID
    
     | 
    
    OH\_VIDEO\_HDR\_VIVID
    
     |
    | 
    
    [pixelFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-buffer-h#oh_nativebuffer_format)
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102
    
     |
    
-   Format combination 2
    
    | 
    **Parameter**
    
     | 
    
    **Input**
    
     | 
    
    **Output**
    
     |
    | :-- | :-- | :-- |
    | 
    
    [ColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_colorspace)
    
     | 
    
    OH\_COLORSPACE\_BT2020\_PQ\_LIMIT
    
     | 
    
    OH\_COLORSPACE\_BT2020\_HLG\_LIMIT
    
     |
    | 
    
    [MetadataType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_metadatatype)
    
     | 
    
    OH\_VIDEO\_HDR\_HDR10
    
     | 
    
    OH\_VIDEO\_HDR\_HLG
    
     |
    | 
    
    [pixelFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-buffer-h#oh_nativebuffer_format)
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102
    
     |
    
-   Format combination 3
    
    | 
    **Parameter**
    
     | 
    
    **Input**
    
     | 
    
    **Output**
    
     |
    | :-- | :-- | :-- |
    | 
    
    [ColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_colorspace)
    
     | 
    
    OH\_COLORSPACE\_BT2020\_PQ\_LIMIT
    
     | 
    
    OH\_COLORSPACE\_BT2020\_HLG\_LIMIT
    
     |
    | 
    
    [MetadataType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_metadatatype)
    
     | 
    
    OH\_VIDEO\_HDR\_VIVID
    
     | 
    
    OH\_VIDEO\_HDR\_HLG
    
     |
    | 
    
    [pixelFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-buffer-h#oh_nativebuffer_format)
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102
    
     |
    
-   Format combination 4
    
    | 
    **Parameter**
    
     | 
    
    **Input**
    
     | 
    
    **Output**
    
     |
    | :-- | :-- | :-- |
    | 
    
    [ColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_colorspace)
    
     | 
    
    OH\_COLORSPACE\_BT2020\_HLG\_LIMIT
    
     | 
    
    OH\_COLORSPACE\_BT2020\_PQ\_LIMIT
    
     |
    | 
    
    [MetadataType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_metadatatype)
    
     | 
    
    OH\_VIDEO\_HDR\_VIVID
    
     | 
    
    OH\_VIDEO\_HDR\_VIVID
    
     |
    | 
    
    [pixelFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-buffer-h#oh_nativebuffer_format)
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102
    
     | 
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,
    
    NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102
    
     |
    

**Supported resolution specifications**

| 
Minimum Resolution (Unit: Pixel)

 | 

Maximum Resolution (Unit: Pixel)

 |
| :-- | :-- |
| 

32\*32

 | 

8192\*8192

 |

#### Constraints

1.  To ensure the conversion efficiency, you are advised to carry out a maximum of five conversion tasks concurrently.
2.  Do not directly call video processing APIs or perform other time-consuming operations in the video processing callback function. Instead, call them in the thread of the application.

#### Development Guidelines

For details, see [sample code](https://gitcode.com/HarmonyOS_Samples/VideoProcessing).

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libvideo\_processing.so)

## How to Develop

1.  Add the header files.
    
    #include <multimedia/video\_processing\_engine/video\_processing.h>
    #include <multimedia/video\_processing\_engine/video\_processing\_types.h>
    #include <native\_window/external\_window.h>
    #include <native\_buffer/native\_buffer.h>
    #include <ace/xcomponent/native\_interface\_xcomponent.h>
    
2.  (Optional) Initialize the environment.
    
    This is usually executed on the initial use within a process to preemptively handle certain time-consuming operations.
    
    OH\_VideoProcessing\_InitializeEnvironment();
    
3.  (Optional) Check for capability support. Perform this operation before using the corresponding capability.
    
    // Input and output formats.
    VideoProcessing\_ColorSpaceInfo inputFormat;
    VideoProcessing\_ColorSpaceInfo outputFormat;
    inputFormat.metadataType = OH\_VIDEO\_HDR\_HDR10;
    inputFormat.colorSpace = OH\_COLORSPACE\_BT2020\_PQ\_LIMIT;
    inputFormat.pixelFormat = NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010;
    outputFormat.metadataType = OH\_VIDEO\_HDR\_HLG;
    outputFormat.colorSpace = OH\_COLORSPACE\_BT2020\_HLG\_LIMIT;
    outputFormat.pixelFormat = NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010;
    
    // Capability query.
    bool isSupport = OH\_VideoProcessing\_IsColorSpaceConversionSupported(&inputFormat, &outputFormat);
    
4.  Create a CSC module.
    
    The application may create a CSC module by using a video processing engine type. In the code snippet below, the following variables are used:
    
    -   **videoProcessor**: CSC module instance.
    -   **VIDEO\_PROCESSING\_TYPE\_COLOR\_SPACE\_CONVERSION**: CSC type
    -   **VIDEO\_PROCESSING\_SUCCESS**: expected return value.
    
    // Create a CSC module instance by specifying the video processing engine type.
    OH\_VideoProcessing\* videoProcessor = nullptr;
    VideoProcessing\_ErrorCode ret = OH\_VideoProcessing\_Create(&videoProcessor, VIDEO\_PROCESSING\_TYPE\_COLOR\_SPACE\_CONVERSION);
    
5.  Configure the asynchronous callback function.
    
    // Declare the callback function (userData is the user data passed during callback registration, for example, this pointer.)
    void OnError(OH\_VideoProcessing\* videoProcessor, VideoProcessing\_ErrorCode error, void\* userData);
    void OnState(OH\_VideoProcessing\* videoProcessor, VideoProcessing\_State state, void\* userData);
    void OnNewOutputBuffer(OH\_VideoProcessing\* videoProcessor, uint32\_t index, void\* userData);
    
    // Create a callback instance.
    VideoProcessing\_Callback\* callback = nullptr;
    ret = OH\_VideoProcessingCallback\_Create(&callback);
    // Bind the callback function.
    OH\_VideoProcessingCallback\_BindOnError(callback, OnError);
    OH\_VideoProcessingCallback\_BindOnState(callback, OnState);
    OH\_VideoProcessingCallback\_BindOnNewOutputBuffer(callback, OnNewOutputBuffer);
    // Register the callback function.
    ret = OH\_VideoProcessing\_RegisterCallback(videoProcessor, callback, this);
    
6.  Obtain a surface.
    
    // Obtain an input surface.
    OHNativeWindow \*inWindow = nullptr;
    ret = OH\_VideoProcessing\_GetSurface(videoProcessor, &inWindow);
    
7.  Set the surface.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/lKG-wlpHRQyD6v0HA45uKQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=782D0230CD0646756B62E73ECF902B11320210638F37A1F27B2AECF2F844327A)
    
    You can obtain an **OHNativeWindow** instance from the **XComponent**. For details, see [Native Window Development](../../../../graphics/arkgraphics-2d/native-window-development-c-c/document.md).
    
    **windowOut** in **SetSurface** of the video processing engine is obtained from the [OnSurfaceCreatedCB](../../../../graphics/arkgraphics-2d/native-window-development-c-c/document.md) callback function of the **XComponent**. Parameters such as the metadata type, data format, and color space need to be set for **windowOut**.
    
    // Set the metadata type, data format, and color space.
    uint8\_t metadataType = OH\_VIDEO\_HDR\_HLG;
    OH\_NativeWindow\_SetMetadataValue(windowOut, OH\_HDR\_METADATA\_TYPE, sizeof(uint8\_t), 
    (uint8\_t \*)&metadataType);
    OH\_NativeBuffer\_Format format = NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010;
    OH\_NativeWindow\_NativeWindowHandleOpt(windowOut, SET\_FORMAT, format);
    OH\_NativeBuffer\_ColorSpace colorSpace = OH\_COLORSPACE\_BT2020\_HLG\_LIMIT;
    OH\_NativeWindow\_SetColorSpace(windowOut, colorSpace);
    // Set the output surface.
    VideoProcessing\_ErrorCode ret = OH\_VideoProcessing\_SetSurface(videoProcessor, windowOut);
    
8.  Call [OH\_VideoProcessing\_Start()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_start) to start CSC.
    
    // Start CSC.
    ret = OH\_VideoProcessing\_Start(videoProcessor);
    
9.  Call [OH\_VideoProcessing\_Stop()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_stop) to stop CSC.
    
    // Stop CSC.
    ret = OH\_VideoProcessing\_Stop(videoProcessor);
    
10.  Release the video processing instance.
     
     OH\_VideoProcessingCallback\_Destroy(callback);
     callback = nullptr;
     OH\_VideoProcessing\_Destroy(videoProcessor);
     videoProcessor = nullptr;
     
11.  Release the video processing resources.
     
     OH\_VideoProcessing\_DeinitializeEnvironment();
