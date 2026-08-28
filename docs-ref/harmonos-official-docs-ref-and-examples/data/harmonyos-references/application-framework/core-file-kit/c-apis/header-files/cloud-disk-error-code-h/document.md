# cloud\_disk\_error\_code.h

#### Overview

This file defines the error codes for the cloud disk management module.

**File to include**: <filemanagement/clouddiskmanager/cloud\_disk\_error\_code.h>

**Library**: libohclouddiskmanager.so

**System capability**: SystemCapability.FileManagement.CloudDiskManager

**Since**: 21

**Related module**: [CloudDisk](../../modules/clouddisk/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [CloudDisk\_ErrorCode](#clouddisk_errorcode) | CloudDisk\_ErrorCode | Enumerates the error codes of the cloud disk management module. |

#### Enum Description

#### \[h2\]CloudDisk\_ErrorCode

enum CloudDisk\_ErrorCode

**Description**

Enumerates the error codes of the cloud disk management module.

**Since**: 21

| Value | Description |
| :-- | :-- |
| CLOUD\_DISK\_OK = 0 | The API is called successfully. |
| CLOUD\_DISK\_PERMISSION\_DENIED = 201 | The permission verification fails. |
| CLOUD\_DISK\_NOT\_SUPPORTED = 801 | This feature is not supported on the device. |
| CLOUD\_DISK\_INVALID\_ARG = 34400001 | The input parameter is invalid. |
| CLOUD\_DISK\_SYNC\_FOLDER\_PATH\_UNAUTHORIZED = 34400002 | The sync root path is not authorized. |
| CLOUD\_DISK\_IPC\_FAILED = 34400003 | IPC connection fails. |
| CLOUD\_DISK\_SYNC\_FOLDER\_LIMIT\_EXCEEDED = 34400004 | The number of sync root paths exceeds the upper limit. |
| CLOUD\_DISK\_CONFLICT\_THIS\_APP = 34400005 | The sync root path conflicts with the existing sync root path of the application. |
| CLOUD\_DISK\_CONFLICT\_OTHER\_APP = 34400006 | The sync root path conflicts with the existing sync root path of another application. |
| CLOUD\_DISK\_REGISTER\_SYNC\_FOLDER\_FAILED = 34400007 | The sync root path fails to be registered. |
| CLOUD\_DISK\_SYNC\_FOLDER\_NOT\_REGISTERED = 34400008 | The sync root path is not registered. |
| CLOUD\_DISK\_UNREGISTER\_SYNC\_FOLDER\_FAILED = 34400009 | The sync root path fails to be unregistered. |
| CLOUD\_DISK\_SYNC\_FOLDER\_PATH\_NOT\_EXIST = 34400010 | The sync root path does not exist. |
| CLOUD\_DISK\_LISTENER\_NOT\_REGISTERED = 34400011 | The change listener is not registered. |
| CLOUD\_DISK\_LISTENER\_ALREADY\_REGISTERED = 34400012 | The change listener has been registered. |
| CLOUD\_DISK\_INVALID\_CHANGE\_SEQUENCE = 34400013 | The change sequence is invalid. You are advised to query all change sequences. |
| CLOUD\_DISK\_TRY\_AGAIN = 34400014 | Temporary failure (for example, due to high underlying I/O load or insufficient memory). Please try again. |
| CLOUD\_DISK\_NOT\_ALLOWED = 34400015 | This feature is not allowed on the current device. |
