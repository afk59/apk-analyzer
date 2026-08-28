# ScsiPeripheral\_BasicSenseInfo

#### Overview

Defines the basic information about the sense data.

**Since**: 18

**Related module**: [SCSIPeripheralDDK](../../modules/scsiperipheralddk/document.md)

**Header file**: [scsi\_peripheral\_types.h](../../header-files/scsi-peripheral-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t responseCode | Response code. |
| bool valid | Information validity flag. |
| uint64\_t information | **Information** field. |
| uint64\_t commandSpecific | **Command-specific information** field. |
| bool sksv | Flag of the **Sense key specific** field. |
| uint32\_t senseKeySpecific | **Sense key specific** field. |
