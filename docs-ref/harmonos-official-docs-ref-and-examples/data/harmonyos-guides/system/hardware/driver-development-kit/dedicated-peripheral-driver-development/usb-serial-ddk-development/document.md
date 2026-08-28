# USB Serial DDK Development

#### Overview

Non-standard serial port devices, such as temperature and humidity meters and special identity card readers, are used in industrial scenarios and on some legacy devices. If the system does not have a driver that adapts to the devices, the devices cannot be used after being connected. The USB Serial Driver Development Kit (DDK) is a toolset that helps you develop USB serial drivers at the application layer based on the user mode. The USB Serial DDK provides a series of APIs for the host to access devices, including APIs for enabling and disabling devices on the host and read/write data through serial ports. With these APIs, third-party peripheral devices can seamlessly integrate with the HarmonyOS ecosystem.

## Basic Concepts

Before developing the USB Serial DDK, you must understand the following basic concepts:

-   **USB serial port**
    
    USB-to-Serial is an interface conversion technology that allows data communication with traditional serial ports (such as RS-232 and RS-485) over USB interfaces. This technology is usually implemented by using a dedicated hardware adapter or a specific built-in chip.
    
-   **AMS**
    
    The Ability Manager Service (AMS) is a system service used to coordinate the running relationships of abilities and schedule the lifecycle of abilities. You can use it to start and disable **DriverExtensionAbility** during driver development.
    
-   **BMS**
    
    The Bundle Manager Service (BMS) is responsible for application installation, uninstallation, and data management on HarmonyOS.
    
-   **DDK**
    
    A toolkit provided by HarmonyOS to develop drivers for non-standard USB serial port devices based on the peripheral framework.
    
-   **Non-standard peripherals**
    
    Non-standard peripherals (also called custom peripherals or dedicated peripherals) are peripherals that do not comply with general standards or are customized for specific application scenarios. This type of device usually requires special software support or special interfaces to implement communication with the host system.
    
-   **Standard peripherals**
    
    Standard peripherals refer to peripherals (such as USB keyboards and mouse devices) that comply with industry standards and specifications. Such devices typically have uniform interface protocols, physical dimensions, and electrical characteristics, so that they can be used interchangeably between different systems.
    

## Implementation Principles

A non-standard peripheral application obtains the USB serial port device ID by using the peripheral management service, and delivers the ID and the action to the USB serial port driver application through RPC. The USB serial port driver application can set the serial port attributes (such as the baud rate, data bit, and parity bit) and read the serial port data by calling the USB Serial DDK API. Then, the DDK API uses the HDI service to deliver instructions to the kernel driver, and the kernel driver uses instructions to communicate with the device.

**Figure 1** Principles of invoking the USB Serial DDK

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/KllQSk_oSz2gO6YZ_65f_Q/en-us_image_0000002537765108.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11346B4EEBADE461B500D875A6A0B4B62A99FCBE0F70C13D8AFBEC6514F36D42)

## Constraints

-   The open APIs of USB Serial DDK can be used to develop drivers of non-standard USB peripherals that use USB serial ports.
    
-   The open APIs of USB Serial DDK can be used only within the **DriverExtensionAbility** lifecycle.
    
-   To use the open APIs of USB Serial DDK, you need to declare the matching ACL permissions in **module.json5**, for example, **ohos.permission.ACCESS\_DDK\_USB\_SERIAL**.
    

#### Environment Setup

Before you get started, make necessary preparations by following instructions in [Environment Preparation](../../setting-up-the-environment/document.md).

#### How to Develop

## Available APIs

| Name | Description |
| :-- | :-- |
| OH\_UsbSerial\_Init(void) | Initializes the USB Serial DDK. |
| OH\_UsbSerial\_Release(void) | Releases the USB Serial DDK. |
| OH\_UsbSerial\_Open(uint64\_t deviceId, uint8\_t interfaceIndex, UsbSerial\_Device \*\*dev) | Opens the USB serial port device based on the specified **deviceId** and **interfaceIndex**. Call **OH\_UsbSerial\_Close ()** to close the device after use. Otherwise, memory leakage occurs. |
| OH\_UsbSerial\_Close(UsbSerial\_Device \*\*dev) | Closes the USB serial port device after use. Otherwise, memory leakage occurs. |
| OH\_UsbSerial\_Read(UsbSerial\_Device \*dev, uint8\_t \*buff, uint32\_t bufferSize, uint32\_t \*bytesRead) | Reads data from the USB serial port device to the buffer. |
| OH\_UsbSerial\_Write(UsbSerial\_Device \*dev, uint8\_t \*buff, uint32\_t bufferSize, uint32\_t \*bytesWritten) | Writes the data in the buffer to the USB serial port device. |
| OH\_UsbSerial\_SetBaudRate(UsbSerial\_DeviceHandle \*dev, uint32\_t baudRate) | Sets the baud rate for a USB serial port device. Call this API if the data bit of the serial port is **8**, the stop bit is **1**, and parity check is not performed. |
| OH\_UsbSerial\_SetParams(UsbSerial\_Device \*dev, UsbSerial\_Params \*params) | Sets the parameters of the USB serial port device, including the baud rate, data transfer bit, stop bit, and parity check. |
| OH\_UsbSerial\_SetTimeout(UsbSerial\_Device \*dev, int timeout) | Sets the timeout interval for reading data reported by a USB serial port device. The default value is **0**. |
| OH\_UsbSerial\_SetFlowControl(UsbSerial\_Device \*dev, UsbSerial\_FlowControl flowControl) | Sets flow control parameters. |
| OH\_UsbSerial\_Flush(UsbSerial\_Device \*dev) | Flushes the input and output buffers after the write operation is complete. |
| OH\_UsbSerial\_FlushInput(UsbSerial\_Device \*dev) | Refreshes the input buffer. The data in the buffer is cleared immediately. |
| OH\_UsbSerial\_FlushOutput(UsbSerial\_Device \*dev) | Refreshes the output buffer. The data in the buffer is cleared immediately. |

