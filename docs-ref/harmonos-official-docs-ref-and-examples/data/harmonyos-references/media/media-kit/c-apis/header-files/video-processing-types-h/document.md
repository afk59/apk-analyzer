# video\_processing\_types.h

#### Overview

The file declares the video processing types.

**File to include**: <multimedia/video\_processing\_engine/video\_processing\_types.h>

**Library**: libvideo\_processing.so

**System capability**: SystemCapability.Multimedia.VideoProcessingEngine

**Since**: 12

**Related module**: [VideoProcessing](../../modules/videoprocessing/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [VideoProcessing\_ColorSpaceInfo](../../structs/videoprocessing-colorspaceinfo/document.md) | VideoProcessing\_ColorSpaceInfo | Describes the color space information of video processing. |
| [OH\_VideoProcessing](../../structs/oh-videoprocessing/document.md) | OH\_VideoProcessing | 
Describes an object for video processing.

You should define a null pointer for **OH\_VideoProcessing** and use [OH\_VideoProcessing\_Create](../video-processing-h/document.md#oh_videoprocessing_create) to create a video processing instance. Before creation, ensure that the pointer is null. You can create different video processing instances with different processing types.

 |
| [NativeWindow](../../structs/nativewindow/document.md) | OHNativeWindow | Describes the NativeWindow object. |
| [OH\_AVFormat](../../structs/oh-avformat/document.md) | OH\_AVFormat | Describes the OH\_AVFormat object. |
| [VideoProcessing\_Callback](../../structs/videoprocessing-callback/document.md) | VideoProcessing\_Callback | 

Describes a callback object for handling video processing events.

You should define a null pointer for **VideoProcessing\_Callback** and use [OH\_VideoProcessingCallback\_Create](../video-processing-h/document.md#oh_videoprocessingcallback_create) to create a callback object. Before creation, ensure that the pointer is null. After creating the callback object, call [OH\_VideoProcessing\_RegisterCallback](../video-processing-h/document.md#oh_videoprocessing_registercallback) to register it with the video processing instance.

 |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [VideoDetailEnhancer\_QualityLevel](#videodetailenhancer_qualitylevel) | VideoDetailEnhancer\_QualityLevel | Enumerates the quality levels for detail enhancement. |
| [VideoMetadataGeneratorStyleControl](#videometadatageneratorstylecontrol) | VideoMetadataGeneratorStyleControl | Enumerates the style modes available for video metadata generation. For details about the enumerated values, see [VIDEO\_METADATA\_GENERATOR\_STYLE\_CONTROL](#variables). |
| [VideoProcessing\_ErrorCode](#videoprocessing_errorcode) | VideoProcessing\_ErrorCode | Enumerates the video processing error codes. |
| [VideoProcessing\_State](#videoprocessing_state) | VideoProcessing\_State | 
Enumerates the video processing states.

The video processing state is reported through the callback function [OH\_VideoProcessingCallback\_OnState](#oh_videoprocessingcallback_onstate).

 |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_VideoProcessingCallback\_OnError)(OH\_VideoProcessing\* videoProcessor, VideoProcessing\_ErrorCode error, void\* userData)](#oh_videoprocessingcallback_onerror) | OH\_VideoProcessingCallback\_OnError | 
Called when an error occurs during video processing.

The following error codes defined in [VideoProcessing\_ErrorCode](#videoprocessing_errorcode) area available:

**VIDEO\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING**: unsupported processing. For example, conversion between the color space types for input and output is not supported.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_VALUE**: invalid video property. For example, the video color space is invalid.

**VIDEO\_PROCESSING\_ERROR\_NO\_MEMORY**: out of memory.

**VIDEO\_PROCESSING\_ERROR\_PROCESS\_FAILED**: An error occurs during the processing.

 |
| [typedef void (\*OH\_VideoProcessingCallback\_OnState)(OH\_VideoProcessing\* videoProcessor, VideoProcessing\_State state, void\* userData)](#oh_videoprocessingcallback_onstate) | OH\_VideoProcessingCallback\_OnState | 

Called when the video processing state changes.

After [OH\_VideoProcessing\_Start](../video-processing-h/document.md#oh_videoprocessing_start) is called, the video processing state changes to [VideoProcessing\_State](#videoprocessing_state).VIDEO\_PROCESSING\_STATE\_RUNNING. After [OH\_VideoProcessing\_Stop](../video-processing-h/document.md#oh_videoprocessing_stop) is called, the video processing state changes to [VideoProcessing\_State](#videoprocessing_state).VIDEO\_PROCESSING\_STATE\_STOPPED after all buffers are processed.

 |
| [typedef void (\*OH\_VideoProcessingCallback\_OnNewOutputBuffer)(OH\_VideoProcessing\* videoProcessor, uint32\_t index, void\* userData)](#oh_videoprocessingcallback_onnewoutputbuffer) | OH\_VideoProcessingCallback\_OnNewOutputBuffer | 

Called when the output buffer is filled with data.

After data is filled in each new output buffer, the index of the buffer is reported. Call [OH\_VideoProcessing\_RenderOutputBuffer](../video-processing-h/document.md#oh_videoprocessing_renderoutputbuffer) to process rendering based on the index and output the buffer. If this callback function is not registered, the data filled in the output buffer is not reported. Instead, the data is directly processed, rendered, and output.

 |

#### \[h2\]Variables

| Name | Description |
| :-- | :-- |
| const int32\_t VIDEO\_PROCESSING\_TYPE\_COLOR\_SPACE\_CONVERSION | 
Instance created for color space conversion during video processing.

Call [OH\_VideoProcessing\_Create](../video-processing-h/document.md#oh_videoprocessing_create) to create such an instance for color space conversion. If color space conversion is not supported, [VideoProcessing\_ErrorCode](#videoprocessing_errorcode).VIDEO\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING is returned.

**Since**: 12

 |
| const int32\_t VIDEO\_PROCESSING\_TYPE\_METADATA\_GENERATION | 

Instance created for metadata generation during video processing.

Call [OH\_VideoProcessing\_Create](../video-processing-h/document.md#oh_videoprocessing_create) to create such an instance for metadata generation. If metadata generation is not supported, [VideoProcessing\_ErrorCode](#videoprocessing_errorcode).VIDEO\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING is returned.

**Since**: 12

 |
| const int32\_t VIDEO\_PROCESSING\_TYPE\_DETAIL\_ENHANCER | 

Instance for detail enhancement during video processing.

Call [OH\_VideoProcessing\_Create](../video-processing-h/document.md#oh_videoprocessing_create) to create such an instance for detail enhancement. If detail enhancement is not supported, [VideoProcessing\_ErrorCode](#videoprocessing_errorcode).VIDEO\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING is returned.

**Since**: 12

 |
| const char\* VIDEO\_DETAIL\_ENHANCER\_PARAMETER\_KEY\_QUALITY\_LEVEL | 

Pointer to the quality level of video detail enhancement. For details, see [VideoDetailEnhancer\_QualityLevel](#videodetailenhancer_qualitylevel).

You can call [OH\_VideoProcessing\_SetParameter](../video-processing-h/document.md#oh_videoprocessing_setparameter) to set the quality level,

and call [OH\_VideoProcessing\_GetParameter](../video-processing-h/document.md#oh_videoprocessing_getparameter) to obtain the quality level.

**Since**: 12

 |
| const char \* VIDEO\_METADATA\_GENERATOR\_STYLE\_CONTROL | 

Style mode available for video metadata generation. For details about the enumerated values, see [VideoMetadataGeneratorStyleControl](#videometadatageneratorstylecontrol). Call [OH\_AVFormat\_SetIntValue](../../../../avcodec-kit/c-apis/header-files/native-avformat-h/document.md#oh_avformat_setintvalue) to set the video metadata generation style in the AVFormat parameter. Call [OH\_VideoProcessing\_SetParameter](../video-processing-h/document.md#oh_videoprocessing_setparameter) to configure the current video metadata generation style. Call [OH\_VideoProcessing\_GetParameter](../video-processing-h/document.md#oh_videoprocessing_getparameter) to obtain the current video metadata generation style.

**Since**: 22

 |

#### Enum Description

#### \[h2\]VideoDetailEnhancer\_QualityLevel

enum VideoDetailEnhancer\_QualityLevel

**Description**

Enumerates the quality levels for detail enhancement. For details about the enumerated values, see [VIDEO\_DETAIL\_ENHANCER\_PARAMETER\_KEY\_QUALITY\_LEVEL](#variables). For details about how to set the quality level, see the development guide.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| VIDEO\_DETAIL\_ENHANCER\_QUALITY\_LEVEL\_NONE | No detail enhancement. |
| VIDEO\_DETAIL\_ENHANCER\_QUALITY\_LEVEL\_LOW | Low-quality detail enhancement, which features fast speed. This is the default value. |
| VIDEO\_DETAIL\_ENHANCER\_QUALITY\_LEVEL\_MEDIUM | Medium-quality detail enhancement, which features moderate speed. |
| VIDEO\_DETAIL\_ENHANCER\_QUALITY\_LEVEL\_HIGH | High-quality detail enhancement, which features slow speed. |

**See also**

[OH\_VideoProcessing\_SetParameter](../video-processing-h/document.md#oh_videoprocessing_setparameter)

[OH\_VideoProcessing\_GetParameter](../video-processing-h/document.md#oh_videoprocessing_getparameter)

#### \[h2\]VideoMetadataGeneratorStyleControl

enum VideoMetadataGeneratorStyleControl

**Description**

Enumerates the style modes available for video metadata generation. For details about the enumerated values, see [VIDEO\_METADATA\_GENERATOR\_STYLE\_CONTROL](#variables).

**Since**: 22

| Enum Item | Description |
| :-- | :-- |
| VIDEO\_METADATA\_GENERATOR\_CONTRAST\_MODE = 0 | Prioritizes contrast optimization in the generated metadata. |
| VIDEO\_METADATA\_GENERATOR\_BRIGHT\_MODE = 1 | Prioritizes brightness optimization in the generated metadata. |

**See also**

[OH\_VideoProcessing\_SetParameter](../video-processing-h/document.md#oh_videoprocessing_setparameter)

[OH\_VideoProcessing\_GetParameter](../video-processing-h/document.md#oh_videoprocessing_getparameter)

[OH\_AVFormat\_SetIntValue](../../../../avcodec-kit/c-apis/header-files/native-avformat-h/document.md#oh_avformat_setintvalue)

#### \[h2\]VideoProcessing\_ErrorCode

enum VideoProcessing\_ErrorCode

**Description**

Enumerates the video processing error codes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| VIDEO\_PROCESSING\_SUCCESS | The processing is successful. |
| VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER = 401 | 
An input parameter is invalid. This error code is returned in the following cases:

1\. The input or output video buffer is either invalid or empty.

2\. The provided parameter is invalid or missing.

3\. The requested processing type is invalid.

 |
| VIDEO\_PROCESSING\_ERROR\_UNKNOWN = 29210001 | An unknown error occurs. For example, the GPU computing or memcpy fails. |
| VIDEO\_PROCESSING\_ERROR\_INITIALIZE\_FAILED | The global video processing environment, for example, the GPU environment, fails to be initialized. |
| VIDEO\_PROCESSING\_ERROR\_CREATE\_FAILED | Creating the video processing instance fails. For example, the total number of instances exceeds the upper limit. |
| VIDEO\_PROCESSING\_ERROR\_PROCESS\_FAILED | The processing fails. For example, the processing times out. |
| VIDEO\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING | The processing type is not supported. You can call **OH\_VideoProcessing\_IsXXXSupported** to check whether a specific processing type is supported. |
| VIDEO\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED | The operation is not allowed. For example, the function is called in an incorrect running state. |
| VIDEO\_PROCESSING\_ERROR\_NO\_MEMORY | Insufficient memory. |
| VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE | The video processing instance is invalid, for example, a null instance. |
| VIDEO\_PROCESSING\_ERROR\_INVALID\_VALUE | 

The input value is invalid. This error code is returned in the following cases:

1\. The width and height of the video buffer are inappropriate or the color space is incorrect.

2\. The parameter contains an invalid value. For example, the quality level of detail enhancement is incorrect.

 |

#### \[h2\]VideoProcessing\_State

enum VideoProcessing\_State

**Description**

Enumerates the video processing states. The video processing state is reported through the callback function [OH\_VideoProcessingCallback\_OnState](#oh_videoprocessingcallback_onstate).

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| VIDEO\_PROCESSING\_STATE\_RUNNING | Video processing is in progress. |
| VIDEO\_PROCESSING\_STATE\_STOPPED | Video processing stopped. |

#### Function Description

#### \[h2\]OH\_VideoProcessingCallback\_OnError()

typedef void (\*OH\_VideoProcessingCallback\_OnError)(OH\_VideoProcessing\* videoProcessor, VideoProcessing\_ErrorCode error, void\* userData)

**Description**

Called when an error occurs during video processing.

The following error codes are defined in [VideoProcessing\_ErrorCode](#videoprocessing_errorcode):

**VIDEO\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING**: unsupported processing. For example, conversion between the color space types for input and output is not supported.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_VALUE**: invalid video property. For example, the video color space is invalid.

**VIDEO\_PROCESSING\_ERROR\_NO\_MEMORY**: out of memory.

**VIDEO\_PROCESSING\_ERROR\_PROCESS\_FAILED**: An error occurs during the processing.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_VideoProcessing](../../structs/oh-videoprocessing/document.md)\* videoProcessor | Pointer to the video processing instance. |
| [VideoProcessing\_ErrorCode](#videoprocessing_errorcode) error | Error code reported. |
| void\* userData | Pointer to user-defined data. |

#### \[h2\]OH\_VideoProcessingCallback\_OnState()

typedef void (\*OH\_VideoProcessingCallback\_OnState)(OH\_VideoProcessing\* videoProcessor, VideoProcessing\_State state, void\* userData)

**Description**

Called when the video processing state changes.

After [OH\_VideoProcessing\_Start](../video-processing-h/document.md#oh_videoprocessing_start) is called, the video processing state changes to [VideoProcessing\_State](#videoprocessing_state).VIDEO\_PROCESSING\_STATE\_RUNNING. After [OH\_VideoProcessing\_Stop](../video-processing-h/document.md#oh_videoprocessing_stop) is called, the video processing state changes to [VideoProcessing\_State](#videoprocessing_state).VIDEO\_PROCESSING\_STATE\_STOPPED after all buffers are processed.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_VideoProcessing](../../structs/oh-videoprocessing/document.md)\* videoProcessor | Pointer to the video processing instance. |
| [VideoProcessing\_State](#videoprocessing_state) state | Video processing state. |
| void\* userData | Pointer to user-defined data. |

#### \[h2\]OH\_VideoProcessingCallback\_OnNewOutputBuffer()

typedef void (\*OH\_VideoProcessingCallback\_OnNewOutputBuffer)(OH\_VideoProcessing\* videoProcessor, uint32\_t index, void\* userData)

**Description**

Called when the output buffer is filled with data.

After data is filled in each new output buffer, the index of the buffer is reported. Call [OH\_VideoProcessing\_RenderOutputBuffer](../video-processing-h/document.md#oh_videoprocessing_renderoutputbuffer) to process rendering based on the index and output the buffer. If this callback function is not registered, the data filled in the output buffer is not reported. Instead, the data is directly processed, rendered, and output.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_VideoProcessing](../../structs/oh-videoprocessing/document.md)\* videoProcessor | Pointer to the video processing instance. |
| uint32\_t index | Index of the output buffer. |
| void\* userData | Pointer to user-defined data. |
