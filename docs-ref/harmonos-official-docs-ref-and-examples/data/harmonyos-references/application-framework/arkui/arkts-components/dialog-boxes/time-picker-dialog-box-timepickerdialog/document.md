# Time Picker Dialog Box (TimePickerDialog)

A time picker dialog box is a dialog box that allows users to select a time from the 24-hour range through scrolling.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/pGoVzqf-QeaO7r7ID8bnUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE1518B2D58BAAB99EB0F989396E66B7D69319ADF99A750D6FBA8219DF4A72AF)

-   The APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The functionality of this module depends on UI context. This means that the APIs of this module cannot be used where [the UI context is ambiguous](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). For details, see [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   This module does not support dynamic updates for color mode (light or dark) changes. To apply a new color mode, close and reopen the dialog box.
    
-   The maximum number of rows that can be displayed varies by screen orientation: In portrait mode, the default number of rows is 5. In landscape mode, the number of rows depends on the system configuration. If no system configuration is set, the default is 3 rows. To check the specific system configuration value for landscape mode, use **$r('sys.float.ohos\_id\_picker\_show\_count\_landscape')**.
    

#### TimePickerDialog

#### \[h2\]show(deprecated)

static show(options?: TimePickerDialogOptions)

Shows a time picker dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/qYuf5fvWQHOvM72dMTdKWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80AD7773323997DAAD758CD26DAC56D57B7A7AF1154FB6F4698DE91BDBD48133)

