# drawing\_shader\_effect.h

#### Overview

This file declares the functions related to the shader effect in the drawing module.

**File to include**: <native\_drawing/drawing\_shader\_effect.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_TileMode](#oh_drawing_tilemode) | OH\_Drawing\_TileMode | Defines an enum for the tile modes of the shader effect. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateColorShader(const uint32\_t color)](#oh_drawing_shadereffectcreatecolorshader) | Creates an **OH\_Drawing\_ShaderEffect** object with a single color. |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateLinearGradient(const OH\_Drawing\_Point\* startPt,const OH\_Drawing\_Point\* endPt, const uint32\_t\* colors,const float\* pos, uint32\_t size, OH\_Drawing\_TileMode tileMode)](#oh_drawing_shadereffectcreatelineargradient) | 
Creates a **ShaderEffect** object that generates a linear gradient between two points.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **startPt**, **endPt**, and **colors** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **tileMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateLinearGradientWithLocalMatrix(const OH\_Drawing\_Point2D\* startPt, const OH\_Drawing\_Point2D\* endPt, const uint32\_t\* colors, const float\* pos,uint32\_t size, OH\_Drawing\_TileMode tileMode, const OH\_Drawing\_Matrix\* matrix)](#oh_drawing_shadereffectcreatelineargradientwithlocalmatrix) | 

Creates a **ShaderEffect** object that generates a linear gradient between two points.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **startPt**, **endPt**, and **colors** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **tileMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateRadialGradient(const OH\_Drawing\_Point\* centerPt, float radius,const uint32\_t\* colors, const float\* pos, uint32\_t size, OH\_Drawing\_TileMode tileMode)](#oh_drawing_shadereffectcreateradialgradient) | 

Creates an **OH\_Drawing\_ShaderEffect** object that generates a radial gradient based on the center and radius of a circle.

The radial gradient transitions colors from the center to the ending shape in a radial manner.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **centerPt** or **colors** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **tileMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateRadialGradientWithLocalMatrix(const OH\_Drawing\_Point2D\* centerPt, float radius, const uint32\_t\* colors, const float\* pos, uint32\_t size,OH\_Drawing\_TileMode tileMode, const OH\_Drawing\_Matrix\* matrix)](#oh_drawing_shadereffectcreateradialgradientwithlocalmatrix) | 

Creates an **OH\_Drawing\_ShaderEffect** object that generates a radial gradient based on the center and radius of a circle.

The radial gradient transitions colors from the center to the ending shape in a radial manner.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **centerPt** or **colors** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **tileMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateSweepGradientWithLocalMatrix(const OH\_Drawing\_Point\* centerPt,const uint32\_t\* colors, const float\* pos, uint32\_t size, OH\_Drawing\_TileMode tileMode, const OH\_Drawing\_Matrix\* matrix)](#oh_drawing_shadereffectcreatesweepgradientwithlocalmatrix) | 

Creates an **OH\_Drawing\_ShaderEffect** object that generates a sweep gradient based on the matrix transformation at the given center.

A sweep gradient paints a gradient in a sweeping arc ranging from 0° to 360°.

 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateSweepGradient(const OH\_Drawing\_Point\* centerPt,const uint32\_t\* colors, const float\* pos, uint32\_t size, OH\_Drawing\_TileMode tileMode)](#oh_drawing_shadereffectcreatesweepgradient) | 

Creates an **OH\_Drawing\_ShaderEffect** object that generates a sweep gradient based on the center.

A sweep gradient paints a gradient in a sweeping arc ranging from 0° to 360°.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **centerPt** or **colors** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **tileMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateImageShader(OH\_Drawing\_Image\* image,OH\_Drawing\_TileMode tileX, OH\_Drawing\_TileMode tileY, const OH\_Drawing\_SamplingOptions\* samplingOptions,const OH\_Drawing\_Matrix\* matrix)](#oh_drawing_shadereffectcreateimageshader) | 

Creates an **OH\_Drawing\_ShaderEffect** object for an image shader. You are advised not to use the function for the canvas of the capture type because it affects the performance.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **image** or **samplingOptions** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If either **tileX** or **tileY** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateTwoPointConicalGradient(const OH\_Drawing\_Point2D\* startPt,float startRadius, const OH\_Drawing\_Point2D\* endPt, float endRadius, const uint32\_t\* colors, const float\* pos,uint32\_t size, OH\_Drawing\_TileMode tileMode, const OH\_Drawing\_Matrix\* matrix)](#oh_drawing_shadereffectcreatetwopointconicalgradient) | 

Creates an **OH\_Drawing\_ShaderEffect** object that generates a gradient between two given circles.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **startPt**, **endPt**, and **colors** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **tileMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateCompose(OH\_Drawing\_ShaderEffect\* dst,OH\_Drawing\_ShaderEffect\* src, OH\_Drawing\_BlendMode mode)](#oh_drawing_shadereffectcreatecompose) | Creates a shader by blending two existing shaders in a certain way. |
| [void OH\_Drawing\_ShaderEffectDestroy(OH\_Drawing\_ShaderEffect\* shaderEffect)](#oh_drawing_shadereffectdestroy) | Destroys an **OH\_Drawing\_ShaderEffect** object and reclaims the memory occupied by the object. |
| [OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreatePixelMapShader(OH\_Drawing\_PixelMap\* pixelMap,OH\_Drawing\_TileMode tileX, OH\_Drawing\_TileMode tileY, const OH\_Drawing\_SamplingOptions\* samplingOptions,const OH\_Drawing\_Matrix\* matrix)](#oh_drawing_shadereffectcreatepixelmapshader) | Creates a PixelMap shader object. |

#### Enum Description

#### \[h2\]OH\_Drawing\_TileMode

enum OH\_Drawing\_TileMode

**Description**

Defines an enum for the tile modes of the shader effect.

**Since**: 11

| Enum | Description |
| :-- | :-- |
| CLAMP | Replicates the edge color if the shader effect draws outside of its original boundary. |
| REPEAT | Repeats the shader effect's image in both horizontal and vertical directions. |
| MIRROR | Repeats the shader effect's image in both horizontal and vertical directions, alternating mirror images. |
| DECAL | Renders the shader effect's image only within the original boundary, and returns transparent black elsewhere. |

#### Function Description

#### \[h2\]OH\_Drawing\_ShaderEffectCreatePixelMapShader()

OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreatePixelMapShader(OH\_Drawing\_PixelMap\* pixelMap,OH\_Drawing\_TileMode tileX, OH\_Drawing\_TileMode tileY, const OH\_Drawing\_SamplingOptions\* samplingOptions,const OH\_Drawing\_Matrix\* matrix)

**Description**

Creates a PixelMap shader object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_PixelMap](../../structs/oh-drawing-pixelmap/document.md)\* pixelMap | Pointer to the [OH\_Drawing\_PixelMap](../../structs/oh-drawing-pixelmap/document.md) object. |
| [OH\_Drawing\_TileMode](#oh_drawing_tilemode) tileX | Tile mode of the shader effect in the horizontal direction. For details about the available options, see [OH\_Drawing\_TileMode](#oh_drawing_tilemode). |
| [OH\_Drawing\_TileMode](#oh_drawing_tilemode) tileY | Tile mode of the shader effect in the vertical direction. For details about the available options, see [OH\_Drawing\_TileMode](#oh_drawing_tilemode). |
| [const OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md)\* samplingOptions | Pointer to the [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md) object. |
| [const OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. If the pointer array is empty, the identity matrix is passed in. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Drawing\_ShaderEffect\* | Returns the pointer to the **OH\_Drawing\_ShaderEffect** object created. |

#### \[h2\]OH\_Drawing\_ShaderEffectCreateColorShader()

OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateColorShader(const uint32\_t color)

**Description**

Creates an **OH\_Drawing\_ShaderEffect** object with a single color.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const uint32\_t color | Color in the ARGB format. The value is a 32-bit unsigned integer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md)\* | Returns the pointer to the [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md) object created. If NULL is returned, the creation fails. The possible failure cause is that no memory is available. |

#### \[h2\]OH\_Drawing\_ShaderEffectCreateLinearGradient()

OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateLinearGradient(const OH\_Drawing\_Point\* startPt,const OH\_Drawing\_Point\* endPt, const uint32\_t\* colors,const float\* pos, uint32\_t size, OH\_Drawing\_TileMode tileMode)

**Description**

Creates a **ShaderEffect** object that generates a linear gradient between two points.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **startPt**, **endPt**, and **colors** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **tileMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md)\* startPt | Start point. |
| const [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md)\* endPt | End point. |
| const uint32\_t\* colors | Colors to distribute between the two points. |
| const float\* pos | Relative position of each color in the color array. The array length must be the same as that of **colors**. If **pos** is NULL, colors are evenly distributed between the start point and end point. |
| uint32\_t size | Number of colors and positions (if **pos** is not NULL). |
| [OH\_Drawing\_TileMode](#oh_drawing_tilemode) tileMode | Tile mode of the shader effect. For details about the available options, see [OH\_Drawing\_TileMode](#oh_drawing_tilemode). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md)\* | Returns the pointer to the **OH\_Drawing\_ShaderEffect** object created. |

#### \[h2\]OH\_Drawing\_ShaderEffectCreateLinearGradientWithLocalMatrix()

OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateLinearGradientWithLocalMatrix(const OH\_Drawing\_Point2D\* startPt, const OH\_Drawing\_Point2D\* endPt, const uint32\_t\* colors, const float\* pos,uint32\_t size, OH\_Drawing\_TileMode tileMode, const OH\_Drawing\_Matrix\* matrix)

**Description**

Creates a **ShaderEffect** object that generates a linear gradient between two points.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **startPt**, **endPt**, and **colors** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **tileMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* startPt | Start point. |
| const [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* endPt | End point. |
| const uint32\_t\* colors | Colors to distribute between the two points. |
| const float\* pos | Relative position of each color in the color array. The array length must be the same as that of **colors**. If **pos** is NULL, colors are evenly distributed between the start point and end point. |
| uint32\_t size | Number of colors and positions (if **pos** is not NULL). |
| [OH\_Drawing\_TileMode](#oh_drawing_tilemode) tileMode | Tile mode of the shader effect. For details about the available options, see [OH\_Drawing\_TileMode](#oh_drawing_tilemode). |
| const [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Matrix applied on the shader effect. If **matrix** is NULL, an identity matrix is applied by default. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md)\* | Returns the pointer to the [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md) object created. If NULL is returned, the creation fails. The possible failure cause is that no memory is available or at least one of the parameters **startPt**, **endPt**, and **colors** is NULL. |

#### \[h2\]OH\_Drawing\_ShaderEffectCreateRadialGradient()

OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateRadialGradient(const OH\_Drawing\_Point\* centerPt, float radius,const uint32\_t\* colors, const float\* pos, uint32\_t size, OH\_Drawing\_TileMode tileMode)

**Description**

Creates an **OH\_Drawing\_ShaderEffect** object that generates a radial gradient based on the center and radius of a circle.

The radial gradient transitions colors from the center to the ending shape in a radial manner.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **centerPt** or **colors** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **tileMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md)\* centerPt | Center of the circle. |
| float radius | Radius of the gradient. The value should be a non-negative number. |
| const uint32\_t\* colors | Colors to distribute in the radial direction. |
| const float\* pos | Relative position of each color in the color array. The array length must be the same as that of **colors**. If **pos** is NULL, colors are evenly distributed in the radial direction. |
| uint32\_t size | Number of colors and positions (if **pos** is not NULL). |
| [OH\_Drawing\_TileMode](#oh_drawing_tilemode) tileMode | Tile mode of the shader effect. For details about the available options, see [OH\_Drawing\_TileMode](#oh_drawing_tilemode). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md)\* | Returns the pointer to the **OH\_Drawing\_ShaderEffect** object created. |

#### \[h2\]OH\_Drawing\_ShaderEffectCreateRadialGradientWithLocalMatrix()

OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateRadialGradientWithLocalMatrix(const OH\_Drawing\_Point2D\* centerPt, float radius, const uint32\_t\* colors, const float\* pos, uint32\_t size,OH\_Drawing\_TileMode tileMode, const OH\_Drawing\_Matrix\* matrix)

**Description**

Creates an **OH\_Drawing\_ShaderEffect** object that generates a radial gradient based on the center and radius of a circle.

The radial gradient transitions colors from the center to the ending shape in a radial manner.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **centerPt** or **colors** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **tileMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* centerPt | Center of the circle. |
| float radius | Radius of the gradient. |
| const uint32\_t\* colors | Colors to distribute in the radial direction. |
| const float\* pos | Relative position of each color in the color array. The array length must be the same as that of **colors**. If **pos** is NULL, colors are evenly distributed in the radial direction. |
| uint32\_t size | Number of colors and positions (if **pos** is not NULL). |
| [OH\_Drawing\_TileMode](#oh_drawing_tilemode) tileMode | Tile mode of the shader effect. For details about the available options, see [OH\_Drawing\_TileMode](#oh_drawing_tilemode). |
| const [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Matrix applied on the shader effect. If **matrix** is NULL, an identity matrix is applied by default. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md)\* | Returns the pointer to the [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md) object created. If NULL is returned, the creation fails. The possible failure cause is that no memory is available or at least one of the parameters **centerPt** and **colors** is NULL. |

#### \[h2\]OH\_Drawing\_ShaderEffectCreateSweepGradientWithLocalMatrix()

OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateSweepGradientWithLocalMatrix(const OH\_Drawing\_Point\* centerPt,const uint32\_t\* colors, const float\* pos, uint32\_t size, OH\_Drawing\_TileMode tileMode, const OH\_Drawing\_Matrix\* matrix)

**Description**

Creates an **OH\_Drawing\_ShaderEffect** object that generates a sweep gradient based on the matrix transformation at the given center.

A sweep gradient paints a gradient in a sweeping arc ranging from 0° to 360°.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md)\* centerPt | Center of the circle. |
| const uint32\_t\* colors | Colors to distribute between the two points. |
| const float\* pos | Relative position of each color in the color array. The array length must be the same as that of **colors**. If **pos** is NULL, colors are evenly distributed between the start angle (0°) and end angle (360°). |
| uint32\_t size | Number of colors and positions (if **pos** is not NULL). |
| [OH\_Drawing\_TileMode](#oh_drawing_tilemode) tileMode | Tile mode of the shader effect. For details about the available options, see [OH\_Drawing\_TileMode](#oh_drawing_tilemode). |
| const [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Matrix applied on the shader effect. If **matrix** is NULL, an identity matrix is applied by default. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md)\* | 
Returns the pointer to the [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md) object created.

A null pointer is returned if any of the following conditions is met:

\- The available memory is empty.

\- **centerPt** or **colors** is NULL.

\- The value of **tileMode** is out of the enumerated value range.

 |

#### \[h2\]OH\_Drawing\_ShaderEffectCreateSweepGradient()

OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateSweepGradient(const OH\_Drawing\_Point\* centerPt,const uint32\_t\* colors, const float\* pos, uint32\_t size, OH\_Drawing\_TileMode tileMode)

**Description**

Creates an **OH\_Drawing\_ShaderEffect** object that generates a sweep gradient based on the center.

A sweep gradient paints a gradient in a sweeping arc ranging from 0° to 360°.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **centerPt** or **colors** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **tileMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md)\* centerPt | Center of the circle. |
| const uint32\_t\* colors | Colors to distribute between the two points. |
| const float\* pos | Relative position of each color in the color array. The array length must be the same as that of **colors**. If **pos** is NULL, colors are evenly distributed between the start angle (0°) and end angle (360°). |
| uint32\_t size | Number of colors and positions (if **pos** is not NULL). |
| [OH\_Drawing\_TileMode](#oh_drawing_tilemode) tileMode | Tile mode of the shader effect. For details about the available options, see [OH\_Drawing\_TileMode](#oh_drawing_tilemode). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md)\* | 
Returns the pointer to the [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md) object created.

A null pointer is returned if any of the following conditions is met:

\- The available memory is empty.

\- **centerPt** or **colors** is NULL.

\- The value of **tileMode** is out of the enumerated value range.

 |

#### \[h2\]OH\_Drawing\_ShaderEffectCreateImageShader()

OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateImageShader(OH\_Drawing\_Image\* image,OH\_Drawing\_TileMode tileX, OH\_Drawing\_TileMode tileY, const OH\_Drawing\_SamplingOptions\* samplingOptions,const OH\_Drawing\_Matrix\* matrix)

**Description**

Creates an **OH\_Drawing\_ShaderEffect** object for an image shader. You are advised not to use the function for the canvas of the capture type because it affects the performance.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **image** or **samplingOptions** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If either **tileX** or **tileY** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md)\* image | Pointer to the [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md) object. |
| [OH\_Drawing\_TileMode](#oh_drawing_tilemode) tileX | Tile mode of the shader effect in the horizontal direction. For details about the available options, see [OH\_Drawing\_TileMode](#oh_drawing_tilemode). |
| [OH\_Drawing\_TileMode](#oh_drawing_tilemode) tileY | Tile mode of the shader effect in the vertical direction. For details about the available options, see [OH\_Drawing\_TileMode](#oh_drawing_tilemode). |
| const [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md)\* samplingOptions | Pointer to the [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md) object. |
| const [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. If the pointer array is empty, the identity matrix is passed in. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md)\* | 
Returns the pointer to the [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md) object created.

A null pointer is returned if any of the following conditions is met:

\- The available memory is empty.

\- **image** or **samplingOptions** is NULL.

\- The value of **tileX** or **tileY** is out of the enumerated value range.

 |

#### \[h2\]OH\_Drawing\_ShaderEffectCreateTwoPointConicalGradient()

OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateTwoPointConicalGradient(const OH\_Drawing\_Point2D\* startPt,float startRadius, const OH\_Drawing\_Point2D\* endPt, float endRadius, const uint32\_t\* colors, const float\* pos,uint32\_t size, OH\_Drawing\_TileMode tileMode, const OH\_Drawing\_Matrix\* matrix)

**Description**

Creates an **OH\_Drawing\_ShaderEffect** object that generates a gradient between two given circles.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **startPt**, **endPt**, and **colors** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **tileMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* startPt | Pointer to the center of the start circle. |
| float startRadius | Start radius of the gradient. The value should be a non-negative number. |
| const [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* endPt | Pointer to the center of the end circle. |
| float endRadius | End radius of the gradient. The value should be a non-negative number. |
| const uint32\_t\* colors | Colors to distribute between the two circles. |
| const float\* pos | Relative position of each color in the color array. The array length must be the same as that of **colors**. If **pos** is NULL, colors are evenly distributed between the two circles. |
| uint32\_t size | Number of colors and positions (if **pos** is not NULL). |
| [OH\_Drawing\_TileMode](#oh_drawing_tilemode) tileMode | Tile mode of the shader effect. For details about the available options, see [OH\_Drawing\_TileMode](#oh_drawing_tilemode). |
| const [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Matrix applied on the shader effect. If **matrix** is NULL, an identity matrix is applied by default. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md)\* | 
Returns the pointer to the [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md) object created. If the returned pointer is NULL, the creation fails. The possible causes are as follows:

\- The available memory is empty.

\- **startPt**, **endPt**, or **colors** is NULL.

\- The value of **tileMode** is out of the enumerated value range.

 |

#### \[h2\]OH\_Drawing\_ShaderEffectCreateCompose()

OH\_Drawing\_ShaderEffect\* OH\_Drawing\_ShaderEffectCreateCompose(OH\_Drawing\_ShaderEffect\* dst,OH\_Drawing\_ShaderEffect\* src, OH\_Drawing\_BlendMode mode)

**Description**

Creates a shader by blending two existing shaders in a certain way.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md)\* dst | Shader that serves as the destination color in blend mode. |
| [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md)\* src | Shader that serves as the source color in blend mode. |
| [OH\_Drawing\_BlendMode](../drawing-types-h/document.md#oh_drawing_blendmode) mode | Blend mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md)\* | 
Returns the pointer to the [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md) object created.

If the returned pointer is NULL, the creation fails. The possible causes are as follows:

\- The available memory is empty.

\- **dst** or **src** is NULL.

\- The value of **mode** is out of the enumerated value range.

 |

#### \[h2\]OH\_Drawing\_ShaderEffectDestroy()

void OH\_Drawing\_ShaderEffectDestroy(OH\_Drawing\_ShaderEffect\* shaderEffect)

**Description**

Destroys an **OH\_Drawing\_ShaderEffect** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_ShaderEffect](../../structs/oh-drawing-shadereffect/document.md)\* shaderEffect | Pointer to an **OH\_Drawing\_ShaderEffect** object. |
