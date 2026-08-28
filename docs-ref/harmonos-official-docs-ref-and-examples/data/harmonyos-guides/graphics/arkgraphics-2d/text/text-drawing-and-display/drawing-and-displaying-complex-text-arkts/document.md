# Drawing and Displaying Complex Text (ArkTS)

Simple text can be drawn and displayed with appropriate fonts, sizes, and colors selected. Additionally, complex text drawing is supported by setting other styles, languages, paragraphs, etc.

Complex text drawing involves the following scenarios:

-   Multi-language text drawing and display
    
-   Multi-line text drawing and display
    
-   Multi-style text drawing and display
    

#### Multi-language Text Drawing and Display

Multi-language support is the foundation of globalized applications. Multi-language text drawing needs to support the character sets of different languages and their unique display requirements, such as right-to-left languages (such as Arabic) or vertical text (such as Chinese). You need to understand the rendering features of different languages to ensure correct text display.

When multi-language text is used, you can specify the **locale** field in [TextStyle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-graphics-text#textstyle) to match the corresponding font, skipping the process of traversing the font list to save time and memory.

## How to Develop

1.  Obtain the canvas object through **context**.
    
    // Here is the drawing code logic.
    let canvas = context.canvas;
    
2.  Initialize the text style.
    
    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 50,
      // Set the preferred language to Simplified Chinese.
      locale: 'zh-Hans'
    };
    
3.  Initialize the paragraph style.
    
    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
    };
    
4.  Initialize the paragraph object and add text.
    
    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
    // Push the text style.
    paragraphBuilder.pushStyle(myTextStyle);
    // Add text.
    paragraphBuilder.addText('你好，世界');
    
5.  Layout the paragraph and draw the text.
    
    // Generate a paragraph.
    let paragraph = paragraphBuilder.build();
    // Layout.
    paragraph.layoutSync(1250);
    // Draw the text.
    paragraph.paint(canvas, 10, 0);
    

## Effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/QttTGQxKS-e2jPxjcgdfZw/en-us_image_0000002568764967.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4925B727527BB7DCC9F5965D6533E1F955B4845A5624067196199F7841FBBA5)

#### Multi-line Text Drawing and Display

Multi-line text is more complex than single-line text. Generally, text typography, word break, text alignment, line limit, etc., are required for multi-line text, mainly achieved by setting paragraph styles.

## How to Implement

[ParagraphStyle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-graphics-text#paragraphstyle) is used to set the style of each paragraph in the multi-line text, including the word break, text alignment, and line limit. You can style different paragraphs to improve text readability and aesthetics.

## How to Develop

1.  Obtain the canvas object through **context**.
    
    // Here is the drawing code logic.
    let canvas = context.canvas;
    
2.  Initialize the text style.
    
    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 50,
      // When wordBreak is set to text.WordBreak.BREAK\_HYPHEN, you need to set the preferred language so that the paragraph can be displayed with the respective word break effect.
      locale: 'en-gb'
    };
    
3.  Initialize the paragraph style.
    
    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
      // Text alignment mode
      align: text.TextAlign.LEFT,
      // Maximum number of lines
      maxLines: 3,
      // Word break policy
      wordBreak: text.WordBreak.BREAK\_WORD
    };
    
4.  Initialize the paragraph object and add placeholders and text.
    
    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
    // Push the text style.
    paragraphBuilder.pushStyle(myTextStyle);
    // Add text.
    paragraphBuilder.addText('Hello World Hello World Hello World Hello World Hello World Hello World ' +
      'Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World ' +
      'Hello World Hello World Hello World Hello World Hello World ');
    
5.  Layout the paragraph and draw the text.
    
    // Generate a paragraph.
    let paragraph = paragraphBuilder.build();
    // Layout.
    paragraph.layoutSync(1250);
    // Draw the text.
    paragraph.paint(canvas, 10, 0);
    

## Effect

| Paragraph Style Settings (Word Break, Text Alignment, and Line Limit) | Effect |
| :-- | :-- |
| text.WordBreak.BREAK\_WORD, text.TextAlign.LEFT, 3 lines at most. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/E_1hEskxQf-oTyBNJRho7A/en-us_image_0000002537765242.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05B77A0005AB0F9406C73C22274A625DFA31916C033A29DCC261830765D73363) |
| text.WordBreak.BREAK\_WORD, text.TextAlign.RIGHT, 3 lines at most. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/XxlN_zo_TKmr4QP3FwCv_w/en-us_image_0000002537925182.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CC992E7FE1CEC8922377C6474E0F6A87A5B8E9118B3C000CBE8D00CA74E13FD) |
| text.WordBreak.BREAK\_WORD, text.TextAlign.JUSTIFY, 10 lines at most. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/HUiegONKQjaTe_dtdwHohg/en-us_image_0000002568684959.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F9C31FF45D288AD9070C45EFE4F6D472B89EED4CF46AB6DE395EA710DA422C0C) |
| text.WordBreak.BREAK\_ALL, text.TextAlign.LEFT, 3 lines at most. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/6yt6AhYyT0WLOuOGPvUv2Q/en-us_image_0000002568764969.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB6286CE98DDA5E9C1728058EAC2FB08F801A412C023204A6F92CDB400331896) |
| text.WordBreak.BREAK\_ALL, text.TextAlign.LEFT, 10 lines at most. | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/aY2mqNtuTTSyTW1SZnw0WA/en-us_image_0000002537765244.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E67A73DD75940705D7CB2F37D57FDADC73545F03180CFF63DB3F31A9723E3F37) |
| 
text.WordBreak.BREAK\_HYPHEN, text.TextAlign.LEFT, 10 lines at most.

