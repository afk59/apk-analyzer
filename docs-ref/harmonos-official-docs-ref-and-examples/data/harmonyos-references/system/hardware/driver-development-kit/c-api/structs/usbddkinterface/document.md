# UsbDdkInterface

#### Overview

Defines a USB DDK API, which is a collection of alternate settings for a particular USB interface.

**Since**: 10

**Related module**: [UsbDDK](../../modules/usbddk/document.md)

**Header file:** [usb\_ddk\_types.h](../../header-files/usb-ddk-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t numAltsetting | Number of alternate settings of the USB interface. |
| struct UsbDdkInterfaceDescriptor\* altsetting | Alternate setting of the USB interface. |
