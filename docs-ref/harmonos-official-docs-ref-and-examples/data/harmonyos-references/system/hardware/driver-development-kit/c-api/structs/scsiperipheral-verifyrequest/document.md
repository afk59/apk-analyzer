# ScsiPeripheral\_VerifyRequest

#### Overview

Defines the request structure of the **verify** command.

**Since**: 18

**Related module**: [SCSIPeripheralDDK](../../modules/scsiperipheralddk/document.md)

**Header file**: [scsi\_peripheral\_types.h](../../header-files/scsi-peripheral-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t lbAddress | Start address of logical blocks. |
| uint16\_t verificationLength | Number of consecutive logical blocks. |
| uint8\_t control | **Control** field used to specify control information. |
| uint8\_t byte1 | First byte of the CDB. |
| uint8\_t byte6 | Sixth byte of the CDB. |
| uint32\_t timeout | Timeout duration, in ms. |
