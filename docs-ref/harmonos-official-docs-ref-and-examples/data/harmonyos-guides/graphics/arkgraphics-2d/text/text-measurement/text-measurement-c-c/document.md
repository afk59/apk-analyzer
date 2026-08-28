# Text Measurement (C/C++)

#### Overview

Text measurement is the process of evaluating the size and layout of text during graphics drawing, and calculating the space (such as the width, height, and other related information) occupied by the text under a given font and style. Text measurement is used in scenarios such as text typesetting, layout, rendering, and adjustment of the text display position and size, to better control and adjust the layout and presentation of the UI to meet the design expectations.

Currently, the following text measurement capabilities are supported:

-   **Text width**: measures the horizontal length of the given text in a specific font, size, and style.
    
-   **Text height**: measures the vertical height of the given text, which usually involves the ascent and descent of the font.
    
-   **Line spacing**: measures the vertical distance between multiple lines of text, which is usually related to the line spacing of the font.
    
-   **Character spacing**: measures the horizontal distance between characters, which is usually related to the glyph and font design.
    

#### Available APIs

The following table lists the APIs commonly used for text measurement. For details about the APIs, see [drawing\_text\_typography.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-text-typography-h).

| Name | Description |
| :-- | :-- |
| double OH\_Drawing\_TypographyGetLongestLine(OH\_Drawing\_Typography\*) | Obtains the width of the longest line. You are advised to round up the returned value. |
| double OH\_Drawing\_TypographyGetLongestLineWithIndent(OH\_Drawing\_Typography\*) | Obtains the width of the longest line (including the width of the current line indentation). You are advised to round up the returned value. |
| size\_t OH\_Drawing\_TypographyGetLineCount (OH\_Drawing\_Typography\* ) | Obtains the number of lines. |
| OH\_Drawing\_LineMetrics\* OH\_Drawing\_TypographyGetLineMetrics (OH\_Drawing\_Typography\* ) | Obtains the measurement information of a paragraph line, including the height, width, and start coordinates of the line. |
| double OH\_Drawing\_TextStyleGetLetterSpacing (OH\_Drawing\_TextStyle \*) | Obtains the letter spacing of a text style. |

#### How to Develop

1.  Add the following library to the src/main/cpp/CMakeLists.txt file of the project:
    
    libnative\_drawing.so
    
2.  Import the required header files.
    
    #include <native\_drawing/drawing\_font\_collection.h>
    #include <native\_drawing/drawing\_text\_declaration.h>
    #include <native\_drawing/drawing\_text\_typography.h>
    
3.  Create a paragraph generator ParagraphBuilder and set the paragraph style.
    
    // Create a paragraph style.
    OH\_Drawing\_TypographyStyle \*typoStyle = OH\_Drawing\_CreateTypographyStyle();
    // Create a paragraph generator.
    OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typoStyle, OH\_Drawing\_CreateFontCollection());
    // Create a text style and set the font size to 50.
    OH\_Drawing\_TextStyle \*txtStyle = OH\_Drawing\_CreateTextStyle();
    OH\_Drawing\_SetTextStyleFontSize(txtStyle, 50);
    OH\_Drawing\_TypographyHandlerPushTextStyle(handler, txtStyle);
    // Add text to the generator.
    const char \*text = "Text measurement information for typesetting";
    OH\_Drawing\_TypographyHandlerAddText(handler, text);
    // Construct a paragraph through the generator.
    OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
    
4.  Call the typesetting API and set the paragraph width.
    
    // Set the paragraph width to 1000.
    OH\_Drawing\_TypographyLayout(typography, 1000);
    
5.  Call the API for obtaining paragraph measurement information to obtain the specified data.
    
    // Case 1: Obtain the width of the longest line after typesetting.
    double longestLine = OH\_Drawing\_TypographyGetLongestLine(typography);
    DRAWING\_LOGI("Line %{public}d: longestLine: %{public}f", longestLine);
    
    // Case 2: Obtain the number of lines in a paragraph after typesetting.
    size\_t lineCnt = OH\_Drawing\_TypographyGetLineCount(typography);
    DRAWING\_LOGI("lineCnt: %{public}zu", lineCnt);
    
    // Case 3: Obtain the measurement information of each line in a paragraph.
    OH\_Drawing\_LineMetrics \*lineMetrics = OH\_Drawing\_TypographyGetLineMetrics(typography);
    int lineMetricsSize = OH\_Drawing\_LineMetricsGetSize(lineMetrics);
    for (int i = 0; i < lineMetricsSize; ++i) {
    // lineMetrics is the text measurement information after typesetting.
    double curLineAscender = lineMetrics\[i\].ascender;
    double curLineWidth = lineMetrics\[i\].width;
        DRAWING\_LOGI("Line %{public}d: lineMetrics ascender: %{public}f", i + 1, curLineAscender);
        DRAWING\_LOGI("Line %{public}d: lineMetrics width: %{public}f", i + 1, curLineWidth);
    }
    
    // Case 4: Obtain the maximum line width of the paragraph and the maximum line width with indentation.
    double longestLineWithIndent = OH\_Drawing\_TypographyGetLongestLineWithIndent(typography);
    DRAWING\_LOGI("longestLineWithIndent: %{public}f", longestLineWithIndent);
    
    OH\_Drawing\_Font\_Metrics fontMetrics;
    // Obtain the font metrics of a text style.
    bool result = OH\_Drawing\_TextStyleGetFontMetrics(typography, myTextStyle, &fontMetrics);
    DRAWING\_LOGI("result: %{public}zu, fontMetrics ascent: %{public}f" , result, fontMetrics.ascent);
    // Obtain the line metrics in a typography object. This function must be called after OH\_Drawing\_TypographyLayout is called.
    OH\_Drawing\_LineMetrics lineMetric;
    OH\_Drawing\_TypographyGetLineMetricsAt(typography, 0, &lineMetric);
    DRAWING\_LOGI("lineMetrics ascender: %{public}f" ,lineMetric.ascender of the first line");
