# Registering and Using Custom Fonts (ArkTS)

#### Overview

Custom fonts are fonts created or selected by developers based on application requirements. They are usually used to implement specific text styles or fulfill distinct design goals. To render specific text styles and characters, applications can register and use custom fonts.

#### Workflow

**Registering custom fonts** is to register font files (such as .ttf and .otf files) from application resources to the system so that applications can use these fonts for text rendering. The registration process is to register font files with the system font library through the font management API so that the font files can be called in the application.

**Using custom fonts** is to explicitly specify registered custom fonts for text rendering in an application. You can select a specific text style (such as regular, bold, and italic) as required and apply it to UI elements, text controls, or other text display areas to meet design requirements and provide consistent visual effect.

#### Available APIs

The following table lists the APIs for registering and using theme fonts. For details, see [@ohos.graphics.text (Text)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-graphics-text).

| API | Description |
| :-- | :-- |
| loadFontSync(name: string, path: string | Resource): void | 
Registers a font from a file in the specified path. This API returns the result synchronously.

**NOTE**

Ensure that the custom font has been registered. If performance is not a critical concern, you are advised to use the synchronous API.

 |
| loadFont(name: string, path: string | Resource): Promise<void> | Registers a font based on the specified name and file path. This API uses a promise to return the result. This API is supported since API version 14. |
| unloadFontSync(name: string): void | Unregisters a font based on the specified name. This API is synchronous. This API is supported since API version 20. |
| unloadFont(name: string): Promise<void> | Unregisters a font based on the specified name. This API uses a promise to return the result. This API is supported since API version 20. |

#### How to Develop

1.  Import the required module.
    
    import { NodeController, FrameNode, RenderNode, DrawContext } from '@kit.ArkUI'
    import { UIContext } from '@kit.ArkUI'
    import { text } from '@kit.ArkGraphics2D'
    
2.  Register a custom font. You can use either of the following methods:
    
    // Register the custom font.
    // Method 1: /system/fonts/NotoSansMalayalamUI-SemiBold.ttf is only an example. Replace the file path with the actual one.
    fontCollection.loadFontSync(familyName, 'file:///system/fonts/NotoSansMalayalamUI-SemiBold.ttf')
    // Method 2: Ensure that the custom font file myFontFile.ttf is stored in the entry/src/main/resources/rawfile directory of your application project.
    // fontCollection.loadFontSync(familyName, $rawfile('myFontFile.ttf'))
    
3.  Use the custom font.
    
    // Use the custom font.
    let myFontFamily: Array<string> = \[familyName\] // If a custom font has been registered, enter the font family name of the custom font.
    // Set the text style.
    let myTextStyle: text.TextStyle = {
      color: {
        alpha: 255,
        red: 255,
        green: 0,
        blue: 0
      },
      fontSize: 30,
      // Add the custom font to the text style.
      fontFamilies: myFontFamily
    };
    
4.  Create a paragraph style and use the font manager instance to construct a **ParagraphBuilder** instance.
    
    // Create a paragraph style object to set the typography style.
    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
      align: 3,
      wordBreak: text.WordBreak.NORMAL
    };
    // Create a paragraph generator.
    let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection)
    
5.  Build a paragraph.
    
    // Set the text style in the paragraph generator.
    paragraphBuilder.pushStyle(myTextStyle);
    // Set the text content in the paragraph generator.
    paragraphBuilder.addText("Custom font test");
    // Generate a paragraph using the paragraph generator.
    let paragraph = paragraphBuilder.build();
    
6.  To release a custom font, call the **unloadFontSync** API.
    
    // Unregister the custom font.
    fontCollection.unloadFontSync(familyName)
    // Refresh the node that uses fontCollection after the unregistration.
    newNode.invalidate()
    

#### Effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/IzXuXC8VS8yXJ6wzkSSDvg/en-us_image_0000002568764963.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8689EC3424FA900F634EAE7ECECD855D12FCA1EC80A9A0D4E3D07403278C982A)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/0Lx1miOwQF-xW8J6tXsdMA/en-us_image_0000002537765238.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B91B3F023E5F5FA8655DEA587F8E468CC1D7011BB5072F8209B473AD5543658B)
