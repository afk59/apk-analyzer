# ScsiPeripheral\_RequestSenseRequest

typedef struct ScsiPeripheral\_RequestSenseRequest {...} ScsiPeripheral\_RequestSenseRequest

#### Overview

Defines the request structure of the **Request Sense** command.

**Since**: 18

**Related module**: [SCSIPeripheralDDK](../../modules/scsiperipheralddk/document.md)

**Header file**: [scsi\_peripheral\_types.h](../../header-files/scsi-peripheral-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t allocationLength | **Allocation length** field used to specify the size of the buffer prepared by the request initiator (usually the host) for the response data. |
| uint8\_t control | **Control** field used to specify control information. |
| uint8\_t byte1 | First byte of the CDB. |
| uint32\_t timeout | Timeout duration, in ms. |
