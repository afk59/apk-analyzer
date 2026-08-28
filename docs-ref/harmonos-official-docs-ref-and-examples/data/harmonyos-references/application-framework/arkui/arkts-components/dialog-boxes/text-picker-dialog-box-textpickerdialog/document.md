# Text Picker Dialog Box (TextPickerDialog)

A text picker dialog box is a dialog box that allows users to select text from the given range.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/JTVfkLUpTrycOzDJko9rQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C08AAB9395C717610C705BBBAD5394145E6755C9BD3B89B341334DF7B0DF5D4E)

-   This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The functionality of this module depends on UI context. This means that the APIs of this module cannot be used where [the UI context is ambiguous](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). For details, see [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   This module does not support dynamic updates for color mode (light or dark) changes. To apply a new color mode, close and reopen the dialog box.
    
-   The maximum number of rows that can be displayed varies by screen orientation: In portrait mode, the default number of rows is 5. In landscape mode, the number of rows depends on the system configuration. If no system configuration is set, the default is 3 rows. To check the specific system configuration value for landscape mode, use **$r('sys.float.ohos\_id\_picker\_show\_count\_landscape')**.
    

#### TextPickerDialog

#### \[h2\]show(deprecated)

static show(options?: TextPickerDialogOptions)

Shows a text picker in the given settings.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/dZXMgupAStiZakIiRinXig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC8391F37036F18666F757D1CB4A871B68167DB14A21BE0F3C5C652F302A91C4)

