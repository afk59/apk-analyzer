# NativeChildProcess\_FdList

typedef struct NativeChildProcess\_FdList {...} NativeChildProcess\_FdList

#### Overview

The struct describes a list of file descriptors passed to the child process. The list can contain a maximum of 16 entries.

**Since**: 13

**Related module**: [ChildProcess](../../modules/childprocess/document.md)

**Header file**: [native\_child\_process.h](../../header-files/native-child-process-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| struct [NativeChildProcess\_Fd](../nativechildprocess-fd/document.md)\* head | Pointer to the first file descriptor in the linked list passed to the child process. |
