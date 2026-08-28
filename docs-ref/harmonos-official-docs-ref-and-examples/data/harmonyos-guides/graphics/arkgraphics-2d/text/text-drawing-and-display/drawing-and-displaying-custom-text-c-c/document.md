# Drawing and Displaying Custom Text (C/C++)

In complex text typesetting scenarios, if the standard text components provided by the system cannot meet specific visual or interaction requirements, you can use the underlying text drawing capability provided by ArkGraphics 2D to directly control the canvas and text style to implement refined control over the text appearance and layout. This capability applies to scenarios that require highly customized text rendering effects, such as artistic fonts, complex rich text orchestration, or special dynamic text effects.

As a core component of the graphics system, the font engine is responsible for converting character codes into visual glyphs and accurately calculating the layout and position of each glyph, providing underlying support for custom text drawing. Through the text measurement API, you can obtain the accurate size of the text, which is the basis for precise layout (such as center display).

#### Text shaping

## Overview

Text shaping is a key capability provided by the font engine. It allows developers to directly obtain the underlying glyph information (such as width and direction measurement information) of the text without going through the default text typesetting process. This enables developers to implement completely customized typesetting logic, drawing operations, and line break policies based on the raw data.

This capability applies to the following scenarios:

-   Custom rich text rendering: For example, in applications such as social media and news clients, image-text mixed typesetting and multi-style text mixed display need to be implemented.
    
-   Cross-platform consistent typesetting requirements: Ensure that the text is displayed with consistent visual effects on different platforms or devices.
    
-   Refined typesetting management: For example, implement artistic typesetting and dynamic text layout, which are difficult to achieve using standard text components.
    

## Available APIs

The following table lists the common APIs used in text shaping. For details about the APIs, see [drawing\_text\_typography.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-text-typography-h) and [drawing\_text\_blob.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-text-blob-h).

| API | Description |
| :-- | :-- |
| OH\_Drawing\_LineTypography\* OH\_Drawing\_CreateLineTypography(OH\_Drawing\_TypographyCreate\* handler) | Creates a pointer to the OH\_Drawing\_LineTypography object, which stores the text content and style and can be used to calculate the layout information of a single line. |
| OH\_Drawing\_TextLine\* OH\_Drawing\_LineTypographyCreateLine(OH\_Drawing\_LineTypography\* lineTypography,size\_t startIndex, size\_t count) | Creates a pointer to the OH\_Drawing\_TextLine object based on the text content in the specified range. |
| OH\_Drawing\_Array\* OH\_Drawing\_TextLineGetGlyphRuns(OH\_Drawing\_TextLine\* line) | Obtains the array of glyph runs in a text line object. |
| OH\_Drawing\_Array\* OH\_Drawing\_GetRunGlyphs(OH\_Drawing\_Run\* run, int64\_t start, int64\_t length) | Obtains an array of glyphs within the specified range of a run. |
| OH\_Drawing\_Font\* OH\_Drawing\_GetRunFont(OH\_Drawing\_Run\* run) | Obtains the font object of a run. |
| OH\_Drawing\_Array\* OH\_Drawing\_GetRunGlyphAdvances(OH\_Drawing\_Run\* run, uint32\_t start, uint32\_t length) | Obtains the glyph advance array of a run. |
| OH\_Drawing\_TextBlobBuilder\* OH\_Drawing\_TextBlobBuilderCreate(void) | Creates an **OH\_Drawing\_TextBlobBuilder** object. |
| OH\_Drawing\_TextBlob\* OH\_Drawing\_TextBlobBuilderMake(OH\_Drawing\_TextBlobBuilder\* textBlobBuilder) | Makes an **OH\_Drawing\_TextBlob** object from an **OH\_Drawing\_TextBlobBuilder**. |
| void OH\_Drawing\_CanvasDrawTextBlob(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_TextBlob\* textBlob, float x, float y) | Draws a text blob. |

## How to Develop

Since API version 18, the text shaping result can be obtained. Since API version 20, the text layout direction and text glyph width can be obtained. Sample code:

1.  Add the following libraries to the src/main/cpp/CMakeLists.txt file of the project.
    
    libnative\_drawing.so
    
2.  Import the dependency header file.
    
    #include <native\_drawing/drawing\_font\_collection.h>
    #include <native\_drawing/drawing\_text\_typography.h>
    #include <native\_drawing/drawing\_text\_blob.h>
    #include <native\_drawing/drawing\_text\_line.h>
    #include <native\_drawing/drawing\_text\_run.h>
    #include <native\_drawing/drawing\_text\_lineTypography.h>
    #include <native\_drawing/drawing\_rect.h>
    #include <native\_drawing/drawing\_point.h>
    