For details about the APIs, see [USB Serial DDK](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-serialddk).

## How to Develop

To develop the USB serial port driver by using the USB Serial DDK, perform the following steps:

**Adding Dynamic Link Libraries**

Add the following libraries to **CMakeLists.txt**.

libusb\_serial\_ndk.z.so

**Including Header Files**

#include <usb\_serial/usb\_serial\_api.h>
#include <usb\_serial/usb\_serial\_types.h>

1.  Initialize the USB Serial DDK.
    
    Use **OH\_UsbSerial\_Init** in **usb\_serial\_api.h** to initialize the USB Serial DDK.
    
    // Initialize the USB Serial DDK.
    OH\_UsbSerial\_Init();
    
2.  Open the USB serial port device.
    
    Use **OH\_UsbSerial\_Open** in **usb\_serial\_api.h** to enable the device.
    
    UsbSerial\_Device \*dev = NULL;
    uint64\_t deviceId = 1;
    uint8\_t interfaceIndex = 0;
    // Open the USB serial port device specified by deviceId and interfaceIndex.
    OH\_UsbSerial\_Open(deviceId, interfaceIndex, &dev);
    
3.  (Optional) Set the parameters of the USB serial port device.
    
    Use **OH\_UsbSerial\_SetParams** in **usb\_serial\_api.h** to set the serial port parameters, or directly use **OH\_UsbSerial\_SetBaudRate** to set the baud rate, and use **OH\_UsbSerial\_SetTimeout** to set the timeout interval for reading data.
    
    UsbSerial\_Params params;
    params.baudRate = NUM\_BAUDRATE;
    params.nDataBits = NUM\_EIGHT;
    params.nStopBits = 1;
    params.parity = 0;
    // Set serial port parameters.
    OH\_UsbSerial\_SetParams(dev, &params);
        
    // Set the baud rate.
    uint32\_t baudRate = NUM\_BAUDRATE;
    OH\_UsbSerial\_SetBaudRate(dev, baudRate);
        
    // Set the timeout interval.
    int timeout = 500;
    OH\_UsbSerial\_SetTimeout(dev, timeout);
    
4.  (Optional) Set the flow control mode, and flush the buffer.
    
    Use **OH\_UsbSerial\_SetFlowControl** in **usb\_serial\_api.h** to set the flow control mode, use **OH\_UsbSerial\_Flush** to flush the buffer, use **OH\_UsbSerial\_FlushInput** to flush the input buffer, and use **OH\_UsbSerial\_FlushOutput** to flush the output buffer.
    
    // Set flow control.
    OH\_UsbSerial\_SetFlowControl(dev, USB\_SERIAL\_SOFTWARE\_FLOW\_CONTROL);
        
    // Flush the buffer.
    OH\_UsbSerial\_Flush(dev);
        
    // Flush the input buffer.
    OH\_UsbSerial\_FlushInput(dev);
        
    // Flush the output buffer.
    OH\_UsbSerial\_FlushOutput(dev);
    
5.  (Optional) Write data to or read data from a USB serial port device.
    
    Use **OH\_UsbSerial\_Write** in **usb\_serial\_api.h** to send data to the device, and use **OH\_UsbSerial\_Read** to read the data sent by the device.
    
    uint32\_t bytesWritten = 0;
    // Command used by the test device to read data. The command varies depending on the device protocol.
    uint8\_t writeBuff\[NUM\_EIGHT\] = {0x01, 0x03, 0x00, 0x00, 0x00, 0x01, 0x84, 0xA};
    // Send data over the connection.
    OH\_UsbSerial\_Write(dev, writeBuff, sizeof(writeBuff), &bytesWritten);
        
    // Callback invoked to receive data.
    uint8\_t readBuff\[100\];
    uint32\_t bytesRead = 0;
    OH\_UsbSerial\_Read(dev, readBuff, sizeof(readBuff), &bytesRead);
    
6.  Close the USB serial port device.
    
    After all requests are processed and before the program exits, use **OH\_UsbSerial\_Close** in **usb\_serial\_api.h** to close the device.
    
    // Close the device.
    OH\_UsbSerial\_Close(&dev);
    
7.  Release the USB Serial DDK.
    
    After the USB serial port device is closed, use **OH\_UsbSerial\_Release** in **usb\_serial\_api.h** to release the USB Serial DDK.
    
    // Release the USB Serial DDK.
    OH\_UsbSerial\_Release();
    

## Debugging and Verification

Upon completion of driver application development, you can install the application on the HarmonyOS device. The test procedure is as follows:

1.  Click the driver application on the device. The application is started on the device.
2.  Click the set button to set serial port attributes such as the baud rate.
3.  Click the data read button to read the data of the serial port device.
