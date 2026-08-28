# oh\_pasteboard\_err\_code.h

#### Overview

Declares the error code information of the pasteboard.

**File to include**: <database/pasteboard/oh\_pasteboard\_err\_code.h>

**Library**: libpasteboard.so

**System capability**: SystemCapability.MiscServices.Pasteboard

**Since**: 13

**Related module**: [Pasteboard](../../modules/pasteboard/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [PASTEBOARD\_ErrCode](#pasteboard_errcode) | PASTEBOARD\_ErrCode | Enumerates the error codes. |

#### Enum Description

#### \[h2\]PASTEBOARD\_ErrCode

enum PASTEBOARD\_ErrCode

**Description**

Enumerates the error codes.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| ERR\_OK = 0 | Operation successful. |
| ERR\_PERMISSION\_ERROR = 201 | Permission verification failed. |
| ERR\_INVALID\_PARAMETER = 401 | Invalid parameter. |
| ERR\_DEVICE\_NOT\_SUPPORTED = 801 | Device capability not supported. |
| ERR\_INNER\_ERROR = 12900000 | Internal error. |
| ERR\_BUSY = 12900003 | System busy. |
| ERR\_PASTEBOARD\_COPY\_FILE\_ERROR = 12900007 | 
Failed to copy files.

Since: 15

 |
| ERR\_PASTEBOARD\_PROGRESS\_START\_ERROR = 12900008 | 

Failed to display the progress.

Since: 15

 |
| ERR\_PASTEBOARD\_PROGRESS\_ABNORMAL = 12900009 | 

Abnormal progress.

Since: 15

 |
| ERR\_PASTEBOARD\_GET\_DATA\_FAILED = 12900010 | 

Failed to obtain the pasteboard data.

Since: 15

 |
