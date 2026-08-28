# video\_output.h

#### Overview

The file declares the video output concepts.

**File to include**: <ohcamera/video\_output.h>

**Library**: libohcamera.so

**System capability**: SystemCapability.Multimedia.Camera.Core

**Since**: 11

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [VideoOutput\_Callbacks](../../structs/videooutput-callbacks/document.md) | VideoOutput\_Callbacks | Describes the callbacks related to video output. |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md) | Camera\_VideoOutput | 
Describes the video output object.

You can use [OH\_CameraManager\_CreateVideoOutput](../camera-manager-h/document.md#oh_cameramanager_createvideooutput) to create such an object.

 |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_VideoOutput\_OnFrameStart)(Camera\_VideoOutput\* videoOutput)](#oh_videooutput_onframestart) | OH\_VideoOutput\_OnFrameStart | Defines the callback defined in the [VideoOutput\_Callbacks](../../structs/videooutput-callbacks/document.md) struct and used to report video output frame start events. |
| [typedef void (\*OH\_VideoOutput\_OnFrameEnd)(Camera\_VideoOutput\* videoOutput, int32\_t frameCount)](#oh_videooutput_onframeend) | OH\_VideoOutput\_OnFrameEnd | Defines the callback defined in the [VideoOutput\_Callbacks](../../structs/videooutput-callbacks/document.md) struct and used to report video output frame end events. |
| [typedef void (\*OH\_VideoOutput\_OnError)(Camera\_VideoOutput\* videoOutput, Camera\_ErrorCode errorCode)](#oh_videooutput_onerror) | OH\_VideoOutput\_OnError | Defines the callback defined in the [VideoOutput\_Callbacks](../../structs/videooutput-callbacks/document.md) struct and used to report video output errors. |
| [Camera\_ErrorCode OH\_VideoOutput\_RegisterCallback(Camera\_VideoOutput\* videoOutput, VideoOutput\_Callbacks\* callback)](#oh_videooutput_registercallback) | \- | Registers a callback to listen for video output events. |
| [Camera\_ErrorCode OH\_VideoOutput\_UnregisterCallback(Camera\_VideoOutput\* videoOutput, VideoOutput\_Callbacks\* callback)](#oh_videooutput_unregistercallback) | \- | Unregisters the callback used to listen for video output events. |
| [Camera\_ErrorCode OH\_VideoOutput\_Start(Camera\_VideoOutput\* videoOutput)](#oh_videooutput_start) | \- | Starts video output. |
| [Camera\_ErrorCode OH\_VideoOutput\_Stop(Camera\_VideoOutput\* videoOutput)](#oh_videooutput_stop) | \- | Stops video output. |
| [Camera\_ErrorCode OH\_VideoOutput\_Release(Camera\_VideoOutput\* videoOutput)](#oh_videooutput_release) | \- | Releases a VideoOutput instance. |
| [Camera\_ErrorCode OH\_VideoOutput\_GetActiveProfile(Camera\_VideoOutput\* videoOutput, Camera\_VideoProfile\*\* profile)](#oh_videooutput_getactiveprofile) | \- | Obtains the profile of a VideoOutput instance. |
| [Camera\_ErrorCode OH\_VideoOutput\_DeleteProfile(Camera\_VideoProfile\* profile)](#oh_videooutput_deleteprofile) | \- | Deletes the profile of a VideoOutput instance. |
| [Camera\_ErrorCode OH\_VideoOutput\_IsMirrorSupported(Camera\_VideoOutput\* videoOutput, bool\* isSupported)](#oh_videooutput_ismirrorsupported) | \- | Checks whether a video output supports mirror mode. |
| [Camera\_ErrorCode OH\_VideoOutput\_EnableMirror(Camera\_VideoOutput\* videoOutput, bool mirrorMode)](#oh_videooutput_enablemirror) | \- | Enables or disables mirror mode for a video output. |
| [Camera\_ErrorCode OH\_VideoOutput\_GetVideoRotation(Camera\_VideoOutput\* videoOutput, int deviceDegree, Camera\_ImageRotation\* imageRotation)](#oh_videooutput_getvideorotation) | \- | Obtains the rotation angle of a video output. |
| [Camera\_ErrorCode OH\_VideoOutput\_GetSupportedFrameRates(Camera\_VideoOutput\* videoOutput, Camera\_FrameRateRange\*\* frameRateRange, uint32\_t\* size)](#oh_videooutput_getsupportedframerates) | \- | Obtains the list of frame rates supported by a VideoOutput instance. |
| [Camera\_ErrorCode OH\_VideoOutput\_DeleteFrameRates(Camera\_VideoOutput\* videoOutput, Camera\_FrameRateRange\* frameRateRange)](#oh_videooutput_deleteframerates) | \- | Deletes the frame rate list. |
| [Camera\_ErrorCode OH\_VideoOutput\_SetFrameRate(Camera\_VideoOutput\* videoOutput,int32\_t minFps, int32\_t maxFps)](#oh_videooutput_setframerate) | \- | Sets the frame rates for a VideoOutput instance. |
| [Camera\_ErrorCode OH\_VideoOutput\_GetActiveFrameRate(Camera\_VideoOutput\* videoOutput, Camera\_FrameRateRange\* frameRateRange)](#oh_videooutput_getactiveframerate) | \- | Obtains the active frame rates of a VideoOutput instance. |

#### Function Description

#### \[h2\]OH\_VideoOutput\_OnFrameStart()

typedef void (\*OH\_VideoOutput\_OnFrameStart)(Camera\_VideoOutput\* videoOutput)

**Description**

Defines the callback defined in the [VideoOutput\_Callbacks](../../structs/videooutput-callbacks/document.md) struct and used to report video output frame start events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the VideoOutput instance that transfers the callback. |

#### \[h2\]OH\_VideoOutput\_OnFrameEnd()

typedef void (\*OH\_VideoOutput\_OnFrameEnd)(Camera\_VideoOutput\* videoOutput, int32\_t frameCount)

**Description**

Defines the callback defined in the [VideoOutput\_Callbacks](../../structs/videooutput-callbacks/document.md) struct and used to report video output frame end events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the VideoOutput instance that transfers the callback. |
| int32\_t frameCount | Number of frames to be included in the callback. |

#### \[h2\]OH\_VideoOutput\_OnError()

typedef void (\*OH\_VideoOutput\_OnError)(Camera\_VideoOutput\* videoOutput, Camera\_ErrorCode errorCode)

**Description**

Defines the callback defined in the [VideoOutput\_Callbacks](../../structs/videooutput-callbacks/document.md) struct and used to report video output errors.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the VideoOutput instance that transfers the callback. |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) errorCode | Error code reported during video output. |

**See also**

[CAMERA\_SERVICE\_FATAL\_ERROR](../camera-h/document.md#camera_errorcode)

#### \[h2\]OH\_VideoOutput\_RegisterCallback()

Camera\_ErrorCode OH\_VideoOutput\_RegisterCallback(Camera\_VideoOutput\* videoOutput, VideoOutput\_Callbacks\* callback)

**Description**

Registers a callback to listen for video output events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the target VideoOutput instance. |
| [VideoOutput\_Callbacks](../../structs/videooutput-callbacks/document.md)\* callback | Pointer to the target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_VideoOutput\_UnregisterCallback()

Camera\_ErrorCode OH\_VideoOutput\_UnregisterCallback(Camera\_VideoOutput\* videoOutput, VideoOutput\_Callbacks\* callback)

**Description**

Unregisters the callback used to listen for video output events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the target VideoOutput instance. |
| [VideoOutput\_Callbacks](../../structs/videooutput-callbacks/document.md)\* callback | Pointer to the target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_VideoOutput\_Start()

Camera\_ErrorCode OH\_VideoOutput\_Start(Camera\_VideoOutput\* videoOutput)

**Description**

Starts video output.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the VideoOutput instance to start. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_VideoOutput\_Stop()

Camera\_ErrorCode OH\_VideoOutput\_Stop(Camera\_VideoOutput\* videoOutput)

**Description**

Stops video output.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the VideoOutput instance to stop. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_VideoOutput\_Release()

Camera\_ErrorCode OH\_VideoOutput\_Release(Camera\_VideoOutput\* videoOutput)

**Description**

Releases a VideoOutput instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the VideoOutput instance to release. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_VideoOutput\_GetActiveProfile()

Camera\_ErrorCode OH\_VideoOutput\_GetActiveProfile(Camera\_VideoOutput\* videoOutput, Camera\_VideoProfile\*\* profile)

**Description**

Obtains the profile of a VideoOutput instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the VideoOutput instance for which the profile is to be obtained. |
| [Camera\_VideoProfile](../../structs/camera-videoprofile/document.md)\*\* profile | Double pointer to the video output profile obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_VideoOutput\_DeleteProfile()

Camera\_ErrorCode OH\_VideoOutput\_DeleteProfile(Camera\_VideoProfile\* profile)

**Description**

Deletes the profile of a VideoOutput instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_VideoProfile](../../structs/camera-videoprofile/document.md)\* profile | Pointer to the profile to delete. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_VideoOutput\_IsMirrorSupported()

 Camera\_ErrorCode OH\_VideoOutput\_IsMirrorSupported(Camera\_VideoOutput\* videoOutput, bool\* isSupported)

**Description**

Checks whether a video output supports mirror mode.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the target VideoOutput instance. |
| bool\* isSupported | Pointer to the check result for the support of mirror mode. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_VideoOutput\_EnableMirror()

 Camera\_ErrorCode OH\_VideoOutput\_EnableMirror(Camera\_VideoOutput\* videoOutput, bool mirrorMode)

**Description**

Enables or disables mirror mode for a video output.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the target VideoOutput instance. |
| bool mirrorMode | Whether to enable or disable mirror mode. **true** to enable, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_VideoOutput\_GetVideoRotation()

 Camera\_ErrorCode  OH\_VideoOutput\_GetVideoRotation(Camera\_VideoOutput\* videoOutput, int deviceDegree,Camera\_ImageRotation\* imageRotation)

**Description**

Obtains the rotation angle of a video output.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the target VideoOutput instance. |
| int deviceDegree | Clockwise rotation angle of the device relative to the natural direction (the charging port faces downward). |
| [Camera\_ImageRotation](../camera-h/document.md#camera_imagerotation)\* imageRotation | Pointer to the rotation angle of the video output. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_VideoOutput\_GetSupportedFrameRates()

Camera\_ErrorCode OH\_VideoOutput\_GetSupportedFrameRates(Camera\_VideoOutput\* videoOutput,Camera\_FrameRateRange\*\* frameRateRange, uint32\_t\* size)

**Description**

Obtains the list of frame rates supported by a VideoOutput instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the target VideoOutput instance. |
| [Camera\_FrameRateRange](../../structs/camera-frameraterange/document.md)\*\* frameRateRange | Double pointer to the list of frame rates, if the function is successfully called. |
| uint32\_t\* size | Pointer to the size of the list of frame rates. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_VideoOutput\_DeleteFrameRates()

Camera\_ErrorCode OH\_VideoOutput\_DeleteFrameRates(Camera\_VideoOutput\* videoOutput,Camera\_FrameRateRange\* frameRateRange)

**Description**

Deletes the frame rate list.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the target VideoOutput instance. |
| [Camera\_FrameRateRange](../../structs/camera-frameraterange/document.md)\* frameRateRange | Pointer to the list of frame rates to delete. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_VideoOutput\_SetFrameRate()

Camera\_ErrorCode OH\_VideoOutput\_SetFrameRate(Camera\_VideoOutput\* videoOutput,int32\_t minFps, int32\_t maxFps)

**Description**

Sets the frame rates for a VideoOutput instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the VideoOutput instance for which the frame rates are to be set. |
| int32\_t minFps | Minimum frame rate. |
| int32\_t maxFps | Maximum frame rate. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_VideoOutput\_GetActiveFrameRate()

Camera\_ErrorCode OH\_VideoOutput\_GetActiveFrameRate(Camera\_VideoOutput\* videoOutput,Camera\_FrameRateRange\* frameRateRange)

**Description**

Obtains the active frame rates of a VideoOutput instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the target VideoOutput instance. |
| [Camera\_FrameRateRange](../../structs/camera-frameraterange/document.md)\* frameRateRange | Pointer to the frame rate range, if the function is successfully called. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |
