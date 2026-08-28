# Obtaining and Using System Fonts (C/C++)

#### Scenario Introduction

System fonts are preset fonts of the operating system. They are used to display text when no custom font is specified, ensuring the readability and consistency of the text. The default system font is HarmonyOS Sans.

**Using system fonts** is applicable when an application does not register custom fonts or does not explicitly specify text styles. In this case, the system uses the default system font. In addition, there are multiple system fonts. You can obtain the configuration information about system fonts and switch and use system fonts based on the font family name in the information.

**Disabling system fonts** is applicable when you want to ensure that only custom fonts are used in an application and are not affected by the default fonts of the operating system. If the custom font does not exist, the system font is not disabled, and the system automatically falls back to the default font. By disabling system fonts, you can prevent the font from falling back to the default system font in any scenario, ensuring that text rendering meets the design expectation and unifying the visual style of the application.

#### Available APIs

The following table lists the common APIs and structures related to system fonts. For details about the APIs, see [Drawing](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing).

| Name | Description |
| :-- | :-- |
| OH\_Drawing\_FontConfigInfo\* OH\_Drawing\_GetSystemFontConfigInfo(OH\_Drawing\_FontConfigInfoErrorCode\*) | Obtains the configuration information about system fonts. The OH\_Drawing\_FontConfigInfo structure is returned. |
| void OH\_Drawing\_DestroySystemFontConfigInfo(OH\_Drawing\_FontConfigInfo\*) | Reclaims the memory occupied by the system font configuration. |
| OH\_Drawing\_FontCollection\* OH\_Drawing\_CreateSharedFontCollection(void) | Creates an OH\_Drawing\_FontCollection object that can be shared. |
| OH\_Drawing\_TextStyle\* OH\_Drawing\_CreateTextStyle(void) | Creates a pointer to the OH\_Drawing\_TextStyle object to set the text style. |
| OH\_Drawing\_SetTextStyleFontFamilies (OH\_Drawing\_TextStyle \*, int, const char \*fontFamilies\[\]) | Sets the font families for a text style. |
| void OH\_Drawing\_DisableFontCollectionSystemFont(OH\_Drawing\_FontCollection\* fontCollection) | Disables the system fonts. |

| Structure Name | Description |
| :-- | :-- |
| OH\_Drawing\_FontConfigInfo | Describes the information about a system font configuration. |
| OH\_Drawing\_FontGenericInfo | Describes the information about generic fonts supported by the system. |
| OH\_Drawing\_FontFallbackGroup | Describes the information about a font fallback group. |

#### Obtaining System Font Information

1.  Add the following lib to the src/main/cpp/CMakeLists.txt file of the project:
    
    libnative\_drawing.so
    
2.  Import the required header files.
    
    #include <native\_drawing/drawing\_font\_collection.h>
    #include <native\_drawing/drawing\_text\_typography.h>
    #include <native\_drawing/drawing\_register\_font.h>
    #include <hilog/log.h>
    
3.  Obtains the system font configuration information. You can determine whether the information is successfully obtained based on the returned status code. For details about the status code and its meaning, see [OH\_Drawing\_FontConfigInfoErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-text-typography-h#oh_drawing_fontconfiginfoerrorcode).
    
    OH\_Drawing\_FontConfigInfoErrorCode fontConfigInfoErrorCode; // Used to receive the error code.
    OH\_Drawing\_FontConfigInfo\* fontConfigInfo = OH\_Drawing\_GetSystemFontConfigInfo(&fontConfigInfoErrorCode);
    if(fontConfigInfoErrorCode != SUCCESS\_FONT\_CONFIG\_INFO) {
        OH\_LOG\_Print (LOG\_APP, LOG\_ERROR, LOG\_DOMAIN, "PrintSysFontMetrics", "Failed to obtain the system information. The error code is %{public}d");
    }
    
4.  [OH\_Drawing\_FontConfigInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-oh-drawing-fontconfiginfo) contains the following information:
    
    -   Number of system font file paths.
        
    -   Number of generic font sets.
        
    -   Number of font fallbacks.
        
    -   Double pointer to the system font file paths.
        
    -   Common font set list. For details, see [OH\_Drawing\_FontGenericInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-oh-drawing-fontgenericinfo).
        
    -   Backup font set list. For details, see [OH\_Drawing\_FontFallbackGroup](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-oh-drawing-fontfallbackgroup).
        
    
    The following example shows how to obtain some specific configuration information about system fonts:
    
    // Example for obtaining system font configuration information
    if (fontConfigInfo != nullptr) {
        // Obtain the number of font file paths and print logs.
        size\_t fontDirCount = fontConfigInfo->fontDirSize;
        OH\_LOG\_Print (LOG\_APP, LOG\_INFO, LOG\_DOMAIN, "PrintSysFontMetrics", "The number of font file paths is: %{public}zu\\n", fontDirCount);
        // Iterate through the font file path list and print logs.
        for (size\_t i = 0; i < fontDirCount; ++i) {
            OH\_LOG\_Print (LOG\_APP, LOG\_INFO, LOG\_DOMAIN, "PrintSysFontMetrics", "The font file path is: %{public}s\\n",
                         fontConfigInfo->fontDirSet\[i\]);
        }
        // Obtain the number of common font sets and print logs.
        size\_t genericCount = fontConfigInfo->fontGenericInfoSize;
        OH\_LOG\_Print (LOG\_APP, LOG\_INFO, LOG\_DOMAIN, "PrintSysFontMetrics", "The number of generic font families is: %{public}zu\\n", genericCount);
        // Iterate through the font family names (for example, HarmonyOS Sans) in each common font set and print logs.
        for (size\_t i = 0; i < genericCount; ++i) {
            OH\_Drawing\_FontGenericInfo &genericInfo = fontConfigInfo->fontGenericInfoSet\[i\];
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_DOMAIN, "PrintSysFontMetrics",
                         "Obtain the font family name of the %{public}s", i, genericInfo.familyName) in the %{public}zu generic font family;
        }
    }
    
    The following log example displays display system font configuration information. The configuration information varies depending on the device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/hMdiYetVT02F_gbykQL6QQ/en-us_image_0000002537925180.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5655C7277CEBBFCD5212C34A7B1CBA8F5666B05E5EB588F6C8C07D9450652580)
    
