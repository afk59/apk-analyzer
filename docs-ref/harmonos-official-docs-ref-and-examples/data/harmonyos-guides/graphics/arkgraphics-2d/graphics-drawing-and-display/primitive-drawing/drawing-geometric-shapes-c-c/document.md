# Drawing Geometric Shapes (C/C++)

#### Overview

Geometric shapes that can be drawn currently include:

-   Point
    
-   Arc
    
-   Circle
    
-   Path
    
-   Region
    
-   Box
    
-   Rounded rectangle
    

Most geometric shapes can be drawn using a brush or a paintbrush. Points can be drawn only using a brush.

#### Available APIs

The following table lists the common APIs for drawing geometric shapes. For details about the APIs and parameters, see [drawing\_canvas.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-canvas-h).

| API | Description |
| :-- | :-- |
| OH\_Drawing\_Point\* OH\_Drawing\_PointCreate (float x, float y) | Creates an **OH\_Drawing\_Point** object. |
| OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawPoint (OH\_Drawing\_Canvas \*canvas, const OH\_Drawing\_Point2D \*point) | Draws a point. |
| OH\_Drawing\_Rect\* OH\_Drawing\_RectCreate (float left, float top, float right, float bottom) | Creates an **OH\_Drawing\_Rect** object. |
| void OH\_Drawing\_CanvasDrawArc (OH\_Drawing\_Canvas\*, const OH\_Drawing\_Rect\*, float startAngle, float sweepAngle) | Draws an arc. |
| void OH\_Drawing\_CanvasDrawCircle (OH\_Drawing\_Canvas\*, const OH\_Drawing\_Point\*, float radius) | Draws a circle. |
| OH\_Drawing\_Path\* OH\_Drawing\_PathCreate (void) | Creates an **OH\_Drawing\_Path** object. |
| void OH\_Drawing\_CanvasDrawPath (OH\_Drawing\_Canvas\*, const OH\_Drawing\_Path\*) | Draws a path. |
| OH\_Drawing\_Region\* OH\_Drawing\_RegionCreate (void) | Creates a region object. |
| void OH\_Drawing\_CanvasDrawRegion (OH\_Drawing\_Canvas\*, const OH\_Drawing\_Region\*) | Draws a region. |
| void OH\_Drawing\_CanvasDrawRect (OH\_Drawing\_Canvas\*, const OH\_Drawing\_Rect\*) | Draws a rectangle. |
| OH\_Drawing\_RoundRect\* OH\_Drawing\_RoundRectCreate (const OH\_Drawing\_Rect\*, float xRad, float yRad) | Creates an **OH\_Drawing\_RoundRect** object. |
| void OH\_Drawing\_CanvasDrawRoundRect (OH\_Drawing\_Canvas\*, const OH\_Drawing\_RoundRect\*) | Draws a rounded rectangle. |

#### Drawing Points

A point can be drawn only on the canvas based on the paint. You can use the OH\_Drawing\_CanvasDrawPoint() API to draw a point. The API accepts two parameters: canvas object and pointer to the point to be drawn. Ensure that the canvas has been created or obtained. For details, see Obtaining a Canvas and Displaying the Drawing Result (C/C++) (canvas-get-result-draw-c.md).

A simple example is as follows:

// Create a paint object.
OH\_Drawing\_Pen\* pen = OH\_Drawing\_PenCreate();
// Set the paint color.
OH\_Drawing\_PenSetColor(pen, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// Set the brush line width to 40.
OH\_Drawing\_PenSetWidth(pen, 40);
// Set the paint for the canvas.
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// Draw five points.
AdaptationUtil\* adaptationUtil = AdaptationUtil::GetInstance();
OH\_Drawing\_Point2D point1 = {value200\_, value200\_};
OH\_Drawing\_CanvasDrawPoint(canvas, &point1);
OH\_Drawing\_Point2D point2 = {value400\_, value400\_};
OH\_Drawing\_CanvasDrawPoint(canvas, &point2);
OH\_Drawing\_Point2D point3 = {value600\_, value600\_};
OH\_Drawing\_CanvasDrawPoint(canvas, &point3);
OH\_Drawing\_Point2D point4 = {value800\_, value800\_};
OH\_Drawing\_CanvasDrawPoint(canvas, &point4);
OH\_Drawing\_Point2D point5 = {value1000\_, value1000\_};
OH\_Drawing\_CanvasDrawPoint(canvas, &point5);
// Remove the brush from the canvas.
OH\_Drawing\_CanvasDetachPen(canvas);
// Destroy objects.
OH\_Drawing\_PenDestroy(pen);

The effect is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/qrK3PTkdS5KUi15MieI6ZA/en-us_image_0000002568764955.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8223299F912D57772C78F6422B3095AE1FE3ED53D71F585D664AB448602A3A3E)

