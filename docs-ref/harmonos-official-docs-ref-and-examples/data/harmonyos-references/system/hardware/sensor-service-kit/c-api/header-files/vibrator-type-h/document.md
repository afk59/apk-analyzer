# vibrator\_type.h

#### Overview

Declares the APIs for starting or stopping vibration.

**Reference file**: <sensors/vibrator\_type.h>

**Library**: libohvibrator.z.so

**System capability**: SystemCapability.Sensors.MiscDevice

**Since**: 11

**Related module**: [Vibrator](../../modules/vibrator/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Vibrator\_Attribute](../../structs/vibrator-attribute/document.md) | Vibrator\_Attribute | Defines a struct for the vibrator attribute. |
| [Vibrator\_FileDescription](../../structs/vibrator-filedescription/document.md) | Vibrator\_FileDescription | Defines a struct for the vibration file description. |

#### \[h2\]Enumeration

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Vibrator\_ErrorCode](#vibrator_errorcode) | Vibrator\_ErrorCode | Enumerates the vibrator error codes. |
| [Vibrator\_Usage](#vibrator_usage) | Vibrator\_Usage | Enumerates the vibration scenarios. |

#### Enum Description

#### \[h2\]Vibrator\_ErrorCode

enum Vibrator\_ErrorCode

**Description**

Enumerates the vibrator error codes.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| PERMISSION\_DENIED = 201 | Permission denied. |
| PARAMETER\_ERROR = 401 | Parameter check failed. For example, a mandatory parameter is not passed in, or the parameter type passed in is incorrect. |
| UNSUPPORTED = 801 | The device does not support this API. Generally, this enumerated value is used for a device that supports the corresponding system capability but only parts of APIs. |
| DEVICE\_OPERATION\_FAILED = 14600101 | Device operation failed. |

#### \[h2\]Vibrator\_Usage

enum Vibrator\_Usage

**Description**

Enumerates the vibration scenarios.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| VIBRATOR\_USAGE\_UNKNOWN = 0 | Unknown scenario |
| VIBRATOR\_USAGE\_ALARM = 1 | Alarming |
| VIBRATOR\_USAGE\_RING = 2 | Ringing |
| VIBRATOR\_USAGE\_NOTIFICATION = 3 | Notification |
| VIBRATOR\_USAGE\_COMMUNICATION = 4 | Telecommunications |
| VIBRATOR\_USAGE\_TOUCH = 5 | Touch |
| VIBRATOR\_USAGE\_MEDIA = 6 | Multimedia |
| VIBRATOR\_USAGE\_PHYSICAL\_FEEDBACK = 7 | Physical feedback |
| VIBRATOR\_USAGE\_SIMULATED\_REALITY = 8 | Simulated reality |