No language preference. No hyphen (-) for word breaks.

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/eFvnnfH-RpK2M9vfZ4DChQ/en-us_image_0000002537925184.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC8B46481A82713F9DA551C86D245CC152717D32FDB13F40D7F708F1D7B5CEB3) |
| 

text.WordBreak.BREAK\_HYPHEN, text.TextAlign.LEFT, 10 lines at most.

Preferred language: en-gb (UK). Hyphens (-) for word breaks.

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/x6SQeKaxQ26VrewSmH0g2g/en-us_image_0000002568684961.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C5DBA7D70C35BADC8CFBF6A5815C18B4301AA3CC518A4B3A80FA94BEC95E9936) |
| 

text.WordBreak.BREAK\_HYPHEN, text.TextAlign.LEFT, 10 lines at most.

Preferred language: en-us (US). Hyphens (-) for word breaks.

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/z-KHHrXLTKmP737InTeX8w/en-us_image_0000002568764971.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9CE3C3EC2B3333929A3558B1F3F61835C91101819A12A570DBE4F8CE98FFF097) |

#### Multi-style Text Drawing and Display

In addition to the basic text and typography attributes, you may need to set different drawing styles or capabilities for different text designs in applications to highlight the unique performance or style of the corresponding text. In this case, you can use multiple drawing styles to render the text.

The following lists the multi-style drawing supported by the current version and the effects of each drawing style:

-   **Decoration**: decorates the text with different line styles, which can make the text more prominent and expressive.
    
-   **Font feature**: alters the appearance of the text through font changes, including thickness, italics and other features, to enhance the readability and aesthetics of the text.
    
-   **Font variation**: flexibly adjusts the text in different display environments and devices for more refined visual effects.
    
-   **Text shadow**: adds shadow effects around the text to enhance the text's sense of depth and three-dimensionality, making the text more attractive.
    
-   **Placeholder**: maintains the stability of the text layout when the text content is uncertain, making text display smoother and more natural.
    
-   **Automatic spacing**: adds extra spacing in places where characters are mixed and switched, improving the reading experience.
    
-   **Vertical alignment**: adjusts the typography position of text in the vertical direction to improve typography quality.
    
-   **Superscript and subscript**: processes any character into superscript or subscript.
    
-   **High-contrast text**: turns dark text black and light text white to enhance the contrast effect of the text.
    
-   **Line height adjustment**: adjusts the line height to change the vertical spacing of text lines, making the line spacing looser or tighter, significantly addressing the problem of vertical truncation of text and improving readability.
    
-   **Line spacing adjustment**: adjusts the line spacing to change the line height, optimizing the reading experience.
    

## Decoration

