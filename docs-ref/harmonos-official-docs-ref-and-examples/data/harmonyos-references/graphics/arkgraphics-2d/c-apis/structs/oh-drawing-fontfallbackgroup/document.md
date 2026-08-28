# OH\_Drawing\_FontFallbackGroup

typedef struct {...} OH\_Drawing\_FontFallbackGroup

#### Overview

This struct describes the information about a font fallback group.

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

**Header file**: [drawing\_text\_typography.h](../../header-files/drawing-text-typography-h/document.md)

#### Total

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char\* groupName | Pointer to the name of the group corresponding to the font fallback group. If null is passed in, all fonts in the font fallback group can be used. |
| size\_t fallbackInfoSize | Number of font fallbacks. |
| [OH\_Drawing\_FontFallbackInfo](../oh-drawing-fontfallbackinfo/document.md)\* fallbackInfoSet | Pointer to the set of font fallbacks. |
