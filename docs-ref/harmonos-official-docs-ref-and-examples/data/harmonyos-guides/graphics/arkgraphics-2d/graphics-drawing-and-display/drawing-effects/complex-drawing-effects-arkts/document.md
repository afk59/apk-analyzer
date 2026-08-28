# Complex Drawing Effects (ArkTS)

You can use a brush or a pen to implement complex drawing effects in addition to the basic fill color, stroke color, and style settings. For example:

-   Blend mode
    
-   Path effect, such as dashed lines
    
-   Shader effect, such as linear gradient and radial gradient
    
-   Filtering effect, such as blurring
    

#### Blend Mode

The blend mode can be used for brushes or pens. It defines how to combine source pixels (content to be drawn) with target pixels (content that already exists on the canvas).

You can use the **setBlendMode()** API to apply the blend mode to the brush or pen. This API requires the **BlendMode** parameter, that is, the type of the blend mode. For details, see [BlendMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing-e#blendmode).

The following shows the sample code and effect:

import { DrawContext, FrameNode, NodeController, RenderNode, UIContext } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

function drawRenderNode(canvas: drawing.Canvas) {
  canvas.saveLayer(null, null);
  const brushCircle = new drawing.Brush();
  const colorCircle: common2D.Color = {alpha: 255, red: 0, green: 0, blue: 255};
  brushCircle.setColor(colorCircle);
  canvas.attachBrush(brushCircle);
  canvas.drawCircle(500, 500, 200);
  const brush = new drawing.Brush();
  // Set the blend mode.
  brush.setBlendMode(drawing.BlendMode.SRC\_IN);
  canvas.saveLayer(null, brush);

  const brushRect = new drawing.Brush();
  const colorRect: common2D.Color = {alpha: 255, red: 255, green: 255, blue: 0};
  brushRect.setColor(colorRect);
  canvas.attachBrush(brushRect);
  const rect: common2D.Rect = {left:100, top:100, right:500, bottom:500};
  canvas.drawRect(rect);
  canvas.restore();
  canvas.restore();
  canvas.detachBrush();
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/dh2SPFLXRLeKYT9OuwpEbQ/en-us_image_0000002568684925.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2244ABEB0003B211BB20DD10755081185431F33B6CE2C66E9FDF0003840F634)

#### Path Effect

The path effect, such as dashed lines, is available only for the pen.

You can use the **createDashPathEffect()** API to set the path effect. The API takes two parameters, which are as follows:

-   Float array **intervals**: indicates the interval between dashed lines or dotted lines.
    
-   Float **phase**: indicates the offset in the intervals array, that is, the position from which the dashed line or dotted line effect is applied.
    

The following uses the dashed line path effect of a rectangle as an example. The sample code and effect are as follows:

// Create a pen object.
let pen = new drawing.Pen();
// Set the stroke width.
pen.setStrokeWidth(10.0);
// Set the color.
pen.setColor(0xFF, 0xFF, 0x00, 0x00);
// The effect is a cyclic repetition of a 10 px solid line, a 5 px interval, a 2 px solid line, and a 5 px interval.
let intervals = \[10, 5, 2, 5\];
// Set the dashed line path effect.
let effect = drawing.PathEffect.createDashPathEffect(intervals, 0);
pen.setPathEffect(effect);
// Set the stroke effect of the pen.
canvas.attachPen(pen);
// Create a rectangle.
let rect: common2D.Rect = {
  left: VALUE\_200,
  top: VALUE\_200,
  right: VALUE\_1000,
  bottom: VALUE\_700
};
// Draw a rectangle.
canvas.drawRect(rect);
// Remove the stroke effect.
canvas.detachPen();

| Original Image | Dashed Line Effect |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/Q72zcmC2SWu1JoUScLfPlQ/en-us_image_0000002568764935.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC6E36563A7E761118FBFCC160F3FA73292020E3E853CC876F45143608BA4893) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/lFDKKMdERNySmEawwPHnIw/en-us_image_0000002537765210.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C3C0F640F5A68BF71FB0CF69681583F45BF37E431A46F248AFBF7EBBAC4D329) |

#### Shader Effect

