# drawing\_text\_typography.h

#### Overview

This file declares the functions related to typography in the drawing module.

**File to include**: <native\_drawing/drawing\_text\_typography.h>

**Library**: libnative\_drawing.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Related module**: [Drawing](../../modules/drawing/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_PlaceholderSpan](../../structs/oh-drawing-placeholderspan/document.md) | OH\_Drawing\_PlaceholderSpan | Describes the placeholder that acts as a span. |
| [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md) | OH\_Drawing\_FontDescriptor | Describes the detailed information about a system font. |
| [OH\_Drawing\_LineMetrics](../../structs/oh-drawing-linemetrics/document.md) | OH\_Drawing\_LineMetrics | Describes the measurement information about a line of text. |
| [OH\_Drawing\_FontFallbackInfo](../../structs/oh-drawing-fontfallbackinfo/document.md) | OH\_Drawing\_FontFallbackInfo | Describes the information about a font fallback. |
| [OH\_Drawing\_FontFallbackGroup](../../structs/oh-drawing-fontfallbackgroup/document.md) | OH\_Drawing\_FontFallbackGroup | Describes the information about a font fallback group. |
| [OH\_Drawing\_FontAdjustInfo](../../structs/oh-drawing-fontadjustinfo/document.md) | OH\_Drawing\_FontAdjustInfo | Describes the information about a font weight mapping. |
| [OH\_Drawing\_FontAliasInfo](../../structs/oh-drawing-fontaliasinfo/document.md) | OH\_Drawing\_FontAliasInfo | Describes the information about a font alias. |
| [OH\_Drawing\_FontGenericInfo](../../structs/oh-drawing-fontgenericinfo/document.md) | OH\_Drawing\_FontGenericInfo | Describes the information about generic fonts supported by the system. |
| [OH\_Drawing\_FontConfigInfo](../../structs/oh-drawing-fontconfiginfo/document.md) | OH\_Drawing\_FontConfigInfo | Describes the information about a system font configuration. |
| [OH\_Drawing\_FontStyleStruct](../../structs/oh-drawing-fontstylestruct/document.md) | OH\_Drawing\_FontStyleStruct | Describes a font style. |
| [OH\_Drawing\_FontFeature](../../structs/oh-drawing-fontfeature/document.md) | OH\_Drawing\_FontFeature | Describes a font feature. |
| [OH\_Drawing\_StrutStyle](../../structs/oh-drawing-strutstyle/document.md) | OH\_Drawing\_StrutStyle | Describes a strut style. The strut style determines the line spacing, baseline alignment mode, and other properties related to the line height when drawing texts. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Drawing\_TextDirection](#oh_drawing_textdirection) | \- | Enumerates the text directions. |
| [OH\_Drawing\_TextAlign](#oh_drawing_textalign) | \- | Enumerates the text alignment modes. |
| [OH\_Drawing\_FontWeight](#oh_drawing_fontweight) | \- | Enumerates the font weights. |
| [OH\_Drawing\_TextBaseline](#oh_drawing_textbaseline) | \- | Enumerates the text baselines. |
| [OH\_Drawing\_TextDecoration](#oh_drawing_textdecoration) | \- | Enumerates the text decorations. |
| [OH\_Drawing\_FontStyle](#oh_drawing_fontstyle) | \- | Enumerates the font styles. |
| [OH\_Drawing\_PlaceholderVerticalAlignment](#oh_drawing_placeholderverticalalignment) | OH\_Drawing\_PlaceholderVerticalAlignment | Enumerates the vertical alignment modes of placeholders. |
| [OH\_Drawing\_TextDecorationStyle](#oh_drawing_textdecorationstyle) | OH\_Drawing\_TextDecorationStyle | Enumerates the text decoration styles. |
| [OH\_Drawing\_EllipsisModal](#oh_drawing_ellipsismodal) | OH\_Drawing\_EllipsisModal | Enumerates the ellipsis styles. |
| [OH\_Drawing\_BreakStrategy](#oh_drawing_breakstrategy) | OH\_Drawing\_BreakStrategy | Enumerates the text break strategies. |
| [OH\_Drawing\_WordBreakType](#oh_drawing_wordbreaktype) | OH\_Drawing\_WordBreakType | Enumerates the word break types. |
| [OH\_Drawing\_RectHeightStyle](#oh_drawing_rectheightstyle) | OH\_Drawing\_RectHeightStyle | Enumerates the rectangle height styles. |
| [OH\_Drawing\_RectWidthStyle](#oh_drawing_rectwidthstyle) | OH\_Drawing\_RectWidthStyle | Enumerates the rectangle width styles. |
| [OH\_Drawing\_TextBadgeType](#oh_drawing_textbadgetype) | OH\_Drawing\_TextBadgeType | Enumerates the text badge styles. |
| [OH\_Drawing\_FontConfigInfoErrorCode](#oh_drawing_fontconfiginfoerrorcode) | \- | Enumerates the error codes that may be used during the obtaining of system font configurations. |
| [OH\_Drawing\_FontWidth](#oh_drawing_fontwidth) | \- | Enumerates the font widths. |
| [OH\_Drawing\_TextHeightBehavior](#oh_drawing_textheightbehavior) | \- | Enumerates the text height modifier patterns. |
| [OH\_Drawing\_TextStyleType](#oh_drawing_textstyletype) | \- | Enumerates the text style types. |
| [OH\_Drawing\_TextVerticalAlignment](#oh_drawing_textverticalalignment) | OH\_Drawing\_TextVerticalAlignment | Enumerates the vertical alignment modes. |
| [OH\_Drawing\_LineHeightStyle](#oh_drawing_lineheightstyle) | OH\_Drawing\_LineHeightStyle | Enumerates the scaling base styles of the line height. The default style is **TEXT\_LINE\_HEIGHT\_BY\_FONT\_SIZE**. |
| [OH\_Drawing\_TextStyleAttributeId](#oh_drawing_textstyleattributeid) | OH\_Drawing\_TextStyleAttributeId | Enumerates the text style attributes. |
| [OH\_Drawing\_TypographyStyleAttributeId](#oh_drawing_typographystyleattributeid) | OH\_Drawing\_TypographyStyleAttributeId | 
Enumerates the typography style attributes.

For the common attributes of the typography styles and text styles, you are advised to use the text style attributes, which can be obtained from [OH\_Drawing\_TextStyleAttributeId](#oh_drawing_textstyleattributeid).

 |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle\* OH\_Drawing\_CreateTypographyStyle(void)](#oh_drawing_createtypographystyle) | Creates an **OH\_Drawing\_TypographyStyle** object. Release this pointer by calling [OH\_Drawing\_DestroyTypographyStyle](#oh_drawing_destroytypographystyle) when this object is no longer needed. |
| [void OH\_Drawing\_DestroyTypographyStyle(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_destroytypographystyle) | Destroys an **OH\_Drawing\_TypographyStyle** object and reclaims the memory occupied by the object. |
| [void OH\_Drawing\_SetTypographyTextDirection(OH\_Drawing\_TypographyStyle\* style, int direction)](#oh_drawing_settypographytextdirection) | Sets the text direction in a typography style. |
| [void OH\_Drawing\_SetTypographyTextAlign(OH\_Drawing\_TypographyStyle\* style, int align)](#oh_drawing_settypographytextalign) | Sets the text alignment mode. |
| [int OH\_Drawing\_TypographyGetEffectiveAlignment(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographygeteffectivealignment) | Obtains the text alignment mode. |
| [void OH\_Drawing\_SetTypographyTextMaxLines(OH\_Drawing\_TypographyStyle\* style, int lineNumber)](#oh_drawing_settypographytextmaxlines) | Sets the maximum number of lines in the text. |
| [OH\_Drawing\_TextStyle\* OH\_Drawing\_CreateTextStyle(void)](#oh_drawing_createtextstyle) | Creates an **OH\_Drawing\_TextStyle** object. |
| [OH\_Drawing\_TextStyle\* OH\_Drawing\_TypographyGetTextStyle(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographygettextstyle) | Obtains the default text style of a typography style. |
| [void OH\_Drawing\_DestroyTextStyle(OH\_Drawing\_TextStyle\* style)](#oh_drawing_destroytextstyle) | Destroys an **OH\_Drawing\_TextStyle** object and reclaims the memory occupied by the object. |
| [void OH\_Drawing\_SetTextStyleColor(OH\_Drawing\_TextStyle\* style, uint32\_t color)](#oh_drawing_settextstylecolor) | Sets the color for a text style. |
| [void OH\_Drawing\_SetTextStyleFontSize(OH\_Drawing\_TextStyle\* style, double fontSize)](#oh_drawing_settextstylefontsize) | Sets the font size for a text style. |
| [void OH\_Drawing\_SetTextStyleFontWeight(OH\_Drawing\_TextStyle\* style, int fontWeight)](#oh_drawing_settextstylefontweight) | Sets the font weight for a text style. Currently, only the default system font supports font weight adjustment. For other fonts, if the weight is less than semi-bold, there is no variation in stroke thickness. If the weight is greater than or equal to semi-bold, it might result in a fake bold effect. |
| [void OH\_Drawing\_SetTextStyleBaseLine(OH\_Drawing\_TextStyle\* style, int baseline)](#oh_drawing_settextstylebaseline) | Sets the baseline for a text style. |
| [void OH\_Drawing\_SetTextStyleDecoration(OH\_Drawing\_TextStyle\* style, int decoration)](#oh_drawing_settextstyledecoration) | Sets the decoration for a text style. Only one decoration can be set. To add multiple decorations, use [OH\_Drawing\_AddTextStyleDecoration](#oh_drawing_addtextstyledecoration). |
| [void OH\_Drawing\_AddTextStyleDecoration(OH\_Drawing\_TextStyle\* style, int decoration)](#oh_drawing_addtextstyledecoration) | Adds the decoration for a text style. Multiple decoration lines can be displayed. |
| [void OH\_Drawing\_RemoveTextStyleDecoration(OH\_Drawing\_TextStyle\* style, int decoration)](#oh_drawing_removetextstyledecoration) | Removes the decoration for a text style. |
| [void OH\_Drawing\_SetTextStyleDecorationColor(OH\_Drawing\_TextStyle\* style, uint32\_t color)](#oh_drawing_settextstyledecorationcolor) | Sets the decoration color for a text style. If this API is not called or **color** is set to **0**, the decoration color follows the text color. |
| [void OH\_Drawing\_SetTextStyleFontHeight(OH\_Drawing\_TextStyle\* style, double fontHeight)](#oh_drawing_settextstylefontheight) | Sets the line height based on the multiple of the font size. |
| [void OH\_Drawing\_SetTextStyleFontFamilies(OH\_Drawing\_TextStyle\* style,int fontFamiliesNumber, const char\* fontFamilies\[\])](#oh_drawing_settextstylefontfamilies) | Sets the font families for a text style. |
| [void OH\_Drawing\_SetTextStyleFontStyle(OH\_Drawing\_TextStyle\* style, int fontStyle)](#oh_drawing_settextstylefontstyle) | Sets the font style for a text style. |
| [void OH\_Drawing\_SetTextStyleLocale(OH\_Drawing\_TextStyle\* style, const char\* locale)](#oh_drawing_settextstylelocale) | Sets the locale for a text style. |
| [void OH\_Drawing\_SetTextStyleForegroundBrush(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Brush\* foregroundBrush)](#oh_drawing_settextstyleforegroundbrush) | Sets the foreground brush for a text style. |
| [void OH\_Drawing\_TextStyleGetForegroundBrush(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Brush\* foregroundBrush)](#oh_drawing_textstylegetforegroundbrush) | Obtains the foreground brush of a text style. |
| [void OH\_Drawing\_SetTextStyleForegroundPen(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Pen\* foregroundPen)](#oh_drawing_settextstyleforegroundpen) | Sets the foreground pen for a text style. |
| [void OH\_Drawing\_TextStyleGetForegroundPen(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Pen\* foregroundPen)](#oh_drawing_textstylegetforegroundpen) | Obtains the foreground pen of a text style. |
| [void OH\_Drawing\_SetTextStyleBackgroundBrush(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Brush\* backgroundBrush)](#oh_drawing_settextstylebackgroundbrush) | Sets the background brush for a text style. |
| [void OH\_Drawing\_TextStyleGetBackgroundBrush(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Brush\* backgroundBrush)](#oh_drawing_textstylegetbackgroundbrush) | Obtains the background brush of a text style. |
| [void OH\_Drawing\_SetTextStyleBackgroundPen(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Pen\* backgroundPen)](#oh_drawing_settextstylebackgroundpen) | Sets the background pen for a text style. |
| [void OH\_Drawing\_TextStyleGetBackgroundPen(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Pen\* backgroundPen)](#oh_drawing_textstylegetbackgroundpen) | Obtains the background pen of a text style. |
| [OH\_Drawing\_TypographyCreate\* OH\_Drawing\_CreateTypographyHandler(OH\_Drawing\_TypographyStyle\* style,OH\_Drawing\_FontCollection\* fontCollection)](#oh_drawing_createtypographyhandler) | Creates an **OH\_Drawing\_TypographyCreate** object. Release this pointer by calling [OH\_Drawing\_DestroyTypographyHandler](#oh_drawing_destroytypographyhandler) when this object is no longer needed. You are advised to use the [OH\_Drawing\_CreateSharedFontCollection](../drawing-font-collection-h/document.md#oh_drawing_createsharedfontcollection) function to create an [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md) object. |
| [void OH\_Drawing\_DestroyTypographyHandler(OH\_Drawing\_TypographyCreate\* handler)](#oh_drawing_destroytypographyhandler) | Reclaims the memory occupied by an **OH\_Drawing\_TypographyCreate** object. |
| [void OH\_Drawing\_TypographyHandlerPushTextStyle(OH\_Drawing\_TypographyCreate\* handler, OH\_Drawing\_TextStyle\* style)](#oh_drawing_typographyhandlerpushtextstyle) | Pushes a text style into the text style stack. Any text added afterward will use the style currently on top of the stack. |
| [void OH\_Drawing\_TypographyHandlerAddText(OH\_Drawing\_TypographyCreate\* handler, const char\* text)](#oh_drawing_typographyhandleraddtext) | Adds text. |
| [void OH\_Drawing\_TypographyHandlerPopTextStyle(OH\_Drawing\_TypographyCreate\* handler)](#oh_drawing_typographyhandlerpoptextstyle) | Pops the top text style out of the text style stack. |
| [OH\_Drawing\_Typography\* OH\_Drawing\_CreateTypography(OH\_Drawing\_TypographyCreate\* handler)](#oh_drawing_createtypography) | Creates an **OH\_Drawing\_Typography** object. Release this pointer by calling [OH\_Drawing\_DestroyTypography](#oh_drawing_destroytypography) when this object is no longer needed. |
| [void OH\_Drawing\_DestroyTypography(OH\_Drawing\_Typography\* typography)](#oh_drawing_destroytypography) | Destroys an **OH\_Drawing\_Typography** object and reclaims the memory occupied by the object. |
| [void OH\_Drawing\_TypographyLayout(OH\_Drawing\_Typography\* typography, double maxWidth)](#oh_drawing_typographylayout) | Lays out the typography. |
| [void OH\_Drawing\_TypographyPaint(OH\_Drawing\_Typography\* typography, OH\_Drawing\_Canvas\* canvas,double positionX, double positionY)](#oh_drawing_typographypaint) | Draws text from the upper left corner at a specified position. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called and applied. |
| [void OH\_Drawing\_TypographyPaintOnPath(OH\_Drawing\_Typography\* typography, OH\_Drawing\_Canvas\* canvas,OH\_Drawing\_Path\* path, double hOffset, double vOffset)](#oh_drawing_typographypaintonpath) | Draws text along a path. To prevent text overlap caused by the text width exceeding the layout width, you are advised to use [OH\_Drawing\_SetTypographyTextMaxLines](#oh_drawing_settypographytextmaxlines) to limit the text to a single line. |
| [double OH\_Drawing\_TypographyGetMaxWidth(OH\_Drawing\_Typography\* typography)](#oh_drawing_typographygetmaxwidth) | Obtains the typography width set by the user. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. |
| [double OH\_Drawing\_TypographyGetHeight(OH\_Drawing\_Typography\* typography)](#oh_drawing_typographygetheight) | Obtains the overall height of a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. |
| [double OH\_Drawing\_TypographyGetLongestLine(OH\_Drawing\_Typography\* typography)](#oh_drawing_typographygetlongestline) | Obtains the width of the longest line in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. You are advised to round up the return value. If the text content is empty, **0.0** is returned. |
| [double OH\_Drawing\_TypographyGetLongestLineWithIndent(OH\_Drawing\_Typography\* typography)](#oh_drawing_typographygetlongestlinewithindent) | Obtains the width of the longest line of a typography object, including its indentation. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. You are advised to round up the return value. If the text content is empty, **0.0** is returned. |
| [double OH\_Drawing\_TypographyGetMinIntrinsicWidth(OH\_Drawing\_Typography\* typography)](#oh_drawing_typographygetminintrinsicwidth) | Obtains the minimum intrinsic width in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. |
| [double OH\_Drawing\_TypographyGetMaxIntrinsicWidth(OH\_Drawing\_Typography\* typography)](#oh_drawing_typographygetmaxintrinsicwidth) | Obtains the maximum intrinsic width in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. |
| [double OH\_Drawing\_TypographyGetAlphabeticBaseline(OH\_Drawing\_Typography\* typography)](#oh_drawing_typographygetalphabeticbaseline) | Obtains the alphabetic baseline in a typography object. |
| [double OH\_Drawing\_TypographyGetIdeographicBaseline(OH\_Drawing\_Typography\* typography)](#oh_drawing_typographygetideographicbaseline) | Obtains the ideographic baseline in a typography object. |
| [void OH\_Drawing\_TypographyHandlerAddPlaceholder(OH\_Drawing\_TypographyCreate\* handler,OH\_Drawing\_PlaceholderSpan\* span)](#oh_drawing_typographyhandleraddplaceholder) | Adds a placeholder. |
| [bool OH\_Drawing\_TypographyDidExceedMaxLines(OH\_Drawing\_Typography\* typography)](#oh_drawing_typographydidexceedmaxlines) | Checks whether the text in the typography object exceeds the line limit. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. It returns **false** if the line limit is not set using [OH\_Drawing\_SetTypographyTextMaxLines](#oh_drawing_settypographytextmaxlines). |
| [OH\_Drawing\_TextBox\* OH\_Drawing\_TypographyGetRectsForRange(OH\_Drawing\_Typography\* typography,size\_t start, size\_t end, OH\_Drawing\_RectHeightStyle heightStyle, OH\_Drawing\_RectWidthStyle widthStyle)](#oh_drawing_typographygetrectsforrange) | Obtains text boxes in a given range of a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. Release this pointer by calling [OH\_Drawing\_TypographyDestroyTextBox](#oh_drawing_typographydestroytextbox) when this object is no longer needed. |
| [OH\_Drawing\_TextBox\* OH\_Drawing\_TypographyGetRectsForPlaceholders(OH\_Drawing\_Typography\* typography)](#oh_drawing_typographygetrectsforplaceholders) | Obtains text boxes for placeholders in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. Release this pointer by calling [OH\_Drawing\_TypographyDestroyTextBox](#oh_drawing_typographydestroytextbox) when this object is no longer needed. |
| [float OH\_Drawing\_GetLeftFromTextBox(OH\_Drawing\_TextBox\* textbox, int index)](#oh_drawing_getleftfromtextbox) | Obtains the left position of a text box. |
| [float OH\_Drawing\_GetRightFromTextBox(OH\_Drawing\_TextBox\* textbox, int index)](#oh_drawing_getrightfromtextbox) | Obtains the right position of a text box. |
| [float OH\_Drawing\_GetTopFromTextBox(OH\_Drawing\_TextBox\* textbox, int index)](#oh_drawing_gettopfromtextbox) | Obtains the top position of a text box. |
| [float OH\_Drawing\_GetBottomFromTextBox(OH\_Drawing\_TextBox\* textbox, int index)](#oh_drawing_getbottomfromtextbox) | Obtains the bottom position of a text box. |
| [int OH\_Drawing\_GetTextDirectionFromTextBox(OH\_Drawing\_TextBox\* textbox, int index)](#oh_drawing_gettextdirectionfromtextbox) | Obtains the text direction of a text box. |
| [size\_t OH\_Drawing\_GetSizeOfTextBox(OH\_Drawing\_TextBox\* textBox)](#oh_drawing_getsizeoftextbox) | Obtains the number of text boxes. |
| [OH\_Drawing\_PositionAndAffinity\* OH\_Drawing\_TypographyGetGlyphPositionAtCoordinate(OH\_Drawing\_Typography\* typography,double dx, double dy)](#oh_drawing_typographygetglyphpositionatcoordinate) | Obtains the position and affinity of the glyph at the given coordinates. |
| [OH\_Drawing\_PositionAndAffinity\* OH\_Drawing\_TypographyGetGlyphPositionAtCoordinateWithCluster(OH\_Drawing\_Typography\* typography, double dx, double dy)](#oh_drawing_typographygetglyphpositionatcoordinatewithcluster) | Obtains the position and affinity of the glyph cluster to which the glyph at the given coordinates belongs. The glyph cluster is a container that holds one or more glyphs. |
| [size\_t OH\_Drawing\_GetPositionFromPositionAndAffinity(OH\_Drawing\_PositionAndAffinity\* positionAndAffinity)](#oh_drawing_getpositionfrompositionandaffinity) | Obtains the position attribute of an **OH\_Drawing\_PositionAndAffinity** object. |
| [int OH\_Drawing\_GetAffinityFromPositionAndAffinity(OH\_Drawing\_PositionAndAffinity\* positionAndAffinity)](#oh_drawing_getaffinityfrompositionandaffinity) | Obtains the affinity attribute of an **OH\_Drawing\_PositionAndAffinity** object. The affinity determines whether the font is close to the front text or rear text. |
| [OH\_Drawing\_Range\* OH\_Drawing\_TypographyGetWordBoundary(OH\_Drawing\_Typography\* typography, size\_t offset)](#oh_drawing_typographygetwordboundary) | Obtains the word boundary in a typography object. |
| [size\_t OH\_Drawing\_GetStartFromRange(OH\_Drawing\_Range\* range)](#oh_drawing_getstartfromrange) | Obtains the start position of an **OH\_Drawing\_Range** object. |
| [size\_t OH\_Drawing\_GetEndFromRange(OH\_Drawing\_Range\* range)](#oh_drawing_getendfromrange) | Obtains the end position of an **OH\_Drawing\_Range** object. |
| [size\_t OH\_Drawing\_TypographyGetLineCount(OH\_Drawing\_Typography\* typography)](#oh_drawing_typographygetlinecount) | Obtains the number of lines in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. |
| [void OH\_Drawing\_SetTextStyleDecorationStyle(OH\_Drawing\_TextStyle\* style, int decorationStyle)](#oh_drawing_settextstyledecorationstyle) | Sets the decoration style for a text style. |
| [void OH\_Drawing\_SetTextStyleDecorationThicknessScale(OH\_Drawing\_TextStyle\* style, double decorationThicknessScale)](#oh_drawing_settextstyledecorationthicknessscale) | Sets the thickness scale factor for the decoration style of a text style. |
| [void OH\_Drawing\_SetTextStyleLetterSpacing(OH\_Drawing\_TextStyle\* style, double letterSpacing)](#oh_drawing_settextstyleletterspacing) | Sets the letter spacing for a text style. |
| [void OH\_Drawing\_SetTextStyleWordSpacing(OH\_Drawing\_TextStyle\* style, double wordSpacing)](#oh_drawing_settextstylewordspacing) | Sets the word spacing for a text style. |
| [void OH\_Drawing\_SetTextStyleHalfLeading(OH\_Drawing\_TextStyle\* style, bool halfLeading)](#oh_drawing_settextstylehalfleading) | Sets whether to enable half leading for a text style. |
| [void OH\_Drawing\_SetTextStyleEllipsis(OH\_Drawing\_TextStyle\* style, const char\* ellipsis)](#oh_drawing_settextstyleellipsis) | Sets the ellipsis content for a text style. |
| [void OH\_Drawing\_SetTextStyleEllipsisModal(OH\_Drawing\_TextStyle\* style, int ellipsisModal)](#oh_drawing_settextstyleellipsismodal) | Sets the ellipsis style for a text style. |
| [void OH\_Drawing\_SetTypographyTextBreakStrategy(OH\_Drawing\_TypographyStyle\* style, int breakStrategy)](#oh_drawing_settypographytextbreakstrategy) | Sets the text break strategy. |
| [void OH\_Drawing\_SetTypographyTextWordBreakType(OH\_Drawing\_TypographyStyle\* style, int wordBreakType)](#oh_drawing_settypographytextwordbreaktype) | Sets the word break type. |
| [void OH\_Drawing\_SetTypographyTextEllipsisModal(OH\_Drawing\_TypographyStyle\* style, int ellipsisModal)](#oh_drawing_settypographytextellipsismodal) | Sets the ellipsis style for a text style. |
| [void OH\_Drawing\_SetTypographyTextEllipsis(OH\_Drawing\_TypographyStyle\* style, const char\* ellipsis)](#oh_drawing_settypographytextellipsis) | Sets the ellipsis text for a typography style. |
| [double OH\_Drawing\_TypographyGetLineHeight(OH\_Drawing\_Typography\* typography, int lineNumber)](#oh_drawing_typographygetlineheight) | Obtains the line height in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. |
| [double OH\_Drawing\_TypographyGetLineWidth(OH\_Drawing\_Typography\* typography, int lineNumber)](#oh_drawing_typographygetlinewidth) | Obtains the line width of a specified line. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. |
| [void OH\_Drawing\_SetTypographyTextSplitRatio(OH\_Drawing\_TypographyStyle\* style, float textSplitRatio)](#oh_drawing_settypographytextsplitratio) | Sets the text split ratio. |
| [bool OH\_Drawing\_TypographyIsLineUnlimited(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographyislineunlimited) | Checks whether the maximum number of lines is limited. |
| [bool OH\_Drawing\_TypographyIsEllipsized(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographyisellipsized) | Checks whether an ellipsis is configured for a typography style. |
| [void OH\_Drawing\_SetTypographyTextLocale(OH\_Drawing\_TypographyStyle\* style, const char\* locale)](#oh_drawing_settypographytextlocale) | Sets the locale for a typography style. |
| [bool OH\_Drawing\_TextStyleGetFontMetrics(OH\_Drawing\_Typography\* typography,OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Font\_Metrics\* fontmetrics)](#oh_drawing_textstylegetfontmetrics) | Obtains the font metrics of a text style. |
| [void OH\_Drawing\_SetTypographyTextStyle(OH\_Drawing\_TypographyStyle\* handler, OH\_Drawing\_TextStyle\* style)](#oh_drawing_settypographytextstyle) | Sets a text style. |
| [OH\_Drawing\_FontDescriptor\* OH\_Drawing\_CreateFontDescriptor(void)](#oh_drawing_createfontdescriptor) | Creates an **OH\_Drawing\_FontDescriptor** object to describe the detailed information about a system font. |
| [void OH\_Drawing\_DestroyFontDescriptor(OH\_Drawing\_FontDescriptor\* descriptor)](#oh_drawing_destroyfontdescriptor) | Destroys an **OH\_Drawing\_FontDescriptor** object and reclaims the memory occupied by the object. |
| [OH\_Drawing\_FontParser\* OH\_Drawing\_CreateFontParser(void)](#oh_drawing_createfontparser) | Creates an **OH\_Drawing\_FontParser** object to parse a system font. |
| [void OH\_Drawing\_DestroyFontParser(OH\_Drawing\_FontParser\* parser)](#oh_drawing_destroyfontparser) | Destroys an **OH\_Drawing\_FontParser** object and reclaims the memory occupied by the object. |
| [char\*\* OH\_Drawing\_FontParserGetSystemFontList(OH\_Drawing\_FontParser\* fontParser, size\_t\* num)](#oh_drawing_fontparsergetsystemfontlist) | Obtains the list of system fonts. This function can be used only on 2-in-1 devices and phones. |
| [void OH\_Drawing\_DestroySystemFontList(char\*\* fontList, size\_t num)](#oh_drawing_destroysystemfontlist) | Reclaims the memory occupied by the system font list. |
| [OH\_Drawing\_FontDescriptor\* OH\_Drawing\_FontParserGetFontByName(OH\_Drawing\_FontParser\* fontParser, const char\* name)](#oh_drawing_fontparsergetfontbyname) | Obtains the descriptor of a system font based on the font name. |
| [OH\_Drawing\_LineMetrics\* OH\_Drawing\_TypographyGetLineMetrics(OH\_Drawing\_Typography\* typography)](#oh_drawing_typographygetlinemetrics) | Obtains the line metrics in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. Release this pointer by calling [OH\_Drawing\_DestroyLineMetrics](#oh_drawing_destroylinemetrics) when this object is no longer needed. |
| [size\_t OH\_Drawing\_LineMetricsGetSize(OH\_Drawing\_LineMetrics\* lineMetrics)](#oh_drawing_linemetricsgetsize) | Obtains the number of lines. |
| [void OH\_Drawing\_DestroyLineMetrics(OH\_Drawing\_LineMetrics\* lineMetrics)](#oh_drawing_destroylinemetrics) | Destroys an **OH\_Drawing\_LineMetrics** object and reclaims the memory occupied by the object. |
| [bool OH\_Drawing\_TypographyGetLineMetricsAt(OH\_Drawing\_Typography\* typography,int lineNumber, OH\_Drawing\_LineMetrics\* lineMetric)](#oh_drawing_typographygetlinemetricsat) | Obtains the metrics of the given line in a typography object. For details, see the [OH\_Drawing\_LineMetr](../../structs/oh-drawing-linemetrics/document.md) struct. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. |
| [bool OH\_Drawing\_TypographyGetLineInfo(OH\_Drawing\_Typography\* typography, int lineNumber, bool oneLine,bool includeWhitespace, OH\_Drawing\_LineMetrics\* drawingLineMetrics)](#oh_drawing_typographygetlineinfo) | Obtains the metrics of a given line or the metrics of the first character in a given line in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. |
| [void OH\_Drawing\_SetTypographyTextFontWeight(OH\_Drawing\_TypographyStyle\* style, int weight)](#oh_drawing_settypographytextfontweight) | Sets the default font weight for a typography style. Currently, only the default system font supports font weight adjustment. For other fonts, if the weight is less than semi-bold, there is no variation in stroke thickness. If the weight is greater than or equal to semi-bold, it might result in a fake bold effect. |
| [void OH\_Drawing\_SetTypographyTextFontStyle(OH\_Drawing\_TypographyStyle\* style, int fontStyle)](#oh_drawing_settypographytextfontstyle) | Sets the default font style for a typography style. |
| [void OH\_Drawing\_SetTypographyTextFontFamily(OH\_Drawing\_TypographyStyle\* style, const char\* fontFamily)](#oh_drawing_settypographytextfontfamily) | Sets the font family name for text. |
| [void OH\_Drawing\_SetTypographyTextFontSize(OH\_Drawing\_TypographyStyle\* style, double fontSize)](#oh_drawing_settypographytextfontsize) | Sets the font size for text. |
| [void OH\_Drawing\_SetTypographyTextFontHeight(OH\_Drawing\_TypographyStyle\* style, double fontHeight)](#oh_drawing_settypographytextfontheight) | Sets the font height for text. |
| [void OH\_Drawing\_SetTypographyTextHalfLeading(OH\_Drawing\_TypographyStyle\* style, bool halfLeading)](#oh_drawing_settypographytexthalfleading) | Sets whether to enable half leading for text. |
| [void OH\_Drawing\_SetTypographyTextUseLineStyle(OH\_Drawing\_TypographyStyle\* style, bool useLineStyle)](#oh_drawing_settypographytextuselinestyle) | Sets whether to enable the text line style. |
| [void OH\_Drawing\_SetTypographyTextLineStyleFontWeight(OH\_Drawing\_TypographyStyle\* style, int weight)](#oh_drawing_settypographytextlinestylefontweight) | Sets the text font weight of the strut style in a typography style. Currently, only the default system font supports font weight adjustment. For other fonts, if the weight is less than semi-bold, there is no variation in stroke thickness. If the weight is greater than or equal to semi-bold, it might result in a fake bold effect. |
| [void OH\_Drawing\_SetTypographyTextLineStyleFontStyle(OH\_Drawing\_TypographyStyle\* style, int fontStyle)](#oh_drawing_settypographytextlinestylefontstyle) | Sets the font style of the strut style in a typography style. |
| [void OH\_Drawing\_SetTypographyTextLineStyleFontFamilies(OH\_Drawing\_TypographyStyle\* style,int fontFamiliesNumber, const char\* fontFamilies\[\])](#oh_drawing_settypographytextlinestylefontfamilies) | Sets the font families for a text line style. |
| [void OH\_Drawing\_SetTypographyTextLineStyleFontSize(OH\_Drawing\_TypographyStyle\* style, double lineStyleFontSize)](#oh_drawing_settypographytextlinestylefontsize) | Sets the font size for a text line style. |
| [void OH\_Drawing\_SetTypographyTextLineStyleFontHeight(OH\_Drawing\_TypographyStyle\* style, double lineStyleFontHeight)](#oh_drawing_settypographytextlinestylefontheight) | Sets the font height for a text line style. |
| [void OH\_Drawing\_SetTypographyTextLineStyleHalfLeading(OH\_Drawing\_TypographyStyle\* style, bool lineStyleHalfLeading)](#oh_drawing_settypographytextlinestylehalfleading) | Sets whether to enable half leading for a text line style. |
| [void OH\_Drawing\_SetTypographyTextLineStyleSpacingScale(OH\_Drawing\_TypographyStyle\* style, double spacingScale)](#oh_drawing_settypographytextlinestylespacingscale) | Sets the spacing scale factor for a text line style. |
| [void OH\_Drawing\_SetTypographyTextLineStyleOnly(OH\_Drawing\_TypographyStyle\* style, bool lineStyleOnly)](#oh_drawing_settypographytextlinestyleonly) | Sets whether to enable the text line style only. |
| [OH\_Drawing\_TextShadow\* OH\_Drawing\_CreateTextShadow(void)](#oh_drawing_createtextshadow) | Creates an **OH\_Drawing\_TextShadow** object. Release this pointer by calling [OH\_Drawing\_DestroyTextShadow](#oh_drawing_destroytextshadow) when this object is no longer needed. |
| [void OH\_Drawing\_DestroyTextShadow(OH\_Drawing\_TextShadow\* shadow)](#oh_drawing_destroytextshadow) | Destroys an **OH\_Drawing\_TextShadow** object and reclaims the memory occupied by the object. |
| [OH\_Drawing\_TextShadow\* OH\_Drawing\_TextStyleGetShadows(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstylegetshadows) | Obtains a text shadow container. Release this pointer by calling [OH\_Drawing\_DestroyTextShadows](#oh_drawing_destroytextshadows) when this object is no longer needed. |
| [int OH\_Drawing\_TextStyleGetShadowCount(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstylegetshadowcount) | Obtains the size of a text shadow container. |
| [void OH\_Drawing\_TextStyleAddShadow(OH\_Drawing\_TextStyle\* style, const OH\_Drawing\_TextShadow\* shadow)](#oh_drawing_textstyleaddshadow) | Adds a shadow to a text shadow container. |
| [void OH\_Drawing\_TextStyleClearShadows(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstyleclearshadows) | Clears all shadows in a text shadow container. |
| [OH\_Drawing\_TextShadow\* OH\_Drawing\_TextStyleGetShadowWithIndex(OH\_Drawing\_TextStyle\* style, int index)](#oh_drawing_textstylegetshadowwithindex) | Obtains a shadow with a given index in a text shadow container. |
| [void OH\_Drawing\_TypographySetIndents(OH\_Drawing\_Typography\* typography, int indentsNumber, const float indents\[\])](#oh_drawing_typographysetindents) | Sets indents for typography. If this function is not called, texts will have no indentation applied. |
| [float OH\_Drawing\_TypographyGetIndentsWithIndex(OH\_Drawing\_Typography\* typography, int index)](#oh_drawing_typographygetindentswithindex) | Obtains indents with a given index in a typography object. The line index starts from 0. |
| [OH\_Drawing\_Range\* OH\_Drawing\_TypographyGetLineTextRange(OH\_Drawing\_Typography\* typography,int lineNumber, bool includeSpaces)](#oh_drawing_typographygetlinetextrange) | Obtains the line bounds in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. This function can only be used to obtain the bounds of existing lines. That is, the line index must start from 0, and the maximum index is [OH\_Drawing\_TypographyGetLineCount](#oh_drawing_typographygetlinecount) - 1. |
| [void OH\_Drawing\_DestroyTextShadows(OH\_Drawing\_TextShadow\* shadow)](#oh_drawing_destroytextshadows) | Reclaims the memory occupied by the vector consisting of the **OH\_Drawing\_TextShadow** objects. |
| [OH\_Drawing\_FontConfigInfo\* OH\_Drawing\_GetSystemFontConfigInfo(OH\_Drawing\_FontConfigInfoErrorCode\* errorCode)](#oh_drawing_getsystemfontconfiginfo) | Obtains the system font configuration. |
| [void OH\_Drawing\_DestroySystemFontConfigInfo(OH\_Drawing\_FontConfigInfo\* drawFontCfgInfo)](#oh_drawing_destroysystemfontconfiginfo) | Reclaims the memory occupied by the system font configuration. |
| [void OH\_Drawing\_SetTextStyleFontStyleStruct(OH\_Drawing\_TextStyle\* drawingTextStyle,OH\_Drawing\_FontStyleStruct fontStyle)](#oh_drawing_settextstylefontstylestruct) | Sets the font style, including the font weight, width, and slant, for a text style. |
| [void OH\_Drawing\_SetTextStyleBadgeType(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextBadgeType textBadgeType)](#oh_drawing_settextstylebadgetype) | Sets whether to use superscript or subscript in text layout. If this API is not called, the feature is disabled by default. |
| [OH\_Drawing\_FontStyleStruct OH\_Drawing\_TextStyleGetFontStyleStruct(OH\_Drawing\_TextStyle\* drawingTextStyle)](#oh_drawing_textstylegetfontstylestruct) | Obtains the font style, including the font weight, width, and slant, of a text style. |
| [void OH\_Drawing\_SetTypographyStyleFontStyleStruct(OH\_Drawing\_TypographyStyle\* drawingStyle,OH\_Drawing\_FontStyleStruct fontStyle)](#oh_drawing_settypographystylefontstylestruct) | Sets the font style, including the font weight, width, and slant, for the default text style of a typography style. |
| [OH\_Drawing\_FontStyleStruct OH\_Drawing\_TypographyStyleGetFontStyleStruct(OH\_Drawing\_TypographyStyle\* drawingStyle)](#oh_drawing_typographystylegetfontstylestruct) | Obtains the font style, including the font weight, width, and slant, of the default text style of a typography style. |
| [void OH\_Drawing\_TextStyleSetBackgroundRect(OH\_Drawing\_TextStyle\* style,const OH\_Drawing\_RectStyle\_Info\* rectStyleInfo, int styleId)](#oh_drawing_textstylesetbackgroundrect) | Sets a background rectangle and style ID for a text style. The style ID is valid only when the background box is a rounded rectangle. |
| [void OH\_Drawing\_TypographyHandlerAddSymbol(OH\_Drawing\_TypographyCreate\* handler, uint32\_t symbol)](#oh_drawing_typographyhandleraddsymbol) | Adds the symbol to use in the typography creation process. |
| [void OH\_Drawing\_TextStyleAddFontFeature(OH\_Drawing\_TextStyle\* style, const char\* tag, int value)](#oh_drawing_textstyleaddfontfeature) | Adds a font feature for a text style. |
| [void OH\_Drawing\_TextStyleAddFontVariation(OH\_Drawing\_TextStyle\* style, const char\* axis, const float value)](#oh_drawing_textstyleaddfontvariation) | Adds a font variation. This function takes effect only when the corresponding font file (.ttf file) supports variable adjustment. Otherwise, calling this function does not take effect. |
| [OH\_Drawing\_FontFeature\* OH\_Drawing\_TextStyleGetFontFeatures(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstylegetfontfeatures) | Obtains all the contents in a font feature map container of a text style. |
| [void OH\_Drawing\_TextStyleDestroyFontFeatures(OH\_Drawing\_FontFeature\* fontFeature, size\_t fontFeatureSize)](#oh_drawing_textstyledestroyfontfeatures) | Reclaims the memory occupied by the struct array that holds all the font features. |
| [size\_t OH\_Drawing\_TextStyleGetFontFeatureSize(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstylegetfontfeaturesize) | Obtains the size of a font feature map container in a text style. |
| [void OH\_Drawing\_TextStyleClearFontFeature(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstyleclearfontfeature) | Clears all the contents in a font feature map container of a text style. |
| [double OH\_Drawing\_TextStyleGetBaselineShift(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstylegetbaselineshift) | Obtains the baseline drift of a text style. |
| [void OH\_Drawing\_TextStyleSetBaselineShift(OH\_Drawing\_TextStyle\* style, double lineShift)](#oh_drawing_textstylesetbaselineshift) | Sets a baseline drift for a text style. |
| [void OH\_Drawing\_TypographyTextSetHeightBehavior(OH\_Drawing\_TypographyStyle\* style,OH\_Drawing\_TextHeightBehavior heightMode)](#oh_drawing_typographytextsetheightbehavior) | Sets a text height modifier pattern. |
| [OH\_Drawing\_TextHeightBehavior OH\_Drawing\_TypographyTextGetHeightBehavior(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographytextgetheightbehavior) | Obtains the text height modifier pattern. |
| [OH\_Drawing\_Font\_Metrics\* OH\_Drawing\_TypographyGetLineFontMetrics(OH\_Drawing\_Typography\* typography,size\_t lineNumber, size\_t\* fontMetricsSize)](#oh_drawing_typographygetlinefontmetrics) | Obtains all font metrics from a given line in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. Otherwise, a null pointer is returned. Release this pointer by calling [OH\_Drawing\_TypographyDestroyLineFontMetrics](#oh_drawing_typographydestroylinefontmetrics) when this object is no longer needed. |
| [void OH\_Drawing\_TypographyDestroyLineFontMetrics(OH\_Drawing\_Font\_Metrics\* lineFontMetric)](#oh_drawing_typographydestroylinefontmetrics) | Reclaims the memory occupied by the struct array that holds all the font metrics of a given line. |
| [bool OH\_Drawing\_TextStyleIsEqual(const OH\_Drawing\_TextStyle\* style, const OH\_Drawing\_TextStyle\* comparedStyle)](#oh_drawing_textstyleisequal) | Checks whether two text styles are equal. The word width property is not involved in the comparison. |
| [bool OH\_Drawing\_TextStyleIsEqualByFont(const OH\_Drawing\_TextStyle\* style, const OH\_Drawing\_TextStyle\* comparedStyle)](#oh_drawing_textstyleisequalbyfont) | Checks whether the font style properties of two text styles are equal. |
| [bool OH\_Drawing\_TextStyleIsAttributeMatched(const OH\_Drawing\_TextStyle\* style,const OH\_Drawing\_TextStyle\* comparedStyle, OH\_Drawing\_TextStyleType textStyleType)](#oh_drawing_textstyleisattributematched) | Checks whether two text styles have the same font style type. |
| [void OH\_Drawing\_TextStyleSetPlaceholder(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstylesetplaceholder) | Adds a placeholder. |
| [bool OH\_Drawing\_TextStyleIsPlaceholder(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstyleisplaceholder) | Checks whether a placeholder is set for a text style. |
| [OH\_Drawing\_TextAlign OH\_Drawing\_TypographyStyleGetEffectiveAlignment(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographystylegeteffectivealignment) | Obtains the text alignment mode. |
| [bool OH\_Drawing\_TypographyStyleIsHintEnabled(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographystyleishintenabled) | Checks whether font hinting is enabled for a typography style. Font hinting is used to improve the readability and appearance of small-sized text when rendering it. |
| [void OH\_Drawing\_SetTypographyStyleTextStrutStyle(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_StrutStyle\* strutstyle)](#oh_drawing_settypographystyletextstrutstyle) | Sets the strut style for a typography style. |
| [OH\_Drawing\_StrutStyle\* OH\_Drawing\_TypographyStyleGetStrutStyle(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographystylegetstrutstyle) | Obtains the strut style of a typography style. |
| [void OH\_Drawing\_TypographyStyleDestroyStrutStyle(OH\_Drawing\_StrutStyle\* strutstyle)](#oh_drawing_typographystyledestroystrutstyle) | Reclaims the memory occupied by a strut style. |
| [bool OH\_Drawing\_TypographyStyleStrutStyleEquals(OH\_Drawing\_StrutStyle\* from, OH\_Drawing\_StrutStyle\* to)](#oh_drawing_typographystylestrutstyleequals) | Checks whether two strut styles are equal. |
| [void OH\_Drawing\_TypographyStyleSetHintsEnabled(OH\_Drawing\_TypographyStyle\* style, bool hintsEnabled)](#oh_drawing_typographystylesethintsenabled) | Sets whether to enable font hinting for a typography style. Font hinting is used to improve the readability and appearance of small-sized text when rendering it. |
| [void OH\_Drawing\_TypographyMarkDirty(OH\_Drawing\_Typography\* typography)](#oh_drawing_typographymarkdirty) | Marks a typography object as dirty data. This function is used to initialize the typography state. |
| [int32\_t OH\_Drawing\_TypographyGetUnresolvedGlyphsCount(OH\_Drawing\_Typography\* typography)](#oh_drawing_typographygetunresolvedglyphscount) | Obtains the number of unresolved glyphs in a typography object. This function can be called only after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called and applied. |
| [void OH\_Drawing\_TypographyUpdateFontSize(OH\_Drawing\_Typography\* typography, size\_t from, size\_t to, float fontSize)](#oh_drawing_typographyupdatefontsize) | Updates the font size in a typography object. |
| [void OH\_Drawing\_TypographyUpdateFontColor(OH\_Drawing\_Typography\* typography, uint32\_t color)](#oh_drawing_typographyupdatefontcolor) | Updates the font color in a typography object. This API call also updates the decoration color if it hasn't been set yet. The updated font color takes effect after you call [OH\_Drawing\_TypographyPaint](#oh_drawing_typographypaint) to draw the text. |
| [void OH\_Drawing\_TypographyUpdateDecoration(OH\_Drawing\_Typography\* typography, OH\_Drawing\_TextDecoration decoration)](#oh_drawing_typographyupdatedecoration) | Updates the decoration type of a typography object. The updated decoration type takes effect after you call [OH\_Drawing\_TypographyPaint](#oh_drawing_typographypaint) to draw the text. |
| [void OH\_Drawing\_TypographyUpdateDecorationThicknessScale(OH\_Drawing\_Typography\* typography,double decorationThicknessScale)](#oh_drawing_typographyupdatedecorationthicknessscale) | Updates the decoration thickness scale of a typography object. The updated decoration thickness scale takes effect after you call [OH\_Drawing\_TypographyPaint](#oh_drawing_typographypaint) to draw the text. |
| [void OH\_Drawing\_TypographyUpdateDecorationStyle(OH\_Drawing\_Typography\* typography,OH\_Drawing\_TextDecorationStyle decorationStyle)](#oh_drawing_typographyupdatedecorationstyle) | Updates the decoration style of a typography object. The updated decoration style takes effect after you call [OH\_Drawing\_TypographyPaint](#oh_drawing_typographypaint) to draw the text. |
| [bool OH\_Drawing\_TypographyTextGetLineStyle(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographytextgetlinestyle) | Checks whether the text line style is enabled for a typography style. |
| [OH\_Drawing\_FontWeight OH\_Drawing\_TypographyTextlineStyleGetFontWeight(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographytextlinestylegetfontweight) | Obtains the font weight of a text line style. |
| [OH\_Drawing\_FontStyle OH\_Drawing\_TypographyTextlineStyleGetFontStyle(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographytextlinestylegetfontstyle) | Obtains the font style of the strut style in a typography style. |
| [char\*\* OH\_Drawing\_TypographyTextlineStyleGetFontFamilies(OH\_Drawing\_TypographyStyle\* style, size\_t\* num)](#oh_drawing_typographytextlinestylegetfontfamilies) | Obtains the font families of a text line style. |
| [void OH\_Drawing\_TypographyTextlineStyleDestroyFontFamilies(char\*\* fontFamilies, size\_t fontFamiliesNum)](#oh_drawing_typographytextlinestyledestroyfontfamilies) | Reclaims the memory occupied by the font families. |
| [double OH\_Drawing\_TypographyTextlineStyleGetFontSize(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographytextlinestylegetfontsize) | Obtains the font size of a text line style. |
| [double OH\_Drawing\_TypographyTextlineStyleGetHeightScale(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographytextlinestylegetheightscale) | Obtains the height scale factor of a text line style. |
| [bool OH\_Drawing\_TypographyTextlineStyleGetHeightOnly(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographytextlinestylegetheightonly) | Checks whether only the font height is used for a text line style. |
| [bool OH\_Drawing\_TypographyTextlineStyleGetHalfLeading(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographytextlinestylegethalfleading) | Checks whether half leading is enabled for a text line style. |
| [double OH\_Drawing\_TypographyTextlineStyleGetSpacingScale(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographytextlinestylegetspacingscale) | Obtains the spacing scale factor of a text line style. |
| [bool OH\_Drawing\_TypographyTextlineGetStyleOnly(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographytextlinegetstyleonly) | Checks whether only the text line style is enabled for a typography style. |
| [OH\_Drawing\_TextAlign OH\_Drawing\_TypographyGetTextAlign(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographygettextalign) | Obtains the text alignment mode. |
| [OH\_Drawing\_TextDirection OH\_Drawing\_TypographyGetTextDirection(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographygettextdirection) | Obtains the text direction of a typography style. |
| [size\_t OH\_Drawing\_TypographyGetTextMaxLines(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographygettextmaxlines) | Obtains the maximum number of lines. |
| [char\* OH\_Drawing\_TypographyGetTextEllipsis(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_typographygettextellipsis) | Obtains the text ellipsis content of a typography style. |
| [void OH\_Drawing\_TypographyDestroyEllipsis(char\* ellipsis)](#oh_drawing_typographydestroyellipsis) | Reclaims the memory occupied by the text ellipsis names. |
| [bool OH\_Drawing\_TypographyStyleEquals(OH\_Drawing\_TypographyStyle\* from, OH\_Drawing\_TypographyStyle\* to)](#oh_drawing_typographystyleequals) | Checks whether two typography styles are the same. The text height modifier mode [OH\_Drawing\_TextHeightBehavior](#oh_drawing_textheightbehavior) is not involved in the comparison. |
| [uint32\_t OH\_Drawing\_TextStyleGetColor(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstylegetcolor) | Obtains the color of a text style. |
| [OH\_Drawing\_TextDecorationStyle OH\_Drawing\_TextStyleGetDecorationStyle(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstylegetdecorationstyle) | Obtains the decoration style of a text style. |
| [OH\_Drawing\_FontWeight OH\_Drawing\_TextStyleGetFontWeight(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstylegetfontweight) | Obtains the font weight of a text style. |
| [OH\_Drawing\_FontStyle OH\_Drawing\_TextStyleGetFontStyle(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstylegetfontstyle) | Obtains the font style of a text style. |
| [OH\_Drawing\_TextBaseline OH\_Drawing\_TextStyleGetBaseline(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstylegetbaseline) | Obtains the baseline of a text style. |
| [char\*\* OH\_Drawing\_TextStyleGetFontFamilies(OH\_Drawing\_TextStyle\* style, size\_t\* num)](#oh_drawing_textstylegetfontfamilies) | Obtains the font families of a text style. |
| [void OH\_Drawing\_TextStyleDestroyFontFamilies(char\*\* fontFamilies, size\_t num)](#oh_drawing_textstyledestroyfontfamilies) | Reclaims the memory occupied by the font families, where **num** specifies the number of font families. |
| [double OH\_Drawing\_TextStyleGetFontSize(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstylegetfontsize) | Obtains the font size of a text style. |
| [double OH\_Drawing\_TextStyleGetLetterSpacing(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstylegetletterspacing) | Obtains the letter spacing of a text style. |
| [double OH\_Drawing\_TextStyleGetWordSpacing(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstylegetwordspacing) | Obtains the word spacing of a text style. |
| [double OH\_Drawing\_TextStyleGetFontHeight(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstylegetfontheight) | Obtains the font height of a text style. |
| [bool OH\_Drawing\_TextStyleGetHalfLeading(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstylegethalfleading) | Checks whether half leading is enabled for a text style. |
| [const char\* OH\_Drawing\_TextStyleGetLocale(OH\_Drawing\_TextStyle\* style)](#oh_drawing_textstylegetlocale) | Obtains the locale of a text style. |
| [void OH\_Drawing\_TypographyDestroyTextBox(OH\_Drawing\_TextBox\* textBox)](#oh_drawing_typographydestroytextbox) | Releases the memory occupied by a text box. |
| [void OH\_Drawing\_SetTextShadow(OH\_Drawing\_TextShadow\* shadow, uint32\_t color, OH\_Drawing\_Point\* offset,double blurRadius)](#oh_drawing_settextshadow) | Sets a text shadow. |
| [OH\_Drawing\_TextTab\* OH\_Drawing\_CreateTextTab(OH\_Drawing\_TextAlign alignment, float location)](#oh_drawing_createtexttab) | Creates a text tab object. |
| [void OH\_Drawing\_DestroyTextTab(OH\_Drawing\_TextTab\* tab)](#oh_drawing_destroytexttab) | Releases the memory occupied by a text tab object. |
| [OH\_Drawing\_TextAlign OH\_Drawing\_GetTextTabAlignment(OH\_Drawing\_TextTab\* tab)](#oh_drawing_gettexttabalignment) | Obtains the alignment mode of a text tab. |
| [float OH\_Drawing\_GetTextTabLocation(OH\_Drawing\_TextTab\* tab)](#oh_drawing_gettexttablocation) | Obtains the location of a text tab. |
| [void OH\_Drawing\_SetTypographyTextTab(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TextTab\* tab)](#oh_drawing_settypographytexttab) | Sets the alignment mode and location of a text tab. When the text alignment mode or ellipsis style is set, the tab does not take effect. When the tab location is less than 1.0, the tab is replaced with a space. |
| [size\_t OH\_Drawing\_GetDrawingArraySize(OH\_Drawing\_Array\* drawingArray)](#oh_drawing_getdrawingarraysize) | Obtains the number of objects in the input object array [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md). |
| [void OH\_Drawing\_SetTypographyTextTrailingSpaceOptimized(OH\_Drawing\_TypographyStyle\* style, bool trailingSpaceOptimized)](#oh_drawing_settypographytexttrailingspaceoptimized) | Sets whether to include the trailing spaces in alignment calculations during text typography. |
| [void OH\_Drawing\_TypographyHandlerAddEncodedText(OH\_Drawing\_TypographyCreate\* handler, const void\* text,size\_t byteLength, OH\_Drawing\_TextEncoding textEncodingType)](#oh_drawing_typographyhandleraddencodedtext) | Adds text encoded in a specified format. |
| [void OH\_Drawing\_SetTypographyTextAutoSpace(OH\_Drawing\_TypographyStyle \*style, bool enableAutoSpace)](#oh_drawing_settypographytextautospace) | 
Sets whether to enable automatic spacing during text typography.

This feature is disabled by default. If enabled, automatic spacing applies between CJK (Chinese, Japanese, and Korean) and Western characters (Latin, Cyrillic, and Greek), between CJK and digits, between CJK and copyright symbols, between copyright symbols and digits, and between copyright symbols and Western characters.

 |
| [void OH\_Drawing\_TypographyUpdateDecorationColor(OH\_Drawing\_Typography\* typography, uint32\_t color)](#oh_drawing_typographyupdatedecorationcolor) | 

Updates the decoration color of a typography object.

The updated decoration color takes effect after you call [OH\_Drawing\_TypographyPaint](#oh_drawing_typographypaint) to draw the text.

 |
| [void OH\_Drawing\_SetTypographyVerticalAlignment(OH\_Drawing\_TypographyStyle\* style,OH\_Drawing\_TextVerticalAlignment align)](#oh_drawing_settypographyverticalalignment) | Sets the vertical alignment mode of the text. |
| [OH\_Drawing\_TypographyStyle\* OH\_Drawing\_CopyTypographyStyle(OH\_Drawing\_TypographyStyle\* style)](#oh_drawing_copytypographystyle) | Creates a copy of an existing paragraph style object. |
| [OH\_Drawing\_TextStyle\* OH\_Drawing\_CopyTextStyle(OH\_Drawing\_TextStyle\* style)](#oh_drawing_copytextstyle) | Creates a copy of an existing text style object. |
| [OH\_Drawing\_TextShadow\* OH\_Drawing\_CopyTextShadow(OH\_Drawing\_TextShadow\* shadow)](#oh_drawing_copytextshadow) | Creates a copy of an existing text shadow object. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTextStyleAttributeDouble(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, double value)](#oh_drawing_settextstyleattributedouble) | Sets the text style attribute of the **double** type. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetTextStyleAttributeDouble(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, double\* value)](#oh_drawing_gettextstyleattributedouble) | Obtains the text style attribute of the **double** type. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTextStyleAttributeInt(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, int value)](#oh_drawing_settextstyleattributeint) | Sets the text style attribute of the **int** type. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetTextStyleAttributeInt(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, int\* value)](#oh_drawing_gettextstyleattributeint) | Obtains the text style attribute of the **int** type. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTypographyStyleAttributeDouble(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, double value)](#oh_drawing_settypographystyleattributedouble) | Sets the typography style attribute of the **double** type. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetTypographyStyleAttributeDouble(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, double\* value)](#oh_drawing_gettypographystyleattributedouble) | Obtains the typography style attribute of the **double** type. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTypographyStyleAttributeInt(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, int value)](#oh_drawing_settypographystyleattributeint) | Sets the typography style attribute of the **int** type. |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_GetTypographyStyleAttributeInt(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, int\* value)](#oh_drawing_gettypographystyleattributeint) | Obtains the typography style attribute of the **int** type. |

#### Enum Description

#### \[h2\]OH\_Drawing\_TextDirection

enum OH\_Drawing\_TextDirection

**Description**

Enumerates the text directions.

**Since**: 8

| Value | Description |
| :-- | :-- |
| TEXT\_DIRECTION\_RTL | Right to left (RTL). |
| TEXT\_DIRECTION\_LTR | Left to right (LTR). |

#### \[h2\]OH\_Drawing\_TextAlign

enum OH\_Drawing\_TextAlign

**Description**

Enumerates the text alignment modes.

**Since**: 8

| Value | Description |
| :-- | :-- |
| TEXT\_ALIGN\_LEFT | Left-aligned. |
| TEXT\_ALIGN\_RIGHT | Right-aligned. |
| TEXT\_ALIGN\_CENTER | Center-aligned. |
| TEXT\_ALIGN\_JUSTIFY | Justified, which means that each line (except the last line) is stretched so that every line has equal width, and the left and right margins are straight. |
| TEXT\_ALIGN\_START | 
When **OH\_Drawing\_TextDirection** is set to **TEXT\_DIRECTION\_LTR**, **TEXT\_ALIGN\_START** and **TEXT\_ALIGN\_LEFT** are the same.

Similarly, when **OH\_Drawing\_TextDirection** is set to **TEXT\_DIRECTION\_RTL**, **TEXT\_ALIGN\_START** and **TEXT\_ALIGN\_RIGHT** are the same.

 |
| TEXT\_ALIGN\_END | 

When **OH\_Drawing\_TextDirection** is set to **TEXT\_DIRECTION\_LTR**, **TEXT\_ALIGN\_END** and **TEXT\_ALIGN\_RIGHT** are the same.

Similarly, when **OH\_Drawing\_TextDirection** is set to **TEXT\_DIRECTION\_RTL**, **TEXT\_ALIGN\_END** and **TEXT\_ALIGN\_LEFT** are the same.

 |

#### \[h2\]OH\_Drawing\_FontWeight

enum OH\_Drawing\_FontWeight

**Description**

Enumerates the font weights.

**Since**: 8

| Value | Description |
| :-- | :-- |
| FONT\_WEIGHT\_100 | Thin. |
| FONT\_WEIGHT\_200 | Extra-light. |
| FONT\_WEIGHT\_300 | Light. |
| FONT\_WEIGHT\_400 | Normal/Regular. |
| FONT\_WEIGHT\_500 | Medium. |
| FONT\_WEIGHT\_600 | Semi-bold. |
| FONT\_WEIGHT\_700 | Bold. |
| FONT\_WEIGHT\_800 | Extra-bold. |
| FONT\_WEIGHT\_900 | Black. |

#### \[h2\]OH\_Drawing\_TextBaseline

enum OH\_Drawing\_TextBaseline

**Description**

Enumerates the text baselines.

**Since**: 8

| Value | Description |
| :-- | :-- |
| TEXT\_BASELINE\_ALPHABETIC | Alphabetic, where the letters in alphabets like English sit on. |
| TEXT\_BASELINE\_IDEOGRAPHIC | Ideographic, where the baseline is at the bottom of the text area. |

#### \[h2\]OH\_Drawing\_TextDecoration

enum OH\_Drawing\_TextDecoration

**Description**

Enumerates the text decorations.

**Since**: 8

| Value | Description |
| :-- | :-- |
| TEXT\_DECORATION\_NONE = 0x0 | No decoration. |
| TEXT\_DECORATION\_UNDERLINE = 0x1 | An underline is used for decoration. |
| TEXT\_DECORATION\_OVERLINE = 0x2 | An overline is used for decoration. |
| TEXT\_DECORATION\_LINE\_THROUGH = 0x4 | A strikethrough is used for decoration. |

#### \[h2\]OH\_Drawing\_FontStyle

enum OH\_Drawing\_FontStyle

**Description**

Enumerates the font styles.

**Since**: 8

| Value | Description |
| :-- | :-- |
| FONT\_STYLE\_NORMAL | Normal style. |
| FONT\_STYLE\_ITALIC | Italic. |
| FONT\_STYLE\_OBLIQUE | Oblique. |

#### \[h2\]OH\_Drawing\_PlaceholderVerticalAlignment

enum OH\_Drawing\_PlaceholderVerticalAlignment

**Description**

Enumerates the vertical alignment modes of placeholders.

**Since**: 11

| Value | Description |
| :-- | :-- |
| ALIGNMENT\_OFFSET\_AT\_BASELINE | Aligned to the baseline. |
| ALIGNMENT\_ABOVE\_BASELINE | Aligned above the baseline. |
| ALIGNMENT\_BELOW\_BASELINE | Aligned below the baseline. |
| ALIGNMENT\_TOP\_OF\_ROW\_BOX | Aligned to the top of the row box. |
| ALIGNMENT\_BOTTOM\_OF\_ROW\_BOX | Aligned to the bottom of the row box. |
| ALIGNMENT\_CENTER\_OF\_ROW\_BOX | Aligned to the center of the row box. |
| ALIGNMENT\_FOLLOW\_PARAGRAPH20+ | Follows the vertical alignment mode of the text. |

#### \[h2\]OH\_Drawing\_TextVerticalAlignment

enum OH\_Drawing\_TextVerticalAlignment

**Description**

Enumerates the vertical alignment modes.

**Since**: 20

| Value | Description |
| :-- | :-- |
| TEXT\_VERTICAL\_ALIGNMENT\_BASELINE | Aligned to the baseline. |
| TEXT\_VERTICAL\_ALIGNMENT\_BOTTOM | Bottom aligned. |
| TEXT\_VERTICAL\_ALIGNMENT\_CENTER | Center-aligned. |
| TEXT\_VERTICAL\_ALIGNMENT\_TOP | Top aligned. |

#### \[h2\]OH\_Drawing\_TextDecorationStyle

enum OH\_Drawing\_TextDecorationStyle

**Description**

Enumerates the text decoration styles.

**Since**: 11

| Value | Description |
| :-- | :-- |
| TEXT\_DECORATION\_STYLE\_SOLID | Solid style. |
| TEXT\_DECORATION\_STYLE\_DOUBLE | Double style. |
| TEXT\_DECORATION\_STYLE\_DOTTED | Dotted style. |
| TEXT\_DECORATION\_STYLE\_DASHED | Dashed style. |
| TEXT\_DECORATION\_STYLE\_WAVY | Wavy style. |

#### \[h2\]OH\_Drawing\_EllipsisModal

enum OH\_Drawing\_EllipsisModal

**Description**

Enumerates the ellipsis styles.

**Since**: 11

| Value | Description |
| :-- | :-- |
| ELLIPSIS\_MODAL\_HEAD = 0 | Places the ellipsis in the text header. |
| ELLIPSIS\_MODAL\_MIDDLE = 1 | Places the ellipsis in the middle of the text. |
| ELLIPSIS\_MODAL\_TAIL = 2 | Places the ellipsis at the end of the text. |

#### \[h2\]OH\_Drawing\_BreakStrategy

enum OH\_Drawing\_BreakStrategy

**Description**

Enumerates the text break strategies.

**Since**: 11

| Value | Description |
| :-- | :-- |
| BREAK\_STRATEGY\_GREEDY = 0 | Each line is filled as much as possible during line break. |
| BREAK\_STRATEGY\_HIGH\_QUALITY = 1 | Text continuity is preferentially considered during line break. |
| BREAK\_STRATEGY\_BALANCED = 2 | Line breaks are performed at the word boundary. |

#### \[h2\]OH\_Drawing\_WordBreakType

enum OH\_Drawing\_WordBreakType

**Description**

Enumerates the word break types.

**Since**: 11

| Value | Description |
| :-- | :-- |
| WORD\_BREAK\_TYPE\_NORMAL = 0 | Normal mode. |
| WORD\_BREAK\_TYPE\_BREAK\_ALL = 1 | Breaks the words at any character to prevent overflow. |
| WORD\_BREAK\_TYPE\_BREAK\_WORD = 2 | Breaks the words at arbitrary points to prevent overflow. |
| WORD\_BREAK\_TYPE\_BREAK\_HYPHEN = 3 | 
Uses a hyphen (-) to break a word at the end of each line. If adding a hyphen is not possible, it will behave the same as **WORD\_BREAK\_TYPE\_BREAK\_WORD**.

**Since**: 18

 |

#### \[h2\]OH\_Drawing\_RectHeightStyle

enum OH\_Drawing\_RectHeightStyle

**Description**

Enumerates the rectangle height styles.

**Since**: 11

| Value | Description |
| :-- | :-- |
| RECT\_HEIGHT\_STYLE\_TIGHT | Tight style. |
| RECT\_HEIGHT\_STYLE\_MAX | Maximum style. |
| RECT\_HEIGHT\_STYLE\_INCLUDELINESPACEMIDDLE | Middle style that includes the line spacing. |
| RECT\_HEIGHT\_STYLE\_INCLUDELINESPACETOP | Top style that includes the line spacing. |
| RECT\_HEIGHT\_STYLE\_INCLUDELINESPACEBOTTOM | Bottom style that includes the line spacing. |
| RECT\_HEIGHT\_STYLE\_STRUCT | Structure style. |

#### \[h2\]OH\_Drawing\_RectWidthStyle

enum OH\_Drawing\_RectWidthStyle

**Description**

Enumerates the rectangle width styles.

**Since**: 11

| Value | Description |
| :-- | :-- |
| RECT\_WIDTH\_STYLE\_TIGHT | Tight style. |
| RECT\_WIDTH\_STYLE\_MAX | Maximum style. |

#### \[h2\]OH\_Drawing\_TextBadgeType

enum OH\_Drawing\_TextBadgeType

**Description**

Enumerates the text badge styles.

**Since**: 20

| Value | Description |
| :-- | :-- |
| TEXT\_BADGE\_NONE | Disables the superscript and subscript. |
| TEXT\_SUPERSCRIPT | Enables the superscript. |
| TEXT\_SUBSCRIPT | Enables the subscript. |

#### \[h2\]OH\_Drawing\_FontConfigInfoErrorCode

enum OH\_Drawing\_FontConfigInfoErrorCode

**Description**

Enumerates the error codes that may be used during the obtaining of system font configurations.

**Since**: 12

| Value | Description |
| :-- | :-- |
| SUCCESS\_FONT\_CONFIG\_INFO = 0 | Operation successful. |
| ERROR\_FONT\_CONFIG\_INFO\_UNKNOWN = 1 | Unknown error. |
| ERROR\_FONT\_CONFIG\_INFO\_PARSE\_FILE = 2 | Failed to parse the system configuration file. |
| ERROR\_FONT\_CONFIG\_INFO\_ALLOC\_MEMORY = 3 | Memory allocation fails. |
| ERROR\_FONT\_CONFIG\_INFO\_COPY\_STRING\_DATA = 4 | Failed to copy the string data. |

#### \[h2\]OH\_Drawing\_FontWidth

enum OH\_Drawing\_FontWidth

**Description**

Enumerates the font widths.

**Since**: 12

| Value | Description |
| :-- | :-- |
| FONT\_WIDTH\_ULTRA\_CONDENSED = 1 | Ultra condensed font. |
| FONT\_WIDTH\_EXTRA\_CONDENSED = 2 | Extra condensed font. |
| FONT\_WIDTH\_CONDENSED = 3 | Condensed font. |
| FONT\_WIDTH\_SEMI\_CONDENSED = 4 | Semi-condensed font. |
| FONT\_WIDTH\_NORMAL = 5 | Normal font. |
| FONT\_WIDTH\_SEMI\_EXPANDED = 6 | Semi-expanded font. |
| FONT\_WIDTH\_EXPANDED = 7 | Expanded font. |
| FONT\_WIDTH\_EXTRA\_EXPANDED = 8 | Extra expanded font. |
| FONT\_WIDTH\_ULTRA\_EXPANDED = 9 | Ultra expanded font. |

#### \[h2\]OH\_Drawing\_TextHeightBehavior

enum OH\_Drawing\_TextHeightBehavior

**Description**

Enumerates the text height modifier patterns.

**Since**: 12

| Value | Description |
| :-- | :-- |
| TEXT\_HEIGHT\_ALL = 0x0 | Enables the height set by calling [OH\_Drawing\_SetTextStyleFontHeight](#oh_drawing_settextstylefontheight) for the top of the first line and the bottom of the last line in a paragraph. |
| TEXT\_HEIGHT\_DISABLE\_FIRST\_ASCENT = 0x1 | Disables the height set by calling [OH\_Drawing\_SetTextStyleFontHeight](#oh_drawing_settextstylefontheight) for the top of the first line in a paragraph. |
| TEXT\_HEIGHT\_DISABLE\_LAST\_ASCENT = 0x2 | Disables the height set by calling [OH\_Drawing\_SetTextStyleFontHeight](#oh_drawing_settextstylefontheight) for the bottom of the last line in a paragraph. |
| TEXT\_HEIGHT\_DISABLE\_ALL = 0x1 | 0x2 | Disables the height set by calling [OH\_Drawing\_SetTextStyleFontHeight](#oh_drawing_settextstylefontheight) for both the top of the first line and the bottom of the last line in a paragraph. |

#### \[h2\]OH\_Drawing\_TextStyleType

enum OH\_Drawing\_TextStyleType

**Description**

Enumerates the text style types.

**Since**: 12

| Value | Description |
| :-- | :-- |
| TEXT\_STYLE\_NONE | No text style. |
| TEXT\_STYLE\_ALL\_ATTRIBUTES | All text styles. |
| TEXT\_STYLE\_FONT | Font style. |
| TEXT\_STYLE\_FOREGROUND | Text foreground style. |
| TEXT\_STYLE\_BACKGROUND | Text background style. |
| TEXT\_STYLE\_SHADOW | Text shadow style. |
| TEXT\_STYLE\_DECORATIONS | Text decoration style. |
| TEXT\_STYLE\_LETTER\_SPACING | Text letter spacing style. |
| TEXT\_STYLE\_WORD\_SPACING | Text word spacing style. |

#### \[h2\]OH\_Drawing\_LineHeightStyle

enum OH\_Drawing\_LineHeightStyle

**Description**

Enumerates the scaling base styles of the line height. The default style is **TEXT\_LINE\_HEIGHT\_BY\_FONT\_SIZE**.

**Since**: 21

| Value | Description |
| :-- | :-- |
| TEXT\_LINE\_HEIGHT\_BY\_FONT\_SIZE = 0 | 
Uses the font size as the scaling base.

Formula for calculating the line height: **FontSize** x **FontHeight**.

**FontSize** can be obtained from the [OH\_Drawing\_TextStyleGetFontSize](#oh_drawing_textstylegetfontsize) API.

**FontHeight** can be obtained from the [OH\_Drawing\_TextStyleGetFontHeight](#oh_drawing_textstylegetfontheight) API.

 |
| TEXT\_LINE\_HEIGHT\_BY\_FONT\_HEIGHT = 1 | 

Uses the font height as the scaling base.

Formula for calculating the line height: font height x **FontHeight**.

The font height is obtained after the text is shaped using the font file.

**FontHeight** can be obtained from the [OH\_Drawing\_TextStyleGetFontHeight](#oh_drawing_textstylegetfontheight) API.

 |

#### \[h2\]OH\_Drawing\_TextStyleAttributeId

enum OH\_Drawing\_TextStyleAttributeId

**Description**

Enumerates the text style attributes.

**Since**: 21

| Value | Description |
| :-- | :-- |
| TEXT\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MAXIMUM = 0 | 
Maximum line height.

If line height scaling is enabled, the maximum line height takes effect only when **FontHeight** (which can be obtained from [OH\_Drawing\_TextStyleGetFontHeight](#oh_drawing_textstylegetfontheight)) is greater than 0.

The value is the positive part of a single-precision floating point number. By default, it equals the maximum possible value for such a number.

 |
| TEXT\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MINIMUM = 1 | 

Minimum line height.

If line height scaling is enabled, the minimum line height takes effect only when **FontHeight** (which can be obtained from [OH\_Drawing\_TextStyleGetFontHeight](#oh_drawing_textstylegetfontheight)) is greater than 0.

The value is the non-negative part of a single-precision floating point number. The default value is **0**.

 |
| TEXT\_STYLE\_ATTR\_I\_LINE\_HEIGHT\_STYLE = 2 | Scaling base style of the line height. For details, see [OH\_Drawing\_LineHeightStyle](#oh_drawing_lineheightstyle). |
| TEXT\_STYLE\_ATTR\_I\_FONT\_WIDTH = 3 | Font width. |

#### \[h2\]OH\_Drawing\_TypographyStyleAttributeId

enum OH\_Drawing\_TypographyStyleAttributeId

**Description**

Enumerates the typography style attributes.

For the common attributes of the typography styles and text styles, you are advised to use the text style attributes, which can be obtained from [OH\_Drawing\_TextStyleAttributeId](#oh_drawing_textstyleattributeid).

**Since**: 21

| Value | Description |
| :-- | :-- |
| TYPOGRAPHY\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MAXIMUM = 0 | 
Maximum line height.

If line height scaling is enabled, the maximum line height takes effect only when **FontHeight** (which can be obtained from [OH\_Drawing\_TextStyleGetFontHeight](#oh_drawing_textstylegetfontheight)) is greater than 0.

The value is the positive part of a single-precision floating point number.

 |
| TYPOGRAPHY\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MINIMUM = 1 | 

Minimum line height.

If line height scaling is enabled, the minimum line height takes effect only when **FontHeight** (which can be obtained from [OH\_Drawing\_TextStyleGetFontHeight](#oh_drawing_textstylegetfontheight)) is greater than 0.

The value is the non-negative part of a single-precision floating point number. The default value is **0**.

 |
| TYPOGRAPHY\_STYLE\_ATTR\_D\_LINE\_SPACING = 2 | 

Interline spacing.

**lineSpacing** is not restricted by the maximum and minimum line heights.

By default, line spacing is added to the last line.

You can set **textHeightBehavior** to **DISABLE\_LAST\_ASCENT** in [OH\_Drawing\_TypographyTextSetHeightBehavior](#oh_drawing_typographytextsetheightbehavior) to disable the line spacing of the last line.

The default value is **0**.

 |
| TYPOGRAPHY\_STYLE\_ATTR\_I\_LINE\_HEIGHT\_STYLE = 3 | Scaling base style of the line height. For details, see [OH\_Drawing\_LineHeightStyle](#oh_drawing_lineheightstyle). |
| TYPOGRAPHY\_STYLE\_ATTR\_I\_FONT\_WIDTH = 4 | Font width. |

#### Function Description

#### \[h2\]OH\_Drawing\_CreateTypographyStyle()

OH\_Drawing\_TypographyStyle\* OH\_Drawing\_CreateTypographyStyle(void)

**Description**

Creates an **OH\_Drawing\_TypographyStyle** object. Release this pointer by calling [OH\_Drawing\_DestroyTypographyStyle](#oh_drawing_destroytypographystyle) when this object is no longer needed.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* | Pointer to the created [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object. |

#### \[h2\]OH\_Drawing\_DestroyTypographyStyle()

void OH\_Drawing\_DestroyTypographyStyle(OH\_Drawing\_TypographyStyle\* style)

**Description**

Destroys an **OH\_Drawing\_TypographyStyle** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

#### \[h2\]OH\_Drawing\_SetTypographyTextDirection()

void OH\_Drawing\_SetTypographyTextDirection(OH\_Drawing\_TypographyStyle\* style, int direction)

**Description**

Sets the text direction in a typography style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| int direction | Text direction. For details about the available options, see [OH\_Drawing\_TextDirection](#oh_drawing_textdirection). |

#### \[h2\]OH\_Drawing\_SetTypographyTextAlign()

void OH\_Drawing\_SetTypographyTextAlign(OH\_Drawing\_TypographyStyle\* style, int align)

**Description**

Text alignment mode.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| int align | Text alignment mode. For details about the available options, see [OH\_Drawing\_TextAlign](#oh_drawing_textalign). |

#### \[h2\]OH\_Drawing\_TypographyGetEffectiveAlignment()

int OH\_Drawing\_TypographyGetEffectiveAlignment(OH\_Drawing\_TypographyStyle\* style)

**Description**

Obtains the text alignment mode.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Deprecated from**: 18

**Replaced by**: [OH\_Drawing\_TypographyStyleGetEffectiveAlignment](#oh_drawing_typographystylegeteffectivealignment)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Text alignment mode. |

#### \[h2\]OH\_Drawing\_SetTypographyTextMaxLines()

void OH\_Drawing\_SetTypographyTextMaxLines(OH\_Drawing\_TypographyStyle\* style, int lineNumber)

**Description**

Sets the maximum number of lines in the text.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| int lineNumber | Maximum number of lines. |

#### \[h2\]OH\_Drawing\_CreateTextStyle()

OH\_Drawing\_TextStyle\* OH\_Drawing\_CreateTextStyle(void)

**Description**

Creates an **OH\_Drawing\_TextStyle** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* | Pointer to the created [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object. |

#### \[h2\]OH\_Drawing\_TypographyGetTextStyle()

OH\_Drawing\_TextStyle\* OH\_Drawing\_TypographyGetTextStyle(OH\_Drawing\_TypographyStyle\* style)

**Description**

Obtains the default text style of a typography style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object. Release this pointer by calling [OH\_Drawing\_DestroyTextStyle](#oh_drawing_destroytextstyle) when this object is no longer needed. |

#### \[h2\]OH\_Drawing\_DestroyTextStyle()

void OH\_Drawing\_DestroyTextStyle(OH\_Drawing\_TextStyle\* style)

**Description**

Destroys an **OH\_Drawing\_TextStyle** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

#### \[h2\]OH\_Drawing\_SetTextStyleColor()

void OH\_Drawing\_SetTextStyleColor(OH\_Drawing\_TextStyle\* style, uint32\_t color)

**Description**

Sets the color for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| uint32\_t color | Color. |

#### \[h2\]OH\_Drawing\_SetTextStyleFontSize()

void OH\_Drawing\_SetTextStyleFontSize(OH\_Drawing\_TextStyle\* style, double fontSize)

**Description**

Sets the font size for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| double fontSize | Font size to set. |

#### \[h2\]OH\_Drawing\_SetTextStyleFontWeight()

void OH\_Drawing\_SetTextStyleFontWeight(OH\_Drawing\_TextStyle\* style, int fontWeight)

**Description**

Sets the font weight for a text style. Currently, only the default system font supports font weight adjustment. For other fonts, if the weight is less than semi-bold, there is no variation in stroke thickness. If the weight is greater than or equal to semi-bold, it might result in a fake bold effect.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| int fontWeight | 
Font weight.

For details about the available options, see [OH\_Drawing\_FontWeight](#oh_drawing_fontweight).

 |

#### \[h2\]OH\_Drawing\_SetTextStyleBaseLine()

void OH\_Drawing\_SetTextStyleBaseLine(OH\_Drawing\_TextStyle\* style, int baseline)

**Description**

Sets the baseline for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| int baseline | Text baseline. For details about the available options, see [OH\_Drawing\_TextBaseline](#oh_drawing_textbaseline). |

#### \[h2\]OH\_Drawing\_SetTextStyleDecoration()

void OH\_Drawing\_SetTextStyleDecoration(OH\_Drawing\_TextStyle\* style, int decoration)

**Description**

Sets the decoration for a text style. Only one decoration can be set. To add multiple decorations, use [OH\_Drawing\_AddTextStyleDecoration](#oh_drawing_addtextstyledecoration).

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| int decoration | Text decoration. For details about the available options, see [OH\_Drawing\_TextDecoration](#oh_drawing_textdecoration). |

#### \[h2\]OH\_Drawing\_AddTextStyleDecoration()

void OH\_Drawing\_AddTextStyleDecoration(OH\_Drawing\_TextStyle\* style, int decoration)

**Description**

Adds the decoration for a text style. Multiple decoration lines can be displayed.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| int decoration | 
Decoration to add. The value **1** means to add an underline, **2** means to add an overline, and **4** means to add a strikethrough. You can add various decoration lines at a time via bitwise OR operations.

If a decoration style that is not in the [OH\_Drawing\_TextDecoration](#oh_drawing_textdecoration) enumeration is set, the original decoration is retained.

 |

#### \[h2\]OH\_Drawing\_RemoveTextStyleDecoration()

void OH\_Drawing\_RemoveTextStyleDecoration(OH\_Drawing\_TextStyle\* style, int decoration)

**Description**

Removes the decoration for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| int decoration | 
Decoration to remove. The value **1** means to remove an underline, **2** means to remove an overline, and **4** means to remove a strikethrough. You can remove various text decorations at a time via bitwise OR operations.

If a decoration style that is not in the [OH\_Drawing\_TextDecoration](#oh_drawing_textdecoration) enumeration is set, the original decoration is retained.

 |

#### \[h2\]OH\_Drawing\_SetTextStyleDecorationColor()

void OH\_Drawing\_SetTextStyleDecorationColor(OH\_Drawing\_TextStyle\* style, uint32\_t color)

**Description**

Sets the decoration color for a text style. If this API is not called or **color** is set to **0**, the decoration color follows the text color.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| uint32\_t color | Color. |

#### \[h2\]OH\_Drawing\_SetTextStyleFontHeight()

void OH\_Drawing\_SetTextStyleFontHeight(OH\_Drawing\_TextStyle\* style, double fontHeight)

**Description**

Sets the line height based on the multiple of the font size.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| double fontHeight | Multiple of the font size. |

#### \[h2\]OH\_Drawing\_SetTextStyleFontFamilies()

void OH\_Drawing\_SetTextStyleFontFamilies(OH\_Drawing\_TextStyle\* style,int fontFamiliesNumber, const char\* fontFamilies\[\])

**Description**

Sets the font families for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| int fontFamiliesNumber | Number of font families. A negative number is not allowed. |
| fontFamilies | Pointer to the font families. |

#### \[h2\]OH\_Drawing\_SetTextStyleFontStyle()

void OH\_Drawing\_SetTextStyleFontStyle(OH\_Drawing\_TextStyle\* style, int fontStyle)

**Description**

Sets the font style for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| int fontStyle | Font style. For details about the available options, see [OH\_Drawing\_FontStyle](#oh_drawing_fontstyle). |

#### \[h2\]OH\_Drawing\_SetTextStyleLocale()

void OH\_Drawing\_SetTextStyleLocale(OH\_Drawing\_TextStyle\* style, const char\* locale)

**Description**

Sets the locale for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| const char\* locale | Pointer to the locale. For example, **'en'** indicates English, **'zh-Hans'** indicates Simplified Chinese, and **'zh-Hant'** indicates Traditional Chinese. |

#### \[h2\]OH\_Drawing\_SetTextStyleForegroundBrush()

void OH\_Drawing\_SetTextStyleForegroundBrush(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Brush\* foregroundBrush)

**Description**

Sets the foreground brush for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* foregroundBrush | Pointer to the [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object, which is obtained from [OH\_Drawing\_BrushCreate](../drawing-brush-h/document.md#oh_drawing_brushcreate). |

#### \[h2\]OH\_Drawing\_TextStyleGetForegroundBrush()

void OH\_Drawing\_TextStyleGetForegroundBrush(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Brush\* foregroundBrush)

**Description**

Obtains the foreground brush of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* foregroundBrush | Pointer to the [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object, which is obtained from [OH\_Drawing\_BrushCreate](../drawing-brush-h/document.md#oh_drawing_brushcreate). |

#### \[h2\]OH\_Drawing\_SetTextStyleForegroundPen()

void OH\_Drawing\_SetTextStyleForegroundPen(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Pen\* foregroundPen)

**Description**

Sets the foreground pen for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* foregroundPen | Pointer to the [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object, which is obtained from [OH\_Drawing\_PenCreate](../drawing-pen-h/document.md#oh_drawing_pencreate). |

#### \[h2\]OH\_Drawing\_TextStyleGetForegroundPen()

void OH\_Drawing\_TextStyleGetForegroundPen(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Pen\* foregroundPen)

**Description**

Obtains the foreground pen of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* foregroundPen | Pointer to the [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object, which is obtained from [OH\_Drawing\_PenCreate](../drawing-pen-h/document.md#oh_drawing_pencreate). |

#### \[h2\]OH\_Drawing\_SetTextStyleBackgroundBrush()

void OH\_Drawing\_SetTextStyleBackgroundBrush(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Brush\* backgroundBrush)

**Description**

Sets the background brush for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* backgroundBrush | Pointer to the [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object, which is obtained from [OH\_Drawing\_BrushCreate](../drawing-brush-h/document.md#oh_drawing_brushcreate). |

#### \[h2\]OH\_Drawing\_TextStyleGetBackgroundBrush()

void OH\_Drawing\_TextStyleGetBackgroundBrush(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Brush\* backgroundBrush)

**Description**

Obtains the background brush of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md)\* backgroundBrush | Pointer to the [OH\_Drawing\_Brush](../../structs/oh-drawing-brush/document.md) object, which is obtained from [OH\_Drawing\_BrushCreate](../drawing-brush-h/document.md#oh_drawing_brushcreate). |

#### \[h2\]OH\_Drawing\_SetTextStyleBackgroundPen()

void OH\_Drawing\_SetTextStyleBackgroundPen(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Pen\* backgroundPen)

**Description**

Sets the background pen for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* backgroundPen | Pointer to the [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object, which is obtained from [OH\_Drawing\_PenCreate](../drawing-pen-h/document.md#oh_drawing_pencreate). |

#### \[h2\]OH\_Drawing\_TextStyleGetBackgroundPen()

void OH\_Drawing\_TextStyleGetBackgroundPen(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Pen\* backgroundPen)

**Description**

Obtains the background pen of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md)\* backgroundPen | Pointer to the [OH\_Drawing\_Pen](../../structs/oh-drawing-pen/document.md) object, which is obtained from [OH\_Drawing\_PenCreate](../drawing-pen-h/document.md#oh_drawing_pencreate). |

#### \[h2\]OH\_Drawing\_CreateTypographyHandler()

OH\_Drawing\_TypographyCreate\* OH\_Drawing\_CreateTypographyHandler(OH\_Drawing\_TypographyStyle\* style,OH\_Drawing\_FontCollection\* fontCollection)

**Description**

Creates an **OH\_Drawing\_TypographyCreate** object. Release this pointer by calling [OH\_Drawing\_DestroyTypographyHandler](#oh_drawing_destroytypographyhandler) when this object is no longer needed. You are advised to use the [OH\_Drawing\_CreateSharedFontCollection](../drawing-font-collection-h/document.md#oh_drawing_createsharedfontcollection) function to create an [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md) object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md)\* fontCollection | Pointer to the [OH\_Drawing\_FontCollection](../../structs/oh-drawing-fontcollection/document.md) object, which is obtained from [OH\_Drawing\_CreateFontCollection](../drawing-font-collection-h/document.md#oh_drawing_createfontcollection). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md)\* | Pointer to the **OH\_Drawing\_TypographyCreate** object created. |

#### \[h2\]OH\_Drawing\_DestroyTypographyHandler()

void OH\_Drawing\_DestroyTypographyHandler(OH\_Drawing\_TypographyCreate\* handler)

**Description**

Destroys an **OH\_Drawing\_TypographyCreate** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md)\* handler | Pointer to the [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyHandler](#oh_drawing_createtypographyhandler). |

#### \[h2\]OH\_Drawing\_TypographyHandlerPushTextStyle()

void OH\_Drawing\_TypographyHandlerPushTextStyle(OH\_Drawing\_TypographyCreate\* handler, OH\_Drawing\_TextStyle\* style)

**Description**

Pushes a text style into the text style stack. Any text added afterward will use the style currently on top of the stack.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md)\* handler | Pointer to the [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyHandler](#oh_drawing_createtypographyhandler). |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

#### \[h2\]OH\_Drawing\_TypographyHandlerAddText()

void OH\_Drawing\_TypographyHandlerAddText(OH\_Drawing\_TypographyCreate\* handler, const char\* text)

**Description**

Adds text.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md)\* handler | Pointer to the [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyHandler](#oh_drawing_createtypographyhandler). |
| const char\* text | Pointer to the text content. |

#### \[h2\]OH\_Drawing\_TypographyHandlerPopTextStyle()

void OH\_Drawing\_TypographyHandlerPopTextStyle(OH\_Drawing\_TypographyCreate\* handler)

**Description**

Pops the top text style out of the text style stack.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md)\* handler | Pointer to the [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyHandler](#oh_drawing_createtypographyhandler). |

#### \[h2\]OH\_Drawing\_CreateTypography()

OH\_Drawing\_Typography\* OH\_Drawing\_CreateTypography(OH\_Drawing\_TypographyCreate\* handler)

**Description**

Creates an **OH\_Drawing\_Typography** object. Release this pointer by calling [OH\_Drawing\_DestroyTypography](#oh_drawing_destroytypography) when this object is no longer needed.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md)\* handler | Pointer to the [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyHandler](#oh_drawing_createtypographyhandler). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* | Pointer to the **OH\_Drawing\_Typography** object created. |

#### \[h2\]OH\_Drawing\_DestroyTypography()

void OH\_Drawing\_DestroyTypography(OH\_Drawing\_Typography\* typography)

**Description**

Destroys an **OH\_Drawing\_Typography** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |

#### \[h2\]OH\_Drawing\_TypographyLayout()

void OH\_Drawing\_TypographyLayout(OH\_Drawing\_Typography\* typography, double maxWidth)

**Description**

Lays out the typography.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| double maxWidth | Maximum text width. |

#### \[h2\]OH\_Drawing\_TypographyPaint()

void OH\_Drawing\_TypographyPaint(OH\_Drawing\_Typography\* typography, OH\_Drawing\_Canvas\* canvas,double positionX, double positionY)

**Description**

Draws text from the upper left corner at a specified position. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called and applied.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the **OH\_Drawing\_Canvas** object, which is obtained from [OH\_Drawing\_CanvasCreate](../drawing-canvas-h/document.md#oh_drawing_canvascreate). |
| double positionX | X coordinate. |
| double positionY | Y coordinate. |

#### \[h2\]OH\_Drawing\_TypographyPaintOnPath()

void OH\_Drawing\_TypographyPaintOnPath(OH\_Drawing\_Typography\* typography, OH\_Drawing\_Canvas\* canvas,OH\_Drawing\_Path\* path, double hOffset, double vOffset)

**Description**

Draws text along a path. To prevent text overlap caused by the text width exceeding the layout width, you are advised to use [OH\_Drawing\_SetTypographyTextMaxLines](#oh_drawing_settypographytextmaxlines) to limit the text to a single line.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| [OH\_Drawing\_Canvas](../../structs/oh-drawing-canvas/document.md)\* canvas | Pointer to the **OH\_Drawing\_Canvas** object, which is obtained from [OH\_Drawing\_CanvasCreate](../drawing-canvas-h/document.md#oh_drawing_canvascreate). |
| [OH\_Drawing\_Path](../../structs/oh-drawing-path/document.md)\* path | Pointer to the **OH\_Drawing\_Path** object, which is obtained from [OH\_Drawing\_PathCreate](../drawing-path-h/document.md#oh_drawing_pathcreate). |
| double hOffset | Horizontal offset of the text along the path (X axis). A positive number indicates that the text is moved forward, and a negative number indicates that the text is moved backward. |
| double vOffset | Vertical offset of the text along the path (Y axis). A positive number indicates that the text is moved downward, and a negative number indicates that the text is moved upward. |

#### \[h2\]OH\_Drawing\_TypographyGetMaxWidth()

double OH\_Drawing\_TypographyGetMaxWidth(OH\_Drawing\_Typography\* typography)

**Description**

Obtains the typography width set by the user. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Maximum width. |

#### \[h2\]OH\_Drawing\_TypographyGetHeight()

double OH\_Drawing\_TypographyGetHeight(OH\_Drawing\_Typography\* typography)

**Description**

Obtains the overall height of a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Height. |

#### \[h2\]OH\_Drawing\_TypographyGetLongestLine()

double OH\_Drawing\_TypographyGetLongestLine(OH\_Drawing\_Typography\* typography)

**Description**

Obtains the width of the longest line in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. You are advised to round up the return value. If the text content is empty, **0.0** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Width of the longest line. |

#### \[h2\]OH\_Drawing\_TypographyGetLongestLineWithIndent()

double OH\_Drawing\_TypographyGetLongestLineWithIndent(OH\_Drawing\_Typography\* typography)

**Description**

Obtains the width of the longest line of a typography object, including its indentation. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. You are advised to round up the return value. If the text content is empty, **0.0** is returned.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Width of the longest line, including its indentation, in px. |

#### \[h2\]OH\_Drawing\_TypographyGetMinIntrinsicWidth()

double OH\_Drawing\_TypographyGetMinIntrinsicWidth(OH\_Drawing\_Typography\* typography)

**Description**

Obtains the minimum intrinsic width in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Minimum intrinsic width. |

#### \[h2\]OH\_Drawing\_TypographyGetMaxIntrinsicWidth()

double OH\_Drawing\_TypographyGetMaxIntrinsicWidth(OH\_Drawing\_Typography\* typography)

**Description**

Obtains the maximum intrinsic width in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Maximum intrinsic width. |

#### \[h2\]OH\_Drawing\_TypographyGetAlphabeticBaseline()

double OH\_Drawing\_TypographyGetAlphabeticBaseline(OH\_Drawing\_Typography\* typography)

**Description**

Obtains the alphabetic baseline in a typography object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Alphabetic baseline. |

#### \[h2\]OH\_Drawing\_TypographyGetIdeographicBaseline()

double OH\_Drawing\_TypographyGetIdeographicBaseline(OH\_Drawing\_Typography\* typography)

**Description**

Obtains the ideographic baseline in a typography object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Ideographic baseline. |

#### \[h2\]OH\_Drawing\_TypographyHandlerAddPlaceholder()

void OH\_Drawing\_TypographyHandlerAddPlaceholder(OH\_Drawing\_TypographyCreate\* handler,OH\_Drawing\_PlaceholderSpan\* span)

**Description**

Adds a placeholder.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md)\* handler | Pointer to the [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyHandler](#oh_drawing_createtypographyhandler). |
| [OH\_Drawing\_PlaceholderSpan](../../structs/oh-drawing-placeholderspan/document.md)\* span | Pointer to the [OH\_Drawing\_PlaceholderSpan](../../structs/oh-drawing-placeholderspan/document.md) object. |

#### \[h2\]OH\_Drawing\_TypographyDidExceedMaxLines()

bool OH\_Drawing\_TypographyDidExceedMaxLines(OH\_Drawing\_Typography\* typography)

**Description**

Checks whether the text in the typography object exceeds the line limit. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. It returns **false** if the line limit is not set using [OH\_Drawing\_SetTypographyTextMaxLines](#oh_drawing_settypographytextmaxlines).

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the maximum number of lines is exceeded; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_TypographyGetRectsForRange()

OH\_Drawing\_TextBox\* OH\_Drawing\_TypographyGetRectsForRange(OH\_Drawing\_Typography\* typography,size\_t start, size\_t end, OH\_Drawing\_RectHeightStyle heightStyle, OH\_Drawing\_RectWidthStyle widthStyle)

**Description**

Obtains text boxes in a given range of a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. Release this pointer by calling [OH\_Drawing\_TypographyDestroyTextBox](#oh_drawing_typographydestroytextbox) when this object is no longer needed.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| size\_t start | Start position. |
| size\_t end | End position. |
| [OH\_Drawing\_RectHeightStyle](#oh_drawing_rectheightstyle) heightStyle | Height style. For details about the available options, see [OH\_Drawing\_RectHeightStyle](#oh_drawing_rectheightstyle). |
| [OH\_Drawing\_RectWidthStyle](#oh_drawing_rectwidthstyle) widthStyle | Width style. For details about the available options, see [OH\_Drawing\_RectWidthStyle](#oh_drawing_rectwidthstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Drawing\_TextBox\* | Text box in the specified range. For details, see [OH\_Drawing\_TextBox](../../structs/oh-drawing-textbox/document.md). |

#### \[h2\]OH\_Drawing\_TypographyGetRectsForPlaceholders()

OH\_Drawing\_TextBox\* OH\_Drawing\_TypographyGetRectsForPlaceholders(OH\_Drawing\_Typography\* typography)

**Description**

Obtains text boxes for placeholders in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. Release this pointer by calling [OH\_Drawing\_TypographyDestroyTextBox](#oh_drawing_typographydestroytextbox) when this object is no longer needed.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBox](../../structs/oh-drawing-textbox/document.md)\* | Placeholder text box. The return type is [OH\_Drawing\_TextBox](../../structs/oh-drawing-textbox/document.md). |

#### \[h2\]OH\_Drawing\_GetLeftFromTextBox()

float OH\_Drawing\_GetLeftFromTextBox(OH\_Drawing\_TextBox\* textbox, int index)

**Description**

Obtains the left position of a text box.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBox](../../structs/oh-drawing-textbox/document.md)\* textbox | Pointer to the **OH\_Drawing\_TextBox** object, which is obtained from [OH\_Drawing\_TypographyGetRectsForRange](#oh_drawing_typographygetrectsforrange) or [OH\_Drawing\_TypographyGetRectsForPlaceholders](#oh_drawing_typographygetrectsforplaceholders). |
| int index | Index of the text box. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Left position. |

#### \[h2\]OH\_Drawing\_GetRightFromTextBox()

float OH\_Drawing\_GetRightFromTextBox(OH\_Drawing\_TextBox\* textbox, int index)

**Description**

Obtains the right position of a text box.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBox](../../structs/oh-drawing-textbox/document.md)\* textbox | Pointer to the **OH\_Drawing\_TextBox** object, which is obtained from [OH\_Drawing\_TypographyGetRectsForRange](#oh_drawing_typographygetrectsforrange) or [OH\_Drawing\_TypographyGetRectsForPlaceholders](#oh_drawing_typographygetrectsforplaceholders). |
| int index | Index of the text box. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Right position. |

#### \[h2\]OH\_Drawing\_GetTopFromTextBox()

float OH\_Drawing\_GetTopFromTextBox(OH\_Drawing\_TextBox\* textbox, int index)

**Description**

Obtains the top position of a text box.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBox](../../structs/oh-drawing-textbox/document.md)\* textbox | Pointer to the **OH\_Drawing\_TextBox** object, which is obtained from [OH\_Drawing\_TypographyGetRectsForRange](#oh_drawing_typographygetrectsforrange) or [OH\_Drawing\_TypographyGetRectsForPlaceholders](#oh_drawing_typographygetrectsforplaceholders). |
| int index | Index of the text box. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Top position. |

#### \[h2\]OH\_Drawing\_GetBottomFromTextBox()

float OH\_Drawing\_GetBottomFromTextBox(OH\_Drawing\_TextBox\* textbox, int index)

**Description**

Obtains the bottom position of a text box.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBox](../../structs/oh-drawing-textbox/document.md)\* textbox | Pointer to the **OH\_Drawing\_TextBox** object, which is obtained from [OH\_Drawing\_TypographyGetRectsForRange](#oh_drawing_typographygetrectsforrange) or [OH\_Drawing\_TypographyGetRectsForPlaceholders](#oh_drawing_typographygetrectsforplaceholders). |
| int index | Index of the text box. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Bottom position. |

#### \[h2\]OH\_Drawing\_GetTextDirectionFromTextBox()

int OH\_Drawing\_GetTextDirectionFromTextBox(OH\_Drawing\_TextBox\* textbox, int index)

**Description**

Obtains the text direction of a text box.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBox](../../structs/oh-drawing-textbox/document.md)\* textbox | Pointer to the [OH\_Drawing\_TextBox](../../structs/oh-drawing-textbox/document.md) object, which is obtained from [OH\_Drawing\_TypographyGetRectsForRange](#oh_drawing_typographygetrectsforrange) or [OH\_Drawing\_TypographyGetRectsForPlaceholders](#oh_drawing_typographygetrectsforplaceholders). |
| int index | Index of the text box. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Text direction. |

#### \[h2\]OH\_Drawing\_GetSizeOfTextBox()

size\_t OH\_Drawing\_GetSizeOfTextBox(OH\_Drawing\_TextBox\* textBox)

**Description**

Obtains the number of text boxes.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBox](../../structs/oh-drawing-textbox/document.md)\* textBox | Pointer to the **OH\_Drawing\_TextBox** object, which is obtained from [OH\_Drawing\_TypographyGetRectsForRange](#oh_drawing_typographygetrectsforrange) or [OH\_Drawing\_TypographyGetRectsForPlaceholders](#oh_drawing_typographygetrectsforplaceholders). |

**Returns**

| Type | Description |
| :-- | :-- |
| size\_t | Number of text boxes. |

#### \[h2\]OH\_Drawing\_TypographyGetGlyphPositionAtCoordinate()

OH\_Drawing\_PositionAndAffinity\* OH\_Drawing\_TypographyGetGlyphPositionAtCoordinate(OH\_Drawing\_Typography\* typography,double dx, double dy)

**Description**

Obtains the position and affinity of the glyph at the given coordinates.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Deprecated from**: 18

**Replaced by**: [OH\_Drawing\_TypographyGetGlyphPositionAtCoordinateWithCluster](#oh_drawing_typographygetglyphpositionatcoordinatewithcluster)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| double dx | X coordinate. |
| double dy | Y coordinate. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_PositionAndAffinity](../../structs/oh-drawing-positionandaffinity/document.md)\* | [OH\_Drawing\_PositionAndAffinity](../../structs/oh-drawing-positionandaffinity/document.md) struct that holds the position and affinity of the glyph cluster. |

#### \[h2\]OH\_Drawing\_TypographyGetGlyphPositionAtCoordinateWithCluster()

OH\_Drawing\_PositionAndAffinity\* OH\_Drawing\_TypographyGetGlyphPositionAtCoordinateWithCluster(OH\_Drawing\_Typography\* typography, double dx, double dy)

**Description**

Obtains the position and affinity of the glyph cluster to which the glyph at the given coordinates belongs. The glyph cluster is a container that holds one or more glyphs.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| double dx | X coordinate. |
| double dy | Y coordinate. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_PositionAndAffinity](../../structs/oh-drawing-positionandaffinity/document.md)\* | [OH\_Drawing\_PositionAndAffinity](../../structs/oh-drawing-positionandaffinity/document.md) struct that holds the position and affinity of the glyph cluster. |

#### \[h2\]OH\_Drawing\_GetPositionFromPositionAndAffinity()

size\_t OH\_Drawing\_GetPositionFromPositionAndAffinity(OH\_Drawing\_PositionAndAffinity\* positionAndAffinity)

**Description**

Obtains the position attribute of an **OH\_Drawing\_PositionAndAffinity** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_PositionAndAffinity](../../structs/oh-drawing-positionandaffinity/document.md)\* positionAndAffinity | Pointer to the **OH\_Drawing\_PositionAndAffinity** object, which is obtained from [OH\_Drawing\_TypographyGetGlyphPositionAtCoordinate](#oh_drawing_typographygetglyphpositionatcoordinate) or [OH\_Drawing\_TypographyGetGlyphPositionAtCoordinateWithCluster](#oh_drawing_typographygetglyphpositionatcoordinatewithcluster). |

**Returns**

| Type | Description |
| :-- | :-- |
| size\_t | Position attribute. |

#### \[h2\]OH\_Drawing\_GetAffinityFromPositionAndAffinity()

int OH\_Drawing\_GetAffinityFromPositionAndAffinity(OH\_Drawing\_PositionAndAffinity\* positionAndAffinity)

**Description**

Obtains the affinity attribute of an **OH\_Drawing\_PositionAndAffinity** object. The affinity determines whether the font is close to the front text or rear text.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_PositionAndAffinity](../../structs/oh-drawing-positionandaffinity/document.md)\* positionAndAffinity | Pointer to the **OH\_Drawing\_PositionAndAffinity** object, which is obtained from [OH\_Drawing\_TypographyGetGlyphPositionAtCoordinate](#oh_drawing_typographygetglyphpositionatcoordinate) or [OH\_Drawing\_TypographyGetGlyphPositionAtCoordinateWithCluster](#oh_drawing_typographygetglyphpositionatcoordinatewithcluster). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Affinity attribute. |

#### \[h2\]OH\_Drawing\_TypographyGetWordBoundary()

OH\_Drawing\_Range\* OH\_Drawing\_TypographyGetWordBoundary(OH\_Drawing\_Typography\* typography, size\_t offset)

**Description**

Obtains the word boundary in a typography object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| size\_t offset | Index of the word. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Range](../../structs/oh-drawing-range/document.md)\* | [OH\_Drawing\_Range](../../structs/oh-drawing-range/document.md) struct that holds the word boundary. |

#### \[h2\]OH\_Drawing\_GetStartFromRange()

size\_t OH\_Drawing\_GetStartFromRange(OH\_Drawing\_Range\* range)

**Description**

Obtains the start position of an **OH\_Drawing\_Range** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Range](../../structs/oh-drawing-range/document.md)\* range | Pointer to the **OH\_Drawing\_Range** object, which is obtained from [OH\_Drawing\_TypographyGetWordBoundary](#oh_drawing_typographygetwordboundary). |

**Returns**

| Type | Description |
| :-- | :-- |
| size\_t | Start position. |

#### \[h2\]OH\_Drawing\_GetEndFromRange()

size\_t OH\_Drawing\_GetEndFromRange(OH\_Drawing\_Range\* range)

**Description**

Obtains the end position of an **OH\_Drawing\_Range** object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Range](../../structs/oh-drawing-range/document.md)\* range | Pointer to the **OH\_Drawing\_Range** object, which is obtained from [OH\_Drawing\_TypographyGetWordBoundary](#oh_drawing_typographygetwordboundary). |

**Returns**

| Type | Description |
| :-- | :-- |
| size\_t | End position. |

#### \[h2\]OH\_Drawing\_TypographyGetLineCount()

size\_t OH\_Drawing\_TypographyGetLineCount(OH\_Drawing\_Typography\* typography)

**Description**

Obtains the number of lines in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |

**Returns**

| Type | Description |
| :-- | :-- |
| size\_t | Number of rows obtained. |

#### \[h2\]OH\_Drawing\_SetTextStyleDecorationStyle()

void OH\_Drawing\_SetTextStyleDecorationStyle(OH\_Drawing\_TextStyle\* style, int decorationStyle)

**Description**

Sets the decoration style for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| int decorationStyle | Text decoration style. For details about the available options, see [OH\_Drawing\_TextDecorationStyle](#oh_drawing_textdecorationstyle). |

#### \[h2\]OH\_Drawing\_SetTextStyleDecorationThicknessScale()

void OH\_Drawing\_SetTextStyleDecorationThicknessScale(OH\_Drawing\_TextStyle\* style, double decorationThicknessScale)

**Description**

Sets the thickness scale factor for the decoration style of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| double decorationThicknessScale | Thickness scaling ratio. The default value is **1**. If the value is less than or equal to 0, no decoration line is drawn. |

#### \[h2\]OH\_Drawing\_SetTextStyleLetterSpacing()

void OH\_Drawing\_SetTextStyleLetterSpacing(OH\_Drawing\_TextStyle\* style, double letterSpacing)

**Description**

Sets the letter spacing for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| double letterSpacing | Letter spacing. |

#### \[h2\]OH\_Drawing\_SetTextStyleWordSpacing()

void OH\_Drawing\_SetTextStyleWordSpacing(OH\_Drawing\_TextStyle\* style, double wordSpacing)

**Description**

Sets the word spacing for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| double wordSpacing | Letter spacing. |

#### \[h2\]OH\_Drawing\_SetTextStyleHalfLeading()

void OH\_Drawing\_SetTextStyleHalfLeading(OH\_Drawing\_TextStyle\* style, bool halfLeading)

**Description**

Sets whether to enable half leading for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| bool halfLeading | Whether the half leading takes effect. **true** means yes; **false** otherwise. |

#### \[h2\]OH\_Drawing\_SetTextStyleEllipsis()

void OH\_Drawing\_SetTextStyleEllipsis(OH\_Drawing\_TextStyle\* style, const char\* ellipsis)

**Description**

Sets the ellipsis content for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Deprecated from**: 18

**Replaced by**: [OH\_Drawing\_SetTypographyTextEllipsis](#oh_drawing_settypographytextellipsis)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| const char\* ellipsis | Pointer to the ellipsis content. The data type is a pointer pointing to char. |

#### \[h2\]OH\_Drawing\_SetTextStyleEllipsisModal()

void OH\_Drawing\_SetTextStyleEllipsisModal(OH\_Drawing\_TextStyle\* style, int ellipsisModal)

**Description**

Sets the ellipsis style for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Deprecated from**: 18

**Replaced by**: [OH\_Drawing\_SetTypographyTextEllipsisModal](#oh_drawing_settypographytextellipsismodal)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| int ellipsisModal | Ellipsis style. For details about the available options, see [OH\_Drawing\_EllipsisModal](#oh_drawing_ellipsismodal). |

#### \[h2\]OH\_Drawing\_SetTypographyTextBreakStrategy()

void OH\_Drawing\_SetTypographyTextBreakStrategy(OH\_Drawing\_TypographyStyle\* style, int breakStrategy)

**Description**

Sets the text break strategy.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| int breakStrategy | Break strategy. For details about the available options, see [OH\_Drawing\_BreakStrategy](#oh_drawing_breakstrategy). |

#### \[h2\]OH\_Drawing\_SetTypographyTextWordBreakType()

void OH\_Drawing\_SetTypographyTextWordBreakType(OH\_Drawing\_TypographyStyle\* style, int wordBreakType)

**Description**

Sets the word break type.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| int wordBreakType | Word break type. For details about the available options, see [OH\_Drawing\_WordBreakType](#oh_drawing_wordbreaktype). |

#### \[h2\]OH\_Drawing\_SetTypographyTextEllipsisModal()

void OH\_Drawing\_SetTypographyTextEllipsisModal(OH\_Drawing\_TypographyStyle\* style, int ellipsisModal)

**Description**

Sets the ellipsis style for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the **OH\_Drawing\_TypographyStyle** object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| int ellipsisModal | Ellipsis style. For details about the available options, see [OH\_Drawing\_EllipsisModal](#oh_drawing_ellipsismodal). |

#### \[h2\]OH\_Drawing\_SetTypographyTextEllipsis()

void OH\_Drawing\_SetTypographyTextEllipsis(OH\_Drawing\_TypographyStyle\* style, const char\* ellipsis)

**Description**

Sets the ellipsis text for a typography style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| const char\* ellipsis | Ellipsis text. |

#### \[h2\]OH\_Drawing\_TypographyGetLineHeight()

double OH\_Drawing\_TypographyGetLineHeight(OH\_Drawing\_Typography\* typography, int lineNumber)

**Description**

Obtains the line height in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| int lineNumber | Target line. |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Obtains the height of a given line. |

#### \[h2\]OH\_Drawing\_TypographyGetLineWidth()

double OH\_Drawing\_TypographyGetLineWidth(OH\_Drawing\_Typography\* typography, int lineNumber)

**Description**

Obtains the line width of a specified line. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the **OH\_Drawing\_Typography** object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| int lineNumber | Target line. |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Obtains the width of a given line. |

#### \[h2\]OH\_Drawing\_SetTypographyTextSplitRatio()

void OH\_Drawing\_SetTypographyTextSplitRatio(OH\_Drawing\_TypographyStyle\* style, float textSplitRatio)

**Description**

Sets the text split ratio.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| float textSplitRatio | Text split ratio. |

#### \[h2\]OH\_Drawing\_TypographyIsLineUnlimited()

bool OH\_Drawing\_TypographyIsLineUnlimited(OH\_Drawing\_TypographyStyle\* style)

**Description**

Checks whether the maximum number of lines is limited for text.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if that the maximum number of lines is limited; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_TypographyIsEllipsized()

bool OH\_Drawing\_TypographyIsEllipsized(OH\_Drawing\_TypographyStyle\* style)

**Description**

Checks whether an ellipsis is configured for a typography style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Whether ellipsis is configured for the specified typography style. **true** means yes; **false** otherwise. |

#### \[h2\]OH\_Drawing\_SetTypographyTextLocale()

void OH\_Drawing\_SetTypographyTextLocale(OH\_Drawing\_TypographyStyle\* style, const char\* locale)

**Description**

Sets the locale for a typography style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| const char\* locale | Pointer to the locale. For example, **'en'** indicates English, **'zh-Hans'** indicates Simplified Chinese, and **'zh-Hant'** indicates Traditional Chinese. |

#### \[h2\]OH\_Drawing\_TextStyleGetFontMetrics()

bool OH\_Drawing\_TextStyleGetFontMetrics(OH\_Drawing\_Typography\* typography,OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Font\_Metrics\* fontmetrics)

**Description**

Obtains the font metrics of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| [OH\_Drawing\_Font\_Metrics](../../structs/oh-drawing-font-metrics/document.md)\* fontmetrics | Pointer to the [OH\_Drawing\_Font\_Metrics](../../structs/oh-drawing-font-metrics/document.md) object, which is obtained from [OH\_Drawing\_Font\_Metrics](../../structs/oh-drawing-font-metrics/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Whether the font attributes are obtained. **true** means yes; **false** otherwise. |

#### \[h2\]OH\_Drawing\_SetTypographyTextStyle()

void OH\_Drawing\_SetTypographyTextStyle(OH\_Drawing\_TypographyStyle\* handler, OH\_Drawing\_TextStyle\* style)

**Description**

Sets a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* handler | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

#### \[h2\]OH\_Drawing\_CreateFontDescriptor()

OH\_Drawing\_FontDescriptor\* OH\_Drawing\_CreateFontDescriptor(void)

**Description**

Creates an **OH\_Drawing\_FontDescriptor** object to describe the detailed information about a system font.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md)\* | Pointer to the created [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md) object. |

#### \[h2\]OH\_Drawing\_DestroyFontDescriptor()

void OH\_Drawing\_DestroyFontDescriptor(OH\_Drawing\_FontDescriptor\* descriptor)

**Description**

Destroys an **OH\_Drawing\_FontDescriptor** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md)\* descriptor | Pointer to the [OH\_Drawing\_FontDescriptor](../../structs/oh-drawing-fontdescriptor/document.md) object, which is obtained from [OH\_Drawing\_CreateFontDescriptor](#oh_drawing_createfontdescriptor). |

#### \[h2\]OH\_Drawing\_CreateFontParser()

OH\_Drawing\_FontParser\* OH\_Drawing\_CreateFontParser(void)

**Description**

Creates an **OH\_Drawing\_FontParser** object to parse a system font.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontParser](../../structs/oh-drawing-fontparser/document.md)\* | Pointer to the created [OH\_Drawing\_FontParser](../../structs/oh-drawing-fontparser/document.md) object. |

#### \[h2\]OH\_Drawing\_DestroyFontParser()

void OH\_Drawing\_DestroyFontParser(OH\_Drawing\_FontParser\* parser)

**Description**

Destroys an **OH\_Drawing\_FontParser** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontParser](../../structs/oh-drawing-fontparser/document.md)\* parser | Pointer to the [OH\_Drawing\_FontParser](../../structs/oh-drawing-fontparser/document.md) object, which is obtained from [OH\_Drawing\_CreateFontParser](#oh_drawing_createfontparser). |

#### \[h2\]OH\_Drawing\_FontParserGetSystemFontList()

char\*\* OH\_Drawing\_FontParserGetSystemFontList(OH\_Drawing\_FontParser\* fontParser, size\_t\* num)

**Description**

Obtains the list of system fonts. This function can be used only on 2-in-1 devices and phones.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontParser](../../structs/oh-drawing-fontparser/document.md)\* fontParser | Pointer to the [OH\_Drawing\_FontParser](../../structs/oh-drawing-fontparser/document.md) object, which is obtained from [OH\_Drawing\_CreateFontParser](#oh_drawing_createfontparser). |
| size\_t\* num | Pointer to the number of system font names. |

**Returns**

| Type | Description |
| :-- | :-- |
| char\*\* | System font list. |

#### \[h2\]OH\_Drawing\_DestroySystemFontList()

void OH\_Drawing\_DestroySystemFontList(char\*\* fontList, size\_t num)

**Description**

Reclaims the memory occupied by the system font list.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char\*\* fontList | Double pointer to the list of system font names. |
| size\_t num | Number of system font names. |

#### \[h2\]OH\_Drawing\_FontParserGetFontByName()

OH\_Drawing\_FontDescriptor\* OH\_Drawing\_FontParserGetFontByName(OH\_Drawing\_FontParser\* fontParser, const char\* name)

**Description**

Obtains the descriptor of a system font based on the font name.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontParser](../../structs/oh-drawing-fontparser/document.md)\* fontParser | Pointer to the [OH\_Drawing\_FontParser](../../structs/oh-drawing-fontparser/document.md) object, which is obtained from [OH\_Drawing\_CreateFontParser](#oh_drawing_createfontparser). |
| const char\* name | Pointer to the system font name. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Drawing\_FontDescriptor\* | Font descriptor object. Release this pointer by calling [OH\_Drawing\_DestroyFontParser](#oh_drawing_destroyfontparser) when this object is no longer needed. |

#### \[h2\]OH\_Drawing\_TypographyGetLineMetrics()

OH\_Drawing\_LineMetrics\* OH\_Drawing\_TypographyGetLineMetrics(OH\_Drawing\_Typography\* typography)

**Description**

Obtains the line metrics in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. Release this pointer by calling [OH\_Drawing\_DestroyLineMetrics](#oh_drawing_destroylinemetrics) when this object is no longer needed.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_LineMetrics](../../structs/oh-drawing-linemetrics/document.md)\* | Pointer to the [OH\_Drawing\_LineMetrics](../../structs/oh-drawing-linemetrics/document.md) object. |

#### \[h2\]OH\_Drawing\_LineMetricsGetSize()

size\_t OH\_Drawing\_LineMetricsGetSize(OH\_Drawing\_LineMetrics\* lineMetrics)

**Description**

Obtains the number of lines.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_LineMetrics](../../structs/oh-drawing-linemetrics/document.md)\* lineMetrics | Pointer to the [OH\_Drawing\_LineMetrics](../../structs/oh-drawing-linemetrics/document.md) object, which is obtained from [OH\_Drawing\_LineMetrics](../../structs/oh-drawing-linemetrics/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| size\_t | Number of lines. |

#### \[h2\]OH\_Drawing\_DestroyLineMetrics()

void OH\_Drawing\_DestroyLineMetrics(OH\_Drawing\_LineMetrics\* lineMetrics)

**Description**

Destroys an **OH\_Drawing\_LineMetrics** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_LineMetrics](../../structs/oh-drawing-linemetrics/document.md)\* lineMetrics | Pointer to the [OH\_Drawing\_LineMetrics](../../structs/oh-drawing-linemetrics/document.md) object, which is obtained from [OH\_Drawing\_LineMetrics](../../structs/oh-drawing-linemetrics/document.md). |

#### \[h2\]OH\_Drawing\_TypographyGetLineMetricsAt()

bool OH\_Drawing\_TypographyGetLineMetricsAt(OH\_Drawing\_Typography\* typography,int lineNumber, OH\_Drawing\_LineMetrics\* lineMetric)

**Description**

Obtains the metrics of the given line in a typography object. For details, see the [OH\_Drawing\_LineMetr](../../structs/oh-drawing-linemetrics/document.md) struct. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| int lineNumber | Line No. |
| [OH\_Drawing\_LineMetrics](../../structs/oh-drawing-linemetrics/document.md)\* lineMetric | Pointer to the [OH\_Drawing\_LineMetrics](../../structs/oh-drawing-linemetrics/document.md) object, which is obtained from [OH\_Drawing\_LineMetrics](../../structs/oh-drawing-linemetrics/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Whether the metrics of the given line is obtained. **true** means yes; **false** otherwise. |

#### \[h2\]OH\_Drawing\_TypographyGetLineInfo()

bool OH\_Drawing\_TypographyGetLineInfo(OH\_Drawing\_Typography\* typography, int lineNumber, bool oneLine,bool includeWhitespace, OH\_Drawing\_LineMetrics\* drawingLineMetrics)

**Description**

Obtains the metrics of a given line or the metrics of the first character in a given line in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| int lineNumber | Row No. |
| bool oneLine | Whether to obtain the metrics of the entire line. The value **true** means to obtain the metrics of the entire line, and **false** means to obtain the metrics of the first character in the line. |
| bool includeWhitespace | Whether the text width includes the whitespace. **true** means yes; **false** otherwise. |
| [OH\_Drawing\_LineMetrics](../../structs/oh-drawing-linemetrics/document.md)\* drawingLineMetrics | Pointer to the [OH\_Drawing\_LineMetrics](../../structs/oh-drawing-linemetrics/document.md) object, which is obtained from [OH\_Drawing\_LineMetrics](../../structs/oh-drawing-linemetrics/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the metrics of the given line or the metrics of the first character in the given line is obtained; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_SetTypographyTextFontWeight()

void OH\_Drawing\_SetTypographyTextFontWeight(OH\_Drawing\_TypographyStyle\* style, int weight)

**Description**

Sets the default font weight for a typography style. Currently, only the default system font supports font weight adjustment. For other fonts, if the weight is less than semi-bold, there is no variation in stroke thickness. If the weight is greater than or equal to semi-bold, it might result in a fake bold effect.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| int weight | 
Font weight.

For details about the available options, see [OH\_Drawing\_FontWeight](#oh_drawing_fontweight).

 |

#### \[h2\]OH\_Drawing\_SetTypographyTextFontStyle()

void OH\_Drawing\_SetTypographyTextFontStyle(OH\_Drawing\_TypographyStyle\* style, int fontStyle)

**Description**

Sets the default font style for a typography style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| int fontStyle | Font style. For details about the available options, see [OH\_Drawing\_FontStyle](#oh_drawing_fontstyle). |

#### \[h2\]OH\_Drawing\_SetTypographyTextFontFamily()

void OH\_Drawing\_SetTypographyTextFontFamily(OH\_Drawing\_TypographyStyle\* style, const char\* fontFamily)

**Description**

Sets the font family name for text.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| const char\* fontFamily | Pointer to the name of the font family. |

#### \[h2\]OH\_Drawing\_SetTypographyTextFontSize()

void OH\_Drawing\_SetTypographyTextFontSize(OH\_Drawing\_TypographyStyle\* style, double fontSize)

**Description**

Sets the font size for text.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| double fontSize | Font size, which must be greater than 0. |

#### \[h2\]OH\_Drawing\_SetTypographyTextFontHeight()

void OH\_Drawing\_SetTypographyTextFontHeight(OH\_Drawing\_TypographyStyle\* style, double fontHeight)

**Description**

Sets the font height for text.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| double fontHeight | Font height. |

#### \[h2\]OH\_Drawing\_SetTypographyTextHalfLeading()

void OH\_Drawing\_SetTypographyTextHalfLeading(OH\_Drawing\_TypographyStyle\* style, bool halfLeading)

**Description**

Sets whether to enable half leading for text.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| bool halfLeading | Whether to enable half leading. The value **true** means to enable half lading, and **false** means the opposite. |

#### \[h2\]OH\_Drawing\_SetTypographyTextUseLineStyle()

void OH\_Drawing\_SetTypographyTextUseLineStyle(OH\_Drawing\_TypographyStyle\* style, bool useLineStyle)

**Description**

Sets whether to enable the text line style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| bool useLineStyle | Whether to enable the line style. The value **true** means to enable the line style, and **false** means the opposite. |

#### \[h2\]OH\_Drawing\_SetTypographyTextLineStyleFontWeight()

void OH\_Drawing\_SetTypographyTextLineStyleFontWeight(OH\_Drawing\_TypographyStyle\* style, int weight)

**Description**

Sets the text font weight of the strut style in a typography style. Currently, only the default system font supports font weight adjustment. For other fonts, if the weight is less than semi-bold, there is no variation in stroke thickness. If the weight is greater than or equal to semi-bold, it might result in a fake bold effect.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| int weight | Font weight. For details about the available options, see [OH\_Drawing\_FontWeight](#oh_drawing_fontweight). |

#### \[h2\]OH\_Drawing\_SetTypographyTextLineStyleFontStyle()

void OH\_Drawing\_SetTypographyTextLineStyleFontStyle(OH\_Drawing\_TypographyStyle\* style, int fontStyle)

**Description**

Sets the font style of the strut style in a typography style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| int fontStyle | Font style. For details about the available options, see [OH\_Drawing\_FontStyle](#oh_drawing_fontstyle). |

#### \[h2\]OH\_Drawing\_SetTypographyTextLineStyleFontFamilies()

void OH\_Drawing\_SetTypographyTextLineStyleFontFamilies(OH\_Drawing\_TypographyStyle\* style,int fontFamiliesNumber, const char\* fontFamilies\[\])

**Description**

Sets the font families for a text line style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| int fontFamiliesNumber | Number of font families. |
| fontFamilies | Pointer to the font families. |

#### \[h2\]OH\_Drawing\_SetTypographyTextLineStyleFontSize()

void OH\_Drawing\_SetTypographyTextLineStyleFontSize(OH\_Drawing\_TypographyStyle\* style, double lineStyleFontSize)

**Description**

Sets the font size for a text line style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| double lineStyleFontSize | Font size, which must be greater than 0. |

#### \[h2\]OH\_Drawing\_SetTypographyTextLineStyleFontHeight()

void OH\_Drawing\_SetTypographyTextLineStyleFontHeight(OH\_Drawing\_TypographyStyle\* style, double lineStyleFontHeight)

**Description**

Sets the font height for a text line style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| double lineStyleFontHeight | Font height. |

#### \[h2\]OH\_Drawing\_SetTypographyTextLineStyleHalfLeading()

void OH\_Drawing\_SetTypographyTextLineStyleHalfLeading(OH\_Drawing\_TypographyStyle\* style, bool lineStyleHalfLeading)

**Description**

Sets whether to enable half leading for a text line style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| bool lineStyleHalfLeading | Whether the half leading takes effect. **true** means yes; **false** otherwise. |

#### \[h2\]OH\_Drawing\_SetTypographyTextLineStyleSpacingScale()

void OH\_Drawing\_SetTypographyTextLineStyleSpacingScale(OH\_Drawing\_TypographyStyle\* style, double spacingScale)

**Description**

Sets the spacing scale factor for a text line style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| double spacingScale | Spacing ratio. |

#### \[h2\]OH\_Drawing\_SetTypographyTextLineStyleOnly()

void OH\_Drawing\_SetTypographyTextLineStyleOnly(OH\_Drawing\_TypographyStyle\* style, bool lineStyleOnly)

**Description**

Sets whether to enable the text line style only.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| bool lineStyleOnly | Whether to enable the line style only. **true** means yes; **false** otherwise. |

#### \[h2\]OH\_Drawing\_CreateTextShadow()

OH\_Drawing\_TextShadow\* OH\_Drawing\_CreateTextShadow(void)

**Description**

Creates an **OH\_Drawing\_TextShadow** object. Release this pointer by calling [OH\_Drawing\_DestroyTextShadow](#oh_drawing_destroytextshadow) when this object is no longer needed.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextShadow](../../structs/oh-drawing-textshadow/document.md)\* | Pointer to the **OH\_Drawing\_TextShadow** object created. |

#### \[h2\]OH\_Drawing\_DestroyTextShadow()

void OH\_Drawing\_DestroyTextShadow(OH\_Drawing\_TextShadow\* shadow)

**Description**

Destroys an **OH\_Drawing\_TextShadow** object and reclaims the memory occupied by the object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextShadow](../../structs/oh-drawing-textshadow/document.md)\* shadow | Pointer to the [OH\_Drawing\_TextShadow](../../structs/oh-drawing-textshadow/document.md) object, which is obtained from [OH\_Drawing\_CreateTextShadow](#oh_drawing_createtextshadow). |

#### \[h2\]OH\_Drawing\_TextStyleGetShadows()

OH\_Drawing\_TextShadow\* OH\_Drawing\_TextStyleGetShadows(OH\_Drawing\_TextStyle\* style)

**Description**

Obtains a text shadow container. Release this pointer by calling [OH\_Drawing\_DestroyTextShadows](#oh_drawing_destroytextshadows) when this object is no longer needed.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextShadow](../../structs/oh-drawing-textshadow/document.md)\* | Pointer to the [OH\_Drawing\_TextShadow](../../structs/oh-drawing-textshadow/document.md) object. |

#### \[h2\]OH\_Drawing\_TextStyleGetShadowCount()

int OH\_Drawing\_TextStyleGetShadowCount(OH\_Drawing\_TextStyle\* style)

**Description**

Obtains the size of a text shadow container.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Size of a text shadow container. |

#### \[h2\]OH\_Drawing\_TextStyleAddShadow()

void OH\_Drawing\_TextStyleAddShadow(OH\_Drawing\_TextStyle\* style, const OH\_Drawing\_TextShadow\* shadow)

**Description**

Adds a shadow to a text shadow container.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| const [OH\_Drawing\_TextShadow](../../structs/oh-drawing-textshadow/document.md)\* shadow | Pointer to the [OH\_Drawing\_TextShadow](../../structs/oh-drawing-textshadow/document.md) object, which is obtained from [OH\_Drawing\_CreateTextShadow](#oh_drawing_createtextshadow). |

#### \[h2\]OH\_Drawing\_TextStyleClearShadows()

void OH\_Drawing\_TextStyleClearShadows(OH\_Drawing\_TextStyle\* style)

**Description**

Clears all shadows in a text shadow container.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

#### \[h2\]OH\_Drawing\_TextStyleGetShadowWithIndex()

OH\_Drawing\_TextShadow\* OH\_Drawing\_TextStyleGetShadowWithIndex(OH\_Drawing\_TextStyle\* style, int index)

**Description**

Obtains a shadow with a given index in a text shadow container.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| int index | Index. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextShadow](../../structs/oh-drawing-textshadow/document.md)\* | Pointer to the [OH\_Drawing\_TextShadow](../../structs/oh-drawing-textshadow/document.md) object. |

#### \[h2\]OH\_Drawing\_TypographySetIndents()

void OH\_Drawing\_TypographySetIndents(OH\_Drawing\_Typography\* typography, int indentsNumber, const float indents\[\])

**Description**

Sets indents for typography. If this function is not called, texts will have no indentation applied.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| int indentsNumber | Number of indents. The value must be less than or equal to the length of the indents array to avoid display exceptions caused by access to the out-of-bounds array. |
| indents | Pointer to a floating-point array, in which each element indicates an indentation width, in px. Before calling [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) API, you need to declare and initialize the floating-point array. |

#### \[h2\]OH\_Drawing\_TypographyGetIndentsWithIndex()

float OH\_Drawing\_TypographyGetIndentsWithIndex(OH\_Drawing\_Typography\* typography, int index)

**Description**

Obtains indents with a given index in a typography object. The line index starts from 0.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| int index | Index. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Indents. |

#### \[h2\]OH\_Drawing\_TypographyGetLineTextRange()

OH\_Drawing\_Range\* OH\_Drawing\_TypographyGetLineTextRange(OH\_Drawing\_Typography\* typography,int lineNumber, bool includeSpaces)

**Description**

Obtains the line bounds in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. This function can only be used to obtain the bounds of existing lines. That is, the line index must start from 0, and the maximum index is [OH\_Drawing\_TypographyGetLineCount](#oh_drawing_typographygetlinecount) – 1.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| int lineNumber | Row index. |
| bool includeSpaces | Whether the returned bounds contain spaces. The value **true** means that the bounds contain spaces, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Range](../../structs/oh-drawing-range/document.md)\* | Pointer to the [OH\_Drawing\_Range](../../structs/oh-drawing-range/document.md) object. If the line index is invalid, **start** and **end** in the result value are both **0**. |

#### \[h2\]OH\_Drawing\_DestroyTextShadows()

void OH\_Drawing\_DestroyTextShadows(OH\_Drawing\_TextShadow\* shadow)

**Description**

Reclaims the memory occupied by the vector consisting of the **OH\_Drawing\_TextShadow** objects.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextShadow](../../structs/oh-drawing-textshadow/document.md)\* shadow | Pointer to the [OH\_Drawing\_TextShadow](../../structs/oh-drawing-textshadow/document.md) object, which is obtained from [OH\_Drawing\_CreateTextShadow](#oh_drawing_createtextshadow). |

#### \[h2\]OH\_Drawing\_GetSystemFontConfigInfo()

OH\_Drawing\_FontConfigInfo\* OH\_Drawing\_GetSystemFontConfigInfo(OH\_Drawing\_FontConfigInfoErrorCode\* errorCode)

**Description**

Obtains the system font configuration.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontConfigInfoErrorCode](#oh_drawing_fontconfiginfoerrorcode)\* errorCode | Error code. For details, see [OH\_Drawing\_FontConfigInfoErrorCode](#oh_drawing_fontconfiginfoerrorcode). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontConfigInfo](../../structs/oh-drawing-fontconfiginfo/document.md)\* | Pointer to the system font configuration. When it is no longer required, call [OH\_Drawing\_DestroySystemFontConfigInfo](#oh_drawing_destroysystemfontconfiginfo) to release the pointer to the object. |

#### \[h2\]OH\_Drawing\_DestroySystemFontConfigInfo()

void OH\_Drawing\_DestroySystemFontConfigInfo(OH\_Drawing\_FontConfigInfo\* drawFontCfgInfo)

**Description**

Reclaims the memory occupied by the system font configuration.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontConfigInfo](../../structs/oh-drawing-fontconfiginfo/document.md)\* drawFontCfgInfo | Pointer to the [OH\_Drawing\_FontConfigInfo](../../structs/oh-drawing-fontconfiginfo/document.md) object, which is obtained from [OH\_Drawing\_GetSystemFontConfigInfo](#oh_drawing_getsystemfontconfiginfo). |

#### \[h2\]OH\_Drawing\_SetTextStyleFontStyleStruct()

void OH\_Drawing\_SetTextStyleFontStyleStruct(OH\_Drawing\_TextStyle\* drawingTextStyle,OH\_Drawing\_FontStyleStruct fontStyle)

**Description**

Sets the font style, including the font weight, width, and slant, for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* drawingTextStyle | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| [OH\_Drawing\_FontStyleStruct](../../structs/oh-drawing-fontstylestruct/document.md) fontStyle | Font style, including the font weight, width, and slant. |

#### \[h2\]OH\_Drawing\_SetTextStyleBadgeType()

void OH\_Drawing\_SetTextStyleBadgeType(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextBadgeType textBadgeType)

**Description**

Sets whether to use superscript or subscript in text layout. If this API is not called, the feature is disabled by default.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| [OH\_Drawing\_TextBadgeType](#oh_drawing_textbadgetype) textBadgeType | Sets whether to use superscript or subscript in text layout. **TEXT\_SUPERSCRIPT** indicates that superscript is enabled, and **TEXT\_SUBSCRIPT** indicates that subscript is enabled. The default value is **TEXT\_BADGE\_NONE**, indicating that neither superscript nor subscript is enabled. |

#### \[h2\]OH\_Drawing\_TextStyleGetFontStyleStruct()

OH\_Drawing\_FontStyleStruct OH\_Drawing\_TextStyleGetFontStyleStruct(OH\_Drawing\_TextStyle\* drawingTextStyle)

**Description**

Obtains the font style, including the font weight, width, and slant, of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* drawingTextStyle | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontStyleStruct](../../structs/oh-drawing-fontstylestruct/document.md) | Font style, including the font weight, width, and slant. |

#### \[h2\]OH\_Drawing\_SetTypographyStyleFontStyleStruct()

void OH\_Drawing\_SetTypographyStyleFontStyleStruct(OH\_Drawing\_TypographyStyle\* drawingStyle,OH\_Drawing\_FontStyleStruct fontStyle)

**Description**

Sets the font style, including the font weight, width, and slant, for the default text style of a typography style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* drawingStyle | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| [OH\_Drawing\_FontStyleStruct](../../structs/oh-drawing-fontstylestruct/document.md) fontStyle | Font style, including the font weight, width, and slant. |

#### \[h2\]OH\_Drawing\_TypographyStyleGetFontStyleStruct()

OH\_Drawing\_FontStyleStruct OH\_Drawing\_TypographyStyleGetFontStyleStruct(OH\_Drawing\_TypographyStyle\* drawingStyle)

**Description**

Obtains the font style, including the font weight, width, and slant, of the default text style of a typography style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* drawingStyle | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontStyleStruct](../../structs/oh-drawing-fontstylestruct/document.md) | Font style, including the font weight, width, and slant. |

#### \[h2\]OH\_Drawing\_TextStyleSetBackgroundRect()

void OH\_Drawing\_TextStyleSetBackgroundRect(OH\_Drawing\_TextStyle\* style,const OH\_Drawing\_RectStyle\_Info\* rectStyleInfo, int styleId)

**Description**

Sets a background rectangle and style ID for a text style. The style ID is valid only when the background box is a rounded rectangle.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| const [OH\_Drawing\_RectStyle\_Info](../../structs/oh-drawing-rectstyle-info/document.md)\* rectStyleInfo | Pointer to the [OH\_Drawing\_RectStyle\_Info](../../structs/oh-drawing-rectstyle-info/document.md) object. |
| int styleId | 
Style ID. The style ID is valid only when the background box is a rounded rectangle. Text processing is divided into multiple segments. Each segment has its own text style. **id** indicates the sequence number of the background box in which the segment is drawn.

If the ID of each segment in a row is **0**, all segments are drawn in the same background box. If a row contains segments with IDs **0** and **1**, the segment with ID **0** is drawn in a background box, and the segment with ID **1** is drawn in another background box. Other cases can be deduced in the same way.

 |

#### \[h2\]OH\_Drawing\_TypographyHandlerAddSymbol()

void OH\_Drawing\_TypographyHandlerAddSymbol(OH\_Drawing\_TypographyCreate\* handler, uint32\_t symbol)

**Description**

Adds the symbol to use in the typography creation process.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md)\* handler | Pointer to the [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyHandler](#oh_drawing_createtypographyhandler). |
| uint32\_t symbol | Symbol value. For details, see the Unicode value in the [HarmonyOS Symbol library](https://developer.huawei.com/consumer/en/design/harmonyos-symbol/). |

#### \[h2\]OH\_Drawing\_TextStyleAddFontFeature()

void OH\_Drawing\_TextStyleAddFontFeature(OH\_Drawing\_TextStyle\* style, const char\* tag, int value)

**Description**

Adds a font feature for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| const char\* tag | Pointer to the string identified by the keyword in the font feature key-value pair. |
| int value | Value of the font feature key-value pair. |

#### \[h2\]OH\_Drawing\_TextStyleAddFontVariation()

void OH\_Drawing\_TextStyleAddFontVariation(OH\_Drawing\_TextStyle\* style, const char\* axis, const float value)

**Description**

Adds a font variation. This function takes effect only when the corresponding font file (.ttf file) supports variable adjustment. Otherwise, calling this function does not take effect.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| const char\* axis | Pointer to the key in the font variation key-value pair. Currently, only **'wght'** is supported, indicating the font weight. |
| const float value | Value of the font variation key-value pair. Currently, the value range of **'wght'** for the default font is \[0,900\]. |

#### \[h2\]OH\_Drawing\_TextStyleGetFontFeatures()

OH\_Drawing\_FontFeature\* OH\_Drawing\_TextStyleGetFontFeatures(OH\_Drawing\_TextStyle\* style)

**Description**

Obtains all the contents in a font feature map container of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontFeature](../../structs/oh-drawing-fontfeature/document.md)\* | Pointer to the font feature struct, which stores all the contents obtained. |

#### \[h2\]OH\_Drawing\_TextStyleDestroyFontFeatures()

void OH\_Drawing\_TextStyleDestroyFontFeatures(OH\_Drawing\_FontFeature\* fontFeature, size\_t fontFeatureSize)

**Description**

Reclaims the memory occupied by the struct array that holds all the font features.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_FontFeature](../../structs/oh-drawing-fontfeature/document.md)\* fontFeature | Pointer to the struct array that holds all the font features, which is obtained from [OH\_Drawing\_TextStyleGetFontFeatures](#oh_drawing_textstylegetfontfeatures). |
| size\_t fontFeatureSize | Size of the struct array that holds all the font features. |

#### \[h2\]OH\_Drawing\_TextStyleGetFontFeatureSize()

size\_t OH\_Drawing\_TextStyleGetFontFeatureSize(OH\_Drawing\_TextStyle\* style)

**Description**

Obtains the size of a font feature map container in a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| size\_t | Size of a font feature map container. |

#### \[h2\]OH\_Drawing\_TextStyleClearFontFeature()

void OH\_Drawing\_TextStyleClearFontFeature(OH\_Drawing\_TextStyle\* style)

**Description**

Clears all the contents in a font feature map container of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

#### \[h2\]OH\_Drawing\_TextStyleGetBaselineShift()

double OH\_Drawing\_TextStyleGetBaselineShift(OH\_Drawing\_TextStyle\* style)

**Description**

Obtains the baseline drift of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Baseline shift. |

#### \[h2\]OH\_Drawing\_TextStyleSetBaselineShift()

void OH\_Drawing\_TextStyleSetBaselineShift(OH\_Drawing\_TextStyle\* style, double lineShift)

**Description**

Sets a baseline drift for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the **OH\_Drawing\_TextStyle** object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| double lineShift | Baseline drift of the text style. |

#### \[h2\]OH\_Drawing\_TypographyTextSetHeightBehavior()

void OH\_Drawing\_TypographyTextSetHeightBehavior(OH\_Drawing\_TypographyStyle\* style,OH\_Drawing\_TextHeightBehavior heightMode)

**Description**

Sets a text height modifier pattern.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| [OH\_Drawing\_TextHeightBehavior](#oh_drawing_textheightbehavior) heightMode | Text height modifier mode. The value is an enumerated value of the [OH\_Drawing\_TextHeightBehavior](#oh_drawing_textheightbehavior) type. |

#### \[h2\]OH\_Drawing\_TypographyTextGetHeightBehavior()

OH\_Drawing\_TextHeightBehavior OH\_Drawing\_TypographyTextGetHeightBehavior(OH\_Drawing\_TypographyStyle\* style)

**Description**

Obtains the text height modifier pattern.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextHeightBehavior](#oh_drawing_textheightbehavior) | Text height modifier mode, which is an enumerated value of the [OH\_Drawing\_TextHeightBehavior](#oh_drawing_textheightbehavior) type. |

#### \[h2\]OH\_Drawing\_TypographyGetLineFontMetrics()

OH\_Drawing\_Font\_Metrics\* OH\_Drawing\_TypographyGetLineFontMetrics(OH\_Drawing\_Typography\* typography,size\_t lineNumber, size\_t\* fontMetricsSize)

**Description**

Obtains all font metrics from a given line in a typography object. This function must be called after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called. Otherwise, a null pointer is returned. Release this pointer by calling [OH\_Drawing\_TypographyDestroyLineFontMetrics](#oh_drawing_typographydestroylinefontmetrics) when this object is no longer needed.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| size\_t lineNumber | Line number, which is an integer. The minimum value is 1, and the maximum value depends on the number of lines parsed by the font engine after text input. If a value greater than the maximum number is passed in, an error value is returned and an error message is printed. |
| size\_t\* fontMetricsSize | Pointer to the size of the struct. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_Font\_Metrics](../../structs/oh-drawing-font-metrics/document.md)\* | Returns all the font metrics. |

#### \[h2\]OH\_Drawing\_TypographyDestroyLineFontMetrics()

void OH\_Drawing\_TypographyDestroyLineFontMetrics(OH\_Drawing\_Font\_Metrics\* lineFontMetric)

**Description**

Reclaims the memory occupied by the struct array that holds all the font metrics of a given line.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Font\_Metrics](../../structs/oh-drawing-font-metrics/document.md)\* lineFontMetric | Pointer to the first address of the struct array. |

#### \[h2\]OH\_Drawing\_TextStyleIsEqual()

bool OH\_Drawing\_TextStyleIsEqual(const OH\_Drawing\_TextStyle\* style, const OH\_Drawing\_TextStyle\* comparedStyle)

**Description**

Checks whether two text styles are equal. The word width property is not involved in the comparison.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the first text style. |
| const [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* comparedStyle | Pointer to the first text style. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Whether two text style objects are equal. **true** if the source rectangle is equal to the destination rectangle; **false** otherwise. |

#### \[h2\]OH\_Drawing\_TextStyleIsEqualByFont()

bool OH\_Drawing\_TextStyleIsEqualByFont(const OH\_Drawing\_TextStyle\* style, const OH\_Drawing\_TextStyle\* comparedStyle)

**Description**

Checks whether the font style properties of two text styles are equal.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the first text style. |
| const [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* comparedStyle | Pointer to the first text style. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the two are equal; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_TextStyleIsAttributeMatched()

bool OH\_Drawing\_TextStyleIsAttributeMatched(const OH\_Drawing\_TextStyle\* style,const OH\_Drawing\_TextStyle\* comparedStyle, OH\_Drawing\_TextStyleType textStyleType)

**Description**

Checks whether two text styles have the same font style type.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the first text style. |
| const [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* comparedStyle | Pointer to the first text style. |
| [OH\_Drawing\_TextStyleType](#oh_drawing_textstyletype) textStyleType | Text style types as in [OH\_Drawing\_TextStyleType](#oh_drawing_textstyletype). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Whether two text styles have the same font style type. **true** means yes; **false** otherwise. |

#### \[h2\]OH\_Drawing\_TextStyleSetPlaceholder()

void OH\_Drawing\_TextStyleSetPlaceholder(OH\_Drawing\_TextStyle\* style)

**Description**

Adds a placeholder.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

#### \[h2\]OH\_Drawing\_TextStyleIsPlaceholder()

bool OH\_Drawing\_TextStyleIsPlaceholder(OH\_Drawing\_TextStyle\* style)

**Description**

Checks whether a placeholder is set for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Checks whether a placeholder is set for a text style. **true** means yes; **false** otherwise. |

#### \[h2\]OH\_Drawing\_TypographyStyleGetEffectiveAlignment()

OH\_Drawing\_TextAlign OH\_Drawing\_TypographyStyleGetEffectiveAlignment(OH\_Drawing\_TypographyStyle\* style)

**Description**

Obtains the text alignment mode.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextAlign](#oh_drawing_textalign) | Text alignment modes as in [OH\_Drawing\_TextAlign](#oh_drawing_textalign). |

#### \[h2\]OH\_Drawing\_TypographyStyleIsHintEnabled()

bool OH\_Drawing\_TypographyStyleIsHintEnabled(OH\_Drawing\_TypographyStyle\* style)

**Description**

Checks whether font hinting is enabled for a typography style. Font hinting is used to improve the readability and appearance of small-sized text when rendering it.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Whether to enable font hinting for a typography style. **true**: enabled; **false**: disabled. |

#### \[h2\]OH\_Drawing\_SetTypographyStyleTextStrutStyle()

void OH\_Drawing\_SetTypographyStyleTextStrutStyle(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_StrutStyle\* strutstyle)

**Description**

Sets the strut style for a typography style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| [OH\_Drawing\_StrutStyle](../../structs/oh-drawing-strutstyle/document.md)\* strutstyle | Pointer to the [OH\_Drawing\_StrutStyle](../../structs/oh-drawing-strutstyle/document.md) object, which is obtained from [OH\_Drawing\_TypographyStyleGetStrutStyle](#oh_drawing_typographystylegetstrutstyle). |

#### \[h2\]OH\_Drawing\_TypographyStyleGetStrutStyle()

OH\_Drawing\_StrutStyle\* OH\_Drawing\_TypographyStyleGetStrutStyle(OH\_Drawing\_TypographyStyle\* style)

**Description**

Obtains the strut style of a typography style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_StrutStyle](../../structs/oh-drawing-strutstyle/document.md)\* | Pointer to the [OH\_Drawing\_StrutStyle](../../structs/oh-drawing-strutstyle/document.md) object. |

#### \[h2\]OH\_Drawing\_TypographyStyleDestroyStrutStyle()

void OH\_Drawing\_TypographyStyleDestroyStrutStyle(OH\_Drawing\_StrutStyle\* strutstyle)

**Description**

Reclaims the memory occupied by a strut style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_StrutStyle](../../structs/oh-drawing-strutstyle/document.md)\* strutstyle | Pointer to the [OH\_Drawing\_StrutStyle](../../structs/oh-drawing-strutstyle/document.md) object, which is obtained from [OH\_Drawing\_TypographyStyleGetStrutStyle](#oh_drawing_typographystylegetstrutstyle). |

#### \[h2\]OH\_Drawing\_TypographyStyleStrutStyleEquals()

bool OH\_Drawing\_TypographyStyleStrutStyleEquals(OH\_Drawing\_StrutStyle\* from, OH\_Drawing\_StrutStyle\* to)

**Description**

Checks whether two strut styles are equal.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_StrutStyle](../../structs/oh-drawing-strutstyle/document.md)\* from | Pointer to the first strut style. |
| [OH\_Drawing\_StrutStyle](../../structs/oh-drawing-strutstyle/document.md)\* to | Pointer to the second strut style. |

#### \[h2\]OH\_Drawing\_TypographyStyleSetHintsEnabled()

void OH\_Drawing\_TypographyStyleSetHintsEnabled(OH\_Drawing\_TypographyStyle\* style, bool hintsEnabled)

**Description**

Sets whether to enable font hinting for a typography style. Font hinting is used to improve the readability and appearance of small-sized text when rendering it.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| bool hintsEnabled | Whether to enable font hinting. **true**: enabled; **false**: disabled. |

#### \[h2\]OH\_Drawing\_TypographyMarkDirty()

void  OH\_Drawing\_TypographyMarkDirty(OH\_Drawing\_Typography\* typography)

**Description**

Marks a typography object as dirty data. This function is used to initialize the typography state.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |

#### \[h2\]OH\_Drawing\_TypographyGetUnresolvedGlyphsCount()

int32\_t OH\_Drawing\_TypographyGetUnresolvedGlyphsCount(OH\_Drawing\_Typography\* typography)

**Description**

Obtains the number of unresolved glyphs in a typography object. This function can be called only after [OH\_Drawing\_TypographyLayout](#oh_drawing_typographylayout) is called and applied.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Number of unresolved glyphs. |

#### \[h2\]OH\_Drawing\_TypographyUpdateFontSize()

void OH\_Drawing\_TypographyUpdateFontSize(OH\_Drawing\_Typography\* typography, size\_t from, size\_t to, float fontSize)

**Description**

Updates the font size in a typography object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| size\_t from | Reserved field, which is not used. |
| size\_t to | Reserved field, which is not used. |
| float fontSize | New font size. |

#### \[h2\]OH\_Drawing\_TypographyUpdateFontColor()

void OH\_Drawing\_TypographyUpdateFontColor(OH\_Drawing\_Typography\* typography, uint32\_t color)

**Description**

Updates the font color in a typography object. This API call also updates the decoration color if it hasn't been set yet. The updated font color takes effect after you call [OH\_Drawing\_TypographyPaint](#oh_drawing_typographypaint) to draw the text.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| uint32\_t color | New font color. |

#### \[h2\]OH\_Drawing\_TypographyUpdateDecoration()

void OH\_Drawing\_TypographyUpdateDecoration(OH\_Drawing\_Typography\* typography, OH\_Drawing\_TextDecoration decoration)

**Description**

Updates the decoration type of a typography object. The updated decoration type takes effect after you call [OH\_Drawing\_TypographyPaint](#oh_drawing_typographypaint) to draw the text.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| [OH\_Drawing\_TextDecoration](#oh_drawing_textdecoration) decoration | Updated decoration type. For details, see [OH\_Drawing\_TextDecoration](#oh_drawing_textdecoration). You can set multiple text decoration types at a time via bitwise OR operations. If a decoration type that is not in the [OH\_Drawing\_TextDecoration](#oh_drawing_textdecoration) enumeration is set, the original decoration is retained. |

#### \[h2\]OH\_Drawing\_TypographyUpdateDecorationThicknessScale()

void OH\_Drawing\_TypographyUpdateDecorationThicknessScale(OH\_Drawing\_Typography\* typography,double decorationThicknessScale)

**Description**

Updates the decoration thickness scale of a typography object. The updated decoration thickness scale takes effect after you call [OH\_Drawing\_TypographyPaint](#oh_drawing_typographypaint) to draw the text.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| double decorationThicknessScale | Thickness scaling ratio of the updated text decoration line. The thickness of the decoration line increases as the ratio increases. If the value is less than or equal to 0, the decoration line will not be drawn. |

#### \[h2\]OH\_Drawing\_TypographyUpdateDecorationStyle()

void OH\_Drawing\_TypographyUpdateDecorationStyle(OH\_Drawing\_Typography\* typography,OH\_Drawing\_TextDecorationStyle decorationStyle)

**Description**

Updates the decoration style of a typography object. The updated decoration style takes effect after you call [OH\_Drawing\_TypographyPaint](#oh_drawing_typographypaint) to draw the text.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| [OH\_Drawing\_TextDecorationStyle](#oh_drawing_textdecorationstyle) decorationStyle | Updated text decoration style. For details about the available options, see [OH\_Drawing\_TextDecorationStyle](#oh_drawing_textdecorationstyle). |

#### \[h2\]OH\_Drawing\_TypographyTextGetLineStyle()

bool OH\_Drawing\_TypographyTextGetLineStyle(OH\_Drawing\_TypographyStyle\* style)

**Description**

Checks whether the text line style is enabled for a typography style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Whether the line style is enabled. **true**: enabled; **false**: disabled. |

#### \[h2\]OH\_Drawing\_TypographyTextlineStyleGetFontWeight()

OH\_Drawing\_FontWeight OH\_Drawing\_TypographyTextlineStyleGetFontWeight(OH\_Drawing\_TypographyStyle\* style)

**Description**

Obtains the font weight of a text line style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontWeight](#oh_drawing_fontweight) | 
Font weight.

For details about the available options, see [OH\_Drawing\_FontWeight](#oh_drawing_fontweight).

 |

#### \[h2\]OH\_Drawing\_TypographyTextlineStyleGetFontStyle()

OH\_Drawing\_FontStyle OH\_Drawing\_TypographyTextlineStyleGetFontStyle(OH\_Drawing\_TypographyStyle\* style)

**Description**

Obtains the font style of the strut style in a typography style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontStyle](#oh_drawing_fontstyle) | Font style of the strut style in a typography style. **1** indicates italic, and **0** or others indicate non-italic. For details, see the [OH\_Drawing\_FontStyle](#oh_drawing_fontstyle) enumeration. |

#### \[h2\]OH\_Drawing\_TypographyTextlineStyleGetFontFamilies()

char\*\* OH\_Drawing\_TypographyTextlineStyleGetFontFamilies(OH\_Drawing\_TypographyStyle\* style, size\_t\* num)

**Description**

Obtains the font families of a text line style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| size\_t\* num | Pointer to the number of font families. |

**Returns**

| Type | Description |
| :-- | :-- |
| char\*\* | Font families. |

#### \[h2\]OH\_Drawing\_TypographyTextlineStyleDestroyFontFamilies()

void OH\_Drawing\_TypographyTextlineStyleDestroyFontFamilies(char\*\* fontFamilies, size\_t fontFamiliesNum)

**Description**

Reclaims the memory occupied by the font families.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char\*\* fontFamilies | Double pointer to the font families. |
| size\_t fontFamiliesNum | Number of font families. |

#### \[h2\]OH\_Drawing\_TypographyTextlineStyleGetFontSize()

double OH\_Drawing\_TypographyTextlineStyleGetFontSize(OH\_Drawing\_TypographyStyle\* style)

**Description**

Obtains the font size of a text line style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Font size. |

#### \[h2\]OH\_Drawing\_TypographyTextlineStyleGetHeightScale()

double OH\_Drawing\_TypographyTextlineStyleGetHeightScale(OH\_Drawing\_TypographyStyle\* style)

**Description**

Obtains the height scale factor of a text line style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Height scale factor. |

#### \[h2\]OH\_Drawing\_TypographyTextlineStyleGetHeightOnly()

bool OH\_Drawing\_TypographyTextlineStyleGetHeightOnly(OH\_Drawing\_TypographyStyle\* style)

**Description**

Checks whether only the font height is used for a text line style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Method for calculating the height of a font block. **true** means that the height is calculated based on the font size; **false** means that the height is calculated based on the line spacing. |

#### \[h2\]OH\_Drawing\_TypographyTextlineStyleGetHalfLeading()

bool OH\_Drawing\_TypographyTextlineStyleGetHalfLeading(OH\_Drawing\_TypographyStyle\* style)

**Description**

Checks whether half leading is enabled for a text line style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** if half leading is enabled; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_TypographyTextlineStyleGetSpacingScale()

double OH\_Drawing\_TypographyTextlineStyleGetSpacingScale(OH\_Drawing\_TypographyStyle\* style)

**Description**

Obtains the spacing scale factor of a text line style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Spacing scale factor. |

#### \[h2\]OH\_Drawing\_TypographyTextlineGetStyleOnly()

bool OH\_Drawing\_TypographyTextlineGetStyleOnly(OH\_Drawing\_TypographyStyle\* style)

**Description**

Checks whether only the text line style is enabled for a typography style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Whether only the text line style is enabled for a typography style. **true**: enabled; **false**: disabled. |

#### \[h2\]OH\_Drawing\_TypographyGetTextAlign()

OH\_Drawing\_TextAlign OH\_Drawing\_TypographyGetTextAlign(OH\_Drawing\_TypographyStyle\* style)

**Description**

Obtains the text alignment mode.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextAlign](#oh_drawing_textalign) | Alignment mode. For details about the available options, see [OH\_Drawing\_TextAlign](#oh_drawing_textalign). |

#### \[h2\]OH\_Drawing\_TypographyGetTextDirection()

OH\_Drawing\_TextDirection OH\_Drawing\_TypographyGetTextDirection(OH\_Drawing\_TypographyStyle\* style)

**Description**

Obtains the text direction of a typography style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextDirection](#oh_drawing_textdirection) | Text direction. **0** means right-to-left; **1** means left-to-right. For details, see [OH\_Drawing\_TextDirection](#oh_drawing_textdirection). |

#### \[h2\]OH\_Drawing\_TypographyGetTextMaxLines()

size\_t OH\_Drawing\_TypographyGetTextMaxLines(OH\_Drawing\_TypographyStyle\* style)

**Description**

Obtains the maximum number of lines.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| size\_t | Maximum number of lines. |

#### \[h2\]OH\_Drawing\_TypographyGetTextEllipsis()

char\* OH\_Drawing\_TypographyGetTextEllipsis(OH\_Drawing\_TypographyStyle\* style)

**Description**

Obtains the text ellipsis content of a typography style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| char\* | Ellipsis text. |

#### \[h2\]OH\_Drawing\_TypographyDestroyEllipsis()

void OH\_Drawing\_TypographyDestroyEllipsis(char\* ellipsis)

**Description**

Reclaims the memory occupied by the text ellipsis names.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* ellipsis | Pointer to the text ellipsis names. |

#### \[h2\]OH\_Drawing\_TypographyStyleEquals()

bool OH\_Drawing\_TypographyStyleEquals(OH\_Drawing\_TypographyStyle\* from, OH\_Drawing\_TypographyStyle\* to)

**Description**

Checks whether two typography styles are the same. The text height modifier mode [OH\_Drawing\_TextHeightBehavior](#oh_drawing_textheightbehavior) is not involved in the comparison.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* from | Pointer to the first typography style. |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* to | Pointer to the second typography style. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the two are the same; returns **false** otherwise. |

#### \[h2\]OH\_Drawing\_TextStyleGetColor()

uint32\_t OH\_Drawing\_TextStyleGetColor(OH\_Drawing\_TextStyle\* style)

**Description**

Obtains the color of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Text color. |

#### \[h2\]OH\_Drawing\_TextStyleGetDecorationStyle()

OH\_Drawing\_TextDecorationStyle OH\_Drawing\_TextStyleGetDecorationStyle(OH\_Drawing\_TextStyle\* style)

**Description**

Obtains the decoration style of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextDecorationStyle](#oh_drawing_textdecorationstyle) | Text decoration style. For details, see [OH\_Drawing\_TextDecorationStyle](#oh_drawing_textdecorationstyle). |

#### \[h2\]OH\_Drawing\_TextStyleGetFontWeight()

OH\_Drawing\_FontWeight OH\_Drawing\_TextStyleGetFontWeight(OH\_Drawing\_TextStyle\* style)

**Description**

Obtains the font weight of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontWeight](#oh_drawing_fontweight) | Font weight. For details, see [OH\_Drawing\_FontWeight](#oh_drawing_fontweight). |

#### \[h2\]OH\_Drawing\_TextStyleGetFontStyle()

OH\_Drawing\_FontStyle OH\_Drawing\_TextStyleGetFontStyle(OH\_Drawing\_TextStyle\* style)

**Description**

Obtains the font style of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_FontStyle](#oh_drawing_fontstyle) | Font style. For details, see [OH\_Drawing\_FontStyle](#oh_drawing_fontstyle). |

#### \[h2\]OH\_Drawing\_TextStyleGetBaseline()

OH\_Drawing\_TextBaseline OH\_Drawing\_TextStyleGetBaseline(OH\_Drawing\_TextStyle\* style)

**Description**

Obtains the baseline of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBaseline](#oh_drawing_textbaseline) | Font baseline position. For details, see [OH\_Drawing\_TextBaseline](#oh_drawing_textbaseline). |

#### \[h2\]OH\_Drawing\_TextStyleGetFontFamilies()

char\*\* OH\_Drawing\_TextStyleGetFontFamilies(OH\_Drawing\_TextStyle\* style, size\_t\* num)

**Description**

Obtains the font families of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |
| size\_t\* num | Pointer to the number of font families. |

**Returns**

| Type | Description |
| :-- | :-- |
| char\*\* | Font families. |

#### \[h2\]OH\_Drawing\_TextStyleDestroyFontFamilies()

void OH\_Drawing\_TextStyleDestroyFontFamilies(char\*\* fontFamilies, size\_t num)

**Description**

Reclaims the memory occupied by the font families, where **num** specifies the number of font families.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char\*\* fontFamilies | Double pointer to the font families. |
| size\_t num | Number of font families. |

#### \[h2\]OH\_Drawing\_TextStyleGetFontSize()

double OH\_Drawing\_TextStyleGetFontSize(OH\_Drawing\_TextStyle\* style)

**Description**

Obtains the font size of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Font size. |

#### \[h2\]OH\_Drawing\_TextStyleGetLetterSpacing()

double OH\_Drawing\_TextStyleGetLetterSpacing(OH\_Drawing\_TextStyle\* style)

**Description**

Obtains the letter spacing of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Letter spacing. |

#### \[h2\]OH\_Drawing\_TextStyleGetWordSpacing()

double OH\_Drawing\_TextStyleGetWordSpacing(OH\_Drawing\_TextStyle\* style)

**Description**

Obtains the word spacing of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Word spacing. |

#### \[h2\]OH\_Drawing\_TextStyleGetFontHeight()

double OH\_Drawing\_TextStyleGetFontHeight(OH\_Drawing\_TextStyle\* style)

**Description**

Obtains the font height of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| double | Font height of a text style. |

#### \[h2\]OH\_Drawing\_TextStyleGetHalfLeading()

bool OH\_Drawing\_TextStyleGetHalfLeading(OH\_Drawing\_TextStyle\* style)

**Description**

Checks whether half leading is enabled for a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Whether half leading is enabled for a text style. **true** means enabled; **false** otherwise. |

#### \[h2\]OH\_Drawing\_TextStyleGetLocale()

const char\* OH\_Drawing\_TextStyleGetLocale(OH\_Drawing\_TextStyle\* style)

**Description**

Obtains the locale of a text style.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTextStyle](#oh_drawing_createtextstyle). |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Pointer to the locale in the format of language-country. For example, zh-CN indicates Chinese (China), and en-US indicates English (United States). For details, see BCP 47. |

#### \[h2\]OH\_Drawing\_TypographyDestroyTextBox()

void OH\_Drawing\_TypographyDestroyTextBox(OH\_Drawing\_TextBox\* textBox)

**Description**

Releases the memory occupied by a text box.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextBox](../../structs/oh-drawing-textbox/document.md)\* textBox | Pointer to the [OH\_Drawing\_TextBox](../../structs/oh-drawing-textbox/document.md) object. |

#### \[h2\]OH\_Drawing\_SetTextShadow()

void OH\_Drawing\_SetTextShadow(OH\_Drawing\_TextShadow\* shadow, uint32\_t color, OH\_Drawing\_Point\* offset,double blurRadius)

**Description**

Sets a text shadow.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextShadow](../../structs/oh-drawing-textshadow/document.md)\* shadow | Pointer to the [OH\_Drawing\_TextShadow](../../structs/oh-drawing-textshadow/document.md) object, which is obtained from [OH\_Drawing\_CreateTextShadow](#oh_drawing_createtextshadow). |
| uint32\_t color | Color of the text shadow. For example, if the input parameter is 0xAABBCCDD, AA indicates opacity, BB indicates the value of the red component, CC indicates the value of the green component, and DD indicates the value of the blue component. |
| [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md)\* offset | Pointer to the [OH\_Drawing\_Point](../../structs/oh-drawing-point/document.md) object, which is the offset of the text shadow relative to the text. |
| double blurRadius | Blur radius. The value is a floating point number and has no unit. The value **0.0** means that there is no blur effect. |

#### \[h2\]OH\_Drawing\_CreateTextTab()

OH\_Drawing\_TextTab\* OH\_Drawing\_CreateTextTab(OH\_Drawing\_TextAlign alignment, float location)

**Description**

Creates a text tab object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextAlign](#oh_drawing_textalign) alignment | Alignment mode of the text following the tab character. The value **1** means right alignment, **2** means center alignment, and **0** or other values mean left alignment. |
| float location | Alignment position of the text following the tab character. The unit is px. The minimum value is **1.0**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextTab](../../structs/oh-drawing-texttab/document.md)\* | Pointer to the **OH\_Drawing\_TextTab** object created. If a null pointer is returned, the creation fails. A possible cause is that no memory is available. |

#### \[h2\]OH\_Drawing\_DestroyTextTab()

void OH\_Drawing\_DestroyTextTab(OH\_Drawing\_TextTab\* tab)

**Description**

Releases the memory occupied by a text tab object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextTab](../../structs/oh-drawing-texttab/document.md)\* tab | Pointer to an **OH\_Drawing\_TextTab** object. |

#### \[h2\]OH\_Drawing\_GetTextTabAlignment()

OH\_Drawing\_TextAlign OH\_Drawing\_GetTextTabAlignment(OH\_Drawing\_TextTab\* tab)

**Description**

Obtains the alignment mode of a text tab.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextTab](../../structs/oh-drawing-texttab/document.md)\* tab | Pointer to an **OH\_Drawing\_TextTab** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextAlign](#oh_drawing_textalign) | Alignment mode. The value **1** means right alignment, **2** means center alignment, and **0** or other values mean left alignment. |

#### \[h2\]OH\_Drawing\_GetTextTabLocation()

float OH\_Drawing\_GetTextTabLocation(OH\_Drawing\_TextTab\* tab)

**Description**

Obtains the location of a text tab.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextTab](../../structs/oh-drawing-texttab/document.md)\* tab | Pointer to an **OH\_Drawing\_TextTab** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| float | Position of the text tab. |

#### \[h2\]OH\_Drawing\_SetTypographyTextTab()

void OH\_Drawing\_SetTypographyTextTab(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TextTab\* tab)

**Description**

Sets the alignment mode and location of a text tab. When the text alignment mode or ellipsis style is set, the tab does not take effect. When the tab location is less than 1.0, the tab is replaced with a space.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object. |
| [OH\_Drawing\_TextTab](../../structs/oh-drawing-texttab/document.md)\* tab | Pointer to an **OH\_Drawing\_TextTab** object. |

#### \[h2\]OH\_Drawing\_GetDrawingArraySize()

size\_t OH\_Drawing\_GetDrawingArraySize(OH\_Drawing\_Array\* drawingArray)

**Description**

Obtains the number of objects in the input object array [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md).

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md)\* drawingArray | Pointer to the [OH\_Drawing\_Array](../../structs/oh-drawing-array/document.md) object array. |

**Returns**

| Type | Description |
| :-- | :-- |
| size\_t | Number of objects in the array. |

#### \[h2\]OH\_Drawing\_SetTypographyTextTrailingSpaceOptimized()

void OH\_Drawing\_SetTypographyTextTrailingSpaceOptimized(OH\_Drawing\_TypographyStyle\* style, bool trailingSpaceOptimized)

**Description**

Sets whether to include the trailing spaces in alignment calculations during text typography.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object. |
| bool | Sets whether to include the trailing spaces in alignment calculations during text typography. **true** means not to include; **false** (default) means to include. You are advised to set this parameter to **true** for center-aligned text. |

#### \[h2\]OH\_Drawing\_TypographyHandlerAddEncodedText()

void OH\_Drawing\_TypographyHandlerAddEncodedText(OH\_Drawing\_TypographyCreate\* handler, const void\* text,size\_t byteLength, OH\_Drawing\_TextEncoding textEncodingType)

**Description**

Adds text encoded in a specified format.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md)\* handler | Pointer to the [OH\_Drawing\_TypographyCreate](../../structs/oh-drawing-typographycreate/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyHandler](#oh_drawing_createtypographyhandler). |
| const void\* text | Pointer to the text content. |
| size\_t byteLength | Length of the text, in bytes. |
| [OH\_Drawing\_TextEncoding](../drawing-types-h/document.md#oh_drawing_textencoding) textEncodingType | Text encoding type, which is an enumerated value of [OH\_Drawing\_TextEncoding](../drawing-types-h/document.md#oh_drawing_textencoding). Only **TEXT\_ENCODING\_UTF8**, **TEXT\_ENCODING\_UTF16**, and **TEXT\_ENCODING\_UTF32** are supported. |

#### \[h2\]OH\_Drawing\_SetTypographyTextAutoSpace()

void OH\_Drawing\_SetTypographyTextAutoSpace(OH\_Drawing\_TypographyStyle \*style, bool enableAutoSpace)

**Description**

Sets whether to enable automatic spacing during text typography.

This feature is disabled by default. If enabled, automatic spacing applies between CJK (Chinese, Japanese, and Korean) and Western characters (Latin, Cyrillic, and Greek), between CJK and digits, between CJK and copyright symbols, between copyright symbols and digits, and between copyright symbols and Western characters.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) \*style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| bool enableAutoSpace | Sets whether to enable automatic spacing during text typography. **true** means enabled; **false** (default) means disabled. |

#### \[h2\]OH\_Drawing\_TypographyUpdateDecorationColor()

void OH\_Drawing\_TypographyUpdateDecorationColor(OH\_Drawing\_Typography\* typography, uint32\_t color)

**Description**

Updates the decoration color of a typography object.

The updated decoration color takes effect after you call [OH\_Drawing\_TypographyPaint](#oh_drawing_typographypaint) to draw the text.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md)\* typography | Pointer to the [OH\_Drawing\_Typography](../../structs/oh-drawing-typography/document.md) object, which is obtained from [OH\_Drawing\_CreateTypography](#oh_drawing_createtypography). |
| uint32\_t color | Updated text decoration color. |

#### \[h2\]OH\_Drawing\_SetTypographyVerticalAlignment()

void OH\_Drawing\_SetTypographyVerticalAlignment(OH\_Drawing\_TypographyStyle\* style,OH\_Drawing\_TextVerticalAlignment align)

**Description**

Vertical alignment mode of the text.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object, which is obtained from [OH\_Drawing\_CreateTypographyStyle](#oh_drawing_createtypographystyle). |
| [OH\_Drawing\_TextVerticalAlignment](#oh_drawing_textverticalalignment) align | Vertical alignment mode of the text. The default mode is baseline alignment. For details about other options, see [OH\_Drawing\_TextVerticalAlignment](#oh_drawing_textverticalalignment). |

#### \[h2\]OH\_Drawing\_CopyTypographyStyle()

OH\_Drawing\_TypographyStyle\* OH\_Drawing\_CopyTypographyStyle(OH\_Drawing\_TypographyStyle\* style)

**Description**

Creates a copy of an existing paragraph style object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to the [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object to be copied. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* | Pointer to the copied [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object. If a null pointer is returned, the creation fails. The possible cause is that no memory is available or **style** is a null pointer. Release this pointer by calling [OH\_Drawing\_DestroyTypographyStyle](#oh_drawing_destroytypographystyle) when this object is no longer needed. |

#### \[h2\]OH\_Drawing\_CopyTextStyle()

OH\_Drawing\_TextStyle\* OH\_Drawing\_CopyTextStyle(OH\_Drawing\_TextStyle\* style)

**Description**

Creates a copy of an existing text style object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to the [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object to be copied. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* | Pointer to the copied [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object. If a null pointer is returned, the creation fails. The possible cause is that no memory is available or **style** is a null pointer. Release this pointer by calling [OH\_Drawing\_DestroyTextStyle](#oh_drawing_destroytextstyle) when this object is no longer needed. |

#### \[h2\]OH\_Drawing\_CopyTextShadow()

OH\_Drawing\_TextShadow\* OH\_Drawing\_CopyTextShadow(OH\_Drawing\_TextShadow\* shadow)

**Description**

Creates a copy of an existing text shadow object.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextShadow](../../structs/oh-drawing-textshadow/document.md)\* shadow | Pointer to the [OH\_Drawing\_TextShadow](../../structs/oh-drawing-textshadow/document.md) object to be copied. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_TextShadow](../../structs/oh-drawing-textshadow/document.md)\* | Pointer to the copied [OH\_Drawing\_TextShadow](../../structs/oh-drawing-textshadow/document.md) object. If a null pointer is returned, the creation fails. The possible cause is that no memory is available or **shadow** is a null pointer. Release this pointer by calling [OH\_Drawing\_DestroyTextShadow](#oh_drawing_destroytextshadow) when this object is no longer needed. |

#### \[h2\]OH\_Drawing\_SetTextStyleAttributeDouble()

OH\_Drawing\_ErrorCode OH\_Drawing\_SetTextStyleAttributeDouble(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, double value)

**Description**

Sets the text style attribute of the **double** type.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to an [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object. |
| [OH\_Drawing\_TextStyleAttributeId](#oh_drawing_textstyleattributeid) id | Text style attribute ID. |
| double value | Text style attribute value. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns the execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **style** is NULL.

**OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH** if the input attribute ID does not match the called function.

 |

#### \[h2\]OH\_Drawing\_GetTextStyleAttributeDouble()

OH\_Drawing\_ErrorCode OH\_Drawing\_GetTextStyleAttributeDouble(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, double\* value)

**Description**

Obtains the text style attribute of the **double** type.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to an [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object. |
| [OH\_Drawing\_TextStyleAttributeId](#oh_drawing_textstyleattributeid) id | Text style attribute ID. |
| double\* value | Pointer to the attribute of the **double** type. It is used as an output parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns the execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **style** is NULL.

**OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH** if the input attribute ID does not match the called function.

 |

#### \[h2\]OH\_Drawing\_SetTextStyleAttributeInt()

OH\_Drawing\_ErrorCode OH\_Drawing\_SetTextStyleAttributeInt(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, int value)

**Description**

Sets the text style attribute of the **int** type.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to an [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object. |
| [OH\_Drawing\_TextStyleAttributeId](#oh_drawing_textstyleattributeid) id | Text style attribute ID. |
| int value | Attribute value to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns the execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **style** is NULL.

**OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH** if the input attribute ID does not match the called function.

**OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** if the input value exceeds the value range of the attribute to be set.

 |

#### \[h2\]OH\_Drawing\_GetTextStyleAttributeInt()

OH\_Drawing\_ErrorCode OH\_Drawing\_GetTextStyleAttributeInt(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, int\* value)

**Description**

Obtains the text style attribute of the **int** type.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md)\* style | Pointer to an [OH\_Drawing\_TextStyle](../../structs/oh-drawing-textstyle/document.md) object. |
| [OH\_Drawing\_TextStyleAttributeId](#oh_drawing_textstyleattributeid) id | Text style attribute ID. |
| int\* value | Pointer to the attribute of the **int** type. It is used as an output parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns the execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **style** is NULL.

**OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH** if the input attribute ID does not match the called function.

 |

#### \[h2\]OH\_Drawing\_SetTypographyStyleAttributeDouble()

OH\_Drawing\_ErrorCode OH\_Drawing\_SetTypographyStyleAttributeDouble(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, double value)

**Description**

Sets the typography style attribute of the **double** type.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to an [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object. |
| [OH\_Drawing\_TypographyStyleAttributeId](#oh_drawing_typographystyleattributeid) id | Attribute ID of the text style. |
| double value | Attribute value to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns the execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **style** is NULL.

**OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH** if the input attribute ID does not match the called function.

 |

#### \[h2\]OH\_Drawing\_GetTypographyStyleAttributeDouble()

OH\_Drawing\_ErrorCode OH\_Drawing\_GetTypographyStyleAttributeDouble(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, double\* value)

**Description**

Obtains the typography style attribute of the **double** type.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to an [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object. |
| [OH\_Drawing\_TypographyStyleAttributeId](#oh_drawing_typographystyleattributeid) id | Attribute ID of the text style. |
| double\* value | Pointer to the attribute of the **double** type. It is used as an output parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns the execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **style** is NULL.

**OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH** if the input attribute ID does not match the called function.

 |

#### \[h2\]OH\_Drawing\_SetTypographyStyleAttributeInt()

OH\_Drawing\_ErrorCode OH\_Drawing\_SetTypographyStyleAttributeInt(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, int value)

**Description**

Sets the typography style attribute of the **int** type.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to an [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object. |
| [OH\_Drawing\_TypographyStyleAttributeId](#oh_drawing_typographystyleattributeid) id | Attribute ID of the text style. |
| int value | Attribute value to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns the execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **style** is NULL.

**OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH** if the input attribute ID does not match the called function.

**OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE** if the input value exceeds the value range of the attribute to be set.

 |

#### \[h2\]OH\_Drawing\_GetTypographyStyleAttributeInt()

OH\_Drawing\_ErrorCode OH\_Drawing\_GetTypographyStyleAttributeInt(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, int\* value)

**Description**

Obtains the typography style attribute of the **int** type.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeDrawing

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md)\* style | Pointer to an [OH\_Drawing\_TypographyStyle](../../structs/oh-drawing-typographystyle/document.md) object. |
| [OH\_Drawing\_TypographyStyleAttributeId](#oh_drawing_typographystyleattributeid) id | Attribute ID of the text style. |
| int\* value | Pointer to the attribute of the **int** type. It is used as an output parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](../drawing-error-code-h/document.md#oh_drawing_errorcode) | 
Returns the execution result.

**OH\_DRAWING\_SUCCESS** if the operation is successful.

**OH\_DRAWING\_ERROR\_INVALID\_PARAMETER** if **style** is NULL.

**OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH** if the input attribute ID does not match the called function.

 |
