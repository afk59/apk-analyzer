# drawing\_pixel\_map.h

#### Overview

This file declares the functions related to the pixel map in the drawing module.

**File to include**: <native\_drawing/drawing\_pixel\_map.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [NativePixelMap\_](../../structs/nativepixelmap/document.md) | NativePixelMap\_ | Defines a pixel map defined by the image framework. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) | OH\_PixelmapNative | Defines a pixel map defined by the image framework. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_PixelMap\* OH\_Drawing\_PixelMapGetFromNativePixelMap(NativePixelMap\_\* nativePixelMap)](#oh_drawing_pixelmapgetfromnativepixelmap) | Obtains the pixel map defined by this module from a pixel map defined by the image framework. |
| [OH\_Drawing\_PixelMap\* OH\_Drawing\_PixelMapGetFromOhPixelMapNative(OH\_PixelmapNative\* pixelmapNative)](#oh_drawing_pixelmapgetfromohpixelmapnative) | Obtains the pixel map defined by this module from a pixel map defined by the image framework. |
| [void OH\_Drawing\_PixelMapDissolve(OH\_Drawing\_PixelMap\* pixelMap)](#oh_drawing_pixelmapdissolve) | Removes the relationship between a pixel map defined by this module and a pixel map defined by the image framework. The relationship is established by calling [OH\_Drawing\_PixelMapGetFromNativePixelMap](#oh_drawing_pixelmapgetfromnativepixelmap) or [OH\_Drawing\_PixelMapGetFromOhPixelMapNative](#oh_drawing_pixelmapgetfromohpixelmapnative). |

#### Function Description

#### \[h2\]OH\_Drawing\_PixelMapGetFromNativePixelMap()

OH\_Drawing\_PixelMap\* OH\_Drawing\_PixelMapGetFromNativePixelMap(NativePixelMap\_\* nativePixelMap)

**Description**

Obtains the pixel map defined by this module from a pixel map defined by the image framework.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [NativePixelMap\_](../../structs/nativepixelmap/document.md)\* nativePixelMap | Pointer to a [NativePixelMap\_](../../structs/nativepixelmap/document.md) object, which is the pixel map defined by the image framework. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_PixelMap](../../structs/oh-drawing-pixelmap/document.md)\* | Returns the pointer to an [OH\_Drawing\_PixelMap](../../structs/oh-drawing-pixelmap/document.md) object, which is the pixel map defined by this module. If NULL is returned, the creation fails. The possible failure cause is that **NativePixelMap\_** is NULL. |

#### \[h2\]OH\_Drawing\_PixelMapGetFromOhPixelMapNative()

OH\_Drawing\_PixelMap\* OH\_Drawing\_PixelMapGetFromOhPixelMapNative(OH\_PixelmapNative\* pixelmapNative)

**Description**

Obtains the pixel map defined by this module from a pixel map defined by the image framework.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\* pixelmapNative | Pointer to a [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) object, which is the pixel map defined by the image framework. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_PixelMap](../../structs/oh-drawing-pixelmap/document.md)\* | Returns the pointer to an [OH\_Drawing\_PixelMap](../../structs/oh-drawing-pixelmap/document.md) object, which is the pixel map defined by this module. If NULL is returned, the creation fails. The possible failure cause is that **OH\_PixelmapNative** is NULL. |

#### \[h2\]OH\_Drawing\_PixelMapDissolve()

void OH\_Drawing\_PixelMapDissolve(OH\_Drawing\_PixelMap\* pixelMap)

**Description**

Removes the relationship between a pixel map defined by this module and a pixel map defined by the image framework. The relationship is established by calling [OH\_Drawing\_PixelMapGetFromNativePixelMap](#oh_drawing_pixelmapgetfromnativepixelmap) or [OH\_Drawing\_PixelMapGetFromOhPixelMapNative](#oh_drawing_pixelmapgetfromohpixelmapnative).

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_PixelMap](../../structs/oh-drawing-pixelmap/document.md)\* pixelMap | Pointer to an [OH\_Drawing\_PixelMap](../../structs/oh-drawing-pixelmap/document.md) object. |
