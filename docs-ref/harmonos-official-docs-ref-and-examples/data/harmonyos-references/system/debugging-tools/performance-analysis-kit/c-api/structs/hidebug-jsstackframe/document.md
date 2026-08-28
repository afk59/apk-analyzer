# HiDebug\_JsStackFrame

typedef struct HiDebug\_JsStackFrame {...} HiDebug\_JsStackFrame

#### Overview

Defines the JS stack frame content.

**Since**: 20

**Related module**: [HiDebug](../../modules/hidebug/document.md)

**Header file**: [hidebug\_type.h](../../header-files/hidebug-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint64\_t relativePc | Relative PC address, which is the offset of the current PC relative to the start address of its mapping area (such as an executable file or shared library). |
| int32\_t line | Line number of the code corresponding to the current stack frame. |
| int32\_t column | Column number of the code corresponding to the current stack frame. |
| const char\* mapName | Name of the mapping area to which the current stack frame belongs. |
| const char\* functionName | Name of the function corresponding to the current stack frame. |
| const char\* url | URL of the code file corresponding to the current stack frame. It can be used to find the corresponding code file in the local path or on the remote server. |
| const char\* packageName | Name of the package to which the code corresponding to the current stack frame belongs. |
