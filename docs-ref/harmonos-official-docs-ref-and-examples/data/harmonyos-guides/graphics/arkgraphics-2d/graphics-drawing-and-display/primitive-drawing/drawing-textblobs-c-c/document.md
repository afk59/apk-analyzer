# Drawing TextBlobs (C/C++)

#### Overview

A TextBlob is a set of texts. You can draw both a single text and a paragraph by using TextBlobs.

In addition to the basic TextBlob drawing, you can add various drawing effects to texts. Common TextBlob drawing scenarios include [text stroke](#text-stroke) and [text gradient](#text-gradient). For more effects, see [Overview of Drawing Effects](../../drawing-effects/overview-of-drawing-effects/document.md).

This topic does not involve text measurement and typography. For details about how to handle text drawing requirements, see [Introduction to Text Development](../../../text/introduction-to-text-development/document.md). This topic describes the typography policies and related usage.

#### Basic TextBlob Drawing

Use the **OH\_Drawing\_CanvasDrawTextBlob()** API to draw a TextBlob. The API takes four parameters: **Canvas** object, **TextBlob** object, and X and Y coordinates of the left endpoint of the text baseline.

For details about the **Canvas** object, see [Obtaining a Canvas and Displaying Drawing Results (C/C++)](../../canvas-acquisition-and-display-of-drawing-results/obtaining-a-canvas-and-displaying-drawing-results-c-c/document.md).

A **TextBlob** object can be created in multiple ways. For details about how to create a block, see [drawing\_text\_blob.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-text-blob-h).

The following uses the **OH\_Drawing\_TextBlobCreateFromString()** API as an example to create a **TextBlob** object. The API takes three parameters:

-   Text string to be displayed.
    
-   Pointer to the **OH\_Drawing\_Font** object, which is used to set and obtain various font attributes, such as the font size, text style, font alignment mode, font rendering mode, and font stroke mode. For details about the APIs, see [draw\_font](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-font-h).
    
-   Text encoding mode.
    

The following shows the sample code and effect:

// Create a font object.
OH\_Drawing\_Font \*font = OH\_Drawing\_FontCreate();
// Set the font size.
OH\_Drawing\_FontSetTextSize(font, value100\_);
// Text to be drawn.
const char \*str = "Hello world";
// Create a TextBlob object.
OH\_Drawing\_TextBlob \*textBlob =
    OH\_Drawing\_TextBlobCreateFromString(str, font, OH\_Drawing\_TextEncoding::TEXT\_ENCODING\_UTF8);
// Draw the TextBlob.
OH\_Drawing\_CanvasDrawTextBlob(canvas, textBlob, value200\_, value800\_);
// Release the TextBlob object.
OH\_Drawing\_TextBlobDestroy(textBlob);
// Release the font object.
OH\_Drawing\_FontDestroy(font);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/8XmP_qfrRXyKxDATlDox-g/en-us_image_0000002568684949.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B924EC0B0DA31195B47AB9AE18F731384EF42FF9267299E4CDFC0E03053723F)

#### Text Stroke

