# OH\_Drawing\_FontDescriptor

typedef struct {...} OH\_Drawing\_FontDescriptor

#### Overview

This struct describes the detailed information about a system font.

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

**Header file**: [drawing\_text\_typography.h](../../header-files/drawing-text-typography-h/document.md)

#### Total

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char\* path | File path of the system font. |
| char\* postScriptName | PostScript name that uniquely identifies the system font. |
| char\* fullName | Full name of the system font. |
| char\* fontFamily | Family of the system font. |
| char\* fontSubfamily | Subfamily of the system font. |
| int weight | Weight of the system font. |
| int width | Width of the system font. |
| int italic | Slope of the system font. |
| bool monoSpace | Whether the system font is monospaced. **true** means yes; **false** otherwise. |
| bool symbolic | Whether the system font supports symbols. **true** means yes; **false** otherwise. |
