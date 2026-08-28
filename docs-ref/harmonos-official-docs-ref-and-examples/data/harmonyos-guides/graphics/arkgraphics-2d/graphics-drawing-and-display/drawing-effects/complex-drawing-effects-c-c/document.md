# Complex Drawing Effects (C/C++)

You can use a brush or a pen to implement complex drawing effects in addition to the basic fill color, stroke color, and style settings. The following lists some major challenges:

-   Blend mode
    
-   Path effect, such as dashed lines
    
-   Shader effect, such as linear gradient and radial gradient
    
-   Filtering effect, such as blurring
    

#### Blend Mode

The blend mode can be used for brushes or pens. It defines how to combine source pixels (content to be drawn) with target pixels (content that already exists on the canvas).

You can use the **OH\_Drawing\_BrushSetBlendMode()** API to apply the blend mode to a brush and use the **OH\_Drawing\_PenSetBlendMode()** API to apply the blend mode to a pen. Both APIs need to take the **OH\_Drawing\_BlendMode** parameter, that is, the type of the blend mode. For details, see [OH\_Drawing\_BlendMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-types-h#oh_drawing_blendmode).

The following describes how to use the brush to set the blend mode. (To prevent the blend mode effect from being interfered by the background color, the default black background is used.) The sample code and effect are as follows:

// Create a brush object.
OH\_Drawing\_Brush\* brush = OH\_Drawing\_BrushCreate();
// Set the target pixel color.
OH\_Drawing\_BrushSetColor(brush, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// Attach the brush effect of the target pixels to the canvas.
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
// Create a rectangle object.
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value100\_, value100\_, value600\_, value600\_);
// Draw a rectangle (target pixels).
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// Set the source pixel color.
OH\_Drawing\_BrushSetColor(brush, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MIN, RGBA\_MIN, 0xFF));
// Set the blend mode to PLUS.
OH\_Drawing\_BrushSetBlendMode(brush, OH\_Drawing\_BlendMode::BLEND\_MODE\_PLUS);
// Attach the brush effect of the source pixels to the canvas.
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
// Create a point object for the circle center.
OH\_Drawing\_Point \*point = OH\_Drawing\_PointCreate(value600\_, value600\_);
// Draw a circle (source pixels).
OH\_Drawing\_CanvasDrawCircle(canvas, point, value300\_);
// Remove the brush from the canvas.
OH\_Drawing\_CanvasDetachBrush(canvas);
// Destroy objects.
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_PointDestroy(point);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/8yRHu8plSuqrYb3jlzOHrg/en-us_image_0000002568764941.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=471BAB9992ACDC27DE669587FC7611392C60B80143ED41167EAE3C7D1BF2E50A)

#### Path Effect

The path effect, such as dashed lines, is available only for the pen.

You can use the **OH\_Drawing\_CreateDashPathEffect()** API to set the path effect. The API takes three parameters, which are as follows:

-   Float array **intervals**: indicates the interval between dashed lines or dotted lines.
    
-   Integer **count**: indicates the number of elements in the **intervals** array.
    
-   Float **phase**: indicates the offset in the intervals array, that is, the position from which the dashed line or dotted line effect is applied.
    

The following uses the dashed line path effect of a rectangle as an example. The sample code and effect are as follows:

// Create a pen object.
OH\_Drawing\_Pen \*pen = OH\_Drawing\_PenCreate();
// Set the stroke color of the pen.
OH\_Drawing\_PenSetColor(pen, 0xffff0000);
// Set the pen width to 10.
OH\_Drawing\_PenSetWidth(pen, 10);
// The effect is a cyclic repetition of a 10 px solid line, a 5 px interval, a 2 px solid line, and a 5 px interval.
float intervals\[\] = {10, 5, 2, 5};
// Set the dashed line path effect.
OH\_Drawing\_PathEffect \*pathEffect = OH\_Drawing\_CreateDashPathEffect(intervals, 4, 0.0);
OH\_Drawing\_PenSetPathEffect(pen, pathEffect);
// Set the pen on the canvas. Ensure that the canvas object has been obtained.
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// Create a rectangle.
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value300\_, value300\_, value900\_, value900\_);
// Draw a rectangle.
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// Remove the pen from the canvas.
OH\_Drawing\_CanvasDetachPen(canvas);
// Destroy objects.
OH\_Drawing\_PenDestroy(pen);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_PathEffectDestroy(pathEffect);

