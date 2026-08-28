# Drawing and Displaying Complex Text (C/C++)

When drawing text, simple text can be drawn and displayed by selecting appropriate fonts, sizes, and colors. Additionally, complex text drawing is supported by setting other styles, languages, paragraphs, etc.

Complex text drawing involves the following scenarios:

-   Multi-language text drawing and display
    
-   Multi-line text drawing and display
    
-   Multi-style text drawing and display
    
-   Style copying, drawing, and display
    

#### Multi-language Text Drawing and Display

Multi-language support is the foundation of globalized applications. Multi-language text drawing needs to support the character sets of different languages and their unique display requirements, such as right-to-left languages (such as Arabic) or vertical text (such as Chinese). You need to understand the rendering features of different languages to ensure correct text display.

When multi-language text is used, you can specify the **locale** field in **TextStyle** to match the corresponding font, skipping the process of traversing the font list to save time and memory.

## Available APIs

| API Definition | Description |
| :-- | :-- |
| void OH\_Drawing\_SetTypographyTextLocale(OH\_Drawing\_TypographyStyle\* style, const char\* locale) | Sets the locale for a typography style. |

## How to Develop

For details about the **Canvas** object, see [Obtaining a Canvas and Displaying Drawing Results](../../../graphics-drawing-and-display/canvas-acquisition-and-display-of-drawing-results/obtaining-a-canvas-and-displaying-drawing-results-c-c/document.md).

// Create a TypographyStyle object, which is required for creating TypographyCreate.
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// Set the text alignment mode to center.
OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);
// Set the locale to Chinese.
OH\_Drawing\_SetTypographyTextLocale(typoStyle, "zh-Hans");

// Set the text color, size, and weight. If TextStyle is not set, the default TextStyle in TypographyStyle is used.
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyle, FONT\_WEIGHT\_400);

// Create a FontCollection object to manage the font matching logic.
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
// Use the FontCollection object and the created TypographyStyle object to create a TypographyCreate object, which is used to create a Typography object.
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);

// Add the created TextStyle object to handler.
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
// Add the text to handler.
const char \*text = "你好，中文\\n";
OH\_Drawing\_TypographyHandlerAddText(handler, text);

// Create a Typography object based on handler.
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// Set the maximum width.
double maxWidth = width\_;
OH\_Drawing\_TypographyLayout(typography, maxWidth);
// Draw the text on the canvas.
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// Release the memory.
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

## Effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/CeDfQypPQ9CCpR26IMv3mg/en-us_image_0000002537765256.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=776522CE1FFE795D19847FF18DA2ABD393801E401E2936E60C95DA5E09127A58)

#### Multi-line Text Drawing and Display

Multi-line text is more complex than single-line text. Generally, text typography, word break, text alignment, line limit, etc., are required for multi-line text, mainly achieved by setting paragraph styles.

## Available APIs

| API Definition | Description |
| :-- | :-- |
| void OH\_Drawing\_SetTypographyTextAlign(OH\_Drawing\_TypographyStyle\* style, int align) | Sets the text alignment mode. |
| void OH\_Drawing\_SetTypographyTextWordBreakType(OH\_Drawing\_TypographyStyle\* style, int wordBreakType) | Sets the word break type. |
| void OH\_Drawing\_SetTypographyTextMaxLines(OH\_Drawing\_TypographyStyle\* style, int lineNumber) | Sets the maximum number of lines in the text. |

## How to Develop

The following uses the **BREAK\_ALL** word break policy as an example. The same method applies to other word break policies.

// Create a FontCollection object to manage the font matching logic.
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();

// Set the text color, size, and weight. If TextStyle is not set, the default TextStyle in TypographyStyle is used.
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TWENTY(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyle, FONT\_WEIGHT\_400);

// Add text.
const char \*text =
    "Nunc quis augue viverra, venenatis arcu eu, gravida odio. Integer posuere nisi quis ex pretium, a dapibus "
    "nisl gravida. Mauris lacinia accumsan enim, non tempus ligula. Mauris iaculis dui eu nisi tristique, in porta "
    "urna varius. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Mauris "
    "congue nibh mi, vel ultrices ex volutpat et. Aliquam consectetur odio in libero tristique, a mattis ex "
    "mollis. Praesent et nisl iaculis, facilisis metus nec, faucibus lacus. Duis nec dolor at nibh eleifend "
    "tempus. Nunc et enim interdum, commodo eros ac, pretium sapien. Pellentesque laoreet orci a nunc pharetra "
    "pharetra.";

// Create a TypographyStyle object with the word break policy set to BREAK\_ALL.
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// Set the text alignment mode to center.
OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);
// Set the word break policy to WORD\_BREAK\_TYPE\_BREAK\_ALL.
OH\_Drawing\_SetTypographyTextWordBreakType(typoStyle, OH\_Drawing\_WordBreakType::WORD\_BREAK\_TYPE\_BREAK\_ALL);
// Set the maximum number of lines to 10. Lines beyond the maximum number are not displayed.
OH\_Drawing\_SetTypographyTextMaxLines(typoStyle, 10);

// Use the created FontCollection and TypographyStyle objects to create a TypographyCreate object, which is used to create a Typography object.
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
// Add the created TextStyle object to handler.
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
// Add the text to handler.
OH\_Drawing\_TypographyHandlerAddText(handler, text);

OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// Set the maximum width.
double maxWidth = width\_;
OH\_Drawing\_TypographyLayout(typography, maxWidth);
// Draw the text on the canvas.
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// Release the memory.
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

| BREAK\_ALL | BREAK\_WORD |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/tXyNoc6pTja3cS9qn2_d0Q/en-us_image_0000002537925196.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10888038E0010ACC19DA40C0E71DB153DBAC37D21C569EE6285B399500F28DAC) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/wOJ1A2mwRiyxNCTgFT9u6Q/en-us_image_0000002568684973.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92E5C793A754BE8C7EC7147FA0A14567F022555D42675B77AA11BF28DC49AD6D) |

