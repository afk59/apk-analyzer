# Drawing and Displaying Simple Text (ArkTS)

#### Overview

In a simple user interface, only a few lines of static text need to be displayed, such as the text on a label, button, menu item, or status bar. In this case, you only need to select a proper font, size, and color to complete the rendering.

#### Related Attributes

In this scenario, the following text style attributes are involved. For details, see [TextStyle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-graphics-text#textstyle).

-   **color**: font color. The default value is white. Note that the font color must be different from the canvas color to ensure that the text can be properly displayed.
    
-   **fontSize**: font size, in units of px. The value is a floating point number. The default value is **14.0**.
    

#### How to Develop

1.  Obtain the canvas object through **context**.
    
    let canvas = context.canvas;
    
2.  Initialize the text style. Set the font color to red and font size to 50.
    
    // Obtain the text style.
    let myTextStyle: text.TextStyle = {
      // Text color.
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      // Text size.
      fontSize: 100
    };
    
3.  Initialize the paragraph style.
    
    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
    };
    
4.  Initialize the paragraph object and add text.
    
    let fontCollection = text.FontCollection.getGlobalInstance();
    let ParagraphGraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
    // Push the text style.
    ParagraphGraphBuilder.pushStyle(myTextStyle);
    // Add text.
    ParagraphGraphBuilder.addText("Hello World");
    
5.  Layout the paragraph and draw the text.
    
    // Generate a paragraph.
    let paragraph = ParagraphGraphBuilder.build();
    // Layout.
    paragraph.layoutSync(1250);
    // Draw the text.
    paragraph.paint(canvas, 0, 100);
    

#### Effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/JJVz3AK1RQ61zMNi2J_TjQ/en-us_image_0000002568684957.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE82D08E9119F2F86C0693E1DEF41B1524F56D90B3594D6228F111E0DA44F35D)
