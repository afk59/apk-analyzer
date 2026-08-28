# UsbDdkConfigDescriptor

#### Overview

Defines configuration descriptors.

**Since**: 10

**Related module**: [UsbDDK](../../modules/usbddk/document.md)

**Header file:** [usb\_ddk\_types.h](../../header-files/usb-ddk-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| struct UsbConfigDescriptor configDescriptor | Standard configuration descriptor. |
| struct UsbDdkInterface\* interface | Interfaces contained in the configuration. |
| const uint8\_t\* extra | Unresolved descriptor, including class- or vendor-specific descriptors. |
| uint32\_t extraLength | Length of the unresolved descriptor. |