#### Drawing an Arc

You can draw an arc on the canvas using a paint or brush by calling OH\_Drawing\_CanvasDrawArc(). The API requires four parameters:

-   Canvas object. Ensure that the canvas has been created or obtained. For details, see Obtaining a Canvas and Displaying the Drawing Result (C/C++). (canvas-get-result-draw-c.md)
    
-   A rectangle, which is used as the outline of the arc.
    
-   A floating-point parameter, which indicates the start angle of the arc.
    
-   Another floating-point parameter, which indicates the scanning angle of the arc.
    

The following is a simple example for drawing an arc using a paint:

// Create a paint object.
OH\_Drawing\_Pen\* pen = OH\_Drawing\_PenCreate();
// Set the stroke color of the paint.
OH\_Drawing\_PenSetColor(pen, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// Set the paint line width to 20.
OH\_Drawing\_PenSetWidth(pen, 20);
// Set the paint of the canvas.
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// Create a rectangle object. The upper left corner coordinates are (100, 200) and the lower right corner coordinates are (500, 300).
OH\_Drawing\_Rect\* rect = OH\_Drawing\_RectCreate(100, 200, 500, 300);
// Draw an arc based on the rectangle object. The angle is 10°, and the scan angle is 200°.
OH\_Drawing\_CanvasDrawArc(canvas, rect, 10, 200);
// Remove the paint from the canvas.
OH\_Drawing\_CanvasDetachPen(canvas);
// Destroy objects.
OH\_Drawing\_PenDestroy(pen);
OH\_Drawing\_RectDestroy(rect);

The effect is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/XK34JIr3QHWcrBVlKSAecg/en-us_image_0000002537765230.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A9412BD43B4034E778A990EA82DDCBF61405529A2BADDF242A53601236DA714)

#### Drawing a Circle

You can use the paint or brush to draw a circle on the canvas. The OH\_Drawing\_CanvasDrawCircle() API is used to draw a circle. The API requires three parameters, which are described as follows:

-   Canvas object. Ensure that the canvas has been created or obtained. For details, see Obtaining a Canvas and Displaying the Drawing Result (C/C++) (canvas-get-result-draw-c.md).
    
-   Pointer to the center point of the circle. The circle is drawn with this point as the center.
    
-   Floating-point parameter, indicating the radius of the circle.
    

The following is a simple example of drawing a circle using the paint:

// Create a paint object.
OH\_Drawing\_Pen\* pen = OH\_Drawing\_PenCreate();
// Set the stroke color of the paint.
OH\_Drawing\_PenSetColor(pen, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// Set the paint line width to 20.
OH\_Drawing\_PenSetWidth(pen, 20);
// Set the paint of the canvas.
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// Create the center point of the circle.
OH\_Drawing\_Point \*point = OH\_Drawing\_PointCreate(value700\_, value700\_);
// Draw a circle on the canvas based on the center point and radius.
OH\_Drawing\_CanvasDrawCircle(canvas, point, value600\_);
// Remove the brush from the canvas.
OH\_Drawing\_CanvasDetachPen(canvas);
// Destroy objects.
OH\_Drawing\_PenDestroy(pen);
OH\_Drawing\_PointDestroy(point);

The effect is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/0iNTn5LGTfy-JgcaYI9eFg/en-us_image_0000002537925170.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55C52968DEBC66A062D8A06E365A6D185E91E0126C058393F0366B0251A91888)

