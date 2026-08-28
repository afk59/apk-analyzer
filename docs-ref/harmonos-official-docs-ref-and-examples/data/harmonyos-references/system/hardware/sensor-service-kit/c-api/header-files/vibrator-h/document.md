# vibrator.h

#### Overview

Declares the APIs for starting or stopping vibration.

**Header file**: <sensors/vibrator.h>

**Library**: libohvibrator.z.so

**System capability**: SystemCapability.Sensors.MiscDevice

**Since**: 11

**Related module**: [Vibrator](../../modules/vibrator/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_Vibrator\_PlayVibration(int32\_t duration, Vibrator\_Attribute attribute)](#oh_vibrator_playvibration) | Configures the vibrator to vibrate continuously for a given duration. |
| [int32\_t OH\_Vibrator\_PlayVibrationCustom(Vibrator\_FileDescription fileDescription, Vibrator\_Attribute vibrateAttribute)](#oh_vibrator_playvibrationcustom) | Configures the vibrator to vibrate with the custom sequence. |
| [int32\_t OH\_Vibrator\_Cancel()](#oh_vibrator_cancel) | Stops the vibration. |

#### Function Description

#### \[h2\]OH\_Vibrator\_PlayVibration()

int32\_t OH\_Vibrator\_PlayVibration(int32\_t duration, Vibrator\_Attribute attribute)

**Description**

Controls the vibrator to vibrate continuously for a given duration.

**Required permissions**: ohos.permission.VIBRATE

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t duration | Vibration duration, in milliseconds. |
| [Vibrator\_Attribute](../../structs/vibrator-attribute/document.md) attribute | Vibration attribute. For details, see **VibrateAttribute**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns a non-zero value otherwise. For details, see [Vibrator\_ErrorCode](../vibrator-type-h/document.md#vibrator_errorcode). |

#### \[h2\]OH\_Vibrator\_PlayVibrationCustom()

int32\_t OH\_Vibrator\_PlayVibrationCustom(Vibrator\_FileDescription fileDescription, Vibrator\_Attribute vibrateAttribute)

**Description**

Configure the vibrator to vibrate with the custom sequence.

**Required permissions**: ohos.permission.VIBRATE

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Vibrator\_FileDescription](../../structs/vibrator-filedescription/document.md) fileDescription | File descriptor of the custom vibration effect. For details, see [Vibrator\_FileDescription](../../structs/vibrator-filedescription/document.md). |
| [Vibrator\_Attribute](../../structs/vibrator-attribute/document.md) vibrateAttribute | Vibration attribute. For details, see [Vibrator\_Attribute](../../structs/vibrator-attribute/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns a non-zero value otherwise. For details, see [Vibrator\_ErrorCode](../vibrator-type-h/document.md#vibrator_errorcode). |

#### \[h2\]OH\_Vibrator\_Cancel()

int32\_t OH\_Vibrator\_Cancel()

**Description**

Stops the vibration.

**Required permissions**: ohos.permission.VIBRATE

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns a non-zero value otherwise. For details, see [Vibrator\_ErrorCode](../vibrator-type-h/document.md#vibrator_errorcode). |
