# ScsiPeripheral\_InquiryInfo

typedef struct ScsiPeripheral\_InquiryInfo {...} ScsiPeripheral\_InquiryInfo

#### Overview

Defines the SCSI inquiry data.

**Since**: 18

**Related module**: [SCSIPeripheralDDK](../../modules/scsiperipheralddk/document.md)

**Header file**: [scsi\_peripheral\_types.h](../../header-files/scsi-peripheral-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t deviceType | Device type. |
| char idVendor\[[SCSIPERIPHERAL\_VENDOR\_ID\_LEN](../../header-files/scsi-peripheral-types-h/document.md) + 1\] | Vendor ID. |
| char idProduct\[[SCSIPERIPHERAL\_PRODUCT\_ID\_LEN](../../header-files/scsi-peripheral-types-h/document.md) + 1\] | Product ID. |
| char revProduct\[[SCSIPERIPHERAL\_PRODUCT\_REV\_LEN](../../header-files/scsi-peripheral-types-h/document.md) + 1\] | Product version. |
| ScsiPeripheral\_DeviceMemMap\* data | Inquiry data. |