| Path Without Dashed Lines | Path With Dashed Lines |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/oVaxGJ1rQ5SL3yCIxg75xA/en-us_image_0000002537765216.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDA72E3057B82B85590617129C58B0EC6F90C61861F0B21FECA1F51E2C77995B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/HIAyycWbRparfUpakRX4hw/en-us_image_0000002537925156.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E87D0E3F10234B11F05329073DDF9CBF143908D132FEC57E25D695BCB79DA026) |

#### Shader Effect

The shader effect is implemented based on the brush or pen. You can use **OH\_Drawing\_BrushSetShaderEffect()** to set the shader effect of the brush, or use **OH\_Drawing\_PenSetShaderEffect()** to set the shader effect of the pen. Currently, different shader effects are supported, such as linear gradient, radial gradient, and sector gradient.

For details about shader-related APIs and parameters, see [drawing\_shader\_effect](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-shader-effect-h).

## Linear Gradient Shader Effect

You can use the **OH\_Drawing\_ShaderEffectCreateLinearGradient()** API to create the linear gradient shader effect to be set. The API takes six parameters, which are the start point, end point, color array, relative position array, color array size, and tiling mode.

-   The start point and end point are used to determine the gradient direction.
    
-   The color array is used to store the colors used in the gradient.
    
-   The relative position array is used to determine the relative position of each color in the gradient. If the relative position is empty, the colors are evenly distributed between the start point and end point.
    
-   The tiling mode is used to determine how to continue the gradient effect outside the gradient area. The options are as follows:
    
    -   **CLAMP**: Replicates the edge color if the image exceeds its original boundary.
    -   **REPEAT**: Repeats the image in both horizontal and vertical directions.
    -   **MIRROR**: Repeats the image in both horizontal and vertical directions and alternates the mirrored image between adjacent images.
    -   **DECAL**: Renders the shader effect's image only within the original boundary, and returns transparent black elsewhere.

The following uses the rectangle drawing and the linear gradient shader effect implemented by a brush as an example. The sample code and effect are as follows:

// Start point.
OH\_Drawing\_Point \*startPt = OH\_Drawing\_PointCreate(20, 20);
// End point.
OH\_Drawing\_Point \*endPt = OH\_Drawing\_PointCreate(value900\_, value900\_);
// Color array.
uint32\_t colors\[\] = {0xFFFFFF00, 0xFFFF0000, 0xFF0000FF};
// Relative position array.
float pos\[\] = {0.0f, 0.5f, 1.0f};
// Create a linear gradient shader effect.
OH\_Drawing\_ShaderEffect \*colorShaderEffect =
    OH\_Drawing\_ShaderEffectCreateLinearGradient(startPt, endPt, colors, pos, 3, OH\_Drawing\_TileMode::CLAMP);
// Create a brush object.
OH\_Drawing\_Brush\* brush = OH\_Drawing\_BrushCreate();
// Set the shader effect based on the brush.
OH\_Drawing\_BrushSetShaderEffect(brush, colorShaderEffect);
// Set the brush on the canvas. Ensure that the canvas object has been obtained.
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value100\_, value100\_, value900\_, value900\_);
 // Draw a rectangle.
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// Remove the brush from the canvas.
OH\_Drawing\_CanvasDetachBrush(canvas);
// Destroy objects.
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_ShaderEffectDestroy(colorShaderEffect);
OH\_Drawing\_PointDestroy(startPt);
OH\_Drawing\_PointDestroy(endPt);

The following figure shows the rectangle with the linear gradient shader effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/GB9iIIvkQPigdQOcizmVeg/en-us_image_0000002568684933.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43F7C6DF4B4660DB785D3301E37C47895AC06D61541B285B23298AB4D8A76691)

## Radial Gradient Shader Effect

You can use the **OH\_Drawing\_ShaderEffectCreateRadialGradient()** API to create the radial gradient shader effect to be set. The API takes six parameters, which are the center coordinates (**centerPt**), radius (**radius**), color array (**colors**), relative position array (**pos**), number of colors and positions (**size**), and tiling mode (**OH\_Drawing\_TileMode**).

The implementation method is similar to that of the linear gradient shader. The difference is that the radial gradient starts from the center and gradually changes outward.

The following uses the rectangle drawing and the radial gradient shader effect implemented by a brush as an example. The sample code and effect are as follows:

