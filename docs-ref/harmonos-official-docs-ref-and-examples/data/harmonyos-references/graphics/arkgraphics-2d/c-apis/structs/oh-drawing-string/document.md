# OH\_Drawing\_String

typedef struct {...} OH\_Drawing\_String

#### Overview

This struct describes a string of characters encoded in UTF-16.

**Since**: 14

**Related module**: [Drawing](../../modules/drawing/document.md)

**Header file**: [drawing\_types.h](../../header-files/drawing-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t\* strData | Pointer to a byte array that stores characters in the UTF-16 encoding format. |
| uint32\_t strLen | Actual length of the string that **strData** points to, in bytes. |