[Decoration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-graphics-text#decoration) is a decorative line added above, below, or in the middle of the text. Currently, the overline, underline, and strikethrough are supported.

You can add text decoration to enhance the visual effect and readability of the text.

To use decoration, you need to initialize the decoration style object and add it to the text style so that the decoration take effect when the text is drawn.

For details, see [Example 1](#example-1-decoration-and-font-feature).

## Font Feature

[FontFeature](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-graphics-text#fontfeature) focuses on processing font features (such as bold, italic, and font variants) during text rendering. It allows fonts to display different effects in different typography scenarios, enhancing the expressiveness of text to better meet design and reading requirements.

Common **FontFeature** includes liga, frac, and case, which can be enabled only when the corresponding TTF file is supported.

For details, see [Example 1](#example-1-decoration-and-font-feature).

## Font Variation

[FontVariation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-graphics-text#fontvariation) is a font format that contains multiple glyph variants in a single font file. It allows you to flexibly adjust various font attributes (such as font weight, font width, and italic) in a single font file.

Unlike regular font files (each variant requires an independent file), font variation contain multiple variant axes in a single font file to implement smooth transition during text rendering and drawing.

For details, see [Example 2](#example-2-font-variation-text-shadow-and-placeholder).

## Text Shadow

[TextShadow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-graphics-text#textshadow) creates a 3D effect for text by adding depth against the background. It is usually used to improve the visual appeal or readability of text, especially in scenarios with low color contrast.

**TextShadow** has three attributes: **color** (shadow color), **point** (shadow offset from the text), and **blurRadius** (shadow radius).

To use the shadow effect, you need to set the shadow effect array in the text style so that the shadow effect takes effect when the text is drawn.

For details, see [Example 2](#example-2-font-variation-text-shadow-and-placeholder).

## Placeholder

Placeholder drawing is used to render placeholder symbols in the text.

Placeholder drawing is also used to implement image and text layout. It is a visual element used to provide or replace a position before the actual image or content is registered.

For details, see [Example 2](#example-2-font-variation-text-shadow-and-placeholder).

## Automatic Spacing

When automatic spacing is enabled, it applies between CJK (Chinese, Japanese, and Korean) and Western characters (Latin, Cyrillic, and Greek), between CJK and digits, between CJK and copyright symbols, between copyright symbols and digits, and between copyright symbols and Western characters. For example, in an English-Chinese mixed layout scenario, automatic spacing adds extra spacing in places where English and Chinese are switched, improving the reading experience.

Sample code:

let myParagraphStyle: text.ParagraphStyle = {
  autoSpace: true
};

## Vertical Alignment

Vertical alignment is used to adjust the vertical layout position of text in a line. Vertical alignment aligns the text to the top, center, bottom, or baseline (default) when line height scaling is enabled or when text in different font sizes is mixed in a line. Sample code:

let myParagraphStyle: text.ParagraphStyle = {
  verticalAlign: text.TextVerticalAlign.CENTER
};

For details, see [Example 3](#example-3-vertical-alignment).

## Superscript and Subscript

Superscript or subscript text can be enabled in cases such as mathematical and chemical formulas. Sample code:

let superScriptStyle: text.TextStyle = {
    badgeType: text.TextBadgeType.TEXT\_SUPERSCRIPT
};

For details, see [Example 4](#example-4-superscript-and-subscript).

## High Contrast

High contrast can change dark text to black and light text to white. You can enable or disable high contrast text rendering in your application, or follow the system settings.

There are three high contrast modes. For details, see [TextHighContrast](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-graphics-text#texthighcontrast20).

For details, see [Example 5](#example-5-high-contrast).

## Line Height Adjustment

You can adjust the line height either by setting the maximum and minimum line heights or using a line height scaling coefficient.

**Method 1**

Starting from API version 21, you can adjust the line height by setting the maximum and minimum line heights. The sample code is as follows:

let myTextStyle: text.TextStyle = {
    // Set the maximum line height.
    lineHeightMaximum: 65,
    // Set the minimum line height.
    lineHeightMinimum: 65
};

For details, see [Example 6](#example-6-line-height-adjustment-method-1).

**Method 2**

You can adjust the line height by setting the line height scaling coefficient. The sample code is as follows:

let myTextStyle: text.TextStyle = {
    // Enable line height scaling.
    heightOnly: true,
    // Set the line height scaling coefficient.
    heightScale: 1.5,
    // Set the line height scaling style.
    lineHeightStyle: text.LineHeightStyle.FONT\_HEIGHT
};

For details, see [Example 7](#example-7-line-height-adjustment-method-2).

## Line Spacing Adjustment

Starting from API version 21, you can adjust the line spacing to improve the reading experience. The sample code is as follows:

let myParagraphStyle: text.ParagraphStyle = {
  // Set the line spacing.
  lineSpacing: 100,
  // Disable the ascent and descent of the paragraph.
  textHeightBehavior: text.TextHeightBehavior.DISABLE\_ALL,
};

For details, see [Example 8](#example-8-line-spacing-adjustment).

## Example 1 (Decoration and Font Feature)

The following uses the decoration and font feature in the text style as an example to describe how to draw and display multi-style text.

import { NodeController, FrameNode, RenderNode, DrawContext } from '@kit.ArkUI'
import { UIContext } from '@kit.ArkUI'
import { text } from '@kit.ArkGraphics2D'

// Create a MyRenderNode class and draw the text.
class MyRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    let canvas = context.canvas;

    // Initialize the decoration object.
    let decorations: text.Decoration =
      {
        // Decoration type, which can be overline, underline, or strikethrough.
        textDecoration: text.TextDecorationType.UNDERLINE,
        // Decoration color.
        color: {
          alpha: 255,
          red: 255,
          green: 0,
          blue: 0
        },
        // Decoration style, which can be wave, dashed line, or straight line.
        decorationStyle:text.TextDecorationStyle.SOLID,
        // Decoration height.
        decorationThicknessScale: 1
      };

    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 200,
      // Set the decoration.
      decoration: decorations,
      // Enable the font feature.
      fontFeatures: \[{name: 'frac', value: 1}\]
    };

    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
    };

    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    // Push the text style.
    paragraphBuilder.pushStyle(myTextStyle);
    // Add text.
    paragraphBuilder.addText('1/2 1/3 1/4 ');

    // Generate a paragraph.
    let paragraph = paragraphBuilder.build();
    // Layout.
    paragraph.layoutSync(1250);
    // Draw the text.
    paragraph.paint(canvas, 0, 0);
  }
}

// Create a MyRenderNode object.
const textNode = new MyRenderNode();
// Define the pixel format of MyRenderNode.
textNode.frame = {
  x: 0,
  y: 0,
  width: 400,
  height: 600
};
textNode.pivot = { x: 0.2, y: 0.8 };
textNode.scale = { x: 1, y: 1 };

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext);
    if (this.rootNode == null) {
      return this.rootNode;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.frame = {
        x: 0,
        y: 0,
        width: 10,
        height: 500
      }
    }
    return this.rootNode;
  }

  addNode(node: RenderNode): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.appendChild(node);
    }
  }

  clearNodes(): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.clearChildren();
    }
  }
}

let myNodeController: MyNodeController = new MyNodeController();

async function performTask() {
  myNodeController.clearNodes();
  myNodeController.addNode(textNode);
}

@Entry
@Component
struct Font08 {
  @State src: Resource = $r('app.media.startIcon');
  build() {
    Column() {
      Row() {
        NodeContainer(myNodeController)
          .height('100%')
          .width('100%')
        Image(this.src)
          .width('0%').height('0%')
          .onComplete(
            () => {
              performTask();
            })
      }
      .width('100%')
    }
  }
}

The following figures show the effect.

| Style Settings (Decoration Style and Font Feature) | Effect |
| :-- | :-- |
| Disabled | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/uiodjzTPTgWWxs9-sEVXOQ/en-us_image_0000002537765246.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E941E0C904049F96277FF3B2A7B26A2416B97E48E5ACDCA0BB5F136E499883C2) |
| Enabled | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/bEUfaiMZS9CyVKeMZNbS_A/en-us_image_0000002537925186.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68028C96626D3744184B9F02F60266C5D40069EC57D65E2B09430D7DCD0FBC3D) |

## Example 2 (Font Variation, Text Shadow, and Placeholder)

The following uses the font variation, text shadow, and placeholder features as an example to describe how to draw and display multi-style text.

import { NodeController, FrameNode, RenderNode, DrawContext } from '@kit.ArkUI'
import { UIContext } from '@kit.ArkUI'
import { drawing } from '@kit.ArkGraphics2D'
import { text } from '@kit.ArkGraphics2D'
import { common2D } from '@kit.ArkGraphics2D'

// Create a MyRenderNode class and draw the text.
class MyRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    let canvas = context.canvas;

    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 120,
      // Font variation.
      fontVariations: \[{axis: 'wght', value: 555}\],
      // Text shadow.
      textShadows: \[{color: { alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00 }, point: {x:10,y:10}, blurRadius: 10}\],
    };

    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
    };

    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    // Initialize the placeholder object.
    let myPlaceholderSpan: text.PlaceholderSpan = {
      // Width.
      width: 300,
      // Height.
      height: 300,
      // Baseline alignment policy.
      align: text.PlaceholderAlignment.BOTTOM\_OF\_ROW\_BOX,
      // Text baseline type.
      baseline: text.TextBaseline.ALPHABETIC,
      // Offset relative to the baseline. This parameter is valid only when the alignment policy is OFFSET\_AT\_BASELINE.
      baselineOffset: 100
    };
    // Add a placeholder.
    paragraphBuilder.addPlaceholder(myPlaceholderSpan);

    // Push the text style.
    paragraphBuilder.pushStyle(myTextStyle);
    // Add text.
    paragraphBuilder.addText('Hello Test');

    // Generate a paragraph.
    let paragraph = paragraphBuilder.build();
    // Layout.
    paragraph.layoutSync(1250);
    // Draw the text.
    paragraph.paint(canvas, 0, 0);

    // Obtain the array of all placeholders.
    let placeholderRects = paragraph.getRectsForPlaceholders();
    // Obtain the left bound of the first placeholder.
    let left = placeholderRects\[0\].rect.left;
    // Obtain the top bound of the first placeholder.
    let top = placeholderRects\[0\].rect.top;
    // Obtain the right bound of the first placeholder.
    let right = placeholderRects\[0\].rect.right;
    // Obtain the bottom bound of the first placeholder.
    let bottom = placeholderRects\[0\].rect.bottom;
    let pen: drawing.Pen =  new drawing.Pen();
    let penColor : common2D.Color = { alpha: 0xFF, red: 0xFF, green: 0x00, blue: 0x00 };
    pen.setColor(penColor);
    canvas.attachPen(pen);
    // Use the draw method to draw the placeholder rectangle.
    canvas.drawRect(left,top,right,bottom);
  }
}