This API is supported since API version 8 and deprecated since API version 18. You are advised to use [showTimePickerDialog](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#showtimepickerdialog) instead. **showTimePickerDialog** can be called only after a [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) instance is obtained.

Since API version 10, you can use the [showTimePickerDialog](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#showtimepickerdialog) API in [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md), which ensures that the time picker dialog box is shown in the intended UI instance.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TimePickerDialogOptions](#timepickerdialogoptions) | No | Parameters of the time picker dialog box. |

#### TimePickerDialogOptions

Defines the configuration options of the time picker dialog box.

Inherited from [TimePickerOptions](../../buttons-and-selections/timepicker/document.md#timepickeroptions).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| useMilitaryTime | boolean | No | Yes | 
Whether to display the time in 24-hour format or 12-hour format.

\- **true**: 24-hour format.

\- **false**: 12-hour format.

Default value: **false**.

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

Font color, font size, and font weight of the selected item.

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

Offset of the dialog box relative to the alignment position.

Default value: **{ dx: 0 , dy: 0 }**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| maskRect10+ | [Rectangle](../alert-dialog-box-alertdialog/document.md#rectangle8) | No | Yes | 

Mask area of the dialog box. Events outside the mask area are transparently transmitted, and events within the mask area are not.

Default value: **{ x: 0, y: 0, width: '100%', height: '100%' }**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onAccept | (value: [TimePickerResult](../../buttons-and-selections/timepicker/document.md#timepickerresult)) => void | No | Yes | 

Callback invoked when the OK button in the dialog box is clicked.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onCancel | () => void | No | Yes | 

Callback invoked when the cancel button in the dialog box is clicked.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onChange | (value: [TimePickerResult](../../buttons-and-selections/timepicker/document.md#timepickerresult)) => void | No | Yes | 

Triggered when the text picker in the dialog box snaps to the selected item.

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
| onDidAppear12+ | () => void | No | Yes | 

Event callback after the dialog box appears.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onAccept/onCancel/onChange) > onWillDisappear > onDidDisappear.

2\. You can set the callback event for changing the dialog box display effect in **onDidAppear**. The settings take effect next time the dialog box appears.

3\. If the user closes the dialog box immediately after it appears, **onWillDisappear** is invoked before **onDidAppear**.

4\. If the dialog box is closed before its entrance animation is finished, this callback is not invoked.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onDidDisappear12+ | () => void | No | Yes | 

Event callback after the dialog box disappears.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onAccept/onCancel/onChange) > onWillDisappear > onDidDisappear.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onWillAppear12+ | () => void | No | Yes | 

Event callback when the dialog box is about to appear.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onAccept/onCancel/onChange) > onWillDisappear > onDidDisappear.

2\. You can set the callback event for changing the dialog box display effect in **onWillAppear**. The settings take effect next time the dialog box appears.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onWillDisappear12+ | () => void | No | Yes | 

Event callback when the dialog box is about to disappear.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onAccept/onCancel/onChange) > onWillDisappear > onDidDisappear.

2\. If the user closes the dialog box immediately after it appears, **onWillDisappear** is invoked before **onDidAppear**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| shadow12+ | [ShadowOptions](../../universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../universal-attributes/visual-effects/image-effect/document.md#shadowstyle10) | No | Yes | 

Shadow of the dialog box.

**NOTE**

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

Whether to enable the hover mode.

\- **true**: Respond when the device is in semi-folded mode.

\- **false**: Do not respond when the device is in semi-folded mode.

Default value: **false**.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| hoverModeArea14+ | [HoverModeAreaType](../../universal-attributes/transition/sheet-transition/document.md#hovermodeareatype14) | No | Yes | 

Display area of the dialog box in hover mode.

Default value: **HoverModeAreaType.BOTTOM\_SCREEN**

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| onEnterSelectedArea18+ | Callback<[TimePickerResult](../../buttons-and-selections/timepicker/document.md#timepickerresult)\> | No | Yes | 

Represents the callback triggered during the scrolling of the text picker when an item enters the divider area. Compared to the **onChange** event, this event is triggered earlier, specifically when the scroll distance of the current column exceeds half the height of the selected item, which indicates that the item has entered the divider area.

**NOTE**

When **enableCascade** is set to **true**, using this callback is not recommended due to the interdependent relationship between the AM/PM and hour columns. This callback indicates the moment an option enters the divider area during scrolling, and only the value of the currently scrolled column will change. The values of other non-scrolled columns will remain unchanged.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| enableCascade18+ | boolean | No | Yes | 

Whether the AM/PM indicator automatically switches based on the hour value. Only takes effect when **useMilitaryTime** is set to **false**.

\- **true**: The AM/PM indicator automatically switches based on the hour value.

\- **false**: The AM/PM indicator remains static regardless of hour changes.

Default value: **false**.

When **enableCascade** is set to **true**, it only takes effect if the **loop** parameter is also **true**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| enableHapticFeedback18+ | boolean | No | Yes | 

Whether to enable haptic feedback.

\- **true**: Enable haptic feedback.

\- **false**: Disable haptic feedback.

Default value: **true**.

**NOTE**

1\. Whether this parameter takes effect after being set to **true** depends on hardware support.

2\. To enable haptic feedback, you must declare the following permission under **requestPermissions** in **module** in **src/main/module.json5** of the project.

"requestPermissions": \[{"name": "ohos.permission.VIBRATE"}\]

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/hhc8H5R7QYubjSLyRu7oxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA3E90EEF9E2481A51872FE3B14DD47886C68E50A54EBF12265F1AFEB6849C7B)

For clarity in UI execution context, you are advised to use the [showTimePickerDialog](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#showtimepickerdialog) API in [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md).

## Example 1: Setting the Display Time Format

This example demonstrates how to set the display time using **useMilitaryTime**, **dateTimeOptions**, and **format**.

@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog 12-hour format')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            selected: this.selectTime,
            format: TimePickerFormat.HOUR\_MINUTE,
            useMilitaryTime: false,
            dateTimeOptions: { hour: 'numeric', minute: '2-digit' },
            onAccept: (value: TimePickerResult) => {
              // Set selectTime to the time when the OK button is clicked. In this way, when the dialog box is displayed again, the selected time is the time when the operation was confirmed last time.
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            },
            onCancel: () => {
              console.info('TimePickerDialog:onCancel()');
            },
            onChange: (value: TimePickerResult) => {
              console.info('TimePickerDialog:onChange()' + JSON.stringify(value));
            },
            onDidAppear: () => {
              console.info('TimePickerDialog:onDidAppear()');
            },
            onDidDisappear: () => {
              console.info('TimePickerDialog:onDidDisappear()');
            },
            onWillAppear: () => {
              console.info('TimePickerDialog:onWillAppear()');
            },
            onWillDisappear: () => {
              console.info('TimePickerDialog:onWillDisappear()');
            }
          });
        })
      Button('TimePickerDialog 24-hour format')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            selected: this.selectTime,
            format: TimePickerFormat.HOUR\_MINUTE\_SECOND,
            useMilitaryTime: true,
            onAccept: (value: TimePickerResult) => {
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            },
          })
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/fmOXEWKBRga2rGy9TEPX-w/en-us_image_0000002537765926.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CF8049018BCD1248583ABDB4F8AEF57A48EE05D2BDD0FDB20DC3AC60B2A9356)

