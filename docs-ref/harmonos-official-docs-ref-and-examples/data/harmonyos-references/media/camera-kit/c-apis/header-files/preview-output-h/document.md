# preview\_output.h

#### Overview

The file declares the preview output concepts.

**File to include**: <ohcamera/preview\_output.h>

**Library**: libohcamera.so

**System capability**: SystemCapability.Multimedia.Camera.Core

**Since**: 11

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [PreviewOutput\_Callbacks](../../structs/previewoutput-callbacks/document.md) | PreviewOutput\_Callbacks | Describes the callbacks related to preview output. |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md) | Camera\_PreviewOutput | 
Describes the preview output object.

You can use [OH\_CameraManager\_CreatePreviewOutput](../camera-manager-h/document.md#oh_cameramanager_createpreviewoutput) to create such an object.

 |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_PreviewOutput\_OnFrameStart)(Camera\_PreviewOutput\* previewOutput)](#oh_previewoutput_onframestart) | OH\_PreviewOutput\_OnFrameStart | Defines the callback defined in the [PreviewOutput\_Callbacks](../../structs/previewoutput-callbacks/document.md) struct and used to report preview output frame start events. |
| [typedef void (\*OH\_PreviewOutput\_OnFrameEnd)(Camera\_PreviewOutput\* previewOutput, int32\_t frameCount)](#oh_previewoutput_onframeend) | OH\_PreviewOutput\_OnFrameEnd | Defines the callback defined in the [PreviewOutput\_Callbacks](../../structs/previewoutput-callbacks/document.md) struct and used to report preview output frame end events. |
| [typedef void (\*OH\_PreviewOutput\_OnError)(Camera\_PreviewOutput\* previewOutput, Camera\_ErrorCode errorCode)](#oh_previewoutput_onerror) | OH\_PreviewOutput\_OnError | Defines the callback defined in the [PreviewOutput\_Callbacks](../../structs/previewoutput-callbacks/document.md) struct and used to report preview output errors. |
| [Camera\_ErrorCode OH\_PreviewOutput\_RegisterCallback(Camera\_PreviewOutput\* previewOutput, PreviewOutput\_Callbacks\* callback)](#oh_previewoutput_registercallback) | \- | Registers a callback to listen for preview output events. |
| [Camera\_ErrorCode OH\_PreviewOutput\_UnregisterCallback(Camera\_PreviewOutput\* previewOutput, PreviewOutput\_Callbacks\* callback)](#oh_previewoutput_unregistercallback) | \- | Unregisters the callback used to listen for preview output events. |
| [Camera\_ErrorCode OH\_PreviewOutput\_Start(Camera\_PreviewOutput\* previewOutput)](#oh_previewoutput_start) | \- | Starts preview output. |
| [Camera\_ErrorCode OH\_PreviewOutput\_Stop(Camera\_PreviewOutput\* previewOutput)](#oh_previewoutput_stop) | \- | Stops preview output. |
| [Camera\_ErrorCode OH\_PreviewOutput\_Release(Camera\_PreviewOutput\* previewOutput)](#oh_previewoutput_release) | \- | Releases a PreviewOutput instance. |
| [Camera\_ErrorCode OH\_PreviewOutput\_GetActiveProfile(Camera\_PreviewOutput\* previewOutput, Camera\_Profile\*\* profile)](#oh_previewoutput_getactiveprofile) | \- | Obtains the profile of a PreviewOutput instance. |
| [Camera\_ErrorCode OH\_PreviewOutput\_DeleteProfile(Camera\_Profile\* profile)](#oh_previewoutput_deleteprofile) | \- | Deletes the profile of a PreviewOutput instance. |
| [Camera\_ErrorCode OH\_PreviewOutput\_GetPreviewRotation(Camera\_PreviewOutput\* previewOutput, int displayRotation, Camera\_ImageRotation\* imageRotation)](#oh_previewoutput_getpreviewrotation) | \- | Obtains the preview rotation angle. |
| [Camera\_ErrorCode OH\_PreviewOutput\_SetPreviewRotation(Camera\_PreviewOutput\* previewOutput, Camera\_ImageRotation previewRotation, bool isDisplayLocked)](#oh_previewoutput_setpreviewrotation) | \- | Sets the preview rotation angle. |
| [Camera\_ErrorCode OH\_PreviewOutput\_GetSupportedFrameRates(Camera\_PreviewOutput\* previewOutput, Camera\_FrameRateRange\*\* frameRateRange, uint32\_t\* size)](#oh_previewoutput_getsupportedframerates) | \- | Obtains the list of frame rates supported by a PreviewOutput instance. |
| [Camera\_ErrorCode OH\_PreviewOutput\_DeleteFrameRates(Camera\_PreviewOutput\* previewOutput, Camera\_FrameRateRange\* frameRateRange)](#oh_previewoutput_deleteframerates) | \- | Deletes the frame rate list. |
| [Camera\_ErrorCode OH\_PreviewOutput\_SetFrameRate(Camera\_PreviewOutput\* previewOutput, int32\_t minFps, int32\_t maxFps)](#oh_previewoutput_setframerate) | \- | Sets the frame rates for a PreviewOutput instance. |
| [Camera\_ErrorCode OH\_PreviewOutput\_GetActiveFrameRate(Camera\_PreviewOutput\* previewOutput, Camera\_FrameRateRange\* frameRateRange)](#oh_previewoutput_getactiveframerate) | \- | Obtains the active frame rates of a PreviewOutput instance. |

#### Function Description

#### \[h2\]OH\_PreviewOutput\_OnFrameStart()

typedef void (\*OH\_PreviewOutput\_OnFrameStart)(Camera\_PreviewOutput\* previewOutput)

**Description**

Defines the callback defined in the [PreviewOutput\_Callbacks](../../structs/previewoutput-callbacks/document.md) struct and used to report preview output frame start events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the PreviewOutput instance that transfers the callback. |

#### \[h2\]OH\_PreviewOutput\_OnFrameEnd()

typedef void (\*OH\_PreviewOutput\_OnFrameEnd)(Camera\_PreviewOutput\* previewOutput, int32\_t frameCount)

**Description**

Defines the callback defined in the [PreviewOutput\_Callbacks](../../structs/previewoutput-callbacks/document.md) struct and used to report preview output frame end events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the PreviewOutput instance that transfers the callback. |
| int32\_t frameCount | Number of frames to be included in the callback. |

#### \[h2\]OH\_PreviewOutput\_OnError()

typedef void (\*OH\_PreviewOutput\_OnError)(Camera\_PreviewOutput\* previewOutput, Camera\_ErrorCode errorCode)

**Description**

Defines the callback defined in the [PreviewOutput\_Callbacks](../../structs/previewoutput-callbacks/document.md) struct and used to report preview output errors.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the PreviewOutput instance that transfers the callback. |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) errorCode | Error code reported during preview output. |

**See also**

[CAMERA\_SERVICE\_FATAL\_ERROR](../camera-h/document.md#camera_errorcode)

#### \[h2\]OH\_PreviewOutput\_RegisterCallback()

Camera\_ErrorCode OH\_PreviewOutput\_RegisterCallback(Camera\_PreviewOutput\* previewOutput,PreviewOutput\_Callbacks\* callback)

**Description**

Registers a callback to listen for preview output events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the target PreviewOutput instance. |
| [PreviewOutput\_Callbacks](../../structs/previewoutput-callbacks/document.md)\* callback | Pointer to the target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PreviewOutput\_UnregisterCallback()

Camera\_ErrorCode OH\_PreviewOutput\_UnregisterCallback(Camera\_PreviewOutput\* previewOutput,PreviewOutput\_Callbacks\* callback)

**Description**

Unregisters the callback used to listen for preview output events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the target PreviewOutput instance. |
| [PreviewOutput\_Callbacks](../../structs/previewoutput-callbacks/document.md)\* callback | Pointer to the target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PreviewOutput\_Start()

Camera\_ErrorCode OH\_PreviewOutput\_Start(Camera\_PreviewOutput\* previewOutput)

**Description**

Starts preview output.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the PreviewOutput instance to start. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PreviewOutput\_Stop()

Camera\_ErrorCode OH\_PreviewOutput\_Stop(Camera\_PreviewOutput\* previewOutput)

**Description**

Stops preview output.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the PreviewOutput instance to stop. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PreviewOutput\_Release()

Camera\_ErrorCode OH\_PreviewOutput\_Release(Camera\_PreviewOutput\* previewOutput)

**Description**

Releases a PreviewOutput instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the PreviewOutput instance to release. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PreviewOutput\_GetActiveProfile()

Camera\_ErrorCode OH\_PreviewOutput\_GetActiveProfile(Camera\_PreviewOutput\* previewOutput, Camera\_Profile\*\* profile)

**Description**

Obtains the profile of a PreviewOutput instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the PreviewOutput instance for which the profile is to be obtained. |
| [Camera\_Profile](../../structs/camera-profile/document.md)\*\* profile | Double pointer to the preview output profile obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PreviewOutput\_DeleteProfile()

Camera\_ErrorCode OH\_PreviewOutput\_DeleteProfile(Camera\_Profile\* profile)

**Description**

Deletes the profile of a PreviewOutput instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Profile](../../structs/camera-profile/document.md)\* profile | Pointer to the profile to delete. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PreviewOutput\_GetPreviewRotation()

Camera\_ErrorCode OH\_PreviewOutput\_GetPreviewRotation(Camera\_PreviewOutput\* previewOutput, int displayRotation,Camera\_ImageRotation\* imageRotation)

**Description**

Obtains the preview rotation angle.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the PreviewOutput instance used to obtain the rotation angle. |
| int displayRotation | Rotation angle of the display. |
| [Camera\_ImageRotation](../camera-h/document.md#camera_imagerotation)\* imageRotation | Pointer to the preview rotation angle. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PreviewOutput\_SetPreviewRotation()

Camera\_ErrorCode OH\_PreviewOutput\_SetPreviewRotation(Camera\_PreviewOutput\* previewOutput,Camera\_ImageRotation previewRotation, bool isDisplayLocked)

**Description**

Sets the preview rotation angle.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the PreviewOutput instance used to set the rotation angle. |
| [Camera\_ImageRotation](../camera-h/document.md#camera_imagerotation) previewRotation | Preview rotation angle. |
| bool isDisplayLocked | Whether the orientation of the surface is locked when the screen rotates. If this parameter is not set, the default value **false** is used, indicating that the orientation is not locked. **true** if locked, **false** otherwise. For details, see [SurfaceRotationOptions](../../../../../application-framework/arkui/arkts-components/rendering-drawing/xcomponent/document.md#surfacerotationoptions12). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PreviewOutput\_GetSupportedFrameRates()

Camera\_ErrorCode OH\_PreviewOutput\_GetSupportedFrameRates(Camera\_PreviewOutput\* previewOutput,Camera\_FrameRateRange\*\* frameRateRange, uint32\_t\* size)

**Description**

Obtains the list of frame rates supported by a PreviewOutput instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the PreviewOutput instance used to obtain the frame rates. |
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

#### \[h2\]OH\_PreviewOutput\_DeleteFrameRates()

Camera\_ErrorCode OH\_PreviewOutput\_DeleteFrameRates(Camera\_PreviewOutput\* previewOutput,Camera\_FrameRateRange\* frameRateRange)

**Description**

Deletes the frame rate list.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the target PreviewOutput instance. |
| [Camera\_FrameRateRange](../../structs/camera-frameraterange/document.md)\* frameRateRange | Pointer to the list of frame rates to delete. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PreviewOutput\_SetFrameRate()

Camera\_ErrorCode OH\_PreviewOutput\_SetFrameRate(Camera\_PreviewOutput\* previewOutput,int32\_t minFps, int32\_t maxFps)

**Description**

Sets the frame rates for a PreviewOutput instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the PreviewOutput instance used to set the frame rates. |
| int32\_t minFps | Minimum frame rate. |
| int32\_t maxFps | Maximum frame rate. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PreviewOutput\_GetActiveFrameRate()

Camera\_ErrorCode OH\_PreviewOutput\_GetActiveFrameRate(Camera\_PreviewOutput\* previewOutput,Camera\_FrameRateRange\* frameRateRange)

**Description**

Obtains the active frame rates of a PreviewOutput instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the PreviewOutput instance used to obtain the active frame rates. |
| [Camera\_FrameRateRange](../../structs/camera-frameraterange/document.md)\* frameRateRange | Pointer to the frame rate range, which is defined in the [Camera\_FrameRateRange](../../structs/camera-frameraterange/document.md) struct, if the function is successfully called. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |
