# DialogV2

The dialog box is a modal window that commands attention while retaining the current context. It is frequently used to draw the user's attention to vital information or prompt the user to complete a specific task. As all modal windows, this component requires the user to interact before exiting.

This component is implemented based on [state management V2](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state-management-overview#state-management-v2). Compared with [state management V1](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state-management-overview#state-management-v1), V2 offers a higher level of observation and management over data objects beyond the component level. You can now more easily manage dialog box data and states with greater flexibility, leading to faster UI updates.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/-mCCeuqnRZ6VJ-1NCa6HZg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D4A6D88D205B033946649ADA79D7C50ECF44CC758E52B43C11B24FE814027D6)

This component is supported since API version 18. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { TipsDialogV2, SelectDialogV2, ConfirmDialogV2, AlertDialogV2, LoadingDialogV2, CustomContentDialogV2, PopoverDialogV2 } from '@kit.ArkUI';

#### Child Components

Not supported

#### TipsDialogV2

TipsDialogV2({imageRes: ResourceStr | PixelMap, imageSize?: SizeOptions, imageBorderColor: ColorMetrics, imageBorderWidth: LengthMetrics, title?: ResourceStr, content?: ResourceStr, checkTips?: ResourceStr, checked?: boolean, onCheckedChange?: AdvancedDialogV2OnCheckedChange, primaryButton?: AdvancedDialogV2Button, secondaryButton?: AdvancedDialogV2Button})

Displays an image-attached confirmation dialog box.

**Decorator**: @ComponentV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| imageRes | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | 
@Param

@Require

 | Image to be displayed. |
| imageSize | [SizeOptions](../../common-definitions/basic-types/document.md#sizeoptions) | No | @Param | 

Size of the image.

Default value: **64\*64vp**.

 |
| imageBorderColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Stroke color of the image.

Default value: **Color.Black**.

 |
| imageBorderWidth | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Stroke width of the image.

By default, there is no stroke effect.

 |
| title | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Param | 

Title of the dialog box.

It is not displayed by default.

**NOTE**

If the title exceeds two lines, it will be truncated with an ellipsis (...).

 |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Param | 

Content of the dialog box.

It is not displayed by default.

 |
| checkTips | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Param | 

Content of the check box.

It is not displayed by default.

 |
| checked | boolean | No | @Param | 

Whether to select the check box.

**true**: The check box is selected. **false**: The check box is not selected.

Default value: **false**.

 |
| onCheckedChange | [AdvancedDialogV2OnCheckedChange](#advanceddialogv2oncheckedchange) | No | @Param | 

Event triggered when the selected status of the check box changes.

By default, there is no event.

 |
| primaryButton | [AdvancedDialogV2Button](#advanceddialogv2button) | No | @Param | 

Left button of the dialog box.

It is not displayed by default.

 |
| secondaryButton | [AdvancedDialogV2Button](#advanceddialogv2button) | No | @Param | 

Right button of the dialog box.

It is not displayed by default.

 |

#### AdvancedDialogV2OnCheckedChange

type AdvancedDialogV2OnCheckedChange = (checked: boolean) => void

Defines the event triggered when the selected status of the check box changes.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| checked | boolean | Yes | 
Whether to select the check box.

**true**: The check box is selected. **false**: The check box is not selected.

 |

#### SelectDialogV2

SelectDialogV2({title: ResourceStr, content?: ResourceStr, selectedIndex?: number, confirm?: AdvancedDialogV2Button, radioContent: SheetInfo\[\]})

Displays a dialog box from which the user can select items presented in a list or grid.

**Decorator**: @ComponentV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 
@Param

@Require

 | 

Title of the dialog box.

**NOTE**

If the title exceeds two lines, it will be truncated with an ellipsis (...).

 |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Param | Content of the dialog box. It is not displayed by default. |
| selectedIndex | number | No | @Param | 

Index of the selected item in the dialog box.

The default value is **\-1**, indicating that there is no selected option. Values beyond the valid range are treated as no selected option.

Value range: less than the length of the list of items displayed in the dialog box.

 |
| confirm | [AdvancedDialogV2Button](#advanceddialogv2button) | No | @Param | 

Button at the bottom of the dialog box.

It is not displayed by default.

 |
| radioContent | [SheetInfo](../../dialog-boxes/action-sheet-actionsheet/document.md#sheetinfo)\[\] | Yes | 

@Param

@Require

 | List of items displayed in the dialog box. You can set text and a selection callback for each item. |

#### ConfirmDialogV2

ConfirmDialogV2({title: ResourceStr, content?: ResourceStr, checkTips?: ResourceStr, checked?: boolean, onCheckedChange: AdvancedDialogV2OnCheckedChange, primaryButton?: AdvancedDialogV2Button, secondaryButton?: AdvancedDialogV2Button})

Displays an error dialog box that informs the user of an operational error (for example, a network error or low battery level) or an incorrect operation (for example, fingerprint enrollment).

**Decorator**: @ComponentV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 
@Param

@Require

 | 

Title of the dialog box.

**NOTE**

If the title exceeds two lines, it will be truncated with an ellipsis (...).

 |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Param | 

Content of the dialog box.

It is not displayed by default.

 |
| checkTips | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Param | 

Content of the check box.

It is not displayed by default.

 |
| checked | boolean | No | @Param | 

Whether to select the check box. The value **true** means to select the check box, and **false** means the opposite.

Default value: **false**.

 |
| onCheckedChange | [AdvancedDialogV2OnCheckedChange](#advanceddialogv2oncheckedchange) | No | @Param | 

Event triggered when the selected status of the check box changes.

By default, there is no event.

 |
| primaryButton | [AdvancedDialogV2Button](#advanceddialogv2button) | No | @Param | 

Left button of the dialog box.

It is not displayed by default.

 |
| secondaryButton | [AdvancedDialogV2Button](#advanceddialogv2button) | No | @Param | 

Right button of the dialog box.

It is not displayed by default.

 |

#### AlertDialogV2

AlertDialogV2({primaryTitle?: ResourceStr, secondaryTitle?: ResourceStr, content: ResourceStr, primaryButton?: AdvancedDialogV2Button, secondaryButton?: AdvancedDialogV2Button})

Displays an alert dialog box to prompt the user to confirm an action that is irreversible and may cause serious consequences, such as deletion, reset, editing cancellation, and stop.

**Decorator**: @ComponentV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| primaryTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Param | 
Primary title of the dialog box.

It is not displayed by default.

**NOTE**

If the title exceeds two lines, it will be truncated with an ellipsis (...).

 |
| secondaryTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Param | 

Secondary title of the dialog box.

It is not displayed by default.

**NOTE**

If the title exceeds two lines, it will be truncated with an ellipsis (...).

 |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 

@Param

@Require

 | 

Content of the dialog box.

 |
| primaryButton | [AdvancedDialogV2Button](#advanceddialogv2button) | No | @Param | 

Left button of the dialog box.

It is not displayed by default.

 |
| secondaryButton | [AdvancedDialogV2Button](#advanceddialogv2button) | No | @Param | 

Right button of the dialog box.

It is not displayed by default.

 |

#### LoadingDialogV2

LoadingDialogV2({content?: ResourceStr})

Displays a loading dialog box to inform the user of the operation progress.

**Decorator**: @ComponentV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Param | 
Content of the dialog box.

It is empty by default.

**NOTE**

If the title exceeds 10 lines, it will be truncated with an ellipsis (...).

 |

#### CustomContentDialogV2

CustomContentDialogV2({contentBuilder: () => void, primaryTitle?: ResourceStr, secondaryTitle?: ResourceStr, contentAreaPadding?: LocalizedPadding, buttons?: AdvancedDialogV2Button\[\]})

Displays a dialog box that contains custom content and operation area.

**Decorator**: @ComponentV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| contentBuilder | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | Yes | @BuilderParam | Content of the dialog box. |
| primaryTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Param | 
Primary title of the dialog box.

It is not displayed by default.

**NOTE**

If the title exceeds two lines, it will be truncated with an ellipsis (...).

 |
| secondaryTitle | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Param | 

Secondary title of the dialog box.

It is not displayed by default.

**NOTE**

If the title exceeds two lines, it will be truncated with an ellipsis (...).

 |
| contentAreaPadding | [LocalizedPadding](../../common-definitions/basic-types/document.md#localizedpadding12) | No | @Param | 

Padding of the content area of the dialog box.

It is not displayed by default.

 |
| buttons | [AdvancedDialogV2Button](#advanceddialogv2button)\[\] | No | @Param | 

Buttons in the operation area of the dialog box. A maximum of four buttons are allowed.

It is not displayed by default.

 |

#### PopoverDialogV2OnVisibleChange

type PopoverDialogV2OnVisibleChange = (visible: boolean) => void

Defines the event triggered when the visibility of the popover dialog box changes.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| visible | boolean | Yes | 
Whether the popover dialog box is visible.

**true**: The popover dialog box is displayed. **false**: The popover dialog box is hidden.

 |

#### PopoverDialogV2

PopoverDialogV2({visible: boolean, $visible: PopoverDialogV2OnVisibleChange, popover: PopoverDialogV2Options, targetBuilder: CustomBuilder})

Displays a popover dialog box that is positioned relative to the target component. This dialog box can contain a variety of content types, including: TipsDialogV2, SelectDialogV2, ConfirmDialogV2, AlertDialogV2, LoadingDialogV2, and CustomContentDialogV2.

**Decorator**: @ComponentV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| visible | boolean | Yes | 
@Param

@Require

 | 

Whether the popover dialog box is visible.

**true**: The popover dialog box is displayed. **false**: The popover dialog box is hidden.

 |
| $visible | [PopoverDialogV2OnVisibleChange](#popoverdialogv2onvisiblechange) | No | @Event | 

Callback invoked when the visibility of the dialog box changes. Use the **!!** syntax for two-way binding with **visible**.

By default, there is no event.

 |
| popover | [PopoverDialogV2Options](#popoverdialogv2options) | Yes | 

@Param

@Require

 | Options of the popover dialog box. |
| targetBuilder | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | Yes | @BuilderParam | Target component relative to which the popover dialog box is positioned. |

#### PopoverDialogV2Options

Defines a set of options used to configure the popover dialog box, including its content and position.

Inherits [CustomPopupOptions](../../universal-attributes/dialog-box-control/popup-control/document.md#custompopupoptions8).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/Sc8TL7Q2TPGgJIwzL5U35A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C888F8C2F579411F51864B92A20D58BBEC97E36CCE270384A896A25E68890CD)

The default value of **radius** is **32vp**.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### AdvancedDialogV2ButtonAction

type AdvancedDialogV2ButtonAction = () => void

Defines the click event type for buttons in the dialog box action area.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### AdvancedDialogV2Button

Defines the button used in a dialog box to perform actions.

**Decorator**: @ObservedV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Content of the button.

Decorator: @Trace

 |
| action | [AdvancedDialogV2ButtonAction](#advanceddialogv2buttonaction) | No | Yes | 

Action triggered when the button is clicked.

By default, there is no action.

Decorator: @Trace

 |
| background | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Background of the button.

The setting follows **buttonStyle** by default.

Decorator: @Trace

 |
| fontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Font color of the button.

The setting follows **buttonStyle** by default.

Decorator: @Trace

 |
| buttonStyle | [ButtonStyleMode](../../buttons-and-selections/button/document.md#buttonstylemode11) | No | Yes | 

Style of the button.

Default value: **ButtonStyleMode.NORMAL** for 2-in-1 devices and **ButtonStyleMode.TEXTUAL** for other devices

Decorator: @Trace

 |
| role | [ButtonRole](../../buttons-and-selections/button/document.md#buttonrole12) | No | Yes | 

Role of the button.

Default value: **ButtonRole.NORMAL**

Decorator: @Trace

 |
| defaultFocus | boolean | No | Yes | 

Whether the button is the default focus.

**true**: The button is the default focus.

**false**: The button is not the default focus.

Default value: **false**.

Decorator: @Trace

 |
| enabled | boolean | No | Yes | 

Whether the button is enabled.

**true**: The button is enabled.

**false**: The button is disabled.

Default value: **true**.

Decorator: @Trace

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/f9zT6qKXRXK0V7sZf6GHKQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0AE5CF132284F496AF1928E02FF0A7713C951F98F335828C02B0183770460E73)

The priority of **buttonStyle** and **role** is higher than that of **fontColor** and **background**. If **buttonStyle** and **role** are at the default values, the settings of **fontColor** and **background** take effect.

If **defaultFocus** is set for multiple buttons, the default focus is the first button in the display order that has **defaultFocus** set.

#### \[h2\]constructor

constructor(options: AdvancedDialogV2ButtonOptions)

A constructor used to create an **AdvancedDialogV2Button** instance.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [AdvancedDialogV2ButtonOptions](#advanceddialogv2buttonoptions) | Yes | Configuration options of the button. |

#### AdvancedDialogV2ButtonOptions

Provides options used to initialize an **AdvancedDialogV2Button** object.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | Content of the button. |
| action | [AdvancedDialogV2ButtonAction](#advanceddialogv2buttonaction) | No | Yes | 
Action triggered when the button is clicked.

By default, there is no action.

 |
| background | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Background of the button.

The setting follows **buttonStyle** by default.

 |
| fontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Font color of the button.

The setting follows **buttonStyle** by default.

 |
| buttonStyle | [ButtonStyleMode](../../buttons-and-selections/button/document.md#buttonstylemode11) | No | Yes | 

Style of the button.

Default value: **ButtonStyleMode.NORMAL** for 2-in-1 devices and **ButtonStyleMode.TEXTUAL** for other devices

 |
| role | [ButtonRole](../../buttons-and-selections/button/document.md#buttonrole12) | No | Yes | 

Role of the button.

Default value: **ButtonRole.NORMAL**

 |
| defaultFocus | boolean | No | Yes | 

Whether the button is the default focus.

**true**: The button is the default focus.

**false**: The button is not the default focus.

Default value: **false**.

 |
| enabled | boolean | No | Yes | 

Whether the button is enabled.

**true**: The button is enabled.

**false**: The button is disabled.

Default value: **true**.

 |

#### Example

## Example 1: Dialog Box with an Image Above Text

This example implements a dialog box with an image above the text content, through the use of **imageRes**, **content**, and other properties.

import { TipsDialogV2, AdvancedDialogV2Button, UIContext  } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local checked: boolean = false;

  @Builder
  dialogBuilder(): void {
    TipsDialogV2({
      imageRes: $r('sys.media.ohos\_ic\_public\_voice'),
      content: 'Delete this app?',
      title: 'TipsDialogV2',
      checkTips: 'Do not show again',
      checked: this.checked,
      primaryButton: new AdvancedDialogV2Button({
        content: 'Cancel',
        action: () => {
          console.info('Callback when the first button is clicked');
        },
      }),
      secondaryButton: new AdvancedDialogV2Button({
        content: 'Delete',
        role: ButtonRole.ERROR,
        action: () => {
          console.info('Callback when the second button is clicked');
        }
      }),
      onCheckedChange: (checked: boolean) => {
        console.info('Callback when the checkbox is clicked');
        this.checked = checked;
      }
    })
  }

  build() {
    Row() {
      Stack() {
        Column() {
          Button("Open TipsDialogV2")
            .width(96)
            .height(40)
            .onClick(() => {
              let uiContext: UIContext = this.getUIContext();
              uiContext.getPromptAction().openCustomDialog({
                builder: () => {
                  this.dialogBuilder();
                },
              });
            })
        }.margin({ bottom: 300 })
      }.align(Alignment.Bottom)
      .width('100%').height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/HLpLYh5wT5qoV-UvVeRQtQ/en-us_image_0000002537765966.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B0A8E38C5A24F30EAA270180E44BF8503EC39C2F9C50C5F5723F7D80FF7053F)

## Example 2: List-only Dialog Box

This example presents a dialog box consisting solely of a list defined with **selectedIndex** and **radioContent**.

import { SelectDialogV2, AdvancedDialogV2Button ,UIContext  } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local radioIndex: number = 0;
  @Builder
  dialogBuilder(): void {
    SelectDialogV2({
      title:'Title',
      selectedIndex: this.radioIndex,
      confirm: new AdvancedDialogV2Button({
        content: 'Cancel',
        action: () => {},
      }),
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
    })
  }
  build() {
    Row() {
      Stack() {
        Column() {
          Button("List Dialog Box")
            .width(96)
            .height(40)
            .onClick(() => {
              let uiContext: UIContext = this.getUIContext();
              uiContext.getPromptAction().openCustomDialog({
                builder: () => {
                  this.dialogBuilder();
                }
              })
            })
        }.margin({ bottom: 300 })
      }.align(Alignment.Bottom)
      .width('100%').height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/uV_cAj3hSWaIoHFsLlppSg/en-us_image_0000002568765661.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4017633D8448E52488242B71355A25A90F85FBC9A01CD46DEDDCB6B26C254FF7)

## Example 3: Dialog Box with Text and Check Boxes

This example illustrates a dialog box that combines text content with check boxes defined with **content** and **checkTips**.

import { ConfirmDialogV2, AdvancedDialogV2Button, UIContext  } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local checked: boolean = false;

  @Builder
  dialogBuilder(): void {
    ConfirmDialogV2({
      title:'Title',
      content: 'This is where the content of this dialog box is presented.',
      checked: this.checked,
      checkTips: 'Do not ask me again',
      primaryButton: new AdvancedDialogV2Button({
        content: 'Deny',
        action: () => {
          console.info('Callback when the primary button is clicked');
        },
      }),
      secondaryButton: new AdvancedDialogV2Button({
        content: 'Allow',
        action: () => {
          this.checked = false
          console.info('Callback when the second button is clicked');
        }
      }),
      onCheckedChange: (checked: boolean) => {
        console.info('Callback when the checkbox is clicked');
        this.checked = checked;
      },
    })
  }

  build() {
    Row() {
      Stack() {
        Column() {
          Button("Open ConfirmDialogV2")
            .width(96)
            .height(40)
            .onClick(() => {
              let uiContext: UIContext = this.getUIContext();
              uiContext.getPromptAction().openCustomDialog({
                builder: () => {
                  this.dialogBuilder();
                },
                alignment: DialogAlignment.Bottom
              });
            })
        }.margin({ bottom: 300 })
      }.align(Alignment.Bottom)
      .width('100%').height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/R3xyNmu0SpCQn_hMBWraHA/en-us_image_0000002537765936.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BCD76CAA22852DE9664D89768476F16181E048DCE2243A0C7055322DCA84D122)

## Example 4: Text-only Dialog Box

This example demonstrates a simple text-only dialog box defined with **primaryTitle**, **secondaryTitle**, and **content**.

import { AlertDialogV2, AdvancedDialogV2Button, UIContext  } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Builder
  dialogBuilder(): void {
    AlertDialogV2({
      primaryTitle: 'Primary title',
      secondaryTitle: 'Secondary title',
      content: 'This is where content is displayed.',
      primaryButton: new AdvancedDialogV2Button({
        content: 'Cancel',
        action: () => {
          console.info('Callback when the primary button is clicked');
        },
      }),
      secondaryButton: new AdvancedDialogV2Button({
        content: 'OK',
        role: ButtonRole.ERROR,
        action: () => {
          console.info('Callback when the second button is clicked');
        }
      }),
    })
  }

  build() {
    Row() {
      Stack() {
        Column() {
          Button("Open AlertDialogV2")
            .width(96)
            .height(40)
            .onClick(() => {
              let uiContext: UIContext = this.getUIContext();
              uiContext.getPromptAction().openCustomDialog({
                builder: () => {
                  this.dialogBuilder();
                }
              });
            })
        }.margin({ bottom: 300 })
      }.align(Alignment.Bottom)
      .width('100%').height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/BeBvT1kHQBOsyVpNzcRxCQ/en-us_image_0000002537925876.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F32FE9B29E58ACD27294FEF33ADE1AF0A363F121C1947157AC3FC057CB7FA1F7)

## Example 5: Loading Dialog Box

This example implements a loading dialog box that contains a progress indicator.

import { LoadingDialogV2, UIContext  } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Builder
  dialogBuilder(): void {
    LoadingDialogV2({
      content: 'This is where content is displayed.',
    })
  }

  build() {
    Row() {
      Stack() {
        Column() {
          Button("Open LoadingDialogV2")
            .width(96)
            .height(40)
            .onClick(() => {
              let uiContext: UIContext = this.getUIContext();
              uiContext.getPromptAction().openCustomDialog({
                builder: () => {
                  this.dialogBuilder();
                }
              });
            })
        }.margin({ bottom: 300 })
      }.align(Alignment.Bottom)
      .width('100%').height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/xa9OrUhbTISjMaVrAb3wJg/en-us_image_0000002568685653.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E40745B518100888EF9BF9E5EF2614F21AEDC8B2982531A4067217D3CE4E19A)

## Example 6: Dialog Box with a Custom Theme

This example presents a dialog box with a custom theme, through the use of **content**, **theme**, and other properties.

import { CustomColors, CustomTheme, LoadingDialogV2, UIContext  } from '@kit.ArkUI';

class CustomThemeImpl implements CustomTheme {
  colors?: CustomColors;

  constructor(colors: CustomColors) {
    this.colors = colors;
  }
}

class CustomThemeColors implements CustomColors {
  fontPrimary = '#ffd0a300';
  iconSecondary = '#ffd000cd';
}

@Entry
@ComponentV2
struct Index {
  @Builder
  dialogBuilder(): void {
    WithTheme({ theme: new CustomThemeImpl(new CustomThemeColors()) }) {
      LoadingDialogV2({
        content: 'Text text text text text text...',
      })
    }
  }

  build() {
    Row() {
      Stack() {
        Column() {
          Button("Open LoadingDialogV2")
            .width(96)
            .height(40)
            .onClick(() => {
              let uiContext: UIContext = this.getUIContext();
              uiContext.getPromptAction().openCustomDialog({
                builder: () => {
                  this.dialogBuilder();
                }
              });
            })
        }.margin({ bottom: 300 })
      }.align(Alignment.Bottom)
      .width('100%').height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/bQQbIa9qSfSJhwdUqx7cgQ/en-us_image_0000002537925906.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B20083235F774A48B16584FAFCB35E30EE8CCDAC3F2A866EFD2E5E5DD5AC68EC)

## Example 7: Dialog Box with Custom Content

This example implements a dialog box with custom content defined with **contentBuilder** and **buttons**.

import { CustomContentDialogV2, AdvancedDialogV2Button, UIContext  } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Builder
  dialogBuilder(): void {
    CustomContentDialogV2({
      primaryTitle: 'Primary title',
      secondaryTitle: 'Secondary title',
      contentBuilder: () => {
        this.buildContent();
      },
      buttons: \[
        new AdvancedDialogV2Button({
          content: 'Button 1', buttonStyle: ButtonStyleMode.TEXTUAL,
          action: () => {
            console.info('Callback when the button is clicked');
          }
        }),
        new AdvancedDialogV2Button({
          content: 'Button 2', buttonStyle: ButtonStyleMode.TEXTUAL, role: ButtonRole.ERROR,
        })
      \],
    })
  }

  build() {
    Column() {
      Button("Open CustomContentDialogV2")
        .onClick(() => {
            let uiContext: UIContext = this.getUIContext();
            uiContext.getPromptAction().openCustomDialog({
            builder: () => {
              this.dialogBuilder();
            }
          })
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  @Builder
  buildContent(): void {
    Column() {
      Text('Content area')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/7btWtw-fSHSE4RToX_JbWQ/en-us_image_0000002568685683.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=556FD526EB5BD85E813037A429E5E950CC23712220003C5CA79780D0C04E0AFA)

## Example 8: Popover Dialog Box

This example demonstrates a popover dialog box for alert purposes, through the use of **visible**, **popover**, **targetBuilder**, and other properties.

import { AlertDialogV2, PopoverDialogV2, PopoverDialogV2Options, AdvancedDialogV2Button} from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local isShow: boolean = false;
  @Local popoverOptions: PopoverDialogV2Options = {
    builder: () => {
      this.dialogBuilder();
    }
  }

  @Builder dialogBuilder() {
    AlertDialogV2({
      content: 'Popover dialog box',
      primaryButton: new AdvancedDialogV2Button({
        content: 'Cancel',
        action: () => {
          this.isShow = false;
        },
      }),
      secondaryButton: new AdvancedDialogV2Button({
        content: 'OK',
        action: () => {
          this.isShow = false;
        },
      }),
    });
  }

  @Builder buttonBuilder() {
    Button('Target Component').onClick(() => {
      this.isShow = true;
    });
  }

  build() {
    Column() {
      PopoverDialogV2({
        visible: this.isShow!!,
        popover: this.popoverOptions,
        targetBuilder: () => {
          this.buttonBuilder();
        },
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/69UdwlZLTPSQsUvkfSLYqg/en-us_image_0000002568765693.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AFC18EB68385FBCD3B143222D09E4E80E7A8B5C7DCE5441505CC297AC325B97E)
