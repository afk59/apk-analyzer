# Supported Devices

The following table lists the device types supported by the Emulator in different operating systems.

| 
Operating System

 | 

Device Type

 | 

Product Type

 | 

Remarks

 |
| :-- | :-- | :-- | :-- |
| 

Windows (x86)

macOS (ARM)

 | 

Phone

 | 

Bar phone

 | 

The function of emulating phones on Windows (x86) or macOS (ARM) is only available in the Chinese mainland.

 |
| 

Bi-fold phone

 |
| 

Widescreen foldable phone

 |
| 

Tri-fold phone

 |
| 

Tablet

 | 

Tablet

 | 

The function of emulating tablets on Windows (x86) or macOS (ARM) is only available in the Chinese mainland.

 |
| 

2-in-1 device

 | 

2-in-1 device

 | 

Since DevEco Studio 5.0.13.200, the function of emulating 2-in-1 devices on Windows (x86) or macOS (ARM) is only available in the Chinese mainland.

 |
| 

2-in-1 foldable

 | 

Since DevEco Studio 6.0.0.456, the function of emulating 2-in-1 foldables on Windows (x86) or macOS (ARM) is only available in the Chinese mainland.

 |
| 

Wearable

 | 

Wearable

 | 

Since DevEco Studio 6.0.0.828, the function of emulating wearables on Windows (x86) or macOS (ARM) is only available in the Chinese mainland.

Since DevEco Studio 6.0.1.249, the function of emulating wearables on Windows (x86) or macOS (ARM) is available in all countries/regions.

 |
| 

TV

 | 

TV

 | 

Since DevEco Studio 5.1.1.840, the function of emulating TVs on Windows (x86) or macOS (ARM) is only available in the Chinese mainland.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/Eaft-ZtGRZq-2tdcl26vdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F3AF81D480195AD5C84C4FA7113C5EA91202311A3F5846EBB1B12098C5CE0B5)

When the x86 Emulator is used, the C++ project and third-party library need to compile .so files of the x86\_64 version. Add **x86\_64** to the value of **externalNativeOptions/abiFilters** in the project-level or module-level **build-profile.json5** file. For details about the compilation configuration, see [externalNativeOptions](../../../../building-an-app/configuring-your-build/configuring-for-c-builds/document.md#section0721057575).
