# hiappevent\_cfg.h

#### Overview

Defines the configuration items of the event logging configuration function. To configure the application event logging functionality, you can directly use configuration item constants.

**File to include**: <hiappevent/hiappevent\_cfg.h>

**Library**: libhiappevent\_ndk.z.so

**System capability**: SystemCapability.HiviewDFX.HiAppEvent

**Since**: 8

**Related module**: [HiAppEvent](../../modules/hiappevent/document.md)

#### Summary

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| [DISABLE](#disable) "disable" | 
Whether to disable event logging. The default value is **false**. The value **true** means to disable the event logging function, and the value **false** means the opposite.

**Since**: 8

 |
| [MAX\_STORAGE](#max_storage) "max\_storage" | 

Storage quota of the event file directory. The default value is **10M**.

**Since**: 8

 |

#### Macro Description

#### \[h2\]DISABLE

#define DISABLE "disable"

**Description**

Whether to disable event logging. The default value is **false**. The value **true** means to disable the event logging function, and the value **false** means the opposite.

**Since**: 8

#### \[h2\]MAX\_STORAGE

#define MAX\_STORAGE "max\_storage"

**Description**

Storage quota of the event file directory. The default value is **10M**.

**Since**: 8