| BREAK\_HYPHEN (locale: Not Set) | BREAK\_HYPHEN (locale: en-gb) | BREAK\_HYPHEN (locale: en-us) |
| :-- | :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/jizLK3IdTNm9cdbHO7EDGw/en-us_image_0000002568764983.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C281C621488005F7D794DAC9C75BA821384EF790D3F1EB4BA1E479480A28036B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/uEBlGc5kQRK1PKrZEMLVGw/en-us_image_0000002537765258.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=572951113E2CC193C9444BE181B76FB967AC60AA390AD6490CA2DC6157E3F066) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/JXQNb5TYSpuA5DT1NEz8aQ/en-us_image_0000002537925198.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9670B4069B387D19A5A7BA38B6FB38C90E11CE1FC09ABA81E5D95E6D12D5F65) |

#### Multi-style Text Drawing and Display

In addition to the basic text and typography attributes, you may need to set different drawing styles or capabilities for different text designs in applications to highlight the unique performance or style of the corresponding text. In this case, you can use multiple drawing styles to render the text.

The following lists the multi-style drawing supported by the current version and the effects of each drawing style:

-   **Decoration**: decorates the text with different line styles, which can make the text more prominent and expressive.
    
-   **Font feature**: alters the appearance of the text through font changes, including thickness, italics and other features, to enhance the readability and aesthetics of the text.
    
-   **Font variation**: flexibly adjusts the text in different display environments and devices for more refined visual effects.
    
-   **Text shadow**: adds shadow effects around the text to enhance the text's sense of depth and three-dimensionality, making the text more attractive.
    
-   **Placeholder**: maintains the stability of the text layout when the text content is uncertain, making text display smoother and more natural.
    
-   **Automatic spacing**: adds extra spacing in places where characters are mixed and switched, improving the reading experience.
    
-   **Gradient color**: provides gradient color effects for text to enhance text expressiveness.
    
-   **Vertical alignment**: adjusts the typography position of text in the vertical direction to improve typography quality.
    
-   **Superscript and subscript**: processes any character into superscript or subscript.
    
-   **High-contrast text**: turns dark text black and light text white to enhance the contrast effect of the text.
    
-   **Line height adjustment**: adjusts the line height to change the vertical spacing of text lines, making the line spacing looser or tighter, significantly addressing the problem of vertical truncation of text and improving readability.
    
-   **Line spacing adjustment**: adjusts the line spacing to change the line height, optimizing the reading experience.
    

## Decoration

Decoration is a decorative line added above, below, or in the middle of the text. Currently, the overline, underline, and strikethrough are supported.

You can add text decoration lines to enhance the visual effect and readability of the text.

To use decoration lines, you need to initialize the decoration line style object and add it to the text style so that the decoration lines take effect when the text is drawn.

| API Definition | Description |
| :-- | :-- |
| void OH\_Drawing\_SetTextStyleDecoration(OH\_Drawing\_TextStyle\* style, int decoration) | Sets the decoration for a text style. Only one decoration can be set. To add multiple decorations, use **OH\_Drawing\_AddTextStyleDecoration**. |
| void OH\_Drawing\_SetTextStyleDecorationStyle(OH\_Drawing\_TextStyle\* style, int decorationStyle) | Sets the decoration style for a text style. |
| void OH\_Drawing\_SetTextStyleDecorationColor(OH\_Drawing\_TextStyle\* style, uint32\_t color) | Sets the decoration color for a text style. |

The following is an example:

// Create a TypographyStyle object, which is required for creating Typography.
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// Set the text alignment mode to center.
OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);
// Add text.
const char \*text = "Hello World Drawing\\n";

// Set the text color, size, and weight. If TextStyle is not set, the default TextStyle in TypographyStyle is used.
OH\_Drawing\_TextStyle \*txtStyleWithDeco = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_SetTextStyleColor(txtStyleWithDeco, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyleWithDeco, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyleWithDeco, FONT\_WEIGHT\_400);
// Set the decoration to LINE\_THROUGH.
OH\_Drawing\_SetTextStyleDecoration(txtStyleWithDeco, TEXT\_DECORATION\_LINE\_THROUGH);
// Set the decoration style to WAVY.
OH\_Drawing\_SetTextStyleDecorationStyle(txtStyleWithDeco, TEXT\_DECORATION\_STYLE\_WAVY);
// Set the decoration color.
OH\_Drawing\_SetTextStyleDecorationColor(txtStyleWithDeco, OH\_Drawing\_ColorSetArgb(0xFF, 0x6F, 0xFF, 0xFF));

// Create a TextStyle object without any decoration for comparison.
OH\_Drawing\_TextStyle \*txtStyleNoDeco = OH\_Drawing\_CreateTextStyle();
// Set the text color, size, and weight. If TextStyle is not set, the default TextStyle in TypographyStyle is used.
OH\_Drawing\_SetTextStyleColor(txtStyleNoDeco, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyleNoDeco, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyleNoDeco, FONT\_WEIGHT\_400);

// Create a FontCollection object to manage the font matching logic.
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
// Use the FontCollection object and the created TypographyStyle object to create a TypographyCreate object, which is used to create a Typography object.
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);

// Add a text style with decoration.
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyleWithDeco);
// Add the text to handler.
OH\_Drawing\_TypographyHandlerAddText(handler, text);

// Add a text style without decoration.
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyleNoDeco);
// Add the text to handler.
OH\_Drawing\_TypographyHandlerAddText(handler, text);

OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// Set the maximum width.
double maxWidth = width\_;
OH\_Drawing\_TypographyLayout(typography, maxWidth);
// Draw the text on the canvas.
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// Release the memory.
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTextStyle(txtStyleWithDeco);
OH\_Drawing\_DestroyTextStyle(txtStyleNoDeco);
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/5qITjx_VRSiQgp5r4RwePQ/en-us_image_0000002568684975.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6CA705FE9E87DE48B0D6FE6EB00D6890DE6C9EE7880F7B34FC321B5366B4B775)

## Font Feature

**FontFeature** focus on processing font features (such as bold, italic, and font variants) during text rendering. It allows fonts to display different effects in different typesetting scenarios, enhancing the expressiveness of text to better meet design and reading requirements.

Common **FontFeature** includes liga, frac, and case, which can be enabled only when the corresponding TTF file is supported.

| API Definition | Description |
| :-- | :-- |
| void OH\_Drawing\_TextStyleAddFontFeature(OH\_Drawing\_TextStyle\* style, const char\* tag, int value) | Adds a font feature for a text style. |

