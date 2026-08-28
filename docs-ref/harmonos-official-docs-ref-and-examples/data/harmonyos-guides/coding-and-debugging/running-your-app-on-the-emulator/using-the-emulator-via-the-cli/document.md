# Using the Emulator via the CLI

In addition to using the Emulator in the device management module of DevEco Studio, you can also use it via the Emulator CLI on Windows and macOS.

#### Environment Setup

The Emulator CLI is in the **tools/emulator** directory of the DevEco Studio installation directory. You can run the command in either of the following ways:

-   Method 1: Go to the **emulator** directory in the CLI and run the command.
-   Method 2: Configure the environment variables and run the command in any directory.
    -   On Windows:
        
        Add the Emulator path **_{DevEco Studio installation directory}_/tools/emulator** to the system or user **PATH** variable. After the configuration is complete, open the CLI again for the environment variables to take effect.
        
    -   On macOS:
        
        Open the CLI and run the following command:
        
        export PATH={_DevEco Studio installation directory_}/tools/emulator:$PATH
        

#### Prerequisites

Before using the CLI, create an emulator using DevEco Studio and note down the emulator instance path and emulator image path. For details, see [Creating an Emulator](../managing-the-emulator/creating-an-emulator/document.md).

#### Emulator Commands

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/Ftbusq5TR-2MHZIqLXG0Mg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21E9FE9275AA22366583E044E591940F0E63850D172E078FC9DC08594E32CF13)

-   If the emulator name or path contains special characters or spaces, add quotation marks ("") to the name or path.
-   The following commands use the Windows environment as an example. If the commands are executed on macOS and environment variables are not configured, add **./** before **Emulator**, for example, **./Emulator -help**.

## Getting Help

\# Display all executable commands.
Emulator -help

## Starting the Emulator

Emulator -hvd {_Emulator name_} -path {_Emulator instance path_} -imageRoot {_Emulator image path_} -hdcport {_HDC port number_}

**Parameters**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

\-hvd

 | 

(Mandatory) Emulator name.

 |
| 

\-path

 | 

(Mandatory) Emulator instance path.

 |
| 

\-imageRoot

 | 

(Mandatory) Emulator image path.

 |
| 

\-hdcport

 | 

(Optional) HDC port number. The value ranges from 10000 to 16555. This parameter is supported since DevEco Studio 6.0.1 Beta1.

 |

**Example**

Emulator -hvd "my Emulator" -path D:\\Emulator -imageRoot D:\\Sdk

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/Zs8r0hrsSuG92Sk9LJIy-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EDA7CBB458FB14BD51F672C3CE834E80B7797FACB92E46D9C81E78AC9B5AE6D5)

If you are required to sign in to your developer account to use the Emulator in DevEco Studio, the Emulator of this version cannot be started using the CLI. In this case, start the Emulator in DevEco Studio.

## Stopping the Emulator

Emulator -stop {_Emulator name_}

**Example**

Emulator -stop "my Emulator"

## Collecting Emulator Logs

Once the emulator is up and running, logs can be collected.

\# The {_Path for storing the .zip log file_} must be suffixed with .zip.
Emulator -logZip {_Emulator name_} -logPath {_Path for storing the .zip log file_}

**Example**

Emulator -logZip "my Emulator" -logPath D:\\EmulatorLog\\20250730.zip

## Obtaining the Emulator Instance Information

Obtaining the emulator instance information is supported since DevEco Studio 6.0.0 Beta3.

Emulator -list -details

**Parameters**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

\-list

 | 

(Mandatory) List of local emulator instances to query.

 |
| 

\-details

 | 

(Optional) Detailed information about local emulator instances to query, including the emulator version, image path, and instance path. Supported since DevEco Studio 6.0.2 Beta1.

 |

**Common Returns**

| 
Returned Information

 | 

Description

 |
| :-- | :-- |
| 

name

 | 

Emulator name.

 |
| 

deviceType

 | 

Device type of the emulator.

 |
| 

deviceModel

 | 

Product model of the emulator.

 |
| 

productModel

 | 

Specific product model of the emulator.

 |
| 

vendorCountry

 | 

Country/Region code

 |
| 

uuid

 | 

Emulator UUID.

 |
| 

isCustomize

 | 

Whether the current emulator has a customized screen configuration.

 |
| 

configPath

 | 

Configuration directory for the emulator.

 |
| 

logPath

 | 

Log directory for the emulator.

 |
| 

sdkPath

 | 

Path to the SDK used by the emulator.

 |
| 

imageRoot

 | 

Emulator image download path.

 |
| 

imageSubPath

 | 

Subfolder path of the emulator image. The absolute image path is **imageRoot** + **imageSubPath**.

 |
| 

instancePath

 | 

Emulator instance path.

 |
| 

os.osVersion

 | 

Version number of the emulator image.

 |
| 

os.apiVersion

 | 

API version of the emulator image.

 |
| 

os.softwareVersion

 | 

Specific version number of the emulator image.

 |
| 

os.isPublic

 | 

Whether the emulator is a public version.

 |
| 

hw.cpu.arch

 | 

CPU architecture type of the emulator.

 |
| 

hw.cpu.ncore

 | 

Number of CPU cores of the emulator.

 |
| 

hw.lcd.density

 | 

Emulator DPI.

 |
| 

hw.lcd.phy.height/width

 | 

Physical dimensions of the corresponding device model for the emulator.

 |
| 

hw.lcd.number

 | 

Number of screen states for the corresponding device model (for example, a foldable device has folded and unfolded states).

 |
| 

hw.lcd.single.diagonalSize/height/width

 | 

Single-screen size and resolution of the emulator.

 |
| 

hw.lcd.double.diagonalSize/height/width

 | 

Dual-screen size and resolution of the emulator (for foldables).

 |
| 

hw.lcd.triple.diagonalSize/height/width

 | 

Triple-screen size and resolution of the emulator (for tri-fold phones).

 |
| 

hw.ramSize

 | 

RAM size of the emulator.

 |
| 

hw.dataPartitionSize

 | 

Storage space size of the emulator.

 |
| 

hw.hdc.port

 | 

HDC port number.

 |

## Obtaining the Emulator Version

Emulator -version
