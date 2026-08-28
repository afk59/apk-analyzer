# @ohos.distributedHardware.mechanicManager (Mechanic Manager)

The **mechanicManager** module provides the mechanic device interaction capabilities, such as listening for the device connection status, tracking control, and listening for the tracking status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/j_a1bKABQFiJAUhX0Elj2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A29F5A18E6EB67C00EF7898C041791CE1C07C08A6A69EE50016818DD28F830E)

The initial APIs of this module are supported since API version 20. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { mechanicManager } from '@kit.MechanicKit';

#### mechanicManager.on('attachStateChange')

on(type: 'attachStateChange', callback: Callback<AttachStateChangeInfo>): void

Registers a callback listener for connection state changes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Mechanic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | 'attachStateChange' | Yes | Event type. The value **attachStateChange** indicates a connection state change. |
| callback | Callback<[AttachStateChangeInfo](#attachstatechangeinfo)\> | Yes | Callback used to return the connection state change of the mechanic device. |

**Error codes**

For details about the error codes, see [Mechanic Manager Error Codes](../../error-codes/mechanic-manager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 33300001 | Service exception. |

**Example**

let callback = (result: mechanicManager.AttachStateChangeInfo) => {
  console.info(\`'callback result:' ${result}\`);
};

console.info('Register');
mechanicManager.on("attachStateChange", callback);
console.info('Register: success');

#### mechanicManager.off('attachStateChange')

off(type: 'attachStateChange', callback?: Callback<AttachStateChangeInfo>): void

Unregisters the callback listener for connection state changes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Mechanic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | 'attachStateChange' | Yes | Event type. The value **attachStateChange** indicates a connection state change. |
| callback | Callback<[AttachStateChangeInfo](#attachstatechangeinfo)\> | No | Callback to unregister. If this parameter is not specified, all callbacks for the specified type of events are unregistered. |

**Error codes**

For details about the error codes, see [Mechanic Manager Error Codes](../../error-codes/mechanic-manager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 33300001 | Service exception. |

**Example**

let callback = (result: mechanicManager.AttachStateChangeInfo) => {
  console.info(\`'callback result:' ${result}\`);
};

console.info('Unregister');
mechanicManager.off("attachStateChange", callback);
console.info('Unregister: success');

#### mechanicManager.getAttachedMechDevices

getAttachedMechDevices(): MechInfo\[\]

Obtain the list of connected mechanic devices.

**System capability**: SystemCapability.Mechanic.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [MechInfo](#mechinfo)\[\] | List of connected mechanic devices. |

**Error codes**

For details about the error codes, see [Mechanic Manager Error Codes](../../error-codes/mechanic-manager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 33300001 | Service exception. |

**Example**

console.info('Query device list');
let mechanicInfos = mechanicManager.getAttachedMechDevices();
console.info(\`'device list:' ${mechanicInfos}\`);

#### mechanicManager.setCameraTrackingEnabled

setCameraTrackingEnabled(isEnabled: boolean): void

Enables or disables camera tracking for the current mechanic device.

**System capability**: SystemCapability.Mechanic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isEnabled | boolean | Yes | Whether to enable camera tracking. The value **true** means to enable camera tracking, and the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Mechanic Manager Error Codes](../../error-codes/mechanic-manager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 33300001 | Service exception. |
| 33300002 | Device not connected. |
| 33300003 | Feature not supported. |

**Example**

console.info('Enable tracing');
mechanicManager.setCameraTrackingEnabled(true);
console.info('Enable Tracking Success');

#### mechanicManager.getCameraTrackingEnabled

getCameraTrackingEnabled(): boolean

Checks whether camera tracking is enabled for the current mechanic device.

**System capability**: SystemCapability.Mechanic.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether camera tracking is enabled. The value **true** indicates that camera tracking is enabled, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Mechanic Manager Error Codes](../../error-codes/mechanic-manager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 33300001 | Service exception. |
| 33300002 | Device not connected. |

**Example**

console.info('Get tracking status');
let enabled = mechanicManager.getCameraTrackingEnabled();
console.info(\`'current tracking status:' ${enabled}\`);

#### mechanicManager.on('trackingStateChange')

on(type: 'trackingStateChange', callback: Callback<TrackingEventInfo>): void

Registers a callback listener for tracking state changes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Mechanic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | 'trackingStateChange' | Yes | Event type. The value **trackingStateChange** indicates a tracking state change. |
| callback | Callback<[TrackingEventInfo](#trackingeventinfo)\> | Yes | Callback used to return the tracking state change of the mechanic device. |

**Error codes**

For details about the error codes, see [Mechanic Manager Error Codes](../../error-codes/mechanic-manager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 33300001 | Service exception. |

**Example**

let callback = (result: mechanicManager.TrackingEventInfo) => {
  console.info(\`'callback result:' ${result}\`);
};

console.info('Register');
mechanicManager.on("trackingStateChange", callback);
console.info('Register: success');

#### mechanicManager.off('trackingStateChange')

off(type: 'trackingStateChange', callback?: Callback<TrackingEventInfo>): void

Unregisters the callback listener for tracking state changes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Mechanic.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | 'trackingStateChange' | Yes | Event type. The value **trackingStateChange** indicates a tracking state change. |
| callback | Callback<[TrackingEventInfo](#trackingeventinfo)\> | No | Callback to unregister. If this parameter is not specified, all callbacks for the specified type of events are unregistered. |

**Error codes**

For details about the error codes, see [Mechanic Manager Error Codes](../../error-codes/mechanic-manager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 33300001 | Service exception. |

**Example**

let callback = (result: mechanicManager.TrackingEventInfo) => {
  console.info(\`'callback result:' ${result}\`);
};

console.info('Unregister');
mechanicManager.off("trackingStateChange", callback);
console.info('Unregister: success');

#### mechanicManager.getCameraTrackingLayout

getCameraTrackingLayout(): CameraTrackingLayout

Obtains the camera tracking layout of the current mechanic device.

**System capability**: SystemCapability.Mechanic.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [CameraTrackingLayout](#cameratrackinglayout) | Camera tracking layout of the current mechanic device. |

**Error codes**

For details about the error codes, see [Mechanic Manager Error Codes](../../error-codes/mechanic-manager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 33300001 | Service exception. |
| 33300002 | Device not connected. |

**Example**

console.info('Query layout');
let layout = mechanicManager.getCameraTrackingLayout();
console.info(\`'Query layout successful, current layout:' ${layout}\`);

#### MechInfo

Defines information about the mechanic device.

**System capability**: SystemCapability.Mechanic.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| mechId | number | No | No | ID of the mechanic device. |
| mechDeviceType | [MechDeviceType](#mechdevicetype) | No | No | Type of the mechanic device. |
| mechName | string | No | No | Name of the mechanic device. |

#### TrackingEventInfo

Defines the tracking event information.

**System capability**: SystemCapability.Mechanic.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| event | [TrackingEvent](#trackingevent) | No | No | Tracking event. |

#### AttachStateChangeInfo

Defines the connection state change information.

**System capability**: SystemCapability.Mechanic.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| state | [AttachState](#attachstate) | No | No | Device connection state. |
| mechInfo | [MechInfo](#mechinfo) | No | No | Device information. |

#### TrackingEvent

Enumerates the camera tracking events.

**System capability**: SystemCapability.Mechanic.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CAMERA\_TRACKING\_USER\_ENABLED | 0 | Camera tracking is enabled. |
| CAMERA\_TRACKING\_USER\_DISABLED | 1 | Camera tracking is disabled. |
| CAMERA\_TRACKING\_LAYOUT\_CHANGED | 2 | The camera tracking layout is changed. |

#### MechDeviceType

Enumerates the mechanic device types.

**System capability**: SystemCapability.Mechanic.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| GIMBAL\_DEVICE | 0 | Portable gimbal device. |

#### AttachState

Enumerates the device connection states.

**System capability**: SystemCapability.Mechanic.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ATTACHED | 0 | Device connected. |
| DETACHED | 1 | Device disconnected. |

#### CameraTrackingLayout

Enumerates the camera tracking layouts.

**System capability**: SystemCapability.Mechanic.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | Default tracking layout. |
| LEFT | 1 | Left layout. |
| MIDDLE | 2 | Center layout. |
| RIGHT | 3 | Right layout. |