// Center coordinates.
OH\_Drawing\_Point \*centerPt = OH\_Drawing\_PointCreate(value500\_, value500\_);
// Radius.
float radius = value600\_;
// Color array.
uint32\_t gColors\[\] = {0xFFFF0000, 0xFF00FF00, 0xFF0000FF};
// Relative position array.
float\_t gPos\[\] = {0.0f, 0.25f, 0.75f};
// Create a radial gradient shader.
OH\_Drawing\_ShaderEffect \*colorShaderEffect =
    OH\_Drawing\_ShaderEffectCreateRadialGradient(centerPt, radius, gColors, gPos, 3, OH\_Drawing\_TileMode::REPEAT);
// Create a brush object.
OH\_Drawing\_Brush\* brush = OH\_Drawing\_BrushCreate();
// Set the shader effect based on the brush.
OH\_Drawing\_BrushSetShaderEffect(brush, colorShaderEffect);
// Set the brush on the canvas. Ensure that the canvas object has been obtained.
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value100\_, value100\_, value900\_, value900\_);
 // Draw a rectangle.
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// Remove the brush from the canvas.
OH\_Drawing\_CanvasDetachBrush(canvas);
// Destroy objects.
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_ShaderEffectDestroy(colorShaderEffect);
OH\_Drawing\_PointDestroy(centerPt);

The following figure shows the rectangle with the radial gradient shader effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/SGAy_-KcR7ydnTEHK3lIIw/en-us_image_0000002568764943.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7DAD0FD7738BC7B9E3BB399DE7322E9413B421162F940669ABE4F1663D263526)

## Sector Gradient Shader Effect

You can use the **OH\_Drawing\_ShaderEffectCreateSweepGradient()** API to create the sector gradient shader effect to be set. The API takes five parameters, which are the center point, color array, relative position array, number of colors and relative positions, and tiling mode.

The implementation method is similar to that of the linear gradient shader. The difference is that the sector gradient is gradually changed during rotation around the center point.

The following uses the rectangle drawing and the sector gradient shader effect implemented by a brush as an example. The sample code and effect are as follows:

// Center point.
OH\_Drawing\_Point \*centerPt = OH\_Drawing\_PointCreate(value500\_, value500\_);
// Color array.
uint32\_t colors\[3\] = {0xFF00FFFF, 0xFFFF00FF, 0xFFFFFF00};
// Relative position array.
float pos\[3\] = {0.0f, 0.5f, 1.0f};
// Create a sector gradient shader.
OH\_Drawing\_ShaderEffect\* colorShaderEffect =
    OH\_Drawing\_ShaderEffectCreateSweepGradient(centerPt, colors, pos, 3, OH\_Drawing\_TileMode::CLAMP);
// Create a brush object.
OH\_Drawing\_Brush\* brush = OH\_Drawing\_BrushCreate();
// Set the shader effect based on the brush.
OH\_Drawing\_BrushSetShaderEffect(brush, colorShaderEffect);
// Set the brush on the canvas. Ensure that the canvas object has been obtained.
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value100\_, value100\_, value900\_, value900\_);
 // Draw a rectangle.
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// Remove the brush from the canvas.
OH\_Drawing\_CanvasDetachBrush(canvas);
// Destroy objects.
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_ShaderEffectDestroy(colorShaderEffect);
OH\_Drawing\_PointDestroy(centerPt);

The following figure shows the rectangle with the sector gradient shader effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/a3mo6emxSvaP3-x2WzfBkw/en-us_image_0000002537765218.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD31C0C378B26BB2D9EA87DBE1B600F10D39ADB890E9642B348D0CFDF247C9C4)

#### Filter Effects

The filter effect can be implemented based on the brush or pen. You can use **OH\_Drawing\_PenSetFilter()** to set the filter effect of the pen, or use **OH\_Drawing\_BrushSetFilter()** to set the filter effect of the brush. Currently, different filter effects are supported, such as image filters, color filters, and mask filters.

For details about the filter-related APIs and parameters, see [drawing\_filter.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-filter-h).

## Color Filter Effects

The color filter can be implemented based on the pen or brush. For details about the color filter-related APIs and parameters, see [drawing\_color\_filter.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-color-filter-h).

Currently, multiple color filters can be implemented, including:

-   Color filter object with a given blend mode
    
-   Color filter object with a given 5 x 4 color matrix
    
-   Color filter object with the SRGB gamma curve applied to the RGB color channel
    
-   Color filter object with the RGB color channel applied to the SRGB gamma curve
    
-   Color filter object that multiplies the input luminance value by the transparency channel and sets the red, green, and blue channels to zero
    
-   Color filter object composed of two color filters
    

The following uses the color filter with a 5 x 4 color matrix as an example.

