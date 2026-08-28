# Interface (PhotoSession)

**PhotoSession** inherits from [Session](../interface-session/document.md), [Flash](../interface-flash/document.md), [AutoExposure](../interface-autoexposure/document.md), [WhiteBalance](../interface-whitebalance/document.md), [Focus](../interface-focus/document.md), [Zoom](../interface-zoom/document.md), [ColorManagement](../interface-colormanagement/document.md), [AutoDeviceSwitch](../interface-autodeviceswitch/document.md), and [Macro](../interface-macro/document.md).

It implements a photo session, which provides operations on the flash, exposure, white balance, focus, zoom, color space, and macro mode.

**PhotoSession** is provided for the default photo mode. It is used to take standard photos. It supports multiple photo formats and resolutions, which are suitable for most daily photo capture scenarios.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/o8nLBR4mREyuERv03pdDwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED9EA3940F334B896C70359FB177DEA9F307D134FF993312AA6AAA9DA671B189)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 11.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### canPreconfig12+

canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean

Checks whether this session supports a preconfigured resolution.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| preconfigType | [PreconfigType](../enums/document.md#preconfigtype12) | Yes | Resolution type. |
| preconfigRatio | [PreconfigRatio](../enums/document.md#preconfigratio12) | No | Aspect ratio. The default value is 4:3. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether a preconfigured resolution is supported. **true** if supported, **false** otherwise. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function testCanPreconfig(photoSession: camera.PhotoSession, preconfigType: camera.PreconfigType,
  preconfigRatio: camera.PreconfigRatio): void {
  try {
    let result = photoSession.canPreconfig(preconfigType, preconfigRatio);
    console.info(\`canPreconfig ${preconfigType} ${preconfigRatio} result is : ${result}\`);
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`The canPreconfig call failed. error code: ${err.code}\`);
  }
}

#### preconfig12+

preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void

Preconfigures this session.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| preconfigType | [PreconfigType](../enums/document.md#preconfigtype12) | Yes | Resolution type. |
| preconfigRatio | [PreconfigRatio](../enums/document.md#preconfigratio12) | No | Aspect ratio. The default value is 4:3. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function testPreconfig(photoSession: camera.PhotoSession, preconfigType: camera.PreconfigType,
  preconfigRatio: camera.PreconfigRatio): void {
  try {
    photoSession.preconfig(preconfigType, preconfigRatio);
    console.info(\`preconfig success preconfigType: ${preconfigType}, preconfigRatio: ${preconfigRatio}\`);
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`The preconfig call failed. error code: ${err.code}\`);
  }
}

#### on('error')11+

on(type: 'error', callback: ErrorCallback): void

Subscribes to **PhotoSession** error events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/CxoOupFhQ6aQdWYzw6_zPw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F6209A07532484945A2095407F2271BDB7C7048BA93FB2F68785DEE00CABF0C)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a session is created. This event is triggered and the error message is returned when an error occurs during the calling of a session-related API such as [beginConfig](../interface-session/document.md#beginconfig11), [commitConfig](../interface-session/document.md#commitconfig11), and [addInput](../interface-session/document.md#addinput11). |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | Yes | Callback used to return an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode). |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError): void {
  console.error(\`Photo session error code: ${err.code}\`);
}

function registerSessionError(photoSession: camera.PhotoSession): void {
  photoSession.on('error', callback);
}

#### off('error')11+

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from **PhotoSession** error events. This API uses a callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a session is created. |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterSessionError(photoSession: camera.PhotoSession): void {
  photoSession.off('error');
}

#### on('focusStateChange')11+

on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void

Subscribes to focus state change events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/wdkSqCTwTgGk9QuelxBHRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60ECE612E3BEC58A1DF5FEF34F20E0B8BB51E13C05F7BC4371C1461F50713D93)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'focusStateChange'**. The event can be listened for when a session is created. This event is triggered only when the camera focus state changes in autofocus mode. |
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

function registerFocusStateChange(photoSession: camera.PhotoSession): void {
  photoSession.on('focusStateChange', callback);
}

#### off('focusStateChange')11+

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

function unregisterFocusStateChange(photoSession: camera.PhotoSession): void {
  photoSession.off('focusStateChange');
}

#### on('smoothZoomInfoAvailable')11+

on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void

Subscribes to smooth zoom state change events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/pAUVXWtlSFGv2aloWD6axQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1F97F5A7C2496AC22F4EF29CF0327C15E22CFF06ECB3643D63ED486986FF98A)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'smoothZoomInfoAvailable'**. The event can be listened for when a session is created. |
| callback | AsyncCallback<[SmoothZoomInfo](../interfaces-others/document.md#smoothzoominfo11)\> | Yes | Callback used to return the smooth zoom state change. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, smoothZoomInfo: camera.SmoothZoomInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info(\`The duration of smooth zoom: ${smoothZoomInfo.duration}\`);
}

function registerSmoothZoomInfo(photoSession: camera.PhotoSession): void {
  photoSession.on('smoothZoomInfoAvailable', callback);
}

#### off('smoothZoomInfoAvailable')11+

off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback<SmoothZoomInfo>): void

Unsubscribes from smooth zoom state change events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'smoothZoomInfoAvailable'**. The event can be listened for when a session is created. |
| callback | AsyncCallback<[SmoothZoomInfo](../interfaces-others/document.md#smoothzoominfo11)\> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterSmoothZoomInfo(photoSession: camera.PhotoSession): void {
  photoSession.off('smoothZoomInfoAvailable');
}

#### on('autoDeviceSwitchStatusChange')13+

on(type: 'autoDeviceSwitchStatusChange', callback: AsyncCallback<AutoDeviceSwitchStatus>): void

Subscribes to automatic camera switch status change events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/59HAvMeqTG2bqAnKQK1Ydw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A55B276297C4BD9A04A50511818B3461965760F27727AF8D45F229E3324076F1)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'autoDeviceSwitchStatusChange'**. The event can be listened for when a session is created. |
| callback | AsyncCallback<[AutoDeviceSwitchStatus](../interfaces-others/document.md#autodeviceswitchstatus13)\> | Yes | Callback function, which is used to obtain the status of automatic camera switch. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, autoDeviceSwitchStatus: camera.AutoDeviceSwitchStatus): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info(\`isDeviceSwitched: ${autoDeviceSwitchStatus.isDeviceSwitched}, isDeviceCapabilityChanged: ${autoDeviceSwitchStatus.isDeviceCapabilityChanged}\`);
}

function registerAutoDeviceSwitchStatus(photoSession: camera.PhotoSession): void {
  photoSession.on('autoDeviceSwitchStatusChange', callback);
}

#### off('autoDeviceSwitchStatusChange')13+

off(type: 'autoDeviceSwitchStatusChange', callback?: AsyncCallback<AutoDeviceSwitchStatus>): void

Unsubscribes from automatic camera switch status change events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'autoDeviceSwitchStatusChange'**. The event can be listened for when a session is created. |
| callback | AsyncCallback<[AutoDeviceSwitchStatus](../interfaces-others/document.md#autodeviceswitchstatus13)\> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterSmoothZoomInfo(photoSession: camera.PhotoSession): void {
  photoSession.off('autoDeviceSwitchStatusChange');
}

#### on('systemPressureLevelChange')20+

on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void

Subscribes to system pressure level change events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/JiJHbyqWQkeVMKc-hqElfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9DCA7CC7F1E7A682AAD010C2C77563524E4F0C39D85CCCFA030C7006D76C76AE)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'systemPressureLevelChange'**. The event can be listened for when a session is created. |
| callback | AsyncCallback<[SystemPressureLevel](../enums/document.md#systempressurelevel20)\> | Yes | Callback used to return the current system pressure level. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, systemPressureLevel: camera.SystemPressureLevel): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info(\`systemPressureLevel: ${systemPressureLevel}\`);
}

function registerSystemPressureLevelChangeCallback(photoSession: camera.PhotoSession): void {
    photoSession.on('systemPressureLevelChange', callback);
}

#### off('systemPressureLevelChange')20+

off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void

Unsubscribes from system pressure level change events.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'systemPressureLevelChange'**. The event can be listened for when a session is created. |
| callback | AsyncCallback<[SystemPressureLevel](../enums/document.md#systempressurelevel20)\> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterSystemPressureLevelChangeCallback(photoSession: camera.PhotoSession): void {
  photoSession.off('systemPressureLevelChange');
}

#### on('macroStatusChanged')20+

on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void

Subscribes to macro state change events. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'macroStatusChanged'**. The event can be listened for when a session is created. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the macro state. **true** if enabled, **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, macroStatus: boolean): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info(\`Macro state: ${macroStatus}\`);
}

function registerMacroStatusChanged(photoSession: camera.PhotoSession): void {
  photoSession.on('macroStatusChanged', callback);
}

#### off('macroStatusChanged')20+

off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void

Unsubscribes from macro state change events.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'macroStatusChanged'**. The event can be listened for when a session is created. |
| callback | AsyncCallback<boolean> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterMacroStatusChanged(photoSession: camera.PhotoSession): void {
  photoSession.off('macroStatusChanged');
}
