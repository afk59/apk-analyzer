# Class (Font)

Provides APIs for registering custom fonts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/Oep2hdklSWeouTEYjGmI0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67434E34AFB0E099D3C2ED0DE506F1125DAB87B976DF97B0B1C69677201A08B5)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 10.
    
-   In the following API examples, you must first use [getFont()](../class-uicontext/document.md#getfont) in **UIContext** to obtain a **Font** instance, and then call the APIs using the obtained instance.
    
-   You are advised to use the [loadFontSync](../../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#loadfontsync) API of the font engine to register custom fonts.
    

#### registerFont

registerFont(options: font.FontOptions): void

Registers a custom font with the font manager.

This API is asynchronous and does not support concurrent calls.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [font.FontOptions](../../ohos-font-custom-font-registration/document.md#fontoptions) | Yes | 
Information about the custom font to register.

**NOTE**

When setting the path to the font file, you are advised to use a string with the **file://** path prefix for resources within the system sandbox path. Ensure that the file exists in the sandbox directory path and has read permissions.

 |

**Example**

// xxx.ets
import { Font } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  private uiContext: UIContext = this.getUIContext();
  private font: Font = this.uiContext.getFont();

  aboutToAppear() {
    this.font.registerFont({
      familyName: 'medium',
      familySrc: '/font/medium.ttf' // The font folder is at the same level as the pages folder.
    })
  }

  build() {
    Column() {
      Text(this.message)
        .align(Alignment.Center)
        .fontSize(20)
        .fontFamily('medium') // medium: name of the registered custom font. (Registered fonts such as $r('app.string.mediumFamilyName') and 'mediumRawFile' can also be used.)
    }.width('100%')
  }
}

#### getSystemFontList

getSystemFontList(): Array<string>

Obtains the list of supported fonts.

This API only takes effect on PCs/2-in-1 devices and returns an empty array on other devices.

You are advised to use the [getSystemFontFullNamesByType](../../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#textgetsystemfontfullnamesbytype14) API to obtain the latest system-supported font list data.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | List of supported fonts. |

**Example**

// xxx.ets
import { Font } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private uiContext: UIContext = this.getUIContext();
  private font: Font = this.uiContext.getFont();
  fontList: Array<string> = new Array<string>();

  build() {
    Column() {
      Button("getSystemFontList")
        .width('60%')
        .height('6%')
        .onClick(() => {
          this.fontList = this.font.getSystemFontList();
          console.info('getSystemFontList', JSON.stringify(this.fontList))
        })
    }.width('100%')
  }
}

#### getFontByName

getFontByName(fontName: string): font.FontInfo

Obtains information about a system font based on the font name.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fontName | string | Yes | System font name. |

**Return value**

| Type | Description |
| :-- | :-- |
| [font.FontInfo](../../ohos-font-custom-font-registration/document.md#fontinfo10) | 
Detailed information of the font.

If no font is found, **undefined** is returned.

 |

**Example**

// xxx.ets
import { Font, font } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private uiContext: UIContext = this.getUIContext();
  private font: Font = this.uiContext.getFont();
  fontInfo: font.FontInfo = this.font.getFontByName('');

  build() {
    Column() {
      Button("getFontByName")
        .width('60%')
        .height('6%')
        .onClick(() => {
          this.fontInfo = this.font.getFontByName('HarmonyOS Sans Italic');
          console.info("getFontByName(): path = " + this.fontInfo.path);
          console.info("getFontByName(): postScriptName = " + this.fontInfo.postScriptName);
          console.info("getFontByName(): fullName = " + this.fontInfo.fullName);
          console.info("getFontByName(): family = " + this.fontInfo.family);
          console.info("getFontByName(): subfamily = " + this.fontInfo.subfamily);
          console.info("getFontByName(): weight = " + this.fontInfo.weight);
          console.info("getFontByName(): width = " + this.fontInfo.width);
          console.info("getFontByName(): italic = " + this.fontInfo.italic);
          console.info("getFontByName(): monoSpace = " + this.fontInfo.monoSpace);
          console.info("getFontByName(): symbolic = " + this.fontInfo.symbolic);
        })
    }.width('100%')
  }
}
