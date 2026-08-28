# @ohos.font (Custom Font Registration)

The **font** module provides APIs for registering custom fonts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/sLJr2zmxQpKFofAbmeXtvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A417236DF13715BB7076904DEEC8ADAD5948CDF07D9BD493DEAC87D70FE73545)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The functionality of this module depends on UI context. This means that the APIs of this module cannot be used where [the UI context is ambiguous](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). For details, see [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   You are advised to use the [loadFontSync](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#loadfontsync) API of the font engine to register custom fonts.
    

#### Modules to Import

import { font } from '@kit.ArkUI';

#### font.registerFont(deprecated)

registerFont(options: FontOptions): void

Registers a custom font with the font manager.

This API is asynchronous and does not support concurrent calls.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/ali5Z4FBSnSqom3Q2eYNpA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F9009285CCF1E30F37E28F442A7DF37CDB4F59BFDFD9502D9B66AFEA306C059F)

-   This API is supported since API version 9 and deprecated since API version 18. You are advised to use [registerFont](../ohos-arkui-uicontext-uicontext/class-font/document.md#registerfont) instead. Before calling this API, you need to obtain the [Font](../ohos-arkui-uicontext-uicontext/class-font/document.md) object using the [getFont](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getfont) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md). Directly using **registerFont** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context).
    
-   Since API version 10, you can use the [getFont](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getfont) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Font](../ohos-arkui-uicontext-uicontext/class-font/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [FontOptions](#fontoptions) | Yes | Information about the custom font to register. |

#### FontOptions

Information about the custom font to register.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| familyName | string | [Resource](../../../arkts-components/common-definitions/basic-types/document.md#resource)10+ | No | No | Name of the custom font to register. |
| familySrc | string | [Resource](../../../arkts-components/common-definitions/basic-types/document.md#resource)10+ | No | No | 
Path of the custom font file to register.

**NOTE**

If the font file to specify is a resource located within the system sandbox directory, you are advised to use a string with the **file://** path prefix. Ensure the target file exists in the sandbox path and has read permissions granted.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Vyt5EIpJTGuJ5aZSzAxS3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=338ECF39E1A95F4A10044D74257A08BE731FCCCDD3F16E1F9C49CEA99A6FE772)

Directly using **font** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). To avoid this, obtain the [Font](../ohos-arkui-uicontext-uicontext/class-font/document.md) object associated with the current UI context by using the [getFont](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getfont) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).

**Example**

// xxx.ets
@Entry
@Component
struct FontExample {
  @State message: string = 'Hello World';
  // iconFont example, where 0000 is the Unicode character of the specified icon. You need to obtain the Unicode character from the TTF file of the registered iconFont.
  @State unicode: string = '\\u0000';
  @State codePoint: string = String.fromCharCode(0x0000);
  private uiContext: UIContext = this.getUIContext();

  aboutToAppear() {
    // Both familyName and familySrc support the Resource type.
    this.uiContext.getFont().registerFont({
      // You are advised to use this.getUIContext().getFont().registerFont().
      // Replace 'app.string.font\_name' and 'app.string.font\_src' with the actual resource strings.
      familyName: $r('app.string.font\_name'),
      familySrc: $r('app.string.font\_src')
    })

    // familySrc supports the RawFile type.
    this.uiContext.getFont().registerFont({
      familyName: 'mediumRawFile',
      familySrc: $rawfile('font/medium.ttf')// 'font/medium.ttf' is used only as an example. Replace it with the font resource file you use.
    })

    // Register iconFont.
    this.uiContext.getFont().registerFont({
      familyName: 'iconFont',
      familySrc: '/font/iconFont.ttf'
    })

    // Both familyName and familySrc support the string type.
    this.uiContext.getFont().registerFont({
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

      // Two methods of using iconFont
      Text(this.unicode)
        .align(Alignment.Center)
        .fontSize(20)
        .fontFamily('iconFont')
      Text(this.codePoint)
        .align(Alignment.Center)
        .fontSize(20)
        .fontFamily('iconFont')
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/AePuzPpWQKeKk0uAcdKs4g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA1534F1A16C96630E6CF875E74061006C83AD0B1A1EB9CF43C7CEA586285CCA)

To use custom fonts globally in an application, register the fonts through the [windowStage.loadContent](../../window-manager/ohos-window-window/interface-window/document.md#loadcontent9) API in the [onWindowStageCreate](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md#onwindowstagecreate) lifecycle callback in the **EntryAbility.ets** file.

In HSP projects, avoid using relative paths to register custom fonts. For details, see [Accessing Resources in an HSP Through $r](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/in-app-hsp).

#### font.getSystemFontList(deprecated)

getSystemFontList(): Array<string>

Obtains the system font list.

This API only takes effect on PCs/2-in-1 devices and returns an empty array on other devices.

You are advised to use the [getSystemFontFullNamesByType](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#textgetsystemfontfullnamesbytype14) API to obtain the latest system-supported font list data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/C1dbh2B8To-3-1DsWeTLjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F54802C85678B9C3D75A1CD304B398C382ECD4367DAE0FFACB3C52B7309B4B59)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [getSystemFontList](../ohos-arkui-uicontext-uicontext/class-font/document.md#getsystemfontlist) instead. Before calling this API, you need to obtain the [Font](../ohos-arkui-uicontext-uicontext/class-font/document.md) object using the [getFont](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getfont) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md). Directly using **getSystemFontList** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context).
    
-   Since API version 10, you can use the [getFont](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getfont) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Font](../ohos-arkui-uicontext-uicontext/class-font/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | List of supported fonts. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/HGlsPxtvQUKiuykqHoI4vA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=01A5A9257A5C4B3DB70CC2992CA980B397397FCA20863FC0410A8C49BACCAE92)

Directly using **font** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). To avoid this, obtain the [Font](../ohos-arkui-uicontext-uicontext/class-font/document.md) object associated with the current UI context by using the [getFont](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getfont) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).

**Example**

// xxx.ets
import { font } from '@kit.ArkUI';

@Entry
@Component
struct FontExample {
  fontList: Array<string> = new Array<string>();

  build() {
    Column() {
      Button("getSystemFontList")
        .width('60%')
        .height('6%')
        .onClick(() => {
          this.fontList = font.getSystemFontList(); // You are advised to use the this.getUIContext().getFont().getSystemFontList() API.
        })
    }.width('100%')
  }
}

#### font.getFontByName(deprecated)

getFontByName(fontName: string): FontInfo

Obtains information about a system font based on the font name.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/gZM9vqNVQGWEaEQ_QxqXFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=76C19DC12F4D68DC06D189762FDFF225C77840E44F68C1AC9823E470698D060B)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [getFontByName](../ohos-arkui-uicontext-uicontext/class-font/document.md#getfontbyname) instead. Before calling this API, you need to obtain the [Font](../ohos-arkui-uicontext-uicontext/class-font/document.md) object using the [getFont](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getfont) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md). Directly using **getFontByName** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context).
    
-   Since API version 10, you can use the [getFont](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getfont) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [Font](../ohos-arkui-uicontext-uicontext/class-font/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fontName | string | Yes | System font name. |

**Return value**

| Type | Description |
| :-- | :-- |
| FontInfo | Information about the system font. |

#### FontInfo10+

Information about the system font.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| path | string | No | No | File path of the system font. |
| postScriptName | string | No | No | PostScript name of the system font. |
| fullName | string | No | No | Name of the system font. |
| family | string | No | No | Family of the system font. |
| subfamily | string | No | No | Subfamily of the system font. |
| weight | number | No | No | 
Weight of the system font.

Value range: \[100, 900\], with intervals of 100, corresponding to the values in the [FontWeight](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#fontweight) enum

Default value: **100**

 |
| width | number | No | No | 

Width of the system font.

Value range: \[1, 9\], with intervals of 1, corresponding to the values in the [FontWidth](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#fontwidth) enum

 |
| italic | boolean | No | No | 

Whether the system font is italic.

Default value: **false**

**true**: The system font is italic. **false**: The system font is not italic.

 |
| monoSpace | boolean | No | No | 

Whether the system font is monospaced.

Default value: **false**

**true**: The system font is monospaced. **false**: The system font is not monospaced.

 |
| symbolic | boolean | No | No | 

Whether the system font supports symbols.

Default value: **false**

**true**: The system font supports symbols. **false**: The system font does not support symbols.

 |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/pr1MAMUKTD-fTPJjNr78FQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3B2EB0F60B3B20127D2A2693EBB816F8BC4B28C96CA283DA105B756B279D844)

Directly using **font** can lead to the issue of ambiguous UI context. To avoid this, obtain the [Font](../ohos-arkui-uicontext-uicontext/class-font/document.md) object associated with the current UI context by using the [getFont](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getfont) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).

// xxx.ets
import { font } from '@kit.ArkUI';

@Entry
@Component
struct FontExample {
  fontList: Array<string> = new Array<string>();
  uiFont = this.getUIContext().getFont();
  fontInfo: font.FontInfo = this.uiFont.getFontByName(''); // You are advised to use the this.getUIContext().getFont().getFontByName() API.

  build() {
    Column() {
      Button("getFontByName")
        .onClick(() => {
          this.fontInfo =
            this.uiFont.getFontByName('HarmonyOS Sans Italic');
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

#### font.getUIFontConfig11+

getUIFontConfig() : UIFontConfig

Obtains the UI font configuration information in the system font configuration file.

This API can only obtain the information in the configuration file. If the UI context is not clear, **undefined** may be returned. If you want to obtain the full font configuration information, you are advised to use the [getSystemFontFullNamesByType](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-text-text/document.md#textgetsystemfontfullnamesbytype14) API of the font engine.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [UIFontConfig](#uifontconfig11) | UI font configuration of the system. |

#### UIFontConfig11+

UI font configuration of the system.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fontDir | Array<string> | No | No | Path to the system font file. |
| generic | Array<[UIFontGenericInfo](#uifontgenericinfo11)\> | No | No | List of supported generic font families. |
| fallbackGroups | Array<[UIFontFallbackGroupInfo](#uifontfallbackgroupinfo11)\> | No | No | List of fallback generic font families. |

#### UIFontGenericInfo11+

Defines a list of supported generic font families.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| family | string | No | No | Font family name, which is the value of **family** specified in the font file. |
| alias | Array<[UIFontAliasInfo](#uifontaliasinfo11)\> | No | No | Font alias configuration information. |
| adjust | Array<[UIFontAdjustInfo](#uifontadjustinfo11)\> | No | No | Weight of the font when displayed, which corresponds to the original weight. |

#### UIFontFallbackGroupInfo11+

Defines a list of fallback generic font families.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fontSetName | string | No | No | Name of the font family corresponding to the fallback fonts. |
| fallback | Array<[UIFontFallbackInfo](#uifontfallbackinfo11)\> | No | No | Fallback fonts for the font family. If **fontSetName** is **""**, it indicates that the fonts can be used as fallback fonts for all font families. |

#### UIFontAliasInfo11+

Defines font alias configuration information.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Alias name. |
| weight | number | No | No | 
Weight of the fonts included in the font family. If the value is greater than 0, the font family contains only the fonts with the specified weight. If the value is 0, the font family contains all fonts.

Valid values are **0**, **100**, **400**, **700**, and **900**.

 |

#### UIFontAdjustInfo11+

Provides a mapping list between the original weight value of a font and the actual displayed weight value.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| weight | number | No | No | 
Original weight of the font.

Valid values are **50**, **80**, **100**, and **200**.

 |
| to | number | No | No | 

Weight of the font displayed in the application.

Valid values are **100**, **400**, **700**, and **900**.

 |

#### UIFontFallbackInfo11+

Provides the fallback font of the font set.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| language | string | No | No | Language supported by the font family. The language format is BCP 47. |
| family | string | No | No | Font family name, which is the value of **family** specified in the font file. |

**Example**

// xxx.ets
import { font } from '@kit.ArkUI';

@Entry
@Component
struct FontExample {
  build() {
    Column() {
      Button("getUIFontConfig")
        .width('60%')
        .height('6%')
        .margin(50)
        .onClick(() => {
          let fontConfig = font.getUIFontConfig();
          console.info("font-dir -----------" + String(fontConfig.fontDir.length));
          for (let i = 0; i < fontConfig.fontDir.length; i++) {
            console.info(fontConfig.fontDir\[i\]);
          }
          console.info("generic-------------" + String(fontConfig.generic.length));
          for (let i = 0; i < fontConfig.generic.length; i++) {
            console.info("family:" + fontConfig.generic\[i\].family);
            for (let j = 0; j < fontConfig.generic\[i\].alias.length; j++) {
              console.info(fontConfig.generic\[i\].alias\[j\].name + " " + fontConfig.generic\[i\].alias\[j\].weight);
            }
            for (let j = 0; j < fontConfig.generic\[i\].adjust.length; j++) {
              console.info(fontConfig.generic\[i\].adjust\[j\].weight + " " + fontConfig.generic\[i\].adjust\[j\].to);
            }
          }
          console.info("fallback------------" + String(fontConfig.fallbackGroups.length));
          for (let i = 0; i < fontConfig.fallbackGroups.length; i++) {
            console.info("fontSetName:" + fontConfig.fallbackGroups\[i\].fontSetName);
            for (let j = 0; j < fontConfig.fallbackGroups\[i\].fallback.length; j++) {
              console.info("language:" + fontConfig.fallbackGroups\[i\].fallback\[j\].language + " family:" +
              fontConfig.fallbackGroups\[i\].fallback\[j\].family);
            }
          }
        })
    }.width('100%')
  }
}
