# USB DDK Development

#### Overview

The USB Driver Development Kit (DDK) is a toolset that helps you develop USB device drivers at the application layer based on the user mode. It provides a series of device access APIs, for example, opening and closing USB interfaces, and performing non-isochronous transfer, isochronous transfer, control transfer, and interrupt transfer over USB pipes.

The USB DDK can be used to develop device drivers for all devices that use the USB protocol to transfer data over a USB bus. For the peripherals that are not supported by standard kernel drivers, you can use the peripheral driver application developed based on the USB DDK to implement unique device capabilities.

## Basic Concepts

Before developing the USB DDK, you must understand the following basic concepts:

-   **USB**
    
    Universal Serial Bus (USB) is a widely used interface technology that connects a computer to various external devices, such as a keyboard, mouse, printer, storage device, and smartphone. The USB is designed to provide a standardized, efficient, and easy-to-use connection mode that replaces the traditional serial and parallel interface communication.
    
-   **DDK**
    
    DDK is a tool package provided by HarmonyOS for developing drivers for non-standard USB serial port devices based on the peripheral framework.
    

## Implementation Principles

A non-standard peripheral application obtains the USB device ID by using the peripheral management service, and delivers the ID and the action to the USB driver application through RPC. The USB driver application can obtain or set the device descriptor and initiate a control transfer or interrupt transfer request by calling the USB DDK API. Then, the DDK API uses the HDI service to deliver instructions to the kernel driver, and the kernel driver uses instructions to communicate with the device.

**Figure 1** Principles of invoking the USB DDK

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/mukmCk14QeGIoSjZNORbgw/en-us_image_0000002537765108.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7EADB4E19938CC6D29E2FA84A86F47AB0DD7B75A9A478D56072B5F15FC5FCDE0)

#### Constraints

-   The open APIs of USB DDK can be used to develop drivers of non-standard USB peripherals.
    
-   The open APIs of USB DDK can be used only within the lifecycle of **DriverExtensionAbility**.
    
-   To use the open APIs of the USB DDK, you need to declare the matching ACL permissions in **module.json5**, for example, **ohos.permission.ACCESS\_DDK\_USB**.
    

#### Environment Setup

Before you get started, make necessary preparations by following instructions in [Environment Preparation](../../setting-up-the-environment/document.md).

#### How to Develop

## Available APIs

| Name | Description |
| :-- | :-- |
| OH\_Usb\_Init(void) | Initializes the USB DDK. |
| OH\_Usb\_Release(void) | Releases the USB DDK. |
| OH\_Usb\_GetDeviceDescriptor(uint64\_t deviceId, struct UsbDeviceDescriptor \*desc) | Obtains the device descriptor of a USB device. |
| OH\_Usb\_GetConfigDescriptor(uint64\_t deviceId, uint8\_t configIndex, struct UsbDdkConfigDescriptor \*\*const config) | Obtains a USB configuration descriptor. To avoid memory leakage, use **OH\_Usb\_FreeConfigDescriptor()** to release a descriptor after use. |
| OH\_Usb\_FreeConfigDescriptor(const struct UsbDdkConfigDescriptor \*const config) | Releases a configuration descriptor. To avoid memory leakage, release a descriptor in time after use. |
| OH\_Usb\_ClaimInterface(uint64\_t deviceId, uint8\_t interfaceIndex, uint64\_t \*interfaceHandle) | Declares a USB interface. |
| OH\_Usb\_SelectInterfaceSetting(uint64\_t interfaceHandle, uint8\_t settingIndex) | Activates the alternate setting of a USB interface. |
| OH\_Usb\_GetCurrentInterfaceSetting(uint64\_t interfaceHandle, uint8\_t \*settingIndex) | Obtains the alternate setting of a USB interface. |
| OH\_Usb\_SendControlReadRequest(uint64\_t interfaceHandle, const struct UsbControlRequestSetup \*setup, uint32\_t timeout, uint8\_t \*data, uint32\_t \*dataLen) | Sends a control read transfer request. This API returns the result synchronously. |
| OH\_Usb\_SendControlWriteRequest(uint64\_t interfaceHandle, const struct UsbControlRequestSetup \*setup, uint32\_t timeout, const uint8\_t \*data, uint32\_t dataLen) | Sends a control write transfer request. This API returns the result synchronously. |
| OH\_Usb\_ReleaseInterface(uint64\_t interfaceHandle) | Releases a USB interface. |
| OH\_Usb\_SendPipeRequest(const struct UsbRequestPipe \*pipe, UsbDeviceMemMap \*devMmap) | Sends a pipe request. This API returns the result synchronously. It applies to interrupt transfer and bulk transfer. |
| OH\_Usb\_CreateDeviceMemMap(uint64\_t deviceId, size\_t size, UsbDeviceMemMap \*\*devMmap) | Create a buffer. To avoid resource leakage, use **OH\_Usb\_DestroyDeviceMemMap()** to destroy a buffer after use. |
| OH\_Usb\_DestroyDeviceMemMap(UsbDeviceMemMap \*devMmap) | Destroy a buffer. To avoid resource leakage, destroy a buffer in time after use. |
| OH\_Usb\_GetDevices(struct Usb\_DeviceArray \*devices) | Obtains the USB device ID list. Ensure that the input pointer is valid and the number of devices does not exceed 128. To prevent resource leakage, release the member memory after usage. Besides, make sure that the obtained USB device ID has been filtered by **vid** in the driver configuration information. |

