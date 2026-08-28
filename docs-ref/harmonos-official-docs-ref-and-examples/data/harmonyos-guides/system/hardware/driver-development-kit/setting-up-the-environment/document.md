# Setting Up the Environment

#### Development Tool and Configuration

DevEco Studio, as the driver development tool, allows you to develop, debug, and package drivers.

[Download and install](https://developer.huawei.com/consumer/en/download/) DevEco Studio and verify basic operations to ensure that it can function properly. For details, see [Creating and Running a Project](../../../../environment-setup/creating-a-project/creating-a-project/document.md) in [DevEco Studio User Guide](../../../../environment-setup/overview/document.md).

#### SDK Version Configuration

The ArkTs APIs for peripheral management are applicable only when the SDK is of API version 10 or later.

The following table lists the SDK versions required to develop dedicated peripheral drivers or enhanced peripheral drivers based on the DDK.

| NDK API | SDK Version |
| :-- | :-- |
| USB DDK | API version 10 or later |
| HID DDK | API version 11 or later |
| USB Serial DDK | API version 18 or later |
| SCSI Peripheral DDK | API version 18 or later |

#### Verifying the Environment

Check whether DevEco Studio is connected to the HarmonyOS device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/MhgGdft2TqGLmuW-uvCqLQ/en-us_image_0000002568764833.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6948EC1E781D8891E5DC8592F9964C56F02D9DCFEA8EAC98D48356BBFB49251)

#### HDC Configuration

HarmonyOS Device Connector (hdc) is a command-line tool for debugging. It can be used to interact with real devices or the Emulators on Windows, Linux, and macOS. For details about the configuration, see [hdc](../../../debugging-tools/performance-analysis-kit/command-line-tools/hdc/document.md).

**NOTE**

Configuration of the environment variable **hdc\_server\_port** and global environment variables is mandatory.

#### Development Device

-   Currently, PC is used as the device for development, debugging, and verification.
-   During peripheral client and driver development, you need to connect an external USB device for debugging. Currently, **only an external USB device is supported**.
-   The product ID and vendor ID of the USB device are required for defining drivers and implementing IPC.
