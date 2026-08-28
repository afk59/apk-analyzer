# WithTheme

The **WithTheme** component is designed to customize the theme style for a specific part of an application page. It allows for the setting of light and dark modes for child components, as well as the use of custom color schemes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/j1oWeOg2QJyliRF4-fPwrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F8095D83AC1A43288FB737A74B49877C7FD70C341A9F71A19BA0948CCCEF96F)

This component is supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

**WithTheme** supports the following built-in components: [TextInput](../../text-and-input/textinput/document.md), [Search](../../text-and-input/search/document.md), [Button](../../buttons-and-selections/button/document.md), [Badge](../../information-display/badge/document.md), [Swiper](../../scroll-and-swipe/swiper/document.md), [Text](../../text-and-input/text/document.md), [Select](../../buttons-and-selections/select/document.md), [Menu](../../menus/menu/document.md), [TimePicker](../../buttons-and-selections/timepicker/document.md), [DatePicker](../../buttons-and-selections/datepicker/document.md), [TextPicker](../../buttons-and-selections/textpicker/document.md), [Checkbox](../../buttons-and-selections/checkbox/document.md), [CheckboxGroup](../../buttons-and-selections/checkboxgroup/document.md), [Radio](../../buttons-and-selections/radio/document.md), [Slider](../../buttons-and-selections/slider/document.md), [Progress](../../information-display/progress/document.md), [QRCode](../../information-display/qrcode/document.md), [Toggle](../../buttons-and-selections/toggle/document.md), [PatternLock](../../information-display/patternlock/document.md), and [Divider](../../blank-and-divider/divider/document.md).

For details about how to use **WithTheme**, see [Configuring In-Application Theme Skinning](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/theme_skinning).

#### Child Components

This component supports only one child component.

#### APIs

WithTheme(options: WithThemeOptions)

Sets a custom theme style for specific application pages.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [WithThemeOptions](#withthemeoptions) | Yes | Color scheme for components within the scope. |

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### WithThemeOptions

Defines the default theme and color mode for components within the **WithTheme** scope.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| theme | [CustomTheme](#customtheme) | No | Yes | 
Default theme for components in the **WithTheme** scope.

Default value: **undefined**. The default style follows the [default token style](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/theme_skinning#system-default-token-color-values).

 |
| colorMode | [ThemeColorMode](../../universal-attributes/visual-effects/foreground-blur/document.md#themecolormode) | No | Yes | 

Color mode for components in the **WithTheme** scope.

Default value: **ThemeColorMode.SYSTEM**

 |

#### CustomTheme

type CustomTheme = CustomTheme

Defines a custom theme.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [CustomTheme](../../../arkts-api/ui/ohos-arkui-theme-theme/document.md#customtheme) | Default theme for components in the **WithTheme** scope. |

#### Example

For the light and dark modes to take effect, add a **dark.json** resource file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/pmyzcIkHQXud9l8HzB25zg/en-us_image_0000002568765667.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C75B84824368001191C9C52A1AF777B58B3217334E3733A3B531AF7AE58DAE05)

Example of the **dark.json** file content:

  {
    "color": \[
      {
        "name": "start\_window\_background",
        "value": "#000000"
      }
    \]
  }

## Example 1: Setting the Local Color Mode

// Set the local color mode.
@Entry
@Component
struct Index {
  build() {
    Column() {
    // System default
      Column() {
        Text('WithTheme not used')
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('33%')
      .backgroundColor($r('app.color.start\_window\_background'))
      // Set the component to the dark mode.
      WithTheme({ colorMode: ThemeColorMode.DARK }) {
        Column() {
          Text('WithTheme')
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
          Text('DARK')
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('33%')
        .backgroundColor($r('sys.color.background\_primary'))
      }
      // Set the component to the light mode.
      WithTheme({ colorMode: ThemeColorMode.LIGHT }) {
        Column() {
          Text('WithTheme')
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
          Text('LIGHT')
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('33%')
        .backgroundColor($r('sys.color.background\_primary'))
      }
    }
    .height('100%')
    .expandSafeArea(\[SafeAreaType.SYSTEM\], \[SafeAreaEdge.TOP, SafeAreaEdge.END, SafeAreaEdge.BOTTOM, SafeAreaEdge.START\])
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/UhyeCOHjQVe7I2lkfrwrqA/en-us_image_0000002537765942.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4E7DAD5F841EBE4406C0BCD2A9DE6DE8682CF1B46A9047487B0CA4D799412F1)

## Example 2: Customizing the Theme with WithTheme

// Customize the theme for components in the WithTheme scope.
import { CustomTheme, CustomColors } from '@kit.ArkUI';

class GreenColors implements CustomColors {
  fontPrimary = '#ff049404';
  fontEmphasize = '#FF00541F';
  fontOnPrimary = '#FFFFFFFF';
  compBackgroundTertiary = '#1111FF11';
  backgroundEmphasize = '#FF00541F';
  compEmphasizeSecondary = '#3322FF22';
}

class RedColors implements CustomColors {
  fontPrimary = '#fff32b3c';
  fontEmphasize = '#FFD53032';
  fontOnPrimary = '#FFFFFFFF';
  compBackgroundTertiary = '#44FF2222';
  backgroundEmphasize = '#FFD00000';
  compEmphasizeSecondary = '#33FF1111';
}

class PageCustomTheme implements CustomTheme {
  colors?: CustomColors

  constructor(colors: CustomColors) {
    this.colors = colors
  }
}

@Entry
@Component
struct IndexPage {
  static readonly themeCount = 3;
  themeNames: string\[\] = \['System', 'Custom (green)', 'Custom (red)'\];
  themeArray: (CustomTheme | undefined)\[\] = \[
    undefined, // System
    new PageCustomTheme(new GreenColors()),
    new PageCustomTheme(new RedColors())
  \]
  @State themeIndex: number = 0;

  build() {
    Column() {
      Column({ space: '8vp' }) {
        Text('WithTheme not used')
        // Click the button to change the theme.
        Button(\`Switch Theme: ${this.themeNames\[this.themeIndex\]}\`)
          .onClick(() => {
            this.themeIndex = (this.themeIndex + 1) % IndexPage.themeCount;
          })

        // Default button color
        Button('Button.style(NORMAL) with System Theme')
          .buttonStyle(ButtonStyleMode.NORMAL)
        Button('Button.style(EMP..ED) with System Theme')
          .buttonStyle(ButtonStyleMode.EMPHASIZED)
        Button('Button.style(TEXTUAL) with System Theme')
          .buttonStyle(ButtonStyleMode.TEXTUAL)
      }
      .margin({
        top: '50vp'
      })

      WithTheme({ theme: this.themeArray\[this.themeIndex\] }) {
        // WithTheme scope
        Column({ space: '8vp' }) {
          Text('WithTheme used')
          Button('Button.style(NORMAL) with Custom Theme')
            .buttonStyle(ButtonStyleMode.NORMAL)
          Button('Button.style(EMP..ED) with Custom Theme')
            .buttonStyle(ButtonStyleMode.EMPHASIZED)
          Button('Button.style(TEXTUAL) with Custom Theme')
            .buttonStyle(ButtonStyleMode.TEXTUAL)
        }
        .width('100%')
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/bzXZYpTmRuOKPvWMYsjF3w/en-us_image_0000002537925882.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7488A85E4F53571A2D4436521E31BBB71DF3C6BD1CA1B211D4332F3447197D40)
