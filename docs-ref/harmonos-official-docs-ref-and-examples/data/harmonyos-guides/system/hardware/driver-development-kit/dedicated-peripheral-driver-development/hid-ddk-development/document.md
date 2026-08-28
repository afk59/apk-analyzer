# HID DDK Development

#### Overview

Driver Development Kit (DDK) of Human Interface Device (HID) is a toolset that helps you develop HID drivers at the application layer based on the user mode. It provides APIs for accessing HID devices on a host, including creating a HID device, sending events to a device, destroying a device, opening or closing a device, reading and writing a report, and obtaining device information.

The HID DDK can be used to develop drivers for devices that use HID protocol to transfer data over a USB bus, or for devices that use peripheral drivers to create virtual devices to exchange information with non-standard devices.

## Basic Concepts

Before developing the HID DDK, you must understand the following basic concepts:

-   **HID**
    
    HID is a type of hardware device that implements interaction between a person and a computer or another electronic device. The primary function of HID is to convert user input (such as a key, a click, or a movement) into a data signal, and send the signal to a host device (such as a computer, tablet, or game console), so that the user can control and operate the device.
    
-   **DDK**
    
    A toolkit provided by HarmonyOS for developing drivers for non-standard USB serial port devices based on the peripheral framework.
    

## Implementation Principles

A non-standard peripheral application obtains the HID device ID by using the peripheral management service, and delivers the ID and the action to the HID device driver application through RPC. The driver application calls the HID DDK API to create and destroy a HID device, send events to a HID device, or obtain and parse packets sent from a HID device. The DDK API uses the HDI service to deliver instructions to the kernel driver, and the kernel driver uses instructions to communicate with the device.

**Figure 1** Principles of invoking the HID DDK

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/0m1jMGtdSAyFZk1q5RyY_A/en-us_image_0000002537765108.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2139CD3627A85159E7710B91B0DC62059E65CE9F44C8DB3C2EDBAC91E027F42F)

#### Constraints

-   The APIs provided by the HID DDK can be used to develop drivers of non-standard HID devices.
    
-   The open APIs of HID DDK can be used only within the lifecycle of **DriverExtensionAbility**.
    
-   Before using the open APIs of the HID DDK, you must declare the matching ACL permissions in **module.json5**, for example, **ohos.permission.ACCESS\_DDK\_HID**.
    

#### Available APIs

| Name | Description |
| :-- | :-- |
| OH\_Hid\_CreateDevice(Hid\_Device \*hidDevice, Hid\_EventProperties \*hidEventProperties) | Creates a HID device. When the device is no longer required, call **OH\_Hid\_DestroyDevice** to destroy it. |
| OH\_Hid\_EmitEvent(int32\_t deviceId, const Hid\_EmitItem items\[\], uint16\_t length) | Sends an event to a HID device. |
| OH\_Hid\_DestroyDevice(int32\_t deviceId) | Destroys a HID device. |
| int32\_t OH\_Hid\_Init(void) | Initializes the HID DDK. |
| int32\_t OH\_Hid\_Release(void) | Releases the HID DDK. |
| int32\_t OH\_Hid\_Open(uint64\_t deviceId, uint8\_t interfaceIndex, Hid\_DeviceHandle \*\*dev) | Opens the device specified by **deviceId** and **interfaceIndex**. |
| int32\_t OH\_Hid\_Close(Hid\_DeviceHandle \*\*dev) | Closes a HID device. |
| int32\_t OH\_Hid\_Write(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t length, uint32\_t \*bytesWritten) | Writes a report to a HID device. |
| int32\_t OH\_Hid\_ReadTimeout(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t buffSize, int timeout, uint32\_t \*bytesRead) | Reads a report from a HID device within the specified time. |
| int32\_t OH\_Hid\_Read(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t buffSize, uint32\_t \*bytesRead) | Reads a report from a HID device in the specified mode. The blocking mode (that is, blocking remains active until data can be read) is used by default. You can call **OH\_Hid\_SetNonBlocking** to change the mode. |
| int32\_t OH\_Hid\_SetNonBlocking(Hid\_DeviceHandle \*dev, int nonblock) | Sets the device read mode to non-blocking mode. |
| int32\_t OH\_Hid\_GetRawInfo(Hid\_DeviceHandle \*dev, Hid\_RawDevInfo \*rawDevInfo) | Obtains the raw information of a HID device. |
| int32\_t OH\_Hid\_GetRawName(Hid\_DeviceHandle \*dev, char \*data, uint32\_t buffSize) | Obtains the raw name of a HID device. |
| int32\_t OH\_Hid\_GetPhysicalAddress(Hid\_DeviceHandle \*dev, char \*data, uint32\_t buffSize) | Obtains the physical address of a HID device. |
| int32\_t OH\_Hid\_GetRawUniqueId(Hid\_DeviceHandle \*dev, uint8\_t \*data, uint32\_t buffSize) | Obtains the raw unique identifier of a HID device. |
| int32\_t OH\_Hid\_SendReport(Hid\_DeviceHandle \*dev, Hid\_ReportType reportType, const uint8\_t \*data, uint32\_t length) | Sends a report to a HID device. |
| int32\_t OH\_Hid\_GetReport(Hid\_DeviceHandle \*dev, Hid\_ReportType reportType, uint8\_t \*data, uint32\_t buffSize) | Obtains a report from a HID device. |
| int32\_t OH\_Hid\_GetReportDescriptor(Hid\_DeviceHandle \*dev, uint8\_t \*buf, uint32\_t buffSize, uint32\_t \*bytesRead) | Obtains the report descriptor of a HID device. |