For details about the APIs, see [USB DDK](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-usbddk).

## How to Develop

To develop a USB driver using the USB DDK, perform the following steps:

**Adding Dynamic Link Libraries**

Add the following libraries to **CMakeLists.txt**.

libusb\_ndk.z.so

**Including Header Files**

#include <usb/usb\_ddk\_api.h>
#include <usb/usb\_ddk\_types.h>

1.  Obtain the device descriptor of a USB device.
    
    Call **OH\_Usb\_Init** of **usb\_ddk\_api.h** to initialize the USB DDK, and call **OH\_Usb\_GetDeviceDescriptor** to obtain the device descriptor.
    

    // Initialize the USB DDK.
    int32\_t ret = OH\_Usb\_Init();
    OH\_LOG\_INFO(LOG\_APP, "OH\_Usb\_Init ret=:%{public}d\\n", ret);
    // ···
    struct UsbDeviceDescriptor devDesc;
    // Obtain the device descriptor.
    ret = OH\_Usb\_GetDeviceDescriptor(g\_devHandle, &devDesc);

1.  Obtain a configuration descriptor, and declare the USB interface.
    
    Call **OH\_Usb\_GetConfigDescriptor** of **usb\_ddk\_api.h** to obtain the configuration descriptor **config**, and call **OH\_Usb\_ClaimInterface** to declare claiming of the USB interface.
    

    struct UsbDdkConfigDescriptor \*config = nullptr;
    // Obtain the configuration descriptor.
    auto ret = OH\_Usb\_GetConfigDescriptor(g\_devHandle, 1, &config);
    OH\_LOG\_INFO(LOG\_APP, "OH\_Usb\_GetConfigDescriptor ret = %{public}d", ret);
    if (ret != 0) {
        OH\_LOG\_ERROR(LOG\_APP, "get config desc failed:%{public}d", ret);
        return false;
    }
    // Obtain the handwriting tablet-related interface and endpoint from the configuration descriptor.
    auto \[res, interface, endpoint, maxPktSize\] = GetInterfaceAndEndpoint(config);
    OH\_LOG\_INFO(LOG\_APP, "OH\_Usb\_GetConfigDescriptor ret = %{public}d", res);
    if (!res) {
        OH\_LOG\_ERROR(LOG\_APP, "GetInterfaceAndEndpoint failed");
        return false;
    }
    // Release the configuration descriptor to prevent memory leakage.
    OH\_Usb\_FreeConfigDescriptor(config);
    g\_dataEp = endpoint;
    g\_maxPktSize = maxPktSize;
    g\_interface = interface;
    // Claim the interface. The kernel keyboard driver will be uninstalled.
    ret = OH\_Usb\_ClaimInterface(g\_devHandle, g\_interface, &g\_interfaceHandle);

1.  (Optional) Obtain the activated alternate setting of a USB interface.
    
    Call **OH\_Usb\_GetCurrentInterfaceSetting** of **usb\_ddk\_api.h** to obtain the alternate setting, and call **OH\_Usb\_SelectInterfaceSetting** to activate it.
    

    uint8\_t settingIndex = 0;
    // Obtain the alternate setting.
    int32\_t ret = OH\_Usb\_GetCurrentInterfaceSetting(g\_interfaceHandle, &settingIndex);
    if (ret != USB\_DDK\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_Usb\_GetCurrentInterfaceSetting failed, ret=%{public}d", ret);
    }

    // Activate the alternate setting.
    ret = OH\_Usb\_SelectInterfaceSetting(g\_interfaceHandle, settingIndex);
    if (ret != USB\_DDK\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_Usb\_SelectInterfaceSetting failed, ret=%{public}d", ret);
    }

