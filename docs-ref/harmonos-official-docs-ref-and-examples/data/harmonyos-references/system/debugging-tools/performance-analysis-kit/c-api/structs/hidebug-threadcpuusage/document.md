# HiDebug\_ThreadCpuUsage

typedef struct HiDebug\_ThreadCpuUsage {...} HiDebug\_ThreadCpuUsage

#### Overview

Defines the struct for the CPU usage of all threads of an application.

**Since**: 12

**Related module**: [HiDebug](../../modules/hidebug/document.md)

**Header file**: [hidebug\_type.h](../../header-files/hidebug-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t threadId | Thread ID. |
| double cpuUsage | Thread CPU usage, in percentage. |
| struct [HiDebug\_ThreadCpuUsage](#) \*next | Pointer to the CPU usage of the next thread. |
