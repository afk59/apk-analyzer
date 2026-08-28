# ScsiPeripheral\_Request

typedef struct ScsiPeripheral\_Request {...} ScsiPeripheral\_Request

#### Overview

Defines the request structure.

**Since**: 18

**Related module**: [SCSIPeripheralDDK](../../modules/scsiperipheralddk/document.md)

**Header file**: [scsi\_peripheral\_types.h](../../header-files/scsi-peripheral-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t commandDescriptorBlock\[SCSIPERIPHERAL\_MAX\_CMD\_DESC\_BLOCK\_LEN\] | Command descriptor block. |
| uint8\_t cdbLength | Length of the command descriptor block. |
| int8\_t dataTransferDirection | Data transfer direction: **–1** indicates no data transfer, **–2** indicates data transfer (write) from the host to the device, **–3** indicates data transfer (read) from the device to the host, and **–4** indicates bidirectional data transfer. |
| ScsiPeripheral\_DeviceMemMap\* data | Buffer for data transmission. |
| uint32\_t timeout | Timeout duration, in ms. |
