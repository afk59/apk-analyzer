# usb\_ddk\_api.h

#### Overview

Claims the USB DDK APIs used by the USB host to access USB devices.

**File to include**: <usb/usb\_ddk\_api.h>

**Library**: libusb\_ndk.z.so

**System capability**: SystemCapability.Driver.USB.Extension

**Since**: 10

**Related module**: [UsbDdk](../../modules/usbddk/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_Usb\_Init(void)](#oh_usb_init) | Initializes the USB DDK. |
| [void OH\_Usb\_Release(void)](#oh_usb_release) | Releases the USB DDK. |
| [int32\_t OH\_Usb\_ReleaseResource(void)](#oh_usb_releaseresource) | Releases the DDK. |
| [int32\_t OH\_Usb\_GetDeviceDescriptor(uint64\_t deviceId, struct UsbDeviceDescriptor \*desc)](#oh_usb_getdevicedescriptor) | Obtains the device descriptor. |
| [int32\_t OH\_Usb\_GetConfigDescriptor(uint64\_t deviceId, uint8\_t configIndex, struct UsbDdkConfigDescriptor \*\* const config)](#oh_usb_getconfigdescriptor) | Obtains the configuration descriptor. To avoid memory leakage, use [OH\_Usb\_FreeConfigDescriptor](#oh_usb_freeconfigdescriptor) to release a descriptor after use. |
| [void OH\_Usb\_FreeConfigDescriptor(struct UsbDdkConfigDescriptor \* const config)](#oh_usb_freeconfigdescriptor) | Releases a configuration descriptor after use to prevent memory leakage. |
| [int32\_t OH\_Usb\_ClaimInterface(uint64\_t deviceId, uint8\_t interfaceIndex, uint64\_t \*interfaceHandle)](#oh_usb_claiminterface) | Claims a USB interface. |
| [int32\_t OH\_Usb\_ReleaseInterface(uint64\_t interfaceHandle)](#oh_usb_releaseinterface) | Releases a USB interface. |
| [int32\_t OH\_Usb\_SelectInterfaceSetting(uint64\_t interfaceHandle, uint8\_t settingIndex)](#oh_usb_selectinterfacesetting) | Activates the alternate setting of a USB interface. |
| [int32\_t OH\_Usb\_GetCurrentInterfaceSetting(uint64\_t interfaceHandle, uint8\_t \*settingIndex)](#oh_usb_getcurrentinterfacesetting) | Obtains the activated alternate setting of a USB interface. |
| [int32\_t OH\_Usb\_SendControlReadRequest(uint64\_t interfaceHandle, const struct UsbControlRequestSetup \*setup,uint32\_t timeout, uint8\_t \*data, uint32\_t \*dataLen)](#oh_usb_sendcontrolreadrequest) | Sends a control read transfer request. This API works in a synchronous manner. |
| [int32\_t OH\_Usb\_SendControlWriteRequest(uint64\_t interfaceHandle, const struct UsbControlRequestSetup \*setup,uint32\_t timeout, const uint8\_t \*data, uint32\_t dataLen)](#oh_usb_sendcontrolwriterequest) | Sends a control write transfer request. This API works in a synchronous manner. |
| [int32\_t OH\_Usb\_SendPipeRequest(const struct UsbRequestPipe \*pipe, UsbDeviceMemMap \*devMmap)](#oh_usb_sendpiperequest) | Sends a pipe request. This API works in a synchronous manner. It applies to interrupt transfer and bulk transfer. |
| [int32\_t OH\_Usb\_SendPipeRequestWithAshmem(const struct UsbRequestPipe \*pipe, DDK\_Ashmem \*ashmem)](#oh_usb_sendpiperequestwithashmem) | Sends a pipe request based on the shared memory. This API returns the result synchronously. It applies to interrupt transfer and bulk transfer. |
| [int32\_t OH\_Usb\_CreateDeviceMemMap(uint64\_t deviceId, size\_t size, UsbDeviceMemMap \*\*devMmap)](#oh_usb_createdevicememmap) | Creates a buffer. To avoid resource leakage, use [OH\_Usb\_DestroyDeviceMemMap](#oh_usb_destroydevicememmap) to destroy a buffer after use. |
| [void OH\_Usb\_DestroyDeviceMemMap(UsbDeviceMemMap \*devMmap)](#oh_usb_destroydevicememmap) | Destroys a buffer. To prevent resource leakage, destroy a buffer in time after use. |
| [int32\_t OH\_Usb\_GetDevices(struct Usb\_DeviceArray \*devices)](#oh_usb_getdevices) | Obtains the USB device ID list. Ensure that the pointer parameters passed in are valid. To avoid excessive memory usage, the size of the requested device ID array is recommended not to exceed 128. After using the struct, release the memory of its members; otherwise, resource leaks may occur. Besides, make sure that the obtained USB device ID has been filtered by **vid** in the driver configuration information. |

#### Function Description

#### \[h2\]OH\_Usb\_Init()

int32\_t OH\_Usb\_Init(void)

**Description**

Initializes the USB DDK.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_DDK\_SUCCESS](../usb-ddk-types-h/document.md#usbddkerrcode): The operation is successful.

[USB\_DDK\_INVALID\_OPERATION](../usb-ddk-types-h/document.md#usbddkerrcode): The USB DDK service connection fails, or an internal error occurs.

[USB\_DDK\_NO\_PERM](../usb-ddk-types-h/document.md#usbddkerrcode): The permission check fails.

[USB\_DDK\_MEMORY\_ERROR](../usb-ddk-types-h/document.md#usbddkerrcode): The memory allocation fails.

 |

#### \[h2\]OH\_Usb\_Release()

void OH\_Usb\_Release(void)

**Description**

Releases the USB DDK.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB

**Since**: 10

#### \[h2\]OH\_Usb\_ReleaseResource()

int32\_t OH\_Usb\_ReleaseResource(void)

**Description**

Releases the USB DDK.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB

**Since**: 18

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_DDK\_SUCCESS](../usb-ddk-types-h/document.md#usbddkerrcode): The operation is successful.

[USB\_DDK\_NO\_PERM](../usb-ddk-types-h/document.md#usbddkerrcode): The permission check fails.

[USB\_DDK\_INVALID\_OPERATION](../usb-ddk-types-h/document.md#usbddkerrcode): The USB DDK service connection fails.

 |

#### \[h2\]OH\_Usb\_GetDeviceDescriptor()

int32\_t OH\_Usb\_GetDeviceDescriptor(uint64\_t deviceId, struct UsbDeviceDescriptor \*desc)

**Description**

Obtains the device descriptor.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| uint64\_t deviceId | Device ID. |
| [struct UsbDeviceDescriptor](../../structs/usbdevicedescriptor/document.md) \*desc | Device descriptor. For details, see [UsbDeviceDescriptor](../../structs/usbdevicedescriptor/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_DDK\_SUCCESS](../usb-ddk-types-h/document.md#usbddkerrcode): The operation is successful.

[USB\_DDK\_NO\_PERM](../usb-ddk-types-h/document.md#usbddkerrcode): The permission check fails.

[USB\_DDK\_INVALID\_OPERATION](../usb-ddk-types-h/document.md#usbddkerrcode): The USB DDK service connection fails.

[USB\_DDK\_INVALID\_PARAMETER](../usb-ddk-types-h/document.md#usbddkerrcode): The input **desc** is a null pointer.

 |

#### \[h2\]OH\_Usb\_GetConfigDescriptor()

int32\_t OH\_Usb\_GetConfigDescriptor(uint64\_t deviceId, uint8\_t configIndex, struct UsbDdkConfigDescriptor \*\* const config)

**Description**

Obtains the configuration descriptor. To avoid memory leakage, use [OH\_Usb\_FreeConfigDescriptor](#oh_usb_freeconfigdescriptor) to release a descriptor after use.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| uint64\_t deviceId | Device ID. |
| uint8\_t configIndex | Configuration index, which corresponds to **bConfigurationValue** in the USB protocol. |
| struct [UsbDdkConfigDescriptor](../../structs/usbddkconfigdescriptor/document.md) \*\* const config | Configuration descriptor, which includes the standard configuration descriptor defined in the USB protocol and the associated interface descriptor and endpoint descriptor. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_DDK\_SUCCESS](../usb-ddk-types-h/document.md#usbddkerrcode): The operation is successful.

[USB\_DDK\_NO\_PERM](../usb-ddk-types-h/document.md#usbddkerrcode): The permission check fails.

[USB\_DDK\_INVALID\_OPERATION](../usb-ddk-types-h/document.md#usbddkerrcode): The USB DDK service connection fails.

[USB\_DDK\_INVALID\_PARAMETER](../usb-ddk-types-h/document.md#usbddkerrcode): The input **config** is a null pointer.

[USB\_DDK\_IO\_FAILED](../usb-ddk-types-h/document.md#usbddkerrcode): An I/O exception occurs.

[USB\_DDK\_MEMORY\_ERROR](../usb-ddk-types-h/document.md#usbddkerrcode): The memory allocation fails.

 |

#### \[h2\]OH\_Usb\_FreeConfigDescriptor()

void OH\_Usb\_FreeConfigDescriptor(struct UsbDdkConfigDescriptor \* const config)

**Description**

Releases a configuration descriptor after use to prevent memory leakage.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const struct [UsbDdkConfigDescriptor](../../structs/usbddkconfigdescriptor/document.md) \* const config | Configuration descriptor, which is obtained by calling [OH\_Usb\_GetConfigDescriptor](#oh_usb_getconfigdescriptor). |

#### \[h2\]OH\_Usb\_ClaimInterface()

int32\_t OH\_Usb\_ClaimInterface(uint64\_t deviceId, uint8\_t interfaceIndex, uint64\_t \*interfaceHandle)

**Description**

Claims a USB interface.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| uint64\_t deviceId | Device ID. |
| uint8\_t interfaceIndex | Interface index, which corresponds to [bInterfaceNumber](../../structs/usbinterfacedescriptor/document.md) in the USB protocol. |
| uint64\_t \*interfaceHandle | Interface operation handle. After the interface is claimed successfully, a value will be assigned to this parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_DDK\_SUCCESS](../usb-ddk-types-h/document.md#usbddkerrcode): The operation is successful.

[USB\_DDK\_NO\_PERM](../usb-ddk-types-h/document.md#usbddkerrcode): The permission check fails.

[USB\_DDK\_INVALID\_OPERATION](../usb-ddk-types-h/document.md#usbddkerrcode): The USB DDK service connection fails.

[USB\_DDK\_INVALID\_PARAMETER](../usb-ddk-types-h/document.md#usbddkerrcode): The input **interfaceHandle** is a null pointer.

[USB\_DDK\_MEMORY\_ERROR](../usb-ddk-types-h/document.md#usbddkerrcode): The memory to be allocated exceeds the limit.

 |

#### \[h2\]OH\_Usb\_ReleaseInterface()

int32\_t OH\_Usb\_ReleaseInterface(uint64\_t interfaceHandle)

**Description**

Releases a USB interface.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| uint64\_t interfaceHandle | Interface operation handle. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_DDK\_SUCCESS](../usb-ddk-types-h/document.md#usbddkerrcode): The operation is successful.

[USB\_DDK\_NO\_PERM](../usb-ddk-types-h/document.md#usbddkerrcode): The permission check fails.

[USB\_DDK\_INVALID\_OPERATION](../usb-ddk-types-h/document.md#usbddkerrcode): The USB DDK service connection fails.

[USB\_DDK\_INVALID\_PARAMETER](../usb-ddk-types-h/document.md#usbddkerrcode): One or more parameters are invalid.

 |

#### \[h2\]OH\_Usb\_SelectInterfaceSetting()

int32\_t OH\_Usb\_SelectInterfaceSetting(uint64\_t interfaceHandle, uint8\_t settingIndex)

**Description**

Activates the alternate setting of a USB interface.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| uint64\_t interfaceHandle | Interface operation handle. |
| uint8\_t settingIndex | Index of the alternate setting, which corresponds to **bAlternateSetting** in the USB protocol. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_DDK\_SUCCESS](../usb-ddk-types-h/document.md#usbddkerrcode): The operation is successful.

[USB\_DDK\_NO\_PERM](../usb-ddk-types-h/document.md#usbddkerrcode): The permission check fails.

[USB\_DDK\_INVALID\_OPERATION](../usb-ddk-types-h/document.md#usbddkerrcode): The USB DDK service connection fails.

[USB\_DDK\_INVALID\_PARAMETER](../usb-ddk-types-h/document.md#usbddkerrcode): One or more parameters are invalid.

 |

#### \[h2\]OH\_Usb\_GetCurrentInterfaceSetting()

int32\_t OH\_Usb\_GetCurrentInterfaceSetting(uint64\_t interfaceHandle, uint8\_t \*settingIndex)

**Description**

Obtains the activated alternate setting of a USB interface.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| uint64\_t interfaceHandle | Interface operation handle. |
| uint8\_t \*settingIndex | Index of the alternate setting, which corresponds to **bAlternateSetting** in the USB protocol. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_DDK\_SUCCESS](../usb-ddk-types-h/document.md#usbddkerrcode): The operation is successful.

[USB\_DDK\_NO\_PERM](../usb-ddk-types-h/document.md#usbddkerrcode): The permission check fails.

[USB\_DDK\_INVALID\_OPERATION](../usb-ddk-types-h/document.md#usbddkerrcode): The USB DDK service connection fails.

[USB\_DDK\_INVALID\_PARAMETER](../usb-ddk-types-h/document.md#usbddkerrcode): The input **settingIndex** is a null pointer.

 |

#### \[h2\]OH\_Usb\_SendControlReadRequest()

int32\_t OH\_Usb\_SendControlReadRequest(uint64\_t interfaceHandle, const struct UsbControlRequestSetup \*setup,uint32\_t timeout, uint8\_t \*data, uint32\_t \*dataLen)

**Description**

Sends a control read transfer request. This API works in a synchronous manner.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| uint64\_t interfaceHandle | Interface operation handle. |
| [const struct UsbControlRequestSetup](../../structs/usbcontrolrequestsetup/document.md) \*setup | Request parameters. For details, see [UsbControlRequestSetup](../../structs/usbcontrolrequestsetup/document.md). |
| uint32\_t timeout | Timeout duration, in ms. |
| uint8\_t \*data | Data to transfer. |
| uint32\_t \*dataLen | Data length. The return value indicates the length of the actually read data. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_DDK\_SUCCESS](../usb-ddk-types-h/document.md#usbddkerrcode): The operation is successful.

[USB\_DDK\_FAILED](../usb-ddk-types-h/document.md#usbddkerrcode): The permission check fails.

[USB\_DDK\_INVALID\_OPERATION](../usb-ddk-types-h/document.md#usbddkerrcode): The USB DDK service connection fails.

[USB\_DDK\_INVALID\_PARAMETER](../usb-ddk-types-h/document.md#usbddkerrcode): The input **setup**, **data**, or **dataLen** is a null pointer, or the value of **datalen** is less than the length of the read data.

[USB\_DDK\_MEMORY\_ERROR](../usb-ddk-types-h/document.md#usbddkerrcode): The attempt to copy the memory that stores the read data fails.

[USB\_DDK\_IO\_FAILED](../usb-ddk-types-h/document.md#usbddkerrcode): An I/O exception occurs.

[USB\_DDK\_TIMEOUT](../usb-ddk-types-h/document.md#usbddkerrcode): The operation times out.

 |

#### \[h2\]OH\_Usb\_SendControlWriteRequest()

int32\_t OH\_Usb\_SendControlWriteRequest(uint64\_t interfaceHandle, const struct UsbControlRequestSetup \*setup,uint32\_t timeout, const uint8\_t \*data, uint32\_t dataLen)

**Description**

Sends a control write transfer request. This API works in a synchronous manner.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| uint64\_t interfaceHandle | Interface operation handle. |
| [const struct UsbControlRequestSetup](../../structs/usbcontrolrequestsetup/document.md) \*setup | Request parameters. For details, see [UsbControlRequestSetup](../../structs/usbcontrolrequestsetup/document.md). |
| uint32\_t timeout | Timeout duration, in ms. |
| const uint8\_t \*data | Data to transfer. |
| uint32\_t dataLen | Data length. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_DDK\_SUCCESS](../usb-ddk-types-h/document.md#usbddkerrcode): The operation is successful.

[USB\_DDK\_FAILED](../usb-ddk-types-h/document.md#usbddkerrcode): The permission check fails.

[USB\_DDK\_INVALID\_OPERATION](../usb-ddk-types-h/document.md#usbddkerrcode): The USB DDK service connection fails.

[USB\_DDK\_INVALID\_PARAMETER](../usb-ddk-types-h/document.md#usbddkerrcode): The input **setup** or **data** is a null pointer.

[USB\_DDK\_MEMORY\_ERROR](../usb-ddk-types-h/document.md#usbddkerrcode): The attempt to copy the memory that stores the read data fails.

[USB\_DDK\_IO\_FAILED](../usb-ddk-types-h/document.md#usbddkerrcode): An I/O exception occurs.

[USB\_DDK\_TIMEOUT](../usb-ddk-types-h/document.md#usbddkerrcode): The operation times out.

 |

#### \[h2\]OH\_Usb\_SendPipeRequest()

int32\_t OH\_Usb\_SendPipeRequest(const struct UsbRequestPipe \*pipe, UsbDeviceMemMap \*devMmap)

**Description**

Sends a pipe request. This API works in a synchronous manner. It applies to interrupt transfer and bulk transfer.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct UsbRequestPipe](../../structs/usbrequestpipe/document.md) \*pipe | Pipe used to transfer data. |
| [UsbDeviceMemMap](../../structs/usbdevicememmap/document.md) \*devMmap | Data buffer, which can be obtained by calling [OH\_Usb\_CreateDeviceMemMap](#oh_usb_createdevicememmap). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_DDK\_SUCCESS](../usb-ddk-types-h/document.md#usbddkerrcode): The operation is successful.

[USB\_DDK\_NO\_PERM](../usb-ddk-types-h/document.md#usbddkerrcode): The permission check fails.

[USB\_DDK\_INVALID\_OPERATION](../usb-ddk-types-h/document.md#usbddkerrcode): The USB DDK service connection fails.

[USB\_DDK\_INVALID\_PARAMETER](../usb-ddk-types-h/document.md#usbddkerrcode): The input **pipe** or **devMmap** is a null pointer, or the **devMmap** address is null.

[USB\_DDK\_MEMORY\_ERROR](../usb-ddk-types-h/document.md#usbddkerrcode): The attempt to copy the memory that stores the read data fails.

[USB\_DDK\_IO\_FAILED](../usb-ddk-types-h/document.md#usbddkerrcode): An I/O exception occurs.

[USB\_DDK\_TIMEOUT](../usb-ddk-types-h/document.md#usbddkerrcode): The operation times out.

 |

#### \[h2\]OH\_Usb\_SendPipeRequestWithAshmem()

int32\_t OH\_Usb\_SendPipeRequestWithAshmem(const struct UsbRequestPipe \*pipe, DDK\_Ashmem \*ashmem)

**Description**

Sends a pipe request based on the shared memory. This API returns the result synchronously. It applies to interrupt transfer and bulk transfer.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const struct UsbRequestPipe](../../structs/usbrequestpipe/document.md) \*pipe | Pipe used to transfer data. |
| [DDK\_Ashmem](../../structs/ddk-ashmem/document.md) \*ashmem | Shared memory, which can be obtained through [OH\_DDK\_CreateAshmem](../ddk-api-h/document.md#oh_ddk_createashmem). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_DDK\_SUCCESS](../usb-ddk-types-h/document.md#usbddkerrcode): The operation is successful.

[USB\_DDK\_NO\_PERM](../usb-ddk-types-h/document.md#usbddkerrcode): The permission check fails.

[USB\_DDK\_INVALID\_OPERATION](../usb-ddk-types-h/document.md#usbddkerrcode): The USB DDK service connection fails.

[USB\_DDK\_INVALID\_PARAMETER](../usb-ddk-types-h/document.md#usbddkerrcode): The input **pipe** or **ashmem** is a null pointer, or the **ashmem** address is null.

[USB\_DDK\_MEMORY\_ERROR](../usb-ddk-types-h/document.md#usbddkerrcode): The attempt to copy the memory that stores the read data fails.

[USB\_DDK\_IO\_FAILED](../usb-ddk-types-h/document.md#usbddkerrcode): An I/O exception occurs.

[USB\_DDK\_TIMEOUT](../usb-ddk-types-h/document.md#usbddkerrcode): The operation times out.

 |

#### \[h2\]OH\_Usb\_CreateDeviceMemMap()

int32\_t OH\_Usb\_CreateDeviceMemMap(uint64\_t deviceId, size\_t size, UsbDeviceMemMap \*\*devMmap)

**Description**

Creates a buffer. To avoid resource leakage, use [OH\_Usb\_DestroyDeviceMemMap](#oh_usb_destroydevicememmap) to destroy a buffer after use.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| uint64\_t deviceId | Device ID. |
| size\_t size | Buffer size. |
| [UsbDeviceMemMap](../../structs/usbdevicememmap/document.md) \*\*devMmap | Data memory map, through which the created buffer is returned to the caller. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_DDK\_SUCCESS](../usb-ddk-types-h/document.md#usbddkerrcode): The operation is successful.

[USB\_DDK\_NO\_PERM](../usb-ddk-types-h/document.md#usbddkerrcode): The permission check fails.

[USB\_DDK\_INVALID\_PARAMETER](../usb-ddk-types-h/document.md#usbddkerrcode): The input parameter **devMmap** or \***devMmap** is a null pointer.

[USB\_DDK\_MEMORY\_ERROR](../usb-ddk-types-h/document.md#usbddkerrcode): The memory mapping fails, or the memory allocation of **devMmap** fails.

 |

#### \[h2\]OH\_Usb\_DestroyDeviceMemMap()

void OH\_Usb\_DestroyDeviceMemMap(UsbDeviceMemMap \*devMmap)

**Description**

Destroys a buffer. To prevent resource leakage, destroy a buffer in time after use.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [UsbDeviceMemMap](../../structs/usbdevicememmap/document.md) \*devMmap | Destroys the buffer created by calling [OH\_Usb\_CreateDeviceMemMap](#oh_usb_createdevicememmap). |

#### \[h2\]OH\_Usb\_GetDevices()

int32\_t OH\_Usb\_GetDevices(struct Usb\_DeviceArray \*devices)

**Description**

Obtains the USB device ID list. Ensure that the pointer parameters passed in are valid. To avoid excessive memory usage, the size of the requested device ID array is recommended not to exceed 128. After using the struct, release the memory of its members; otherwise, resource leaks may occur. Besides, make sure that the obtained USB device ID has been filtered by **vid** in the driver configuration information.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct Usb\_DeviceArray](../../structs/usb-devicearray/document.md) \*devices | Device memory address, which is used to store the obtained device ID list and quantity. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_DDK\_SUCCESS](../usb-ddk-types-h/document.md#usbddkerrcode): The operation is successful.

[USB\_DDK\_NO\_PERM](../usb-ddk-types-h/document.md#usbddkerrcode): The permission check fails.

[USB\_DDK\_INVALID\_OPERATION](../usb-ddk-types-h/document.md#usbddkerrcode): The USB DDK service connection fails.

[USB\_DDK\_INVALID\_PARAMETER](../usb-ddk-types-h/document.md#usbddkerrcode): The input **devices** is a null pointer.

 |
