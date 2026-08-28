# Usb\_DeviceArray

#### Overview

Defines the device ID list, which is used to store the device IDs and device quantity obtained using **OH\_Usb\_GetDevices**.

**Since**: 18

**Related module**: [UsbDDK](../../modules/usbddk/document.md)

**Header file:** [usb\_ddk\_types.h](../../header-files/usb-ddk-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint64\_t\* deviceIds | Defines the start address of the device ID array. The number of device IDs cannot exceed 128. |
| uint32\_t num | Defines the device quantity. Device IDs are obtained by traversing **deviceIds** based on the value of this parameter. If the value is **0**, there is no USB device. |
