# Interface (VideoSession)

**VideoSession** inherits from [Session](../interface-session/document.md), [Flash](../interface-flash/document.md), [AutoExposure](../interface-autoexposure/document.md), [WhiteBalance](../interface-whitebalance/document.md), [Focus](../interface-focus/document.md), [Zoom](../interface-zoom/document.md), [Stabilization](../interface-stabilization/document.md), [ColorManagement](../interface-colormanagement/document.md), [AutoDeviceSwitch](../interface-autodeviceswitch/document.md), [Macro](../interface-macro/document.md), and [ControlCenter](../interface-controlcenter/document.md).

It implements a video session, which provides operations on the flash, exposure, white balance, focus, zoom, video stabilization, color space, macro mode, and controller.

**VideoSession** is provided for the default video recording mode. It applies to common scenarios. It supports recording at various resolutions (such as 720p and 1080p) and frame rates (such as 30 fps and 60 fps).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/kZQ8PRVrQ7StaswBY1N-1A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BF108B411C5368D77126EBAEFA59704437B62D9F7AE60F8BB14401DA3501335)

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
| preconfigRatio | [PreconfigRatio](../enums/document.md#preconfigratio12) | No | Aspect ratio. The default value is 16:9. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
**true**: The preconfigured resolution is supported.

**false**: The preconfigured resolution is not supported.

 |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function testCanPreconfig(videoSession: camera.VideoSession, preconfigType: camera.PreconfigType,
  preconfigRatio: camera.PreconfigRatio): void {
  try {
    let result = videoSession.canPreconfig(preconfigType, preconfigRatio);
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
| preconfigRatio | [PreconfigRatio](../enums/document.md#preconfigratio12) | No | Aspect ratio. The default value is 16:9. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function testPreconfig(videoSession: camera.VideoSession, preconfigType: camera.PreconfigType,
  preconfigRatio: camera.PreconfigRatio): void {
  try {
    videoSession.preconfig(preconfigType, preconfigRatio);
    console.info(\`preconfig ${preconfigType} ${preconfigRatio} success\`);
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`The preconfig call failed. error code: ${err.code}\`);
  }
}

#### on('error')11+

on(type: 'error', callback: ErrorCallback): void

Subscribes to **VideoSession** error events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/D9CiGOaGTmmEzK52yqrCzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C5682CC3994D02E124BB4CB2C145AD915FCF59E0FEA2EAA231D432361773EE4)

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
  console.error(\`Video session error code: ${err.code}\`);
}

function registerSessionError(videoSession: camera.VideoSession): void {
  videoSession.on('error', callback);
}

#### off('error')11+

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from **VideoSession** error events. This API uses a callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'error'**. The event can be listened for when a session is created. |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterSessionError(videoSession: camera.VideoSession): void {
  videoSession.off('error');
}

#### on('focusStateChange')11+

on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void

Subscribes to focus state change events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/xm8ub_yjRly4iCfjtpM4vw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=989FF07CC2C745A5FDF90619659B5EDF4FD681716AAD44968F683AA342264E2C)

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

function registerFocusStateChange(videoSession: camera.VideoSession): void {
  videoSession.on('focusStateChange', callback);
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

function unregisterFocusStateChange(videoSession: camera.VideoSession): void {
  videoSession.off('focusStateChange');
}

#### on('smoothZoomInfoAvailable')11+

on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void

Subscribes to smooth zoom state change events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/Mo-bTyvhROqpUPP_clpSVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7581DB19C39284D11B083E658AB5E9CDA73FCB8043C79A1A66A9CCEEA386C9F)

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

function registerSmoothZoomInfo(videoSession: camera.VideoSession): void {
  videoSession.on('smoothZoomInfoAvailable', callback);
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

function unregisterSmoothZoomInfo(videoSession: camera.VideoSession): void {
  videoSession.off('smoothZoomInfoAvailable');
}

#### on('autoDeviceSwitchStatusChange')13+

on(type: 'autoDeviceSwitchStatusChange', callback: AsyncCallback<AutoDeviceSwitchStatus>): void

Subscribes to automatic camera switch status change events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/bmD2C4lcQi-MqzLtRLjG-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=863E0B147A60A9BF079AC34BEE9FFEEA93B7D0E335616E96F98AF7170479431B)

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

function registerAutoDeviceSwitchStatus(videoSession: camera.VideoSession): void {
  videoSession.on('autoDeviceSwitchStatusChange', callback);
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

function unregisterSmoothZoomInfo(videoSession: camera.VideoSession): void {
  videoSession.off('autoDeviceSwitchStatusChange');
}

#### setQualityPrioritization14+

setQualityPrioritization(quality : QualityPrioritization) : void;

Sets the priority level for video recording quality.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/hWXas1VDSfmRYsP3S0492A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DBF98D8233FF8D9E1C7BD45A783EB2FAEBDD6E4EAE394FD03C73CE2DF5D5F6F0)

-   The default value is **HIGH\_QUALITY**. Switching to **POWER\_BALANCE** will compromise video recording quality to achieve lower power usage. The extent of power conservation achieved varies depending on the platform.
-   It is recommended that this API be called between [commitConfig](../interface-session/document.md#commitconfig11) and [start](../interface-session/document.md#start11-1).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| quality | [QualityPrioritization](../enums/document.md#qualityprioritization14) | Yes | Priority level to set. The default value is **HIGH\_QUALITY**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 7400103 | Session not config. The session has not been committed or configured. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setQualityPrioritization(videoSession: camera.VideoSession): void {
  try {
    videoSession.setQualityPrioritization(camera.QualityPrioritization.POWER\_BALANCE);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The setQualityPrioritization call failed. error code: ${err.code}\`);
  }
}

#### on('systemPressureLevelChange')20+

on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void

Subscribes to system pressure level change events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/ceabpSrFSP-YoSBBjytlew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=642F08C8DA199C3F7637F30687D2F5DB30FD0D08AE956017DEF4418BB663DEC7)

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

function registerSystemPressureLevelChangeCallback(videoSession: camera.VideoSession): void {
    videoSession.on('systemPressureLevelChange', callback);
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

function unregisterSystemPressureLevelChangeCallback(videoSession: camera.VideoSession): void {
  videoSession.off('systemPressureLevelChange');
}

#### on('controlCenterEffectStatusChange')20+

on(type: 'controlCenterEffectStatusChange', callback: AsyncCallback<ControlCenterStatusInfo>): void

Subscribes to events indicating that the camera controller effect status changes. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/TqhGxTXHQOiRCoP7ZD45pg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E2DBEAFE1694E69B5E1B3F71548951DBE395FE1C2419FAB0788FB848F49DAF3)

Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'controlCenterEffectStatusChange'**. The event can be listened for when a session is created. |
| callback | AsyncCallback<[ControlCenterStatusInfo](../interfaces-others/document.md#controlcenterstatusinfo20)\> | Yes | Callback used to return the effect status of the current controller. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, status: camera.ControlCenterStatusInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info(\`controlCenterEffectStatusChange: ${status}\`);
}

function registerControlCenterEffectStatusChangeCallback(videoSession: camera.VideoSession): void {
  videoSession.on('controlCenterEffectStatusChange', callback);
}

#### off('controlCenterEffectStatusChange')20+

off(type: 'controlCenterEffectStatusChange', callback?: AsyncCallback<ControlCenterStatusInfo>): void

Unsubscribes from events indicating that the camera controller effect status changes.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'controlCenterEffectStatusChange'**. The event can be listened for when a session is created. |
| callback | AsyncCallback<[ControlCenterStatusInfo](../interfaces-others/document.md#controlcenterstatusinfo20)\> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

**Example**

function unregisterControlCenterEffectStatusChange(videoSession: camera.VideoSession): void {
  videoSession.off('controlCenterEffectStatusChange');
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

function registerMacroStatusChanged(videoSession: camera.VideoSession): void {
  videoSession.on('macroStatusChanged', callback);
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
| callback | AsyncCallback<boolean> | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. If **true** is returned, the unsubscription is successful. If **false** is returned, the unsubscription fails. |

**Example**

function unregisterMacroStatusChanged(videoSession: camera.VideoSession): void {
  videoSession.off('macroStatusChanged');
}

#### onIsoInfoChange22+

onIsoInfoChange(callback: Callback<IsoInfo>): void

Subscribes to sensitivity (ISO) state change events and obtains the latest ISO value through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[IsoInfo](../interfaces-others/document.md#isoinfo22)\> | Yes | Callback function, which is used to obtain the current ISO value of the camera. |

**Example**

function callback(isoInfo: camera.IsoInfo): void {
  console.info(\`Iso : ${isoInfo}\`);
}

function registerIsoInfoChanged(videoSession: camera.VideoSession): void {
  videoSession.onIsoInfoChange(callback);
}

#### offIsoInfoChange22+

offIsoInfoChange(callback?: Callback<IsoInfo>): void

Unsubscribes from ISO state change events.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[IsoInfo](../interfaces-others/document.md#isoinfo22)\> | No | 
Callback used for unsubscription.

If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.)

Otherwise, the subscriptions to the specified event with all the callbacks are canceled.

 |

**Example**

function callback(isoInfo: camera.IsoInfo): void {
  console.info(\`Iso : ${isoInfo}\`);
}

function unregisterIsoInfoChanged(videoSession: camera.VideoSession): void {
  videoSession.offIsoInfoChange(callback);
}

function unregisterAllIsoInfoChanged(videoSession: camera.VideoSession): void {
  videoSession.offIsoInfoChange();
}
