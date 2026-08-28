# camera\_input.h

#### Overview

The file declares the camera input concepts.

**File to include**: <ohcamera/camera\_input.h>

**Library**: libohcamera.so

**System capability**: SystemCapability.Multimedia.Camera.Core

**Since**: 11

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [CameraInput\_Callbacks](../../structs/camerainput-callbacks/document.md) | CameraInput\_Callbacks | Describes the callbacks used to listen for camera input errors. |
| [Camera\_Input](../../structs/camera-input/document.md) | Camera\_Input | Describes the camera input object. You can use [OH\_CameraManager\_CreateCameraInput](../camera-manager-h/document.md#oh_cameramanager_createcamerainput) to create such an object. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_CameraInput\_OnError)(const Camera\_Input\* cameraInput, Camera\_ErrorCode errorCode)](#oh_camerainput_onerror) | OH\_CameraInput\_OnError | Defines the callback defined in the [CameraInput\_Callbacks](../../structs/camerainput-callbacks/document.md) struct and used to report camera input errors. |
| [Camera\_ErrorCode OH\_CameraInput\_RegisterCallback(Camera\_Input\* cameraInput, CameraInput\_Callbacks\* callback)](#oh_camerainput_registercallback) | \- | Registers a callback to listen for camera input events. |
| [Camera\_ErrorCode OH\_CameraInput\_UnregisterCallback(Camera\_Input\* cameraInput, CameraInput\_Callbacks\* callback)](#oh_camerainput_unregistercallback) | \- | Unregisters the callback used to listen for camera input events. |
| [Camera\_ErrorCode OH\_CameraInput\_Open(Camera\_Input\* cameraInput)](#oh_camerainput_open) | \- | Opens a camera. |
| [Camera\_ErrorCode OH\_CameraInput\_OpenSecureCamera(Camera\_Input\* cameraInput, uint64\_t\* secureSeqId)](#oh_camerainput_opensecurecamera) | \- | Opens a camera in secure mode. |
| [Camera\_ErrorCode OH\_CameraInput\_OpenConcurrentCameras(Camera\_Input\* cameraInput, Camera\_ConcurrentType type)](#oh_camerainput_openconcurrentcameras) | \- | Opens the camera based on the specified concurrency type. |
| [Camera\_ErrorCode OH\_CameraInput\_Close(Camera\_Input\* cameraInput)](#oh_camerainput_close) | \- | Closes a camera. |
| [Camera\_ErrorCode OH\_CameraInput\_Release(Camera\_Input\* cameraInput)](#oh_camerainput_release) | \- | 
Releases a Camera\_Input instance.

Either this function or [OH\_CameraInput\_Close](#oh_camerainput_close) needs to be called.

 |
| [Camera\_ErrorCode OH\_CameraInput\_IsPhysicalCameraOrientationVariable(Camera\_Input\* cameraInput, bool\* isVariable)](#oh_camerainput_isphysicalcameraorientationvariable) | \- | Checks whether the physical camera orientation is adjustable in different fold states of the device. |
| [Camera\_ErrorCode OH\_CameraInput\_GetPhysicalCameraOrientation(Camera\_Input\* cameraInput, uint32\_t\* orientation)](#oh_camerainput_getphysicalcameraorientation) | \- | Obtains the physical camera orientation in the current fold state of the device. |
| [Camera\_ErrorCode OH\_CameraInput\_UsePhysicalCameraOrientation(Camera\_Input\* cameraInput, bool isUsed)](#oh_camerainput_usephysicalcameraorientation) | \- | Enables or disables the use of the physical camera orientation. |

#### Function Description

#### \[h2\]OH\_CameraInput\_OnError()

typedef void (\*OH\_CameraInput\_OnError)(const Camera\_Input\* cameraInput, Camera\_ErrorCode errorCode)

**Description**

Defines the callback defined in the [CameraInput\_Callbacks](../../structs/camerainput-callbacks/document.md) struct and used to report camera input errors.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const [Camera\_Input](../../structs/camera-input/document.md)\* cameraInput | Pointer to the target Camera\_Input instance. |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) errorCode | Error code reported during camera input and defined in the Camera\_ErrorCode struct. |

**See also**

[CAMERA\_CONFLICT\_CAMERA](../camera-h/document.md#camera_errorcode)

[CAMERA\_DEVICE\_DISABLED](../camera-h/document.md#camera_errorcode)

[CAMERA\_DEVICE\_PREEMPTED](../camera-h/document.md#camera_errorcode)

[CAMERA\_SERVICE\_FATAL\_ERROR](../camera-h/document.md#camera_errorcode)

#### \[h2\]OH\_CameraInput\_RegisterCallback()

Camera\_ErrorCode OH\_CameraInput\_RegisterCallback(Camera\_Input\* cameraInput, CameraInput\_Callbacks\* callback)

**Description**

Registers a callback to listen for camera input events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Input](../../structs/camera-input/document.md)\* cameraInput | Pointer to the target Camera\_Input instance. |
| [CameraInput\_Callbacks](../../structs/camerainput-callbacks/document.md)\* callback | Pointer to the target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CameraInput\_UnregisterCallback()

Camera\_ErrorCode OH\_CameraInput\_UnregisterCallback(Camera\_Input\* cameraInput, CameraInput\_Callbacks\* callback)

**Description**

Unregisters the callback used to listen for camera input events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Input](../../structs/camera-input/document.md)\* cameraInput | Pointer to the target Camera\_Input instance. |
| [CameraInput\_Callbacks](../../structs/camerainput-callbacks/document.md)\* callback | Pointer to the target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CameraInput\_Open()

Camera\_ErrorCode OH\_CameraInput\_Open(Camera\_Input\* cameraInput)

**Description**

Opens a camera.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Input](../../structs/camera-input/document.md)\* cameraInput | Pointer to the target Camera\_Input instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_CONFLICT\_CAMERA**: The camera cannot be used due to a conflict.

**CAMERA\_DEVICE\_DISABLED**: The camera is disabled due to security reasons.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraInput\_OpenSecureCamera()

Camera\_ErrorCode OH\_CameraInput\_OpenSecureCamera(Camera\_Input\* cameraInput, uint64\_t\* secureSeqId)

**Description**

Opens a camera in secure mode.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Input](../../structs/camera-input/document.md)\* cameraInput | Pointer to the target Camera\_Input instance. |
| uint64\_t\* secureSeqId | Pointer to the sequence ID of the camera. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_CONFLICT\_CAMERA**: The camera cannot be used due to a conflict.

**CAMERA\_DEVICE\_DISABLED**: The camera is disabled due to security reasons.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraInput\_OpenConcurrentCameras()

Camera\_ErrorCode OH\_CameraInput\_OpenConcurrentCameras(Camera\_Input\* cameraInput, Camera\_ConcurrentType type)

**Description**

Opens the camera based on the specified concurrency type.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Input](../../structs/camera-input/document.md)\* cameraInput | Pointer to the target Camera\_Input instance. |
| [Camera\_ConcurrentType](../camera-h/document.md#camera_concurrenttype) type | Concurrency type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_CONFLICT\_CAMERA**: The camera cannot be used due to a conflict.

**CAMERA\_DEVICE\_DISABLED**: The camera is disabled due to security reasons.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraInput\_Close()

Camera\_ErrorCode OH\_CameraInput\_Close(Camera\_Input\* cameraInput)

**Description**

Closes a camera.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Input](../../structs/camera-input/document.md)\* cameraInput | Pointer to the target Camera\_Input instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraInput\_Release()

Camera\_ErrorCode OH\_CameraInput\_Release(Camera\_Input\* cameraInput)

**Description**

Releases a Camera\_Input instance.

Either this function or [OH\_CameraInput\_Close](#oh_camerainput_close) needs to be called.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Input](../../structs/camera-input/document.md)\* cameraInput | Pointer to the target Camera\_Input instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraInput\_IsPhysicalCameraOrientationVariable()

Camera\_ErrorCode OH\_CameraInput\_IsPhysicalCameraOrientationVariable(Camera\_Input\* cameraInput, bool\* isVariable)

**Description**

Checks whether the physical camera orientation is adjustable in different fold states of the device.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Input](../../structs/camera-input/document.md)\* cameraInput | Pointer to the target Camera\_Input instance. |
| bool\* isVariable | Pointer to the check result for whether the physical camera orientation is adjustable. **true** if adjustable, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CameraInput\_GetPhysicalCameraOrientation()

Camera\_ErrorCode OH\_CameraInput\_GetPhysicalCameraOrientation(Camera\_Input\* cameraInput, uint32\_t\* orientation)

**Description**

Obtains the physical camera orientation in the current fold state of the device.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Input](../../structs/camera-input/document.md)\* cameraInput | Pointer to the target Camera\_Input instance. |
| uint32\_t\* orientation | Pointer to the physical camera orientation if the operation is successful. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CameraInput\_UsePhysicalCameraOrientation()

Camera\_ErrorCode OH\_CameraInput\_UsePhysicalCameraOrientation(Camera\_Input\* cameraInput, bool isUsed)

**Description**

Enables or disables the use of the physical camera orientation.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Input](../../structs/camera-input/document.md)\* cameraInput | Pointer to the target Camera\_Input instance. |
| bool isUsed | Whether to enable the use of the physical camera orientation. **true** to enable, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_OPERATION\_NOT\_ALLOWED**: The operation is not allowed.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |
