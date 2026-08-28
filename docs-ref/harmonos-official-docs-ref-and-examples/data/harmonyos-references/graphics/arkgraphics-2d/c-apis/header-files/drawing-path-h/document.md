# drawing\_path.h

#### Overview

This file declares the functions related to the path in the drawing module.

**File to include**: <native\_drawing/drawing\_path.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_PathDirection](#oh_drawing_pathdirection) | OH\_Drawing\_PathDirection | Defines an enum for the directions of a closed contour. |
| [OH\_Drawing\_PathFillType](#oh_drawing_pathfilltype) | OH\_Drawing\_PathFillType | Defines an enum for the fill types of a path. |
| [OH\_Drawing\_PathAddMode](#oh_drawing_pathaddmode) | OH\_Drawing\_PathAddMode | Defines an enum for the path adding modes. |
| [OH\_Drawing\_PathOpMode](#oh_drawing_pathopmode) | OH\_Drawing\_PathOpMode | Defines an enum for the operation modes available for a path. |
| [OH\_Drawing\_PathMeasureMatrixFlags](#oh_drawing_pathmeasurematrixflags) | OH\_Drawing\_PathMeasureMatrixFlags | Defines an enum for the types of matrix information obtained during path measurement. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path\* OH\_Drawing\_PathCreate(void)](#oh_drawing_pathcreate) | Creates an **OH\_Drawing\_Path** object. |
| [OH\_Drawing\_Path\* OH\_Drawing\_PathCopy(OH\_Drawing\_Path\* path)](#oh_drawing_pathcopy) | 
Creates a copy of the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathDestroy(OH\_Drawing\_Path\* path)](#oh_drawing_pathdestroy) | Destroys an **OH\_Drawing\_Path** object and reclaims the memory occupied by the object. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathSetPath(OH\_Drawing\_Path\* path, OH\_Drawing\_Path\* other)](#oh_drawing_pathsetpath) | Sets a path object as the current path object. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathIsEmpty(OH\_Drawing\_Path\* path, bool\* isEmpty)](#oh_drawing_pathisempty) | Checks whether a path object is empty. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathIsRect(OH\_Drawing\_Path\* path, OH\_Drawing\_Rect\* rect, bool\* isRect)](#oh_drawing_pathisrect) | Checks whether a path object forms a rectangle. |
| [void OH\_Drawing\_PathMoveTo(OH\_Drawing\_Path\* path, float x, float y)](#oh_drawing_pathmoveto) | 

Sets the start point of this path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathLineTo(OH\_Drawing\_Path\* path, float x, float y)](#oh_drawing_pathlineto) | 

Draws a line segment from the last point of this path to the target point. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathArcTo(OH\_Drawing\_Path\* path,float x1, float y1, float x2, float y2, float startDeg, float sweepDeg)](#oh_drawing_patharcto) | 

Draws an arc to a path. This is done by using angle arc mode. In this mode, a rectangle is specified first,

and then a start angle and scanning degree are specified. The inscribed ellipse of the rectangle will be used to intercept the arc.

The arc is a portion of the ellipse defined by the start angle and the sweep angle. If the path is empty, a line segment from the last point of the path to the start point of the arc is also added.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathQuadTo(OH\_Drawing\_Path\* path, float ctrlX, float ctrlY, float endX, float endY)](#oh_drawing_pathquadto) | 

Draws a quadratic Bezier curve from the last point of a path to the target point. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathConicTo(OH\_Drawing\_Path\* path, float ctrlX, float ctrlY, float endX, float endY, float weight)](#oh_drawing_pathconicto) | 

Draws a conic curve from the last point of a path to the target point. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathCubicTo(OH\_Drawing\_Path\* path, float ctrlX1, float ctrlY1, float ctrlX2, float ctrlY2, float endX, float endY)](#oh_drawing_pathcubicto) | 

Draws a cubic Bezier curve from the last point of this path to the target point. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathRMoveTo(OH\_Drawing\_Path\* path, float x, float y)](#oh_drawing_pathrmoveto) | 

Sets the start position relative to the last point of a path. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathRLineTo(OH\_Drawing\_Path\* path, float x, float y)](#oh_drawing_pathrlineto) | 

Draws a line segment from the last point of this path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathRQuadTo(OH\_Drawing\_Path\* path, float ctrlX, float ctrlY, float endX, float endY)](#oh_drawing_pathrquadto) | 

Draws a quadratic Bezier curve from the last point of this path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathRConicTo(OH\_Drawing\_Path\* path, float ctrlX, float ctrlY, float endX, float endY, float weight)](#oh_drawing_pathrconicto) | 

Draws a conic curve from the last point of a path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathRCubicTo(OH\_Drawing\_Path\* path, float ctrlX1, float ctrlY1, float ctrlX2, float ctrlY2,float endX, float endY)](#oh_drawing_pathrcubicto) | 

Draws a cubic Bezier curve from the last point of a path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathAddRect(OH\_Drawing\_Path\* path, float left, float top, float right, float bottom,OH\_Drawing\_PathDirection pathDirection)](#oh_drawing_pathaddrect) | 

Adds a rectangle to a path in the specified direction. The start point is the upper left corner of the rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathDirection** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_PathAddRectWithInitialCorner(OH\_Drawing\_Path\* path, const OH\_Drawing\_Rect\* rect,OH\_Drawing\_PathDirection pathDirection, uint32\_t start)](#oh_drawing_pathaddrectwithinitialcorner) | 

Adds a rectangle contour to a path in the specified direction.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathDirection** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_PathAddRoundRect(OH\_Drawing\_Path\* path,const OH\_Drawing\_RoundRect\* roundRect, OH\_Drawing\_PathDirection pathDirection)](#oh_drawing_pathaddroundrect) | 

Adds a rounded rectangle to a path in the specified direction. When the path direction is clockwise, the start point is at the intersection of the rounded rectangle's left boundary and its lower left corner. When the path direction is counterclockwise, the start point is at the intersection point between the left boundary and the upper left corner.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **roundRect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathDirection** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_PathAddOvalWithInitialPoint(OH\_Drawing\_Path\* path, const OH\_Drawing\_Rect\* rect,uint32\_t start, OH\_Drawing\_PathDirection pathDirection)](#oh_drawing_pathaddovalwithinitialpoint) | 

Adds an oval to a path. **OH\_Drawing\_Rect** specifies the outer tangent rectangle of the oval, and **OH\_Drawing\_PathDirection** specifies whether the drawing is clockwise or counterclockwise.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathDirection** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_PathAddOval(OH\_Drawing\_Path\* path,const OH\_Drawing\_Rect\* rect, OH\_Drawing\_PathDirection pathDirection)](#oh_drawing_pathaddoval) | 

Adds an oval to a path in the specified direction.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathDirection** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_PathAddArc(OH\_Drawing\_Path\* path, const OH\_Drawing\_Rect\* rect, float startAngle, float sweepAngle)](#oh_drawing_pathaddarc) | 

Adds an arc to a path as the start of a new contour. The arc added is part of the inscribed ellipse of the rectangle, from the start angle through the sweep angle. If the sweep angle is less than or equal to -360°, or if the sweep angle is greater than or equal to 360°, and start angle modulo 90 is nearly zero, an oval instead of an ellipse is added.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathAddPath(OH\_Drawing\_Path\* path, const OH\_Drawing\_Path\* src, const OH\_Drawing\_Matrix\* matrix)](#oh_drawing_pathaddpath) | 

Transforms the points in a **src** path by a matrix and adds the new one to the current path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **src** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathAddPathWithMatrixAndMode(OH\_Drawing\_Path\* path, const OH\_Drawing\_Path\* src,const OH\_Drawing\_Matrix\* matrix, OH\_Drawing\_PathAddMode pathAddMode)](#oh_drawing_pathaddpathwithmatrixandmode) | 

Transforms the points in a **src** path by a matrix and adds the new one to the current path with the specified adding mode.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **src** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathAddMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_PathAddPathWithMode(OH\_Drawing\_Path\* path,const OH\_Drawing\_Path\* src, OH\_Drawing\_PathAddMode pathAddMode)](#oh_drawing_pathaddpathwithmode) | 

Adds a **src** path to the current path with the specified adding mode.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **src** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathAddMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_PathAddPathWithOffsetAndMode(OH\_Drawing\_Path\* path, const OH\_Drawing\_Path\* src, float dx, float dy,OH\_Drawing\_PathAddMode pathAddMode)](#oh_drawing_pathaddpathwithoffsetandmode) | 

Translates a **src** path by an offset and adds the new one to the current path with the specified adding mode.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **src** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathAddMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_PathAddPolygon(OH\_Drawing\_Path\* path, const OH\_Drawing\_Point2D\* points, uint32\_t count, bool isClosed)](#oh_drawing_pathaddpolygon) | 

Adds a polygon to a path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **points** is NULL or **count** is **0**, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathAddCircle(OH\_Drawing\_Path\* path,float x, float y, float radius, OH\_Drawing\_PathDirection pathDirection)](#oh_drawing_pathaddcircle) | 

Adds a circle to a path in the specified direction.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **radius** is less than or equal to 0, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

If **pathDirection** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [bool OH\_Drawing\_PathBuildFromSvgString(OH\_Drawing\_Path\* path, const char\* str)](#oh_drawing_pathbuildfromsvgstring) | 

Parses the path represented by an SVG string.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **str** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_PathContains(OH\_Drawing\_Path\* path, float x, float y)](#oh_drawing_pathcontains) | 

Checks whether a coordinate point is included in this path. For details, see [OH\_Drawing\_PathFillType](#oh_drawing_pathfilltype).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathTransform(OH\_Drawing\_Path\* path, const OH\_Drawing\_Matrix\* matrix)](#oh_drawing_pathtransform) | 

Transforms the points in a path by matrix.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathTransformWithPerspectiveClip(OH\_Drawing\_Path\* src, const OH\_Drawing\_Matrix\* matrix,OH\_Drawing\_Path\* dst, bool applyPerspectiveClip)](#oh_drawing_pathtransformwithperspectiveclip) | 

Transforms the points in a path by matrix, and uses the new one to replace the **dst** path. If **dst** is NULL, the **src** path is replaced.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **src** or **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathSetFillType(OH\_Drawing\_Path\* path, OH\_Drawing\_PathFillType pathFillType)](#oh_drawing_pathsetfilltype) | 

Sets the fill type of a path. The fill type determines how "inside" of the path is drawn.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathFillType** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathGetFillType(OH\_Drawing\_Path\* path, OH\_Drawing\_PathFillType\* pathFillType)](#oh_drawing_pathgetfilltype) | Obtains the fill type of a path. |
| [float OH\_Drawing\_PathGetLength(OH\_Drawing\_Path\* path, bool forceClosed)](#oh_drawing_pathgetlength) | 

Obtains the length of a path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathGetBounds(OH\_Drawing\_Path\* path, OH\_Drawing\_Rect\* rect)](#oh_drawing_pathgetbounds) | 

Obtains the minimum bounds that enclose a path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathClose(OH\_Drawing\_Path\* path)](#oh_drawing_pathclose) | 

Draws a line segment from the current point to the start point of this path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathOffset(OH\_Drawing\_Path\* path, OH\_Drawing\_Path\* dst, float dx, float dy)](#oh_drawing_pathoffset) | 

Translates a path by an offset along the X axis and Y axis and adds the new one to the **dst** path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_PathReset(OH\_Drawing\_Path\* path)](#oh_drawing_pathreset) | 

Resets the path data.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_PathIsClosed(OH\_Drawing\_Path\* path, bool forceClosed)](#oh_drawing_pathisclosed) | 

Checks whether a path is closed.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_PathGetPositionTangent(OH\_Drawing\_Path\* path, bool forceClosed,float distance, OH\_Drawing\_Point2D\* position, OH\_Drawing\_Point2D\* tangent)](#oh_drawing_pathgetpositiontangent) | 

Obtains the coordinates and tangent at a distance from the start point of this path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **path**, **position**, or **tangent** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathGetSegment(OH\_Drawing\_Path\* path, bool forceClosed,float start, float stop, bool startWithMoveTo, OH\_Drawing\_Path\* dst, bool\* result)](#oh_drawing_pathgetsegment) | Extracts a segment of a path and appends it to a destination path. |
| [bool OH\_Drawing\_PathOp(OH\_Drawing\_Path\* path, const OH\_Drawing\_Path\* other, OH\_Drawing\_PathOpMode op)](#oh_drawing_pathop) | 

Combines two paths based on the specified operation mode.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **srcPath** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **op** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [bool OH\_Drawing\_PathGetMatrix(OH\_Drawing\_Path\* path, bool forceClosed,float distance, OH\_Drawing\_Matrix\* matrix, OH\_Drawing\_PathMeasureMatrixFlags flag)](#oh_drawing_pathgetmatrix) | 

Obtains a transformation matrix at a distance from the start point of this path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **flag** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathApproximate(OH\_Drawing\_Path\* path, float acceptableError, float\* vals,uint32\_t\* count)](#oh_drawing_pathapproximate) | Converts the existing path into an approximate path consisting of consecutive line segments. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathInterpolate(OH\_Drawing\_Path\* path, OH\_Drawing\_Path\* other,float weight, bool\* success, OH\_Drawing\_Path\* interpolatedPath)](#oh_drawing_pathinterpolate) | 

Interpolates between the existing path and another path based on the given weight and stores the result in the target path object.

Interpolation is achievable if the two paths have the same number of points. The target path is created based on the structure of the existing path.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathIsInterpolate(OH\_Drawing\_Path\* path, OH\_Drawing\_Path\* other, bool\* result)](#oh_drawing_pathisinterpolate) | 

Checks whether the existing path and another path (**other**) are compatible for interpolation in terms of structure and operation sequence.

If the paths contain conic operations, the weight values of the operations must be the same.

 |

#### Enum Description

#### \[h2\]OH\_Drawing\_PathDirection

enum OH\_Drawing\_PathDirection

**Description**

Enumerates the directions of a closed contour.

**Since**: 12

| Value | Description |
| :-- | :-- |
| PATH\_DIRECTION\_CW | Adds a closed contour clockwise. |
| PATH\_DIRECTION\_CCW | Adds a closed contour counterclockwise. |

#### \[h2\]OH\_Drawing\_PathFillType

enum OH\_Drawing\_PathFillType

**Description**

Enumerates the fill types of a path.

**Since**: 12

| Value | Description |
| :-- | :-- |
| PATH\_FILL\_TYPE\_WINDING | 
For any point within the drawing area, a ray is cast in an arbitrary direction. The count starts at 0 for all intersections between this ray and the path.

Each clockwise intersection—where the path crosses the ray from left to right—results in the count being incremented by 1, while each counterclockwise intersection—where the path crosses the ray from right to left—causes the count to be decremented by 1. A point is deemed inside the path and needs to be colored if the final count is non-zero; if the count is 0, the point remains uncolored.

 |
| PATH\_FILL\_TYPE\_EVEN\_ODD | For any point in the drawing area, a ray is cast in an arbitrary direction. If the number of intersections between this ray and the path is odd, the point is deemed inside the path and needs to be colored; if the number is even, it remains uncolored. |
| PATH\_FILL\_TYPE\_INVERSE\_WINDING | Same as **PATH\_FILL\_TYPE\_WINDING**, but draws outside of the path, rather than inside. |
| PATH\_FILL\_TYPE\_INVERSE\_EVEN\_ODD | Same as **PATH\_FILL\_TYPE\_EVEN\_ODD**, but draws outside of the path, rather than inside. |

#### \[h2\]OH\_Drawing\_PathAddMode

enum OH\_Drawing\_PathAddMode

**Description**

Enumerates the path adding modes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| PATH\_ADD\_MODE\_APPEND | Adds a path in append mode. |
| PATH\_ADD\_MODE\_EXTEND | Adds a line segment to close the path if the previous path is not closed. |

#### \[h2\]OH\_Drawing\_PathOpMode

enum OH\_Drawing\_PathOpMode

**Description**

Enumerates the operation modes available for a path.

**Since**: 12

| Value | Description |
| :-- | :-- |
| PATH\_OP\_MODE\_DIFFERENCE | Difference operation. |
| PATH\_OP\_MODE\_INTERSECT | Intersection operation. |
| PATH\_OP\_MODE\_UNION | Union operation. |
| PATH\_OP\_MODE\_XOR | XOR operation. |
| PATH\_OP\_MODE\_REVERSE\_DIFFERENCE | Reverse difference operation. |

#### \[h2\]OH\_Drawing\_PathMeasureMatrixFlags

enum OH\_Drawing\_PathMeasureMatrixFlags

**Description**

Enumerates the types of matrix information obtained during path measurement.

**Since**: 12

| Value | Description |
| :-- | :-- |
| GET\_POSITION\_MATRIX | Matrix corresponding to the position information. |
| GET\_TANGENT\_MATRIX | Matrix corresponding to the tangent information. |
| GET\_POSITION\_AND\_TANGENT\_MATRIX | Matrix corresponding to the position and tangent information. |

#### Function Description

#### \[h2\]OH\_Drawing\_PathCreate()

OH\_Drawing\_Path\* OH\_Drawing\_PathCreate(void)

**Description**

Creates an **OH\_Drawing\_Path** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* | Returns the pointer to the **OH\_Drawing\_Path** object created. |

#### \[h2\]OH\_Drawing\_PathCopy()

OH\_Drawing\_Path\* OH\_Drawing\_PathCopy(OH\_Drawing\_Path\* path)

**Description**

Creates a copy of the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* | Pointer to the copy of the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |

#### \[h2\]OH\_Drawing\_PathDestroy()

void OH\_Drawing\_PathDestroy(OH\_Drawing\_Path\* path)

**Description**

Destroys an **OH\_Drawing\_Path** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to an **OH\_Drawing\_Path** object. |

#### \[h2\]OH\_Drawing\_PathSetPath()

OH\_Drawing\_ErrorCode OH\_Drawing\_PathSetPath(OH\_Drawing\_Path\* path, OH\_Drawing\_Path\* other)

**Description**

Sets a path object as the current path object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* other | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object to be set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **path** or **other** is NULL.

 |

#### \[h2\]OH\_Drawing\_PathIsEmpty()

OH\_Drawing\_ErrorCode OH\_Drawing\_PathIsEmpty(OH\_Drawing\_Path\* path, bool\* isEmpty)

**Description**

Checks whether a path object is empty.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| bool\* isEmpty | Whether the path object is empty. **true** means empty; **false** otherwise. It as an output parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **path** or **isEmpty** is NULL.

 |

#### \[h2\]OH\_Drawing\_PathIsRect()

OH\_Drawing\_ErrorCode OH\_Drawing\_PathIsRect(OH\_Drawing\_Path\* path, OH\_Drawing\_Rect\* rect, bool\* isRect)

**Description**

Checks whether a path object forms a rectangle.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object, which is used as an output parameter and can be null. |
| bool\* isRect | Whether a path forms a rectangle. **true** means yes; **false** otherwise. It as an output parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **path** or **isRect** is NULL.

 |

#### \[h2\]OH\_Drawing\_PathMoveTo()

void OH\_Drawing\_PathMoveTo(OH\_Drawing\_Path\* path, float x, float y)

**Description**

Sets the start point of this path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to an **OH\_Drawing\_Path** object. |
| float x | X coordinate of the start point. |
| float y | Y coordinate of the start point. |

#### \[h2\]OH\_Drawing\_PathLineTo()

void OH\_Drawing\_PathLineTo(OH\_Drawing\_Path\* path, float x, float y)

**Description**

Draws a line segment from the last point of this path to the target point. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to an **OH\_Drawing\_Path** object. |
| float x | X coordinate of the target point. |
| float y | Y coordinate of the target point. |

#### \[h2\]OH\_Drawing\_PathArcTo()

void OH\_Drawing\_PathArcTo(OH\_Drawing\_Path\* path,float x1, float y1, float x2, float y2, float startDeg, float sweepDeg)

**Description**

Draws an arc to a path. This is done by using angle arc mode. In this mode, a rectangle is specified first,

and then a start angle and scanning degree are specified. The inscribed ellipse of the rectangle will be used to intercept the arc.

The arc is a portion of the ellipse defined by the start angle and the sweep angle. If the path is empty, a line segment from the last point of the path to the start point of the arc is also added.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to an **OH\_Drawing\_Path** object. |
| float x1 | X coordinate of the upper left corner of the rectangle. |
| float y1 | Y coordinate of the upper left corner of the rectangle. |
| float x2 | X coordinate of the lower right corner of the rectangle. |
| float y2 | Y coordinate of the lower right corner of the rectangle. |
| float startDeg | Start angle. The start direction (0°) of the angle is the positive direction of the X axis. |
| float sweepDeg | Angle to sweep, in degrees. A positive number indicates a clockwise sweep, and a negative value indicates a counterclockwise swipe. The actual swipe degree is the modulo operation result of the input parameter by 360. |

#### \[h2\]OH\_Drawing\_PathQuadTo()

void OH\_Drawing\_PathQuadTo(OH\_Drawing\_Path\* path, float ctrlX, float ctrlY, float endX, float endY)

**Description**

Draws a quadratic Bezier curve from the last point of a path to the target point. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to an **OH\_Drawing\_Path** object. |
| float ctrlX | X coordinate of the control point. |
| float ctrlY | Y coordinate of the control point. |
| float endX | X coordinate of the target point. |
| float endY | Y coordinate of the target point. |

#### \[h2\]OH\_Drawing\_PathConicTo()

void OH\_Drawing\_PathConicTo(OH\_Drawing\_Path\* path, float ctrlX, float ctrlY, float endX, float endY, float weight)

**Description**

Draws a conic curve from the last point of a path to the target point. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| float ctrlX | X coordinate of the control point. |
| float ctrlY | Y coordinate of the control point. |
| float endX | X coordinate of the target point. |
| float endY | Y coordinate of the target point. |
| float weight | 
Weight of the curve, which determines its shape. The larger the value, the closer of the curve to the control point.

If the value is less than or equal to **0**, the result is equivalent to a line segment from the start point to the end point, which is added by calling [OH\_Drawing\_PathLineTo](#oh_drawing_pathlineto).

If the value is **1**, the result is equivalent to [OH\_Drawing\_PathQuadTo](#oh_drawing_pathquadto).

 |

#### \[h2\]OH\_Drawing\_PathCubicTo()

void OH\_Drawing\_PathCubicTo(OH\_Drawing\_Path\* path, float ctrlX1, float ctrlY1, float ctrlX2, float ctrlY2, float endX, float endY)

**Description**

Draws a cubic Bezier curve from the last point of this path to the target point. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to an **OH\_Drawing\_Path** object. |
| float ctrlX1 | X coordinate of the first control point. |
| float ctrlY1 | Y coordinate of the first control point. |
| float ctrlX2 | X coordinate of the second control point. |
| float ctrlY2 | Y coordinate of the second control point. |
| float endX | X coordinate of the target point. |
| float endY | Y coordinate of the target point. |

#### \[h2\]OH\_Drawing\_PathRMoveTo()

void OH\_Drawing\_PathRMoveTo(OH\_Drawing\_Path\* path, float x, float y)

**Description**

Sets the start position relative to the last point of a path. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| float x | X-axis offset relative to the end point of a path. A positive number indicates an offset in the positive direction of the X axis, and a negative number indicates an offset in the negative direction of the X axis. |
| float y | Y-axis offset relative to the end point of a path. A positive number indicates an offset in the positive direction of the Y axis, and a negative number indicates an offset in the negative direction of the Y axis. |

#### \[h2\]OH\_Drawing\_PathRLineTo()

void OH\_Drawing\_PathRLineTo(OH\_Drawing\_Path\* path, float x, float y)

**Description**

Draws a line segment from the last point of this path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| float x | X offset relative to the last point, which is used to specify the X coordinate of the target point. |
| float y | Y offset relative to the last point, which is used to specify the X coordinate of the target point. |

#### \[h2\]OH\_Drawing\_PathRQuadTo()

void OH\_Drawing\_PathRQuadTo(OH\_Drawing\_Path\* path, float ctrlX, float ctrlY, float endX, float endY)

**Description**

Draws a quadratic Bezier curve from the last point of this path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| float ctrlX | X offset relative to the last point, which is used to specify the X coordinate of the control point. |
| float ctrlY | Y offset relative to the last point, which is used to specify the Y coordinate of the control point. |
| float endX | X offset relative to the last point, which is used to specify the X coordinate of the target point. |
| float endY | Y offset relative to the last point, which is used to specify the Y coordinate of the target point. |

#### \[h2\]OH\_Drawing\_PathRConicTo()

void OH\_Drawing\_PathRConicTo(OH\_Drawing\_Path\* path, float ctrlX, float ctrlY, float endX, float endY, float weight)

**Description**

Draws a conic curve from the last point of a path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| float ctrlX | X offset relative to the last point, which is used to specify the X coordinate of the control point. |
| float ctrlY | Y offset relative to the last point, which is used to specify the Y coordinate of the control point. |
| float endX | X offset relative to the last point, which is used to specify the X coordinate of the target point. |
| float endY | Y offset relative to the last point, which is used to specify the Y coordinate of the target point. |
| float weight | 
Weight of the curve, which determines its shape. The larger the value, the closer of the curve to the control point.

If the value is less than or equal to **0**, the result is equivalent to a line segment from the start point to the end point, which is added by calling [OH\_Drawing\_PathRLineTo](#oh_drawing_pathrlineto).

If the value is **1**, the result is equivalent to [OH\_Drawing\_PathRQuadTo](#oh_drawing_pathrquadto).

 |

#### \[h2\]OH\_Drawing\_PathRCubicTo()

void OH\_Drawing\_PathRCubicTo(OH\_Drawing\_Path\* path, float ctrlX1, float ctrlY1, float ctrlX2, float ctrlY2,float endX, float endY)

**Description**

Draws a cubic Bezier curve from the last point of a path to a point relative to the last point. If the path is empty, the start point (0, 0) is used.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| float ctrlX1 | X offset relative to the last point, which is used to specify the X coordinate of the first control point. |
| float ctrlY1 | Y offset relative to the last point, which is used to specify the Y coordinate of the first control point. |
| float ctrlX2 | X offset relative to the last point, which is used to specify the X coordinate of the second control point. |
| float ctrlY2 | Y offset relative to the last point, which is used to specify the Y coordinate of the second control point. |
| float endX | X offset relative to the last point, which is used to specify the X coordinate of the target point. |
| float endY | Y offset relative to the last point, which is used to specify the Y coordinate of the target point. |

#### \[h2\]OH\_Drawing\_PathAddRect()

void OH\_Drawing\_PathAddRect(OH\_Drawing\_Path\* path, float left, float top, float right, float bottom,OH\_Drawing\_PathDirection pathDirection)

**Description**

Adds a rectangle to a path in the specified direction. The start point is the upper left corner of the rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathDirection** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| float left | X coordinate of the upper left corner of the rectangle. |
| float top | Y coordinate of the upper left corner of the rectangle. |
| float right | X coordinate of the lower right corner of the rectangle. |
| float bottom | Y coordinate of the lower right corner of the rectangle. |
| [OH\_Drawing\_PathDirection](#oh_drawing_pathdirection) pathDirection | [OH\_Drawing\_PathDirection](#oh_drawing_pathdirection) object. |

#### \[h2\]OH\_Drawing\_PathAddRectWithInitialCorner()

void OH\_Drawing\_PathAddRectWithInitialCorner(OH\_Drawing\_Path\* path, const OH\_Drawing\_Rect\* rect,OH\_Drawing\_PathDirection pathDirection, uint32\_t start)

**Description**

Adds a rectangle contour to a path in the specified direction.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathDirection** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object. |
| OH\_Drawing\_PathDirection | [OH\_Drawing\_PathDirection](#oh_drawing_pathdirection) object. |
| uint32\_t start | Start point, indicating the corner of the rectangle from which the path is drawn. The value **0** means the upper left corner, **1** means the upper right corner, **2** means the lower right corner, and **3** means the lower left corner. |

#### \[h2\]OH\_Drawing\_PathAddRoundRect()

void OH\_Drawing\_PathAddRoundRect(OH\_Drawing\_Path\* path,const OH\_Drawing\_RoundRect\* roundRect, OH\_Drawing\_PathDirection pathDirection)

**Description**

Adds a rounded rectangle to a path in the specified direction. When the path direction is clockwise, the start point is at the intersection of the rounded rectangle's left boundary and its lower left corner. When the path direction is counterclockwise, the start point is at the intersection point between the left boundary and the upper left corner.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **roundRect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathDirection** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| const [OH\_Drawing\_RoundRect](../../structs/oh-drawing-roundrect/document.md)\* roundRect | Pointer to the [OH\_Drawing\_RoundRect](../../structs/oh-drawing-roundrect/document.md) object. |
| [OH\_Drawing\_PathDirection](#oh_drawing_pathdirection) pathDirection | [OH\_Drawing\_PathDirection](#oh_drawing_pathdirection) object. |

#### \[h2\]OH\_Drawing\_PathAddOvalWithInitialPoint()

void OH\_Drawing\_PathAddOvalWithInitialPoint(OH\_Drawing\_Path\* path, const OH\_Drawing\_Rect\* rect,uint32\_t start, OH\_Drawing\_PathDirection pathDirection)

**Description**

Adds an oval to a path. **OH\_Drawing\_Rect** specifies the outer tangent rectangle of the oval, and **OH\_Drawing\_PathDirection** specifies whether the drawing is clockwise or counterclockwise.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathDirection** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object. |
| uint32\_t start | Start point of the oval. |
| [OH\_Drawing\_PathDirection](#oh_drawing_pathdirection) pathDirection | [OH\_Drawing\_PathDirection](#oh_drawing_pathdirection) object. |

#### \[h2\]OH\_Drawing\_PathAddOval()

void OH\_Drawing\_PathAddOval(OH\_Drawing\_Path\* path,const OH\_Drawing\_Rect\* rect, OH\_Drawing\_PathDirection pathDirection)

**Description**

Adds an oval to a path in the specified direction.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathDirection** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object. |
| [OH\_Drawing\_PathDirection](#oh_drawing_pathdirection) pathDirection | [OH\_Drawing\_PathDirection](#oh_drawing_pathdirection) object. |

#### \[h2\]OH\_Drawing\_PathAddArc()

void OH\_Drawing\_PathAddArc(OH\_Drawing\_Path\* path, const OH\_Drawing\_Rect\* rect, float startAngle, float sweepAngle)

**Description**

Adds an arc to a path as the start of a new contour. The arc added is part of the inscribed ellipse of the rectangle, from the start angle through the sweep angle. If the sweep angle is less than or equal to -360°, or if the sweep angle is greater than or equal to 360°, and start angle modulo 90 is nearly zero, an oval instead of an ellipse is added.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object. |
| float startAngle | Start angle of the arc, in degrees. |
| float sweepAngle | Angle to sweep, in degrees. A positive number indicates a clockwise sweep, and a negative value indicates a counterclockwise swipe. The actual swipe degree is the modulo operation result of the input parameter by 360. |

#### \[h2\]OH\_Drawing\_PathAddPath()

void OH\_Drawing\_PathAddPath(OH\_Drawing\_Path\* path, const OH\_Drawing\_Path\* src, const OH\_Drawing\_Matrix\* matrix)

**Description**

Transforms the points in a **src** path by a matrix and adds the new one to the current path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **src** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the existing [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| const [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* src | Pointer to the source [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| const [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. A null pointer means an identity matrix. |

#### \[h2\]OH\_Drawing\_PathAddPathWithMatrixAndMode()

void OH\_Drawing\_PathAddPathWithMatrixAndMode(OH\_Drawing\_Path\* path, const OH\_Drawing\_Path\* src,const OH\_Drawing\_Matrix\* matrix, OH\_Drawing\_PathAddMode pathAddMode)

**Description**

Transforms the points in a **src** path by a matrix and adds the new one to the current path with the specified adding mode.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **src** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathAddMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the existing [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| const [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* src | Pointer to the source [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| const [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. A null pointer means an identity matrix. |
| [OH\_Drawing\_PathAddMode](#oh_drawing_pathaddmode) pathAddMode | [OH\_Drawing\_PathAddMode](#oh_drawing_pathaddmode) object. |

#### \[h2\]OH\_Drawing\_PathAddPathWithMode()

void OH\_Drawing\_PathAddPathWithMode(OH\_Drawing\_Path\* path,const OH\_Drawing\_Path\* src, OH\_Drawing\_PathAddMode pathAddMode)

**Description**

Adds a **src** path to the current path with the specified adding mode.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **src** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathAddMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the existing [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| const [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* src | Pointer to the source [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| [OH\_Drawing\_PathAddMode](#oh_drawing_pathaddmode) pathAddMode | [OH\_Drawing\_PathAddMode](#oh_drawing_pathaddmode) object. |

#### \[h2\]OH\_Drawing\_PathAddPathWithOffsetAndMode()

void OH\_Drawing\_PathAddPathWithOffsetAndMode(OH\_Drawing\_Path\* path, const OH\_Drawing\_Path\* src, float dx, float dy,OH\_Drawing\_PathAddMode pathAddMode)

**Description**

Translates a **src** path by an offset and adds the new one to the current path with the specified adding mode.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **src** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathAddMode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the existing [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| const [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* src | Pointer to the source [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| float dx | X offset. |
| float dy | Y offset. |
| [OH\_Drawing\_PathAddMode](#oh_drawing_pathaddmode) pathAddMode | [OH\_Drawing\_PathAddMode](#oh_drawing_pathaddmode) object. |

#### \[h2\]OH\_Drawing\_PathAddPolygon()

void OH\_Drawing\_PathAddPolygon(OH\_Drawing\_Path\* path, const OH\_Drawing\_Point2D\* points, uint32\_t count, bool isClosed)

**Description**

Adds a polygon to a path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **points** is NULL or **count** is **0**, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the existing [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| const [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* points | Pointer to an array that holds the vertex coordinates of the polygon. |
| uint32\_t count | Size of the array. |
| bool isClosed | Whether the path is closed. The value **true** means that the path is closed, and **false** means the opposite. |

#### \[h2\]OH\_Drawing\_PathAddCircle()

void OH\_Drawing\_PathAddCircle(OH\_Drawing\_Path\* path,float x, float y, float radius, OH\_Drawing\_PathDirection pathDirection)

**Description**

Adds a circle to a path in the specified direction.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **radius** is less than or equal to 0, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

If **pathDirection** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| float x | X coordinate of the circle center. |
| float y | Y coordinate of the circle center. |
| float radius | Radius of the circle. |
| [OH\_Drawing\_PathDirection](#oh_drawing_pathdirection) pathDirection | [OH\_Drawing\_PathDirection](#oh_drawing_pathdirection) object. |

#### \[h2\]OH\_Drawing\_PathBuildFromSvgString()

bool OH\_Drawing\_PathBuildFromSvgString(OH\_Drawing\_Path\* path, const char\* str)

**Description**

Parses the path represented by an SVG string.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **str** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| const char\* str | Pointer to the SVG string. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns whether the SVG string is successfully parsed. **true** means successful; **false** otherwise. |

#### \[h2\]OH\_Drawing\_PathContains()

bool OH\_Drawing\_PathContains(OH\_Drawing\_Path\* path, float x, float y)

**Description**

Checks whether a coordinate point is included in this path. For details, see [OH\_Drawing\_PathFillType](#oh_drawing_pathfilltype).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| float x | Coordinate point on the X axis. |
| float y | Coordinate point on the Y axis. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the coordinate point is included in the path; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_PathTransform()

void OH\_Drawing\_PathTransform(OH\_Drawing\_Path\* path, const OH\_Drawing\_Matrix\* matrix)

**Description**

Transforms the points in a path by matrix.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| const [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |

#### \[h2\]OH\_Drawing\_PathTransformWithPerspectiveClip()

void OH\_Drawing\_PathTransformWithPerspectiveClip(OH\_Drawing\_Path\* src, const OH\_Drawing\_Matrix\* matrix,OH\_Drawing\_Path\* dst, bool applyPerspectiveClip)

**Description**

Transforms the points in a path by matrix, and uses the new one to replace the **dst** path. If **dst** is NULL, the **src** path is replaced.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **src** or **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* src | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| const [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* dst | Pointer to the target [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| bool applyPerspectiveClip | Whether to apply perspective cropping to the new path. The value **true** means to apply perspective cropping, and **false** means the opposite. |

#### \[h2\]OH\_Drawing\_PathSetFillType()

void OH\_Drawing\_PathSetFillType(OH\_Drawing\_Path\* path, OH\_Drawing\_PathFillType pathFillType)

**Description**

Sets the fill type of a path. The fill type determines how "inside" of the path is drawn.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **pathFillType** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| [OH\_Drawing\_PathFillType](#oh_drawing_pathfilltype) pathFillType | [OH\_Drawing\_PathFillType](#oh_drawing_pathfilltype) object. |

#### \[h2\]OH\_Drawing\_PathGetFillType()

OH\_Drawing\_ErrorCode OH\_Drawing\_PathGetFillType(OH\_Drawing\_Path\* path, OH\_Drawing\_PathFillType\* pathFillType)

**Description**

Obtains the fill type of a path.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| [OH\_Drawing\_PathFillType](#oh_drawing_pathfilltype)\* pathFillType | Pointer to the [OH\_Drawing\_PathFillType](#oh_drawing_pathfilltype) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **path** or **pathFillType** is NULL.

 |

#### \[h2\]OH\_Drawing\_PathGetLength()

float OH\_Drawing\_PathGetLength(OH\_Drawing\_Path\* path, bool forceClosed)

**Description**

Obtains the length of a path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| bool forceClosed | Whether the path is measured as a closed path. **true** means that the path is forcibly considered as a closed path; **false** means that the path is measured depending on whether it is a closed path. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Returns the length of the path. |

#### \[h2\]OH\_Drawing\_PathGetBounds()

void OH\_Drawing\_PathGetBounds(OH\_Drawing\_Path\* path, OH\_Drawing\_Rect\* rect)

**Description**

Obtains the minimum bounds that enclose a path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object. |

#### \[h2\]OH\_Drawing\_PathClose()

void OH\_Drawing\_PathClose(OH\_Drawing\_Path\* path)

**Description**

Draws a line segment from the current point to the start point of this path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |

#### \[h2\]OH\_Drawing\_PathOffset()

void OH\_Drawing\_PathOffset(OH\_Drawing\_Path\* path, OH\_Drawing\_Path\* dst, float dx, float dy)

**Description**

Translates a path by an offset along the X axis and Y axis and adds the new one to the **dst** path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the existing [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* dst | Pointer to a destination path, which is an [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. If NULL is passed in, the result is stored in the current path. |
| float dx | X offset. |
| float dy | Y offset. |

#### \[h2\]OH\_Drawing\_PathReset()

void OH\_Drawing\_PathReset(OH\_Drawing\_Path\* path)

**Description**

Resets the path data.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to an **OH\_Drawing\_Path** object. |

#### \[h2\]OH\_Drawing\_PathIsClosed()

bool OH\_Drawing\_PathIsClosed(OH\_Drawing\_Path\* path, bool forceClosed)

**Description**

Checks whether a path is closed.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| bool forceClosed | Whether the path is measured as a closed path. The value **true** means that the path is considered closed during measurement, and **false** means that the path is measured based on the actual closed status. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the path is closed; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_PathGetPositionTangent()

bool OH\_Drawing\_PathGetPositionTangent(OH\_Drawing\_Path\* path, bool forceClosed,float distance, OH\_Drawing\_Point2D\* position, OH\_Drawing\_Point2D\* tangent)

**Description**

Obtains the coordinates and tangent at a distance from the start point of this path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If any of **path**, **position**, or **tangent** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| bool forceClosed | Whether the path is measured as a closed path. The value **true** means that the path is considered closed during measurement, and **false** means that the path is measured based on the actual closed status. |
| float distance | Distance from the start point. If the distance is less than 0, it is considered as 0. If the distance is greater than the path length, it is considered as the path length. |
| [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* position | Pointer to the coordinates. |
| [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* tangent | Pointer to the tangent, where **tangent.x** and **tangent.y** represent the cosine and sine of the tangent of the point, respectively. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns whether the measurement is successful. **true** means successful; **false** otherwise. |

#### \[h2\]OH\_Drawing\_PathGetSegment()

OH\_Drawing\_ErrorCode OH\_Drawing\_PathGetSegment(OH\_Drawing\_Path\* path, bool forceClosed,float start, float stop, bool startWithMoveTo, OH\_Drawing\_Path\* dst, bool\* result)

**Description**

Extracts a segment of a path and appends it to a destination path.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| bool forceClosed | Whether the path is measured as a closed path. The value **true** means that the path is considered closed during measurement, and **false** means that the path is measured based on the actual closed status. |
| float start | Distance from the start point of the path to the start point of the segment. If it is less than 0, it defaults to 0. If it is greater than or equal to **stop**, the extraction fails. |
| float stop | Distance from the start point of the path to the end point of the segment. If it is less than or equal to **start**, the extraction fails. If it is greater than the path length, it defaults to the path length. |
| bool startWithMoveTo | Whether to execute [OH\_Drawing\_PathMoveTo](#oh_drawing_pathmoveto) in the destination path to move to its start point. The value **true** means to move to the start point, and **false** means the opposite. |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* dst | Pointer to a destination path, which is an [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. If the extraction succeeds, the segment is appended to the path. If the extraction fails, nothing changes. |
| bool\* result | Pointer to the extraction result. The value **true** means that the extraction is successful, and **false** means the opposite. It as an output parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if at least one of the **path**, **dst**, and **result** parameters is a null pointer.

 |

#### \[h2\]OH\_Drawing\_PathOp()

bool OH\_Drawing\_PathOp(OH\_Drawing\_Path\* path, const OH\_Drawing\_Path\* other, OH\_Drawing\_PathOpMode op)

**Description**

Combines two paths based on the specified operation mode.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **srcPath** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **op** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to an [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object, in which the resulting path is saved. |
| const [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* other | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| [OH\_Drawing\_PathOpMode](#oh_drawing_pathopmode) op | Operation mode of the path. For details about the available options, see [OH\_Drawing\_PathOpMode](#oh_drawing_pathopmode). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the resulting path is not empty; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_PathGetMatrix()

bool OH\_Drawing\_PathGetMatrix(OH\_Drawing\_Path\* path, bool forceClosed,float distance, OH\_Drawing\_Matrix\* matrix, OH\_Drawing\_PathMeasureMatrixFlags flag)

**Description**

Obtains a transformation matrix at a distance from the start point of this path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **path** or **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **flag** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| bool forceClosed | Whether the path is measured as a closed path. The value **true** means that the path is considered closed during measurement, and **false** means that the path is measured based on the actual closed status. |
| float distance | Distance from the start point. If the distance is less than 0, it is considered as 0. If the distance is greater than the path length, it is considered as the path length. |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the transformation matrix. |
| [OH\_Drawing\_PathMeasureMatrixFlags](#oh_drawing_pathmeasurematrixflags) flag | Type of the matrix information. For details about the available options, see [OH\_Drawing\_PathMeasureMatrixFlags](#oh_drawing_pathmeasurematrixflags). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the transformation matrix is obtained successfully; returns **false** otherwise. The possible failure cause is that **path** is NULL or the path length is 0. |

#### \[h2\]OH\_Drawing\_PathApproximate()

OH\_Drawing\_ErrorCode OH\_Drawing\_PathApproximate(OH\_Drawing\_Path\* path, float acceptableError, float\* vals,uint32\_t\* count)

**Description**

Converts the existing path into an approximate path consisting of consecutive line segments.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| float acceptableError | 
Acceptable error of each line segment on the path. The value cannot be less than 0.

1\. Avoid setting **acceptableError** to **0** as it heavily divides the curve path, significantly impacting performance and memory usage.

2\. Setting a high **acceptableError** simplifies the path greatly by keeping only essential points, potentially distorting the original shape.

3\. When you set a high **acceptableError** for curves such as ellipses, the fitting process often simplifies them to polygons by keeping just the start and end points of their Bezier curve segments.

 |
| float\* vals | 

An array of approximate points of the path.

Each point consists of three values, indicating:

1\. Length ratio of the point to the start point of the path.

2\. X coordinate of the point.

3\. Y coordinate of the point.

 |
| uint32\_t\* count | Size of the returned array, which is at least 6. The size of the point array after fitting is returned if **vals** is a null pointer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **path** or **count** is a null pointer.

**OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** if **acceptableError** is less than 0.

 |

#### \[h2\]OH\_Drawing\_PathInterpolate()

OH\_Drawing\_ErrorCode OH\_Drawing\_PathInterpolate(OH\_Drawing\_Path\* path, OH\_Drawing\_Path\* other,float weight, bool\* success, OH\_Drawing\_Path\* interpolatedPath)

**Description**

Interpolates between the existing path and another path based on the given weight and stores the result in the target path object.

Interpolation is achievable if the two paths have the same number of points. The target path is created based on the structure of the existing path.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* other | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object of the other path used for interpolation. |
| float weight | Interpolation weight. The value range is \[0, 1\]. |
| bool\* success | Whether the interpolation is successful. **true** means yes; **false** otherwise. It as an output parameter. |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* interpolatedPath | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object used to store the interpolation result. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **path**, **other**, **success**, or **interpolatedPath** is a null pointer.

**OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** if **weight** is not in the range of \[0, 1\].

 |

#### \[h2\]OH\_Drawing\_PathIsInterpolate()

OH\_Drawing\_ErrorCode OH\_Drawing\_PathIsInterpolate(OH\_Drawing\_Path\* path, OH\_Drawing\_Path\* other, bool\* result)

**Description**

Checks whether the existing path and another path (**other**) are compatible for interpolation in terms of structure and operation sequence.

If the paths contain conic operations, the weight values of the operations must be the same.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* other | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| bool\* result | 
Checks whether a path is compatible with another path. It is used as an output parameter.

**true** if the paths are compatible, **false** otherwise.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **path**, **other**, or **result** is a null pointer.

 |