The following is an example:

// Create a TypographyStyle object, which is required for creating TypographyCreate.
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// Set the text alignment mode to center.
OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);
// Add text.
const char \*text = "1/2 1/3 1/4\\n";

// Set the text color, size, and weight. If TextStyle is not set, the text cannot be drawn.
OH\_Drawing\_TextStyle \*txtStyleWithFeature = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_SetTextStyleColor(txtStyleWithFeature, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyleWithFeature, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyleWithFeature, FONT\_WEIGHT\_900);
// Enable the frac font feature. This feature replaces numbers separated by slashes with common (diagonal) fractions.
OH\_Drawing\_TextStyleAddFontFeature(txtStyleWithFeature, "frac", 1);

// Create a TextStyle object without any font feature for comparison.
OH\_Drawing\_TextStyle \*txtStyleNoFeature = OH\_Drawing\_CreateTextStyle();
// Set the text color, size, and weight. If TextStyle is not set, the text cannot be drawn.
OH\_Drawing\_SetTextStyleColor(txtStyleNoFeature, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyleNoFeature, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyleNoFeature, FONT\_WEIGHT\_900);

// Create a FontCollection object to manage the font matching logic.
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
// Use the FontCollection object and the created TypographyStyle object to create a TypographyCreate object, which is used to create a Typography object.
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);

// Add a text style with font features.
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyleWithFeature);
// Add the text to handler.
OH\_Drawing\_TypographyHandlerAddText(handler, text);
// Destroy the created TextStyle object.
OH\_Drawing\_TypographyHandlerPopTextStyle(handler);

// Add a text style without font features.
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyleNoFeature);
// Add the text to handler.
OH\_Drawing\_TypographyHandlerAddText(handler, text);
// Destroy the created TextStyle object.
OH\_Drawing\_TypographyHandlerPopTextStyle(handler);

OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// Set the maximum width.
double maxWidth = width\_;
OH\_Drawing\_TypographyLayout(typography, maxWidth);
// Draw the text on the canvas.
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// Release the memory.
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTextStyle(txtStyleWithFeature);
OH\_Drawing\_DestroyTextStyle(txtStyleNoFeature);
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/GV7W60-sR6y-QmrHzmseuw/en-us_image_0000002568764985.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DE2D0FE6B5CE7E737F66F0E1009DDD2F305B1166C3B04F753DA4D24BF860CAD)

## Font Variation

Font variation is a font format that contains multiple glyph variants in a single font file. It allows you to flexibly adjust various font attributes (such as font weight, font width, and italic) in a single font file.

Unlike regular font files (each variant requires an independent file), font variation contain multiple variant axes in a single font file to implement smooth transition during text rendering and drawing.

| API Definition | Description |
| :-- | :-- |
| void OH\_Drawing\_TextStyleAddFontVariation(OH\_Drawing\_TextStyle\* style, const char\* axis, const float value) | Adds a font variation. This function takes effect only when the corresponding font file (.ttf file) supports variable adjustment. Otherwise, calling this function does not take effect. |

The following is an example:

// Create a TypographyStyle object, which is required for creating Typography.
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// Set the text alignment mode to center.
OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);
// Set the text content.
const char \*text = "Hello World Drawing\\n";

OH\_Drawing\_TextStyle \*txtStyleWithVar = OH\_Drawing\_CreateTextStyle();
// Set the font weight to 800. You can also set slnt and wdth if supported by the font file.
OH\_Drawing\_TextStyleAddFontVariation(txtStyleWithVar, "wght", 800);
// Set the text color, size, and weight. If TextStyle is not set, the default TextStyle in TypographyStyle is used.
OH\_Drawing\_SetTextStyleColor(txtStyleWithVar, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyleWithVar, DIV\_TEN(width\_));
// The font weight setting does not take effect and will be overwritten by the font weight of the font variation.
OH\_Drawing\_SetTextStyleFontWeight(txtStyleWithVar, FONT\_WEIGHT\_400);

// Create a TextStyle without font variation for comparison.
OH\_Drawing\_TextStyle \*txtStyleNoVar = OH\_Drawing\_CreateTextStyle();
// Set the text color, size, and weight. If TextStyle is not set, the default TextStyle in TypographyStyle is used.
OH\_Drawing\_SetTextStyleColor(txtStyleNoVar, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyleNoVar, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyleNoVar, FONT\_WEIGHT\_400);

// Create a FontCollection object to manage the font matching logic.
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
// Use the FontCollection object and the created TypographyStyle object to create a TypographyCreate object, which is used to create a Typography object.
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);

// Add a text style with font variation.
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyleWithVar);
// Add the text to handler.
OH\_Drawing\_TypographyHandlerAddText(handler, text);
// Display the created TextStyle object.
OH\_Drawing\_TypographyHandlerPopTextStyle(handler);

// Add a text style without font variation.
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyleNoVar);
// Add the text to handler.
OH\_Drawing\_TypographyHandlerAddText(handler, text);
// Display the created TextStyle object.
OH\_Drawing\_TypographyHandlerPopTextStyle(handler);

OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// Set the maximum width.
double maxWidth = width\_;
OH\_Drawing\_TypographyLayout(typography, maxWidth);
// Draw the text on the canvas.
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// Release the memory.
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTextStyle(txtStyleWithVar);
OH\_Drawing\_DestroyTextStyle(txtStyleNoVar);
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/OUATRr3RS3as_tCtcoftJg/en-us_image_0000002537765260.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A3BD5CDDB12FAD5EC3E7E0D7740E87817EEB59EA96E4BEE2A34D9E91D211FAE)

## Text Shadow

Text shadow creates a 3D effect for text by adding depth against the background. It is usually used to improve the visual appeal or readability of text, especially in scenarios with low color contrast.

**TextShadow** has three attributes: **color** (shadow color), **point** (shadow offset from the text), and **blurRadius** (shadow radius).

To use the shadow effect, you need to set the shadow effect array in the text style so that the shadow effect takes effect when the text is drawn.