#### Draw a route.

You can use a brush or a paint to draw a path on the canvas. The path can be used to draw a straight line, an arc, a Bezier curve, or other complex shapes.

[drawing\_path](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-path-h) describes the APIs and implementation of drawing a path. The common APIs are as follows:

1.  Use the OH\_Drawing\_PathCreate() API to create a path object.
    
2.  Use the OH\_Drawing\_PathMoveTo() API to set the start point of a custom path.
    
3.  Use the OH\_Drawing\_PathLineTo() API to add a line segment from the start point or the last point of the path (if the path is empty, the default value is (0,0)) to the target point.
    

The following uses a brush and a paint to draw a five-pointed star as an example:

// Create a paint object.
OH\_Drawing\_Pen\* pen = OH\_Drawing\_PenCreate();
// Set the stroke color of the paint.
OH\_Drawing\_PenSetColor(pen, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// Set the brush line width to 10.
OH\_Drawing\_PenSetWidth(pen, 10);
// Set the corner style of the brush.
OH\_Drawing\_PenSetJoin(pen, LINE\_ROUND\_JOIN);
// Set the brush on the canvas.
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// Create a brush. In this example, the closed path is filled with color, so a brush is required.
OH\_Drawing\_Brush \*brush = OH\_Drawing\_BrushCreate();
OH\_Drawing\_BrushSetColor(brush, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MIN, RGBA\_MAX, RGBA\_MIN));
// Set the brush on the canvas.
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
int len = value551\_;
float aX = value630\_;
float aY = value551\_;
float dX = aX - len \* std::sin(18.0f);
float dY = aY + len \* std::cos(18.0f);
float cX = aX + len \* std::sin(18.0f);
float cY = dY;
float bX = aX + (len / 2.0);
float bY = aY + std::sqrt((cX - dX) \* (cX - dX) + (len / 2.0) \* (len / 2.0));
float eX = aX - (len / 2.0);
float eY = bY;
// Create a path.
OH\_Drawing\_Path\* path = OH\_Drawing\_PathCreate();
// Go to the start point.
OH\_Drawing\_PathMoveTo(path, aX, aY);
// Draw a line.
OH\_Drawing\_PathLineTo(path, bX, bY);
OH\_Drawing\_PathLineTo(path, cX, cY);
OH\_Drawing\_PathLineTo(path, dX, dY);
OH\_Drawing\_PathLineTo(path, eX, eY);
// Close the line to form a five-pointed star.
OH\_Drawing\_PathClose(path);
// Draw a closed path.
OH\_Drawing\_CanvasDrawPath(canvas, path);
// Remove the brush and brush from the canvas.
OH\_Drawing\_CanvasDetachPen(canvas);
OH\_Drawing\_CanvasDetachBrush(canvas);
// Destroy objects.
OH\_Drawing\_PenDestroy(pen);
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_PathDestroy(path);

The effect is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/TQEmJJdWScOTdXgmpIgxdw/en-us_image_0000002568684947.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ECD36A1F1A7B02E130979506050336315D001215479DC6C81E8E543017D91BCB)

#### Viewport rectangle

A region is not a specific shape. It can be set to a specified rectangle or path, or two regions can be combined. You can use a brush or paintbrush to draw a region on the canvas. For details about the APIs, see [drawing\_region.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-region-h).

Currently, the rectangle region and path region can be set by calling OH\_Drawing\_RegionSetRect() and OH\_Drawing\_RegionSetPath(), respectively.

The following example demonstrates how to use a brush to draw a combined region of rectangles:

