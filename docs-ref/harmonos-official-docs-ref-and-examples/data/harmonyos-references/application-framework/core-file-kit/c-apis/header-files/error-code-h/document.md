# error\_code.h

#### Overview

Defines the error codes for the **FileIO** module.

**File to include**: <filemanagement/fileio/error\_code.h>

**Library**: NA

**System capability**: SystemCapability.FileManagement.File.FileIO

**Since**: 12

**Related module**: [FileIO](../../modules/fileio/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [FileManagement\_ErrCode](#filemanagement_errcode) | FileManagement\_ErrCode | Enumerates the error codes used in the **FileIO** module. |

#### Enum Description

#### \[h2\]FileManagement\_ErrCode

enum FileManagement\_ErrCode

**Description**

Enumerates the error codes used in the **FileIO** module.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| ERR\_OK = 0 | The API is called successfully. |
| ERR\_PERMISSION\_ERROR = 201 | The permission verification fails. |
| ERR\_INVALID\_PARAMETER = 401 | Invalid parameter. |
| ERR\_DEVICE\_NOT\_SUPPORTED = 801 | The device does not support this API. |
| ERR\_EPERM = 13900001 | The operation is not allowed. |
| ERR\_ENOENT = 13900002 | The file or folder does not exist. |
| ERR\_ENOMEM = 13900011 | A memory overflow occurs. |
| ERR\_UNKNOWN = 13900042 | Internal unknown error. |
