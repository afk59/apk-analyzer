# ScsiPeripheral\_InquiryRequest

#### Overview

Defines the request structure of the **inquiry** command.

**Since**: 18

**Related module**: [SCSIPeripheralDDK](../../modules/scsiperipheralddk/document.md)

**Header file**: [scsi\_peripheral\_types.h](../../header-files/scsi-peripheral-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t pageCode | **Page code** field. Set this field if you want to obtain certain types of device information. When an **Inquiry** command with a specific page code is run, the device returns details related to the page code. If the page code is set to **0x00**, it indicates that the standard inquiry data rather than the data of specific pages is requested. |
| uint16\_t allocationLength | **Allocation length** field used to specify the size of the buffer prepared by the request initiator (usually the host) for the response data. |
| uint8\_t control | **Control** field used to specify control information. |
| uint8\_t byte1 | First byte of the CDB. |
| uint32\_t timeout | Timeout duration, in ms. |