| API Definition | Description |
| :-- | :-- |
| OH\_Drawing\_Point\* OH\_Drawing\_PointCreate(float x, float y) | Creates an **OH\_Drawing\_Point** object. |
| OH\_Drawing\_TextShadow\* OH\_Drawing\_CreateTextShadow(void) | Creates an **OH\_Drawing\_TextShadow** object. |
| void OH\_Drawing\_SetTextShadow(OH\_Drawing\_TextShadow\* shadow, uint32\_t color, OH\_Drawing\_Point\* offset, double blurRadius) | Sets a text shadow. |
| void OH\_Drawing\_TextStyleAddShadow(OH\_Drawing\_TextStyle\* style, const OH\_Drawing\_TextShadow\* shadow) | Adds a shadow to a text shadow container. |
| void OH\_Drawing\_DestroyTextShadow(OH\_Drawing\_TextShadow\* shadow) | Destroys an **OH\_Drawing\_TextShadow** object and reclaims the memory occupied by the object. |

The following is an example:

// Create a TypographyStyle object, which is required for creating Typography.
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// Set the text alignment mode to center.
OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);
// Add text.
const char \*text = "Hello World Drawing\\n";

// Set the text color, size, and weight. If TextStyle is not set, the default TextStyle in TypographyStyle is used.
OH\_Drawing\_TextStyle \*txtStyleWithShadow = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_SetTextStyleColor(txtStyleWithShadow, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyleWithShadow, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyleWithShadow, FONT\_WEIGHT\_400);
// Set the shadow offset.
OH\_Drawing\_Point \*offset = OH\_Drawing\_PointCreate(1, 1);
OH\_Drawing\_TextShadow \*shadow = OH\_Drawing\_CreateTextShadow();
double radius = 10.0;
// Set the style for TextShadow.
OH\_Drawing\_SetTextShadow(shadow, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00), offset, radius);
// Add TextShadow to TextStyle.
OH\_Drawing\_TextStyleAddShadow(txtStyleWithShadow, shadow);

// Create a TextStyle object without any shadow for comparison.
OH\_Drawing\_TextStyle \*txtStyleNoShadow = OH\_Drawing\_CreateTextStyle();
// Set the text color, size, and weight. If TextStyle is not set, the default TextStyle in TypographyStyle is used.
OH\_Drawing\_SetTextStyleColor(txtStyleNoShadow, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyleNoShadow, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyleNoShadow, FONT\_WEIGHT\_400);

// Create a FontCollection object to manage the font matching logic.
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
// Use the FontCollection object and the created TypographyStyle object to create a TypographyCreate object, which is used to create a Typography object.
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);

// Add a text style with a shadow.
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyleWithShadow);
// Add the text to handler.
OH\_Drawing\_TypographyHandlerAddText(handler, text);

// Add a text style without a shadow.
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyleNoShadow);
// Add the text to handler.
OH\_Drawing\_TypographyHandlerAddText(handler, text);

OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// Set the maximum width.
double maxWidth = width\_;
OH\_Drawing\_TypographyLayout(typography, maxWidth);
// Draw the text on the canvas.
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// Release the memory.
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTextStyle(txtStyleWithShadow);
OH\_Drawing\_PointDestroy(offset);
OH\_Drawing\_DestroyTextShadow(shadow);
OH\_Drawing\_DestroyTextStyle(txtStyleNoShadow);
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/XX0bh4hTSL-dq0u_w8blZQ/en-us_image_0000002537925200.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F071ABC30DB3DE6204EC04B8106912E8962D01CC1ABF04190AB7E87802497291)

## Placeholder

Placeholder drawing is used to render placeholder symbols in the text.

Placeholder drawing is also used to implement image and text layout. It is a visual element used to provide or replace a position before the actual image or content is registered.

| API Definition | Description |
| :-- | :-- |
| void OH\_Drawing\_TypographyHandlerAddPlaceholder(OH\_Drawing\_TypographyCreate\* handler, OH\_Drawing\_PlaceholderSpan\* span) | Adds a placeholder. |

The following is an example:

// Set the maximum width.
double maxWidth = width\_;
// Create a FontCollection object to manage the font matching logic.
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();

// Set the text color, size, and weight. If TextStyle is not set, the default TextStyle in TypographyStyle is used.
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TEN(width\_));
OH\_Drawing\_SetTextStyleFontWeight(txtStyle, FONT\_WEIGHT\_400);

// Add text.
const char \*text = "Hello World Drawing\\n";

// Create a TypographyStyle object, which is required for creating Typography.
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// Set the text alignment mode to center.
OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);

// Use the FontCollection object and the created TypographyStyle object to create a TypographyCreate object, which is used to create a Typography object.
OH\_Drawing\_TypographyCreate \*handlerWithPlaceholder = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
// Create a placeholder and initialize its member variables.
OH\_Drawing\_PlaceholderSpan placeholder;
placeholder.width = DIV\_TEN(width\_);
placeholder.height = DIV\_FIVE(width\_);
placeholder.alignment = ALIGNMENT\_ABOVE\_BASELINE; // Baseline alignment.
placeholder.baseline = TEXT\_BASELINE\_ALPHABETIC; // Text baseline type.
placeholder.baselineOffset = 0.0; // Offset relative to the baseline. This parameter is valid only when the alignment policy is OFFSET\_AT\_BASELINE.

// Place the placeholder at the beginning.
OH\_Drawing\_TypographyHandlerAddPlaceholder(handlerWithPlaceholder, &placeholder);

// Add the created TextStyle object to handler.
OH\_Drawing\_TypographyHandlerPushTextStyle(handlerWithPlaceholder, txtStyle);
// Add the text to handler.
OH\_Drawing\_TypographyHandlerAddText(handlerWithPlaceholder, text);

OH\_Drawing\_Typography \*typographyWithPlaceholder = OH\_Drawing\_CreateTypography(handlerWithPlaceholder);
OH\_Drawing\_TypographyLayout(typographyWithPlaceholder, maxWidth);
// Draw the text on the canvas.
OH\_Drawing\_TypographyPaint(typographyWithPlaceholder, cCanvas\_, 0, DIV\_TEN(width\_));

// Create OH\_Drawing\_TypographyCreate.
OH\_Drawing\_TypographyCreate \*handlerNoPlaceholder = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
// Add the created TextStyle object to handler.
OH\_Drawing\_TypographyHandlerPushTextStyle(handlerNoPlaceholder, txtStyle);
// Add the text to handler.
OH\_Drawing\_TypographyHandlerAddText(handlerNoPlaceholder, text);

