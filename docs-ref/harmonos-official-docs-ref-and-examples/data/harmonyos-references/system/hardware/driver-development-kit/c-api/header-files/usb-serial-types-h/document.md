# usb\_serial\_types.h

#### Overview

Provides the enum variables, structures, and macros used in USB Serial DDK APIs.

**File to include**: <usb\_serial/usb\_serial\_types.h>

**Library:** libusb\_serial\_ndk.z.so

**System capability**: SystemCapability.Driver.UsbSerial.Extension

**Since**: 18

**Related module**: [USBSerialDDK](../../modules/usbserialddk/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [UsbSerial\_Params](../../structs/usbserial-params/document.md) | \_\_attribute\_\_((aligned(8))) UsbSerial\_Params | Defines the USB serial port parameters for the USB Serial DDK. |
| [UsbSerial\_Device](../../structs/usbserial-device/document.md) | UsbSerial\_Device | Defines the data structures for the USB serial port device (opaque). |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [UsbSerial\_DdkRetCode](#usbserial_ddkretcode) | UsbSerial\_DdkRetCode | Defines the return codes used by the USB Serial DDK. |
| [UsbSerial\_FlowControl](#usbserial_flowcontrol) | UsbSerial\_FlowControl | Defines the flow control mode for the USB Serial DDK. |
| [UsbSerial\_Parity](#usbserial_parity) | UsbSerial\_Parity | Defines the enums of the parity parameter used by the USB Serial DDK. |

#### Enum Description

#### \[h2\]UsbSerial\_DdkRetCode

enum UsbSerial\_DdkRetCode

**Description**

Defines the return codes used by the USB Serial DDK.

**Since**: 18

| Enum | Description |
| :-- | :-- |
| USB\_SERIAL\_DDK\_NO\_PERM = 201 | No access permission. |
| USB\_SERIAL\_DDK\_INVALID\_PARAMETER = 401 | Invalid parameter. |
| USB\_SERIAL\_DDK\_SUCCESS = 31600000 | Operation success. |
| USB\_SERIAL\_DDK\_INVALID\_OPERATION = 31600001 | Invalid operation. |
| USB\_SERIAL\_DDK\_INIT\_ERROR = 31600002 | Initialization error. |
| USB\_SERIAL\_DDK\_SERVICE\_ERROR = 31600003 | Service error. |
| USB\_SERIAL\_DDK\_MEMORY\_ERROR = 31600004 | Memory-related errors, such as insufficient memory, memory data replication failure, or memory application fault. |
| USB\_SERIAL\_DDK\_IO\_ERROR = 31600005 | I/O error. |
| USB\_SERIAL\_DDK\_DEVICE\_NOT\_FOUND = 31600006 | Device not found. |

#### \[h2\]UsbSerial\_FlowControl

enum UsbSerial\_FlowControl

**Description**

Defines the flow control mode for the USB Serial DDK.

**Since**: 18

| Enum | Description |
| :-- | :-- |
| USB\_SERIAL\_NO\_FLOW\_CONTROL = 0 | No flow control. |
| USB\_SERIAL\_SOFTWARE\_FLOW\_CONTROL = 1 | Software flow control. |
| USB\_SERIAL\_HARDWARE\_FLOW\_CONTROL = 2 | Hardware flow control. |

#### \[h2\]UsbSerial\_Parity

enum UsbSerial\_Parity

**Description**

Defines the enums of the parity parameter used by the USB Serial DDK.

**Since**: 18

| Enum | Description |
| :-- | :-- |
| USB\_SERIAL\_PARITY\_NONE = 0 | No parity. |
| USB\_SERIAL\_PARITY\_ODD = 1 | Odd parity. |
| USB\_SERIAL\_PARITY\_EVEN = 2 | Even parity. |
