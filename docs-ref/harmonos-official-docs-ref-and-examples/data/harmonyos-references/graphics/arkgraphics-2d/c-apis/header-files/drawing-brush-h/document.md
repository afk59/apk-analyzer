# drawing\_brush.h

#### Overview

This file declares the functions related to the brush in the drawing module.

**File to include**: <native\_drawing/drawing\_brush.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md) | OH\_NativeColorSpaceManager | Declares a color space manager object to provide the capability of obtaining basic color space attributes. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Brush\* OH\_Drawing\_BrushCreate(void)](#oh_drawing_brushcreate) | Creates an **OH\_Drawing\_Brush** object. |
| [OH\_Drawing\_Brush\* OH\_Drawing\_BrushCopy(OH\_Drawing\_Brush\* brush)](#oh_drawing_brushcopy) | 
Copies an existing [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object to create a new one.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_BrushDestroy(OH\_Drawing\_Brush\* brush)](#oh_drawing_brushdestroy) | Destroys an **OH\_Drawing\_Brush** object and reclaims the memory occupied by the object. |
| [bool OH\_Drawing\_BrushIsAntiAlias(const OH\_Drawing\_Brush\* brush)](#oh_drawing_brushisantialias) | 

Checks whether anti-aliasing is enabled for a brush. Anti-aliasing makes the pixels around the shape edges semi-transparent.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_BrushSetAntiAlias(OH\_Drawing\_Brush\* brush, bool antiAlias)](#oh_drawing_brushsetantialias) | 

Enables or disables anti-aliasing for a brush. Anti-aliasing makes the pixels around the shape edges semi-transparent.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [uint32\_t OH\_Drawing\_BrushGetColor(const OH\_Drawing\_Brush\* brush)](#oh_drawing_brushgetcolor) | 

Obtains the color of a brush. The color is used by the brush to fill in a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_BrushSetColor(OH\_Drawing\_Brush\* brush, uint32\_t color)](#oh_drawing_brushsetcolor) | 

Sets the color for a brush. The color is used by the brush to fill in a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [uint8\_t OH\_Drawing\_BrushGetAlpha(const OH\_Drawing\_Brush\* brush)](#oh_drawing_brushgetalpha) | 

Obtains the alpha value of a brush. This value is used by the alpha channel when the brush fills in a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_BrushSetAlpha(OH\_Drawing\_Brush\* brush, uint8\_t alpha)](#oh_drawing_brushsetalpha) | 

Sets the alpha value for a brush. This value is used by the alpha channel when the brush fills in a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_BrushSetShaderEffect(OH\_Drawing\_Brush\* brush, OH\_Drawing\_ShaderEffect\* shaderEffect)](#oh_drawing_brushsetshadereffect) | 

Sets the shader effect for a brush.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_BrushSetShadowLayer(OH\_Drawing\_Brush\* brush, OH\_Drawing\_ShadowLayer\* shadowLayer)](#oh_drawing_brushsetshadowlayer) | 

Sets the shadow layer for a brush. The shadow layer effect takes effect only when text is drawn.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_BrushSetFilter(OH\_Drawing\_Brush\* brush, OH\_Drawing\_Filter\* filter)](#oh_drawing_brushsetfilter) | 

Sets the filter [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md) for a brush. The filter is a container that holds a mask filter and color filter.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_BrushGetFilter(OH\_Drawing\_Brush\* brush, OH\_Drawing\_Filter\* filter)](#oh_drawing_brushgetfilter) | 

Obtains the [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md) object from the brush. The filter is a container that holds a mask filter and color filter.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **brush** or **filter** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_BrushSetBlendMode(OH\_Drawing\_Brush\* brush, OH\_Drawing\_BlendMode blendMode)](#oh_drawing_brushsetblendmode) | 

Sets a blender for a brush. The blender implements the specified blend mode.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **blendMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_BrushReset(OH\_Drawing\_Brush\* brush)](#oh_drawing_brushreset) | 

Resets a brush to the initial state. All configured attributes are cleared.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_BrushSetColor4f(OH\_Drawing\_Brush\* brush, float a, float r, float g, float b,OH\_NativeColorSpaceManager\* colorSpaceManager)](#oh_drawing_brushsetcolor4f) | 

Sets a color for this brush. The color will be used by the brush to fill in a shape.

The color is in ARGB format represented by floating-point numbers. The color space is specified by [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md).

If **colorSpaceManager** is a null pointer, the SRGB (standard red, green, and blue color space based on IEC 61966-2.1:1999) color space is used as the default value.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_BrushGetAlphaFloat(const OH\_Drawing\_Brush\* brush, float\* a)](#oh_drawing_brushgetalphafloat) | Obtains the alpha value of the brush color. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_BrushGetRedFloat(const OH\_Drawing\_Brush\* brush, float\* r)](#oh_drawing_brushgetredfloat) | Obtains the red component of the brush color. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_BrushGetGreenFloat(const OH\_Drawing\_Brush\* brush, float\* g)](#oh_drawing_brushgetgreenfloat) | Obtains the green component of the brush color. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_BrushGetBlueFloat(const OH\_Drawing\_Brush\* brush, float\* b)](#oh_drawing_brushgetbluefloat) | Obtains the blue component of the brush color. |

#### Function Description

#### \[h2\]OH\_Drawing\_BrushCreate()

OH\_Drawing\_Brush\* OH\_Drawing\_BrushCreate(void)

**Description**

Creates an **OH\_Drawing\_Brush** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* | Returns the pointer to the **OH\_Drawing\_Brush** object created. |

#### \[h2\]OH\_Drawing\_BrushCopy()

OH\_Drawing\_Brush\* OH\_Drawing\_BrushCopy(OH\_Drawing\_Brush\* brush)

**Description**

Copies an existing [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object to create a new one.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an **OH\_Drawing\_Brush** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* | Returns a pointer to the [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object created. If NULL is returned, the creation fails. The possible failure cause is that no memory is available or **brush** is NULL. |

#### \[h2\]OH\_Drawing\_BrushDestroy()

void OH\_Drawing\_BrushDestroy(OH\_Drawing\_Brush\* brush)

**Description**

Destroys an **OH\_Drawing\_Brush** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an **OH\_Drawing\_Brush** object. |

#### \[h2\]OH\_Drawing\_BrushIsAntiAlias()

bool OH\_Drawing\_BrushIsAntiAlias(const OH\_Drawing\_Brush\* brush)

**Description**

Checks whether anti-aliasing is enabled for a brush. Anti-aliasing makes the pixels around the shape edges semi-transparent.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an **OH\_Drawing\_Brush** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if anti-aliasing is enabled; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_BrushSetAntiAlias()

void OH\_Drawing\_BrushSetAntiAlias(OH\_Drawing\_Brush\* brush, bool antiAlias)

**Description**

Enables or disables anti-aliasing for a brush. Anti-aliasing makes the pixels around the shape edges semi-transparent.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an **OH\_Drawing\_Brush** object. |
| bool antiAlias | Whether to enable anti-aliasing. The value **true** means to enable anti-aliasing, and **false** means the opposite. |

#### \[h2\]OH\_Drawing\_BrushGetColor()

uint32\_t OH\_Drawing\_BrushGetColor(const OH\_Drawing\_Brush\* brush)

**Description**

Obtains the color of a brush. The color is used by the brush to fill in a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an **OH\_Drawing\_Brush** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Returns a 32-bit (ARGB) variable that describes the color. |

#### \[h2\]OH\_Drawing\_BrushSetColor()

void OH\_Drawing\_BrushSetColor(OH\_Drawing\_Brush\* brush, uint32\_t color)

**Description**

Sets the color for a brush. The color is used by the brush to fill in a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an **OH\_Drawing\_Brush** object. |
| uint32\_t color | Color, which is a 32-bit (ARGB) variable. |

#### \[h2\]OH\_Drawing\_BrushGetAlpha()

uint8\_t OH\_Drawing\_BrushGetAlpha(const OH\_Drawing\_Brush\* brush)

**Description**

Obtains the alpha value of a brush. This value is used by the alpha channel when the brush fills in a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an **OH\_Drawing\_Brush** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint8\_t | Returns an 8-bit variable that describes the alpha value. |

#### \[h2\]OH\_Drawing\_BrushSetAlpha()

void OH\_Drawing\_BrushSetAlpha(OH\_Drawing\_Brush\* brush, uint8\_t alpha)

**Description**

Sets the alpha value for a brush. This value is used by the alpha channel when the brush fills in a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an **OH\_Drawing\_Brush** object. |
| uint8\_t alpha | Alpha value, which is an 8-bit variable. |

#### \[h2\]OH\_Drawing\_BrushSetShaderEffect()

void OH\_Drawing\_BrushSetShaderEffect(OH\_Drawing\_Brush\* brush, OH\_Drawing\_ShaderEffect\* shaderEffect)

**Description**

Sets the shader effect for a brush.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an **OH\_Drawing\_Brush** object. |
| [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md)\* shaderEffect | Pointer to an **OH\_Drawing\_ShaderEffect** object. If NULL is passed in, the shader effect of the brush will be cleared. |

#### \[h2\]OH\_Drawing\_BrushSetShadowLayer()

void OH\_Drawing\_BrushSetShadowLayer(OH\_Drawing\_Brush\* brush, OH\_Drawing\_ShadowLayer\* shadowLayer)

**Description**

Sets the shadow layer for a brush. The shadow layer effect takes effect only when text is drawn.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an **OH\_Drawing\_Brush** object. |
| [OH\_Drawing\_ShadowLayer](../../structs/oh-drawing-shadowlayer/document.md)\* shadowLayer | Pointer to an **OH\_Drawing\_ShadowLayer** object. If NULL is passed in, the shadow layer effect of the brush will be cleared. |

#### \[h2\]OH\_Drawing\_BrushSetFilter()

void OH\_Drawing\_BrushSetFilter(OH\_Drawing\_Brush\* brush, OH\_Drawing\_Filter\* filter)

**Description**

Sets the filter [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md) for a brush. The filter is a container that holds a mask filter and color filter.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an **OH\_Drawing\_Brush** object. |
| [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md)\* filter | Pointer to an **OH\_Drawing\_Filter** object. If null is passed in, the filter will be cleared. |

#### \[h2\]OH\_Drawing\_BrushGetFilter()

void OH\_Drawing\_BrushGetFilter(OH\_Drawing\_Brush\* brush, OH\_Drawing\_Filter\* filter)

**Description**

Obtains the [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md) object from the brush. The filter is a container that holds a mask filter and color filter.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **brush** or **filter** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to the [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object. |
| [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md)\* filter | Pointer to an [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md) object. |

#### \[h2\]OH\_Drawing\_BrushSetBlendMode()

void OH\_Drawing\_BrushSetBlendMode(OH\_Drawing\_Brush\* brush, OH\_Drawing\_BlendMode blendMode)

**Description**

Sets a blender for a brush. The blender implements the specified blend mode.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **blendMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to the [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object. |
| [OH\_Drawing\_BlendMode](../drawing-types-h/document.md#oh_drawing_blendmode) blendMode | Enumeration of blend modes. |

#### \[h2\]OH\_Drawing\_BrushReset()

void OH\_Drawing\_BrushReset(OH\_Drawing\_Brush\* brush)

**Description**

Resets a brush to the initial state. All configured attributes are cleared.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to the [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object. |

#### \[h2\]OH\_Drawing\_BrushSetColor4f()

OH\_Drawing\_ErrorCode OH\_Drawing\_BrushSetColor4f(OH\_Drawing\_Brush\* brush, float a, float r, float g, float b,OH\_NativeColorSpaceManager\* colorSpaceManager)

**Description**

Sets a color for this brush. The color will be used by the brush to fill in a shape.

The color is in ARGB format represented by floating-point numbers. The color space is specified by [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md).

If **colorSpaceManager** is a null pointer, the SRGB (standard red, green, and blue color space based on IEC 61966-2.1:1999) color space is used as the default value.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Drawing\_Brush\* brush | Pointer to an [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object. |
| float a | Alpha value of the color, which is a floating-point number ranging from 0.0 to 1.0. Values above 1.0 default to 1.0, while values below 0.0 default to 0.0. |
| float r | Red component of the color, which is a floating-point number ranging from 0.0 to 1.0. Values above 1.0 default to 1.0, while values below 0.0 default to 0.0. |
| float g | Green component of the color, which is a floating-point number ranging from 0.0 to 1.0. Values above 1.0 default to 1.0, while values below 0.0 default to 0.0. |
| float b | Blue component of the color, which is a floating-point number ranging from 0.0 to 1.0. Values above 1.0 default to 1.0, while values below 0.0 default to 0.0. |
| [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md)\* colorSpaceManager | Pointer to an [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **brush** is NULL.

 |

#### \[h2\]OH\_Drawing\_BrushGetAlphaFloat()

OH\_Drawing\_ErrorCode OH\_Drawing\_BrushGetAlphaFloat(const OH\_Drawing\_Brush\* brush, float\* a)

**Description**

Obtains the alpha value of the brush color.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object. |
| float\* a | Alpha value of the color. The value is a floating-point number ranging from 0.0 to 1.0. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **brush** or **a** is NULL.

 |

#### \[h2\]OH\_Drawing\_BrushGetRedFloat()

OH\_Drawing\_ErrorCode OH\_Drawing\_BrushGetRedFloat(const OH\_Drawing\_Brush\* brush, float\* r)

**Description**

Obtains the red component of the brush color.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object. |
| float\* r | Red component of the pen color. The value is a floating-point number ranging from 0.0 to 1.0. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **brush** or **r** is NULL.

 |

#### \[h2\]OH\_Drawing\_BrushGetGreenFloat()

OH\_Drawing\_ErrorCode OH\_Drawing\_BrushGetGreenFloat(const OH\_Drawing\_Brush\* brush, float\* g)

**Description**

Obtains the green component of the brush color.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object. |
| float\* g | Green component of the pen color. The value is a floating-point number ranging from 0.0 to 1.0. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **brush** or **g** is NULL.

 |

#### \[h2\]OH\_Drawing\_BrushGetBlueFloat()

OH\_Drawing\_ErrorCode OH\_Drawing\_BrushGetBlueFloat(const OH\_Drawing\_Brush\* brush, float\* b)

**Description**

Obtains the blue component of the brush color.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object. |
| float\* b | Blue component of the pen color. The value is a floating-point number ranging from 0.0 to 1.0. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **brush** or **b** is NULL.

 |
