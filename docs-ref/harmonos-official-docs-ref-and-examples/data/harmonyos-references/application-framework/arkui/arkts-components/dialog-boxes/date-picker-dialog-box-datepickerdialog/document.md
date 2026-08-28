# Date Picker Dialog Box (DatePickerDialog)

A date picker dialog box is a dialog box that allows users to select a date from the given range.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/TTex_S2NTvya8qKd4wGMNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37EEFD512A962D0AF83BB33E83672697AB9F1085DFF955128302EA8A70CBCB61)

-   This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The functionality of this module depends on UI context. This means that the APIs of this module cannot be used where [the UI context is ambiguous](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). For details, see [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   This module does not support dynamic updates for color mode (light or dark) changes. To apply a new color mode, close and reopen the dialog box.
    
-   The maximum number of rows that can be displayed varies by screen orientation: In portrait mode, the default number of rows is 5. In landscape mode, the number of rows depends on the system configuration. If no system configuration is set, the default is 3 rows. To check the specific system configuration value for the landscape mode, use **$r('sys.float.ohos\_id\_picker\_show\_count\_landscape')**.
    

#### DatePickerDialog

#### \[h2\]show(deprecated)

static show(options?: DatePickerDialogOptions)

Shows a date picker dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/Bh1UPH50TeSr3xPND9G1Ig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5118CFA5A6095847BD4493B0C2CB2C95BEB83771A6A28C1B788ADDDDBA292A9D)

