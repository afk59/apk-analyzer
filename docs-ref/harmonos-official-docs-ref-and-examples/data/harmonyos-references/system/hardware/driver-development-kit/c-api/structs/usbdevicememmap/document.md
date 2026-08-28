# UsbDeviceMemMap

typedef struct UsbDeviceMemMap {...} UsbDeviceMemMap

#### Overview

Device memory map created by calling **OH\_Usb\_CreateDeviceMemMap**. A buffer using the device memory map can improve data transmission performance.

**Since**: 10

**Related module**: [UsbDDK](../../modules/usbddk/document.md)

**Header file:** [usb\_ddk\_types.h](../../header-files/usb-ddk-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t\* const address | Buffer address. |
| const size\_t size | Buffer size. |
| uint32\_t offset | Offset of the used buffer. The default value is **0**, indicating that there is no offset and the offset starts from the buffer address. |
| uint32\_t bufferLength | Length of the used buffer. By default, the value is equal to the buffer size, indicating that the entire buffer is used. |
| uint32\_t transferedLength | Length of the transferred data. |