For details about the APIs, see [HID DDK](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-hidddk).

#### How to Develop

## Developing a Basic HID Driver

The following steps you through on how to develop a HID device driver using the HID DDK.

**Adding Dynamic Link Libraries**

Add the following libraries to **CMakeLists.txt**.

libhid.z.so

**Including Header Files**

#include <hid/hid\_ddk\_api.h>
#include <hid/hid\_ddk\_types.h>

1.  Create a HID device.
    
    Use **OH\_Hid\_CreateDevice** of **hid\_ddk\_api.h** to create a HID device. If the operation is successful, a device ID is returned. If the operation fails, an [error code](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-hid-ddk-types-h#hid_ddkerrcode) is returned.
    

    Hid\_Device hidDevice = {
        .deviceName = deviceName.c\_str(),
        .vendorId = 0x6006,
        .productId = 0x6008,
        .version = 1,
        .bustype = BUS\_USB
    };
    std::vector<Hid\_EventType> eventType = {HID\_EV\_KEY};
    Hid\_EventTypeArray eventTypeArray = {.hidEventType = eventType.data(), .length = (uint16\_t)eventType.size()};
    std::vector<Hid\_KeyCode> keyCode = {
        HID\_KEY\_1,          HID\_KEY\_SPACE,       HID\_KEY\_BACKSPACE,   HID\_KEY\_ENTER,     HID\_KEY\_ESC, HID\_KEY\_SYSRQ,
        HID\_KEY\_LEFT\_SHIFT, HID\_KEY\_RIGHT\_SHIFT, HID\_KEY\_VOLUME\_DOWN, HID\_KEY\_VOLUME\_UP, HID\_KEY\_0,   HID\_KEY\_2,
        HID\_KEY\_3,          HID\_KEY\_4,           HID\_KEY\_5,           HID\_KEY\_6,         HID\_KEY\_7,   HID\_KEY\_8,
        HID\_KEY\_9,          HID\_KEY\_A,           HID\_KEY\_B,           HID\_KEY\_C,         HID\_KEY\_D,   HID\_KEY\_E,
        HID\_KEY\_F,          HID\_KEY\_G,           HID\_KEY\_H,           HID\_KEY\_I,         HID\_KEY\_J,   HID\_KEY\_K,
        HID\_KEY\_L,          HID\_KEY\_M,           HID\_KEY\_N,           HID\_KEY\_O,         HID\_KEY\_P,   HID\_KEY\_Q,
        HID\_KEY\_R,          HID\_KEY\_S,           HID\_KEY\_T,           HID\_KEY\_U,         HID\_KEY\_V,   HID\_KEY\_W,
        HID\_KEY\_X,          HID\_KEY\_Y,           HID\_KEY\_Z,           HID\_KEY\_DELETE};
    Hid\_KeyCodeArray keyCodeArray = {.hidKeyCode = keyCode.data(), .length = (uint16\_t)keyCode.size()};
    Hid\_EventProperties hidEventProp = {.hidEventTypes = eventTypeArray, .hidKeys = keyCodeArray};
    int deviceId = OH\_Hid\_CreateDevice(&hidDevice, &hidEventProp);

1.  Send an event to the HID device.
    
    Call **OH\_Hid\_EmitEvent** in **hid\_ddk\_api.h** to send an event to the device with the specified **deviceId**.
    

            // Send an event to the device identified by the specified deviceId. The event is injected by the physical peripheral through InjectEvent.
            int32\_t ret = OH\_Hid\_EmitEvent(item.first, item.second.data(), (uint16\_t)item.second.size());
            if (ret != HID\_DDK\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_EmitEvent failed, deviceId:%{public}d", item.first);
            }

1.  Release resources.
    
    Call **OH\_Hid\_DestroyDevice** in **hid\_ddk\_api.h** to destroy the device after all requests are processed and before the application exits.
    

    // Destroy a HID device.
    int32\_t res = OH\_Hid\_DestroyDevice(deviceId);

## Developing a HID Packet Communication Driver

The following steps you through on how to develop a HID packet communication driver using the HID DDK.

**Adding Dynamic Link Libraries**

Add the following libraries to **CMakeLists.txt**.

libhid.z.so

**Including Header Files**

#include <hid/hid\_ddk\_api.h>
#include <hid/hid\_ddk\_types.h>

1.  Initialize the HID DDK.
    
    Call **OH\_Hid\_Init** in **hid\_ddk\_api.h** to initialize the HID DDK.
    

    // Initialize the HID DDK.
    int32\_t ret = OH\_Hid\_Init();
    if (ret != HID\_DDK\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_Init() return failed: %{public}d", ret);
        return ret;
    }

1.  Open the device.
    
    Call **OH\_Hid\_Open** in **hid\_ddk\_api.h** to open a HID device.
    

    uint32\_t bInterfaceNum1 = 0x00;
    // Open the HID device specified by deviceId and interfaceIndex1. Generally, it is a /dev/hidraw0 file.
    ret = OH\_Hid\_Open(deviceID\_, bInterfaceNum1, &hid\_);
    if (ret != 0) {
        OH\_LOG\_ERROR(LOG\_APP, "Failed to open hid device, interface number:%{public}u ret:%{public}d",
            bInterfaceNum1, ret);
        return ret;
    }
    uint32\_t bInterfaceNum2 = 0x01;
    // Open the HID device specified by deviceId and interfaceIndex2. Generally, it is a /dev/hidraw1 file.
    ret = OH\_Hid\_Open(deviceID\_, bInterfaceNum2, &hid2\_);
    if (ret != 0) {
        OH\_LOG\_ERROR(LOG\_APP, "Failed to open hid device, interface number:%{public}u ret:%{public}d",
            bInterfaceNum2, ret);
        return ret;
    }

1.  (Optional) Write or send reports from the host to the HID device as data packets.
    -   If the report type is **HID\_OUTPUT\_REPORT** (output report), you can write/send the report in any of the following ways:
        
        -   Call **OH\_Hid\_Write** in **hid\_ddk\_api.h** to write an output report to the HID device.
            
        
            uint32\_t bytesWritten;
            // Write a report.
            int32\_t ret = OH\_Hid\_Write(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff), &bytesWritten);
            if (ret != HID\_DDK\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_Write failed. ret: %{public}u", ret);
            }
        
        -   Call **OH\_Hid\_SendReport** in **hid\_ddk\_api.h** to send an output report to the HID device.
            
        
            // Send an output report.
            int32\_t ret = OH\_Hid\_SendReport(DataParser::GetInstance().getHidObject(), HID\_OUTPUT\_REPORT, dataBuff,
                                            sizeof(dataBuff));
            if (ret != HID\_DDK\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_SendReport failed. ret: %{public}u", ret);
            }
        
    -   If the report type is **HID\_FEATURE\_REPORT** (feature report), call **OH\_Hid\_SendReport** in **hid\_ddk\_api.h** to send a feature report to the HID device.
        

    uint8\_t dataBuff\[NUM\_EIGHT\] = { 0x00 };
    string str(hexFormat);
    HexStringToUint8Array(str, dataBuff, sizeof(dataBuff));
    // Send a feature report.
    int32\_t ret = OH\_Hid\_SendReport(DataParser::GetInstance().getHid2Object(), HID\_FEATURE\_REPORT, dataBuff,
                                    sizeof(dataBuff));
    if (ret != HID\_DDK\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_SendReport failed. ret: %{public}u", ret);
    }

