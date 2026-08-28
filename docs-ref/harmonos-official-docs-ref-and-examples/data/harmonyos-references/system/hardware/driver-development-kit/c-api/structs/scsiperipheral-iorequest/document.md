# ScsiPeripheral\_IORequest

typedef struct ScsiPeripheral\_IORequest {...} ScsiPeripheral\_IORequest

#### Overview

Defines the read/write operation request.

**Since**: 18

**Related module**: [SCSIPeripheralDDK](../../modules/scsiperipheralddk/document.md)

**Header file**: [scsi\_peripheral\_types.h](../../header-files/scsi-peripheral-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t lbAddress | Start address of a logical block. |
| uint16\_t transferLength | Number of consecutive logical blocks to be operated. |
| uint8\_t control | **Control** field used to specify control information. |
| uint8\_t byte1 | First byte of the CDB. |
| uint8\_t byte6 | Sixth byte of the CDB. |
| ScsiPeripheral\_DeviceMemMap\* data | Buffer for data transmission. |
| uint32\_t timeout | Timeout duration, in ms. |
