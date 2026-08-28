# drawing\_register\_font.h

#### Overview

This file declares the functions related to the font manager in the drawing module.

**File to include**: <native\_drawing/drawing\_register\_font.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [uint32\_t OH\_Drawing\_RegisterFont(OH\_Drawing\_FontCollection\*, const char\* fontFamily, const char\* familySrc)](#oh_drawing_registerfont) | Registers a custom font with the font manager. The supported font file formats are .ttf and .otf. |
| [uint32\_t OH\_Drawing\_RegisterFontBuffer(OH\_Drawing\_FontCollection\*, const char\* fontFamily, uint8\_t\* fontBuffer,size\_t length)](#oh_drawing_registerfontbuffer) | Registers a font buffer with the font manager. |
| [uint32\_t OH\_Drawing\_UnregisterFont(OH\_Drawing\_FontCollection\* fontCollection, const char\* fontFamily)](#oh_drawing_unregisterfont) | 
Unregisters a custom font by font family name.

Unregistering a font that is currently in use may lead to text rendering exceptions (such as garbled characters or missing glyphs).

All typography objects using the unregistered font family should be destroyed and re-created.

 |

#### Function Description

#### \[h2\]OH\_Drawing\_RegisterFont()

uint32\_t OH\_Drawing\_RegisterFont(OH\_Drawing\_FontCollection\*, const char\* fontFamily, const char\* familySrc)

**Description**

Registers a custom font with the font manager. The supported font file formats are .ttf and .otf.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md)\* | Pointer to an [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md) object. |
| const char\* fontFamily | Pointer to the family name of the font to register. |
| const char\* familySrc | Pointer to the path of the font file to register. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Returns **0** if the font is registered; returns **1** if the file does not exist; returns **2** if opening the file fails; returns **3** if reading the file fails; returns **4** if the file is not found; returns **5** if the file size is not obtained; returns **9** if the file is damaged. |

#### \[h2\]OH\_Drawing\_RegisterFontBuffer()

uint32\_t OH\_Drawing\_RegisterFontBuffer(OH\_Drawing\_FontCollection\*, const char\* fontFamily, uint8\_t\* fontBuffer,size\_t length)

**Description**

Registers a font buffer with the font manager.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md)\* | Pointer to an [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md) object. |
| const char\* fontFamily | Pointer to the family name of the font to register. |
| uint8\_t\* fontBuffer | Pointer to the buffer of the font file. |
| size\_t length | Length of the font file. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Returns **0** if the font is registered; returns **6** if the buffer size is zero; returns **7** if the font set is empty; returns **9** if the file is damaged. |

#### \[h2\]OH\_Drawing\_UnregisterFont()

uint32\_t OH\_Drawing\_UnregisterFont(OH\_Drawing\_FontCollection\* fontCollection, const char\* fontFamily)

**Description**

Unregisters a custom font by font family name.

Unregistering a font that is currently in use may lead to text rendering exceptions (such as garbled characters or missing glyphs).

All typography objects using the unregistered font family should be destroyed and re-created.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md)\* fontCollection | Pointer to an [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md) object. |
| const char\* fontFamily | Name of the font family to be unregistered. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Returns the result code. **0**: success; **8**: invalid input parameter; **1**: failure. |