1.  (Optional) Read reports from the HID device.
    
    -   If the report type is **HID\_INPUT\_REPORT** (input report), you can read the report in any of the following ways:
        
        -   Use **OH\_Hid\_SetNonBlocking** in **hid\_ddk\_api.h** to set the read mode.
            
        
                // nonblock: 1 (enabled); 0 (disabled)
                ret = OH\_Hid\_SetNonBlocking(DataParser::GetInstance().getHidObject(), nonblockTag);
                if (ret != HID\_DDK\_SUCCESS) {
                    OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_SetNonBlocking failed. ret: %{public}u", ret);
                    return false;
                }
        
        -   Use **OH\_Hid\_Read** or **OH\_Hid\_ReadTimeout** in **hid\_ddk\_api.h** to read an input report from the HID device in non-blocking or blocking mode.
            
        
                if (nonblock) {
                    ret = OH\_Hid\_Read(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff), &bytesRead);
                } else {
                    ret = OH\_Hid\_ReadTimeout(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff),
                                             CONST\_TIMEOUT, &bytesRead);
                }
        
        -   Call **OH\_Hid\_GetReport** in **hid\_ddk\_api.h** to obtain an input report from the HID device.
            
        
            uint8\_t dataBuff\[NUM\_NINE\] = { 0x00 };
            // Obtain an input report.
            int32\_t ret = OH\_Hid\_GetReport(DataParser::GetInstance().getHidObject(), HID\_INPUT\_REPORT, dataBuff,
                                           sizeof(dataBuff));
            if (ret != HID\_DDK\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_GetReport failed. ret: %{public}u", ret);
                return nullptr;
            }
        
    -   If the report type is **HID\_FEATURE\_REPORT** (feature report), call **OH\_Hid\_GetReport** in **hid\_ddk\_api.h** to obtain a feature report from a HID device.
        
            uint8\_t dataBuff\[NUM\_EIGHT\] = { 0x00 };
            // Specify the report ID.
            dataBuff\[0\] = 0x07;
            // Obtain a feature report.
            int32\_t ret = OH\_Hid\_GetReport(DataParser::GetInstance().getHid2Object(), HID\_FEATURE\_REPORT, dataBuff,
                                           sizeof(dataBuff));
            if (ret != HID\_DDK\_SUCCESS) {
                OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_GetReport failed. ret: %{public}u", ret);
                return nullptr;
            }
        
