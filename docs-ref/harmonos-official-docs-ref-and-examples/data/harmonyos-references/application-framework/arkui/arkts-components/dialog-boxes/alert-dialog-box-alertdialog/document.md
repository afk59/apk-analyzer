# Alert Dialog Box (AlertDialog)

You can set the text content and response callback for an alert dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/H--XmEi1TD-K0FRaPKL9ew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24FE93D30C8598DBE2C77DA78BBB3D0A11F6E1FCC8E920C97F297ECBC2B3E293)

The initial APIs of this module are supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

The functionality of this module depends on UI context. This means that the APIs of this module cannot be used where [the UI context is ambiguous](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). For details, see [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md).

#### AlertDialogParam

Enumerates the alert dialog box styles.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Title of the dialog box.

Prior to API version 20: The title of the dialog box is left-aligned.

API version 20 and later: The title of the dialog box is center-aligned.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| subtitle10+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Subtitle of the dialog box.

Prior to API version 20: The subtitle of the dialog box is left-aligned.

API version 20 and later: The subtitle of the dialog box is center-aligned.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| message | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 

Content of the dialog box.

Prior to API version 20: The content of the dialog box is left-aligned.

API version 20 and later: The content of the dialog box is center-aligned.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| autoCancel | boolean | No | Yes | 

Whether to dismiss the dialog box when the mask is touched. The value **true** means to dismiss the dialog box when the mask is touched, and **false** means the opposite.

Default value: **true**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| cancel | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 