## Example 2: Customizing the Style

In this example, **disappearTextStyle**, **textStyle**, **selectedTextStyle**, **acceptButtonStyle**, and **cancelButtonStyle** are configured to customize the text and button style.

// xxx.ets
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog 12-hour format')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
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
            onAccept: (value: TimePickerResult) => {
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/eYPM3xbKSU-IhSeD9nsmEg/en-us_image_0000002537925866.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB918B72281D5370F082E66563244DD760BFAA40F5D5ED391D7AF5AEE0E7057B)

## Example 3: Configuring a Dialog Box in the Hover State

This example demonstrates how to set the layout area of a dialog box in hover mode on a foldable device.

@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog 12-hour format')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            selected: this.selectTime,
            disappearTextStyle: { color: Color.Red, font: { size: 15, weight: FontWeight.Lighter } },
            textStyle: { color: Color.Black, font: { size: 20, weight: FontWeight.Normal } },
            selectedTextStyle: { color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } },
            onAccept: (value: TimePickerResult) => {
              // Set selectTime to the time when the OK button is clicked. In this way, when the dialog box is displayed again, the selected time is the time when the operation was confirmed last time.
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            },
            onCancel: () => {
              console.info('TimePickerDialog:onCancel()');
            },
            onChange: (value: TimePickerResult) => {
              console.info('TimePickerDialog:onChange()' + JSON.stringify(value));
            },
            onDidAppear: () => {
              console.info('TimePickerDialog:onDidAppear()');
            },
            onDidDisappear: () => {
              console.info('TimePickerDialog:onDidDisappear()');
            },
            onWillAppear: () => {
              console.info('TimePickerDialog:onWillAppear()');
            },
            onWillDisappear: () => {
              console.info('TimePickerDialog:onWillDisappear()');
            },
            enableHoverMode: true,
            hoverModeArea: HoverModeAreaType.TOP\_SCREEN
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/GfXojtppTGatdZkUAlrJcQ/en-us_image_0000002568685643.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=851F83C63873657DFD0280E6F76B13C78CDD67FC1F652AF639DCEBD5CF130106)

## Example 4: Setting the Dialog Box Position

This example demonstrates how to set the position of a dialog box using **alignment** and **offset**.

// xxx.ets
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            alignment: DialogAlignment.Center,
            offset: { dx: 20 , dy: 0 },
            onAccept: (value: TimePickerResult) => {
              // Set selectTime to the time when the OK button is clicked. In this way, when the dialog box is displayed again, the selected time is the time when the operation was confirmed last time.
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/kjRidid0T1CJnh9V9-Bwew/en-us_image_0000002568765653.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF32992098C8785C610E27B617382B029F4FDC0497FC6C309735D537257ACE8A)

## Example 5: Setting the Mask Area

This example demonstrates how to set the mask area using **maskRect**.

// xxx.ets
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            maskRect: { x: 30, y: 60, width: '100%', height: '60%' },
            onAccept: (value: TimePickerResult) => {
              // Set selectTime to the time when the OK button is clicked. In this way, when the dialog box is displayed again, the selected time is the time when the operation was confirmed last time.
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/z5JW-y5YQSiaRpgPv3ZIKA/en-us_image_0000002537765928.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BEA39BD3065C92344E4E5D54C2742BEA91FE19C9161B20EF85F0FB109314F95D)

## Example 6: Setting the Background

This example demonstrates how to set the dialog box background using **maskRect**.

