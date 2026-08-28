# Action Sheet (ActionSheet)

An action sheet is a dialog box that displays actions a user can take.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/lw8q_aBhTF-qSDGtNmU9lA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D808CDDEEBFADAE9BAEB4419127AB752A3A9E918E7858BD95950E92791A66123)

The initial APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

The functionality of this module depends on UI context. This means that the APIs of this module cannot be used where [the UI context is ambiguous](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). For details, see [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md).

#### ActionSheetOptions

Provides **ActionSheet** configuration options.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | No | 
Title of the dialog box.

If the text is too long to display, it is truncated with an ellipsis (...).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| subtitle10+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Subtitle of the dialog box.

If the text is too long to display, it is truncated with an ellipsis (...).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| message | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | No | 

Content of the dialog box.

If the text is too long to display, a scrollbar is displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| autoCancel | boolean | No | Yes | 

Whether to close the dialog box when the overlay is clicked.

Default value: **true**

The value **true** means to close the dialog box when the overlay is clicked, and **false** means the opposite.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| confirm | [ActionSheetButtonOptions](#actionsheetbuttonoptions18) | No | Yes | 

Information about the confirm button. When the dialog box has focus and the **Tab** key is not pressed for sequential focus navigation, the button responds to the **Enter** key by default. Multiple dialog boxes can automatically gain focus and respond to user interactions in a sequential manner. The default response to the **Enter** key does not work when **defaultFocus** is set to **true**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| cancel | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 

Callback invoked when the dialog box is closed after the overlay is clicked.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| alignment | [DialogAlignment](../alert-dialog-box-alertdialog/document.md#dialogalignment) | No | Yes | 

Alignment mode of the dialog box in the vertical direction.

Default value: **DialogAlignment.Bottom**

**Atomic service API**: This API can be used in atomic services since API version 11.

**NOTE**

If **showInSubWindow** is set to **true** in **UIExtension**, the dialog box is aligned with the host window based on **UIExtension**.

 |
| offset | [ActionSheetOffset](#actionsheetoffset18) | No | Yes | 

Offset of the dialog box relative to the alignment position.

Default value:

1\. If **alignment** is set to **Top**, **TopStart**, or **TopEnd**, the default offset value is **{dx: 0,dy: "40vp"}**.

2\. If **alignment** is set to other values, the default offset value is **{dx: 0,dy: "-40vp"}**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| sheets | Array<[SheetInfo](#sheetinfo)\> | No | No | 

Options in the dialog box. Each option supports the image, text, and callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| maskRect10+ | [Rectangle](../alert-dialog-box-alertdialog/document.md#rectangle8) | No | Yes | 

Mask area of the dialog box. Events outside the mask area are transparently transmitted, and events within the mask area are not.

Default value: **{ x: 0, y: 0, width: '100%', height: '100%' }**

**NOTE**

**maskRect** does not take effect when **showInSubWindow** is set to **true**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| showInSubWindow11+ | boolean | No | Yes | 

Whether to show the dialog box in a subwindow when the dialog box needs to be displayed outside the main window. **true**: The dialog box is shown in a subwindow.

Default value: **false**, meaning the dialog box is displayed within the application, not in a separate subwindow.

**NOTE**

A dialog box whose **showInSubWindow** attribute is **true** cannot trigger the display of another dialog box whose **showInSubWindow** attribute is also **true**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| isModal11+ | boolean | No | Yes | 

Whether the dialog box is a modal. A modal dialog box has a mask applied, while a non-modal dialog box does not. **false**: The dialog box is not a modal.

Default value: **true**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundColor11+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Background color of the dialog box.

Default value: **Color.Transparent**

**NOTE**

The background color will be visually combined with the blur effect when both properties are set. If the resulting effect does not match your design requirements, you can disable the blur effect entirely by explicitly setting the **backgroundBlurStyle** property to **BlurStyle.NONE**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundBlurStyle11+ | [BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | Yes | 

Background blur style of the dialog box.

Default value: **BlurStyle.COMPONENT\_ULTRA\_THICK**

**NOTE**

Setting this parameter to **BlurStyle.NONE** disables the background blur. When **backgroundBlurStyle** is set to a value other than **NONE**, do not set **backgroundColor**. If you do, the color display may not produce the expected visual effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](../../universal-attributes/basic-attributes/background/document.md#backgroundblurstyleoptions10) | No | Yes | 

Options for customizing the background blur style. For details about the default value, see **BackgroundBlurStyleOptions**.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| backgroundEffect19+ | [BackgroundEffectOptions](../../universal-attributes/basic-attributes/background/document.md#backgroundeffectoptions11) | No | Yes | 

Options for customizing the background effect. For details about the default value, see **BackgroundEffectOptions**.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| onWillDismiss12+ | Callback<[DismissDialogAction](#dismissdialogaction12)\> | No | Yes | 

Callback for interactive closure of the dialog box.

**NOTE**

1\. If this callback is registered, the dialog box will not be dismissed immediately after the user touches the mask or the Back button, presses the Esc key, or swipes left or right on the screen. The **reason** parameter in the callback is used to determine whether the dialog box can be closed. The reason returned by the component does not support the value **CLOSE\_BUTTON**.

2\. In the **onWillDismiss** callback, another **onWillDismiss** callback is not allowed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| cornerRadius12+ | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | [BorderRadiuses](../../common-definitions/basic-types/document.md#borderradiuses9) | [LocalizedBorderRadiuses](../../common-definitions/basic-types/document.md#localizedborderradiuses12) | No | Yes | 

Corner radius of the background.

You can set the radius for each of the four corners individually.

Default value: **{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }**

The corner radius is subject to the component size, with the maximum value being half of the component width or height. If the value is negative, the default value is used.

When set to a percentage, the value defines the radius as a percentage of the parent dialog box's width or height.

**NOTE**

When **cornerRadius** is of type LocalizedBorderRadiuses, the layout order can be dynamically adjusted based on the user's language settings.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| borderWidth12+ | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | [EdgeWidths](../../common-definitions/basic-types/document.md#edgewidths9) | [LocalizedEdgeWidths](../../common-definitions/basic-types/document.md#localizededgewidths12) | No | Yes | 

Border width of the dialog box.

You can set the width for all four sides or set separate widths for individual sides.

Default value: **0**

When set to a percentage, the value defines the border width as a percentage of the parent dialog box's width.

If the left and right borders are greater than its width, or the top and bottom borders are greater than its height, the dialog box may not display as expected.

**NOTE**

When **borderWidth** is of type LocalizedEdgeWidths, the layout order can be dynamically adjusted based on the user's language settings.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| borderColor12+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | [EdgeColors](../../common-definitions/basic-types/document.md#edgecolors9) | [LocalizedEdgeColors](../../common-definitions/basic-types/document.md#localizededgecolors12) | No | Yes | 

Border color of the dialog box.

Default value: **Color.Black**

**borderColor** must be used with **borderWidth** in pairs.

**NOTE**

When **borderColor** is of type LocalizedEdgeColors, the layout order can be dynamically adjusted based on the user's language settings.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| borderStyle12+ | [BorderStyle](../../common-definitions/enums/document.md#borderstyle) | [EdgeStyles](../../common-definitions/basic-types/document.md#edgestyles9) | No | Yes | 

Border style of the dialog box.

Default value: **BorderStyle.Solid**

**borderStyle** must be used with **borderWidth** in pairs.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| width12+ | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Width of the dialog box.

**NOTE**

\- Default maximum width of the dialog box: 400 vp

\- When this parameter is set to a percentage, the reference width of the dialog box is the width of the window where the dialog box is located. You can decrease or increase the width as needed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| height12+ | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Height of the dialog box.

**NOTE**

\- Default maximum height of the dialog box: 0.9 x (Window height – Safe area)

\- When this parameter is set to a percentage, the reference height of the dialog box is the height of the window where the dialog box is located minus the safe area. You can decrease or increase the height as needed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| shadow12+ | [ShadowOptions](../../universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../universal-attributes/visual-effects/image-effect/document.md#shadowstyle10) | No | Yes | 

Shadow of the dialog box.

Default value on 2-in-1 devices: **ShadowStyle.OUTER\_FLOATING\_MD** when the dialog box is focused and **ShadowStyle.OUTER\_FLOATING\_SM** otherwise On other devices, the dialog box has no shadow by default.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| transition12+ | [TransitionEffect](../../animation/component-transition-transition/document.md#transitioneffect10) | No | Yes | 

Transition effect for the entrance and exit of the dialog box.

**NOTE**

1\. If this parameter is not set, the default effect is used.

2\. Touching the Back button during the entrance animation pauses the entrance animation and starts the exit animation. The final effect is one obtained after the curves of the entrance and exit animations are combined.

3\. Touching the Back button during the exit animation does not affect the animation playback. Touching the Back button again closes the application.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| enableHoverMode14+ | boolean | No | Yes | 

Whether to respond when the device is in semi-folded mode. The value **true** means to respond when the device is in semi-folded mode.

Default value: **false**, meaning not to enable the hover mode.

**NOTE**

For a PC or 2-in-1 device, the dialog box is displayed on the upper half of the screen by default when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display the dialog box on the lower half of the screen. For other devices, the dialog box is displayed on the lower half of the screen by default when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display the dialog box on the upper half of the screen.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| hoverModeArea14+ | [HoverModeAreaType](../../universal-attributes/transition/sheet-transition/document.md#hovermodeareatype14) | No | Yes | 

Display area of the dialog box in hover mode.

Default value: **HoverModeAreaType.BOTTOM\_SCREEN**

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| onWillAppear19+ | Callback<void> | No | Yes | 

Event callback when the dialog box is about to appear.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

2\. You can set the callback event for changing the dialog box display effect in **onWillAppear**. The settings take effect next time the dialog box appears.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| onDidAppear19+ | Callback<void> | No | Yes | 

Event callback after the dialog box appears.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

2\. You can set the callback event for changing the dialog box display effect in **onDidAppear**. The settings take effect next time the dialog box appears.

3\. When a dialog box is dismissed immediately after being shown, **onWillDisappear** may be triggered before **onDidAppear**.

4\. If the dialog box is dismissed before its entrance animation is finished, the animation will be interrupted, and **onDidAppear** will not be triggered.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| onWillDisappear19+ | Callback<void> | No | Yes | 

Event callback when the dialog box is about to disappear.

**NOTE**

The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| onDidDisappear19+ | Callback<void> | No | Yes | 

Event callback after the dialog box disappears.

**NOTE**

The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| levelMode15+ | [LevelMode](#levelmode15) | No | Yes | 

Display level of the dialog box.

**NOTE**

\- Default value: **LevelMode.OVERLAY**

\- This parameter takes effect only when **showInSubWindow** is set to **false**.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| levelUniqueId15+ | number | No | Yes | 

[Unique ID](../../../arkts-api/ui/arkui/framenode/document.md#getuniqueid12) of the node under the display level for the page-level dialog box.

Value range: a number no less than 0

**NOTE**

\- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| immersiveMode15+ | [ImmersiveMode](#immersivemode15) | No | Yes | 

Overlay effect for the page-level dialog box.

**NOTE**

\- Default value: **ImmersiveMode.DEFAULT**

\- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| levelOrder18+ | [LevelOrder](../../../arkts-api/ui/ohos-promptaction-prompt/document.md#levelorder18) | No | Yes | 

Display order of the dialog box.

**NOTE**

\- Default value: **LevelOrder.clamp(0)**

\- Dynamic updating is not supported.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### SheetInfo

Defines the option content in the dialog box. You can configure the text, icon, and callback for each option.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | No | 
Sheet text.

If the text is too long to display, a scrollbar is displayed.

 |
| icon | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 

Sheet icon. By default, no icon is displayed.

The string type can be used to load local images and, more frequently, online images. The value can be a relative path to a local image, for example, **Image("common/test.jpg")**.

 |
| action | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | No | Callback when the sheet is selected. |

#### LevelMode15+

type LevelMode = LevelMode

Defines the display level mode for the dialog box.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [LevelMode](../../../arkts-api/ui/ohos-promptaction-prompt/document.md#levelmode15) | Display level of the dialog box. |

#### ImmersiveMode15+

type ImmersiveMode = ImmersiveMode

Defines the overlay effect for the dialog box.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [ImmersiveMode](../../../arkts-api/ui/ohos-promptaction-prompt/document.md#immersivemode15) | Overlay effect for the page-level dialog box. |

#### DismissDialogAction12+

Provides information about the action to dismiss the dialog box.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

## Properties

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| dismiss | Callback<void> | No | No | Callback for dismissing the dialog box. This API is called only when the dialog box needs to be exited. |
| reason | [DismissReason](../../universal-attributes/dialog-box-control/popup-control/document.md#dismissreason12) | No | No | Reason why the dialog box cannot be dismissed. You must specify whether to close the dialog box for each of the listed actions. |

#### ActionSheetButtonOptions18+

Provides button style configuration for the dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/AAqdoJGVRFayE5wUaozrUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04466FBEDC98FD976B2E7EC1C1A138EBD688F2909779251CAE836F324DF8861C)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| enabled10+ | boolean | No | Yes | 
Whether to respond when the button is clicked. The value **true** means to respond when the button is clicked, and **false** means the opposite.

Default value: **true**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| defaultFocus10+ | boolean | No | Yes | 

Whether the button is the default focus. The value **true** means that the button is the default focus, and **false** means the opposite.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| style10+ | [DialogButtonStyle](../../common-definitions/enums/document.md#dialogbuttonstyle10) | No | Yes | 

Button style.

Default value: **DialogButtonStyle.DEFAULT**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| value8+ | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | No | 

Button text.

If the text is too long to display, it is truncated with an ellipsis (...).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| action8+ | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | No | 

Callback invoked when the button is selected.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### ActionSheetOffset18+

Alignment mode of the dialog box.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| dx | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | No | 
Offset of the action sheet along the x-axis relative to the alignment position.

Explicitly specify the length unit explicitly, for example, **'10px'**, or provide the length in percentage, for example, **'100%'**.

**NOTE**

If the unit is not specified, the default unit vp is used, in which case **'10'** is equivalent to **10**.

 |
| dy | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | No | 

Offset of the action sheet along the y-axis relative to the alignment position.

Explicitly specify the length unit explicitly, for example, **'10px'**, or provide the length in percentage, for example, **'100%'**.

**NOTE**

If the unit is not specified, the default unit vp is used, in which case **'10'** is equivalent to **10**.

 |

#### ActionSheet

#### \[h2\]show(deprecated)

static show(value: ActionSheetOptions)

Shows an action sheet in the given settings.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/CEVkY8AnTaO6J8bguIopmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=588CF64ACEA3D78E356320DB5D47EB70867D9F939D39530FFAC16E618EEB9C68)

This API is supported since API version 8 and deprecated since API version 18. You are advised to use [showActionSheet](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#showactionsheet) instead. **showActionSheet** can be called only after a [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) instance is obtained.

Since API version 10, you can use [showActionSheet](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#showactionsheet) in [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to specify the UI execution context.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ActionSheetOptions](#actionsheetoptions) | Yes | Parameters of the action sheet. |

#### Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/ycQNdhWQQcOfcNeG5gZY0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8ADFEB0848E73288D2A93BF44227302BBE9B07DEB596717028025388CC350D01)

Directly using **ActionSheet** can lead to instance ambiguity. To avoid this, obtain the [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) object using the **getUIContext()** API and then use [showActionSheet](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#showactionsheet) to invoke the **ActionSheet.show()** method of the bound instance.

## Example 1: Displaying an Action Sheet

This example demonstrates how to display an action sheet when a button is touched.

// xxx.ets
@Entry
@Component
struct ActionSheetExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('Click to Show ActionSheet')
        .onClick(() => {
          this.getUIContext().showActionSheet({
            title: 'ActionSheet title',
            subtitle: 'ActionSheet subtitle',
            message: 'message',
            autoCancel: true,
            confirm: {
              defaultFocus: true,
              value: 'Confirm button',
              action: () => {
                console.info('Get ActionSheet handled');
              }
            },
            cancel: () => {
              console.info('ActionSheet canceled');
            },
            onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
              console.info(\`reason= ${dismissDialogAction.reason}\`);
              console.info('ActionSheet onWillDismiss');
              if (dismissDialogAction.reason === DismissReason.PRESS\_BACK) {
                dismissDialogAction.dismiss();
              }
              if (dismissDialogAction.reason === DismissReason.TOUCH\_OUTSIDE) {
                dismissDialogAction.dismiss();
              }
            },
            alignment: DialogAlignment.Bottom,
            offset: { dx: 0, dy: -10 },
            sheets: \[
              {
                title: 'apples',
                action: () => {
                  console.info('apples');
                }
              },
              {
                title: 'bananas',
                action: () => {
                  console.info('bananas');
                }
              },
              {
                title: 'pears',
                action: () => {
                  console.info('pears');
                }
              }
            \]
          })
        })
    }.width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/pJ_o0wb7ShmT5H003fj8CA/en-us_image_0000002537765910.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B056E74794525364A6D22A864B5F1776E8D4D2C6118ED998171C7A1AD05C1DFB)

## Example 2: Opening a Dialog Box Outside the Main Window

This example demonstrates how to configure a dialog box to display outside the main window on a 2-in-1 device by setting [showInSubWindow](#actionsheetoptions) to **true**.

// xxx.ets
@Entry
@Component
struct ActionSheetExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('Click to Show ActionSheet')
        .onClick(() => {
          this.getUIContext().showActionSheet({
            title: 'ActionSheet title',
            subtitle: 'ActionSheet subtitle',
            message: 'message',
            autoCancel: true,
            showInSubWindow: true,
            isModal: true,
            confirm: {
              defaultFocus: true,
              value: 'Confirm button',
              action: () => {
                console.info('Get ActionSheet handled');
              }
            },
            cancel: () => {
              console.info('ActionSheet canceled');
            },
            onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
              console.info(\`reason= ${dismissDialogAction.reason}\`);
              console.info('ActionSheet onWillDismiss');
              if (dismissDialogAction.reason === DismissReason.PRESS\_BACK) {
                dismissDialogAction.dismiss();
              }
              if (dismissDialogAction.reason === DismissReason.TOUCH\_OUTSIDE) {
                dismissDialogAction.dismiss();
              }
            },
            alignment: DialogAlignment.Center,
            offset: { dx: 0, dy: -10 },
            sheets: \[
              {
                title: 'apples',
                action: () => {
                  console.info('apples');
                }
              },
              {
                title: 'bananas',
                action: () => {
                  console.info('bananas');
                }
              },
              {
                title: 'pears',
                action: () => {
                  console.info('pears');
                }
              }
            \]
          })
        })
    }.width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/Fr7Y5Ft8TnGotJ5nO5tObw/en-us_image_0000002537925850.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A3E01C4B9CD2E48514A5F2C7D1865A1C5F1E00F43A513848B25EECF8D1E9824)

## Example 3: Setting the Dialog Box Animation

This example illustrates how to use the [transition](#actionsheetoptions) API to create custom animation effects for the dialog box's appearance and disappearance.

// xxx.ets
@Entry
@Component
struct ActionSheetExample {
  build() {
    Column({ space: 5 }) {
      Button('ActionSheet Set Duration')
        .onClick(() => {
          this.getUIContext().showActionSheet({
            title: 'ActionSheet 1',
            message: 'Set Animation Duration open 3 second, close 100 ms',
            autoCancel: true,
            alignment: DialogAlignment.Top,
            transition: TransitionEffect.asymmetric(TransitionEffect.OPACITY
              .animation({ duration: 3000, curve: Curve.Sharp })
              .combine(TransitionEffect.scale({ x: 1.5, y: 1.5 }).animation({ duration: 3000, curve: Curve.Sharp })),
              TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
                .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 }).animation({ duration: 100, curve: Curve.Smooth }))),
            offset: { dx: 0, dy: -20 },
            confirm: {
              value: 'button',
              action: () => {
                console.info('Button-clicking callback');
              }
            },
            cancel: () => {
              console.info('Closed callbacks');
            },
            sheets: \[
              {
                title: 'apples',
                action: () => {
                  console.info('apples');
                }
              },
              {
                title: 'bananas',
                action: () => {
                  console.info('bananas');
                }
              },
              {
                title: 'pears',
                action: () => {
                  console.info('pears');
                }
              }
            \]
          })
        }).backgroundColor(0x317aff).height("88px")
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/kYAPunuwRBKmi68AmqC1Kg/en-us_image_0000002568685627.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0FEA4B01BC3D6612840C37BCCCDA15DF5999539BAED82EA4C80D11F27C88BF14)

## Example 4: Setting the Dialog Box Style

This example demonstrates how to set styles of a dialog box, including the width, height, background color, and shadow.

// xxx.ets
@Entry
@Component
struct ActionSheetExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
      Button('Click to Show ActionSheet')
        .onClick(() => {
          this.getUIContext().showActionSheet({
            title: 'ActionSheet title',
            subtitle: 'ActionSheet subtitle',
            message: 'message',
            autoCancel: true,
            width: 300,
            height: 350,
            cornerRadius: 20,
            borderWidth: 1,
            borderStyle: BorderStyle.Solid, // borderStyle must be used with borderWidth in pairs.
            borderColor: Color.Blue, // borderColor must be used with borderWidth in pairs.
            backgroundColor: Color.White,
            shadow: ({
              radius: 20,
              color: Color.Grey,
              offsetX: 50,
              offsetY: 0
            }),
            confirm: {
              defaultFocus: true,
              value: 'Confirm button',
              action: () => {
                console.info('Get ActionSheet handled');
              }
            },
            cancel: () => {
              console.info('ActionSheet canceled');
            },
            onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
              console.info(\`reason= ${dismissDialogAction.reason}\`);
              console.info('ActionSheet onWillDismiss');
              if (dismissDialogAction.reason === DismissReason.PRESS\_BACK) {
                dismissDialogAction.dismiss();
              }
              if (dismissDialogAction.reason === DismissReason.TOUCH\_OUTSIDE) {
                dismissDialogAction.dismiss();
              }
            },
            alignment: DialogAlignment.Bottom,
            offset: { dx: 0, dy: -10 },
            sheets: \[
              {
                title: 'apples',
                action: () => {
                  console.info('apples');
                }
              },
              {
                title: 'bananas',
                action: () => {
                  console.info('bananas');
                }
              },
              {
                title: 'pears',
                action: () => {
                  console.info('pears');
                }
              }
            \]
          })
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/rmdQIFboTZG3bHpDbzC2qA/en-us_image_0000002568765637.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65F244AD1BF99F082FEBF6DF26ADA329FF9E5620D1023B967355391921CB3DA0)

## Example 5: Configuring a Dialog Box in the Hover State

This example demonstrates how to set the layout area of a dialog box in hover mode on a foldable device.

// xxx.ets
@Entry
@Component
struct ActionSheetExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('Click to Show ActionSheet')
        .onClick(() => {
          this.getUIContext().showActionSheet({
            title: 'ActionSheet title',
            subtitle: 'ActionSheet subtitle',
            message: 'message',
            autoCancel: true,
            confirm: {
              defaultFocus: true,
              value: 'Confirm button',
              action: () => {
                console.info('Get ActionSheet handled');
              }
            },
            cancel: () => {
              console.info('ActionSheet canceled');
            },
            onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
              console.info(\`reason= ${dismissDialogAction.reason}\`);
              console.info('ActionSheet onWillDismiss');
              if (dismissDialogAction.reason === DismissReason.PRESS\_BACK) {
                dismissDialogAction.dismiss();
              }
              if (dismissDialogAction.reason === DismissReason.TOUCH\_OUTSIDE) {
                dismissDialogAction.dismiss();
              }
            },
            alignment: DialogAlignment.Bottom,
            offset: { dx: 0, dy: -10 },
            enableHoverMode: true,
            hoverModeArea: HoverModeAreaType.TOP\_SCREEN,
            sheets: \[
              {
                title: 'apples',
                action: () => {
                  console.info('apples');
                }
              },
              {
                title: 'bananas',
                action: () => {
                  console.info('bananas');
                }
              },
              {
                title: 'pears',
                action: () => {
                  console.info('pears');
                }
              }
            \]
          })
        })
    }.width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/UjcflO8SRZKcgqW4-yPStg/en-us_image_0000002537765908.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B54149E2E30851A438156E9F610328DB43B321719452DCAED6EB9388AEA10659)

## Example 6: Using Dialog Box Lifecycle Callbacks

This example demonstrates how to configure the lifecycle callbacks for the dialog box.

The **onDidAppear**, **onDidDisappear**, **onWillAppear**, and **onWillDisappear** properties are supported in [ActionSheetOptions](#actionsheetoptions) since API version 19.

// xxx.ets
@Entry
@Component
struct Example1 {
  @State log: string = 'Log information:';
  flag: boolean = false;

  build() {
    Column({ space: 5 }) {
      Button('ActionSheet')
        .onClick(() => {
          this.getUIContext().showActionSheet({
            title: 'ActionSheet',
            message: 'message',
            autoCancel: true,
            alignment: DialogAlignment.Bottom,
            offset: { dx: 0, dy: -20 },
            confirm: {
              value: 'button',
              action: () => {
                console.info('ActionSheet Button-clicking callback');
              }
            },
            cancel: () => {
              console.info('ActionSheet Closed callbacks');
            },
            sheets: \[
              {
                title: 'apples',
                action: () => {
                  console.info('ActionSheet apples')
                }
              },
              {
                title: 'bananas',
                action: () => {
                  console.info('ActionSheet bananas')
                }
              },
              {
                title: 'pears',
                action: () => {
                  console.info('ActionSheet pears')
                }
              }
            \],
            onDidAppear: () => {
              this.log += '# onDidAppear';
              console.info('ActionSheet,is onDidAppear!');
            },
            onDidDisappear: () => {
              this.log += '# onDidDisappear';
              console.info('ActionSheet,is onDidDisappear!');
            },
            onWillAppear: () => {
              this.log = 'Log information:onWillAppear';
              console.info('ActionSheet,is onWillAppear!');
            },
            onWillDisappear: () => {
              this.log += '# onWillDisappear';
              console.info('ActionSheet,is onWillDisappear!');
            }
          })
        })
      Text(this.log).fontSize(30).margin({ top: 200 })
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/hQ0v8CWnRvmU6DP-bqlFNg/en-us_image_0000002537765912.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBBC5C6F6AB224FF78555EA3E43F383CBA213E00AB0F4860B88945A452F2EA5C)

## Example 7: Customizing the Background Blur Effect

This example demonstrates how to customize the background blur effect by configuring [backgroundBlurStyleOptions](#actionsheetoptions).

The **backgroundBlurStyleOptions** property is supported in [ActionSheetOptions](#actionsheetoptions) since API version 19.

@Entry
@Component
struct ActionSheetExample {
  build() {
    Stack({ alignContent: Alignment.Top }) {
      Image($r('app.media.bg'))
      Column() {
        Button("ActionSheet")
          .margin(20)
          .onClick(() => {
            this.getUIContext().showActionSheet({
              title: 'ActionSheet Title',
              subtitle: 'ActionSheet Subtitle',
              message: 'ActionSheet Text',
              sheets: \[
                {
                  title: 'Apples',
                  action: () => {
                    console.info('apples');
                  }
                },
                {
                  title: 'Bananas',
                  action: () => {
                    console.info('bananas');
                  }
                },
                {
                  title: 'Pears',
                  action: () => {
                    console.info('pears');
                  }
                }
              \],
              alignment: DialogAlignment.Center,
              backgroundColor: undefined,
              backgroundBlurStyle: BlurStyle.Thin,
              backgroundBlurStyleOptions: {
                colorMode: ThemeColorMode.LIGHT,
                adaptiveColor: AdaptiveColor.AVERAGE,
                scale: 1,
                blurOptions: { grayscale: \[20, 20\] },
              },
            });
          })
      }.width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/HHxYBuO4R-aHH0yd6YEo8Q/en-us_image_0000002537925852.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA51338ABB8F310152138EEC13A6B0F1F01841737B0352456F34B7DBB845FCB6)

## Example 8: Customizing the Background Effect

This example demonstrates how to customize the background effect by configuring [backgroundEffect](#actionsheetoptions).

The **backgroundEffect** property is supported in [ActionSheetOptions](#actionsheetoptions) since API version 19.

@Entry
@Component
struct ActionSheetExample {
  build() {
    Stack({ alignContent: Alignment.Top }) {
      Image($r('app.media.bg'))
      Column() {
        Button("ActionSheet")
          .margin(20)
          .onClick(() => {
            this.getUIContext().showActionSheet({
              title: 'ActionSheet Title',
              subtitle: 'ActionSheet Subtitle',
              message: 'ActionSheet Text',
              sheets: \[
                {
                  title: 'Apples',
                  action: () => {
                    console.info('apples');
                  }
                },
                {
                  title: 'Bananas',
                  action: () => {
                    console.info('bananas');
                  }
                },
                {
                  title: 'Pears',
                  action: () => {
                    console.info('pears');
                  }
                }
              \],
              alignment: DialogAlignment.Center,
              backgroundColor: undefined,
              backgroundBlurStyle: BlurStyle.Thin,
              backgroundEffect: {
                radius: 60,
                saturation: 0,
                brightness: 1,
                color: Color.White,
                blurOptions: { grayscale: \[20, 20\] }
              },
            });
          })
      }.width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/AcS3CyL6Q0uL9nyNzo-3kQ/en-us_image_0000002568685629.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4F5541C54FC97B471B5EA539CAD3245CABEBFD2EA8F1CCF1BB69B38B91588CA)
