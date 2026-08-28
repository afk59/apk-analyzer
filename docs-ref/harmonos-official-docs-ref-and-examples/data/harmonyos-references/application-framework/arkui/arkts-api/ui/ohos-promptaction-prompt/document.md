# @ohos.promptAction (Prompt)

This module provides API for creating and displaying toasts, dialog boxes, and action menus.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/_tvNLErkSOarxqEN5RuXyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2DE81F0F0C057BFDB0A6DCA01B37194DC4F4A772F27923D63078C837C03E54F5)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   This module cannot be used in the file declaration of the [UIAbility](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md). In other words, the APIs of this module can be used only after a component instance is created; they cannot be called in the lifecycle of the UIAbility.
    
-   The functionality of this module depends on UI context. This means that the APIs of this module cannot be used where [the UI context is ambiguous](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). For details, see [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md). It is recommended that you use the dialog box APIs provided by **UIContext**.
    

#### Modules to Import

import { promptAction } from '@kit.ArkUI';

#### promptAction.openToast18+

openToast(options: ShowToastOptions): Promise<number>

Shows a toast. This API uses a promise to return the toast ID.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/euIEmAOkT-WB_A2SVIF4eg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0756D35897EEBA3493D6770B68420651C71A53B192E2719B9ACC0A3CB092213D)

