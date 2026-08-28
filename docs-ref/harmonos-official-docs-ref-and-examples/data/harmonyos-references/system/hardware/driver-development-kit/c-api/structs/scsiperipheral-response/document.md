# ScsiPeripheral\_Response

#### Overview

Defines the response structure.

**Since**: 18

**Related module**: [SCSIPeripheralDDK](../../modules/scsiperipheralddk/document.md)

**Header file**: [scsi\_peripheral\_types.h](../../header-files/scsi-peripheral-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t senseData\[SCSIPERIPHERAL\_MAX\_SENSE\_DATA\_LEN\] | Sense data, that is, information returned by the SCSI device to the host to report the device status, error information, and diagnosis information. |
| ScsiPeripheral\_Status status | Status when the call is complete, for example, **Good** or **Busy**. |
| uint8\_t maskedStatus | Masked status, which is used in SCSI Generic (SG) interfaces of Linux to store the processed SCSI status for easy access by applications. |
| uint8\_t msgStatus | Message status. |
| uint8\_t sbLenWr | Number of bytes that are actually written to the sense buffer. |
| uint16\_t hostStatus | Host adapter status, for example, success (0x00), connection failure (0x01), busy bus (0x02), or timeout (0x03). |
| uint16\_t driverStatus | Driver status, for example, success (0x00) or busy device or resource (0x01). |
| int32\_t resId | Length deviation of the actually transmitted data, that is, the number of bytes that are not transmitted. |
| uint32\_t duration | Command execution duration, in ms. |