3.  Create a paragraph style and use the ParagraphBuilder to generate a paragraph instance.
    
     // Create a TypographyStyle. It is required when creating TypographyCreate.
     OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
     // Set the text color, size, and weight. If TextStyle is not set, the default TextStyle in TypographyStyle is used.
     OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
     OH\_Drawing\_SetTextStyleFontSize(txtStyle, 100);
    
     // Create a FontCollection object to manage font matching logic.
     OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
     // Use the FontCollection object and the TypographyStyle object to create a TypographyCreate object for creating a Typography object.
     OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
    
4.  Set the text style and add text content.
    
     // Set the text content and add the text to the handler.
     OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
     const char \*text = "Hello World";
     OH\_Drawing\_TypographyHandlerAddText(handler, text);
    
5.  Create a line object. Obtain the shaping result of all texts in a line.
    
    Use the OH\_Drawing\_LineTypographyCreateLine() method to create a single line object, and use the OH\_Drawing\_TextLineGetGlyphRuns() method of the line object to obtain text units with the same style.
    
     // Create a Typography object through the handler.
     OH\_Drawing\_LineTypography \*lineTypography = OH\_Drawing\_CreateLineTypography(handler);
     OH\_Drawing\_TextLine \*textLine = OH\_Drawing\_LineTypographyCreateLine(lineTypography, 0, 11);
     // Obtain the shaping result.
     OH\_Drawing\_Array \*runs = OH\_Drawing\_TextLineGetGlyphRuns(textLine);
    
6.  This step is the custom drawing step in the text shaping process. You can call the OH\_Drawing\_GetRunGlyphs() method to obtain the glyph sequence number corresponding to each character in the text, and then obtain the font object using the OH\_Drawing\_GetRunFont() method to determine the specific graphic information of each glyph.
    
    From API version 20 onwards, the new OH\_Drawing\_GetRunGlyphAdvances() method can return an array that contains the recommended width and height of each glyph during drawing. Based on these precise measurement data, you can freely calculate and define the drawing position of each glyph to implement complex text layout effects, such as custom character spacing, vertical offset, or special typesetting.
    
    for (int i = 0; i < runsLength; i++) {
         OH\_Drawing\_Run \*run = OH\_Drawing\_GetRunByIndex(runs, i);
         // Obtain all glyph data.
         OH\_Drawing\_Array \*glyphs = OH\_Drawing\_GetRunGlyphs(run, 0, 0);
         size\_t glyphsLength = OH\_Drawing\_GetDrawingArraySize(glyphs);
         // Obtain the font of the same drawing unit.
         OH\_Drawing\_Font \*font = OH\_Drawing\_GetRunFont(run);
         OH\_Drawing\_Array \*advances = OH\_Drawing\_GetRunGlyphAdvances(run, 0, 0);
    
         OH\_Drawing\_TextBlobBuilder \*builder = OH\_Drawing\_TextBlobBuilderCreate();
         OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(0, 0, 20, 20);
         const OH\_Drawing\_RunBuffer \*runBuffer =
             OH\_Drawing\_TextBlobBuilderAllocRunPos(builder, font, glyphsLength, rect);
         
         // Create a glyph buffer and draw glyphs independently through the drawing API.
         int x = 0, y = 0;
         for (int index = 0; index < glyphsLength; index++) {
             uint16\_t glyph = OH\_Drawing\_GetRunGlyphsByIndex(glyphs, index);
    
             runBuffer->glyphs\[index\] = glyph;
             runBuffer->pos\[index \* 2\] = x;
             runBuffer->pos\[index \* 2 + 1\] = y;
    
             OH\_Drawing\_Point \*advance = OH\_Drawing\_GetRunGlyphAdvanceByIndex(advances, index);
             float glyphX = 0;
             float glyphY = 0;
             OH\_Drawing\_PointGetX(advance, &glyphX);
             OH\_Drawing\_PointGetY(advance, &glyphY);
             x += glyphX + 10; // The horizontal spacing between glyphs is 10 px.
             y += glyphY + 30; // The vertical spacing between glyphs is 30 px.
         }
         
         // Draw a series of consecutive glyphs with the same attributes.
         OH\_Drawing\_TextBlob\* textBlob = OH\_Drawing\_TextBlobBuilderMake(builder);
         OH\_Drawing\_CanvasDrawTextBlob(cCanvas\_, textBlob, 20, 100);
         
         // Release the memory.
         OH\_Drawing\_TextBlobDestroy(textBlob);
         OH\_Drawing\_FontDestroy(font);
         OH\_Drawing\_DestroyRunGlyphAdvances(advances);
         OH\_Drawing\_DestroyRunGlyphs(glyphs);
    }
    
