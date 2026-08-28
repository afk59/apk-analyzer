# @ohos.arkui.theme (Theme)

You can define a custom theme to apply to components in your application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/3JYlsBiHSCmPhqHk1i3LLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EB68E82B5D53A7989F7FA8FC312AEF2DEEBE0D2C54B5349246A7B91274AD4D74)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { Theme, ThemeControl, CustomColors, Colors, CustomTheme, CustomDarkColors } from '@kit.ArkUI';

#### Theme

Defines the **Theme** object in use, which can be obtained through [onWillApplyTheme](../../../arkts-components/custom-components/custom-component-lifecycle/document.md#onwillapplytheme12).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| colors | [Colors](#colors) | No | No | Color resources of the theme. |

#### Colors

Defines the color resources of a theme.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/28nTeVCbSTC7Dvcc6mIDTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E09A040B693FDCD29F6C0C4CBAAB39AC4F1778D7F63376241F84CDB292E4653)

For details about the components corresponding to the colors, see [Font Color and Icon Color](https://developer.huawei.com/consumer/en/doc/design-guides/color-0000001776857164#section137153164914).

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| brand | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 
Brand color.

**Affected components**: [TextInput](../../../arkts-components/text-and-input/textinput/document.md), [Search](../../../arkts-components/text-and-input/search/document.md)

 |
| warning | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Warning color.

Affected components: [TipsDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#tipsdialog), [AlertDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#alertdialog), [CustomContentDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#customcontentdialog12),

[Badge](../../../arkts-components/information-display/badge/document.md), [Button](../../../arkts-components/buttons-and-selections/button/document.md)

 |
| alert | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Alert color.

**Affected components**: N/A

 |
| confirm | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Confirmation color.

**Affected components**: N/A

 |
| fontPrimary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Primary font color.

**Affected components**: [EditableTitleBar](../../../arkts-components/system-preset-ui-component-library/editabletitlebar/document.md), [LoadingDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#loadingdialog), [TipsDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#tipsdialog)

[ConfirmDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#confirmdialog), [AlertDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#alertdialog), [SelectDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#selectdialog),

[CustomContentDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#customcontentdialog12), [Swiper](../../../arkts-components/scroll-and-swipe/swiper/document.md), [Text](../../../arkts-components/text-and-input/text/document.md),

[SubHeader](../../../arkts-components/system-preset-ui-component-library/subheader/document.md), [ProgressButton](../../../arkts-components/system-preset-ui-component-library/progressbutton/document.md), [AlphabetIndexer](../../../arkts-components/information-display/alphabetindexer/document.md),

[Popup](../../../arkts-components/system-preset-ui-component-library/popup/document.md), [Select](../../../arkts-components/buttons-and-selections/select/document.md), [Chip](../../../arkts-components/system-preset-ui-component-library/chip/document.md),

[ToolBar](../../../arkts-components/system-preset-ui-component-library/toolbar/document.md), [Menu](../../../arkts-components/menus/menu/document.md), [TextInput](../../../arkts-components/text-and-input/textinput/document.md),

[Search](../../../arkts-components/text-and-input/search/document.md), [Counter](../../../arkts-components/information-display/counter/document.md), [TimePicker](../../../arkts-components/buttons-and-selections/timepicker/document.md), [DatePicker](../../../arkts-components/buttons-and-selections/datepicker/document.md),

[TextPicker](../../../arkts-components/buttons-and-selections/textpicker/document.md), [ComposeListItem](../../../arkts-components/system-preset-ui-component-library/composelistitem/document.md), [TreeView](../../../arkts-components/system-preset-ui-component-library/treeview/document.md)

 |
| fontSecondary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Secondary font color.

**Affected components**: [EditableTitleBar](../../../arkts-components/system-preset-ui-component-library/editabletitlebar/document.md), [AlertDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#alertdialog), [CustomContentDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#customcontentdialog12),

[SubHeader](../../../arkts-components/system-preset-ui-component-library/subheader/document.md), [AlphabetIndexer](../../../arkts-components/information-display/alphabetindexer/document.md), [Popup](../../../arkts-components/system-preset-ui-component-library/popup/document.md),

[TextInput](../../../arkts-components/text-and-input/textinput/document.md), [Search](../../../arkts-components/text-and-input/search/document.md), [ComposeListItem](../../../arkts-components/system-preset-ui-component-library/composelistitem/document.md),

[TreeView](../../../arkts-components/system-preset-ui-component-library/treeview/document.md)

 |
| fontTertiary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Tertiary font color.

**Affected components**: [ComposeListItem](../../../arkts-components/system-preset-ui-component-library/composelistitem/document.md)

 |
| fontFourth | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Fourth-level font color.

**Affected components**: N/A

 |
| fontEmphasize | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Emphasis font color.

**Affected components**: [TipsDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#tipsdialog), [ConfirmDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#confirmdialog), [AlertDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#alertdialog)

[SelectDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#selectdialog), [CustomContentDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#customcontentdialog12), [SubHeader](../../../arkts-components/system-preset-ui-component-library/subheader/document.md),

[AlphabetIndexer](../../../arkts-components/information-display/alphabetindexer/document.md), [Popup](../../../arkts-components/system-preset-ui-component-library/popup/document.md), [Button](../../../arkts-components/buttons-and-selections/button/document.md),

[Select](../../../arkts-components/buttons-and-selections/select/document.md), [ToolBar](../../../arkts-components/system-preset-ui-component-library/toolbar/document.md), [Search](../../../arkts-components/text-and-input/search/document.md),

[TimePicker](../../../arkts-components/buttons-and-selections/timepicker/document.md), [DatePicker](../../../arkts-components/buttons-and-selections/datepicker/document.md), [TextPicker](../../../arkts-components/buttons-and-selections/textpicker/document.md)

 |
| fontOnPrimary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Primary inverted font color used on color background.

**Affected components**: [Badge](../../../arkts-components/information-display/badge/document.md), [Button](../../../arkts-components/buttons-and-selections/button/document.md), [Chip](../../../arkts-components/system-preset-ui-component-library/chip/document.md)

 |
| fontOnSecondary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Secondary inverted font color used on color background.

**Affected components**: N/A

 |
| fontOnTertiary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Tertiary inverted font color used on color background.

**Affected components**: N/A

 |
| fontOnFourth | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Fourth-level inverted font color used on color background.

**Affected components**: N/A

 |
| iconPrimary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Primary icon color.

**Affected components**: [EditableTitleBar](../../../arkts-components/system-preset-ui-component-library/editabletitlebar/document.md), [Swiper](../../../arkts-components/scroll-and-swipe/swiper/document.md), [ToolBar](../../../arkts-components/system-preset-ui-component-library/toolbar/document.md)

[TreeView](../../../arkts-components/system-preset-ui-component-library/treeview/document.md)

 |
| iconSecondary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Secondary icon color.

**Affected components**: [LoadingDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#loadingdialog), [SubHeader](../../../arkts-components/system-preset-ui-component-library/subheader/document.md), [LoadingProgress](../../../arkts-components/information-display/loadingprogress/document.md)

[Popup](../../../arkts-components/system-preset-ui-component-library/popup/document.md), [Chip](../../../arkts-components/system-preset-ui-component-library/chip/document.md), [Search](../../../arkts-components/text-and-input/search/document.md),

[TreeView](../../../arkts-components/system-preset-ui-component-library/treeview/document.md)

 |
| iconTertiary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Tertiary icon color.

**Affected components**: [SubHeader](../../../arkts-components/system-preset-ui-component-library/subheader/document.md)

 |
| iconFourth | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Fourth-level icon color.

**Affected components**: [Checkbox](../../../arkts-components/buttons-and-selections/checkbox/document.md), [CheckboxGroup](../../../arkts-components/buttons-and-selections/checkboxgroup/document.md), [Radio](../../../arkts-components/buttons-and-selections/radio/document.md)

 |
| iconEmphasize | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Emphasis icon color.

**Affected components**: [ToolBar](../../../arkts-components/system-preset-ui-component-library/toolbar/document.md)

 |
| iconSubEmphasize | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Color of the emphasis auxiliary icon.

**Affected components**: N/A

 |
| iconOnPrimary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Primary inverted icon color used on color background.

**Affected components**: [Checkbox](../../../arkts-components/buttons-and-selections/checkbox/document.md), [CheckboxGroup](../../../arkts-components/buttons-and-selections/checkboxgroup/document.md), [Radio](../../../arkts-components/buttons-and-selections/radio/document.md)

 |
| iconOnSecondary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Secondary inverted icon color used on color background.

**Affected components**: [Chip](../../../arkts-components/system-preset-ui-component-library/chip/document.md)

 |
| iconOnTertiary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Tertiary inverted icon color used on color background.

**Affected components**: N/A

 |
| iconOnFourth | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Fourth-level inverted icon color used on color background.

**Affected components**: [ProgressButton](../../../arkts-components/system-preset-ui-component-library/progressbutton/document.md)

 |
| backgroundPrimary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Primary background color (solid, opaque).

**Affected components**: [TextInput](../../../arkts-components/text-and-input/textinput/document.md), [QRCode](../../../arkts-components/information-display/qrcode/document.md)

 |
| backgroundSecondary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Secondary background color (solid, opaque).

**Affected components**: N/A

 |
| backgroundTertiary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Tertiary background color (solid, opaque).

**Affected components**: N/A

 |
| backgroundFourth | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Fourth-level background color (solid, opaque).

**Affected components**: N/A

 |
| backgroundEmphasize | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Emphasis background color (solid, opaque).

**Affected components**: [Progress](../../../arkts-components/information-display/progress/document.md), [Button](../../../arkts-components/buttons-and-selections/button/document.md), [Slider](../../../arkts-components/buttons-and-selections/slider/document.md)

 |
| compForegroundPrimary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Foreground.

**Affected components**: [QRCode](../../../arkts-components/information-display/qrcode/document.md)

 |
| compBackgroundPrimary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

White background.

**Affected components**: N/A

 |
| compBackgroundPrimaryTran | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

White transparent background.

**Affected components**: N/A

 |
| compBackgroundPrimaryContrary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Always-on background.

**Affected components**: [Toggle](../../../arkts-components/buttons-and-selections/toggle/document.md), [Slider](../../../arkts-components/buttons-and-selections/slider/document.md)

 |
| compBackgroundGray | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Gray background.

**Affected components**: N/A

 |
| compBackgroundSecondary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Secondary background.

**Affected components**: [Swiper](../../../arkts-components/scroll-and-swipe/swiper/document.md), [Slider](../../../arkts-components/buttons-and-selections/slider/document.md)

 |
| compBackgroundTertiary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Tertiary background.

**Affected components**: [EditableTitleBar](../../../arkts-components/system-preset-ui-component-library/editabletitlebar/document.md), [Progress](../../../arkts-components/information-display/progress/document.md), [AlphabetIndexer](../../../arkts-components/information-display/alphabetindexer/document.md)

[Button](../../../arkts-components/buttons-and-selections/button/document.md), [Select](../../../arkts-components/buttons-and-selections/select/document.md), [Toggle](../../../arkts-components/buttons-and-selections/toggle/document.md),

[Chip](../../../arkts-components/system-preset-ui-component-library/chip/document.md), [TextInput](../../../arkts-components/text-and-input/textinput/document.md), [Search](../../../arkts-components/text-and-input/search/document.md)

 |
| compBackgroundEmphasize | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Emphasis background.

**Affected components**: [Swiper](../../../arkts-components/scroll-and-swipe/swiper/document.md), [Toggle](../../../arkts-components/buttons-and-selections/toggle/document.md), [Chip](../../../arkts-components/system-preset-ui-component-library/chip/document.md)

[Checkbox](../../../arkts-components/buttons-and-selections/checkbox/document.md), [CheckboxGroup](../../../arkts-components/buttons-and-selections/checkboxgroup/document.md), [Radio](../../../arkts-components/buttons-and-selections/radio/document.md)

 |
| compBackgroundNeutral | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Black, neutral, emphasis background.

**Affected components**: [PatternLock](../../../arkts-components/information-display/patternlock/document.md)

 |
| compEmphasizeSecondary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

20% emphasis background color.

**Affected components**: [Progress](../../../arkts-components/information-display/progress/document.md), [ProgressButton](../../../arkts-components/system-preset-ui-component-library/progressbutton/document.md), [AlphabetIndexer](../../../arkts-components/information-display/alphabetindexer/document.md)

[Select](../../../arkts-components/buttons-and-selections/select/document.md), [Toggle](../../../arkts-components/buttons-and-selections/toggle/document.md)

 |
| compEmphasizeTertiary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

10% emphasis background color.

**Affected components**: N/A

 |
| compDivider | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Common divider color.

**Affected components**: [SelectDialog](../../../arkts-components/dialog-boxes/dialog-box-dialog/document.md#selectdialog), [PatternLock](../../../arkts-components/information-display/patternlock/document.md), [Divider](../../../arkts-components/blank-and-divider/divider/document.md)

 |
| compCommonContrary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Common inverted color.

**Affected components**: N/A

 |
| compBackgroundFocus | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Background color in the focused state.

**Affected components**: N/A

 |
| compFocusedPrimary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Primary inverted color in the focused state.

**Affected components**: N/A

 |
| compFocusedSecondary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Secondary inverted color in the focused state.

**Affected components**: N/A

 |
| compFocusedTertiary | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Tertiary inverted color in the focused state.

**Affected components**: [Scroll](../../../arkts-components/scroll-and-swipe/scroll/document.md)

 |
| interactiveHover | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Common interactive color for the hover state.

**Affected components**: [EditableTitleBar](../../../arkts-components/system-preset-ui-component-library/editabletitlebar/document.md), [Chip](../../../arkts-components/system-preset-ui-component-library/chip/document.md), [TreeView](../../../arkts-components/system-preset-ui-component-library/treeview/document.md)

 |
| interactivePressed | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Common interactive color for the pressed state.

**Affected components**: [EditableTitleBar](../../../arkts-components/system-preset-ui-component-library/editabletitlebar/document.md), [Chip](../../../arkts-components/system-preset-ui-component-library/chip/document.md), [TreeView](../../../arkts-components/system-preset-ui-component-library/treeview/document.md)

 |
| interactiveFocus | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Common interactive color for the focused state.

**Affected components**: [EditableTitleBar](../../../arkts-components/system-preset-ui-component-library/editabletitlebar/document.md), [Chip](../../../arkts-components/system-preset-ui-component-library/chip/document.md), [TreeView](../../../arkts-components/system-preset-ui-component-library/treeview/document.md)

 |
| interactiveActive | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Common interactive color for the active state.

**Affected components**: [TreeView](../../../arkts-components/system-preset-ui-component-library/treeview/document.md)

 |
| interactiveSelect | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Common interactive color for the selected state.

**Affected components**: [TreeView](../../../arkts-components/system-preset-ui-component-library/treeview/document.md)

 |
| interactiveClick | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Common interactive color for the clicked state.

**Affected components**: N/A

 |

#### CustomTheme

Defines a custom theme object.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| colors | [CustomColors](#customcolors) | No | Yes | 
Custom light theme color resources.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| darkColors20+ | [CustomDarkColors](#customdarkcolors20) | No | Yes | 

Custom dark theme color resources.

Note: If **darkColors** is not configured, the color values will default to those specified in the **colors** configuration for light mode and will not adapt to dark mode changes, unless the colors are defined using resources from the **dark** directory.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### CustomColors

type CustomColors = Partial<Colors>

Defines the type for custom theme color resources.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| Partial<[Colors](#colors)\> | Type representing customizable theme color resources. |

#### CustomDarkColors20+

type CustomDarkColors = Partial<Colors>

Defines the type for dark theme color resources.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| Partial<[Colors](#colors)\> | Type representing customizable dark theme color resources. |

#### ThemeControl

Implements a **ThemeControl** object to apply the custom theme to the components in the application.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]setDefaultTheme

setDefaultTheme(theme: [CustomTheme](#customtheme)): void

Sets a custom theme as the default, application-level theme, applying it to all components within the application. When using this API within a page, ensure that the API is called before the page's **build** API executes. When using this API within a UIAbility, ensure that the API is called in the callback after windowStage.[loadContent](../../window-manager/ohos-window-window/interface-windowstage/document.md#loadcontent9) during the **onWindowStageCreate** lifecycle phase. For a complete implementation example, see [Setting Custom Theme Colors for Application Components](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/theme_skinning#setting-custom-theme-colors-for-application-components).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| theme | [CustomTheme](#customtheme) | Yes | Custom theme to set. |

**Example**

import { CustomTheme, CustomColors, ThemeControl } from '@kit.ArkUI';
// Custom theme color
class BlueColors implements CustomColors {
  fontPrimary = "#FF707070";
  backgroundPrimary = "#FF2787D9";
  brand = "#FFEEAAFF"; // Brand color.
}

class PageCustomTheme implements CustomTheme {
  colors?: CustomColors;

  constructor(colors: CustomColors) {
    this.colors = colors;
  }
}
// Create an instance.
const BlueColorsTheme = new PageCustomTheme(new BlueColors());
// Call ThemeControl.setDefaultTheme before page build to set the default application style to BlueColorsTheme.
ThemeControl.setDefaultTheme(BlueColorsTheme);

@Entry
@Component
struct Index {

  build() {
    Row() {
      Column() {
        // Apply fontPrimary to the text color.
        Text('This is a piece of text.')
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .margin('5%')
        // Apply backgroundPrimary to the QR code background color.
        QRCode('Hello')
          .width(100)
          .height(100)
        // Apply brand to the input box cursor color.
        TextInput({placeholder: 'input your word...'})
          .width('80%')
          .height(40)
          .margin(20)
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/J1wuwSN5TsqAxmxW9TrnRA/en-us_image_0000002537925260.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA83640B9B63E3BDEECC176684C205FF27F2FA9CB0F302F992C159BF7D7C75E3)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/ueRZYGkbSRWRcb7ES4M8iQ/en-us_image_0000002568685037.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=499DFBDCCA7ADB01C50D9780A78C7B338C151FD4D99232AD8EB52795763B6927)
