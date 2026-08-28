# OH\_Drawing\_FontGenericInfo

typedef struct {...} OH\_Drawing\_FontGenericInfo

#### Overview

This struct describes the information about generic fonts supported by the system.

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

**Header file**: [drawing\_text\_typography.h](../../header-files/drawing-text-typography-h/document.md)

#### Total

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char\* familyName | Pointer to the name of a font family. |
| size\_t aliasInfoSize | Number of font aliases. |
| size\_t adjustInfoSize | Number of font weight mappings. |
| [OH\_Drawing\_FontAliasInfo](../oh-drawing-fontaliasinfo/document.md)\* aliasInfoSet | Pointer to a set of font aliases. |
| [OH\_Drawing\_FontAdjustInfo](../oh-drawing-fontadjustinfo/document.md)\* adjustInfoSet | Pointer to a set of font weight mappings. |
