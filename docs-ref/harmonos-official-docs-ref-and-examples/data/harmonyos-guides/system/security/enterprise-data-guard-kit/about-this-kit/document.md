# About This Kit

Enterprise Data Guard Kit provides capabilities for mobile device management ([MDM](../../../basic-functions/mdm-kit/document.md)) apps to identify \\key information asset (KIA) files and prevent their unauthorized outflow. By harnessing native sensitive data security management capabilities of HarmonyOS, it enables enterprises to construct a robust data leak prevention solution that ensures greater visibility, control, and traceability of data assets and implements the enterprise recovery key management function.

Currently, Enterprise Data Guard Kit provides two types of capabilities: hierarchical file management and enterprise recovery key management.

#### Use Case

-   Provides the file scanning and tiering function. Enterprise apps can capture scanned file content, parse and recognize the data, and assign a security tier to the file, building an enterprise-grade asset map.
-   Enterprise Data Guard Kit provides flexible control policy configurations, allowing enterprises to establish tiered control over files and manage permissions to send sensitive files to external recipients.
-   Enterprise Data Guard Kit prohibits unauthorized activities, such as sending sensitive files to external recipients, and applies watermark protection for opened files based on predefined policies and a list of sensitive files.
-   Enterprise Data Guard Kit provides the capability of managing enterprise recovery keys.

#### Restrictions

## Access Restriction

-   Hierarchical file management currently supports only file scanning and grading capabilities for users. The default scanning path range includes the following paths.

| 
File Path

 | 

Description

 |
| :-- | :-- |
| 

/data/service/el2/

 | 

For details about the mapping between file paths and physical (real) paths and the differences between encryption partitions, please refer to [Mappings Between Application Sandbox Paths and Physical Paths](../../../../application-framework/core-file-kit/application-files/application-sandbox/document.md#mappings-between-application-sandbox-paths-and-physical-paths) and [Obtaining and Modifying Encryption Levels](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/context-stage-model/document.md#obtaining-and-modifying-encryption-levels).

 |
| 

/data/app/el1/bundle/public/

 |
| 

/mnt/hmdfs/

 |
| 

/data/app/el1/

 |
| 

/data/app/el2/

 |
| 

/data/app/el3/

 |
| 

/data/app/el4/

 |
| 

/data/app/el5/

 |

-   The functions of [obtaining the file URI](../hierarchical-file-management/obtaining-the-uri-of-a-file/document.md), [deleting files in a specified directory](../hierarchical-file-management/deleting-files-in-a-specified-directory/document.md), and [opening a file](../hierarchical-file-management/opening-a-file/document.md) in write-only mode are available only to the following paths.

| 
File Path

 | 

Description

 |
| :-- | :-- |
| 

/data/service/el2/<userId>/hmdfs/account/files/

 | 

Personal data directory of a specific user.

 |

## Supported Countries/Regions

Currently, this kit is available only in the Chinese mainland.

## Supported Devices

Currently, only PCs/2-in-1 devices are supported. The following table lists the details. Running or debugging using the Emulator is not supported.

| 
Device Type

 | 

Device Model

 |
| :-- | :-- |
| 

PC/2-in-1 device

 | 

Qingyun series

 |
