# OH\_Drawing\_FontConfigInfo

typedef struct {...} OH\_Drawing\_FontConfigInfo

#### Overview

This struct describes the information about a system font configuration.

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

**Header file**: [drawing\_text\_typography.h](../../header-files/drawing-text-typography-h/document.md)

#### Total

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| size\_t fontDirSize | Number of system font file paths. |
| size\_t fontGenericInfoSize | Number of generic fonts. |
| size\_t fallbackGroupSize | Number of font fallbacks. |
| char\*\* fontDirSet | Double pointer to the system font file paths. |
| [OH\_Drawing\_FontGenericInfo](../oh-drawing-fontgenericinfo/document.md)\* fontGenericInfoSet | Pointer to a set of generic fonts. |
| [OH\_Drawing\_FontFallbackGroup](../oh-drawing-fontfallbackgroup/document.md)\* fallbackGroupSet | Pointer to a set of font fallbacks. |
