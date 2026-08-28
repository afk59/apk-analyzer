# drawing\_canvas.h

#### Overview

This file declares the functions related to the canvas in the drawing module.

By default, the canvas has a black brush with anti-aliasing enabled and without any other style. This brush takes effect only when no brush or pen is proactively set in the canvas.

**File to include**: <native\_drawing/drawing\_canvas.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_SrcRectConstraint](#oh_drawing_srcrectconstraint) | OH\_Drawing\_SrcRectConstraint | Defines an enum for the constraint types of the source rectangle. |
| [OH\_Drawing\_PointMode](#oh_drawing_pointmode) | OH\_Drawing\_PointMode | Defines an enum for the modes of drawing multiple points. The modes include discrete points, line segments, and open polygons. |
| [OH\_Drawing\_CanvasClipOp](#oh_drawing_canvasclipop) | OH\_Drawing\_CanvasClipOp | Defines an enum for the canvas clipping modes. |
| [OH\_Drawing\_CanvasShadowFlags](#oh_drawing_canvasshadowflags) | OH\_Drawing\_CanvasShadowFlags | Defines an enum for the shadow flags. |
| [OH\_Drawing\_VertexMode](#oh_drawing_vertexmode) | OH\_Drawing\_VertexMode | Defines an enum for the modes of interpreting the geometry of a given vertex. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas\* OH\_Drawing\_CanvasCreate(void)](#oh_drawing_canvascreate) | Creates an **OH\_Drawing\_Canvas** object. |
| [OH\_Drawing\_Canvas\* OH\_Drawing\_CanvasCreateWithPixelMap(OH\_Drawing\_PixelMap\* pixelMap)](#oh_drawing_canvascreatewithpixelmap) | 
Binds a pixel map to a canvas so that the content drawn on the canvas is output to the pixel map. (This process is called CPU rendering.) A canvas bound to a pixel map is a non-recording canvas.

You should unbind the pixel map object by calling [OH\_Drawing\_PixelMapDissolve](../drawing-pixel-map-h/document.md#oh_drawing_pixelmapdissolve) after the canvas object is destroyed.

 |
| [void OH\_Drawing\_CanvasDestroy(OH\_Drawing\_Canvas\* canvas)](#oh_drawing_canvasdestroy) | Destroys an **OH\_Drawing\_Canvas** object and reclaims the memory occupied by the object. |
| [void OH\_Drawing\_CanvasBind(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Bitmap\* bitmap)](#oh_drawing_canvasbind) | 

Binds a bitmap to a canvas so that the content drawn on the canvas is output to the bitmap. (This process is called CPU rendering.) A canvas bound to a bitmap is a non-recording canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasAttachPen(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Pen\* pen)](#oh_drawing_canvasattachpen) | 

Attaches a pen to a canvas so that the canvas can use the style and color of the pen to outline a shape. If the pen effect changes after this function is called, you must call the function again to use the new effect in the subsequent drawing.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasDetachPen(OH\_Drawing\_Canvas\* canvas)](#oh_drawing_canvasdetachpen) | 

Detaches the pen from a canvas so that the canvas can no longer use the style and color of the pen to outline a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasAttachBrush(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Brush\* brush)](#oh_drawing_canvasattachbrush) | 

Attaches a brush to a canvas so that the canvas can use the style and color of the brush to fill in a shape. If the brush effect changes after this function is called, you must call the function again to use the new effect in the subsequent drawing.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasDetachBrush(OH\_Drawing\_Canvas\* canvas)](#oh_drawing_canvasdetachbrush) | 

Detaches the brush from a canvas so that the canvas can no longer use the previously set brush to fill in a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasSave(OH\_Drawing\_Canvas\* canvas)](#oh_drawing_canvassave) | 

Saves the current canvas status (canvas matrix) to the top of the stack. This function works with [OH\_Drawing\_CanvasRestore](#oh_drawing_canvasrestore).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasSaveLayer(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect, const OH\_Drawing\_Brush\* brush)](#oh_drawing_canvassavelayer) | 

Saves the matrix and cropping region, and allocates a bitmap for subsequent drawing. If you call [OH\_Drawing\_CanvasRestore](#oh_drawing_canvasrestore), changes made to the matrix and clipping region are discarded, and the bitmap is drawn.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasRestore(OH\_Drawing\_Canvas\* canvas)](#oh_drawing_canvasrestore) | 

Restores the canvas status (canvas matrix) saved on the top of the stack.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [uint32\_t OH\_Drawing\_CanvasGetSaveCount(OH\_Drawing\_Canvas\* canvas)](#oh_drawing_canvasgetsavecount) | 

Obtains the number of canvas statuses (canvas matrices) saved in the stack.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasRestoreToCount(OH\_Drawing\_Canvas\* canvas, uint32\_t saveCount)](#oh_drawing_canvasrestoretocount) | 

Restores to a given number of canvas statuses (canvas matrices).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasDrawLine(OH\_Drawing\_Canvas\* canvas, float x1, float y1, float x2, float y2)](#oh_drawing_canvasdrawline) | 

Draws a line segment.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasDrawPath(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Path\* path)](#oh_drawing_canvasdrawpath) | 

Draws a path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawPixelMapNine(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_PixelMap\* pixelMap,const OH\_Drawing\_Rect\* center, const OH\_Drawing\_Rect\* dst, OH\_Drawing\_FilterMode mode)](#oh_drawing_canvasdrawpixelmapnine) | 

Splits a pixel map into nine sections using two horizontal and two vertical lines: four edge sections, four corner sections, and a central section.

If the four corner sections are smaller than the target rectangle, they will be drawn in the target rectangle without scaling. Otherwise, they will be scaled to fit the target rectangle.

Any remaining space will be filled by stretching or compressing the other five sections to cover the entire target rectangle.

 |
| [void OH\_Drawing\_CanvasDrawPixelMapRect(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_PixelMap\* pixelMap,const OH\_Drawing\_Rect\* src, const OH\_Drawing\_Rect\* dst, const OH\_Drawing\_SamplingOptions\* samplingOptions)](#oh_drawing_canvasdrawpixelmaprect) | 

Draws a portion of a pixel map onto a specified area of the canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If one of **canvas**, **pixelMap**, or **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasDrawBackground(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Brush\* brush)](#oh_drawing_canvasdrawbackground) | 

Draws a background filled with a brush.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasDrawRegion(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Region\* region)](#oh_drawing_canvasdrawregion) | 

Draws a region.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **region** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawPoint(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Point2D\* point)](#oh_drawing_canvasdrawpoint) | Draws a point. |
| [void OH\_Drawing\_CanvasDrawPoints(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_PointMode mode,uint32\_t count, const OH\_Drawing\_Point2D\* point2D)](#oh_drawing_canvasdrawpoints) | 

Draws multiple points. You can draw a single point, a line segment, or an open polygon.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **point2D** is NULL, or **count** is **0**, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned. If **mode** is not within the enumerated range, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_CanvasDrawBitmap(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Bitmap\* bitmap, float left, float top)](#oh_drawing_canvasdrawbitmap) | 

Draws a bitmap. A bitmap, also referred to as a dot matrix image, a pixel map image, or a grid image, includes single points called pixels (image elements).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasDrawBitmapRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Bitmap\* bitmap,const OH\_Drawing\_Rect\* src, const OH\_Drawing\_Rect\* dst, const OH\_Drawing\_SamplingOptions\* samplingOptions)](#oh_drawing_canvasdrawbitmaprect) | 

Draws a portion of a bitmap onto a specified area of the canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If one of **canvas**, **bitmap**, or **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasDrawRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect)](#oh_drawing_canvasdrawrect) | 

Draws a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **OH\_Drawing\_Rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasDrawCircle(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Point\* point, float radius)](#oh_drawing_canvasdrawcircle) | 

Draws a circle. This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget). If either **canvas** or **point** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **radius** is less than or equal to 0, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawColor(OH\_Drawing\_Canvas\* canvas, uint32\_t color,OH\_Drawing\_BlendMode blendMode)](#oh_drawing_canvasdrawcolor) | Fills the entire canvas with the specified color and blend mode. |
| [void OH\_Drawing\_CanvasDrawOval(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect)](#oh_drawing_canvasdrawoval) | Draws an oval. This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget). If either **canvas** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned. |
| [void OH\_Drawing\_CanvasDrawArc(OH\_Drawing\_Canvas\* canvas,const OH\_Drawing\_Rect\* rect, float startAngle, float sweepAngle)](#oh_drawing_canvasdrawarc) | 

Draws an arc. If the absolute value of the sweep angle exceeds 360 degrees, an ellipse is drawn.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawArcWithCenter(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect,float startAngle, float sweepAngle, bool useCenter)](#oh_drawing_canvasdrawarcwithcenter) | Draws an arc. It enables you to define the starting angle, sweep angle, and whether the arc's endpoints should connect to its center. |
| [void OH\_Drawing\_CanvasDrawRoundRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_RoundRect\* roundRect)](#oh_drawing_canvasdrawroundrect) | Draws a rounded rectangle. This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget). If either **canvas** or **roundRect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawNestedRoundRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_RoundRect\* outer,const OH\_Drawing\_RoundRect\* inner)](#oh_drawing_canvasdrawnestedroundrect) | Draws two nested rounded rectangles. The outer rectangle boundary must contain the inner rectangle boundary. Otherwise, there is no drawing effect. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawSingleCharacter(OH\_Drawing\_Canvas\* canvas, const char\* str,const OH\_Drawing\_Font\* font, float x, float y)](#oh_drawing_canvasdrawsinglecharacter) | Draws a single character. If the typeface of the current font does not support the character to draw, the system typeface is used to draw the character. |
| [void OH\_Drawing\_CanvasDrawTextBlob(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_TextBlob\* textBlob, float x, float y)](#oh_drawing_canvasdrawtextblob) | 

Draws a text blob. If the typeface used to construct **OH\_Drawing\_TextBlob** does not support a character, that character will not be drawn.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **textBlob** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasClipRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect,OH\_Drawing\_CanvasClipOp clipOp, bool doAntiAlias)](#oh_drawing_canvascliprect) | 

Clips a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **clipOp** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_CanvasClipRoundRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_RoundRect\* roundRect,OH\_Drawing\_CanvasClipOp clipOp, bool doAntiAlias)](#oh_drawing_canvascliproundrect) | 

Clips a rounded rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **roundRect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **clipOp** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_CanvasClipPath(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Path\* path,OH\_Drawing\_CanvasClipOp clipOp, bool doAntiAlias)](#oh_drawing_canvasclippath) | 

Clips a path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **clipOp** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasClipRegion(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Region\* region,OH\_Drawing\_CanvasClipOp clipOp)](#oh_drawing_canvasclipregion) | Clips a rectangle. |
| [void OH\_Drawing\_CanvasRotate(OH\_Drawing\_Canvas\* canvas, float degrees, float px, float py)](#oh_drawing_canvasrotate) | 

Rotates a canvas by a given angle. A positive value indicates a clockwise rotation, and a negative value indicates a counterclockwise rotation.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasTranslate(OH\_Drawing\_Canvas\* canvas, float dx, float dy)](#oh_drawing_canvastranslate) | 

Translates a canvas by a given distance.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasScale(OH\_Drawing\_Canvas\* canvas, float sx, float sy)](#oh_drawing_canvasscale) | 

Scales a canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasSkew(OH\_Drawing\_Canvas\* canvas, float sx, float sy)](#oh_drawing_canvasskew) | 

Skews a canvas. This function premultiplies the current canvas matrix by a skew transformation matrix and applies the resulting matrix to the canvas. The skew transformation matrix is as follows:

|1 sx 0|

|sy 1 0|

|0 0 1|.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [int32\_t OH\_Drawing\_CanvasGetWidth(OH\_Drawing\_Canvas\* canvas)](#oh_drawing_canvasgetwidth) | 

Obtains the canvas width.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [int32\_t OH\_Drawing\_CanvasGetHeight(OH\_Drawing\_Canvas\* canvas)](#oh_drawing_canvasgetheight) | 

Obtains the canvas height.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasGetLocalClipBounds(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Rect\* rect)](#oh_drawing_canvasgetlocalclipbounds) | 

Obtains the bounds of the cropping region of the canvas. This function cannot be used for a canvas of the recording type.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasGetTotalMatrix(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Matrix\* matrix)](#oh_drawing_canvasgettotalmatrix) | 

Obtains the 3x3 matrix of a canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasConcatMatrix(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Matrix\* matrix)](#oh_drawing_canvasconcatmatrix) | 

Preconcats the existing matrix of the canvas with the passed-in matrix. The drawing operation triggered before this API is called is not affected.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasDrawShadow(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Path\* path, OH\_Drawing\_Point3D planeParams,OH\_Drawing\_Point3D devLightPos, float lightRadius, uint32\_t ambientColor, uint32\_t spotColor,OH\_Drawing\_CanvasShadowFlags flag)](#oh_drawing_canvasdrawshadow) | 

Draws a spot shadow and uses a given path to outline the ambient shadow.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **flag** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [void OH\_Drawing\_CanvasClear(OH\_Drawing\_Canvas\* canvas, uint32\_t color)](#oh_drawing_canvasclear) | 

Clears a canvas by using a given color.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasSetMatrix(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Matrix\* matrix)](#oh_drawing_canvassetmatrix) | 

Sets the matrix status for a canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasResetMatrix(OH\_Drawing\_Canvas\* canvas)](#oh_drawing_canvasresetmatrix) | 

Resets the matrix of this canvas to an identity matrix.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasDrawImageRectWithSrc(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Image\* image,const OH\_Drawing\_Rect\* src, const OH\_Drawing\_Rect\* dst, const OH\_Drawing\_SamplingOptions\* samplingOptions,OH\_Drawing\_SrcRectConstraint srcRectConstraint)](#oh_drawing_canvasdrawimagerectwithsrc) | 

Draws a portion of an image onto a specified area of the canvas. The area selected by the source rectangle is scaled and translated to the destination rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If one of **canvas**, **image**, **src**, or **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasDrawImageRect(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Image\* image,OH\_Drawing\_Rect\* rect, OH\_Drawing\_SamplingOptions\* samplingOptions)](#oh_drawing_canvasdrawimagerect) | 

Draws an image onto a specified area of the canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If one of **canvas**, **image**, or **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [void OH\_Drawing\_CanvasDrawVertices(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_VertexMode vertexMmode,int32\_t vertexCount, const OH\_Drawing\_Point2D\* positions, const OH\_Drawing\_Point2D\* texs,const uint32\_t\* colors, int32\_t indexCount, const uint16\_t\* indices, OH\_Drawing\_BlendMode mode)](#oh_drawing_canvasdrawvertices) | 

Draws a triangular grid described by a vertex array.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **positions** is NULL, **vertexCount** is less than 3, or **indexCount** is less than 3 but not 0, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If either **vertexMmode** or **mode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

 |
| [bool OH\_Drawing\_CanvasReadPixels(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Image\_Info\* imageInfo,void\* dstPixels, uint32\_t dstRowBytes, int32\_t srcX, int32\_t srcY)](#oh_drawing_canvasreadpixels) | 

Copies pixel data from a canvas to a specified address. This function cannot be used for a canvas of the recording type.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If one of **canvas**, **imageInfo**, or **dstPixels** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [bool OH\_Drawing\_CanvasReadPixelsToBitmap(OH\_Drawing\_Canvas\* canvas,OH\_Drawing\_Bitmap\* bitmap, int32\_t srcX, int32\_t srcY)](#oh_drawing_canvasreadpixelstobitmap) | 

Copies pixel data from a canvas to an image. This function cannot be used for a canvas of the recording type.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasIsClipEmpty(OH\_Drawing\_Canvas\* canvas, bool\* isClipEmpty)](#oh_drawing_canvasisclipempty) | 

Checks whether the region that can be drawn is empty after clipping.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasGetImageInfo(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Image\_Info\* imageInfo)](#oh_drawing_canvasgetimageinfo) | 

Obtains the image information of a canvas.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawRecordCmd(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_RecordCmd\* recordCmd)](#oh_drawing_canvasdrawrecordcmd) | 

Draws an **OH\_Drawing\_RecordCmd** object.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawRecordCmdNesting(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_RecordCmd\* recordCmd)](#oh_drawing_canvasdrawrecordcmdnesting) | 

Draws an **OH\_Drawing\_RecordCmd** object. This API supports nesting.

Specifically, it can use the canvas object generated by [OH\_Drawing\_RecordCmdUtilsBeginRecording](../drawing-record-cmd-h/document.md#oh_drawing_recordcmdutilsbeginrecording) as the input parameter. However, multi-layer nesting is not recommended because it affects performance.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasQuickRejectPath(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Path\* path,bool\* quickReject)](#oh_drawing_canvasquickrejectpath) | 

Checks whether the path is not intersecting with the canvas area. The canvas area includes its boundaries.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasQuickRejectRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect,bool\* quickReject)](#oh_drawing_canvasquickrejectrect) | 

Checks whether the rectangle is not intersecting with the canvas area. The canvas area includes its boundaries.

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawPixelMapRectConstraint(OH\_Drawing\_Canvas\* canvas,OH\_Drawing\_PixelMap\* pixelMap, const OH\_Drawing\_Rect\* src, const OH\_Drawing\_Rect\* dst,const OH\_Drawing\_SamplingOptions\* samplingOptions, OH\_Drawing\_SrcRectConstraint constraint)](#oh_drawing_canvasdrawpixelmaprectconstraint) | Draws a portion of a pixel map onto a specified area of the canvas. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawSingleCharacterWithFeatures(OH\_Drawing\_Canvas\* canvas, const char\* str,const OH\_Drawing\_Font\* font, float x, float y, OH\_Drawing\_FontFeatures\* fontFeatures)](#oh_drawing_canvasdrawsinglecharacterwithfeatures) | Draws a single character with font features. If the typeface of the current font does not support the character to draw, the system typeface is used to draw the character. |

#### Enum Description

#### \[h2\]OH\_Drawing\_SrcRectConstraint

enum OH\_Drawing\_SrcRectConstraint

**Description**

Enumerates the constraint types of the source rectangle.

**Since**: 12

| Value | Description |
| :-- | :-- |
| STRICT\_SRC\_RECT\_CONSTRAINT | The source rectangle must be completely contained in the image. |
| FAST\_SRC\_RECT\_CONSTRAINT | The source rectangle can be partly outside the image. |

#### \[h2\]OH\_Drawing\_PointMode

enum OH\_Drawing\_PointMode

**Description**

Enumerates the modes of drawing multiple points. The modes include discrete points, line segments, and open polygons.

**Since**: 12

| Value | Description |
| :-- | :-- |
| POINT\_MODE\_POINTS | Draws each point separately. |
| POINT\_MODE\_LINES | Draws every two points as a line segment. |
| POINT\_MODE\_POLYGON | Draws an array of points as an open polygon. |

#### \[h2\]OH\_Drawing\_CanvasClipOp

enum OH\_Drawing\_CanvasClipOp

**Description**

Enumerates the canvas clipping modes.

**Since**: 11

| Value | Description |
| :-- | :-- |
| DIFFERENCE | Clips a specified area. That is, the difference set is obtained. |
| INTERSECT | Retains a specified area. That is, the intersection is obtained. |

#### \[h2\]OH\_Drawing\_CanvasShadowFlags

enum OH\_Drawing\_CanvasShadowFlags

**Description**

Enumerates the shadow flags.

**Since**: 12

| Value | Description |
| :-- | :-- |
| SHADOW\_FLAGS\_NONE | There is no shadow flag. |
| SHADOW\_FLAGS\_TRANSPARENT\_OCCLUDER | The occluding object is transparent. |
| SHADOW\_FLAGS\_GEOMETRIC\_ONLY | No analysis on the shadows is required. |
| SHADOW\_FLAGS\_ALL | All the preceding shadow flags are used. |

#### \[h2\]OH\_Drawing\_VertexMode

enum OH\_Drawing\_VertexMode

**Description**

Enumerates the modes of interpreting the geometry of a given vertex.

**Since**: 12

| Value | Description |
| :-- | :-- |
| VERTEX\_MODE\_TRIANGLES | Draws a triangle list. Specifically, a list of isolated triangles are drawn using every three vertices. If the number of vertices is not a multiple of 3, the extra vertices will be ignored. |
| VERTEX\_MODE\_TRIANGLES\_STRIP | Draws a triangle strip. Specifically, the first triangle is drawn between the first 3 vertices, and all subsequent triangles use the previous 2 vertices plus the next additional vertex. |
| VERTEX\_MODE\_TRIANGLE\_FAN | Draws a triangle fan. A triangle fan is similar to a triangle strip, except that all the triangles share one vertex (the first vertex). |

#### Function Description

#### \[h2\]OH\_Drawing\_CanvasDrawSingleCharacterWithFeatures()

OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawSingleCharacterWithFeatures(OH\_Drawing\_Canvas\* canvas, const char\* str, const OH\_Drawing\_Font\* font, float x, float y, OH\_Drawing\_FontFeatures\* fontFeatures)

**Description**

Draws a single character with font features. If the typeface of the current font does not support the character to draw, the system typeface is used to draw the character.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| const char\* str | Pointer to the single character to draw. A string can be passed in, but only the first character in the string is parsed and drawn in UTF-8 encoding. |
| [const OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| float x | X coordinate of the left point of the character baseline. |
| float y | Y coordinate of the left point of the character baseline. |
| [OH\_Drawing\_FontFeatures](../../structs/oh-drawing-fontfeatures/document.md)\* fontFeatures | Pointer to the [OH\_Drawing\_FontFeatures](../../structs/oh-drawing-fontfeatures/document.md) object. If no font feature is set, the preset font feature in the TrueType fonts (TTF) file is used. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if at least one of the parameters **canvas**, **str**, **font**, or **fontFeatures** is NULL, or the length of **str** is **0**.

 |

#### \[h2\]OH\_Drawing\_CanvasDrawPixelMapRectConstraint()

OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawPixelMapRectConstraint(OH\_Drawing\_Canvas\* canvas,OH\_Drawing\_PixelMap\* pixelMap, const OH\_Drawing\_Rect\* src, const OH\_Drawing\_Rect\* dst, const OH\_Drawing\_SamplingOptions\* samplingOptions, OH\_Drawing\_SrcRectConstraint constraint)

**Description**

Draws a portion of a pixel map onto a specified area of the canvas.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| [OH\_Drawing\_PixelMap](../../structs/oh-drawing-pixelmap/document.md)\* pixelMap | Pointer to the [OH\_Drawing\_PixelMap](../../structs/oh-drawing-pixelmap/document.md) object. |
| [const OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* src | Pointer to a rectangle on the pixel map. If NULL is passed in, it refers to the entire pixel map. |
| [const OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* dst | Pointer to a rectangle on the canvas. |
| [const OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md)\* samplingOptions | Pointer to the [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md) object. A null pointer means that the default sampling options are used. |
| [OH\_Drawing\_SrcRectConstraint](#oh_drawing_srcrectconstraint) constraint | Constraint type. For details about the available options, see [OH\_Drawing\_SrcRectConstraint](#oh_drawing_srcrectconstraint). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **canvas**, **pixelMap**, or **dst** is NULL.

 |

#### \[h2\]OH\_Drawing\_CanvasDrawRecordCmdNesting()

OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawRecordCmdNesting(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_RecordCmd\* recordCmd)

**Description**

Draws an **OH\_Drawing\_RecordCmd** object. This API supports nesting.

Specifically, it can use the canvas object generated by [OH\_Drawing\_RecordCmdUtilsBeginRecording](../drawing-record-cmd-h/document.md#oh_drawing_recordcmdutilsbeginrecording) as the input parameter. However, multi-layer nesting is not recommended because it affects performance.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Drawing\_Canvas\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. Only the canvas of the recording type is supported. |
| OH\_Drawing\_RecordCmd\* recordCmd | Pointer to the [OH\_Drawing\_RecordCmd](../../structs/oh-drawing-recordcmd/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Operation code.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if either **canvas** or **recordCmd** is NULL.

 |

#### \[h2\]OH\_Drawing\_CanvasCreate()

OH\_Drawing\_Canvas\* OH\_Drawing\_CanvasCreate(void)

**Description**

Creates an **OH\_Drawing\_Canvas** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* | Returns the pointer to the **OH\_Drawing\_Canvas** object created. |

#### \[h2\]OH\_Drawing\_CanvasCreateWithPixelMap()

OH\_Drawing\_Canvas\* OH\_Drawing\_CanvasCreateWithPixelMap(OH\_Drawing\_PixelMap\* pixelMap)

**Description**

Binds a pixel map to a canvas so that the content drawn on the canvas is output to the pixel map. (This process is called CPU rendering.) A canvas bound to a pixel map is a non-recording canvas.

You should unbind the pixel map object by calling [OH\_Drawing\_PixelMapDissolve](../drawing-pixel-map-h/document.md#oh_drawing_pixelmapdissolve) after the canvas object is destroyed.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_PixelMap](../../structs/oh-drawing-pixelmap/document.md)\* pixelMap | Pointer to the [OH\_Drawing\_PixelMap](../../structs/oh-drawing-pixelmap/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* | Pointer to the created canvas object [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md). If the returned object is NULL, the creation fails due to insufficient memory or an empty pixel map object. |

#### \[h2\]OH\_Drawing\_CanvasDestroy()

void OH\_Drawing\_CanvasDestroy(OH\_Drawing\_Canvas\* canvas)

**Description**

Destroys an **OH\_Drawing\_Canvas** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |

#### \[h2\]OH\_Drawing\_CanvasBind()

void OH\_Drawing\_CanvasBind(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Bitmap\* bitmap)

**Description**

Binds a bitmap to a canvas so that the content drawn on the canvas is output to the bitmap. (This process is called CPU rendering.) A canvas bound to a bitmap is a non-recording canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md)\* bitmap | Pointer to an **OH\_Drawing\_Bitmap** object. |

#### \[h2\]OH\_Drawing\_CanvasAttachPen()

void OH\_Drawing\_CanvasAttachPen(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Pen\* pen)

**Description**

Attaches a pen to a canvas so that the canvas can use the style and color of the pen to outline a shape. If the pen effect changes after this function is called, you must call the function again to use the new effect in the subsequent drawing.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **pen** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| const [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* pen | Pointer to an **OH\_Drawing\_Pen** object. |

#### \[h2\]OH\_Drawing\_CanvasDetachPen()

void OH\_Drawing\_CanvasDetachPen(OH\_Drawing\_Canvas\* canvas)

**Description**

Detaches the pen from a canvas so that the canvas can no longer use the style and color of the pen to outline a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |

#### \[h2\]OH\_Drawing\_CanvasAttachBrush()

void OH\_Drawing\_CanvasAttachBrush(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Brush\* brush)

**Description**

Attaches a brush to a canvas so that the canvas can use the style and color of the brush to fill in a shape. If the brush effect changes after this function is called, you must call the function again to use the new effect in the subsequent drawing.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| const [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an **OH\_Drawing\_Brush** object. |

#### \[h2\]OH\_Drawing\_CanvasDetachBrush()

void OH\_Drawing\_CanvasDetachBrush(OH\_Drawing\_Canvas\* canvas)

**Description**

Detaches the brush from a canvas so that the canvas can no longer use the previously set brush to fill in a shape.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |

#### \[h2\]OH\_Drawing\_CanvasSave()

void OH\_Drawing\_CanvasSave(OH\_Drawing\_Canvas\* canvas)

**Description**

Saves the current canvas status (canvas matrix) to the top of the stack. This function works with [OH\_Drawing\_CanvasRestore](#oh_drawing_canvasrestore).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |

#### \[h2\]OH\_Drawing\_CanvasSaveLayer()

void OH\_Drawing\_CanvasSaveLayer(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect, const OH\_Drawing\_Brush\* brush)

**Description**

Saves the matrix and cropping region, and allocates a bitmap for subsequent drawing. If you call [OH\_Drawing\_CanvasRestore](#oh_drawing_canvasrestore), changes made to the matrix and clipping region are discarded, and the bitmap is drawn.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object, which is used to limit the layer size. A null pointer means no limit. |
| const [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object. The alpha value, filter effect, and blend mode of the brush are applied when the bitmap is drawn. If NULL is passed in, no effect is applied. |

#### \[h2\]OH\_Drawing\_CanvasRestore()

void OH\_Drawing\_CanvasRestore(OH\_Drawing\_Canvas\* canvas)

**Description**

Restores the canvas status (canvas matrix) saved on the top of the stack.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |

#### \[h2\]OH\_Drawing\_CanvasGetSaveCount()

uint32\_t OH\_Drawing\_CanvasGetSaveCount(OH\_Drawing\_Canvas\* canvas)

**Description**

Obtains the number of canvas statuses (canvas matrices) saved in the stack.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Returns a 32-bit value that describes the number of canvas statuses (canvas matrices). The initial number is **1**. |

#### \[h2\]OH\_Drawing\_CanvasRestoreToCount()

void OH\_Drawing\_CanvasRestoreToCount(OH\_Drawing\_Canvas\* canvas, uint32\_t saveCount)

**Description**

Restores to a given number of canvas statuses (canvas matrices).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| uint32\_t saveCount | Number of canvas statuses (canvas matrices). If the value is less than or equal to 1, the canvas is restored to the initial state. If the value is greater than the number of canvas statuses that have been saved, no operation is performed. |

#### \[h2\]OH\_Drawing\_CanvasDrawLine()

void OH\_Drawing\_CanvasDrawLine(OH\_Drawing\_Canvas\* canvas, float x1, float y1, float x2, float y2)

**Description**

Draws a line segment.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| float x1 | X coordinate of the start point of the line segment. |
| float y1 | Y coordinate of the start point of the line segment. |
| float x2 | X coordinate of the end point of the line segment. |
| float y2 | Y coordinate of the end point of the line segment. |

#### \[h2\]OH\_Drawing\_CanvasDrawPath()

void OH\_Drawing\_CanvasDrawPath(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Path\* path)

**Description**

Draws a path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| const [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to an **OH\_Drawing\_Path** object. |

#### \[h2\]OH\_Drawing\_CanvasDrawPixelMapNine()

OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawPixelMapNine(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_PixelMap\* pixelMap,const OH\_Drawing\_Rect\* center, const OH\_Drawing\_Rect\* dst, OH\_Drawing\_FilterMode mode)

**Description**

Splits a pixel map into nine sections using two horizontal and two vertical lines: four edge sections, four corner sections, and a central section.

If the four corner sections are smaller than the target rectangle, they will be drawn in the target rectangle without scaling. Otherwise, they will be scaled to fit the target rectangle.

Any remaining space will be filled by stretching or compressing the other five sections to cover the entire target rectangle.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| [OH\_Drawing\_PixelMap](../../structs/oh-drawing-pixelmap/document.md)\* pixelMap | Pointer to the [OH\_Drawing\_PixelMap](../../structs/oh-drawing-pixelmap/document.md) object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* center | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object, which indicates the central rectangle splitting the pixel map. It divides the image into nine sections by extending its four edges. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* dst | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object, which indicates the target region on the canvas. |
| [OH\_Drawing\_FilterMode](../drawing-sampling-options-h/document.md#oh_drawing_filtermode) mode | Enumeration of filter modes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **canvas**, **pixelMap**, or **dst** is NULL.

 |

#### \[h2\]OH\_Drawing\_CanvasDrawPixelMapRect()

void OH\_Drawing\_CanvasDrawPixelMapRect(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_PixelMap\* pixelMap,const OH\_Drawing\_Rect\* src, const OH\_Drawing\_Rect\* dst, const OH\_Drawing\_SamplingOptions\* samplingOptions)

**Description**

Draws a portion of a pixel map onto a specified area of the canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If one of **canvas**, **pixelMap**, or **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| [OH\_Drawing\_PixelMap](../../structs/oh-drawing-pixelmap/document.md)\* pixelMap | Pointer to the [OH\_Drawing\_PixelMap](../../structs/oh-drawing-pixelmap/document.md) object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* src | Pointer to a rectangle on the pixel map. If NULL is passed in, it refers to the entire pixel map. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* dst | Pointer to a rectangle on the canvas. |
| const [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md)\* samplingOptions | Pointer to the [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md) object. A null pointer means that the default sampling options are used. |

#### \[h2\]OH\_Drawing\_CanvasDrawBackground()

void OH\_Drawing\_CanvasDrawBackground(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Brush\* brush)

**Description**

Draws a background filled with a brush.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **brush** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| const [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* brush | Pointer to an **OH\_Drawing\_Brush** object. |

#### \[h2\]OH\_Drawing\_CanvasDrawRegion()

void OH\_Drawing\_CanvasDrawRegion(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Region\* region)

**Description**

Draws a region.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **region** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| const [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md)\* region | Pointer to an **OH\_Drawing\_Region** object. |

#### \[h2\]OH\_Drawing\_CanvasDrawPoint()

OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawPoint(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Point2D\* point)

**Description**

Draws a point.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| const [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* point | Pointer to the [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if either **canvas** or **point** is NULL.

 |

#### \[h2\]OH\_Drawing\_CanvasDrawPoints()

void OH\_Drawing\_CanvasDrawPoints(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_PointMode mode,uint32\_t count, const OH\_Drawing\_Point2D\* point2D)

**Description**

Draws multiple points. You can draw a single point, a line segment, or an open polygon.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **point2D** is NULL, or **count** is **0**, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned. If **mode** is not within the enumerated range, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| [OH\_Drawing\_PointMode](#oh_drawing_pointmode) mode | Mode for drawing multiple points. For details, see [OH\_Drawing\_PointMode](#oh_drawing_pointmode). |
| uint32\_t count | Number of vertices, that is, the number of vertices in the vertex array. |
| const [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* point2D | Pointer to an array holding the vertices. |

#### \[h2\]OH\_Drawing\_CanvasDrawBitmap()

void OH\_Drawing\_CanvasDrawBitmap(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Bitmap\* bitmap, float left, float top)

**Description**

Draws a bitmap. A bitmap, also referred to as a dot matrix image, a pixel map image, or a grid image, includes single points called pixels (image elements).

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| const [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md)\* bitmap | Pointer to an **OH\_Drawing\_Bitmap** object. |
| float left | X coordinate of the upper left corner of the bitmap. |
| float top | Y coordinate of the upper left corner of the bitmap. |

#### \[h2\]OH\_Drawing\_CanvasDrawBitmapRect()

void OH\_Drawing\_CanvasDrawBitmapRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Bitmap\* bitmap,const OH\_Drawing\_Rect\* src, const OH\_Drawing\_Rect\* dst, const OH\_Drawing\_SamplingOptions\* samplingOptions)

**Description**

Draws a portion of a bitmap onto a specified area of the canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If one of **canvas**, **bitmap**, or **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| const [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md)\* bitmap | Pointer to the [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md) object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* src | Pointer to a rectangle on the bitmap. If NULL is passed in, it refers to the entire bitmap. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* dst | Pointer to a rectangle on the canvas. |
| const [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md)\* samplingOptions | Pointer to the [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md) object. A null pointer means that the default sampling options are used. |

#### \[h2\]OH\_Drawing\_CanvasDrawRect()

void OH\_Drawing\_CanvasDrawRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect)

**Description**

Draws a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **OH\_Drawing\_Rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |

#### \[h2\]OH\_Drawing\_CanvasDrawCircle()

void OH\_Drawing\_CanvasDrawCircle(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Point\* point, float radius)

**Description**

Draws a circle. This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget). If either **canvas** or **point** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **radius** is less than or equal to 0, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| const [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md)\* point | Pointer to an **OH\_Drawing\_Point** object, which indicates the center of the circle. |
| float radius | Radius of the circle. The value is invalid if it is less than or equal to 0. |

#### \[h2\]OH\_Drawing\_CanvasDrawColor()

OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawColor(OH\_Drawing\_Canvas\* canvas, uint32\_t color,OH\_Drawing\_BlendMode blendMode)

**Description**

Fills the entire canvas with the specified color and blend mode.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| uint32\_t color | Color, represented by a 32-bit (ARGB) variable. |
| [OH\_Drawing\_BlendMode](../drawing-types-h/document.md#oh_drawing_blendmode) blendMode | Blend mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **canvas** is NULL.

**OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** if **blendMode** is not set to one of the enumerated values.

 |

#### \[h2\]OH\_Drawing\_CanvasDrawOval()

void OH\_Drawing\_CanvasDrawOval(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect)

**Description**

Draws an oval. This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget). If either **canvas** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |

#### \[h2\]OH\_Drawing\_CanvasDrawArc()

void OH\_Drawing\_CanvasDrawArc(OH\_Drawing\_Canvas\* canvas,const OH\_Drawing\_Rect\* rect, float startAngle, float sweepAngle)

**Description**

Draws an arc. If the absolute value of the sweep angle exceeds 360 degrees, an ellipse is drawn.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |
| float startAngle | Start angle. When the degree is 0, the start point is located at the right end of the oval. A positive number indicates that the start point is placed clockwise, and a negative number indicates that the start point is placed counterclockwise. |
| float sweepAngle | Angle to sweep, in degrees. A positive number indicates a clockwise sweep, and a negative value indicates a counterclockwise swipe. The valid range is from -360 degrees to 360 degrees. If the absolute value of the sweep angle exceeds 360 degrees, an ellipse is drawn. |

#### \[h2\]OH\_Drawing\_CanvasDrawArcWithCenter()

OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawArcWithCenter(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect,float startAngle, float sweepAngle, bool useCenter)

**Description**

Draws an arc. It enables you to define the start angle, sweep angle, and whether the arc's endpoints should connect to its center.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object. |
| float startAngle | Start angle, in degrees. The value is a floating point number. When the degree is 0, the start point is located at the right end of the oval. A positive number indicates that the start point is placed clockwise, and a negative number indicates that the start point is placed counterclockwise. |
| float sweepAngle | Angle to sweep, in degrees. The value is a floating point number. A positive number indicates a clockwise sweep, and a negative value indicates a counterclockwise swipe. The swipe angle can exceed 360 degrees, and a complete ellipse is drawn. |
| bool useCenter | Whether the start point and end point of the arc are connected to its center. The value **true** means that they are connected to the center; the value **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if either **canvas** or **rect** is NULL.

 |

#### \[h2\]OH\_Drawing\_CanvasDrawRoundRect()

void OH\_Drawing\_CanvasDrawRoundRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_RoundRect\* roundRect)

**Description**

Draws a rounded rectangle. This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget). If either **canvas** or **roundRect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| const [OH\_Drawing\_RoundRect](../../structs/oh-drawing-roundrect/document.md)\* roundRect | Pointer to an **OH\_Drawing\_RoundRect** object. |

#### \[h2\]OH\_Drawing\_CanvasDrawNestedRoundRect()

OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawNestedRoundRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_RoundRect\* outer,const OH\_Drawing\_RoundRect\* inner)

**Description**

Draws two nested rounded rectangles. The outer rectangle boundary must contain the inner rectangle boundary. Otherwise, there is no drawing effect.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| const [OH\_Drawing\_RoundRect](../../structs/oh-drawing-roundrect/document.md)\* outer | Pointer to the [OH\_Drawing\_RoundRect](../../structs/oh-drawing-roundrect/document.md) object, indicating the outer rounded rectangle. |
| const [OH\_Drawing\_RoundRect](../../structs/oh-drawing-roundrect/document.md)\* inner | Pointer to the [OH\_Drawing\_RoundRect](../../structs/oh-drawing-roundrect/document.md) object, indicating the inner rounded rectangle. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **canvas**, **outer**, or **inner** is NULL.

 |

#### \[h2\]OH\_Drawing\_CanvasDrawSingleCharacter()

OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawSingleCharacter(OH\_Drawing\_Canvas\* canvas, const char\* str,const OH\_Drawing\_Font\* font, float x, float y)

**Description**

Draws a single character. If the typeface of the current font does not support the character to draw, the system typeface is used to draw the character.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| const char\* str | Pointer to the single character to draw. A string can be passed in, but only the first character in the string is parsed and drawn in UTF-8 encoding. |
| const [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md)\* font | Pointer to the [OH\_Drawing\_Font](../../structs/oh-drawing-font/document.md) object. |
| float x | X coordinate of the left point of the character baseline. |
| float y | Y coordinate of the left point of the character baseline. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if at least one of the parameters **canvas**, **str**, or **font** is NULL, or the length of **str** is **0**.

 |

#### \[h2\]OH\_Drawing\_CanvasDrawTextBlob()

void OH\_Drawing\_CanvasDrawTextBlob(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_TextBlob\* textBlob, float x, float y)

**Description**

Draws a text blob. If the typeface used to construct **OH\_Drawing\_TextBlob** does not support a character, that character will not be drawn.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **textBlob** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| const [OH\_Drawing\_TextBlob](../../structs/oh-drawing-textblob/document.md)\* textBlob | Pointer to an **OH\_Drawing\_TextBlob** object. |
| float x | X coordinate of the left point of the text baseline. |
| float y | Y coordinate of the left point of the text baseline. |

#### \[h2\]OH\_Drawing\_CanvasClipRect()

void OH\_Drawing\_CanvasClipRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect,OH\_Drawing\_CanvasClipOp clipOp, bool doAntiAlias)

**Description**

Clips a rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **clipOp** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to an **OH\_Drawing\_Rect** object. |
| [OH\_Drawing\_CanvasClipOp](#oh_drawing_canvasclipop) clipOp | Clip mode. For details about the available options, see [OH\_Drawing\_CanvasClipOp](#oh_drawing_canvasclipop). |
| bool doAntiAlias | Whether to enable anti-aliasing. The value **true** means to enable anti-aliasing, and **false** means the opposite. |

#### \[h2\]OH\_Drawing\_CanvasClipRoundRect()

void OH\_Drawing\_CanvasClipRoundRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_RoundRect\* roundRect,OH\_Drawing\_CanvasClipOp clipOp, bool doAntiAlias)

**Description**

Clips a rounded rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **roundRect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **clipOp** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| const [OH\_Drawing\_RoundRect](../../structs/oh-drawing-roundrect/document.md)\* roundRect | Pointer to an **OH\_Drawing\_RoundRect** object. |
| [OH\_Drawing\_CanvasClipOp](#oh_drawing_canvasclipop) clipOp | Clip mode. For details about the available options, see [OH\_Drawing\_CanvasClipOp](#oh_drawing_canvasclipop). |
| bool doAntiAlias | Whether to perform anti-aliasing. The value **true** means to perform anti-aliasing, and **false** means the opposite. |

#### \[h2\]OH\_Drawing\_CanvasClipPath()

void OH\_Drawing\_CanvasClipPath(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Path\* path,OH\_Drawing\_CanvasClipOp clipOp, bool doAntiAlias)

**Description**

Clips a path.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **clipOp** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| const [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to an **OH\_Drawing\_Path** object. |
| [OH\_Drawing\_CanvasClipOp](#oh_drawing_canvasclipop) clipOp | Clip mode. For details about the available options, see [OH\_Drawing\_CanvasClipOp](#oh_drawing_canvasclipop). |
| bool doAntiAlias | Whether to enable anti-aliasing. The value **true** means to enable anti-aliasing, and **false** means the opposite. |

#### \[h2\]OH\_Drawing\_CanvasClipRegion()

OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasClipRegion(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Region\* region,OH\_Drawing\_CanvasClipOp clipOp)

**Description**

Clips a rectangle.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| const [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md)\* region | Pointer to the [OH\_Drawing\_Region](../../structs/oh-drawing-region/document.md) object. |
| [OH\_Drawing\_CanvasClipOp](#oh_drawing_canvasclipop) clipOp | Clip mode. For details about the available options, see [OH\_Drawing\_CanvasClipOp](#oh_drawing_canvasclipop). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if either **canvas** or **region** is NULL.

**OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** if **clipOp** is not set to one of the enumerated values.

 |

#### \[h2\]OH\_Drawing\_CanvasRotate()

void OH\_Drawing\_CanvasRotate(OH\_Drawing\_Canvas\* canvas, float degrees, float px, float py)

**Description**

Rotates a canvas by a given angle. A positive value indicates a clockwise rotation, and a negative value indicates a counterclockwise rotation.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| float degrees | Rotation angle. |
| float px | X coordinate of the rotation point. |
| float py | Y coordinate of the rotation point. |

#### \[h2\]OH\_Drawing\_CanvasTranslate()

void OH\_Drawing\_CanvasTranslate(OH\_Drawing\_Canvas\* canvas, float dx, float dy)

**Description**

Translates a canvas by a given distance.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| float dx | Distance to translate on the X axis. |
| float dy | Distance to translate on the Y axis. |

#### \[h2\]OH\_Drawing\_CanvasScale()

void OH\_Drawing\_CanvasScale(OH\_Drawing\_Canvas\* canvas, float sx, float sy)

**Description**

Scales a canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| float sx | Scale ratio on the X axis. |
| float sy | Scale ratio on the Y axis. |

#### \[h2\]OH\_Drawing\_CanvasSkew()

void OH\_Drawing\_CanvasSkew(OH\_Drawing\_Canvas\* canvas, float sx, float sy)

**Description**

Skews a canvas. This function premultiplies the current canvas matrix by a skew transformation matrix and applies the resulting matrix to the canvas. The skew transformation matrix is as follows:

|1 sx 0|

|sy 1 0|

|0 0 1|

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| float sx | Amount of tilt on the X axis. A positive number tilts the drawing rightwards along the positive direction of the Y axis, and a negative number tilts the drawing leftwards along the positive direction of the Y axis. |
| float sy | Amount of tilt on the Y axis. A positive number tilts the drawing downwards along the positive direction of the X axis, and a negative number tilts the drawing upwards along the positive direction of the X axis. |

#### \[h2\]OH\_Drawing\_CanvasGetWidth()

int32\_t OH\_Drawing\_CanvasGetWidth(OH\_Drawing\_Canvas\* canvas)

**Description**

Obtains the canvas width.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns the canvas width, in px. |

#### \[h2\]OH\_Drawing\_CanvasGetHeight()

int32\_t OH\_Drawing\_CanvasGetHeight(OH\_Drawing\_Canvas\* canvas)

**Description**

Obtains the canvas height.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns the canvas height, in pixels. |

#### \[h2\]OH\_Drawing\_CanvasGetLocalClipBounds()

void OH\_Drawing\_CanvasGetLocalClipBounds(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Rect\* rect)

**Description**

Obtains the bounds of the cropping region of the canvas. This function cannot be used for a canvas of the recording type.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **rect** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object. You can call [OH\_Drawing\_RectCreate](../drawing-rect-h/document.md#oh_drawing_rectcreate) to create a rectangle object. |

#### \[h2\]OH\_Drawing\_CanvasGetTotalMatrix()

void OH\_Drawing\_CanvasGetTotalMatrix(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Matrix\* matrix)

**Description**

Obtains the 3x3 matrix of a canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. You can call [OH\_Drawing\_MatrixCreate](../drawing-matrix-h/document.md#oh_drawing_matrixcreate) to create a matrix object. |

#### \[h2\]OH\_Drawing\_CanvasConcatMatrix()

void OH\_Drawing\_CanvasConcatMatrix(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Matrix\* matrix)

**Description**

Preconcats the existing matrix of the canvas with the passed-in matrix. The drawing operation triggered before this API is called is not affected.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. |

#### \[h2\]OH\_Drawing\_CanvasDrawShadow()

void OH\_Drawing\_CanvasDrawShadow(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Path\* path, OH\_Drawing\_Point3D planeParams,OH\_Drawing\_Point3D devLightPos, float lightRadius, uint32\_t ambientColor, uint32\_t spotColor,OH\_Drawing\_CanvasShadowFlags flag)

**Description**

Draws a spot shadow and uses a given path to outline the ambient shadow.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **path** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If **flag** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object, which is used to generate shadows. |
| [OH\_Drawing\_Point3D](../../structs/oh-drawing-point3d/document.md) planeParams | Z-axis offset of an occluder relative to the canvas, based on its x and y coordinates. |
| [OH\_Drawing\_Point3D](../../structs/oh-drawing-point3d/document.md) devLightPos | Position of the light relative to the canvas. |
| float lightRadius | Radius of the light source. The value must be greater than or equal to 0. |
| uint32\_t ambientColor | Ambient shadow color, which is represented by a 32-bit (ARGB) variable. |
| uint32\_t spotColor | Point shadow color, which is represented by a 32-bit (ARGB) variable. |
| [OH\_Drawing\_CanvasShadowFlags](#oh_drawing_canvasshadowflags) flag | Enumeration of shadow flags. |

#### \[h2\]OH\_Drawing\_CanvasClear()

void OH\_Drawing\_CanvasClear(OH\_Drawing\_Canvas\* canvas, uint32\_t color)

**Description**

Clears a canvas by using a given color.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| uint32\_t color | Color, which is a 32-bit (ARGB) variable. |

#### \[h2\]OH\_Drawing\_CanvasSetMatrix()

void OH\_Drawing\_CanvasSetMatrix(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Matrix\* matrix)

**Description**

Sets the matrix status for a canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **matrix** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md)\* matrix | Pointer to the [OH\_Drawing\_Matrix](../../structs/oh-drawing-matrix/document.md) object. You can call [OH\_Drawing\_MatrixCreate](../drawing-matrix-h/document.md#oh_drawing_matrixcreate) to create a matrix object. |

#### \[h2\]OH\_Drawing\_CanvasResetMatrix()

void OH\_Drawing\_CanvasResetMatrix(OH\_Drawing\_Canvas\* canvas)

**Description**

Resets the matrix of this canvas to an identity matrix.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If **canvas** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |

#### \[h2\]OH\_Drawing\_CanvasDrawImageRectWithSrc()

void OH\_Drawing\_CanvasDrawImageRectWithSrc(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Image\* image,const OH\_Drawing\_Rect\* src, const OH\_Drawing\_Rect\* dst, const OH\_Drawing\_SamplingOptions\* samplingOptions,OH\_Drawing\_SrcRectConstraint srcRectConstraint)

**Description**

Draws a portion of an image onto a specified area of the canvas. The area selected by the source rectangle is scaled and translated to the destination rectangle.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If one of **canvas**, **image**, **src**, or **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| const [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md)\* image | Pointer to the [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md) object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* src | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* dst | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object. |
| const [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md)\* samplingOptions | Pointer to the [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md) object. A null pointer means that the default sampling options are used. |
| [OH\_Drawing\_SrcRectConstraint](#oh_drawing_srcrectconstraint) srcRectConstraint | Constraint type. For details about the available options, see [OH\_Drawing\_SrcRectConstraint](#oh_drawing_srcrectconstraint). |

#### \[h2\]OH\_Drawing\_CanvasDrawImageRect()

void OH\_Drawing\_CanvasDrawImageRect(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Image\* image,OH\_Drawing\_Rect\* rect, OH\_Drawing\_SamplingOptions\* samplingOptions)

**Description**

Draws an image onto a specified area of the canvas.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If one of **canvas**, **image**, or **dst** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md)\* image | Pointer to the [OH\_Drawing\_Image](../../structs/oh-drawing-image/document.md) object. |
| [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object. |
| [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md)\* samplingOptions | Pointer to the [OH\_Drawing\_SamplingOptions](../../structs/oh-drawing-samplingoptions/document.md) object. A null pointer means that the default sampling options are used. |

#### \[h2\]OH\_Drawing\_CanvasDrawVertices()

void OH\_Drawing\_CanvasDrawVertices(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_VertexMode vertexMmode,int32\_t vertexCount, const OH\_Drawing\_Point2D\* positions, const OH\_Drawing\_Point2D\* texs,const uint32\_t\* colors, int32\_t indexCount, const uint16\_t\* indices, OH\_Drawing\_BlendMode mode)

**Description**

Draws a triangular grid described by a vertex array.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **positions** is NULL, **vertexCount** is less than 3, or **indexCount** is less than 3 but not 0, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

If either **vertexMmode** or **mode** is not set to one of the enumerated values, **OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to an **OH\_Drawing\_Canvas** object. |
| [OH\_Drawing\_VertexMode](#oh_drawing_vertexmode) vertexMmode | Mode for drawing vertices. For details about the available options, see [OH\_Drawing\_VertexMode](#oh_drawing_vertexmode). |
| int32\_t vertexCount | Number of elements in the vertex array. The value must be greater than or equal to 3. |
| const [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* positions | Pointer to the array that holds the position of every vertex. The array cannot be null and its length must be equal to the value of **vertexCount**. |
| const [OH\_Drawing\_Point2D](../../structs/oh-drawing-point2d/document.md)\* texs | Pointer to the array that holds the texture space coordinate corresponding to each vertex. The array can be null. If the array is not null, its length must be equal to the value of **vertexCount**. |
| const uint32\_t\* colors | Pointer to the array that holds the color corresponding to each vertex. It is used for interpolation in a triangle. The array can be null. If the array is not null, its length must be equal to the value of **vertexCount**. |
| int32\_t indexCount | Number of indices. The value can be 0 or a value greater than or equal to 3. |
| const uint16\_t\* indices | Pointer to the array that holds the index of each vertex. The array can be null. If the array is not null, its length must be equal to the value of **indexCount**. |
| [OH\_Drawing\_BlendMode](../drawing-types-h/document.md#oh_drawing_blendmode) mode | Enumeration of blend modes. For details about the available options, see [OH\_Drawing\_BlendMode](../drawing-types-h/document.md#oh_drawing_blendmode). |

#### \[h2\]OH\_Drawing\_CanvasReadPixels()

bool OH\_Drawing\_CanvasReadPixels(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Image\_Info\* imageInfo,void\* dstPixels, uint32\_t dstRowBytes, int32\_t srcX, int32\_t srcY)

**Description**

Copies pixel data from a canvas to a specified address. This function cannot be used for a canvas of the recording type.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If one of **canvas**, **imageInfo**, or **dstPixels** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| [OH\_Drawing\_Image\_Info](../../structs/oh-drawing-image-info/document.md)\* imageInfo | Pointer to the [OH\_Drawing\_Image\_Info](../../structs/oh-drawing-image-info/document.md) object. |
| void\* dstPixels | Pointer to the start address for storing the pixel data. |
| uint32\_t dstRowBytes | Number of bytes in each row of pixels. The value is invalid if it is less than or equal to 0. |
| int32\_t srcX | X offset of the pixels on the canvas, in px. |
| int32\_t srcY | Y offset of the pixels on the canvas, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the pixel data is copied to the start address of the storage; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_CanvasReadPixelsToBitmap()

bool OH\_Drawing\_CanvasReadPixelsToBitmap(OH\_Drawing\_Canvas\* canvas,OH\_Drawing\_Bitmap\* bitmap, int32\_t srcX, int32\_t srcY)

**Description**

Copies pixel data from a canvas to an image. This function cannot be used for a canvas of the recording type.

This API may return an error code. For details, call [OH\_Drawing\_ErrorCodeGet](../drawing-error-code-h/document.md#oh_drawing_errorcodeget).

If either **canvas** or **bitmap** is NULL, **OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md)\* bitmap | Pointer to the [OH\_Drawing\_Bitmap](../../structs/oh-drawing-bitmap/document.md) object. |
| int32\_t srcX | X offset of the pixels on the canvas, in px. |
| int32\_t srcY | Y offset of the pixels on the canvas, in px. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the pixel data is copied to the image; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_CanvasIsClipEmpty()

OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasIsClipEmpty(OH\_Drawing\_Canvas\* canvas, bool\* isClipEmpty)

**Description**

Checks whether the region that can be drawn is empty after clipping.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| bool\* isClipEmpty | Pointer to the variable that specifies whether the region is empty. The value **true** means that the region is empty, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if either **canvas** or **isClipEmpty** is NULL.

 |

#### \[h2\]OH\_Drawing\_CanvasGetImageInfo()

OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasGetImageInfo(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Image\_Info\* imageInfo)

**Description**

Obtains the image information of a canvas.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| [OH\_Drawing\_Image\_Info](../../structs/oh-drawing-image-info/document.md)\* imageInfo | Pointer to the [OH\_Drawing\_Image\_Info](../../structs/oh-drawing-image-info/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if either **canvas** or **imageInfo** is NULL.

 |

#### \[h2\]OH\_Drawing\_CanvasDrawRecordCmd()

OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawRecordCmd(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_RecordCmd\* recordCmd)

**Description**

Draws an **OH\_Drawing\_RecordCmd** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. Only the canvas of the recording type is supported. |
| [OH\_Drawing\_RecordCmd](../../structs/oh-drawing-recordcmd/document.md)\* recordCmd | Pointer to the [OH\_Drawing\_RecordCmd](../../structs/oh-drawing-recordcmd/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if either **canvas** or **recordCmd** is NULL.

 |

#### \[h2\]OH\_Drawing\_CanvasQuickRejectPath()

OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasQuickRejectPath(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Path\* path,bool\* quickReject)

**Description**

Checks whether the path is not intersecting with the canvas area. The canvas area includes its boundaries.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| const [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md) object. |
| bool\* quickReject | Pointer to the check result. The value **true** means that the path is not intersecting with the canvas area, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **canvas**, **path**, or **quickReject** is NULL.

 |

#### \[h2\]OH\_Drawing\_CanvasQuickRejectRect()

OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasQuickRejectRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect,bool\* quickReject)

**Description**

Checks whether the rectangle is not intersecting with the canvas area. The canvas area includes its boundaries.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md) object. |
| const [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md)\* rect | Pointer to the [OH\_Drawing\_Rect](../../structs/oh-drawing-rect/document.md) object. |
| bool\* quickReject | Pointer to the check result. The value **true** means that the rectangle is not intersecting with the canvas area, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns one of the following result codes:

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **canvas**, **rect**, or **quickReject** is NULL.

 |