1.  (Optional) Send control read requests and control write requests.
    
    Call **OH\_Usb\_SendControlReadRequest** of **usb\_ddk\_api.h** to send a control read request, or call **OH\_Usb\_SendControlWriteRequest** to send a control write request.
    
        uint8\_t strDesc\[100\] = {0};
        // Obtain the product's string descriptor.
        uint32\_t len = 100;
        struct UsbControlRequestSetup strDescSetup;
        strDescSetup.bmRequestType = 0x80;
        strDescSetup.bRequest = 0x06;
        strDescSetup.wValue = (0x03 << BIT\_EIGHT) | (iProduct); // desc Index
        strDescSetup.wIndex = 0x409;                    // language Id
        strDescSetup.wLength = len;
        auto ret = OH\_Usb\_SendControlReadRequest(g\_interfaceHandle, &strDescSetup, UINT32\_MAX, strDesc, &len);
    
        // Set the feature.
        uint32\_t timeout = 5000;
        struct UsbControlRequestSetup strDescSetup;
        strDescSetup.bmRequestType = 0x21;
        strDescSetup.bRequest = 0x09;
        strDescSetup.wValue = ((0x03 << BIT\_EIGHT) | 0x02); // desc Index
        strDescSetup.wIndex = 0x0;
        strDescSetup.wLength = 0x02;
        uint8\_t data\[128\] = {0x02, 0x02};
        uint32\_t dataLen = 2;
        int32\_t ret = OH\_Usb\_SendControlWriteRequest(g\_interfaceHandle, &strDescSetup, timeout, data, dataLen);
    
2.  (Optional) Create a buffer, and send a request.
    
    Call **OH\_Usb\_CreateDeviceMemMap** of **usb\_ddk\_api.h** to create the buffer **devMmap**, and call **OH\_Usb\_SendPipeRequest** to send a request.
    
        // Claim the interface. The kernel keyboard driver will be uninstalled.
        // Create a buffer for storing data.
        int32\_t ret = OH\_Usb\_CreateDeviceMemMap(g\_devHandle, bufferLen, &devMmap);
    
            struct UsbRequestPipe pipe;
            pipe.interfaceHandle = g\_interfaceHandle;
            pipe.endpoint = g\_dataEp;
            pipe.timeout = 4; // Interrupt transfer timeout interval, which must be the same as the bInterval value of the handwriting tablet.
            // Read the handwriting tablet data.
            // Read key values in interrupt transfer mode.
            ret = OH\_Usb\_SendPipeRequest(&pipe, devMmap);
    
3.  Release resources.
    
    After all requests are processed and before the application exits, call **OH\_Usb\_DestroyDeviceMemMap** of **usb\_ddk\_api.h** to destroy the buffer, call **OH\_Usb\_ReleaseInterface** to release the USB interface, , and call **OH\_Usb\_Release** to release the USB DDK.
    

    // Destroy the buffer.
    OH\_Usb\_DestroyDeviceMemMap(devMmap);
    // Release the USB interface.
    int32\_t ret = OH\_Usb\_ReleaseInterface(g\_interfaceHandle);
    if (ret != 0) {
        OH\_LOG\_ERROR(LOG\_APP, "ReleaseInterface failed %{public}d", ret);
    }
    // Release the USB DDK.
    OH\_Usb\_Release();

1.  (Optional) Obtain the USB device ID list.
    
    After the driver is started, call **OH\_Usb\_GetDevices** to obtain the device ID that matches the VID in the driver configuration for subsequent application development. (VID is the ID of the device vendor and is configured in the driver application to indicate the applicable devices. The queried device IDs need to be filtered by VID.)
    

    constexpr size\_t maxUsbDeviceNum = 128;
    struct Usb\_DeviceArray deviceArray;
    deviceArray.deviceIds = new uint64\_t\[maxUsbDeviceNum\];
    // Obtain the USB device list.
    int32\_t ret = OH\_Usb\_GetDevices(&deviceArray);
    if (ret != USB\_DDK\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_Usb\_GetDevices failed, ret=%{public}d", ret);
    }