The shader effect is implemented based on the brush or pen. You can use the **setShaderEffect()** API to set the shader effect of the brush or pen. Currently, different shader effects are supported, such as linear gradient, radial gradient, and sector gradient.

For details about shader-related APIs and parameters, see [ShaderEffect](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing-shadereffect).

## Linear Gradient Shader Effect

You can use the **createLinearGradient()** API to create the linear gradient shader effect to be set. The API takes six parameters, which are the start point, end point, color array, tiling mode, relative position array, and matrix object.

-   The start point and end point are used to determine the gradient direction.
    
-   The color array is used to store the colors used in the gradient.
    
-   The relative position array is used to determine the relative position of each color in the gradient. If the relative position is empty, the colors are evenly distributed between the start point and end point.
    
-   Matrix object, which is used to perform matrix transformation on the shader. The default value is **null**, indicating the unit matrix.
    
-   The tiling mode is used to determine how to continue the gradient effect outside the gradient area. The options are as follows:
    
    -   **CLAMP**: Replicates the edge color if the image exceeds its original boundary.
    -   **REPEAT**: Repeats the image in both horizontal and vertical directions.
    -   **MIRROR**: Repeats the image in both horizontal and vertical directions and alternates the mirrored image between adjacent images.
    -   **DECAL**: Renders the shader effect's image only within the original boundary, and returns transparent black elsewhere.

The following uses the rectangle drawing and the linear gradient shader effect implemented by a brush as an example. The sample code and effect are as follows:

let startPt: common2D.Point = { x: VALUE\_100, y: VALUE\_100 };
let endPt: common2D.Point = { x: VALUE\_900, y: VALUE\_900 };
let colors = \[0xFFFFFF00, 0xFFFF0000, 0xFF0000FF\];
// Create a linear gradient shader.
let shaderEffect = drawing.ShaderEffect.createLinearGradient(startPt, endPt, colors, drawing.TileMode.CLAMP);
// Create a brush object.
let brush = new drawing.Brush();
// Set the linear shader.
brush.setShaderEffect(shaderEffect);
// Set the brush fill effect.
canvas.attachBrush(brush);
let rect: common2D.Rect = {
  left: VALUE\_100,
  top: VALUE\_100,
  right: VALUE\_900,
  bottom: VALUE\_900
};
// Draw a rectangle.
canvas.drawRect(rect);
// Remove the fill effect.
canvas.detachBrush();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/IiLUbIeRQzG4hzDlJ_WNcg/en-us_image_0000002537925150.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF057F706C85DE4A55E3623EEA67301766AFC388C387471703F80D9970849006)

## Radial Gradient Shader Effect

You can use the **createRadialGradient()** API to create the radial gradient shader effect to be set. The API takes six parameters, which are the center point (**centerPt**), radius (**radius**), color array (**colors**), tiling mode (**TileMode**), relative position array (**pos**), and matrix object (**matrix**).

The implementation method is similar to that of the linear gradient shader. The difference is that the radial gradient starts from the center and gradually changes outward.

The following uses the rectangle drawing and the radial gradient shader effect implemented by a brush as an example. The sample code and effect are as follows:

let centerPt: common2D.Point = { x: VALUE\_500, y: VALUE\_500 };
let colors = \[0xFFFF0000, 0xFF00FF00, 0xFF0000FF\];
// Create a radial gradient shader.
let shaderEffect = drawing.ShaderEffect.createRadialGradient(centerPt, VALUE\_600, colors, drawing.TileMode.CLAMP);
// Create a brush object.
let brush = new drawing.Brush();
// Set the radial gradient shader.
brush.setShaderEffect(shaderEffect);
// Set the brush fill effect.
canvas.attachBrush(brush);
let rect: common2D.Rect = {
  left: VALUE\_100,
  top: VALUE\_100,
  right: VALUE\_900,
  bottom: VALUE\_900
};
// Draw a rectangle.
canvas.drawRect(rect);
// Remove the fill effect.
canvas.detachBrush();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/edcg_U82Qmm-QUxL9fysTA/en-us_image_0000002568684927.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E84A8902098235727FFBA8CE100CB31D55706D91D900ECEA41B1BAD9757ADBB6)

## Sector Gradient Shader Effect

