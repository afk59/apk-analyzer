# ffrt\_cond\_t

typedef struct {...} ffrt\_cond\_t

#### Overview

The **ffrt\_cond\_t** struct describes a condition variable.

**Since**: 10

**Related module**: [FFRT](../../modules/ffrt/document.md)

**Header file**: [type\_def.h](../../header-files/type-def-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t storage\[(ffrt\_cond\_storage\_size + sizeof(uint32\_t) - 1) / sizeof(uint32\_t)\] | Storage size of a condition variable. |