5.  If the system font configuration information is no longer required, release the memory occupied by the configuration information.
    
    OH\_Drawing\_DestroySystemFontConfigInfo(fontConfigInfo);
    

#### Using or Switching System Fonts

You can obtain the system font configuration information and then switch and use the system font based on the font family name.

If no font is specified, the default system font HarmonyOS Sans is used to display text.

1.  Add the following lib to the src/main/cpp/CMakeLists.txt file of the project:
    
    libnative\_drawing.so
    
2.  Import the required header files.
    
    #include <native\_drawing/drawing\_font\_collection.h>
    #include <native\_drawing/drawing\_text\_typography.h>
    #include <native\_drawing/drawing\_register\_font.h>
    #include <hilog/log.h>
    
3.  Create a font manager. You are advised to use OH\_Drawing\_CreateSharedFontCollection to create a shared font set object.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/Y2Y3RU4zRRWS2lDm0BlR5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C87829854D43E83675A2C9FC57370A18CFA8D7ECB13A3FEFFA3D924435C4BD3D)
    
    Both OH\_Drawing\_CreateFontCollection and OH\_Drawing\_CreateSharedFontCollection can be used to create the font manager OH\_Drawing\_FontCollection object. However, the font set pointer object created by OH\_Drawing\_CreateFontCollection can be used by only one paragraph generator OH\_Drawing\_TypographyCreate object and cannot be shared by multiple paragraph generator OH\_Drawing\_TypographyCreate objects. If the font set object needs to be shared by multiple paragraph generator OH\_Drawing\_TypographyCreate objects, use OH\_Drawing\_CreateSharedFontCollection to create a shared font set object.
    
    OH\_Drawing\_FontCollection \*fontCollection = OH\_Drawing\_CreateSharedFontCollection();
    
4.  Create a text style object OH\_Drawing\_TextStyle to set the text style.
    
    OH\_Drawing\_TextStyle\* textStyle = OH\_Drawing\_CreateTextStyle();
    
5.  [Obtaining system font information](#obtaining-system-font-information). Obtain the font family name of the system font and set the system font in the text style.
    
    //Case 1: Set the system font to HarmonyOS Sans Condensed.
    const char \*myFontFamilies\[\] = {"HarmonyOS Sans Condensed"};
    OH\_Drawing\_SetTextStyleFontFamilies(textStyle, 1, myFontFamilies);
    
    //Case 2: Do not set the system font. The default system font HarmonyOS Sans is used.
    // const char\* myFontFamilies\[\] = {"HarmonyOS Sans Condensed"};
    // OH\_Drawing\_SetTextStyleFontFamilies(textStyle, 1, myFontFamilies);
    
6.  Generate the final paragraph text to implement final text drawing and display.
    
    //Case 1: Set the system font to HarmonyOS Sans Condensed.
    const char \*myFontFamilies\[\] = {"HarmonyOS Sans Condensed"};
    OH\_Drawing\_SetTextStyleFontFamilies(textStyle, 1, myFontFamilies);
    
    //Case 2: Do not set the system font. The default system font HarmonyOS Sans is used.
    // const char\* myFontFamilies\[\] = {"HarmonyOS Sans Condensed"};
    // OH\_Drawing\_SetTextStyleFontFamilies(textStyle, 1, myFontFamilies);
    

#### Disabling the System Font

If the custom font does not exist, the system font is not disabled. The system automatically falls back to the default font. By disabling the system font, you can prevent the font from falling back to the default system font in any scenario, ensuring that the text rendering meets the design expectation and unifying the visual style of the application.

In some application scenarios, you may want to use only custom fonts to ensure font consistency or provide a more personalized user experience. In this case, you can disable the system font to ensure that the application uses only the registered custom font instead of the system font.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/y1StPTdXRc2k4nO62gQrSg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8309FF3D58CA62B1405FE73C3D7CA8DADF5A217854968CD2A6B3BFDBE3C1B0FF)

