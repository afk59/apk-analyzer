# OH\_Drawing\_FontAliasInfo

typedef struct {...} OH\_Drawing\_FontAliasInfo

#### Overview

This struct describes the information about a font alias.

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

**Header file**: [drawing\_text\_typography.h](../../header-files/drawing-text-typography-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char\* familyName | Pointer to the name of a font family. |
| int weight | Font weight. If the value is greater than 0, only the fonts with the specified weight in the font family are contained. If the value is 0, all the fonts in the font family are contained. |
