# drawing\_bitmap.h

#### Overview

This file declares the functions related to the bitmap in the drawing module.

**File to include**: <native\_drawing/drawing\_bitmap.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_BitmapFormat](../../structs/oh-drawing-bitmapformat/document.md) | OH\_Drawing\_BitmapFormat | Defines the pixel format of a bitmap, including the color type and alpha type. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Bitmap\* OH\_Drawing\_BitmapCreate(void)](#oh_drawing_bitmapcreate) | Creates an **OH\_Drawing\_Bitmap** object. |
| [void OH\_Drawing\_BitmapDestroy(OH\_Drawing\_Bitmap\* bitmap)](#oh_drawing_bitmapdestroy) | Destroys an **OH\_Drawing\_Bitmap** object and reclaims the memory occupied by the object. |
| [OH\_Drawing\_Bitmap\* OH\_Drawing\_BitmapCreateFromPixels(OH\_Drawing\_Image\_Info\* imageInfo, void\* pixels, uint32\_t rowBytes)](#oh_drawing_bitmapcreatefrompixels) | 
Creates an **OH\_Drawing\_Bitmap** object, with the address of the memory for storing the bitmap pixels set to the memory address that you applied for.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **imageInfo** or **pixels** is NULL or **rowBytes** is **0**, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_BitmapBuild(OH\_Drawing\_Bitmap\* bitmap,const uint32\_t width, const uint32\_t height, const OH\_Drawing\_BitmapFormat\* bitmapFormat)](#oh_drawing_bitmapbuild) | 

Initializes the width and height of a bitmap and sets the pixel format for the bitmap.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **bitmap** or **bitmapFormat** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [uint32\_t OH\_Drawing\_BitmapGetWidth(OH\_Drawing\_Bitmap\* bitmap)](#oh_drawing_bitmapgetwidth) | 

Obtains the width of a bitmap.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [uint32\_t OH\_Drawing\_BitmapGetHeight(OH\_Drawing\_Bitmap\* bitmap)](#oh_drawing_bitmapgetheight) | 

Obtains the height of a bitmap.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_ColorFormat OH\_Drawing\_BitmapGetColorFormat(OH\_Drawing\_Bitmap\* bitmap)](#oh_drawing_bitmapgetcolorformat) | 

Obtains the pixel format of a bitmap.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_AlphaFormat OH\_Drawing\_BitmapGetAlphaFormat(OH\_Drawing\_Bitmap\* bitmap)](#oh_drawing_bitmapgetalphaformat) | 

Obtains the alpha component of a bitmap.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void\* OH\_Drawing\_BitmapGetPixels(OH\_Drawing\_Bitmap\* bitmap)](#oh_drawing_bitmapgetpixels) | 

Obtains the pixel address of a bitmap. You can use this address to obtain the pixel data of the bitmap.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_BitmapGetImageInfo(OH\_Drawing\_Bitmap\* bitmap, OH\_Drawing\_Image\_Info\* imageInfo)](#oh_drawing_bitmapgetimageinfo) | 

Obtains the image information of a bitmap.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **bitmap** or **imageInfo** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_BitmapReadPixels(OH\_Drawing\_Bitmap\* bitmap, const OH\_Drawing\_Image\_Info\* dstInfo,void\* dstPixels, size\_t dstRowBytes, int32\_t srcX, int32\_t srcY)](#oh_drawing_bitmapreadpixels) | 

Reads pixels of a rectangle in a bitmap to the specified buffer.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **bitmap**, **dstInfo**, and **dstPixels** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |

#### Function Description

#### \[h2\]OH\_Drawing\_BitmapCreate()

OH\_Drawing\_Bitmap\* OH\_Drawing\_BitmapCreate(void)

**Description**

Creates an **OH\_Drawing\_Bitmap** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md)\* | Returns the pointer to the **OH\_Drawing\_Bitmap** object created. |

#### \[h2\]OH\_Drawing\_BitmapDestroy()

void OH\_Drawing\_BitmapDestroy(OH\_Drawing\_Bitmap\* bitmap)

**Description**

Destroys an **OH\_Drawing\_Bitmap** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md)\* bitmap | Pointer to an **OH\_Drawing\_Bitmap** object. |

#### \[h2\]OH\_Drawing\_BitmapCreateFromPixels()

OH\_Drawing\_Bitmap\* OH\_Drawing\_BitmapCreateFromPixels(OH\_Drawing\_Image\_Info\* imageInfo, void\* pixels, uint32\_t rowBytes)

**Description**

Creates an **OH\_Drawing\_Bitmap** object, with the address of the memory for storing the bitmap pixels set to the memory address that you applied for.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **imageInfo** or **pixels** is NULL or **rowBytes** is **0**, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Image\_Info](../../structs/oh-drawing-image-info/document.md)\* imageInfo | Pointer to an [OH\_Drawing\_Image\_Info](../../structs/oh-drawing-image-info/document.md) object. |
| void\* pixels | Pointer to the start address of the memory for storing the bitmap pixels. You need to apply for the memory and ensure its validity. |
| uint32\_t rowBytes | Number of bytes in each row of pixels. The value is invalid if it is less than or equal to 0. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md)\* | Returns a pointer to the [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md) object created. |

#### \[h2\]OH\_Drawing\_BitmapBuild()

void OH\_Drawing\_BitmapBuild(OH\_Drawing\_Bitmap\* bitmap,const uint32\_t width, const uint32\_t height, const OH\_Drawing\_BitmapFormat\* bitmapFormat)

**Description**

Initializes the width and height of a bitmap and sets the pixel format for the bitmap.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **bitmap** or **bitmapFormat** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md)\* bitmap | Pointer to an **OH\_Drawing\_Bitmap** object. |
| const uint32\_t width | Width of the bitmap to be initialized. |
| const uint32\_t height | Height of the bitmap to be initialized. |
| const [OH\_Drawing\_BitmapFormat](../../structs/oh-drawing-bitmapformat/document.md)\* bitmapFormat | Pointer to the pixel format of the bitmap to be initialized, including the pixel color type and alpha type. |