This API is supported since API version 8 and deprecated since API version 18. You are advised to use [showTextPickerDialog](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#showtextpickerdialog) instead. **showTextPickerDialog** can be called only after a [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) instance is obtained.

Since API version 10, you can use the [showTextPickerDialog](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#showtextpickerdialog) API in [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md), which ensures that the text picker dialog box is shown in the intended UI instance.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TextPickerDialogOptions](#textpickerdialogoptions) | No | Parameters of the text picker dialog box. |

#### TextPickerDialogOptions

Inherits from [TextPickerOptions](../../buttons-and-selections/textpicker/document.md#textpickeroptions).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| defaultPickerItemHeight | number | string | No | Yes | 
Height of the picker item. For the number type, the value range is \[0, +∞). For the string type, only numeric string values, for example, **"56"**, are supported.

Default value: 56 vp (selected) and 36 vp (unselected). The set value applies to both selected and unselected items.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| disappearTextStyle10+ | [PickerTextStyle](../../buttons-and-selections/picker-common-apis/document.md#pickertextstyle) | No | Yes | 

Text color, font size, and font weight of edge items (the second item above or below the selected item).

Default value:

{

color: '#ff182431',

font: {

size: '14fp',

weight: FontWeight.Regular

}

}

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| textStyle10+ | [PickerTextStyle](../../buttons-and-selections/picker-common-apis/document.md#pickertextstyle) | No | Yes | 

Text color, font size, and font weight of candidate items (the first item immediately above or below the selected item).

Default value:

{

color: '#ff182431',

font: {

size: '16fp',

weight: FontWeight.Regular

}

}

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| selectedTextStyle10+ | [PickerTextStyle](../../buttons-and-selections/picker-common-apis/document.md#pickertextstyle) | No | Yes | 

Text color, font size, and font weight of the selected item.

Default value:

{

color: '#ff007dff',

font: {

size: '20fp',

weight: FontWeight.Medium

}

}

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| acceptButtonStyle12+ | [PickerDialogButtonStyle](../../buttons-and-selections/picker-common-apis/document.md#pickerdialogbuttonstyle12) | No | Yes | 

Style of the accept button.

**NOTE**

1\. In **acceptButtonStyle** and **cancelButtonStyle**, at most one **primary** field can be set to **true**. If both are set to **true**, the **primary** field will remain at the default value of **false**.

2\. The default button height is 40 vp and remains fixed even in accessibility and large-font modes. In addition, even if the button style is set to [ROUNDED\_RECTANGLE](../../buttons-and-selections/button/document.md#buttontype), the displayed effect is still a capsule button ([Capsule](../../buttons-and-selections/button/document.md#buttontype)).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| cancelButtonStyle12+ | [PickerDialogButtonStyle](../../buttons-and-selections/picker-common-apis/document.md#pickerdialogbuttonstyle12) | No | Yes | 

Style of the cancel button.

**NOTE**

1\. In **acceptButtonStyle** and **cancelButtonStyle**, at most one **primary** field can be set to **true**. If both are set to **true**, the **primary** field will remain at the default value of **false**.

2\. The default button height is 40 vp and remains fixed even in accessibility and large-font modes. In addition, even if the button style is set to [ROUNDED\_RECTANGLE](../../buttons-and-selections/button/document.md#buttontype), the displayed effect is still a capsule button ([Capsule](../../buttons-and-selections/button/document.md#buttontype)).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| canLoop10+ | boolean | No | Yes | 

Whether to enable loop scrolling.

\- **true**: Enable loop scrolling.

\- **false**: Disable loop scrolling.

Default value: **true**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| alignment10+ | [DialogAlignment](../alert-dialog-box-alertdialog/document.md#dialogalignment) | No | Yes | 

Alignment mode of the dialog box in the vertical direction.

Default value: **DialogAlignment.Default**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| offset10+ | [Offset](../../common-definitions/basic-types/document.md#offset) | No | Yes | 

Offset of the dialog box based on the **alignment** settings.

Default value: **{ dx: 0 , dy: 0 }**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| maskRect10+ | [Rectangle](../alert-dialog-box-alertdialog/document.md#rectangle8) | No | Yes | 

Mask area of the dialog box. Events outside the mask area are transparently transmitted, and events within the mask area are not.

Default value: **{ x: 0, y: 0, width: '100%', height: '100%' }**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onAccept | (value: [TextPickerResult](#textpickerresult)) => void | No | Yes | 

Triggered when the OK button in the dialog box is clicked.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onCancel | () => void | No | Yes | 

Triggered when the Cancel button in the dialog box is clicked.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onChange | (value: [TextPickerResult](#textpickerresult)) => void | No | Yes | 

Triggered when the text picker in the dialog box snaps to the selected item.

This callback is triggered only after the scroll animation completes. To obtain real-time index changes, use **onEnterSelectedArea** instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onScrollStop14+ | [Callback](../../common-definitions/basic-types/document.md#callback12)<[TextPickerResult](#textpickerresult)\> | No | Yes | 

Triggered when the scrolling in the text picker of the dialog box stops.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| backgroundColor11+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Backplane color of the dialog box.

Default value: **Color.Transparent**

**NOTE**

When **backgroundColor** is set to a non-transparent color, **backgroundBlurStyle** must be set to **BlurStyle.NONE**; otherwise, the color display may not meet the expected effect.

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

Options for customizing the background blur style.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| backgroundEffect19+ | [BackgroundEffectOptions](../../universal-attributes/basic-attributes/background/document.md#backgroundeffectoptions11) | No | Yes | 

Options for customizing the background effect.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| onDidAppear12+ | () => void | No | Yes | 

Event callback after the dialog box appears.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onAccept/onCancel/onChange/onScrollStop) > onWillDisappear > onDidDisappear.

2\. You can set the callback event for changing the dialog box display effect in **onDidAppear**. The settings take effect next time the dialog box appears.

3\. If the user closes the dialog box immediately after it appears, **onWillDisappear** is invoked before **onDidAppear**.

4\. If the dialog box is closed before its entrance animation is finished, this callback is not invoked.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onDidDisappear12+ | () => void | No | Yes | 

Event callback after the dialog box disappears.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onAccept/onCancel/onChange/onScrollStop) > onWillDisappear > onDidDisappear.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onWillAppear12+ | () => void | No | Yes | 

Event callback when the dialog box is about to appear.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onAccept/onCancel/onChange/onScrollStop) > onWillDisappear > onDidDisappear.

2\. You can set the callback event for changing the dialog box display effect in **onWillAppear**. The settings take effect next time the dialog box appears.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onWillDisappear12+ | () => void | No | Yes | 

Event callback when the dialog box is about to disappear.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onAccept/onCancel/onChange/onScrollStop) > onWillDisappear > onDidDisappear.

2\. If the user closes the dialog box immediately after it appears, **onWillDisappear** is invoked before **onDidAppear**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| shadow12+ | [ShadowOptions](../../universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../universal-attributes/visual-effects/image-effect/document.md#shadowstyle10) | No | Yes | 

Shadow of the dialog box.

Default value on 2-in-1 devices: **ShadowStyle.OUTER\_FLOATING\_MD** when the dialog box is focused and **ShadowStyle.OUTER\_FLOATING\_SM** otherwise

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| enableHoverMode14+ | boolean | No | Yes | 

Whether to respond when the device is in semi-folded mode.

\- **true**: Respond when the device is in semi-folded mode.

\- **false**: Do not respond when the device is in semi-folded mode.

Default value: **false**.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| hoverModeArea14+ | [HoverModeAreaType](../../universal-attributes/transition/sheet-transition/document.md#hovermodeareatype14) | No | Yes | 

Display area of the dialog box when the device is in semi-folded mode.

Default value: **HoverModeAreaType.BOTTOM\_SCREEN**

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| disableTextStyleAnimation15+ | boolean | No | Yes | 

Whether to disable the animation effect of text style changes during scrolling.

\- **true**: Disable the animation effect of text style changes.

\- **false**: Do not disable the animation effect of text style changes.

Default value: **false**.

**NOTE**

When this API is used with **true**, there are no text style changes, including the font size, weight, and color, during scrolling, and all text is displayed in the style set by **defaultTextStyle**. If **defaultTextStyle** is not set, the default style of the [Text](../../text-and-input/text/document.md) component is used.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| defaultTextStyle15+ | [TextPickerTextStyle](../../buttons-and-selections/textpicker/document.md#textpickertextstyle15) | No | Yes | 

Style of the text items when the text style change animation during the scrolling process is disabled. It is effective only when **disableTextStyleAnimation** is **true**.

Default value: same as the default value of the [Text](../../text-and-input/text/document.md) component

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| onEnterSelectedArea18+ | Callback<[TextPickerResult](#textpickerresult)\> | No | Yes | 

Represents the callback triggered during the scrolling of the text picker when an item enters the divider area. Compared to the **onChange** event, this event is triggered earlier, specifically when the scroll distance of the current column exceeds half the height of the selected item, which indicates that the item has entered the divider area.

**NOTE**

In scenarios where the picker contains linked columns, the use of this callback is not recommended. The reason is that it identifies nodes where items enter the divider area during scrolling. However, items that change in response to the scrolling do not themselves scroll. As a result, the callback's return values will only reflect changes for the currently scrolling column, while other non-scrolling columns will remain unchanged.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| enableHapticFeedback18+ | boolean | No | Yes | 

Whether to enable haptic feedback.

\- **true**: Enable haptic feedback.

\- **false**: Disable haptic feedback.

Default value: **true**.

**Atomic service API**: This API can be used in atomic services since API version 18.

**NOTE**

1\. Whether this parameter takes effect after being set to **true** depends on hardware support.

2\. To enable haptic feedback, you must declare the following permission under **requestPermissions** in **module** in **src/main/module.json5** of the project.

"requestPermissions": \[{"name": "ohos.permission.VIBRATE"}\]

 |
| selectedBackgroundStyle20+ | [PickerBackgroundStyle](../../buttons-and-selections/textpicker/document.md#pickerbackgroundstyle20) | No | Yes | 

Background color of the selected item.

Default value:

{

color: $r('sys.color.comp\_background\_tertiary'),

borderRadius: $r('sys.float.corner\_radius\_level12')

}

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### TextPickerDialogOptionsExt20+

Inherits from [TextPickerOptions](../../buttons-and-selections/textpicker/document.md#textpickeroptions).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| defaultPickerItemHeight | number | string | No | Yes | 
Height of the picker item. For the number type, the value range is \[0, +∞). For the string type, only numeric string values, for example, **"56"**, are supported.

Default value: 56 vp (selected) and 36 vp (unselected). The set value applies to both selected and unselected items.

 |
| acceptButtonStyle | [PickerDialogButtonStyle](../../buttons-and-selections/picker-common-apis/document.md#pickerdialogbuttonstyle12) | No | Yes | 

Style of the accept button.

**NOTE**

1\. In **acceptButtonStyle** and **cancelButtonStyle**, at most one **primary** field can be set to **true**. If both are set to **true**, the **primary** field will remain at the default value of **false**.

2\. The default button height is 40 vp and remains fixed even in accessibility and large-font modes. In addition, even if the button style is set to [ROUNDED\_RECTANGLE](../../buttons-and-selections/button/document.md#buttontype), the displayed effect is still a capsule button ([Capsule](../../buttons-and-selections/button/document.md#buttontype)).

 |
| cancelButtonStyle | [PickerDialogButtonStyle](../../buttons-and-selections/picker-common-apis/document.md#pickerdialogbuttonstyle12) | No | Yes | 

Style of the cancel button.

**NOTE**

1\. In **acceptButtonStyle** and **cancelButtonStyle**, at most one **primary** field can be set to **true**. If both are set to **true**, the **primary** field will remain at the default value of **false**.

2\. The default button height is 40 vp and remains fixed even in accessibility and large-font modes. In addition, even if the button style is set to [ROUNDED\_RECTANGLE](../../buttons-and-selections/button/document.md#buttontype), the displayed effect is still a capsule button ([Capsule](../../buttons-and-selections/button/document.md#buttontype)).

 |
| canLoop | boolean | No | Yes | 

Whether to enable loop scrolling.

\- **true**: Enable loop scrolling.

\- **false**: Disable loop scrolling.

Default value: **true**.

 |
| alignment | [DialogAlignment](../alert-dialog-box-alertdialog/document.md#dialogalignment) | No | Yes | 

Alignment mode of the dialog box in the vertical direction.

Default value: **DialogAlignment.Default**

 |
| offset | [Offset](../../common-definitions/basic-types/document.md#offset) | No | Yes | 

Offset of the dialog box based on the **alignment** settings.

Default value: **{ dx: 0 , dy: 0 }**

 |
| maskRect | [Rectangle](../alert-dialog-box-alertdialog/document.md#rectangle8) | No | Yes | 

Mask area of the dialog box. Events outside the mask area are transparently transmitted, and events within the mask area are not.

Default value: **{ x: 0, y: 0, width: '100%', height: '100%' }**

 |
| onAccept | [Callback](../../common-definitions/basic-types/document.md#callback12)<[TextPickerResult](#textpickerresult)\> | No | Yes | Triggered when the OK button in the dialog box is clicked. |
| onCancel | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | Triggered when the Cancel button in the dialog box is clicked. |
| onChange | [Callback](../../common-definitions/basic-types/document.md#callback12)<[TextPickerResult](#textpickerresult)\> | No | Yes | 

Triggered when the text picker in the dialog box snaps to the selected item.

This callback is triggered only after the scroll animation completes. To obtain real-time index changes, use **onEnterSelectedArea** instead.

 |
| onScrollStop | [Callback](../../common-definitions/basic-types/document.md#callback12)<[TextPickerResult](#textpickerresult)\> | No | Yes | Triggered when the scrolling in the text picker of the dialog box stops. |
| backgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Backplane color of the dialog box.

Default value: **Color.Transparent**

**NOTE**

When **backgroundColor** is set to a non-transparent color, **backgroundBlurStyle** must be set to **BlurStyle.NONE**; otherwise, the color display may not meet the expected effect.

 |
| backgroundBlurStyle | [BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | Yes | 

Background blur style of the dialog box.

Default value: **BlurStyle.COMPONENT\_ULTRA\_THICK**

**NOTE**

Setting this parameter to **BlurStyle.NONE** disables the background blur. When **backgroundBlurStyle** is set to a value other than **NONE**, do not set **backgroundColor**. If you do, the color display may not produce the expected visual effect.

 |
| backgroundBlurStyleOptions | [BackgroundBlurStyleOptions](../../universal-attributes/basic-attributes/background/document.md#backgroundblurstyleoptions10) | No | Yes | 

Options for customizing the background blur style.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| backgroundEffect | [BackgroundEffectOptions](../../universal-attributes/basic-attributes/background/document.md#backgroundeffectoptions11) | No | Yes | Options for customizing the background effect. |
| onDidAppear | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 

Event callback after the dialog box appears.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onAccept/onCancel/onChange/onScrollStop) > onWillDisappear > onDidDisappear.

2\. You can set the callback event for changing the dialog box display effect in **onDidAppear**. The settings take effect next time the dialog box appears.

3\. If the user closes the dialog box immediately after it appears, **onWillDisappear** is invoked before **onDidAppear**.

4\. If the dialog box is closed before its entrance animation is finished, this callback is not invoked.

 |
| onDidDisappear | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 

Event callback after the dialog box disappears.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onAccept/onCancel/onChange/onScrollStop) > onWillDisappear > onDidDisappear.

 |
| onWillAppear | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 

Event callback when the dialog box is about to appear.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onAccept/onCancel/onChange/onScrollStop) > onWillDisappear > onDidDisappear.

2\. You can set the callback event for changing the dialog box display effect in **onWillAppear**. The settings take effect next time the dialog box appears.

 |
| onWillDisappear | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 

Event callback when the dialog box is about to disappear.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onAccept/onCancel/onChange/onScrollStop) > onWillDisappear > onDidDisappear.

2\. If the user closes the dialog box immediately after it appears, **onWillDisappear** is invoked before **onDidAppear**.

 |
| shadow | [ShadowOptions](../../universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../universal-attributes/visual-effects/image-effect/document.md#shadowstyle10) | No | Yes | 

Shadow of the dialog box.

Default value on 2-in-1 devices: **ShadowStyle.OUTER\_FLOATING\_MD** when the dialog box is focused and **ShadowStyle.OUTER\_FLOATING\_SM** otherwise

 |
| enableHoverMode | boolean | No | Yes | 

Whether to respond when the device is in semi-folded mode.

\- **true**: Respond when the device is in semi-folded mode.

\- **false**: Do not respond when the device is in semi-folded mode.

Default value: **false**

 |
| hoverModeArea | [HoverModeAreaType](../../universal-attributes/transition/sheet-transition/document.md#hovermodeareatype14) | No | Yes | 

Display area of the dialog box when the device is in semi-folded mode.

Default value: **HoverModeAreaType.BOTTOM\_SCREEN**

 |
| disableTextStyleAnimation | boolean | No | Yes | 

Whether to disable the animation effect of text style changes during scrolling.

\- **true**: Disable the animation effect of text style changes.

\- **false**: Do not disable the animation effect of text style changes.

Default value: **false**.

**NOTE**

When this API is used with **true**, there are no text style changes, including the font size, weight, and color, during scrolling, and all text is displayed in the style set by **defaultTextStyle**. If **defaultTextStyle** is not set, the default style of the [Text](../../text-and-input/text/document.md) component is used.

 |
| defaultTextStyle | [TextPickerTextStyle](../../buttons-and-selections/textpicker/document.md#textpickertextstyle15) | No | Yes | 

Style of the text items when the text style change animation during the scrolling process is disabled. It is effective only when **disableTextStyleAnimation** is **true**.

Default value: same as the default value of the [Text](../../text-and-input/text/document.md) component

 |
| onEnterSelectedArea | [Callback](../../common-definitions/basic-types/document.md#callback12)<[TextPickerResult](#textpickerresult)\> | No | Yes | 

Represents the callback triggered during the scrolling of the text picker when an item enters the divider area. Compared to the **onChange** event, this event is triggered earlier, specifically when the scroll distance of the current column exceeds half the height of the selected item, which indicates that the item has entered the divider area.

**NOTE**

In scenarios where the picker contains linked columns, the use of this callback is not recommended. The reason is that it identifies nodes where items enter the divider area during scrolling. However, items that change in response to the scrolling do not themselves scroll. As a result, the callback's return values will only reflect changes for the currently scrolling column, while other non-scrolling columns will remain unchanged.

 |
| enableHapticFeedback | boolean | No | Yes | 

Whether to enable haptic feedback.

\- **true**: Enable haptic feedback.

\- **false**: Disable haptic feedback.

Default value: **true**.

**NOTE**

1\. Whether this parameter takes effect after being set to **true** depends on hardware support.

2\. To enable haptic feedback, you must declare the following permission under **requestPermissions** in **module** in **src/main/module.json5** of the project.

"requestPermissions": \[{"name": "ohos.permission.VIBRATE"}\]

 |
| selectedBackgroundStyle | [PickerBackgroundStyle](../../buttons-and-selections/textpicker/document.md#pickerbackgroundstyle20) | No | Yes | 

Background color of the selected item.

Default value:

{

color: $r('sys.color.comp\_background\_tertiary'),

borderRadius: $r('sys.float.corner\_radius\_level12')

}

 |
| disappearTextStyle | [TextPickerTextStyle](../../buttons-and-selections/textpicker/document.md#textpickertextstyle15) | No | Yes | 

Style of edge items (the second item above or below the selected item), covering the following: text color, font size, font weight, maximum font size, minimum font size, text overflow mode.

Default value:

{

color: '#ff182431',

font: {

size: '14fp',

weight: FontWeight.Regular

},

minFontSize: 0,

maxFontSize: 0,

overflow: TextOverflow.CLIP

}

 |
| textStyle | [TextPickerTextStyle](../../buttons-and-selections/textpicker/document.md#textpickertextstyle15) | No | Yes | 

Style of candidate items (the first item immediately above or below the selected item), covering the following: text color, font size, font weight, maximum font size, minimum font size, text overflow mode.

Default value:

{

color: '#ff182431',

font: {

size: '16fp',

weight: FontWeight.Regular

},

minFontSize: 0,

maxFontSize: 0,

overflow: TextOverflow.CLIP

}

 |
| selectedTextStyle | [TextPickerTextStyle](../../buttons-and-selections/textpicker/document.md#textpickertextstyle15) | No | Yes | 

Style of the selected item, covering the following: text color, font size, font weight, maximum font size, minimum font size, text overflow mode.

Default value:

{

color: '#ff007dff',

font: {

size: '20fp',

weight: FontWeight.Medium

},

minFontSize: 0,

maxFontSize: 0,

overflow: TextOverflow.CLIP

}

 |

#### TextPickerResult

Represents the selection result of a **TextPicker** component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | string | string \[\]10+ | No | No | 
Text of the selected item.

**NOTE**

When the picker contains text only or both text and imagery, **value** indicates the text value of the selected item. (For a multi-column picker, **value** is of the array type.)

For an image list, **value** is empty.

The value cannot contain the following escape character: \\

 |
| index | number | number \[\]10+ | No | No | Index of the selected item in the range. The index is zero-based. (For a multi-column picker, **index** is of the array type.) |

#### Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/5nhZsEhoSXaTf7Pr5h86aA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=409F4426CB0CAE2A2C1DE2FB3C611A63DE61EE0712C8AEE6A841A092E9A42A94)

For clarity in UI execution context, you are advised to use the [showTextPickerDialog](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#showtextpickerdialog) API in [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md).

## Example 1: Displaying a Text Picker Dialog Box

This example demonstrates how to display a text picker dialog box when a button is touched.

// xxx.ets
@Entry
@Component
struct TextPickerDialogExample {
  private select: number | number\[\] = 0;
  private fruits: string\[\] = \['apple1', 'orange2', 'peach3', 'grape4', 'banana5'\];
  @State selectedValue: string = '';

  build() {
    Row() {
      Column() {
        Button('TextPickerDialog:' + this.selectedValue)
          .margin(20)
          .onClick(() => {
            this.getUIContext().showTextPickerDialog({
              range: this.fruits,
              selected: this.select,
              value: this.selectedValue,
              defaultPickerItemHeight: 40,
              onAccept: (value: TextPickerResult) => {
                // Set select to the index of the item selected when the OK button is touched. In this way, when the text picker dialog box is displayed again, the selected item is the one last confirmed.
                this.select = value.index;
                console.info(this.select + '');
                // After OK is clicked, the selected item is displayed on the page.
                this.selectedValue = value.value as string;
                console.info('TextPickerDialog:onAccept()' + JSON.stringify(value));
              },
              onCancel: () => {
                console.info('TextPickerDialog:onCancel()');
              },
              onChange: (value: TextPickerResult) => {
                console.info('TextPickerDialog:onChange()' + JSON.stringify(value));
              },
              onScrollStop: (value: TextPickerResult) => {
                console.info('TextPickerDialog:onScrollStop()' + JSON.stringify(value));
              },
              onDidAppear: () => {
                console.info('TextPickerDialog:onDidAppear()');
              },
              onDidDisappear: () => {
                console.info('TextPickerDialog:onDidDisappear()');
              },
              onWillAppear: () => {
                console.info('TextPickerDialog:onWillAppear()');
              },
              onWillDisappear: () => {
                console.info('TextPickerDialog:onWillDisappear()');
              }
            });
          })
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/xf-Z7FJATCWtAdcQxiaBDw/en-us_image_0000002568765657.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CBF68923865D159C6AC65B9F9108A7BC76E9EF8FD78DAE8E85B4344D7A12C09)

## Example 2: Customizing the Style

In this example, **disappearTextStyle**, **textStyle**, **selectedTextStyle**, **acceptButtonStyle**, and **cancelButtonStyle** are configured to customize the text and button style.

// xxx.ets
@Entry
@Component
struct TextPickerDialogExample {
  private select: number | number\[\] = 0;
  private fruits: string\[\] = \['apple1', 'orange2', 'peach3', 'grape4', 'banana5'\];
  @State selectedValue: string = '';

  build() {
    Row() {
      Column() {
        Button('TextPickerDialog:' + this.selectedValue)
          .margin(20)
          .onClick(() => {
            this.getUIContext().showTextPickerDialog({
              range: this.fruits,
              selected: this.select,
              disappearTextStyle: { color: '#297bec', font: { size: 15, weight: FontWeight.Lighter } },
              textStyle: { color: Color.Black, font: { size: 20, weight: FontWeight.Normal } },
              selectedTextStyle: { color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } },
              acceptButtonStyle: {
                type: ButtonType.Normal,
                style: ButtonStyleMode.NORMAL,
                role: ButtonRole.NORMAL,
                fontColor: 'rgb(81, 81, 216)',
                fontSize: '26fp',
                fontWeight: FontWeight.Bolder,
                fontStyle: FontStyle.Normal,
                fontFamily: 'sans-serif',
                backgroundColor: '#A6ACAF',
                borderRadius: 20
              },
              cancelButtonStyle: {
                type: ButtonType.Normal,
                style: ButtonStyleMode.NORMAL,
                role: ButtonRole.NORMAL,
                fontColor: Color.Blue,
                fontSize: '16fp',
                fontWeight: FontWeight.Normal,
                fontStyle: FontStyle.Italic,
                fontFamily: 'sans-serif',
                backgroundColor: '#50182431',
                borderRadius: 10
              },
              onAccept: (value: TextPickerResult) => {
                // Set select to the index of the item selected when the OK button is touched. In this way, when the text picker dialog box is displayed again, the selected item is the one last confirmed.
                this.select = value.index;
                console.info(this.select + '');
                // After OK is clicked, the selected item is displayed on the page.
                this.selectedValue = value.value as string;
                console.info('TextPickerDialog:onAccept()' + JSON.stringify(value));
              },
              onCancel: () => {
                console.info('TextPickerDialog:onCancel()');
              },
              onChange: (value: TextPickerResult) => {
                console.info('TextPickerDialog:onChange()' + JSON.stringify(value));
              },
              onScrollStop: (value: TextPickerResult) => {
                console.info('TextPickerDialog:onScrollStop()' + JSON.stringify(value));
              },
              onDidAppear: () => {
                console.info('TextPickerDialog:onDidAppear()');
              },
              onDidDisappear: () => {
                console.info('TextPickerDialog:onDidDisappear()');
              },
              onWillAppear: () => {
                console.info('TextPickerDialog:onWillAppear()');
              },
              onWillDisappear: () => {
                console.info('TextPickerDialog:onWillDisappear()');
              }
            });
          })
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/Hn1eKQXrQDe-rFZqSpKb-A/en-us_image_0000002537765932.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39CF1752CFF5F4397C3AC26BDB902CDD37B2E1E999CBED42F80DB5A4E306A34B)

## Example 3: Configuring a Dialog Box in the Hover State

This example demonstrates how to set the layout area of a dialog box when the device is in semi-folded mode.

@Entry
@Component
struct TextPickerDialogExample {
  private select: number | number\[\] = 0;
  private fruits: string\[\] = \['apple1', 'orange2', 'peach3', 'grape4', 'banana5'\];
  @State selectedValue: string = '';

  build() {
    Row() {
      Column() {
        Button('TextPickerDialog:' + this.selectedValue)
          .margin(20)
          .onClick(() => {
            this.getUIContext().showTextPickerDialog({
              range: this.fruits,
              selected: this.select,
              disappearTextStyle: { color: Color.Red, font: { size: 15, weight: FontWeight.Lighter }},
              textStyle: { color: Color.Black, font: { size: 20, weight: FontWeight.Normal }},
              selectedTextStyle: { color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder }},
              onAccept: (value: TextPickerResult) => {
                // Set select to the index of the item selected when the OK button is touched. In this way, when the text picker dialog box is displayed again, the selected item is the one last confirmed.
                this.select = value.index;
                console.info(this.select + '');
                // After OK is clicked, the selected item is displayed on the page.
                this.selectedValue = value.value as string;
                console.info('TextPickerDialog:onAccept()' + JSON.stringify(value));
              },
              onCancel: () => {
                console.info('TextPickerDialog:onCancel()');
              },
              onChange: (value: TextPickerResult) => {
                console.info('TextPickerDialog:onChange()' + JSON.stringify(value));
              },
              onScrollStop: (value: TextPickerResult) => {
                console.info('TextPickerDialog:onScrollStop()' + JSON.stringify(value));
              },
              onDidAppear: () => {
                console.info('TextPickerDialog:onDidAppear()');
              },
              onDidDisappear: () => {
                console.info('TextPickerDialog:onDidDisappear()');
              },
              onWillAppear: () => {
                console.info('TextPickerDialog:onWillAppear()');
              },
              onWillDisappear: () => {
                console.info('TextPickerDialog:onWillDisappear()');
              },
              enableHoverMode: true,
              hoverModeArea: HoverModeAreaType.TOP\_SCREEN
            });
          })
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/k5g0zkRGStGOvvzQGOh7NQ/en-us_image_0000002537925872.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EBDF669848E63F9465E55F70A5C7696E41BD9A3F73CB392F8D3015812FF47181)

## Example 4: Setting the Dialog Box Position

This example demonstrates how to set the position of a dialog box using **alignment** and **offset**.

// xxx.ets
@Entry
@Component
struct TextPickerDialogExample {
  private select: number | number\[\] = 0;
  private fruits: string\[\] = \['apple1', 'orange2', 'peach3', 'grape4', 'banana5'\];
  @State selectedValue: string = '';

  build() {
    Row() {
      Column() {
        Button('TextPickerDialog:' + this.selectedValue)
          .margin(20)
          .onClick(() => {
            this.getUIContext().showTextPickerDialog({
              range: this.fruits,
              selected: this.select,
              alignment: DialogAlignment.Center,
              offset: { dx: 20, dy: 0 },
              onAccept: (value: TextPickerResult) => {
                // Set select to the index of the item selected when the OK button is touched. In this way, when the text picker dialog box is displayed again, the selected item is the one last confirmed.
                this.select = value.index;
                console.info(this.select + '');
                // After OK is clicked, the selected item is displayed on the page.
                this.selectedValue = value.value as string;
                console.info('TextPickerDialog:onAccept()' + JSON.stringify(value));
              }
            });
          })
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/PdSXMoWHTkWey4cOzEZi4g/en-us_image_0000002568685649.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E89DC896273023DFD65651101B4A836AAE1469C9373FFB26EDC1C1A99758D142)

## Example 5: Setting the Mask Area

This example demonstrates how to set the mask area using **maskRect**.

// xxx.ets
@Entry
@Component
struct TextPickerDialogExample {
  private select: number | number\[\] = 0;
  private fruits: string\[\] = \['apple1', 'orange2', 'peach3', 'grape4', 'banana5'\];
  @State selectedValue: string = '';

  build() {
    Row() {
      Column() {
        Button('TextPickerDialog:' + this.selectedValue)
          .margin(20)
          .onClick(() => {
            this.getUIContext().showTextPickerDialog({
              range: this.fruits,
              selected: this.select,
              maskRect: {
                x: 30,
                y: 60,
                width: '100%',
                height: '60%'
              },
              onAccept: (value: TextPickerResult) => {
                // Set select to the index of the item selected when the OK button is touched. In this way, when the text picker dialog box is displayed again, the selected item is the one last confirmed.
                this.select = value.index;
                console.info(this.select + '');
                // After OK is clicked, the selected item is displayed on the page.
                this.selectedValue = value.value as string;
                console.info('TextPickerDialog:onAccept()' + JSON.stringify(value));
              }
            });
          })
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/BscZrvakRSCQM0pQA9p4gg/en-us_image_0000002568765659.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AFC2EB0D441EA3D64546C2A20B85871A084F9F18DF9867C720B4A2707B654AC4)

## Example 6: Setting the Background

This example demonstrates how to set the dialog box background using **backgroundColor**, **backgroundBlurStyle**, and **shadow**.

// xxx.ets
@Entry
@Component
struct TextPickerDialogExample {
  private select: number | number\[\] = 0;
  private fruits: string\[\] = \['apple1', 'orange2', 'peach3', 'grape4', 'banana5'\];
  @State selectedValue: string = '';

  build() {
    Row() {
      Column() {
        Button('TextPickerDialog:' + this.selectedValue)
          .margin(20)
          .onClick(() => {
            this.getUIContext().showTextPickerDialog({
              range: this.fruits,
              selected: this.select,
              backgroundColor: 'rgb(204, 226, 251)',
              backgroundBlurStyle: BlurStyle.NONE,
              shadow: ShadowStyle.OUTER\_FLOATING\_SM,
              onAccept: (value: TextPickerResult) => {
                // Set select to the index of the item selected when the OK button is touched. In this way, when the text picker dialog box is displayed again, the selected item is the one last confirmed.
                this.select = value.index;
                console.info(this.select + '');
                // After OK is clicked, the selected item is displayed on the page.
                this.selectedValue = value.value as string;
                console.info('TextPickerDialog:onAccept()' + JSON.stringify(value));
              }
            });
          })
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/FH9UDKxMR7GvGECoH7tE4w/en-us_image_0000002537765934.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F45305450D29986CF287E061CC567DC94FEA4F729EB7D49C25A2FDD406F8E7C8)

## Example 7: Setting Cyclic Scrolling

This example demonstrates how to set whether to enable cyclic scrolling using **canLoop**.

// xxx.ets
@Entry
@Component
struct TextPickerDialogExample {
  private select: number | number\[\] = 0;
  private fruits: string\[\] = \['apple1', 'orange2', 'peach3', 'grape4', 'banana5'\];
  @State selectedValue: string = '';

  build() {
    Row() {
      Column() {
        Button('TextPickerDialog:' + this.selectedValue)
          .margin(20)
          .onClick(() => {
            this.getUIContext().showTextPickerDialog({
              range: this.fruits,
              selected: this.select,
              value: this.selectedValue,
              canLoop: false,
              onAccept: (value: TextPickerResult) => {
                // Set select to the index of the item selected when the OK button is touched. In this way, when the text picker dialog box is displayed again, the selected item is the one last confirmed.
                this.select = value.index;
                console.info(this.select + '');
                // After OK is clicked, the selected item is displayed on the page.
                this.selectedValue = value.value as string;
                console.info('TextPickerDialog:onAccept()' + JSON.stringify(value));
              }
            });
          })
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/k9kKEyk2ThGjCNW0rmE4Rg/en-us_image_0000002537925874.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F61064264210B01A78AAA16E4504FA4AF81F7E2546C8DD47E669DB14D27763B3)

## Example 8: Setting the Background Style of the Selected Item

This example shows how to set the background style of the selected item by configuring **selectedBackgroundStyle**.

Since API version 20, the **selectedBackgroundStyle** attribute is added for [TextPickerDialogOptions](#textpickerdialogoptions).

// xxx.ets
@Entry
@Component
struct TextPickerExample {
  private showText1: string \[\] = \['Text1', 'Text1', 'Text1', 'Text1'\]
  build() {
    Column() {
      Row() {
        Button('TextPickerDialog')
          .margin(20)
          .onClick(() => {
            this.getUIContext().showTextPickerDialog({
              range: this.showText1,
              selectedBackgroundStyle: {
                borderRadius: {
                  topLeft:15,
                  topRight:15,
                  bottomLeft:15,
                  bottomRight:15
                },
                color: 'FFC3C3C3'
              }
            })
          })
      }
    }.height('100%')
  }
}

## Example 9: Customizing the Background Blur Effect

This example demonstrates how to customize the background blur effect by configuring [backgroundBlurStyleOptions](#textpickerdialogoptions). This functionality is supported since API version 19.

@Entry
@Component
struct TextPickerExample {
  private showText1: string \[\] = \['Text1', 'Text1', 'Text1', 'Text1'\]

  build() {
    Stack({ alignContent: Alignment.Top }) {
      // Replace $r('app.media.bg') with the image resource file you use.
      Image($r('app.media.bg'))
      Column() {
        Button('TextPickerDialog')
          .margin(20)
          .onClick(() => {
            this.getUIContext().showTextPickerDialog({
              range: this.showText1,
              backgroundColor: undefined,
              backgroundBlurStyle: BlurStyle.Thin,
              backgroundBlurStyleOptions: {
                colorMode: ThemeColorMode.LIGHT,
                adaptiveColor: AdaptiveColor.AVERAGE,
                scale: 1,
                blurOptions: { grayscale: \[20, 20\] },
              },
            })
          })
      }.width('100%')
    }
  }
}

## Example 10: Customizing the Background Effect

This example demonstrates how to customize the background effect by configuring [backgroundEffect](#textpickerdialogoptions). This functionality is supported since API version 19.

@Entry
@Component
struct TextPickerExample {
  private showText1: string \[\] = \['Text1', 'Text1', 'Text1', 'Text1'\]

  build() {
    Stack({ alignContent: Alignment.Top }) {
      // Replace $r('app.media.bg') with the image resource file you use.
      Image($r('app.media.bg'))
      Column() {
        Button('TextPickerDialog')
          .margin(20)
          .onClick(() => {
            this.getUIContext().showTextPickerDialog({
              range: this.showText1,
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
          })
      }.width('100%')
    }
  }
}
