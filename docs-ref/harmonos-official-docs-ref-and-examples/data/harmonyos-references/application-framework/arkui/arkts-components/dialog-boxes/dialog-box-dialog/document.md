# Dialog Box (Dialog)

A dialog is a modal window that temporarily displays information that requires user attention or actions that need to be performed, while preserving the current context. Users must complete the interaction before exiting this modal state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/faKv-8GgSYmNfYTFCM5cOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26BFC949A493668E2907E18B76970A594370E58BC3A886FE8B01900FAA626C3B)

This component is supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { TipsDialog, SelectDialog, ConfirmDialog, AlertDialog, LoadingDialog, CustomContentDialog } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### TipsDialog

TipsDialog({controller: CustomDialogController, imageRes: ResourceStr | PixelMap, imageSize?: SizeOptions, title?: ResourceStr, content?: ResourceStr, checkTips?: ResourceStr, isChecked?: boolean, checkAction?: (isChecked: boolean) => void, onCheckedChange?: Callback<boolean>, primaryButton?: ButtonOptions, secondaryButton?: ButtonOptions, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

Displays an image-attached confirmation dialog box.

**Decorator type**: @CustomDialog

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| controller | [CustomDialogController](../custom-dialog-box-customdialog/document.md#customdialogcontroller) | Yes | \- | 
Controller of the dialog box.

**NOTE**

If not decorated by @Require, this parameter is not subject to mandatory validation during construction.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| imageRes | [ResourceStr12+](../../common-definitions/basic-types/document.md#resourcestr) | [PixelMap12+](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | \- | 

Image to be displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| imageSize | [SizeOptions](../../common-definitions/basic-types/document.md#sizeoptions) | No | \- | 

Image size.

Default value: **64\*64vp**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| title | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | \- | 

Title of the dialog box.

If this parameter is not set or is set to **undefined**, the title is not displayed.

**NOTE**

If the title exceeds two lines, it will be truncated with an ellipsis (...).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | \- | 

Content of the dialog box.

If this parameter is not set or is set to **undefined**, the content is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| checkTips | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | \- | 

Content of the check box.

If this parameter is not set or is set to **undefined**, the check box content is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| isChecked | boolean | No | @Prop | 

Whether to select the check box. The value **true** means to select the check box, and **false** means the opposite.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| checkAction12+ | (isChecked: boolean) => void | No | \- | 

Event triggered when the selected status of the check box changes. **isChecked** indicates whether the check box is selected. The value **true** means the check box is selected, and **false** means the opposite. You are advised to use **onCheckedChange12+** instead.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onCheckedChange12+ | [Callback](../../common-definitions/basic-types/document.md#callback12)<boolean> | No | \- | 

Event triggered when the selected status of the check box changes. The value **Callback<true>** means the check box is selected, and **Callback<false>** means the opposite.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| primaryButton | [ButtonOptions](#buttonoptions) | No | \- | 

Left button of the dialog box.

If this parameter is not set or is set to **undefined**, the left button is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| secondaryButton | [ButtonOptions](#buttonoptions) | No | \- | 

Right button of the dialog box.

If this parameter is not set or is set to **undefined**, the right button is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| theme12+ | [Theme](../../../arkts-api/ui/ohos-arkui-theme-theme/document.md#theme) | [CustomTheme](../../../arkts-api/ui/ohos-arkui-theme-theme/document.md#customtheme) | No | \- | 

Theme information, which can be a custom theme or a **Theme** instance obtained from **onWillApplyTheme**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| themeColorMode12+ | [ThemeColorMode](../../universal-attributes/visual-effects/foreground-blur/document.md#themecolormode) | No | \- | 

Theme color mode of the dialog box.

Default value: **ThemeColorMode.SYSTEM**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### SelectDialog

SelectDialog({controller: CustomDialogController, title: ResourceStr, content?: ResourceStr, selectedIndex?: number, confirm?: ButtonOptions, radioContent: Array<SheetInfo>, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

Displays a dialog box from which the user can select options presented in a list or grid.

**Decorator type**: @CustomDialog

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| controller | [CustomDialogController](../custom-dialog-box-customdialog/document.md#customdialogcontroller) | Yes | 
Controller of the dialog box.

**NOTE**

If not decorated by @Require, this parameter is not subject to mandatory validation during construction.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| title | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 

Title of the dialog box.

**NOTE**

If the title exceeds two lines, it will be truncated with an ellipsis (...).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | 

Content of the dialog box.

If this parameter is not set or is set to **undefined**, the content is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| selectedIndex | number | No | 

Index of the selected option in the dialog box.

Value range: an integer no less than -1

The default value is **\-1**, indicating that there is no selected option. Values less than -1 are treated as no selected option.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| confirm | [ButtonOptions](#buttonoptions) | No | 

Button at the bottom of the dialog box.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| radioContent | Array<[SheetInfo](../action-sheet-actionsheet/document.md#sheetinfo)\> | Yes | 

List of subitems in the dialog box. You can set text and a select callback for each subitem.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| theme12+ | [Theme](../../../arkts-api/ui/ohos-arkui-theme-theme/document.md#theme) | [CustomTheme](../../../arkts-api/ui/ohos-arkui-theme-theme/document.md#customtheme) | No | 

Theme information, which can be a custom theme or a **Theme** instance obtained from **onWillApplyTheme**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| themeColorMode12+ | [ThemeColorMode](../../universal-attributes/visual-effects/foreground-blur/document.md#themecolormode) | No | 

Theme color mode of the dialog box.

Default value: **ThemeColorMode.SYSTEM**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### ConfirmDialog

ConfirmDialog({controller: CustomDialogController, title: ResourceStr, content?: ResourceStr, checkTips?: ResourceStr, isChecked?: boolean, primaryButton?: ButtonOptions, secondaryButton?: ButtonOptions, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

Displays an error dialog box that informs the user of an operational error (for example, a network error or low battery level) or an incorrect operation (for example, fingerprint enrollment).

**Decorator type**: @CustomDialog

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| controller | [CustomDialogController](../custom-dialog-box-customdialog/document.md#customdialogcontroller) | Yes | \- | 
Controller of the dialog box.

**NOTE**

If not decorated by @Require, this parameter is not subject to mandatory validation during construction.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| title | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | \- | 

Title of the dialog box.

**NOTE**

If the title exceeds two lines, it will be truncated with an ellipsis (...).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | \- | 

Content of the dialog box.

If this parameter is not set or is set to **undefined**, the content is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| checkTips | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | \- | 

Content of the check box.

If this parameter is not set or is set to **undefined**, the check box content is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| isChecked | boolean | No | @Prop | 

Whether to select the check box. The value **true** means to select the check box, and **false** means the opposite.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onCheckedChange12+ | [Callback](../../common-definitions/basic-types/document.md#callback12)<boolean> | No | \- | 

Event triggered when the selected status of the check box changes. The value **Callback<true>** means the check box is selected, and **Callback<false>** means the opposite.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| primaryButton | [ButtonOptions](#buttonoptions) | No | \- | 

Left button of the dialog box.

If this parameter is not set or is set to **undefined**, the left button is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| secondaryButton | [ButtonOptions](#buttonoptions) | No | \- | 

Right button of the dialog box.

If this parameter is not set or is set to **undefined**, the right button is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| theme12+ | [Theme](../../../arkts-api/ui/ohos-arkui-theme-theme/document.md#theme) | [CustomTheme](../../../arkts-api/ui/ohos-arkui-theme-theme/document.md#customtheme) | No | \- | 

Theme information, which can be a custom theme or a **Theme** instance obtained from **onWillApplyTheme**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| themeColorMode12+ | [ThemeColorMode](../../universal-attributes/visual-effects/foreground-blur/document.md#themecolormode) | No | \- | 

Theme color mode of the dialog box.

Default value: **ThemeColorMode.SYSTEM**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### AlertDialog

AlertDialog({controller: CustomDialogController, primaryTitle?: ResourceStr, secondaryTitle?: ResourceStr, content: ResourceStr, primaryButton?: ButtonOptions, secondaryButton?: ButtonOptions, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

Displays an alert dialog box to prompt the user to confirm an action that is irreversible and may cause serious consequences, such as deletion, reset, editing cancellation, and stop.

**Decorator type**: @CustomDialog

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| controller | [CustomDialogController](../custom-dialog-box-customdialog/document.md#customdialogcontroller) | Yes | 
Controller of the dialog box.

**NOTE**

If not decorated by @Require, this parameter is not subject to mandatory validation during construction.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| primaryTitle12+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | 

Level-1 title of the confirmation dialog box.

If this parameter is not set or is set to undefined, the level-1 title of the confirmation dialog box is not displayed by default.

**NOTE**

If the title exceeds two lines, it will be truncated with an ellipsis (...).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| secondaryTitle12+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | 

Level-2 title of the confirmation dialog box.

If this parameter is not set or is set to **undefined**, the level-2 title is not displayed.

**NOTE**

If the title exceeds two lines, it will be truncated with an ellipsis (...).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 

Content of the dialog box.

If this parameter is not set or is set to **undefined**, the content is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| primaryButton | [ButtonOptions](#buttonoptions) | No | 

Left button of the dialog box.

If this parameter is not set or is set to **undefined**, the left button is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| secondaryButton | [ButtonOptions](#buttonoptions) | No | 

Right button of the dialog box.

If this parameter is not set or is set to **undefined**, the right button is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| theme12+ | [Theme](../../../arkts-api/ui/ohos-arkui-theme-theme/document.md#theme) | [CustomTheme](../../../arkts-api/ui/ohos-arkui-theme-theme/document.md#customtheme) | No | 

Theme information, which can be a custom theme or a **Theme** instance obtained from **onWillApplyTheme**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| themeColorMode12+ | [ThemeColorMode](../../universal-attributes/visual-effects/foreground-blur/document.md#themecolormode) | No | 

Theme color mode of the dialog box.

Default value: **ThemeColorMode.SYSTEM**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### LoadingDialog

LoadingDialog({Controller: CustomDialogController, content?: ResourceStr, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

Displays a loading dialog box to inform the user of the operation progress.

**Decorator type**: @CustomDialog

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| Controller | [CustomDialogController](../custom-dialog-box-customdialog/document.md#customdialogcontroller) | Yes | 
Controller of the dialog box.

**NOTE**

If not decorated by @Require, this parameter is not subject to mandatory validation during construction.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | 

Content of the dialog box.

If this parameter is not set or is set to **undefined**, the content is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| theme12+ | [Theme](../../../arkts-api/ui/ohos-arkui-theme-theme/document.md#theme) | [CustomTheme](../../../arkts-api/ui/ohos-arkui-theme-theme/document.md#customtheme) | No | 

Theme information, which can be a custom theme or a **Theme** instance obtained from **onWillApplyTheme**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| themeColorMode12+ | [ThemeColorMode](../../universal-attributes/visual-effects/foreground-blur/document.md#themecolormode) | No | 

Theme color mode of the dialog box.

Default value: **ThemeColorMode.SYSTEM**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### CustomContentDialog12+

CustomContentDialog({controller: CustomDialogController, contentBuilder: () => void, primaryTitle?: ResourceStr, secondaryTitle?: ResourceStr, contentAreaPadding?: Padding, buttons?: ButtonOptions\[\], theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

Displays a dialog box that contains custom content and operation area.

**Decorator type**: @CustomDialog

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| controller | [CustomDialogController](../custom-dialog-box-customdialog/document.md#customdialogcontroller) | Yes | \- | 
Controller of the dialog box.

**NOTE**

If not decorated by @Require, this parameter is not subject to mandatory validation during construction.

 |
| contentBuilder | () => void | Yes | @BuilderParam | Content of the dialog box. |
| primaryTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | \- | 

Primary title of the dialog box.

If this parameter is not set or is set to **undefined**, the primary title is not displayed.

**NOTE**

If the title exceeds two lines, it will be truncated with an ellipsis (...).

 |
| secondaryTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | \- | 

Secondary title of the dialog box.

If this parameter is not set or is set to **undefined**, the secondary title is not displayed.

**NOTE**

If the title exceeds two lines, it will be truncated with an ellipsis (...).

 |
| localizedContentAreaPadding | [LocalizedPadding](../../common-definitions/basic-types/document.md#localizedpadding12) | No | \- | Padding of the content area of the dialog box. |
| contentAreaPadding | [Padding](../../common-definitions/basic-types/document.md#padding) | No | \- | Padding of the content area of the dialog box. This attribute does not take effect when **localizedContentAreaPadding** is set. |
| buttons | [ButtonOptions](#buttonoptions)\[\] | No | \- | Buttons in the operation area of the dialog box. A maximum of four buttons are allowed. |
| theme | [Theme](../../../arkts-api/ui/ohos-arkui-theme-theme/document.md#theme) | [CustomTheme](../../../arkts-api/ui/ohos-arkui-theme-theme/document.md#customtheme) | No | \- | Theme information, which can be a custom theme or a **Theme** instance obtained from **onWillApplyTheme**. |
| themeColorMode | [ThemeColorMode](../../universal-attributes/visual-effects/foreground-blur/document.md#themecolormode) | No | \- | 

Theme color mode of the dialog box.

Default value: **ThemeColorMode.SYSTEM**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/TVQ8w5tHQ_elvxe3nKGXzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D64CD8AA29D4E107DE653754A33D8DB13B2BC04DB33ACEF0E3C40398AB15AEF)

When the height of the dialog box is insufficient, the area defined by **contentBuilder** will be compressed. Global scrolling will be enabled if the compressed area's height falls below 100 vp.

You must define scrolling of the content area in **CustomContentDialog**. In addition, the custom scrolling of the content area must be used in conjunction with the **nestedScroll** property, as in the **nestedScroll({ scrollForward: NestedScrollMode.PARALLEL, scrollBackward: NestedScrollMode.PARALLEL })** example.

#### PopoverDialog14+

PopoverDialog({visible: boolean, popover: PopoverOptions, targetBuilder: Callback<void>})

Displays a popover dialog box that is positioned relative to the target component. This dialog box can contain a variety of content types, including: TipsDialog, SelectDialog, ConfirmDialog, AlertDialog, LoadingDialog, and CustomContentDialog.

**Decorator**: @Component

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| visible | boolean | Yes | @Link | 
Whether the popover dialog box is visible. The value **true** means that the popover dialog box is displayed, and **false** means the opposite.

Default value: **false**

 |
| popover | [PopoverOptions](#popoveroptions14) | Yes | 

@Prop

@Require

 | Options of the popover dialog box. |
| targetBuilder | [Callback](../../common-definitions/basic-types/document.md#callback12)<void> | Yes | 

@Require

@BuilderParam

 | Target component relative to which the popover dialog box is positioned. |

#### ButtonOptions

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Content of the button.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| action | () => void | No | Yes | 

Click event of the button.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| background | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Background color of the button.

The setting follows **buttonStyle** by default.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| fontColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Font color of the button.

The setting follows **buttonStyle** by default.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| buttonStyle12+ | [ButtonStyleMode](../../buttons-and-selections/button/document.md#buttonstylemode11) | No | Yes | 

Style of the button.

Default value: **ButtonStyleMode.NORMAL** for 2-in-1 devices and **ButtonStyleMode.TEXTUAL** for other devices

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| role12+ | [ButtonRole](../../buttons-and-selections/button/document.md#buttonrole12) | No | Yes | 

Role of the button.

Default value: **ButtonRole.NORMAL**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| defaultFocus18+ | boolean | No | Yes | 

Whether the button is the default focus.

**true**: The button is the default focus.

**false**: The button is not the default focus.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/lLOkRKTZS-6YzZqyc309kA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E98E0831987C52B6534B7740E2FEFC7E3340E231414C4F8A1712F1300F7C5788)

The priority of **buttonStyle** and **role** is higher than that of **fontColor** and **background**. If **buttonStyle** and **role** are at the default values, the settings of **fontColor** and **background** take effect.

If **defaultFocus** is set for multiple buttons, the default focus is the first button in the display order that has **defaultFocus** set to **true**.

#### PopoverOptions14+

Defines a set of options used to configure the popover dialog box, including its content and position.

Inherits [CustomPopupOptions](../../universal-attributes/dialog-box-control/popup-control/document.md#custompopupoptions8).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/ccI2_t6PTdKwBc6LyjVVrg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4375CBDF152DE08DB647B0ACD6F1CF59474710A2DB0B3A93F99E8320FB1BFBE7)

The default value of **radius** is **32vp**.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

## Example 1: Dialog Box with an Image Above Text

This example implements a dialog box with an image above the text content, through the use of **imageRes**, **content**, and other properties.

import { TipsDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogControllerImage: CustomDialogController = new CustomDialogController({
    builder: TipsDialog({
      imageRes: $r('sys.media.ohos\_ic\_public\_voice'),
      content: 'Delete this app?',
      primaryButton: {
        value: 'Cancel',
        action: () => {
          console.info('Callback when the first button is clicked')
        },
      },
      secondaryButton: {
        value: 'Delete',
        role: ButtonRole.ERROR,
        action: () => {
          console.info('Callback when the second button is clicked')
        }
      },
      onCheckedChange: () => {
        console.info('Callback when the checkbox is clicked')
      }
    }),
  })

  build() {
    Row() {
      Stack() {
        Column(){
          Button("Text Below Image")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogControllerImage.open()
            })
        }.margin({bottom: 300})
      }.align(Alignment.Bottom)
      .width('100%').height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/aSLMsGhOQ8uUdOiFMdr0Qg/en-us_image_0000002568685651.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6367107296BB6E7F4D7826A7557E94C7D910EBD7D5B3A5EB27BE42380D29EEEE)

## Example 2: List-only Dialog Box

This example presents a dialog box consisting solely of a list defined with **selectedIndex** and **radioContent**.

import { SelectDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  // Set the index of the default selected option.
  radioIndex = 0;
  dialogControllerList: CustomDialogController = new CustomDialogController({
    builder: SelectDialog({
      title:'Title',
      selectedIndex: this.radioIndex,
      confirm: {
        value: 'Cancel',
        action: () => {},
      },
      radioContent: \[
        {
          title: 'List item',
          action: () => {
            this.radioIndex = 0
          }
        },
        {
          title: 'List item',
          action: () => {
            this.radioIndex = 1
          }
        },
        {
          title: 'List item',
          action: () => {
            this.radioIndex = 2
          }
        },
      \]
    }),
  })

  build() {
    Row() {
      Stack() {
        Column() {
          Button("List Dialog Box")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogControllerList.open()
            })
        }.margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/DdmNjWMURt-hPRo9GLU5cg/en-us_image_0000002568765661.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=809322C70F7129E9D9E130114F79489E29647D1BBC8A6494C823D7CBD4E7018E)

## Example 3: Dialog Box with Text and Check Boxes

This example illustrates a dialog box that combines text content with check boxes defined with **content** and **checkTips**.

import { ConfirmDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  isChecked = false;
  dialogControllerCheckBox: CustomDialogController = new CustomDialogController({
    builder: ConfirmDialog({
      title:'Title',
      content: 'This is where the content of this dialog box is presented.',
      // Selected state of the check box
      isChecked: this.isChecked,
      // Content of the check box
      checkTips: 'Do not ask me again',
      primaryButton: {
        value: 'Deny',
        action: () => {},
      },
      secondaryButton: {
        value: 'Allow',
        action: () => {
          this.isChecked = false
          console.info('Callback when the second button is clicked')
        }
      },
      onCheckedChange: () => {
        console.info('Callback when the checkbox is clicked')
      },
    }),
    autoCancel: true,
    alignment: DialogAlignment.Bottom
  })

  build() {
    Row() {
      Stack() {
        Column(){
          Button("Text + Check Box Dialog Box")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogControllerCheckBox.open()
            })
        }
        .margin({bottom: 300})
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/SJudITKOQL-hWB4hh3nwpw/en-us_image_0000002537765936.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B908C1567ABAF952CF02CA8E076346786CB24D9EB69AC6F393B9DB08AB23F3E)

## Example 4: Text-only Dialog Box

This example demonstrates a simple text-only dialog box defined with **primaryTitle**, **secondaryTitle**, and **content**.

import { AlertDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogControllerConfirm: CustomDialogController = new CustomDialogController({
    builder: AlertDialog({
      primaryTitle: 'Primary title',
      secondaryTitle: 'Secondary title',
      content: 'This is where content is displayed.',
      primaryButton: {
        value: 'Cancel',
        action: () => {
        },
      },
      secondaryButton: {
        value: 'OK',
        role: ButtonRole.ERROR,
        action: () => {
          console.info('Callback when the second button is clicked')
        }
      },
    }),
  })

  build() {
    Row() {
      Stack() {
        Column() {
          Button("Text Dialog Box")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogControllerConfirm.open()
            })
        }
        .margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/FaqYKposTXeIr14y_RsT1g/en-us_image_0000002537925876.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C427577C54095857DA2C43DFC601ACEBEFC6EDA28C9A3A9830882C5139F5E73)

## Example 5: Loading Dialog Box

This example implements a loading dialog box that contains a progress indicator.

import { LoadingDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogControllerProgress: CustomDialogController = new CustomDialogController({
    builder: LoadingDialog({
      content: 'This is where content is displayed.',
    }),
  })

  build() {
    Row() {
      Stack() {
        Column() {
          Button("Loading Dialog Box")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogControllerProgress.open()
            })
        }
        .margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/OE94LdeDQ2SawfgjlYBfGA/en-us_image_0000002568685653.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D29D75283471035711F75EBBD6EDE279020E6C487E8264EC39410C157FAF0F54)

## Example 6: Dialog Box with a Custom Theme

This example presents a dialog box with a custom theme, through the use of **content**, **theme**, and other properties.

import { CustomColors, CustomTheme, LoadingDialog } from '@kit.ArkUI';

class CustomThemeImpl implements CustomTheme {
  colors?: CustomColors;

  constructor(colors: CustomColors) {
    this.colors = colors;
  }
}

// Custom text content and colors for the dialog box theme
class CustomThemeColors implements CustomColors {
  fontPrimary = '#ffd0a300';
  iconSecondary = '#ffd000cd';
}

@Entry
@Component
struct Index {
  @State customTheme: CustomTheme = new CustomThemeImpl(new CustomThemeColors());
  dialogController: CustomDialogController = new CustomDialogController({
    builder: LoadingDialog({
      content: 'text',
      theme: this.customTheme,
    })
  });

  build() {
    Row() {
      Stack() {
        Column() {
          Button('dialog')
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogController.open();
            })
        }
        .margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/xMS27S9gSCWQU1GY1BNjIA/en-us_image_0000002568765663.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70212855CA28CFC5FA2C03899BF65495D3F190C50071AB80CFC8A4B611EF291B)

## Example 7: Dialog Box in Custom Color Mode

This example presents a dialog box in the specified light or dark mode, through the use of **content**, **themeColorMode**, and other properties.

import { LoadingDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: LoadingDialog({
      content: 'Text',
      themeColorMode: ThemeColorMode.DARK, // Set the color mode to dark mode.
    })
  });

  build() {
    Row() {
      Stack() {
        Column() {
          Button('Dialog')
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogController.open();
            })
        }
        .margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/MgCTyNAtR0KIMkCoQn6WSQ/en-us_image_0000002537765938.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=106FED60EC5F4DD7791A52B08BBBD7AA1B1D1BE6A351E94C3BD98BB13F8CBF83)

## Example 8: Dialog Box with Custom Content

This example implements a dialog box with custom content defined with **contentBuilder** and **buttons**.

import { CustomContentDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomContentDialog({
      primaryTitle: 'Primary title',
      secondaryTitle: 'Secondary title',
      contentBuilder: () => {
        this.buildContent();
      },
      buttons: \[
        {
          value: 'Button 1',
          buttonStyle: ButtonStyleMode.TEXTUAL,
          action: () => {
            console.info('Callback when the button is clicked')
          }
        },
        {
          value: 'Button 2',
          buttonStyle: ButtonStyleMode.TEXTUAL,
          role: ButtonRole.ERROR
        }
      \],
    }),
  });

  build() {
    Column() {
      Button("Dialog Box with Custom Content")
        .onClick(() => {
          this.dialogController.open()
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
  
  // Custom content area of the dialog box
  @Builder
  buildContent(): void {
    Column() {
      Text('Content area')
    }
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/cvBADdxpTi2K_bU_4p-9Kg/en-us_image_0000002537925878.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2EE269DE7238FECB5B78BF563984F5DEC933132730D25471913AE44C5B3FBFAE)

## Example 9: Popover Dialog Box

This example demonstrates a popover dialog box for alert purposes, through the use of **visible**, **popover**, **targetBuilder**, and other properties. This functionality is supported since API version 14.

import { AlertDialog, PopoverDialog, PopoverOptions } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State isShow: boolean = false;
  @State popoverOptions: PopoverOptions = {
    builder: () => {
      this.dialogBuilder();
    },
    width: 320,
  }
  
  // Popover dialog box
  @Builder dialogBuilder() {
    AlertDialog({
      content: 'Popover dialog box',
      primaryButton: {
        value: 'Cancel',
        action: () => {
          this.isShow = false;
        },
      },
      secondaryButton: {
        value: 'OK',
        action: () => {
          this.isShow = false;
        },
      },
    });
  }
  
  // Builder for the button that triggers the popover dialog box
  @Builder buttonBuilder() {
    Button('Target Component')
    .onClick(() => {
      this.isShow = true;
    });
  }

  build() {
    Column() {
      PopoverDialog({
        visible: this.isShow,
        popover: this.popoverOptions,
        targetBuilder: () => {
          this.buttonBuilder();
        },
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/UdOCYc3-SsGJY7zwiX2uJQ/en-us_image_0000002568685655.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D082854FA61350FB7DD6C95E081193C5C7DC3545B8D8A51B7BAA7B02E423347B)

## Example 10: Setting the Default Focus Button for a Dialog Box

This example demonstrates how to set the button that receives focus by default in a dialog box using **AlertDialog**, including the **defaultFocus** property. This functionality is supported since API version 18.

import { AlertDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: AlertDialog({
      primaryTitle: 'AlertDialog',
      secondaryTitle: 'Subtitle',
      content: 'The second button gains focus by default.',
      primaryButton: {
        value: 'DEFAULT',
        action: () => {}
      },
      secondaryButton: {
        value: 'TRUE',
        defaultFocus: true, // Set the button as the default focus button.
        action: () => {}
      },
    })
  });

  build() {
    Row() {
      Stack() {
        Column() {
          Button("AlertDialog")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogController.open()
            })
        }
        .margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/H0zk4KvrTRSjhltcKlrcNw/en-us_image_0000002568765665.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A1B6D8DD5CF341DB3757F8BE4C68BF06C2E0D0C72E3692886BF2911A9947051)