#### \[h2\]OH\_Drawing\_BitmapGetWidth()

uint32\_t OH\_Drawing\_BitmapGetWidth(OH\_Drawing\_Bitmap\* bitmap)

**Description**

Obtains the width of a bitmap.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md)\* bitmap | Pointer to an **OH\_Drawing\_Bitmap** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Returns the width. |

#### \[h2\]OH\_Drawing\_BitmapGetHeight()

uint32\_t OH\_Drawing\_BitmapGetHeight(OH\_Drawing\_Bitmap\* bitmap)

**Description**

Obtains the height of a bitmap.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md)\* bitmap | Pointer to an **OH\_Drawing\_Bitmap** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Returns the height. |

#### \[h2\]OH\_Drawing\_BitmapGetColorFormat()

OH\_Drawing\_ColorFormat OH\_Drawing\_BitmapGetColorFormat(OH\_Drawing\_Bitmap\* bitmap)

**Description**

Obtains the pixel format of a bitmap.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md)\* bitmap | Pointer to an **OH\_Drawing\_Bitmap** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ColorFormat](../drawing-types-h/document.md#oh_drawing_colorformat) | Returns the pixel format. For details about the supported formats, see [OH\_Drawing\_ColorFormat](../drawing-types-h/document.md#oh_drawing_colorformat). |

#### \[h2\]OH\_Drawing\_BitmapGetAlphaFormat()

OH\_Drawing\_AlphaFormat OH\_Drawing\_BitmapGetAlphaFormat(OH\_Drawing\_Bitmap\* bitmap)

**Description**

Obtains the alpha component of a bitmap.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md)\* bitmap | Pointer to an **OH\_Drawing\_Bitmap** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_AlphaFormat](../drawing-types-h/document.md#oh_drawing_alphaformat) | Returns the alpha component. For details about the supported formats, see [OH\_Drawing\_AlphaFormat](../drawing-types-h/document.md#oh_drawing_alphaformat). |

#### \[h2\]OH\_Drawing\_BitmapGetPixels()

void\* OH\_Drawing\_BitmapGetPixels(OH\_Drawing\_Bitmap\* bitmap)

**Description**

Obtains the pixel address of a bitmap. You can use this address to obtain the pixel data of the bitmap.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md)\* bitmap | Pointer to an **OH\_Drawing\_Bitmap** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| void\* | Returns the pixel address. |

#### \[h2\]OH\_Drawing\_BitmapGetImageInfo()

void OH\_Drawing\_BitmapGetImageInfo(OH\_Drawing\_Bitmap\* bitmap, OH\_Drawing\_Image\_Info\* imageInfo)

**Description**

Obtains the image information of a bitmap.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **bitmap** or **imageInfo** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md)\* bitmap | Pointer to the [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md) object. |
| [OH\_Drawing\_Image\_Info](../../structs/oh-drawing-image-info/document.md)\* imageInfo | Pointer to an [OH\_Drawing\_Image\_Info](../../structs/oh-drawing-image-info/document.md) object. |

#### \[h2\]OH\_Drawing\_BitmapReadPixels()

bool OH\_Drawing\_BitmapReadPixels(OH\_Drawing\_Bitmap\* bitmap, const OH\_Drawing\_Image\_Info\* dstInfo,void\* dstPixels, size\_t dstRowBytes, int32\_t srcX, int32\_t srcY)

**Description**

Reads pixels of a rectangle in a bitmap to the specified buffer.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **bitmap**, **dstInfo**, and **dstPixels** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md)\* bitmap | Pointer to the [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md) object. |
| const [OH\_Drawing\_Image\_Info](../../structs/oh-drawing-image-info/document.md)\* dstInfo | Pointer to an [OH\_Drawing\_Image\_Info](../../structs/oh-drawing-image-info/document.md) object. |
| void\* dstPixels | Pointer to the buffer for storing the pixels read. |
| size\_t dstRowBytes | Number of bytes in each row of the pixel data read. The value must be greater than or equal to the minimum number of bytes in each row in the **OH\_Drawing\_Image\_Info** object. |
| int32\_t srcX | Start X coordinate of the pixel data to read from the bitmap. The value must be less than the width of the bitmap. |
| int32\_t srcY | Start Y coordinate of the pixel data to read from the bitmap. The value must be less than the height of the bitmap. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the pixels are read; returns **false** otherwise. |
