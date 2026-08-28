# SCSI Peripheral DDK Development

#### Overview

Small Computer System Interface (SCSI) devices, such as disk arrays, tape libraries, and specific types of storage servers, are widely used in enterprise-level storage solutions and industrial application scenarios. If the operating system does not have an adaptation driver for these devices, the devices cannot be identified or used after being connected. SCSI Peripheral Driver Development Kit (DDK) is a suite provided for SCSI device driver development. It allows you to develop SCSI device drivers at the application layer based on the user mode.

The SCSI Peripheral DDK supports seven common commands (including INQUIRY, READ CAPACITY, TEST UNIT READY, REQUEST SENSE, READ, WRITE, and VERIFY) in the three command sets: SCSI Primary Commands (SPC), SCSI Block Commands (SBC), and Multimedia Commands (MMC). You can use these commands at your preference.

## Basic Concepts

Before developing the SCSI Peripheral DDK, you must understand the following basic concepts:

-   **SCSI**
    
    SCSI is a standard protocol set used for communication between computers and peripherals such as hard disk drives, tape drives, optical disk drives, and scanners.
    
-   **AMS**
    
    The Ability Manager Service (AMS) is a system service used to coordinate the running relationships of abilities and schedule the lifecycle of abilities.
    
-   **BMS**
    
    The Bundle Manager Service (BMS) is responsible for application installation, uninstallation, and data management on HarmonyOS.
    
-   **DDK**
    
    The Driver Development Kit (DDK) is a tool package provided by HarmonyOS for developing drivers for non-standard SCSI peripherals based on the peripheral framework.
    
-   **Non-standard peripherals**
    
    Non-standard peripherals (also called custom peripherals or dedicated peripherals) are peripherals that do not comply with general standards or are customized for specific application scenarios. This type of device usually requires special software support or special interfaces to implement communication with the host system.
    
-   **Standard peripherals**
    
    Standard peripherals refer to peripherals (such as USB keyboards and mouse devices) that comply with industry standards and specifications. Such devices typically have uniform interface protocols, physical dimensions, and electrical characteristics, so that they can be used interchangeably between different systems.
    
-   **Logical block**
    
    A logical block is a basic data storage unit. It represents a data area of a fixed size on a device and is usually used for data read and write operations. The size of a logical block may be 512 bytes, 1024 bytes, 2048 bytes, and so on. A specific size depends on a configuration of the device and a design of the file system.
    
-   **CDB**
    
    A command descriptor block (CDB) is a standard data structure used to send commands in the SCSI protocol. A CDB is a byte array with a fixed length. It contains the operation code (Opcode) and related parameters of the SCSI command and is used to instruct the device to perform operations (such as read, write, and query).
    

## Implementation Principles

A non-standard peripheral application obtains the SCSI device ID by using the peripheral management service, and delivers the ID and the action to the SCSI driver application through RPC. The SCSI driver application can obtain the basic information about the SCSI device and read and write data by invoking the SCSI Peripheral DDK API. Then, the DDK API uses the HDI service to deliver instructions to the kernel driver, and the kernel driver uses instructions to communicate with the device.

**Figure 1** Principle of invoking the SCSI Peripheral DDK

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/ChlB_zYYRjujucxCxTCM1A/en-us_image_0000002537765108.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2868386AEB7C46314E022E99DA55B970B59946081ADA58643C340E8BEE4859ED)

## Constraints

-   The open APIs of SCSI Peripheral DDK support the development of standard SCSI peripheral drivers.
    
-   The open APIs of SCSI Peripheral DDK can be used only within the lifecycle of **DriverExtensionAbility**.
    
-   To use the open APIs of SCSI Peripheral DDK, you need to declare the corresponding ACL permission **ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL** in **module.json5**.
    

#### Environment Setup

Before you get started, make necessary preparations by following instructions in [Environment Preparation](../../setting-up-the-environment/document.md).

#### How to Develop

## Available APIs

