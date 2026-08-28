# UsbDdkEndpointDescriptor

#### Overview

Defines endpoint descriptors.

**Since**: 10

**Related module**: [UsbDDK](../../modules/usbddk/document.md)

**Header file:** [usb\_ddk\_types.h](../../header-files/usb-ddk-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| struct UsbEndpointDescriptor endpointDescriptor | Standard endpoint descriptor. |
| const uint8\_t\* extra | Unresolved descriptor, including class- or vendor-specific descriptors. |
| uint32\_t extraLength | Length of the unresolved descriptor. |
