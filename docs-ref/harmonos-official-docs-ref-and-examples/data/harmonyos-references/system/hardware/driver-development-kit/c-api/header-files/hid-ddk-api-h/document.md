# hid\_ddk\_api.h

#### Overview

Declares the HID DDK functions for accessing an input device from the host.

**File to include**: <hid/hid\_ddk\_api.h>

**Library**: libhid.z.so

**System capability**: SystemCapability.Driver.HID.Extension

**Since**: 11

**Related module**: [HidDdk](../../modules/hidddk/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_Hid\_CreateDevice(Hid\_Device \*hidDevice, Hid\_EventProperties \*hidEventProperties)](#oh_hid_createdevice) | Creates a device. |
| [int32\_t OH\_Hid\_EmitEvent(int32\_t deviceId, const Hid\_EmitItem items\[\], uint16\_t length)](#oh_hid_emitevent) | Sends an event list to a device. |
| [int32\_t OH\_Hid\_DestroyDevice(int32\_t deviceId)](#oh_hid_destroydevice) | Destroys a device. |
| [int32\_t OH\_Hid\_Init(void)](#oh_hid_init) | Initializes an HID DDK. |
| [int32\_t OH\_Hid\_Release(void)](#oh_hid_release) | Releases an HID DDK. |
| [int32\_t OH\_Hid\_Open(uint64\_t deviceId, uint8\_t interfaceIndex, Hid\_DeviceHandle \*\*dev)](#oh_hid_open) | Opens the device specified by **deviceId** and **interfaceIndex**. |
| [int32\_t OH\_Hid\_Close(Hid\_DeviceHandle \*\*dev)](#oh_hid_close) | Closes an HID device. |
| [int32\_t OH\_Hid\_Write(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t length, uint32\_t \*bytesWritten)](#oh_hid_write) | Writes a report to an HID device. |
| [int32\_t OH\_Hid\_ReadTimeout(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t bufSize, int timeout, uint32\_t \*bytesRead)](#oh_hid_readtimeout) | Reads a report from the HID device within the specified timeout interval. |
| [int32\_t OH\_Hid\_Read(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t bufSize, uint32\_t \*bytesRead)](#oh_hid_read) | Reads a report from the HID device. The blocking mode (that is, blocking remains active until data can be read) is used by default. You can call [OH\_Hid\_SetNonBlocking](#oh_hid_setnonblocking) to change the mode. |
| [int32\_t OH\_Hid\_SetNonBlocking(Hid\_DeviceHandle \*dev, int nonBlock)](#oh_hid_setnonblocking) | Sets the device read mode to non-blocking mode. |
| [int32\_t OH\_Hid\_GetRawInfo(Hid\_DeviceHandle \*dev, Hid\_RawDevInfo \*rawDevInfo)](#oh_hid_getrawinfo) | Obtains the original device information. |
| [int32\_t OH\_Hid\_GetRawName(Hid\_DeviceHandle \*dev, char \*data, uint32\_t bufSize)](#oh_hid_getrawname) | Obtains the original device name. |
| [int32\_t OH\_Hid\_GetPhysicalAddress(Hid\_DeviceHandle \*dev, char \*data, uint32\_t bufSize)](#oh_hid_getphysicaladdress) | Obtains the physical address of the HID device. |
| [int32\_t OH\_Hid\_GetRawUniqueId(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t bufSize)](#oh_hid_getrawuniqueid) | Obtains the original unique identifier of a device. |
| [int32\_t OH\_Hid\_SendReport(Hid\_DeviceHandle \*dev, Hid\_ReportType reportType, const uint8\_t \*data, uint32\_t length)](#oh_hid_sendreport) | Sends a report to the HID device. |
| [int32\_t OH\_Hid\_GetReport(Hid\_DeviceHandle \*dev, Hid\_ReportType reportType, uint8\_t \*data, uint32\_t bufSize)](#oh_hid_getreport) | Obtains a report from the HID device. |
| [int32\_t OH\_Hid\_GetReportDescriptor(Hid\_DeviceHandle \*dev, uint8\_t \*buf, uint32\_t bufSize, uint32\_t \*bytesRead)](#oh_hid_getreportdescriptor) | Obtains the report descriptor of the HID device. |

#### Function Description

#### \[h2\]OH\_Hid\_CreateDevice()

int32\_t OH\_Hid\_CreateDevice(Hid\_Device \*hidDevice, Hid\_EventProperties \*hidEventProperties)

**Description**

Creates a device.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Hid\_Device](../../structs/hid-device/document.md) \*hidDevice | Pointer to the basic information about the device to create, including the device name, vendor ID, and product ID. |
| [Hid\_EventProperties](../../structs/hid-eventproperties/document.md) \*hidEventProperties | Pointer to the event properties related to the device to create, including the event type, key event properties, absolute coordinate event properties, and relative coordinate event properties. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
deviceID (a non-negative number) if the API call is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INVALID\_OPERATION](../hid-ddk-types-h/document.md#hid_ddkerrcode): The hid\_ddk service connection fails.

[HID\_DDK\_INVALID\_PARAMETER](../hid-ddk-types-h/document.md#hid_ddkerrcode): The parameter check fails. Possible causes: 1. The input **hidDevice** is a null pointer.

2\. The input **hidEventProperties** is a null pointer. 3. The length of **properties** exceeds 7 characters. 4. The length of **hidEventTypes** exceeds 5 characters.

5\. The length of **hidKeys** exceeds 100 characters. 6. The length of **hidAbs** exceeds 26 characters. 7. The length of **hidRelBits** exceeds 13 characters.

8\. The length of **hidMiscellaneous** exceeds 6 characters.

[HID\_DDK\_FAILURE](../hid-ddk-types-h/document.md#hid_ddkerrcode): The number of devices reaches the maximum value 200.

 |

#### \[h2\]OH\_Hid\_EmitEvent()

int32\_t OH\_Hid\_EmitEvent(int32\_t deviceId, const Hid\_EmitItem items\[\], uint16\_t length)

**Description**

Sends an event list to a device.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t deviceId | Device ID. |
| items | List of the events to send. The event information includes the event type (**Hid\_EventType**), code (**Hid\_SynEvent**, **Hid\_KeyCode**, **HidBtnCode**, **Hid\_AbsAxes**, **Hid\_RelAxes**, or **Hid\_MscEvent**), and value (depending on the actual device input). |
| uint16\_t length | Length of the event list (number of events to be sent at a time). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode): The API call is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INVALID\_OPERATION](../hid-ddk-types-h/document.md#hid_ddkerrcode): The hid\_ddk service connection fails or the caller is not the device creator.

[HID\_DDK\_INVALID\_PARAMETER](../hid-ddk-types-h/document.md#hid_ddkerrcode): The parameter check fails. Possible causes: 1. The device ID is less than 0.

2\. The length of the input parameter **length** exceeds 7 characters. 3. The input parameter **items** is a null pointer.

[HID\_DDK\_NULL\_PTR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The input device is a null pointer.

 |

#### \[h2\]OH\_Hid\_DestroyDevice()

int32\_t OH\_Hid\_DestroyDevice(int32\_t deviceId)

**Description**

Destroys a device.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t deviceId | Device ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode): The API call is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INVALID\_OPERATION](../hid-ddk-types-h/document.md#hid_ddkerrcode): The hid\_ddk service connection fails or the caller is not the device creator.

[HID\_DDK\_FAILURE](../hid-ddk-types-h/document.md#hid_ddkerrcode): The corresponding device does not exist.

 |

#### \[h2\]OH\_Hid\_Init()

int32\_t OH\_Hid\_Init(void)

**Description**

Initializes an HID DDK.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 18

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode): The operation is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INIT\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The DDK initialization fails.

[HID\_DDK\_SERVICE\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): Communication with the DDK server fails.

 |

#### \[h2\]OH\_Hid\_Release()

int32\_t OH\_Hid\_Release(void)

**Description**

Releases an HID DDK.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 18

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode): The operation is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INIT\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The DDK initialization fails.

[HID\_DDK\_SERVICE\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): Communication with the DDK server fails.

 |

#### \[h2\]OH\_Hid\_Open()

int32\_t OH\_Hid\_Open(uint64\_t deviceId, uint8\_t interfaceIndex, Hid\_DeviceHandle \*\*dev)

**Description**

Opens the device specified by **deviceId** and **interfaceIndex**.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| uint64\_t deviceId | Device ID. |
| uint8\_t interfaceIndex | Interface index for the API of the HID device. |
| [Hid\_DeviceHandle](../../structs/hid-devicehandle/document.md) \*\*dev | Device operation handle. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode): The operation is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INIT\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The DDK initialization fails.

[HID\_DDK\_SERVICE\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): Communication with the DDK server fails.

[HID\_DDK\_MEMORY\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): Memory allocation for the device fails.

[HID\_DDK\_IO\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The I/O operation fails.

[HID\_DDK\_INVALID\_PARAMETER](../hid-ddk-types-h/document.md#hid_ddkerrcode): The **dev** parameter is null.

[HID\_DDK\_DEVICE\_NOT\_FOUND](../hid-ddk-types-h/document.md#hid_ddkerrcode): No device is found based on **deviceId** and **interfaceIndex**.

 |

#### \[h2\]OH\_Hid\_Close()

int32\_t OH\_Hid\_Close(Hid\_DeviceHandle \*\*dev)

**Description**

Closes an HID device.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [Hid\_DeviceHandle](../../structs/hid-devicehandle/document.md) \*\*dev | Device operation handle. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode): The operation is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INIT\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The DDK initialization fails.

[HID\_DDK\_SERVICE\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): Communication with the DDK server fails.

[HID\_DDK\_IO\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The I/O operation fails.

[HID\_DDK\_INVALID\_PARAMETER](../hid-ddk-types-h/document.md#hid_ddkerrcode): The **dev** parameter is null.

 |

#### \[h2\]OH\_Hid\_Write()

int32\_t OH\_Hid\_Write(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t length, uint32\_t \*bytesWritten)

**Description**

Writes a report to an HID device.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [Hid\_DeviceHandle](../../structs/hid-devicehandle/document.md) \*dev | Device operation handle. |
| uint8\_t \*data | Data to be written. |
| uint32\_t length | Length of the data to be written, in bytes. The value cannot exceed [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size). |
| uint32\_t \*bytesWritten | Number of written bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode): The operation is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INVALID\_PARAMETER](../hid-ddk-types-h/document.md#hid_ddkerrcode): The parameter check fails. Possible causes: 1. **dev** is null.

2\. **data** is null. 3. The value of **length** is **0**; 4. The value of **length** exceeds [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size).

5\. **bytesWritten** is null.

[HID\_DDK\_INIT\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The DDK initialization fails.

[HID\_DDK\_SERVICE\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): Communication with the DDK server fails.

[HID\_DDK\_IO\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The I/O operation fails.

 |

#### \[h2\]OH\_Hid\_ReadTimeout()

int32\_t OH\_Hid\_ReadTimeout(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t bufSize, int timeout, uint32\_t \*bytesRead)

**Description**

Reads a report from the HID device within the specified timeout interval.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [Hid\_DeviceHandle](../../structs/hid-devicehandle/document.md) \*dev | Device operation handle. |
| uint8\_t \*data | Buffer for storing the read data. |
| uint32\_t bufSize | Size of the buffer for storing read data. The value cannot exceed [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size). |
| int timeout | Timeout interval, in ms. The value **\-1** indicates block waiting. |
| uint32\_t \*bytesRead | Number of bytes to read. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode): The operation is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INVALID\_PARAMETER](../hid-ddk-types-h/document.md#hid_ddkerrcode): The parameter check fails. Possible causes: 1. **dev** is null.

2\. **data** is null. 3. The value of **bufSize** is **0**. 4. The value of **bufSize** exceeds [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size).

5\. **bytesRead** is null.

[HID\_DDK\_INIT\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The DDK initialization fails.

[HID\_DDK\_SERVICE\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): Communication with the DDK server fails.

[HID\_DDK\_MEMORY\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The memory data copy fails.

[HID\_DDK\_IO\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The I/O operation fails.

[HID\_DDK\_TIMEOUT](../hid-ddk-types-h/document.md#hid_ddkerrcode): The read operation times out.

 |

#### \[h2\]OH\_Hid\_Read()

int32\_t OH\_Hid\_Read(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t bufSize, uint32\_t \*bytesRead)

**Description**

Reads a report from the HID device. The blocking mode (that is, blocking remains active until data can be read) is used by default. You can call [OH\_Hid\_SetNonBlocking](#oh_hid_setnonblocking) to change the mode.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [Hid\_DeviceHandle](../../structs/hid-devicehandle/document.md) \*dev | Device operation handle. |
| uint8\_t \*data | Buffer for storing the read data. |
| uint32\_t bufSize | Size of the buffer for storing read data. The value cannot exceed [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size). |
| uint32\_t \*bytesRead | Number of bytes to read. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode): The operation is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INVALID\_PARAMETER](../hid-ddk-types-h/document.md#hid_ddkerrcode): The parameter check fails. Possible causes: 1. **dev** is null.

2\. **data** is null. 3. The value of **bufSize** is **0**. 4. The value of **bufSize** exceeds [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size).

5\. **bytesRead** is null.

[HID\_DDK\_INIT\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The DDK initialization fails.

[HID\_DDK\_SERVICE\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): Communication with the DDK server fails.

[HID\_DDK\_MEMORY\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The memory data copy fails.

[HID\_DDK\_IO\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The I/O operation fails.

[HID\_DDK\_TIMEOUT](../hid-ddk-types-h/document.md#hid_ddkerrcode): The read operation times out.

 |

#### \[h2\]OH\_Hid\_SetNonBlocking()

int32\_t OH\_Hid\_SetNonBlocking(Hid\_DeviceHandle \*dev, int nonBlock)

**Description**

Sets the device read mode to non-blocking mode.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [Hid\_DeviceHandle](../../structs/hid-devicehandle/document.md) \*dev | Device operation handle. |
| int nonBlock | 
Whether to enable the non-blocking mode for reading data. - **1**: The non-blocking mode is enabled. When [OH\_Hid\_Read](#oh_hid_read) is called, if the device has readable data, [HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode) is returned;

if the device has no readable data, [HID\_DDK\_TIMEOUT](../hid-ddk-types-h/document.md#hid_ddkerrcode) is returned. - **0**: The non-blocking mode is disabled.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode): The operation is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INIT\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The DDK initialization fails.

[HID\_DDK\_INVALID\_PARAMETER](../hid-ddk-types-h/document.md#hid_ddkerrcode): The parameter check fails. Possible causes: 1. **dev** is null.

2\. The value of **nonBlock** is not **1** or **0**.

[HID\_DDK\_SERVICE\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): Communication with the DDK server fails.

 |

#### \[h2\]OH\_Hid\_GetRawInfo()

int32\_t OH\_Hid\_GetRawInfo(Hid\_DeviceHandle \*dev, Hid\_RawDevInfo \*rawDevInfo)

**Description**

Obtains the original device information.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [Hid\_DeviceHandle](../../structs/hid-devicehandle/document.md) \*dev | Device operation handle. |
| [Hid\_RawDevInfo](../../structs/hid-rawdevinfo/document.md) \*rawDevInfo | Original device information, including the vendor ID, product ID, and bus type. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode): The operation is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INVALID\_PARAMETER](../hid-ddk-types-h/document.md#hid_ddkerrcode): The parameter check fails. Possible causes: 1. **dev** is null.

2\. **rawDevInfo** is null.

[HID\_DDK\_INIT\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The DDK initialization fails.

[HID\_DDK\_SERVICE\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): Communication with the DDK server fails.

[HID\_DDK\_IO\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The I/O operation fails.

[HID\_DDK\_INVALID\_OPERATION](../hid-ddk-types-h/document.md#hid_ddkerrcode): This operation is not supported.

 |

#### \[h2\]OH\_Hid\_GetRawName()

int32\_t OH\_Hid\_GetRawName(Hid\_DeviceHandle \*dev, char \*data, uint32\_t bufSize)

**Description**

Obtains the original device name.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [Hid\_DeviceHandle](../../structs/hid-devicehandle/document.md) \*dev | Device operation handle. |
| char \*data | Buffer for storing the read data. |
| uint32\_t bufSize | Size of the buffer for storing read data. The value cannot exceed [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode): The operation is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INVALID\_PARAMETER](../hid-ddk-types-h/document.md#hid_ddkerrcode): The parameter check fails. Possible causes: 1. **dev** is null.

2\. **data** is null. 3. The value of **bufSize** is **0**. 4. The value of **bufSize** exceeds [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size).

[HID\_DDK\_INIT\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The DDK initialization fails.

[HID\_DDK\_SERVICE\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): Communication with the DDK server fails.

[HID\_DDK\_MEMORY\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The memory data copy fails.

[HID\_DDK\_IO\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The I/O operation fails.

[HID\_DDK\_INVALID\_OPERATION](../hid-ddk-types-h/document.md#hid_ddkerrcode): This operation is not supported.

 |

#### \[h2\]OH\_Hid\_GetPhysicalAddress()

int32\_t OH\_Hid\_GetPhysicalAddress(Hid\_DeviceHandle \*dev, char \*data, uint32\_t bufSize)

**Description**

Obtains the physical address of the HID device.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [Hid\_DeviceHandle](../../structs/hid-devicehandle/document.md) \*dev | Device operation handle. |
| char \*data | Buffer for storing the read data. |
| uint32\_t bufSize | Size of the buffer for storing read data. The value cannot exceed [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode): The operation is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INVALID\_PARAMETER](../hid-ddk-types-h/document.md#hid_ddkerrcode): The parameter check fails. Possible causes: 1. **dev** is null.

2\. **data** is null. 3. The value of **bufSize** is **0**. 4. The value of **bufSize** exceeds [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size).

[HID\_DDK\_INIT\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The DDK initialization fails.

[HID\_DDK\_SERVICE\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): Communication with the DDK server fails.

[HID\_DDK\_MEMORY\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The memory data copy fails.

[HID\_DDK\_IO\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The I/O operation fails.

[HID\_DDK\_INVALID\_OPERATION](../hid-ddk-types-h/document.md#hid_ddkerrcode): This operation is not supported.

 |

#### \[h2\]OH\_Hid\_GetRawUniqueId()

int32\_t OH\_Hid\_GetRawUniqueId(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t bufSize)

**Description**

Obtains the original unique identifier of a device.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [Hid\_DeviceHandle](../../structs/hid-devicehandle/document.md) \*dev | Device operation handle. |
| uint8\_t \*data | Buffer for storing the read data. |
| uint32\_t bufSize | Size of the buffer for storing read data. The value cannot exceed [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode): The operation is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INVALID\_PARAMETER](../hid-ddk-types-h/document.md#hid_ddkerrcode): The parameter check fails. Possible causes: 1. **dev** is null.

2\. **data** is null. 3. The value of **bufSize** is **0**. 4. The value of **bufSize** exceeds [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size).

[HID\_DDK\_INIT\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The DDK initialization fails.

[HID\_DDK\_SERVICE\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): Communication with the DDK server fails.

[HID\_DDK\_MEMORY\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The memory data copy fails.

[HID\_DDK\_IO\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The I/O operation fails.

[HID\_DDK\_INVALID\_OPERATION](../hid-ddk-types-h/document.md#hid_ddkerrcode): This operation is not supported.

 |

#### \[h2\]OH\_Hid\_SendReport()

int32\_t OH\_Hid\_SendReport(Hid\_DeviceHandle \*dev, Hid\_ReportType reportType, const uint8\_t \*data, uint32\_t length)

**Description**

Sends a report to the HID device.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [Hid\_DeviceHandle](../../structs/hid-devicehandle/document.md) \*dev | Device operation handle. |
| [Hid\_ReportType](../hid-ddk-types-h/document.md#hid_reporttype) reportType | Report type. |
| const uint8\_t \*data | Data to be sent. |
| uint32\_t length | Length of the data to be sent, in bytes. The value cannot exceed [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode): The operation is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INVALID\_PARAMETER](../hid-ddk-types-h/document.md#hid_ddkerrcode): The parameter check fails. Possible causes: 1. **dev** is null.

2\. **data** is null. 3. The value of **length** is **0**; 4. The value of **length** exceeds [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size).

[HID\_DDK\_INIT\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The DDK initialization fails.

[HID\_DDK\_SERVICE\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): Communication with the DDK server fails.

[HID\_DDK\_IO\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The I/O operation fails.

[HID\_DDK\_INVALID\_OPERATION](../hid-ddk-types-h/document.md#hid_ddkerrcode): This operation is not supported.

 |

#### \[h2\]OH\_Hid\_GetReport()

int32\_t OH\_Hid\_GetReport(Hid\_DeviceHandle \*dev, Hid\_ReportType reportType, uint8\_t \*data, uint32\_t bufSize)

**Description**

Obtains a report from the HID device.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [Hid\_DeviceHandle](../../structs/hid-devicehandle/document.md) \*dev | Device operation handle. |
| [Hid\_ReportType](../hid-ddk-types-h/document.md#hid_reporttype) reportType | Report type. |
| uint8\_t \*data | Buffer for storing the read data. |
| uint32\_t bufSize | Size of the buffer for storing read data. The value cannot exceed [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode): The operation is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INVALID\_PARAMETER](../hid-ddk-types-h/document.md#hid_ddkerrcode): The parameter check fails. Possible causes: 1. **dev** is null.

2\. **data** is null. 3. The value of **bufSize** is **0**. 4. The value of **bufSize** exceeds [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size).

[HID\_DDK\_INIT\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The DDK initialization fails.

[HID\_DDK\_SERVICE\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): Communication with the DDK server fails.

[HID\_DDK\_MEMORY\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The memory data copy fails.

[HID\_DDK\_IO\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The I/O operation fails.

[HID\_DDK\_INVALID\_OPERATION](../hid-ddk-types-h/document.md#hid_ddkerrcode): This operation is not supported.

 |

#### \[h2\]OH\_Hid\_GetReportDescriptor()

int32\_t OH\_Hid\_GetReportDescriptor(Hid\_DeviceHandle \*dev, uint8\_t \*buf, uint32\_t bufSize, uint32\_t \*bytesRead)

**Description**

Obtains the report descriptor of the HID device.

**Required permissions**: ohos.permission.ACCESS\_DDK\_HID

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [Hid\_DeviceHandle](../../structs/hid-devicehandle/document.md) \*dev | Device operation handle. |
| uint8\_t \*buf | Buffer for storing descriptors. |
| uint32\_t bufSize | Buffer size, in bytes. The value cannot exceed [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size). |
| uint32\_t \*bytesRead | Number of bytes to read. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[HID\_DDK\_SUCCESS](../hid-ddk-types-h/document.md#hid_ddkerrcode): The operation is successful.

[HID\_DDK\_NO\_PERM](../hid-ddk-types-h/document.md#hid_ddkerrcode): The permission verification fails.

[HID\_DDK\_INVALID\_PARAMETER](../hid-ddk-types-h/document.md#hid_ddkerrcode): The parameter check fails. Possible causes: 1. **dev** is null.

2\. **buf** is null. 3. The value of **bufSize** is **0**. 4. The value of **bufSize** exceeds [HID\_MAX\_REPORT\_BUFFER\_SIZE](../hid-ddk-types-h/document.md#hid_max_report_buffer_size).

5\. **bytesRead** is null.

[HID\_DDK\_INIT\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The DDK initialization fails.

[HID\_DDK\_SERVICE\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): Communication with the DDK server fails.

[HID\_DDK\_MEMORY\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The memory data copy fails.

[HID\_DDK\_IO\_ERROR](../hid-ddk-types-h/document.md#hid_ddkerrcode): The I/O operation fails.

[HID\_DDK\_INVALID\_OPERATION](../hid-ddk-types-h/document.md#hid_ddkerrcode): This operation is not supported.

 |
