# NativeChildProcess\_Fd

typedef struct {...} NativeChildProcess\_Fd

#### Overview

The struct describes the information about the file descriptor passed to the child process.

**Since**: 13

**Related module**: [ChildProcess](../../modules/childprocess/document.md)

**Header file**: [native\_child\_process.h](../../header-files/native-child-process-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char\* fdName | Pointer to the name of the file descriptor. It contains a maximum of 20 characters. |
| int32\_t fd | Value of the file descriptor. |
| struct [NativeChildProcess\_Fd](#)\* next | Pointer to the next file descriptor. |