This API is supported since API version 8 and deprecated since API version 18. You are advised to use [showDatePickerDialog](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#showdatepickerdialog) instead. **showDatePickerDialog** can be called only after a [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) instance is obtained.

Since API version 10, you can use the [showDatePickerDialog](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#showdatepickerdialog) API in [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md), which ensures that the date picker dialog box is shown in the intended UI instance.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [DatePickerDialogOptions](#datepickerdialogoptions) | No | Parameters of the date picker dialog box. |

#### DatePickerDialogOptions

Defines the configuration options of the date picker dialog box.

Inherited from [DatePickerOptions](../../buttons-and-selections/datepicker/document.md#datepickeroptions).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| lunar | boolean | No | Yes | 
Whether to display dates in lunar calendar format.

\- **true**: Display dates in lunar calendar format.

\- **false**: Do not display dates in lunar calendar format.

Default value: **false**

**NOTE**

This attribute takes effect only in Simplified Chinese and Traditional Chinese locales; it has no effect in other locales.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| showTime10+ | boolean | No | Yes | 

Whether to display the time picker in the dialog box.

\- **true**: Display the time picker.

\- **false**: Do not display the time picker.

Default value: **false**

**NOTE**

1\. When **showTime** is **true**, clicking the date in the dialog box header toggles between date-only and date+time views.

2\. When **showTime** is **true**, the **mode** parameter is ignored, meaning the date picker always shows year, month, and day columns.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| useMilitaryTime10+ | boolean | No | Yes | 

Whether the time picker in the dialog box is in 24-hour format. This parameter has effect only when **showTime** is **true**.

\- **true**: 24-hour format.

\- **false**: 12-hour format.

Default value: **false**

**NOTE**

When 12-hour format is used in the time picker, the AM/PM indicator does not automatically update when the hour value changes.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| lunarSwitch10+ | boolean | No | Yes | 

Whether to display the lunar calendar switch.

\- **true**: Display the lunar calendar switch.

\- **false**: Do not display the lunar calendar switch.

Default value: **false**

**NOTE**

After being enabled, this attribute takes effect only in Simplified Chinese and Traditional Chinese; it has no effect in other locales. Therefore, you are advised to set this attribute to **false** in other locales.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| lunarSwitchStyle14+ | [LunarSwitchStyle](#lunarswitchstyle14) | No | Yes | 

Style of the lunar calendar switch.

Default value: {

selectedColor: $r('sys.color.ohos\_id\_color\_text\_primary\_actived'),

unselectedColor: $r('sys.color.ohos\_id\_color\_switch\_outline\_off'),

strokeColor: Color.White

}

**Atomic service API**: This API can be used in atomic services since API version 14.

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
| onAccept(deprecated) | (value: [DatePickerResult](../../buttons-and-selections/datepicker/document.md#datepickerresult)) => void | No | Yes | 

Callback invoked when the OK button in the dialog box is clicked.

**NOTE**

This API is supported since API version 8 and deprecated since API version 10. You are advised to use **onDateAccept** instead.

 |
| onCancel | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 

Callback invoked when the Cancel button in the dialog box is clicked.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onChange(deprecated) | (value: [DatePickerResult](../../buttons-and-selections/datepicker/document.md#datepickerresult)) => void | No | Yes | 

Callback invoked when the selected item in the picker changes.

**NOTE**

This API is supported since API version 8 and deprecated since API version 10. You are advised to use **onDateChange** instead.

 |
| onDateAccept10+ | [Callback](../../common-definitions/basic-types/document.md#callback12)<Date> | No | Yes | 

Callback invoked when the OK button in the dialog box is clicked.

**NOTE**

When **showTime** is set to **true**, the hour and minute in the value returned by the callback are the hour and minute selected in the picker. Otherwise, the hour and minute are the hour and minute of the system time.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onDateChange10+ | [Callback](../../common-definitions/basic-types/document.md#callback12)<Date> | No | Yes | 

Callback triggered when date selection changes through scrolling in the dialog box.

**NOTE**

When **showTime** is set to **true**, the hour and minute in the value returned by the callback are the hour and minute selected in the picker. Otherwise, the hour and minute are the hour and minute of the system time.

**Atomic service API**: This API can be used in atomic services since API version 11.

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
| onDidAppear12+ | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 

Event callback after the dialog box appears.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange) > onWillDisappear > onDidDisappear.

2\. You can set the callback event for changing the dialog box display effect in **onDidAppear**. The settings take effect next time the dialog box appears.

3\. If the user closes the dialog box immediately after it appears, **onWillDisappear** is invoked before **onDidAppear**.

4\. If the dialog box is closed before its entrance animation is finished, this callback is not invoked.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onDidDisappear12+ | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 

Event callback after the dialog box disappears.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange) > onWillDisappear > onDidDisappear.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onWillAppear12+ | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 

Event callback when the dialog box is about to appear.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange) > onWillDisappear > onDidDisappear.

2\. You can set the callback event for changing the dialog box display effect in **onWillAppear**. The settings take effect next time the dialog box appears.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onWillDisappear12+ | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 

Event callback when the dialog box is about to disappear.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange) > onWillDisappear > onDidDisappear.

2\. If the user closes the dialog box immediately after it appears, **onWillDisappear** is invoked before **onDidAppear**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| shadow12+ | [ShadowOptions](../../universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../universal-attributes/visual-effects/image-effect/document.md#shadowstyle10) | No | Yes | 

Shadow of the dialog box.

Default value on 2-in-1 devices: **ShadowStyle.OUTER\_FLOATING\_MD** when the dialog box is focused and **ShadowStyle.OUTER\_FLOATING\_SM** otherwise

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| dateTimeOptions12+ | [DateTimeOptions](../../../../localization-kit/arkts-apis/ohos-intl-internationalization/document.md#datetimeoptionsdeprecated) | No | Yes | 

Whether to display a leading zero for the hours and minutes. Currently only the configuration of the **hour** and **minute** parameters is supported.

Default value:

**hour**: For the 24-hour format, the default value is **"2-digit"**, meaning the hour is displayed as a two-digit number. If the actual value is less than 10, a leading zero is added, displayed as "0X". For the 12-hour format, the default value is **"numeric"**, meaning no leading zero.

**minute**: The default value is **"2-digit"**, meaning the minute is displayed as a two-digit number. If the actual value is less than 10, a leading zero is added, displayed as "0X".

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| enableHoverMode14+ | boolean | No | Yes | 

Whether to respond when the device is in semi-folded mode.

\- **true**: Respond when the device is in semi-folded mode.

\- **false**: Do not respond when the device is in semi-folded mode.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| hoverModeArea14+ | [HoverModeAreaType](../../universal-attributes/transition/sheet-transition/document.md#hovermodeareatype14) | No | Yes | 

Display area of the dialog box when the device is in semi-folded mode.

Default value: **HoverModeAreaType.BOTTOM\_SCREEN**

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| enableHapticFeedback18+ | boolean | No | Yes | 

Whether to enable haptic feedback.

\- **true**: Enable haptic feedback.

\- **false**: Disable haptic feedback.

Default value: **true**

**Atomic service API**: This API can be used in atomic services since API version 18.

**NOTE**

1\. Whether this parameter takes effect after being set to **true** depends on hardware support.

2\. To enable haptic feedback, you must declare the following permission under **requestPermissions** in **module** in **src/main/module.json5** of the project:

"requestPermissions": \[{"name": "ohos.permission.VIBRATE"}\]

 |
| canLoop20+ | boolean | No | Yes | 

Whether to enable cyclic scrolling.

Default value: **true**

**NOTE**

**true**: Cyclic scrolling is enabled, where the year values increment or decrement with month cycling, and month values increment or decrement with day cycling.

**false**: Cyclic scrolling is disabled, preventing out-of-bounds scrolling in year, month, and day columns and cross-column value synchronization.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### LunarSwitchStyle14+

Defines the style of the lunar calendar switch in the **DatePickerDialog** component.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| selectedColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 
Background color of the switch when it is on.

Default value: **$r('sys.color.ohos\_id\_color\_text\_primary\_actived')**

 |
| unselectedColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Border color of the switch when it is off.

Default value: **$r('sys.color.ohos\_id\_color\_switch\_outline\_off')**

 |
| strokeColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Color of the icon inside the switch.

Default value: **Color.White**

 |

#### Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/hLGTm5f_TdSdK_7_TZ5qXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE76E4BED0F000BCD9AC9C92B40B3B390B34609DF3835EA40A96AD428D39432B)

For clarity in UI execution context, you are advised to use the [showDatePickerDialog](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#showdatepickerdialog) API in [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md).

## Example 1: Setting the Display Time

This example demonstrates how to set the display time using **showTime**, **useMilitaryTime**, and **dateTimeOptions**.

// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-01-01');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            showTime: true,
            useMilitaryTime: false,
            dateTimeOptions: { hour: "numeric", minute: "2-digit" },
            onDateAccept: (value: Date) => {
              // Save the date settings when the OK button is touched. In this way, when the date picker dialog box is displayed again, the selected date is the date last confirmed.
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            },
            onCancel: () => {
              console.info('DatePickerDialog:onCancel()');
            },
            onDateChange: (value: Date) => {
              console.info('DatePickerDialog:onDateChange()' + value.toString());
            },
            onDidAppear: () => {
              console.info('DatePickerDialog:onDidAppear()');
            },
            onDidDisappear: () => {
              console.info('DatePickerDialog:onDidDisappear()');
            },
            onWillAppear: () => {
              console.info('DatePickerDialog:onWillAppear()');
            },
            onWillDisappear: () => {
              console.info('DatePickerDialog:onWillDisappear()');
            }
          })
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/8AbAz-lKQiaV12mX1fotYg/en-us_image_0000002537925860.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1228A9F389A56CC013FA7E7BFDCBF35F8E228558191678B90DC8FEFEA47B1C04)

## Example 2: Customizing the Style

In this example, **disappearTextStyle**, **textStyle**, **selectedTextStyle**, **acceptButtonStyle**, and **cancelButtonStyle** are configured to customize the text and button style.

// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-01-01');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            disappearTextStyle: { color: '#297bec', font: { size: '20fp', weight: FontWeight.Bold } },
            textStyle: { color: Color.Black, font: { size: '18fp', weight: FontWeight.Normal } },
            selectedTextStyle: { color: Color.Blue, font: { size: '26fp', weight: FontWeight.Regular } },
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
            onDateAccept: (value: Date) => {
              // Save the date settings when the OK button is touched. In this way, when the date picker dialog box is displayed again, the selected date is the date last confirmed.
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            },
            onCancel: () => {
              console.info('DatePickerDialog:onCancel()');
            },
            onDateChange: (value: Date) => {
              console.info('DatePickerDialog:onDateChange()' + value.toString());
            },
            onDidAppear: () => {
              console.info('DatePickerDialog:onDidAppear()');
            },
            onDidDisappear: () => {
              console.info('DatePickerDialog:onDidDisappear()');
            },
            onWillAppear: () => {
              console.info('DatePickerDialog:onWillAppear()');
            },
            onWillDisappear: () => {
              console.info('DatePickerDialog:onWillDisappear()');
            }
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/8XkIuEhQSTGpvKr6V9c7CQ/en-us_image_0000002568685637.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCAF12165EF351669F88128C87962FA98DA59E606FB1684799090FD7A6A6DF85)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/EZs4e7z8SQ-GJO9f7XtHHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00BEE4D4B38B87D55381E0F4F18B53E5C49771AB09621C25C5EC024A303A4BA1)

To implement a fully customized date picker dialog box, create a [custom dialog box](../custom-dialog-box-customdialog/document.md) and then implement the [DatePicker](../../buttons-and-selections/datepicker/document.md) component.

## Example 3: Configuring a Dialog Box in the Hover State

This example demonstrates how to set the layout area of a dialog box when the device is in semi-folded mode.

@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-01-01');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            showTime: true,
            useMilitaryTime: false,
            disappearTextStyle: { color: Color.Pink, font: { size: '22fp', weight: FontWeight.Bold }},
            textStyle: { color: '#ff00ff00', font: { size: '18fp', weight: FontWeight.Normal }},
            selectedTextStyle: { color: '#ff182431', font: { size: '14fp', weight: FontWeight.Regular }},
            onDateAccept: (value: Date) => {
              // Save the date settings when the OK button is touched. In this way, when the date picker dialog box is displayed again, the selected date is the date last confirmed.
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            },
            onCancel: () => {
              console.info('DatePickerDialog:onCancel()');
            },
            onDateChange: (value: Date) => {
              console.info('DatePickerDialog:onDateChange()' + value.toString());
            },
            onDidAppear: () => {
              console.info('DatePickerDialog:onDidAppear()');
            },
            onDidDisappear: () => {
              console.info('DatePickerDialog:onDidDisappear()');
            },
            onWillAppear: () => {
              console.info('DatePickerDialog:onWillAppear()');
            },
            onWillDisappear: () => {
              console.info('DatePickerDialog:onWillDisappear()');
            },
            enableHoverMode: true,
            hoverModeArea: HoverModeAreaType.TOP\_SCREEN
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/ulcfaXAmTHuZXNouUuPj9Q/en-us_image_0000002568765647.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=547CF5FB11B9A8F7D871E2AC589580053E669DE228C684928F096C1B30F69E43)

## Example 4: Setting the Dialog Box Position

This example demonstrates how to set the position of a dialog box using **alignment** and **offset**.

// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-01-01');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            alignment: DialogAlignment.Center,
            offset: { dx: 20, dy: 0 },
            onDateAccept: (value: Date) => {
              // Save the date settings when the OK button is touched. In this way, when the date picker dialog box is displayed again, the selected date is the date last confirmed.
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            }
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/WJs2oFwZQYuXk1kz8T81kA/en-us_image_0000002537765922.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8AC3529A512A6F1583A90ACD3BBD02A6A1C655F8BA304FFDDFB5953C6BE8CF5)

## Example 5: Setting the Mask Area

This example demonstrates how to set the mask area using **maskRect**.

// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-01-01');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            maskRect: {
              x: 30,
              y: 60,
              width: '100%',
              height: '60%'
            },
            onDateAccept: (value: Date) => {
              // Save the date settings when the OK button is touched. In this way, when the date picker dialog box is displayed again, the selected date is the date last confirmed.
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            }
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/T_YpKL3YRUSfLgHcICSiYA/en-us_image_0000002537925862.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53FCDE4340DE0F0947E3F43E7BECE2C639A80212B78C1405F792BE72A7F37A1E)

## Example 6: Setting the Background

This example demonstrates how to set the dialog box background using **backgroundColor**, **backgroundBlurStyle**, and **shadow**.

// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-01-01');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            backgroundColor: 'rgb(204, 226, 251)',
            backgroundBlurStyle: BlurStyle.NONE,
            shadow: ShadowStyle.OUTER\_FLOATING\_SM,
            onDateAccept: (value: Date) => {
              // Save the date settings when the OK button is touched. In this way, when the date picker dialog box is displayed again, the selected date is the date last confirmed.
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            }
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/HXfRMZrESumr8aTaT5k01Q/en-us_image_0000002568685639.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B91438AB7C12879E0AF8BA90D18C77E39E0EC7AE1A879979E8373FE80E2D5647)