// Create a brush object.
OH\_Drawing\_Brush\* brush = OH\_Drawing\_BrushCreate();
// Set the fill color of the brush.
OH\_Drawing\_BrushSetColor(brush, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// Set the brush of the canvas.
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
// Rectangle region 1.
OH\_Drawing\_Region \*region1 = OH\_Drawing\_RegionCreate();
OH\_Drawing\_Rect \*rect1 = OH\_Drawing\_RectCreate(value100\_, value100\_, value600\_, value600\_);
OH\_Drawing\_RegionSetRect(region1, rect1);
// Rectangle region 2.
OH\_Drawing\_Region \*region2 = OH\_Drawing\_RegionCreate();
OH\_Drawing\_Rect \*rect2 = OH\_Drawing\_RectCreate(value300\_, value300\_, value900\_, value900\_);
OH\_Drawing\_RegionSetRect(region2, rect2);
// Combining two rectangles
OH\_Drawing\_RegionOp(region1, region2, OH\_Drawing\_RegionOpMode::REGION\_OP\_MODE\_XOR);
OH\_Drawing\_CanvasDrawRegion(canvas, region1);
// Remove the brush from the canvas.
OH\_Drawing\_CanvasDetachBrush(canvas);
// Destroying objects
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_RegionDestroy(region1);
OH\_Drawing\_RegionDestroy(region2);
OH\_Drawing\_RectDestroy(rect1);
OH\_Drawing\_RectDestroy(rect2);

The effect is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/DHK71Er8RwmcY4VWPJp0VQ/en-us_image_0000002568764949.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F59D99383ABB7F17D024D0275A0BBAAE43FFE5751C8794B1AC8B3DF8F3D18296)

#### Draws a rectangle.

You can use a pen or brush to draw a rectangle on the canvas. Use the OH\_Drawing\_RectCreate() API to create a rectangle. The API needs to pass four floating points to indicate the coordinates of the left, top, right, and bottom of the rectangle. The four coordinates form a rectangle.

A simple example is as follows:

// Create a brush object.
OH\_Drawing\_Brush \*brush = OH\_Drawing\_BrushCreate();
// Set the fill color of the brush.
OH\_Drawing\_BrushSetColor(brush, 0xffff0000);
// Set the brush of the canvas.
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
OH\_Drawing\_Rect\* rect = OH\_Drawing\_RectCreate(0, 0, value800\_, value800\_);
// Draw a rectangle.
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// Remove the brush from the canvas.
OH\_Drawing\_CanvasDetachBrush(canvas);
// Destroying objects
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_RectDestroy(rect);

The effect is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/W3AJTmImSGmAMN-D3n_KYg/en-us_image_0000002568764957.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=253ADC0E0AE0EFEC9A36FC023B585A9FE8A2C4B2932C5B9528F53586F79E10CB)

#### Drawing a Rounded Rectangle

You can use a brush or a paint to draw a rounded rectangle on the canvas. Use the OH\_Drawing\_RoundRectCreate() API to create a rounded rectangle. The API needs to pass three parameters, as follows:

-   Pointer to the OH\_Drawing\_Rect rectangle object, which is used to draw a rounded rectangle.
    
-   A floating-point parameter, indicating the radius of the rounded rectangle on the x axis.
    
-   A floating-point parameter, indicating the radius of the rounded rectangle on the y axis.
    

A simple example is as follows:

// Create a brush object.
OH\_Drawing\_Brush \*brush = OH\_Drawing\_BrushCreate();
// Set the fill color of the brush.
OH\_Drawing\_BrushSetColor(brush, 0xffff0000);
// Set the brush of the canvas.
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
// Create a rectangle.
OH\_Drawing\_Rect\* rect = OH\_Drawing\_RectCreate(value100\_, value100\_, value900\_, value600\_);
// Create a rounded rectangle.
OH\_Drawing\_RoundRect\* roundRect = OH\_Drawing\_RoundRectCreate(rect, 30, 30);
// Draw a rounded rectangle.
OH\_Drawing\_CanvasDrawRoundRect(canvas, roundRect);
// Remove the brush from the canvas.
OH\_Drawing\_CanvasDetachBrush(canvas);
// Destroying objects
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_RoundRectDestroy(roundRect);

The effect is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/oQhxnNzBTtCX7nEqZE_7BQ/en-us_image_0000002537765232.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC830D2126C1C5F251E1B4F912CF1C4879D67C167EFABBBB614BBA2DC11EDEAA)
