# transient\_task\_type.h

#### Overview

The **transient\_task\_type.h** file declares the error codes and structs of a transient task.

**File to include**: <transient\_task/transient\_task\_type.h>

**Library**: libtransient\_task.so

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**Since**: 11

**Related module**: [TransientTask](../../modules/transienttask/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [TransientTask\_DelaySuspendInfo](../../structs/transienttask-delaysuspendinfo/document.md) | TransientTask\_DelaySuspendInfo | A struct that describes the returned information about a transient task. |
| [TransientTask\_TransientTaskInfo](../../structs/transienttask-transienttaskinfo/document.md) | TransientTask\_TransientTaskInfo | A struct that describes all transient task information. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| TRANSIENT\_TASK\_MAX\_NUM 3 | 
Defines the maximum number of transient tasks at the same time.

**Since**: 20

 |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [TransientTask\_ErrorCode](#transienttask_errorcode) | TransientTask\_ErrorCode | Enumerates the error codes available for a transient task. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*TransientTask\_Callback)(void)](#transienttask_callback) | TransientTask\_Callback | Defines a callback for transient task timeout. |

#### Enum Description

#### \[h2\]TransientTask\_ErrorCode

enum TransientTask\_ErrorCode

**Description**

Enumerates the error codes available for a transient task.

**Since**: 13

| Enum | Description |
| :-- | :-- |
| ERR\_TRANSIENT\_TASK\_OK = 0 | Operation successful. |
| ERR\_TRANSIENT\_TASK\_INVALID\_PARAM = 401 | Parameter check failed. Possible causes: 1. Mandatory parameters are not passed. 2. Incorrect parameter types. |
| ERR\_TRANSIENT\_TASK\_PARCEL\_FAILED = 9800002 | Parcel read/write operation failed. |
| ERR\_TRANSIENT\_TASK\_TRANSACTION\_FAILED = 9800003 | IPC failed. |
| ERR\_TRANSIENT\_TASK\_SYS\_NOT\_READY = 9800004 | System service failed. |
| ERR\_TRANSIENT\_TASK\_CLIENT\_INFO\_VERIFICATION\_FAILED = 9900001 | Failed to verify the client information of the transient task. |
| ERR\_TRANSIENT\_TASK\_SERVICE\_VERIFICATION\_FAILED = 9900002 | Failed to verify the server information of the transient task. |
| ERR\_TRANSIENT\_TASK\_PARCELABLE\_FAILED = 9900003 | Parcel read/write operation failed for the transient task. Possible causes: 1. The parameter is invalid. 2. Memory allocation fails. |
| ERR\_TRANSIENT\_TASK\_SERVICE\_NOT\_READY = 9900004 | System service failed for the transient task. |

#### Function Description

#### \[h2\]TransientTask\_Callback()

typedef void (\*TransientTask\_Callback)(void)

**Description**

Defines a callback for transient task timeout.

**Since**: 13