## Example 7: Switching Between Gregorian and Lunar Calendars

This example demonstrates how to set the date picker dialog box to display either the Gregorian (solar) calendar or the lunar calendar using **lunar** and **lunarSwitch**.

// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-11-09');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            lunar: false,
            onDateAccept: (value: Date) => {
              // Save the date settings when the OK button is touched. In this way, when the date picker dialog box is displayed again, the selected date is the date last confirmed.
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            }
          });
        })

      Button('Lunar DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            lunar: true,
            lunarSwitch: true,
            onDateAccept: (value: Date) => {
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            }
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/s2GuVbk6S8qx0dTMUwoKzg/en-us_image_0000002568765649.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7648F65482315622C259A502041DC4A1B5B43FEFDCFEAEA397DE89B7AD6A3CC)

## Example 8: Setting Display of Month and Day Columns

This example demonstrates how to configure the **mode** parameter to display only the month and day columns in the date picker dialog box.

// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-10-13');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            mode: DatePickerMode.MONTH\_AND\_DAY,
            onDateAccept: (value: Date) => {
              // Save the date settings when the OK button is touched. In this way, when the date picker dialog box is displayed again, the selected date is the date last confirmed.
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            }
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/WYzGXqM4Q56Q4hd7843dYQ/en-us_image_0000002537765924.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7FFFFE6E36D5D1A4A52833B3B7F9D09DD515B1FE715FCCABA9EAB4E5E9D2AE06)

