# camera\_manager.h

#### Overview

The file declares the camera manager concepts.

**File to include**: <ohcamera/camera\_manager.h>

**Library**: libohcamera.so

**System capability**: SystemCapability.Multimedia.Camera.Core

**Since**: 11

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [CameraManager\_Callbacks](../../structs/cameramanager-callbacks/document.md) | CameraManager\_Callbacks | Describes the callbacks used to listen for camera status changes. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_CameraManager\_StatusCallback)(Camera\_Manager\* cameraManager, Camera\_StatusInfo\* status)](#oh_cameramanager_statuscallback) | OH\_CameraManager\_StatusCallback | Defines the callback defined in the [CameraManager\_Callbacks](../../structs/cameramanager-callbacks/document.md) struct and used to report the camera manager status. |
| [typedef void (\*OH\_CameraManager\_TorchStatusCallback)(Camera\_Manager\* cameraManager, Camera\_TorchStatusInfo\* status)](#oh_cameramanager_torchstatuscallback) | OH\_CameraManager\_TorchStatusCallback | Defines the callback to listen for flashlight status changes. |
| [typedef void (\*OH\_CameraManager\_OnFoldStatusInfoChange)(Camera\_Manager\* cameraManager, Camera\_FoldStatusInfo\* foldStatusInfo)](#oh_cameramanager_onfoldstatusinfochange) | OH\_CameraManager\_OnFoldStatusInfoChange | Defines the callback to listen for fold status changes of the camera manager. |
| [Camera\_ErrorCode OH\_CameraManager\_RegisterCallback(Camera\_Manager\* cameraManager, CameraManager\_Callbacks\* callback)](#oh_cameramanager_registercallback) | \- | Registers a callback to listen for camera status changes. |
| [Camera\_ErrorCode OH\_CameraManager\_UnregisterCallback(Camera\_Manager\* cameraManager, CameraManager\_Callbacks\* callback)](#oh_cameramanager_unregistercallback) | \- | Unregisters the callback used to listen for camera status changes. |
| [Camera\_ErrorCode OH\_CameraManager\_RegisterTorchStatusCallback(Camera\_Manager\* cameraManager, OH\_CameraManager\_TorchStatusCallback torchStatusCallback)](#oh_cameramanager_registertorchstatuscallback) | \- | Registers a callback to listen for flashlight status changes. |
| [Camera\_ErrorCode OH\_CameraManager\_UnregisterTorchStatusCallback(Camera\_Manager\* cameraManager, OH\_CameraManager\_TorchStatusCallback torchStatusCallback)](#oh_cameramanager_unregistertorchstatuscallback) | \- | Unregisters the callback used to listen for flashlight status changes. |
| [Camera\_ErrorCode OH\_CameraManager\_RegisterFoldStatusInfoCallback(Camera\_Manager\* cameraManager, OH\_CameraManager\_OnFoldStatusInfoChange foldStatusInfoCallback)](#oh_cameramanager_registerfoldstatusinfocallback) | \- | Registers a callback to listen for fold status changes. |
| [Camera\_ErrorCode OH\_CameraManager\_UnregisterFoldStatusInfoCallback(Camera\_Manager\* cameraManager, OH\_CameraManager\_OnFoldStatusInfoChange foldStatusInfoCallback)](#oh_cameramanager_unregisterfoldstatusinfocallback) | \- | Unregisters the callback used to listen for fold status changes. |
| [Camera\_ErrorCode OH\_CameraManager\_GetSupportedCameras(Camera\_Manager\* cameraManager, Camera\_Device\*\* cameras, uint32\_t\* size)](#oh_cameramanager_getsupportedcameras) | \- | Obtains the supported cameras. |
| [Camera\_ErrorCode OH\_CameraManager\_DeleteSupportedCameras(Camera\_Manager\* cameraManager, Camera\_Device\* cameras, uint32\_t size)](#oh_cameramanager_deletesupportedcameras) | \- | Deletes supported cameras. |
| [Camera\_ErrorCode OH\_CameraManager\_GetSupportedCameraOutputCapability(Camera\_Manager\* cameraManager, const Camera\_Device\* camera, Camera\_OutputCapability\*\* cameraOutputCapability)](#oh_cameramanager_getsupportedcameraoutputcapability) | \- | Obtains the output capability supported by a camera. |
| [Camera\_ErrorCode OH\_CameraManager\_GetSupportedCameraOutputCapabilityWithSceneMode(Camera\_Manager\* cameraManager, const Camera\_Device\* camera, Camera\_SceneMode sceneMode, Camera\_OutputCapability\*\* cameraOutputCapability)](#oh_cameramanager_getsupportedcameraoutputcapabilitywithscenemode) | \- | Obtains the output capability supported by a camera in the specified mode. |
| [Camera\_ErrorCode OH\_CameraManager\_DeleteSupportedCameraOutputCapability(Camera\_Manager\* cameraManager, Camera\_OutputCapability\* cameraOutputCapability)](#oh_cameramanager_deletesupportedcameraoutputcapability) | \- | Deletes the output capability supported by a camera. |
| [Camera\_ErrorCode OH\_CameraManager\_IsCameraMuted(Camera\_Manager\* cameraManager, bool\* isCameraMuted)](#oh_cameramanager_iscameramuted) | \- | Checks whether a camera is muted. |
| [Camera\_ErrorCode OH\_CameraManager\_CreateCaptureSession(Camera\_Manager\* cameraManager, Camera\_CaptureSession\*\* captureSession)](#oh_cameramanager_createcapturesession) | \- | Creates a **CaptureSession** instance. |
| [Camera\_ErrorCode OH\_CameraManager\_CreateCameraInput(Camera\_Manager\* cameraManager, const Camera\_Device\* camera, Camera\_Input\*\* cameraInput)](#oh_cameramanager_createcamerainput) | \- | Creates a **Camera\_Input** instance. |
| [Camera\_ErrorCode OH\_CameraManager\_CreateCameraInput\_WithPositionAndType(Camera\_Manager\* cameraManager, Camera\_Position position, Camera\_Type type, Camera\_Input\*\* cameraInput)](#oh_cameramanager_createcamerainput_withpositionandtype) | \- | Creates a **Camera\_Input** instance with the specified camera position and type. |
| [Camera\_ErrorCode OH\_CameraManager\_CreatePreviewOutput(Camera\_Manager\* cameraManager, const Camera\_Profile\* profile, const char\* surfaceId, Camera\_PreviewOutput\*\* previewOutput)](#oh_cameramanager_createpreviewoutput) | \- | Creates a **PreviewOutput** instance. |
| [Camera\_ErrorCode OH\_CameraManager\_CreatePreviewOutputUsedInPreconfig(Camera\_Manager\* cameraManager, const char\* surfaceId, Camera\_PreviewOutput\*\* previewOutput)](#oh_cameramanager_createpreviewoutputusedinpreconfig) | \- | Creates a **PreviewOutput** instance to be used in a preconfiguration stream. |
| [Camera\_ErrorCode OH\_CameraManager\_CreatePhotoOutput(Camera\_Manager\* cameraManager, const Camera\_Profile\* profile, const char\* surfaceId, Camera\_PhotoOutput\*\* photoOutput)](#oh_cameramanager_createphotooutput) | \- | Creates a **PhotoOutput** instance. |
| [Camera\_ErrorCode OH\_CameraManager\_CreatePhotoOutputUsedInPreconfig(Camera\_Manager\* cameraManager, const char\* surfaceId, Camera\_PhotoOutput\*\* photoOutput)](#oh_cameramanager_createphotooutputusedinpreconfig) | \- | Creates a **PhotoOutput** instance to be used in a preconfiguration stream. |
| [Camera\_ErrorCode OH\_CameraManager\_CreatePhotoOutputWithoutSurface(Camera\_Manager \*cameraManager, const Camera\_Profile \*profile, Camera\_PhotoOutput \*\*photoOutput)](#oh_cameramanager_createphotooutputwithoutsurface) | \- | Creates a **PhotoOutput** instance. **surfaceId** is not required in this function. |
| [Camera\_ErrorCode OH\_CameraManager\_CreateVideoOutput(Camera\_Manager\* cameraManager, const Camera\_VideoProfile\* profile, const char\* surfaceId, Camera\_VideoOutput\*\* videoOutput)](#oh_cameramanager_createvideooutput) | \- | Creates a **VideoOutput** instance. |
| [Camera\_ErrorCode OH\_CameraManager\_CreateVideoOutputUsedInPreconfig(Camera\_Manager\* cameraManager, const char\* surfaceId, Camera\_VideoOutput\*\* videoOutput)](#oh_cameramanager_createvideooutputusedinpreconfig) | \- | Creates a **VideoOutput** instance to be used in a preconfiguration stream. |
| [Camera\_ErrorCode OH\_CameraManager\_CreateMetadataOutput(Camera\_Manager\* cameraManager, const Camera\_MetadataObjectType\* profile, Camera\_MetadataOutput\*\* metadataOutput)](#oh_cameramanager_createmetadataoutput) | \- | Creates a **MetadataOutput** instance. |
| [Camera\_ErrorCode OH\_CameraManager\_GetSupportedSceneModes(Camera\_Device\* camera, Camera\_SceneMode\*\* sceneModes, uint32\_t\* size)](#oh_cameramanager_getsupportedscenemodes) | \- | Obtains the scene modes supported by a camera. |
| [Camera\_ErrorCode OH\_CameraManager\_DeleteSceneModes(Camera\_Manager\* cameraManager, Camera\_SceneMode\* sceneModes)](#oh_cameramanager_deletescenemodes) | \- | Deletes scene modes. |
| [Camera\_ErrorCode OH\_CameraManager\_IsTorchSupported(Camera\_Manager\* cameraManager, bool\* isTorchSupported)](#oh_cameramanager_istorchsupported) | \- | Checks whether the device supports the flashlight. |
| [Camera\_ErrorCode OH\_CameraManager\_IsTorchSupportedByTorchMode(Camera\_Manager\* cameraManager, Camera\_TorchMode torchMode, bool\* isTorchSupported)](#oh_cameramanager_istorchsupportedbytorchmode) | \- | Checks whether the device supports the specified flashlight mode. |
| [Camera\_ErrorCode OH\_CameraManager\_SetTorchMode(Camera\_Manager\* cameraManager, Camera\_TorchMode torchMode)](#oh_cameramanager_settorchmode) | \- | Sets a flashlight mode. |
| [Camera\_ErrorCode OH\_CameraManager\_GetCameraDevice(Camera\_Manager\* cameraManager, Camera\_Position position, Camera\_Type type, Camera\_Device\* camera)](#oh_cameramanager_getcameradevice) | \- | Obtains the specified camera based on the camera position and type. |
| [Camera\_ErrorCode OH\_CameraManager\_GetCameraConcurrentInfos(Camera\_Manager\* cameraManager, const Camera\_Device\* camera, uint32\_t deviceSize, Camera\_ConcurrentInfo\*\* cameraConcurrentInfo, uint32\_t\* infoSize)](#oh_cameramanager_getcameraconcurrentinfos) | \- | Obtains the concurrency information of the specified cameras. |

#### Function Description

#### \[h2\]OH\_CameraManager\_StatusCallback()

typedef void (\*OH\_CameraManager\_StatusCallback)(Camera\_Manager\* cameraManager, Camera\_StatusInfo\* status)

**Description**

Defines the callback defined in the [CameraManager\_Callbacks](../../structs/cameramanager-callbacks/document.md) struct and used to report the camera manager status.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance that transfers the callback. |
| [Camera\_StatusInfo](../../structs/camera-statusinfo/document.md)\* status | Pointer to the status information of each camera. |

#### \[h2\]OH\_CameraManager\_TorchStatusCallback()

typedef void (\*OH\_CameraManager\_TorchStatusCallback)(Camera\_Manager\* cameraManager, Camera\_TorchStatusInfo\* status)

**Description**

Defines the callback to listen for flashlight status changes.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance that transfers the callback. |
| [Camera\_TorchStatusInfo](../../structs/camera-torchstatusinfo/document.md)\* status | Pointer to the flashlight status information. |

#### \[h2\]OH\_CameraManager\_OnFoldStatusInfoChange()

typedef void (\*OH\_CameraManager\_OnFoldStatusInfoChange)(Camera\_Manager\* cameraManager, Camera\_FoldStatusInfo\* foldStatusInfo)

**Description**

Defines the callback to listen for fold status changes of the camera manager.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance that transfers the callback. |
| [Camera\_FoldStatusInfo](../../structs/camera-foldstatusinfo/document.md)\* foldStatusInfo | Pointer to the fold status information of the device. |

#### \[h2\]OH\_CameraManager\_RegisterCallback()

Camera\_ErrorCode OH\_CameraManager\_RegisterCallback(Camera\_Manager\* cameraManager, CameraManager\_Callbacks\* callback)

**Description**

Registers a callback to listen for camera status changes.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| [CameraManager\_Callbacks](../../structs/cameramanager-callbacks/document.md)\* callback | Pointer to the target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CameraManager\_UnregisterCallback()

Camera\_ErrorCode OH\_CameraManager\_UnregisterCallback(Camera\_Manager\* cameraManager, CameraManager\_Callbacks\* callback)

**Description**

Unregisters the callback used to listen for camera status changes.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| [CameraManager\_Callbacks](../../structs/cameramanager-callbacks/document.md)\* callback | Pointer to the target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CameraManager\_RegisterTorchStatusCallback()

Camera\_ErrorCode OH\_CameraManager\_RegisterTorchStatusCallback(Camera\_Manager\* cameraManager,OH\_CameraManager\_TorchStatusCallback torchStatusCallback)

**Description**

Registers a callback to listen for flashlight status changes.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| [OH\_CameraManager\_TorchStatusCallback](#oh_cameramanager_torchstatuscallback) torchStatusCallback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CameraManager\_UnregisterTorchStatusCallback()

Camera\_ErrorCode OH\_CameraManager\_UnregisterTorchStatusCallback(Camera\_Manager\* cameraManager,OH\_CameraManager\_TorchStatusCallback torchStatusCallback)

**Description**

Unregisters the callback used to listen for flashlight status changes.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| [OH\_CameraManager\_TorchStatusCallback](#oh_cameramanager_torchstatuscallback) torchStatusCallback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CameraManager\_RegisterFoldStatusInfoCallback()

Camera\_ErrorCode OH\_CameraManager\_RegisterFoldStatusInfoCallback(Camera\_Manager\* cameraManager,OH\_CameraManager\_OnFoldStatusInfoChange foldStatusInfoCallback)

**Description**

Registers a callback to listen for fold status changes.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| [OH\_CameraManager\_OnFoldStatusInfoChange](#oh_cameramanager_onfoldstatusinfochange) foldStatusInfoCallback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CameraManager\_UnregisterFoldStatusInfoCallback()

Camera\_ErrorCode OH\_CameraManager\_UnregisterFoldStatusInfoCallback(Camera\_Manager\* cameraManager,OH\_CameraManager\_OnFoldStatusInfoChange foldStatusInfoCallback)

**Description**

Unregisters the callback used to listen for fold status changes.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| [OH\_CameraManager\_OnFoldStatusInfoChange](#oh_cameramanager_onfoldstatusinfochange) foldStatusInfoCallback | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CameraManager\_GetSupportedCameras()

Camera\_ErrorCode OH\_CameraManager\_GetSupportedCameras(Camera\_Manager\* cameraManager, Camera\_Device\*\* cameras, uint32\_t\* size)

**Description**

Obtains the supported cameras.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| [Camera\_Device](../../structs/camera-device/document.md)\*\* cameras | Double pointer to the list of cameras, which are defined in the Camera\_Device struct, if the function is successfully called. |
| uint32\_t\* size | Pointer to the size of the list of cameras. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CameraManager\_DeleteSupportedCameras()

Camera\_ErrorCode OH\_CameraManager\_DeleteSupportedCameras(Camera\_Manager\* cameraManager, Camera\_Device\* cameras, uint32\_t size)

**Description**

Deletes supported cameras.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| [Camera\_Device](../../structs/camera-device/document.md)\* cameras | Pointer to a list of cameras, which are defined in the Camera\_Device struct. |
| uint32\_t size | Number of cameras to delete. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CameraManager\_GetSupportedCameraOutputCapability()

Camera\_ErrorCode OH\_CameraManager\_GetSupportedCameraOutputCapability(Camera\_Manager\* cameraManager, const Camera\_Device\* camera, Camera\_OutputCapability\*\* cameraOutputCapability)

**Description**

Obtains the output capability supported by a camera.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| const [Camera\_Device](../../structs/camera-device/document.md)\* camera | Pointer to the **Camera\_Device** instance. |
| [Camera\_OutputCapability](../../structs/camera-outputcapability/document.md)\*\* cameraOutputCapability | Double pointer to the output capability, which is defined in the Camera\_OutputCapability struct, if the function is successfully called. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CameraManager\_GetSupportedCameraOutputCapabilityWithSceneMode()

Camera\_ErrorCode OH\_CameraManager\_GetSupportedCameraOutputCapabilityWithSceneMode(Camera\_Manager\* cameraManager, const Camera\_Device\* camera, Camera\_SceneMode sceneMode, Camera\_OutputCapability\*\* cameraOutputCapability)

**Description**

Obtains the output capability supported by a camera in the specified mode.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| const [Camera\_Device](../../structs/camera-device/document.md)\* camera | Pointer to the **Camera\_Device** instance. |
| [Camera\_SceneMode](../camera-h/document.md#camera_scenemode) sceneMode | Scene mode. |
| [Camera\_OutputCapability](../../structs/camera-outputcapability/document.md)\*\* cameraOutputCapability | Double pointer to output capability, which is defined in the **Camera\_OutputCapability** struct, if the function is successfully called. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraManager\_DeleteSupportedCameraOutputCapability()

Camera\_ErrorCode OH\_CameraManager\_DeleteSupportedCameraOutputCapability(Camera\_Manager\* cameraManager, Camera\_OutputCapability\* cameraOutputCapability)

**Description**

Deletes the output capability supported by a camera.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| [Camera\_OutputCapability](../../structs/camera-outputcapability/document.md)\* cameraOutputCapability | Pointer to the output capability, which is defined in the **Camera\_OutputCapability** struct. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CameraManager\_IsCameraMuted()

Camera\_ErrorCode OH\_CameraManager\_IsCameraMuted(Camera\_Manager\* cameraManager, bool\* isCameraMuted)

**Description**

Checks whether a camera is muted.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| bool\* isCameraMuted | Pointer to the check result for whether the camera is muted, if the function is successfully called. **true** if muted, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CameraManager\_CreateCaptureSession()

Camera\_ErrorCode OH\_CameraManager\_CreateCaptureSession(Camera\_Manager\* cameraManager, Camera\_CaptureSession\*\* captureSession)

**Description**

Creates a **CaptureSession** instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\*\* captureSession | Double pointer to the **Camera\_CaptureSession** instance created, if the function is successfully called. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraManager\_CreateCameraInput()

Camera\_ErrorCode OH\_CameraManager\_CreateCameraInput(Camera\_Manager\* cameraManager, const Camera\_Device\* camera, Camera\_Input\*\* cameraInput)

**Description**

Creates a **Camera\_Input** instance.

**Required permissions**: ohos.permission.CAMERA

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| const [Camera\_Device](../../structs/camera-device/document.md)\* camera | Pointer to the **Camera\_Device** instance. |
| [Camera\_Input](../../structs/camera-input/document.md)\*\* cameraInput | Double pointer to the **Camera\_Input** instance created, if the function is successfully called. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraManager\_CreateCameraInput\_WithPositionAndType()

Camera\_ErrorCode OH\_CameraManager\_CreateCameraInput\_WithPositionAndType(Camera\_Manager\* cameraManager, Camera\_Position position, Camera\_Type type, Camera\_Input\*\* cameraInput)

**Description**

Creates a **Camera\_Input** instance with the specified camera position and type.

**Required permissions**: ohos.permission.CAMERA

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| [Camera\_Position](../camera-h/document.md#camera_position) position | Camera position. |
| [Camera\_Type](../camera-h/document.md#camera_type) type | Camera type. |
| [Camera\_Input](../../structs/camera-input/document.md)\*\* cameraInput | Double pointer to the **Camera\_Input** instance created, if the function is successfully called. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraManager\_CreatePreviewOutput()

Camera\_ErrorCode OH\_CameraManager\_CreatePreviewOutput(Camera\_Manager\* cameraManager, const Camera\_Profile\* profile, const char\* surfaceId, Camera\_PreviewOutput\*\* previewOutput)

**Description**

Creates a **PreviewOutput** instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| const [Camera\_Profile](../../structs/camera-profile/document.md)\* profile | Pointer to the profile used for creating the **Camera\_PreviewOutput** instance. |
| const char\* surfaceId | Pointer to the surface ID used for creating the **Camera\_PreviewOutput** instance. |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\*\* previewOutput | Double pointer to the **Camera\_PreviewOutput** instance created, if the function is successfully called. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraManager\_CreatePreviewOutputUsedInPreconfig()

Camera\_ErrorCode OH\_CameraManager\_CreatePreviewOutputUsedInPreconfig(Camera\_Manager\* cameraManager, const char\* surfaceId, Camera\_PreviewOutput\*\* previewOutput)

**Description**

Creates a **PreviewOutput** instance to be used in a preconfiguration stream.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| const char\* surfaceId | Pointer to the surface ID used for creating the **Camera\_PreviewOutput** instance. |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\*\* previewOutput | Double pointer to the **Camera\_PreviewOutput** instance created, if the function is successfully called. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraManager\_CreatePhotoOutput()

Camera\_ErrorCode OH\_CameraManager\_CreatePhotoOutput(Camera\_Manager\* cameraManager, const Camera\_Profile\* profile, const char\* surfaceId, Camera\_PhotoOutput\*\* photoOutput)

**Description**

Creates a **PhotoOutput** instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| const [Camera\_Profile](../../structs/camera-profile/document.md)\* profile | Pointer to the profile used for creating the **Camera\_PhotoOutput** instance. |
| const char\* surfaceId | Pointer to the surface ID used for creating the **Camera\_PhotoOutput** instance. |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\*\* photoOutput | Double pointer to the **Camera\_PhotoOutput** instance created, if the function is successfully called. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraManager\_CreatePhotoOutputUsedInPreconfig()

Camera\_ErrorCode OH\_CameraManager\_CreatePhotoOutputUsedInPreconfig(Camera\_Manager\* cameraManager, const char\* surfaceId, Camera\_PhotoOutput\*\* photoOutput)

**Description**

Creates a **PhotoOutput** instance to be used in a preconfiguration stream.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| const char\* surfaceId | Pointer to the surface ID used for creating the **Camera\_PhotoOutput** instance. |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\*\* photoOutput | Double pointer to the **Camera\_PhotoOutput** instance created, if the function is successfully called. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraManager\_CreatePhotoOutputWithoutSurface()

Camera\_ErrorCode OH\_CameraManager\_CreatePhotoOutputWithoutSurface(Camera\_Manager \*cameraManager, const Camera\_Profile \*profile, Camera\_PhotoOutput \*\*photoOutput)

**Description**

Creates a **PhotoOutput** instance. **surfaceId** is not required in this function.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md) \*cameraManager | Pointer to the **Camera\_Manager** instance. |
| const [Camera\_Profile](../../structs/camera-profile/document.md) \*profile | Pointer to the profile used for creating the **Camera\_PhotoOutput** instance. |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md) \*\*photoOutput | Double pointer to the **Camera\_PhotoOutput** instance created, if the function is successfully called. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraManager\_CreateVideoOutput()

Camera\_ErrorCode OH\_CameraManager\_CreateVideoOutput(Camera\_Manager\* cameraManager, const Camera\_VideoProfile\* profile, const char\* surfaceId, Camera\_VideoOutput\*\* videoOutput)

**Description**

Creates a **VideoOutput** instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| const [Camera\_VideoProfile](../../structs/camera-videoprofile/document.md)\* profile | Pointer to the profile for creating the **Camera\_VideoOutput** instance. |
| const char\* surfaceId | Pointer to the surface ID used for creating the **Camera\_VideoOutput** instance. |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\*\* videoOutput | Double pointer to the **Camera\_VideoOutput** instance created, if the function is successfully called. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraManager\_CreateVideoOutputUsedInPreconfig()

Camera\_ErrorCode OH\_CameraManager\_CreateVideoOutputUsedInPreconfig(Camera\_Manager\* cameraManager, const char\* surfaceId, Camera\_VideoOutput\*\* videoOutput)

**Description**

Creates a **VideoOutput** instance to be used in a preconfiguration stream.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| const char\* surfaceId | Pointer to the surface ID used for creating the **Camera\_VideoOutput** instance. |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\*\* videoOutput | Double pointer to the **Camera\_VideoOutput** instance created, if the function is successfully called. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraManager\_CreateMetadataOutput()

Camera\_ErrorCode OH\_CameraManager\_CreateMetadataOutput(Camera\_Manager\* cameraManager, const Camera\_MetadataObjectType\* profile, Camera\_MetadataOutput\*\* metadataOutput)

**Description**

Creates a **MetadataOutput** instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| const [Camera\_MetadataObjectType](../camera-h/document.md#camera_metadataobjecttype)\* profile | Pointer to the metadata object type used for creating the **Camera\_MetadataOutput** instance. |
| [Camera\_MetadataOutput](../../structs/camera-metadataoutput/document.md)\*\* metadataOutput | Double pointer to the **Camera\_MetadataOutput** instance created, if the function is successfully called. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraManager\_GetSupportedSceneModes()

Camera\_ErrorCode OH\_CameraManager\_GetSupportedSceneModes(Camera\_Device\* camera, Camera\_SceneMode\*\* sceneModes, uint32\_t\* size)

**Description**

Obtains the scene modes supported by a camera.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Device](../../structs/camera-device/document.md)\* camera | Pointer to the **Camera\_Device** instance. |
| [Camera\_SceneMode](../camera-h/document.md#camera_scenemode)\*\* sceneModes | Double pointer to the list of scene modes, which are defined in the Camera\_SceneMode struct, if the function is successfully called. |
| uint32\_t\* size | Pointer to the size of the list of scene modes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraManager\_DeleteSceneModes()

Camera\_ErrorCode OH\_CameraManager\_DeleteSceneModes(Camera\_Manager\* cameraManager, Camera\_SceneMode\* sceneModes)

**Description**

Deletes scene modes.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| [Camera\_SceneMode](../camera-h/document.md#camera_scenemode)\* sceneModes | Pointer to the list of scene modes to delete. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CameraManager\_IsTorchSupported()

Camera\_ErrorCode OH\_CameraManager\_IsTorchSupported(Camera\_Manager\* cameraManager,bool\* isTorchSupported)

**Description**

Checks whether the device supports the flashlight.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| bool\* isTorchSupported | Pointer to the check result for the support of the flashlight. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CameraManager\_IsTorchSupportedByTorchMode()

Camera\_ErrorCode OH\_CameraManager\_IsTorchSupportedByTorchMode(Camera\_Manager\* cameraManager, Camera\_TorchMode torchMode, bool\* isTorchSupported)

**Description**

Checks whether the device supports the specified flashlight mode.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| [Camera\_TorchMode](../camera-h/document.md#camera_torchmode) torchMode | Flashlight mode to check. |
| bool\* isTorchSupported | Pointer to the check result for the support of the flashlight mode. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraManager\_SetTorchMode()

Camera\_ErrorCode OH\_CameraManager\_SetTorchMode(Camera\_Manager\* cameraManager, Camera\_TorchMode torchMode)

**Description**

Sets a flashlight mode.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| [Camera\_TorchMode](../camera-h/document.md#camera_torchmode) torchMode | Flashlight mode to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraManager\_GetCameraDevice()

Camera\_ErrorCode OH\_CameraManager\_GetCameraDevice(Camera\_Manager\* cameraManager, Camera\_Position position, Camera\_Type type, Camera\_Device\* camera)

**Description**

Obtains the specified camera based on the camera position and type.

Obtains the camera lens of the specified [Camera\_Position](../camera-h/document.md#camera_position) and [Camera\_Type](../camera-h/document.md#camera_type). If the returned result is **CAMERA\_SERVICE\_FATAL\_ERROR**, the camera lens is not found on the current device.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| [Camera\_Position](../camera-h/document.md#camera_position) position | Camera position. |
| [Camera\_Type](../camera-h/document.md#camera_type) type | Camera type. |
| [Camera\_Device](../../structs/camera-device/document.md)\* camera | Pointer to the **Camera\_Device** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraManager\_GetCameraConcurrentInfos()

Camera\_ErrorCode OH\_CameraManager\_GetCameraConcurrentInfos(Camera\_Manager\* cameraManager, const Camera\_Device\* camera, uint32\_t deviceSize, Camera\_ConcurrentInfo\*\* cameraConcurrentInfo, uint32\_t\* infoSize)

**Description**

Obtains the concurrency information of the specified cameras.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the **Camera\_Manager** instance. |
| const [Camera\_Device](../../structs/camera-device/document.md)\* camera | Pointer to the list of cameras, which are defined in the **Camera\_Device** struct. You are advised to include both front and rear cameras obtained by calling [OH\_CameraManager\_GetCameraDevice](#oh_cameramanager_getcameradevice). |
| uint32\_t deviceSize | Length of the camera device list. The value must be set to 2 (indicating that both the front and rear cameras are used for concurrency information query). |
| [Camera\_ConcurrentInfo](../../structs/camera-concurrentinfo/document.md)\*\* cameraConcurrentInfo | 
Double pointer to an array of **Camera\_ConcurrentInfo** objects representing the concurrency information of the cameras. This parameter must be set to NULL by default when being passed in.

If the camera supports concurrency, it is assigned the **Camera\_ConcurrentInfo** array obtained.

If the camera does not support concurrency, the passed-in value is retained and the error code [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode).CAMERA\_SERVICE\_FATAL\_ERROR is returned.

 |
| uint32\_t\* infoSize | 

Pointer to the length of the array. This parameter must be set to **0** by default when being passed in.

If the camera supports concurrency, it is assigned the length of the **Camera\_ConcurrentInfo** array obtained.

If the camera does not support concurrency, the passed-in value is retained and the error code [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode).CAMERA\_SERVICE\_FATAL\_ERROR is returned.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal, or the camera does not support concurrency.

 |
