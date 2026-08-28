# UsbConfigDescriptor

#### Overview

Defines standard configuration descriptors, which correspond to **Standard Configuration Descriptor** in the USB protocol.

**Since**: 10

**Related module**: [UsbDDK](../../modules/usbddk/document.md)

**Header file:** [usb\_ddk\_types.h](../../header-files/usb-ddk-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t bLength | Size of the descriptor, in bytes. |
| uint8\_t bDescriptorType | Descriptor type. |
| uint16\_t wTotalLength | Total length of the configuration descriptor, including the configuration, interface, endpoint, and class- or vendor-specific descriptors. |
| uint8\_t bNumInterfaces | Number of interfaces supported by the configuration. |
| uint8\_t bConfigurationValue | Configuration index, which is used to select the configuration. |
| uint8\_t iConfiguration | Index of the string descriptor that describes the configuration. |
| uint8\_t bmAttributes | Configuration attributes, including the power mode and remote wakeup. |
| uint8\_t bMaxPower | Maximum power consumption of the bus-powered USB device, in 2 mA. |
