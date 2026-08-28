# Basic Drawing Effects (C/C++)

#### Overview

You can set some basic effects during drawing, such as setting the fill color, anti-aliasing, graphic stroke, and graphic line connection style.

You can set the basic filling effect through the brush and set the basic stroke effect through the pen.

#### Filling Effect

You can set the basic fill color through the brush. You can also use the brush to use the blending mode, shader effect, and filter effect to implement more complex drawing effects. For details, see complex-drawing-effect-c.md.

## Available APIs

The following table lists the common APIs for using the brush to set the drawing effect. For details about the usage and parameters, see [drawing\_brush](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-brush-h).

| API | Description |
| :-- | :-- |
| OH\_Drawing\_Brush\* OH\_Drawing\_BrushCreate (void) | Creates an **OH\_Drawing\_Brush** object. |
| void OH\_Drawing\_CanvasAttachBrush (OH\_Drawing\_Canvas\*, const OH\_Drawing\_Brush\*) | Sets the brush for the canvas. The canvas uses the set brush style and color to fill the drawn graphic shape. |
| void OH\_Drawing\_BrushSetColor (OH\_Drawing\_Brush\* , uint32\_t color) | Sets the color for a brush. The color is used by the brush to fill in a shape. |
| void OH\_Drawing\_BrushSetAntiAlias (OH\_Drawing\_Brush\* , bool) | Sets the anti-aliasing attribute of the brush. If this attribute is set to true, the brush blurs the edge pixels of the graphic in a semi-transparent manner when drawing the graphic, so that the edge of the graphic is smoother. |
| void OH\_Drawing\_CanvasDetachBrush (OH\_Drawing\_Canvas\*) | Removes the brush from the canvas. After the brush is removed, the canvas does not use the brush and restores to the default filling effect. |
| void OH\_Drawing\_BrushDestroy (OH\_Drawing\_Brush\*) | Destroys an **OH\_Drawing\_Brush** object and reclaims the memory occupied by the object. |

## How to Develop

1.  Create a brush object by calling OH\_Drawing\_BrushCreate().
    
    // Create a brush.
    OH\_Drawing\_Brush\* brush = OH\_Drawing\_BrushCreate();
    
2.  (Optional) Set the basic drawing effect using the brush. You can select one or more of the following effects:
    
    -   Call OH\_Drawing\_BrushSetColor() to set the fill color.
        
        // Set the fill color to red.
        uint32\_t color = 0xffff0000;
        OH\_Drawing\_BrushSetColor(brush, color);
        
        color is a 32-bit (ARGB) variable, for example, 0xffff0000.
        
    -   Call OH\_Drawing\_BrushSetAntiAlias() to enable the anti-aliasing effect to make the edges of the graphics smoother.
        
        // Enable anti-aliasing.
        OH\_Drawing\_BrushSetAntiAlias(brush, true);
        
3.  Call OH\_Drawing\_CanvasAttachBrush() to set the brush for the canvas. This API accepts two parameters. One is the canvas object. Ensure that the canvas has been created or obtained. For details, see [Obtaining a Canvas and Displaying the Drawing Result (C/C++)](../../canvas-acquisition-and-display-of-drawing-results/obtaining-a-canvas-and-displaying-drawing-results-c-c/document.md). The other is the brush object to be set. The canvas uses the set brush style and color to fill the graphics.
    
    // Set the brush of the canvas.
    OH\_Drawing\_CanvasAttachBrush(canvas, brush);
    
4.  Draw primitives as required. For details, see [Drawing Primitives](../../primitive-drawing/drawing-primitives/document.md).
    
5.  When the filling effect is not required, you can call OH\_Drawing\_CanvasDetachBrush() to remove the brush. The input parameter is the canvas object.
    
    // Remove the brush from the canvas.
    OH\_Drawing\_CanvasDetachBrush(canvas);
    
