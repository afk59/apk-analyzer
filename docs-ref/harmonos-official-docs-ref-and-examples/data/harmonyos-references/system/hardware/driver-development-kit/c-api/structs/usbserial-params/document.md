# UsbSerial\_Params

typedef struct UsbSerial\_Params {...} \_\_attribute\_\_((aligned(8))) UsbSerial\_Params

#### Overview

Defines the USB serial port parameters for the USB Serial DDK.

**Since**: 18

**Related module**: [SerialDdk](../../modules/usbserialddk/document.md)

**Header file:** [usb\_serial\_types.h](../../header-files/usb-serial-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t baudRate | Baud rate, in bauds. |
| uint8\_t nDataBits | Number of data bits. |
| uint8\_t nStopBits | Number of stop bits. |
| uint8\_t parity | Parity parameter setting. **0**: no parity; **1**: odd parity; **2**: even parity; **3**: mark parity (parity bit always 1); **4**: space parity (parity bit always 0) |
