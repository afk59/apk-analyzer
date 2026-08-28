# JSVM\_HeapStatistics

typedef struct {...} JSVM\_HeapStatistics

#### Overview

Stores statistics about JavaScript heap memory usage.

**Since**: 12

**Related module**: [JSVM](../../modules/jsvm/document.md)

**Header file**: [jsvm\_types.h](../../header-files/jsvm-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| size\_t totalHeapSize | Total heap size, in KB. |
| size\_t totalHeapSizeExecutable | Total size of the executable heap, in KB. |
| size\_t totalPhysicalSize | Total physical memory size, in KB. |
| size\_t totalAvailableSize | Total available memory size, in KB. |
| size\_t usedHeapSize | Used heap size, in KB. |
| size\_t heapSizeLimit | Heap size limit, in KB. |
| size\_t mallocedMemory | Allocated memory size, in KB. |
| size\_t externalMemory | External memory size, in KB. |
| size\_t peakMallocedMemory | Maximum size of the memory that can be allocated, in KB. |
| size\_t numberOfNativeContexts | Number of active native contexts. If the value keeps increasing, memory leaks may occur. |
| size\_t numberOfDetachedContexts | Number of detached contexts. |
| size\_t totalGlobalHandlesSize | Total size of global handles, in KB. |
| size\_t usedGlobalHandlesSize | Size of the used global handles, in KB. |
