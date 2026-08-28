# Using Theme Fonts (C/C++)

#### Overview

Theme fonts are specialized custom fonts available for use in theme applications. You can enable them using specific APIs.

#### Implementation Mechanism

**Figure 1** Switching and using theme fonts

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/2emA-eKwQy-UC8nayEjz6A/en-us_image_0000002537765236.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F76B218E856767289C37359CEF135AC27F252CC0001899D25D15438A056B380A)

When switching and using theme fonts, the application must subscribe to theme font change events. After receiving such an event, it must call the page refresh API to switch the theme font. Without this step, the new theme font will apply only after the application is restarted. To draw text with a theme font, use **OH\_Drawing\_GetFontCollectionGlobalInstance** to obtain the global font collection object, which contains theme font information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/MNSDeXbOQlCmQtkCcUdwtg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1942EFC9AFF909386D0B991D64625786FABBE526DC00F90BC99D0DB0D1C69AC5)

You cannot use **OH\_Drawing\_CreateSharedFontCollection** to draw text with a theme font because this API returns a font collection object that does not contain any theme font information.

#### Available APIs

The following table lists the APIs for registering and using theme fonts. For details, see [Drawing](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing).

| Name | Description |
| :-- | :-- |
| OH\_Drawing\_FontCollection\* OH\_Drawing\_GetFontCollectionGlobalInstance(void) | Obtains an **OH\_Drawing\_FontCollection** object. |
| [onConfigurationUpdate()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-ability#abilityonconfigurationupdate) | 
Called when system configuration is updated.

Currently, theme applications provide only an ArkTS API to publish change events. Therefore, cross-language calling is required for your application.

 |

#### How to Develop

1.  Make sure that you can apply a theme font in the theme applications on your device.
    
2.  Override the **onConfigurationUpdate** function in the application entry file (**EntryAbility.ets** in the default project) to respond to **fontId** changes, adapt to theme font switching, and refresh pages. For details, see [Using Theme Fonts (ArkTS)](../using-theme-fonts-arkts/document.md#how-to-develop).
    
    When the system configuration information (**newConfig** in the example) changes, the **onConfigurationUpdate** function is triggered. The application can obtain the **fontId** from the configuration information sent by the system and determine whether the **fontId** is the same as that saved locally to identify the theme font switching. If they are different, update the local **fontId** and call the C++ code to update the typography result. The call path from ArkTS to C++ requires the application to select the appropriate calling method based on actual scenarios, and no recommendation is provided in this example. For details about cross-language calling, see [Node-API Overview](../../../../../ndk-development/code-development/using-node-api/node-api-overview/document.md).
    
3.  Import the C++ dependencies. This step and subsequent steps describe the usage of theme fonts on the C++ side.
    
    Add the following library to the src/main/cpp/CMakeLists.txt file of the project.
    
    libnative\_drawing.so
    
    Include header files.
    
    #include <native\_drawing/drawing\_font\_collection.h>
    #include <native\_drawing/drawing\_text\_typography.h>
    #include <native\_drawing/drawing\_register\_font.h>
    
4.  Create a font manager.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/7nw2fvssRzWn-AZsfRJMVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2C790418B4272422EFE5623ABA1738EA0D34B3356F1F333CFB6CBFF376427DC)
    
    The registered theme fonts are used for the global font collection object. Therefore, you must use **OH\_Drawing\_GetFontCollectionGlobalInstance**. If you use **OH\_Drawing\_CreateSharedFontCollection** or **OH\_Drawing\_CreateFontCollection**, the theme fonts will be unavailable. The global font collection object obtained by **OH\_Drawing\_GetFontCollectionGlobalInstance** cannot be released because it can lead to disordered font rendering.
    
    OH\_Drawing\_FontCollection \*fontCollection = OH\_Drawing\_GetFontCollectionGlobalInstance();
    
5.  **OH\_Drawing\_SetTextStyleFontFamilies()** can be used to specify the font family name for implementing the specified font. However, to use a theme font, do not call **OH\_Drawing\_SetTextStyleFontFamilies()** to avoid using the specified font instead of the theme font.
    
    OH\_Drawing\_TextStyle \*myTextStyle = OH\_Drawing\_CreateTextStyle();
    // const char\* myFontFamilies\[\] = {"otherFontFamilyName"};
    // Do not use this API to specify the font.
    // OH\_Drawing\_SetTextStyleFontFamilies(textStyle, 1, myFontFamilies);
    
6.  Set the paragraph text content to "Hello World. \\nThis is the theme font." In this case, the theme font is used for the paragraph text.
    
    // Set other text styles.
    OH\_Drawing\_SetTextStyleColor(myTextStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
    // Set the font size to 100.0.
    OH\_Drawing\_SetTextStyleFontSize(myTextStyle, 100.0);
    // Create a paragraph style object to set the typography style.
    OH\_Drawing\_TypographyStyle \*typographyStyle = OH\_Drawing\_CreateTypographyStyle();
    OH\_Drawing\_SetTypographyTextAlign(typographyStyle, TEXT\_ALIGN\_LEFT); // Set the typography to left alignment.
    // Create a paragraph generator.
    OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typographyStyle, fontCollection);
    // Set the text style in the paragraph generator.
    OH\_Drawing\_TypographyHandlerPushTextStyle(handler, myTextStyle);
    // Set the text content in the paragraph generator.
    const char \*text = "Hello World. \\nThis is the theme font.";
    OH\_Drawing\_TypographyHandlerAddText(handler, text);
    // Generate a paragraph using the paragraph generator.
    OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
    

#### Effect

The following figures show how text is rendered with different theme fonts in a theme application.

The following figures are for reference only.

**Figure 2** Effect of theme font 1

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/It6oQUGUQ-Gt4oxVeqFGwA/en-us_image_0000002568764965.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37782B45D72B6AF7761167204996019773AB1C5200D8F9BE8A366943DA2396D4)

**Figure 3** Effect of theme font 2

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/8EiEYf_DQWiJMNoWgZFtRw/en-us_image_0000002537765240.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35DC105A5D8C19DD480E1FE844C657574B12150BA410B1D551070CCD0010596D)