6.  When the brush is no longer needed, use the OH\_Drawing\_BrushDestroy() API to destroy the brush object in a timely manner.
    
    // Destroy objects.
    OH\_Drawing\_BrushDestroy(brush);
    

#### Stroke Effect

You can set the basic stroke color by using a pen, and use the pen to implement more complex drawing effects by using the blending mode, path effect, shader effect, and filter effect. For details, see [Complex Drawing Effects](../complex-drawing-effects-c-c/document.md).

## Available APIs

The following table lists the common APIs for setting the drawing effect by using a pen. For details about the APIs and parameters, see [drawing\_pen](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-pen-h).

| API | Description |
| :-- | :-- |
| OH\_Drawing\_Pen\* OH\_Drawing\_PenCreate (void) | Creates an **OH\_Drawing\_Pen** object. |
| void OH\_Drawing\_CanvasAttachPen (OH\_Drawing\_Canvas\* , const OH\_Drawing\_Pen\* ) | Attaches a pen to a canvas so that the canvas can use the style and color of the pen to outline a shape. |
| void OH\_Drawing\_PenSetColor (OH\_Drawing\_Pen\* , uint32\_t color) | Sets the color for a pen. The color is used by the pen to outline a shape. |
| void OH\_Drawing\_PenSetWidth (OH\_Drawing\_Pen\* , float width) | Sets the width for a pen. A line width of 0 is considered as a special ultra-fine line width. The line width is always drawn as 1 pixel during drawing and does not change with the canvas scaling. A negative line width is considered as 0 during actual drawing. |
| void OH\_Drawing\_PenSetAntiAlias (OH\_Drawing\_Pen\* , bool ) | Sets the anti-aliasing attribute of the pen. If this attribute is set to true, the pen performs semi-transparent blurring on the edge pixels of the shape when drawing the shape. |
| void OH\_Drawing\_PenSetCap (OH\_Drawing\_Pen\* , OH\_Drawing\_PenLineCapStyle) | Sets the line cap style of the pen. |
| void OH\_Drawing\_PenSetJoin (OH\_Drawing\_Pen\* , OH\_Drawing\_PenLineJoinStyle) | Sets the line join style for a pen. |
| void OH\_Drawing\_CanvasDetachPen (OH\_Drawing\_Canvas\*) | Removes the pen from the canvas. After the execution, the canvas does not draw the outline of the shape and restores to the default filling effect. |
| void OH\_Drawing\_PenDestroy (OH\_Drawing\_Pen\*) | Destroys an **OH\_Drawing\_Pen** object and reclaims the memory occupied by the object. |

## How to Develop

1.  Use the OH\_Drawing\_PenCreate() API to create a pen object.
    
    // Create a pen.
    OH\_Drawing\_Pen\* pen = OH\_Drawing\_PenCreate();
    
2.  Use the OH\_Drawing\_CanvasAttachPen() API to set the pen for the canvas. The API accepts two parameters. One is the canvas object. Ensure that the canvas has been created or obtained. For details, see [Obtaining a Canvas and Displaying the Drawing Result (C/C++)](../../canvas-acquisition-and-display-of-drawing-results/obtaining-a-canvas-and-displaying-drawing-results-c-c/document.md). The other is the pen object to be set. The canvas uses the configured pen style and color to draw the outline of the shape.
    
    // Set the pen for the canvas.
    OH\_Drawing\_CanvasAttachPen(canvas, pen);
    
