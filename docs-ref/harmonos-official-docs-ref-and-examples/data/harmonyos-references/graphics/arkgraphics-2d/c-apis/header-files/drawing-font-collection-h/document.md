# drawing\_font\_collection.h

#### Overview

This file declares the functions related to the font collection in the drawing module.

**File to include**: <native\_drawing/drawing\_font\_collection.h>

**Library**: libnative\_drawing.so

**Since**: 8

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontCollection\* OH\_Drawing\_CreateFontCollection(void)](#oh_drawing_createfontcollection) | Creates an [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md) object. |
| [void OH\_Drawing\_DestroyFontCollection(OH\_Drawing\_FontCollection\* fontCollection)](#oh_drawing_destroyfontcollection) | Destroys an **OH\_Drawing\_FontCollection** object and reclaims the memory occupied by the object. |
| [void OH\_Drawing\_DisableFontCollectionFallback(OH\_Drawing\_FontCollection\* fontCollection)](#oh_drawing_disablefontcollectionfallback) | Disables the system fonts. |
| [void OH\_Drawing\_DisableFontCollectionSystemFont(OH\_Drawing\_FontCollection\* fontCollection)](#oh_drawing_disablefontcollectionsystemfont) | Disables the system fonts. |
| [OH\_Drawing\_FontCollection\* OH\_Drawing\_CreateSharedFontCollection(void)](#oh_drawing_createsharedfontcollection) | Creates a shareable [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md) object. |
| [void OH\_Drawing\_ClearFontCaches(OH\_Drawing\_FontCollection\* fontCollection)](#oh_drawing_clearfontcaches) | Clears the font cache. (The font cache has a memory limit and a clearing mechanism. It occupies limited memory. You are not advised to clear it unless otherwise required.) |
| [OH\_Drawing\_FontCollection\* OH\_Drawing\_GetFontCollectionGlobalInstance(void)](#oh_drawing_getfontcollectionglobalinstance) | Obtains the global [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md) object, which can be used to sense the theme font information. Do not release the object. |

#### Function Description

#### \[h2\]OH\_Drawing\_CreateFontCollection()

OH\_Drawing\_FontCollection\* OH\_Drawing\_CreateFontCollection(void)

**Description**

Creates an [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md) object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md)\* | Returns the pointer to the **OH\_Drawing\_FontCollection** object created. The **OH\_Drawing\_FontCollection** object created by this function cannot be shared by multiple [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md) objects. You need to use the [OH\_Drawing\_CreateSharedFontCollection](#oh_drawing_createsharedfontcollection) function to create an **OH\_Drawing\_FontCollection** object for sharing. |

#### \[h2\]OH\_Drawing\_DestroyFontCollection()

void OH\_Drawing\_DestroyFontCollection(OH\_Drawing\_FontCollection\* fontCollection)

**Description**

Destroys an **OH\_Drawing\_FontCollection** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md)\* fontCollection | Pointer to an **OH\_Drawing\_FontCollection** object. |

#### \[h2\]OH\_Drawing\_DisableFontCollectionFallback()

void OH\_Drawing\_DisableFontCollectionFallback(OH\_Drawing\_FontCollection\* fontCollection)

**Description**

Disables the system fonts.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md)\* fontCollection | Pointer to an [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md) object. |

#### \[h2\]OH\_Drawing\_DisableFontCollectionSystemFont()

void OH\_Drawing\_DisableFontCollectionSystemFont(OH\_Drawing\_FontCollection\* fontCollection)

**Description**

Disables the system fonts.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md)\* fontCollection | Pointer to an [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md) object. |

#### \[h2\]OH\_Drawing\_CreateSharedFontCollection()

OH\_Drawing\_FontCollection\* OH\_Drawing\_CreateSharedFontCollection(void)

**Description**

Creates a shareable [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md) object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md)\* | Returns the pointer to the **OH\_Drawing\_FontCollection** object created. |

#### \[h2\]OH\_Drawing\_ClearFontCaches()

void OH\_Drawing\_ClearFontCaches(OH\_Drawing\_FontCollection\* fontCollection)

**Description**

Clears the font cache. (The font cache has a memory limit and a clearing mechanism. It occupies limited memory. You are not advised to clear it unless otherwise required.)

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md)\* fontCollection | Pointer to an [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md) object. |

#### \[h2\]OH\_Drawing\_GetFontCollectionGlobalInstance()

OH\_Drawing\_FontCollection\* OH\_Drawing\_GetFontCollectionGlobalInstance(void)

**Description**

Obtains the global [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md) object, which can be used to sense the theme font information. Do not release the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 14

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md)\* | Returns the pointer to the global {@link OH\_Drawing\_FontCollection} object obtained. |
