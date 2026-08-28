# Drawing Geometric Shapes (ArkTS)

#### Overview

Currently, the following geometric shapes can be drawn:

-   Point
    
-   Arc
    
-   Circle
    
-   Path
    
-   Region
    
-   Box
    
-   Rounded rectangle
    

Most geometric shapes can be drawn using a brush or a paintbrush. Points can be drawn only using a brush.

#### Available APIs

The following table describes the APIs commonly used for drawing geometric shapes. For details about the APIs and parameters, see [drawing.Canvas](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing-canvas).

| API | Description |
| :-- | :-- |
| drawPoint(x: number, y: number): void | Draws a point. |
| drawArc(arc: common2D.Rect, startAngle: number, sweepAngle: number): void | Draws an arc. |
| drawCircle(x: number, y: number, radius: number): void | Draws a circle. |
| drawPath(path: Path): void | Draws a path. |
| drawRegion(region: Region): void | Draws a region. |
| drawRect(left: number, top: number, right: number, bottom: number): void | Draws a rectangle. |
| drawRoundRect(roundRect: RoundRect): void | Draws a rounded rectangle. |

#### Drawing Points

Points can be drawn on the canvas only using a brush. You can use the drawPoint() API to draw a point. A point has two parameters, which are the x coordinate and y coordinate of the point to be drawn.

A simple example is as follows:

// Set the brush.
let pen = new drawing.Pen();
// Set the color
pen.setColor(0xFF, 0xFF, 0x00, 0x00);
// Set the line width.
pen.setStrokeWidth(40);
// Set the stroke effect of the paint.
canvas.attachPen(pen);
// Draw five points.
canvas.drawPoint(VALUE\_200, VALUE\_200);
canvas.drawPoint(VALUE\_400, VALUE\_400);
canvas.drawPoint(VALUE\_600, VALUE\_600);
canvas.drawPoint(VALUE\_800, VALUE\_800);
canvas.drawPoint(VALUE\_1000, VALUE\_1000);
// Remove the stroke effect.
canvas.detachPen();

The effect is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/3WHytlMQQJ-PkOVC12I2_g/en-us_image_0000002568764947.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C14329ADE7CFCBBA37253C140054B1AAED6E8DA476A18A8FB660E47184F80B0)

#### Drawing an Arc

You can use a paint or brush to draw an arc on the canvas. The drawArc() API is used to draw an arc.

Drawing an arc requires a rectangle ([common2D.Rect](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-graphics-common2d#rect)) and two parameters, which indicate the start angle (startAngle) and sweep angle (sweepAngle) of the arc.

The following is a simple example of drawing an arc using a paint:

// Create a pen.
let pen = new drawing.Pen();
// Set the color
pen.setColor({
  alpha: 0xFF,
  red: 0xFF,
  green: 0x00,
  blue: 0x00
});
// Set the line width.
pen.setStrokeWidth(20);
// Set the stroke effect of the paint.
canvas.attachPen(pen);
// Create a rectangle.
const rect: common2D.Rect = {
  left: VALUE\_100,
  top: VALUE\_200,
  right: VALUE\_1000,
  bottom: VALUE\_600
};
// Draw a rectangle.
canvas.drawArc(rect, 0, 180);
// Remove the stroke effect.
canvas.detachPen();

The effect is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/H32hVefjSbulus6oOkE4qA/en-us_image_0000002537765222.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FEC7FD586E9BAD791B11F4995AA491B80DD01FB11914C31A0C399B4075FE4A63)

#### Drawing a Circle

You can use a paint or brush to draw a circle on the canvas. The drawCircle() API is used to draw a circle.

Drawing a circle requires the x and y coordinates of the circle center and the radius of the circle.

The following example uses a brush to draw a circle.

// Create a pen.
let pen = new drawing.Pen();
// Set the color
pen.setColor({
  alpha: 0xFF,
  red: 0xFF,
  green: 0x00,
  blue: 0x00
});
// Set the line width.
pen.setStrokeWidth(20);
// Set the stroke effect of the paint.
canvas.attachPen(pen);
// Draw a circle.
canvas.drawCircle(VALUE\_630, VALUE\_630, VALUE\_500);
// Remove the stroke effect.
canvas.detachPen();

The effect is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/NL9Y3_J4Q3u_4BLsYbKuoA/en-us_image_0000002537925162.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B45EAB732AF905E42F49090B33B783CF2F49EB9850E81E745FD40411881594BE)

#### Draw a route.

You can use a brush or a brush to draw a path on the canvas. A path can be used to draw a straight line, arc, or Bezier curve. You can also combine paths to form other complex shapes.

The following describes the APIs and implementation of drawing a path. For details about the usage and parameters, see [Path](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing-path). Common APIs are as follows:

1.  new drawing.Path() is used to create a path object.
    
2.  moveTo() is used to set the start point of a custom path.
    
3.  lineTo() is used to add a line segment from the start point or the last point of the path (if the path is empty, the default value is (0,0)) to the target point.
    

The following example uses a brush and a brush to draw a five-pointed star.

let height\_ = VALUE\_1800;
let width\_ = VALUE\_1800;
let len = height\_ / 4;
let aX = width\_ / 3;
let aY = height\_ / 6;
let dX = aX - len \* Math.sin(18.0);
let dY = aY + len \* Math.cos(18.0);
let cX = aX + len \* Math.sin(18.0);
let cY = dY;
let bX = aX + (len / 2.0);
let bY = aY + Math.sqrt((cX - dX) \* (cX - dX) + (len / 2.0) \* (len / 2.0));
let eX = aX - (len / 2.0);
let eY = bY;

