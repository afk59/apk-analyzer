# HiDebug\_MemoryLimit

typedef struct HiDebug\_MemoryLimit {...} HiDebug\_MemoryLimit

#### Overview

Defines the struct for the memory limit of the application process.

**Since**: 12

**Related module**: [HiDebug](../../modules/hidebug/document.md)

**Header file**: [hidebug\_type.h](../../header-files/hidebug-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint64\_t rssLimit | Limit on the physical memory size of the application process, in KB. Currently, the system does not limit the physical memory size of the process. However, the available physical memory of the process cannot exceed the maximum physical memory of the device. You can call [OH\_HiDebug\_GetSystemMemInfo](../../header-files/hidebug-h/document.md#oh_hidebug_getsystemmeminfo) to obtain the physical memory usage of the device. |
| uint64\_t vssLimit | Limit on the virtual set size, in KB. |