Callback invoked when the dialog box is closed after the overlay is clicked.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| alignment | [DialogAlignment](#dialogalignment) | No | Yes | 

Alignment mode of the dialog box in the vertical direction.

Default value: **DialogAlignment.Default**

**Atomic service API**: This API can be used in atomic services since API version 11.

**NOTE**

If **showInSubWindow** is set to **true** in **UIExtension**, the dialog box is aligned with the host window based on **UIExtension**.

 |
| offset | [Offset](../../common-definitions/basic-types/document.md#offset) | No | Yes | 

Offset of the dialog box based on the **alignment** settings.

Default value: **{ dx: 0 , dy: 0 }**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| gridCount | number | No | Yes | 

Number of grid columns occupied by the width of the dialog box.

Default value: **4**

Value range: an integer no less than 0

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| maskRect10+ | [Rectangle](#rectangle8) | No | Yes | 

Mask area of the dialog box. Events outside the mask area are transparently transmitted, and events within the mask area are not.

Default value: **{ x: 0, y: 0, width: '100%', height: '100%' }**

**NOTE**

**maskRect** does not take effect when **showInSubWindow** is set to **true**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| showInSubWindow11+ | boolean | No | Yes | 

Whether to show the dialog box in a subwindow when the dialog box needs to be displayed outside the main window.

**true**: The dialog box is shown in a subwindow.

Default value: **false**, meaning the dialog box is displayed within the application, not in a separate subwindow

**NOTE**

A dialog box whose **showInSubWindow** attribute is **true** cannot trigger the display of another dialog box whose **showInSubWindow** attribute is also **true**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| isModal11+ | boolean | No | Yes | 

Whether the dialog box is a modal. A modal dialog box has a mask applied, while a non-modal dialog box does not. **false**: The dialog box is not a modal.

Default value: **true**.

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

Callback for interactive dismissal of the dialog box.

**NOTE**

1\. If this callback is registered, the dialog box will not be dismissed immediately after the user touches the mask or the Back button, presses the **Esc** key, or swipes left or right on the screen. The **reason** parameter in the callback is used to determine whether the dialog box can be dismissed. The reason returned by the component does not support the value **CLOSE\_BUTTON**.

2\. In the **onWillDismiss** callback, another **onWillDismiss** callback is not allowed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| cornerRadius12+ | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | [BorderRadiuses](../../common-definitions/basic-types/document.md#borderradiuses9) | [LocalizedBorderRadiuses](../../common-definitions/basic-types/document.md#localizedborderradiuses12) | No | Yes | 

Corner radius of the background.

You can set separate radii for the four corners.

Default value: **{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }**

The radius of the rounded corners is subject to the component size. Its maximum value is half of the component width or height. If the value is negative, the default value is used.

When set to a percentage, the value defines the radius as a percentage of the parent dialog box's width or height.

**NOTE**

When **cornerRadius** is of type LocalizedBorderRadiuses, the layout order can be dynamically adjusted based on the user's language settings.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| transition12+ | [TransitionEffect](../../animation/component-transition-transition/document.md#transitioneffect10) | No | Yes | 

Transition effect for the appearance and disappearance of the dialog box.

**NOTE**

1\. If this parameter is not set, the default effect is used.

2\. Touching the Back button during the appearance animation pauses the appearance animation and starts the disappearance animation. The final effect is one obtained after the curves of the appearance and disappearance animations are combined.

3\. Touching the Back button during the exit animation does not affect the animation playback. Touching the Back button again closes the application.

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
| borderWidth12+ | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | [EdgeWidths](../../common-definitions/basic-types/document.md#edgewidths9) | [LocalizedEdgeWidths](../../common-definitions/basic-types/document.md#localizededgewidths12) | No | Yes | 

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

Default value: **BorderStyle.Solid**.

**borderStyle** must be used with **borderWidth** in pairs.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| shadow12+ | [ShadowOptions](../../universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../universal-attributes/visual-effects/image-effect/document.md#shadowstyle10) | No | Yes | 

Shadow of the dialog box.

Default value on 2-in-1 devices: **ShadowStyle.OUTER\_FLOATING\_MD** when the dialog box is focused and **ShadowStyle.OUTER\_FLOATING\_SM** otherwise On other devices, the dialog box has no shadow by default.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| textStyle12+ | [TextStyle](#textstyle12) | No | Yes | 

Text style of the message in the dialog box.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| enableHoverMode14+ | boolean | No | Yes | 

Whether to respond when the device is in semi-folded mode. The value **true** means to respond when the device is in semi-folded mode.

Default value: **false**, meaning not to respond when the device is in semi-folded mode.

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

The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| onDidDisappear19+ | Callback<void> | No | Yes | 

Event callback after the dialog box disappears.

**NOTE**

The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| levelMode15+ | [LevelMode](../../../arkts-api/ui/ohos-promptaction-prompt/document.md#levelmode15) | No | Yes | 

Display level of the dialog box.

**NOTE**

\- Default value: **LevelMode.OVERLAY**

\- This parameter takes effect only when **showInSubWindow** is set to **false**.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| levelUniqueId15+ | number | No | Yes | 

[Unique ID](../../../arkts-api/ui/arkui/framenode/document.md#getuniqueid12) of the node under the display level for the page-level dialog box. This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.

Value range: a number no less than 0

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| immersiveMode15+ | [ImmersiveMode](../../../arkts-api/ui/ohos-promptaction-prompt/document.md#immersivemode15) | No | Yes | 

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

#### LevelOrder18+

type LevelOrder = LevelOrder

Defines the display order of the dialog box.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [LevelOrder](../../../arkts-api/ui/ohos-promptaction-prompt/document.md#levelorder18) | Display order of the dialog box. |

#### AlertDialogParamWithConfirm

Inherited from [AlertDialogParam](#alertdialogparam).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| confirm | [AlertDialogButtonBaseOptions](#alertdialogbuttonbaseoptions18) | No | Yes | Information about the confirm button. When the dialog box has focus and the **Tab** key is not pressed for sequential focus navigation, the button responds to the **Enter** key by default. Multiple dialog boxes can automatically gain focus and respond to user interactions in a sequential manner. The default response to the **Enter** key does not work when **defaultFocus** is set to **true**. |

Priorities of the **confirm** parameters: **fontColor** and **backgroundColor** > **style** > **defaultFocus**

| backgroundColor | fontColor | style | defaultFocus | Effect |
| :-- | :-- | :-- | :-- | :-- |
| Green | Red | \- | \- | Red text on green background |
| Green | \- | DialogButtonStyle.HIGHLIGHT | \- | White text on green background |
| Green | \- | DialogButtonStyle.DEFAULT | \- | Blue text on green background |
| Green | \- | \- | TRUE | White text on green background |
| Green | \- | \- | FALSE/- | Blue text on green background |
| \- | Red | DialogButtonStyle.HIGHLIGHT | \- | Red text on blue background |
| \- | Red | DialogButtonStyle.DEFAULT | \- | Red text on white background |
| \- | Red | \- | TRUE | Red text on blue background |
| \- | Red | \- | FALSE/- | Red text on white background |
| \- | \- | DialogButtonStyle.HIGHLIGHT | \- | White text on blue background |
| \- | \- | DialogButtonStyle.DEFAULT | \- | Blue text on white background |
| \- | \- | \- | TRUE | White text on blue background |
| \- | \- | \- | FALSE/- | Blue text on white background |

#### AlertDialogParamWithButtons

Inherited from [AlertDialogParam](#alertdialogparam).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| primaryButton | [AlertDialogButtonBaseOptions](#alertdialogbuttonbaseoptions18) | No | No | Information about the confirm button. When the dialog box has focus and focus has not been shifted using the **Tab** key, the button responds to the **Enter** key by default, and multiple dialog boxes can gain focus consecutively to respond automatically. The default response to the **Enter** key does not work when **defaultFocus** is set to **true**. |
| secondaryButton | [AlertDialogButtonBaseOptions](#alertdialogbuttonbaseoptions18) | No | No | Information about the confirm button. |

#### AlertDialogParamWithOptions10+

Inherited from [AlertDialogParam](#alertdialogparam).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| buttons | Array<[AlertDialogButtonOptions](#alertdialogbuttonoptions10)\> | No | No | Buttons in the dialog box. |
| buttonDirection | [DialogButtonDirection](#dialogbuttondirection10) | No | Yes | Button layout direction. The default value is **DialogButtonDirection.AUTO**. You are advised to use the auto mode for more than three buttons. (Vertical layout is used for more than two buttons, typically accommodating more buttons.) In non-auto mode, more than three buttons may not be completely displayed, and the buttons that exceed the display range will be truncated. |

#### AlertDialogButtonOptions10+

Inherits from [AlertDialogButtonBaseOptions](#alertdialogbuttonbaseoptions18).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| primary12+ | boolean | No | Yes | 
Whether the button responds to the **Enter** key by default when the dialog box has focus and the **Tab** key is not pressed for sequential focus navigation. If there are multiple buttons, set this parameter to **true** for only one button. Otherwise, no button will respond. Multiple dialog boxes can automatically gain focus and respond to user interactions in a sequential manner. This parameter does not take effect when **defaultFocus** is set to **true**. **true**: The button responds to the **Enter** key by default. **false**: The button does not respond to the **Enter** key by default.

Default value: **false**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### AlertDialogButtonBaseOptions18+

Defines the button style of the alert dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/BQJKTANtSnGYqJgrsYVUXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A29F1D65286D3E442E497CA953ABFD24D57F1DE3C1AAC0E1A9C147D282D5CFF)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| enabled10+ | boolean | No | Yes | 
Whether to respond when the button is clicked.

Default value: **true**

**true**: Respond when the button is clicked. **false**: Do not respond when the button is clicked.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| defaultFocus10+ | boolean | No | Yes | 

Whether the button is the default focus. Default value: **false**. **true**: The button is the default focus. **false**: The button is not the default focus.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| style10+ | [DialogButtonStyle](../../common-definitions/enums/document.md#dialogbuttonstyle10) | No | Yes | 

Style of the button.

Default value: **DialogButtonStyle.DEFAULT**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| value10+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 

Text of the button. If the value is null, the button is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| fontColor10+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Font color of the button.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| backgroundColor10+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Background color of the button.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| action10+ | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | No | 

Callback upon button clicking.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### DialogButtonDirection10+

Enumerates the alignment modes of the buttons in the alert dialog box.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| AUTO | 0 | Buttons are laid out horizontally when there are two or fewer buttons and vertically otherwise. |
| HORIZONTAL | 1 | Buttons are laid out horizontally. |
| VERTICAL | 2 | Buttons are laid out vertically. |

#### DialogAlignment

Enumerates the alignment modes of the alert dialog boxes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Top | 0 | Vertical top alignment. |
| Center | 1 | Vertical center alignment. |
| Bottom | 2 | Vertical bottom alignment. |
| Default | 3 | Default alignment. |
| TopStart8+ | 4 | Top left alignment. |
| TopEnd8+ | 5 | Top right alignment. |
| CenterStart8+ | 6 | Center left alignment. |
| CenterEnd8+ | 7 | Center right alignment. |
| BottomStart8+ | 8 | Bottom left alignment. |
| BottomEnd8+ | 9 | Bottom right alignment. |

#### Rectangle8+

The **Rectangle** type is used to represent a mask area of a dialog box.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 
X coordinate of the mask area of the dialog box relative to the upper left corner of the window.

Default value: **0vp**

 |
| y | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Y coordinate of the mask area of the dialog box relative to the upper left corner of the window.

Default value: **0vp**

 |
| width | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Width of the mask area of the dialog box.

Default value: **'100%'**

 |
| height | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Height of the mask area of the dialog box.

Default value: **'100%'**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/hH-xXk4_Q3ecX9iqpxxbYw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F9C31666CB3E738B80AC7B28BA77B7DFA63B8204F1CCA3E5B3D11732821B7A32)

**x** and **y** can be set to a positive or negative percentage value. When **x** is set to **'100%'**, the mask area is moved rightward by the window width. When **x** is set to **'-100%'**, the mask area is moved leftward by the window width. When **y** is set to **'100%'**, the mask area is moved downward by the window height. When **y** is set to **'-100%'**, the mask area is moved upward by the window height.

**width** and **height** can be set in percentage and can only be set to positive values. If they are set to negative values, the default values are used instead.

The percentage is calculated based on the width and height of the window.

#### DismissDialogAction12+

Provides information about the action to dismiss the dialog box.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

## Attributes

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| dismiss | Callback<void> | No | No | Callback for dismissing the dialog box. This API is called only when the dialog box needs to be exited. |
| reason | [DismissReason](../../universal-attributes/dialog-box-control/popup-control/document.md#dismissreason12) | No | No | Reason why the dialog box cannot be dismissed. You must specify whether to close the dialog box for each of the listed actions. |

#### TextStyle12+

Describes the word break rule of the message in the dialog box.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| wordBreak | [WordBreak](../../common-definitions/enums/document.md#wordbreak11) | No | Yes | 
Word break rule.

Default value: **WordBreak.BREAK\_ALL**

 |

#### AlertDialog

#### \[h2\]show(deprecated)

static show(value: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions)

Shows an alert dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/4RewNtclQ16dnJe3wqY5Gw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA84621212D4395A0FAC061402C4C363B3D1D71B13CD6CA665F161F23425E7D2)

This API is supported since API version 7 and deprecated since API version 18. You are advised to use [showAlertDialog](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#showalertdialog) instead. **showAlertDialog** can be called only after a [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) instance is obtained.

Since API version 10, you can use the [showAlertDialog](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#showalertdialog) API in [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md), which ensures that the alert dialog box is shown in the intended UI instance.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [AlertDialogParamWithConfirm](#alertdialogparamwithconfirm) | [AlertDialogParamWithButtons](#alertdialogparamwithbuttons) | [AlertDialogParamWithOptions](#alertdialogparamwithoptions10)10+ | Yes | Defines and displays the **AlertDialog** component. |

#### Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/VqLL06eaTIym-oAbRmbsjg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ABC05F0D74E5EE3B4C98203716009352ACAEF320619D49D6EF8F93C4BD83B2C1)

Directly using **AlertDialog** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). To avoid this, obtain the [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) object using the **getUIContext()** API and then call **AlertDialog.show()** bound to the instance using the [showAlertDialog](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#showalertdialog) API.

## Example 1: Displaying Dialog Boxes with Different Numbers of Buttons

This example uses [AlertDialogParamWithConfirm](#alertdialogparamwithconfirm), [AlertDialogParamWithButtons](#alertdialogparamwithbuttons), and [AlertDialogParamWithOptions](#alertdialogparamwithoptions10) to display dialog boxes with one, two, and three buttons, respectively.

// xxx.ets
@Entry
@Component
struct AlertDialogExample {
  build() {
    Column({ space: 5 }) {
      Button('one button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Bottom,
              offset: { dx: 0, dy: -20 },
              gridCount: 3,
              confirm: {
                value: 'button',
                action: () => {
                  console.info('Button-clicking callback');
                }
              },
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(\`reason= ${dismissDialogAction.reason}\`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS\_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH\_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            }
          )
        })
        .backgroundColor(0x317aff)
      Button('two button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              subtitle: 'subtitle',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Bottom,
              gridCount: 4,
              offset: { dx: 0, dy: -20 },
              primaryButton: {
                value: 'cancel',
                action: () => {
                  console.info('Callback when the first button is clicked');
                }
              },
              secondaryButton: {
                enabled: true,
                defaultFocus: true,
                style: DialogButtonStyle.HIGHLIGHT,
                value: 'ok',
                action: () => {
                  console.info('Callback when the second button is clicked');
                }
              },
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(\`reason= ${dismissDialogAction.reason}\`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS\_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH\_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            }
          )
        }).backgroundColor(0x317aff)
      Button('three button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              subtitle: 'subtitle',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Bottom,
              gridCount: 4,
              offset: { dx: 0, dy: -20 },
              buttonDirection: DialogButtonDirection.HORIZONTAL,
              buttons: \[
                {
                  value: 'Button',
                  action: () => {
                    console.info('Callback when button1 is clicked');
                  }
                },
                {
                  value: 'Button',
                  action: () => {
                    console.info('Callback when button2 is clicked');
                  }
                },
                {
                  value: 'Button',
                  enabled: true,
                  defaultFocus: true,
                  style: DialogButtonStyle.HIGHLIGHT,
                  action: () => {
                    console.info('Callback when button3 is clicked');
                  }
                },
              \],
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(\`reason= ${dismissDialogAction.reason}\`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS\_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH\_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            }
          )
        }).backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/frtmLUEdTeu4MBc7wYPVLQ/en-us_image_0000002537765906.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C53BD947EABF08C5BD78DFC8A557D54A9FF4E1F4204B2704D265A51E99A2973F)

## Example 2: Opening a Dialog Box Outside the Main Window

This example demonstrates how to configure a dialog box to display outside the main window on a 2-in-1 device by setting **showInSubWindow** in [AlertDialogParam](#alertdialogparam) to **true**.

// xxx.ets
@Entry
@Component
struct AlertDialogExample {
  build() {
    Column({ space: 5 }) {
      Button('one button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              subtitle: 'subtitle',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Center,
              gridCount: 4,
              showInSubWindow: true,
              isModal: true,
              offset: { dx: 0, dy: -20 },
              buttonDirection: DialogButtonDirection.HORIZONTAL,
              buttons: \[
                {
                  value: 'Button',
                  action: () => {
                    console.info('Callback when button1 is clicked');
                  }
                },
                {
                  value: 'Button',
                  action: () => {
                    console.info('Callback when button2 is clicked');
                  }
                },
                {
                  value: 'Button',
                  enabled: true,
                  defaultFocus: true,
                  style: DialogButtonStyle.HIGHLIGHT,
                  action: () => {
                    console.info('Callback when button3 is clicked');
                  }
                },
              \],
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(\`reason= ${dismissDialogAction.reason}\`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS\_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH\_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            })
        })
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/RzuBlp77R3eUHI44JzyFdA/en-us_image_0000002537925846.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E54819FC27259FCE5F35436E7A2FF465D141076288275FD470A35E36E76582E6)

## Example 3: Setting the Dialog Box Animation

This example demonstrates how to use the **transition** attribute in [AlertDialogParam](#alertdialogparam) to create animation effects for the dialog box's appearance and disappearance.

// xxx.ets
@Entry
@Component
struct AlertDialogExample {
  build() {
    Column({ space: 5 }) {
      Button('AlertDialog Set Duration')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'AlertDialog 1',
              message: 'Set Animation Duration open 3 second, close 100ms',
              autoCancel: true,
              alignment: DialogAlignment.Top,
              offset: { dx: 0, dy: -20 },
              gridCount: 3,
              transition: TransitionEffect.asymmetric(TransitionEffect.OPACITY
                .animation({ duration: 3000, curve: Curve.Sharp })
                .combine(TransitionEffect.scale({ x: 1.5, y: 1.5 }).animation({ duration: 3000, curve: Curve.Sharp })),
                TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
                  .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
                    .animation({ duration: 100, curve: Curve.Smooth }))),
              confirm: {
                value: 'button',
                action: () => {
                  console.info('Button-clicking callback');
                }
              },
              cancel: () => {
                console.info('Closed callbacks');
              }
            }
          )
        })
        .backgroundColor(0x317aff).height('88px')
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/G5snA63lSI2puBUzxp50Vw/en-us_image_0000002568685623.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFDA51CCE09F42BB43C3003B8ECD5F9A739A7819905861137C87DFC3608DCD7E)

## Example 4: Setting the Dialog Box Style

This example demonstrates how to set styles of an alert dialog box, including the width, height, background color, and shadow.

// xxx.ets
@Entry
@Component
struct AlertDialogExample {
  build() {
    Column({ space: 5 }) {
      Button('one button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Center,
              offset: { dx: 0, dy: -20 },
              gridCount: 3,
              width: 300,
              height: 200,
              cornerRadius: 20,
              borderWidth: 1,
              borderStyle: BorderStyle.Dashed, // borderStyle must be used with borderWidth in pairs.
              borderColor: Color.Blue, // borderColor must be used with borderWidth in pairs.
              backgroundColor: Color.White,
              shadow: ({
                radius: 20,
                color: Color.Grey,
                offsetX: 50,
                offsetY: 0
              }),
              textStyle: { wordBreak: WordBreak.BREAK\_ALL },
              confirm: {
                value: 'button',
                action: () => {
                  console.info('Button-clicking callback');
                }
              },
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(\`reason= ${dismissDialogAction.reason}\`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS\_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH\_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            }
          )
        })
        .backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/L4M_cjLxSOqjvqMFXIa33g/en-us_image_0000002568765633.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14178409E5FB3CB1D9FA150BBAA7A1190F3CBCD2A7803737B17C69464D39DEFD)

## Example 5: Configuring a Dialog Box in the Hover State

This example demonstrates how to set the layout area of a dialog box in hover mode on a foldable device.

// xxx.ets
@Entry
@Component
struct AlertDialogExample {
  build() {
    Column({ space: 5 }) {
      Button('one button dialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog(
            {
              title: 'title',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Bottom,
              gridCount: 3,
              confirm: {
                value: 'button',
                action: () => {
                  console.info('Button-clicking callback');
                }
              },
              cancel: () => {
                console.info('Closed callbacks');
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                console.info(\`reason= ${dismissDialogAction.reason}\`);
                console.info('AlertDialog onWillDismiss');
                if (dismissDialogAction.reason === DismissReason.PRESS\_BACK) {
                  dismissDialogAction.dismiss();
                }
                if (dismissDialogAction.reason === DismissReason.TOUCH\_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              },
              enableHoverMode: true,
              hoverModeArea: HoverModeAreaType.TOP\_SCREEN
            }
          )
        })
        .backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/gAtfLoOUT6qsWi2hhwOkaQ/en-us_image_0000002537765908.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BF54AD6115286C6BADACFE4A14DD6C0A84F165A8A920F0356E27579492C06D8)

## Example 6: Using Dialog Box Lifecycle Callbacks

This example demonstrates the usage of dialog box lifecycle callbacks.

// xxx.ets
@Entry
@Component
struct Example2 {
  @State log: string = 'Log information:';

  build() {
    Column({ space: 5 }) {
      Button('AlertDialog')
        .onClick(() => {
          this.getUIContext().showAlertDialog({
            title: 'AlertDialog',
            message: 'message',
            autoCancel: true,
            alignment: DialogAlignment.Bottom,
            offset: { dx: 0, dy: -20 },
            confirm: {
              value: 'button',
              action: () => {
                console.info('AlertDialog Button-clicking callback');
              }
            },
            cancel: () => {
              console.info('Closed callbacks');
            },
            onDidAppear: () => {
              this.log += '# onDidAppear';
              console.info('AlertDialog,is onDidAppear!');
            },
            onDidDisappear: () => {
              this.log += '# onDidDisappear';
              console.info('AlertDialog,is onDidDisappear!');
            },
            onWillAppear: () => {
              this.log = 'Log information:onWillAppear';
              console.info('AlertDialog,is onWillAppear!');
            },
            onWillDisappear: () => {
              this.log += '# onWillDisappear';
              console.info('AlertDialog,is onWillDisappear!');
            }
          })
        })
      Text(this.log).fontSize(30).margin({ top: 200 })
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Qfec9rbMSbu_T66WJTyv2Q/en-us_image_0000002537925848.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3D0311B5C302812AA22E7226062CD2E95E56F8A2581467A2C0A4BDE0BE3D713)

## Example 7: Customizing the Background Blur Effect

This example demonstrates how to customize the background blur effect by setting **backgroundBlurStyleOptions** in [AlertDialogParam](#alertdialogparam).

The **backgroundBlurStyleOptions** attribute is added to **AlertDialogParam** since API version 19.

@Entry
@Component
struct AlertDialogExample {
  build() {
    Stack({ alignContent: Alignment.Top }) {
      // Replace $r('app.media.bg') with the image resource file you use.
      Image($r('app.media.bg'))
      Column() {
        Button("AlertDialog")
          .margin(20)
          .onClick(() => {
            this.getUIContext().showAlertDialog({
              title: 'AlertDialog Title',
              message: 'AlertDialog Text',
              primaryButton: {
                value: 'OK',
                action: () => {
                  console.info('primaryButton');
                }
              },
              secondaryButton: {
                value: 'Cancel',
                action: () => {
                  console.info('secondaryButton');
                }
              },
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/fmHTxGqHThaVPfomYjfRNA/en-us_image_0000002568685625.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D26017FDD2C604702D6AD81D1B5CB853231F1545B4FD2713DB8A275D30FED45)

## Example 8: Customizing the Background Effect

This example demonstrates how to customize the background effect by setting **backgroundEffect** in [AlertDialogParam](#alertdialogparam).

The **backgroundEffect** attribute is added to **AlertDialogParam** since API version 19.

@Entry
@Component
struct AlertDialogExample {
  build() {
    Stack({ alignContent: Alignment.Top }) {
      // Replace $r('app.media.bg') with the image resource file you use.
      Image($r('app.media.bg'))
      Column() {
        Button("AlertDialog")
          .margin(20)
          .onClick(() => {
            this.getUIContext().showAlertDialog({
              title: 'AlertDialog Title',
              message: 'AlertDialog Text',
              primaryButton: {
                value: 'OK',
                action: () => {
                  console.info('primaryButton');
                }
              },
              secondaryButton: {
                value: 'Cancel',
                action: () => {
                  console.info('secondaryButton');
                }
              },
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/O4TUxgOvS3uLOCQJk73yxQ/en-us_image_0000002568765635.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94F9334205850905DF80A7F71BBC127967D8B0C849DBC5A0942AFD1C4D0B10B4)
