# UsbEndpointDescriptor

#### Overview

Defines standard endpoint descriptors, which correspond to **Standard Endpoint Descriptor** in the USB protocol.

**Since**: 10

**Related module**: [UsbDDK](../../modules/usbddk/document.md)

**Header file:** [usb\_ddk\_types.h](../../header-files/usb-ddk-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t bLength | Size of the descriptor, in bytes. |
| uint8\_t bDescriptorType | Descriptor type. |
| uint8\_t bEndpointAddress | Endpoint address, including the endpoint number and endpoint direction. |
| uint8\_t bmAttributes | Endpoint attributes, including the transfer type, synchronization type, and usage type. |
| uint16\_t wMaxPacketSize | Maximum packet size supported by an endpoint. |
| uint8\_t bInterval | Interval for polling endpoints for data transfer. |
| uint8\_t bRefresh | Refresh rate for audio devices. |
| uint8\_t bSynchAddress | Endpoint synchronization address for audio devices. |
