# Basic Drawing Effects (ArkTS)

#### Overview

You can set some basic effects, such as the fill color, anti-aliasing, stroke, and line connection style.

You can set the basic fill effect using a brush and set the basic stroke effect using a pen.

#### Fill Effect

You can set the basic fill color using a brush and use the brush to implement more complex drawing effects, such as the blend mode, shader effect, and filter effect. For details, see [Complex Drawing Effects](../complex-drawing-effects-arkts/document.md).

## Available APIs

The following table lists the APIs for setting the drawing effect using a brush. For details, see [drawing.Brush](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing-brush).

| API | Description |
| :-- | :-- |
| attachBrush(brush: Brush): void | Attaches a brush to a canvas so that the canvas can use the style and color of the brush to fill in a shape. |
| setColor(alpha: number, red: number, green: number, blue: number): void | Sets the color for a brush, which is used to fill in a shape. |
| setAntiAlias(aa: boolean) : void | Enables or disables anti-aliasing for a brush. Anti-aliasing makes the pixels around the shape edges semi-transparent, delivering a smoother effect. |
| detachBrush(): void | Removes the brush from the canvas. After the execution, the canvas does not use the previously set brush and restores to the default fill effect. |

## How to Develop

1.  Create a brush object.
    
    // Set the brush.
    const brush = new drawing.Brush();
    
2.  Use the brush to set basic drawing effects, such as setting the fill color and enabling the anti-aliasing effect.
    
    You can call **setColor()** to set the fill color.
    
    // Set the fill color to red.
    brush.setColor(0xFF, 0xFF, 0x00, 0x00);
    
    You can call **setAntiAlias()** to enable the anti-aliasing effect to smooth the edges of the graphics.
    
    // Enable the anti-aliasing effect.
    brush.setAntiAlias(true);
    
3.  Call **attachBrush()** to set a brush for the canvas.
    
    // Set a brush for the canvas.
    canvas.attachBrush(brush);
    
4.  Draw primitives as required. For details, see [Drawing Primitives](../../primitive-drawing/drawing-primitives/document.md).
    
5.  If the fill effect is not required, you can use the **detachBrush()** API to remove the brush from the canvas.
    
    // Remove the brush.
    canvas.detachBrush();
    

#### Stroke Effect

You can set the basic stroke color using a pen and use the pen to implement more complex drawing effects, such as the blend mode, path effect, shader effect, and filter effect. For details, see [Complex Drawing Effects](../complex-drawing-effects-arkts/document.md).

## Available APIs

The following table lists the APIs for setting the drawing effect using a pen. For details, see [drawing.Pen](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing-pen).

| API | Description |
| :-- | :-- |
| attachPen(pen: Pen): void | Attaches a pen to a canvas so that the canvas can use the style and color of the pen to outline a shape. |
| setColor(alpha: number, red: number, green: number, blue: number): void | Sets the color for a pen, which is used to outline a shape. |
| setStrokeWidth(width: number) : void | Sets the width for a pen. The value **0** is treated as an unusually thin width. During drawing, the width of 0 is always drawn as 1 pixel wide, regardless of any scaling applied to the canvas. Negative values are also regarded as the value **0** during the drawing process. |
| setAntiAlias(aa: boolean) : void | Enables or disables anti-aliasing for a pen. Anti-aliasing makes the pixels around the shape edges semi-transparent. |
| setCapStyle(style: CapStyle): void | Sets the line cap style for a pen. |
| setJoinStyle(style: JoinStyle): void | Sets the line join style for a pen. |
| detachPen(): void | Removes the brush from the canvas. After the execution, the canvas does not draw the outline of the shape and restores to the default fill effect. |

## How to Develop

1.  Create a pen object.
    
    // Create a pen object.
    let pen = new drawing.Pen();
    
2.  Call **attachPen()** to set a pen for the canvas. The canvas uses the pen style and color to draw the outline.
    
    // Set a pen for the canvas.
    canvas.attachPen(pen);
    
3.  (Optional) Use the pen to set the stroke effect. You can select one or more of the following effects:
    
    -   You can call **setColor()** to set the pen color, which is used to outline a shape.
        
        // Set the color to red.
        pen.setColor(0xFF, 0xFF, 0x00, 0x00);
        
    -   You can call **setStrokeWidth()** to set the pen width.
        
        // Set the stroke width.
        pen.setStrokeWidth(15);
        
    -   You can call **setAntiAlias()** to set anti-aliasing for the pen to make the drawing edge smoother.
        
        // Set the anti-aliasing effect.
        pen.setAntiAlias(true);
        
    -   You can call **setCapStyle()** to set the pen cap style.
        
        // Set the pen cap style.
        pen.setCapStyle(drawing.CapStyle.SQUARE\_CAP);
        
        The options of **CapStyle** are as follows.
        
        | Line Cap Style | Description | Effect |
        | :-- | :-- | :-- |
        | FLAT\_CAP | No cap style. Both ends of the line segment are cut off square. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/0Nend5kmSW2jfROZLUGP1Q/en-us_image_0000002537765206.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77320D97E5FA5979E980D7517E540FE20534CFEE6A299BF68DDC3FB2BFBA07A6) |
        | SQUARE\_CAP | Square cap style. Both ends have a square, the height of which is half of the width of the line segment, with the same width. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/85kTlYByTsylTC5xxgxV6A/en-us_image_0000002537925146.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ABFF4A28723404872CDBA41C7333E90EC958BEB8B8DEFB51F24424D16241DB23) |
        | ROUND\_CAP | Round cap style. Both ends have a semicircle centered, the diameter of which is the same as the width of the line segment. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/4TPbCOdmQ7KwZUh2w5P07g/en-us_image_0000002568684923.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26707488C37D39D5866FC149C3696212B2DF258F82A215A5F6CAE39B88C6223B) |
        
    -   You can call **setJoinStyle()** to set the pen join style.
        
        // Set the pen join style.
        pen.setJoinStyle(drawing.JoinStyle.ROUND\_JOIN);
        
        The options of **JoinStyle** are as follows.
        
        | Line Join Style | Description | Effect |
        | :-- | :-- | :-- |
        | MITER\_JOIN | Miter join. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/xdGJvRdGQ4yrTtfZAifh7g/en-us_image_0000002568764933.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4F55D7FE860EDA923981029EE95CA33C231BD4EC79D49EDDE2D63864872D07B) |
        | ROUND\_JOIN | Round join. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/s434JEG8RJaC9-QxtpHHKg/en-us_image_0000002537765208.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BB94FFEB0FBCB065F32A9CAEB0C419807FC6C5DF57D8EA72BB63B858B9182FE) |
        | BEVEL\_JOIN | Beveled join. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/1Y1IcYgiSVGRx9i9guo4mw/en-us_image_0000002537925148.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=288DD02B0FC6311F979ED7FA5E3E720B6BE40ECC5CAF73F850EB9E5DE04C098A) |
        
4.  Draw primitives as required. For details, see [Drawing Primitives](../../primitive-drawing/drawing-primitives/document.md).
    
5.  If the stroke effect is not required, you can use the **detachPen()** API to remove the pen from the canvas.
    
    // Remove the stroke effect.
    canvas.detachPen();
