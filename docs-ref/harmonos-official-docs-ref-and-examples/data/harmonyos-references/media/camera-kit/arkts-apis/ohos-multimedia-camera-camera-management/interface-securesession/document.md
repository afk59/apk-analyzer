# Interface (SecureSession)

**SecureSession** inherits from [Session](../interface-session/document.md), [Flash](../interface-flash/document.md), [AutoExposure](../interface-autoexposure/document.md), [WhiteBalance](../interface-whitebalance/document.md), [Focus](../interface-focus/document.md), and [Zoom](../interface-zoom/document.md).

It implements a secure session, which provides operations on the flash, exposure, white balance, focus, and zoom.

You can call [createSession](../interface-cameramanager/document.md#createsession11) with [SceneMode](../enums/document.md#scenemode11) set to **SECURE\_PHOTO** to create a session in secure mode. The secure mode is designed for applications with high security requirements, such as facial recognition systems and banking services. It must be used together with the Device Security Kit to support service scenarios where both standard preview streams and security streams are output.For details, see [Secure Mode Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/camera-secure-photo).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/Ju3J0usRS5u9eTd7_BlIKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=174EC4A5377C11D3D94EE7B5ACC86B7812D6381D28B2762B521C7C26EB561DC9)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 12.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### addSecureOutput12+

addSecureOutput(previewOutput: PreviewOutput): void

Marks a [PreviewOutput](../interface-previewoutput/document.md) stream as secure output.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| previewOutput | [PreviewOutput](../interface-previewoutput/document.md) | Yes | Preview output stream. An error code is returned if the input parameter is invalid. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function addSecureOutput(session: camera.SecureSession, previewOutput: camera.PreviewOutput): void {
  try {
    session.addSecureOutput(previewOutput);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The addOutput call failed. error code: ${err.code}\`);
  }
}

#### on('error')12+

on(type: 'error', callback: ErrorCallback): void

Subscribes to SecureSession error events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/CPWjK2yXR6yJX8WYA1oLVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F12EADFC3E31F84AB8D41EC7A88DD9A901651AAD175665B979C9AFAAD8E191AA)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a session is created. This event is triggered and the error message is returned when an error occurs during the calling of a session-related API such as [beginConfig](../interface-session/document.md#beginconfig11), [commitConfig](../interface-session/document.md#commitconfig11-1), and [addInput](../interface-session/document.md#addinput11). |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | Yes | Callback used to return an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  console.error(\`Video session error code: ${err.code}\`);
}

function registerSessionError(secureSession: camera.SecureSession): void {
  secureSession.on('error', callback);
}

#### off('error')12+

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from SecureSession error events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a session is created. |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterSessionError(secureSession: camera.SecureSession): void {
  secureSession.off('error');
}

#### on('focusStateChange')12+

on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void

Subscribes to focus state change events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/i1-uJcmdTsKtC_9maEa5GQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A1A2E8ACA3A582A46411D4588AC2BEB1480136358E8034C34CAC2953916F6D1)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'focusStateChange'**. The event can be listened for when a session is created. This event is triggered only when the camera focus state changes in auto focus mode. |
| callback | AsyncCallback<[FocusState](../enums/document.md#focusstate)\> | Yes | Callback used to return the focus state change. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, focusState: camera.FocusState): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info(\`Focus state: ${focusState}\`);
}

function registerFocusStateChange(secureSession: camera.SecureSession): void {
  secureSession.on('focusStateChange', callback);
}

#### off('focusStateChange')12+

off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void

Unsubscribes from focus state change events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'focusStateChange'**. The event can be listened for when a session is created. |
| callback | AsyncCallback<[FocusState](../enums/document.md#focusstate)\> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterFocusStateChange(secureSession: camera.SecureSession): void {
  secureSession.off('focusStateChange');
}