// xxx.ets
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            backgroundColor: 'rgb(204, 226, 251)',
            backgroundBlurStyle: BlurStyle.NONE,
            shadow: ShadowStyle.OUTER\_FLOATING\_SM,
            onAccept: (value: TimePickerResult) => {
              // Set selectTime to the time when the OK button is clicked. In this way, when the dialog box is displayed again, the selected time is the time when the operation was confirmed last time.
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/9XwzDPjaSp6zfHKnjgdJtw/en-us_image_0000002537925868.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35C2EC37702007BEDF50CC2896BD846640AA7E8161B4B03CF875C64DAECAAAC9)

## Example 7: Setting the Start Time

This example demonstrates how to set the start time for the time picker dialog box.

// xxx.ets
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2022-07-22T08:50:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            useMilitaryTime: false,
            selected: this.selectTime,
            format: TimePickerFormat.HOUR\_MINUTE\_SECOND,
            start: new Date('2022-07-22T08:30:00'),
            onAccept: (value: TimePickerResult) => {
              // Set selectTime to the time when the OK button is clicked. In this way, when the dialog box is displayed again, the selected time is the time when the operation was confirmed last time.
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/0k5XyABdSVmUXpMj46OwCA/en-us_image_0000002568685645.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C500657144F1DCBE7A24BD8C595A788C1C8A0928005B40794D1E28AF9B866B80)

## Example 8: Setting the End Time

This example demonstrates how to set the end time for the time picker dialog box.

// xxx.ets
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2022-07-22T08:50:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            useMilitaryTime: false,
            selected: this.selectTime,
            format: TimePickerFormat.HOUR\_MINUTE\_SECOND,
            end: new Date('2022-07-22T15:20:00'),
            onAccept: (value: TimePickerResult) => {
              // Set selectTime to the time when the OK button is clicked. In this way, when the dialog box is displayed again, the selected time is the time when the operation was confirmed last time.
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/D9LzqE4xR86ouhAZObukdg/en-us_image_0000002568765655.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8ED97A56464B5E572051BA2565F9B24406A15AC1103C5FC20551C660F4C263E1)

## Example 9: Enabling the AM/PM Indicator to Automatically Switch Based on the Hour Value in 12-hour Format

This example demonstrates how to enable the AM/PM indicator to automatically switch based on the hour value in 12-hour format using **enableCascade**.

// xxx.ets
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2022-07-22T08:00:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            useMilitaryTime: false,
            selected: this.selectTime,
            enableCascade:true,
            onAccept: (value: TimePickerResult) => {
              // Set selectTime to the time when the OK button is clicked. In this way, when the dialog box is displayed again, the selected time is the time when the operation was confirmed last time.
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/6vbU2_1xQ5KtquIWLiFiSg/en-us_image_0000002537765930.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=920E322B91631A54FFD13670FDF2AED1699B22547188667E2CAA380D2BB83E72)

## Example 10: Customizing the Background Blur Effect

This example demonstrates how to customize the background blur effect by configuring [backgroundBlurStyleOptions](#timepickerdialogoptions). This functionality is supported since API version 19.

@Entry
@Component
struct TimePickerDialogExample {
  build() {
    Stack({ alignContent: Alignment.Top }) {
      // Replace $r('app.media.bg') with the image resource file you use.
      Image($r('app.media.bg'))
      Column() {
        Button('TimePickerDialog')
          .margin(20)
          .onClick(() => {
            this.getUIContext().showTimePickerDialog({
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/PEML9TAVSjWNWGSDWGNQtA/en-us_image_0000002537925870.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=613813C1ACBBA0C48AECE472AF5467436D6A182FFFC0F44186DB5CA531BC5BBD)

## Example 11: Customizing the Background Effect

This example demonstrates how to customize the background effect by configuring [backgroundEffect](#timepickerdialogoptions). This functionality is supported since API version 19.

@Entry
@Component
struct TimePickerDialogExample {
  build() {
    Stack({ alignContent: Alignment.Top }) {
      // Replace $r('app.media.bg') with the image resource file you use.
      Image($r('app.media.bg'))
      Column() {
        Button('TimePickerDialog')
          .margin(20)
          .onClick(() => {
            this.getUIContext().showTimePickerDialog({
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/S-Pxnr_ZQEOOzkTcKAjZcA/en-us_image_0000002568685647.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A8AA2AB65EE11F453C8B82C09DC72DDCF94A47C79D48F38FB4F855DC3804FDE)
