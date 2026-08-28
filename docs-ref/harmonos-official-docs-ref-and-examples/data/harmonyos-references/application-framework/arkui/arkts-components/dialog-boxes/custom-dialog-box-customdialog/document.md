# Custom Dialog Box (CustomDialog)

A custom dialog box is implemented using the **CustomDialogController** class APIs. When using a dialog box component, prioritize custom dialog boxes for easier style and content customization.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/SEeVayorR4q9UCKb0VWTSQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDBF6E7482EF02EE6F589013B25177EED1872758FCD39028BAA34D835762BC56)

The initial APIs of this module are supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### CustomDialogController

Defines the controller of the custom dialog box.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

## Objects to Import

dialogController : CustomDialogController | null = new CustomDialogController(CustomDialogControllerOptions)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/OCD8QILJQXiQHnSVyq0AIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BB4A9D937543B57C3F973FEDF915A241621478BDA2D7F03989E0265D7294986)

-   **CustomDialogController** is effective only when it is a member variable of the @CustomDialog and @Component decorated struct and is defined in the @Component decorated struct. For details, see the following example.
    
-   You can pass in multiple other controllers in the CustomDialog to open one or more other CustomDialogs in the CustomDialog. In this case, you must place the controller pointing to the self behind all controllers. For details, see [Example 1: Opening Nested Dialog Boxes](#example-1-opening-nested-dialog-boxes).
    

#### \[h2\]constructor

constructor(value: CustomDialogControllerOptions)

Constructor for a custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/azGvtho4TBKARFJFlDB_cQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B8AD0A5AFEBC45566683584223ECDA092E245CFA1C68A2783EBEC828409BE2D5)

Custom dialog box parameters do not support dynamic updates. However, by setting **customStyle** to **true** and configuring attributes such as [background color](../../universal-attributes/basic-attributes/background/document.md#backgroundcolor), [background blur](../../universal-attributes/basic-attributes/background/document.md#backgroundblurstyle9), and [width/height](../../universal-attributes/layout-and-borders/sizing/document.md) on the custom component, dynamic updates can be achieved through state variables bound to these attributes.

If **CustomDialogController** is used as a global variable to implement global custom dialog boxes, the previous dialog box cannot be closed after a new value is assigned to the controller. You are advised to close the dialog box before reassigning the value.

When a custom dialog box is started within another custom dialog box, you are advised not to close the latter custom dialog box directly.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CustomDialogControllerOptions](#customdialogcontrolleroptions) | Yes | Parameters of the custom dialog box. |

#### \[h2\]open

open()

Opens the content of the custom dialog box. This API can be called multiple times. If the dialog box is displayed in a subwindow, no new subwindow is allowed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/kGWaXv6yTxuzICmaDU3C2Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB4831EBB6132CB8356541961D85EB86714DD1B54656CDF156F25B85ABB483F6)