## Example 9: Setting Cyclic Scrolling

This example demonstrates how to set whether to enable cyclic scrolling using **canLoop**, available since API version 20.

// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  @State isLoop: boolean = true;
  selectedDate: Date = new Date('2009-12-31');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            canLoop: this.isLoop,
            onDateAccept: (value: Date) => {
              // Save the date settings when the OK button is touched. In this way, when the date picker dialog box is displayed again, the selected date is the date last confirmed.
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            }
          });
        })

      Row() {
        Text('Loop scrolling').fontSize(20)
        Toggle({ type: ToggleType.Switch, isOn: true })
          .onChange((isOn: boolean) => {
            this.isLoop = isOn;
          })
      }.position({ x: '60%', y: '40%' })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/B05_exAEQYKokg3myKL5-A/en-us_image_0000002537925864.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84A853108DBA6C9C92F987167E10C001FC5E2675F0ED1027B8505B9711747D1D)

## Example 10: Customizing the Background Blur Effect

This example demonstrates how to customize the background blur effect by configuring [backgroundBlurStyleOptions](#datepickerdialogoptions), available since API version 19.

@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-01-01');

  build() {
    Stack({ alignContent: Alignment.Top }) {
      Image($r('app.media.bg'))
      Column() {
        Button('DatePickerDialog')
          .margin(20)
          .onClick(() => {
            this.getUIContext().showDatePickerDialog({
              start: new Date('2000-01-01'),
              end: new Date('2100-12-31'),
              selected: this.selectedDate,
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/h2YirtUVQCqlXXs-97tuIg/en-us_image_0000002568685641.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04D5EEB5ED2D651F4E0B8CEE9EF92179E45CAAD8959E8EC87C06829334DCCE3D)

## Example 11: Customizing the Background Effect

This example demonstrates how to customize the background effect by configuring [backgroundEffect](#datepickerdialogoptions). This functionality is supported since API version 19.

@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-01-01');

  build() {
    Stack({ alignContent: Alignment.Top }) {
      // Replace $r('app.media.bg') with the image resource file you use.
      Image($r('app.media.bg'))
      Column() {
        Button('DatePickerDialog')
          .margin(20)
          .onClick(() => {
            this.getUIContext().showDatePickerDialog({
              start: new Date('2000-01-01'),
              end: new Date('2100-12-31'),
              selected: this.selectedDate,
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/rW24xeLcS8WWIBAc2xL_VA/en-us_image_0000002568765651.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD3FF8F559B846AF41F8F9D7FBE225D06C6F6BD0F3870035CA0E3C3E7D96F54A)
