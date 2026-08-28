# Drawing and Displaying Simple Text (C/C++)

#### Overview

In a simple user interface, only a few lines of static text need to be displayed, such as the text on a label, button, menu item, or status bar. In this case, you only need to select a proper font, size, and color to complete the rendering.

#### Available APIs

| API Definition | Description |
| :-- | :-- |
| OH\_Drawing\_TextStyle\* OH\_Drawing\_CreateTextStyle(void) | Creates an **OH\_Drawing\_TextStyle** object. |
| void OH\_Drawing\_SetTextStyleFontSize(OH\_Drawing\_TextStyle\* style, double fontSize) | Sets the font size for a text style. |
| void OH\_Drawing\_SetTextStyleFontWeight(OH\_Drawing\_TextStyle\* style, int fontWeight) | Sets the font weight for a text style. Currently, only the default system font supports font weight adjustment. For other fonts, if the weight is less than semi-bold, there is no variation in stroke thickness. If the weight is greater than or equal to semi-bold, it might result in a fake bold effect. |

#### How to Develop

1.  Create a canvas object. For details about how to create a canvas object, see [Obtaining a Canvas and Displaying Drawing Results (C/C++)](../../../graphics-drawing-and-display/canvas-acquisition-and-display-of-drawing-results/obtaining-a-canvas-and-displaying-drawing-results-c-c/document.md).
    
2.  Initialize the paragraph style and set the text alignment to center alignment.
    
    // Create a TypographyStyle object, which is required for creating Typography.
    OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
    // Set the text alignment mode to center.
    OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);
    
3.  Initialize the text style. Here, the font color is set to pure black, the font size to **60**, and the font weight to **400**.
    
    // Set the text color, size, and weight. If TextStyle is not set, the default TextStyle in TypographyStyle is used.
    OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
    OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
    OH\_Drawing\_SetTextStyleFontSize(txtStyle, 60);
    OH\_Drawing\_SetTextStyleFontWeight(txtStyle, FONT\_WEIGHT\_400);
    
4.  Initialize the paragraph object and add text.
    
    // Create a FontCollection object to manage the font matching logic.
    OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateFontCollection();
    // Use the FontCollection object and the created TypographyStyle object to create a TypographyCreate object, which is used to create a Typography object.
    OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
    
    // Add the created TextStyle object to handler.
    OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
    // Add text to handler.
    const char \*text = "Hello World Drawing\\n";
    OH\_Drawing\_TypographyHandlerAddText(handler, text);
    
    OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
    
5.  Layout the paragraph and draw the text.
    
    // Set the maximum width.
    double maxWidth = width\_;
    OH\_Drawing\_TypographyLayout(typography, maxWidth);
    // Draw the text on the canvas.
    OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, 100);
    
6.  Release the memory.
    
    // Release the memory.
    OH\_Drawing\_DestroyTypographyStyle(typoStyle);
    OH\_Drawing\_DestroyTextStyle(txtStyle);
    OH\_Drawing\_DestroyFontCollection(fc);
    OH\_Drawing\_DestroyTypographyHandler(handler);
    OH\_Drawing\_DestroyTypography(typography);
    

#### Effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/vvTeOKaJQeCnOv2BRqDu4Q/en-us_image_0000002568764981.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6092FE0DA05456C6C3CDC73BE06F7188B2958CA80D51DB240524D73408E26236)
