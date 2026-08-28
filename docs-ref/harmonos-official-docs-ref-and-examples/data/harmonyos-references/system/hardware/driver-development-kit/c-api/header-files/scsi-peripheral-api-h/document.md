# scsi\_peripheral\_api.h

#### Overview

Declares the SCSI Peripheral DDK APIs used by the host to access the SCSI device.

**File to include**: <scsi\_peripheral/scsi\_peripheral\_api.h>

**Library**: libscsi.z.so

**System capability**: SystemCapability.Driver.SCSI.Extension

**Since**: 18

**Related module**: [ScsiPeripheralDDK](../../modules/scsiperipheralddk/document.md)

#### Summary

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_ScsiPeripheral\_Init(void)](#oh_scsiperipheral_init) | Initializes the SCSI Peripheral DDK. |
| [int32\_t OH\_ScsiPeripheral\_Release(void)](#oh_scsiperipheral_release) | Releases the SCSI Peripheral DDK. |
| [int32\_t OH\_ScsiPeripheral\_Open(uint64\_t deviceId, uint8\_t interfaceIndex, ScsiPeripheral\_Device \*\*dev)](#oh_scsiperipheral_open) | Opens the SCSI device specified by **deviceId** and **interfaceIndex**. The **deviceId** can be obtained by shifting the bus number of the USB device left by 32 bits and then performing a bitwise OR operation with the device address. **interfaceIndex** refers to the index of the USB interface to be opened. |
| [int32\_t OH\_ScsiPeripheral\_Close(ScsiPeripheral\_Device \*\*dev)](#oh_scsiperipheral_close) | Closes the SCSI device. |
| [int32\_t OH\_ScsiPeripheral\_TestUnitReady(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_TestUnitReadyRequest \*request,ScsiPeripheral\_Response \*response)](#oh_scsiperipheral_testunitready) | Checks whether the logical unit is ready. |
| [int32\_t OH\_ScsiPeripheral\_Inquiry(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_InquiryRequest \*request,ScsiPeripheral\_InquiryInfo \*inquiryInfo, ScsiPeripheral\_Response \*response)](#oh_scsiperipheral_inquiry) | Queries basic information about the SCSI device. |
| [int32\_t OH\_ScsiPeripheral\_ReadCapacity10(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_ReadCapacityRequest \*request,ScsiPeripheral\_CapacityInfo \*capacityInfo, ScsiPeripheral\_Response \*response)](#oh_scsiperipheral_readcapacity10) | Obtains the capacity information about the SCSI device. |
| [int32\_t OH\_ScsiPeripheral\_RequestSense(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_RequestSenseRequest \*request,ScsiPeripheral\_Response \*response)](#oh_scsiperipheral_requestsense) | Obtains sense data, that is, information returned by the SCSI device to the host to report the device status, error information, and diagnosis information. |
| [int32\_t OH\_ScsiPeripheral\_Read10(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_IORequest \*request,ScsiPeripheral\_Response \*response)](#oh_scsiperipheral_read10) | Reads data from a specified logical block. |
| [int32\_t OH\_ScsiPeripheral\_Write10(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_IORequest \*request,ScsiPeripheral\_Response \*response)](#oh_scsiperipheral_write10) | Writes data to a specified logical block of a device. |
| [int32\_t OH\_ScsiPeripheral\_Verify10(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_VerifyRequest \*request,ScsiPeripheral\_Response \*response)](#oh_scsiperipheral_verify10) | Verifies a specified logical block. |
| [int32\_t OH\_ScsiPeripheral\_SendRequestByCdb(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_Request \*request,ScsiPeripheral\_Response \*response)](#oh_scsiperipheral_sendrequestbycdb) | Sends SCSI commands in CDB mode. |
| [int32\_t OH\_ScsiPeripheral\_CreateDeviceMemMap(ScsiPeripheral\_Device \*dev, size\_t size,ScsiPeripheral\_DeviceMemMap \*\*devMmap)](#oh_scsiperipheral_createdevicememmap) | Creates a buffer. To avoid resource leakage, use [OH\_ScsiPeripheral\_DestroyDeviceMemMap](#oh_scsiperipheral_destroydevicememmap) to destroy a buffer after use. |
| [int32\_t OH\_ScsiPeripheral\_DestroyDeviceMemMap(ScsiPeripheral\_DeviceMemMap \*devMmap)](#oh_scsiperipheral_destroydevicememmap) | Destroys a buffer. To prevent resource leakage, destroy a buffer in time after use. |
| [int32\_t OH\_ScsiPeripheral\_ParseBasicSenseInfo(uint8\_t \*senseData, uint8\_t senseDataLen,ScsiPeripheral\_BasicSenseInfo \*senseInfo)](#oh_scsiperipheral_parsebasicsenseinfo) | Parses basic sense data, including the **Information**, **Command specific information**, and **Sense key specific** fields. |

#### Function Description

#### \[h2\]OH\_ScsiPeripheral\_Init()

int32\_t OH\_ScsiPeripheral\_Init(void)

**Description**

Initializes the SCSI Peripheral DDK.

**Required permissions**: ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL

**Since**: 18

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCSIPERIPHERAL\_DDK\_SUCCESS](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The API call is successful.

[SCSIPERIPHERAL\_DDK\_NO\_PERM](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The permission verification fails.

[SCSIPERIPHERAL\_DDK\_INIT\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The DDK initialization fails.

[SCSIPERIPHERAL\_DDK\_SERVICE\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The communication with the DDK service fails.

 |

#### \[h2\]OH\_ScsiPeripheral\_Release()

int32\_t OH\_ScsiPeripheral\_Release(void)

**Description**

Releases the SCSI Peripheral DDK.

**Required permissions**: ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL

**Since**: 18

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCSIPERIPHERAL\_DDK\_SUCCESS](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The API call is successful.

[SCSIPERIPHERAL\_DDK\_NO\_PERM](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The permission verification fails.

[SCSIPERIPHERAL\_DDK\_INIT\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The DDK is not initialized.

[SCSIPERIPHERAL\_DDK\_SERVICE\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The communication with the DDK service fails.

 |

#### \[h2\]OH\_ScsiPeripheral\_Open()

int32\_t OH\_ScsiPeripheral\_Open(uint64\_t deviceId, uint8\_t interfaceIndex, ScsiPeripheral\_Device \*\*dev)

**Description**

Opens the SCSI device specified by **deviceId** and **interfaceIndex**. The **deviceId** can be obtained by shifting the bus number of the USB device left by 32 bits and then performing a bitwise OR operation with the device address. **interfaceIndex** refers to the index of the USB interface to be opened.

**Required permissions**: ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| uint64\_t deviceId | Device ID. |
| uint8\_t interfaceIndex | Interface index for the API of the SCSI device. |
| [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md) \*\*dev | Device handle. For details, see [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCSIPERIPHERAL\_DDK\_SUCCESS](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The API call is successful.

[SCSIPERIPHERAL\_DDK\_NO\_PERM](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The permission verification fails.

[SCSIPERIPHERAL\_DDK\_INIT\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The DDK is not initialized.

[SCSIPERIPHERAL\_DDK\_INVALID\_PARAMETER](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The input **dev** or \***dev** is null.

[SCSIPERIPHERAL\_DDK\_SERVICE\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The communication with the DDK service fails.

[SCSIPERIPHERAL\_DDK\_MEMORY\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The memory operation fails.

[SCSIPERIPHERAL\_DDK\_IO\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): An I/O error occurs.

[SCSIPERIPHERAL\_DDK\_DEVICE\_NOT\_FOUND](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): No device is found based on the specified **deviceId** and **interfaceIndex**.

[SCSIPERIPHERAL\_DDK\_INVALID\_OPERATION](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The operation is not supported.

 |

#### \[h2\]OH\_ScsiPeripheral\_Close()

int32\_t OH\_ScsiPeripheral\_Close(ScsiPeripheral\_Device \*\*dev)

**Description**

Closes the SCSI device.

**Required permissions**: ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md) \*\*dev | Device handle. For details, see [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCSIPERIPHERAL\_DDK\_SUCCESS](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The API call is successful.

[SCSIPERIPHERAL\_DDK\_NO\_PERM](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The permission verification fails.

[SCSIPERIPHERAL\_DDK\_INIT\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The DDK is not initialized.

[SCSIPERIPHERAL\_DDK\_INVALID\_PARAMETER](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The input **dev** or \***dev** is null.

[SCSIPERIPHERAL\_DDK\_SERVICE\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The communication with the DDK service fails.

[SCSIPERIPHERAL\_DDK\_IO\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): An I/O error occurs.

 |

#### \[h2\]OH\_ScsiPeripheral\_TestUnitReady()

int32\_t OH\_ScsiPeripheral\_TestUnitReady(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_TestUnitReadyRequest \*request,ScsiPeripheral\_Response \*response)

**Description**

Checks whether the logical unit is ready.

**Required permissions**: ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md) \*dev | Device handle. For details, see [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md). |
| [ScsiPeripheral\_TestUnitReadyRequest](../../structs/scsiperipheral-testunitreadyrequest/document.md) \*request | Request of the **test unit ready** command. For details, see [ScsiPeripheral\_TestUnitReadyRequest](../../structs/scsiperipheral-testunitreadyrequest/document.md). |
| [ScsiPeripheral\_Response](../../structs/scsiperipheral-response/document.md) \*response | Response returned by the **test unit ready** command. For details, see [ScsiPeripheral\_Response](../../structs/scsiperipheral-response/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCSIPERIPHERAL\_DDK\_SUCCESS](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The API call is successful.

[SCSIPERIPHERAL\_DDK\_NO\_PERM](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The permission verification fails.

[SCSIPERIPHERAL\_DDK\_INIT\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The DDK is not initialized.

[SCSIPERIPHERAL\_DDK\_INVALID\_PARAMETER](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The input **dev**, **request**, or **response** is null.

[SCSIPERIPHERAL\_DDK\_SERVICE\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The communication with the DDK service fails.

[SCSIPERIPHERAL\_DDK\_MEMORY\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The memory operation fails.

[SCSIPERIPHERAL\_DDK\_IO\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): An I/O error occurs.

[SCSIPERIPHERAL\_DDK\_TIMEOUT](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The transmission times out.

[SCSIPERIPHERAL\_DDK\_INVALID\_OPERATION](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The operation is not supported.

 |

#### \[h2\]OH\_ScsiPeripheral\_Inquiry()

int32\_t OH\_ScsiPeripheral\_Inquiry(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_InquiryRequest \*request,ScsiPeripheral\_InquiryInfo \*inquiryInfo, ScsiPeripheral\_Response \*response)

**Description**

Queries basic information about the SCSI device.

**Required permissions**: ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md) \*dev | Device handle. For details, see [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md). |
| [ScsiPeripheral\_InquiryRequest](../../structs/scsiperipheral-inquiryrequest/document.md) \*request | Request of the **inquiry** command. For details, see [ScsiPeripheral\_InquiryRequest](../../structs/scsiperipheral-inquiryrequest/document.md). |
| [ScsiPeripheral\_InquiryInfo](../../structs/scsiperipheral-inquiryinfo/document.md) \*inquiryInfo | Query result returned by the **inquiry** command. For details, see [ScsiPeripheral\_InquiryInfo](../../structs/scsiperipheral-inquiryinfo/document.md). |
| [ScsiPeripheral\_Response](../../structs/scsiperipheral-response/document.md) \*response | Raw response returned by the inquiry command. For details, see [ScsiPeripheral\_Response](../../structs/scsiperipheral-response/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCSIPERIPHERAL\_DDK\_SUCCESS](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The API call is successful.

[SCSIPERIPHERAL\_DDK\_NO\_PERM](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The permission verification fails.

[SCSIPERIPHERAL\_DDK\_INIT\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The DDK is not initialized.

[SCSIPERIPHERAL\_DDK\_INVALID\_PARAMETER](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The input **dev**, **request**, **inquiryInfo**, **inquiryInfo->data**, or **response** is null.

[SCSIPERIPHERAL\_DDK\_SERVICE\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The communication with the DDK service fails.

[SCSIPERIPHERAL\_DDK\_MEMORY\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The memory operation fails.

[SCSIPERIPHERAL\_DDK\_IO\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): An I/O error occurs.

[SCSIPERIPHERAL\_DDK\_TIMEOUT](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The transmission times out.

[SCSIPERIPHERAL\_DDK\_INVALID\_OPERATION](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The operation is not supported.

 |

#### \[h2\]OH\_ScsiPeripheral\_ReadCapacity10()

int32\_t OH\_ScsiPeripheral\_ReadCapacity10(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_ReadCapacityRequest \*request,ScsiPeripheral\_CapacityInfo \*capacityInfo, ScsiPeripheral\_Response \*response)

**Description**

Obtains the capacity information about the SCSI device.

**Required permissions**: ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md) \*dev | Device handle. For details, see [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md). |
| [ScsiPeripheral\_ReadCapacityRequest](../../structs/scsiperipheral-readcapacityrequest/document.md) \*request | Request of the **read capacity** command. For details, see [ScsiPeripheral\_ReadCapacityRequest](../../structs/scsiperipheral-readcapacityrequest/document.md). |
| [ScsiPeripheral\_CapacityInfo](../../structs/scsiperipheral-capacityinfo/document.md) \*capacityInfo | Capacity information returned by the **read capacity** command. For details, see [ScsiPeripheral\_CapacityInfo](../../structs/scsiperipheral-capacityinfo/document.md). |
| [ScsiPeripheral\_Response](../../structs/scsiperipheral-response/document.md) \*response | Original response returned by the **read capacity** command. For details, see [ScsiPeripheral\_Response](../../structs/scsiperipheral-response/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCSIPERIPHERAL\_DDK\_SUCCESS](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The API call is successful.

[SCSIPERIPHERAL\_DDK\_NO\_PERM](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The permission verification fails.

[SCSIPERIPHERAL\_DDK\_INIT\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The DDK is not initialized.

[SCSIPERIPHERAL\_DDK\_INVALID\_PARAMETER](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The input **dev**, **request**, **capacityInfo**, or **response** is null.

[SCSIPERIPHERAL\_DDK\_SERVICE\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The communication with the DDK service fails.

[SCSIPERIPHERAL\_DDK\_MEMORY\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The memory operation fails.

[SCSIPERIPHERAL\_DDK\_IO\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): An I/O error occurs.

[SCSIPERIPHERAL\_DDK\_TIMEOUT](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The transmission times out.

[SCSIPERIPHERAL\_DDK\_INVALID\_OPERATION](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The operation is not supported.

 |

#### \[h2\]OH\_ScsiPeripheral\_RequestSense()

int32\_t OH\_ScsiPeripheral\_RequestSense(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_RequestSenseRequest \*request,ScsiPeripheral\_Response \*response)

**Description**

Obtains sense data, that is, information returned by the SCSI device to the host to report the device status, error information, and diagnosis information.

**Required permissions**: ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md) \*dev | Device handle. For details, see [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md). |
| [ScsiPeripheral\_RequestSenseRequest](../../structs/scsiperipheral-requestsenserequest/document.md) \*request | Request of the **Request Sense** command. For details, see [ScsiPeripheral\_RequestSenseRequest](../../structs/scsiperipheral-requestsenserequest/document.md). |
| [ScsiPeripheral\_Response](../../structs/scsiperipheral-response/document.md) \*response | Response returned by the **Request Sense** command. For details, see [ScsiPeripheral\_Response](../../structs/scsiperipheral-response/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCSIPERIPHERAL\_DDK\_SUCCESS](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The API call is successful.

[SCSIPERIPHERAL\_DDK\_NO\_PERM](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The permission verification fails.

[SCSIPERIPHERAL\_DDK\_INIT\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The DDK is not initialized.

[SCSIPERIPHERAL\_DDK\_INVALID\_PARAMETER](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The input **dev**, **request**, or **response** is null.

[SCSIPERIPHERAL\_DDK\_SERVICE\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The communication with the DDK service fails.

[SCSIPERIPHERAL\_DDK\_MEMORY\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The memory operation fails.

[SCSIPERIPHERAL\_DDK\_IO\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): An I/O error occurs.

[SCSIPERIPHERAL\_DDK\_TIMEOUT](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The transmission times out.

[SCSIPERIPHERAL\_DDK\_INVALID\_OPERATION](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The operation is not supported.

 |

#### \[h2\]OH\_ScsiPeripheral\_Read10()

int32\_t OH\_ScsiPeripheral\_Read10(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_IORequest \*request,ScsiPeripheral\_Response \*response)

**Description**

Reads data from a specified logical block.

**Required permissions**: ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md) \*dev | Device handle. For details, see [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md). |
| [ScsiPeripheral\_IORequest](../../structs/scsiperipheral-iorequest/document.md) \*request | Request of the **read** command. For details, see [ScsiPeripheral\_IORequest](../../structs/scsiperipheral-iorequest/document.md). |
| [ScsiPeripheral\_Response](../../structs/scsiperipheral-response/document.md) \*response | Response returned by the **read** command. For details, see [ScsiPeripheral\_Response](../../structs/scsiperipheral-response/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCSIPERIPHERAL\_DDK\_SUCCESS](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The API call is successful.

[SCSIPERIPHERAL\_DDK\_NO\_PERM](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The permission verification fails.

[SCSIPERIPHERAL\_DDK\_INIT\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The DDK is not initialized.

[SCSIPERIPHERAL\_DDK\_INVALID\_PARAMETER](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The input **dev**, **request**, **request->data**, or **response** is null.

[SCSIPERIPHERAL\_DDK\_SERVICE\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The communication with the DDK service fails.

[SCSIPERIPHERAL\_DDK\_MEMORY\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The memory operation fails.

[SCSIPERIPHERAL\_DDK\_IO\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): An I/O error occurs.

[SCSIPERIPHERAL\_DDK\_TIMEOUT](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The transmission times out.

[SCSIPERIPHERAL\_DDK\_INVALID\_OPERATION](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The operation is not supported.

 |

#### \[h2\]OH\_ScsiPeripheral\_Write10()

int32\_t OH\_ScsiPeripheral\_Write10(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_IORequest \*request,ScsiPeripheral\_Response \*response)

**Description**

Writes data to a specified logical block of a device.

**Required permissions**: ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md) \*dev | Device handle. For details, see [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md). |
| [ScsiPeripheral\_IORequest](../../structs/scsiperipheral-iorequest/document.md) \*request | Request of the **write** command. For details, see [ScsiPeripheral\_IORequest](../../structs/scsiperipheral-iorequest/document.md). |
| [ScsiPeripheral\_Response](../../structs/scsiperipheral-response/document.md) \*response | Response returned by the **write** command. For details, see [ScsiPeripheral\_Response](../../structs/scsiperipheral-response/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCSIPERIPHERAL\_DDK\_SUCCESS](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The API call is successful.

[SCSIPERIPHERAL\_DDK\_NO\_PERM](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The permission verification fails.

[SCSIPERIPHERAL\_DDK\_INIT\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The DDK is not initialized.

[SCSIPERIPHERAL\_DDK\_INVALID\_PARAMETER](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The input **dev**, **request**, **request->data**, or **response** is null.

[SCSIPERIPHERAL\_DDK\_SERVICE\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The communication with the DDK service fails.

[SCSIPERIPHERAL\_DDK\_MEMORY\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The memory operation fails.

[SCSIPERIPHERAL\_DDK\_IO\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): An I/O error occurs.

[SCSIPERIPHERAL\_DDK\_TIMEOUT](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The transmission times out.

[SCSIPERIPHERAL\_DDK\_INVALID\_OPERATION](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The operation is not supported.

 |

#### \[h2\]OH\_ScsiPeripheral\_Verify10()

int32\_t OH\_ScsiPeripheral\_Verify10(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_VerifyRequest \*request,ScsiPeripheral\_Response \*response)

**Description**

Verifies a specified logical block.

**Required permissions**: ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md) \*dev | Device handle. For details, see [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md). |
| [ScsiPeripheral\_VerifyRequest](../../structs/scsiperipheral-verifyrequest/document.md) \*request | Request of the **verify** command. For details, see [ScsiPeripheral\_VerifyRequest](../../structs/scsiperipheral-verifyrequest/document.md). |
| [ScsiPeripheral\_Response](../../structs/scsiperipheral-response/document.md) \*response | Response returned by the **verify** command. For details, see [ScsiPeripheral\_Response](../../structs/scsiperipheral-response/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCSIPERIPHERAL\_DDK\_SUCCESS](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The API call is successful.

[SCSIPERIPHERAL\_DDK\_NO\_PERM](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The permission verification fails.

[SCSIPERIPHERAL\_DDK\_INIT\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The DDK is not initialized.

[SCSIPERIPHERAL\_DDK\_INVALID\_PARAMETER](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The input **dev**, **request**, or **response** is null.

[SCSIPERIPHERAL\_DDK\_SERVICE\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The communication with the DDK service fails.

[SCSIPERIPHERAL\_DDK\_MEMORY\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The memory operation fails.

[SCSIPERIPHERAL\_DDK\_IO\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): An I/O error occurs.

[SCSIPERIPHERAL\_DDK\_TIMEOUT](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The transmission times out.

[SCSIPERIPHERAL\_DDK\_INVALID\_OPERATION](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The operation is not supported.

 |

#### \[h2\]OH\_ScsiPeripheral\_SendRequestByCdb()

int32\_t OH\_ScsiPeripheral\_SendRequestByCdb(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_Request \*request,ScsiPeripheral\_Response \*response)

**Description**

Sends SCSI commands in CDB mode.

**Required permissions**: ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md) \*dev | Device handle. For details, see [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md). |
| [ScsiPeripheral\_Request](../../structs/scsiperipheral-request/document.md) \*request | Request. For details, see [ScsiPeripheral\_Request](../../structs/scsiperipheral-request/document.md). |
| [ScsiPeripheral\_Response](../../structs/scsiperipheral-response/document.md) \*response | Response. For details, see [ScsiPeripheral\_Response](../../structs/scsiperipheral-response/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCSIPERIPHERAL\_DDK\_SUCCESS](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The API call is successful.

[SCSIPERIPHERAL\_DDK\_NO\_PERM](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The permission verification fails.

[SCSIPERIPHERAL\_DDK\_INIT\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The DDK is not initialized.

[SCSIPERIPHERAL\_DDK\_INVALID\_PARAMETER](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The input **dev**, **request**, **request->data**, or **response**

is null, or **request->cdbLength** is 0.

[SCSIPERIPHERAL\_DDK\_SERVICE\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The communication with the DDK service fails.

[SCSIPERIPHERAL\_DDK\_MEMORY\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The memory operation fails.

[SCSIPERIPHERAL\_DDK\_IO\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): An I/O error occurs.

[SCSIPERIPHERAL\_DDK\_TIMEOUT](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The transmission times out.

[SCSIPERIPHERAL\_DDK\_INVALID\_OPERATION](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The operation is not supported.

 |

#### \[h2\]OH\_ScsiPeripheral\_CreateDeviceMemMap()

int32\_t OH\_ScsiPeripheral\_CreateDeviceMemMap(ScsiPeripheral\_Device \*dev, size\_t size,ScsiPeripheral\_DeviceMemMap \*\*devMmap)

**Description**

Creates a buffer. To avoid resource leakage, use [OH\_ScsiPeripheral\_DestroyDeviceMemMap](#oh_scsiperipheral_destroydevicememmap) to destroy a buffer after use.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md) \*dev | Device handle. For details, see [ScsiPeripheral\_Device](../../structs/scsiperipheral-device/document.md). |
| size\_t size | Buffer size. |
| [ScsiPeripheral\_DeviceMemMap](../../structs/scsiperipheral-devicememmap/document.md) \*\*devMmap | Device memory mapping used to return the created buffer to the caller. For details, see [ScsiPeripheral\_DeviceMemMap](../../structs/scsiperipheral-devicememmap/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCSIPERIPHERAL\_DDK\_SUCCESS](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The API call is successful.

[SCSIPERIPHERAL\_DDK\_INVALID\_PARAMETER](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The input **dev**, **devMmap**, or \***devMmap** is null.

[SCSIPERIPHERAL\_DDK\_MEMORY\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The memory operation fails.

 |

#### \[h2\]OH\_ScsiPeripheral\_DestroyDeviceMemMap()

int32\_t OH\_ScsiPeripheral\_DestroyDeviceMemMap(ScsiPeripheral\_DeviceMemMap \*devMmap)

**Description**

Destroys a buffer. To prevent resource leakage, destroy a buffer in time after use.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ScsiPeripheral\_DeviceMemMap](../../structs/scsiperipheral-devicememmap/document.md) \*devMmap | Buffer to be destroyed, which is created by calling [OH\_ScsiPeripheral\_CreateDeviceMemMap](#oh_scsiperipheral_createdevicememmap). For details, see [ScsiPeripheral\_DeviceMemMap](../../structs/scsiperipheral-devicememmap/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCSIPERIPHERAL\_DDK\_SUCCESS](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The API call is successful.

[SCSIPERIPHERAL\_DDK\_INVALID\_PARAMETER](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The input **devMmap** is null.

[SCSIPERIPHERAL\_DDK\_MEMORY\_ERROR](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The memory operation fails.

 |

#### \[h2\]OH\_ScsiPeripheral\_ParseBasicSenseInfo()

int32\_t OH\_ScsiPeripheral\_ParseBasicSenseInfo(uint8\_t \*senseData, uint8\_t senseDataLen,ScsiPeripheral\_BasicSenseInfo \*senseInfo)

**Description**

Parses basic sense data, including the **Information**, **Command specific information**, and **Sense key specific** fields.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| uint8\_t \*senseData | Sense data to be parsed. |
| uint8\_t senseDataLen | Length of sense data. |
| [ScsiPeripheral\_BasicSenseInfo](../../structs/scsiperipheral-basicsenseinfo/document.md) \*senseInfo | Basic sense data after parsing. For details, see [ScsiPeripheral\_BasicSenseInfo](../../structs/scsiperipheral-basicsenseinfo/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCSIPERIPHERAL\_DDK\_SUCCESS](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The API call is successful.

[SCSIPERIPHERAL\_DDK\_INVALID\_PARAMETER](../scsi-peripheral-types-h/document.md#scsiperipheral_ddkerrcode): The input **senseData** is not a descriptor or is not of the fixed format, or **senseDataLen** is smaller than

**SCSIPERIPHERAL\_MIN\_DESCRIPTOR\_FORMAT\_SENSE** or **SCSIPERIPHERAL\_MIN\_FIXED\_FORMAT\_SENSE**.

 |