// Create a MyRenderNode object.
const textNode = new MyRenderNode();
// Define the pixel format of MyRenderNode.
textNode.frame = {
  x: 0,
  y: 0,
  width: 400,
  height: 600,
};
textNode.pivot = { x: 0.2, y: 0.8 };
textNode.scale = { x: 1, y: 1 };

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext);
    if (this.rootNode == null) {
      return this.rootNode;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.frame = {
        x: 0,
        y: 0,
        width: 10,
        height: 500
      };
    }
    return this.rootNode;
  }

  addNode(node: RenderNode): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.appendChild(node);
    }
  }

  clearNodes(): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.clearChildren();
    }
  }
}

let myNodeController: MyNodeController = new MyNodeController();

async function performTask() {
  myNodeController.clearNodes();
  myNodeController.addNode(textNode);
}

@Entry
@Component
struct Font08 {
  @State src: Resource = $r('app.media.startIcon');
  build() {
    Column() {
      Row() {
        NodeContainer(myNodeController)
          .height('100%')
          .width('100%')
        Image(this.src)
          .width('0%').height('0%')
          .onComplete(
            () => {
              performTask();
            })
      }
      .width('100%')
    }
  }
}

The following figures show the effect.

| Style (Font Variation, Text Shadow, and Placeholder) | Effect |
| :-- | :-- |
| Disabled | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/8i_uUZsxRNCRH9irPgsuWg/en-us_image_0000002568684963.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E555138E56DA0334FAE3833B3508A1C5FA241E7480D71D4B8877D074BA6BBC9C) |
| Enabled | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/pznwaU2ETwysRfG5H_Q1zA/en-us_image_0000002568764973.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99D81E708B81578D10F6ABB1B2512C7BB8545F7964C813BB09C6F0B6B48BDA1F) |

