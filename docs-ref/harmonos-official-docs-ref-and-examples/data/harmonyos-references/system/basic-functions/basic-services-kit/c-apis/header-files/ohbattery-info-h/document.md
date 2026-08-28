# ohbattery\_info.h

#### Overview

Declares the battery APIs that are used to obtain the current battery capacity and power supply type and define common battery events.

**File to include**: <BasicServicesKit/ohbattery\_info.h>

**Library**: libohbattery\_info.so

**System capability**: SystemCapability.PowerManager.BatteryManager.Core

**Since**: 13

**Related modules**: [OH\_BatteryInfo](../../modules/oh-batteryinfo/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [BatteryInfo\_BatteryPluggedType](#batteryinfo_batterypluggedtype) | BatteryInfo\_BatteryPluggedType | Enumerates the battery plugged types. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_BatteryInfo\_GetCapacity()](#oh_batteryinfo_getcapacity) | Obtains the current battery capacity. |
| [BatteryInfo\_BatteryPluggedType OH\_BatteryInfo\_GetPluggedType()](#oh_batteryinfo_getpluggedtype) | Obtains the battery plugged type. |

#### \[h2\]Variables

| Name | Description |
| :-- | :-- |
| static const char \* COMMON\_EVENT\_KEY\_CAPACITY = "soc" | 
Defines the common event indicating a battery capacity change.

**Since**: 13

 |
| static const char \* COMMON\_EVENT\_KEY\_CHARGE\_STATE = "chargeState" | 

Defines the common event indicating a charging status change.

**Since**: 13

 |
| static const char \* COMMON\_EVENT\_KEY\_PLUGGED\_TYPE = "pluggedType" | 

Defines the common event indicating a battery plugged type change.

**Since**: 13

 |

#### Enum Description

#### \[h2\]BatteryInfo\_BatteryPluggedType

enum BatteryInfo\_BatteryPluggedType

**Description**

Enumerates the battery plugged types.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| PLUGGED\_TYPE\_NONE = 0 | No power supply. |
| PLUGGED\_TYPE\_AC = 1 | AC charging. |
| PLUGGED\_TYPE\_USB = 2 | USB DC charging. |
| PLUGGED\_TYPE\_WIRELESS = 3 | Wireless charging. |
| PLUGGED\_TYPE\_BUTT = 4 | Reserved. |

#### Function Description

#### \[h2\]OH\_BatteryInfo\_GetCapacity()

int32\_t OH\_BatteryInfo\_GetCapacity()

**Description**

Obtains the current battery capacity.

**System capability**: SystemCapability.PowerManager.BatteryManager.Core

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | A number in the range from 0 to 100. |

#### \[h2\]OH\_BatteryInfo\_GetPluggedType()

BatteryInfo\_BatteryPluggedType OH\_BatteryInfo\_GetPluggedType()

**Description**

Obtains the battery plugged type.

**System capability**: SystemCapability.PowerManager.BatteryManager.Core

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| [BatteryInfo\_BatteryPluggedType](#batteryinfo_batterypluggedtype) | 
Returns [PLUGGED\_TYPE\_NONE](#batteryinfo_batterypluggedtype) if the power supply is removed;

returns [PLUGGED\_TYPE\_AC](#batteryinfo_batterypluggedtype) if the power supply is in AC charging mode;

returns [PLUGGED\_TYPE\_USB](#batteryinfo_batterypluggedtype) if the power supply is in USB DC charging mode;

returns [PLUGGED\_TYPE\_WIRELESS](#batteryinfo_batterypluggedtype) if the power supply is in wireless charging mode;

returns [PLUGGED\_TYPE\_BUTT](#batteryinfo_batterypluggedtype) if the battery plugged type is unknown.

 |
