# ScsiPeripheral\_ReadCapacityRequest

typedef struct ScsiPeripheral\_ReadCapacityRequest {...} ScsiPeripheral\_ReadCapacityRequest

#### Overview

Request structure of the **read capacity** command.

**Since**: 18

**Related module**: [SCSIPeripheralDDK](../../modules/scsiperipheralddk/document.md)

**Header file**: [scsi\_peripheral\_types.h](../../header-files/scsi-peripheral-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t lbAddress | Address of the logical unit. |
| uint8\_t control | **Control** field used to specify control information. |
| uint8\_t byte8 | Eighth byte of the CDB. |
| uint32\_t timeout | Timeout duration, in ms. |