## Example 3 (Vertical Alignment)

The following uses vertical alignment - center alignment as an example to describe the vertical typography feature.

import { NodeController, FrameNode, RenderNode, DrawContext, UIContext } from '@kit.ArkUI'
import { text } from '@kit.ArkGraphics2D'

// Create a MyRenderNode class and draw the text.
class MyRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    let canvas = context.canvas;

    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 30,
      // Enable line height scaling.
      heightOnly: true,
      // Set the line height scaling coefficient to twice the font size.
      heightScale: 2
    };

    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
      // Set the vertical alignment mode to center alignment.
      verticalAlign: text.TextVerticalAlign.CENTER,
    };

    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    // Set the style to be applied to the typography text.
    paragraphBuilder.pushStyle(myTextStyle);
    // Add text.
    paragraphBuilder.addText('VerticalAlignment-center');

    // Generate a paragraph.
    let paragraph = paragraphBuilder.build();
    // Layout.
    paragraph.layoutSync(1000);
    // Draw the text.
    paragraph.paint(canvas, 0, 0);
  }
}

// Create a MyRenderNode object.
const textNode = new MyRenderNode();
// Define the pixel format of MyRenderNode.
textNode.frame = {
  x: 0,
  y: 0,
  width: 400,
  height: 600
};
textNode.pivot = { x: 0.2, y: 0.8 };
textNode.scale = { x: 1, y: 1 };

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext);
    if (this.rootNode == null) {
      return this.rootNode;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.frame = {
        x: 0,
        y: 0,
        width: 10,
        height: 500
      }
      renderNode.pivot = { x: 50, y: 50 };
    }
    return this.rootNode;
  }

  addNode(node: RenderNode): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.appendChild(node);
    }
  }

  clearNodes(): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.clearChildren();
    }
  }
}

let myNodeController: MyNodeController = new MyNodeController();

async function performTask() {
  myNodeController.clearNodes();
  myNodeController.addNode(textNode);
}

@Entry
@Component
struct Font08 {
  @State src: Resource = $r('app.media.startIcon');
  build() {
    Column() {
      Row() {
        NodeContainer(myNodeController)
          .height('100%')
          .width('100%')
        Text('Test for vertical alignment')
          .onAppear(() => {
            performTask();
          })
      }
      .width('100%')
    }
  }
}

The following figures show the effect.

| Style (Vertical Alignment) | Effect (The black box only shows the text drawing area and is not drawn in actual.) |
| :-- | :-- |
| Baseline alignment (default) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/gBK9up80TCKU1NRcQCskvw/en-us_image_0000002537765248.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CA4F3466E4167857D13499A5773403D69672D439DE1E0845D2BA8085FAC148A) |
| Top alignment | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/cTBkc_q1SIavicxuK4sWng/en-us_image_0000002537925188.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E15FAD06CAF5591D66089AEF5B85B5F126B081E120B30EABDBC88D867465D00D) |
| Center alignment | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/J8etzh_YQRG9KTjBgeFawA/en-us_image_0000002568684965.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DAFD9F4F093FCCE4E586545A1A301AEC07B33B9AD1C297EB998E4573ACD029E) |
| Bottom alignment | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/cgzU3GszRLm4E32krVqIMg/en-us_image_0000002568764975.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D39678B34C072E64041854FBEE91FBC339D93B4B2B272D4068D40C467B1E532) |

## Example 4 (Superscript and Subscript)

The following uses the subscript style as an example to describe the superscript and subscript typography feature.