OH\_Drawing\_Typography \*typographyNoPlaceholder = OH\_Drawing\_CreateTypography(handlerNoPlaceholder);

OH\_Drawing\_TypographyLayout(typographyNoPlaceholder, maxWidth);
// Draw the text on the canvas.
OH\_Drawing\_TypographyPaint(typographyNoPlaceholder, cCanvas\_, 0, DIV\_TWO(width\_));

// Release the memory.
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTypographyHandler(handlerWithPlaceholder);
OH\_Drawing\_DestroyTypographyHandler(handlerNoPlaceholder);
OH\_Drawing\_DestroyTypography(typographyWithPlaceholder);
OH\_Drawing\_DestroyTypography(typographyNoPlaceholder);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/TE_E5OEvTpC4_wBKzWiZMw/en-us_image_0000002568684977.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A7E0D18D81771C9C281D0B4CBD6393C6B389BF888546E437A20B93A967770EE9)

## Automatic Spacing

When automatic spacing is enabled, it applies between CJK (Chinese, Japanese, and Korean) and Western characters (Latin, Cyrillic, and Greek), between CJK and digits, between CJK and copyright symbols, between copyright symbols and digits, and between copyright symbols and Western characters. For example, in an English-Chinese mixed layout scenario, automatic spacing adds extra spacing in places where English and Chinese are switched, improving the reading experience.

| API Definition | Description |
| :-- | :-- |
| void OH\_Drawing\_SetTypographyTextAutoSpace(OH\_Drawing\_TypographyStyle \*style, bool enableAutoSpace) | Sets whether to enable automatic spacing during text typography. This feature is disabled by default. If enabled, automatic spacing applies between CJK (Chinese, Japanese, and Korean) and Western characters (Latin, Cyrillic, and Greek), between CJK and digits, between CJK and copyright symbols, between copyright symbols and digits, and between copyright symbols and Western characters. |

The following is an example:

// Create a TypographyStyle object, which is required for creating Typography.
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// Enable automatic spacing. The default value is false.
OH\_Drawing\_SetTypographyTextAutoSpace(typoStyle, true);
// Set the text content.
const char \*text = "test测试©test©测。";

OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
// Set the text color, size, and weight. If TextStyle is not set, the default TextStyle in TypographyStyle is used.
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TEN(width\_));

// Create a FontCollection object to manage the font matching logic.
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
// Use the FontCollection object and the created TypographyStyle object to create a TypographyCreate object, which is used to create a Typography object.
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);

// Add the text style to handler.
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
// Add the text to handler.
OH\_Drawing\_TypographyHandlerAddText(handler, text);
// Create a paragraph.
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// Set the maximum width.
double maxWidth = width\_;
// Apply the paragraph according to the typography width.
OH\_Drawing\_TypographyLayout(typography, maxWidth);
// Draw the text on the canvas.
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// Enable automatic spacing for comparison.
OH\_Drawing\_SetTypographyTextAutoSpace(typoStyle, false);

// Use the FontCollection object and the created TypographyStyle object to create a TypographyCreate object, which is used to create a Typography object.
OH\_Drawing\_TypographyCreate \*handlerWithoutAutoSpace = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);

// Add the text style to handlerWithoutAutoSpace.
OH\_Drawing\_TypographyHandlerPushTextStyle(handlerWithoutAutoSpace, txtStyle);
// Add the text to handlerWithoutAutoSpace.
OH\_Drawing\_TypographyHandlerAddText(handlerWithoutAutoSpace, text);
// Create a paragraph.
OH\_Drawing\_Typography \*typographyWithoutAutoSpace = OH\_Drawing\_CreateTypography(handlerWithoutAutoSpace);
// Apply the paragraph according to the typography width.
OH\_Drawing\_TypographyLayout(typographyWithoutAutoSpace, maxWidth);
// Draw the text on the canvas.
OH\_Drawing\_TypographyPaint(typographyWithoutAutoSpace, cCanvas\_, 0, DIV\_FOUR(width\_));

// Release the memory.
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypographyHandler(handlerWithoutAutoSpace);
OH\_Drawing\_DestroyTypography(typography);
OH\_Drawing\_DestroyTypography(typographyWithoutAutoSpace);

| Paragraph Style Setting (Automatic Spacing) | Effect |
| :-- | :-- |
| Disabled | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/FrdqIOoaTFmSA0IxNIp_oA/en-us_image_0000002568764987.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C33EB96D0C45E00E20BC9E30D338ABE74190C89FC4553ABC8F6BE412C5F16B2) |
| Enabled | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/1pzyEJbbT2mSnJr3TKmSmw/en-us_image_0000002537765262.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4B8A537958890EEECCACC4188A5837B133EEB9EBB22C9786315FEAFE9BB0739) |

## Gradients

Gradient color is a visual effect widely used in text design. It creates a smooth transition from one color to another by applying different colors to different parts of the text. You can use a shader to implement the gradient effect of text. For more information about shaders, see [Shader Effect](../../../graphics-drawing-and-display/drawing-effects/complex-drawing-effects-c-c/document.md#shader-effect).

| API Definition | Description |
| :-- | :-- |
| void OH\_Drawing\_SetTextStyleForegroundBrush(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Brush\* foregroundBrush) | Adds a foreground brush. The gradient shader attribute is attached to the foreground brush. |

The following is an example:

OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
// Set the text size.
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TEN(width\_));
// Create a shader object and set the color, start point, and end point.
OH\_Drawing\_Point \*startPt = OH\_Drawing\_PointCreate(0, 0);
// The end point is (900, 900).
OH\_Drawing\_Point \*endPt = OH\_Drawing\_PointCreate(900, 900);
uint32\_t colors\[\] = {0xFFFFFF00, 0xFFFF0000, 0xFF0000FF};
float pos\[\] = {0.0f, 0.5f, 1.0f};
// The length of the pos array is 3.
OH\_Drawing\_ShaderEffect \*colorShaderEffect =
    OH\_Drawing\_ShaderEffectCreateLinearGradient(startPt, endPt, colors, pos, 3, OH\_Drawing\_TileMode::CLAMP);