3.  (Optional) Use the pen to set the specific stroke effect (one or more of the following effects).
    
    -   Use the OH\_Drawing\_PenSetColor() API to set the pen color, which is the color used for drawing the outline of the shape.
        
        // Set the stroke color to red.
        uint32\_t color = 0xffff0000;
        OH\_Drawing\_PenSetColor(pen, color);
        
        color is a 32-bit (ARGB) variable, for example, 0xffff0000.
        
    -   Use the OH\_Drawing\_PenSetWidth() API to set the pen width.
        
        // Set the pen width to 50 pixels.
        float width = 50.0;
        OH\_Drawing\_PenSetWidth(pen, width);
        
        width indicates the pixel value of the line width.
        
    -   Use the OH\_Drawing\_PenSetAntiAlias() API to set anti-aliasing for the pen to make the edges of the drawn shape smoother.
        
        // Enable anti-aliasing for the pen.
        OH\_Drawing\_PenSetAntiAlias(pen, true);
        
    -   Use the OH\_Drawing\_PenSetCap() API to set the pen line cap style.
        
        // Set the cap style for the pen.
        OH\_Drawing\_PenSetCap(pen, OH\_Drawing\_PenLineCapStyle::LINE\_ROUND\_CAP);
        
        The line cap styles of OH\_Drawing\_PenLineCapStyle are as follows:
        
        | Line Cap Style | Description | Diagram |
        | :-- | :-- | :-- |
        | LINE\_FLAT\_CAP | There is no cap style. Both ends of the line segment are cut off square. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/RGCLzAKiRs2pF5uK0MMj1w/en-us_image_0000002537765206.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6EAB4E0CAABAF029C0B09A511F8714C66E80E7E37AF78180DB0A4CB9ACF71E4E) |
        | LINE\_SQUARE\_CAP | Square cap style. Both ends have a square, the height of which is half of the width of the line segment, with the same width. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/tT4IQO66RW-Jokk__B6XKw/en-us_image_0000002537925146.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=52D7AD6DE1B3295F40E96E63F82C9C8CBB11181F9031677887E995B1DD0E1796) |
        | LINE\_ROUND\_CAP | Round cap style. Both ends have a semicircle centered, the diameter of which is the same as the width of the line segment. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/qddR45DERLWv_iv86HMBYQ/en-us_image_0000002568684923.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D89FD964636083CA7B8A0B44A1E8A97EE4B9A53F7EC7C73C77428243DD905C31) |
        
    -   You can use the OH\_Drawing\_PenSetJoin() API to set the pen corner style.
        
        // Set the join style for the pen.
        OH\_Drawing\_PenSetJoin(pen, OH\_Drawing\_PenLineJoinStyle::LINE\_BEVEL\_JOIN);
        
        The corner styles of OH\_Drawing\_PenLineJoinStyle are as follows:
        
        | Corner Style | Description | Diagram |
        | :-- | :-- | :-- |
        | LINE\_MITER\_JOIN | The corner type is sharp. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/-P0t0hiySAyHiPx8B70QFw/en-us_image_0000002537765214.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D25BD7D9423C54A1BE2BB29562A8F357B1C84775819A5D26BB6ED4C799CF44D) |
        | LINE\_ROUND\_JOIN | Round corner. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/AvHhQygqTmWUUt7d2_AlDw/en-us_image_0000002537925154.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C0C9BD7CE5BF533D62E6C910A5F9FEB22F7F93706A5D982333728E5469310A3) |
        | LINE\_BEVEL\_JOIN | Beveled corner. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/PhrsQhW5RxC1ayPJAXl5qw/en-us_image_0000002568684931.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=325038D42DDF301531EDDB62F3BC733F11EAA304A7953794CAF6C511F4C69161) |
        
4.  Draw primitives as required. For details, see [Drawing Primitives](../../primitive-drawing/drawing-primitives/document.md).
    
5.  If the stroke effect is not required, you can use OH\_Drawing\_CanvasDetachPen() to remove it. The input parameter is the canvas object. Ensure that the canvas has been created or obtained. For details, see Obtaining a Canvas and Displaying the Drawing Result (C/C++).
    
    // Remove the pen from the canvas.
    OH\_Drawing\_CanvasDetachPen(canvas);
    
6.  When the pen is no longer needed, use the OH\_Drawing\_PenDestroy() API to destroy the pen object in a timely manner.
    
    // Destroy objects.
    OH\_Drawing\_PenDestroy(pen);