import { NodeController, FrameNode, RenderNode, DrawContext, UIContext } from '@kit.ArkUI'
import { text } from '@kit.ArkGraphics2D'

// Create a MyRenderNode class and draw the text.
class MyRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    let canvas = context.canvas;

    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 30,
    };

    let subScriptStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 30,
      // Set the subscript style.
      badgeType: text.TextBadgeType.TEXT\_SUBSCRIPT
    };

    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
    };

    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    // Set the style to be applied to the typography text.
    paragraphBuilder.pushStyle(myTextStyle);
    // Add text.
    paragraphBuilder.addText('The chemical formula for water: H');
    paragraphBuilder.pushStyle(subScriptStyle);
    paragraphBuilder.addText('2');
    paragraphBuilder.pushStyle(myTextStyle);
    paragraphBuilder.addText('o');

    // Generate a paragraph.
    let paragraph = paragraphBuilder.build();
    // Layout.
    paragraph.layoutSync(1000);
    // Draw the text.
    paragraph.paint(canvas, 0, 0);
  }
}

// Create a MyRenderNode object.
const textNode = new MyRenderNode();
// Define the pixel format of MyRenderNode.
textNode.frame = {
  x: 0,
  y: 0,
  width: 400,
  height: 600
};
textNode.pivot = { x: 0.2, y: 0.8 };
textNode.scale = { x: 1, y: 1 };

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext);
    if (this.rootNode == null) {
      return this.rootNode;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.frame = {
        x: 0,
        y: 0,
        width: 10,
        height: 500
      }
      renderNode.pivot = { x: 50, y: 50 };
    }
    return this.rootNode;
  }

  addNode(node: RenderNode): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.appendChild(node);
    }
  }

  clearNodes(): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.clearChildren();
    }
  }
}

let myNodeController: MyNodeController = new MyNodeController();

async function performTask() {
  myNodeController.clearNodes();
  myNodeController.addNode(textNode);
}

@Entry
@Component
struct Font08 {
  @State src: Resource = $r('app.media.startIcon');
  build() {
    Column() {
      Row() {
        NodeContainer(myNodeController)
          .height('100%')
          .width('100%')
        Text('Test for superscript and subscript')
          .onAppear(() => {
            performTask();
          })
      }
    }
    .width('100%')
  }
}

The following figures show the effect.

| Style (Superscript and Subscript) | Effect |
| :-- | :-- |
| Superscript text | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/mWt13wL8SdiowUNFpfks1g/en-us_image_0000002537765250.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B879BF6900EC2628474B840E5A5128DF8A4C3B5E173BCB5E717F040774AB8F0F) |
| Subscript text | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/-gXrzpE8Td6p6pLu46J_cA/en-us_image_0000002537925190.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50CF012BABFB75366E1551B62024AC1A27DB4734973ECC07D737D40A808CDF0F) |

## Example 5 (High Contrast)

The following uses high contrast as an example to describe how to draw and display high-contrast text.

import { NodeController, FrameNode, RenderNode, DrawContext, UIContext} from '@kit.ArkUI'
import { text } from '@kit.ArkGraphics2D'

// Create a MyRenderNode class and draw the text.
class MyRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    let canvas = context.canvas;

    // Enable high contrast for text rendering of your application.
    text.setTextHighContrast(text.TextHighContrast.TEXT\_APP\_ENABLE\_HIGH\_CONTRAST);

    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 111,
        green: 255,
        blue: 255
      },
      fontSize: 100,
    };

    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
    };

    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    // Push the text style.
    paragraphBuilder.pushStyle(myTextStyle);
    // Add text.
    paragraphBuilder.addText('Hello World');

    // Generate a paragraph.
    let paragraph = paragraphBuilder.build();
    // Layout.
    paragraph.layoutSync(1250);
    // Draw the text.
    paragraph.paint(canvas, 10, 800);
  }
}

// Create a MyRenderNode object.
const textNode = new MyRenderNode();
// Define the pixel format of MyRenderNode.
textNode.frame = {
  x: 0,
  y: 0,
  width: 400,
  height: 600
};
textNode.pivot = { x: 0.2, y: 0.8 };
textNode.scale = { x: 1, y: 1 };

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext);
    if (this.rootNode == null) {
      return this.rootNode;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.frame = {
        x: 0,
        y: 0,
        width: 10,
        height: 500
      };
      renderNode.pivot = { x: 0.2, y: 0.8 };
    }
    return this.rootNode;
  }

  addNode(node: RenderNode): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.appendChild(node);
    }
  }

  clearNodes(): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.clearChildren();
    }
  }
}

let myNodeController: MyNodeController = new MyNodeController();

async function performTask() {
  myNodeController.clearNodes();
  myNodeController.addNode(textNode);
}

@Entry
@Component
struct Font08 {
  build() {
    Column() {
      Row() {
        NodeContainer(myNodeController)
          .height('100%')
          .width('100%')
        Text('Test high contrast')
          .onAppear(() => {
            performTask();
          })
      }
      .width('100%')
    }
  }
}