Based on the basic TextBlob drawing, you can also use the brush to implement the text stroke effect. For details, see [Stroke Effect](../../drawing-effects/basic-drawing-effects-c-c/document.md#stroke-effect).

The following uses English and Chinese text strokes as examples.

## English Text Stroke

The following shows the sample code and effect of English text strokes.

// Create a pen.
OH\_Drawing\_Pen \*pen = OH\_Drawing\_PenCreate();
// Set anti-aliasing.
OH\_Drawing\_PenSetAntiAlias(pen, true);
// Set the stroke color.
OH\_Drawing\_PenSetColor(pen, OH\_Drawing\_ColorSetArgb(RGBA\_MAX, RGBA\_MAX, RGBA\_MIN, RGBA\_MIN));
// Set the stroke width to 3.
OH\_Drawing\_PenSetWidth(pen, 3);
// Set the stroke effect of the pen.
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// Create a font object.
OH\_Drawing\_Font \*font = OH\_Drawing\_FontCreate();
// Set the font size.
OH\_Drawing\_FontSetTextSize(font, value150\_);
const char \*str = "Hello world";
// Create a TextBlob object.
OH\_Drawing\_TextBlob \*textBlob =
    OH\_Drawing\_TextBlobCreateFromString(str, font, OH\_Drawing\_TextEncoding::TEXT\_ENCODING\_UTF8);
// Draw the TextBlob.
OH\_Drawing\_CanvasDrawTextBlob(canvas, textBlob, value200\_, value800\_);
// Remove the stroke effect.
OH\_Drawing\_CanvasDetachPen(canvas);
// Destroy objects.
OH\_Drawing\_TextBlobDestroy(textBlob);
OH\_Drawing\_FontDestroy(font);
OH\_Drawing\_PenDestroy(pen);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/smeDfGO5RD2NCGWM-AGhjg/en-us_image_0000002568764959.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B839277ED857FDF52564AAB372F73E2E44E3D5BF80638EA5527CB5AD135B152)

## Chinese Text Stroke

To achieve the stroke effect for Chinese text, first use a pen to outline the strokes, then apply a brush to fill the inner color and eliminate impurities and overlapping areas in the middle of the font.

The following shows the sample code and effect of Chinese text strokes.

// Create a brush.
OH\_Drawing\_Brush \*brush = OH\_Drawing\_BrushCreate();
// Create a pen.
OH\_Drawing\_Pen \*pen = OH\_Drawing\_PenCreate();
// Set anti-aliasing for the brush.
OH\_Drawing\_BrushSetAntiAlias(brush, true);
// Set the stroke color of the brush.
OH\_Drawing\_BrushSetColor(brush, OH\_Drawing\_ColorSetArgb(0xFF, 0xFF, 0xFF, 0xFF));
// Set anti-aliasing for the pen.
OH\_Drawing\_PenSetAntiAlias(pen, true);
// Set the stroke width to 3.
OH\_Drawing\_PenSetWidth(pen, 3);
// Set the stroke color of the pen.
OH\_Drawing\_PenSetColor(pen, OH\_Drawing\_ColorSetArgb(0xFF, 0xFF, 0x00, 0x00));
// Set the stroke effect of the pen.
OH\_Drawing\_CanvasAttachPen(canvas, pen);
// Create a font object.
OH\_Drawing\_Font \*font = OH\_Drawing\_FontCreate();
// Set the font size.
OH\_Drawing\_FontSetTextSize(font, value150\_);
const char \*str = "你好";
// Create a TextBlob object.
OH\_Drawing\_TextBlob \*textBlob =
    OH\_Drawing\_TextBlobCreateFromString(str, font, OH\_Drawing\_TextEncoding::TEXT\_ENCODING\_UTF8);
// Draw the TextBlob.
OH\_Drawing\_CanvasDrawTextBlob(canvas, textBlob, value200\_, value800\_);
// Remove the stroke effect.
OH\_Drawing\_CanvasDetachPen(canvas);
// Set the stroke effect of the brush.
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
OH\_Drawing\_CanvasDrawTextBlob(canvas, textBlob, value200\_, value800\_);

// Destroy objects.
OH\_Drawing\_TextBlobDestroy(textBlob);
OH\_Drawing\_FontDestroy(font);
OH\_Drawing\_PenDestroy(pen);
OH\_Drawing\_BrushDestroy(brush);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/jpA4i17rTdKQ2HbxKzJmsQ/en-us_image_0000002537765234.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CD35D4944DDDD57F1D2283D2FF523125939D3B464DC12D49205A243041AAC83)

#### Text Gradient

