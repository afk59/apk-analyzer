# drawing\_image.h

#### Overview

This file declares the functions related to the image in the drawing module.

**File to include**: <native\_drawing/drawing\_image.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Image\* OH\_Drawing\_ImageCreate(void)](#oh_drawing_imagecreate) | Creates an **OH\_Drawing\_Image** object that describes an array of two-dimensional pixels to draw. |
| [void OH\_Drawing\_ImageDestroy(OH\_Drawing\_Image\* image)](#oh_drawing_imagedestroy) | Destroys an **OH\_Drawing\_Image** object and reclaims the memory occupied by the object. |
| [bool OH\_Drawing\_ImageBuildFromBitmap(OH\_Drawing\_Image\* image, OH\_Drawing\_Bitmap\* bitmap)](#oh_drawing_imagebuildfrombitmap) | 
Builds an image from a bitmap by sharing or copying bitmap pixels. If the bitmap is marked as immutable, the pixel memory is shared, not copied.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **image** or **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [int32\_t OH\_Drawing\_ImageGetWidth(OH\_Drawing\_Image\* image)](#oh_drawing_imagegetwidth) | 

Obtains the image width, that is, the number of pixels in each line.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **image** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [int32\_t OH\_Drawing\_ImageGetHeight(OH\_Drawing\_Image\* image)](#oh_drawing_imagegetheight) | 

Obtains the image height, that is, the number of pixel lines.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **image** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_ImageGetImageInfo(OH\_Drawing\_Image\* image, OH\_Drawing\_Image\_Info\* imageInfo)](#oh_drawing_imagegetimageinfo) | 

Obtains the image information. After this function is called, the passed-in image information object is filled.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **image** or **imageInfo** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |

#### Function Description

#### \[h2\]OH\_Drawing\_ImageCreate()

OH\_Drawing\_Image\* OH\_Drawing\_ImageCreate(void)

**Description**

Creates an **OH\_Drawing\_Image** object that describes an array of two-dimensional pixels to draw.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md)\* | Returns a pointer to the [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md) object created. |

#### \[h2\]OH\_Drawing\_ImageDestroy()

void OH\_Drawing\_ImageDestroy(OH\_Drawing\_Image\* image)

**Description**

Destroys an **OH\_Drawing\_Image** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md)\* image | Pointer to the [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md) object. |

#### \[h2\]OH\_Drawing\_ImageBuildFromBitmap()

bool OH\_Drawing\_ImageBuildFromBitmap(OH\_Drawing\_Image\* image, OH\_Drawing\_Bitmap\* bitmap)

**Description**

Builds an image from a bitmap by sharing or copying bitmap pixels. If the bitmap is marked as immutable, the pixel memory is shared, not copied.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **image** or **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md)\* image | Pointer to the [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md) object. |
| [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md)\* bitmap | Pointer to the [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the image is built; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_ImageGetWidth()

int32\_t OH\_Drawing\_ImageGetWidth(OH\_Drawing\_Image\* image)

**Description**

Obtains the image width, that is, the number of pixels in each line.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **image** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md)\* image | Pointer to the [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns the width. |

#### \[h2\]OH\_Drawing\_ImageGetHeight()

int32\_t OH\_Drawing\_ImageGetHeight(OH\_Drawing\_Image\* image)

**Description**

Obtains the image height, that is, the number of pixel lines.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **image** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md)\* image | Pointer to the [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns the height. |

#### \[h2\]OH\_Drawing\_ImageGetImageInfo()

void OH\_Drawing\_ImageGetImageInfo(OH\_Drawing\_Image\* image, OH\_Drawing\_Image\_Info\* imageInfo)

**Description**

Obtains the image information. After this function is called, the passed-in image information object is filled.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **image** or **imageInfo** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md)\* image | Pointer to the [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md) object. |
| [OH\_Drawing\_Image\_Info](../../structs/oh-drawing-image-info/document.md)\* imageInfo | Pointer to an [OH\_Drawing\_Image\_Info](../../structs/oh-drawing-image-info/document.md) object, which can be created by calling [OH\_Drawing\_Image\_Info](../../structs/oh-drawing-image-info/document.md). |
