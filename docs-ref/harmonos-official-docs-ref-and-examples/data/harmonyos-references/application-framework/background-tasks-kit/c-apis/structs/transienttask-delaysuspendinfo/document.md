# TransientTask\_DelaySuspendInfo

typedef struct TransientTask\_DelaySuspendInfo {...} TransientTask\_DelaySuspendInfo

#### Overview

A struct that describes the returned information about a transient task.

**Since**: 13

**Related module**: [TransientTask](../../modules/transienttask/document.md)

**Header file**: [transient\_task\_type.h](../../header-files/transient-task-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t requestId | Request ID of a transient task. |
| int32\_t actualDelayTime | Remaining time, in ms. |
