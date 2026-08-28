# video\_processing.h

#### Overview

The file declares the video processing functions.

It provides video processing capabilities, including color space conversion, metadata generation, and video scaling.

**File to include**: <multimedia/video\_processing\_engine/video\_processing.h>

**Library**: libvideo\_processing.so

**System capability**: SystemCapability.Multimedia.VideoProcessingEngine

**Since**: 12

**Related module**: [VideoProcessing](../../modules/videoprocessing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_InitializeEnvironment(void)](#oh_videoprocessing_initializeenvironment) | 
Initializes the global video processing environment.

This function is optional.

It is called only once when the main process is started to initialize the global video processing environment. This reduces the duration for running [OH\_VideoProcessing\_Create](#oh_videoprocessing_create).

 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_DeinitializeEnvironment(void)](#oh_videoprocessing_deinitializeenvironment) | 

Releases the global video processing environment.

Before calling this API, you must call [OH\_VideoProcessing\_InitializeEnvironment](#oh_videoprocessing_initializeenvironment) to initialize the environment.

Generally, this function is called when the main process is about to exit.

Do not call this function when a video processing instance is running.

 |
| [bool OH\_VideoProcessing\_IsColorSpaceConversionSupported(const VideoProcessing\_ColorSpaceInfo\* sourceVideoInfo, const VideoProcessing\_ColorSpaceInfo\* destinationVideoInfo)](#oh_videoprocessing_iscolorspaceconversionsupported) | Checks whether color space conversion is supported during video processing. |
| [bool OH\_VideoProcessing\_IsMetadataGenerationSupported(const VideoProcessing\_ColorSpaceInfo\* sourceVideoInfo)](#oh_videoprocessing_ismetadatagenerationsupported) | Checks whether metadata generation is supported during video processing. |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_Create(OH\_VideoProcessing\*\* videoProcessor, int type)](#oh_videoprocessing_create) | Creates a video processing instance. |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_Destroy(OH\_VideoProcessing\* videoProcessor)](#oh_videoprocessing_destroy) | 

Destroys a video processing instance.

Before destroying the instance, call [OH\_VideoProcessing\_Stop](#oh_videoprocessing_stop) to stop it.

 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_RegisterCallback(OH\_VideoProcessing\* videoProcessor,const VideoProcessing\_Callback\* callback, void\* userData)](#oh_videoprocessing_registercallback) | 

Registers a callback for video processing.

The callback function should be registered before video processing starts. During video processing, it cannot be registered.

 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_SetSurface(OH\_VideoProcessing\* videoProcessor,const OHNativeWindow\* window)](#oh_videoprocessing_setsurface) | 

Sets an output surface for video processing.

An output surface must be set before video processing starts.

 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_GetSurface(OH\_VideoProcessing\* videoProcessor, OHNativeWindow\*\* window)](#oh_videoprocessing_getsurface) | 

Obtains a surface for video processing.

An input surface must be created before video processing starts, it must be destroyed by calling [OH\_NativeWindow\_DestroyNativeWindow](../../../../../graphics/arkgraphics-2d/c-apis/header-files/external-window-h/document.md#oh_nativewindow_destroynativewindow) when it is no longer needed.

 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_SetParameter(OH\_VideoProcessing\* videoProcessor, const OH\_AVFormat\* parameter)](#oh_videoprocessing_setparameter) | Sets video processing parameters. |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_GetParameter(OH\_VideoProcessing\* videoProcessor, OH\_AVFormat\* parameter)](#oh_videoprocessing_getparameter) | Obtains video processing parameters. |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_Start(OH\_VideoProcessing\* videoProcessor)](#oh_videoprocessing_start) | 

Starts video processing.

After video processing starts, the callback [OH\_VideoProcessingCallback\_OnState](../video-processing-types-h/document.md#oh_videoprocessingcallback_onstate) reports the [VIDEO\_PROCESSING\_STATE\_RUNNING](../video-processing-types-h/document.md#videoprocessing_state) state.

 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_Stop(OH\_VideoProcessing\* videoProcessor)](#oh_videoprocessing_stop) | 

Stops video processing.

After video processing stops, the callback [OH\_VideoProcessingCallback\_OnState](../video-processing-types-h/document.md#oh_videoprocessingcallback_onstate) reports the [VIDEO\_PROCESSING\_STATE\_STOPPED](../video-processing-types-h/document.md#videoprocessing_state) state.

 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_RenderOutputBuffer(OH\_VideoProcessing\* videoProcessor, uint32\_t index)](#oh_videoprocessing_renderoutputbuffer) | 

Renders and processes the buffer, and then outputs it.

If the callback function [OH\_VideoProcessingCallback\_OnNewOutputBuffer](../video-processing-types-h/document.md#oh_videoprocessingcallback_onnewoutputbuffer) is set, the buffer index is returned through the callback function after the output buffer is ready.

 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessingCallback\_Create(VideoProcessing\_Callback\*\* callback)](#oh_videoprocessingcallback_create) | Creates a video processing callback object. |
| [VideoProcessing\_ErrorCode OH\_VideoProcessingCallback\_Destroy(VideoProcessing\_Callback\* callback)](#oh_videoprocessingcallback_destroy) | Destroys a video processing callback object. The video processing callback object can be destroyed after the callback function is registered. |
| [VideoProcessing\_ErrorCode OH\_VideoProcessingCallback\_BindOnError(VideoProcessing\_Callback\* callback,OH\_VideoProcessingCallback\_OnError onError)](#oh_videoprocessingcallback_bindonerror) | Binds the callback function [OH\_VideoProcessingCallback\_OnError](../video-processing-types-h/document.md#oh_videoprocessingcallback_onerror) to a video processing callback object. |
| [VideoProcessing\_ErrorCode OH\_VideoProcessingCallback\_BindOnState(VideoProcessing\_Callback\* callback,OH\_VideoProcessingCallback\_OnState onState)](#oh_videoprocessingcallback_bindonstate) | Binds the callback function [OH\_VideoProcessingCallback\_OnState](../video-processing-types-h/document.md#oh_videoprocessingcallback_onstate) to a video processing callback object. |
| [VideoProcessing\_ErrorCode OH\_VideoProcessingCallback\_BindOnNewOutputBuffer(VideoProcessing\_Callback\* callback,OH\_VideoProcessingCallback\_OnNewOutputBuffer onNewOutputBuffer)](#oh_videoprocessingcallback_bindonnewoutputbuffer) | Binds the callback function [OH\_VideoProcessingCallback\_OnNewOutputBuffer](../video-processing-types-h/document.md#oh_videoprocessingcallback_onnewoutputbuffer) to a video processing callback object. |

#### Function Description

#### \[h2\]OH\_VideoProcessing\_InitializeEnvironment()

VideoProcessing\_ErrorCode OH\_VideoProcessing\_InitializeEnvironment(void)

**Description**

Initializes the global video processing environment.

This function is optional.

It is called only once when the main process is started to initialize the global video processing environment. This reduces the duration for running [OH\_VideoProcessing\_Create](#oh_videoprocessing_create).

The global video processing environment must be released by calling [OH\_VideoProcessing\_DeinitializeEnvironment](#oh_videoprocessing_deinitializeenvironment).

For details about how and when to release the environment, see [OH\_VideoProcessing\_DeinitializeEnvironment](#oh_videoprocessing_deinitializeenvironment).

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode](../video-processing-types-h/document.md#videoprocessing_errorcode) | 
**VIDEO\_PROCESSING\_SUCCESS**: The initialization is successful.

**VIDEO\_PROCESSING\_ERROR\_INITIALIZE\_FAILED**: The initialization fails.

If the operation fails, check whether the GPU works properly.

 |

#### \[h2\]OH\_VideoProcessing\_DeinitializeEnvironment()

VideoProcessing\_ErrorCode OH\_VideoProcessing\_DeinitializeEnvironment(void)

**Description**

Releases the global video processing environment.

Before calling this API, you must call [OH\_VideoProcessing\_InitializeEnvironment](#oh_videoprocessing_initializeenvironment) to initialize the environment.

Generally, this function is called when the main process is about to exit.

Do not call this function when a video processing instance is running.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode](../video-processing-types-h/document.md#videoprocessing_errorcode) | 
**VIDEO\_PROCESSING\_SUCCESS**: The processing is successful.

**VIDEO\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED**: A video processing instance is not destroyed or [OH\_VideoProcessing\_InitializeEnvironment](#oh_videoprocessing_initializeenvironment) is not called to initialize the environment.

 |

#### \[h2\]OH\_VideoProcessing\_IsColorSpaceConversionSupported()

bool OH\_VideoProcessing\_IsColorSpaceConversionSupported(const VideoProcessing\_ColorSpaceInfo\* sourceVideoInfo,const VideoProcessing\_ColorSpaceInfo\* destinationVideoInfo)

**Description**

Checks whether color space conversion is supported during video processing.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [VideoProcessing\_ColorSpaceInfo](../../structs/videoprocessing-colorspaceinfo/document.md)\* sourceVideoInfo | Pointer to the color space information of the input video. |
| const [VideoProcessing\_ColorSpaceInfo](../../structs/videoprocessing-colorspaceinfo/document.md)\* destinationVideoInfo | Pointer to the color space information of the output video. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for the support of color space conversion. **true** if supported, **false** otherwise. |

#### \[h2\]OH\_VideoProcessing\_IsMetadataGenerationSupported()

bool OH\_VideoProcessing\_IsMetadataGenerationSupported(const VideoProcessing\_ColorSpaceInfo\* sourceVideoInfo)

**Description**

Checks whether metadata generation is supported during video processing.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [VideoProcessing\_ColorSpaceInfo](../../structs/videoprocessing-colorspaceinfo/document.md)\* sourceVideoInfo | Pointer to the color space information of the input video. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for the support of metadata generation. **true** if supported, **false** otherwise. |

#### \[h2\]OH\_VideoProcessing\_Create()

VideoProcessing\_ErrorCode OH\_VideoProcessing\_Create(OH\_VideoProcessing\*\* videoProcessor, int type)

**Description**

Creates a video processing instance.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_VideoProcessing](../../structs/oh-videoprocessing/document.md)\*\* videoProcessor | Double pointer to the video processing instance created. Before any input, **\*videoProcessor** must be nullptr. |
| int type | Video processing type. The processing type of an instance cannot be changed. |

**Returns**

| Type | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode](../video-processing-types-h/document.md#videoprocessing_errorcode) | 
**VIDEO\_PROCESSING\_SUCCESS**: The video processing instance is created successfully.

**VIDEO\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING**: The processing type is not supported. For example, metadata generation is not supported.

**VIDEO\_PROCESSING\_ERROR\_CREATE\_FAILED**: The video processing instance fails to be created.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or the pointer to the instance is not null.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: The video processing type is invalid.

 |

#### \[h2\]OH\_VideoProcessing\_Destroy()

VideoProcessing\_ErrorCode OH\_VideoProcessing\_Destroy(OH\_VideoProcessing\* videoProcessor)

**Description**

Destroys a video processing instance.

Before destroying the instance, call [OH\_VideoProcessing\_Stop](#oh_videoprocessing_stop) to stop it.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_VideoProcessing](../../structs/oh-videoprocessing/document.md)\* videoProcessor | Pointer to the video processing instance. You are advised to set the pointer to nullptr after the instance is destroyed. |

**Returns**

| Type | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode](../video-processing-types-h/document.md#videoprocessing_errorcode) | 
**VIDEO\_PROCESSING\_SUCCESS**: The instance is destroyed.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or is not a video processing instance.

**VIDEO\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED**: The instance is still running.

 |

#### \[h2\]OH\_VideoProcessing\_RegisterCallback()

VideoProcessing\_ErrorCode OH\_VideoProcessing\_RegisterCallback(OH\_VideoProcessing\* videoProcessor,const VideoProcessing\_Callback\* callback, void\* userData)

**Description**

Registers a callback for video processing.

The callback function should be registered before video processing starts. During video processing, it cannot be registered.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_VideoProcessing](../../structs/oh-videoprocessing/document.md)\* videoProcessor | Pointer to the video processing instance. |
| const [VideoProcessing\_Callback](../../structs/videoprocessing-callback/document.md)\* callback | Pointer to the callback function. |
| void\* userData | Pointer to user-defined data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode](../video-processing-types-h/document.md#videoprocessing_errorcode) | 
**VIDEO\_PROCESSING\_SUCCESS**: The callback function is registered.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or is not a video processing instance.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: The callback function pointer is null.

**VIDEO\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED**: The instance is still running.

 |

#### \[h2\]OH\_VideoProcessing\_SetSurface()

VideoProcessing\_ErrorCode OH\_VideoProcessing\_SetSurface(OH\_VideoProcessing\* videoProcessor,const OHNativeWindow\* window)

**Description**

Sets an output surface for video processing.

An output surface must be set before video processing starts.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_VideoProcessing](../../structs/oh-videoprocessing/document.md)\* videoProcessor | Pointer to the video processing instance. |
| const [OHNativeWindow](../../structs/nativewindow/document.md)\* window | Pointer to the output surface. |

**Returns**

| Type | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode](../video-processing-types-h/document.md#videoprocessing_errorcode) | 
**VIDEO\_PROCESSING\_SUCCESS**: The output surface is successfully set.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or is not a video processing instance.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: The window is nullptr.

 |

#### \[h2\]OH\_VideoProcessing\_GetSurface()

VideoProcessing\_ErrorCode OH\_VideoProcessing\_GetSurface(OH\_VideoProcessing\* videoProcessor, OHNativeWindow\*\* window)

**Description**

Obtains a surface for video processing.

An input surface must be created before video processing starts, and it must be destroyed by calling [OH\_NativeWindow\_DestroyNativeWindow](../../../../../graphics/arkgraphics-2d/c-apis/header-files/external-window-h/document.md#oh_nativewindow_destroynativewindow) when it is no longer needed.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_VideoProcessing](../../structs/oh-videoprocessing/document.md)\* videoProcessor | Pointer to the video processing instance. |
| [OHNativeWindow](../../structs/nativewindow/document.md)\*\* window | Double pointer to the input surface. For example, the input surface pointer can point to an output surface of the video decoder. |

**Returns**

| Type | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode](../video-processing-types-h/document.md#videoprocessing_errorcode) | 
**VIDEO\_PROCESSING\_SUCCESS**: The processing is successful.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or is not a video processing instance.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: The window is nullptr or the pointer to the window is not null.

**VIDEO\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED**: The surface fails to be created, an input surface has been created, or the video processing instance is running.

 |

#### \[h2\]OH\_VideoProcessing\_SetParameter()

VideoProcessing\_ErrorCode OH\_VideoProcessing\_SetParameter(OH\_VideoProcessing\* videoProcessor,const OH\_AVFormat\* parameter)

**Description**

Sets video processing parameters.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_VideoProcessing](../../structs/oh-videoprocessing/document.md)\* videoProcessor | Pointer to the video processing instance. |
| const [OH\_AVFormat](../../structs/oh-avformat/document.md)\* parameter | Pointer to the video processing parameter instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode](../video-processing-types-h/document.md#videoprocessing_errorcode) | 
**VIDEO\_PROCESSING\_SUCCESS**: The parameters are successfully set.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or is not a video processing instance.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: The parameter is empty.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_VALUE**: Some properties of a parameter are invalid, for example, unsupported parameter value.

**VIDEO\_PROCESSING\_ERROR\_NO\_MEMORY**: Memory allocation fails.

 |

#### \[h2\]OH\_VideoProcessing\_GetParameter()

VideoProcessing\_ErrorCode OH\_VideoProcessing\_GetParameter(OH\_VideoProcessing\* videoProcessor, OH\_AVFormat\* parameter)

**Description**

Obtains video processing parameters.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_VideoProcessing](../../structs/oh-videoprocessing/document.md)\* videoProcessor | Pointer to the video processing instance. |
| [OH\_AVFormat](../../structs/oh-avformat/document.md)\* parameter | Pointer to the video processing parameter instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode](../video-processing-types-h/document.md#videoprocessing_errorcode) | 
**VIDEO\_PROCESSING\_SUCCESS**: The parameters are obtained.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or is not a video processing instance.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: The parameter is empty.

 |

#### \[h2\]OH\_VideoProcessing\_Start()

VideoProcessing\_ErrorCode OH\_VideoProcessing\_Start(OH\_VideoProcessing\* videoProcessor)

**Description**

Starts video processing.

After video processing starts, the callback [OH\_VideoProcessingCallback\_OnState](../video-processing-types-h/document.md#oh_videoprocessingcallback_onstate) reports the [VideoProcessing\_State](../video-processing-types-h/document.md#videoprocessing_state).VIDEO\_PROCESSING\_STATE\_RUNNING state.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_VideoProcessing](../../structs/oh-videoprocessing/document.md)\* videoProcessor | Pointer to the video processing instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode](../video-processing-types-h/document.md#videoprocessing_errorcode) | 
**VIDEO\_PROCESSING\_SUCCESS**: The processing is successful.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or is not a video processing instance.

**VIDEO\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED**: No output surface is set, no input surface is created, or the instance is running.

 |

#### \[h2\]OH\_VideoProcessing\_Stop()

VideoProcessing\_ErrorCode OH\_VideoProcessing\_Stop(OH\_VideoProcessing\* videoProcessor)

**Description**

Stops video processing.

After video processing stops, the callback [OH\_VideoProcessingCallback\_OnState](../video-processing-types-h/document.md#oh_videoprocessingcallback_onstate) reports the [VideoProcessing\_State](../video-processing-types-h/document.md#videoprocessing_state).VIDEO\_PROCESSING\_STATE\_STOPPED state.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_VideoProcessing](../../structs/oh-videoprocessing/document.md)\* videoProcessor | Pointer to the video processing instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode](../video-processing-types-h/document.md#videoprocessing_errorcode) | 
**VIDEO\_PROCESSING\_SUCCESS**: The processing is successful.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or is not a video processing instance.

**VIDEO\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED**: The instance is stopped.

 |

#### \[h2\]OH\_VideoProcessing\_RenderOutputBuffer()

VideoProcessing\_ErrorCode OH\_VideoProcessing\_RenderOutputBuffer(OH\_VideoProcessing\* videoProcessor, uint32\_t index)

**Description**

Renders and processes the buffer, and then outputs it.

If the callback function [OH\_VideoProcessingCallback\_OnNewOutputBuffer](../video-processing-types-h/document.md#oh_videoprocessingcallback_onnewoutputbuffer) is set, the buffer index is returned through the callback function after the output buffer is ready.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_VideoProcessing](../../structs/oh-videoprocessing/document.md)\* videoProcessor | Pointer to the video processing instance. |
| uint32\_t index | Index of the output buffer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode](../video-processing-types-h/document.md#videoprocessing_errorcode) | 
**VIDEO\_PROCESSING\_SUCCESS**: The processing is successful.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or is not a video processing instance.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: The index is invalid.

**VIDEO\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED**: The callback function [OH\_VideoProcessingCallback\_OnNewOutputBuffer](../video-processing-types-h/document.md#oh_videoprocessingcallback_onnewoutputbuffer) is not set or the instance is stopped.

 |

#### \[h2\]OH\_VideoProcessingCallback\_Create()

VideoProcessing\_ErrorCode OH\_VideoProcessingCallback\_Create(VideoProcessing\_Callback\*\* callback)

**Description**

Creates a video processing callback object.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [VideoProcessing\_Callback](../../structs/videoprocessing-callback/document.md)\*\* callback | Double pointer to the video processing callback object. Before creating a callback object, **\*callback** must be nullptr. |

**Returns**

| Type | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode](../video-processing-types-h/document.md#videoprocessing_errorcode) | 
**VIDEO\_PROCESSING\_SUCCESS**: The callback object is created.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: **callback** is null or **callback** is not null.

**VIDEO\_PROCESSING\_ERROR\_NO\_MEMORY**: The memory is insufficient.

 |

#### \[h2\]OH\_VideoProcessingCallback\_Destroy()

VideoProcessing\_ErrorCode OH\_VideoProcessingCallback\_Destroy(VideoProcessing\_Callback\* callback)

**Description**

Destroys a video processing callback object. The video processing callback object can be destroyed after the callback function is registered.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [VideoProcessing\_Callback](../../structs/videoprocessing-callback/document.md)\* callback | Pointer to the callback object. You are advised to set the pointer to nullptr after the callback object is destroyed. |

**Returns**

| Type | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode](../video-processing-types-h/document.md#videoprocessing_errorcode) | 
**VIDEO\_PROCESSING\_SUCCESS**: The callback object is destroyed.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: **callback** is null.

 |

#### \[h2\]OH\_VideoProcessingCallback\_BindOnError()

VideoProcessing\_ErrorCode OH\_VideoProcessingCallback\_BindOnError(VideoProcessing\_Callback\* callback,OH\_VideoProcessingCallback\_OnError onError)

**Description**

Binds the callback function [OH\_VideoProcessingCallback\_OnError](../video-processing-types-h/document.md#oh_videoprocessingcallback_onerror) to a video processing callback object.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [VideoProcessing\_Callback](../../structs/videoprocessing-callback/document.md)\* callback | Pointer to the callback object. |
| [OH\_VideoProcessingCallback\_OnError](../video-processing-types-h/document.md#oh_videoprocessingcallback_onerror) onError | Callback function to bind. |

**Returns**

| Type | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode](../video-processing-types-h/document.md#videoprocessing_errorcode) | 
**VIDEO\_PROCESSING\_SUCCESS**: The binding is successful.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: **callback** or **onError** is null.

 |

#### \[h2\]OH\_VideoProcessingCallback\_BindOnState()

VideoProcessing\_ErrorCode OH\_VideoProcessingCallback\_BindOnState(VideoProcessing\_Callback\* callback,OH\_VideoProcessingCallback\_OnState onState)

**Description**

Binds the callback function [OH\_VideoProcessingCallback\_OnState](../video-processing-types-h/document.md#oh_videoprocessingcallback_onstate) to a video processing callback object.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [VideoProcessing\_Callback](../../structs/videoprocessing-callback/document.md)\* callback | Pointer to the callback object. |
| [OH\_VideoProcessingCallback\_OnState](../video-processing-types-h/document.md#oh_videoprocessingcallback_onstate) onState | Callback function to bind. |

**Returns**

| Type | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode](../video-processing-types-h/document.md#videoprocessing_errorcode) | 
**VIDEO\_PROCESSING\_SUCCESS**: The binding is successful.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: **callback** or **onState** is null.

 |

#### \[h2\]OH\_VideoProcessingCallback\_BindOnNewOutputBuffer()

VideoProcessing\_ErrorCode OH\_VideoProcessingCallback\_BindOnNewOutputBuffer(VideoProcessing\_Callback\* callback,OH\_VideoProcessingCallback\_OnNewOutputBuffer onNewOutputBuffer)

**Description**

Binds the callback function [OH\_VideoProcessingCallback\_OnNewOutputBuffer](../video-processing-types-h/document.md#oh_videoprocessingcallback_onnewoutputbuffer) to a video processing callback object.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [VideoProcessing\_Callback](../../structs/videoprocessing-callback/document.md)\* callback | Pointer to the callback object. |
| [OH\_VideoProcessingCallback\_OnNewOutputBuffer](../video-processing-types-h/document.md#oh_videoprocessingcallback_onnewoutputbuffer) onNewOutputBuffer | Callback function to bind. |

**Returns**

| Type | Description |
| :-- | :-- |
| [VideoProcessing\_ErrorCode](../video-processing-types-h/document.md#videoprocessing_errorcode) | 
**VIDEO\_PROCESSING\_SUCCESS**: The binding is successful.

**VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: **callback** is null.

 |
