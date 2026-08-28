# @ohos.thermal (Thermal Management)

The **thermal** module provides thermal level-related callback and query APIs to obtain the information required for thermal control.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/1lO7NmrVQG27C5unB2ogAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC6E2B689E19E6451A4C8500B0088B582275A2E922A2C70F31CEB0DA1E08F440)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import {thermal} from '@kit.BasicServicesKit';

#### thermal.registerThermalLevelCallback9+

registerThermalLevelCallback(callback: Callback<ThermalLevel>): void

**API description**: Registers a callback to be invoked when the thermal level changes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.PowerManager.ThermalManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[ThermalLevel](#thermallevel)\> | Yes | Callback used to return thermal level. This parameter is of the function type. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**Example**

try {
    thermal.registerThermalLevelCallback((level: thermal.ThermalLevel) => {
        console.info('thermal level is: ' + level);
    });
    console.info('register thermal level callback success.');
} catch(err) {
    console.error('register thermal level callback failed, err: ' + err);
}

#### thermal.unregisterThermalLevelCallback9+

unregisterThermalLevelCallback(callback?: Callback<void>): void

**API description**: Unregisters the callback to be invoked when the thermal level changes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.PowerManager.ThermalManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<void> | No | (Optional) Callback that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**Example**

try {
    thermal.unregisterThermalLevelCallback(() => {
        console.info('unsubscribe thermal level success.');
    });
    console.info('unregister thermal level callback success.');
} catch(err) {
    console.error('unregister thermal level callback failed, err: ' + err);
}

#### thermal.getLevel9+

getLevel(): ThermalLevel

**API description**: Obtains this thermal level.

**System capability**: SystemCapability.PowerManager.ThermalManager

**Return value**

| Type | Description |
| :-- | :-- |
| [ThermalLevel](#thermallevel) | Thermal level. |

**Example**

let level = thermal.getLevel();
console.info('thermal level is: ' + level);

#### thermal.subscribeThermalLevel(deprecated)

subscribeThermalLevel(callback: AsyncCallback<ThermalLevel>): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/-kQU-wNIS8uUGUzvWPYsUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07C36AF84A03069B03D4E6E423AF556B31127A43204B8ED7BDBCF5A3F8247C7F)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [thermal.registerThermalLevelCallback](#thermalregisterthermallevelcallback9) instead.

**API description**: Subscribes to the thermal level changes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.PowerManager.ThermalManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[ThermalLevel](#thermallevel)\> | Yes | Callback used to return the result. The return value contains only one parameter, that is, thermal level. |

**Example**

thermal.subscribeThermalLevel((err: Error, level: thermal.ThermalLevel) => {
    console.info('thermal level is: ' + level);
});

#### thermal.unsubscribeThermalLevel(deprecated)

unsubscribeThermalLevel(callback?: AsyncCallback<void>): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/4s2wwj9NSMSiWGg5jEGj-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B593B5B01A42DA178DDC4C3B724F9C653CCE6DDE588477DC6520E3013A64EFB)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [thermal.unregisterThermalLevelCallback](#thermalunregisterthermallevelcallback9) instead.

**API description**: Unsubscribes from the thermal level changes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.PowerManager.ThermalManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | No | Callback that returns no value. If this parameter is not set, all callbacks will be unregistered. |

**Example**

thermal.unsubscribeThermalLevel(() => {
    console.info('unsubscribe thermal level success.');
});

#### thermal.getThermalLevel(deprecated)

getThermalLevel(): ThermalLevel

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/D8bmzTa2TaKZrHIWZzvkWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C4793EF158946D636F1D883154094A5F4ADC71C3B30841FFA36719DAE6BB4E8)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [thermal.getLevel](#thermalgetlevel9) instead.

**API description**: Obtains this thermal level.

**System capability**: SystemCapability.PowerManager.ThermalManager

**Return value**

| Type | Description |
| :-- | :-- |
| [ThermalLevel](#thermallevel) | Thermal level. |

**Example**

let level = thermal.getThermalLevel();
console.info('thermal level is: ' + level);

#### ThermalLevel

Enumerates thermal levels.

**System capability**: SystemCapability.PowerManager.ThermalManager

| Name | Value | Description |
| :-- | :-- | :-- |
| COOL | 0 | The device is cool, and services are not restricted. |
| NORMAL | 1 | The device is in the normal temperature range but it is getting warm. You need to downgrade or reduce the load of imperceptible services. |
| WARM | 2 | The device is warm. You need to stop or delay some imperceptible services. |
| HOT | 3 | The device is heating up. You need to stop all imperceptible services and downgrade or reduce the load of non-critical services. |
| OVERHEATED | 4 | The device is overheated. You need to stop all imperceptible services and downgrade or reduce the load of major foreground services. |
| WARNING | 5 | The device is overheated and is about to enter the emergency state. You need to stop all imperceptible services and downgrade major foreground services to the maximum extent. |
| EMERGENCY | 6 | The device has entered the emergency state. You need to stop all services except those for fundamental use. |
| ESCAPE11+ | 7 | 
The device is about to enter the escape state. You need to stop all services and take necessary emergency measures such as data backup.

Note: This API is supported since API version 11.

 |