You can use the **createSweepGradient()** API to create the sector gradient shader effect to be set. The API takes seven parameters: which are the center coordinates (**centerPt**), color array (**colors**), tiling mode (**TileMode**), start angle of the sector gradient (**startAngle**), end angle of the sector gradient (**endAngle**), relative position array (**pos**), and matrix object (**matrix**).

The implementation method is similar to that of the linear gradient shader. The difference is that the sector gradient is gradually changed during rotation around the center point.

The following uses the rectangle drawing and the sector gradient shader effect implemented by a brush as an example. The sample code and effect are as follows:

let centerPt: common2D.Point = { x: VALUE\_500, y: VALUE\_500 };
let colors = \[0xFF00FFFF, 0xFFFF00FF, 0xFFFFFF00\];
// Create a sector gradient shader.
let shaderEffect = drawing.ShaderEffect.createSweepGradient(centerPt, colors, drawing.TileMode.CLAMP, 0, 360);
// Create a brush object.
let brush = new drawing.Brush();
// Set the sector gradient shader.
brush.setShaderEffect(shaderEffect);
// Set the brush fill effect.
canvas.attachBrush(brush);
let rect: common2D.Rect = {
  left: VALUE\_100,
  top: VALUE\_100,
  right: VALUE\_900,
  bottom: VALUE\_900
};
// Draw a rectangle.
canvas.drawRect(rect);
// Remove the fill effect.
canvas.detachBrush();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/hledLxF_RwiZnd0KgkWW5g/en-us_image_0000002568764937.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DB8F129E69807C5B80AE982936326AE5FEC03E954CCA2BBB849573A0F1B2603)

#### Filter Effects

The filter effect can be implemented based on the brush or pen. Currently, different filter effects are supported, such as image filters, color filters, and mask filters.

For details about the filter-related APIs and parameters, see [ImageFilter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing-imagefilter).

## Color Filter Effects

The color filter can be implemented based on the pen or brush. For details about the color filter-related APIs and parameters, see [ColorFilter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing-colorfilter).

Currently, multiple color filters can be implemented, including:

-   Color filter object with a given blend mode
    
-   Color filter object with a given 5 x 4 color matrix
    
-   Color filter object with the SRGB gamma curve applied to the RGB color channel
    
-   Color filter object with the RGB color channel applied to the SRGB gamma curve
    
-   Color filter object that multiplies the input luminance value by the transparency channel and sets the red, green, and blue channels to zero
    
-   Color filter object composed of two color filters
    

The following uses the color filter with a 5 x 4 color matrix as an example.

You can use the **createMatrixColorFilter()** API to create a color filter with a 5 x 4 color matrix. The API takes one parameter, which is the color matrix. The color matrix is a floating-point array of 20 elements. The array format is as follows:

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
let brush = new drawing.Brush();
// Set the color.
brush.setColor(0xFF, 0xFF, 0x00, 0x00);
// Set the color matrix.
let matrix: number\[\] = \[
  1, 0, 0, 0, 0,
  0, 1, 0, 0, 0,
  0, 0, 0.5, 0.5, 0,
  0, 0, 0.5, 0.5, 0
\];
// Create a color filter object with a given 5x4 color matrix.
let filter = drawing.ColorFilter.createMatrixColorFilter(matrix);
// Set the color filter.
brush.setColorFilter(filter);
// Set the brush fill effect.
canvas.attachBrush(brush);
let rect: common2D.Rect = {
  left: VALUE\_300,
  top: VALUE\_300,
  right: VALUE\_900,
  bottom: VALUE\_900
};
// Draw a rectangle.
canvas.drawRect(rect);
// Remove the fill effect.
canvas.detachBrush();

| Original Image | Image with a Color Filter Based on a 5×4 Color Matrix |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/-dikcdXyTBqr5QCDoV-M8w/en-us_image_0000002537765212.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C752A4DFCD4D051970203B75C119F642140402C57A498C5B496DD5FF4418517A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/mDZ6Qz2QSuait9Q2lxSL3w/en-us_image_0000002537925152.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9EA81FFB920E27E8B6C4E2F0F23C4F28EAA2033DA43B509EB544490D6F5003F) |

## Image Filter Effects

The image filter can be implemented based on the pen or brush. For details about the image filter-related APIs and parameters, see [ImageFilter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing-imagefilter).