| **Name** | Description |
| :-- | :-- |
| int32\_t OH\_ScsiPeripheral\_Init(void) | Initializes the SCSI Peripheral DDK. |
| int32\_t OH\_ScsiPeripheral\_Release(void) | Releases the SCSI Peripheral DDK. |
| int32\_t OH\_ScsiPeripheral\_Open(uint64\_t deviceId, uint8\_t interfaceIndex, ScsiPeripheral\_Device \*\*dev) | Opens the SCSI device specified by **deviceId** and **interfaceIndex**. |
| int32\_t OH\_ScsiPeripheral\_Close(ScsiPeripheral\_Device \*\*dev) | Disables the SCSI device. |
| int32\_t OH\_ScsiPeripheral\_TestUnitReady(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_TestUnitReadyRequest \*request, ScsiPeripheral\_Response \*response) | Checks whether the logical units are ready. |
| int32\_t OH\_ScsiPeripheral\_Inquiry(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_InquiryRequest \*request, ScsiPeripheral\_InquiryInfo \*inquiryInfo, ScsiPeripheral\_Response \*response) | Queries basic information about the SCSI device. |
| int32\_t OH\_ScsiPeripheral\_ReadCapacity10(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_ReadCapacityRequest \*request, ScsiPeripheral\_CapacityInfo \*capacityInfo, ScsiPeripheral\_Response \*response) | Obtains the capacity information about the SCSI device. |
| int32\_t OH\_ScsiPeripheral\_RequestSense(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_RequestSenseRequest \*request, ScsiPeripheral\_Response \*response) | Obtains sense data, that is, information returned by the SCSI device to the host, which is used to report the device status, error information, and diagnosis information. |
| int32\_t OH\_ScsiPeripheral\_Read10(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_IORequest \*request, ScsiPeripheral\_Response \*response) | Reads data from a specified logical block. |
| int32\_t OH\_ScsiPeripheral\_Write10(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_IORequest \*request, ScsiPeripheral\_Response \*response) | Writes data to a specified logical block of a device. |
| int32\_t OH\_ScsiPeripheral\_Verify10(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_VerifyRequest \*request, ScsiPeripheral\_Response \*response) | Verifies a specified logical block. |
| int32\_t OH\_ScsiPeripheral\_SendRequestByCdb(ScsiPeripheral\_Device \*dev, ScsiPeripheral\_Request \*request, ScsiPeripheral\_Response \*response) | Sends the SCSI command in CDB mode. |
| int32\_t OH\_ScsiPeripheral\_CreateDeviceMemMap(ScsiPeripheral\_Device \*dev, size\_t size, ScsiPeripheral\_DeviceMemMap \*\*devMmap) | Creates a buffer. |
| int32\_t OH\_ScsiPeripheral\_DestroyDeviceMemMap(ScsiPeripheral\_DeviceMemMap \*devMmap) | Destroys a buffer. |
| int32\_t OH\_ScsiPeripheral\_ParseBasicSenseInfo(uint8\_t \*senseData, uint8\_t senseDataLen, ScsiPeripheral\_BasicSenseInfo \*senseInfo) | Parses basic sense data, including the **Information**, **Command specific information**, and **Sense key specific** fields. |

For details about the interface, see [SCSI Peripheral DDK](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-scsiperipheralddk).

## How to Develop

The following describes how to use the SCSI Peripheral DDK to develop non-standard SCSI peripheral drivers.

**Adding Dynamic Link Libraries**

Add the following libraries to **CMakeLists.txt**.

libscsi.z.so

**Including Header Files**

#include <scsi\_peripheral/scsi\_peripheral\_api.h>
#include <scsi\_peripheral/scsi\_peripheral\_types.h>

1.  Initialize the SCSI Peripheral DDK.
    
    Use **OH\_ScsiPeripheral\_Init** in **scsi\_peripheral\_api.h** to initialize the SCSI Peripheral DDK.
    

    // Initialize the SCSI Peripheral DDK.
    int32\_t ret = OH\_ScsiPeripheral\_Init();

1.  Open the device.
    
    After the SCSI Peripheral DDK is initialized, use **OH\_ScsiPeripheral\_Open** in **scsi\_peripheral\_api.h** to open the SCSI device.
    

        ret = OH\_ScsiPeripheral\_Open(g\_devHandle, interfaceIndex, &g\_scsiPeripheralDevice);

1.  (Optional) Create a buffer.
    
    Use **OH\_ScsiPeripheral\_CreateDeviceMemMap** in **scsi\_peripheral\_api.h** to create the memory buffer **devMmap**.
    

        ret = OH\_ScsiPeripheral\_CreateDeviceMemMap(g\_scsiPeripheralDevice, DEVICE\_MEM\_MAP\_SIZE, &g\_scsiDeviceMemMap);