// Create a brush object and add the shader to the brush.
OH\_Drawing\_Brush \*brush = OH\_Drawing\_BrushCreate();
OH\_Drawing\_BrushSetShaderEffect(brush, colorShaderEffect);
// Add the brush to the text style.
OH\_Drawing\_SetTextStyleForegroundBrush(txtStyle, brush);
// Create a typography object and draw the text.
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
const char \*text = "Hello World";
OH\_Drawing\_TypographyHandlerAddText(handler, text);
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// Set the maximum width.
double maxWidth = width\_;
// Apply the paragraph according to the typography width.
OH\_Drawing\_TypographyLayout(typography, maxWidth);
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// Release the object.
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_ShaderEffectDestroy(colorShaderEffect);
OH\_Drawing\_BrushDestroy(brush);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/DQmAxtpwTuK35XniLnBUpg/en-us_image_0000002537925202.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D8F54E103035B31DCB61EC22C6288BDADA17A6F29D3ACF1848DDB1A91A226C1)

## Vertical Alignment

Vertical alignment is used to adjust the vertical layout position of text in a line. Vertical alignment aligns the text to the top, center, bottom, or baseline (default) when line height scaling is enabled or when text in different font sizes is mixed in a line.

| API Definition | Description |
| :-- | :-- |
| void OH\_Drawing\_SetTypographyVerticalAlignment(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TextVerticalAlignment align) | Sets the vertical typography mode of text. |

The following is an example:

OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
// Set the vertical alignment mode.
OH\_Drawing\_SetTypographyVerticalAlignment(typoStyle,
                                          OH\_Drawing\_TextVerticalAlignment::TEXT\_VERTICAL\_ALIGNMENT\_CENTER);
// Set the text size.
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TEN(width\_));
// Set the text color.
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
// Create a typography object and draw the text.
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
const char \*text = "VerticalAlignment-center";
OH\_Drawing\_TypographyHandlerAddText(handler, text);
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// Set the maximum width.
double maxWidth = width\_;
// Apply the paragraph according to the typography width.
OH\_Drawing\_TypographyLayout(typography, maxWidth);
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// Release the object.
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

The following figure shows the effect (The black box only shows the text drawing area and is not drawn in practice).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/YYlLW_t5RP27sXkYxr0gyw/en-us_image_0000002568684965.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CA55469BAABE5F5A79A3916AE6AAB4AB2EFA9885514A96CAC028332E5175FE7)

## Superscript and Subscript

Superscript or subscript text can be enabled in cases such as mathematical and chemical formulas.

| API Definition | Description |
| :-- | :-- |
| void OH\_Drawing\_SetTextStyleBadgeType(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextBadgeType textBadgeType) | Enables the superscript and subscript style. |

The following is an example:

OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_TextStyle \*badgeTxtStyle = OH\_Drawing\_CreateTextStyle();
// Set the text size.
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TWENTY(width\_));
OH\_Drawing\_SetTextStyleFontSize(badgeTxtStyle, DIV\_TWENTY(width\_));
// Set the text color.
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleColor(badgeTxtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
// Enable the superscript.
OH\_Drawing\_SetTextStyleBadgeType(badgeTxtStyle, OH\_Drawing\_TextBadgeType::TEXT\_SUPERSCRIPT);
// Create a typography object and draw the text.
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
const char \*text = "Mass-energy equivalence: E=mc";
OH\_Drawing\_TypographyHandlerAddText(handler, text);
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, badgeTxtStyle);
const char \*badgeText = "2";
OH\_Drawing\_TypographyHandlerAddText(handler, badgeText);
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// Set the maximum width.
double maxWidth = width\_;
// Apply the paragraph according to the typography width.
OH\_Drawing\_TypographyLayout(typography, maxWidth);
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// Release the object.
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTextStyle(badgeTxtStyle);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/q2LFMa8MTRmZCL2pt0SWIw/en-us_image_0000002537925190.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4AB8855D2D114D24F587E0F72CF7F85A7B785B33E97B34355F559209D4451E14)

## High Contrast

High contrast can change dark text to black and light text to white. You can enable or disable high contrast text rendering in your application, or follow the system settings.

| API Definition | Description |
| :-- | :-- |
| void OH\_Drawing\_SetTextHighContrast(OH\_Drawing\_TextHighContrast action) | Sets the high contrast mode for text rendering. For details about the modes, see [OH\_Drawing\_TextHighContrast](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-text-global-h#oh_drawing_texthighcontrast). |

The following is an example:

// Enable the high contrast mode for text rendering in the application. The priority of this mode is higher than the mode following the system settings.
OH\_Drawing\_SetTextHighContrast(TEXT\_APP\_ENABLE\_HIGH\_CONTRAST);
// Create a TypographyStyle object, which is required for creating Typography.
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();

// Set the text color and size. If TextStyle is not set, the default TextStyle in TypographyStyle is used.
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x6F, 0xFF, 0xFF));
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TEN(width\_));

// Create a FontCollection object to manage the font matching logic.
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
// Use the FontCollection object and the created TypographyStyle object to create a TypographyCreate object.
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);

// Add the created TextStyle object to handler.
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
// Add the text to handler.
const char \*text = "Hello World Drawing\\n";
OH\_Drawing\_TypographyHandlerAddText(handler, text);

OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// Set the maximum width.
double maxWidth = width\_;
// Apply the paragraph according to the typography width.
OH\_Drawing\_TypographyLayout(typography, maxWidth);
// Draw the text on the canvas.
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// Release the memory.
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

| High Contrast | Effect |
| :-- | :-- |
| Disabled | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/sTT0pHi7RUOIwzTFE6VjGQ/en-us_image_0000002568684979.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E804801E39656E1E8E88415BA2F1C92A4747D7707904528393AD23F5F7BF9CAC) |
| Enabled | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/3hUGKS1PQQOtsyIcPFjsKA/en-us_image_0000002568764989.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F8B4D0698FEAFB6BF12493C539A0D40C9F0AC206E394DCF8292C1E6855B6FB9) |

## Line Height Adjustment

Adjusting the line height can change the vertical spacing of text lines, making the line spacing looser or tighter, significantly addressing the problem of vertical truncation of text and improving readability.

