# ScsiPeripheral\_DeviceMemMap

typedef struct ScsiPeripheral\_DeviceMemMap {...} ScsiPeripheral\_DeviceMemMap

#### Overview

Represents the device memory mapping created by calling **OH\_ScsiPeripheral\_CreateDeviceMemMap**. The buffer that uses the device memory mapping can provide better performance.

**Since**: 18

**Related module**: [SCSIPeripheralDDK](../../modules/scsiperipheralddk/document.md)

**Header file**: [scsi\_peripheral\_types.h](../../header-files/scsi-peripheral-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t\* const address | Buffer address. |
| const size\_t size | Buffer size. |
| uint32\_t offset | Offset of the used buffer. The default value is **0**, indicating that there is no offset and the buffer starts from the specified address. |
| uint32\_t bufferLength | Length of the used buffer. By default, the value is equal to the size of the buffer, indicating that the entire buffer is used. |
| uint32\_t transferredLength | Length of the transferred data. |
