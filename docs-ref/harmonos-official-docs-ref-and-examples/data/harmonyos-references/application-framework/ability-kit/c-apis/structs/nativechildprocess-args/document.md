# NativeChildProcess\_Args

typedef struct {...} NativeChildProcess\_Args

#### Overview

The struct describes the parameters passed to the child process.

**Since**: 13

**Related module**: [ChildProcess](../../modules/childprocess/document.md)

**Header file**: [native\_child\_process.h](../../header-files/native-child-process-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char\* entryParams | Pointer to the entry parameters. The size cannot exceed 150 KB. |
| struct [NativeChildProcess\_FdList](../nativechildprocess-fdlist/document.md) fdList | List of file descriptors passed to the child process. |
