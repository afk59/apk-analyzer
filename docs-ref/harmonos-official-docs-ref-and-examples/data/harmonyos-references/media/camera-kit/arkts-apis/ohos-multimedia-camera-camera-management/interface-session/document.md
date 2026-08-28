# Interface (Session)

**Session** implements a session, which saves all [CameraInput](../interface-camerainput/document.md) and [CameraOutput](../interface-cameraoutput/document.md) instances required to run the camera and requests the camera to take a photo or record a video.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/j1bBEZ_gQnmxKGXCL1rDqg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EC6192AF6D7A69A3EB7AF5E99925C711C3BF370616E2A3C43E47510E7FD4ECC)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 11.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### beginConfig11+

beginConfig(): void

Starts configuration for the session.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400105 | Session config locked. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function beginConfig(session: camera.Session): void {
  try {
    session.beginConfig();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The beginConfig call failed. error code: ${err.code}\`);
  }
}

#### commitConfig11+

commitConfig(callback: AsyncCallback<void>): void

Commits the configuration for this session. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the configuration is successfully committed, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). For example, if the aspect ratio of the preview stream is different from that of the video output stream, error code 7400201 is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function commitConfig(session: camera.Session): void {
  session.commitConfig((err: BusinessError) => {
    if (err) {
      console.error(\`The commitConfig call failed. error code: ${err.code}\`);
      return;
    }
    console.info('Callback invoked to indicate the commit config success.');
  });
}

#### commitConfig11+

commitConfig(): Promise<void>

Commits the configuration for this session. This API uses a promise to return the result.

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
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function commitConfig(session: camera.Session): void {
  session.commitConfig().then(() => {
    console.info('Promise returned to indicate the commit config success.');
  }).catch((error: BusinessError) => {
    // If the operation fails, error.code is returned and processed.
    console.error(\`The commitConfig call failed. error code: ${error.code}\`);
  });
}

#### canAddInput11+

canAddInput(cameraInput: CameraInput): boolean

Checks whether a **CameraInput** instance can be added to this session. This API must be called after [beginConfig](#beginconfig11) and before [commitConfig](#commitconfig11-1).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cameraInput | [CameraInput](../interface-camerainput/document.md) | Yes | **CameraInput** instance to add. The API does not take effect if the input parameter is invalid (for example, the value is out of range, null, or undefined). |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for adding the **CameraInput** instance. **true** if it can be added, **false** otherwise. |

**Example**

function canAddInput(session: camera.Session, cameraInput: camera.CameraInput): void {
  let canAdd: boolean = session.canAddInput(cameraInput);
  console.info(\`The input canAddInput: ${canAdd}\`);
}

#### addInput11+

addInput(cameraInput: CameraInput): void

Adds a [CameraInput](../interface-camerainput/document.md) instance to this session.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cameraInput | [CameraInput](../interface-camerainput/document.md) | Yes | **CameraInput** instance to add. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function addInput(session: camera.Session, cameraInput: camera.CameraInput): void {
  try {
    session.addInput(cameraInput);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The addInput call failed. error code: ${err.code}\`);
  }
}

#### removeInput11+

removeInput(cameraInput: CameraInput): void

Removes a [CameraInput](../interface-camerainput/document.md) instance from this session. This API must be called after [beginConfig](#beginconfig11) and before [commitConfig](#commitconfig11-1).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cameraInput | [CameraInput](../interface-camerainput/document.md) | Yes | **CameraInput** instance to remove. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function removeInput(session: camera.Session, cameraInput: camera.CameraInput): void {
  try {
    session.removeInput(cameraInput);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The removeInput call failed. error code: ${err.code}\`);
  }
}

#### canAddOutput11+

canAddOutput(cameraOutput: CameraOutput): boolean

Determines whether a CameraOutput instance can be added to this session. This API must be called after [addInput](#addinput11) and before [commitConfig](#commitconfig11-1).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cameraOutput | [CameraOutput](../interface-cameraoutput/document.md) | Yes | **CameraOutput** instance to add. The API does not take effect if the input parameter is invalid (for example, the value is out of range, null, or undefined). |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for adding the **CameraOutput** instance. **true** if it can be added, **false** otherwise. |

**Example**

function canAddOutput(session: camera.Session, cameraOutput: camera.CameraOutput): void {
  let canAdd: boolean = session.canAddOutput(cameraOutput);
  console.info(\`This addOutput can add: ${canAdd}\`);
}

#### addOutput11+

addOutput(cameraOutput: CameraOutput): void

Adds a [CameraOutput](../interface-cameraoutput/document.md) instance to this session.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cameraOutput | [CameraOutput](../interface-cameraoutput/document.md) | Yes | **CameraOutput** instance to add. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function addOutput(session: camera.Session, cameraOutput: camera.CameraOutput): void {
  try {
    session.addOutput(cameraOutput);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The addOutput call failed. error code: ${err.code}\`);
  }
}

#### removeOutput11+

removeOutput(cameraOutput: CameraOutput): void

Removes a [CameraOutput](../interface-cameraoutput/document.md) instance from this session.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cameraOutput | [CameraOutput](../interface-cameraoutput/document.md) | Yes | **CameraOutput** instance to remove. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function removeOutput(session: camera.Session, previewOutput: camera.PreviewOutput): void {
  try {
    session.removeOutput(previewOutput);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The removeOutput call failed. error code: ${err.code}\`);
  }
}

#### start11+

start(callback: AsyncCallback<void>): void

Starts this session. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the session starts successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400102 | Operation not allowed. |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function startCaptureSession(session: camera.Session): void {
  session.start((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to start the session, error code: ${err.code}.\`);
      return;
    }
    console.info('Callback invoked to indicate the session start success.');
  });
}

#### start11+

start(): Promise<void>

Starts this session. This API uses a promise to return the result.

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
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function startCaptureSession(session: camera.Session): void {
  session.start().then(() => {
    console.info('Promise returned to indicate the session start success.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to start the session, error code: ${error.code}.\`);
  });
}

#### stop11+

stop(callback: AsyncCallback<void>): void

Stops this session. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the session stops successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function stopCaptureSession(session: camera.Session): void {
  session.stop((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to stop the session, error code: ${err.code}.\`);
      return;
    }
    console.info('Callback invoked to indicate the session stop success.');
  });
}

#### stop11+

stop(): Promise<void>

Stops this session. This API uses a promise to return the result.

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

function stopCaptureSession(session: camera.Session): void {
  session.stop().then(() => {
    console.info('Promise returned to indicate the session stop success.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to stop the session, error code: ${error.code}.\`);
  });
}

#### release11+

release(callback: AsyncCallback<void>): void

Releases this session. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the session is released successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function releaseCaptureSession(session: camera.Session): void {
  session.release((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to release the session instance, error code: ${err.code}.\`);
      return;
    }
    console.info('Callback invoked to indicate that the session instance is released successfully.');
  });
}

#### release11+

release(): Promise<void>

Releases this session. This API uses a promise to return the result.

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

function releaseCaptureSession(session: camera.Session): void {
  session.release().then(() => {
    console.info('Promise returned to indicate that the session instance is released successfully.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to release the session instance, error code: ${error.code}.\`);
  });
}