You can use the **OH\_Drawing\_ColorFilterCreateMatrix()** API to create a color filter with a 5 x 4 color matrix. The API takes one parameter, which is the color matrix. The color matrix is a floating-point array of 20 elements. The array format is as follows:

\[ a0, a1, a2, a3, a4 \]

\[ b0, b1, b2, b3, b4 \]

\[ c0, c1, c2, c3, c4 \]

\[ d0, d1, d2, d3, d4 \]

For each original pixel color value (R, G, B, A), the formula for calculating the transformed color value (R', G', B', A') is as follows:

R' = a0\*R + a1\*G + a2\*B + a3\*A + a4

G' = b0\*R + b1\*G + b2\*B + b3\*A + b4

B' = c0\*R + c1\*G + c2\*B + c3\*A + c4

A' = d0\*R + d1\*G + d2\*B + d3\*A + d4

The following uses the rectangle drawing and the color filter effect with a 5 x 4 color matrix implemented by a brush as an example. The sample code and effect are as follows:

// Create a brush object.
OH\_Drawing\_Brush \*brush = OH\_Drawing\_BrushCreate();
// Set anti-aliasing for the brush.
OH\_Drawing\_BrushSetAntiAlias(brush, true);
// Set the fill color of the brush.
OH\_Drawing\_BrushSetColor(brush, 0xffff0000);
// Set the color matrix.
const float matrix\[20\] = {
    1, 0, 0, 0, 0,
    0, 1, 0, 0, 0,
    0, 0, 0.5f, 0.5f, 0,
    0, 0, 0.5f, 0.5f, 0
};
    
// Create a filter color.
OH\_Drawing\_ColorFilter\* colorFilter = OH\_Drawing\_ColorFilterCreateMatrix(matrix);
// Create a filter object.
OH\_Drawing\_Filter \*filter = OH\_Drawing\_FilterCreate();
// Set a color filter object for the filter object.
OH\_Drawing\_FilterSetColorFilter(filter, colorFilter);
// Set the filter effect of the brush.
OH\_Drawing\_BrushSetFilter(brush, filter);
// Set the brush on the canvas. Ensure that the canvas object has been obtained.
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
// Create a rectangle.
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value300\_, value300\_, value900\_, value900\_);
// Draw a rectangle.
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// Remove the brush from the canvas.
OH\_Drawing\_CanvasDetachBrush(canvas);
// Destroy objects.
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_ColorFilterDestroy(colorFilter);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_FilterDestroy(filter);

| Original Image | Image with a Color Filter Based on a 5×4 Color Matrix |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/subIpFAfQfeB776Gx0LX4g/en-us_image_0000002537925158.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CFF7A50A349D10E2C8AAC3D515D58E354559182A459F151A2D3D27CB69BE391) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/YepuVq7NTiKxSISGrhYUFg/en-us_image_0000002568684935.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7950DA7C98093B99BF5C826FF72E1DD77F8D4731427CAFD29CD8A9613311616C) |

## Image Filter Effects

The image filter can be implemented based on the pen or brush. For details about the image filter-related APIs and parameters, see [drawing\_image\_filter.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-image-filter-h).

Currently, only the following two types of image filters are supported:

-   Image filter based on the color filter
    
    You can use the **OH\_Drawing\_ImageFilterCreateFromColorFilter()** API to implement this type of image filter. This API takes two parameters: **colorFilter** and **input**. That is, the effect of the color filter is superimposed on the image filter. **input** can be empty, which means that only the color filter effect is added.
    
-   Image filter with a given blur effect
    
    You can call **OH\_Drawing\_ImageFilterCreateBlur()** to create a blur filter. The API takes four parameters, which are the blur standard deviation on the X axis, blur standard deviation on the Y axis, tiling mode, and image filter (**input**).
    
    The final effect is to blur the input image filter **input**. That is, the filter effect can be superimposed. **input** can be empty, which means that only the blur effect is added.
    

The following uses the rectangle drawing and the blur effect implemented by a pen as an example. The sample code and effect are as follows:

// Create a pen object.
OH\_Drawing\_Pen \*pen = OH\_Drawing\_PenCreate();
// Set anti-aliasing for the pen.
OH\_Drawing\_PenSetAntiAlias(pen, true);
// Set the stroke color of the pen.
OH\_Drawing\_PenSetColor(pen, 0xffff0000);
// Set the pen width to 20.
OH\_Drawing\_PenSetWidth(pen, 20);
// Create an image filter to implement the blur effect.
OH\_Drawing\_ImageFilter \*imageFilter =
    OH\_Drawing\_ImageFilterCreateBlur(20.0f, 20.0f, OH\_Drawing\_TileMode::CLAMP, nullptr);
