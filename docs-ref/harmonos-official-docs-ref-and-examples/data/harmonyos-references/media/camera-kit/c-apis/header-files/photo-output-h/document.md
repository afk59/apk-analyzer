# photo\_output.h

#### Overview

The file declares the photo output concepts.

**File to include**: <ohcamera/photo\_output.h>

**Library**: libohcamera.so

**System capability**: SystemCapability.Multimedia.Camera.Core

**Since**: 11

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [PhotoOutput\_Callbacks](../../structs/photooutput-callbacks/document.md) | PhotoOutput\_Callbacks | Describes the callbacks related to photo output. |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md) | Camera\_PhotoOutput | 
Describes the photo output object.

You can use [OH\_CameraManager\_CreatePhotoOutput](../camera-manager-h/document.md#oh_cameramanager_createphotooutput) to create such an object.

 |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_PhotoOutput\_OnFrameStart)(Camera\_PhotoOutput\* photoOutput)](#oh_photooutput_onframestart) | OH\_PhotoOutput\_OnFrameStart | Defines the callback defined in the [PhotoOutput\_Callbacks](../../structs/photooutput-callbacks/document.md) struct and used to report photo output frame start events. |
| [typedef void (\*OH\_PhotoOutput\_OnFrameShutter)(Camera\_PhotoOutput\* photoOutput, Camera\_FrameShutterInfo\* info)](#oh_photooutput_onframeshutter) | OH\_PhotoOutput\_OnFrameShutter | Defines the callback defined in the [PhotoOutput\_Callbacks](../../structs/photooutput-callbacks/document.md) struct and used to report frame shutter events. |
| [typedef void (\*OH\_PhotoOutput\_OnFrameEnd)(Camera\_PhotoOutput\* photoOutput, int32\_t frameCount)](#oh_photooutput_onframeend) | OH\_PhotoOutput\_OnFrameEnd | Defines the callback defined in the [PhotoOutput\_Callbacks](../../structs/photooutput-callbacks/document.md) struct and used to report photo output frame end events. |
| [typedef void (\*OH\_PhotoOutput\_OnError)(Camera\_PhotoOutput\* photoOutput, Camera\_ErrorCode errorCode)](#oh_photooutput_onerror) | OH\_PhotoOutput\_OnError | Defines the callback defined in the [PhotoOutput\_Callbacks](../../structs/photooutput-callbacks/document.md) struct and used to report photo output errors. |
| [typedef void (\*OH\_PhotoOutput\_CaptureEnd)(Camera\_PhotoOutput\* photoOutput, int32\_t frameCount)](#oh_photooutput_captureend) | OH\_PhotoOutput\_CaptureEnd | Defines the callback invoked when the capture ends. |
| [typedef void (\*OH\_PhotoOutput\_CaptureStartWithInfo)(Camera\_PhotoOutput\* photoOutput, Camera\_CaptureStartInfo\* Info)](#oh_photooutput_capturestartwithinfo) | OH\_PhotoOutput\_CaptureStartWithInfo | Defines the callback invoked when the capture starts. |
| [typedef void (\*OH\_PhotoOutput\_OnFrameShutterEnd)(Camera\_PhotoOutput\* photoOutput, Camera\_FrameShutterInfo\* Info)](#oh_photooutput_onframeshutterend) | OH\_PhotoOutput\_OnFrameShutterEnd | Defines the callback invoked when frame shutter ends. |
| [typedef void (\*OH\_PhotoOutput\_CaptureReady)(Camera\_PhotoOutput\* photoOutput)](#oh_photooutput_captureready) | OH\_PhotoOutput\_CaptureReady | Defines the callback invoked when the camera is ready to take photos. When the callback is received, the next capture can be performed. |
| [typedef void (\*OH\_PhotoOutput\_EstimatedCaptureDuration)(Camera\_PhotoOutput\* photoOutput, int64\_t duration)](#oh_photooutput_estimatedcaptureduration) | OH\_PhotoOutput\_EstimatedCaptureDuration | Defines the callback for the estimated capture duration. |
| [typedef void (\*OH\_PhotoOutput\_PhotoAvailable)(Camera\_PhotoOutput\* photoOutput, OH\_PhotoNative\* photo)](#oh_photooutput_photoavailable) | OH\_PhotoOutput\_PhotoAvailable | Defines the callback invoked when a high-resolution photo is available. |
| [typedef void (\*OH\_PhotoOutput\_PhotoAssetAvailable)(Camera\_PhotoOutput\* photoOutput, OH\_MediaAsset\* photoAsset)](#oh_photooutput_photoassetavailable) | OH\_PhotoOutput\_PhotoAssetAvailable | Defines the callback invoked when a photo asset is available. |
| [Camera\_ErrorCode OH\_PhotoOutput\_RegisterCallback(Camera\_PhotoOutput\* photoOutput, PhotoOutput\_Callbacks\* callback)](#oh_photooutput_registercallback) | \- | Registers a callback to listen for photo output events. |
| [Camera\_ErrorCode OH\_PhotoOutput\_UnregisterCallback(Camera\_PhotoOutput\* photoOutput, PhotoOutput\_Callbacks\* callback)](#oh_photooutput_unregistercallback) | \- | Unregisters the callback used to listen for photo output events. |
| [Camera\_ErrorCode OH\_PhotoOutput\_RegisterCaptureStartWithInfoCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureStartWithInfo callback)](#oh_photooutput_registercapturestartwithinfocallback) | \- | Registers a callback to listen for capture start events. |
| [Camera\_ErrorCode OH\_PhotoOutput\_GetPhotoRotation(Camera\_PhotoOutput\* photoOutput, int deviceDegree, Camera\_ImageRotation\* imageRotation)](#oh_photooutput_getphotorotation) | \- | Obtains the photo rotation angle. |
| [Camera\_ErrorCode OH\_PhotoOutput\_UnregisterCaptureStartWithInfoCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureStartWithInfo callback)](#oh_photooutput_unregistercapturestartwithinfocallback) | \- | Unregisters the callback used to listen for capture start events. |
| [Camera\_ErrorCode OH\_PhotoOutput\_RegisterCaptureEndCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureEnd callback)](#oh_photooutput_registercaptureendcallback) | \- | Registers a callback to listen for capture end events. |
| [Camera\_ErrorCode OH\_PhotoOutput\_UnregisterCaptureEndCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureEnd callback)](#oh_photooutput_unregistercaptureendcallback) | \- | Unregisters the callback used to listen for capture end events. |
| [Camera\_ErrorCode OH\_PhotoOutput\_RegisterFrameShutterEndCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_OnFrameShutterEnd callback)](#oh_photooutput_registerframeshutterendcallback) | \- | Registers a callback to listen for frame shutter end events. |
| [Camera\_ErrorCode OH\_PhotoOutput\_UnregisterFrameShutterEndCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_OnFrameShutterEnd callback)](#oh_photooutput_unregisterframeshutterendcallback) | \- | Unregisters the callback used to listen for frame shutter end events. |
| [Camera\_ErrorCode OH\_PhotoOutput\_RegisterCaptureReadyCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureReady callback)](#oh_photooutput_registercapturereadycallback) | \- | Registers a callback to listen for camera ready events. When the callback is received, the next capture can be performed. |
| [Camera\_ErrorCode OH\_PhotoOutput\_UnregisterCaptureReadyCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureReady callback)](#oh_photooutput_unregistercapturereadycallback) | \- | Unregisters the callback used to listen for camera ready events. |
| [Camera\_ErrorCode OH\_PhotoOutput\_RegisterEstimatedCaptureDurationCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_EstimatedCaptureDuration callback)](#oh_photooutput_registerestimatedcapturedurationcallback) | \- | Registers a callback to listen for estimated capture duration events. |
| [Camera\_ErrorCode OH\_PhotoOutput\_UnregisterEstimatedCaptureDurationCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_EstimatedCaptureDuration callback)](#oh_photooutput_unregisterestimatedcapturedurationcallback) | \- | Unregisters the callback used to listen for estimated capture duration events. |
| [Camera\_ErrorCode OH\_PhotoOutput\_RegisterPhotoAvailableCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_PhotoAvailable callback)](#oh_photooutput_registerphotoavailablecallback) | \- | Registers a callback to listen for photo availability events. |
| [Camera\_ErrorCode OH\_PhotoOutput\_UnregisterPhotoAvailableCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_PhotoAvailable callback)](#oh_photooutput_unregisterphotoavailablecallback) | \- | Unregisters the callback used to listen for photo availability events. |
| [Camera\_ErrorCode OH\_PhotoOutput\_RegisterPhotoAssetAvailableCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_PhotoAssetAvailable callback)](#oh_photooutput_registerphotoassetavailablecallback) | \- | Registers a callback to listen for photo asset availability events. |
| [Camera\_ErrorCode OH\_PhotoOutput\_UnregisterPhotoAssetAvailableCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_PhotoAssetAvailable callback)](#oh_photooutput_unregisterphotoassetavailablecallback) | \- | Unregisters the callback used to listen for photo asset availability events. |
| [Camera\_ErrorCode OH\_PhotoOutput\_Capture(Camera\_PhotoOutput\* photoOutput)](#oh_photooutput_capture) | \- | 
Captures a photo.

This function must be called in prior to [OH\_PreviewOutput\_Release](../preview-output-h/document.md#oh_previewoutput_release). Otherwise, photo capture fails.

 |
| [Camera\_ErrorCode OH\_PhotoOutput\_Capture\_WithCaptureSetting(Camera\_PhotoOutput\* photoOutput, Camera\_PhotoCaptureSetting setting)](#oh_photooutput_capture_withcapturesetting) | \- | Captures a photo with photographing parameters. |
| [Camera\_ErrorCode OH\_PhotoOutput\_Release(Camera\_PhotoOutput\* photoOutput)](#oh_photooutput_release) | \- | Releases a PhotoOutput instance. |
| [Camera\_ErrorCode OH\_PhotoOutput\_IsMirrorSupported(Camera\_PhotoOutput\* photoOutput, bool\* isSupported)](#oh_photooutput_ismirrorsupported) | \- | Checks whether mirroring is supported. |
| [Camera\_ErrorCode OH\_PhotoOutput\_EnableMirror(Camera\_PhotoOutput\* photoOutput, bool enabled)](#oh_photooutput_enablemirror) | \- | Enables dynamic photo capture. |
| [Camera\_ErrorCode OH\_PhotoOutput\_GetActiveProfile(Camera\_PhotoOutput\* photoOutput, Camera\_Profile\*\* profile)](#oh_photooutput_getactiveprofile) | \- | Obtains the profile of a PhotoOutput instance. |
| [Camera\_ErrorCode OH\_PhotoOutput\_DeleteProfile(Camera\_Profile\* profile)](#oh_photooutput_deleteprofile) | \- | Deletes the profile of a PhotoOutput instance. |
| [Camera\_ErrorCode OH\_PhotoOutput\_IsMovingPhotoSupported(Camera\_PhotoOutput\* photoOutput, bool\* isSupported)](#oh_photooutput_ismovingphotosupported) | \- | Checks whether moving photos are supported. |
| [Camera\_ErrorCode OH\_PhotoOutput\_EnableMovingPhoto(Camera\_PhotoOutput\* photoOutput, bool enabled)](#oh_photooutput_enablemovingphoto) | \- | Enables moving photos. |
| [Camera\_ErrorCode OH\_PhotoOutput\_IsPhotoQualityPrioritizationSupported(Camera\_PhotoOutput\* photoOutput, Camera\_PhotoQualityPrioritization qualityPrioritization, bool\* isSupported)](#oh_photooutput_isphotoqualityprioritizationsupported) | \- | Checks whether the specified photo quality prioritization strategy is supported. |
| [Camera\_ErrorCode OH\_PhotoOutput\_SetPhotoQualityPrioritization(Camera\_PhotoOutput\* photoOutput, Camera\_PhotoQualityPrioritization qualityPrioritization)](#oh_photooutput_setphotoqualityprioritization) | \- | Sets the photo quality prioritization strategy. |

#### Function Description

#### \[h2\]OH\_PhotoOutput\_OnFrameStart()

typedef void (\*OH\_PhotoOutput\_OnFrameStart)(Camera\_PhotoOutput\* photoOutput)

**Description**

Defines the callback defined in the [PhotoOutput\_Callbacks](../../structs/photooutput-callbacks/document.md) struct and used to report photo output frame start events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the PhotoOutput instance that transfers the callback. |

#### \[h2\]OH\_PhotoOutput\_OnFrameShutter()

typedef void (\*OH\_PhotoOutput\_OnFrameShutter)(Camera\_PhotoOutput\* photoOutput, Camera\_FrameShutterInfo\* info)

**Description**

Defines the callback defined in the [PhotoOutput\_Callbacks](../../structs/photooutput-callbacks/document.md) struct and used to report frame shutter events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the PhotoOutput instance that transfers the callback. |
| [Camera\_FrameShutterInfo](../../structs/camera-frameshutterinfo/document.md)\* info | Pointer to the frame shutter information. |

#### \[h2\]OH\_PhotoOutput\_OnFrameEnd()

typedef void (\*OH\_PhotoOutput\_OnFrameEnd)(Camera\_PhotoOutput\* photoOutput, int32\_t frameCount)

**Description**

Defines the callback defined in the [PhotoOutput\_Callbacks](../../structs/photooutput-callbacks/document.md) struct and used to report photo output frame end events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the PhotoOutput instance that transfers the callback. |
| int32\_t frameCount | Number of frames to be included in the callback. |

#### \[h2\]OH\_PhotoOutput\_OnError()

typedef void (\*OH\_PhotoOutput\_OnError)(Camera\_PhotoOutput\* photoOutput, Camera\_ErrorCode errorCode)

**Description**

Defines the callback defined in the [PhotoOutput\_Callbacks](../../structs/photooutput-callbacks/document.md) struct and used to report photo output errors.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the PhotoOutput instance that transfers the callback. |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) errorCode | Error code reported during photo output. |

**See also**

[CAMERA\_SERVICE\_FATAL\_ERROR](../camera-h/document.md#camera_errorcode)

#### \[h2\]OH\_PhotoOutput\_CaptureEnd()

typedef void (\*OH\_PhotoOutput\_CaptureEnd)(Camera\_PhotoOutput\* photoOutput, int32\_t frameCount)

**Description**

Defines the callback invoked when the capture ends.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the PhotoOutput instance that transfers the callback. |
| int32\_t frameCount | Number of frames to be included in the callback. |

#### \[h2\]OH\_PhotoOutput\_CaptureStartWithInfo()

typedef void (\*OH\_PhotoOutput\_CaptureStartWithInfo)(Camera\_PhotoOutput\* photoOutput, Camera\_CaptureStartInfo\* Info)

**Description**

Defines the callback invoked when the capture starts.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the PhotoOutput instance that transfers the callback. |
| [Camera\_CaptureStartInfo](../../structs/camera-capturestartinfo/document.md)\* Info | Pointer to the capture start information passed by the callback. |

#### \[h2\]OH\_PhotoOutput\_OnFrameShutterEnd()

typedef void (\*OH\_PhotoOutput\_OnFrameShutterEnd)(Camera\_PhotoOutput\* photoOutput, Camera\_FrameShutterInfo\* Info)

**Description**

Defines the callback invoked when frame shutter ends.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the PhotoOutput instance that transfers the callback. |
| [Camera\_FrameShutterInfo](../../structs/camera-frameshutterinfo/document.md)\* Info | Pointer to the frame shutter information. |

#### \[h2\]OH\_PhotoOutput\_CaptureReady()

typedef void (\*OH\_PhotoOutput\_CaptureReady)(Camera\_PhotoOutput\* photoOutput)

**Description**

Defines the callback invoked when the camera is ready to take photos. When the callback is received, the next capture can be performed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the PhotoOutput instance that transfers the callback. |

#### \[h2\]OH\_PhotoOutput\_EstimatedCaptureDuration()

typedef void (\*OH\_PhotoOutput\_EstimatedCaptureDuration)(Camera\_PhotoOutput\* photoOutput, int64\_t duration)

**Description**

Defines the callback for the estimated capture duration.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the PhotoOutput instance that transfers the callback. |
| int64\_t duration | Estimated capture duration passed by the callback, measured in milliseconds. |

#### \[h2\]OH\_PhotoOutput\_PhotoAvailable()

typedef void (\*OH\_PhotoOutput\_PhotoAvailable)(Camera\_PhotoOutput\* photoOutput, OH\_PhotoNative\* photo)

**Description**

Defines the callback invoked when a high-resolution photo is available.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the PhotoOutput instance that transfers the callback. |
| [OH\_PhotoNative](../../structs/oh-photonative/document.md)\* photo | Pointer to OH\_PhotoNative passed by the callback. |

#### \[h2\]OH\_PhotoOutput\_PhotoAssetAvailable()

typedef void (\*OH\_PhotoOutput\_PhotoAssetAvailable)(Camera\_PhotoOutput\* photoOutput, OH\_MediaAsset\* photoAsset)

**Description**

Defines the callback invoked when a photo asset is available.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the PhotoOutput instance that transfers the callback. |
| [OH\_MediaAsset](../../../../media-library-kit/c-apis/structs/oh-mediaasset/document.md)\* photoAsset | Pointer to the media asset passed by the callback. |

#### \[h2\]OH\_PhotoOutput\_RegisterCallback()

Camera\_ErrorCode OH\_PhotoOutput\_RegisterCallback(Camera\_PhotoOutput\* photoOutput, PhotoOutput\_Callbacks\* callback)

**Description**

Registers a callback to listen for photo output events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [PhotoOutput\_Callbacks](../../structs/photooutput-callbacks/document.md)\* callback | Pointer to the target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PhotoOutput\_UnregisterCallback()

Camera\_ErrorCode OH\_PhotoOutput\_UnregisterCallback(Camera\_PhotoOutput\* photoOutput, PhotoOutput\_Callbacks\* callback)

**Description**

Unregisters the callback used to listen for photo output events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [PhotoOutput\_Callbacks](../../structs/photooutput-callbacks/document.md)\* callback | Pointer to the target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PhotoOutput\_RegisterCaptureStartWithInfoCallback()

Camera\_ErrorCode OH\_PhotoOutput\_RegisterCaptureStartWithInfoCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureStartWithInfo callback)

**Description**

Registers a callback to listen for capture start events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [OH\_PhotoOutput\_CaptureStartWithInfo](#oh_photooutput_capturestartwithinfo) callback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PhotoOutput\_GetPhotoRotation()

Camera\_ErrorCode OH\_PhotoOutput\_GetPhotoRotation(Camera\_PhotoOutput\* photoOutput, int deviceDegree, Camera\_ImageRotation\* imageRotation)

**Description**

Obtains the photo rotation angle.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| int deviceDegree | Rotation angle of the device. |
| [Camera\_ImageRotation](../camera-h/document.md#camera_imagerotation)\* imageRotation | Pointer to the rotation angle of the photo. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PhotoOutput\_UnregisterCaptureStartWithInfoCallback()

Camera\_ErrorCode OH\_PhotoOutput\_UnregisterCaptureStartWithInfoCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureStartWithInfo callback)

**Description**

Unregisters the callback used to listen for capture start events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [OH\_PhotoOutput\_CaptureStartWithInfo](#oh_photooutput_capturestartwithinfo) callback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PhotoOutput\_RegisterCaptureEndCallback()

Camera\_ErrorCode OH\_PhotoOutput\_RegisterCaptureEndCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureEnd callback)

**Description**

Registers a callback to listen for capture end events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [OH\_PhotoOutput\_CaptureEnd](#oh_photooutput_captureend) callback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PhotoOutput\_UnregisterCaptureEndCallback()

Camera\_ErrorCode OH\_PhotoOutput\_UnregisterCaptureEndCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureEnd callback)

**Description**

Unregisters the callback used to listen for capture end events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [OH\_PhotoOutput\_CaptureEnd](#oh_photooutput_captureend) callback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PhotoOutput\_RegisterFrameShutterEndCallback()

Camera\_ErrorCode OH\_PhotoOutput\_RegisterFrameShutterEndCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_OnFrameShutterEnd callback)

**Description**

Registers a callback to listen for frame shutter end events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [OH\_PhotoOutput\_OnFrameShutterEnd](#oh_photooutput_onframeshutterend) callback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PhotoOutput\_UnregisterFrameShutterEndCallback()

Camera\_ErrorCode OH\_PhotoOutput\_UnregisterFrameShutterEndCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_OnFrameShutterEnd callback)

**Description**

Unregisters the callback used to listen for frame shutter end events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [OH\_PhotoOutput\_OnFrameShutterEnd](#oh_photooutput_onframeshutterend) callback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PhotoOutput\_RegisterCaptureReadyCallback()

Camera\_ErrorCode OH\_PhotoOutput\_RegisterCaptureReadyCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureReady callback)

**Description**

Registers a callback to listen for camera ready events. When the callback is received, the next capture can be performed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [OH\_PhotoOutput\_CaptureReady](#oh_photooutput_captureready) callback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PhotoOutput\_UnregisterCaptureReadyCallback()

Camera\_ErrorCode OH\_PhotoOutput\_UnregisterCaptureReadyCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_CaptureReady callback)

**Description**

Unregisters the callback used to listen for camera ready events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [OH\_PhotoOutput\_CaptureReady](#oh_photooutput_captureready) callback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PhotoOutput\_RegisterEstimatedCaptureDurationCallback()

Camera\_ErrorCode OH\_PhotoOutput\_RegisterEstimatedCaptureDurationCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_EstimatedCaptureDuration callback)

**Description**

Registers a callback to listen for estimated capture duration events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [OH\_PhotoOutput\_EstimatedCaptureDuration](#oh_photooutput_estimatedcaptureduration) callback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PhotoOutput\_UnregisterEstimatedCaptureDurationCallback()

Camera\_ErrorCode OH\_PhotoOutput\_UnregisterEstimatedCaptureDurationCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_EstimatedCaptureDuration callback)

**Description**

Unregisters the callback used to listen for estimated capture duration events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [OH\_PhotoOutput\_EstimatedCaptureDuration](#oh_photooutput_estimatedcaptureduration) callback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PhotoOutput\_RegisterPhotoAvailableCallback()

Camera\_ErrorCode OH\_PhotoOutput\_RegisterPhotoAvailableCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_PhotoAvailable callback)

**Description**

Registers a callback to listen for photo availability events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [OH\_PhotoOutput\_PhotoAvailable](#oh_photooutput_photoavailable) callback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PhotoOutput\_UnregisterPhotoAvailableCallback()

Camera\_ErrorCode OH\_PhotoOutput\_UnregisterPhotoAvailableCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_PhotoAvailable callback)

**Description**

Unregisters the callback used to listen for photo availability events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [OH\_PhotoOutput\_PhotoAvailable](#oh_photooutput_photoavailable) callback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PhotoOutput\_RegisterPhotoAssetAvailableCallback()

Camera\_ErrorCode OH\_PhotoOutput\_RegisterPhotoAssetAvailableCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_PhotoAssetAvailable callback)

**Description**

Registers a callback to listen for photo asset availability events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [OH\_PhotoOutput\_PhotoAssetAvailable](#oh_photooutput_photoassetavailable) callback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PhotoOutput\_UnregisterPhotoAssetAvailableCallback()

Camera\_ErrorCode OH\_PhotoOutput\_UnregisterPhotoAssetAvailableCallback(Camera\_PhotoOutput\* photoOutput, OH\_PhotoOutput\_PhotoAssetAvailable callback)

**Description**

Unregisters the callback used to listen for photo asset availability events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [OH\_PhotoOutput\_PhotoAssetAvailable](#oh_photooutput_photoassetavailable) callback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PhotoOutput\_Capture()

Camera\_ErrorCode OH\_PhotoOutput\_Capture(Camera\_PhotoOutput\* photoOutput)

**Description**

Captures a photo.

This function must be called in prior to [OH\_PreviewOutput\_Release](../preview-output-h/document.md#oh_previewoutput_release). Otherwise, photo capture fails.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_RUNNING**: The capture session is not running.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PhotoOutput\_Capture\_WithCaptureSetting()

Camera\_ErrorCode OH\_PhotoOutput\_Capture\_WithCaptureSetting(Camera\_PhotoOutput\* photoOutput, Camera\_PhotoCaptureSetting setting)

**Description**

Captures a photo with photographing parameters.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [Camera\_PhotoCaptureSetting](../../structs/camera-photocapturesetting/document.md) setting | Photographing parameters, which are defined in the [Camera\_PhotoCaptureSetting](../../structs/camera-photocapturesetting/document.md) struct. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_RUNNING**: The capture session is not running.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PhotoOutput\_Release()

Camera\_ErrorCode OH\_PhotoOutput\_Release(Camera\_PhotoOutput\* photoOutput)

**Description**

Releases a PhotoOutput instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PhotoOutput\_IsMirrorSupported()

Camera\_ErrorCode OH\_PhotoOutput\_IsMirrorSupported(Camera\_PhotoOutput\* photoOutput, bool\* isSupported)

**Description**

Checks whether mirroring is supported.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| bool\* isSupported | Pointer to the check result for the support of mirroring. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PhotoOutput\_EnableMirror()

Camera\_ErrorCode OH\_PhotoOutput\_EnableMirror(Camera\_PhotoOutput\* photoOutput, bool enabled)

**Description**

Enables dynamic photo capture.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| bool enabled | Whether to enable or disable dynamic photo capture. **true** to enable, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PhotoOutput\_GetActiveProfile()

Camera\_ErrorCode OH\_PhotoOutput\_GetActiveProfile(Camera\_PhotoOutput\* photoOutput, Camera\_Profile\*\* profile)

**Description**

Obtains the profile of a PhotoOutput instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [Camera\_Profile](../../structs/camera-profile/document.md)\*\* profile | Double pointer to the photo output profile obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PhotoOutput\_DeleteProfile()

Camera\_ErrorCode OH\_PhotoOutput\_DeleteProfile(Camera\_Profile\* profile)

**Description**

Deletes the profile of a PhotoOutput instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Profile](../../structs/camera-profile/document.md)\* profile | Pointer to the target PhotoOutput instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PhotoOutput\_IsMovingPhotoSupported()

Camera\_ErrorCode OH\_PhotoOutput\_IsMovingPhotoSupported(Camera\_PhotoOutput\* photoOutput, bool\* isSupported)

**Description**

Checks whether moving photos are supported.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| bool\* isSupported | Pointer to the check result for the support of moving photos. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PhotoOutput\_EnableMovingPhoto()

Camera\_ErrorCode OH\_PhotoOutput\_EnableMovingPhoto(Camera\_PhotoOutput\* photoOutput, bool enabled)

**Description**

Enables moving photos.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| bool enabled | Whether to enable or disable moving photos. **true** to enable, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PhotoOutput\_IsPhotoQualityPrioritizationSupported()

Camera\_ErrorCode OH\_PhotoOutput\_IsPhotoQualityPrioritizationSupported(Camera\_PhotoOutput\* photoOutput, Camera\_PhotoQualityPrioritization qualityPrioritization, bool\* isSupported)

**Description**

Checks whether the specified photo quality prioritization strategy is supported.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [Camera\_PhotoQualityPrioritization](../camera-h/document.md#camera_photoqualityprioritization) qualityPrioritization | Photo quality prioritization strategy. |
| bool\* isSupported | Pointer to the check result for the support of the specified photo quality prioritization strategy. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_PhotoOutput\_SetPhotoQualityPrioritization()

Camera\_ErrorCode OH\_PhotoOutput\_SetPhotoQualityPrioritization(Camera\_PhotoOutput\* photoOutput, Camera\_PhotoQualityPrioritization qualityPrioritization)

**Description**

Sets the photo quality prioritization strategy.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the target PhotoOutput instance. |
| [Camera\_PhotoQualityPrioritization](../camera-h/document.md#camera_photoqualityprioritization) qualityPrioritization | Photo quality prioritization strategy. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_OPERATION\_NOT\_ALLOWED**: The operation is not allowed.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |
