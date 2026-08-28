# Drawing TextBlobs (ArkTS)

#### Overview

A TextBlob is a set of texts. You can draw both a single text and a paragraph by using TextBlobs.

In addition to the basic TextBlob drawing, you can add various drawing effects to texts. Common TextBlob drawing scenarios include [text stroke](#text-stroke) and [text gradient](#text-gradient). For more effects, see [Overview of Drawing Effects](../../drawing-effects/overview-of-drawing-effects/document.md).

This topic does not involve text measurement and typography. For details about how to handle text drawing requirements, see [Introduction to Text Development](../../../text/introduction-to-text-development/document.md). This topic describes the typography policies and related usage.

#### Basic TextBlob Drawing

The Canvas component draws TextBlobs using **drawTextBlob()**. This function takes three parameters: **TextBlob** object, and X and Y coordinates of the left end point of the text baseline.

For details about the **Canvas** object, see [Obtaining a Canvas and Displaying Drawing Results (ArkTS)](../../canvas-acquisition-and-display-of-drawing-results/obtaining-a-canvas-and-displaying-drawing-results-arkts/document.md).

A **TextBlob** object can be created in multiple ways. For details about how to create a block and how to use the API, see [TextBlob](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing-textblob).

The following uses the **makeFromString()** API as an example to create a **TextBlob** object. The API takes three parameters:

-   String text to be displayed.
    
-   **font** object, which is used to set and obtain various font attributes, such as the font size, text style, font alignment mode, font rendering mode, and font stroke mode. For details about the APIs, see [Font](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing-font).
    
-   Text encoding mode. The following modes are supported:
    
    -   **TEXT\_ENCODING\_UTF8**: One byte is used to indicate UTF-8 or ASCII characters.
    -   **TEXT\_ENCODING\_UTF16**: Two bytes are used to indicate most Unicode characters.
    -   **TEXT\_ENCODING\_UTF32**: Four bytes are used to indicate all Unicode characters.
    -   **TEXT\_ENCODING\_GLYPH\_ID**: Two bytes are used to indicate the glyph index.

The sample code and effect are as follows:

// Create a font object.
const font = new drawing.Font();
// Set the font size.
font.setSize(100);
// Create a TextBlob object.
const textBlob = drawing.TextBlob.makeFromString('Hello world', font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
// Draw the TextBlob.
canvas.drawTextBlob(textBlob, VALUE\_200, VALUE\_300);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/S8AOlj3xR-K_YAV8b3CMuw/en-us_image_0000002568764951.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=524D6A1A2EA7AF35CBCB81CF7921EB5D81392B26A3B818ECD98A51B9285A86B4)

#### Text Stroke

Based on the basic TextBlob drawing, you can also use the brush to implement the text stroke effect. For details, see [Stroke Effect](../../drawing-effects/basic-drawing-effects-arkts/document.md#stroke-effect).

The following uses English and Chinese text strokes as examples.

## English Text Stroke

The following shows the sample code and effect of English text strokes.

// Create a pen.
let pen = new drawing.Pen();
// Set anti-aliasing.
pen.setAntiAlias(true);
// Set the stroke width.
pen.setStrokeWidth(3.0);
// Set the stroke color.
pen.setColor(0xFF, 0xFF, 0x00, 0x00);
// Create a font object.
const font = new drawing.Font();
// Set the font size.
font.setSize(100);
// Add the pen stroke effect.
canvas.attachPen(pen);
// Create a TextBlob object.
const textBlob = drawing.TextBlob.makeFromString('Hello world', font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
// Draw the TextBlob.
canvas.drawTextBlob(textBlob, VALUE\_200, VALUE\_300);
// Remove the stroke effect.
canvas.detachPen();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/6ZR0mLRPS3ed5_QbQovKiQ/en-us_image_0000002537765226.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0E1C24292E78B4B581D27C236B7CF2FE4D063C81B5F36264CE81AC61A2E4682)

## Chinese Text Stroke

To achieve the stroke effect for Chinese text, first use a pen to outline the strokes, then apply a brush to fill the inner color and eliminate impurities and overlapping areas in the middle of the font.

The following shows the sample code and effect of Chinese text strokes.

// Create a brush.
let brush = new drawing.Brush();
// Create a pen.
let pen = new drawing.Pen();
// Set anti-aliasing.
brush.setAntiAlias(true);
// Set the stroke color.
brush.setColor(0xFF, 0xFF, 0xFF, 0xFF);

pen.setAntiAlias(true);
// Set the stroke width.
pen.setStrokeWidth(3.0);
// Set the stroke color.
pen.setColor(0xFF, 0xFF, 0x00, 0x00);

// Create a font object.
const font = new drawing.Font();
// Set the font size.
font.setSize(100);
// Add the pen stroke effect.
canvas.attachPen(pen);
// Create a TextBlob object.
const textBlob = drawing.TextBlob.makeFromString(STROKE\_SAMPLE, font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
// Draw the TextBlob.
canvas.drawTextBlob(textBlob, VALUE\_200,  VALUE\_300);
// Remove the stroke effect.
canvas.detachPen();

canvas.attachBrush(brush);
canvas.drawTextBlob(textBlob, VALUE\_200, VALUE\_300);
canvas.detachBrush();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/CuqgBqdhRUKS8M5QUNmdHQ/en-us_image_0000002537925166.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28AF53A9A7D8E1EFDE445B32835ABFEA487EF31F1BAD974B3D36DC9900FD4B4D)

#### Text Gradient

In addition to TextBlob drawing, you can use a shader to implement the gradient effect of text. For more information about shaders, see [Shader Effect](../../drawing-effects/complex-drawing-effects-arkts/document.md#shader-effect).

The following shows the sample code and effect of adding a linear gradient shader to text.

let startPt: common2D.Point = { x: VALUE\_100, y: VALUE\_100 };
let endPt: common2D.Point = { x: VALUE\_900, y: VALUE\_900 };
let colors = \[0xFFFFFF00, 0xFFFF0000, 0xFF0000FF\];
// Create a linear gradient shader.
let shaderEffect = drawing.ShaderEffect.createLinearGradient(startPt, endPt, colors, drawing.TileMode.CLAMP);
// Create a brush.
let brush = new drawing.Brush();
// Set the shader.
brush.setShaderEffect(shaderEffect);
// Add the brush fill effect.
canvas.attachBrush(brush);
// Create a font.
const font = new drawing.Font();
// Set the font size.
font.setSize(VALUE\_200);
// Create a TextBlob.
const textBlob = drawing.TextBlob.makeFromString('Hello world', font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
// Draw the TextBlob.
canvas.drawTextBlob(textBlob, VALUE\_100, VALUE\_300);
// Remove the fill effect.
canvas.detachBrush();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/mB7j9kQ5QxaQYkKVG5PzwQ/en-us_image_0000002568684943.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2875E16CE80910B31917BAB55CD7CAA2BA6C96F5521FCD1E9F2C70FCA25969A1)

#### Theme Font

Theme fonts are specialized custom fonts available for use in theme applications. For details about text measurement and typography, see [Using Theme Fonts (ArkTS)](../../../text/font-management/using-theme-fonts-arkts/document.md).

The following shows the sample code and effect for setting the theme font.

// Create a linear gradient shader.
const font = new drawing.Font();
// Set the text size.
font.setSize(100);
// Set the theme font.
font.setThemeFontFollowed(true);
// Create a TextBlob object.
const textBlob = drawing.TextBlob.makeFromString('Hello World', font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
// Draw the TextBlob.
canvas.drawTextBlob(textBlob, VALUE\_200, VALUE\_300);

| Theme Font Not Followed | Theme Font Followed (For Reference) |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/GZpEsR-uQmiVj5CJyMjeQw/en-us_image_0000002568764953.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD1CBBC31C568E73FC91F87CC396A369ADA393AD0138877CF4854517F1BFC58C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/1bhwRH2fRLmEmLBuvlfP0A/en-us_image_0000002537765228.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2178CF71EC9A7BBE3D77BF6C1B13CA9700FF981E0E44961FC45709FC788D01DB) |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/Sd7GXmyVT0K_FhPqUVhYvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA13F57C76FA823329B9C286CAC560CDD024D97EB9B8D51968EAF3983C5C2048)

You need to override the **onConfigurationUpdate** function in the application entry file (**EntryAbility.ets** in the default project) to respond to the theme font switching operation, ensuring that the page can be refreshed and take effect in a timely manner after the switching. For details, see [Using Theme Fonts (ArkTS)](../../../text/font-management/using-theme-fonts-arkts/document.md).

#### Single-Character Drawing

Single-character drawing is a refined technology for controlling text rendering. Compared with TextBlob drawing, single-character drawing has the following advantages: The font degradation mechanism is used. If a character cannot be displayed in the current font, the system automatically uses the system font to draw the character, improving compatibility with special characters and avoiding character loss. In addition, single-character drawing supports character-by-character configuration of font features (such as ligatures and alternates) to meet complex typography requirements for better user experience. For details about the APIs, see [drawing.Canvas](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing-canvas#drawsinglecharacter12).

Basic scenario: drawing characters without font features

In common text rendering scenarios where font features are not required, you can use **drawSingleCharacter** to draw a single character and use **measureSingleCharacter** to measure the width of a single character. The sample code and effect are as follows:

// Create a font object.
const font = new drawing.Font();
// Set the text size.
font.setSize(100);
let startX = 100;
let startY = 100;
let text = \['H', 'e', 'l', 'l', 'o'\];
for (let s of text) {
  // Draw a single character.
  canvas.drawSingleCharacter(s, font, startX, startY);
  // Measure the width of a single character.
  let textWidth = font.measureSingleCharacter(s);
  startX += textWidth;
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/DkIoqeP2Tp2DGxyvTUrfPw/en-us_image_0000002537925168.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27A65AD7C3AD74BD418271C88F1C57AEA52A75D5FC6AD28E8E2ED09CE816AC69)

Advanced scenario: drawing characters with font features

In text rendering scenarios where font features are required, you can use **drawSingleCharacterWithFeatures** to draw a single character and use **measureSingleCharacterWithFeatures** to measure the width of a single character. The sample code and effect are as follows:

// Create a font object.
const font = new drawing.Font();
// Set the text size.
font.setSize(100);
let startX = 100;
let startY = 100;
let text = \['a', '2', '+', 'b', '2'\];
// Create an array of font feature objects.
let fontFeatures: drawing.FontFeature\[\] = \[{name: 'frac', value: 1}\];
for (let s of text) {
  // Draw a single character.
  canvas.drawSingleCharacterWithFeatures(s, font, startX, startY, fontFeatures);
  // Measure the width of a single character.
  let textWidth = font.measureSingleCharacterWithFeatures(s, fontFeatures);
  startX += textWidth;
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/_f7d3JvETVSIIRQw9qcWUg/en-us_image_0000002568684945.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=635BB29DDBC15ECBC595B4F5C2D433263A42569D0733F174F7E10BFE76D9019B)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/2qCs0L0eRG2r6LOhA2hoMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13E5CA9809042C6C24D6176E56C62395F2B1AA6DCCB77815C534CD18299DDFC3)

If drawSingleCharacterWithFeatures and measureSingleCharacter are used together, or drawSingleCharacter and measureSingleCharacterWithFeatures are used together, font drawing may overlap.