1.  (Optional) Check whether the logical unit is ready.
    
    Use **OH\_ScsiPeripheral\_TestUnitReady** in **scsi\_peripheral\_api.h** to check whether the logical unit is ready.
    

        int32\_t ret = OH\_ScsiPeripheral\_TestUnitReady(g\_scsiPeripheralDevice, &request, &response);

1.  (Optional) Query the basic information about the SCSI device.
    
    Use **OH\_ScsiPeripheral\_Inquiry** in **scsi\_peripheral\_api.h** to obtain the basic information about the SCSI device.
    

    int32\_t ret = OH\_ScsiPeripheral\_Inquiry(g\_scsiPeripheralDevice, &inquiryRequest, &inquiryInfo, &response);

1.  (Optional) Obtain the capacity information of the SCSI device.
    
    Use **OH\_ScsiPeripheral\_ReadCapacity10** in **scsi\_peripheral\_api.h** to obtain the SCSI device capacity information.
    

    ret = OH\_ScsiPeripheral\_ReadCapacity10(g\_scsiPeripheralDevice, &readCapacityRequest, &capacityInfo, &response);

1.  (Optional) Obtain sense data.
    
    Use **OH\_ScsiPeripheral\_RequestSense** in **scsi\_peripheral\_api.h** to obtain sense data.
    

    int32\_t ret = OH\_ScsiPeripheral\_RequestSense(g\_scsiPeripheralDevice, &senseRequest, &response);

1.  (Optional) Parse sense data.
    
    Use **OH\_ScsiPeripheral\_ParseBasicSenseInfo** in **scsi\_peripheral\_api.h** to parse basic sense data, including the **Information**, **Command specific information**, and **Sense key specific** fields.
    

        int32\_t ret = OH\_ScsiPeripheral\_ParseBasicSenseInfo(response.senseData, SCSIPERIPHERAL\_MAX\_SENSE\_DATA\_LEN,
            &senseInfo);

1.  (Optional) Read data.
    
    Use **OH\_ScsiPeripheral\_Read10** in **scsi\_peripheral\_api.h** to read data from a specified logical block.
    

    int32\_t ret = OH\_ScsiPeripheral\_Read10(g\_scsiPeripheralDevice, &request, &response);

1.  (Optional) Write data.
    
    Use **OH\_ScsiPeripheral\_Write10** in **scsi\_peripheral\_api.h** to write data to a specified logical block of the device.
    

        int32\_t ret = OH\_ScsiPeripheral\_Write10(g\_scsiPeripheralDevice, &request, &response);

1.  (Optional) Verify a specified logical block.
    
    Use **OH\_ScsiPeripheral\_Verify10** in **scsi\_peripheral\_api.h** to verify a specified logical block.
    

        int32\_t ret = OH\_ScsiPeripheral\_Verify10(g\_scsiPeripheralDevice, &request, &response);

1.  (Optional) Send SCSI commands in CDB mode.
    
    Use **OH\_SCSIPeripheral\_SendRequestByCdb** in **scsi\_peripheral\_api.h** to send SCSI commands.
    

    int32\_t ret = OH\_ScsiPeripheral\_SendRequestByCdb(g\_scsiPeripheralDevice, &request, &response);

1.  (Optional) Destroy the buffer.
    
    After all requests are processed and before the program exits, use **OH\_ScsiPeripheral\_DestroyDeviceMemMap** in **scsi\_peripheral\_api.h** to destroy the buffer.
    

            ret = OH\_ScsiPeripheral\_DestroyDeviceMemMap(g\_scsiDeviceMemMap);

1.  Close the HID device.
    
    After the buffer is destroyed, use **OH\_ScsiPeripheral\_Close** in **scsi\_peripheral\_api.h** to close the device.
    

            ret = OH\_ScsiPeripheral\_Close(&g\_scsiPeripheralDevice);

1.  Release the SCSI Peripheral DDK.
    
    After the SCSI device is closed, use **OH\_ScsiPeripheral\_Release** in **scsi\_peripheral\_api.h** to release the SCSI Peripheral DDK.
    

        ret = OH\_ScsiPeripheral\_Release();

## Debugging and Verification

Upon completion of driver application development, you can install the application on the HarmonyOS device. The test procedure is as follows:

1.  Click the driver application on the device. The application is started on the device.
2.  Check whether the application can read the basic information about the SCSI device.
3.  Select a SCSI command, enter parameters, and click the **Send** button.
4.  (Optional) Set the direction, CDB data, and CDB length, and click the **Send** button to run the corresponding SCSI command.
