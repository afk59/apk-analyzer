# Deprecated Interface (CaptureSession, deprecated)

**CaptureSession** implements a capture session, which saves all [CameraInput](../interface-camerainput/document.md) and [CameraOutput](../interface-cameraoutput/document.md) instances required to run the camera and requests the camera to complete shooting or video recording.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/jLK6a5E0Q0edFBSbvlJJSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1344D314C14916187C267EB68CB3EFB79ADAA3D54B98CD04E10E688638C3C517)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [PhotoSession](../interface-photosession/document.md) and [VideoSession](../interface-videosession/document.md) instead.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### beginConfig(deprecated)

beginConfig(): void

Starts configuration for the session.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/ZhTY0CN0RSeeQTNPLZRlzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21FCBFF94AC2ADFEC0334E23BE088E7C01982237CE529AB8AD762CA2ED6921F7)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Session.beginConfig](../interface-session/document.md#beginconfig11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400105 | Session config locked. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function beginConfig(captureSession: camera.CaptureSession): void {
  try {
    captureSession.beginConfig();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The beginConfig call failed. error code: ${err.code}\`);
  }
}

#### commitConfig(deprecated)

commitConfig(callback: AsyncCallback<void>): void

Commits the configuration for this session. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/BPPCnVW0T-CrMmksIfbcnQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B067D6C0CA657794C5E7287C8D72D618976B0F015A7B4D649B707E910474B63)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Session.commitConfig](../interface-session/document.md#commitconfig11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the configuration is successfully committed, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function commitConfig(captureSession: camera.CaptureSession): void {
  captureSession.commitConfig((err: BusinessError) => {
    if (err) {
      console.error(\`The commitConfig call failed. error code: ${err.code}\`);
      return;
    }
    console.info('Callback invoked to indicate the commit config success.');
  });
}

#### commitConfig(deprecated)

commitConfig(): Promise<void>

Commits the configuration for this session. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/6P14p5caQdi6RNHJjpr6AA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC76D4B1FBFCB77F87C6C80B8B394888374726F4E154BEFF8D578FD51805AC8A)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Session.commitConfig](../interface-session/document.md#commitconfig11-1) instead.

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

function commitConfig(captureSession: camera.CaptureSession): void {
  captureSession.commitConfig().then(() => {
    console.info('Promise returned to indicate the commit config success.');
  }).catch((error: BusinessError) => {
    // If the operation fails, error.code is returned and processed.
    console.error(\`The commitConfig call failed. error code: ${error.code}\`);
  });
}

#### addInput(deprecated)

addInput(cameraInput: CameraInput): void

Adds a [CameraInput](../interface-camerainput/document.md) instance to this session.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/RsQJI1Q-TSSNrorvkqzhZg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=859CE4FC51670FB96E50A747F18AA612C3B93F7060734308C364A9E85A7BAF2E)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Session.addInput](../interface-session/document.md#addinput11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cameraInput | [CameraInput](../interface-camerainput/document.md) | Yes | CameraInput instance to add. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function addInput(captureSession: camera.CaptureSession, cameraInput: camera.CameraInput): void {
  try {
    captureSession.addInput(cameraInput);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The addInput call failed. error code: ${err.code}\`);
  }
}

#### removeInput(deprecated)

removeInput(cameraInput: CameraInput): void

Removes a [CameraInput](../interface-camerainput/document.md) instance from this session.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/29jNlmz-TGW9T0ViqzsLUA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=38259D6EC715A9021EC1B724BA98DF143941A2B04101576AEAD3E566DA339BC8)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Session.removeInput](../interface-session/document.md#removeinput11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cameraInput | [CameraInput](../interface-camerainput/document.md) | Yes | CameraInput instance to remove. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function removeInput(captureSession: camera.CaptureSession, cameraInput: camera.CameraInput): void {
  try {
    captureSession.removeInput(cameraInput);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The removeInput call failed. error code: ${err.code}\`);
  }
}

#### addOutput(deprecated)

addOutput(cameraOutput: CameraOutput): void

Adds a [CameraOutput](../interface-cameraoutput/document.md) instance to this session.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/-6hQA5qORcyfOIXnNWyiHA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8BD327B75EC0D7A3B72A6FADA68115BDAD3392EFFFF70E7192EADB09129BD86)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Session.addOutput](../interface-session/document.md#addoutput11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cameraOutput | [CameraOutput](../interface-cameraoutput/document.md) | Yes | CameraOutput instance to add. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function addOutput(captureSession: camera.CaptureSession, cameraOutput: camera.CameraOutput): void {
  try {
    captureSession.addOutput(cameraOutput);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The addOutput call failed. error code: ${err.code}\`);
  }
}

#### removeOutput(deprecated)

removeOutput(cameraOutput: CameraOutput): void

Removes a [CameraOutput](../interface-cameraoutput/document.md) instance from this session.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/FshPYBdhRJGlJd_UNc_hhA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E12DCA84E7D3C8AC4B0AB0598EA13521D2A9FDB91D7E7B3F0E96A7C93BB4A44)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Session.removeOutput](../interface-session/document.md#removeoutput11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cameraOutput | [CameraOutput](../interface-cameraoutput/document.md) | Yes | CameraOutput instance to remove. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function removeOutput(captureSession: camera.CaptureSession, previewOutput: camera.PreviewOutput): void {
  try {
    captureSession.removeOutput(previewOutput);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The removeOutput call failed. error code: ${err.code}\`);
  }
}

#### start(deprecated)

start(callback: AsyncCallback<void>): void

Starts this session. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/P-H26JZnQfKblwl7ziquhw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CAD4B2648F2045AC1605AAE631D1E8849BCCCF6CA49838CAC8666F63C0D412A)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Session.start](../interface-session/document.md#start11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the session starts successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function startCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.start((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to start the session, error code: ${err.code}.\`);
      return;
    }
    console.info('Callback invoked to indicate the session start success.');
  });
}

#### start(deprecated)

start(): Promise<void>

Starts this session. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/Cdc55WDxTkKZeboKPUhjAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=492AFEA234666BAD261F185D0601A265DA84603367CA50650E3D4CAC6FE53DC7)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Session.start](../interface-session/document.md#start11-1) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function startCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.start().then(() => {
    console.info('Promise returned to indicate the session start success.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to start the session, error code: ${err.code}.\`);
  });
}

#### stop(deprecated)

stop(callback: AsyncCallback<void>): void

Stops this session. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/yVO5ykyTTDyYF8qngbnVFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94BE06288E58781782FFA0787103E52850F4765B0ADAB9ECCCA7500B3E1C0EF6)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Session.stop](../interface-session/document.md#stop11) instead.

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

function stopCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.stop((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to stop the session, error code: ${err.code}.\`);
      return;
    }
    console.info('Callback invoked to indicate the session stop success.');
  });
}

#### stop(deprecated)

stop(): Promise<void>

Stops this session. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/bcBjNaefTAmVrJD0c52tYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58EEB32AFC36599C55D6B4C000C7A6597411948686CE9DE3E19673913B98AE3A)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Session.stop](../interface-session/document.md#stop11-1) instead.

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

function stopCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.stop().then(() => {
    console.info('Promise returned to indicate the session stop success.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to stop the session, error code: ${err.code}.\`);
  });
}

#### release(deprecated)

release(callback: AsyncCallback<void>): void

Releases this session. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/oD3CMhCUTRW_Io8WwT1xpA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65DEB99376DD8CE67A98BB9952CF3122353F9E75161FF995A08C2B6B51ABF82D)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Session.release](../interface-session/document.md#release11) instead.

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

function releaseCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.release((err: BusinessError) => {
    if (err) {
      console.error(\`Failed to release the CaptureSession instance, error code: ${err.code}.\`);
      return;
    }
    console.info('Callback invoked to indicate that the CaptureSession instance is released successfully.');
  });
}

#### release(deprecated)

release(): Promise<void>

Releases this session. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/0LPpMOJNRHmJxZ8PB8G5Bw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C05A269E877886C86DBBF156A33A6004750832466526B2C43EE09082AF4EF24)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Session.release](../interface-session/document.md#release11-1) instead.

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

function releaseCaptureSession(captureSession: camera.CaptureSession): void {
  captureSession.release().then(() => {
    console.info('Promise returned to indicate that the CaptureSession instance is released successfully.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to release the CaptureSession instance, error code: ${err.code}.\`);
  });
}

#### hasFlash(deprecated)

hasFlash(): boolean

Checks whether the camera device has flash.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/RdrfXHPQS1SZLP05YyUhCA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8FF5CC95ABD3636BDCB5067BBBB5F4D1F246672FE1B09C28EA2DB5C8A4422C4)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Flash.hasFlash](../interface-flashquery/document.md#hasflash11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the camera device has flash. **true** if it has flash, **false** otherwise. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function hasFlash(captureSession: camera.CaptureSession): boolean {
  let status: boolean = false;
  try {
    status = captureSession.hasFlash();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The hasFlash call failed. error code: ${err.code}\`);
  }
  return status;
}

#### isFlashModeSupported(deprecated)

isFlashModeSupported(flashMode: FlashMode): boolean

Checks whether the flash mode is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/4a76WcOsTEKsSWF34F_v7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10C47674C32C3F9731D7856E32302E982EB637185C2A7343E716F58523EB297F)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Flash.isFlashModeSupported](../interface-flashquery/document.md#isflashmodesupported11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| flashMode | [FlashMode](../enums/document.md#flashmode) | Yes | Flash mode. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of the flash mode. **true** if supported, **false** otherwise. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function isFlashModeSupported(captureSession: camera.CaptureSession): boolean {
  let status: boolean = false;
  try {
    status = captureSession.isFlashModeSupported(camera.FlashMode.FLASH\_MODE\_AUTO);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The isFlashModeSupported call failed. error code: ${err.code}\`);
  }
  return status;
}

#### setFlashMode(deprecated)

setFlashMode(flashMode: FlashMode): void

Sets a flash mode.

Before the setting, do the following checks:

1.  Use [hasFlash](#hasflashdeprecated) to check whether the camera device has flash.
2.  Use [isFlashModeSupported](#isflashmodesupporteddeprecated) to check whether the camera device supports the flash mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/aw6ehk9NSNiHKJs07QZ47g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97D7DD716B7B21F6E4A882C646E385B0CD2A4003A0B1C4C8BFB87AE3F3438AEC)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Flash.setFlashMode](../interface-flash/document.md#setflashmode11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| flashMode | [FlashMode](../enums/document.md#flashmode) | Yes | Flash mode. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setFlashMode(captureSession: camera.CaptureSession): void {
  try {
    captureSession.setFlashMode(camera.FlashMode.FLASH\_MODE\_AUTO);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The setFlashMode call failed. error code: ${err.code}\`);
  }
}

#### getFlashMode(deprecated)

getFlashMode(): FlashMode

Obtains the flash mode in use.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/vGX0Peh2Sbq6Ebn4FnIQzQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD06B0BB5754A596232D439E4FE2BAD5B6AC74F3B9A22A12A166B0430CC9568C)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Flash.getFlashMode](../interface-flash/document.md#getflashmode11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [FlashMode](../enums/document.md#flashmode) | Flash mode obtained. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getFlashMode(captureSession: camera.CaptureSession): camera.FlashMode | undefined {
  let flashMode: camera.FlashMode | undefined = undefined;
  try {
    flashMode = captureSession.getFlashMode();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getFlashMode call failed.error code: ${err.code}\`);
  }
  return flashMode;
}

#### isExposureModeSupported(deprecated)

isExposureModeSupported(aeMode: ExposureMode): boolean

Checks whether an exposure mode is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/FV1XrITlSGmaCoyNt7Qr1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0A1A16EF56EE316B0CD832DFFF5561BAC0A29DD853BE26ABB3F0F61E9586979)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [AutoExposure.isExposureModeSupported](../interface-autoexposurequery/document.md#isexposuremodesupported11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| aeMode | [ExposureMode](../enums/document.md#exposuremode) | Yes | Exposure mode. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of the exposure mode. **true** if supported, **false** otherwise. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function isExposureModeSupported(captureSession: camera.CaptureSession): boolean {
  let isSupported: boolean = false;
  try {
    isSupported = captureSession.isExposureModeSupported(camera.ExposureMode.EXPOSURE\_MODE\_LOCKED);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The isExposureModeSupported call failed. error code: ${err.code}\`);
  }
  return isSupported;
}

#### getExposureMode(deprecated)

getExposureMode(): ExposureMode

Obtains the exposure mode in use.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/IEjF7u6BRa2Ilw08gB7YIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69A40881E1B62084927530099D6CAF735F258D0907FE09593E56C8DF08D30884)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [AutoExposure.getExposureMode](../interface-autoexposure/document.md#getexposuremode11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ExposureMode](../enums/document.md#exposuremode) | Exposure mode obtained. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getExposureMode(captureSession: camera.CaptureSession): camera.ExposureMode | undefined {
  let exposureMode: camera.ExposureMode | undefined = undefined;
  try {
    exposureMode = captureSession.getExposureMode();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getExposureMode call failed. error code: ${err.code}\`);
  }
  return exposureMode;
}

#### setExposureMode(deprecated)

setExposureMode(aeMode: ExposureMode): void

Sets an exposure mode. Before the setting, call [isExposureModeSupported](#isexposuremodesupporteddeprecated) to check whether the target exposure mode is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/XjKw0OWTQVSBLR8XvX2-7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B594EB4A77C3E3E5722B32C495EA4776485A00B55CE07E7898EBFDAB62FDC48)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [AutoExposure.setExposureMode](../interface-autoexposure/document.md#setexposuremode11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| aeMode | [ExposureMode](../enums/document.md#exposuremode) | Yes | Exposure mode. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setExposureMode(captureSession: camera.CaptureSession): void {
  try {
    captureSession.setExposureMode(camera.ExposureMode.EXPOSURE\_MODE\_LOCKED);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The setExposureMode call failed. error code: ${err.code}\`);
  }
}

#### getMeteringPoint(deprecated)

getMeteringPoint(): Point

Obtains the metering point of the camera device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/djQZMSZ3TkGToOmI47WgAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=200FF1CD97F68F1AE4B8854D0812E4C201D76969827A4010CB8CC2A01191234F)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [AutoExposure.getMeteringPoint](../interface-autoexposure/document.md#getmeteringpoint11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Point](../interfaces-others/document.md#point) | Metering point obtained. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getMeteringPoint(captureSession: camera.CaptureSession): camera.Point | undefined {
  let exposurePoint: camera.Point | undefined = undefined;
  try {
    exposurePoint = captureSession.getMeteringPoint();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getMeteringPoint call failed. error code: ${err.code}\`);
  }
  return exposurePoint;
}

#### setMeteringPoint(deprecated)

setMeteringPoint(point: Point): void

Sets the metering point, which is the center point of the metering rectangle. The metering point must be in the coordinate system (0-1), where the top-left corner is {0, 0} and the bottom-right corner is {1, 1}.

The coordinate system is based on the horizontal device direction with the device's charging port on the right. If the layout of the preview screen of an application is based on the vertical direction with the charging port on the lower side, the layout width and height are {w, h}, and the touch point is {x, y}, then the coordinate point after conversion is {y/h, 1-x/w}.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/nx8X3PtvRoiDxaM6kV-1yA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16326AA17884A0F6A9E522D86FB4DDDF7CB400252C21207976613CCD9629D27A)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [AutoExposure.setMeteringPoint](../interface-autoexposure/document.md#setmeteringpoint11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| point | [Point](../interfaces-others/document.md#point) | Yes | Metering point. The value range of x and y must be within \[0,1\]. If a value less than 0 is passed, the value **0** is used. If a value greater than **1** is passed, the value **1** is used. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setMeteringPoint(captureSession: camera.CaptureSession): void {
  const point: camera.Point = {x: 1, y: 1};
  try {
    captureSession.setMeteringPoint(point);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The setMeteringPoint call failed. error code: ${err.code}\`);
  }
}

#### getExposureBiasRange(deprecated)

getExposureBiasRange(): Array<number>

Obtains the exposure compensation values of the camera device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/J6kf5rlKQgivcjOJB9l5_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A5EF53B7AA5A6376161D865425211CD2809E7C863EB95F4571E9F7EB3841B9A)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [AutoExposure.getExposureBiasRange](../interface-autoexposurequery/document.md#getexposurebiasrange11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<number> | Array of compensation values. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getExposureBiasRange(captureSession: camera.CaptureSession): Array<number> {
  let biasRangeArray: Array<number> = \[\];
  try {
    biasRangeArray = captureSession.getExposureBiasRange();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getExposureBiasRange call failed. error code: ${err.code}\`);
  }
  return biasRangeArray;
}

#### setExposureBias(deprecated)

setExposureBias(exposureBias: number): void

Sets an exposure compensation value (EV).

Before the setting, you are advised to use [getExposureBiasRange](#getexposurebiasrangedeprecated) to obtain the supported values.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/_6Ws3cxlS9-mZhjiU2fY5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1CCA0CECDA5950C73D6F694D585F99402D56FC4CCB8F24792D7CA65DF6DFE60A)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [AutoExposure.setExposureBias](../interface-autoexposure/document.md#setexposurebias11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| exposureBias | number | Yes | EV. The supported EV range can be obtained by calling [getExposureBiasRange](../interface-autoexposurequery/document.md#getexposurebiasrange11). If the value passed is not within the supported range, the nearest critical point is used. There is a step for EV. For example, if the step is 0.5 and this parameter is set to 1.2, the EV that takes effect is 1.0. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. If the input parameter is null or undefined, the EV is set to 0. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setExposureBias(captureSession: camera.CaptureSession, biasRangeArray: Array<number>): void {
  if (biasRangeArray && biasRangeArray.length > 0) {
    let exposureBias = biasRangeArray\[0\];
    try {
      captureSession.setExposureBias(exposureBias);
    } catch (error) {
      // If the operation fails, error.code is returned and processed.
      let err = error as BusinessError;
      console.error(\`The setExposureBias call failed. error code: ${err.code}\`);
    }
  }
}

#### getExposureValue(deprecated)

getExposureValue(): number

Obtains the exposure value in use.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/MjA3Ol8xTMKfCcPFg8l_9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16C035B4CEB32F6DC794AB8B69D092F37F82EF862E4ECB07BBD2A2037E9E085C)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [AutoExposure.getExposureValue](../interface-autoexposure/document.md#getexposurevalue11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Exposure value obtained. There is a step for EV. For example, if the step is 0.5 and this parameter is set to 1.2, the EV that takes effect is 1.0. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getExposureValue(captureSession: camera.CaptureSession): number {
  const invalidValue: number = -1;
  let exposureValue: number = invalidValue;
  try {
    exposureValue = captureSession.getExposureValue();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getExposureValue call failed. error code: ${err.code}\`);
  }
  return exposureValue;
}

#### isFocusModeSupported(deprecated)

isFocusModeSupported(afMode: FocusMode): boolean

Checks whether a focus mode is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/a2LFFKNhRFOk96FNceiDgA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7F9344C4C037A2141C976FCB0B7A62B99927E6292909F767DBC8A2AB6CE0AE3)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Focus.isFocusModeSupported](../interface-focusquery/document.md#isfocusmodesupported11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| afMode | [FocusMode](../enums/document.md#focusmode) | Yes | Focus mode. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of the focus mode. **true** if supported, **false** otherwise. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function isFocusModeSupported(captureSession: camera.CaptureSession): boolean {
  let status: boolean = false;
  try {
    status = captureSession.isFocusModeSupported(camera.FocusMode.FOCUS\_MODE\_AUTO);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The isFocusModeSupported call failed. error code: ${err.code}\`);
  }
  return status;
}

#### setFocusMode(deprecated)

setFocusMode(afMode: FocusMode): void

Sets a focus mode.

Before the setting, call [isFocusModeSupported](#isfocusmodesupporteddeprecated) to check whether the focus mode is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/SAlBDROGSiiuRtSrh3RF5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05ECF486637DB562754406D518D5BAD4644B8D634EABD55C7D3F743DC29440D6)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Focus.setFocusMode](../interface-focus/document.md#setfocusmode11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| afMode | [FocusMode](../enums/document.md#focusmode) | Yes | Focus mode. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setFocusMode(captureSession: camera.CaptureSession): void {
  try {
    captureSession.setFocusMode(camera.FocusMode.FOCUS\_MODE\_AUTO);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The setFocusMode call failed. error code: ${err.code}\`);
  }
}

#### getFocusMode(deprecated)

getFocusMode(): FocusMode

Obtains the focus mode in use.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/RcVdB0WHSNiSUTj7E_uoWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC8306761BD7DB1F38508AFA759E3B421496B0B714ACF5CEA0B3C6B867092A67)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Focus.getFocusMode](../interface-focus/document.md#getfocusmode11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [FocusMode](../enums/document.md#focusmode) | Focus mode obtained. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getFocusMode(captureSession: camera.CaptureSession): camera.FocusMode | undefined {
  let afMode: camera.FocusMode | undefined = undefined;
  try {
    afMode = captureSession.getFocusMode();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getFocusMode call failed. error code: ${err.code}\`);
  }
  return afMode;
}

#### setFocusPoint(deprecated)

setFocusPoint(point: Point): void

Sets the focal point. The focal point must be in the coordinate system (0-1), where the top-left corner is {0, 0} and the bottom-right corner is {1, 1}.

The coordinate system is based on the horizontal device direction with the device's charging port on the right. If the layout of the preview screen of an application is based on the vertical direction with the charging port on the lower side, the layout width and height are {w, h}, and the touch point is {x, y}, then the coordinate point after conversion is {y/h, 1-x/w}.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/1Rmq99CwRQyTqgkSdYty0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F6F9893244F1160E657222506AD60D5F79837661326A3154E057E52190B571D1)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Focus.setFocusPoint](../interface-focus/document.md#setfocuspoint11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| point | [Point](../interfaces-others/document.md#point) | Yes | Focal point. The value range of x and y must be within \[0,1\]. If a value less than 0 is passed, the value **0** is used. If a value greater than **1** is passed, the value **1** is used. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setFocusPoint(captureSession: camera.CaptureSession): void {
  const focusPoint: camera.Point = {x: 1, y: 1};
  try {
    captureSession.setFocusPoint(focusPoint);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The setFocusPoint call failed. error code: ${err.code}\`);
  }
}

#### getFocusPoint(deprecated)

getFocusPoint(): Point

Obtains the focal point of the camera device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/flEAfoumQB-Yp8uuNeGjBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D542D0D8D9B90D2D4BBDC5D94804862F325741719C92C14D0D682D2565D13A30)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Focus.getFocusPoint](../interface-focus/document.md#getfocuspoint11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Point](../interfaces-others/document.md#point) | Focal point obtained. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getFocusPoint(captureSession: camera.CaptureSession): camera.Point | undefined {
  let point: camera.Point | undefined = undefined;
  try {
    point = captureSession.getFocusPoint();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getFocusPoint call failed. error code: ${err.code}\`);
  }
  return point;
}

#### getFocalLength(deprecated)

getFocalLength(): number

Obtains the focal length of the camera device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/WrR4HUu2R1CluKneIZlOGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8ABE5CBC8D2F9B7506AECEC95C6D21BCDAA2DA5C58045A856503CFBBA422178)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Focus.getFocalLength](../interface-focus/document.md#getfocallength11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Focal length obtained. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getFocalLength(captureSession: camera.CaptureSession): number {
  const invalidValue: number = -1;
  let focalLength: number = invalidValue;
  try {
    focalLength = captureSession.getFocalLength();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getFocalLength call failed. error code: ${err.code}\`);
  }
  return focalLength;
}

#### getZoomRatioRange(deprecated)

getZoomRatioRange(): Array<number>

Obtains the supported zoom ratio range.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/35AcCkaTSfGzshFM7Hlq1A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4147A8CA32A9131B9ACF1299F55E3FF5E57921191CDE3BCA9CC6FA7662BEA08B)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Zoom.getZoomRatioRange](../interface-zoomquery/document.md#getzoomratiorange11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<number> | Array containing the minimum and maximum zoom ratios. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getZoomRatioRange(captureSession: camera.CaptureSession): Array<number> {
  let zoomRatioRange: Array<number> = \[\];
  try {
    zoomRatioRange = captureSession.getZoomRatioRange();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getZoomRatioRange call failed. error code: ${err.code}\`);
  }
  return zoomRatioRange;
}

#### setZoomRatio(deprecated)

setZoomRatio(zoomRatio: number): void

Sets a zoom ratio, with a maximum precision of two decimal places.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/WrGnKVmMQzyllX0uVayGzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FDBCB7D0911BD55D62FE373C5C46F898E5D63FA2775375A163CB27370CFC216D)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Zoom.setZoomRatio](../interface-zoom/document.md#setzoomratio11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| zoomRatio | number | Yes | Zoom ratio. The supported zoom ratio range can be obtained by calling [getZoomRatioRange](../interface-zoomquery/document.md#getzoomratiorange11). If the value passed in is not within the supported range, the value within the precision range is retained. If the input parameter is null or undefined, it is treated as 0 and the minimum zoom ratio is used. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setZoomRatio(captureSession: camera.CaptureSession, zoomRatioRange: Array<number>): void {
  if (zoomRatioRange === undefined || zoomRatioRange.length <= 0) {
    return;
  }
  let zoomRatio = zoomRatioRange\[0\];
  try {
    captureSession.setZoomRatio(zoomRatio);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The setZoomRatio call failed. error code: ${err.code}\`);
  }
}

#### getZoomRatio(deprecated)

getZoomRatio(): number

Obtains the zoom ratio in use.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/WSQmahb-R7W11nZGbDvv0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8ECCAF8A5CA3EB87591F416251AE68B6E91D3A4F57D2A80B8F626E15A38A591C)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Zoom.getZoomRatio](../interface-zoom/document.md#getzoomratio11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Zoom ratio obtained. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getZoomRatio(captureSession: camera.CaptureSession): number {
  const invalidValue: number = -1;
  let zoomRatio: number = invalidValue;
  try {
    zoomRatio = captureSession.getZoomRatio();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getZoomRatio call failed. error code: ${err.code}\`);
  }
  return zoomRatio;
}

#### isVideoStabilizationModeSupported(deprecated)

isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): boolean

Checks whether a video stabilization mode is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/ZGWsRaZxQoCbKuEMDJrnaw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9030AA364C02FE31BF7EA4CB3E3639DF9091CF9429335B3CFFA4096CAEDB3833)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Stabilization.isVideoStabilizationModeSupported](../interface-stabilizationquery/document.md#isvideostabilizationmodesupported11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| vsMode | [VideoStabilizationMode](../enums/document.md#videostabilizationmode) | Yes | Video stabilization mode. If the input parameter is null or undefined, it is treated as 0 and video stabilization is disabled. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of the video stabilization mode. **true** if supported, **false** otherwise. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function isVideoStabilizationModeSupported(captureSession: camera.CaptureSession): boolean {
  let isSupported: boolean = false;
  try {
    isSupported = captureSession.isVideoStabilizationModeSupported(camera.VideoStabilizationMode.OFF);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The isVideoStabilizationModeSupported call failed. error code: ${err.code}\`);
  }
  return isSupported;
}

#### getActiveVideoStabilizationMode(deprecated)

getActiveVideoStabilizationMode(): VideoStabilizationMode

Obtains the video stabilization mode in use.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/O6GCebkDQyqLkgI1zz5U9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=807674A528D92AB0D519E6D773B27133FD4974141A91FC92DF6B45C290B2F5B8)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Stabilization.getActiveVideoStabilizationMode](../interface-stabilization/document.md#getactivevideostabilizationmode11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [VideoStabilizationMode](../enums/document.md#videostabilizationmode) | Video stabilization mode obtained. If the operation fails, an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getActiveVideoStabilizationMode(captureSession: camera.CaptureSession): camera.VideoStabilizationMode | undefined {
  let vsMode: camera.VideoStabilizationMode | undefined = undefined;
  try {
    vsMode = captureSession.getActiveVideoStabilizationMode();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getActiveVideoStabilizationMode call failed. error code: ${err.code}\`);
  }
  return vsMode;
}

#### setVideoStabilizationMode(deprecated)

setVideoStabilizationMode(mode: VideoStabilizationMode): void

Sets a video stabilization mode. Before the setting, call [isVideoStabilizationModeSupported](#isvideostabilizationmodesupporteddeprecated) to check whether the target video stabilization mode is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/s9z6Qo4sRQacuVe06rlCuA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A605EF3086BE83C96C10D47759BFF6F7FEEE617DD8748ADF3587E75AFB762F9)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [Stabilization.setVideoStabilizationMode](../interface-stabilization/document.md#setvideostabilizationmode11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [VideoStabilizationMode](../enums/document.md#videostabilizationmode) | Yes | Video stabilization mode. If the input parameter is null or undefined, it is treated as 0 and video stabilization is disabled. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setVideoStabilizationMode(captureSession: camera.CaptureSession): void {
  try {
    captureSession.setVideoStabilizationMode(camera.VideoStabilizationMode.OFF);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The setVideoStabilizationMode call failed. error code: ${err.code}\`);
  }
}

#### on('focusStateChange')(deprecated)

on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void

Subscribes to focus state change events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/AhEDikhhTM6hoknWdnoA7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A3C7ACB79865B3907C8F2630BAC039715838B74D0C8A47F71B1E50F2C200783)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [VideoSession.on('focusStateChange')](../interface-videosession/document.md#onfocusstatechange11) instead.

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'focusStateChange'**. The event can be listened for when a session is created. This event is triggered only when the camera focus state changes in auto focus mode. |
| callback | AsyncCallback<[FocusState](../enums/document.md#focusstate)\> | Yes | Callback used to return the focus state change. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function registerFocusStateChange(captureSession: camera.CaptureSession): void {
  captureSession.on('focusStateChange', (err: BusinessError, focusState: camera.FocusState) => {
    if (err !== undefined && err.code !== 0) {
      console.error(\`Callback Error, errorCode: ${err.code}\`);
      return;
    }
    console.info(\`Focus state: ${focusState}\`);
  });
}

#### off('focusStateChange')(deprecated)

off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void

Unsubscribes from focus state change events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/IorIk1g2T7WweUeiX_0ZxA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F0E0F5B6F616D8E27309E4B8BE85FA2CFF532840706F99C1A9C85554611EDAB8)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [VideoSession.off('focusStateChange')](../interface-videosession/document.md#offfocusstatechange11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'focusStateChange'**. The event can be listened for when a session is created. |
| callback | AsyncCallback<[FocusState](../enums/document.md#focusstate)\> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterFocusStateChange(captureSession: camera.CaptureSession): void {
  captureSession.off('focusStateChange');
}

#### on('error')(deprecated)

on(type: 'error', callback: ErrorCallback): void

Subscribes to CaptureSession error events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/BrJ2783MROOP7lZ8050HFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5F45BF6DF72D73BDE099C3BA619A6C8CC951F0A0359354ACF9560A3674FC863)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [VideoSession.on('error')](../interface-videosession/document.md#onerror11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a session is created. This event is triggered and the error message is returned when an error occurs during the calling of a session-related API such as [beginConfig](#beginconfigdeprecated), [commitConfig](#commitconfigdeprecated-1), and [addInput](#addinputdeprecated). |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | Yes | Callback used to return an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function registerCaptureSessionError(captureSession: camera.CaptureSession): void {
  captureSession.on('error', (error: BusinessError) => {
    console.error(\`Capture session error code: ${error.code}\`);
  });
}

#### off('error')(deprecated)

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from CaptureSession error events. This API uses a callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/aHsqxh2JQKuW9WiQMELIzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C7FFEF303B279EE29837E9D05612E252D9B67D61EB1FA40CD71B98CA4F1F150)

This API is supported since API version 10 and deprecated since API version 11. You are advised to use [VideoSession.off('error')](../interface-videosession/document.md#offerror11) instead.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a session is created. |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterCaptureSessionError(captureSession: camera.CaptureSession): void {
  captureSession.off('error');
}
