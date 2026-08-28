# drawing\_image\_filter.h

#### Overview

This file declares the functions related to the image filter in the drawing module.

**File to include**: <native\_drawing/drawing\_image\_filter.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_ImageFilter\* OH\_Drawing\_ImageFilterCreateBlur(float sigmaX, float sigmaY, OH\_Drawing\_TileMode tileMode,OH\_Drawing\_ImageFilter\* imageFilter)](#oh_drawing_imagefiltercreateblur) | Creates an image filter with a given blur effect. |
| [OH\_Drawing\_ImageFilter\* OH\_Drawing\_ImageFilterCreateBlurWithCrop(float sigmaX, float sigmaY,OH\_Drawing\_TileMode tileMode, OH\_Drawing\_ImageFilter\* input, const OH\_Drawing\_Rect\* rect)](#oh_drawing_imagefiltercreateblurwithcrop) | 
Creates an image filter with a given blur effect.

You can pass a cropping rectangle to limit the blur effect to take effect only in the specified rectangular area of the image.​

 |
| [OH\_Drawing\_ImageFilter\* OH\_Drawing\_ImageFilterCreateFromColorFilter(OH\_Drawing\_ColorFilter\* colorFilter,OH\_Drawing\_ImageFilter\* imageFilter)](#oh_drawing_imagefiltercreatefromcolorfilter) | Creates an **OH\_Drawing\_ImageFilter** object with a color filter effect. This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget). If **colorFilter** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned. |
| [OH\_Drawing\_ImageFilter\* OH\_Drawing\_ImageFilterCreateOffset(float x, float y, OH\_Drawing\_ImageFilter\* imageFilter)](#oh_drawing_imagefiltercreateoffset) | Creates an offset filter to translate the input filter based on the specified vector. |
| [OH\_Drawing\_ImageFilter\* OH\_Drawing\_ImageFilterCreateFromShaderEffect(OH\_Drawing\_ShaderEffect\* shaderEffect)](#oh_drawing_imagefiltercreatefromshadereffect) | Creates an **ImageFilter** object based on a shader. |
| [void OH\_Drawing\_ImageFilterDestroy(OH\_Drawing\_ImageFilter\* imageFilter)](#oh_drawing_imagefilterdestroy) | Destroys an **OH\_Drawing\_ImageFilter** object and reclaims the memory occupied by the object. |

#### Function Description

#### \[h2\]OH\_Drawing\_ImageFilterCreateBlur()

OH\_Drawing\_ImageFilter\* OH\_Drawing\_ImageFilterCreateBlur(float sigmaX, float sigmaY, OH\_Drawing\_TileMode tileMode,OH\_Drawing\_ImageFilter\* imageFilter)

**Description**

Creates an image filter with a given blur effect.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| float sigmaX | Standard deviation of the Gaussian blur to apply along the X axis. The value must be greater than 0. |
| float sigmaY | Standard deviation of the Gaussian blur to apply along the Y axis. The value must be greater than 0. |
| [OH\_Drawing\_TileMode](../drawing-shader-effect-h/document.md#oh_drawing_tilemode) tileMode | Tile mode of the shader effect. For details about the available options, see [OH\_Drawing\_TileMode](../drawing-shader-effect-h/document.md#oh_drawing_tilemode). |
| [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md)\* imageFilter | Pointer to the filter to which the image filter will be applied. If NULL is passed in, the image filter is directly applied to the original image. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md)\* | Returns the pointer to the [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md) object created. If NULL is returned, the creation fails. The possible failure cause is that no memory is available. |

#### \[h2\]OH\_Drawing\_ImageFilterCreateBlurWithCrop()

OH\_Drawing\_ImageFilter\* OH\_Drawing\_ImageFilterCreateBlurWithCrop(float sigmaX, float sigmaY, OH\_Drawing\_TileMode tileMode, OH\_Drawing\_ImageFilter\* input, const OH\_Drawing\_Rect\* rect)

**Description**

Creates an image filter with a given blur effect.

You can pass a cropping rectangle to limit the blur effect to take effect only in the specified rectangular area of the image.​

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| float sigmaX | Standard deviation of the Gaussian blur to apply along the X axis. The value must be greater than 0.0. |
| float sigmaY | Standard deviation of the Gaussian blur to apply along the Y axis. The value must be greater than 0.0. |
| [OH\_Drawing\_TileMode](../drawing-shader-effect-h/document.md#oh_drawing_tilemode) tileMode | Tile mode of the shader effect. For details about the available options, see [OH\_Drawing\_TileMode](../drawing-shader-effect-h/document.md#oh_drawing_tilemode). |
| [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md)\* input | Pointer to the filter to which the image filter will be applied. If NULL is passed in, the image filter is directly applied to the original image. |
| [const OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to the rectangular region to be cropped. If NULL is passed in, the blur effect is directly applied to the entire image. |

**Return value**

| Type | Description |
| :-- | :-- |
| OH\_Drawing\_ImageFilter\* | Returns the pointer to the [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md) object created. If NULL is returned, the creation fails. The possible failure cause is that no memory is available. |

#### \[h2\]OH\_Drawing\_ImageFilterCreateFromColorFilter()

OH\_Drawing\_ImageFilter\* OH\_Drawing\_ImageFilterCreateFromColorFilter(OH\_Drawing\_ColorFilter\* colorFilter,OH\_Drawing\_ImageFilter\* imageFilter)

**Description**

Creates an **OH\_Drawing\_ImageFilter** object with a color filter effect. This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget). If **colorFilter** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_ColorFilter](../../structs/oh-drawing-colorfilter/document.md)\* colorFilter | Pointer to an [OH\_Drawing\_ColorFilter](../../structs/oh-drawing-colorfilter/document.md) object. |
| [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md)\* imageFilter | Pointer to the filter to which the image filter will be applied. If NULL is passed in, the image filter is directly applied to the original image. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md)\* | Returns the pointer to the [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md) object created. If NULL is returned, the creation fails. The possible failure cause is that no memory is available or **colorFilter** is NULL. |

#### \[h2\]OH\_Drawing\_ImageFilterCreateOffset()

OH\_Drawing\_ImageFilter\* OH\_Drawing\_ImageFilterCreateOffset(float x, float y, OH\_Drawing\_ImageFilter\* imageFilter)

**Description**

Creates an offset filter to translate the input filter based on the specified vector.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| float x | Distance to translate on the X axis. |
| float y | Distance to translate on the Y axis. |
| [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md)\* imageFilter | Filter to be translated. If NULL is passed in, the drawing result without the filtering effect is translated. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md)\* | Returns the pointer to the [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md) object created. If NULL is returned, the creation fails. The possible failure cause is that no memory is available. |

#### \[h2\]OH\_Drawing\_ImageFilterCreateFromShaderEffect()

OH\_Drawing\_ImageFilter\* OH\_Drawing\_ImageFilterCreateFromShaderEffect(OH\_Drawing\_ShaderEffect\* shaderEffect)

**Description**

Creates an **ImageFilter** object based on a shader.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md)\* shaderEffect | Shader effect to be applied to the image. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md)\* | Returns the pointer to the [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md) object created. If NULL is returned, the creation fails. The possible failure cause is that no memory is available. |

#### \[h2\]OH\_Drawing\_ImageFilterDestroy()

void OH\_Drawing\_ImageFilterDestroy(OH\_Drawing\_ImageFilter\* imageFilter)

**Description**

Destroys an **OH\_Drawing\_ImageFilter** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md)\* imageFilter | Pointer to an [OH\_Drawing\_ImageFilter](../../structs/oh-drawing-imagefilter/document.md) object. |
