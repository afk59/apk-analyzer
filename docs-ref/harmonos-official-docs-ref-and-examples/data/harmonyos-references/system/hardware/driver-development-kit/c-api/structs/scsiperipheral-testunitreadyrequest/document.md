# ScsiPeripheral\_TestUnitReadyRequest

#### Overview

Defines the request structure of the **test unit ready** command.

**Since**: 18

**Related module**: [SCSIPeripheralDDK](../../modules/scsiperipheralddk/document.md)

**Header file**: [scsi\_peripheral\_types.h](../../header-files/scsi-peripheral-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t control | **Control** field used to specify control information. |
| uint32\_t timeout | Timeout duration, in ms. |
