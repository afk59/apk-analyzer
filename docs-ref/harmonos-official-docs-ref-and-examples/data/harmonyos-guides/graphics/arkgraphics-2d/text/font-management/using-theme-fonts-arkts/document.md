# Using Theme Fonts (ArkTS)

#### Overview

Theme fonts are specialized custom fonts available for use in theme applications. You can enable them using specific APIs.

#### Implementation Mechanism

**Figure 1** Switching and using theme fonts

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/gYHTyUzxQ0mOLvNM0nOH8Q/en-us_image_0000002537765236.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AEA63A32EF8AAEEF9D7BDDB1AAD72DEDB19A0FFD308DB1C15291AFB1C903A954)

For the switching and usage of theme fonts, the application must subscribe to the theme font change event. Upon receiving the event, the application needs to actively trigger a page refresh to enable theme font switching. Otherwise, the theme font changes will only take effect after the application is restarted.

#### Available APIs

The following table lists the APIs for registering and using theme fonts. For details, see [@ohos.graphics.text (Text)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-graphics-text).

| Name | Description |
| :-- | :-- |
| getGlobalInstance(): FontCollection | Obtains a global font collection instance. |

#### How to Develop

1.  Make sure that you can apply a theme font in the theme applications on your device.
    
2.  Import the required module.
    
    import { text } from '@kit.ArkGraphics2D';
    
3.  Call the **getGlobalInstance()** API to obtain the global font collection object. The system framework only passes theme font information to the global font collection object during theme font registration.
    
    // Obtain the global FontCollection instance of the font manager.
    let fontCollection = text.FontCollection.getGlobalInstance();
    
4.  Create a paragraph style and use the font manager instance to construct a **ParagraphBuilder** instance for generating paragraphs.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/YRMIf5vNTbyUyeGv8_Mw8A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=311FA0A80ADA666ED068D3B4048C56EE427B66E830716F679F4217FCF0BCD0FF)
    
    When setting the input parameters of the paragraph style for generating a paragraph object, do not specify the **fontFamilies** attribute. Otherwise, the specified font instead of the theme font is used.
    
    If no theme font is set in the theme applications, the default system font is used.
    
    // Set the text style.
    let myTextStyle: text.TextStyle = {
      color: { alpha: 255, red: 255, green: 0, blue: 0 },
      fontSize: 33
    };
    // Create a paragraph style object to set the typography style.
    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
      align: 3,
      wordBreak:text.WordBreak.NORMAL
    };
    // Create a paragraph generator.
    let paragraphGraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
    
5.  Set the text style, add text content, and generate paragraph text for subsequent text drawing and display.
    
    // Set the text style in the paragraph generator.
    paragraphGraphBuilder.pushStyle(myTextStyle);
    // Set the text content in the paragraph generator.
    paragraphGraphBuilder.addText("Hello World. \\nThis is the theme font.");
    // Generate a paragraph using the paragraph generator.
    let paragraph = paragraphGraphBuilder.build();
    
6.  Create a render node and save it to an array. (This sample code is simplified and uses an array as the container. During development, you should choose a proper container based on your use case to ensure that the addition and deletion of nodes correspond to each other.)
    
    // Create a render node array.
    const renderNodeMap: Array<RenderNode> = new Array();
    // Create a node controller.
    class MyNodeController extends NodeController {
      private rootNode: FrameNode | null = null;
      makeNode(uiContext: UIContext): FrameNode {
        this.rootNode = new FrameNode(uiContext);
        if (this.rootNode == null) {
          return this.rootNode;
        }
        const renderNode = this.rootNode.getRenderNode();
        if (renderNode != null) {
          renderNode.frame = { x: 0, y: 0, width: 300, height: 50 };
          renderNode.pivot = { x: 0, y: 0 };
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
          // Add the node to the render node array.
          renderNodeMap.push(node);
        }
      }
      clearNodes(): void {
        if (this.rootNode == null) {
          return;
        }
        const renderNode = this.rootNode.getRenderNode();
        if (renderNode != null) {
          renderNode.clearChildren();
          // Remove the node from the render node array.
          renderNodeMap.pop();
        }
      }
    }
    
7.  Create and export the render node update function for files (such as EntryAbility.ets) to use. The purpose of redrawing the node is to update the font information in the typography. If the font information is not updated, the residual result may be used, causing garbled characters.
    
    // Export the render node update function.
    export function updateRenderNodeData() {
      renderNodeMap.forEach((node) => {
        // Trigger node redrawing.
        node.invalidate();
      });
    }
    
8.  Receive the theme font change event in EntryAbility.ets and call the render node update function.
    
    import { AbilityConstant, Configuration, UIAbility, Want } from '@kit.AbilityKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { window } from '@kit.ArkUI';
    import { updateRenderNodeData } from '../pages/Index';
    
    // ...
    
    export default class EntryAbility extends UIAbility {
      preFontId = "";
      // ...
    
      onConfigurationUpdate(newConfig: Configuration): void {
        let fontId = newConfig.fontId;
        if (fontId && fontId !== this.preFontId) {
          this.preFontId = fontId;
          updateRenderNodeData();
          // ...
        }
      }
    }
    

#### Effect

The following figures show how text is rendered with different theme fonts in a theme application.

The following figures are for reference only.

**Figure 2** Effect of theme font 1

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/p0syl-KKQb2EtzcK8G0Fpw/en-us_image_0000002537925176.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E26E69FE4CB319B3D7C39417F45ADA203D68B7A106F5D5A12A57A4F0A984582)

**Figure 3** Effect of theme font 2

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/yM2DD7-WS5uENULl1wfzIQ/en-us_image_0000002568684953.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90081023AE9DDCAA4D62381EEF445902FD9A68172F317B8B6FEAB90C9B973DFD)