The following figures show the effect.

| High Contrast | Effect |
| :-- | :-- |
| Disabled | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/Ppd7YpPgSIWPmBF1MCIxYw/en-us_image_0000002568684967.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60D915E8F167A97ABA66B704CAE86E355D44C14B84E653B0D4096CD950D27E5E) |
| Enabled | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/l431VQYqSH6opIFKU1vaWA/en-us_image_0000002568764977.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B325A6E1F78DF3FBD1F12469F1B422D50014D0A6B1D58530FB937D886634CE1D) |

## Example 6 (Line Height Adjustment: Method 1)

In this example, the maximum and minimum line heights are set to the same value to show the drawing effect when the line height is fixed.

import { NodeController, FrameNode, RenderNode, DrawContext, UIContext } from '@kit.ArkUI'
import { text } from '@kit.ArkGraphics2D'

// Create a MyRenderNode class and draw the text.
class MyRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    let canvas = context.canvas;

    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 50,
      // Set the maximum line height.
      lineHeightMaximum: 65,
      // Set the minimum line height.
      lineHeightMinimum: 65,
    };

    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
    };

    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    // Set the style to be applied to the typography text.
    paragraphBuilder.pushStyle(myTextStyle);
    // Add text.
    paragraphBuilder.addText('Hello World!');

    // Generate a paragraph.
    let paragraph = paragraphBuilder.build();
    // Layout.
    paragraph.layoutSync(1000);
    // Draw the text.
    paragraph.paint(canvas, 0, 0);
  }
}

// Create a MyRenderNode object.
const textNode = new MyRenderNode()
// Define the pixel format of MyRenderNode.
textNode.frame = {
  x: 0,
  y: 0,
  width: 400,
  height: 600
}
textNode.pivot = { x: 0.2, y: 0.8 };
textNode.scale = { x: 1, y: 1 };

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext)
    if (this.rootNode == null) {
      return this.rootNode;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.frame = {
        x: 0,
        y: 0,
        width: 10,
        height: 500
      }
      renderNode.pivot = { x: 50, y: 50 };
    }
    return this.rootNode;
  }

  addNode(node: RenderNode): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.appendChild(node);
    }
  }

  clearNodes(): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode()
    if (renderNode != null) {
      renderNode.clearChildren();
    }
  }
}

let myNodeController: MyNodeController = new MyNodeController();

async function performTask() {
  myNodeController.clearNodes();
  myNodeController.addNode(textNode);
}

@Entry
@Component
struct Font08 {
  @State src: Resource = $r('app.media.startIcon')
  build() {
    Column() {
      Row() {
        NodeContainer(myNodeController)
          .height('100%')
          .width('100%')
        Text('Test for line height limit')
          .onAppear(() => {
            performTask();
          })
      }
    }
    .width('100%')
  }
}

The following figures show the effect.

| Maximum Line Height | Minimum Line Height | Effect (The black box only shows the text drawing area and is not drawn in actual.) |
| :-- | :-- | :-- |
| 65 | 65 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/F-bJd--cTIK7di2mRd-LUQ/en-us_image_0000002537765252.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5687C77683CBD3F2F96AF1B2F77EB28824E321F095EE5519A9739980D75706ED) |
| 200 | 200 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/56-VMDzpRB-_yUi0pvtoAw/en-us_image_0000002537925192.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF2029F99A669C1AEF18FCF8BA80E270EBC2E7F61BB86541351C4BA73DF05CA7) |

## Example 7 (Line Height Adjustment: Method 2)

The following uses line height scaling (**FontHeight**) as an example to describe how to draw and display text after the line height is adjusted.

import { NodeController, FrameNode, RenderNode, DrawContext, UIContext } from '@kit.ArkUI'
import { text } from '@kit.ArkGraphics2D'

// Create a MyRenderNode class and draw the text.
class MyRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    let canvas = context.canvas;

    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 50,
      // Enable line height scaling.
      heightOnly: true,
      // Set the line height scaling coefficient.
      heightScale: 1.5,
      // Set the line height scaling style.
      lineHeightStyle: text.LineHeightStyle.FONT\_HEIGHT,
    };

    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
    };

    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    // Set the style to be applied to the typography text.
    paragraphBuilder.pushStyle(myTextStyle);
    // Add text.
    paragraphBuilder.addText('Hello World!');

    // Generate a paragraph.
    let paragraph = paragraphBuilder.build();
    // Layout.
    paragraph.layoutSync(1000);
    // Draw the text.
    paragraph.paint(canvas, 0, 0);
  }
}

