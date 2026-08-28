# @ohos.graphics.text (Text)

The Text module provides a set of APIs for text layout and font management. It aims to deliver high-quality typesetting through features like character-to-glyph conversion, kerning, line breaking, alignment, and text measurement. Additionally, it provides font management capabilities, including font registration, font descriptors, and font collection management.

This module provides the following classes for creating complex text paragraphs:

-   [TextStyle](#textstyle): defines the font type, size, spacing, and other text properties.
-   [FontCollection](#fontcollection): manages a collection of different fonts.
-   [FontDescriptor](#fontdescriptor14): provides information about font descriptors.
-   [ParagraphStyle](#paragraphstyle): controls line break and word break strategies for the entire paragraph.
-   [ParagraphBuilder](#paragraphbuilder): used to create different paragraph objects.
-   [Paragraph](#paragraph): created by calling [build()](#build) of the **ParagraphBuilder** class.
-   [LineTypeset](#linetypeset18): created by calling [buildLineTypeset()](#buildlinetypeset18) of the **ParagraphBuilder** class.
-   [TextLine](#textline): paragraph text on a line-by-line basis, obtained by calling [getTextLines()](#gettextlines) of the **Paragraph** class.
-   [Run](#run): text typesetting unit, obtained by calling [getGlyphRuns()](#getglyphruns) of the **TextLine** class.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/eLnQFHwMRdG10LVok4FNMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E380C26BFDDC3A115B8CBBE37B8F40EE950DF4C0FCF385C252FBE345215903AC)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { text } from '@kit.ArkGraphics2D'

#### text.setTextHighContrast20+

setTextHighContrast(action: TextHighContrast): void

Sets the high contrast mode for text rendering.

The setting of this API takes effect for the entire process, and all pages in the process share the same mode.

You can call this API to set the high contrast mode, or enable or disable the high contrast mode by toggling the switch on the system settings screen. This API is used to set the high contrast mode for text rendering. The setting of this API takes precedence over the one based on system settings.

This API does not take effect for the text drawing scenario.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| action | [TextHighContrast](#texthighcontrast20) | Yes | High contrast mode for text rendering. |

**Example**

text.setTextHighContrast(text.TextHighContrast.TEXT\_APP\_DISABLE\_HIGH\_CONTRAST)

#### text.setTextUndefinedGlyphDisplay20+

setTextUndefinedGlyphDisplay(noGlyphShow: TextUndefinedGlyphDisplay): void

Sets the glyph type to be used when characters are mapped to the .notdef (undefined) glyph.

This setting affects all text rendered subsequently.

This setting affects how to display undefined characters in the font:

-   The default behavior follows the .notdef glyph design of the font.
-   After this feature is enabled, characters without glyphs are displayed as a tofu block of text.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| noGlyphShow | [TextUndefinedGlyphDisplay](#textundefinedglyphdisplay20) | Yes | Display mode of characters that cannot be shaped. |

**Example**

text.setTextUndefinedGlyphDisplay(text.TextUndefinedGlyphDisplay.USE\_TOFU)

#### text.matchFontDescriptors18+

matchFontDescriptors(desc: FontDescriptor): Promise<Array<FontDescriptor>>

Obtains all system font descriptors that match the provided font descriptor. This API uses a promise to return the result.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| desc | [FontDescriptor](#fontdescriptor14) | Yes | Font descriptor to match against. If this parameter is left unspecified, all system font descriptors are returned. If a specific value is provided, the matching is performed based on the value provided. If the matching fails, an empty array is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[FontDescriptor](#fontdescriptor14)\>> | Promise used to return all matched system font descriptors. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { text } from '@kit.ArkGraphics2D'
import { BusinessError } from '@kit.BasicServicesKit'

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button("font descriptor")
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .width(300)
          .height(80)
          .onClick(() => {
            console.info(\`Get font descriptor start\`)
            let promise = text.matchFontDescriptors({
              weight: text.FontWeight.W400,
            })
            promise.then((data) => {
              console.info(\`Font descriptor array size: ${data.length}\`);
              console.info(\`Font descriptor result: ${JSON.stringify(data)}\`)
            }).catch((error: BusinessError) => {
              console.error(\`Failed to match the font descriptor, error: ${JSON.stringify(error)}\`);
            });
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### text.getSystemFontFullNamesByType14+

getSystemFontFullNamesByType(fontType: SystemFontType): Promise<Array<string>>

Obtains the full names of all fonts of the specified type. This API uses a promise to return the result.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fontType | [SystemFontType](#systemfonttype14) | Yes | Font type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the full names of all fonts of the specified type. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { text } from '@kit.ArkGraphics2D'
import { BusinessError } from '@kit.BasicServicesKit'

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button("get font list")
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .width(300)
          .height(80)
          .onClick(() => {
            let fontType:text.SystemFontType = text.SystemFontType.GENERIC
            let promise = text.getSystemFontFullNamesByType(fontType)
            promise.then((data) => {
              console.info(\`then font list size: ${data.length}\`)
              data.forEach((fontItem) => {
                console.info(fontItem)
              })
            }).catch((error: BusinessError) => {
              console.error(\`Failed to get font fullNames by type, error: ${JSON.stringify(error)}\`);
            });
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### text.getFontDescriptorByFullName14+

getFontDescriptorByFullName(fullName: string, fontType: SystemFontType): Promise<FontDescriptor>

Obtains the font descriptor based on the font name and type. This API uses a promise to return the result.

A font descriptor is a data structure that describes font features. It contains details of the font appearance and properties.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fullName | string | Yes | Font name, It is obtained by calling [getSystemFontFullNamesByType](#textgetsystemfontfullnamesbytype14). |
| fontType | [SystemFontType](#systemfonttype14) | Yes | Font type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[FontDescriptor](#fontdescriptor14)\> | Promise used to return the font descriptor. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**Example**

import { text } from '@kit.ArkGraphics2D'
import { BusinessError } from '@kit.BasicServicesKit'

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button("get fontDesciptor")
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .width(300)
          .height(80)
          .onClick(() => {
            let fontType:text.SystemFontType = text.SystemFontType.GENERIC
            let promise = text.getFontDescriptorByFullName("HarmonyOS Sans", fontType)
            promise.then((fontDescriptor) => {
              console.info(\`desc: ${JSON.stringify(fontDescriptor)}\`)
            }).catch((error: BusinessError) => {
              console.error(\`Failed to get fontDescriptor by fullName, error: ${JSON.stringify(error)}\`);
            });
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### text.getFontDescriptorsFromPath22+

getFontDescriptorsFromPath(path: string | Resource): Promise<Array<FontDescriptor>>

Obtains an array of font descriptors by font file path. This API uses a promise to return the result.

An empty array is returned if the font file is not found, the font file path is invalid, the font file does not have the required permission, or the file is not in the font format.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | [Resource](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource) | Yes | Path of the font file to be queried. The value must be in the format of "file:// + Absolute path of the font file" or $rawfile (Name of the file in the resources/rawfile directory of the project). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[FontDescriptor](#fontdescriptor14)\>> | Promise used to return all font descriptors. |

**Example**

import { text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct GetFontDescriptorsFromPathTest {
  build() {
    Column({ space: 10 }) {
      Button("get fontDesciptors")
        .onClick(async () => {
          let promise = text.getFontDescriptorsFromPath("file:///system/fonts/NotoSansCJK-Regular.ttc")
          promise.then((fontFullDescriptors) => {
            for (let index = 0; index < fontFullDescriptors.length; index++) {
              console.info("Path:" + fontFullDescriptors\[index\].path +
                          "\\npostScriptName:" + fontFullDescriptors\[index\].postScriptName +
                          "\\nfullName:" + fontFullDescriptors\[index\].fullName +
                          "\\nfamilyName:" + fontFullDescriptors\[index\].fontFamily +
                          "\\nfontSubName:" + fontFullDescriptors\[index\].fontSubfamily +
                          "\\nweight:" + fontFullDescriptors\[index\].weight +
                          "\\nwidth:" + fontFullDescriptors\[index\].width +
                          "\\nitalic:" + fontFullDescriptors\[index\].italic +
                          "\\nmonoSpace:" + fontFullDescriptors\[index\].monoSpace +
                          "\\nsymbolic:" + fontFullDescriptors\[index\].symbolic)
            }
          })
        })
    }.width("100%")
    .height("100%")
    .justifyContent(FlexAlign.Center)
  }
}

#### TextHighContrast20+

Enumerates the high contrast types for text rendering.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| TEXT\_FOLLOW\_SYSTEM\_HIGH\_CONTRAST | 0 | Follows the high contrast mode for text rendering in the system settings. |
| TEXT\_APP\_DISABLE\_HIGH\_CONTRAST | 1 | Disables the high contrast mode for text rendering in the application. This mode takes precedence over the one based on system settings. |
| TEXT\_APP\_ENABLE\_HIGH\_CONTRAST | 2 | Enables the high contrast mode for text rendering in the application. The priority of this mode is higher than the mode following the system settings. |

#### TextUndefinedGlyphDisplay20+

Enumerates the modes for displaying undefined text glyphs.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| USE\_DEFAULT | 0 | Follows the internal .notdef glyph design of the font, which can be an empty box, space, or custom symbol. |
| USE\_TOFU | 1 | Always uses explicit tofu blocks to replace undefined glyphs, overriding the default behavior of fonts. It is suitable for debugging missing characters or forcing a uniform display of missing symbols. |

#### TextAlign

Enumerates the text alignment modes.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| LEFT | 0 | Left-aligned. |
| RIGHT | 1 | Right-aligned. |
| CENTER | 2 | Center-aligned. |
| JUSTIFY | 3 | Justified, which means that each line (except the last line) is stretched so that every line has equal width, and the left and right margins are straight. |
| START | 4 | Aligned with the start position, which depends on [TextDirection](#textdirection). |
| END | 5 | Aligned with the end position, which depends on [TextDirection](#textdirection). |

#### TextVerticalAlign20+

Enumerates the vertical alignment modes of text.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| BASELINE | 0 | Aligned to the baseline. |
| BOTTOM | 1 | Bottom-aligned. |
| CENTER | 2 | Center-aligned. |
| TOP | 3 | Top-aligned. |

#### TextDirection

Enumerates the text directions.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| RTL | 0 | Right to left (RTL). |
| LTR | 1 | Left to right (LTR). |

#### BreakStrategy

Enumerates the text break strategies.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| GREEDY | 0 | Fills the current line as much as possible without adding hyphens. |
| HIGH\_QUALITY | 1 | Optimizes layout and may add hyphens when necessary. |
| BALANCED | 2 | Ensures consistent line width in a paragraph, adding hyphens if needed. |

#### WordBreak

Enumerates the word break types.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| NORMAL | 0 | Default mode that break words based on language-specific conventions. |
| BREAK\_ALL | 1 | Allows breaks within any character in non-CJK text. (CJK means Chinese, Japanese, and Korean.) This value is suitable for Asian text that contains some non-Asian text. For example, it can be used to break consecutive English characters. |
| BREAK\_WORD | 2 | Allows breaks between any two characters in non-CJK text. It prioritizes breaking at whitespace or other natural breakpoints to keep words intact. If no breakpoints are found, it breaks between any two characters. For CJK text, this behaves like **NORMAL**. |
| BREAK\_HYPHEN18+ | 3 | 
Attempts to break words at the end of a line using a hyphen. If a hyphen cannot be added, it behaves like **BREAK\_WORD**.

When using this word break strategy, you need to use the locale attribute in [TextStyle](#textstyle) to define the language environment, which affects the word break effect.

 |

#### Decoration

Describes a text decoration.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| textDecoration | [TextDecorationType](#textdecorationtype) | No | Yes | Type of the decoration. The default value is **NONE**. |
| color | [common2D.Color](../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#color) | No | Yes | Color of the decoration. The default value is the text color. |
| decorationStyle | [TextDecorationStyle](#textdecorationstyle) | No | Yes | Style of the decoration. The default value is **SOLID**. |
| decorationThicknessScale | number | No | Yes | Scale factor for the thickness of the decoration line. The value is a floating point number. The default value is **1.0**. If the value is less than or equal to 0, no decoration line is drawn. |

#### TextDecorationType

Enumerates the text decoration types.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | No decoration is used. |
| UNDERLINE | 1 | An underline is used for decoration. |
| OVERLINE | 2 | An overline is used for decoration. |
| LINE\_THROUGH | 4 | A strikethrough is used for decoration. |

#### TextDecorationStyle

Enumerates the text decoration styles.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| SOLID | 0 | Solid style. |
| DOUBLE | 1 | Double style. |
| DOTTED | 2 | Dotted style. |
| DASHED | 3 | Dashed style. |
| WAVY | 4 | Wavy style. |

#### FontWeight

Enumerates the font weights.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| W100 | 0 | Font weight W100. |
| W200 | 1 | Font weight W200. |
| W300 | 2 | Font weight W300. |
| W400 | 3 | Font weight W400. |
| W500 | 4 | Font weight W500. |
| W600 | 5 | Font weight W600. |
| W700 | 6 | Font weight W700. |
| W800 | 7 | Font weight W800. |
| W900 | 8 | Font weight W900. |

#### FontWidth

Enumerates the font widths.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| ULTRA\_CONDENSED | 1 | Ultra condensed. |
| EXTRA\_CONDENSED | 2 | Extra condensed. |
| CONDENSED | 3 | Condensed. |
| SEMI\_CONDENSED | 4 | Semi condensed. |
| NORMAL | 5 | Normal. |
| SEMI\_EXPANDED | 6 | Semi expanded. |
| EXPANDED | 7 | Expanded. |
| EXTRA\_EXPANDED | 8 | Extra expanded. |
| ULTRA\_EXPANDED | 9 | Ultra expanded. |

#### FontStyle

Enumerates the font styles.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| NORMAL | 0 | Normal. |
| ITALIC | 1 | Italic. If no italic version is available for the current font, the oblique version will be used instead. |
| OBLIQUE | 2 | Oblique. If no oblique version is available for the current font, the italic version will be used instead. |

#### TextHeightBehavior

Enumerates the text height modifier patterns.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| ALL | 0x0 | Allows the first line of the paragraph to rise and the last line to drop. |
| DISABLE\_FIRST\_ASCENT | 0x1 | Prevents the first line of a paragraph from rising. |
| DISABLE\_LAST\_ASCENT | 0x2 | Prevents the last line of a paragraph from dropping. |
| DISABLE\_ALL | 0x1 | 0x2 | Prevents the first line of the paragraph to rise and the last line to drop. |

#### TextBaseline

Enumerates the text baseline types.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| ALPHABETIC | 0 | Alphabetic baseline, where the letters in Latin alphabets sit on. |
| IDEOGRAPHIC | 1 | Ideographic baseline, where the baseline is at the bottom of the text area. It is usually used for CJK text. |

#### EllipsisMode

Enumerates the ellipsis styles.

**EllipsisMode.START** and **EllipsisMode.MIDDLE** take effect only when text overflows in a single line.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| START | 0 | Places the ellipsis in the text header. It is valid only when **maxLines** is set to **1** in [ParagraphStyle](#paragraphstyle). |
| MIDDLE | 1 | Places the ellipsis in the middle of the text. It is valid only when **maxLines** is set to **1** in [ParagraphStyle](#paragraphstyle). |
| END | 2 | Places the ellipsis at the end of the text. |

#### TextShadow

Describes the text shadow.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| color | [common2D.Color](../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#color) | No | Yes | Color of the text shadow. The default value is black (255, 0, 0, 0). |
| point | [common2D.Point](../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#point12) | No | Yes | Position of the text shadow relative to the text. The horizontal and vertical coordinates must be greater than or equal to 0. |
| blurRadius | number | No | Yes | Blur radius. The value is a floating point number. The default value is **0.0px**. |

#### RectStyle

Describes the style of a rectangle.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| color | [common2D.Color](../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#color) | No | No | Color of the rectangle. |
| leftTopRadius | number | No | No | Left top radius of the rectangle. |
| rightTopRadius | number | No | No | Right top radius of the rectangle. |
| rightBottomRadius | number | No | No | Right bottom radius of the rectangle. |
| leftBottomRadius | number | No | No | Left bottom radius of the rectangle. |

#### FontFeature

Describes a font feature.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | String identified by the keyword in the font feature key-value pair. |
| value | number | No | No | Value in the font feature key-value pair. |

#### FontVariation

Describes a font variation.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| axis | string | No | No | String identified by the keyword in the font variation key-value pair. |
| value | number | No | No | Value in the font variation key-value pair. |

#### TextBadgeType20+

Enumerates the text badges.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| TEXT\_BADGE\_NONE | 0 | Disables the superscript and subscript. |
| TEXT\_SUPERSCRIPT | 1 | Enables the superscript. |
| TEXT\_SUBSCRIPT | 2 | Enables the subscript. |

#### LineHeightStyle21+

Enumerates the line height scaling base.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| FONT\_SIZE | 0 | Uses the font size as the scaling base. The line height is calculated as follows: [TextStyle](#textstyle).fontSize \* [TextStyle](#textstyle).heightScale. |
| FONT\_HEIGHT | 1 | Uses the font height as the scaling base. The line height is calculated as follows: the height of the shaped glyph \* [TextStyle](#textstyle).heightScale. |

#### TextStyle

Describes a text style.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| decoration | [Decoration](#decoration) | No | Yes | Text decoration. By default, no decoration is used. |
| color | [common2D.Color](../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#color) | No | Yes | Text color. The default color is white. |
| fontWeight | [FontWeight](#fontweight) | No | Yes | Font weight. The default value is **W400**. Currently, only the default system font supports font weight adjustment. For other fonts, if the weight is less than semi-bold (W600), there is no variation in stroke thickness. If the weight is greater than or equal to semi-bold, it might result in a fake bold effect. |
| fontWidth21+ | [FontWidth](#fontwidth) | No | Yes | Font width. The default value is **NORMAL**. |
| fontStyle | [FontStyle](#fontstyle) | No | Yes | Font style. The default value is **NORMAL**. |
| baseline | [TextBaseline](#textbaseline) | No | Yes | Text baseline type. The default value is **ALPHABETIC**. |
| fontFamilies | Array<string> | No | Yes | Array of font families. By default, the array is empty, indicating that all system fonts are matched. |
| fontSize | number | No | Yes | Font size, in units of px. The value is a floating point number. The default value is **14.0**. |
| letterSpacing | number | No | Yes | Letter spacing, in units of px. The value is a floating point number. The default value is **0.0**. A positive value causes characters to spread farther apart, and a negative value bring characters closer together. |
| wordSpacing | number | No | Yes | Word spacing, in units of px. The value is a floating point number. The default value is **0.0**. |
| heightScale | number | No | Yes | Scale factor of the line height. The value is a floating point number. The default value is **1.0**. This parameter is valid only when **heightOnly** is set to\*\* true\*\*. |
| heightOnly | boolean | No | Yes | How the height of the text box is set. The value **true** means that the height of the text box is set based on the font size and the value of **heightScale**, and **false** means that the height is set based on the line height and line spacing. The default value is **false**. |
| halfLeading | boolean | No | Yes | Whether half leading is enabled. Half leading is the leading split in half and applied equally to the top and bottom edges. The value **true** means that half leading is enabled, and **false** means the opposite. The default value is **false**. |
| ellipsis | string | No | Yes | Ellipsis content, which will be used to replace the extra content. |
| ellipsisMode | [EllipsisMode](#ellipsismode) | No | Yes | Ellipsis type. The default value is **END**, indicating that the ellipsis is at the end of a line. |
| locale | string | No | Yes | Locale. For example, **'en'** indicates English, **'zh-Hans'** indicates Simplified Chinese, and **'zh-Hant'** indicates Traditional Chinese. For details, see ISO 639-1. The default value is an empty string. |
| baselineShift | number | No | Yes | Shift of the baseline. The value is a floating point number. The default value is **0.0px**. |
| fontFeatures | Array<[FontFeature](#fontfeature)\> | No | Yes | Array of font features. |
| fontVariations | Array<[FontVariation](#fontvariation)\> | No | Yes | Array of font variations. |
| textShadows | Array<[TextShadow](#textshadow)\> | No | Yes | Array of shadows. |
| backgroundRect | [RectStyle](#rectstyle) | No | Yes | Rectangle style. |
| badgeType20+ | [TextBadgeType](#textbadgetype20) | No | Yes | Sets whether to use superscript or subscript in text layout. **TEXT\_SUPERSCRIPT** indicates that superscript is enabled, and **TEXT\_SUBSCRIPT** indicates that subscript is enabled. The default value is **TEXT\_BADGE\_NONE**, indicating that neither superscript nor subscript is enabled. |
| lineHeightMaximum21+ | number | No | Yes | Maximum line height. If the line height is scaled, the maximum line height takes effect when [TextStyle](#textstyle).heightScale is greater than 0. The value is a positive floating point number. The default value is **Number.MAX\_VALUE**. |
| lineHeightMinimum21+ | number | No | Yes | Minimum line height. If the line height is scaled, the minimum line height takes effect when [TextStyle](#textstyle).heightScale is greater than 0. The value is a non-negative floating point number. The default value is **0**. |
| lineHeightStyle21+ | [LineHeightStyle](#lineheightstyle21) | No | Yes | Scaling base style of the line height. The default value is **FONT\_SIZE**. |

#### StrutStyle

Describes the strut style, which determines the line spacing, baseline alignment mode, and other properties related to the line height when drawing texts. The strut style is disabled by default.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fontFamilies | Array<string> | No | Yes | Array of font families. By default, the array is empty, indicating that all system fonts are matched. |
| fontStyle | [FontStyle](#fontstyle) | No | Yes | Font style. The default value is **NORMAL**. |
| fontWidth | [FontWidth](#fontwidth) | No | Yes | Font width. The default value is **NORMAL**. |
| fontWeight | [FontWeight](#fontweight) | No | Yes | Font weight. The default value is **W400**. The default system font supports font weight adjustment. For other fonts, if the weight is less than W600, there is no variation in stroke thickness. If the weight is greater than or equal to W600, it might result in a fake bold effect. |
| fontSize | number | No | Yes | Font size, in units of px. The value is a floating point number. The default value is **14.0**. |
| height | number | No | Yes | Scale factor of the line height. The value is a floating point number. The default value is **1.0**. |
| leading | number | No | Yes | Custom leading to be applied to the strut. The value is a floating point number. The default value is **\-1.0**. |
| forceHeight | boolean | No | Yes | Whether to forcibly use the strut height for all lines. The value **true** means to forcibly use the strut height for all lines, and **false** means the opposite. The default value is **false**. |
| enabled | boolean | No | Yes | Whether to enable the strut style. The value **true** means to enable the strut style, and **false** means the opposite. The default value is **false**. |
| heightOverride | boolean | No | Yes | Whether to override the height. The value **true** means to override the height, and **false** means the opposite. The default value is **false**. |
| halfLeading | boolean | No | Yes | Whether half leading is enabled. Half leading is the leading split in half and applied equally to the top and bottom edges. The value **true** means that half leading is enabled, and **false** means the opposite. The default value is **false**. |

#### FontDescriptor14+

Describes the font descriptor information.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| path | string | No | Yes | Absolute path of the font. Any string that complies with the system restrictions is acceptable. The default value is an empty string. |
| postScriptName | string | No | Yes | Unique name of the font. Any string is acceptable. The default value is an empty string. |
| fullName | string | No | Yes | Font name. Any string is acceptable. The default value is an empty string. |
| fontFamily | string | No | Yes | Family name of the font. Any string is acceptable. The default value is an empty string. |
| fontSubfamily | string | No | Yes | Subfamily name of the font. Any string is acceptable. The default value is an empty string. |
| weight | [FontWeight](#fontweight) | No | Yes | Font weight. The default value is **0**. |
| width | number | No | Yes | Font width. The value is an integer ranging from 1 to 9. The default value is **0**. |
| italic | number | No | Yes | Whether the font is italic. The value **0** means that the font is not italic, and **1** means the opposite. The default value is **0**. |
| monoSpace | boolean | No | Yes | Whether the font is monospaced. The value **true** means that the font is monospaced, and **false** means the opposite. The default value is **false**. |
| symbolic | boolean | No | Yes | Whether the font is symbolic. The value **true** means that the font is symbolic, and **false** means the opposite. |

#### FontCollection

Implements a collection of fonts.

#### \[h2\]getGlobalInstance

static getGlobalInstance(): FontCollection

Obtains a global **FontCollection** instance.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| [FontCollection](#fontcollection) | **FontCollection** instance. |

**Example**

import { text } from '@kit.ArkGraphics2D'

function textFunc() {
  let fontCollection = text.FontCollection.getGlobalInstance();
}

@Entry
@Component
struct Index {
  fun: Function = textFunc;
  build() {
    Column() {
      Button().onClick(() => {
        this.fun();
      })
    }
  }
}

#### \[h2\]getLocalInstance22+

static getLocalInstance(): FontCollection

Obtains the local **FontCollection** instance. This API is recommended for widgets.

**Widget capability**: This API can be used in ArkTS widgets since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| [FontCollection](#fontcollection) | **FontCollection** instance. |

**Example**

import { text } from '@kit.ArkGraphics2D'
let fontCollection = text.FontCollection.getLocalInstance();

#### \[h2\]loadFontSync

loadFontSync(name: string, path: string | Resource): void

Loads a custom font. This API returns the result synchronously. In this API, **name** specifies the alias of the font, and the custom font effect can be displayed only when the value of **name** is set in **fontFamilies** in **[TextStyle](#textstyle)**. The supported font file formats are .ttf and .otf.

**Widget capability**: This API can be used in ArkTS widgets since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the font. |
| path | string | [Resource](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource) | Yes | Path of the font file to import. The value must be \*\*file://\*\*absolute path of the font file or \*\*rawfile/\*\*directory or file name. |

**Example**

import { text } from '@kit.ArkGraphics2D'

let fontCollection: text.FontCollection = new text.FontCollection();

@Entry
@Component
struct RenderTest {
  LoadFontSyncTest() {
    fontCollection.loadFontSync('Clock\_01', 'file:///system/fonts/HarmonyClock\_01.ttf')
    let fontFamilies: Array<string> = \["Clock\_01"\]
    let myTextStyle: text.TextStyle = {
      fontFamilies: fontFamilies
    };
    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
    }
    let paragraphBuilder: text.ParagraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    let textData = "Test loadFontSync to load the font HarmonyClock\_01.ttf."
    paragraphBuilder.addText(textData);
    let paragraph: text.Paragraph = paragraphBuilder.build();
    paragraph.layoutSync(600);
  }

  aboutToAppear() {
    this.LoadFontSyncTest();
  }

  build() {
  }
}

#### \[h2\]loadFont18+

loadFont(name: string, path: string | Resource): Promise<void>

Loads a custom font. This API uses a promise to return the result. In this API, **name** specifies the alias of the font, and the custom font effect can be displayed only when the value of **name** is set in **fontFamilies** in **[TextStyle](#textstyle)**. The supported font file formats are ttf and otf.

**Widget capability**: This API can be used in ArkTS widgets since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the font. Any string is acceptable. |
| path | string | [Resource](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource) | Yes | Path of the font file to load. The value must be \*\*file://\*\*absolute path of the font file or \*\*rawfile/\*\*directory or file name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { text } from '@kit.ArkGraphics2D'

let fontCollection: text.FontCollection = new text.FontCollection();

@Entry
@Component
struct RenderTest {
  async loadFontPromise() {
    fontCollection.loadFont('testName', 'file:///system/fonts/a.ttf').then((data) => {
      console.info(\`Succeeded in doing loadFont ${JSON.stringify(data)} \`);
    }).catch((error: Error) => {
      console.error(\`Failed to do loadFont, error: ${JSON.stringify(error)} message: ${error.message}\`);
    });
  }

  aboutToAppear() {
    this.loadFontPromise();
  }

  build() {
  }
}

#### \[h2\]unloadFontSync20+

unloadFontSync(name: string): void

Uninstalls a specified custom font. This API is synchronous.

After this API is called to unload a custom font corresponding to a font alias, the custom font is no longer available.

All layout objects that use the font alias must be destroyed and recreated.

-   Unloading a non-existent font alias does not produce any effect and does not throw an error.
-   This operation only affects future font usage.
-   Unloading a font that is currently in use may lead to text rendering exceptions (such as garbled characters or missing glyphs).

**Widget capability**: This API can be used in ArkTS widgets since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Font alias to be unregistered, which is the same as the alias used for loading the font. |

**Example**

import { text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct UnloadFontSyncTest {
  private fc: text.FontCollection = text.FontCollection.getGlobalInstance();
  @State content: string = "Default font"

  build() {
    Column({ space: 10 }) {
      Text(this.content)
        .fontFamily("custom")
      Button("load font")
        .onClick(() => {
          this.fc.loadFontSync("custom", "file:///system/fonts/NotoSansCJK-Regular.ttc")
          this.content = "Custom font"
        })
      Button("unload font")
        .onClick(() => {
          this.fc.unloadFontSync("custom")
          this.content = "Default font"
        })
    }.width("100%")
    .height("100%")
    .justifyContent(FlexAlign.Center)
  }
}

#### \[h2\]unloadFont20+

unloadFont(name: string): Promise<void>

Uninstalls a specified custom font. This API uses a promise to return the result.

After this API is called to unload a custom font corresponding to a font alias, the custom font is no longer available.

All layout objects that use the font alias must be destroyed and recreated.

-   Unloading a non-existent font alias does not produce any effect and does not throw an error.
-   This operation only affects future font usage.
-   Unloading a font that is currently in use may lead to text rendering exceptions (such as garbled characters or missing glyphs).

**Widget capability**: This API can be used in ArkTS widgets since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Alias of the font to be uninstalled, which is the same as the alias used when the font is loaded. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct UnloadFontTest {
  private fc: text.FontCollection = text.FontCollection.getGlobalInstance();
  @State content: string = "Default font"

  build() {
    Column({ space: 10 }) {
      Text(this.content)
        .fontFamily("custom")
      Button("load font")
        .onClick(async () => {
          await this.fc.loadFont("custom", "file:///system/fonts/NotoSansCJK-Regular.ttc")
          this.content = "Custom font"
        })
      Button("unload font")
        .onClick(async () => {
          await this.fc.unloadFont("custom")
          this.content = "Default font"
        })
    }.width("100%")
    .height("100%")
    .justifyContent(FlexAlign.Center)
  }
}

#### \[h2\]clearCaches

clearCaches(): void

Clears the font cache. (The font cache has a memory limit and a clearing mechanism. It occupies limited memory. You are not advised to clear it unless otherwise required.)

**Widget capability**: This API can be used in ArkTS widgets since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Example**

import { text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button().onClick(() => {
        text.FontCollection.getGlobalInstance().clearCaches();
      })
    }
  }
}

#### ParagraphStyle

Describes a paragraph style.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| textStyle | [TextStyle](#textstyle) | No | Yes | Text style applied to the paragraph. The default value is the initial text style. |
| textDirection | [TextDirection](#textdirection) | No | Yes | Text direction. The default value is **LTR**. |
| align | [TextAlign](#textalign) | No | Yes | Text alignment mode. The default value is **START**. This parameter is invalid when the **tab** parameter is configured. |
| wordBreak | [WordBreak](#wordbreak) | No | Yes | Word break type. The default value is **BREAK\_WORD**. |
| maxLines | number | No | Yes | Maximum number of lines. The value is an integer. The default value is **1e9**. |
| breakStrategy | [BreakStrategy](#breakstrategy) | No | Yes | Text break strategy. The default value is **GREEDY**. |
| strutStyle | [StrutStyle](#strutstyle) | No | Yes | Strut style. The default value is the initial **StrutStyle** object. |
| textHeightBehavior | [TextHeightBehavior](#textheightbehavior) | No | Yes | Text height modifier pattern. The default value is **ALL**. |
| tab18+ | [TextTab](#texttab18) | No | Yes | Alignment mode and position of the text after the tab character in a paragraph. By default, the tab character is replaced with a space. This parameter is invalid when it is used together with the **align** parameter or the **ellipsis** parameter in [TextStyle](#textstyle). |
| trailingSpaceOptimized20+ | boolean | No | Yes | Whether to include the trailing spaces in alignment calculations during text typography. **true** means not to include; **false** (default) means to include. |
| autoSpace20+ | boolean | No | Yes | Sets whether to enable automatic spacing during text typography. **true** indicates that the automatic spacing feature is enabled. In this case, automatic spacing applies between CJK (Chinese, Japanese, and Korean) and Western characters (Latin, Cyrillic, and Greek), between CJK and digits, between CJK and copyright symbols, between copyright symbols and digits, and between copyright symbols and Western characters. **false** (default) indicates that the automatic spacing feature is disabled. |
| verticalAlign20+ | [TextVerticalAlign](#textverticalalign20) | No | Yes | Vertical alignment of text. This parameter takes effect when line height scaling (that is, **heightScale** of [TextStyle](#textstyle)) is enabled or different font sizes (that is, **fontSize** of [TextStyle](#textstyle)) are set for text in a line. If superscript and subscript text (that is, **badgeType** of [TextStyle](#textstyle)) is set in a line, the superscript and subscript text will participate in vertical alignment as common text. |
| lineSpacing21+ | number | No | Yes | Line spacing. The default value is **0**. **lineSpacing** is not restricted by **lineHeightMaximum** and **lineHeightMinimum** in [TextStyle](#textstyle). By default, line spacing is added to the last line. You can set **textHeightBehavior** in [TextStyle](#textstyle) to **DISABLE\_ALL** or **DISABLE\_LAST\_ASCENT** to disable the line spacing of the last line. |

#### PlaceholderAlignment

Enumerates the vertical alignment modes of a placeholder relative to the surrounding text.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| OFFSET\_AT\_BASELINE | 0 | Aligns the baseline of the placeholder to the baseline of the text. |
| ABOVE\_BASELINE | 1 | Aligns the bottom edge of the placeholder to the baseline of the text. |
| BELOW\_BASELINE | 2 | Aligns the top edge of the placeholder to the baseline of the text. |
| TOP\_OF\_ROW\_BOX | 3 | Aligns the top edge of the placeholder to the top edge of the text. |
| BOTTOM\_OF\_ROW\_BOX | 4 | Aligns the bottom edge of the placeholder to the bottom edge of the text. |
| CENTER\_OF\_ROW\_BOX | 5 | Center-aligned. |
| FOLLOW\_PARAGRAPH20+ | 6 | Aligns with the text baseline. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/NgoemjeWROSIdOXKHISjhQ/en-us_image_0000002568686155.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F02B158A81BF791A1434B2FBAC23E69AB3BDE613418A2197D1213BB100841BC0)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/YeqyeiTCRfyLwddceb2rfQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B3CE6FC860E989A284479E809BF8C324AB615247A2E70FA0C7718E238754A45)

The preceding figure shows only the last three alignment modes. The first three alignment modes are similar. The only difference is that the comparison position changes to the text baseline, which is the green line shown below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/Mr0azDEVSxee_sHvy8Yo_w/en-us_image_0000002568766165.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=641134415FD5CBAB4F7F915CB7AD5F2063A65FC3AABB75F54D5184ABBAEAB1C1)

#### PlaceholderSpan

Describes the placeholder style.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | number | No | No | Width of the placeholder, in units of px. The value is a floating point number. |
| height | number | No | No | Height of the placeholder, in units of px. The value is a floating point number. |
| align | [PlaceholderAlignment](#placeholderalignment) | No | No | Vertical alignment of the placeholder relative to the surrounding text. |
| baseline | [TextBaseline](#textbaseline) | No | No | Type of the text baseline. |
| baselineOffset | number | No | No | Offset to the text baseline, in units of px. The value is a floating point number. |

#### Range

Describes a left-closed and right-open interval.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start | number | No | No | Index of the leftmost point of the interval. The value is an integer. |
| end | number | No | No | Index of the rightmost point of the interval. The value is an integer. |

#### Paragraph

Implements a carrier that stores the text content and style. You can perform operations such as layout and drawing.

Before calling any of the following APIs, you must use [build()](#build) of the [ParagraphBuilder](#paragraphbuilder) class to create a **Paragraph** object.

#### \[h2\]layoutSync

layoutSync(width: number): void

Performs layout and calculates the positions of all glyphs.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | Maximum width of a single line, in units of px. The value is a floating point number. |

**Example**

paragraph.layoutSync(100);

#### \[h2\]layout18+

layout(width: number): Promise<void>

Performs layout and calculates the positions of all glyphs. This API uses a promise to return the result.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | Maximum width of a single line, in units of px. The value is a floating point number. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { drawing, text } from '@kit.ArkGraphics2D'
import { image } from '@kit.ImageKit'

let textStyle: text.TextStyle = {
  color: {
    alpha: 255,
    red: 255,
    green: 0,
    blue: 0
  },
  fontSize: 30,
};
let paragraphStyle: text.ParagraphStyle = {
  textStyle: textStyle,
};
let fontCollection: text.FontCollection = new text.FontCollection();
let paragraphBuilder = new text.ParagraphBuilder(paragraphStyle, fontCollection);
// Add a text string.
paragraphBuilder.addText("test");
// Create a paragraph object.
let paragraph = paragraphBuilder.build();

function textFunc(pixelmap: PixelMap) {
  // Construct a canvas using an image object.
  let canvas = new drawing.Canvas(pixelmap);
  // Draw a text string.
  paragraph.paint(canvas, 100, 10);
}

@Entry
@Component
struct Index {
  @State pixelmap?: PixelMap = undefined;
  fun: Function = textFunc;

  async prepareLayoutPromise() {
    // Calculate the layout of the paragraph object.
    paragraph.layout(200).then((data) => {
      console.info(\`Succeeded in doing layout,  ${JSON.stringify(data)}\`);
    }).catch((error: Error) => {
      console.error(\`Failed to do layout, error: ${JSON.stringify(error)} message: ${error.message}\`);
    });
  }

  aboutToAppear() {
    this.prepareLayoutPromise();
  }

  build() {
    Column() {
      Image(this.pixelmap).width(200).height(200);
      Button("layout")
        .width(100)
        .height(50)
        .onClick(() => {
          const color: ArrayBuffer = new ArrayBuffer(160000);
          let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 } }
          if (this.pixelmap == undefined) {
            // Construct an image object.
            this.pixelmap = image.createPixelMapSync(color, opts);
          }
          // Draw the text.
          this.fun(this.pixelmap);
        })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/ba1S-3IgQKywLrnmRpeIJA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF0C31E1835612AF96ECE8941F52E49A8C064D33C6957E71B2D08141B7F2C836)

The following figure shows the running result of the sample code of the **layout** API after the button is tapped.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/JbHbEwVERV2nqR7kjbtmtg/en-us_image_0000002537766440.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20C8ACB49A290DC2C84F2FEBDA3CF09A1A90A96FD463A8118A347348F74A0C33)

#### \[h2\]paint

paint(canvas: drawing.Canvas, x: number, y: number): void

Paints the text on the canvas with the coordinate point (x, y) as the upper left corner.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| canvas | [drawing.Canvas](../ohos-graphics-drawing-drawing-module/class-canvas/document.md) | Yes | Target canvas. |
| x | number | Yes | X coordinate of the upper left corner. The value is a floating point number. |
| y | number | Yes | Y coordinate of the upper left corner. The value is a floating point number. |

**Example**

const color: ArrayBuffer = new ArrayBuffer(160000);
let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 } }
let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
let canvas = new drawing.Canvas(pixelMap);
paragraph.paint(canvas, 0, 0);

#### \[h2\]paintOnPath

paintOnPath(canvas: drawing.Canvas, path: drawing.Path, hOffset: number, vOffset: number): void

Draws text along a path on the canvas.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| canvas | [drawing.Canvas](../ohos-graphics-drawing-drawing-module/class-canvas/document.md) | Yes | Target canvas. |
| path | [drawing.Path](../ohos-graphics-drawing-drawing-module/class-path/document.md) | Yes | Path along which the text is drawn. |
| hOffset | number | Yes | Horizontal offset along the path direction. A positive number indicates a position that is ahead along the path from its start point, and a negative number indicates a position that is behind from the start point. |
| vOffset | number | Yes | Vertical offset along the path direction. A positive number indicates a position on the left side of the path, and a negative number indicates a position on the right side of the path. |

**Example**

const color: ArrayBuffer = new ArrayBuffer(160000);
let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 } }
let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
let canvas = new drawing.Canvas(pixelMap);
let path = new drawing.Path();
path.arcTo(20, 20, 180, 180, 180, 90);
paragraph.paintOnPath(canvas, path, 0, 0);

#### \[h2\]getMaxWidth

getMaxWidth(): number

Obtains the maximum width of the line in the text.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| number | Maximum line width, in units of px. The value is a floating point number. |

**Example**

let maxWidth = paragraph.getMaxWidth();

#### \[h2\]getHeight

getHeight(): number

Obtains the total height of the text.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| number | Total height, in units of px. The value is a floating point number. |

**Example**

let height = paragraph.getHeight();

#### \[h2\]getLongestLine

getLongestLine(): number

Obtains the longest line in the text.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| number | Longest line, in units of px. The value is a floating point number. |

**Example**

let longestLine = paragraph.getLongestLine();

#### \[h2\]getLongestLineWithIndent13+

getLongestLineWithIndent(): number

Obtains the width of the longest line, including its indentation, in the text. You are advised to round up the return value. If the text content is empty, **0** is returned.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| number | Width of the longest line, including its indentation. The value is a floating point number, in px. |

**Example**

let longestLineWithIndent = paragraph.getLongestLineWithIndent();

#### \[h2\]getMinIntrinsicWidth

getMinIntrinsicWidth(): number

Obtains the minimum intrinsic width of the paragraph.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| number | Minimum intrinsic width, in units of px. The value is a floating point number. |

**Example**

let minIntrinsicWidth = paragraph.getMinIntrinsicWidth();

#### \[h2\]getMaxIntrinsicWidth

getMaxIntrinsicWidth(): number

Obtains the maximum intrinsic width of the paragraph.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| number | Maximum intrinsic width, in units of px. The value is a floating point number. |

**Example**

let maxIntrinsicWidth = paragraph.getMaxIntrinsicWidth();

#### \[h2\]getAlphabeticBaseline

getAlphabeticBaseline(): number

Obtains the alphabetic baseline.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| number | Alphabetic baseline, in units of px. The value is a floating point number. |

**Example**

let alphabeticBaseline = paragraph.getAlphabeticBaseline();

#### \[h2\]getIdeographicBaseline

getIdeographicBaseline(): number

Obtains the ideographic baseline.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| number | Ideographic baseline, in units of px. The value is a floating point number. |

**Example**

let ideographicBaseline = paragraph.getIdeographicBaseline();

#### \[h2\]getRectsForRange

getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>

Obtains the rectangles occupied by the characters in the range of the text under the given rectangle width and height.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| range | [Range](#range) | Yes | Range of the text. |
| widthStyle | [RectWidthStyle](#rectwidthstyle) | Yes | Width of the rectangle. |
| heightStyle | [RectHeightStyle](#rectheightstyle) | Yes | Height of the rectangle. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[TextBox](#textbox)\> | Array holding the rectangles obtained. |

**Example**

let range: text.Range = { start: 0, end: 1};
let rects = paragraph.getRectsForRange(range, text.RectWidthStyle.TIGHT, text.RectHeightStyle.TIGHT);

#### \[h2\]getRectsForPlaceholders

getRectsForPlaceholders(): Array<TextBox>

Obtains the rectangles occupied by all placeholders in the text.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[TextBox](#textbox)\> | Array holding the rectangles obtained. |

**Example**

let placeholderRects = paragraph.getRectsForPlaceholders();

#### \[h2\]getGlyphPositionAtCoordinate

getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity

Obtains the position of a glyph closest to the given coordinates.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | X coordinate. The value is a floating point number. |
| y | number | Yes | Y coordinate. The value is a floating point number. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PositionWithAffinity](#positionwithaffinity) | Position of the glyph. |

**Example**

let positionWithAffinity = paragraph.getGlyphPositionAtCoordinate(0, 0);

#### \[h2\]getWordBoundary

getWordBoundary(offset: number): Range

Obtains the range of the word where the glyph with a given offset is located.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| offset | number | Yes | Offset of the glyph. The value is an integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Range](#range) | Range of the word. |

**Example**

let wordRange = paragraph.getWordBoundary(0);

#### \[h2\]getLineCount

getLineCount(): number

Obtains the number of text lines.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of text lines. The value is an integer. |

**Example**

let lineCount = paragraph.getLineCount();

#### \[h2\]getLineHeight

getLineHeight(line: number): number

Obtains the height of a given line.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| line | number | Yes | Index of the line. The value is an integer ranging from 0 to getLineCount() – 1. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Line height. |

**Example**

let lineHeight = paragraph.getLineHeight(0);

#### \[h2\]getLineWidth

getLineWidth(line: number): number

Obtains the width of a given line.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| line | number | Yes | Index of the line. The value is an integer ranging from 0 to getLineCount() – 1. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Line width. |

**Example**

let lineWidth = paragraph.getLineWidth(0);

#### \[h2\]didExceedMaxLines

didExceedMaxLines(): boolean

Checks whether the number of lines in the paragraph exceeds the maximum.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** means that the number of lines exceeds the maximum, and **false** means the opposite. |

**Example**

let didExceed = paragraph.didExceedMaxLines();

#### \[h2\]getTextLines

getTextLines(): Array<TextLine>

Obtains all the text lines.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[TextLine](#textline)\> | Array of text lines. |

**Example**

let lines = paragraph.getTextLines();

#### \[h2\]getActualTextRange

getActualTextRange(lineNumber: number, includeSpaces: boolean): Range

Obtains the actually visible text range in the specified line, excluding any overflow ellipsis.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| lineNumber | number | Yes | Line number of the text range, starting from 0. This API can only be used to obtain the bounds of existing lines. That is, the line number must start from 0, and the maximum line number is [getLineCount](#getlinecount) - 1. |
| includeSpaces | boolean | Yes | Whether spaces are included. The value **true** means that spaces are contained, and **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Range](#range) | Text range obtained. If the line index is invalid, **start** and **end** are both 0. |

**Example**

let rang = paragraph.getActualTextRange(0, true);

#### \[h2\]getLineMetrics

getLineMetrics(): Array<LineMetrics>

Obtains an array of line measurement information.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[LineMetrics](#linemetrics)\> | Array of line measurement information. |

**Example**

let arrLineMetric =  paragraph.getLineMetrics();

#### \[h2\]getLineMetrics

getLineMetrics(lineNumber: number): LineMetrics | undefined

Obtains the line measurement information of a line.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| lineNumber | number | Yes | Line number, starting from 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| [LineMetrics](#linemetrics) | undefined | **LineMetrics** object containing the measurement information if the specified line number is valid and the measurement information exists. If the line number is invalid or the measurement information cannot be obtained, **undefined** is returned. |

**Example**

let lineMetrics =  paragraph.getLineMetrics(0);

#### \[h2\]updateColor20+

updateColor(color: common2D.Color): void;

Updates the color of the entire text span. This API call also updates the decoration color if it hasn't been set yet.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [common2D.Color](../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#color) | Yes | Updated font color. |

**Example**

paragraph.updateColor({ alpha: 255, red: 255, green: 0, blue: 0 });

#### \[h2\]updateDecoration20+

updateDecoration(decoration: Decoration): void;

Updates the decoration line of the entire text span.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| decoration | [Decoration](#decoration) | Yes | Updated decoration line. |

**Example**

paragraph.updateDecoration({
  textDecoration: text.TextDecorationType.OVERLINE,
  color: { alpha: 255, red: 255, green: 0, blue: 0 },
  decorationStyle: text.TextDecorationStyle.WAVY,
  decorationThicknessScale: 2.0,
});

#### LineTypeset18+

Implements a carrier that stores the text content and style. It can be used to compute layout details for individual lines of text.

Before calling any of the following APIs, you must use [buildLineTypeset()](#buildlinetypeset18) in the [ParagraphBuilder](#paragraphbuilder) class to create a **LineTypeset** object.

#### \[h2\]getLineBreak18+

getLineBreak(startIndex: number, width: number): number

Obtains the number of characters that can fit in the layout from the specified position within a limited width.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| startIndex | number | Yes | Start position (inclusive) for calculation. The value is an integer in the range \[0, total number of text characters). If the parameter is invalid, an exception is thrown. |
| width | number | Yes | Layout width. The value is a floating point number greater than 0, in px. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of characters. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3. Parameter verification failed. |

**Example**

let startIndex = 0;
let width = 100.0;
let count = lineTypeset.getLineBreak(startIndex, width);

#### \[h2\]createLine18+

createLine(startIndex: number, count: number): TextLine

Generates a text line object based on the specified layout range.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| startIndex | number | Yes | Start position for layout calculation. The value is an integer in the range \[0, total number of text characters). |
| count | number | Yes | Number of characters from the specified start position. The value is an integer in the range \[0, total number of text characters). The sum of **startIndex** and **count** cannot be greater than the total number of text characters. When **count** is **0**, the range is \[startIndex, end of the text\]. You can use [getLineBreak](#getlinebreak18) to obtain the number of characters that can fit in the layout. |

**Return value**

| Type | Description |
| :-- | :-- |
| [TextLine](#textline) | **TextLine** object generated based on the characters in the text range. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3. Parameter verification failed. |

**Example**

let startIndex = 0;
let width = 100.0;
let count = lineTypeset.getLineBreak(startIndex, width);
let line : text.TextLine = lineTypeset.createLine(startIndex, count);

#### RunMetrics

Describes the layout information and measurement information of a run of text in a text line.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| textStyle | [TextStyle](#textstyle) | No | No | Text style. |
| fontMetrics | [drawing.FontMetrics](../ohos-graphics-drawing-drawing-module/interfaces-others/document.md#fontmetrics) | No | No | Font measurement information. |

#### LineMetrics

Describes the measurement information of a single line of text in the text layout.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| startIndex | number | No | No | Start index of the line in the text buffer. |
| endIndex | number | No | No | End index of the line in the text buffer. |
| ascent | number | No | No | Ascent, that is, the distance from the baseline to the top of the character. |
| descent | number | No | No | Descent, that is, the distance from the baseline to the bottom of the character. |
| height | number | No | No | Height of the line, which is Math.round(ascent + descent). |
| width | number | No | No | Width of the line. |
| left | number | No | No | Left edge of the line. The right edge is the value of **left** plus the value of **width**. |
| baseline | number | No | No | Y coordinate of the baseline in the line relative to the top of the paragraph. |
| lineNumber | number | No | No | Line number, starting from 0. |
| topHeight | number | No | No | Height from the top to the current line. |
| runMetrics | Map<number, [RunMetrics](#runmetrics)\> | No | No | Mapping between the text index range and the associated font measurement information. |

#### TextBox

Describes the rectangle that holds the text.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| rect | [common2D.Rect](../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#rect) | No | No | Information about the rectangle. |
| direction | [TextDirection](#textdirection) | No | No | Text direction. |

#### PositionWithAffinity

Describes the position and affinity of a glyph.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| position | number | No | No | Index of the glyph relative to the paragraph. The value is an integer. |
| affinity | [Affinity](#affinity) | No | No | Affinity of the position. |

#### RectWidthStyle

Enumerates the rectangle width styles.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| TIGHT | 0 | If **letterSpacing** is not set, the rectangle conforms tightly to the text it contains. However, if **letterSpacing** is set, a gap is introduced between the rectangle and text. |
| MAX | 1 | The rectangle's width is extended to align with the widest rectangle across all lines. |

#### RectHeightStyle

Enumerates the rectangle height styles.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| TIGHT | 0 | Tight style. |
| MAX | 1 | Extends the height to match the highest rectangle in all lines. |
| INCLUDE\_LINE\_SPACE\_MIDDLE | 2 | Includes half of the line spacing to both the top and bottom of the rectangle. |
| INCLUDE\_LINE\_SPACE\_TOP | 3 | Includes the line spacing to the top of the rectangle. |
| INCLUDE\_LINE\_SPACE\_BOTTOM | 4 | Includes the line spacing to the bottom of the rectangle. |
| STRUT | 5 | Sets the height according to the strut style. |

#### Affinity

Enumerates the affinity modes.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| UPSTREAM | 0 | The position has affinity for the upstream side of the text position. |
| DOWNSTREAM | 1 | The position has affinity for the downstream side of the text position. |

#### ParagraphBuilder

Implements a paragraph builder.

#### \[h2\]constructor

constructor(paragraphStyle: ParagraphStyle, fontCollection: FontCollection)

A constructor used to create a **ParagraphBuilder** object.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| paragraphStyle | [ParagraphStyle](#paragraphstyle) | Yes | Paragraph style. |
| fontCollection | [FontCollection](#fontcollection) | Yes | Font collection. |

**Example**

import { text } from '@kit.ArkGraphics2D'

function textFunc() {
  let myTextStyle: text.TextStyle = {
    color: { alpha: 255, red: 255, green: 0, blue: 0 },
    fontSize: 33,
  };
  let myParagraphStyle: text.ParagraphStyle = {
    textStyle: myTextStyle,
    align: text.TextAlign.END,
  };
  let fontCollection = new text.FontCollection();
  let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
}

@Entry
@Component
struct Index {
  fun: Function = textFunc;
  build() {
    Column() {
      Button().onClick(() => {
        this.fun();
      })
    }
  }
}

#### \[h2\]pushStyle

pushStyle(textStyle: TextStyle): void

Applies a new style to the current text blob.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/bQX0bAs9TTijUwEEDV8prA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3219CD56D539031DCFEDD89448E0D51D69E2AC36FC4ABBBEE7AA5C4986D6BB09)

When you update the style of the current text blob, all text added afterward will use this new style.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| textStyle | [TextStyle](#textstyle) | Yes | Text style, which describes various visual attributes of text, such as font, font size, color, font weight, word spacing, line spacing, decoration (such as underline and strikethrough), and text shadow. |

**Example**

import { drawing } from '@kit.ArkGraphics2D'
import { text } from '@kit.ArkGraphics2D'
import { common2D } from '@kit.ArkGraphics2D'
import { image } from '@kit.ImageKit'

function textFunc() {
  let myTextStyle: text.TextStyle = {
    color: { alpha: 255, red: 255, green: 0, blue: 0 },
    fontSize: 33,
  };
  let myParagraphStyle: text.ParagraphStyle = {
    textStyle: myTextStyle,
    align: text.TextAlign.CENTER,
  };
  let fontCollection = new text.FontCollection();
  let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
  paragraphBuilder.pushStyle(myTextStyle);
}

@Entry
@Component
struct Index {
  fun: Function = textFunc;
  build() {
    Column() {
      Button().onClick(() => {
        this.fun();
      })
    }
  }
}

#### \[h2\]popStyle

popStyle(): void

Restores the previous text style.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Example**

import { drawing } from '@kit.ArkGraphics2D'
import { text } from '@kit.ArkGraphics2D'
import { common2D } from '@kit.ArkGraphics2D'
import { image } from '@kit.ImageKit'

function textFunc() {
  let myTextStyle: text.TextStyle = {
    color: { alpha: 255, red: 255, green: 0, blue: 0 },
    fontSize: 33,
  };
  let myParagraphStyle: text.ParagraphStyle = {
    textStyle: myTextStyle,
    align: text.TextAlign.END,
  };
  let fontCollection = new text.FontCollection();
  let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
  paragraphBuilder.pushStyle(myTextStyle);
  paragraphBuilder.popStyle();
}

@Entry
@Component
struct Index {
  fun: Function = textFunc;
  build() {
    Column() {
      Button().onClick(() => {
        this.fun();
      })
    }
  }
}

#### \[h2\]addText

addText(text: string): void

Inserts a text string into the paragraph being built.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Exact text string inserted into the paragraph. If an invalid Unicode character is provided, it is displayed as �. |

**Example**

import { drawing } from '@kit.ArkGraphics2D'
import { text } from '@kit.ArkGraphics2D'
import { common2D } from '@kit.ArkGraphics2D'
import { image } from '@kit.ImageKit'

function textFunc() {
  let myTextStyle: text.TextStyle = {
    color: { alpha: 255, red: 255, green: 0, blue: 0 },
    fontSize: 33,
  };
  let myParagraphStyle: text.ParagraphStyle = {
    textStyle: myTextStyle,
    align: text.TextAlign.END,
  };
  let fontCollection = new text.FontCollection();
  let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
  paragraphBuilder.addText("123666");
}

@Entry
@Component
struct Index {
  fun: Function = textFunc;
  build() {
    Column() {
      Button().onClick(() => {
        this.fun();
      })
    }
  }
}

#### \[h2\]addPlaceholder

addPlaceholder(placeholderSpan: PlaceholderSpan): void

Inserts a placeholder into the paragraph being built.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| placeholderSpan | [PlaceholderSpan](#placeholderspan) | Yes | Placeholder span, which describes the size, alignment, baseline type, and baseline offset of the placeholder. |

**Example**

import { drawing } from '@kit.ArkGraphics2D'
import { text } from '@kit.ArkGraphics2D'
import { common2D } from '@kit.ArkGraphics2D'
import { image } from '@kit.ImageKit'

function textFunc() {
  let myParagraphStyle: text.ParagraphStyle = {
    align: text.TextAlign.END,
  };
  let myPlaceholderSpan: text.PlaceholderSpan = {
    width: 100,
    height: 100,
    align: text.PlaceholderAlignment.ABOVE\_BASELINE,
    baseline: text.TextBaseline.ALPHABETIC,
    baselineOffset: 100
  };
  let fontCollection = new text.FontCollection();
  let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
  paragraphBuilder.addPlaceholder(myPlaceholderSpan);
}

@Entry
@Component
struct Index {
  fun: Function = textFunc;
  build() {
    Column() {
      Button().onClick(() => {
        this.fun();
      })
    }
  }
}

#### \[h2\]build

build(): Paragraph

Creates a paragraph object that can be used for subsequent layout and rendering.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| [Paragraph](#paragraph) | **Paragraph** object that can be used for subsequent rendering. |

**Example**

import { drawing, text, common2D } from '@kit.ArkGraphics2D'
import { image } from '@kit.ImageKit'

function textFunc() {
  let myTextStyle: text.TextStyle = {
    color : {alpha: 255, red: 255, green: 0, blue: 0},
    fontSize : 20,
  };
  let myParagraphStyle: text.ParagraphStyle = {
    textStyle : myTextStyle,
  };
  let fontCollection = new text.FontCollection();
  let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
  paragraphBuilder.addText("123456789");
  let paragraph = paragraphBuilder.build();
  paragraph.layoutSync(200);
}

@Entry
@Component
struct Index {
  fun: Function = textFunc;
  build() {
    Column() {
      Button().onClick(() => {
        this.fun();
      })
    }
  }
}

#### \[h2\]buildLineTypeset18+

buildLineTypeset(): LineTypeset

Builds a line typesetter.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| [LineTypeset](#linetypeset18) | **LineTypeset** object that can be used for subsequent rendering. |

**Example**

import { text } from '@kit.ArkGraphics2D'

function test() {
  let myParagraphStyle: text.ParagraphStyle = {
    align: text.TextAlign.JUSTIFY,
  };
  let fontCollection = new text.FontCollection();
  let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
  paragraphBuilder.addText("123456789");
  let lineTypeset = paragraphBuilder.buildLineTypeset();
}

@Entry
@Component
struct Index {
  fun: Function = test;
  build() {
    Column() {
      Button().onClick(() => {
        this.fun();
      })
    }
  }
}

#### \[h2\]addSymbol

addSymbol(symbolId: number): void

Inserts a symbol into the paragraph being built.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| symbolId | number | Yes | Symbol code to insert. The value is a hexadecimal number in the range 0xF0000-0xF0C97. For details about the configurable symbol codes (unicode values in the list view), see [HarmonyOS Symbol](https://developer.huawei.com/consumer/en/design/harmonyos-symbol/). |

**Example**

import { text } from '@kit.ArkGraphics2D'

function textFunc() {
  let myTextStyle: text.TextStyle = {
    color: { alpha: 255, red: 255, green: 0, blue: 0 },
    fontSize: 33,
  };
  let myParagraphStyle: text.ParagraphStyle = {
    textStyle: myTextStyle,
    align: text.TextAlign.END,
  };
  let fontCollection = new text.FontCollection();
  let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
  paragraphBuilder.addSymbol(0xF0000);
  let paragraph = paragraphBuilder.build();
}

@Entry
@Component
struct Index {
  fun: Function = textFunc;
  build() {
    Column() {
      Button().onClick(() => {
        this.fun();
      })
    }
  }
}

#### TypographicBounds18+

Describes the typographic boundaries of a text line. These boundaries depend on the typographic font and font size, not on the characters themselves. For example, for the string " a b " (which has a space before "a" and a space after "b"), the typographic boundaries include the spaces at the beginning and end of the line. Similarly, the strings "j" and "E" have identical typographic boundaries, which are independent of the characters themselves.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ascent | number | No | No | Ascent of a text line. The value is a floating point number. |
| descent | number | No | No | Descent of a text line. The value is a floating point number. |
| leading | number | No | No | Leading of a text line. The value is a floating point number. |
| width | number | No | No | Width of the typographic boundaries. The value is a floating point number. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/VJow0fp1QyauLxKrsW1H5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0309FDE9B07F217605C0A52F16596E0D9E3C83A2D89F4155906CEA2EE8F9CCBE)

The following figure shows the meanings of ascent, descent, leading, top, baseline, bottom and next line top, where **width** is the width of the text line, including the left and right spaces; **ascent** is the highest point that the text line reaches upward; **descent** is the lowest point that the text line reaches downward; **leading** is the space between lines of text; **top** is the very highest point of the text line; **baseline** is where the characters sit; **bottom** is the lowest point of the text line; **next line top** is the highest point of the next text line.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/2flnUptCSoqDCPxEA1GjVg/en-us_image_0000002537926380.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A4DF7945EB47FDF5F2A7144A560002504C6EF86A1C85DC22DB1581D542B0F13)

The following figure shows the typographic boundaries of the string " a b ".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/TWFkrFEdQUiUzOscqrFIeQ/en-us_image_0000002568686157.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C207D41E14454D6B7A0DBC014800E5B86DD9AC834E8C232F2AE0C4A4529665E)

The following figure shows the typographic boundaries of the strings "j" and "E".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/oDRMk9Z7S-e9xWUru0TYWg/en-us_image_0000002568766167.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C44FB754B2C63E987C350D49DCD330B1A02D9185B1EBD68350023958C14DFE7E)

#### CaretOffsetsCallback18+

type CaretOffsetsCallback = (offset: number, index: number, leadingEdge: boolean) => boolean

Defines the callback used to receive the offset and index of each character in a text line object as its parameters.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| offset | number | Yes | Offset of each character in a text line. The value is a floating point number. |
| index | number | Yes | Index of each character in a text line. The value is an integer. |
| leadingEdge | boolean | Yes | Whether the cursor is located at the front of the character. The value **true** means that the cursor is located at the front of the character, that is, the offset does not contain the character width. The value **false** means that the cursor is located at the rear of the character, that is, the offset contains the character width. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether to stop calling the callback. The value **true** means to stop calling the callback, and **false** means to continue calling the callback. |

#### TextLine

Implements a carrier that describes the basic text line structure of a paragraph.

Before calling any of the following APIs, you must use [getTextLines()](#gettextlines) of the [Paragraph](#paragraph) class or [createLine()](#createline18) of the [LineTypeset](#linetypeset18) class to create a **TextLine** object.

#### \[h2\]getGlyphCount

getGlyphCount(): number

Obtains the number of glyphs in this text line.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of glyphs. The value is an integer. |

**Example**

let glyphCount = lines\[0\].getGlyphCount();

#### \[h2\]getTextRange

getTextRange(): Range

Obtains the range of the text in this text line in the entire paragraph.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| [Range](#range) | Range of the text in this text line in the entire paragraph. |

**Example**

let textRange = lines\[0\].getTextRange();

#### \[h2\]getGlyphRuns

getGlyphRuns(): Array<Run>

Obtains the array of glyph runs in the text line.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[Run](#run)\> | Array of the runs obtained. |

**Example**

let runs = lines\[0\].getGlyphRuns();

#### \[h2\]paint

paint(canvas: drawing.Canvas, x: number, y: number): void

Paints this text line on the canvas with the coordinate point (x, y) as the upper left corner.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| canvas | [drawing.Canvas](../ohos-graphics-drawing-drawing-module/class-canvas/document.md) | Yes | Target canvas. |
| x | number | Yes | X coordinate of the upper left corner. The value is a floating point number. |
| y | number | Yes | Y coordinate of the upper left corner. The value is a floating point number. |

**Example**

import { drawing } from '@kit.ArkGraphics2D'
import { text } from '@kit.ArkGraphics2D'
import { common2D } from '@kit.ArkGraphics2D'
import { image } from '@kit.ImageKit'

function textFunc(pixelmap: PixelMap) {
  let canvas = new drawing.Canvas(pixelmap);
  lines\[0\].paint(canvas, 0, 0);
}

@Entry
@Component
struct Index {
  @State pixelmap?: PixelMap = undefined;
  fun: Function = textFunc;
  build() {
    Column() {
      Image(this.pixelmap).width(200).height(200);
      Button().onClick(() => {
        if (this.pixelmap == undefined) {
          const color: ArrayBuffer = new ArrayBuffer(160000);
          let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 } }
          this.pixelmap = image.createPixelMapSync(color, opts);
        }
        this.fun(this.pixelmap);
      })
    }
  }
}

#### \[h2\]createTruncatedLine18+

createTruncatedLine(width: number, ellipsisMode: EllipsisMode, ellipsis: string): TextLine

Creates a truncated text line object.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | Width of the line after truncation. The value is a floating point number. |
| ellipsisMode | [EllipsisMode](#ellipsismode) | Yes | Ellipsis mode. Currently, only **START** and **END** are supported. |
| ellipsis | string | Yes | String used to mark a truncation. |

**Return value**

| Type | Description |
| :-- | :-- |
| [TextLine](#textline) | Truncated text line object. |

**Example**

import { drawing, text, common2D } from '@kit.ArkGraphics2D'
import { image } from '@kit.ImageKit'

function textFunc(pixelmap: PixelMap) {
  let canvas = new drawing.Canvas(pixelmap);
  let truncatedTextLine = lines\[0\].createTruncatedLine(100, text.EllipsisMode.START, "...");
  truncatedTextLine.paint(canvas, 0, 100);
}

@Entry
@Component
struct Index {
  @State pixelmap?: PixelMap = undefined;
  fun: Function = textFunc;
  build() {
    Column() {
      Image(this.pixelmap).width(200).height(200);
      Button().onClick(() => {
        if (this.pixelmap == undefined) {
          const color: ArrayBuffer = new ArrayBuffer(160000);
          let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 } }
          this.pixelmap = image.createPixelMapSync(color, opts);
        }
        this.fun(this.pixelmap);
      })
    }
  }
}

#### \[h2\]getTypographicBounds18+

getTypographicBounds(): TypographicBounds

Obtains the typographic boundaries of this text line. These boundaries depend on the typographic font and font size, but not on the characters themselves. For example, for the string " a b " (which has a space before "a" and a space after "b"), the typographic boundaries include the spaces at the beginning and end of the line. Similarly, the strings "j" and "E" have identical typographic boundaries, which are independent of the characters themselves.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/6_ytz27mQxqj3G_m9HCpVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12AC81AAE8B09B42167662C3EB3FCCE71AB644AE432A558014644CBCC6C98253)

The following figure shows the typographic boundaries of the string " a b ".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/D0C5-GL7Qc-jz07XrOXiVQ/en-us_image_0000002568686157.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE5A43E73FDE25B7C0A631FA2947B92261336264AA49DD9E0102548A8D7348AE)

The following figure shows the typographic boundaries of the strings "j" and "E".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/eLA9LpOLRfGPW9InHTqxRw/en-us_image_0000002568766167.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=402F3E29C36B91DEA901930667D38B9264F6D50DD8DD2DD47DCA91A9CCECF278)

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| [TypographicBounds](#typographicbounds18) | Describes the typographic boundaries of a text line. |

**Example**

let bounds = lines\[0\].getTypographicBounds();
console.info('textLine ascent:' + bounds.ascent + ', descent:' + bounds.descent + ', leading:' + bounds.leading + ', width:' + bounds.width);

#### \[h2\]getImageBounds18+

getImageBounds(): common2D.Rect

Obtains the image boundaries of this text line. The image boundaries, equivalent to visual boundaries, depend on the font, font size, and characters. For example, for the string " a b " (which has a space before "a" and a space after "b"), only "a b" are visible to users, and therefore the image boundaries do not include these spaces at the beginning and end of the line. For the strings "j" and "E", their image boundaries are different. Specifically, the width of the boundary for "j" is narrower than that for "E", and the height of the boundary for "j" is taller than that for "E".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/f2II07JpTiufUIkRz7CQbg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9BFC88B6B5BB46A3ED92AA4DCED252BE5363178C096C5AB8CA2F20745A9D4A22)

The following figure shows the image boundaries of the string " a b ".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/Hzbzh3qxQ4qB9ZulcTwf9g/en-us_image_0000002537766442.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82EF63E7D3ED7150E3B5810E49A31623D576B02BA3CB50033FFC75E85ED5260E)

The following figure shows the image boundaries of the strings "j" and "E".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/K2BLBnagTRGy4FaUwsUJXQ/en-us_image_0000002537926382.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EDFC8A2F724531D54715EF0399881570BE22F6ED5CD8A153DF80D047D7F0B0D9)

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| [common2D.Rect](../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#rect) | Image boundary of the text line. |

**Example**

let imageBounds = lines\[0\].getImageBounds();

#### \[h2\]getTrailingSpaceWidth18+

getTrailingSpaceWidth(): number

Obtains the width of the spaces at the end of this text line.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of spaces at the end of the text line. The value is a floating point number. |

**Example**

let trailingSpaceWidth = lines\[0\].getTrailingSpaceWidth();

#### \[h2\]getStringIndexForPosition18+

getStringIndexForPosition(point: common2D.Point): number

Obtains the index of a character at the specified position in the original string.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| point | [common2D.Point](../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#point12) | Yes | Position of the character. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Index of the character in the text line. The value is an integer. |

**Example**

let point : common2D.Point = { x: 15.0, y: 2.0 };
let index = lines\[0\].getStringIndexForPosition(point);

#### \[h2\]getOffsetForStringIndex18+

getOffsetForStringIndex(index: number): number

Obtains the offset of a character with the specified index in this text line.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the character. The value is an integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Offset of the character with the specified index. The value is a floating point number. |

**Example**

let offset = lines\[0\].getOffsetForStringIndex(3);

#### \[h2\]enumerateCaretOffsets18+

enumerateCaretOffsets(callback: CaretOffsetsCallback): void

Enumerates the offset and index of each character in a text line.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [CaretOffsetsCallback](#caretoffsetscallback18) | Yes | Custom function, which contains the offset and index of each character in the text line. |

**Example**

function callback(offset: number, index: number, leadingEdge: boolean): boolean {
  console.info('textLine: offset: ' + offset + ', index: ' + index + ', leadingEdge: ' + leadingEdge);
  return index > 50;
}
lines\[0\].enumerateCaretOffsets(callback);

#### \[h2\]getAlignmentOffset18+

getAlignmentOffset(alignmentFactor: number, alignmentWidth: number): number

Obtains the offset of this text line after alignment based on the alignment factor and alignment width.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| alignmentFactor | number | Yes | Alignment factor, which determines how text is aligned. The value is a floating point number. A value less than or equal to 0.0 means that the text is left-aligned; a value between 0.0 and 0.5 means that the text is slightly left-aligned; the value 0.5 means that the text is centered; a value between 0.5 and 1 means that the text is slightly right-aligned; a value greater than or equal to 1.0 means that the text is right-aligned. |
| alignmentWidth | number | Yes | Alignment width, that is, the width of the text line. The value is a floating point number. If the width is less than the actual width of the text line, **0** is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Offset required for alignment. The value is a floating point number. |

**Example**

let alignmentOffset = lines\[0\].getAlignmentOffset(0.5, 500);

#### Run

Implements a unit for text layout.

Before calling any of the following APIs, you must use [getGlyphRuns()](#getglyphruns) of the [TextLine](#textline) class to create a **Run** object.

#### \[h2\]getGlyphCount

getGlyphCount(): number

Obtains the number of glyphs in this run.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of glyphs. The value is an integer. |

**Example**

let glyphs = runs\[0\].getGlyphCount();

#### \[h2\]getGlyphs

getGlyphs(): Array<number>

Obtains the index of each glyph in this run.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| Array<number> | Array holding the index of each glyph in the run. |

**Example**

let glyph = runs\[0\].getGlyphs();

#### \[h2\]getGlyphs18+

getGlyphs(range: Range): Array<number>

Obtains the index of each glyph in the specified range of this run.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| range | [Range](#range) | Yes | Range of the glyphs, where **range.start** indicates the start position of the range, and **range.end** indicates the length of the range. If the length is 0, the range is from **range.start** to the end of the run. If **range.end** or **range.start** is set to a negative value, **null**, or **undefined**, **undefined** is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<number> | Array holding the index of each glyph in the run. |

**Example**

import { text } from '@kit.ArkGraphics2D'

function textFunc() {
  let glyphs = runs\[0\].getGlyphs(); // Obtain the index of all glyphs of the run.
  let glyphsRange = runs\[0\].getGlyphs ({start:1, end:2}); // Obtain the indices of glyphs in the range starting from position 1, with a length of 2.
  glyphsRange = runs\[0\].getGlyphs({start:-1, end:2}); // -1 is an invalid value, and undefined is returned.
  glyphsRange = runs\[0\].getGlyphs({start:0, end:-10}); // -10 is an invalid value, and undefined is returned.
  let glyphsNull = runs\[0\].getGlyphs(null); // null is an invalid value, and undefined is returned.
  let glyphsUndefined = runs\[0\].getGlyphs(undefined); // undefined is an invalid value, and undefined is returned.
}

@Entry
@Component
struct Index {
  fun: Function = textFunc;
  build() {
    Column() {
      Button().onClick(() => {
        this.fun();
      })
    }
  }
}

#### \[h2\]getPositions

getPositions(): Array<common2D.Point>

Obtains the position of each glyph relative to the respective line in this run.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[common2D.Point](../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#point12)\> | Array holding the position of each glyph relative to the respective line in the run. |

**Example**

let positions = runs\[0\].getPositions();

#### \[h2\]getPositions18+

getPositions(range: Range): Array<common2D.Point>

Obtains the position array of each glyph relative to the respective line within the specified range of this run.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| range | [Range](#range) | Yes | Range of the glyphs, where **range.start** indicates the start position of the range, and **range.end** indicates the length of the range. If the length is 0, the range is from **range.start** to the end of the run. If **range.end** or **range.start** is set to a negative value, **null**, or **undefined**, **undefined** is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[common2D.Point](../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#point12)\> | Array holding the position of each glyph relative to the respective line in the run. |

**Example**

import { text } from '@kit.ArkGraphics2D'

function textFunc() {
  let positions = runs\[0\].getPositions(); // Obtain the positions of all glyphs in the run.
  let positionsRange = runs\[0\].getPositions({start:1, end:2}); // Obtain the positions of glyphs in the range starting from position 1, with a length of 2.
  positionsRange = runs\[0\].getPositions({start:-1, end:2}); // -1 is an invalid value, and undefined is returned.
  positionsRange = runs\[0\].getPositions({start:0, end:-10}); // -10 is an invalid value, and undefined is returned.
  let positionsNull = runs\[0\].getPositions(null); // null is an invalid value, and undefined is returned.
  let positionsUndefined = runs\[0\].getPositions(undefined); // undefined is an invalid value, and undefined is returned.
}

@Entry
@Component
struct Index {
  fun: Function = textFunc;
  build() {
    Column() {
      Button().onClick(() => {
        this.fun();
      })
    }
  }
}

#### \[h2\]getOffsets

getOffsets(): Array<common2D.Point>

Obtains the offset of each glyph in this run relative to its index.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[common2D.Point](../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#point12)\> | Array holding the offset of each glyph in the run relative to its index. |

**Example**

let offsets = runs\[0\].getOffsets();

#### \[h2\]getFont

getFont(): drawing.Font

Obtains the **Font** object of this run.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| [drawing.Font](../ohos-graphics-drawing-drawing-module/class-font/document.md) | **Font** object of this run. |

**Example**

let font = runs\[0\].getFont();

#### \[h2\]paint

paint(canvas: drawing.Canvas, x: number, y: number): void

Paints this run on the canvas with the coordinate point (x, y) as the upper left corner.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| canvas | [drawing.Canvas](../ohos-graphics-drawing-drawing-module/class-canvas/document.md) | Yes | Target canvas. |
| x | number | Yes | X coordinate of the upper left corner. The value is a floating point number. |
| y | number | Yes | Y coordinate of the upper left corner. The value is a floating point number. |

**Example**

import { drawing } from '@kit.ArkGraphics2D'
import { text } from '@kit.ArkGraphics2D'
import { common2D } from '@kit.ArkGraphics2D'
import { image } from '@kit.ImageKit'

function textFunc(pixelmap: PixelMap) {
  let canvas = new drawing.Canvas(pixelmap);
  runs\[0\].paint(canvas, 0, 0);
}

@Entry
@Component
struct Index {
  @State pixelmap?: PixelMap = undefined;
  fun: Function = textFunc;
  build() {
    Column() {
      Image(this.pixelmap).width(200).height(200);
      Button().onClick(() => {
        if (this.pixelmap == undefined) {
          const color: ArrayBuffer = new ArrayBuffer(160000);
          let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 } }
          this.pixelmap = image.createPixelMapSync(color, opts);
        }
        this.fun(this.pixelmap);
      })
    }
  }
}

#### \[h2\]getStringRange18+

getStringRange(): Range

Obtains the range of glyphs generated by this run.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| [Range](#range) | Range of the glyphs, where **start** indicates the start position of the range, which is the index relative to the entire paragraph, and **end** indicates the length of the range. |

**Example**

let runStringRange = runs\[0\].getStringRange();
let location = runStringRange.start;
let length = runStringRange.end;

#### \[h2\]getStringIndices18+

getStringIndices(range?: Range): Array<number>

Obtains an array of character indices for glyphs within a specified range of this run, where the indices are offsets relative to the entire paragraph.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| range | [Range](#range) | No | Range of the glyphs, where **range.start** indicates the start position of the range, and **range.end** indicates the length of the range. If the length is 0, the range is from **range.start** to the end of the run. If **range.end** or **range.start** is set to a negative value, **null**, or **undefined**, **undefined** is returned. If this parameter is not passed, the entire run is obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<number> | Array of character indices. |

**Example**

import { text } from '@kit.ArkGraphics2D'

function textFunc() {
  let indices = runs\[0\].getStringIndices(); // Obtain the indices of all characters in the run.
  let indicesRange = runs\[0\].getStringIndices({start:1, end:2}); // Obtain the indices of characters in the range starting from position 1, with a length of 2.
  indicesRange = runs\[0\].getStringIndices({start:-1, end:2}); // -1 is an invalid value, and undefined is returned.
  indicesRange = runs\[0\].getStringIndices({start:0, end:-10}); // -10 is an invalid value, and undefined is returned.
  let indicesNull = runs\[0\].getStringIndices(null); // null is an invalid value, and undefined is returned.
  let indicesUndefined = runs\[0\].getStringIndices(undefined); // undefined is an invalid value, and undefined is returned.
}

@Entry
@Component
struct Index {
  fun: Function = textFunc;
  build() {
    Column() {
      Button().onClick(() => {
        this.fun();
      })
    }
  }
}

#### \[h2\]getImageBounds18+

getImageBounds(): common2D.Rect

Obtains the image boundary of this run. The image boundary, equivalent to a visual boundary, is related to the font, font size, and characters. For example, for the string " a b " (which has a space before "a" and a space after "b"), only "a b" are visible to users, and therefore the image boundary does not include these spaces at the beginning and end.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/7ZGA_HM8SdOB-69deUekDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E619DAD86DE0C96B299D94C66031C16DE5DD13CD29B7723E22B2D110C0217A8C)

The following figure shows the image boundaries of the string " a b ".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/L7TlZEKJSdOTMRPp9yji8A/en-us_image_0000002537766442.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37A80FAD091AD5FAFBDA873ED61349C35818A850DEC53D54F0B398B083A54C24)

The following figure shows the image boundaries of the strings "j" and "E".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/O-u7JVDRQMmDRVt5SGOw7Q/en-us_image_0000002537926382.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60840EC0DB249D9CC819FBA8A892F98A830EB096135253E9F4A52493461B566E)

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| [common2D.Rect](../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#rect) | Image boundary of the run. |

**Example**

let bounds = runs\[0\].getImageBounds();

#### \[h2\]getTypographicBounds18+

getTypographicBounds(): TypographicBounds

Obtain the typographic boundaries of this run. These boundaries depend on the typographic font and font size, but not on the characters themselves. For example, for the string " a b " (which has a space before "a" and a space after "b"), the typographic boundaries include the spaces at the beginning and end of the line.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/QGZvdyicTYGJeXKNBOlH7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8CE13FAECCDD98665179B66CA84DFD33570E232FE3C8FA494A01C80D005CA17)

The following figure shows the typographic boundaries of the string " a b ".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/NVdXrhJoQWqac7uGEz3GTw/en-us_image_0000002568686157.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=750A95FF037A6826BF2C1BF1D6E7390B2C0B3362D698707AF58A70ADBFBA66A9)

The following figure shows the typographic boundaries of the strings "j" and "E".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/5RygXhnzSOaWqgsyGvDlLg/en-us_image_0000002568766167.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC7774B1DAA736790BD5F0AD4ABD7AFD63BD04FFBDD655ABF13BD3D9EBBD2111)

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| [TypographicBounds](#typographicbounds18) | Typographic boundaries of the run. |

**Example**

let typographicBounds = runs\[0\].getTypographicBounds();

#### \[h2\]getTextDirection20+

getTextDirection(): TextDirection

Obtains the text direction of the run.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Return value**

| Type | Description |
| :-- | :-- |
| [TextDirection](#textdirection) | Obtains the text direction of the run. |

**Example**

let textDirection = runs\[0\].getTextDirection();

#### \[h2\]getAdvances20+

getAdvances(range: Range): Array<common2D.Point>

Obtains the glyph width array of each glyph within the specified range of the run.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| range | [Range](#range) | Yes | Range of the glyph position to be obtained. **range.start** indicates the start position of the range, and **range.end** indicates the range length. If the length is 0, the range starts from **range.start** and ends at the end of the rendering block. If **range.end** or **range.start** is set to a negative value, **null**, or **undefined**, **undefined** is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[common2D.Point](../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#point12)\> | Returns the glyph width array of each glyph in the run unit relative to the horizontal direction. In [common2D.Point](../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#point12), **x** indicates the glyph width of each glyph relative to the horizontal direction, and **y** is a reserved field. By default, **0** is returned. |

**Example**

let advancesRange = runs\[0\].getAdvances({start:1, end:2}); // Obtain the widths of glyphs in the range starting from position 1, with a length of 2.
advancesRange = runs\[0\].getAdvances({start:-1, end:2}); // -1 is an invalid value, and undefined is returned.
advancesRange = runs\[0\].getAdvances({start:0, end:-10}); // -10 is an invalid value, and undefined is returned.
let advancesNull = runs\[0\].getAdvances(null); // null is an invalid value, and undefined is returned.

#### TextTab18+

Implements a paragraph-style text tab, which stores the alignment mode and position.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| alignment | [TextAlign](#textalign) | No | No | Alignment mode of the text following the tab character in a paragraph. It can be set to **LEFT**, **RIGHT**, and **CENTER** defined in [TextAlign](#textalign). Other enumerated values have the effect of left alignment. The default value is left alignment. |
| location | number | No | No | Alignment position of the text following the tab character. The value is a floating point number, in px. The minimum value is 1.0. When the value is less than 1.0, the tab character is replaced with a space. |

**Example**

**alignment** is **CENTER**, **location** is **200**, and the text is "12/t345".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/y-H8BcepQRK5ers5EonQhA/en-us_image_0000002568686159.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5ADF2A12E703B3A02AE4067E0D90F52D220D8223B0421AFBDFBD3E0F57C162E7)

**alignment** is **LEFT**, **location** is **100**, and the text is "abccccccccc/tdef".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/1XnkY9K4Q-SHrYnBdH6vsQ/en-us_image_0000002568766169.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C3546ACA25B79F6CDAE6B9DEFA22C12B30611C540F1ADA8E91658F505F8D9BD)

**alignment** is **RIGHT**, **location** is **100**, and the text is "aabcdef/tg hi/tjkl/tmno/tp qr".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/UUmyxK0sSQO_XzkWDapNyg/en-us_image_0000002537766444.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=801E1E336E7DB7134C355B57E2476863B838E1B282862EC5592ABE1155EE476F)

#### SystemFontType14+

Enumerates the font types, which can be combined through bitwise OR operations.

**System capability**: SystemCapability.Graphics.Drawing

**Atomic service API**: This API can be used in atomic services since API version 22.

| Name | Value | Description |
| :-- | :-- | :-- |
| ALL | 1 << 0 | All font types, including the system font type, style font type, and user-installed font type. |
| GENERIC | 1 << 1 | System font type. |
| STYLISH | 1 << 2 | Style font type. The style font type is designed for 2-in-1 devices. |
| INSTALLED | 1 << 3 | Font type that has been installed. |
| CUSTOMIZED18+ | 1 << 4 | Custom font type. |
