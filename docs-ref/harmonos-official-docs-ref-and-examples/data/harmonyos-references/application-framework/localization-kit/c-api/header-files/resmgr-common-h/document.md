# resmgr\_common.h

#### Overview

Provides the enum types and structures for resource manager APIs.

**File to include**: <resourcemanager/resmgr\_common.h>

**Library**: libohresmgr.so

**System capability**: SystemCapability.Global.ResourceManager

**Since**: 12

**Related module**: [resourcemanager](../../modules/resourcemanager/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ResourceManager\_Configuration](../../structs/resourcemanager-configuration/document.md) | ResourceManager\_Configuration | Enumerates device states. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ResourceManager\_ErrorCode](#resourcemanager_errorcode) | \- | Enumerates resource manager error codes. |
| [ScreenDensity](#screendensity) | \- | Enumerates screen density types. |
| [ResourceManager\_Direction](#resourcemanager_direction) | ResourceManager\_Direction | Enumerates screen orientations. |
| [ResourceManager\_ColorMode](#resourcemanager_colormode) | ResourceManager\_ColorMode | Enumerates color modes. |
| [ResourceManager\_DeviceType](#resourcemanager_devicetype) | ResourceManager\_DeviceType | Enumerates device types. |

#### Enum Description

#### \[h2\]ResourceManager\_ErrorCode

enum ResourceManager\_ErrorCode

**Description**

Enumerates resource manager error codes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| SUCCESS = 0 | Operation successful. |
| ERROR\_CODE\_INVALID\_INPUT\_PARAMETER = 401 | Invalid input parameter. |
| ERROR\_CODE\_RES\_ID\_NOT\_FOUND = 9001001 | Invalid resource ID. |
| ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID = 9001002 | Invalid resource name. |
| ERROR\_CODE\_RES\_NAME\_NOT\_FOUND = 9001003 | No matching resource found based on the resource ID. |
| ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME = 9001004 | No matching resource found based on the resource name. |
| ERROR\_CODE\_RES\_PATH\_INVALID = 9001005 | Invalid relative path. |
| ERROR\_CODE\_RES\_REF\_TOO\_MUCH = 9001006 | Resource referenced cyclically. |
| ERROR\_CODE\_RES\_ID\_FORMAT\_ERROR = 9001007 | Failed to format the resource obtained based on the specified resource ID. |
| ERROR\_CODE\_RES\_NAME\_FORMAT\_ERROR = 9001008 | Failed to format the resource obtained based on the specified resource name. |
| ERROR\_CODE\_SYSTEM\_RES\_MANAGER\_GET\_FAILED = 9001009 | Failed to access system resources. |
| ERROR\_CODE\_OVERLAY\_RES\_PATH\_INVALID = 9001010 | Invalid overlay path. |
| ERROR\_CODE\_OUT\_OF\_MEMORY = 9001100 | A memory overflow occurs. |

#### \[h2\]ScreenDensity

enum ScreenDensity

**Description**

Enumerates screen density types.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| SCREEN\_SDPI = 120 | Screen density with small-scale dots per inch (SDPI). |
| SCREEN\_MDPI = 160 | Screen density with medium-scale dots per inch (MDPI). |
| SCREEN\_LDPI = 240 | Screen density with large-scale dots per inch (LDPI). |
| SCREEN\_XLDPI = 320 | Screen density with extra-large-scale dots per inch (XLDPI). |
| SCREEN\_XXLDPI = 480 | Screen density with extra-extra-large-scale dots per inch (XXLDPI). |
| SCREEN\_XXXLDPI = 640 | Screen density with extra-extra-extra-large-scale dots per inch (XXXLDPI). |

#### \[h2\]ResourceManager\_Direction

enum ResourceManager\_Direction

**Description**

Enumerates screen orientations.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| DIRECTION\_VERTICAL = 0 | Vertical direction. |
| DIRECTION\_HORIZONTAL = 1 | Horizontal direction. |

#### \[h2\]ResourceManager\_ColorMode

enum ResourceManager\_ColorMode

**Description**

Enumerates color modes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| COLOR\_MODE\_DARK = 0 | Dark mode. |
| COLOR\_MODE\_LIGHT = 1 | Light mode. |

#### \[h2\]ResourceManager\_DeviceType

enum ResourceManager\_DeviceType

**Description**

Enumerates device types.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| DEVICE\_TYPE\_PHONE = 0X00 | Smartphone |
| DEVICE\_TYPE\_TABLET = 0x01 | Tablet |
| DEVICE\_TYPE\_CAR = 0x02 | Automobile |
| DEVICE\_TYPE\_PC = 0x03 | Computer |
| DEVICE\_TYPE\_TV = 0x04 | TV. |
| DEVICE\_TYPE\_WEARABLE = 0x06 | Wearable |
| DEVICE\_TYPE\_2IN1 = 0x07 | 2-in-1 device |
