# Video Dynamic Metadata Generation

With the [C APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-videoprocessing) provided by the VideoProcessing module, you can generate HDR Vivid dynamic metadata.

A typical usage scenario is video editing, as shown in the figure below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/hDJOITkSRbWTs_LM4VU4rA/en-us_image_0000002530325615.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=250B8F7F43AF22AECA8406D3E7876EEA34742EBC47FEB63A7A5CE5F63359302C "Click to enlarge")

#### Specifications

The following data input format combinations are supported:

-   Format combination 1
    
    | 
    Parameter
    
     | 
    
    Data Input Format
    
     |
    | :-- | :-- |
    | 
    
    [ColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_colorspace)
    
     | 
    
    OH\_COLORSPACE\_BT2020\_PQ\_LIMIT
    
     |
    | 
    
    [MetadataType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_metadatatype)
    
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
    

-   Format combination 2
    
    | 
    Parameter
    
     | 
    
    Data Input Format
    
     |
    | :-- | :-- |
    | 
    
    [ColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_colorspace)
    
     | 
    
    OH\_COLORSPACE\_BT2020\_HLG\_LIMIT
    
     |
    | 
    
    [MetadataType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_metadatatype)
    
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
    
-   Format combination 3
    
    | 
    Parameter
    
     | 
    
    Data Input Format
    
     |
    | :-- | :-- |
    | 
    
    [ColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_colorspace)
    
     | 
    
    OH\_COLORSPACE\_BT2020\_HLG\_LIMIT
    
     |
    | 
    
    [MetadataType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_metadatatype)
    
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
    
-   Format combination 4
    
    | 
    Parameter
    
     | 
    
    Data Input Format
    
     |
    | :-- | :-- |
    | 
    
    [ColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_colorspace)
    
     | 
    
    OH\_COLORSPACE\_BT2020\_PQ\_LIMIT
    
     |
    | 
    
    [MetadataType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_metadatatype)
    
     | 
    
    OH\_VIDEO\_HDR\_HDR10
    
     |
    | 
    
    [pixelFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-buffer-h#oh_nativebuffer_format)
    
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
2.  Only dynamic metadata of the OH\_VIDEO\_HDR\_VIVID type can be generated. After conversion, **metadataType** is changed to OH\_VIDEO\_HDR\_VIVID.
3.  Do not directly call video processing APIs or perform other time-consuming operations in the video processing callback function. Instead, call them in the thread of the application.

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
    #include <multimedia/player\_framework/native\_avformat.h>
    
2.  (Optional) Initialize the environment.
    
    This is usually executed on the initial use within a process to preemptively handle certain time-consuming operations.
    
    OH\_VideoProcessing\_InitializeEnvironment();
    
3.  (Optional) Check for capability support. Perform this operation before using the corresponding capability.
    
    // Input format.
    VideoProcessing\_ColorSpaceInfo videoInfo;
    videoInfo.metadataType = OH\_VIDEO\_HDR\_HDR10;
    videoInfo.colorSpace = OH\_COLORSPACE\_BT2020\_PQ\_LIMIT;
    videoInfo.pixelFormat = NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010;
    
    // Check whether the input format can be converted to the HDR Vivid metadata type.
    bool isSupport = OH\_VideoProcessing\_IsMetadataGenerationSupported(&videoInfo);
    
4.  Create a dynamic metadata generation module.
    
    The application may create a dynamic metadata generation module by using a video processing engine type. In the code snippet below, the following variables are used:
    
    -   **videoProcessor**: dynamic metadata generation module instance.
    -   **VIDEO\_PROCESSING\_TYPE\_METADATA\_GENERATION**: dynamic metadata generation type.
    -   **VIDEO\_PROCESSING\_SUCCESS**: expected return value.
    
    // Create a dynamic metadata generation module instance by specifying the video processing engine type.
    OH\_VideoProcessing\* videoProcessor = nullptr;
    VideoProcessing\_ErrorCode ret = OH\_VideoProcessing\_Create(&videoProcessor, VIDEO\_PROCESSING\_TYPE\_METADATA\_GENERATION);
    
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
    
6.  (Optional) From API version 22, the mode for generating dynamic video metadata can be configured. Currently, two modes are supported: contrast and brightness. If no mode is configured, the contrast mode is used by default.
    
    // Create a format instance.
    OH\_AVFormat\* parameter = OH\_AVFormat\_Create();
    // Specify the brightness mode.
    OH\_AVFormat\_SetIntValue(parameter, VIDEO\_METADATA\_GENERATOR\_STYLE\_CONTROL, VIDEO\_METADATA\_GENERATOR\_BRIGHT\_MODE);
    // Set parameters.
    OH\_VideoProcessing\_SetParameter(videoProcessor, parameter);
    
7.  Obtain a surface.
    
    // Obtain an input surface.
    OHNativeWindow \*inWindow = nullptr;
    ret = OH\_VideoProcessing\_GetSurface(videoProcessor, &inWindow);
    
8.  Set the surface.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/CU4J_CJ5QsapOXk_KE9GAw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C6E00F3004FE40603528DD7239CCBC7E20A31C1350BCE1991C5F796E126CE02)
    
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
    
9.  Call [OH\_VideoProcessing\_Start()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_start) to start dynamic metadata generation.
    
    // Start dynamic metadata generation and conversion.
    ret = OH\_VideoProcessing\_Start(videoProcessor);
    
10.  Call [OH\_VideoProcessing\_Stop()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_stop) to stop dynamic metadata generation.
     
     // Stop dynamic metadata generation.
     ret = OH\_VideoProcessing\_Stop(videoProcessor);
     
11.  Release the video processing instance.
     
     OH\_VideoProcessingCallback\_Destroy(callback);
     callback = nullptr;
     OH\_VideoProcessing\_Destroy(videoProcessor);
     videoProcessor = nullptr;
     
12.  Release the video processing resources.
     
     OH\_VideoProcessing\_DeinitializeEnvironment();
