# usb\_ddk\_types.h

#### Overview

Provides the enumerated variables, structures, and macros used in USB DDK APIs.

**File to include**: <usb/usb\_ddk\_types.h>

**Library**: libusb\_ndk.z.so

**System capability**: SystemCapability.Driver.USB.Extension

**Since**: 10

**Related module**: [UsbDdk](../../modules/usbddk/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [UsbControlRequestSetup](../../structs/usbcontrolrequestsetup/document.md) | \_\_attribute\_\_((aligned(8))) UsbControlRequestSetup | Control transfer setup data, which corresponds to **Setup Data** in the USB protocol. |
| [UsbDeviceDescriptor](../../structs/usbdevicedescriptor/document.md) | \_\_attribute\_\_((aligned(8))) UsbDeviceDescriptor | Standard device descriptor, which corresponds to **Standard Device Descriptor** in the USB protocol. |
| [UsbConfigDescriptor](../../structs/usbconfigdescriptor/document.md) | \_\_attribute\_\_((packed)) UsbConfigDescriptor | Standard configuration descriptor, which corresponds to **Standard Configuration Descriptor** in the USB protocol. |
| [UsbInterfaceDescriptor](../../structs/usbinterfacedescriptor/document.md) | \_\_attribute\_\_((packed)) UsbInterfaceDescriptor | Standard interface descriptor, which corresponds to **Standard Interface Descriptor** in the USB protocol. |
| [UsbEndpointDescriptor](../../structs/usbendpointdescriptor/document.md) | \_\_attribute\_\_((packed)) UsbEndpointDescriptor | Standard endpoint descriptor, which corresponds to **Standard Endpoint Descriptor** in the USB protocol. |
| [UsbDdkEndpointDescriptor](../../structs/usbddkendpointdescriptor/document.md) | UsbDdkEndpointDescriptor | Endpoint descriptor. |
| [UsbDdkInterfaceDescriptor](../../structs/usbddkinterfacedescriptor/document.md) | UsbDdkInterfaceDescriptor | Interface descriptor. |
| [UsbDdkInterface](../../structs/usbddkinterface/document.md) | UsbDdkInterface | USB DDK interface, which is a collection of alternate settings for a particular USB interface. |
| [UsbDdkConfigDescriptor](../../structs/usbddkconfigdescriptor/document.md) | UsbDdkConfigDescriptor | Configuration descriptor. |
| [UsbRequestPipe](../../structs/usbrequestpipe/document.md) | \_\_attribute\_\_((aligned(8))) UsbRequestPipe | Defines a USB request pipe. |
| [UsbDeviceMemMap](../../structs/usbdevicememmap/document.md) | UsbDeviceMemMap | Device memory map created by calling **OH\_Usb\_CreateDeviceMemMap**. A buffer using the device memory map can provide better performance. |
| [Usb\_DeviceArray](../../structs/usb-devicearray/document.md) | Usb\_DeviceArray | Defines the device ID list, which is used to store the device IDs and device quantity obtained using **OH\_Usb\_GetDevices**. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [UsbDdkErrCode](#usbddkerrcode) | UsbDdkErrCode | USB DDK error code definitions. |

#### Enum Description

#### \[h2\]UsbDdkErrCode

enum UsbDdkErrCode

**Description**

USB DDK error code definitions.

**Since**: 10

| Enum | Description |
| :-- | :-- |
| USB\_DDK\_SUCCESS = 0 | Operation succeeded. |
| USB\_DDK\_FAILED = -1 | 
Operation failed.

**Deprecated from**: 16

 |
| USB\_DDK\_NO\_PERM = 201 | 

No permission.

**Since**: 14

 |
| USB\_DDK\_INVALID\_PARAMETER = 401 | Invalid parameter. The value is **\-2** before API version 16. |
| USB\_DDK\_MEMORY\_ERROR = 27400001 | Memory errors, such as insufficient memory, memory data copy failure, or memory allocation failure. The value is **\-3** before API version 16. |
| USB\_DDK\_INVALID\_OPERATION = 27400002 | Invalid operation. The value is **\-4** before API version 16. |
| USB\_DDK\_NULL\_PTR = -5 | 

Null pointer.

**Deprecated from**: 16

 |
| USB\_DDK\_DEVICE\_BUSY = -6 | 

Device busy.

**Deprecated from**: 16

 |
| USB\_DDK\_IO\_FAILED = 27400003 | 

Device I/O operation failure.

**Since**: 14

 |
| USB\_DDK\_TIMEOUT = 27400004 | Transmission timeout. The value is **\-7** before API version 16. |
