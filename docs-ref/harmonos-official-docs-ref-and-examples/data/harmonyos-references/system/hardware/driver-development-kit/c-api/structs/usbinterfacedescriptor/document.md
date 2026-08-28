# UsbInterfaceDescriptor

#### Overview

Defines standard interface descriptors, which correspond to **Standard Interface Descriptor** in the USB protocol.

**Since**: 10

**Related module**: [UsbDDK](../../modules/usbddk/document.md)

**Header file:** [usb\_ddk\_types.h](../../header-files/usb-ddk-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t bLength | Size of the descriptor, in bytes. |
| uint8\_t bDescriptorType | Descriptor type. |
| uint8\_t bInterfaceNumber | Interface ID. |
| uint8\_t bAlternateSetting | Value used to select the alternate setting of the interface. |
| uint8\_t bNumEndpoints | Number of endpoints (excluding endpoint 0) used by the interface. |
| uint8\_t bInterfaceClass | Interface class code allocated by the USB-IF. |
| uint8\_t bInterfaceSubClass | Device subclass code allocated by USB-IF. The value is limited by that of {@link bInterfaceClass}. |
| uint8\_t bInterfaceProtocol | Protocol code allocated by USB-IF. The value is limited by that of {@link bInterfaceClass} and {@link bInterfaceSubClass}. |
| uint8\_t iInterface | Index of the string descriptor that describes the interface. |
