# OH\_Drawing\_StrutStyle

typedef struct {...} OH\_Drawing\_StrutStyle

#### Overview

This struct describes a strut style. The strut style determines the line spacing, baseline alignment mode, and other properties related to the line height when drawing text.

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

**Header file**: [drawing\_text\_typography.h](../../header-files/drawing-text-typography-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontWeight](../../header-files/drawing-text-typography-h/document.md#oh_drawing_fontweight) weight | Font weight used for calculating the strut. |
| [OH\_Drawing\_FontStyle](../../header-files/drawing-text-typography-h/document.md#oh_drawing_fontstyle) style | Font style used for calculating the strut. |
| double size | Size of the ascent plus descent in the logical pixels. |
| double heightScale | Scale factor of the line height. |
| bool heightOverride | Whether to enable height override. **true**: enabled; **false**: disabled. |
| bool halfLeading | Whether to enable half leading. **true**: enabled; **false**: disabled. |
| double leading | Custom leading to be applied to the strut. |
| bool forceStrutHeight | Whether to forcibly use the strut height for all rows. **true** means yes; **false** otherwise. |
| size\_t familiesSize | Number of font families. |
| char\*\* families | Double pointer to the font families used for calculating the strut. |
