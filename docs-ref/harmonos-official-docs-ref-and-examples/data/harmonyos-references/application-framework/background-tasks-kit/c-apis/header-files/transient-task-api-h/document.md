# transient\_task\_api.h

#### Overview

The **transient\_task\_api.h** file declares the APIs for requesting, querying, and canceling transient tasks.

**File to include**: <transient\_task/transient\_task\_api.h>

**Library**: libtransient\_task.so

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**Since**: 13

**Related module**: [TransientTask](../../modules/transienttask/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_BackgroundTaskManager\_RequestSuspendDelay(const char\* reason,TransientTask\_Callback callback, TransientTask\_DelaySuspendInfo \*info)](#oh_backgroundtaskmanager_requestsuspenddelay) | Requests a transient task. |
| [int32\_t OH\_BackgroundTaskManager\_GetRemainingDelayTime(int32\_t requestId, int32\_t \*delayTime)](#oh_backgroundtaskmanager_getremainingdelaytime) | Obtains the remaining time of a transient task. |
| [int32\_t OH\_BackgroundTaskManager\_CancelSuspendDelay(int32\_t requestId)](#oh_backgroundtaskmanager_cancelsuspenddelay) | Cancels a transient task. |
| [int32\_t OH\_BackgroundTaskManager\_GetTransientTaskInfo(TransientTask\_TransientTaskInfo \*transientTaskInfo)](#oh_backgroundtaskmanager_gettransienttaskinfo) | Obtains all information about a transient task, including the remaining quota of the current day. |

#### Function Description

#### \[h2\]OH\_BackgroundTaskManager\_RequestSuspendDelay()

int32\_t OH\_BackgroundTaskManager\_RequestSuspendDelay(const char\* reason,TransientTask\_Callback callback, TransientTask\_DelaySuspendInfo \*info)

**Description**

Requests a transient task.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* reason | Reason for requesting the transient task. |
| [TransientTask\_Callback](../transient-task-type-h/document.md#transienttask_callback) callback | Callback used to notify the application that the transient task is about to time out. Generally, the callback is invoked 6 seconds before the timeout. |
| [TransientTask\_DelaySuspendInfo](../../structs/transienttask-delaysuspendinfo/document.md) \*info | Information about the transient task. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns 0 if the operation is successful.

Returns 401 if the input parameter is incorrect.

Returns 9800002 if the Parcel read/write operation fails.

Returns 9800003 if the IPC fails.

Returns 9800004 if the system service fails.

Returns 9900001 if the client information of the transient task fails to be verified.

Returns 9900002 if the server information of the transient task fails to be verified.

For details about the error codes, see [TransientTask\_ErrorCode](../transient-task-type-h/document.md#transienttask_errorcode).

 |

#### \[h2\]OH\_BackgroundTaskManager\_GetRemainingDelayTime()

int32\_t OH\_BackgroundTaskManager\_GetRemainingDelayTime(int32\_t requestId, int32\_t \*delayTime)

**Description**

Obtains the remaining time of a transient task.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t requestId | Request ID of the transient task. |
| int32\_t \*delayTime | Pointer to the remaining time of the transient task, in ms. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns 0 if the operation is successful.

Returns 401 if the input parameter is incorrect.

Returns 9800002 if the Parcel read/write operation fails.

Returns 9800003 if the IPC fails.

Returns 9800004 if the system service fails.

Returns 9900001 if the client information of the transient task fails to be verified.

Returns 9900002 if the server information of the transient task fails to be verified.

For details about the error codes, see [TransientTask\_ErrorCode](../transient-task-type-h/document.md#transienttask_errorcode).

 |

#### \[h2\]OH\_BackgroundTaskManager\_CancelSuspendDelay()

int32\_t OH\_BackgroundTaskManager\_CancelSuspendDelay(int32\_t requestId)

**Description**

Cancels a transient task.

**System capability**: SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t requestId | Request ID of the transient task. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns 0 if the operation is successful.

Returns 401 if the input parameter is incorrect.

Returns 9800002 if the Parcel read/write operation fails.

Returns 9800003 if the IPC fails.

Returns 9800004 if the system service fails.

Returns 9900001 if the client information of the transient task fails to be verified.

Returns 9900002 if the server information of the transient task fails to be verified.

For details about the error codes, see [TransientTask\_ErrorCode](../transient-task-type-h/document.md#transienttask_errorcode).

 |

#### \[h2\]OH\_BackgroundTaskManager\_GetTransientTaskInfo()

int32\_t OH\_BackgroundTaskManager\_GetTransientTaskInfo(TransientTask\_TransientTaskInfo  \*transientTaskInfo)

**Description**

Obtains all information about a transient task, including the remaining quota of the current day.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [TransientTask\_TransientTaskInfo](../../structs/transienttask-transienttaskinfo/document.md) \*transientTaskInfo | All information about a transient task. For details, see [TransientTask\_TransientTaskInfo](../../structs/transienttask-transienttaskinfo/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns 0 if the operation is successful.

Returns 9900001 if the client information of the transient task fails to be verified.

Returns 9900003 if the Parcel read/write operation fails.

Returns 9900004 if the system service fails.

For details about the error codes, see [TransientTask\_ErrorCode](../transient-task-type-h/document.md#transienttask_errorcode).

 |