7.  Releasing memory
    
    // Release the memory.
    OH\_Drawing\_DestroyTypographyStyle(typoStyle);
    OH\_Drawing\_DestroyTextStyle(txtStyle);
    OH\_Drawing\_DestroyFontCollection(fc);
    OH\_Drawing\_DestroyTypographyHandler(handler);
    OH\_Drawing\_DestroyLineTypography(lineTypography);
    OH\_Drawing\_DestroyTextLine(textLine);
    OH\_Drawing\_DestroyRuns(runs);
    

## Sample Code

The following is a complete example of text shaping.

// Create a TypographyStyle. This TypographyStyle will be used when creating TypographyCreate.
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// Set the text color, size, and weight. If TextStyle is not set, the default TextStyle in TypographyStyle will be used.
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TEN(width\_));

// Create a FontCollection, which is used to manage the font matching logic.
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
// Use FontCollection and the created TypographyStyle to create TypographyCreate. TypographyCreate is used to create Typography.
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
// Set the text content and add the text to the handler.
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
const char \*text = "Hello World";
OH\_Drawing\_TypographyHandlerAddText(handler, text);

// Create a Typography through the handler.
OH\_Drawing\_LineTypography \*lineTypography = OH\_Drawing\_CreateLineTypography(handler);
// Create a TextLine and obtain characters (0, 11).
OH\_Drawing\_TextLine \*textLine = OH\_Drawing\_LineTypographyCreateLine(lineTypography, 0, 11);

// Obtain the shaping result.
OH\_Drawing\_Array \*runs = OH\_Drawing\_TextLineGetGlyphRuns(textLine);
size\_t runsLength = OH\_Drawing\_GetDrawingArraySize(runs);
for (int i = 0; i < runsLength; i++) {
    OH\_Drawing\_Run \*run = OH\_Drawing\_GetRunByIndex(runs, i);
    // Obtain all glyph data.
    OH\_Drawing\_Array \*glyphs = OH\_Drawing\_GetRunGlyphs(run, 0, 0);
    size\_t glyphsLength = OH\_Drawing\_GetDrawingArraySize(glyphs);
    // Obtain the font of the same drawing unit.
    OH\_Drawing\_Font \*font = OH\_Drawing\_GetRunFont(run);
    OH\_Drawing\_Array \*advances = OH\_Drawing\_GetRunGlyphAdvances(run, 0, 0);

    OH\_Drawing\_TextBlobBuilder \*builder = OH\_Drawing\_TextBlobBuilderCreate();
    // Create a 20 x 20 rectangle.
    OH\_Drawing\_Rect \*rect = OH\_Drawing\_RectCreate(0, 0, 20, 20);
    const OH\_Drawing\_RunBuffer \*buffer = OH\_Drawing\_TextBlobBuilderAllocRunPos(builder, font, glyphsLength, rect);

    // Create a glyph buffer and draw glyphs independently through the drawing API.
    int x = 0;
    int y = 0;
    for (int index = 0; index < glyphsLength; index++) {
        buffer->glyphs\[index\] = OH\_Drawing\_GetRunGlyphsByIndex(glyphs, index);
        // Set the glyph position.
        buffer->pos\[index \* TWO\_INT\] = x;
        buffer->pos\[index \* TWO\_INT + 1\] = y;

        OH\_Drawing\_Point \*advance = OH\_Drawing\_GetRunGlyphAdvanceByIndex(advances, index);
        float pos = 0;
        OH\_Drawing\_PointGetX(advance, &pos);
        x += pos + 10; // The horizontal spacing between glyphs is 10 px.
        OH\_Drawing\_PointGetY(advance, &pos);
        y += pos + 30; // The vertical spacing between glyphs is 30 px.
    }

    // Draw a series of consecutive glyphs with the same attributes.
    OH\_Drawing\_TextBlob \*textBlob = OH\_Drawing\_TextBlobBuilderMake(builder);
    // Draw the text to the canvas (20, 100).
    OH\_Drawing\_CanvasDrawTextBlob(cCanvas\_, textBlob, 20, 100);

    // Release the memory.
    OH\_Drawing\_TextBlobDestroy(textBlob);
    OH\_Drawing\_FontDestroy(font);
    OH\_Drawing\_DestroyRunGlyphAdvances(advances);
    OH\_Drawing\_DestroyRunGlyphs(glyphs);
}

// Release the memory.
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyLineTypography(lineTypography);
OH\_Drawing\_DestroyTextLine(textLine);
OH\_Drawing\_DestroyRuns(runs);

Effect:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/3hOS7gTUQWKQCojeJtwhIA/en-us_image_0000002537925204.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6ED5B856807E6CC1F0E27B205E0E7AB84EA0B98EADFB9A6FF58AC7C67F20F63C)
