# scsi\_peripheral\_types.h

#### Overview

Provides the enum variables, structures, and macros used in the SCSI Peripheral DDK APIs.

**File to include**: <scsi\_peripheral/scsi\_peripheral\_types.h>

**Library**: libscsi.z.so

**System capability**: SystemCapability.Driver.SCSI.Extension

**Since**: 18

**Related module**: [ScsiPeripheralDDK](../../modules/scsiperipheralddk/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ScsiPeripheral\_DeviceMemMap](../../structs/scsiperipheral-devicememmap/document.md) | ScsiPeripheral\_DeviceMemMap | Represents the device memory mapping created by calling **OH\_ScsiPeripheral\_CreateDeviceMemMap**. The buffer that uses the device memory mapping can provide better performance. |
| [ScsiPeripheral\_IORequest](../../structs/scsiperipheral-iorequest/document.md) | ScsiPeripheral\_IORequest | Read/write operation request. |
| [ScsiPeripheral\_Request](../../structs/scsiperipheral-request/document.md) | ScsiPeripheral\_Request | Request structure. |
| [ScsiPeripheral\_Response](../../structs/scsiperipheral-response/document.md) | ScsiPeripheral\_Response | Response structure. |
| [ScsiPeripheral\_TestUnitReadyRequest](../../structs/scsiperipheral-testunitreadyrequest/document.md) | ScsiPeripheral\_TestUnitReadyRequest | Request structure of the **test unit ready** command. |
| [ScsiPeripheral\_InquiryRequest](../../structs/scsiperipheral-inquiryrequest/document.md) | ScsiPeripheral\_InquiryRequest | Request structure of the **inquiry** command. |
| [ScsiPeripheral\_InquiryInfo](../../structs/scsiperipheral-inquiryinfo/document.md) | ScsiPeripheral\_InquiryInfo | SCSI inquiry data. |
| [ScsiPeripheral\_ReadCapacityRequest](../../structs/scsiperipheral-readcapacityrequest/document.md) | ScsiPeripheral\_ReadCapacityRequest | Request structure of the **read capacity** command. |
| [ScsiPeripheral\_CapacityInfo](../../structs/scsiperipheral-capacityinfo/document.md) | ScsiPeripheral\_CapacityInfo | SCSI read capacity. |
| [ScsiPeripheral\_RequestSenseRequest](../../structs/scsiperipheral-requestsenserequest/document.md) | ScsiPeripheral\_RequestSenseRequest | Request structure of the **Request Sense** command. |
| [ScsiPeripheral\_BasicSenseInfo](../../structs/scsiperipheral-basicsenseinfo/document.md) | ScsiPeripheral\_BasicSenseInfo | Basic information about the sense data. |
| [ScsiPeripheral\_VerifyRequest](../../structs/scsiperipheral-verifyrequest/document.md) | ScsiPeripheral\_VerifyRequest | Request structure of the **verify** command. |
| [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md) | ScsiPeripheral\_Device | Opaque SCSI device structure. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ScsiPeripheral\_DdkErrCode](#scsiperipheral_ddkerrcode) | ScsiPeripheral\_DdkErrCode | SCSI Peripheral DDK error codes. |
| [ScsiPeripheral\_Status](#scsiperipheral_status) | ScsiPeripheral\_Status | SCSI status used for the response. |

#### Enum Description

#### \[h2\]ScsiPeripheral\_DdkErrCode

enum ScsiPeripheral\_DdkErrCode

**Description**

SCSI Peripheral DDK error codes.

**Since**: 18

| Enum | Description |
| :-- | :-- |
| SCSIPERIPHERAL\_DDK\_NO\_PERM = 201 | Permission denied. |
| SCSIPERIPHERAL\_DDK\_INVALID\_PARAMETER = 401 | Invalid parameter. |
| SCSIPERIPHERAL\_DDK\_SUCCESS = 31700000 | Operation success. |
| SCSIPERIPHERAL\_DDK\_MEMORY\_ERROR = 31700001 | Memory-related errors, such as insufficient memory, memory data replication failure, or memory request failure. |
| SCSIPERIPHERAL\_DDK\_INVALID\_OPERATION = 31700002 | Invalid operation. |
| SCSIPERIPHERAL\_DDK\_IO\_ERROR = 31700003 | Device input/output operation failed. |
| SCSIPERIPHERAL\_DDK\_TIMEOUT = 31700004 | Transfer timeout. |
| SCSIPERIPHERAL\_DDK\_INIT\_ERROR = 31700005 | DDK initialization error, or DDK uninitialized. |
| SCSIPERIPHERAL\_DDK\_SERVICE\_ERROR = 31700006 | Communication with the SCSI Peripheral DDK failed. |
| SCSIPERIPHERAL\_DDK\_DEVICE\_NOT\_FOUND = 31700007 | Device not found. |

#### \[h2\]ScsiPeripheral\_Status

enum ScsiPeripheral\_Status

**Description**

Enumerates the SCSI status codes used for the response.

**Since**: 18

| Enum | Description |
| :-- | :-- |
| SCSIPERIPHERAL\_STATUS\_GOOD = 0x00 | Normal state. |
| SCSIPERIPHERAL\_STATUS\_CHECK\_CONDITION\_NEEDED = 0x02 | Status check required. |
| SCSIPERIPHERAL\_STATUS\_CONDITION\_MET = 0x04 | Conditions met. |
| SCSIPERIPHERAL\_STATUS\_BUSY = 0x08 | Occupying. |
| SCSIPERIPHERAL\_STATUS\_RESERVATION\_CONFLICT = 0x18 | Resource reservation conflict. |
| SCSIPERIPHERAL\_STATUS\_TASK\_SET\_FULL = 0x28 | Task set already full. |
| SCSIPERIPHERAL\_STATUS\_ACA\_ACTIVE = 0x30 | ACA activity status. |
| SCSIPERIPHERAL\_STATUS\_TASK\_ABORTED = 0x40 | Task aborted. |

#### \[h2\]SCSIPERIPHERAL\_MIN\_DESCRIPTOR\_FORMAT\_SENSE

SCSIPERIPHERAL\_MIN\_DESCRIPTOR\_FORMAT\_SENSE 8

**Description**

Defines the minimum length of the sensing data in the descriptor format.

**Since**: 18

#### \[h2\]SCSIPERIPHERAL\_MIN\_FIXED\_FORMAT\_SENSE

SCSIPERIPHERAL\_MIN\_FIXED\_FORMAT\_SENSE 18

**Description**

Defines the minimum length of the sensing data in the fixed format.

**Since**: 18

#### \[h2\]SCSIPERIPHERAL\_MAX\_CMD\_DESC\_BLOCK\_LEN

SCSIPERIPHERAL\_MAX\_CMD\_DESC\_BLOCK\_LEN 16

**Description**

Maximum length of a command description block.

**Since**: 18

#### \[h2\]SCSIPERIPHERAL\_MAX\_SENSE\_DATA\_LEN

SCSIPERIPHERAL\_MAX\_SENSE\_DATA\_LEN 252

**Description**

Defines the maximum length of the sensing data.

**Since**: 18

#### \[h2\]SCSIPERIPHERAL\_VENDOR\_ID\_LEN

SCSIPERIPHERAL\_VENDOR\_ID\_LEN 8

**Description**

Defines the length of a vendor ID.

**Since**: 18

#### \[h2\]SCSIPERIPHERAL\_PRODUCT\_ID\_LEN

SCSIPERIPHERAL\_PRODUCT\_ID\_LEN 16

**Description**

Defines the length of a product ID.

**Since**: 18

#### \[h2\]SCSIPERIPHERAL\_PRODUCT\_REV\_LEN

SCSIPERIPHERAL\_PRODUCT\_REV\_LEN 4

**Description**

Defines the length of a product revision version.

**Since**: 18