// Create a MyRenderNode object.
const textNode = new MyRenderNode();
// Define the pixel format of MyRenderNode.
textNode.frame = {
  x: 0,
  y: 0,
  width: 400,
  height: 600
}
textNode.pivot = { x: 0.2, y: 0.8 };
textNode.scale = { x: 1, y: 1 };

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext)
    if (this.rootNode == null) {
      return this.rootNode;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.frame = {
        x: 0,
        y: 0,
        width: 10,
        height: 500
      };
      renderNode.pivot = { x: 50, y: 50 };
    }
    return this.rootNode;
  }

  addNode(node: RenderNode): void {
    if (this.rootNode == null) {
      return
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.appendChild(node);
    }
  }

  clearNodes(): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode()
    if (renderNode != null) {
      renderNode.clearChildren();
    }
  }
}

let myNodeController: MyNodeController = new MyNodeController();

async function performTask() {
  myNodeController.clearNodes();
  myNodeController.addNode(textNode);
}

@Entry
@Component
struct Font08 {
  @State src: Resource = $r('app.media.startIcon')
  build() {
    Column() {
      Row() {
        NodeContainer(myNodeController)
          .height('100%')
          .width('100%')
        Text('Test for line height limit')
          .onAppear(() => {
            performTask();
          })
      }
    }
    .width('100%')
  }
}

The following figures show the effect.

| Line Height Scaling Style | Effect (The black box only shows the text drawing area and is not drawn in actual.) |
| :-- | :-- |
| FontSize | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/G5Sen4MvQU2tIMK29SxOKg/en-us_image_0000002568684969.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92A3ADB6359B0ABE3A012927B879C10E9D901EEFF5FF39998F0CC30F7E32854A) |
| FontHeight | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/c0HKfTb1TcGhTB5l_LLLDQ/en-us_image_0000002568764979.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61D1C63A9A60C8CB4D6F083ECD97DD50B14D6E7B7D31911F1CBB6EF7B8189E57) |

## Example 8 (Line Spacing Adjustment)

The following uses the example of disabling the paragraph ascent and descent and setting the line spacing to show how to draw and display text after line spacing is increased.

import { NodeController, FrameNode, RenderNode, DrawContext, UIContext } from '@kit.ArkUI'
import { text } from '@kit.ArkGraphics2D'

// Create a MyRenderNode class and draw the text.
class MyRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    let canvas = context.canvas;

    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 50,
    };

    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
      // Set the line spacing.
      lineSpacing: 100,
      // Disable the ascent and descent of the paragraph.
      textHeightBehavior: text.TextHeightBehavior.DISABLE\_ALL,
    };

    let fontCollection = text.FontCollection.getGlobalInstance();
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    // Set the style to be applied to the typography text.
    paragraphBuilder.pushStyle(myTextStyle);
    // Add text.
    paragraphBuilder.addText('Hello World!');

    // Generate a paragraph.
    let paragraph = paragraphBuilder.build();
    // Layout.
    paragraph.layoutSync(200);
    // Draw the text.
    paragraph.paint(canvas, 0, 0);
  }
}

// Create a MyRenderNode object.
const textNode = new MyRenderNode();
// Define the pixel format of MyRenderNode.
textNode.frame = {
  x: 0,
  y: 0,
  width: 400,
  height: 600
}
textNode.pivot = { x: 0.2, y: 0.8 };
textNode.scale = { x: 1, y: 1 };

class MyNodeController extends NodeController {
  private rootNode: FrameNode | null = null;

  makeNode(uiContext: UIContext): FrameNode {
    this.rootNode = new FrameNode(uiContext);
    if (this.rootNode == null) {
      return this.rootNode
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.frame = {
        x: 0,
        y: 0,
        width: 10,
        height: 500
      }
      renderNode.pivot = { x: 50, y: 50 };
    }
    return this.rootNode;
  }

  addNode(node: RenderNode): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.appendChild(node);
    }
  }

  clearNodes(): void {
    if (this.rootNode == null) {
      return;
    }
    const renderNode = this.rootNode.getRenderNode();
    if (renderNode != null) {
      renderNode.clearChildren();
    }
  }
}

let myNodeController: MyNodeController = new MyNodeController();

async function performTask() {
  myNodeController.clearNodes();
  myNodeController.addNode(textNode);
}

@Entry
@Component
struct Font08 {
  @State src: Resource = $r('app.media.startIcon')
  build() {
    Column() {
      Row() {
        NodeContainer(myNodeController)
          .height('100%')
          .width('100%')
        Text('Test for lineSpacing and height behavior')
          .onAppear(() => {
            performTask();
          })
      }
    }
    .width('100%')
  }
}

The following figures show the effect.

| Ascent and Descent | Effect (The black box only shows the text drawing area and is not drawn in actual.) |
| :-- | :-- |
| DISABLE\_ALL | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/lzPaSgeWTT21WHo4LteUnw/en-us_image_0000002537765254.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B5B6D1C29F44EDA1C1F50E7B0A5B48786F2FCC35561C93572E73692F4A45AB8) |
| ALL | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/bujxdI61RqK4YST_wZdRLQ/en-us_image_0000002537925194.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=445F758762BFAF9855F50CB7BF5746A28E7669A044EEE95E416BD3B44BFF9296) |
