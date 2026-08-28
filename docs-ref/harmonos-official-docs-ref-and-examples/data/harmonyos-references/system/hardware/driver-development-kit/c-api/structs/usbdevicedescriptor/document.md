# UsbDeviceDescriptor

typedef struct UsbDeviceDescriptor {...} \_\_attribute\_\_((aligned(8))) UsbDeviceDescriptor

#### Overview

Defines standard device descriptors, which correspond to **Standard Device Descriptor** in the USB protocol.

**Since**: 10

**Related module**: [UsbDDK](../../modules/usbddk/document.md)

**Header file:** [usb\_ddk\_types.h](../../header-files/usb-ddk-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t bLength | Size of the descriptor, in bytes. |
| uint8\_t bDescriptorType | Descriptor type. |
| uint16\_t bcdUSB | Version of the USB protocol. |
| uint8\_t bDeviceClass | Device class code allocated by the USB-IF. |
| uint8\_t bDeviceSubClass | Device subclass code allocated by the USB-IF. The value is limited by that of **bDeviceClass**. |
| uint8\_t bDeviceProtocol | Device protocol code allocated by the USB-IF. The value is limited by that of **bDeviceClass** and **bDeviceSubClass**. |
| uint8\_t bMaxPacketSize0 | Maximum packet size of endpoint 0. Only values 8, 16, 32, and 64 are valid. |
| uint16\_t idVendor | Vendor ID allocated by USB-IF. |
| uint16\_t idProduct | Product ID allocated by the vendor. |
| uint16\_t bcdDevice | Device version number. |
| uint8\_t iManufacturer | Index of the string descriptor that describes the vendor. |
| uint8\_t iProduct | Index of the string descriptor that describes the product. |
| uint8\_t iSerialNumber | Index of the string descriptor that describes the device SN. |
| uint8\_t bNumConfigurations | Configuration quantity. |