Currently, only the following two types of image filters are supported:

-   Image filter based on the color filter
    
    You can use the **createFromColorFilter()** API to implement this type of image filter. This API takes two parameters: **colorFilter** and **imageFilter**. That is, the effect of the color filter is superimposed on the image filter. **imageFilter** can be empty, which means that only the color filter effect is added.
    
-   Image filter with a given blur effect
    
    You can use the **createBlurImageFilter()** API to implement this type of image filter. This API takes four parameters: **sigmaX**, **sigmaY**, **cTileMode**, and **imageFilter**. **sigmaX** and **sigmaY** are the standard deviations of the blur, **cTileMode** is the tiling mode, and **imageFilter** is the input image filter.
    
    The final effect is to blur the input image filter **imageFilter**. That is, the filter effect can be superimposed. **imageFilter** can be empty, which means that only the blur effect is added.
    

The following uses the rectangle drawing and the blur effect implemented by a pen as an example. The sample code and effect are as follows:

// Set the pen.
let pen = new drawing.Pen();
// Set the stroke width.
pen.setStrokeWidth(10.0);
// Set the color.
pen.setColor(0xFF, 0xFF, 0x00, 0x00);
// Create an image filter with the blur effect.
let filter = drawing.ImageFilter.createBlurImageFilter(20, 20, drawing.TileMode.CLAMP);
// Set the image filter.
pen.setImageFilter(filter);
// Set the stroke effect of the pen.
canvas.attachPen(pen);
let rect: common2D.Rect = {
  left: VALUE\_300,
  top: VALUE\_300,
  right: VALUE\_900,
  bottom: VALUE\_900
};
// Draw a rectangle.
canvas.drawRect(rect);
// Remove the stroke effect.
canvas.detachPen();

| Original Image | Blurred Image |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/FJylr42bQGCndIqcLWgbuQ/en-us_image_0000002568684929.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B16EEB2880DEF39B4D18A0BE0232CC538B584D5F9617E132C5A0799D9CFBEA3E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/KerTpEBoTxGjNF4AqXXBJw/en-us_image_0000002568764939.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D8EEA5E1BF288605EF9A811EF5A5698FFAF24AA53AE5EA2114207D55BEBC6C6) |

## Mask Filter Effect

The blur effect of the mask filter only blurs the transparency and shape edges, which is less costly than that of the image filter.

The mask filter can be implemented based on the pen or brush. For details about the mask filter-related APIs and parameters, see [MaskFilter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing-maskfilter).

You can use the **createBlurMaskFilter()** API to create a mask filter with the blur effect. The API takes two parameters, which are as follows:

-   **blurType**: specifies the blur type to be applied. For details, see [BlurType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing-e#blurtype12).
    
-   **sigma**: specifies the standard deviation of the Gaussian blur to be applied. The standard deviation must be greater than 0.
    

The following uses the rectangle drawing and the mask filter effect implemented by a pen as an example. The sample code and effect are as follows:

// Create a pen object.
let pen = new drawing.Pen();
// Set the stroke width.
pen.setStrokeWidth(10.0);
// Set the color.
pen.setColor(0xFF, 0xFF, 0x00, 0x00);
// Create a mask filter object with the blur effect.
let filter = drawing.MaskFilter.createBlurMaskFilter(drawing.BlurType.NORMAL, 20);
// Set the blur effect.
pen.setMaskFilter(filter);
// Set the stroke effect of the pen.
canvas.attachPen(pen);
let rect: common2D.Rect = {
  left: VALUE\_300,
  top: VALUE\_300,
  right: VALUE\_900,
  bottom: VALUE\_900
};
// Draw a rectangle.
canvas.drawRect(rect);
// Remove the stroke effect.
canvas.detachPen();

| Original Image | Blurred Image |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/F6P1GLPeQhaCeb5bC_OQKA/en-us_image_0000002568684929.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D1464D02E6C76B9DEBDB69D1871E67E8D6388B31D78C9749D0D88DE637D9AFA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/T2z7nJA8RnyLicGFopTjuQ/en-us_image_0000002568764939.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062048Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C9691CCB54B5CEC338943F654D083CDE31CA675BFE567349ADEFC2B13C6ED30) |