You can adjust the line height either by setting the maximum and minimum line heights or using a line height scaling coefficient.

**Method 1**

Starting from API version 21, you can set the maximum and minimum line heights for text lines.

| API Definition | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTextStyleAttributeDouble(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, double value)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_settextstyleattributedouble) | Sets the maximum line height. The input ID is **OH\_Drawing\_TextStyleAttributeId::TEXT\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MAXIMUM**. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTextStyleAttributeDouble(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, double value)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_settextstyleattributedouble) | Sets the minimum line height. The input ID is **OH\_Drawing\_TextStyleAttributeId::TEXT\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MINIMUM**. |

The following is an example:

OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
// Set the text size to 50.
OH\_Drawing\_SetTextStyleFontSize(txtStyle, 50);
// Set the text color.
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleAttributeDouble(txtStyle,
    OH\_Drawing\_TextStyleAttributeId::TEXT\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MAXIMUM, 65); // Set the maximum line height to 65.
OH\_Drawing\_SetTextStyleAttributeDouble(txtStyle,
    OH\_Drawing\_TextStyleAttributeId::TEXT\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MINIMUM, 65); // Set the minimum line height to 65.
// Create a typography object and draw the text.
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
const char \*text = "Hello World!";
OH\_Drawing\_TypographyHandlerAddText(handler, text);
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// Set the typography width to 1000.
OH\_Drawing\_TypographyLayout(typography, 1000);
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, 0);

// Release the object.
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

The following figures show the effect.

| Maximum Line Height | Minimum Line Height | Effect (The black box only shows the text drawing area and is not drawn in practice.) |
| :-- | :-- | :-- |
| 65 | 65 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/myGdCs7qQ460gfrDIDLjNg/en-us_image_0000002537765252.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD0399C422C4DF9E41A5569F741F6258D7C5ADFAC5A0DFDC6ED9F398C785C07C) |
| 200 | 200 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/K1HrwN3dREaFlaQ045k93A/en-us_image_0000002537925192.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04B948B6CAD5E9C61BEC90E6D7F41BA0953C845C2DE19CC346A41F2FF11EEDCF) |

**Method 2**

Set the line height scaling coefficient.

| API Definition | Description |
| :-- | :-- |
| [void OH\_Drawing\_SetTextStyleFontHeight(OH\_Drawing\_TextStyle\* style, double fontHeight)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_settextstylefontheight) | Enables line height scaling. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTextStyleAttributeInt(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_settextstyleattributeint) | Enables the line height scaling style. The input ID is **OH\_Drawing\_TextStyleAttributeId::TEXT\_STYLE\_ATTR\_I\_LINE\_HEIGHT\_STYLE**. |

The following is an example:

OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
// Set the text size to 50.
OH\_Drawing\_SetTextStyleFontSize(txtStyle, 50);
// Set the text color.
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
// Set the line height scaling coefficient to 1.5.
OH\_Drawing\_SetTextStyleFontHeight(txtStyle, 1.5);
// Set the line height scaling style. (1 indicates that the line height scaling uses the glyph height as the scaling base.)
OH\_Drawing\_SetTextStyleAttributeInt(txtStyle,
    OH\_Drawing\_TextStyleAttributeId::TEXT\_STYLE\_ATTR\_I\_LINE\_HEIGHT\_STYLE, 1);
// Create a typography object and draw the text.
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
const char \*text = "Hello World!";
OH\_Drawing\_TypographyHandlerAddText(handler, text);
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// Set the typography width to 1000.
OH\_Drawing\_TypographyLayout(typography, 1000);
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, 0);

// Release the object.
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

The following figures show the effect.

| Line Height Scaling Style | Effect (The black box only shows the text drawing area and is not drawn in practice.) |
| :-- | :-- |
| TEXT\_LINE\_HEIGHT\_BY\_FONT\_SIZE | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/rNURKNHEQkimU10Z-54Z9w/en-us_image_0000002568684969.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DF4E75E5D34E64DC69A58210DFAE0A25A46EF1A3C57F566DC5FB2DF3B074B3A) |
| TEXT\_LINE\_HEIGHT\_BY\_FONT\_HEIGHT | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/CcK_enYnT_6yoWOAOr9UAw/en-us_image_0000002568764979.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4E6CBFC14979A4F2049D340521CF2C5E9371258F666FF33CC2F1D8B494BAB15) |

## Line Spacing Adjustment

Starting from API version 21, you can adjust the line spacing to improve the reading experience.

| API Definition | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTypographyStyleAttributeDouble(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, double value)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_settypographystyleattributedouble) | Sets the line spacing. The input ID is **OH\_Drawing\_TypographyStyleAttributeId::TYPOGRAPHY\_STYLE\_ATTR\_D\_LINE\_SPACING as the input ID**. |

The following is an example:

OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
OH\_Drawing\_SetTypographyStyleAttributeDouble(typoStyle,
    OH\_Drawing\_TypographyStyleAttributeId::TYPOGRAPHY\_STYLE\_ATTR\_D\_LINE\_SPACING, 100); // Set the line spacing to 100.
OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
// Set the text size to 50.
OH\_Drawing\_SetTextStyleFontSize(txtStyle, 50);
// Set the text color.
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
// Create a typography object and draw the text.
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
const char \*text = "Hello World!";
OH\_Drawing\_TypographyHandlerAddText(handler, text);
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
// Set the width to 200.
OH\_Drawing\_TypographyLayout(typography, 200);
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, 0);

// Release the object.
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);

The following figures show the effect.

| Ascent and Descent | Effect (The black box only shows the text drawing area and is not drawn in practice.) |
| :-- | :-- |
| TEXT\_HEIGHT\_DISABLE\_ALL | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/qHWaSGd1QWmpjpztrMeDKg/en-us_image_0000002537765254.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18B5FF3BBAC9F7CD0FB1ABD8D26E63711842EDF3CA4D5025031047E04150E125) |
| TEXT\_HEIGHT\_ALL | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/SNE2aQwnRvG75Bcx1a1REQ/en-us_image_0000002537925194.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8095DFE8C86E0B3836ACA2ADD16F8D9E96757DE800F15470B97FFAD71307118) |

#### Style Copying, Drawing, and Display

