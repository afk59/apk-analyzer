# ffrt\_rwlock\_t

typedef struct {...} ffrt\_rwlock\_t

#### Overview

The **ffrt\_rwlock\_t** struct describes an FFRT read-write lock.

**Since**: 18

**Related module**: [FFRT](../../modules/ffrt/document.md)

**Header file**: [type\_def.h](../../header-files/type-def-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t storage\[(ffrt\_rwlock\_storage\_size + sizeof(uint32\_t) - 1) / sizeof(uint32\_t)\] | Storage size of a read-write lock. |