In addition to TextBlob drawing, you can use a shader to implement the gradient effect of text. For more information about shaders, see [Shader Effect](../../drawing-effects/complex-drawing-effects-c-c/document.md#shader-effect).

The following shows the sample code and effect of adding a linear gradient shader to text.

// Start point.
OH\_Drawing\_Point \*startPt = OH\_Drawing\_PointCreate(value100\_, value100\_);
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
OH\_Drawing\_Brush \*brush = OH\_Drawing\_BrushCreate();
// Set the shader effect based on the brush.
OH\_Drawing\_BrushSetShaderEffect(brush, colorShaderEffect);
// Set the brush fill effect.
OH\_Drawing\_CanvasAttachBrush(canvas, brush);
// Create a font object.
OH\_Drawing\_Font \*font = OH\_Drawing\_FontCreate();
// Set the font size.
OH\_Drawing\_FontSetTextSize(font, value150\_);
const char \*str = "Hello world";
// Create a TextBlob object.
OH\_Drawing\_TextBlob \*textBlob =
    OH\_Drawing\_TextBlobCreateFromString(str, font, OH\_Drawing\_TextEncoding::TEXT\_ENCODING\_UTF8);
// Draw the TextBlob.
OH\_Drawing\_CanvasDrawTextBlob(canvas, textBlob, value200\_, value800\_);
// Cancel the fill effect.
OH\_Drawing\_CanvasDetachBrush(canvas);
// Destroy objects.
OH\_Drawing\_TextBlobDestroy(textBlob);
OH\_Drawing\_FontDestroy(font);
OH\_Drawing\_BrushDestroy(brush);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/2l8bM5qnToiKy3r-IzSMeg/en-us_image_0000002537925174.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E27A07A208760E978E7F3B3E0AA9C8404593C13DBFB152BD748E069507C3F05)

#### Theme Font

Theme fonts are specialized custom fonts available for use in theme applications. For details about text measurement and typography, see [Using Theme Fonts (C/C++)](../../../text/font-management/using-theme-fonts-c-c/document.md).

The following shows the sample code and effect for setting the theme font.

// Create a font object.
OH\_Drawing\_Font \*font = OH\_Drawing\_FontCreate();
// Set the text size.
OH\_Drawing\_FontSetTextSize(font, value100\_);
// Set the theme font.
OH\_Drawing\_FontSetThemeFontFollowed(font, true);
// Text to be drawn.
const char \*str = "Hello World";
// Create a TextBlob object.
OH\_Drawing\_TextBlob \*textBlob =
    OH\_Drawing\_TextBlobCreateFromString(str, font, OH\_Drawing\_TextEncoding::TEXT\_ENCODING\_UTF8);
// Draw the TextBlob.
OH\_Drawing\_CanvasDrawTextBlob(canvas, textBlob, value200\_, value800\_);
// Release the TextBlob object.
OH\_Drawing\_TextBlobDestroy(textBlob);
// Release the font object.
OH\_Drawing\_FontDestroy(font);

| Theme Font Not Followed | Theme Font Followed (For Reference) |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/ht38ojZtS9mwPcLCs4-CFg/en-us_image_0000002568764953.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6590649F47C08B039693AB042F013408FC80E5027127AB97A41B5B65644A098C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/4Ff7DurmSbGoZNltjSMbSQ/en-us_image_0000002537765228.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79F5F7E10218C83A7D942846CF4ADF46A436517F6222EF21C6058A56874DCFDD) |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/F2Cdlq1aTrKq_yziC5KiSQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82C4DDC6263971A254215A27569A16A531D49D4661F289E26F09292829B22875)

You need to override the **onConfigurationUpdate** function in the application entry file (**EntryAbility.ets** in the default project) to respond to the theme font switching operation, ensuring that the page can be refreshed and take effect in a timely manner after the switching. For details, see [Using Theme Fonts (C/C++)](../../../text/font-management/using-theme-fonts-c-c/document.md).

#### Single-Character Drawing

