# drawing\_matrix.h

#### Overview

This file declares the functions related to the matrix in the drawing module.

**File to include**: <native\_drawing/drawing\_matrix.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_ScaleToFit](#oh_drawing_scaletofit) | OH\_Drawing\_ScaleToFit | Defines an enum for the matrix scaling modes. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix\* OH\_Drawing\_MatrixCreate(void)](#oh_drawing_matrixcreate) | Creates an **OH\_Drawing\_Matrix** object. |
| [OH\_Drawing\_Matrix\* OH\_Drawing\_MatrixCopy(const OH\_Drawing\_Matrix\* matrix)](#oh_drawing_matrixcopy) | Creates a copy of a matrix object. |
| [OH\_Drawing\_Matrix\* OH\_Drawing\_MatrixCreateRotation(float deg, float x, float y)](#oh_drawing_matrixcreaterotation) | 
Creates an **OH\_Drawing\_Matrix** with the rotation attribute.

The matrix is obtained by rotating an identity matrix by a given degree around the rotation point (x, y).

 |
| [OH\_Drawing\_Matrix\* OH\_Drawing\_MatrixCreateScale(float sx, float sy, float px, float py)](#oh_drawing_matrixcreatescale) | 

Creates an **OH\_Drawing\_Matrix** with the scale attribute.

The matrix is obtained by scaling an identity matrix with the factor (sx, sy) at the rotation point (px, py).

 |
| [OH\_Drawing\_Matrix\* OH\_Drawing\_MatrixCreateTranslation(float dx, float dy)](#oh_drawing_matrixcreatetranslation) | 

Creates an **OH\_Drawing\_Matrix** with the translation attribute.

The matrix is obtained by translating the identity matrix by the distance (dx, dy).

 |
| [void OH\_Drawing\_MatrixSetMatrix(OH\_Drawing\_Matrix\* matrix, float scaleX, float skewX, float transX,float skewY, float scaleY, float transY, float persp0, float persp1, float persp2)](#oh_drawing_matrixsetmatrix) | 

Sets matrix parameters for an **OH\_Drawing\_Matrix** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **OH\_Drawing\_Matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_MatrixSetRectToRect(OH\_Drawing\_Matrix\* matrix, const OH\_Drawing\_Rect\* src,const OH\_Drawing\_Rect\* dst, OH\_Drawing\_ScaleToFit stf)](#oh_drawing_matrixsetrecttorect) | 

Scales a matrix to map a source rectangle to a destination rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **matrix**, **src**, and **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_MatrixPreRotate(OH\_Drawing\_Matrix\* matrix, float degree, float px, float py)](#oh_drawing_matrixprerotate) | Premultiplies a matrix by an identity matrix that rotates by a given degree around the rotation point (px, py). |
| [void OH\_Drawing\_MatrixPreScale(OH\_Drawing\_Matrix\* matrix, float sx, float sy, float px, float py)](#oh_drawing_matrixprescale) | Premultiplies a matrix by an identity matrix that scales with the factor (sx, sy) at the scale point (px, py). |
| [void OH\_Drawing\_MatrixPreTranslate(OH\_Drawing\_Matrix\* matrix, float dx, float dy)](#oh_drawing_matrixpretranslate) | Premultiplies a matrix by an identity matrix that translates by a given distance (dx, dy). |
| [void OH\_Drawing\_MatrixPostRotate(OH\_Drawing\_Matrix\* matrix, float degree, float px, float py)](#oh_drawing_matrixpostrotate) | Post multiplies a matrix by an identity matrix that rotates a given degree around the rotation point (px, py). |
| [void OH\_Drawing\_MatrixPostScale(OH\_Drawing\_Matrix\* matrix, float sx, float sy, float px, float py)](#oh_drawing_matrixpostscale) | Post multiplies a matrix by an identity matrix that scales with the factor (sx, sy) at the scale point (px, py). |
| [void OH\_Drawing\_MatrixPostTranslate(OH\_Drawing\_Matrix\* matrix, float dx, float dy)](#oh_drawing_matrixposttranslate) | Post multiplies a matrix by an identity matrix that translates by a given distance (dx, dy). |
| [void OH\_Drawing\_MatrixReset(OH\_Drawing\_Matrix\* matrix)](#oh_drawing_matrixreset) | Resets a matrix to an identity matrix. |
| [void OH\_Drawing\_MatrixConcat(OH\_Drawing\_Matrix\* total, const OH\_Drawing\_Matrix\* a,const OH\_Drawing\_Matrix\* b)](#oh_drawing_matrixconcat) | Multiplies two matrices to produce a new matrix. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_MatrixGetAll(OH\_Drawing\_Matrix\* matrix, float value\[9\])](#oh_drawing_matrixgetall) | Obtains all element values of a matrix. |
| [float OH\_Drawing\_MatrixGetValue(OH\_Drawing\_Matrix\* matrix, int index)](#oh_drawing_matrixgetvalue) | 

Obtains a matrix value of a given index, which ranges from 0 to 8.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **index** is less than 0 or greater than 8, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_MatrixRotate(OH\_Drawing\_Matrix\* matrix, float degree, float px, float py)](#oh_drawing_matrixrotate) | 

Sets this matrix as an identity matrix and rotates it by a given degree around the rotation point (px, py).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_MatrixTranslate(OH\_Drawing\_Matrix\* matrix, float dx, float dy)](#oh_drawing_matrixtranslate) | 

Sets a matrix as an identity matrix and translates it by a given distance (dx, dy).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_MatrixScale(OH\_Drawing\_Matrix\* matrix, float sx, float sy, float px, float py)](#oh_drawing_matrixscale) | 

Sets a matrix as an identity matrix and scales it with the factor (sx, sy) at the rotation point (px, py).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_MatrixInvert(OH\_Drawing\_Matrix\* matrix, OH\_Drawing\_Matrix\* inverse)](#oh_drawing_matrixinvert) | 

Inverts a matrix and returns the result.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **matrix** or **inverse** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_MatrixSetPolyToPoly(OH\_Drawing\_Matrix\* matrix, const OH\_Drawing\_Point2D\* src,const OH\_Drawing\_Point2D\* dst, uint32\_t count)](#oh_drawing_matrixsetpolytopoly) | 

Generates a transformation matrix by setting source points and destination points.

Both the number of source points and that of destination points must be in the range \[0, 4\]. This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **count** is less than 0 or greater than 4, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_MatrixMapPoints(const OH\_Drawing\_Matrix\* matrix, const OH\_Drawing\_Point2D\* src,OH\_Drawing\_Point2D\* dst, int count)](#oh_drawing_matrixmappoints) | 

Maps a source point array to a destination point array by means of matrix transformation.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **matrix**, **src**, and **dst** is NULL or **count** is less than or equal to 0, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_MatrixMapRect(const OH\_Drawing\_Matrix\* matrix, const OH\_Drawing\_Rect\* src, OH\_Drawing\_Rect\* dst)](#oh_drawing_matrixmaprect) | 

Maps a rectangle to the smallest rectangle that can enclose the vertices to which the four source vertices are mapped by means of matrix transformation.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **matrix**, **src**, and **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_MatrixIsEqual(OH\_Drawing\_Matrix\* matrix, OH\_Drawing\_Matrix\* other)](#oh_drawing_matrixisequal) | 

Checks whether two **OH\_Drawing\_Matrix** objects are equal.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **matrix** or **other** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_MatrixIsIdentity(OH\_Drawing\_Matrix\* matrix)](#oh_drawing_matrixisidentity) | Checks whether an **OH\_Drawing\_Matrix** object is an identity matrix. |
| [void OH\_Drawing\_MatrixDestroy(OH\_Drawing\_Matrix\* matrix)](#oh_drawing_matrixdestroy) | Destroys an **OH\_Drawing\_Matrix** object and reclaims the memory occupied by the object. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_MatrixPreConcat(OH\_Drawing\_Matrix\* a, OH\_Drawing\_Matrix\* b)](#oh_drawing_matrixpreconcat) | Left-multiplies matrix a by matrix b. |

#### Enum Description

#### \[h2\]OH\_Drawing\_ScaleToFit

enum OH\_Drawing\_ScaleToFit

**Description**

Defines an enum for the matrix scaling modes.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| SCALE\_TO\_FIT\_FILL | Scales the source rectangle both horizontally and vertically to exactly match the destination rectangle. |
| SCALE\_TO\_FIT\_START | Scales the source rectangle and aligns it to the left and top edges of the destination rectangle. |
| SCALE\_TO\_FIT\_CENTER | Scales the source rectangle and aligns it to the center of the destination rectangle. |
| SCALE\_TO\_FIT\_END | Scales the source rectangle and aligns it to the right and bottom edges of the destination rectangle. |

#### Function Description

#### \[h2\]OH\_Drawing\_MatrixCreate()

OH\_Drawing\_Matrix\* OH\_Drawing\_MatrixCreate(void)

**Description**

Creates an **OH\_Drawing\_Matrix** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* | Returns the pointer to the **OH\_Drawing\_Matrix** object created. |

#### \[h2\]OH\_Drawing\_MatrixCopy()

OH\_Drawing\_Matrix\* OH\_Drawing\_MatrixCopy(const OH\_Drawing\_Matrix\* matrix)

**Description**

Creates a copy of a matrix object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object to be copied. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* | Returns the pointer to the **OH\_Drawing\_Matrix** object created. |

#### \[h2\]OH\_Drawing\_MatrixCreateRotation()

OH\_Drawing\_Matrix\* OH\_Drawing\_MatrixCreateRotation(float deg, float x, float y)

**Description**

Creates an **OH\_Drawing\_Matrix** with the rotation attribute.

The matrix is obtained by rotating an identity matrix by a given degree around the rotation point (x, y).

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| float deg | Angle to rotate, in degrees. A positive value indicates a clockwise rotation, and a negative value indicates a counterclockwise rotation. |
| float x | Coordinate point on the X axis. |
| float y | Coordinate point on the Y axis. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* | Returns a pointer to the created [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |

#### \[h2\]OH\_Drawing\_MatrixCreateScale()

OH\_Drawing\_Matrix\* OH\_Drawing\_MatrixCreateScale(float sx, float sy, float px, float py)

**Description**

Creates an **OH\_Drawing\_Matrix** with the scale attribute.

The matrix is obtained by scaling an identity matrix with the factor (sx, sy) at the rotation point (px, py).

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| float sx | Scale factor on the X axis. If a negative number is passed in, the matrix is mirrored around y = px before being scaled. The value is a floating point number. |
| float sy | Scale factor on the Y axis. If a negative number is passed in, the matrix is mirrored around x = py before being scaled. The value is a floating point number. |
| float px | Coordinate point on the X axis. |
| float py | Coordinate point on the Y axis. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* | Returns a pointer to the created [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |

#### \[h2\]OH\_Drawing\_MatrixCreateTranslation()

OH\_Drawing\_Matrix\* OH\_Drawing\_MatrixCreateTranslation(float dx, float dy)

**Description**

Creates an **OH\_Drawing\_Matrix** with the translation attribute.

The matrix is obtained by translating the identity matrix by the distance (dx, dy).

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| float dx | Distance to translate on the X axis. A positive number indicates a translation towards the positive direction of the X axis, and a negative number indicates a translation towards the negative direction of the X axis. The value is a floating point number. |
| float dy | Distance to translate on the Y axis. A positive number indicates a translation towards the positive direction of the Y axis, and a negative number indicates a translation towards the negative direction of the Y axis. The value is a floating point number. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* | Returns a pointer to the created [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |

#### \[h2\]OH\_Drawing\_MatrixSetMatrix()

void OH\_Drawing\_MatrixSetMatrix(OH\_Drawing\_Matrix\* matrix, float scaleX, float skewX, float transX,float skewY, float scaleY, float transY, float persp0, float persp1, float persp2)

**Description**

Sets matrix parameters for an **OH\_Drawing\_Matrix** object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **OH\_Drawing\_Matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to an **OH\_Drawing\_Matrix** object. |
| float scaleX | Scale factor on the X axis. |
| float skewX | Skew factor on the X axis. |
| float transX | Translation coefficient on the X axis. |
| float skewY | Skew factor on the Y axis. |
| float scaleY | Scale factor on the Y axis. |
| float transY | Translation coefficient on the Y axis. |
| float persp0 | Perspective coefficient of the X axis. |
| float persp1 | Perspective coefficient of the Y axis. |
| float persp2 | Perspective scale coefficient. |

#### \[h2\]OH\_Drawing\_MatrixSetRectToRect()

bool OH\_Drawing\_MatrixSetRectToRect(OH\_Drawing\_Matrix\* matrix, const OH\_Drawing\_Rect\* src,const OH\_Drawing\_Rect\* dst, OH\_Drawing\_ScaleToFit stf)

**Description**

Scales a matrix to map a source rectangle to a destination rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **matrix**, **src**, and **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* src | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object of the mapping source. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* dst | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object of the mapping destination. |
| [OH\_Drawing\_ScaleToFit](#oh_drawing_scaletofit) stf | Scaling mode. For details about the available options, see [OH\_Drawing\_ScaleToFit](#oh_drawing_scaletofit). |

**Return value**

| Type | Description |
| :-- | :-- |
| bool | 
Returns **true** if the operation is successful; returns **false** if the operation fails; returns **true** and sets the matrix as follows if the passed-in matrix is empty:

If the width or height of **src** is less than or equal to 0, **false** is returned and the matrix is set to an identity matrix.

If the width or height of **dst** is less than or equal to 0, **true** is returned and the matrix is set as follows (perspective scale coefficient = 1; other values = 0).

 |

#### \[h2\]OH\_Drawing\_MatrixPreRotate()

void OH\_Drawing\_MatrixPreRotate(OH\_Drawing\_Matrix\* matrix, float degree, float px, float py)

**Description**

Premultiplies this matrix by a matrix that is derived from an identity matrix after it has been rotated by a given degree around the rotation point (px, py).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| float degree | Angle to rotate, in degrees. A positive value indicates a clockwise rotation, and a negative value indicates a counterclockwise rotation. |
| float px | X coordinate of the rotation point. |
| float py | Y coordinate of the rotation point. |

#### \[h2\]OH\_Drawing\_MatrixPreScale()

void OH\_Drawing\_MatrixPreScale(OH\_Drawing\_Matrix\* matrix, float sx, float sy, float px, float py)

**Description**

Premultiplies a matrix by an identity matrix that scales with the factor (sx, sy) at the scale point (px, py).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| float sx | Scale factor on the X axis. If a negative number is passed in, the matrix is mirrored around y = px before being scaled. The value is a floating point number. |
| float sy | Scale factor on the Y axis. If a negative number is passed in, the matrix is mirrored around x = py before being scaled. The value is a floating point number. |
| float px | X coordinate of the scale point. |
| float py | Y coordinate of the scale point. |

#### \[h2\]OH\_Drawing\_MatrixPreTranslate()

void OH\_Drawing\_MatrixPreTranslate(OH\_Drawing\_Matrix\* matrix, float dx, float dy)

**Description**

Premultiplies this matrix by a matrix that is derived from an identity matrix after it has been translated by a given distance (dx, dy).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| float dx | Horizontal distance to translate. A positive number indicates a translation towards the positive direction of the X axis, and a negative number indicates a translation towards the negative direction of the X axis. The value is a floating point number. |
| float dy | Vertical distance to translate. A positive number indicates a translation towards the positive direction of the Y axis, and a negative number indicates a translation towards the negative direction of the Y axis. The value is a floating point number. |

#### \[h2\]OH\_Drawing\_MatrixPostRotate()

void OH\_Drawing\_MatrixPostRotate(OH\_Drawing\_Matrix\* matrix, float degree, float px, float py)

**Description**

Post multiplies this matrix by a matrix that is derived from an identity matrix after it has been rotated by a given degree around the rotation point (px, py).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| float degree | Angle to rotate, in degrees. A positive value indicates a clockwise rotation, and a negative value indicates a counterclockwise rotation. |
| float px | X coordinate of the rotation point. |
| float py | Y coordinate of the rotation point. |

#### \[h2\]OH\_Drawing\_MatrixPostScale()

void OH\_Drawing\_MatrixPostScale(OH\_Drawing\_Matrix\* matrix, float sx, float sy, float px, float py)

**Description**

Post multiplies a matrix by an identity matrix that scales with the factor (sx, sy) at the scale point (px, py).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| float sx | Scale factor on the X axis. If a negative number is passed in, the matrix is mirrored around y = px before being scaled. The value is a floating point number. |
| float sy | Scale factor on the Y axis. If a negative number is passed in, the matrix is mirrored around x = py before being scaled. The value is a floating point number. |
| float px | X coordinate of the scale point. |
| float py | Y coordinate of the scale point. |

#### \[h2\]OH\_Drawing\_MatrixPostTranslate()

void OH\_Drawing\_MatrixPostTranslate(OH\_Drawing\_Matrix\* matrix, float dx, float dy)

**Description**

Post multiplies this matrix by a matrix that is derived from an identity matrix after it has been translated by a given distance (dx, dy).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| float dx | Horizontal distance to translate. A positive number indicates a translation towards the positive direction of the X axis, and a negative number indicates a translation towards the negative direction of the X axis. The value is a floating point number. |
| float dy | Vertical distance to translate. A positive number indicates a translation towards the positive direction of the Y axis, and a negative number indicates a translation towards the negative direction of the Y axis. The value is a floating point number. |

#### \[h2\]OH\_Drawing\_MatrixReset()

void OH\_Drawing\_MatrixReset(OH\_Drawing\_Matrix\* matrix)

**Description**

Resets a matrix to an identity matrix.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |

#### \[h2\]OH\_Drawing\_MatrixConcat()

void OH\_Drawing\_MatrixConcat(OH\_Drawing\_Matrix\* total, const OH\_Drawing\_Matrix\* a,const OH\_Drawing\_Matrix\* b)

**Description**

Multiplies two matrices to produce a new matrix.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **total**, **a**, and **b** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* total | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| const [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* a | Pointer to [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object a. |
| const [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* b | Pointer to [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object b. |

#### \[h2\]OH\_Drawing\_MatrixGetAll()

OH\_Drawing\_ErrorCode OH\_Drawing\_MatrixGetAll(OH\_Drawing\_Matrix\* matrix, float value\[9\])

**Description**

Obtains all element values of a matrix.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| value | Array used to store the obtained element values. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns an execution result.

**OH\_DRAWING\_SUCCESS** if all element values of the matrix are successfully obtained.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if the matrix element values fail to be obtained. The failure cause is that **matrix** or **value** is NULL.

 |

#### \[h2\]OH\_Drawing\_MatrixGetValue()

float OH\_Drawing\_MatrixGetValue(OH\_Drawing\_Matrix\* matrix, int index)

**Description**

Obtains a matrix value of a given index, which ranges from 0 to 8.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **index** is less than 0 or greater than 8, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| int index | Index, which ranges from 0 to 8. |

**Return value**

| Type | Description |
| :-- | :-- |
| float | Returns the matrix value. |

#### \[h2\]OH\_Drawing\_MatrixRotate()

void OH\_Drawing\_MatrixRotate(OH\_Drawing\_Matrix\* matrix, float degree, float px, float py)

**Description**

Sets this matrix as an identity matrix and rotates it by a given degree around the rotation point (px, py).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| float degree | Angle to rotate, in degrees. A positive value indicates a clockwise rotation, and a negative value indicates a counterclockwise rotation. |
| float px | Coordinate point on the X axis. |
| float py | Coordinate point on the Y axis. |

#### \[h2\]OH\_Drawing\_MatrixTranslate()

void OH\_Drawing\_MatrixTranslate(OH\_Drawing\_Matrix\* matrix, float dx, float dy)

**Description**

Sets a matrix as an identity matrix and translates it by a given distance (dx, dy).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| float dx | Distance to translate on the X axis. A positive number indicates a translation towards the positive direction of the X axis, and a negative number indicates a translation towards the negative direction of the X axis. The value is a floating point number. |
| float dy | Distance to translate on the Y axis. A positive number indicates a translation towards the positive direction of the Y axis, and a negative number indicates a translation towards the negative direction of the Y axis. The value is a floating point number. |

#### \[h2\]OH\_Drawing\_MatrixScale()

void OH\_Drawing\_MatrixScale(OH\_Drawing\_Matrix\* matrix, float sx, float sy, float px, float py)

**Description**

Sets a matrix as an identity matrix and scales it with the factor (sx, sy) at the rotation point (px, py).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| float sx | Scale factor on the X axis. If a negative number is passed in, the matrix is mirrored around y = px before being scaled. The value is a floating point number. |
| float sy | Scale factor on the Y axis. If a negative number is passed in, the matrix is mirrored around x = py before being scaled. The value is a floating point number. |
| float px | Coordinate point on the X axis. |
| float py | Coordinate point on the Y axis. |

#### \[h2\]OH\_Drawing\_MatrixInvert()

bool OH\_Drawing\_MatrixInvert(OH\_Drawing\_Matrix\* matrix, OH\_Drawing\_Matrix\* inverse)

**Description**

Inverts a matrix and returns the result.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **matrix** or **inverse** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* inverse | Pointer to the inverse [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. You can call [OH\_Drawing\_MatrixCreate](#oh_drawing_matrixcreate) to create an inverse matrix object. |

**Return value**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the matrix is reversible and the passed-in **inverse** is inverted; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_MatrixSetPolyToPoly()

bool OH\_Drawing\_MatrixSetPolyToPoly(OH\_Drawing\_Matrix\* matrix, const OH\_Drawing\_Point2D\* src,const OH\_Drawing\_Point2D\* dst, uint32\_t count)

**Description**

Generates a transformation matrix by setting source points and destination points.

Both the number of source points and that of destination points must be in the range \[0, 4\]. This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **count** is less than 0 or greater than 4, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| const [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* src | Array of source points. If NULL is passed in, **count** must be 0. |
| const [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* dst | Array of destination points. The number of destination points must be the same as that of source points. If NULL is passed in, **count** must be 0. |
| uint32\_t count | Number of source points or destination points. If 0 is passed in, the matrix is set to an identity matrix. |

**Return value**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the matrix is generated; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_MatrixMapPoints()

void OH\_Drawing\_MatrixMapPoints(const OH\_Drawing\_Matrix\* matrix, const OH\_Drawing\_Point2D\* src,OH\_Drawing\_Point2D\* dst, int count)

**Description**

Maps a source point array to a destination point array by means of matrix transformation.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **matrix**, **src**, and **dst** is NULL or **count** is less than or equal to 0, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| const [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* src | Array of source points. |
| [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* dst | Array of destination points. The number of destination points must be the same as that of source points. |
| int count | Number of source points or destination points. |

#### \[h2\]OH\_Drawing\_MatrixMapRect()

bool OH\_Drawing\_MatrixMapRect(const OH\_Drawing\_Matrix\* matrix, const OH\_Drawing\_Rect\* src, OH\_Drawing\_Rect\* dst)

**Description**

Maps a rectangle to the smallest rectangle that can enclose the vertices to which the four source vertices are mapped by means of matrix transformation.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **matrix**, **src**, and **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* src | Source rectangle. |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* dst | Destination rectangle. |

**Return value**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the objects are equal; **false** otherwise. |

#### \[h2\]OH\_Drawing\_MatrixIsEqual()

bool OH\_Drawing\_MatrixIsEqual(OH\_Drawing\_Matrix\* matrix, OH\_Drawing\_Matrix\* other)

**Description**

Checks whether two **OH\_Drawing\_Matrix** objects are equal.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **matrix** or **other** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to one [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* other | Pointer to the other [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |

**Return value**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the two matrices are equal; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_MatrixIsIdentity()

bool OH\_Drawing\_MatrixIsIdentity(OH\_Drawing\_Matrix\* matrix)

**Description**

Checks whether an **OH\_Drawing\_Matrix** object is an identity matrix.

An identity matrix is as follows: | 1 0 0 || 0 1 0 || 0 0 1 |. This API may return an error code. For details, see [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |

**Return value**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the matrix is an identity matrix; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_MatrixDestroy()

void OH\_Drawing\_MatrixDestroy(OH\_Drawing\_Matrix\* matrix)

**Description**

Destroys an **OH\_Drawing\_Matrix** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to an **OH\_Drawing\_Matrix** object. |

#### \[h2\]OH\_Drawing\_MatrixPreConcat()

OH\_Drawing\_ErrorCode OH\_Drawing\_MatrixPreConcat(OH\_Drawing\_Matrix\* a, OH\_Drawing\_Matrix\* b)

**Description**

Left-multiplies matrix a by matrix b.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* a | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* b | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns an execution result.

**OH\_DRAWING\_SUCCESS**: Left multiplication successful.

OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER: Incorrect input parameter, that is **rect** or **other** is empty.

 |
