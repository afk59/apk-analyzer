# Interface (CameraInput)

**CameraInput** defines the camera input object.

It provides camera device information used in [Session](../interface-session/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/nMujxTIMQEK3wGBXyvafZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062425Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CCE53BCEF56F0D37521D62E76D7314B38898FAC9BEDAC3CE83F68CB6BC0E5283)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### open

open(callback: AsyncCallback<void>): void

Opens this camera device. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the camera device is opened successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400107 | Can not use camera cause of conflict. |
| 7400108 | Camera disabled cause of security reason. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function openCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.open((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to open the camera, error code: ${err.code}.\`);
      return;
    }
    console.info('Callback returned with camera opened.');
  });
}

#### open

open(): Promise<void>

Opens this camera device. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400102 | Operation not allowed. |
| 7400107 | Can not use camera cause of conflict. |
| 7400108 | Camera disabled cause of security reason. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function openCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.open().then(() => {
    console.info('Promise returned with camera opened.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to open the camera, error code: ${error.code}.\`);
  });
}

#### open12+

open(isSecureEnabled: boolean): Promise<bigint>

Opens this camera device. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isSecureEnabled | boolean | Yes | Whether to open the camera device in secure mode. **true** to open in secure mode, **false** otherwise. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<bigint> | Promise used to return the handle to the camera device in secure mode. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400107 | Can not use camera cause of conflict. |
| 7400108 | Camera disabled cause of security reason. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function openCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.open(true).then(() => {
    console.info('Promise returned with camera opened.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to open the camera, error code: ${error.code}.\`);
  });
}

#### open18+

open(type: CameraConcurrentType): Promise<void>

Opens the camera with the specified concurrency type. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [CameraConcurrentType](../enums/document.md#cameraconcurrenttype18) | Yes | Concurrency type. If the API fails to be called, an error code is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400102 | Operation not allowed. |
| 7400107 | Can not use camera cause of conflict. |
| 7400108 | Camera disabled cause of security reason. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function openCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.open(0).then(() => {
    console.info('Promise returned with camera opened.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to open the camera, error code: ${error.code}.\`);
  });
}

#### close

close(callback: AsyncCallback<void>): void

Closes this camera device. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the camera device is closed successfully, **err** is **undefined**. Otherwise, **err** is an error object with an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function closeCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.close((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to close the cameras, error code: ${err.code}.\`);
      return;
    }
    console.info('Callback returned with camera closed.');
  });
}

#### close

close(): Promise<void>

Closes this camera device. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function closeCameraInput(cameraInput: camera.CameraInput): void {
  cameraInput.close().then(() => {
    console.info('Promise returned with camera closed.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to close the cameras, error code: ${error.code}.\`);
  });
}

#### on('error')

on(type: 'error', camera: CameraDevice, callback: ErrorCallback): void

Subscribes to CameraInput error events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/1tyXN0LlRGCXlmNOGs-0zQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062425Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99D419530CB40D098E198493E3C30EACEEE15D43A6609F0EB8F73AB0C0748439)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a CameraInput instance is created. This event is triggered and the result is returned when an error occurs on the camera device. For example, if the camera device is unavailable or a conflict occurs, the error information is returned. |
| camera | [CameraDevice](../interfaces-others/document.md#cameradevice) | Yes | Camera device. |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | Yes | Callback used to return an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  console.error(\`Camera input error code: ${err.code}\`);
}

function registerCameraInputError(cameraInput: camera.CameraInput, camera: camera.CameraDevice): void {
  cameraInput.on('error', camera, callback);
}

#### off('error')

off(type: 'error', camera: CameraDevice, callback?: ErrorCallback): void

Unsubscribes from CameraInput error events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a CameraInput instance is created. This event is triggered and the result is returned when an error occurs on the camera device. For example, if the camera device is unavailable or a conflict occurs, the error information is returned. |
| camera | [CameraDevice](../interfaces-others/document.md#cameradevice) | Yes | Camera device. |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | No | Callback used to return the result. If this parameter is specified, only the corresponding callback will be unregistered (the callback object cannot be an anonymous function); otherwise, all registered callbacks will be unregistered. |

**Example**

function unregisterCameraInputError(cameraInput: camera.CameraInput, camera: camera.CameraDevice): void {
  cameraInput.off('error', camera);
}

#### isPhysicalCameraOrientationVariable22+

isPhysicalCameraOrientationVariable(): boolean

Checks whether the physical camera orientation is adjustable in different fold states of the device.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the physical camera orientation is adjustable. **true** if adjustable, **false** otherwise. If the API call fails, undefined is returned. |

**Example**

function isPhysicalCameraOrientationVariable(cameraInput: camera.CameraInput): boolean {
  let isVariable: boolean = cameraInput.isPhysicalCameraOrientationVariable();
  return isVariable;
}

#### getPhysicalCameraOrientation22+

getPhysicalCameraOrientation(): number

Obtains the physical camera orientation in the current fold state of the device.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Physical camera orientation. |

**Example**

function getPhysicalCameraOrientation(cameraInput: camera.CameraInput): number {
  let physicalCameraOrientation: number = cameraInput.getPhysicalCameraOrientation();
  return physicalCameraOrientation;
}

#### usePhysicalCameraOrientation22+

usePhysicalCameraOrientation(isUsed: boolean): void

Enables or disables the use of the physical camera orientation.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isUsed | boolean | Yes | Whether to enable the use of the physical camera orientation. **true** to enable, **false** otherwise. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function usePhysicalCameraOrientation(cameraInput: camera.CameraInput, isUsed: boolean): void {
  try {
    cameraInput.usePhysicalCameraOrientation(isUsed);
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`The usePhysicalCameraOrientation call failed. error code: ${err.code}\`);
  }
}