2.  (Optional) Obtain the raw device information, raw name, physical address, and raw unique identifier of a HID device.
    
    Call **OH\_Hid\_GetRawInfo** in **hid\_ddk\_api.h** to obtain the raw information about a HID device.
    
    Call **OH\_Hid\_GetRawName** to obtain the raw name of a HID device.
    
    Call **OH\_Hid\_GetPhysicalAddress** to obtain the physical address of a HID device.
    
    Call **OH\_Hid\_GetRawUniqueId** to obtain the raw unique identifier of a HID device. The obtained information can be referenced by applications, for example, displaying device information on the GUI.
    
        Hid\_RawDevInfo rawDevInfo;
        int32\_t ret = OH\_Hid\_GetRawInfo(DataParser::GetInstance().getHidObject(), &rawDevInfo);
        if (ret != HID\_DDK\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_GetRawInfo failed, ret:%{public}d", ret);
            return nullptr;
        }
    
        char dataBuff\[DATA\_BUFF\_SIZE\];
        int32\_t ret = OH\_Hid\_GetRawName(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff));
        if (ret != HID\_DDK\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_GetRawName failed, ret:%{public}d", ret);
            return nullptr;
        }
    
        char dataBuff\[DATA\_BUFF\_SIZE\];
        int32\_t ret = OH\_Hid\_GetPhysicalAddress(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff));
        if (ret != HID\_DDK\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_GetPhysicalAddress failed, ret:%{public}d", ret);
            return nullptr;
        }
    
        uint8\_t dataBuff\[NUM\_SIXTY\_FOUR\];
        int32\_t ret = OH\_Hid\_GetRawUniqueId(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff));
        if (ret != HID\_DDK\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_GetRawUniqueId failed, ret:%{public}d", ret);
            return nullptr;
        }
    
3.  (Optional) Obtain the report descriptor.
    
    Call **OH\_Hid\_GetReportDescriptor** in **hid\_ddk\_api.h** to obtain the HID device report descriptor.
    

    uint8\_t dataBuff\[DATA\_BUFF\_SIZE1\];
    uint32\_t bytesRead;
    int32\_t ret = OH\_Hid\_GetReportDescriptor(DataParser::GetInstance().getHidObject(), dataBuff, sizeof(dataBuff),
                                             &bytesRead);
    if (ret != HID\_DDK\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_GetReportDescriptor failed, ret:%{public}d", ret);
        return nullptr;
    }

1.  Close the HID device.
    
    Call **OH\_Hid\_Close** in **hid\_ddk\_api.h** to close the device.
    

    Hid\_DeviceHandle \*hid = DataParser::GetInstance().getHidObject();
    int32\_t ret1 = OH\_Hid\_Close(&hid);
    DataParser::GetInstance().UpdateHid(hid);

1.  Release the HID DDK.
    
    After the HID device is closed, call **OH\_Hid\_Release** in **hid\_ddk\_api.h** to release the HID DDK.
    

        ret1 = OH\_Hid\_Release();
        if (ret1 != HID\_DDK\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_Hid\_Init() return failed: %{public}d", ret1);
        }
