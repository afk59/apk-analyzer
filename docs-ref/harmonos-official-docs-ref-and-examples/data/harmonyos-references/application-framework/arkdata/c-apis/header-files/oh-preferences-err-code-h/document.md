# oh\_preferences\_err\_code.h

#### Overview

Defines the error codes used in the **Preferences** module.

**File to include**: <database/preferences/oh\_preferences\_err\_code.h>

**Library**: libohpreferences.so

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Since**: 13

**Related module**: [Preferences](../../modules/preferences/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Preferences\_ErrCode](#oh_preferences_errcode) | OH\_Preferences\_ErrCode | Enumerates the error codes. |

#### Enum Description

#### \[h2\]OH\_Preferences\_ErrCode

enum OH\_Preferences\_ErrCode

**Description**

Enumerates the error codes.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| PREFERENCES\_OK = 0 | The operation is successful. |
| PREFERENCES\_ERROR\_INVALID\_PARAM = 401 | Invalid parameter. |
| PREFERENCES\_ERROR\_NOT\_SUPPORTED = 801 | The system capability is not supported. |
| PREFERENCES\_ERROR\_BASE = 15500000 | Base error code. |
| PREFERENCES\_ERROR\_DELETE\_FILE = 15500010 | Failed to delete the file. |
| PREFERENCES\_ERROR\_STORAGE = 15500011 | The storage is abnormal. |
| PREFERENCES\_ERROR\_MALLOC = 15500012 | Memory allocation fails. |
| PREFERENCES\_ERROR\_KEY\_NOT\_FOUND = 15500013 | The key does not exist. |
| PREFERENCES\_ERROR\_GET\_DATAOBSMGRCLIENT = 15500019 | Failed to obtain the data change subscription service. |