You can copy text styles, paragraph styles, and shadow styles to quickly apply them to different texts.

| API Definition | Description |
| :-- | :-- |
| OH\_Drawing\_TypographyStyle\* OH\_Drawing\_CopyTypographyStyle(OH\_Drawing\_TypographyStyle\* style) | Creates a copy of an existing paragraph style object. |
| OH\_Drawing\_TextStyle\* OH\_Drawing\_CopyTextStyle(OH\_Drawing\_TextStyle\* style) | Creates a copy of an existing text style object. |
| OH\_Drawing\_TextShadow\* OH\_Drawing\_CopyTextShadow(OH\_Drawing\_TextShadow\* shadow) | Creates a copy of an existing text shadow object. |

The following is an example:

// Create a TypographyStyle object, which is required for creating Typography.
OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
// Configure the paragraph style, including enabling automatic spacing, setting the maximum number of lines, ellipsis style, ellipsis text, and alignment mode.
// Enable automatic spacing.
OH\_Drawing\_SetTypographyTextAutoSpace(typoStyle, true);
// Set the maximum number of lines in the paragraph to 3.
OH\_Drawing\_SetTypographyTextMaxLines(typoStyle, 3);
// Set the ellipsis mode to end ellipsis.
OH\_Drawing\_SetTypographyTextEllipsisModal(typoStyle, ELLIPSIS\_MODAL\_TAIL);
// Set the ellipsis text.
OH\_Drawing\_SetTypographyTextEllipsis(typoStyle, "...");
// Set the alignment mode to center.
OH\_Drawing\_SetTypographyTextAlign(typoStyle, TEXT\_ALIGN\_CENTER);

OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
// Set the text color, size, and weight. If TextStyle is not set, the default TextStyle in TypographyStyle is used.
OH\_Drawing\_SetTextStyleColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
OH\_Drawing\_SetTextStyleFontSize(txtStyle, DIV\_TEN(width\_));
// Set the text decoration.
// Add an underline.
OH\_Drawing\_SetTextStyleDecoration(txtStyle, TEXT\_DECORATION\_UNDERLINE);
// Set the text decoration to a wavy line.
OH\_Drawing\_SetTextStyleDecorationStyle(txtStyle, TEXT\_DECORATION\_STYLE\_WAVY);
// Set the underline thickness.
OH\_Drawing\_SetTextStyleDecorationThicknessScale(txtStyle, 1);
// Set the underline color to blue.
OH\_Drawing\_SetTextStyleDecorationColor(txtStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0xFF));

// Set the shadow color, offset, and blur radius.
// Create a shadow object.
OH\_Drawing\_TextShadow \*shadow = OH\_Drawing\_CreateTextShadow();
// Set the shadow offset to (5, 5).
OH\_Drawing\_Point \*offset = OH\_Drawing\_PointCreate(5, 5);
// Set the shadow blur radius to 4.
double blurRadius = 4;
OH\_Drawing\_SetTextShadow(shadow, OH\_Drawing\_ColorSetArgb(0xFF, 0xFF, 0x00, 0xFF), offset, blurRadius);

// Copy the shadow object.
OH\_Drawing\_TextShadow \*shadowCopy = OH\_Drawing\_CopyTextShadow(shadow);
// Add the copied shadow to the text style.
OH\_Drawing\_TextStyleAddShadow(txtStyle, shadowCopy);

// Create a FontCollection object to manage the font matching logic.
OH\_Drawing\_FontCollection \*fc = OH\_Drawing\_CreateSharedFontCollection();

// Use the FontCollection object and the created TypographyStyle object to create a TypographyCreate object, which is used to create a Typography object.
OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, fc);
// Add the text style of paragraph 1 to handler.
OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
// Add the text of paragraph 1 to handler.
const char \*text = "The text style, paragraph style, and text shadow of the copied text will be exactly the same "
                   "as those of the original text.";
OH\_Drawing\_TypographyHandlerAddText(handler, text);
// Create paragraph 1 and typeset it based on the typography width.
OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
double maxWidth = width\_;
OH\_Drawing\_TypographyLayout(typography, maxWidth);
OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, DIV\_TEN(width\_));

// Generate paragraph 2 whose text style and paragraph style are copied from paragraph 1.
// Copy the text style.
OH\_Drawing\_TextStyle \*textStyleCopy = OH\_Drawing\_CopyTextStyle(txtStyle);
// Copy the paragraph style.
OH\_Drawing\_TypographyStyle \*typographyStyleCopy = OH\_Drawing\_CopyTypographyStyle(typoStyle);

// Apply the copied style to paragraph 2. Verify if both paragraphs have identical visual effects.
OH\_Drawing\_TypographyCreate \*handlerCopy = OH\_Drawing\_CreateTypographyHandler(typographyStyleCopy, fc);
OH\_Drawing\_TypographyHandlerPushTextStyle(handlerCopy, textStyleCopy);
OH\_Drawing\_TypographyHandlerAddText(handlerCopy, text);
OH\_Drawing\_Typography \*typographyCopy = OH\_Drawing\_CreateTypography(handlerCopy);
OH\_Drawing\_TypographyLayout(typographyCopy, maxWidth);
OH\_Drawing\_TypographyPaint(typographyCopy, cCanvas\_, 0, DIV\_TWO(width\_));

// Release the memory.
OH\_Drawing\_DestroyFontCollection(fc);
OH\_Drawing\_DestroyTypographyStyle(typoStyle);
OH\_Drawing\_DestroyTextStyle(txtStyle);
OH\_Drawing\_DestroyTypographyHandler(handler);
OH\_Drawing\_DestroyTypography(typography);
// Release the memory of the copied paragraph style.
OH\_Drawing\_DestroyTypographyStyle(typographyStyleCopy);
// Release the memory of the copied text style.
OH\_Drawing\_DestroyTextStyle(textStyleCopy);
OH\_Drawing\_DestroyTypographyHandler(handlerCopy);
OH\_Drawing\_DestroyTypography(typographyCopy);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/yeFlzU5qSkCUgP_iMku-Wg/en-us_image_0000002537765264.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FBE476EE30AB16B7B69B87D786AA2E2AF8E724315B4A323CE97D9D1DC156614)