**CustomDialog** with subwindow display (**showInSubwindow** set to **true**) is not supported in input method windows. For details, see the constraints in [createPanel](../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#createpanel10-1) of the input method framework documentation.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]close

close()

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

Closes the custom dialog box. If the dialog box is closed, this API does not take effect.

#### \[h2\]getState20+

getState(): PromptActionCommonState

Obtains the state of the custom dialog box.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [PromptActionCommonState](#promptactioncommonstate20) | State of the custom dialog box. |

#### PromptActionCommonState20+

type PromptActionCommonState = promptAction.CommonState

Defines the state of the custom dialog box.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [promptAction.CommonState](../../../arkts-api/ui/ohos-promptaction-prompt/document.md#commonstate20) | State of the custom dialog box. |

#### CustomDialogControllerOptions

Defines the style of the custom dialog box.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| builder | [CustomDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-custom-dialog) | No | No | 
Builder of the custom dialog box content.

**NOTE**

If the builder uses a callback as the input parameter, as in **builder: custombuilder({ callback: ()=> {...}})**, pay attention to the binding of **this**.

To listen for data changes in the builder, use the @Link or @Consume decorator; other decorators, such as @Prop and @ObjectLink, do not apply.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| cancel | () => void | No | Yes | 

Callback invoked when the dialog box is closed after the Back button or mask is touched or the Esc key is pressed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| autoCancel | boolean | No | Yes | 

Whether to close the dialog box when the mask is touched. The value **true** means to close the dialog box when the mask is touched, and **false** means the opposite.

Default value: **true**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| alignment | [DialogAlignment](../alert-dialog-box-alertdialog/document.md#dialogalignment) | No | Yes | 

Alignment mode of the dialog box in the vertical direction.

Default value: **DialogAlignment.Default**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| offset | [Offset](../../common-definitions/basic-types/document.md#offset) | No | Yes | 

Offset of the dialog box relative to the alignment position.

Default value: **{dx: 0, dy: 0}**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| customStyle | boolean | No | Yes | 

Whether to use a custom style for the dialog box. **true** means a custom style cannot be used for the dialog box, and **false** means the opposite.

Default value: **false**

When this parameter is set to **false**:

1\. The default rounded corner radius is 32 vp.

2\. If the width and height of the dialog box are not set, the dialog box automatically adapts its width to the grid system and its height to the custom content node.

3\. The set width of the dialog box cannot exceed the maximum width in the default style (100% width for a custom node), and the set height cannot exceed the maximum height (100% height for a custom node).

4\. Due to safe area constraints, the dialog box display area excludes safe areas. For example, on PC/2-in-1 devices, it avoids screen edges and window title bars.

When this parameter is set to **true**:

1\. The rounded corner radius is 0, and the background color is transparent.

2\. The width, height, border width, border style, border color, and shadow width cannot be set for the dialog box.

3\. The dialog box display area covers the entire screen.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| gridCount8+ | number | No | Yes | 

Number of [grid columns](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-layout-development-grid-layout) occupied by the dialog box.

The default value is subject to the window size, and the maximum value is the maximum number of columns supported by the system. If this parameter is set to an invalid value, the default value is used.

Value range: an integer no less than 0

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| maskColor10+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Custom mask color.

Default value: **0x33000000**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| maskRect10+ | [Rectangle](../alert-dialog-box-alertdialog/document.md#rectangle8) | No | Yes | 

Mask area of the dialog box. Events outside the mask area are transparently transmitted, and events within the mask area are not.

Default value: **{ x: 0, y: 0, width: '100%', height: '100%' }**

**NOTE**

**maskRect** does not take effect when **showInSubWindow** is set to **true**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| openAnimation10+ | [AnimateParam](../../animation/explicit-animation-animateto/document.md#animateparam) | No | Yes | 

Parameters for defining the open animation of the dialog box.

**NOTE**

**tempo**: The default value is **1**; a value less than or equal to 0 is handled as the default value.

**iterations**: The default value is **1**, indicating that the animation is played once; any other value is handled as the default value.

**playMode**: The default value is **PlayMode.Normal**; any other value is handled as the default value.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| closeAnimation10+ | [AnimateParam](../../animation/explicit-animation-animateto/document.md#animateparam) | No | Yes | 

Parameters for defining the close animation of the dialog box.

**NOTE**

**tempo**: The default value is **1**; a value less than or equal to 0 is handled as the default value.

**iterations**: The default value is **1**, indicating that the animation is played once; any other value is handled as the default value.

**playMode**: The default value is **PlayMode.Normal**; any other value is handled as the default value.

For page transition, you are advised to use the default close animation.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| showInSubWindow10+ | boolean | No | Yes | 

Whether to show the dialog box in a subwindow when the dialog box needs to be displayed outside the main window. **true**: The dialog box is shown in a subwindow.

Default value: **false**

**NOTE**

A dialog box whose **showInSubWindow** attribute is **true** cannot trigger the display of another dialog box whose **showInSubWindow** attribute is also **true**. Avoid using the **CalendarPicker**, **CalendarPickerDialog**, **DatePickerDialog**, **TextPickerDialog**, **TimePickerDialog**, and **Toast** components in the dialog box where **showInSubWindow** is set to **true**, as the dialog box may affect the behavior of these components.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| backgroundColor10+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Background color of the dialog box.

Default value: **Color.Transparent**

**NOTE**

If the content builder also has the background color set, the background color set here will be overridden by the background color of the content builder.

The background color will be visually combined with the blur effect when both properties are set. If the resulting effect does not match your design requirements, you can disable the blur effect entirely by explicitly setting the **backgroundBlurStyle** property to **BlurStyle.NONE**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| cornerRadius10+ | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | [BorderRadiuses](../../common-definitions/basic-types/document.md#borderradiuses9) | No | Yes | 

Rounded corner radius of the background.

You can set separate radii for the four corners.

Default value: **{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }**

Note: The default corner radius of the background is 32 vp. This attribute must be used together with the [borderRadius](../../universal-attributes/layout-and-borders/border-styling/document.md#borderradius) attribute.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| isModal11+ | boolean | No | Yes | 

Whether the dialog box is a modal, which has a mask applied and does not allow for interaction with other components around the menu.

**true**: The dialog box is a modal.

**false**: The dialog box is not a modal.

Default value: **true**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onWillDismiss12+ | Callback<[DismissDialogAction](#dismissdialogaction12)\> | No | Yes | 

Callback for interactive closure of the dialog box.

**NOTE**

1\. If this callback is registered, the dialog box will not be dismissed immediately after the user touches the mask or the Back button, presses the Esc key, or swipes left or right on the screen. The **reason** parameter in the callback is used to determine whether the dialog box can be closed. The reason returned by the component does not support the value **CLOSE\_BUTTON**.

2\. In the **onWillDismiss** callback, another **onWillDismiss** callback is not allowed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| borderWidth12+ | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | [EdgeWidths](../../common-definitions/basic-types/document.md#edgewidths9) | No | Yes | 

Border width of the dialog box.

You can set the width for all four sides or set separate widths for individual sides.

Default value: **0**

When set to a percentage, the value defines the border width as a percentage of the parent dialog box's width.

If the left and right borders are greater than its width, or the top and bottom borders are greater than its height, the dialog box may not display as expected.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| borderColor12+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | [EdgeColors](../../common-definitions/basic-types/document.md#edgecolors9) | No | Yes | 

Border color of the dialog box.

Default value: **Color.Black**

**borderColor** must be used with **borderWidth** in pairs.

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
| backgroundBlurStyle12+ | [BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | Yes | 

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
| keyboardAvoidMode12+ | [KeyboardAvoidMode](../../universal-attributes/dialog-box-control/popup-control/document.md#keyboardavoidmode12) | No | Yes | 

How the dialog box avoids the soft keyboard when it is brought up.

Default value: **KeyboardAvoidMode.DEFAULT**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| enableHoverMode14+ | boolean | No | Yes | 

Whether to respond when the device is in semi-folded mode. The value **true** means to respond when the device is in semi-folded mode.

Default value: **false**, meaning not to enable the hover state.

**NOTE**

For a PC or 2-in-1 device, the dialog box is displayed on the upper half of the screen by default when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display the dialog box on the lower half of the screen. For other devices, the dialog box is displayed on the lower half of the screen by default when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display the dialog box on the upper half of the screen.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| hoverModeArea14+ | [HoverModeAreaType](../../universal-attributes/transition/sheet-transition/document.md#hovermodeareatype14) | No | Yes | 

Display area of the dialog box in the hover state.

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

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| onDidDisappear19+ | Callback<void> | No | Yes | 

Event callback after the dialog box disappears.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| keyboardAvoidDistance15+ | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 

Distance between the dialog box and the keyboard after keyboard avoidance is applied.

**NOTE**

\- Default value: **16vp**

\- Default unit: vp

\- This parameter takes effect only when **keyboardAvoidMode** is set to **DEFAULT**.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| levelMode15+ | [LevelMode](../../../arkts-api/ui/ohos-promptaction-prompt/document.md#levelmode15) | No | Yes | 

Display level of the dialog box.

**NOTE**

\- Default value: **LevelMode.OVERLAY.**

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
| immersiveMode15+ | [ImmersiveMode](../../../arkts-api/ui/ohos-promptaction-prompt/document.md#immersivemode15) | No | Yes | 

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
| focusable19+ | boolean | No | Yes | 

Whether the dialog box can gain focus. **true**: The dialog box can gain focus. **false**: The dialog box cannot gain focus.

Default value: **true**

**NOTE**

Only dialog boxes that are displayed on top of the current window can gain focus.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/lNYzn3pDT9ixKL86mIc5UA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0742462355E0EBD9C7C604D75B6924FA2179B3530A98F88B521E9237BBAD080)

-   Pressing the Back or ESC key closes the dialog box.
-   If the dialog box reaches its maximum allowable height on the screen when avoiding the soft keyboard, it reduces its height to fit.
    
    It should be noted that this height adjustment is applied to the outermost container. If a child component within this container has been assigned a larger fixed height, since the container does not clip its content by default, parts of the dialog box may still be displayed off-screen.
    
-   Use the custom dialog box to contain simple alert messages only. Do not use it as a page. When the dialog box avoids the soft keyboard, there is a 16 vp safe spacing between the two.
-   For optimal visual experience, dialog box display and closing include default animations, though the animation duration may vary by device.
    
    Note: During animation playback, the page does not respond to touch, swipe, or click interactions. To disable default dialog box animations, set **duration** of both **openAnimation** and **closeAnimation** to **0**.
    
-   In ArkUI, dialog boxes do not close automatically when you switch pages unless you manually call **close**. To enable a dialog box to be dismissed during page navigation, consider using the [navigation subpage displayed in dialog mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-navigation-navigation#page-display-mode) or [page-level dialog box](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-embedded-dialog).

#### DismissDialogAction12+

Provides information about the action to dismiss the dialog box.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

## Properties

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| dismiss | Callback<void> | No | No | Callback for dismissing the dialog box. This API is called only when the dialog box needs to be exited. |
| reason | [DismissReason](../../universal-attributes/dialog-box-control/popup-control/document.md#dismissreason12) | No | No | Reason why the dialog box cannot be dismissed. You must specify whether to close the dialog box for each of the listed actions. |

#### Example

## Example 1: Opening Nested Dialog Boxes

This example demonstrates how to open one or more custom dialog boxes within another custom dialog box.

// xxx.ets
@CustomDialog
struct CustomDialogExampleTwo {
  controllerTwo?: CustomDialogController;
  build() {
    Column() {
      Text('I'm the second dialog box')
        .fontSize(30)
        .height(100)
      Button('Close Second Dialog Box')
        .onClick(() => {
          if (this.controllerTwo != undefined) {
            this.controllerTwo.close();
          }
        })
        .margin(20)
    }
  }
}
@CustomDialog
@Component
struct CustomDialogExample {
  @Link textValue: string;
  @Link inputValue: string;
  dialogControllerTwo: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExampleTwo(),
    alignment: DialogAlignment.Bottom,
    onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
      console.info(\`reason= ${dismissDialogAction.reason}\`);
      console.info('dialog onWillDismiss');
      if (dismissDialogAction.reason == DismissReason.PRESS\_BACK) {
        dismissDialogAction.dismiss();
      }
      if (dismissDialogAction.reason == DismissReason.TOUCH\_OUTSIDE) {
        dismissDialogAction.dismiss();
      }
    },
    offset: { dx: 0, dy: -25 } })
  controller?: CustomDialogController;
  // You can pass in multiple other controllers in the CustomDialog to open one or more other CustomDialogs in the CustomDialog. In this case, you must place the controller pointing to the self behind all controllers.
  cancel: () => void = () => {
  }
  confirm: () => void = () => {
  }

  build() {
    Column() {
      Text('Change text').fontSize(20).margin({ top: 10, bottom: 10 })
      TextInput({ placeholder: '', text: this.textValue }).height(60).width('90%')
        .onChange((value: string) => {
          this.textValue = value;
        })
      Text('Are you sure you want to change the text?').fontSize(16).margin({ bottom: 10 })
      Flex({ justifyContent: FlexAlign.SpaceAround }) {
        Button('No')
          .onClick(() => {
            if (this.controller != undefined) {
              this.controller.close();
              this.cancel();
            }
          }).backgroundColor(0xffffff).fontColor(Color.Black)
        Button('OK')
          .onClick(() => {
            if (this.controller != undefined) {
              this.inputValue = this.textValue;
              this.controller.close();
              this.confirm();
            }
          }).backgroundColor(0xffffff).fontColor(Color.Red)
      }.margin({ bottom: 10 })

      Button('Open Second Dialog Box')
        .onClick(() => {
          if (this.dialogControllerTwo != null) {
            this.dialogControllerTwo.open();
          }
        })
        .margin(20)
    }.borderRadius(10)
    // When using the border or cornerRadius attribute, use it together with the borderRadius attribute.
  }
}
@Entry
@Component
struct CustomDialogUser {
  @State textValue: string = ''
  @State inputValue: string = 'click me'
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample({
      cancel: ()=> { this.onCancel(); },
      confirm: ()=> { this.onAccept(); },
      textValue: this.textValue,
      inputValue: this.inputValue
    }),
    cancel: this.exitApp,
    autoCancel: true,
    onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
      console.info(\`reason= ${dismissDialogAction.reason}\`);
      console.info('dialog onWillDismiss');
      if (dismissDialogAction.reason == DismissReason.PRESS\_BACK) {
        dismissDialogAction.dismiss();
      }
      if (dismissDialogAction.reason == DismissReason.TOUCH\_OUTSIDE) {
        dismissDialogAction.dismiss();
      }
    },
    alignment: DialogAlignment.Bottom,
    offset: { dx: 0, dy: -20 },
    gridCount: 4,
    customStyle: false,
    cornerRadius: 10,
  })

  // Set dialogController to null when the custom component is about to be destroyed.
  aboutToDisappear() {
    this.dialogController = null; // Set dialogController to null.
  }

  onCancel() {
    console.info('Callback when the first button is clicked');
  }

  onAccept() {
    console.info('Callback when the second button is clicked');
  }

  exitApp() {
    console.info('Click the callback in the blank area');
  }
  build() {
    Column() {
      Button(this.inputValue)
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        }).backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/MaQ60jrCSYuBkQVkQuBkyw/en-us_image_0000002568765639.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8ACFCF51CC5708F57C47A5BFC4C415B23A3F9F722B487278A53D8E23840FFB71)

## Example 2: Opening a Dialog Box Outside the Main Window

This example demonstrates how to configure a dialog box to display outside the main window on a 2-in-1 device by setting [showInSubWindow](#customdialogcontrolleroptions) to **true**.

// xxx.ets
@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;
  cancel: () => void = () => {
  }
  confirm: () => void = () => {
  }
  build() {
    Column() {
      Text('Dialog box outside the main window')
        .fontSize(30)
        .height(100)
      Button('Close')
        .onClick(() => {
          if (this.controller != undefined) {
            this.controller.close();
          }
        })
        .margin(20)
    }
  }
}
@Entry
@Component
struct CustomDialogUser {
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample({
      cancel: ()=> { this.onCancel(); },
      confirm: ()=> { this.onAccept(); }
    }),
    cancel: this.existApp,
    autoCancel: true,
    onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
      console.info(\`reason= ${dismissDialogAction.reason}\`);
      console.info('dialog onWillDismiss');
      if (dismissDialogAction.reason == DismissReason.PRESS\_BACK) {
        dismissDialogAction.dismiss();
      }
      if (dismissDialogAction.reason == DismissReason.TOUCH\_OUTSIDE) {
        dismissDialogAction.dismiss();
      }
    },
    alignment: DialogAlignment.Center,
    offset: { dx: 0, dy: -20 },
    gridCount: 4,
    showInSubWindow: true,
    isModal: true,
    customStyle: false,
    cornerRadius: 10,
    focusable: true
  })
  // Set dialogController to null when the custom component is about to be destroyed.
  aboutToDisappear() {
    this.dialogController = null; // Set dialogController to null.
  }

  onCancel() {
    console.info('Callback when the first button is clicked');
  }

  onAccept() {
    console.info('Callback when the second button is clicked');
  }

  existApp() {
    console.info('Click the callback in the blank area');
  }

  build() {
    Column() {
      Button('Click Me')
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        }).backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/E4Gn8_SgSpqVsho8CYnBaw/en-us_image_0000002537765914.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D62B1295FAADAA3203CE0657B5804CCB3A82E73F373436D9ADC004221B4C1EA1)

## Example 3: Setting the Dialog Box Style

This example demonstrates how to set styles of a custom dialog box, including the width, height, background color, and shadow.

// xxx.ets
@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;
  cancel: () => void = () => {
  }
  confirm: () => void = () => {
  }
  build() {
    Column() {
      Text('This is a custom dialog box')
        .fontSize(30)
        .height(100)
      Button('Close')
        .onClick(() => {
          if (this.controller != undefined) {
            this.controller.close();
          }
        })
        .margin(20)
    }
  }
}
@Entry
@Component
struct CustomDialogUser {
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample({
      cancel: ()=> { this.onCancel(); },
      confirm: ()=> { this.onAccept(); }
    }),
    cancel: this.existApp,
    autoCancel: true,
    onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
      console.info(\`reason= ${dismissDialogAction.reason}\`);
      console.info('dialog onWillDismiss')
      if (dismissDialogAction.reason == DismissReason.PRESS\_BACK) {
        dismissDialogAction.dismiss();
      }
      if (dismissDialogAction.reason == DismissReason.TOUCH\_OUTSIDE) {
        dismissDialogAction.dismiss();
      }
    },
    alignment: DialogAlignment.Center,
    offset: { dx: 0, dy: -20 },
    customStyle: false,
    cornerRadius: 20,
    width: 300,
    height: 200,
    borderWidth: 1,
    borderStyle: BorderStyle.Dashed,// borderStyle must be used with borderWidth in pairs.
    borderColor: Color.Blue,// borderColor must be used with borderWidth in pairs.
    backgroundColor: Color.White,
    shadow: ({ radius: 20, color: Color.Grey, offsetX: 50, offsetY: 0}),
  })
  // Set dialogController to null when the custom component is about to be destroyed.
  aboutToDisappear() {
    this.dialogController = null; // Set dialogController to null.
  }

  onCancel() {
    console.info('Callback when the first button is clicked');
  }

  onAccept() {
    console.info('Callback when the second button is clicked');
  }

  existApp() {
    console.info('Click the callback in the blank area');
  }

  build() {
    Column() {
      Button('Click Me')
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        }).backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/KFsVsILwQ6a0X5-ezn-42Q/en-us_image_0000002537925854.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8CD9D835BE517C49109BC20B6178A18064B6DBB8338E453D6CD3D949BCFE4FF7)

## Example 4: Configuring a Dialog Box in the Hover State

This example demonstrates how to set the layout area of a dialog box in hover mode on a foldable device.

@CustomDialog
@Component
struct CustomDialogExample {
  @Link textValue: string;
  @Link inputValue: string;
  controller?: CustomDialogController;

  build() {
    Column() {
      Text('Change text').fontSize(20).margin({ top: 10, bottom: 10 })
      TextInput({ placeholder: '', text: this.textValue }).height(60).width('90%')
        .onChange((value: string) => {
          this.textValue = value;
        })
      Text('Are you sure you want to change the text?').fontSize(16).margin({ bottom: 10 })
      Flex({ justifyContent: FlexAlign.SpaceAround }) {
        Button('No')
          .onClick(() => {
            if (this.controller != undefined) {
              this.controller.close();
            }
          }).backgroundColor(0xffffff).fontColor(Color.Black)
        Button('OK')
          .onClick(() => {
            if (this.controller != undefined) {
              this.inputValue = this.textValue;
              this.controller.close();
            }
          }).backgroundColor(0xffffff).fontColor(Color.Red)
      }.margin({ bottom: 10 })
    }.borderRadius(10)
    // When using the border or cornerRadius attribute, use it together with the borderRadius attribute.
  }
}
@Entry
@Component
struct CustomDialogUser {
  @State textValue: string = '';
  @State inputValue: string = 'click me';
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample({
      textValue: this.textValue,
      inputValue: this.inputValue
    }),
    cancel: this.exitApp,
    autoCancel: true,
    onWillDismiss: (dismissDialogAction: DismissDialogAction)=> {
      console.info(\`reason= ${dismissDialogAction.reason}\`);
      console.info('dialog onWillDismiss');
      if (dismissDialogAction.reason == DismissReason.PRESS\_BACK) {
        dismissDialogAction.dismiss();
      }
      if (dismissDialogAction.reason == DismissReason.TOUCH\_OUTSIDE) {
        dismissDialogAction.dismiss();
      }
    },
    alignment: DialogAlignment.Bottom,
    offset: { dx: 0, dy: -20 },
    gridCount: 4,
    customStyle: false,
    cornerRadius: 10,
    enableHoverMode: true,
    hoverModeArea: HoverModeAreaType.TOP\_SCREEN
  })

  // Set dialogController to null when the custom component is about to be destroyed.
  aboutToDisappear() {
    this.dialogController = null; // Set dialogController to null.
  }

  exitApp() {
    console.info('Click the callback in the blank area');
  }

  build() {
    Column() {
      Button(this.inputValue)
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        }).backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}

## Example 5: Obtaining the Dialog Box State

This example demonstrates how to call [getState](#getstate20) in [CustomDialogController](#customdialogcontroller) to obtain the current status of the dialog box.

The **getState** API is added to **CustomDialogController** since API version 20.

// xxx.ets
@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController

  build() {
    Column() {
      Button("Check Status: Custom Component Controller")
        .onClick(() => {
          if (this.getDialogController() != undefined) {
            console.info('state:' + this.getDialogController().getState())
          } else {
            console.info('state: no exist')
          }
        }).margin(20)
      Button('Check Status: CustomDialogController')
        .onClick(() => {
          console.info('state:' + this.controller?.getState())
        }).margin(20)
      Button('Close')
        .onClick(() => {
          if (this.getDialogController() != undefined) {
            this.getDialogController().close()
          }
        }).margin(20)
      
    }
  }
}

@Entry
@Component
struct CustomDialogUser {
  @State bg: ResourceColor = Color.Green
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample({
    }),
    autoCancel: false
  })

  build() {
    Column() {
      Button('Click Me')
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open()
          }
        }).backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
    .backgroundColor(this.bg)
  }
}

## Example 6: Using @Link and @Consume to Listen for Data Changes

This example uses @[Link](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-link) and @[Consume](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-provide-and-consume) to implement two-way data binding between the page and the dialog box.

@CustomDialog
@Component
struct CustomDialogExample {
  @Link textValue: string;
  @Consume inputValue: string;
  controller?: CustomDialogController;

  cancel: () => void = () => {
  }
  confirm: () => void = () => {
  }

  build() {
    Column() {
      Text('Change text').fontSize(20).margin({ top: 10, bottom: 10 })
      TextInput({ placeholder: '', text: this.textValue }).height(60).width('90%')
        .onChange((value: string) => {
          this.textValue = value;
        })
      Text('Are you sure you want to change the text?').fontSize(16).margin({ bottom: 10 })
      Flex({ justifyContent: FlexAlign.SpaceAround }) {
        Button('No')
          .onClick(() => {
            if (this.controller != undefined) {
              this.controller.close();
              this.cancel();
            }
          }).backgroundColor(0xffffff).fontColor(Color.Black)
        Button('OK')
          .onClick(() => {
            if (this.controller != undefined) {
              this.inputValue = this.textValue;
              this.controller.close();
              this.confirm();
            }
          }).backgroundColor(0xffffff).fontColor(Color.Red)
      }.margin({ bottom: 10 })
    }.borderRadius(10)
  }
}
@Entry
@Component
struct CustomDialogUser {
  @State textValue: string = ''
  @Provide inputValue: string = 'click me'
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample({
      cancel: ()=> { this.onCancel(); },
      confirm: ()=> { this.onAccept(); },
      textValue: this.textValue
    }),
    cancel: this.exitApp,
    autoCancel: true,
    onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
      if (dismissDialogAction.reason == DismissReason.PRESS\_BACK) {
        dismissDialogAction.dismiss();
      }
      if (dismissDialogAction.reason == DismissReason.TOUCH\_OUTSIDE) {
        dismissDialogAction.dismiss();
      }
    },
    alignment: DialogAlignment.Center,
    offset: { dx: 0, dy: -20 },
    gridCount: 4,
    customStyle: false,
    cornerRadius: 10,
  })

  // Set dialogController to null when the custom component is about to be destroyed.
  aboutToDisappear() {
    this.dialogController = null; // Set dialogController to null.
  }

  onCancel() {
    console.info('Callback when the first button is clicked');
  }

  onAccept() {
    console.info('Callback when the second button is clicked');
  }

  exitApp() {
    console.info('Click the callback in the blank area');
  }
  build() {
    Column() {
      Button(this.inputValue)
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        }).backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/8N4hKdfpRTSHZubSMRz-iw/en-us_image_0000002568685631.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C45D6D466C7546AD51CBDA6CE508C565A4A28CEB36CA617E5353575277CC5E82)

## Example 7: Customizing a Loading Dialog Box

This example uses [maskColor](#customdialogcontrolleroptions), [maskRect](#customdialogcontrolleroptions), and [LoadingProgress](../../information-display/loadingprogress/document.md) to implement a loading dialog box and display the transparent transmission effect of events that are not in the **maskRect** area.

import { window } from '@kit.ArkUI';

@CustomDialog
@Component
struct LoadingDialogExample {
  controller?: CustomDialogController;
  cancel: () => void = () => {
  }
  confirm: () => void = () => {
  }

  build() {
    Column() {
      LoadingProgress().color(Color.Blue).layoutWeight(1)
    }.borderRadius(10).width(100).height(100)
  }
}

@Entry
@Component
struct CustomDialogUser {
  @State number: number = 0;
  dialogController: CustomDialogController | null = null;

  // Set dialogController to null when the custom component is about to be destroyed.
  aboutToDisappear() {
    this.dialogController = null; // Set dialogController to null.
  }

  onCancel() {
    console.info('Callback when the first button is clicked');
  }

  onAccept() {
    console.info('Callback when the second button is clicked');
  }

  exitApp() {
    console.info('Click the callback in the blank area');
  }

  build() {
    Column() {
      Button("click " + this.number).onClick(() => {
        this.number++;
      })
      Button("show loading dialog").onClick(() => {
        // Obtain a window object.
        let windowClass = window.getLastWindow(this.getUIContext().getHostContext());
        windowClass.then(window => {
          // Obtain the window information and set maskRect.
          let properties = window.getWindowProperties();
          let maskRect = {
            x: this.getUIContext().px2vp(properties.windowRect.left + 150),
            y: this.getUIContext().px2vp(properties.windowRect.top + 350),
            width: this.getUIContext().px2vp(properties.windowRect.width - 300),
            height: this.getUIContext().px2vp(properties.windowRect.height - 700)
          } as Rectangle
          if (this.dialogController == null) {
            this.dialogController = new CustomDialogController({
              builder: LoadingDialogExample({
                cancel: () => {
                  this.onCancel();
                },
                confirm: () => {
                  this.onAccept();
                },
              }),
              cancel: this.exitApp,
              maskRect: maskRect,
              autoCancel: false,
              maskColor: "#33AA0000",
              showInSubWindow: false,
              backgroundBlurStyle: BlurStyle.NONE,
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                if (dismissDialogAction.reason == DismissReason.PRESS\_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason == DismissReason.TOUCH\_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              },
              alignment: DialogAlignment.Center,
              customStyle: false,
              cornerRadius: 10,
              openAnimation: { duration: 0, tempo: 0 },
              closeAnimation: { duration: 0, tempo: 0 }
            })
          }
          this.dialogController.close();
          this.dialogController.open();
        })
      }).backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/iQgHedSqS4Kz3yMallrVkg/en-us_image_0000002568765641.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18265360CB150CC74AC85E772DF22C0D9E1945A6E7576512383B3155800140F0)

## Example 8: Adjusting Spacing Between the Dialog Box and the Soft Keyboard Without keyboardAvoidDistance

This example demonstrates how to listen for keyboard changes and adjust the [bottom](../../common-definitions/basic-types/document.md#margin) of [margin](../../universal-attributes/layout-and-borders/sizing/document.md#margin) to achieve the same effect as using [keyboardAvoidDistance](#customdialogcontrolleroptions) to adjust the spacing between the dialog box and the soft keyboard.

Since API version 15, the **keyboardAvoidDistance** attribute is added to **CustomDialogControllerOptions**.

import { window } from '@kit.ArkUI';

@CustomDialog
@Component
struct CustomDialogExample {
  @Link textValue: string;
  @Link inputValue: string;
  @Link isKeyboardShow: boolean
  @Link navigationBarHeight: number
  controller?: CustomDialogController;
  cancel: () => void = () => {
  }
  confirm: () => void = () => {
  }

  build() {
    Column() {
      Text('Change text').fontSize(20).margin({ top: 10, bottom: 10 })
      TextInput({ placeholder: '', text: this.textValue }).height(60).width('90%')
        .onChange((value: string) => {
          this.textValue = value;
        })
      Text('Are you sure you want to change the text?').fontSize(16).margin({ bottom: 10 })
      Flex({ justifyContent: FlexAlign.SpaceAround }) {
        Button('No')
          .onClick(() => {
            if (this.controller != undefined) {
              this.controller.close();
              this.cancel();
            }
          }).backgroundColor(0xffffff).fontColor(Color.Black)
        Button('OK')
          .onClick(() => {
            if (this.controller != undefined) {
              this.inputValue = this.textValue;
              this.controller.close();
              this.confirm();
            }
          }).backgroundColor(0xffffff).fontColor(Color.Red)
      }.margin({ bottom: 10 })
    }.borderRadius(10)
    .margin({
      // Adjust the spacing (spacing between the keyboard and the dialog box is 16 vp) by using the keyboard.
      bottom: this.isKeyboardShow ? -16 : this.navigationBarHeight
    }).backgroundColor(Color.White)
  }
}

@Entry
@Component
struct CustomDialogUser {
  @State textValue: string = ''
  @State inputValue: string = 'click me'
  @State isKeyboardShow: boolean = false
  @State navigationBarHeight: number = 0
  windowClass: window.Window | null = null
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample({
      cancel: () => {
        this.onCancel();
      },
      confirm: () => {
        this.onAccept();
      },
      textValue: this.textValue,
      inputValue: this.inputValue,
      isKeyboardShow: this.isKeyboardShow,
      navigationBarHeight: this.navigationBarHeight
    }),
    cancel: this.exitApp,
    autoCancel: true,
    onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
      if (dismissDialogAction.reason == DismissReason.PRESS\_BACK) {
        dismissDialogAction.dismiss();
      }
      if (dismissDialogAction.reason == DismissReason.TOUCH\_OUTSIDE) {
        dismissDialogAction.dismiss();
      }
    },
    alignment: DialogAlignment.Bottom,
    customStyle: true,
    cornerRadius: 10,
  })

  aboutToAppear(): void {
    let windowClass = window.getLastWindow(this.getUIContext().getHostContext());
    windowClass.then(win => {
      this.windowClass = win;
      // Obtain the height of the bottom navigation bar.
      let navigationArea = this.windowClass?.getWindowAvoidArea(window.AvoidAreaType.TYPE\_NAVIGATION\_INDICATOR);
      this.navigationBarHeight = navigationArea.bottomRect.height;
      this.windowClass?.on('avoidAreaChange', (data) => {
        if (data.type == window.AvoidAreaType.TYPE\_KEYBOARD) {
          this.isKeyboardShow = data.area.bottomRect.height > 0;
        }
      })
    });
  }

  // Set dialogController to null when the custom component is about to be destroyed.
  aboutToDisappear() {
    this.dialogController = null; // Set dialogController to null.
    this.windowClass?.off('avoidAreaChange')
  }

  onCancel() {
    console.info('Callback when the first button is clicked');
  }

  onAccept() {
    console.info('Callback when the second button is clicked');
  }

  exitApp() {
    console.info('Click the callback in the blank area');
  }

  build() {
    Column() {
      Button(this.inputValue)
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        }).backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/6_M095nhQh-vapfWuY2iRA/en-us_image_0000002537765916.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=74CD0225C6D23803EBE7136A2B64A86BFFF4C687990CCF51709852113EF2E2E6)

## Example 9: Configuring the Lifecycle Callback for the Dialog Box

This example demonstrates how to configure the lifecycle callbacks for the dialog box.

Since API version 19, the **onDidAppear**, **onDidDisappear**, **onWillAppear**, and **onWillDisappear** attributes are added to [CustomDialogControllerOptions](#customdialogcontrolleroptions).

// xxx.ets
@CustomDialog
struct CustomDialogExample1 {
  controller?: CustomDialogController
  cancel: () => void = () => {
  }
  confirm: () => void = () => {
  }
  build() {
    Column() {
      Text('Allow access to camera?')
        .fontSize(30)
        .height(100)
      Button('Close')
        .onClick(() => {
          if (this.controller != undefined) {
            this.controller.close();
          }
        })
        .margin(20)
    }
  }
}

@Entry
@Component
struct Example3 {
  @State log: string = 'Log information:';
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample1({
      cancel: ()=> { this.onCancel(); },
      confirm: ()=> { this.onAccept(); }
    }),
    cancel: this.existApp,
    autoCancel: true,
    alignment: DialogAlignment.Bottom,
    onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
      console.info(\`reason= ${dismissDialogAction.reason}\`);
      console.info('dialog onWillDismiss');
      if (dismissDialogAction.reason == DismissReason.PRESS\_BACK) {
        dismissDialogAction.dismiss();
      }
      if (dismissDialogAction.reason == DismissReason.TOUCH\_OUTSIDE) {
        dismissDialogAction.dismiss();
      }
    },
    onDidAppear: () => {
      this.log += '# onDidAppear';
      console.info('CustomDialog,is onDidAppear!');
    },
    onDidDisappear: () => {
      this.log += '# onDidDisappear';
      console.info('CustomDialog,is onDidDisappear!');
    },
    onWillAppear: () => {
      this.log = 'Log information:onWillAppear';
      console.info('CustomDialog,is onWillAppear!');
    },
    onWillDisappear: () => {
      this.log += '# onWillDisappear';
      console.info('CustomDialog,is onWillDisappear!');
    },
    offset: { dx: 0, dy: -20 },
    customStyle: false,
  })
  onCancel() {
    console.info('CustomDialog Callback when the first button is clicked');
  }

  onAccept() {
    console.info('CustomDialog Callback when the second button is clicked');
  }

  existApp() {
    console.info('CustomDialog Click the callback in the blank area');
  }
  build() {
    Column({ space: 5 }) {
      Button('CustomDialog')
        .onClick(() => {
          this.dialogController?.open();
        })
      Text(this.log).fontSize(30).margin({ top: 200 })
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/UoDlnbUyTq27_Zye6ykfdQ/en-us_image_0000002537925856.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D132E477FFEC777EF1639274C0283F2D57495AA7033074F9FF3F1F609C5F25D0)

## Example 10: Implementing Dialog Boxes with Different customStyle Values

This example demonstrates the effect of the dialog box content and safe area when the alignment mode is [DialogAlignment.Bottom](#customdialogcontrolleroptions) and the value of [customStyle](#customdialogcontrolleroptions) is different.

@CustomDialog
@Component
struct CustomStyleDialogExample {
  controller?: CustomDialogController;
  cancel: () => void = () => {
  }
  confirm: () => void = () => {
  }

  build() {
    Column().borderRadius(10).width(110).height(110).backgroundColor("#2787d9")
  }
}

@Entry
@Component
struct CustomDialogUser {
  @State customStyle: boolean = false;
  dialogController: CustomDialogController | null = null;

  // Set dialogController to null when the custom component is about to be destroyed.
  aboutToDisappear() {
    this.dialogController = null; // Set dialogController to null.
  }

  onCancel() {
    console.info('Callback when the first button is clicked');
  }

  onAccept() {
    console.info('Callback when the second button is clicked');
  }

  exitApp() {
    console.info('Click the callback in the blank area');
  }

  build() {
    Column() {
      Button('change  customStyle:' + this.customStyle).onClick(() => {
        this.customStyle = !this.customStyle;
      })
      Button('show dialog').onClick(() => {
        if (this.dialogController != null) {
          this.dialogController.close();
        }
        this.dialogController = new CustomDialogController({
          builder: CustomStyleDialogExample({
            cancel: () => {
              this.onCancel();
            },
            confirm: () => {
              this.onAccept();
            },
          }),
          cancel: this.exitApp,
          autoCancel: true,
          showInSubWindow: false,
          onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
            if (dismissDialogAction.reason == DismissReason.PRESS\_BACK) {
              dismissDialogAction.dismiss();
            }
            if (dismissDialogAction.reason == DismissReason.TOUCH\_OUTSIDE) {
              dismissDialogAction.dismiss();
            }
          },
          alignment: DialogAlignment.Bottom,
          customStyle: this.customStyle,
          cornerRadius: 10,
          openAnimation: { duration: 0, tempo: 0 },
          closeAnimation: { duration: 0, tempo: 0 }
        })
        this.dialogController.open();
      }).margin({ top: 5 })
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/KmfhWPJ0Se6_skR7Jfvb2A/en-us_image_0000002568685633.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=731EC1427F8C74DD7268B9B43A3FB55251BA7346A702FF422BC5D35DA98F3A4E)

## Example 11: Customizing the Background Blur Effect

This example demonstrates how to customize the background blur effect by configuring [backgroundBlurStyleOptions](#customdialogcontrolleroptions).

Since API version 19, the **backgroundBlurStyleOptions** attribute is added to [CustomDialogControllerOptions](#customdialogcontrolleroptions).

@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;

  build() {
    Column() {
      Text('This is a custom dialog box')
        .fontSize(30)
        .height(100)
      Button('Close')
        .onClick(() => {
          if (this.controller != undefined) {
            this.controller.close();
          }
        })
        .margin(20)
    }
  }
}

@Entry
@Component
struct CustomDialogUser {
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample(),
    backgroundColor: undefined,
    backgroundBlurStyle: BlurStyle.Thin,
    backgroundBlurStyleOptions: {
      colorMode: ThemeColorMode.LIGHT,
      adaptiveColor: AdaptiveColor.AVERAGE,
      scale: 1,
      blurOptions: { grayscale: \[20, 20\] },
    },
  })

  build() {
    Stack({ alignContent: Alignment.Top }) {
      // Replace $r('app.media.bg') with the image resource file you use.
      Image($r('app.media.bg'))
      Column() {
        Button('CustomDialog')
          .margin(20)
          .onClick(() => {
            if (this.dialogController != null) {
              this.dialogController.open();
            }
          })
      }.width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/x881zE1zQASm3rG0Xw1rOw/en-us_image_0000002568765643.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=918F460397B5844A2437F0E64BD7E8B2432038270B344833F5B51A03C65E17C2)

## Example 12: Customizing the Background Effect

This example demonstrates how to customize the background effect by configuring [backgroundEffect](#customdialogcontrolleroptions).

Since API version 19, the **backgroundEffect** attribute is added to [CustomDialogControllerOptions](#customdialogcontrolleroptions).

@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;

  build() {
    Column() {
      Text('This is a custom dialog box')
        .fontSize(30)
        .height(100)
      Button('Close')
        .onClick(() => {
          if (this.controller != undefined) {
            this.controller.close();
          }
        })
        .margin(20)
    }
  }
}

@Entry
@Component
struct CustomDialogUser {
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample(),
    backgroundColor: undefined,
    backgroundBlurStyle: BlurStyle.Thin,
    backgroundEffect: {
      radius: 60,
      saturation: 0,
      brightness: 1,
      color: Color.White,
      blurOptions: { grayscale: \[20, 20\] }
    },
  })

  build() {
    Stack({ alignContent: Alignment.Top }) {
      // Replace $r('app.media.bg') with the image resource file you use.
      Image($r('app.media.bg'))
      Column() {
        Button('CustomDialog')
          .margin(20)
          .onClick(() => {
            if (this.dialogController != null) {
              this.dialogController.open();
            }
          })
      }.width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/so8_AxV5RKaWkbTg0aEFUQ/en-us_image_0000002537765918.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40C0FB6F846F969E88573F7D393FD9C424C21647CAEFAF18BD3976F02BB52B31)

## Example 13: Dynamically Updating the Custom Dialog Box Width

This example demonstrates how to dynamically update the custom dialog box width by synchronizing the custom component's width with a state variable.

@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;
  @Link currentWidth: number;

  build() {
    Column() {
      Text('This is a custom dialog box')
        .fontSize(30)
        .height(100)
      Button('Close')
        .onClick(() => {
          if (this.controller != undefined) {
            this.controller.close();
          }
        })
        .margin(20)
    }
    .borderRadius(32)
    .backgroundColor(Color.White)
    .shadow(ShadowStyle.OUTER\_DEFAULT\_SM)
    .width(this.currentWidth + "%")
  }
}

@Entry
@Component
struct CustomDialogUser {
  @State currentWidth: number = 0
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample({ currentWidth: this.currentWidth }),
    customStyle: true,
    isModal: false,
  })

  build() {
    Column() {

      Row() {
        Text("Width:")
          .height(50)
        Slider({ min: 60, max: 100, step: 5 })
          .showTips(true, this.currentWidth + '%')
          .onChange((value: number, mode: SliderChangeMode) => {
            this.currentWidth = value;
          }).width(200)
      }

      Button('CustomDialog')
        .margin(20)
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/s4WRY7vHTsSb8dH80ATz3Q/en-us_image_0000002537925858.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D6D96917D1B416B3C11046AC69B2256EEA14B5779C46E6B43D10AE0565A1DE6)
