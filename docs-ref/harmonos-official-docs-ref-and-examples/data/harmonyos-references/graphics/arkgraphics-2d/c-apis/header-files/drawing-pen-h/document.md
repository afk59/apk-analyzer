# drawing\_pen.h

#### Overview

This file declares functions related to the pen in the drawing module.

**File to include**: <native\_drawing/drawing\_pen.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md) | OH\_NativeColorSpaceManager | Declares a color space manager object to provide the capability of obtaining basic color space attributes. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_PenLineCapStyle](#oh_drawing_penlinecapstyle) | OH\_Drawing\_PenLineCapStyle | Defines an enum for the line cap styles of a pen. The line cap style defines the style of both ends of a line segment drawn by the pen. |
| [OH\_Drawing\_PenLineJoinStyle](#oh_drawing_penlinejoinstyle) | OH\_Drawing\_PenLineJoinStyle | Enumerates the line join styles of a pen. The line join style defines the shape of the joints of a polyline segment drawn by the pen. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen\* OH\_Drawing\_PenCreate(void)](#oh_drawing_pencreate) | Creates an **OH\_Drawing\_Pen** object. |
| [OH\_Drawing\_Pen\* OH\_Drawing\_PenCopy(OH\_Drawing\_Pen\* pen)](#oh_drawing_pencopy) | 
Creates a copy of the [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PenDestroy(OH\_Drawing\_Pen\* pen)](#oh_drawing_pendestroy) | Destroys an **OH\_Drawing\_Pen** object and reclaims the memory occupied by the object. |
| [bool OH\_Drawing\_PenIsAntiAlias(const OH\_Drawing\_Pen\* pen)](#oh_drawing_penisantialias) | 

Checks whether anti-aliasing is enabled for a pen. Anti-aliasing makes the pixels around the shape edges semi-transparent.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PenSetAntiAlias(OH\_Drawing\_Pen\* pen, bool antiAlias)](#oh_drawing_pensetantialias) | 

Enables or disables anti-aliasing for a pen. Anti-aliasing makes the pixels around the shape edges semi-transparent.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [uint32\_t OH\_Drawing\_PenGetColor(const OH\_Drawing\_Pen\* pen)](#oh_drawing_pengetcolor) | 

Obtains the color of a pen. The color is used by the pen to outline a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PenSetColor(OH\_Drawing\_Pen\* pen, uint32\_t color)](#oh_drawing_pensetcolor) | 

Sets the color for a pen. The color is used by the pen to outline a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [uint8\_t OH\_Drawing\_PenGetAlpha(const OH\_Drawing\_Pen\* pen)](#oh_drawing_pengetalpha) | 

Obtains the alpha value of a pen. This value is used by the alpha channel when the pen outlines a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PenSetAlpha(OH\_Drawing\_Pen\* pen, uint8\_t alpha)](#oh_drawing_pensetalpha) | 

Sets the alpha value for a pen. This value is used by the alpha channel when the pen outlines a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [float OH\_Drawing\_PenGetWidth(const OH\_Drawing\_Pen\* pen)](#oh_drawing_pengetwidth) | 

Obtains the thickness of a pen. This thickness determines the width of the outline of a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PenSetWidth(OH\_Drawing\_Pen\* pen, float width)](#oh_drawing_pensetwidth) | 

Sets the thickness for a pen. This thickness determines the width of the outline of a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [float OH\_Drawing\_PenGetMiterLimit(const OH\_Drawing\_Pen\* pen)](#oh_drawing_pengetmiterlimit) | 

Obtains the stroke miter limit of a polyline drawn by a pen. When the corner type is bevel, a beveled corner is displayed if the miter limit is exceeded, and a mitered corner is displayed if the miter limit is not exceeded.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PenSetMiterLimit(OH\_Drawing\_Pen\* pen, float miter)](#oh_drawing_pensetmiterlimit) | 

Sets the stroke miter limit for a polyline drawn by a pen. When the corner type is bevel, a beveled corner is displayed if the miter limit is exceeded, and a mitered corner is displayed if the miter limit is not exceeded.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_PenLineCapStyle OH\_Drawing\_PenGetCap(const OH\_Drawing\_Pen\* pen)](#oh_drawing_pengetcap) | 

Obtains the line cap style of a pen.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PenSetCap(OH\_Drawing\_Pen\* pen, OH\_Drawing\_PenLineCapStyle capStyle)](#oh_drawing_pensetcap) | 

Sets the line cap style for a pen.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **capStyle** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [OH\_Drawing\_PenLineJoinStyle OH\_Drawing\_PenGetJoin(const OH\_Drawing\_Pen\* pen)](#oh_drawing_pengetjoin) | 

Obtains the line join style of a pen.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PenSetJoin(OH\_Drawing\_Pen\* pen, OH\_Drawing\_PenLineJoinStyle joinStyle)](#oh_drawing_pensetjoin) | 

Sets the join style for this pen.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **joinStyle** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_PenSetShaderEffect(OH\_Drawing\_Pen\* pen, OH\_Drawing\_ShaderEffect\* shaderEffect)](#oh_drawing_pensetshadereffect) | 

Sets the shader effect for this pen.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PenSetShadowLayer(OH\_Drawing\_Pen\* pen, OH\_Drawing\_ShadowLayer\* shadowLayer)](#oh_drawing_pensetshadowlayer) | 

Sets the shadow layer for a pen. The shadow layer effect takes effect only when text is drawn.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PenSetPathEffect(OH\_Drawing\_Pen\* pen, OH\_Drawing\_PathEffect\* pathEffect)](#oh_drawing_pensetpatheffect) | 

Sets the path effect for this pen.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PenSetFilter(OH\_Drawing\_Pen\* pen, OH\_Drawing\_Filter\* filter)](#oh_drawing_pensetfilter) | 

Sets a filter for a pen.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PenGetFilter(OH\_Drawing\_Pen\* pen, OH\_Drawing\_Filter\* filter)](#oh_drawing_pengetfilter) | 

Obtains the [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md) object from the pen. The filter is a container that holds a mask filter and color filter.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **pen** or **filter** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PenSetBlendMode(OH\_Drawing\_Pen\* pen, OH\_Drawing\_BlendMode blendMode)](#oh_drawing_pensetblendmode) | 

Sets a blender for a pen. The blender implements the specified blend mode.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **blendMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [bool OH\_Drawing\_PenGetFillPath(OH\_Drawing\_Pen\* pen, const OH\_Drawing\_Path\* src, OH\_Drawing\_Path\* dst,const OH\_Drawing\_Rect\* rect, const OH\_Drawing\_Matrix\* matrix)](#oh_drawing_pengetfillpath) | 

Obtains the source path outline drawn using this pen and represents it using a destination path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **pen**, **src**, and **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PenReset(OH\_Drawing\_Pen\* pen)](#oh_drawing_penreset) | 

Resets a pen to the initial state.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PenSetColor4f(OH\_Drawing\_Pen\* pen, float a, float r, float g, float b,OH\_NativeColorSpaceManager\* colorSpaceManager)](#oh_drawing_pensetcolor4f) | 

Sets the color for a pen, which is used to outline a shape.

The color is in ARGB format represented by floating-point numbers. The color space is specified by [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md).

If **colorSpaceManager** is a null pointer, the SRGB (standard red, green, and blue color space based on IEC 61966-2.1:1999) color space is used as the default value.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PenGetAlphaFloat(OH\_Drawing\_Pen\* pen, float\* a)](#oh_drawing_pengetalphafloat) | Obtains the alpha value of the pen color. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PenGetRedFloat(OH\_Drawing\_Pen\* pen, float\* r)](#oh_drawing_pengetredfloat) | Obtains the red component of the pen color. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PenGetGreenFloat(OH\_Drawing\_Pen\* pen, float\* g)](#oh_drawing_pengetgreenfloat) | Obtains the green component of the pen color. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PenGetBlueFloat(OH\_Drawing\_Pen\* pen, float\* b)](#oh_drawing_pengetbluefloat) | Obtains the blue component of the pen color. |

#### Enum Description

#### \[h2\]OH\_Drawing\_PenLineCapStyle

enum OH\_Drawing\_PenLineCapStyle

**Description**

Enumerates the line cap styles of a pen. The line cap style defines the style of both ends of a line segment drawn by the pen.

**Since**: 8

| Enum | Description |
| :-- | :-- |
| LINE\_FLAT\_CAP | There is no cap style. Both ends of the line segment are cut off square. |
| LINE\_SQUARE\_CAP | Square cap style. Both ends have a square, the height of which is half of the width of the line segment, with the same width. |
| LINE\_ROUND\_CAP | Round cap style. Both ends have a semicircle centered, the diameter of which is the same as the width of the line segment. |

#### \[h2\]OH\_Drawing\_PenLineJoinStyle

enum OH\_Drawing\_PenLineJoinStyle

**Description**

Enumerates the line join styles of a pen. The line join style defines the shape of the joints of a polyline segment drawn by the pen.

**Since**: 8

| Enum | Description |
| :-- | :-- |
| LINE\_MITER\_JOIN | Mitered corner. If the angle of a polyline is small, its miter length may be inappropriate. In this case, you need to use the miter limit to limit the miter length. |
| LINE\_ROUND\_JOIN | Round corner. |
| LINE\_BEVEL\_JOIN | Beveled corner. |

#### Function Description

#### \[h2\]OH\_Drawing\_PenCreate()

OH\_Drawing\_Pen\* OH\_Drawing\_PenCreate(void)

**Description**

Creates an **OH\_Drawing\_Pen** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* | Returns the pointer to the **OH\_Drawing\_Pen** object created. |

#### \[h2\]OH\_Drawing\_PenCopy()

OH\_Drawing\_Pen\* OH\_Drawing\_PenCopy(OH\_Drawing\_Pen\* pen)

**Description**

Creates a copy of the [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an **OH\_Drawing\_Pen** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* | Returns the pointer to the [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object created. If NULL is returned, the creation fails. The possible failure cause is that no memory is available or **pen** is NULL. |

#### \[h2\]OH\_Drawing\_PenDestroy()

void OH\_Drawing\_PenDestroy(OH\_Drawing\_Pen\* pen)

**Description**

Destroys an **OH\_Drawing\_Pen** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an **OH\_Drawing\_Pen** object. |

#### \[h2\]OH\_Drawing\_PenIsAntiAlias()

bool OH\_Drawing\_PenIsAntiAlias(const OH\_Drawing\_Pen\* pen)

**Description**

Checks whether anti-aliasing is enabled for a pen. Anti-aliasing makes the pixels around the shape edges semi-transparent.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an **OH\_Drawing\_Pen** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if anti-aliasing is enabled; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_PenSetAntiAlias()

void OH\_Drawing\_PenSetAntiAlias(OH\_Drawing\_Pen\* pen, bool antiAlias)

**Description**

Enables or disables anti-aliasing for a pen. Anti-aliasing makes the pixels around the shape edges semi-transparent.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an **OH\_Drawing\_Pen** object. |
| bool antiAlias | Whether to enable anti-aliasing. The value **true** means to enable anti-aliasing, and **false** means the opposite. |

#### \[h2\]OH\_Drawing\_PenGetColor()

uint32\_t OH\_Drawing\_PenGetColor(const OH\_Drawing\_Pen\* pen)

**Description**

Obtains the color of a pen. The color is used by the pen to outline a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an **OH\_Drawing\_Pen** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Returns a 32-bit (ARGB) variable that describes the color. |

#### \[h2\]OH\_Drawing\_PenSetColor()

void OH\_Drawing\_PenSetColor(OH\_Drawing\_Pen\* pen, uint32\_t color)

**Description**

Sets the color for a pen. The color is used by the pen to outline a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an **OH\_Drawing\_Pen** object. |
| uint32\_t color | Color, which is a 32-bit (ARGB) variable. |

#### \[h2\]OH\_Drawing\_PenGetAlpha()

uint8\_t OH\_Drawing\_PenGetAlpha(const OH\_Drawing\_Pen\* pen)

**Description**

Obtains the alpha value of a pen. This value is used by the alpha channel when the pen outlines a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an **OH\_Drawing\_Pen** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint8\_t | Returns an 8-bit variable that describes the alpha value. |

#### \[h2\]OH\_Drawing\_PenSetAlpha()

void OH\_Drawing\_PenSetAlpha(OH\_Drawing\_Pen\* pen, uint8\_t alpha)

**Description**

Sets the alpha value for a pen. This value is used by the alpha channel when the pen outlines a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an **OH\_Drawing\_Pen** object. |
| uint8\_t alpha | Alpha value, which is an 8-bit variable. |

#### \[h2\]OH\_Drawing\_PenGetWidth()

float OH\_Drawing\_PenGetWidth(const OH\_Drawing\_Pen\* pen)

**Description**

Obtains the thickness of a pen. This thickness determines the width of the outline of a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an **OH\_Drawing\_Pen** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Returns the thickness. |

#### \[h2\]OH\_Drawing\_PenSetWidth()

void OH\_Drawing\_PenSetWidth(OH\_Drawing\_Pen\* pen, float width)

**Description**

Sets the thickness for a pen. This thickness determines the width of the outline of a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an **OH\_Drawing\_Pen** object. |
| float width | Thickness, which is a variable. |

#### \[h2\]OH\_Drawing\_PenGetMiterLimit()

float OH\_Drawing\_PenGetMiterLimit(const OH\_Drawing\_Pen\* pen)

**Description**

Obtains the stroke miter limit of a polyline drawn by a pen. When the corner type is bevel, a beveled corner is displayed if the miter limit is exceeded, and a mitered corner is displayed if the miter limit is not exceeded.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an **OH\_Drawing\_Pen** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Returns the miter limit. |

#### \[h2\]OH\_Drawing\_PenSetMiterLimit()

void OH\_Drawing\_PenSetMiterLimit(OH\_Drawing\_Pen\* pen, float miter)

**Description**

Sets the stroke miter limit for a polyline drawn by a pen. When the corner type is bevel, a beveled corner is displayed if the miter limit is exceeded, and a mitered corner is displayed if the miter limit is not exceeded.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an **OH\_Drawing\_Pen** object. |
| float miter | Stroke miter limit, which is a variable. |

#### \[h2\]OH\_Drawing\_PenGetCap()

OH\_Drawing\_PenLineCapStyle OH\_Drawing\_PenGetCap(const OH\_Drawing\_Pen\* pen)

**Description**

Obtains the line cap style of a pen.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an **OH\_Drawing\_Pen** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_PenLineCapStyle](#oh_drawing_penlinecapstyle) | Returns the line cap style. |

#### \[h2\]OH\_Drawing\_PenSetCap()

void OH\_Drawing\_PenSetCap(OH\_Drawing\_Pen\* pen, OH\_Drawing\_PenLineCapStyle capStyle)

**Description**

Sets the line cap style for a pen.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **capStyle** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an **OH\_Drawing\_Pen** object. |
| [OH\_Drawing\_PenLineCapStyle](#oh_drawing_penlinecapstyle) capStyle | Line cap style, which is a variable. |

#### \[h2\]OH\_Drawing\_PenGetJoin()

OH\_Drawing\_PenLineJoinStyle OH\_Drawing\_PenGetJoin(const OH\_Drawing\_Pen\* pen)

**Description**

Obtains the line join style of a pen.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an **OH\_Drawing\_Pen** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_PenLineJoinStyle](#oh_drawing_penlinejoinstyle) | Returns the line join style. |

#### \[h2\]OH\_Drawing\_PenSetJoin()

void OH\_Drawing\_PenSetJoin(OH\_Drawing\_Pen\* pen, OH\_Drawing\_PenLineJoinStyle joinStyle)

**Description**

Sets the join style for this pen.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **joinStyle** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an **OH\_Drawing\_Pen** object. |
| [OH\_Drawing\_PenLineJoinStyle](#oh_drawing_penlinejoinstyle) joinStyle | Join style. |

#### \[h2\]OH\_Drawing\_PenSetShaderEffect()

void OH\_Drawing\_PenSetShaderEffect(OH\_Drawing\_Pen\* pen, OH\_Drawing\_ShaderEffect\* shaderEffect)

**Description**

Sets the shader effect for this pen.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to the [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object. |
| [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md)\* shaderEffect | Pointer to an [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md) object. If NULL is passed in, the shader effect will be cleared. |

#### \[h2\]OH\_Drawing\_PenSetShadowLayer()

void OH\_Drawing\_PenSetShadowLayer(OH\_Drawing\_Pen\* pen, OH\_Drawing\_ShadowLayer\* shadowLayer)

**Description**

Sets the shadow layer for a pen. The shadow layer effect takes effect only when text is drawn.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to the [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object. |
| [OH\_Drawing\_ShadowLayer](../../structs/oh-drawing-shadowlayer/document.md)\* shadowLayer | Pointer to an [OH\_Drawing\_ShadowLayer](../../structs/oh-drawing-shadowlayer/document.md) object. If NULL is passed in, the shadow layer effect will be cleared. |

#### \[h2\]OH\_Drawing\_PenSetPathEffect()

void OH\_Drawing\_PenSetPathEffect(OH\_Drawing\_Pen\* pen, OH\_Drawing\_PathEffect\* pathEffect)

**Description**

Sets the path effect for this pen.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to the [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object. |
| [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md)\* pathEffect | Pointer to an [OH\_Drawing\_PathEffect](../../structs/oh-drawing-patheffect/document.md) object. If NULL is passed in, the path effect will be cleared. |

#### \[h2\]OH\_Drawing\_PenSetFilter()

void OH\_Drawing\_PenSetFilter(OH\_Drawing\_Pen\* pen, OH\_Drawing\_Filter\* filter)

**Description**

Sets a filter for a pen.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to the [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object. |
| [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md)\* filter | Pointer to an [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md) object. If NULL is passed in, the filter will be cleared. |

#### \[h2\]OH\_Drawing\_PenGetFilter()

void OH\_Drawing\_PenGetFilter(OH\_Drawing\_Pen\* pen, OH\_Drawing\_Filter\* filter)

**Description**

Obtains the [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md) object from the pen. The filter is a container that holds a mask filter and color filter.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **pen** or **filter** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to the [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object. |
| [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md)\* filter | Pointer to an [OH\_Drawing\_Filter](../../structs/oh-drawing-filter/document.md) object. |

#### \[h2\]OH\_Drawing\_PenSetBlendMode()

void OH\_Drawing\_PenSetBlendMode(OH\_Drawing\_Pen\* pen, OH\_Drawing\_BlendMode blendMode)

**Description**

Sets a blender for a pen. The blender implements the specified blend mode.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **blendMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to the [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object. |
| [OH\_Drawing\_BlendMode](../drawing-types-h/document.md#oh_drawing_blendmode) blendMode | Enumeration of blend modes. |

#### \[h2\]OH\_Drawing\_PenGetFillPath()

bool OH\_Drawing\_PenGetFillPath(OH\_Drawing\_Pen\* pen, const OH\_Drawing\_Path\* src, OH\_Drawing\_Path\* dst,const OH\_Drawing\_Rect\* rect, const OH\_Drawing\_Matrix\* matrix)

**Description**

Obtains the source path outline drawn using this pen and represents it using a destination path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **pen**, **src**, and **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to the [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object. |
| const [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* src | Pointer to the source [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* dst | Pointer to the target [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object. NULL is recommended. |
| const [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to an [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. NULL is recommended. The default value is an identity matrix. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the destination path is obtained; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_PenReset()

void OH\_Drawing\_PenReset(OH\_Drawing\_Pen\* pen)

**Description**

Resets a pen to the initial state.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to the [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object. |

#### \[h2\]OH\_Drawing\_PenSetColor4f()

OH\_Drawing\_ErrorCode OH\_Drawing\_PenSetColor4f(OH\_Drawing\_Pen\* pen, float a, float r, float g, float b,OH\_NativeColorSpaceManager\* colorSpaceManager)

**Description**

Sets the color for a pen, which is used to outline a shape.

The color is in ARGB format represented by floating-point numbers. The color space is specified by [OH\_NativeColorSpaceManager](../../structs/oh-nativecolorspacemanager/document.md).

If **colorSpaceManager** is a null pointer, the SRGB (standard red, green, and blue color space based on IEC 61966-2.1:1999) color space is used as the default value.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Drawing\_Pen\* pen | Pointer to an [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object. |
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

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **pen** is NULL.

 |

#### \[h2\]OH\_Drawing\_PenGetAlphaFloat()

OH\_Drawing\_ErrorCode OH\_Drawing\_PenGetAlphaFloat(OH\_Drawing\_Pen\* pen, float\* a)

**Description**

Obtains the alpha value of the pen color.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object. |
| float\* a | Alpha value of the pen color. The value is a floating-point number ranging from 0.0 to 1.0. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **pen** or **a** is NULL.

 |

#### \[h2\]OH\_Drawing\_PenGetRedFloat()

OH\_Drawing\_ErrorCode OH\_Drawing\_PenGetRedFloat(OH\_Drawing\_Pen\* pen, float\* r)

**Description**

Obtains the red component of the pen color.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object. |
| float\* r | Red component of the pen color. The value is a floating-point number ranging from 0.0 to 1.0. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **pen** or **r** is NULL.

 |

#### \[h2\]OH\_Drawing\_PenGetGreenFloat()

OH\_Drawing\_ErrorCode OH\_Drawing\_PenGetGreenFloat(OH\_Drawing\_Pen\* pen, float\* g)

**Description**

Obtains the green component of the pen color.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object. |
| float\* g | Green component of the pen color. The value is a floating-point number ranging from 0.0 to 1.0. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **pen** or **g** is NULL.

 |

#### \[h2\]OH\_Drawing\_PenGetBlueFloat()

OH\_Drawing\_ErrorCode OH\_Drawing\_PenGetBlueFloat(OH\_Drawing\_Pen\* pen, float\* b)

**Description**

Obtains the blue component of the pen color.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object. |
| float\* b | Blue component of the pen color. The value is a floating-point number ranging from 0.0 to 1.0. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **pen** or **b** is NULL.

 |
