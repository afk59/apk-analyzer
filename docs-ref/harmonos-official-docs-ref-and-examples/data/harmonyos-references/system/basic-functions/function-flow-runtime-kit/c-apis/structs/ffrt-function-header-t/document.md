# ffrt\_function\_header\_t

typedef struct {...} ffrt\_function\_header\_t

#### Overview

The **ffrt\_function\_header\_t** struct describes a task execution function.

**Since**: 10

**Related module**: [FFRT](../../modules/ffrt/document.md)

**Header file**: [type\_def.h](../../header-files/type-def-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [ffrt\_function\_t](../../header-files/type-def-h/document.md#ffrt_function_t) exec | Function used to execute a task. |
| [ffrt\_function\_t](../../header-files/type-def-h/document.md#ffrt_function_t) destroy | Function used to destroy a task. |
| uint64\_t reserve\[2\] | Reserved bit, which must be set to **0**. |