After disabling the system font, ensure that the custom font is registered. Otherwise, the text cannot be properly displayed.

1.  Ensure that the custom font has been successfully registered to ensure that the text can be properly displayed after the system font is disabled. For details, see [Registering and Using Custom Fonts](../registering-and-using-custom-fonts-c-c/document.md).
    
2.  Add the following lib to the src/main/cpp/CMakeLists.txt file of the project.
    
    libnative\_drawing.so
    
3.  Import the header files related to dependencies.
    
    #include <native\_drawing/drawing\_font\_collection.h>
    #include <native\_drawing/drawing\_text\_typography.h>
    #include <native\_drawing/drawing\_register\_font.h>
    #include <hilog/log.h>
    
4.  Create a font manager. You are advised to use OH\_Drawing\_CreateSharedFontCollection to create a shareable font set object.
    
    OH\_Drawing\_FontCollection \*fontCollection = OH\_Drawing\_CreateSharedFontCollection();
    
5.  Disables the system fonts.
    
    OH\_Drawing\_DisableFontCollectionSystemFont(fontCollection);
    
6.  Creates a text style object and uses the custom font that has been successfully registered.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/7Y_NoKPQTIKMJj6lvPFUmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DA881121619C8A597B6CAB90D99AC634971D2847584BAEE2ED057BE0A977EAA)
    
    If no font is set, the system font is used by default. If the system font is disabled and no custom font is set, the text cannot be displayed properly.
    
    OH\_Drawing\_TextStyle \*textStyle = OH\_Drawing\_CreateTextStyle();
    // After the system font is disabled, the following situations occur:
    // Situation 1: If a custom font is used, the text is displayed properly.
    // This path is the path of the custom font file to be registered on the application device. Ensure that the custom font file is correctly placed in this path.
    // When using the custom font, you need to use the font family name.
    const char\* fontFamily = "HarmonyOS\_Sans";
    const char\* fontPath = "/system/fonts/HarmonyOS\_Sans.ttf";
    // Return value 0: success; 1: file not found; 2: file opening failure; 3: file reading failure; 4: file search failure; 5: file size obtaining failure; 9: file damage
    int errorCode = OH\_Drawing\_RegisterFont(fontCollection, fontFamily, fontPath);
    DRAWING\_LOGI("errorCode = %{public}d", errorCode);
    const char \*myFontFamilies\[\] = {"HarmonyOS\_Sans"}; // Ensure that the custom font has been successfully registered and enter the font family name of the custom font.
    OH\_Drawing\_SetTextStyleFontFamilies(textStyle, 1, myFontFamilies);
    
    // Situation 2: If the system font is used, the text cannot be displayed.
    // const char \*myFontFamilies\[\] = {"HarmonyOS\_Sans"};
    // OH\_Drawing\_SetTextStyleFontFamilies(textStyle, 1, myFontFamilies);
    
    // Situation 3: If no font is set, the system default font is used by default. However, the system font has been disabled. As a result, the text cannot be displayed.
    // const char \*myFontFamilies\[\] = {"HarmonyOS\_Sans"};
    // OH\_Drawing\_SetTextStyleFontFamilies(textStyle, 1, myFontFamilies);
    
7.  Generates the final paragraph text to implement the final text drawing and display.
    
    //Set other text styles.
    OH\_Drawing\_SetTextStyleColor(textStyle, OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
    // Set the font size to 30.0.
    OH\_Drawing\_SetTextStyleFontSize(textStyle, 30.0);
    //Create a paragraph style object to set the typesetting style.
    OH\_Drawing\_TypographyStyle \*typographyStyle = OH\_Drawing\_CreateTypographyStyle();
    OH\_Drawing\_SetTypographyTextAlign(typographyStyle, TEXT\_ALIGN\_LEFT); //Set the paragraph style to left alignment.
    //Create a paragraph generator.
    OH\_Drawing\_TypographyCreate \*handler = OH\_Drawing\_CreateTypographyHandler(typographyStyle, fontCollection);
    //Set the text style in the paragraph generator.
    OH\_Drawing\_TypographyHandlerPushTextStyle(handler, textStyle);
    //Set the text content in the paragraph generator.
    const char \*text = "Hello World.\\nThe preceding text uses the custom font.";
    OH\_Drawing\_TypographyHandlerAddText(handler, text);
    // Generate a paragraph through the paragraph generator.
    OH\_Drawing\_Typography \*typography = OH\_Drawing\_CreateTypography(handler);
        
    // Set the maximum width.
    double maxWidth = width\_;
    OH\_Drawing\_TypographyLayout(typography, maxWidth);
    // Draw the text on the canvas (width\_/5.0,height\_/2.0).
    OH\_Drawing\_TypographyPaint(typography, cCanvas\_, width\_ / 5.0, height\_ / 2.0);
