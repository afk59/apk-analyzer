# ffrt\_mutex\_t

typedef struct {...} ffrt\_mutex\_t

#### Overview

The **ffrt\_mutex\_t** struct describes an FFRT mutex.

**Since**: 10

**Related module**: [FFRT](../../modules/ffrt/document.md)

**Header file**: [type\_def.h](../../header-files/type-def-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t storage\[(ffrt\_mutex\_storage\_size + sizeof(uint32\_t) - 1) / sizeof(uint32\_t)\] | Storage size of a mutex. |
