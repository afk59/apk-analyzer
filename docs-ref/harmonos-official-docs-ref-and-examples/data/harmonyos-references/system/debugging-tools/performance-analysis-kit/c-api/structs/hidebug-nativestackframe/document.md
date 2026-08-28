# HiDebug\_NativeStackFrame

typedef struct HiDebug\_NativeStackFrame {...} HiDebug\_NativeStackFrame

#### Overview

Defines the native stack frame content.

**Since**: 20

**Related module**: [HiDebug](../../modules/hidebug/document.md)

**Header file**: [hidebug\_type.h](../../header-files/hidebug-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint64\_t relativePc | Relative PC address, which is the offset of the current PC relative to the start address of its mapping area (such as an executable file or shared library). |
| uint64\_t funcOffset | Offset of the function corresponding to the current stack frame in its mapping area (such as an executable file or shared library). |
| const char\* mapName | Name of the mapping area to which the current stack frame belongs. |
| const char\* functionName | Name of the function corresponding to the current stack frame. |
| const char\* buildId | Build ID that uniquely identifies the current mapping area (such as an executable file or shared library). During debugging and symbol parsing, **buildId** ensures that the symbol file version matches the actual binary file version. |
| const char\* reserved | Reserved field for future extension. |