// Create a path object and use the APIs to construct a pentagram.
let path = new drawing.Path();
// Specify the start point of the path.
path.moveTo(aX, aY);
// Draw a line segment from the last point of a path to the target point.
path.lineTo(bX, bY);
path.lineTo(cX, cY);
path.lineTo(dX, dY);
path.lineTo(eX, eY);
// Close the path. Now the path is drawn.
path.close();

// Create a paint object.
let pen = new drawing.Pen();
// Enable anti-aliasing.
pen.setAntiAlias(true);
// Set the stroke color.
pen.setColor(0xFF, 0xFF, 0x00, 0x00);
// Set the line width.
pen.setStrokeWidth(10.0);
// Set the stroke effect of the paint.
canvas.attachPen(pen);
// Create a brush.
let brush = new drawing.Brush();
// Set the fill color.
brush.setColor(0xFF, 0x00, 0xFF, 0x00);
// Set the fill effect of the brush.
canvas.attachBrush(brush);
// Draw the path.
canvas.drawPath(path);
// Remove the fill effect.
canvas.detachBrush();
// Remove the stroke effect.
canvas.detachPen();

The effect is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/mN0rbWqjQSuJC3akGZ_4og/en-us_image_0000002568684939.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EC301064B85ADD0C99E4BCC70722EC9D4345AE3FB5168BFD7D008194F8D4CDE)

#### Viewport rectangle

A region is not a specific shape. You can set it to a specified rectangle or path, or perform combination operations on two regions. You can use a paint or brush to draw a region. For details about the APIs, see [Region](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing-region).

Currently, a rectangle region and a path region can be set by using the setRect() and setPath() APIs, respectively.

The following uses a brush to draw a combined region of rectangles as an example:

// Create a brush.
let brush = new drawing.Brush();
// Set the color
brush.setColor(0xFF, 0xFF, 0x00, 0x00);
// Set the brush filling effect.
canvas.attachBrush(brush);
// Create region1 in the upper left corner.
let region1 = new drawing.Region();
region1.setRect(VALUE\_100, VALUE\_100, VALUE\_600, VALUE\_600);
// Create region2 in the lower right corner.
let region2 = new drawing.Region();
region2.setRect(VALUE\_300, VALUE\_300, VALUE\_900, VALUE\_900);
// Combine the two regions in XOR mode.
region1.op(region2, drawing.RegionOp.XOR);
// Draw the regions.
canvas.drawRegion(region1);
// Remove the fill effect.
canvas.detachBrush();

The effect is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/ozyFY-0eSemkLeU0wR3zdQ/en-us_image_0000002568764949.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B98AEB8A6F88E71BDBBBC3FE3B52C642B90FAB849BB5596E1D17C29DB15EA1FE)

#### Draws a rectangle.

You can use a brush or pen to draw a rectangle on the canvas. Use the drawRect() API to draw a rectangle. The API needs to pass four floating points, which indicate the coordinates of the left, top, right, and bottom of the rectangle. The four coordinates form a rectangle.

The following is a simple example of drawing a rectangle using a brush:

// Create a brush.
let brush = new drawing.Brush();
// Set the color
brush.setColor(0xFF, 0xFF, 0x00, 0x00);
// Set the brush filling effect.
canvas.attachBrush(brush);
// Draw a rectangle.
canvas.drawRect(VALUE\_200, VALUE\_200, VALUE\_1000, VALUE\_700);
// Remove the fill effect.
canvas.detachBrush();

The effect is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/ykk-oBxeT_iznyHady3GEA/en-us_image_0000002537765224.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E04171FF44CC50D61A643906099E349A95B6D1B6CF454D6F7F76204515951069)

#### Drawing a Rounded Rectangle

You can use a brush or pen to draw a rounded rectangle on the canvas. Use the drawRoundRect() API to draw a rounded rectangle. The API accepts one input parameter roundRect, which is the rounded rectangle object.

The rounded rectangle object is constructed using new drawing.RoundRect() API. The constructor accepts three parameters:

-   common2D.Rect (rectangle object). A rounded rectangle is formed by cutting corners on the rectangle.
    
-   Radius of the rounded corner on the x axis.
    
-   Radius of the rounded corner on the y axis.
    

The following is a simple example of drawing a rounded rectangle using a brush:

// Create a brush.
let brush = new drawing.Brush();
// Set the color
brush.setColor(0xFF, 0xFF, 0x00, 0x00);
// Set the brush filling effect.
canvas.attachBrush(brush);
// Create a rectangle object.
let rect: common2D.Rect = {
  left: VALUE\_200,
  top: VALUE\_200,
  right: VALUE\_1000,
  bottom: VALUE\_700
};
console.info('rect:', rect.right);
// Create a rounded rectangle object.
let rrect = new drawing.RoundRect(rect, 30, 30);
// Draw a rounded rectangle.
canvas.drawRoundRect(rrect);
// Remove the filling effect.
canvas.detachBrush();

The effect is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/ugm4gsMlR5eQvAWYydyBfw/en-us_image_0000002537925164.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=760E40DA3A56BDE308054EB63E8054C69E4843F117C8B3F63A2194016DBC0FBA)
