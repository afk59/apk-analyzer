# @ohos.batteryInfo (Battery Information)

The **batteryInfo** module provides APIs for querying the charger type, battery health status, and battery charging status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/bno8_K8RRM-zRYR29UjDEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9B4D20A3E5282CFF30CCA43EB08B6C59538E7E72A58B44414907368EB482F37)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import {batteryInfo} from '@kit.BasicServicesKit';

#### Constants

Describes battery information.

**System capability**: SystemCapability.PowerManager.BatteryManager.Core

| Name | Type | Read-Only | Description |
| :-- | :-- | :-- | :-- |
| batterySOC | number | Yes | 
Battery state of charge (SoC) of the device, in unit of percentage.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| chargingStatus | [BatteryChargeState](#batterychargestate) | Yes | 

Battery charging state of the current device.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| healthStatus | [BatteryHealthState](#batteryhealthstate) | Yes | Battery health status of the device. |
| pluggedType | [BatteryPluggedType](#batterypluggedtype) | Yes | Charger type of the device. |
| voltage | number | Yes | Battery voltage of the device, in unit of microvolt. |
| technology | string | Yes | Battery technology of the device. |
| batteryTemperature | number | Yes | Battery temperature of the device, in unit of 0.1°C. |
| isBatteryPresent7+ | boolean | Yes | 

Whether the battery is supported or present. The value **true** means that the battery is supported or present; **false** means the opposite.

Default value: **false**.

 |
| batteryCapacityLevel9+ | [BatteryCapacityLevel](#batterycapacitylevel9) | Yes | Battery level of the device. |
| nowCurrent12+ | number | Yes | Battery current of the device, in unit of mA. |

**Example**

import {batteryInfo} from '@kit.BasicServicesKit';

let batterySOCInfo: number = batteryInfo.batterySOC;
console.info("The batterySOCInfo is: " + batterySOCInfo);

let chargingStatusInfo = batteryInfo.chargingStatus;
console.info("The chargingStatusInfo is: " + chargingStatusInfo);

let healthStatusInfo = batteryInfo.healthStatus;
console.info("The healthStatusInfo is: " + healthStatusInfo);

let pluggedTypeInfo = batteryInfo.pluggedType;
console.info("The pluggedTypeInfo is: " + pluggedTypeInfo);

let voltageInfo: number = batteryInfo.voltage;
console.info("The voltageInfo is: " + voltageInfo);

let technologyInfo: string = batteryInfo.technology;
console.info("The technologyInfo is: " + technologyInfo);

let batteryTemperatureInfo: number = batteryInfo.batteryTemperature;
console.info("The batteryTemperatureInfo is: " + batteryTemperatureInfo);

let isBatteryPresentInfo: boolean = batteryInfo.isBatteryPresent;
console.info("The isBatteryPresentInfo is: " + isBatteryPresentInfo);

let batteryCapacityLevelInfo = batteryInfo.batteryCapacityLevel;
console.info("The batteryCapacityLevelInfo is: " + batteryCapacityLevelInfo);

let nowCurrentInfo: number = batteryInfo.nowCurrent;
console.info("The nowCurrentInfo is: " + nowCurrentInfo);

#### BatteryPluggedType

Enumerates charger types.

**System capability**: SystemCapability.PowerManager.BatteryManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | Unknown charger type. |
| AC | 1 | AC charger. |
| USB | 2 | USB charger. |
| WIRELESS | 3 | Wireless charger. |

#### BatteryChargeState

Enumerates charging states.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.PowerManager.BatteryManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | The battery is not being charged. |
| ENABLE | 1 | The battery is being charged. |
| DISABLE | 2 | The battery charging is stopped. |
| FULL | 3 | The battery is fully charged. |

#### BatteryHealthState

Enumerates battery health states.

**System capability**: SystemCapability.PowerManager.BatteryManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN | 0 | Unknown state. |
| GOOD | 1 | The battery is in the healthy state. |
| OVERHEAT | 2 | The battery is overheated. |
| OVERVOLTAGE | 3 | The battery voltage is over high. |
| COLD | 4 | The battery temperature is low. |
| DEAD | 5 | The battery is dead. |

#### BatteryCapacityLevel9+

Enumerates battery levels.

**System capability**: SystemCapability.PowerManager.BatteryManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| LEVEL\_FULL | 1 | Full battery level. |
| LEVEL\_HIGH | 2 | High battery level. |
| LEVEL\_NORMAL | 3 | Normal battery level. |
| LEVEL\_LOW | 4 | Low battery level. |
| LEVEL\_WARNING | 5 | Alarm battery level. |
| LEVEL\_CRITICAL | 6 | Ultra-low battery level. |
| LEVEL\_SHUTDOWN | 7 | Power-down battery level. |

#### CommonEventBatteryChangedKey9+

Enumerates keys for querying the additional information about the **COMMON\_EVENT\_BATTERY\_CHANGED** event.

**System capability**: SystemCapability.PowerManager.BatteryManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| EXTRA\_SOC | "soc" | Remaining battery level in percentage. |
| EXTRA\_CHARGE\_STATE | "chargeState" | Battery charging status of the device. |
| EXTRA\_HEALTH\_STATE | "healthState" | Battery health status of the device. |
| EXTRA\_PLUGGED\_TYPE | "pluggedType" | Type of the charger connected to the device. |
| EXTRA\_VOLTAGE | "voltage" | Battery voltage of the device. |
| EXTRA\_TECHNOLOGY | "technology" | Battery technology of the device. |
| EXTRA\_TEMPERATURE | "temperature" | Battery temperature of the device. |
| EXTRA\_PRESENT | "present" | Whether the battery is supported by the device or installed. |
| EXTRA\_CAPACITY\_LEVEL | "capacityLevel" | Battery level of the device. |
