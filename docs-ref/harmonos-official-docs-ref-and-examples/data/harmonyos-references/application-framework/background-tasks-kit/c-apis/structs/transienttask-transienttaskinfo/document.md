# TransientTask\_TransientTaskInfo

typedef struct TransientTask\_TransientTaskInfo {...} TransientTask\_TransientTaskInfo

#### Overview

A struct that describes all transient task information.

**Since**: 20

**Related module**: [TransientTask](../../modules/transienttask/document.md)

**Header file**: [transient\_task\_type.h](../../header-files/transient-task-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t remainingQuota | Remaining quota of the current day, in ms. |
| [TransientTask\_DelaySuspendInfo](../transienttask-delaysuspendinfo/document.md) transientTasks\[[TRANSIENT\_TASK\_MAX\_NUM](../../header-files/transient-task-type-h/document.md#macros)\] | All requested transient task information, including the task request ID and remaining time, in ms. |
