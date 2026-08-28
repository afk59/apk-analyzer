# drawing\_color\_filter.h

#### Overview

This file declares the functions related to the color filter in the drawing module.

**File to include**: <native\_drawing/drawing\_color\_filter.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateBlendMode(uint32\_t color, OH\_Drawing\_BlendMode blendMode)](#oh_drawing_colorfiltercreateblendmode) | Creates an **OH\_Drawing\_ColorFilter** object with a given blend mode. |
| [OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateCompose(OH\_Drawing\_ColorFilter\* outerColorFilter,OH\_Drawing\_ColorFilter\* innerColorFilter)](#oh_drawing_colorfiltercreatecompose) | 
Creates an **OH\_Drawing\_ColorFilter** object by combining another two color filters.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **outerColorFilter** or **innerColorFilter** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateMatrix(const float matrix\[20\])](#oh_drawing_colorfiltercreatematrix) | 

Creates an **OH\_Drawing\_ColorFilter** object with a given 5x4 color matrix.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateLinearToSrgbGamma(void)](#oh_drawing_colorfiltercreatelineartosrgbgamma) | Creates an **OH\_Drawing\_ColorFilter** object that applies the sRGB gamma curve to the RGB channels. |
| [OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateSrgbGammaToLinear(void)](#oh_drawing_colorfiltercreatesrgbgammatolinear) | Creates an **OH\_Drawing\_ColorFilter** object that applies the RGB channels to the sRGB gamma curve. |
| [OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateLuma(void)](#oh_drawing_colorfiltercreateluma) | Creates a **ColorFilter** object that multiplies the luma into the alpha channel and sets the RGB channels to zero. |
| [OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateLighting(uint32\_t mulColor, uint32\_t addColor)](#oh_drawing_colorfiltercreatelighting) | Creates a lighting color filter. It multiplies the RGB channel values by one color and then adds another color value. The final output stays between 0 and 255. |
| [void OH\_Drawing\_ColorFilterDestroy(OH\_Drawing\_ColorFilter\* colorFilter)](#oh_drawing_colorfilterdestroy) | Destroys an **OH\_Drawing\_ColorFilter** object and reclaims the memory occupied by the object. |

#### Function Description

#### \[h2\]OH\_Drawing\_ColorFilterCreateBlendMode()

OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateBlendMode(uint32\_t color, OH\_Drawing\_BlendMode blendMode)

**Description**

Creates an **OH\_Drawing\_ColorFilter** object with a given blend mode.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| uint32\_t color | Color, which is a 32-bit (ARGB) variable. |
| [OH\_Drawing\_BlendMode](../drawing-types-h/document.md#oh_drawing_blendmode) blendMode | Blend mode. For details about the available options, see [OH\_Drawing\_BlendMode](../drawing-types-h/document.md#oh_drawing_blendmode). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ColorFilter](../../structs/oh-drawing-colorfilter/document.md)\* | Returns the pointer to the **OH\_Drawing\_ColorFilter** object created. |

#### \[h2\]OH\_Drawing\_ColorFilterCreateCompose()

OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateCompose(OH\_Drawing\_ColorFilter\* outerColorFilter,OH\_Drawing\_ColorFilter\* innerColorFilter)

**Description**

Creates an **OH\_Drawing\_ColorFilter** object by combining another two color filters.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **outerColorFilter** or **innerColorFilter** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_ColorFilter](../../structs/oh-drawing-colorfilter/document.md)\* outerColorFilter | Pointer to the first color filter. |
| [OH\_Drawing\_ColorFilter](../../structs/oh-drawing-colorfilter/document.md)\* innerColorFilter | Pointer to the second color filter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ColorFilter](../../structs/oh-drawing-colorfilter/document.md)\* | Returns the pointer to the **OH\_Drawing\_ColorFilter** object created. |

#### \[h2\]OH\_Drawing\_ColorFilterCreateMatrix()

OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateMatrix(const float matrix\[20\])

**Description**

Creates an **OH\_Drawing\_ColorFilter** object with a given 5x4 color matrix.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| matrix | Matrix, which is represented by a floating-point array with a length of 20. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ColorFilter](../../structs/oh-drawing-colorfilter/document.md)\* | Returns the pointer to the **OH\_Drawing\_ColorFilter** object created. |

#### \[h2\]OH\_Drawing\_ColorFilterCreateLinearToSrgbGamma()

OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateLinearToSrgbGamma(void)

**Description**

Creates an **OH\_Drawing\_ColorFilter** object that applies the sRGB gamma curve to the RGB channels.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ColorFilter](../../structs/oh-drawing-colorfilter/document.md)\* | Returns the pointer to the **OH\_Drawing\_ColorFilter** object created. |

#### \[h2\]OH\_Drawing\_ColorFilterCreateSrgbGammaToLinear()

OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateSrgbGammaToLinear(void)

**Description**

Creates an **OH\_Drawing\_ColorFilter** object that applies the RGB channels to the sRGB gamma curve.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ColorFilter](../../structs/oh-drawing-colorfilter/document.md)\* | Returns the pointer to the **OH\_Drawing\_ColorFilter** object created. |

#### \[h2\]OH\_Drawing\_ColorFilterCreateLuma()

OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateLuma(void)

**Description**

Creates a **ColorFilter** object that multiplies the luma into the alpha channel and sets the RGB channels to zero.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ColorFilter](../../structs/oh-drawing-colorfilter/document.md)\* | Returns the pointer to the **OH\_Drawing\_ColorFilter** object created. |

#### \[h2\]OH\_Drawing\_ColorFilterCreateLighting()

OH\_Drawing\_ColorFilter\* OH\_Drawing\_ColorFilterCreateLighting(uint32\_t mulColor, uint32\_t addColor)

**Description**

Creates a lighting color filter. It multiplies the RGB channel values by one color and then adds another color value. The final output stays between 0 and 255.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| uint32\_t mulColor | Color value used for multiplication. |
| uint32\_t addColor | Color value used for addition. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ColorFilter](../../structs/oh-drawing-colorfilter/document.md)\* | Returns the pointer to the **OH\_Drawing\_ColorFilter** object created. |

#### \[h2\]OH\_Drawing\_ColorFilterDestroy()

void OH\_Drawing\_ColorFilterDestroy(OH\_Drawing\_ColorFilter\* colorFilter)

**Description**

Destroys an **OH\_Drawing\_ColorFilter** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_ColorFilter](../../structs/oh-drawing-colorfilter/document.md)\* colorFilter | Pointer to an **OH\_Drawing\_ColorFilter** object. |