Single-character drawing is a refined technology for controlling text rendering. Compared with TextBlob drawing, single-character drawing has the following advantages: The font degradation mechanism is used. If a character cannot be displayed in the current font, the system automatically uses the system font to draw the character, improving compatibility with special characters and avoiding character loss. In addition, single-character drawing supports character-by-character configuration of font features (such as ligatures and alternates) to meet complex typography requirements for better user experience. For details about the APIs, see [drawing\_canvas.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-canvas-h#oh_drawing_canvasdrawsinglecharacter).

Basic scenario: drawing characters without font features

In common text rendering scenarios where font features are not required, you can use **OH\_Drawing\_CanvasDrawSingleCharacter** to draw a single character and use **OH\_Drawing\_FontMeasureSingleCharacter** to measure the width of a single character. The sample code and effect are as follows:

// Create a font object.
OH\_Drawing\_Font \*font = OH\_Drawing\_FontCreate();
// Set the text size.
OH\_Drawing\_FontSetTextSize(font, value100\_);
float startX = 100;
float startY = 100;
int strLen = 5;
const char\* str = "Hello";
for (int i = 0; i < strLen; ++i) {
    // Draw a single character.
    OH\_Drawing\_CanvasDrawSingleCharacter(canvas, &str\[i\], font, startX, startY);
    float textWidth = 0.f;
    // Measure the width of a single character.
    OH\_Drawing\_FontMeasureSingleCharacter(font, &str\[i\], &textWidth);
    startX += textWidth;
}
// Release the font object.
OH\_Drawing\_FontDestroy(font);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/FyqlzOi0R06p-SEIeVFQKA/en-us_image_0000002537925168.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=004E06CF37413016B034FC739042EF0A896D779DF5CB6B923456A3BD67F04AF2)

Advanced scenario: drawing characters with font features

In text rendering scenarios where font features are required, you can use **OH\_Drawing\_CanvasDrawSingleCharacterWithFeatures** to draw a single character and use **OH\_Drawing\_FontMeasureSingleCharacterWithFeatures** to measure the width of a single character. The sample code and effect are as follows:

// Create a font object.
OH\_Drawing\_Font \*font = OH\_Drawing\_FontCreate();
// Set the text size.
OH\_Drawing\_FontSetTextSize(font, value100\_);
// Create a font feature object.
OH\_Drawing\_FontFeatures\* features = OH\_Drawing\_FontFeaturesCreate();
OH\_Drawing\_FontFeaturesAddFeature(features, "frac", 1);
float startX = 100;
float startY = 100;
int strLen = 5;
const char\* str = "a2+b2";
for (int i = 0; i < strLen; ++i) {
    // Draw a single character.
    OH\_Drawing\_CanvasDrawSingleCharacterWithFeatures(canvas, &str\[i\], font, startX, startY, features);
    float textWidth = 0.f;
    // Measure the width of a single character.
    OH\_Drawing\_FontMeasureSingleCharacterWithFeatures(font, &str\[i\], features, &textWidth);
    startX += textWidth;
}
// Release the font feature object.
OH\_Drawing\_FontFeaturesDestroy(features);
// Release the font object.
OH\_Drawing\_FontDestroy(font);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Y3hBlN3nTM2mpbptFlB_pQ/en-us_image_0000002568684945.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F87B079EE8C68DD67110643D21A55C000707AD602291BCCD208F1E562FE3D93)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/YfPw4q-RQ_SKF8aal78lFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F497835C7B6DEE86C1EEB5B1641CF5C723FD479B8AD7122BF75AB7E22FF546E)

If OH\_Drawing\_CanvasDrawSingleCharacterWithFeatures and OH\_Drawing\_FontMeasureSingleCharacter are used together, or OH\_Drawing\_CanvasDrawSingleCharacter and OH\_Drawing\_FontMeasureSingleCharacterWithFeatures are used together, font drawing may overlap.