// Create a filter object.
OH\_Drawing\_Filter \*filter = OH\_Drawing\_FilterCreate();
// Set an image filter object for the filter object.
OH\_Drawing\_FilterSetImageFilter(filter, imageFilter);
// Set the filter effect of the pen.
OH\_Drawing\_PenSetFilter(pen, filter);
// Set the pen on the canvas. Ensure that the canvas object has been obtained.
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// Create a rectangle.
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value300\_, value300\_, value900\_, value900\_);
// Draw a rectangle.
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// Remove the pen from the canvas.
OH\_Drawing\_CanvasDetachPen(canvas);
// Destroy objects.
OH\_Drawing\_PenDestroy(pen);
OH\_Drawing\_ImageFilterDestroy(imageFilter);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_FilterDestroy(filter);

| Original Image | Image with the Filter Effect |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/jXaEh5msSlyL3K5ypWm1Pw/en-us_image_0000002568764945.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=152AF21A185B140E28749876466C2466DEB24D23476A701FD546EE1F5B61DC79) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/blgRzQmpRkiPYgJ-kjFvrA/en-us_image_0000002537765220.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CF26B46E238C272F1F91F43B15CFB2417D4DF6A823D46F8694FB6F11D636162) |

## Mask Filter Effect

The blur effect of the mask filter only blurs the transparency and shape edges, which is less costly than that of the image filter.

The mask filter can be implemented based on the pen or brush. For details about the mask filter-related APIs and parameters, see [drawing\_mask\_filter.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-mask-filter-h).

You can use the **OH\_Drawing\_MaskFilterCreateBlur()** API to create a mask filter with the blur effect. The API takes three parameters, which are as follows:

-   **blurType**: specifies the blur type to be applied. For details, see [OH\_Drawing\_BlurType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-mask-filter-h#oh_drawing_blurtype).
    
-   **sigma**: specifies the standard deviation of the Gaussian blur to be applied. The standard deviation must be greater than 0.
    
-   **respectCTM**: specifies whether the standard deviation of the blur is modified by the coordinate transformation matrix (CTM). The default value is **true**, indicating that the standard deviation is modified.
    

The following uses the rectangle drawing and the mask filter effect implemented by a pen as an example. The sample code and effect are as follows:

// Create a pen object.
OH\_Drawing\_Pen \*pen = OH\_Drawing\_PenCreate();
// Set anti-aliasing for the pen.
OH\_Drawing\_PenSetAntiAlias(pen, true);
// Set the stroke color of the pen.
OH\_Drawing\_PenSetColor(pen, 0xffff0000);
// Set the pen width to 20.
OH\_Drawing\_PenSetWidth(pen, 20);
// Create a mask filter.
OH\_Drawing\_MaskFilter \*maskFilter = OH\_Drawing\_MaskFilterCreateBlur(OH\_Drawing\_BlurType::NORMAL, 20, true);
// Create a filter object.
OH\_Drawing\_Filter \*filter = OH\_Drawing\_FilterCreate();
// Set a mask filter object for the filter object.
OH\_Drawing\_FilterSetMaskFilter(filter, maskFilter);
// Set the filter effect of the pen.
OH\_Drawing\_PenSetFilter(pen, filter);
// Set the pen on the canvas. Ensure that the canvas object has been obtained.
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// Create a rectangle.
OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(value300\_, value300\_, value900\_, value900\_);
// Draw a rectangle.
OH\_Drawing\_CanvasDrawRect(canvas, rect);
// Remove the pen from the canvas.
OH\_Drawing\_CanvasDetachPen(canvas);
// Destroy objects.
OH\_Drawing\_PenDestroy(pen);
OH\_Drawing\_MaskFilterDestroy(maskFilter);
OH\_Drawing\_RectDestroy(rect);
OH\_Drawing\_FilterDestroy(filter);

| Original Image | Image with the Mask Effect |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/afhq6MI_TIC3PLLSVc0QkQ/en-us_image_0000002537925160.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=177D94B6C022D4AA185C189FBF962FEFECAE1EBEA57B673F26898C7541FC7A65) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/s3dcoOE_QYCnw1XIY2RwyQ/en-us_image_0000002568684937.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E3867B93A9779528DA6617248389856FB1F55B721FDE8FC0661FD412687C8F7) |
