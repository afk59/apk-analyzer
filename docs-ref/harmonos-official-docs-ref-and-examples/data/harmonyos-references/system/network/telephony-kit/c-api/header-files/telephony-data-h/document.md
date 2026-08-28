# telephony\_data.h

#### Overview

Defines C APIs for cellular data module.

**File to include**: <telephony/cellular\_data/telephony\_data.h>

**Library**: libtelephony\_data.so

**System capability**: SystemCapability.Telephony.CellularData

**Since**: 13

**Related module**: [Telephony](../../modules/telephony/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_Telephony\_GetDefaultCellularDataSlotId(void)](#oh_telephony_getdefaultcellulardataslotid) | Obtains the default SIM card used for mobile data. |

#### Function Description

#### \[h2\]OH\_Telephony\_GetDefaultCellularDataSlotId()

int32\_t OH\_Telephony\_GetDefaultCellularDataSlotId(void)

**Description**

Obtains the default SIM card used for mobile data.

**System capability**: SystemCapability.Telephony.CellularData

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Default SIM card used for mobile data. The value **0** indicates card slot 1, and the value **1** indicates card slot 2. |
