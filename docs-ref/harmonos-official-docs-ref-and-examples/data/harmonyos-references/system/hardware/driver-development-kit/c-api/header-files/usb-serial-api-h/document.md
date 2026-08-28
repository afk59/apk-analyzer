# usb\_serial\_api.h

#### Overview

Declares the USB Serial DDK APIs used by the host to access the serial port device through the USB port.

**File to include**: <usb\_serial/usb\_serial\_api.h>

**Library:** libusb\_serial\_ndk.z.so

**System capability**: SystemCapability.Driver.UsbSerial.Extension

**Since**: 18

**Related module**: [USBSerialDDK](../../modules/usbserialddk/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_UsbSerial\_Init(void)](#oh_usbserial_init) | Initializes the USB Serial DDK. |
| [int32\_t OH\_UsbSerial\_Release(void)](#oh_usbserial_release) | Releases the USB Serial DDK. |
| [int32\_t OH\_UsbSerial\_Open(uint64\_t deviceId, uint8\_t interfaceIndex, UsbSerial\_Device \*\*dev)](#oh_usbserial_open) | Opens the USB serial port device based on the specified **deviceId** and **interfaceIndex**. |
| [int32\_t OH\_UsbSerial\_Close(UsbSerial\_Device \*\*dev)](#oh_usbserial_close) | Closes the USB serial port device. |
| [int32\_t OH\_UsbSerial\_Read(UsbSerial\_Device \*dev, uint8\_t \*buff, uint32\_t bufferSize, uint32\_t \*bytesRead)](#oh_usbserial_read) | Reads data from the USB serial port device to the buffer. |
| [int32\_t OH\_UsbSerial\_Write(UsbSerial\_Device \*dev, uint8\_t \*buff, uint32\_t bufferSize, uint32\_t \*bytesWritten)](#oh_usbserial_write) | Writes the data in the buffer to the USB serial port device. |
| [int32\_t OH\_UsbSerial\_SetBaudRate(UsbSerial\_Device \*dev, uint32\_t baudRate)](#oh_usbserial_setbaudrate) | Sets the baud rate for a USB serial port device. If the parameters of the USB serial port device are set to the default values (the data bit is **8**, the stop bit is **1**, and parity is disabled for data transfer), you only need to call this API to set the baud rate. |
| [int32\_t OH\_UsbSerial\_SetParams(UsbSerial\_Device \*dev, UsbSerial\_Params \*params)](#oh_usbserial_setparams) | Sets the parameters of the USB serial port device. If the parameters of the USB serial port device are not set to the default values (the data bit is **8**, the stop bit is **1**, and parity is disabled for data transfer), you only need to call this API to set the related parameters. |
| [int32\_t OH\_UsbSerial\_SetTimeout(UsbSerial\_Device \*dev, int timeout)](#oh_usbserial_settimeout) | Sets the timeout interval (ms) for reading data reported by a USB serial port device. If this function is not called, the timeout value is **0** by default, indicating that data is returned immediately regardless of whether data is read. If you need to wait for a certain period of time or data must be read, call this API to set the timeout interval. |
| [int32\_t OH\_UsbSerial\_SetFlowControl(UsbSerial\_Device \*dev, UsbSerial\_FlowControl flowControl)](#oh_usbserial_setflowcontrol) | 
Sets flow control parameters. Flow control is used to manage the data transfer rate during communication with the USB serial port device to ensure that the sender does not send data that exceeds the processing capability of the receiver.

If flow control is required, call this API to set flow control parameters. If this API is not called, flow control is not performed by default.

 |
| [int32\_t OH\_UsbSerial\_Flush(UsbSerial\_Device \*dev)](#oh_usbserial_flush) | Flushes the input and output buffers after the write operation is complete. If a large amount of data is to be transmitted to the USB serial port device, the data may be buffered in the kernel for transmission. If the application closes the file descriptor or exits before the data is completely sent out, some data may be lost. You can call this API to ensure that all data is sent before subsequent operations are performed. |
| [int32\_t OH\_UsbSerial\_FlushInput(UsbSerial\_Device \*dev)](#oh_usbserial_flushinput) | 

Flushes the input buffer. The data in the buffer is cleared immediately. During the communication with the USB serial port device, especially in the debugging phase, disordered data packets or other exceptions may occur.

You can call this API to clear these exceptions to restore the communication.

 |
| [int32\_t OH\_UsbSerial\_FlushOutput(UsbSerial\_Device \*dev)](#oh_usbserial_flushoutput) | 

Flushes the output buffer. The data in the buffer is cleared immediately. During the communication with the USB serial port device, especially in the debugging phase, disordered data packets or other exceptions may occur.

You can call this API to clear these exceptions to restore the communication.

 |

#### Function Description

#### \[h2\]OH\_UsbSerial\_Init()

int32\_t OH\_UsbSerial\_Init(void)

**Description**

Initializes the USB Serial DDK.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB\_SERIAL

**Since**: 18

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_SERIAL\_DDK\_SUCCESS](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is successful.

[USB\_SERIAL\_DDK\_NO\_PERM](../usb-serial-types-h/document.md#usbserial_ddkretcode): The permission verification fails.

[USB\_SERIAL\_DDK\_INIT\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK initialization fails.

 |

#### \[h2\]OH\_UsbSerial\_Release()

int32\_t OH\_UsbSerial\_Release(void)

**Description**

Releases the USB Serial DDK.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB\_SERIAL

**Since**: 18

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_SERIAL\_DDK\_SUCCESS](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is successful.

[USB\_SERIAL\_DDK\_NO\_PERM](../usb-serial-types-h/document.md#usbserial_ddkretcode): The permission verification fails.

[USB\_SERIAL\_DDK\_INIT\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK initialization fails.

[USB\_SERIAL\_DDK\_SERVICE\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK service communication fails.

 |

#### \[h2\]OH\_UsbSerial\_Open()

int32\_t OH\_UsbSerial\_Open(uint64\_t deviceId, uint8\_t interfaceIndex, UsbSerial\_Device \*\*dev)

**Description**

Opens the USB serial port device based on the specified **deviceId** and **interfaceIndex**.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB\_SERIAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| uint64\_t deviceId | Device ID. |
| uint8\_t interfaceIndex | Interface index, which corresponds to [bInterfaceNumber](../../structs/usbinterfacedescriptor/document.md) in the USB protocol. |
| [UsbSerial\_Device](../../structs/usbserial-device/document.md) \*\*dev | Device handle. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_SERIAL\_DDK\_SUCCESS](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is successful.

[USB\_SERIAL\_DDK\_NO\_PERM](../usb-serial-types-h/document.md#usbserial_ddkretcode): The permission verification fails.

[USB\_SERIAL\_DDK\_INVALID\_PARAMETER](../usb-serial-types-h/document.md#usbserial_ddkretcode): The parameter verification fails. The possible cause is that **dev** or \***dev** is null.

[USB\_SERIAL\_DDK\_INIT\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK initialization fails.

[USB\_SERIAL\_DDK\_SERVICE\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK service communication fails.

[USB\_SERIAL\_DDK\_MEMORY\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The memory is insufficient.

[USB\_SERIAL\_DDK\_IO\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): An I/O exception occurs.

[USB\_SERIAL\_DDK\_DEVICE\_NOT\_FOUND](../usb-serial-types-h/document.md#usbserial_ddkretcode): The device or interface is not found.

 |

#### \[h2\]OH\_UsbSerial\_Close()

int32\_t OH\_UsbSerial\_Close(UsbSerial\_Device \*\*dev)

**Description**

Closes the USB serial port device.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB\_SERIAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [UsbSerial\_Device](../../structs/usbserial-device/document.md) \*\*dev | Device handle. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_SERIAL\_DDK\_SUCCESS](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is successful.

[USB\_SERIAL\_DDK\_NO\_PERM](../usb-serial-types-h/document.md#usbserial_ddkretcode): The permission verification fails.

[USB\_SERIAL\_DDK\_INVALID\_PARAMETER](../usb-serial-types-h/document.md#usbserial_ddkretcode): The parameter verification fails. The possible cause is that **dev** or \***dev** is null.

[USB\_SERIAL\_DDK\_INIT\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK initialization fails.

[USB\_SERIAL\_DDK\_SERVICE\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK service communication fails.

[USB\_SERIAL\_DDK\_IO\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): An I/O exception occurs.

[USB\_SERIAL\_DDK\_INVALID\_OPERATION](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is invalid.

 |

#### \[h2\]OH\_UsbSerial\_Read()

int32\_t OH\_UsbSerial\_Read(UsbSerial\_Device \*dev, uint8\_t \*buff, uint32\_t bufferSize, uint32\_t \*bytesRead)

**Description**

Reads data from the USB serial port device to the buffer.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB\_SERIAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [UsbSerial\_Device](../../structs/usbserial-device/document.md) \*dev | Device handle. |
| uint8\_t \*buff | Buffer for storing the data read from the USB serial port device. |
| uint32\_t bufferSize | Buffer size. |
| uint32\_t \*bytesRead | 
Number of bytes that are actually read. If the block mode is set, the number of bytes that are actually read is returned only when it is equal to the value of **bufferSize**.

For details, see [OH\_UsbSerial\_SetTimeout](#oh_usbserial_settimeout).

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_SERIAL\_DDK\_SUCCESS](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is successful.

[USB\_SERIAL\_DDK\_NO\_PERM](../usb-serial-types-h/document.md#usbserial_ddkretcode): The permission verification fails.

[USB\_SERIAL\_DDK\_INVALID\_PARAMETER](../usb-serial-types-h/document.md#usbserial_ddkretcode): The parameter verification fails. Possible causes: 1. **dev** is a null pointer.

2\. **buff** is a null pointer. 3. **bufferSize** is **0**. 4. **bytesRead** is a null pointer.

[USB\_SERIAL\_DDK\_INIT\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK initialization fails.

[USB\_SERIAL\_DDK\_SERVICE\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK service communication fails.

[USB\_SERIAL\_DDK\_MEMORY\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The buffer address is invalid.

[USB\_SERIAL\_DDK\_IO\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): An I/O exception occurs.

[USB\_SERIAL\_DDK\_INVALID\_OPERATION](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is invalid.

 |

#### \[h2\]OH\_UsbSerial\_Write()

int32\_t OH\_UsbSerial\_Write(UsbSerial\_Device \*dev, uint8\_t \*buff, uint32\_t bufferSize, uint32\_t \*bytesWritten)

**Description**

Writes the data in the buffer to the USB serial port device.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB\_SERIAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [UsbSerial\_Device](../../structs/usbserial-device/document.md) \*dev | Device handle. |
| uint8\_t \*buff | Buffer to which the data of the USB serial port device is written. |
| uint32\_t bufferSize | Buffer size. |
| uint32\_t \*bytesWritten | Number of bytes that are actually written. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_SERIAL\_DDK\_SUCCESS](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is successful.

[USB\_SERIAL\_DDK\_NO\_PERM](../usb-serial-types-h/document.md#usbserial_ddkretcode): The permission verification fails.

[USB\_SERIAL\_DDK\_INVALID\_PARAMETER](../usb-serial-types-h/document.md#usbserial_ddkretcode): The parameter verification fails. Possible causes: 1. **dev** is a null pointer.

2\. **buff** is a null pointer. 3. **bufferSize** is **0**. 4. **bytesWritten** is a null pointer.

[USB\_SERIAL\_DDK\_INIT\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK initialization fails.

[USB\_SERIAL\_DDK\_SERVICE\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK service communication fails.

[USB\_SERIAL\_DDK\_MEMORY\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The buffer address is invalid.

[USB\_SERIAL\_DDK\_IO\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): An I/O exception occurs.

[USB\_SERIAL\_DDK\_INVALID\_OPERATION](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is invalid.

 |

#### \[h2\]OH\_UsbSerial\_SetBaudRate()

int32\_t OH\_UsbSerial\_SetBaudRate(UsbSerial\_Device \*dev, uint32\_t baudRate)

**Description**

Sets the baud rate for a USB serial port device. If the parameters of the USB serial port device are set to the default values (the data bit is **8**, the stop bit is **1**, and parity is disabled for data transfer), you only need to call this API to set the baud rate.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB\_SERIAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [UsbSerial\_Device](../../structs/usbserial-device/document.md) \*dev | Device handle. |
| uint32\_t baudRate | Baud rate of the USB serial port device. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_SERIAL\_DDK\_SUCCESS](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is successful.

[USB\_SERIAL\_DDK\_NO\_PERM](../usb-serial-types-h/document.md#usbserial_ddkretcode): The permission verification fails.

[USB\_SERIAL\_DDK\_INVALID\_PARAMETER](../usb-serial-types-h/document.md#usbserial_ddkretcode): The parameter verification fails. Possible cause: The input **dev** is a null pointer.

[USB\_SERIAL\_DDK\_INIT\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK initialization fails.

[USB\_SERIAL\_DDK\_SERVICE\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK service communication fails.

[USB\_SERIAL\_DDK\_IO\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): An I/O exception occurs.

[USB\_SERIAL\_DDK\_INVALID\_OPERATION](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is invalid.

 |

#### \[h2\]OH\_UsbSerial\_SetParams()

int32\_t OH\_UsbSerial\_SetParams(UsbSerial\_Device \*dev, UsbSerial\_Params \*params)

**Description**

Sets the parameters of the USB serial port device. If the parameters of the USB serial port device are not set to the default values (the data bit is **8**, the stop bit is **1**, and parity is disabled for data transfer), you only need to call this API to set the related parameters.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB\_SERIAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [UsbSerial\_Device](../../structs/usbserial-device/document.md) \*dev | Device handle. |
| [UsbSerial\_Params](../../structs/usbserial-params/document.md) \*params | USB serial port device parameters. For details, see [UsbSerial\_Params](../../structs/usbserial-params/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_SERIAL\_DDK\_SUCCESS](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is successful.

[USB\_SERIAL\_DDK\_NO\_PERM](../usb-serial-types-h/document.md#usbserial_ddkretcode): The permission verification fails.

[USB\_SERIAL\_DDK\_INVALID\_PARAMETER](../usb-serial-types-h/document.md#usbserial_ddkretcode): The parameter verification fails. Possible causes: 1. **dev** is a null pointer.

2\. **params** is a null pointer.

[USB\_SERIAL\_DDK\_INIT\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK initialization fails.

[USB\_SERIAL\_DDK\_SERVICE\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK service communication fails.

[USB\_SERIAL\_DDK\_IO\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): An I/O exception occurs.

[USB\_SERIAL\_DDK\_INVALID\_OPERATION](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is invalid.

 |

#### \[h2\]OH\_UsbSerial\_SetTimeout()

int32\_t OH\_UsbSerial\_SetTimeout(UsbSerial\_Device \*dev, int timeout)

**Description**

Sets the timeout interval (ms) for reading data reported by a USB serial port device. If this function is not called, the timeout value is **0** by default, indicating that data is returned immediately regardless of whether data is read. If you need to wait for a certain period of time or data must be read, call this API to set the timeout interval.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB\_SERIAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [UsbSerial\_Device](../../structs/usbserial-device/document.md) \*dev | Device handle. |
| int timeout | Timeout interval for reading data from a USB serial port device, in milliseconds. The value range is - (0, 25500\]. The value is rounded off to the nearest 100 milliseconds as the actual timeout interval. For example, if the value is set to **12321**, the effective timeout interval is **12300**. - **0**: Data is returned immediately. - **\-1**: Data is read in block mode. That is, data is returned only after data of the specified length is read. For details, see [OH\_UsbSerial\_Read](#oh_usbserial_read). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_SERIAL\_DDK\_SUCCESS](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is successful.

[USB\_SERIAL\_DDK\_NO\_PERM](../usb-serial-types-h/document.md#usbserial_ddkretcode): The permission verification fails.

[USB\_SERIAL\_DDK\_INVALID\_PARAMETER](../usb-serial-types-h/document.md#usbserial_ddkretcode): The parameter verification fails. Possible causes: 1. **dev** is a null pointer.

2.timeout < -1 or timeout > 25500.

[USB\_SERIAL\_DDK\_INIT\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK initialization fails.

[USB\_SERIAL\_DDK\_SERVICE\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK service communication fails.

[USB\_SERIAL\_DDK\_IO\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): An I/O exception occurs.

[USB\_SERIAL\_DDK\_INVALID\_OPERATION](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is invalid.

 |

#### \[h2\]OH\_UsbSerial\_SetFlowControl()

int32\_t OH\_UsbSerial\_SetFlowControl(UsbSerial\_Device \*dev, UsbSerial\_FlowControl flowControl)

**Description**

Sets flow control parameters. Flow control is used to manage the data transfer rate during communication with the USB serial port device to ensure that the sender does not send data that exceeds the processing capability of the receiver.

If flow control is required, call this API to set flow control parameters. If this API is not called, flow control is not performed by default.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB\_SERIAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [UsbSerial\_Device](../../structs/usbserial-device/document.md) \*dev | Device handle. |
| [UsbSerial\_FlowControl](../usb-serial-types-h/document.md#usbserial_flowcontrol) flowControl | Flow control mode. For details, see [UsbSerial\_FlowControl](../usb-serial-types-h/document.md#usbserial_flowcontrol). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_SERIAL\_DDK\_SUCCESS](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is successful.

[USB\_SERIAL\_DDK\_NO\_PERM](../usb-serial-types-h/document.md#usbserial_ddkretcode): The permission verification fails.

[USB\_SERIAL\_DDK\_INVALID\_PARAMETER](../usb-serial-types-h/document.md#usbserial_ddkretcode): The parameter verification fails. Possible cause: The input **dev** is a null pointer.

[USB\_SERIAL\_DDK\_INIT\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK initialization fails.

[USB\_SERIAL\_DDK\_SERVICE\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK service communication fails.

[USB\_SERIAL\_DDK\_IO\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): An I/O exception occurs.

[USB\_SERIAL\_DDK\_INVALID\_OPERATION](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is invalid.

 |

#### \[h2\]OH\_UsbSerial\_Flush()

int32\_t OH\_UsbSerial\_Flush(UsbSerial\_Device \*dev)

**Description**

Flushes the input and output buffers after the write operation is complete. If a large amount of data is to be transmitted to the USB serial port device, the data may be buffered in the kernel for transmission. If the application closes the file descriptor or exits before the data is completely sent out, some data may be lost. You can call this API to ensure that all data is sent before subsequent operations are performed.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB\_SERIAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [UsbSerial\_Device](../../structs/usbserial-device/document.md) \*dev | Device handle. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_SERIAL\_DDK\_SUCCESS](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is successful.

[USB\_SERIAL\_DDK\_NO\_PERM](../usb-serial-types-h/document.md#usbserial_ddkretcode): The permission verification fails.

[USB\_SERIAL\_DDK\_INVALID\_PARAMETER](../usb-serial-types-h/document.md#usbserial_ddkretcode): The parameter verification fails. Possible cause: The input **dev** is a null pointer.

[USB\_SERIAL\_DDK\_INIT\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK initialization fails.

[USB\_SERIAL\_DDK\_SERVICE\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK service communication fails.

[USB\_SERIAL\_DDK\_IO\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): An I/O exception occurs.

[USB\_SERIAL\_DDK\_INVALID\_OPERATION](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is invalid.

 |

#### \[h2\]OH\_UsbSerial\_FlushInput()

int32\_t OH\_UsbSerial\_FlushInput(UsbSerial\_Device \*dev)

**Description**

Flushes the input buffer. The data in the buffer is cleared immediately. During the communication with the USB serial port device, especially in the debugging phase, disordered data packets or other exceptions may occur.

You can call this API to clear these exceptions to restore the communication.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB\_SERIAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [UsbSerial\_Device](../../structs/usbserial-device/document.md) \*dev | Device handle. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_SERIAL\_DDK\_SUCCESS](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is successful.

[USB\_SERIAL\_DDK\_NO\_PERM](../usb-serial-types-h/document.md#usbserial_ddkretcode): The permission verification fails.

[USB\_SERIAL\_DDK\_INVALID\_PARAMETER](../usb-serial-types-h/document.md#usbserial_ddkretcode): The parameter verification fails. Possible cause: The input **dev** is a null pointer.

[USB\_SERIAL\_DDK\_INIT\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK initialization fails.

[USB\_SERIAL\_DDK\_SERVICE\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK service communication fails.

[USB\_SERIAL\_DDK\_IO\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): An I/O exception occurs.

[USB\_SERIAL\_DDK\_INVALID\_OPERATION](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is invalid.

 |

#### \[h2\]OH\_UsbSerial\_FlushOutput()

int32\_t OH\_UsbSerial\_FlushOutput(UsbSerial\_Device \*dev)

**Description**

Flushes the output buffer. The data in the buffer is cleared immediately. During the communication with the USB serial port device, especially in the debugging phase, disordered data packets or other exceptions may occur.

You can call this API to clear these exceptions to restore the communication.

**Required permissions**: ohos.permission.ACCESS\_DDK\_USB\_SERIAL

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [UsbSerial\_Device](../../structs/usbserial-device/document.md) \*dev | Device handle. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[USB\_SERIAL\_DDK\_SUCCESS](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is successful.

[USB\_SERIAL\_DDK\_NO\_PERM](../usb-serial-types-h/document.md#usbserial_ddkretcode): The permission verification fails.

[USB\_SERIAL\_DDK\_INVALID\_PARAMETER](../usb-serial-types-h/document.md#usbserial_ddkretcode): The parameter verification fails. Possible cause: The input **dev** is a null pointer.

[USB\_SERIAL\_DDK\_INIT\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK initialization fails.

[USB\_SERIAL\_DDK\_SERVICE\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): The DDK service communication fails.

[USB\_SERIAL\_DDK\_IO\_ERROR](../usb-serial-types-h/document.md#usbserial_ddkretcode): An I/O exception occurs.

[USB\_SERIAL\_DDK\_INVALID\_OPERATION](../usb-serial-types-h/document.md#usbserial_ddkretcode): The operation is invalid.

 |
