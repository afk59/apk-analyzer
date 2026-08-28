# ffrt\_task\_attr\_t

typedef struct {...} ffrt\_task\_attr\_t

#### Overview

The **ffrt\_task\_attr\_t** struct describes a concurrent task attribute.

**Since**: 10

**Related module**: [FFRT](../../modules/ffrt/document.md)

**Header file**: [type\_def.h](../../header-files/type-def-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t storage\[(ffrt\_task\_attr\_storage\_size + sizeof(uint32\_t) - 1) / sizeof(uint32\_t)\] | Storage size of a task attribute. |
