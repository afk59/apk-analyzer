# camera\_device.h

#### Overview

Defines the basic APIs of the camera device.

**File to include**: <ohcamera/camera\_device.h>

**Library**: libohcamera.so

**System capability**: SystemCapability.Multimedia.Camera.Core

**Since**: 12

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [Camera\_ErrorCode OH\_CameraDevice\_GetCameraOrientation(Camera\_Device\* camera, uint32\_t\* orientation)](#oh_cameradevice_getcameraorientation) | Obtains the sensor direction of a camera device. |
| [Camera\_ErrorCode OH\_CameraDevice\_GetHostDeviceName(Camera\_Device\* camera, char\*\* hostDeviceName)](#oh_cameradevice_gethostdevicename) | Obtains the name of a remote device. |
| [Camera\_ErrorCode OH\_CameraDevice\_GetHostDeviceType(Camera\_Device\* camera, Camera\_HostDeviceType\* hostDeviceType)](#oh_cameradevice_gethostdevicetype) | Obtains the type of a remote device. |

#### Function Description

#### \[h2\]OH\_CameraDevice\_GetCameraOrientation()

Camera\_ErrorCode OH\_CameraDevice\_GetCameraOrientation(Camera\_Device\* camera, uint32\_t\* orientation)

**Description**

Obtains the sensor direction of a camera device.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Device](../../structs/camera-device/document.md)\* camera | Pointer to the camera device. |
| uint32\_t\* orientation | Pointer to the sensor direction obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraDevice\_GetHostDeviceName()

Camera\_ErrorCode OH\_CameraDevice\_GetHostDeviceName(Camera\_Device\* camera, char\*\* hostDeviceName)

**Description**

Obtains the name of a remote device.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Device](../../structs/camera-device/document.md)\* camera | Pointer to the camera device. |
| char\*\* hostDeviceName | Double pointer to the name of the remote device. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful, and the remote device name is returned.

**CAMERA\_CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CameraDevice\_GetHostDeviceType()

Camera\_ErrorCode OH\_CameraDevice\_GetHostDeviceType(Camera\_Device\* camera, Camera\_HostDeviceType\* hostDeviceType)

**Description**

Obtains the type of a remote device.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Device](../../structs/camera-device/document.md)\* camera | Pointer to the camera device. |
| [Camera\_HostDeviceType](../camera-h/document.md#camera_hostdevicetype)\* hostDeviceType | Pointer to the type of the remote device. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful, and the remote device name is returned.

**CAMERA\_CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |
