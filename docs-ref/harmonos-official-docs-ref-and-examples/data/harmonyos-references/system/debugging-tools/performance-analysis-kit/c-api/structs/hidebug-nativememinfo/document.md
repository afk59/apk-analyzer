# HiDebug\_NativeMemInfo

typedef struct HiDebug\_NativeMemInfo {...} HiDebug\_NativeMemInfo

#### Overview

Defines the struct for the local memory information of the application process.

**Since**: 12

**Related module**: [HiDebug](../../modules/hidebug/document.md)

**Header file**: [hidebug\_type.h](../../header-files/hidebug-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t pss | Proportional set size, in KB. |
| uint32\_t vss | Virtual memory size, in KB. |
| uint32\_t rss | Resident set size, in KB. |
| uint32\_t sharedDirty | Size of the shared dirty memory, in KB. |
| uint32\_t privateDirty | Size of the private dirty memory, in KB. |
| uint32\_t sharedClean | Size of the shared clean memory, in KB. |
| uint32\_t privateClean | Size of the private clean memory, in KB. |
