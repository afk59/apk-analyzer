# UsbControlRequestSetup

#### Overview

Setup data for control transfer. It corresponds to **Setup Data** in the USB protocol.

**Since**: 10

**Related module**: [UsbDDK](../../modules/usbddk/document.md)

**Header file:** [usb\_ddk\_types.h](../../header-files/usb-ddk-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t bmRequestType | Request type. |
| uint8\_t bRequest | Specific request. |
| uint16\_t wValue | Value corresponding to **wValue** in the USB protocol. Its meaning varies according to the request. |
| uint16\_t wIndex | Index corresponding to **wIndex** in the USB protocol. It is usually used to pass the index or offset. Its meaning varies according to the request. |
| uint16\_t wLength | Data length corresponding to **wLength** in the USB protocol. If data is transferred, this field indicates the number of transferred bytes. |
