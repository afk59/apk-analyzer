# drawing\_text\_global.h

#### Overview

This file declares the functions related to global text information, for example, setting the high contrast mode for text rendering.

**File to include**: <native\_drawing/drawing\_text\_global.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Enumerated value

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_TextHighContrast](#oh_drawing_texthighcontrast) | OH\_Drawing\_TextHighContrast | Enum of the high contrast modes for text rendering. |
| [OH\_Drawing\_TextUndefinedGlyphDisplay](#oh_drawing_textundefinedglyphdisplay) | OH\_Drawing\_TextUndefinedGlyphDisplay | Enum of the modes for displaying undefined glyphs. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [void OH\_Drawing\_SetTextHighContrast(OH\_Drawing\_TextHighContrast action)](#oh_drawing_settexthighcontrast) | Sets the high contrast mode for text rendering. |
| [void OH\_Drawing\_SetTextUndefinedGlyphDisplay(OH\_Drawing\_TextUndefinedGlyphDisplay undefinedGlyphDisplay)](#oh_drawing_settextundefinedglyphdisplay) | Sets how undefined glyphs are displayed. The setting affects all subsequent text rendering. |

#### Enum Description

#### \[h2\]OH\_Drawing\_TextHighContrast

enum OH\_Drawing\_TextHighContrast

**Description**

Defines an enum of the high contrast modes for text rendering.

**Since**: 20

| Value | Description |
| :-- | :-- |
| TEXT\_FOLLOW\_SYSTEM\_HIGH\_CONTRAST | Follows the high contrast mode for text rendering in the system settings. |
| TEXT\_APP\_DISABLE\_HIGH\_CONTRAST | Disables the high contrast mode for text rendering in the application. This mode takes precedence over the one based on system settings. |
| TEXT\_APP\_ENABLE\_HIGH\_CONTRAST | Enables the high contrast mode for text rendering in the application. The priority of this mode is higher than the mode following the system settings. |

#### \[h2\]OH\_Drawing\_TextUndefinedGlyphDisplay

enum OH\_Drawing\_TextUndefinedGlyphDisplay

**Description**

Defines an enum of the modes for displaying undefined glyphs.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

| Value | Description |
| :-- | :-- |
| TEXT\_NO\_GLYPH\_USE\_DEFAULT = 0 | Uses the default glyph (which may be a blank box, space, or custom symbol) defined in the font file. |
| TEXT\_NO\_GLYPH\_USE\_TOFU = 1 | Always uses tofu blocks to represent absent glyphs. |

#### Function Description

#### \[h2\]OH\_Drawing\_SetTextHighContrast()

void OH\_Drawing\_SetTextHighContrast(OH\_Drawing\_TextHighContrast action)

**Description**

Sets the high contrast mode for text rendering.

The setting of this API takes effect for the entire process, and all pages in the process share the same mode.

You can call this API to set the high contrast mode, or enable or disable the high contrast mode by toggling the switch on the system settings screen. This API is used to set the high contrast mode for text rendering. The setting of this API takes precedence over the one based on system settings.

This API does not take effect for the text drawing scenario.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextHighContrast](#oh_drawing_texthighcontrast) action | High contrast mode for text rendering. The value is an enumerated value of the [OH\_Drawing\_TextHighContrast](#oh_drawing_texthighcontrast) type. |

#### \[h2\]OH\_Drawing\_SetTextUndefinedGlyphDisplay()

void OH\_Drawing\_SetTextUndefinedGlyphDisplay(OH\_Drawing\_TextUndefinedGlyphDisplay undefinedGlyphDisplay)

**Description**

Sets how undefined glyphs are displayed. The setting affects all subsequent text rendering.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextUndefinedGlyphDisplay](#oh_drawing_textundefinedglyphdisplay) undefinedGlyphDisplay | Mode of displaying undefined glyphs. The value is an enumerated value of the [OH\_Drawing\_TextUndefinedGlyphDisplay](#oh_drawing_textundefinedglyphdisplay) type. |
