# Registering and Using Custom Fonts (C/C++)

#### Overview

Custom fonts are created or selected by developers based on application requirements. They are usually used to implement specific text styles or meet unique design requirements. If an application needs to use a specific text style and character set, you can register and use custom fonts for text rendering.

#### Implementation Process

**Registering custom fonts** refers to registering font files (such as TTF and OTF files) from application resources to the system so that applications can use these fonts for text rendering. The registration process is to register font files with the system font library through the font management API so that the font files can be called in applications.

**Using custom fonts** refers to explicitly specifying registered custom fonts for text drawing in applications. You can select a specific text style (such as normal, bold, and italic) as required and apply it to UI elements, text controls, or other text display areas to ensure that the design requirements are met and a consistent visual effect is provided.

#### Available APIs

The following table lists the APIs for registering and using custom fonts. For details, see [Drawing](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing).

| Name | Description |
| :-- | :-- |
| OH\_Drawing\_CreateSharedFontCollection (void) | Creates a shareable font set object OH\_Drawing\_FontCollection. |
| OH\_Drawing\_RegisterFont (OH\_Drawing\_FontCollection\* , const char\* fontFamily, const char\* familySrc ) | Registers a custom font with the font manager. The supported font file formats are .ttf and .otf. |
| OH\_Drawing\_CreateTextStyle(void) | Creates a pointer to the OH\_Drawing\_TextStyle object to set the text style. |
| OH\_Drawing\_SetTextStyleFontFamilies (OH\_Drawing\_TextStyle \*, int, const char \*fontFamilies\[\]) | Sets the font families for a text style. |
| OH\_Drawing\_UnregisterFont (OH\_Drawing\_FontCollection\* , const char\* fontFamily) | Unregisters a custom font by font family name. |

#### How to Develop

1.  Add the following libraries to the src/main/cpp/CMakeLists.txt file of the project:
    
    libnative\_drawing.so
    
2.  Import the required header files.
    
    #include <native\_drawing/drawing\_font\_collection.h>
    #include <native\_drawing/drawing\_text\_typography.h>
    #include <native\_drawing/drawing\_register\_font.h>
    
3.  Create a font manager. You are advised to use OH\_Drawing\_CreateSharedFontCollection() to create a shared font set object.
    
    **Note:**
    
    Both OH\_Drawing\_CreateFontCollection() and OH\_Drawing\_CreateSharedFontCollection() can be used to create an OH\_Drawing\_FontCollection object. However, the font set pointer object created by OH\_Drawing\_CreateFontCollection() can be used by only one OH\_Drawing\_TypographyCreate object. If the font set object needs to be shared by multiple OH\_Drawing\_TypographyCreate objects, use OH\_Drawing\_CreateSharedFontCollection() to create a shared font set object.
    
    OH\_Drawing\_FontCollection \*fontCollection = OH\_Drawing\_CreateSharedFontCollection();
    
4.  Set the font family name and sandbox path of the custom font.
    
    **Note:**
    
    Ensure that the available custom font file to be registered is correctly placed in the /system/fonts/NotoSerifTamil\[wdth,wght\].ttf directory on the application device.
    
    //Use the font family name when using the custom font.
    const char\* fontFamily = "myFamilyName";
    //This path is the path of the custom font file to be registered on the application device. Ensure that the custom font file is correctly placed in this path.
    const char\* fontPath = "/system/fonts/NotoSerifTamil\[wdth,wght\].ttf";
    
5.  Register the custom font using OH\_Drawing\_RegisterFont() in the font manager.
    
    You can check the API return result to determine whether the registration is successful.
    
    The following lists the return results of the OH\_Drawing\_RegisterFont API and their meanings:
    
    0 indicates that the registration is successful, 1 indicates that the file does not exist, 2 indicates that the file fails to be opened, 3 indicates that the file fails to be read, 4 indicates that the file fails to be found, 5 indicates that the file size fails to be obtained, and 9 indicates that the file is damaged.
    
    // 0: success; 1: file not found; 2: file opening failure; 3: file reading failure; 4: file search failure; 5: file size obtaining failure; 9: file damage
    int errorCode = OH\_Drawing\_RegisterFont(fontCollection, fontFamily, fontPath);
    
6.  After the custom font is successfully registered, use the OH\_Drawing\_CreateTextStyle() API to create a text style object and use the OH\_Drawing\_SetTextStyleFontFamilies() API to add the custom font.
    
    //If the custom font has been successfully registered, enter the font family name of the custom font.
    const char\* myFontFamilies\[\] = {"myFamilyName"};
    //Add the custom font that can be used.
    OH\_Drawing\_SetTextStyleFontFamilies(textStyle, 1, myFontFamilies);
    
7.  Generate the final paragraph text and use the custom font to implement final text drawing and display.
    
    //Set other text styles.
    OH\_Drawing\_SetTextStyleColor(textStyle , OH\_Drawing\_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
    // Set the font size to 60.0.
    OH\_Drawing\_SetTextStyleFontSize(textStyle, 60.0);
    // Create a paragraph style object to set the typesetting style.
    OH\_Drawing\_TypographyStyle \*typographyStyle = OH\_Drawing\_CreateTypographyStyle();
    OH\_Drawing\_SetTypographyTextAlign(typographyStyle, TEXT\_ALIGN\_LEFT); // Set the paragraph style to left alignment.
    // Create a paragraph generator.
    OH\_Drawing\_TypographyCreate\* handler = OH\_Drawing\_CreateTypographyHandler(typographyStyle, fontCollection);
    // Set the text style in the paragraph generator.
    OH\_Drawing\_TypographyHandlerPushTextStyle(handler, textStyle);
    // Set the text content in the paragraph generator.
    const char\* text = "hello,This text uses a custom font";
    OH\_Drawing\_TypographyHandlerAddText(handler, text);
    // Generate a paragraph using the paragraph generator.
    OH\_Drawing\_Typography\* typography = OH\_Drawing\_CreateTypography(handler);
    // Set the maximum width.
    double maxWidth = width\_;
    OH\_Drawing\_TypographyLayout(typography, maxWidth);
    // Draw the text on the canvas (0,100).
    OH\_Drawing\_TypographyPaint(typography, cCanvas\_, 0, 100);
    
8.  To release a custom font, call OH\_Drawing\_UnregisterFont.
    
    // Unregister the custom font.
    OH\_Drawing\_UnregisterFont(fontCollection, fontFamily);
    OH\_Drawing\_TypographyCreate\* handler1 = OH\_Drawing\_CreateTypographyHandler(typographyStyle, fontCollection);
    // Set the text style in the paragraph generator.
    OH\_Drawing\_TypographyHandlerPushTextStyle(handler1, textStyle);
    // Set the text content in the paragraph generator.
    const char\* text1 = "hello,The custom font of this text is deregistered.";
    OH\_Drawing\_TypographyHandlerAddText(handler1, text1);
    // Generate a paragraph using the paragraph generator.
    OH\_Drawing\_Typography\* typography1 = OH\_Drawing\_CreateTypography(handler1);
    OH\_Drawing\_TypographyLayout(typography1, maxWidth);
    // Draw the text on the canvas (0,300).
    OH\_Drawing\_TypographyPaint(typography1, cCanvas\_, 0, 300);
