# @ohos.multimodalAwareness.motion (Motion Awareness)

The **motion** module provides the user motion awareness capabilities, including user gestures and actions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/x9po46H1Sb2FznJSYxFh8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062410Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5FD6B853912AED3EBBDE00A8430066F34475BF8621562A20BE7A8DF9BE94C17E)

The initial APIs of this module are supported since API version 15. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { motion } from '@kit.MultimodalAwarenessKit';

#### OperatingHandStatus

Defines the status of the operating hand.

**System capability**: SystemCapability.MultimodalAwareness.Motion

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN\_STATUS | 0 | Unknown status. |
| LEFT\_HAND\_OPERATED | 1 | Left hand in use. |
| RIGHT\_HAND\_OPERATED | 2 | Right hand in use. |

#### HoldingHandStatus20+

Represents the holding hand status. The holding hand status is returned if listening for holding hand status changes is enabled.

**System capability**: SystemCapability.MultimodalAwareness.Motion

| Name | Value | Description |
| :-- | :-- | :-- |
| NOT\_HELD | 0 | No holding. |
| LEFT\_HAND\_HELD | 1 | Holding with the left hand. |
| RIGHT\_HAND\_HELD | 2 | Holding with the right hand. |
| BOTH\_HANDS\_HELD | 3 | Holding with both hands. |
| UNKNOWN\_STATUS | 16 | Unknown status. |

#### motion.on('operatingHandChanged')

on(type: 'operatingHandChanged', callback: Callback<OperatingHandStatus>): void

Subscribes to operating hand change events.

If the device does not support this function, error code 801 is returned.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE

**System capability**: SystemCapability.MultimodalAwareness.Motion

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. This parameter has a fixed value of **operatingHandChanged**. |
| callback | Callback<[OperatingHandStatus](#operatinghandstatus)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Motion Awareness Error Codes](../../error-codes/motion-awareness-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. An attempt was made to subscribe operatingHandChanged event forbidden by permission: ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE. |
| 401 | Parameter error. Parameter verification failed. |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 31500001 | Service exception. Possible causes: 1. A system error, such as null pointer, container-related exception; 2. N-API invocation exception, invalid N-API status. |
| 31500002 | Subscription failed. Possible causes: 1. Callback registration failure; 2. Failed to bind native object to js wrapper; 3. N-API invocation exception, invalid N-API status; 4. IPC request exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let callback:Callback<motion.OperatingHandStatus> = (data:motion.OperatingHandStatus) => {
    console.info('callback succeeded' + data);
};

try {
    motion.on('operatingHandChanged', callback);
    console.info("on succeeded");
} catch (err) {
    let error = err as BusinessError;
    console.error("Failed on and err code is " + error.code);
}

#### motion.off('operatingHandChanged')

off(type: 'operatingHandChanged', callback?: Callback<OperatingHandStatus>): void

Unsubscribes from operating hand change events.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE

**System capability**: SystemCapability.MultimodalAwareness.Motion

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. This parameter has a fixed value of **operatingHandChanged**. |
| callback | Callback<[OperatingHandStatus](#operatinghandstatus)\> | No | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Motion Awareness Error Codes](../../error-codes/motion-awareness-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. An attempt was made to unsubscribe operatingHandChanged event forbidden by permission: ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE. |
| 401 | Parameter error. Parameter verification failed. |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 31500001 | Service exception. Possible causes: 1. A system error, such as null pointer, container-related exception; 2. N-API invocation exception, invalid N-API status. |
| 31500003 | Unsubscription failed. Possible causes: 1. Callback failure; 2. N-API invocation exception, invalid N-API status; 3. IPC request exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    motion.off('operatingHandChanged');
    console.info("off succeeded");
} catch (err) {
    let error = err as BusinessError;
    console.error("Failed off and err code is " + error.code);
}

#### motion.getRecentOperatingHandStatus()

getRecentOperatingHandStatus(): OperatingHandStatus

Obtains the latest operating hand status.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE

**System capability**: SystemCapability.MultimodalAwareness.Motion

**Return value**

| Type | Description |
| :-- | :-- |
| [OperatingHandStatus](#operatinghandstatus) | Status of the operating hand. |

**Error codes**

For details about the error codes, see [Motion Awareness Error Codes](../../error-codes/motion-awareness-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. An attempt was made to get the recent operating hand status forbidden by permission: ohos.permission.ACTIVITY\_MOTION or ohos.permission.DETECT\_GESTURE. |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 31500001 | Service exception. Possible causes: 1. A system error, such as null pointer, container-related exception; 2. N-API invocation exception, invalid N-API status. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let data:motion.OperatingHandStatus = motion.getRecentOperatingHandStatus();
    console.info('get succeeded' + data);
} catch (err) {
    let error = err as BusinessError;
    console.error("Failed get and err code is " + error.code);
}

#### motion.on('holdingHandChanged') 20+

on(type: 'holdingHandChanged', callback: Callback<HoldingHandStatus>): void

Enables listening for holding hand status changes.

**Required permissions**: ohos.permission.DETECT\_GESTURE

**System capability**: SystemCapability.MultimodalAwareness.Motion

**Parameter**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **holdingHandChanged** indicates the holding hand status change event. |
| callback | Callback<[HoldingHandStatus](#holdinghandstatus20)\> | Yes | Callback used to return the holding hand status. |

**Error Code**

For details about the error codes, see [Motion Awareness Error Codes](../../error-codes/motion-awareness-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. An attempt was made to subscribe holdingHandChanged event forbidden by permission: ohos.permission.DETECT\_GESTURE. |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 31500001 | Service exception. Possible causes: 1. A system error, such as null pointer, container-related exception; 2. N-API invocation exception, invalid N-API status. |
| 31500002 | Subscription failed. Possible causes: 1. Callback registration failure; 2. Failed to bind native object to js wrapper; 3. N-API invocation exception, invalid N-API status; 4. IPC request exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let callback:Callback<motion.HoldingHandStatus> = (data:motion.HoldingHandStatus) => {
  console.info('callback succeeded: ' + data);
};

try {
  motion.on('holdingHandChanged', callback);
  console.info('on succeeded');
} catch (err) {
  let error = err as BusinessError;
  console.error('Failed on; err code = ' + error.code);
}

#### motion.off('holdingHandChanged') 20+

off(type: 'holdingHandChanged', callback?: Callback<HoldingHandStatus>): void

Disables listening for holding hand status changes.

**Required permissions**: ohos.permission.DETECT\_GESTURE

**System capability**: SystemCapability.MultimodalAwareness.Motion

**Parameter**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **holdingHandChanged** indicates the holding hand status change event. |
| callback | Callback<[HoldingHandStatus](#holdinghandstatus20)\> | No | Callback to unregister. If this parameter is not passed, all callbacks for the holding hand status change event will be unregistered. |

**Error Code**

For details about the error codes, see [Motion Awareness Error Codes](../../error-codes/motion-awareness-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. An attempt was made to unsubscribe holdingHandChanged event forbidden by permission: ohos.permission.DETECT\_GESTURE. |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 31500001 | Service exception. Possible causes: 1. A system error, such as null pointer, container-related exception; 2. N-API invocation exception, invalid N-API status. |
| 31500003 | Unsubscription failed. Possible causes: 1. Callback failure; 2. N-API invocation exception, invalid N-API status; 3. IPC request exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  motion.off('holdingHandChanged'); // Unregister all callbacks for the holding hand status change event.
  console.info('off succeeded');
} catch (err) {
  let error = err as BusinessError;
  console.error('Failed off; err code = ' + error.code);
}