-   Subwindows with **showMode** set to **TOP\_MOST** or **SYSTEM\_TOP\_MOST** do not support **openToast** in input method type windows. For details, see the constraints in the input method framework [createPanel](../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#createpanel10-1).
    
-   Directly using **openToast** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). To avoid this, obtain the **PromptAction** object using the **getPromptAction** API in **UIContext** and then call the [openToast](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md#opentoast18) API through this object.
    

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ShowToastOptions](#showtoastoptions) | Yes | Toast configuration options. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise that returns the toast ID for use with **closeToast**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { PromptAction, UIContext } from '@kit.ArkUI';

@Entry
@Component
struct toastExample {
  @State toastId: number = 0;
  uiContext: UIContext = this.getUIContext();
  promptAction: PromptAction = this.uiContext.getPromptAction();

  build() {
    Column() {
      Button('Open Toast')
        .height(100)
        .type(ButtonType.Capsule)
        .onClick(() => {
          this.promptAction.openToast({
            message: 'Toast Message',
            duration: 10000,
          }).then((toastId: number) => {
            this.toastId = toastId;
          })
            .catch((error: BusinessError) => {
              console.error(\`openToast error code is ${error.code}, message is ${error.message}\`);
            })
        })
      Blank().height(50)
      Button('Close Toast')
        .height(100)
        .type(ButtonType.Capsule)
        .onClick(() => {
          try {
            this.promptAction.closeToast(this.toastId);
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(\`CloseToast error code is ${code}, message is ${message}\`);
          }
        })
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/blKOhnehRPijOh88rEl8vw/en-us_image_0000002537765336.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56E7317F1387AE8D50FA2BA003B36AF9CF79AEBE03D9E4C4C8834E4F7640047C)

#### promptAction.closeToast18+

closeToast(toastId: number): void

Closes the specified toast.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/LlnkoFIBSE6VKlik2tcXOA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCC3D69C5BC676BC2F2666D34D1E3354F0C1561715AC3E9F89F76921B742C8AA)

Directly using **closeToast** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). To avoid this, obtain the **PromptAction** object using the **getPromptAction** API in **UIContext** and then call the [closeToast](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md#closetoast18) API through this object.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| toastId | number | Yes | Toast ID returned from **openToast**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Popup Window Error Codes](../../../error-codes/ui/popup-window-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 103401 | Cannot find the toast. |

**Example**

See the example for [promptAction.openToast18](#promptactionopentoast18).

#### ShowToastOptions

Provides toast configuration options.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| message | string | [Resource](../../../arkts-components/common-definitions/basic-types/document.md#resource) | No | No | 
Text to display.

**NOTE**

The default font is **'Harmony Sans'**. Other fonts are not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| duration | number | No | Yes | 

Duration that the toast will remain on the screen.

Default value: 1500 ms.

Value range: \[1500, 10000\].

If a value less than 1500 ms is set, the default value is used. If the value greater than 10000 ms is set, the upper limit 10000 ms is used.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| bottom | string | number | No | Yes | 

Distance from the bottom of the toast to the navigation bar. If the soft keyboard is raised and the **bottom** value is too small, the toast will automatically avoid being blocked by the soft keyboard by moving up 80 vp above it.

Default value: **80vp**

**NOTE**

When there is no navigation bar at the bottom, **bottom** sets the distance from the bottom of the toast to the bottom of the window.

If the **alignment** property is set, **bottom** will not take effect.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| alignment12+ | [Alignment](../../../arkts-components/common-definitions/enums/document.md#alignment) | No | Yes | 

Alignment mode.

Default value: **undefined**. If **alignment** is not set and a navigation bar or soft keyboard is present, the toast is automatically adjusted according to the position of the navigation bar or soft keyboard. For details, see the description of **bottom**.

**NOTE**

The figure below shows the position of the toast in different alignment modes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/Bnrv5eBqT3GCGn6MNxomgQ/en-us_image_0000002537925276.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=083BDA8563A185EDF37E56D5DBEDA3CDF35B1986A91E2F2773179524D9B129A4)

The text display of the toast is always left-aligned; other alignment modes are not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| offset12+ | [Offset](../../../arkts-components/common-definitions/basic-types/document.md#offset) | No | Yes | 

Offset in the specified alignment mode.

Default value: **{ dx: 0, dy: 0 }**, indicating no offset

**NOTE**

Only values in units of px are supported. Values in other units must be converted to units of px before being passed in. For example, to set a value in vp, convert it to px first and then pass the converted value.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| showMode11+ | [ToastShowMode](#toastshowmode11) | No | Yes | 

Display level mode of the toast.

Default value: **ToastShowMode.DEFAULT**, which means to show the toast in the application.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundColor12+ | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Background color of the toast.

Default value: **Color.Transparent**.

**NOTE**

The background color will be visually combined with the blur effect when both properties are set. If the resulting effect does not match your design requirements, you can disable the blur effect entirely by explicitly setting the **backgroundBlurStyle** property to **BlurStyle.NONE**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| textColor12+ | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Text color of the toast.

Default value: **Color.Black**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundBlurStyle12+ | [BlurStyle](../../../arkts-components/universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | Yes | 

Background blur style of the toast.

Default value: **BlurStyle.COMPONENT\_ULTRA\_THICK**

**NOTE**

Setting this parameter to **BlurStyle.NONE** disables the background blur. When **backgroundBlurStyle** is set to a value other than **NONE**, do not set **backgroundColor**. If you do, the color display may not produce the expected visual effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| shadow12+ | [ShadowOptions](../../../arkts-components/universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../../arkts-components/universal-attributes/visual-effects/image-effect/document.md#shadowstyle10) | No | Yes | 

Shadow of the toast background.

Default value: **ShadowStyle.OUTER\_DEFAULT\_MD**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| enableHoverMode14+ | boolean | No | Yes | 

Whether to respond when the device is in semi-folded mode. The value **true** means to respond when the device is in semi-folded mode.

Default value: **false**, meaning not to respond when the device is in semi-folded mode.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| hoverModeArea14+ | [HoverModeAreaType](../../../arkts-components/universal-attributes/transition/sheet-transition/document.md#hovermodeareatype14) | No | Yes | 

Display area of the toast in the hover state.

Default value: **HoverModeAreaType.BOTTOM\_SCREEN**, indicating that the toast is displayed in the lower half screen

**Atomic service API**: This API can be used in atomic services since API version 14.

 |

#### ToastShowMode11+

Enumerates display modes for toasts. By default, the toast is displayed within the application and supports display in subwindows.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | The toast is displayed within the application. |
| TOP\_MOST | 1 | The toast is displayed in a subwindow. |

#### ShowDialogOptions

Describes the options for showing the dialog box.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | [Resource](../../../arkts-components/common-definitions/basic-types/document.md#resource) | No | Yes | 
Title of the dialog box.

Default value: **undefined**, which indicates that no title is not displayed by default.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| message | string | [Resource](../../../arkts-components/common-definitions/basic-types/document.md#resource) | No | Yes | 

Text body.

Default value: **undefined**, which indicates that no content is displayed by default.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| buttons | Array<[Button](#button)\> | No | Yes | 

Array of buttons in the dialog box. The array structure is {text:'button', color: '#666666'}. More than one button is supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| alignment10+ | [DialogAlignment](../../../arkts-components/dialog-boxes/alert-dialog-box-alertdialog/document.md#dialogalignment) | No | Yes | 

Alignment mode of the dialog box in the vertical direction.

Default value: **DialogAlignment.Default**

**NOTE**

If **showInSubWindow** is set to **true** in **UIExtension**, the dialog box is aligned with the host window based on **UIExtension**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| offset10+ | [Offset](../../../arkts-components/common-definitions/basic-types/document.md#offset) | No | Yes | 

Offset of the dialog box relative to the alignment position.

Default value: **{ dx: 0 , dy: 0 }**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| maskRect10+ | [Rectangle](../../../arkts-components/dialog-boxes/alert-dialog-box-alertdialog/document.md#rectangle8) | No | Yes | 

Mask area of the dialog box. Events within the mask area are blocked, while events outside the mask area are transmitted.

Default value: **{ x: 0, y: 0, width: '100%', height: '100%' }**

**NOTE**

**maskRect** does not take effect when **showInSubWindow** is set to **true**.

If only some properties in [Rectangle](../../../arkts-components/dialog-boxes/alert-dialog-box-alertdialog/document.md#rectangle8) are set, the unset properties default to 0.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| showInSubWindow11+ | boolean | No | Yes | 

Whether to show the dialog box in a subwindow when the dialog box needs to be displayed outside the main window.

**true**: The dialog box is shown in a subwindow.

**false** (default): The dialog box is displayed within the application, not in a separate subwindow.

Note: A dialog box whose **showInSubWindow** attribute is **true** cannot trigger the display of another dialog box whose **showInSubWindow** attribute is also **true**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| isModal11+ | boolean | No | Yes | 

Whether the dialog box is a modal, which has a mask applied and does not allow for interaction with other components around the dialog box.

**true**: The dialog box is a modal.

**false**: The dialog box is not a modal.

Default value: **true**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundColor12+ | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Background color of the dialog box.

Default value: **Color.Transparent**.

**NOTE**

The background color will be visually combined with the blur effect when both properties are set. If the resulting effect does not match your design requirements, you can disable the blur effect entirely by explicitly setting the **backgroundBlurStyle** property to **BlurStyle.NONE**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundBlurStyle12+ | [BlurStyle](../../../arkts-components/universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | Yes | 

Background blur style of the dialog box.

Default value: **BlurStyle.COMPONENT\_ULTRA\_THICK**

**NOTE**

Setting this parameter to **BlurStyle.NONE** disables the background blur. When **backgroundBlurStyle** is set to a value other than **NONE**, do not set **backgroundColor**. If you do, the color display may not produce the expected visual effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](../../../arkts-components/universal-attributes/basic-attributes/background/document.md#backgroundblurstyleoptions10) | No | Yes | 

Options for customizing the background blur style. For details about the default value, see **BackgroundBlurStyleOptions**.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| backgroundEffect19+ | [BackgroundEffectOptions](../../../arkts-components/universal-attributes/basic-attributes/background/document.md#backgroundeffectoptions11) | No | Yes | 

Options for customizing the background effect. For details about the default value, see **BackgroundEffectOptions**.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| shadow12+ | [ShadowOptions](../../../arkts-components/universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../../arkts-components/universal-attributes/visual-effects/image-effect/document.md#shadowstyle10) | No | Yes | 

Shadow of the dialog box.

Default value on 2-in-1 devices: **ShadowStyle.OUTER\_FLOATING\_MD** when the dialog box is focused and **ShadowStyle.OUTER\_FLOATING\_SM** otherwise On other devices, the dialog box has no shadow by default.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| enableHoverMode14+ | boolean | No | Yes | 

Whether to respond when the device is in semi-folded mode. The value **true** means to respond when the device is in semi-folded mode.

Default value: **false**, meaning not to respond when the device is in semi-folded mode.

**NOTE**

For a PC or 2-in-1 device, the prompt is displayed on the upper half of the screen by default when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display the prompt on the lower half of the screen. For other devices, the prompt is displayed on the lower half of the screen by default when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display the prompt on the upper half of the screen.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| hoverModeArea14+ | [HoverModeAreaType](../../../arkts-components/universal-attributes/transition/sheet-transition/document.md#hovermodeareatype14) | No | Yes | 

Default display area of the dialog box in semi-folded mode.

Default value: **HoverModeAreaType.BOTTOM\_SCREEN**

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| onWillAppear19+ | Callback<void> | No | Yes | 

Callback invoked before the dialog box appearance animation.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

2\. You can set the callback event for changing the dialog box display effect in **onWillAppear**. The settings take effect next time the dialog box appears.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| onDidAppear19+ | Callback<void> | No | Yes | 

Callback invoked after the dialog box appears.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

2\. You can set the callback event for changing the dialog box display effect in **onDidAppear**. The settings take effect next time the dialog box appears.

3\. When a dialog box is dismissed immediately after being shown, **onWillDisappear** may be triggered before **onDidAppear**.

4\. If the dialog box is dismissed before its appearance animation is finished, the animation will be interrupted, and **onDidAppear** will not be invoked.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| onWillDisappear19+ | Callback<void> | No | Yes | 

Callback invoked before the dialog box disappearance animation.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| onDidDisappear19+ | Callback<void> | No | Yes | 

Callback invoked after the dialog box disappears.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

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

[Unique ID](../arkui/framenode/document.md#getuniqueid12) of the node under the display level for the page-level dialog box.

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
| levelOrder18+ | [LevelOrder](#levelorder18) | No | Yes | 

Display order of the dialog box.

**NOTE**

\- Default value: **LevelOrder.clamp(0)**

\- Dynamic updating is not supported.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### ShowDialogSuccessResponse

Describes the dialog box response result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| index | number | No | No | Index of the selected button in the **buttons** array, starting from **0**. |

#### ActionMenuOptions

Describes the options for showing the action menu.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | [Resource](../../../arkts-components/common-definitions/basic-types/document.md#resource) | No | Yes | 
Title of the dialog box.

Default value: **undefined**, which indicates that no title is not displayed by default.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| buttons | \[[Button](#button),[Button](#button)?,[Button](#button)?,[Button](#button)?,[Button](#button)?,[Button](#button)?\] | No | No | 

Array of menu item buttons. The array structure is **{text:'button', color: '#666666'}**. Up to six buttons are supported. If there are more than six buttons, only the first six buttons will be displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| showInSubWindow11+ | boolean | No | Yes | 

Whether to show the menu in a subwindow when the menu needs to be displayed outside the main window.

**true**: The menu is shown in a subwindow.

Default value: **false**, indicating that the dialog box is not displayed in a subwindow.

**NOTE**

\- A menu whose **showInSubWindow** attribute is **true** cannot trigger the display of another menu whose **showInSubWindow** attribute is also **true**.

\- If **showInSubWindow** is set to **true** in **UIExtension**, the menu is aligned with the host window based on **UIExtension**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| isModal11+ | boolean | No | Yes | 

Whether the menu is a modal, which has a mask applied and does not allow for interaction with other components around the menu.

**true**: The menu is a modal.

**false**: The menu is not a modal.

Default value: **true**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| levelMode15+ | [LevelMode](#levelmode15) | No | Yes | 

Display level mode of the menu.

**NOTE**

\- Default value: **LevelMode.OVERLAY**

\- This parameter takes effect only when **showInSubWindow** is set to **false**.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| levelUniqueId15+ | number | No | Yes | 

[Unique ID](../arkui/framenode/document.md#getuniqueid12) of the node under the display level for the page-level menu.

Value range: a number no less than 0

**NOTE**

\- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| immersiveMode15+ | [ImmersiveMode](#immersivemode15) | No | Yes | 

Overlay effect for the page-level menu.

**NOTE**

\- Default value: **ImmersiveMode.DEFAULT**

\- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| onWillAppear20+ | Callback<void> | No | Yes | 

Callback invoked before the menu appearance animation.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| onDidAppear20+ | Callback<void> | No | Yes | 

Callback invoked after the menu appears.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

2\. When a menu is dismissed immediately after being shown, **onWillDisappear** may be triggered before **onDidAppear**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| onWillDisappear20+ | Callback<void> | No | Yes | 

Callback invoked before the menu disappearance animation.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| onDidDisappear20+ | Callback<void> | No | Yes | 

Callback invoked after the menu disappears.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### ActionMenuSuccessResponse

Describes the action menu response result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| index | number | No | No | Index of the selected button in the **buttons** array, starting from **0**. |

#### CommonState20+

Enumerates states of the custom dialog box.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| UNINITIALIZED | 0 | State before the controller is bound to the dialog box. |
| INITIALIZED | 1 | State after the controller is bound to the dialog box. |
| APPEARING | 2 | State during the dialog box appearance animation. |
| APPEARED | 3 | State after the dialog display appearance ends. |
| DISAPPEARING | 4 | State during the dialog box disappearance animation. |
| DISAPPEARED | 5 | State after the dialog box disappearance animation ends. |

#### DialogController18+

Implements a custom dialog controller that inherits from [CommonController](#commoncontroller18).

It can be used as a member variable of **UIContext** to display custom dialog boxes. For specific usage, see the examples for [openCustomDialogWithController](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md#opencustomdialogwithcontroller18) and [presentCustomDialog](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md#presentcustomdialog18).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### CommonController18+

Implements a common controller for managing components related to **promptAction**.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor18+

constructor()

A constructor used to create a controller instance.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]close18+

close(): void

Closes the custom dialog box. If the dialog box is already closed, this API has no effect.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]getState20+

getState(): CommonState

Obtains the state of the custom dialog box.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [CommonState](#commonstate20) | State of the custom dialog box. |

#### LevelOrder18+

Defines the display order of a dialog box.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]clamp18+

static clamp(order: number): LevelOrder

Creates a dialog box level with the specified order.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| order | number | Yes | Display order of the dialog box. The value range is \[-100000.0, +100000.0\]. Values outside this range are clamped to the nearest limit. |

**Return value**

| Type | Description |
| :-- | :-- |
| [LevelOrder](#levelorder18) | Current instance. |

#### \[h2\]getOrder18+

getOrder(): number

Obtains the display order of this dialog box.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Display order of the dialog box. |

#### DialogOptions18+

Extends [BaseDialogOptions](#basedialogoptions11) to provide enhanced customization capabilities for the dialog box.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| backgroundColor | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 
Background color of the dialog box.

Default value: **Color.Transparent**.

**NOTE**

The background color will be visually combined with the blur effect when both properties are set. If the resulting effect does not match your design requirements, you can disable the blur effect entirely by explicitly setting the **backgroundBlurStyle** property to **BlurStyle.NONE**.

 |
| cornerRadius | [DialogOptionsCornerRadius](#dialogoptionscornerradius18) | No | Yes | 

Background corner radius of the dialog box.

You can set separate radii for the four corners.

Default value: **{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }**

The radius of the rounded corners is subject to the component size. Its maximum value is half of the component width or height. If the value is negative, the default value is used.

When set to a percentage, the value defines the radius as a percentage of the parent dialog box's width or height.

 |
| borderWidth | [DialogOptionsBorderWidth](#dialogoptionsborderwidth18) | No | Yes | 

Border width of the dialog box.

You can set the width for all four sides or set separate widths for individual sides.

Default value: **0**.

Unit: vp.

When set to a percentage, the value defines the border width as a percentage of the parent dialog box's width.

If the left and right borders are greater than its width, or the top and bottom borders are greater than its height, the dialog box may not display as expected.

 |
| borderColor | [DialogOptionsBorderColor](#dialogoptionsbordercolor18) | No | Yes | 

Border color of the dialog box.

Default value: **Color.Black**.

**borderColor** must be used with **borderWidth** in pairs.

 |
| borderStyle | [DialogOptionsBorderStyle](#dialogoptionsborderstyle18) | No | Yes | 

Border style of the dialog box.

Default value: **BorderStyle.Solid**.

**borderStyle** must be used with **borderWidth** in pairs.

 |
| width | [Dimension](../../../arkts-components/common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Width of the dialog box.

**NOTE**

\- Default maximum value: 400vp

\- Percentage-based configuration: The reference width of the dialog box is adjusted based on the width of the window where the dialog box is located.

 |
| height | [Dimension](../../../arkts-components/common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Height of the dialog box.

**NOTE**

\- Default maximum value: 0.9 x (Window height – Safe area)

\- When this parameter is set to a percentage, the reference height of the dialog box is the height of the window where the dialog box is located minus the safe area. You can decrease or increase the height as needed.

 |
| shadow | [DialogOptionsShadow](#dialogoptionsshadow18) | No | Yes | 

Shadow of the dialog box.

Default value on 2-in-1 devices: **ShadowStyle.OUTER\_FLOATING\_MD** when the dialog box is focused and **ShadowStyle.OUTER\_FLOATING\_SM** otherwise On other devices, the dialog box has no shadow by default.

 |
| backgroundBlurStyle | [BlurStyle](../../../arkts-components/universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | Yes | 

Background blur style of the dialog box.

Default value: **BlurStyle.COMPONENT\_ULTRA\_THICK**

**NOTE**

Setting this parameter to **BlurStyle.NONE** disables the background blur. When **backgroundBlurStyle** is set to a value other than **NONE**, do not set **backgroundColor**. If you do, the color display may not produce the expected visual effect.

 |

#### DialogOptionsCornerRadius18+

type DialogOptionsCornerRadius = Dimension | BorderRadiuses

Defines the allowed data types for specifying the background corner radius of a dialog box.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Dimension](../../../arkts-components/common-definitions/basic-types/document.md#dimension10) | Length type used to represent a size unit. |
| [BorderRadiuses](../../../arkts-components/common-definitions/basic-types/document.md#borderradiuses9) | Type used to describe the corner radius of a component's border. |

#### DialogOptionsBorderWidth18+

type DialogOptionsBorderWidth = Dimension | EdgeWidths

Defines the allowed data types for specifying the background border width of a dialog box.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Dimension](../../../arkts-components/common-definitions/basic-types/document.md#dimension10) | Length type used to represent a size unit. |
| [EdgeWidths](../../../arkts-components/common-definitions/basic-types/document.md#edgewidths9) | Type used to describe the edge width of a component in different directions. |

#### DialogOptionsBorderColor18+

type DialogOptionsBorderColor = ResourceColor | EdgeColors

Defines the allowed data types for specifying the background border color of a dialog box.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | Color type used to describe resource colors. |
| [EdgeColors](../../../arkts-components/common-definitions/basic-types/document.md#edgecolors9) | Type used to describe the border color for each edge of a component. |

#### DialogOptionsBorderStyle18+

type DialogOptionsBorderStyle = BorderStyle | EdgeStyles

Defines the allowed data types for specifying the background border style of a dialog box.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [BorderStyle](../../../arkts-components/common-definitions/enums/document.md#borderstyle) | Type used to describe the border style of a component. |
| [EdgeStyles](../../../arkts-components/common-definitions/basic-types/document.md#edgestyles9) | Type used to describe the border style for each edge of a component. |

#### DialogOptionsShadow18+

type DialogOptionsShadow = ShadowOptions | ShadowStyle

Defines the allowed data types for specifying the background shadow of a dialog box.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [ShadowOptions](../../../arkts-components/universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | Type used to describe shadow attributes, including the blur radius, color, and offset along the x-axis and y-axis. |
| [ShadowStyle](../../../arkts-components/universal-attributes/visual-effects/image-effect/document.md#shadowstyle10) | Type used to describe the shadow style. |

#### CustomDialogOptions11+

Extends [BaseDialogOptions](#basedialogoptions11) to provide enhanced customization capabilities for the dialog box.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| builder | [CustomBuilder](../../../arkts-components/common-definitions/basic-types/document.md#custombuilder8) | No | No | 
Custom content of the dialog box.

**NOTE**

The builder needs to be assigned an arrow function in the following format: () => { this.XXX() }, where XXX indicates the internal builder name.

Global builders must be created inside the component and called within the internal builder.

The width and height percentages of the builder's root node are relative to the size of the dialog box container.

The width and height percentages of non-root nodes are relative to the size of their parent node.

 |
| backgroundColor 12+ | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Background color of the dialog box.

Default value: **Color.Transparent**.

**NOTE**

When **backgroundColor** is set to a non-transparent color, **backgroundBlurStyle** must be set to **BlurStyle.NONE**; otherwise, the color display may not meet the expected effect.

 |
| cornerRadius12+ | [Dimension](../../../arkts-components/common-definitions/basic-types/document.md#dimension10) | [BorderRadiuses](../../../arkts-components/common-definitions/basic-types/document.md#borderradiuses9) | No | Yes | 

Corner radius of the background.

You can set separate radii for the four corners.

Default value: **{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }**

The radius of the rounded corners is subject to the component size. Its maximum value is half of the component width or height. If the value is negative, the default value is used.

When set to a percentage, the value defines the radius as a percentage of the parent dialog box's width or height.

 |
| borderWidth12+ | [Dimension](../../../arkts-components/common-definitions/basic-types/document.md#dimension10) | [EdgeWidths](../../../arkts-components/common-definitions/basic-types/document.md#edgewidths9) | No | Yes | 

Border width of the dialog box.

You can set the width for all four sides or set separate widths for individual sides.

Default value: **0**.

Unit: vp.

When set to a percentage, the value defines the border width as a percentage of the parent dialog box's width.

If the left and right borders are greater than its width, or the top and bottom borders are greater than its height, the dialog box may not display as expected.

 |
| borderColor12+ | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | [EdgeColors](../../../arkts-components/common-definitions/basic-types/document.md#edgecolors9) | No | Yes | 

Border color of the dialog box.

Default value: **Color.Black**.

**borderColor** must be used with **borderWidth** in pairs.

 |
| borderStyle12+ | [BorderStyle](../../../arkts-components/common-definitions/enums/document.md#borderstyle) | [EdgeStyles](../../../arkts-components/common-definitions/basic-types/document.md#edgestyles9) | No | Yes | 

Border style of the dialog box.

Default value: **BorderStyle.Solid**.

**borderStyle** must be used with **borderWidth** in pairs.

 |
| width12+ | [Dimension](../../../arkts-components/common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Width of the dialog box.

**NOTE**

\- Default maximum width of the dialog box: 400 vp

\- Percentage-based configuration: The reference width of the dialog box is adjusted based on the width of the window where the dialog box is located.

 |
| height12+ | [Dimension](../../../arkts-components/common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Height of the dialog box.

**NOTE**

\- Default maximum height of the dialog box: 0.9 x (Window height – Safe area)

\- When this parameter is set to a percentage, the reference height of the dialog box is the height of the window where the dialog box is located minus the safe area. You can decrease or increase the height as needed.

 |
| shadow12+ | [ShadowOptions](../../../arkts-components/universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../../arkts-components/universal-attributes/visual-effects/image-effect/document.md#shadowstyle10) | No | Yes | 

Shadow of the dialog box.

Default value on 2-in-1 devices: **ShadowStyle.OUTER\_FLOATING\_MD** when the dialog box is focused and **ShadowStyle.OUTER\_FLOATING\_SM** otherwise On other devices, the dialog box has no shadow by default.

 |
| backgroundBlurStyle12+ | [BlurStyle](../../../arkts-components/universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | Yes | 

Background blur style of the dialog box.

Default value: **BlurStyle.COMPONENT\_ULTRA\_THICK**

**NOTE**

Setting this parameter to **BlurStyle.NONE** disables the background blur. When **backgroundBlurStyle** is set to a value other than **NONE**, do not set **backgroundColor**. If you do, the color display may not produce the expected visual effect.

 |

#### BaseDialogOptions11+

Defines the options of the dialog box.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| maskRect | [Rectangle](../../../arkts-components/dialog-boxes/alert-dialog-box-alertdialog/document.md#rectangle8) | No | Yes | 
Mask area.

Default value: **{ x: 0, y: 0, width: '100%', height: '100%' }**

**NOTE**

**maskRect** does not take effect when **showInSubWindow** is set to **true**.

If only some properties in [Rectangle](../../../arkts-components/dialog-boxes/alert-dialog-box-alertdialog/document.md#rectangle8) are set, the unset properties default to 0.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| alignment | [DialogAlignment](../../../arkts-components/dialog-boxes/alert-dialog-box-alertdialog/document.md#dialogalignment) | No | Yes | 

Alignment mode of the dialog box in the vertical direction.

Default value: **DialogAlignment.Default**

**NOTE**

If **showInSubWindow** is set to **true** in **UIExtension**, the dialog box is aligned with the host window based on **UIExtension**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| offset | [Offset](../../../arkts-components/common-definitions/basic-types/document.md#offset) | No | Yes | 

Offset of the dialog box based on the **alignment** settings.

Default value: **{ dx: 0 , dy: 0 }**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| isModal | boolean | No | Yes | 

Whether the dialog box is a modal, which has a mask applied and does not allow for interaction with other components around the dialog box.

**true**: The dialog box is a modal.

**false**: The dialog box is not a modal.

Default value: **true**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| showInSubWindow | boolean | No | Yes | 

Whether to show the dialog box in a subwindow when the dialog box needs to be displayed outside the main window.

**true**: The dialog box is shown in a subwindow.

Default value: **false**, meaning the dialog box is displayed within the application, not in a separate subwindow

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onWillDismiss12+ | Callback<[DismissDialogAction](#dismissdialogaction12)\> | No | Yes | 

Callback for interactive dismissal of the dialog box.

**NOTE**

1\. If this callback is registered, the dialog box will not be dismissed immediately after the user touches the mask or the Back button, presses the Esc key, or swipes left or right on the screen. The **reason** parameter in the callback is used to determine whether the dialog box can be dismissed. The reason returned by the component does not support the value **CLOSE\_BUTTON**.

2\. In the **onWillDismiss** callback, another **onWillDismiss** callback is not allowed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| autoCancel12+ | boolean | No | Yes | 

Whether to dismiss the dialog box when the mask is touched. The value **true** means to dismiss the dialog box when the mask is touched, and **false** means the opposite.

Default value: **true**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| maskColor12+ | [ResourceColor](../../../arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Mask color.

Default value: **0x33000000**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| transition12+ | [TransitionEffect](../../../arkts-components/animation/component-transition-transition/document.md#transitioneffect10) | No | Yes | 

Transition effect for the appearance and disappearance of the dialog box.

**NOTE**

1\. If this parameter is not set, the default effect is used.

2\. Touching the Back button during the appearance animation pauses the appearance animation and starts the disappearance animation. The final effect is one obtained after the curves of the appearance and disappearance animations are combined.

3\. Touching the Back button during the exit animation does not affect the animation playback. Touching the Back button again closes the application.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| dialogTransition19+ | [TransitionEffect](../../../arkts-components/animation/component-transition-transition/document.md#transitioneffect10) | No | Yes | 

Transition effect for the dialog box content. By default, there is no transition effect.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| maskTransition19+ | [TransitionEffect](../../../arkts-components/animation/component-transition-transition/document.md#transitioneffect10) | No | Yes | 

Transition effect for the mask. By default, there is no transition effect.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| onDidAppear12+ | () => void | No | Yes | 

Event callback after the dialog box appears.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange) > onWillDisappear > onDidDisappear.

2\. You can set the callback event for changing the dialog box display effect in **onDidAppear**. The settings take effect next time the dialog box appears.

3\. If the user dismisses the dialog box immediately after it appears, **onWillDisappear** is invoked before **onDidAppear**.

4\. If the dialog box is dismissed before its appearance animation is finished, this callback is not invoked.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onDidDisappear12+ | () => void | No | Yes | 

Event callback after the dialog box disappears.

**NOTE**

The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange) > onWillDisappear > onDidDisappear.

This callback is not triggered if the dialog box disappearance animation is interrupted (for example, by page navigation).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onWillAppear12+ | () => void | No | Yes | 

Event callback when the dialog box is about to appear.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange) > onWillDisappear > onDidDisappear.

2\. You can set the callback event for changing the dialog box display effect in **onWillAppear**. The settings take effect next time the dialog box appears.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onWillDisappear12+ | () => void | No | Yes | 

Event callback when the dialog box is about to disappear.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange) > onWillDisappear > onDidDisappear.

2\. If the user dismisses the dialog box immediately after it appears, **onWillDisappear** is invoked before **onDidAppear**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| keyboardAvoidMode12+ | [KeyboardAvoidMode](../../../arkts-components/universal-attributes/dialog-box-control/popup-control/document.md#keyboardavoidmode12) | No | Yes | 

How the dialog box avoids the soft keyboard when it is brought up.

Default value: **KeyboardAvoidMode.DEFAULT**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| enableHoverMode14+ | boolean | No | Yes | 

Whether to respond when the device is in semi-folded mode. The value **true** means to respond when the device is in semi-folded mode.

Default value: **false**, meaning not to respond when the device is in semi-folded mode.

**NOTE**

For a PC or 2-in-1 device, the prompt is displayed on the upper half of the screen by default when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display the prompt on the lower half of the screen. For other devices, the prompt is displayed on the lower half of the screen by default when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display the prompt on the upper half of the screen.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| hoverModeArea14+ | [HoverModeAreaType](../../../arkts-components/universal-attributes/transition/sheet-transition/document.md#hovermodeareatype14) | No | Yes | 

Display area of the dialog box in the hover state.

Default value: **HoverModeAreaType.BOTTOM\_SCREEN**

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](../../../arkts-components/universal-attributes/basic-attributes/background/document.md#backgroundblurstyleoptions10) | No | Yes | 

Options for customizing the background blur style. For details about the default value, see **BackgroundBlurStyleOptions**.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| backgroundEffect19+ | [BackgroundEffectOptions](../../../arkts-components/universal-attributes/basic-attributes/background/document.md#backgroundeffectoptions11) | No | Yes | 

Options for customizing the background effect. For details about the default value, see **BackgroundEffectOptions**.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| keyboardAvoidDistance15+ | [LengthMetrics](../arkui/graphics/document.md#lengthmetrics12) | No | Yes | 

Distance between the dialog box and the keyboard after keyboard avoidance is applied.

**NOTE**

\- Default value: **16vp**

\- Default unit: vp

\- This parameter takes effect only when **keyboardAvoidMode** is set to **DEFAULT**.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| levelMode15+ | [LevelMode](#levelmode15) | No | Yes | 

Display level of the dialog box.

**NOTE**

\- Default value: **LevelMode.OVERLAY**

\- This parameter takes effect only when **showInSubWindow** is set to **false**.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| levelUniqueId15+ | number | No | Yes | 

[Unique ID](../arkui/framenode/document.md#getuniqueid12) of the node under the display level for the page-level dialog box.

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
| levelOrder18+ | [LevelOrder](#levelorder18) | No | Yes | 

Display order of the dialog box.

**NOTE**

\- Default value: **LevelOrder.clamp(0)**

\- Dynamic updating is not supported.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| focusable19+ | boolean | No | Yes | 

Whether the dialog box can gain focus.

**true**: The dialog box can gain focus.

**false**: The dialog box cannot gain focus.

Default value: **true**.

**NOTE**

Only dialog boxes that are displayed on top of the current window can gain focus.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |

#### DismissDialogAction12+

Provides information about the action to dismiss the dialog box.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

## Attributes

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| dismiss | Callback<void> | No | No | Callback for dismissing the dialog box. This API is called only when the dialog box needs to be exited. |
| reason | [DismissReason](../../../arkts-components/universal-attributes/dialog-box-control/popup-control/document.md#dismissreason12) | No | No | Reason why the dialog box cannot be dismissed. You must specify whether to close the dialog box for each of the listed actions. |

#### LevelMode15+

Enumerates the display level modes of the dialog box.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| OVERLAY | 0 | The dialog box is displayed at the root node level of the application window and remains visible during navigation. |
| EMBEDDED | 1 | 
The dialog box is a child of the page's route/navigation and is hidden when the page is hidden.

**NOTE**

1\. Currently, the dialog box can only be mounted to a **Page** or [NavDestination](../../../arkts-components/navigation-and-switching/navdestination/document.md) node, with **Page** nodes taking precedence. The dialog box is displayed only on top of these two page types.

2\. In this mode, new pages can be displayed over the dialog box. When users return to the previous page, the dialog box remains visible and its content is preserved.

3\. In this mode, you must ensure that the target page node, such as the **Page** node, has been attached to the tree before bringing up the dialog box; otherwise, the dialog box will not be able to be attached to the corresponding page node.

 |

#### ImmersiveMode15+

Enumerates the display area modes of the dialog box overlay within a page.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | The dialog box overlay follows the layout constraints of its parent node. |
| EXTEND | 1 | The dialog box overlay can extend to cover the status bar and navigation bar for a more immersive look. |

#### Button

Describes the menu item button in the action menu.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| text | string | [Resource](../../../arkts-components/common-definitions/basic-types/document.md#resource) | No | No | 
Button text.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| color | string | [Resource](../../../arkts-components/common-definitions/basic-types/document.md#resource) | No | No | 

Text color of the button.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| primary12+ | boolean | No | Yes | 

Whether the button responds to the **Enter** key by default when the dialog box has focus and the **Tab** key is not pressed for sequential focus navigation. If there are multiple buttons, set this parameter to **true** for only one button. Otherwise, no button will respond. Multiple dialog boxes can automatically gain focus and respond to user interactions in a sequential manner. **true**: The button responds to the **Enter** key by default. **false**: The button does not respond to the **Enter** key by default.

Default value: **false**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### Example

This example demonstrates how to call the **getState** API of **promptAction.DialogController** to obtain the current state of a dialog box, supported since API version 20.

// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { ComponentContent, promptAction } from '@kit.ArkUI';

@Component
struct CustomDialogExample {
  build() {
    Column() {
      Text('Hello')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .margin({ bottom: 36 })
      Button('Close Dialog Box')
        .onClick(() => {
          if (this.getDialogController()) {
            this.getDialogController().close();
          }
        })
      Button('Obtain State')
        .onClick(() => {
          if (this.getDialogController()) {
            let state: promptAction.CommonState = this.getDialogController().getState();
            switch (state) {
              case promptAction.CommonState.UNINITIALIZED: {
                console.info('The dialog state is uninitialized.');
                break;
              }
              case promptAction.CommonState.INITIALIZED: {
                console.info('The dialog state is initialized.');
                break;
              }
              case promptAction.CommonState.APPEARING: {
                console.info('The dialog state is appearing.');
                break;
              }
              case promptAction.CommonState.APPEARED: {
                console.info('The dialog state is appeared.');
                break;
              }
              case promptAction.CommonState.DISAPPEARING: {
                console.info('The dialog state is disappearing.');
                break;
              }
              case promptAction.CommonState.DISAPPEARED: {
                console.info('The dialog state is disappeared.');
                break;
              }
              default: {
                console.info('The dialog state is unknown.');
                break;
              }
            }
          }
        })

    }.backgroundColor('#FFF0F0F0')
  }
}

@Builder
function buildText() {
   CustomDialogExample()
}

@Entry
@Component
struct Index {

  private dialogController: promptAction.DialogController = new promptAction.DialogController()

  build() {
    Row() {
      Column() {
        Button("click me")
          .onClick(() => {
            let uiContext = this.getUIContext();
            let promptAction = uiContext.getPromptAction();
            let contentNode = new ComponentContent(uiContext, wrapBuilder(buildText),
            );

            promptAction.openCustomDialogWithController(contentNode, this.dialogController, {

              transition: TransitionEffect.OPACITY.animation({
                duration: 3000
              })
            }).then(() => {
              console.info('succeeded')
            }).catch((error: BusinessError) => {
              console.error(\`OpenCustomDialogWithController args error code is ${error.code}, message is ${error.message}\`);
            })
          })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}

#### promptAction.showToast(deprecated)

showToast(options: ShowToastOptions): void

Creates and displays a toast.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/_OPLshQwRgSoQAknmPR6Kw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA1B5763FF559BD037B0235B7210E7115071A05568BF74A76554EB5985FB24F4)

-   This API is supported since API version 9 and deprecated since API version 18. You are advised to use [showToast](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md#showtoast) instead. Before calling this API, you need to obtain the [PromptAction](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md) object using the [getPromptAction](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getpromptaction) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md). Directly using **showToast** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context).
    
-   Since API version 10, you can use the [getPromptAction](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getpromptaction) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [PromptAction](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md) object associated with the current UI context.
    
-   The toast has a fixed style and does not support content customization. For specific supported capabilities, see [ShowToastOptions](#showtoastoptions).
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ShowToastOptions](#showtoastoptions) | Yes | Toast configuration options. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/hLnJX-v1QBq_Cx5M3Zttyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6EB6F2D6B3AEB6CE331C5A5879A1B0D3A266DD25B2E40CAA703493068CC6F794)

If error code 100001 is returned, indicating an ambiguous UI context, use the corresponding APIs from **UIContext** instead. For details, see [Using the UI Context API for UI Operations (UIContext)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**Example**

import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct toastExample {
  build() {
    Column() {
      Button('Show toast').fontSize(20)
        .onClick(() => {
          try {
            promptAction.showToast({
              message: 'Hello World',
              duration: 2000
            });
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(\`showToast args error code is ${code}, message is ${message}\`);
          };
        })
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}

Below is a toast in API version 11 and earlier versions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/waOHl89xRsKkPXH8Mf6dTQ/en-us_image_0000002568685053.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47042A56D753A793B3006BB4BACAB0ABBD05877F57C56E33153BD9C7B60FA3C6)

Below is a toast in API version 12 and later versions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/kvR4AbuhTlu_oVu8hHHKkA/en-us_image_0000002568765063.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E285A39E69505AF3AB6A02D5CF73E4CD2F79005539AC34AD1422F4B5F5FC979)

#### promptAction.showDialog(deprecated)

showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>

Creates and displays a dialog box in the given settings. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/NE1bq8qKR_6gMmMkgP-xtA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E698CD40CF1389471E0433ACCA0CC142F9AAAE28B1801EAF55F7F0F2BC9B5F4)

-   This API is supported since API version 9 and deprecated since API version 18. You are advised to use [showDialog](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md#showdialog-1) instead. Before calling this API, you need to obtain the [PromptAction](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md) object using the [getPromptAction](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getpromptaction) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md). Directly using **showDialog** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context).
    
-   Since API version 10, you can use the [getPromptAction](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getpromptaction) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [PromptAction](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ShowDialogOptions](#showdialogoptions) | Yes | Dialog box configuration options. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ShowDialogSuccessResponse](#showdialogsuccessresponse)\> | Promise that returns the dialog box response. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**Example**

import { promptAction } from '@kit.ArkUI';

promptAction.showDialog({
  title: 'Title Info',
  message: 'Message Info',
  buttons: \[
    {
      text: 'button1',
      color: '#000000'
    },
    {
      text: 'button2',
      color: '#000000'
    }
  \],
})
  .then(data => {
    console.info('showDialog success, click button: ' + data.index);
  })
  .catch((err: Error) => {
    console.info('showDialog error: ' + err);
  })

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/L43rZfFZR-eb24lmM6cvMQ/en-us_image_0000002537765338.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=306DFEB8F6D7BCFE100D4BE3FEA614F119D30F7D8C470D50639FB4E6896825BE)

#### promptAction.showDialog(deprecated)

showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>):void

Creates and displays a dialog box. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/f2pW8rYqRMu7hsdwgZNylA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6584CA32A9B65CDAE45C0072EA1D411869A641CDC9F51156E8F82BC962A50FAE)

-   This API is supported since API version 9 and deprecated since API version 18. You are advised to use [showDialog](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md#showdialog) instead. Before calling this API, you need to obtain the [PromptAction](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md) object using the [getPromptAction](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getpromptaction) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md). Directly using **showDialog** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context).
    
-   Since API version 10, you can use the [getPromptAction](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getpromptaction) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [PromptAction](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ShowDialogOptions](#showdialogoptions) | Yes | Dialog box configuration options. |
| callback | AsyncCallback<[ShowDialogSuccessResponse](#showdialogsuccessresponse)\> | Yes | Callback used to return the result. On success, **err** is **undefined** and **data** contains the dialog box response. On failure, **err** provides error details. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**Example**

import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  promptAction.showDialog({
    title: 'showDialog Title Info',
    message: 'Message Info',
    buttons: \[
      {
        text: 'button1',
        color: '#000000'
      },
      {
        text: 'button2',
        color: '#000000'
      }
    \]
  }, (err, data) => {
    if (err) {
      console.info('showDialog err: ' + err);
      return;
    }
    console.info('showDialog success callback, click button: ' + data.index);
  });
} catch (error) {
  let message = (error as BusinessError).message;
  let code = (error as BusinessError).code;
  console.error(\`showDialog args error code is ${code}, message is ${message}\`);
};

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/pN5iL-reRBOchYUIkqLVpA/en-us_image_0000002537925278.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0BB561D3B32D98BBAA778FEE5A9B9865CC2115FF94A57F0ECCF99EC06B3E06EB)

When the **showInSubWindow** attribute is set to **true**, the toast can be displayed outside the window.

import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  promptAction.showDialog({
    title: 'showDialog Title Info',
    message: 'Message Info',
    isModal: true,
    showInSubWindow: true,
    buttons: \[
      {
        text: 'button1',
        color: '#000000'
      },
      {
        text: 'button2',
        color: '#000000'
      }
    \]
  }, (err, data) => {
    if (err) {
      console.info('showDialog err: ' + err);
      return;
    }
    console.info('showDialog success callback, click button: ' + data.index);
  });
} catch (error) {
  let message = (error as BusinessError).message;
  let code = (error as BusinessError).code;
  console.error(\`showDialog args error code is ${code}, message is ${message}\`);
};

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/ZMz205YVQxaxoXhJGrXVbg/en-us_image_0000002568685055.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1F03AF7A4CF5DB85B6DF3FBFC715C7A2CC83010ED1EE62EC023094F69B4D0D3)

This example demonstrates how to use the **onDidAppear**, **onDidDisappear**, **onWillAppear**, and **onWillDisappear** properties of [ShowDialogOptions](#showdialogoptions) to implement the dialog box lifecycle callbacks, supported since API version 19.

// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct DialogExample {
  @State log: string = 'Log information:';
  build() {
    Column() {
      Button('showDialog')
        .onClick(() => {
          this.showCustomDialog();
        })
      Text(this.log).fontSize(30).margin({ top: 200 })
    }.width('100%').margin({ top: 5 })
  }

  showCustomDialog() {
    try {
      this.getUIContext().getPromptAction().showDialog({
        title: 'Confirm',
        message: 'Are you sure you want to continue?',
        alignment: DialogAlignment.Bottom,
        buttons: \[
          {
            text: 'Cancel',
            color: '#999999'
          },
          {
            text: 'OK',
            color: '#007DFF'
          }
        \],
        onDidAppear: () => {
          this.log += '# onDidAppear';
          console.info("showDialog,is onDidAppear!");
        },
        onDidDisappear: () => {
          this.log += '# onDidDisappear';
          console.info("showDialog,is onDidDisappear!");
        },
        onWillAppear: () => {
          this.log = 'Log information:#onWillAppear';
          console.info("showDialog,is onWillAppear!");
        },
        onWillDisappear: () => {
          this.log += '# onWillDisappear';
          console.info("showDialog,is onWillDisappear!");
        },
      })
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(\`Exception caught: ${err.code}, ${err.message}\`);
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/te7wE1U6TRW01VaGfz3QPw/en-us_image_0000002568765065.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B566539448218A674FD3CEDCAF52EF95F64D609B5A02DBB93AEEFD6F5A4A97FD)

#### promptAction.showActionMenu(deprecated)

showActionMenu(options: ActionMenuOptions, callback: AsyncCallback<ActionMenuSuccessResponse>):void

Creates and displays an action menu. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/ohdT-0SuQaO5YJJP7avwgw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68F6CAAFE8CD2081BABE6B16C5BFD9129399A4E2A50BC90C96AB4D91B2352D00)

-   This API is supported since API version 9 and deprecated since API version 18. You are advised to use [showActionMenu](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md#showactionmenu11) instead. Before calling this API, you need to obtain the [PromptAction](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md) object using the [getPromptAction](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getpromptaction) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md). Directly using **showActionMenu** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context).
    
-   Since API version 11, you can use the [getPromptAction](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getpromptaction) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [PromptAction](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ActionMenuOptions](#actionmenuoptions) | Yes | Action menu options. |
| callback | AsyncCallback<[ActionMenuSuccessResponse](#actionmenusuccessresponse)\> | Yes | Callback used to return the result. On success, **err** is **undefined** and **data** contains the action menu response. On failure, **err** provides error details. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**Example 1**

import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  promptAction.showActionMenu({
    title: 'Title Info',
    buttons: \[
      {
        text: 'item1',
        color: '#666666'
      },
      {
        text: 'item2',
        color: '#000000'
      },
    \]
  }, (err, data) => {
    if (err) {
      console.info('showActionMenu err: ' + err);
      return;
    }
    console.info('showActionMenu success callback, click button: ' + data.index);
  })
} catch (error) {
  let message = (error as BusinessError).message
  let code = (error as BusinessError).code
  console.error(\`showActionMenu args error code is ${code}, message is ${message}\`);
};

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/gUQsnEDRRRir-3mPSOsNZA/en-us_image_0000002537765340.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=54085B5DCC80E467723E4CCF9205C30CF1EC437C430833D1B6254434E169DD99)

**Example 2**

This example demonstrates how to use the **onDidAppear**, **onDidDisappear**, **onWillAppear**, and **onWillDisappear** properties of [ActionMenuOptions](#actionmenuoptions) to implement the action menu lifecycle callbacks, supported since API version 19.

import { promptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State isShown: boolean = false
  @State textColor: Color = Color.Black
  @State blueColor: Color = Color.Blue

  @State onWillAppear: boolean = false
  @State onDidAppear: boolean = false
  @State onWillDisappear: boolean = false
  @State onDidDisappear: boolean = false
  build() {
    Column({ space: 50 }) {
      Text('onWillAppear').fontColor(this.onWillAppear ? this.blueColor : this.textColor)
      Text('onDidAppear').fontColor(this.onDidAppear ? this.blueColor : this.textColor)
      Text('onWillDisappear').fontColor(this.onWillDisappear ? this.blueColor : this.textColor)
      Text('onDidDisappear').fontColor(this.onDidDisappear ? this.blueColor : this.textColor)
      Button('click')
        .width(200)
        .height(100)
        .margin(100)
        .fontColor(this.textColor)
        .onClick(() => {
          promptAction.showActionMenu({
            title: 'showActionMenu Title Info',
            buttons: \[
              {
                text: 'item1',
                color: '#666666'
              },
              {
                text: 'item2',
                color: '#000000'
              },
            \],
            onWillAppear:() => {
              console.info("promptAction menu cycle life onWillAppear");
              this.onWillAppear = true;
            },
            onDidAppear:() => {
              console.info("promptAction menu cycle life onDidAppear");
              this.onDidAppear = true;
            },
            onWillDisappear:() => {
              this.isShown = false;
              console.info("promptAction menu cycle life onWillDisappear");
              this.onWillDisappear = true;
            },
            onDidDisappear:() => {
              console.info("promptAction menu cycle life onDidDisappear");
              this.onDidDisappear = true;
            }
          })
            .then(data => {
              console.info('showActionMenu success, click button: ' + data.index);
            })
            .catch((err: Error) => {
              console.info('showActionMenu error: ' + err);
            })
        })
    }
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/e2xlNWG4SymIyCCX4fvYRA/en-us_image_0000002537925280.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59BAEB978250B588DA1BC93459765BC423A9ABF421A9D3BB782D9DDC1E231C73)

#### promptAction.showActionMenu(deprecated)

showActionMenu(options: ActionMenuOptions): Promise<ActionMenuSuccessResponse>

Creates and displays an action menu in the given settings. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/RPwT-GcGQpqoqWY-EVPZvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FAAC022654F93A6604F4D7E2B2839FA72BEAFD1CE547926EABFE64CA7159457)

-   This API is supported since API version 9 and deprecated since API version 18. You are advised to use [showActionMenu](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md#showactionmenu) instead. Before calling this API, you need to obtain the [PromptAction](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md) object using the [getPromptAction](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getpromptaction) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md). Directly using **showActionMenu** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context).
    
-   Since API version 10, you can use the [getPromptAction](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getpromptaction) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [PromptAction](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ActionMenuOptions](#actionmenuoptions) | Yes | Promise that returns the action menu response. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ActionMenuSuccessResponse](#actionmenusuccessresponse)\> | Promise that returns the action menu response. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**Example**

import { promptAction } from '@kit.ArkUI';

promptAction.showActionMenu({
  title: 'showActionMenu Title Info',
  buttons: \[
    {
      text: 'item1',
      color: '#666666'
    },
    {
      text: 'item2',
      color: '#000000'
    },
  \]
})
  .then(data => {
    console.info('showActionMenu success, click button: ' + data.index);
  })
  .catch((err: Error) => {
    console.info('showActionMenu error: ' + err);
  })

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/PcBHzKJhRN6Mzt8aWsFGow/en-us_image_0000002568685057.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D825A2D8CBC55F6DD82548100185B460E8767581412F0DBD81C489A3D177CA46)

#### promptAction.openCustomDialog(deprecated)

openCustomDialog(options: CustomDialogOptions): Promise<number>

Opens a custom dialog box. This API uses a promise to return the result.

By default, the width of the dialog box in portrait mode is the width of the window where it is located minus the left and right margins (40 vp for 2-in-1 devices and 16 vp for other devices), and the maximum width is 400 vp.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/KNJL9_fER2utC1pLqpEPfA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=143BB8E61B171FDA3F7E6D4A386F893BA46246499B497CD6BC1797FE7985E6AA)

-   This API is supported since API version 11 and deprecated since API version 18. You are advised to use [openCustomDialog](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md#opencustomdialog12-1) instead. Before calling this API, you need to obtain the [PromptAction](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md) object using the [getPromptAction](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getpromptaction) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md). Directly using **openCustomDialog** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context).
    
-   Since API version 12, you can use the [getPromptAction](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getpromptaction) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [PromptAction](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [CustomDialogOptions](#customdialogoptions11) | Yes | 
Content of the custom dialog box.

Note: If both [isModal](#basedialogoptions11) and [showInSubWindow](#basedialogoptions11) in **BaseDialogOptions** are set to **true**, only **showInSubWindow** takes effect. In this case, the non-modal dialog box is displayed without mask in the subwindow.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | ID of the custom dialog box, which can be used in **closeCustomDialog**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**Example**

import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private customDialogComponentId: number = 0;

  @Builder
  customDialogComponent() {
    Column() {
      Text('Dialog box').fontSize(30)
      Row({ space: 50 }) {
        Button("OK").onClick(() => {
          try {
            promptAction.closeCustomDialog(this.customDialogComponentId)
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(\`closeCustomDialog error code is ${code}, message is ${message}\`);
          }
        })
        Button("Cancel").onClick(() => {
          try {
            promptAction.closeCustomDialog(this.customDialogComponentId)
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(\`closeCustomDialog error code is ${code}, message is ${message}\`);
          }
        })
      }
    }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween)
  }

  build() {
    Row() {
      Column({ space: 20 }) {
        Text('In-component dialog box')
          .fontSize(30)
          .onClick(() => {
            promptAction.openCustomDialog({
              builder: () => {
                this.customDialogComponent()
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info('reason' + JSON.stringify(dismissDialogAction.reason));
                console.info('dialog onWillDismiss');
                if (dismissDialogAction.reason == DismissReason.PRESS\_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason == DismissReason.TOUCH\_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            }).then((dialogId: number) => {
              this.customDialogComponentId = dialogId;
            })
              .catch((error: BusinessError) => {
                console.error(\`openCustomDialog error code is ${error.code}, message is ${error.message}\`);
              })
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

This example demonstrates how to set styles of a dialog box, including the width, height, background color, and shadow.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/w7edoikOSfum27Yk5M1O8Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=535286B90D625404420857DF4EBB8529582ADE3C4D2BB8C35937EFDA21C3A674)

Directly using **openCustomDialog** can lead to the issue of ambiguous UI context. To avoid this, obtain the [PromptAction](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md) object using the [getPromptAction](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getpromptaction) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) and then call the [openCustomDialog](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md#opencustomdialog12-1) API through this object.

import { LevelMode, ImmersiveMode } from '@kit.ArkUI';

let customDialogId: number = 0;

@Builder
function customDialogBuilder(uiContext: UIContext) {
  Column() {
    Text('Custom dialog Message').fontSize(10)
    Row() {
      Button("OK").onClick(() => {
        uiContext.getPromptAction().closeCustomDialog(customDialogId);
      })
      Blank().width(50)
      Button("Cancel").onClick(() => {
        uiContext.getPromptAction().closeCustomDialog(customDialogId);
      })
    }
  }
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  private uiContext: UIContext = this.getUIContext();

  @Builder
  customDialogComponent() {
    customDialogBuilder(this.uiContext)
  }

  build() {
    Row() {
      Column() {
        Text(this.message).id("test\_text")
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            const node: FrameNode | null = this.uiContext.getFrameNodeById("test\_text") || null;
            this.uiContext.getPromptAction().openCustomDialog({
              builder: () => {
                this.customDialogComponent()
              },
              keyboardAvoidMode: KeyboardAvoidMode.NONE,
              showInSubWindow: false,
              offset: { dx: 5, dy: 5 },
              backgroundColor: 0xd9ffffff,
              cornerRadius: 20,
              width: '80%',
              height: 200,
              borderWidth: 1,
              borderStyle: BorderStyle.Dashed, // borderStyle must be used with borderWidth in pairs.
              borderColor: Color.Blue, // borderColor must be used with borderWidth in pairs.
              shadow: ({
                radius: 20,
                color: Color.Grey,
                offsetX: 50,
                offsetY: 0
              }),
              levelMode: LevelMode.EMBEDDED,
              levelUniqueId: node?.getUniqueId(),
              immersiveMode: ImmersiveMode.DEFAULT,
            }).then((dialogId: number) => {
              customDialogId = dialogId;
            })
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/vecIf0DoT9m88wRqi3ZS5A/en-us_image_0000002568765067.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9880820FA8EB134DAB56266D5E90072390319DF62F8959E78D7EF391ECCC3ECA)

This example shows how to implement a dialog box on a page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/4m_l7MqFQfGQ4TAHGIrJEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A6D5CC44BC6F64F533BA2E29CA8BFE668333527E55794EF9879421D17E1AEEAE)

Directly using **openCustomDialog** can lead to the issue of ambiguous UI context. To avoid this, obtain the [PromptAction](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md) object using the [getPromptAction](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getpromptaction) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) and then call the [openCustomDialog](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md#opencustomdialog12-1) API through this object.

// Index.ets
import { LevelMode, ImmersiveMode } from '@kit.ArkUI';

let customDialogId: number = 0;

@Builder
function customDialogBuilder(uiContext: UIContext) {
  Column() {
    Text('Custom dialog Message').fontSize(10).height(100)
    Row() {
      Button("Next").onClick(() => {
        uiContext.getRouter().pushUrl({ url: 'pages/Next' });
      })
      Blank().width(50)
      Button("Close").onClick(() => {
        uiContext.getPromptAction().closeCustomDialog(customDialogId);
      })
    }
  }.padding(20)
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  private uiContext: UIContext = this.getUIContext();

  @Builder
  customDialogComponent() {
    customDialogBuilder(this.uiContext)
  }

  build() {
    Row() {
      Column() {
        Text(this.message).id("test\_text")
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            const node: FrameNode | null = this.uiContext.getFrameNodeById("test\_text") || null;
            this.uiContext.getPromptAction().openCustomDialog({
              builder: () => {
                this.customDialogComponent()
              },
              levelMode: LevelMode.EMBEDDED,
              levelUniqueId: node?.getUniqueId(),
              immersiveMode: ImmersiveMode.DEFAULT,
            }).then((dialogId: number) => {
              customDialogId = dialogId;
            })
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

// Next.ets
@Entry
@Component
struct Next {
  @State message: string = 'Back';

  build() {
    Row() {
      Column() {
        Button(this.message)
          .onClick(() => {
            this.getUIContext().getRouter().back();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/rna4WLWyQKKI2T86nYNQ4Q/en-us_image_0000002537765342.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA379D6646F4B4AD41DA1772A85A3E93EB1ED8DF4BEEF6087D33715E7709729A)

#### promptAction.closeCustomDialog(deprecated)

closeCustomDialog(dialogId: number): void

Closes the specified custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/Hz2fwQpqTcmK49jikneqWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6FC4DC5F485F0047B2CEFF63B0E6787893E0C0DA625C86E4193AF6E8A9953B08)

-   This API is supported since API version 11 and deprecated since API version 18. You are advised to use [closeCustomDialog](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md#closecustomdialog12-1) instead. Before calling this API, you need to obtain the [PromptAction](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md) object using the [getPromptAction](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getpromptaction) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md). Directly using **closeCustomDialog** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context).
    
-   Since API version 12, you can use the [getPromptAction](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getpromptaction) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [PromptAction](../ohos-arkui-uicontext-uicontext/class-promptaction/document.md) object associated with the current UI context.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dialogId | number | Yes | ID of the custom dialog box to close. It is returned from **openCustomDialog**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**Example**

See the example of [promptAction.openCustomDialog](#promptactionopencustomdialogdeprecated).
