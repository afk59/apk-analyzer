# Interface (CameraManager)

**CameraManager** implements camera management. Before calling any API in CameraManager, you must use [getCameraManager](../functions/document.md#cameragetcameramanager) to obtain a **CameraManager** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/tqHbbPSCQSGbZJHrerXppQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062425Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A801318CEF057B44434987E9CD42D05840CA48D886A2CAD4C472248EAC0FEB26)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### getSupportedCameras

getSupportedCameras(): Array<CameraDevice>

Obtains the supported camera devices. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[CameraDevice](../interfaces-others/document.md#cameradevice)\> | Array of camera devices supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getSupportedCameras(cameraManager: camera.CameraManager): Array<camera.CameraDevice> {
  let cameras: Array<camera.CameraDevice> = \[\];
  try {
    cameras = cameraManager.getSupportedCameras();
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`The getSupportedCameras call failed. error code: ${err.code}\`);
  }
  return cameras;
}

#### getSupportedSceneModes11+

getSupportedSceneModes(camera: CameraDevice): Array<SceneMode>

Obtains the scene modes supported by a camera device. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| camera | [CameraDevice](../interfaces-others/document.md#cameradevice) | Yes | **CameraDevice** instance, which is obtained through [getSupportedCameras](#getsupportedcameras). Error code [7400101](../../../error-codes/camera-error-codes/document.md#section7400101-invalid-parameter) is returned if the input parameter is invalid. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[SceneMode](../enums/document.md#scenemode11)\> | Array of scene modes supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getSupportedSceneModes(cameraManager: camera.CameraManager, camera: camera.CameraDevice): Array<camera.SceneMode> {
  let modes: Array<camera.SceneMode> = \[\];
  try {
    modes = cameraManager.getSupportedSceneModes(camera);
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`The getSupportedSceneModes call failed. error code: ${err.code}\`);
  }
  return modes;
}

#### getSupportedOutputCapability11+

getSupportedOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability

Obtains the output capability supported by a camera device in a given scene mode. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| camera | [CameraDevice](../interfaces-others/document.md#cameradevice) | Yes | **CameraDevice** instance, which is obtained through [getSupportedCameras](#getsupportedcameras). |
| mode | [SceneMode](../enums/document.md#scenemode11) | Yes | Scene mode, which is obtained through [getSupportedSceneModes](#getsupportedscenemodes11). |

**Return value**

| Type | Description |
| :-- | :-- |
| [CameraOutputCapability](../interfaces-others/document.md#cameraoutputcapability) | Camera output capability obtained. |

**Example**

function getSupportedOutputCapability(camera: camera.CameraDevice, cameraManager: camera.CameraManager, sceneMode: camera.SceneMode): camera.CameraOutputCapability {
  let cameraOutputCapability: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(camera, sceneMode);
  return cameraOutputCapability;
}

#### isCameraMuted

isCameraMuted(): boolean

Checks whether this camera is muted.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the camera is muted. **true** if muted, **false** otherwise. |

**Example**

function isCameraMuted(cameraManager: camera.CameraManager): boolean {
  let isMuted: boolean = cameraManager.isCameraMuted();
  return isMuted;
}

#### createCameraInput

createCameraInput(camera: CameraDevice): CameraInput

Creates a **CameraInput** instance with the specified **CameraDevice** instance. This API returns the result synchronously.

Before calling this API, call [getSupportedCameras](#getsupportedcameras) to obtain the list of supported camera devices, select the camera device that meets the requirements based on the actual usage scenario, and then create the **CameraInput** instance.

**Required permissions**: ohos.permission.CAMERA

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| camera | [CameraDevice](../interfaces-others/document.md#cameradevice) | Yes | **CameraDevice** instance, which is obtained through [getSupportedCameras](#getsupportedcameras). |

**Return value**

| Type | Description |
| :-- | :-- |
| [CameraInput](../interface-camerainput/document.md) | **CameraInput** instance created. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function createCameraInput(camera: camera.CameraDevice, cameraManager: camera.CameraManager): camera.CameraInput | undefined {
  let cameraInput: camera.CameraInput | undefined = undefined;
  try {
    cameraInput = cameraManager.createCameraInput(camera);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The createCameraInput call failed. error code: ${err.code}\`);
  }
  return cameraInput;
}

#### createCameraInput

createCameraInput(position: CameraPosition, type: CameraType): CameraInput

Creates a **CameraInput** instance with the specified camera position and type. This API returns the result synchronously.

Before calling this API, specify the camera position and type based on the usage scenario. For example, open the front camera for the selfie feature

**Required permissions**: ohos.permission.CAMERA

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| position | [CameraPosition](../enums/document.md#cameraposition) | Yes | Camera position. You need to obtain the supported camera object by calling [getSupportedCameras](#getsupportedcameras) and then obtain the device position information based on the returned camera object. |
| type | [CameraType](../enums/document.md#cameratype) | Yes | Camera type. You need to obtain the supported camera object by calling [getSupportedCameras](#getsupportedcameras) and then obtain the camera type based on the returned camera object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [CameraInput](../interface-camerainput/document.md) | **CameraInput** instance created. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function createCameraInput(camera: camera.CameraDevice, cameraManager: camera.CameraManager): camera.CameraInput | undefined {
  let position: camera.CameraPosition = camera.cameraPosition;
  let type: camera.CameraType = camera.cameraType;
  let cameraInput: camera.CameraInput | undefined = undefined;
  try {
    cameraInput = cameraManager.createCameraInput(position, type);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The createCameraInput call failed. error code: ${err.code}\`);
  }
  return cameraInput;
}

#### createPreviewOutput

createPreviewOutput(profile: Profile, surfaceId: string): PreviewOutput

Creates a **PreviewOutput** instance. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| profile | [Profile](../interfaces-others/document.md#profile) | Yes | Supported preview profile, which is obtained through [getSupportedOutputCapability](#getsupportedoutputcapability11). |
| surfaceId | string | Yes | Surface ID, which is obtained from [XComponent](../../../../../application-framework/arkui/arkts-components/rendering-drawing/xcomponent/document.md) or [ImageReceiver](../../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-imagereceiver/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| [PreviewOutput](../interface-previewoutput/document.md) | **PreviewOutput** instance created. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function createPreviewOutput(cameraOutputCapability: camera.CameraOutputCapability, cameraManager: camera.CameraManager, surfaceId: string): camera.PreviewOutput | undefined {
  let profile: camera.Profile = cameraOutputCapability.previewProfiles\[0\];
  let previewOutput: camera.PreviewOutput | undefined = undefined;
  try {
    previewOutput = cameraManager.createPreviewOutput(profile, surfaceId);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The createPreviewOutput call failed. error code: ${err.code}\`);
  }
  return previewOutput;
}

#### createPreviewOutput12+

createPreviewOutput(surfaceId: string): PreviewOutput

Creates a **PreviewOutput** instance without configuration. This API returns the result synchronously. It must be used with [preconfig](../interface-photosession/document.md#preconfig12).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| surfaceId | string | Yes | Surface ID, which is obtained from [XComponent](../../../../../application-framework/arkui/arkts-components/rendering-drawing/xcomponent/document.md) or [ImageReceiver](../../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-imagereceiver/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| [PreviewOutput](../interface-previewoutput/document.md) | **PreviewOutput** instance created. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function createPreviewOutput(cameraManager: camera.CameraManager, surfaceId: string): camera.PreviewOutput | undefined {
  let previewOutput: camera.PreviewOutput | undefined = undefined;
  try {
    previewOutput = cameraManager.createPreviewOutput(surfaceId);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The createPreviewOutput call failed. error code: ${err.code}\`);
  }
  return previewOutput;
}

#### createPhotoOutput11+

createPhotoOutput(profile?: Profile): PhotoOutput

Creates a **PhotoOutput** instance. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| profile | [Profile](../interfaces-others/document.md#profile) | No | 
Supported photo profile, which is obtained through [getSupportedOutputCapability](#getsupportedoutputcapability11).

In API version 11, this parameter is mandatory. Starting from API version 12, it will overwrite the preconfigured parameters passed in through [preconfig](../interface-photosession/document.md#preconfig12).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [PhotoOutput](../interface-photooutput/document.md) | **PhotoOutput** instance created. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function createPhotoOutput(cameraOutputCapability: camera.CameraOutputCapability, cameraManager: camera.CameraManager): camera.PhotoOutput | undefined {
  let profile: camera.Profile = cameraOutputCapability.photoProfiles\[0\];
  let photoOutput: camera.PhotoOutput | undefined = undefined;
  try {
    photoOutput = cameraManager.createPhotoOutput(profile);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The createPhotoOutput call failed. error code: ${err.code}\`);
  }
  return photoOutput;
}

#### createVideoOutput

createVideoOutput(profile: VideoProfile, surfaceId: string): VideoOutput

Creates a **VideoOutput** instance. This API returns the result synchronously.

In video recording mode, if SDR or HDR VIVID is enabled, the camera format and color space must be configured according to the relationships specified in the table below. Configurations that do not match the table will cause issues such as preview exceptions.

| SDR/HDR Photo Capture | CameraFormat | ColorSpace |
| :-- | :-- | :-- |
| SDR | CAMERA\_FORMAT\_YUV\_420\_SP | BT709\_LIMIT |
| HDR\_VIVID | 
CAMERA\_FORMAT\_YCRCB\_P010

CAMERA\_FORMAT\_YCBCR\_P010

 | 

BT2020\_HLG\_LIMIT

BT2020\_HLG\_FULL

 |

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| profile | [VideoProfile](../interfaces-others/document.md#videoprofile) | Yes | Supported video profile, which is obtained through [getSupportedOutputCapability](#getsupportedoutputcapability11). |
| surfaceId | string | Yes | Surface ID, which is obtained from [AVRecorder](../../../../media-kit/arkts-apis/ohos-multimedia-media-media/interface-avrecorder/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| [VideoOutput](../interface-videooutput/document.md) | **VideoOutput** instance created. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function createVideoOutput(cameraOutputCapability: camera.CameraOutputCapability, cameraManager: camera.CameraManager, surfaceId: string): camera.VideoOutput | undefined {
  let profile: camera.VideoProfile = cameraOutputCapability.videoProfiles\[0\];
  let videoOutput: camera.VideoOutput | undefined = undefined;
  try {
    videoOutput = cameraManager.createVideoOutput(profile, surfaceId);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The createVideoOutput call failed. error code: ${err.code}\`);
  }
  return videoOutput;
}

#### createVideoOutput12+

createVideoOutput(surfaceId: string): VideoOutput

Creates a **VideoOutput** instance without configuration. This API returns the result synchronously. It must be used with [preconfig](../interface-videosession/document.md#preconfig12).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| surfaceId | string | Yes | Surface ID, which is obtained from [AVRecorder](../../../../media-kit/arkts-apis/ohos-multimedia-media-media/interface-avrecorder/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| [VideoOutput](../interface-videooutput/document.md) | **VideoOutput** instance created. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function createVideoOutput(cameraManager: camera.CameraManager, surfaceId: string): camera.VideoOutput | undefined {
  let videoOutput: camera.VideoOutput | undefined = undefined;
  try {
    videoOutput = cameraManager.createVideoOutput(surfaceId);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The createVideoOutput call failed. error code: ${err.code}\`);
  }
  return videoOutput;
}

#### createMetadataOutput

createMetadataOutput(metadataObjectTypes: Array<MetadataObjectType>): MetadataOutput

Creates a **MetadataOutput** instance. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| metadataObjectTypes | Array<[MetadataObjectType](../enums/document.md#metadataobjecttype)\> | Yes | Metadata object types, which are obtained through [getSupportedOutputCapability](#getsupportedoutputcapability11). |

**Return value**

| Type | Description |
| :-- | :-- |
| [MetadataOutput](../interface-metadataoutput/document.md) | **MetadataOutput** instance created. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function createMetadataOutput(cameraManager: camera.CameraManager, cameraOutputCapability: camera.CameraOutputCapability): void {
  let metadataObjectTypes: Array<camera.MetadataObjectType> = cameraOutputCapability.supportedMetadataObjectTypes;
  let metadataOutput: camera.MetadataOutput | undefined = undefined;
  try {
    metadataOutput = cameraManager.createMetadataOutput(metadataObjectTypes);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`createMetadataOutput error. error code: ${err.code}\`);
  }
}

#### createSession11+

createSession<T extends Session>(mode: SceneMode): T

Creates a **Session** instance with a given scene mode. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [SceneMode](../enums/document.md#scenemode11) | Yes | Scene mode. The API does not take effect if the input parameter is invalid (for example, the value is out of range, null, or undefined). |

**Return value**

| Type | Description |
| :-- | :-- |
| [T](../interface-session/document.md) | **Session** instance created. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3.Parameter verification failed. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function createSession(cameraManager: camera.CameraManager, mode: camera.SceneMode): camera.Session | undefined {
  let photoSession: camera.PhotoSession | undefined = undefined;
  try {
    photoSession = cameraManager.createSession(mode) as camera.PhotoSession;
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`createCaptureSession error. error code: ${err.code}\`);
  }
  return photoSession;
}

#### on('cameraStatus')

on(type: 'cameraStatus', callback: AsyncCallback<CameraStatusInfo>): void

Subscribes to camera status events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/16HXN4WPTm6bVkM3QmZVJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062425Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F636CF92E80CDEE3B3C8748BC7FDBEE78DBF42DFB36FFEB1AD978803D7621395)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'cameraStatus'**. The event can be listened for when a **CameraManager** instance is obtained. This event is triggered and the corresponding information is returned only when the camera device is enabled or disabled. |
| callback | AsyncCallback<[CameraStatusInfo](../interfaces-others/document.md#camerastatusinfo)\> | Yes | Callback used to return the camera status change. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error('cameraStatus with errorCode = ' + err.code);
    return;
  }
  console.info(\`camera : ${cameraStatusInfo.camera.cameraId}\`);
  console.info(\`status: ${cameraStatusInfo.status}\`);
}

function registerCameraStatus(cameraManager: camera.CameraManager): void {
  cameraManager.on('cameraStatus', callback);
}

#### off('cameraStatus')

off(type: 'cameraStatus', callback?: AsyncCallback<CameraStatusInfo>): void

Unsubscribes from camera status events. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'cameraStatus'**. The event can be listened for when a **CameraManager** instance is obtained. |
| callback | AsyncCallback<[CameraStatusInfo](../interfaces-others/document.md#camerastatusinfo)\> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterCameraStatus(cameraManager: camera.CameraManager): void {
  cameraManager.off('cameraStatus');
}

#### on('foldStatusChange')12+

on(type: 'foldStatusChange', callback: AsyncCallback<FoldStatusInfo>): void

Subscribes to fold status change events of the foldable device. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/_lYNVxhNQdiu5sRwqzmvfw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062425Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AEC7EA515FDC2B90CF2EC290E853A29506D7428CAEB8F0C7BDC996C957D0B3C1)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'foldStatusChange'**. The event is triggered when the fold state of the foldable device changes. |
| callback | AsyncCallback<[FoldStatusInfo](../interfaces-others/document.md#foldstatusinfo12)\> | Yes | Callback used to return the fold state information about the foldable device. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, foldStatusInfo: camera.FoldStatusInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error('foldStatusChange with errorCode = ' + err.code);
    return;
  }
  console.info(\`camera length: ${foldStatusInfo.supportedCameras.length}\`);
  console.info(\`foldStatus: ${foldStatusInfo.foldStatus}\`);
}

function registerFoldStatusChange(cameraManager: camera.CameraManager): void {
  cameraManager.on('foldStatusChange', callback);
}

#### off('foldStatusChange')12+

off(type: 'foldStatusChange', callback?: AsyncCallback<FoldStatusInfo>): void

Unsubscribes from fold state change events of the foldable device.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'foldStatusChange'**. The event is triggered when the fold state of the foldable device changes. |
| callback | AsyncCallback<[FoldStatusInfo](../interfaces-others/document.md#foldstatusinfo12)\> | No | Callback used to return the fold state information about the foldable device. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterFoldStatusChange(cameraManager: camera.CameraManager): void {
  cameraManager.off('foldStatusChange');
}

#### isTorchSupported11+

isTorchSupported(): boolean

Checks whether the camera device supports the flashlight.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of the flashlight. **true** if supported, **false** otherwise. If the API call fails, undefined is returned. |

**Example**

function isTorchSupported(cameraManager: camera.CameraManager): boolean {
  let isSupported = cameraManager.isTorchSupported();
  return isSupported;
}

#### isTorchModeSupported11+

isTorchModeSupported(mode: TorchMode): boolean

Checks whether a flashlight mode is supported.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [TorchMode](../enums/document.md#torchmode11) | Yes | Flashlight mode. If the input parameter is null or undefined, it is treated as 0 and the flashlight is turned off. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of the flashlight mode. **true** if supported, **false** otherwise. If the API call fails, undefined is returned. |

**Example**

function isTorchModeSupported(cameraManager: camera.CameraManager, torchMode: camera.TorchMode): boolean {
  let isSupported = cameraManager.isTorchModeSupported(torchMode);
  return isSupported;
}

#### getTorchMode11+

getTorchMode(): TorchMode

Obtains the flashlight mode of this camera device.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [TorchMode](../enums/document.md#torchmode11) | Flashlight mode. |

**Example**

function getTorchMode(cameraManager: camera.CameraManager): camera.TorchMode | undefined {
  let torchMode: camera.TorchMode | undefined = undefined;
  torchMode = cameraManager.getTorchMode();
  return torchMode;
}

#### setTorchMode11+

setTorchMode(mode: TorchMode): void

Sets the flashlight mode.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [TorchMode](../enums/document.md#torchmode11) | Yes | Flashlight mode. If the input parameter is null or undefined, it is treated as 0 and the flashlight is turned off. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setTorchMode(cameraManager: camera.CameraManager, torchMode: camera.TorchMode): void {
  try {
    cameraManager.setTorchMode(torchMode);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The setTorchMode call failed. error code: ${err.code}\`);
  }
}

#### on('torchStatusChange')11+

on(type: 'torchStatusChange', callback: AsyncCallback<TorchStatusInfo>): void

Subscribes to flashlight status change events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/g87TS9rrTlOiuExA5SQdwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062425Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1212FCBBA9029E89DD740B3541F99618D4FC971BD032E8727007653DFE26EE63)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'torchStatusChange'**. The event can be listened for when a **CameraManager** instance is obtained. Currently, this event is triggered only in the following scenarios: The flashlight is turned on or turned off, or becomes unavailable or available. |
| callback | AsyncCallback<[TorchStatusInfo](../interfaces-others/document.md#torchstatusinfo11)\> | Yes | Callback used to return the flashlight status. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, torchStatusInfo: camera.TorchStatusInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info(\`onTorchStatusChange, isTorchAvailable: ${torchStatusInfo.isTorchAvailable}, isTorchActive: ${torchStatusInfo.isTorchActive}, level: ${torchStatusInfo.torchLevel}\`);
}

function registerTorchStatusChange(cameraManager: camera.CameraManager): void {
  cameraManager.on('torchStatusChange', callback);
}

#### off('torchStatusChange')11+

off(type: 'torchStatusChange', callback?: AsyncCallback<TorchStatusInfo>): void

Unsubscribes from flashlight status change events. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'torchStatusChange'**. The event can be listened for when a **CameraManager** instance is obtained. |
| callback | AsyncCallback<[TorchStatusInfo](../interfaces-others/document.md#torchstatusinfo11)\> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterTorchStatusChange(cameraManager: camera.CameraManager): void {
  cameraManager.off('torchStatusChange');
}

#### getCameraDevice18+

getCameraDevice(position: CameraPosition, type: CameraType): CameraDevice

Obtains the specified camera based on the camera position and type.

Obtains the camera lens of the specified [CameraPosition](../enums/document.md#cameraposition) and [CameraType](../enums/document.md#cameratype). If the returned result is undefined, the camera lens is not found on the current device.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| position | [CameraPosition](../enums/document.md#cameraposition) | Yes | Camera position. |
| type | [CameraType](../enums/document.md#cameratype) | Yes | Camera type. |

**Return value**

| Type | Description |
| :-- | :-- |
| [CameraDevice](../interfaces-others/document.md#cameradevice) | Camera obtained. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';

function getCameraDevice(cameraManager: camera.CameraManager, position: camera.CameraPosition, type: camera.CameraType): void {
  try {
    let curCameraDev: camera.CameraDevice | undefined = undefined;
    curCameraDev = cameraManager.getCameraDevice(position, type);
  } catch (error) {
    // If the operation fails, an error code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getCameraDevice call failed. error code: ${err.code}\`);
  }
}

#### getCameraConcurrentInfos18+

getCameraConcurrentInfos(cameras: Array<CameraDevice>): Array<CameraConcurrentInfo>

Obtains the concurrency information of the specified cameras. If the return value is an empty array, concurrency is not supported.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cameras | Array<[CameraDevice](../interfaces-others/document.md#cameradevice)\> | Yes | Array of **CameraDevice** objects. You are advised to use the front and rear cameras obtained by calling [getCameraDevice](#getcameradevice18). |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[CameraConcurrentInfo](../interfaces-others/document.md#cameraconcurrentinfo18)\> | Array of concurrency information corresponding to the provided CameraDevice objects, with a one-to-one mapping. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';

function getCameraConcurrentInfos(cameraManager: camera.CameraManager,
  cameraDeviceArray: Array<camera.CameraDevice>): Array<camera.CameraConcurrentInfo> {
  let cameraConcurrentInfos: Array<camera.CameraConcurrentInfo> = \[\];
  try {
    cameraConcurrentInfos = cameraManager.getCameraConcurrentInfos(cameraDeviceArray);
  } catch (error) {
    // If the operation fails, an error code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getCameraConcurrentInfos call failed. error code: ${err.code}\`);
  }
  return cameraConcurrentInfos;
}

#### getSupportedOutputCapability(deprecated)

getSupportedOutputCapability(camera: CameraDevice): CameraOutputCapability

Obtains the output capability supported by a camera device. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/CE937H1XQMyYHKwtCslhfA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062425Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03BA9701A28F7B69D144539D4518B88F88B7E9B45D1613126B7AF96E3228CA43)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [getSupportedOutputCapability](#getsupportedoutputcapability11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| camera | [CameraDevice](../interfaces-others/document.md#cameradevice) | Yes | **CameraDevice** instance, which is obtained through [getSupportedCameras](#getsupportedcameras). An error code is returned if the input parameter is invalid. |

**Return value**

| Type | Description |
| :-- | :-- |
| [CameraOutputCapability](../interfaces-others/document.md#cameraoutputcapability) | Camera output capability obtained. |

**Example**

function getSupportedOutputCapability(camera: camera.CameraDevice, cameraManager: camera.CameraManager): camera.CameraOutputCapability {
  let cameraOutputCapability: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(camera);
  return cameraOutputCapability;
}

#### createPhotoOutput(deprecated)

createPhotoOutput(profile: Profile, surfaceId: string): PhotoOutput

Creates a **PhotoOutput** instance. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/G3IQGuFdSleOd7Vefw8aWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062425Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF307D48841C7A254F09EEAA94D361D051AB2A99C8B8A6B33A4270012FDA45E3)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [createPhotoOutput](#createphotooutput11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| profile | [Profile](../interfaces-others/document.md#profile) | Yes | Supported photo profile, which is obtained through [getSupportedOutputCapability](#getsupportedoutputcapability11). |
| surfaceId | string | Yes | Surface ID, which is obtained from [ImageReceiver](../../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-imagereceiver/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| [PhotoOutput](../interface-photooutput/document.md) | **PhotoOutput** instance created. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |

import { BusinessError } from '@kit.BasicServicesKit';

function createPhotoOutput(cameraOutputCapability: camera.CameraOutputCapability, cameraManager: camera.CameraManager, surfaceId: string): camera.PhotoOutput | undefined {
  let profile: camera.Profile = cameraOutputCapability.photoProfiles\[0\];
  let photoOutput: camera.PhotoOutput | undefined = undefined;
  try {
    photoOutput = cameraManager.createPhotoOutput(profile, surfaceId);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The createPhotoOutput call failed. error code: ${err.code}\`);
  }
  return photoOutput;
}

#### createCaptureSession(deprecated)

createCaptureSession(): CaptureSession

Creates a **CaptureSession** instance. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/tXmQ1ubtRQifk6muMg1dkQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062425Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD73F4761909ACF007D3990E2A540899021B481053C916529D028F4817099398)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [createSession](#createsession11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [CaptureSession](../deprecated-interface-capturesession-deprecated/document.md) | **CaptureSession** instance created. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function createCaptureSession(cameraManager: camera.CameraManager): camera.CaptureSession | undefined {
  let captureSession: camera.CaptureSession | undefined = undefined;
  try {
    captureSession = cameraManager.createCaptureSession();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`createCaptureSession error. error code: ${err.code}\`);
  }
  return captureSession;
}
