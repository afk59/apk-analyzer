# JSVM\_TypeTag

typedef struct {...} JSVM\_TypeTag

#### Overview

Defines the type tag, which is stored as a 128-bit value of two unsigned 64-bit integers. As a UUID, it can tag JavaScript objects to ensure that their types remain unchanged.

**Since**: 11

**Related module**: [JSVM](../../modules/jsvm/document.md)

**Header file**: [jsvm\_types.h](../../header-files/jsvm-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint64\_t lower | Lower 64 bits. |
| uint64\_t upper | Upper 64 bits. |
