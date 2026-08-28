# Calendar Picker Dialog Box (CalendarPickerDialog)

A calendar picker dialog box is a dialog box that allows users to select a date from a calendar picker.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/aJcWUBygSMOyacnTxwioAw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8461ED24DB4075F05AACDD628DD46774814F1215DAB71B194BCE0BC55CC876C)

-   This component is supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The functionality of this module depends on UI context. This means that the APIs of this module cannot be used where [the UI context is ambiguous](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). For details, see [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   This module does not support dynamic updates for color mode (light or dark) changes. To apply a new color mode, close and reopen the dialog box.
    

#### CalendarPickerDialog

#### \[h2\]show

static show(options?: CalendarDialogOptions): void

Defines a calendar picker dialog box.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [CalendarDialogOptions](#calendardialogoptions) | No | Parameters of the calendar picker dialog box. |

#### CalendarDialogOptions

Defines the configuration options of the calendar picker dialog box.

Inherits from [CalendarOptions](../../buttons-and-selections/calendarpicker/document.md#calendaroptions).

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| onAccept | [Callback](../../common-definitions/basic-types/document.md#callback12)<Date> | No | Yes | 
Triggered when the OK button in the dialog box is clicked.

The callback parameter represents the selected date value.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onCancel | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 

Triggered when the Cancel button in the dialog box is clicked.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onChange | [Callback](../../common-definitions/basic-types/document.md#callback12)<Date> | No | Yes | 

Triggered when the selection in the picker changes the selected date.

The callback parameter represents the selected date value.

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
| acceptButtonStyle12+ | [PickerDialogButtonStyle](../../buttons-and-selections/picker-common-apis/document.md#pickerdialogbuttonstyle12) | No | Yes | 

Style of the accept button.

**NOTE**

In the **acceptButtonStyle** and **cancelButtonStyle** configurations, only one **primary** field can be set to **true** at most. If both the **primary** fields are set to **true**, neither will take effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| cancelButtonStyle12+ | [PickerDialogButtonStyle](../../buttons-and-selections/picker-common-apis/document.md#pickerdialogbuttonstyle12) | No | Yes | 

Style of the cancel button.

**NOTE**

In the **acceptButtonStyle** and **cancelButtonStyle** configurations, only one **primary** field can be set to **true** at most. If both the **primary** fields are set to **true**, neither will take effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onDidAppear12+ | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 

Event callback after the dialog box appears.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onAccept/onCancel/onChange) > onWillDisappear > onDidDisappear.

2\. You can set the callback event for changing the dialog box display effect in **onDidAppear**. The settings take effect next time the dialog box appears.

3\. If the user dismisses the dialog box immediately after it appears, **onWillDisappear** is invoked before **onDidAppear**.

4\. If the dialog box is dismissed before its entrance animation is finished, this callback is not invoked.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onDidDisappear12+ | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 

Event callback after the dialog box disappears.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onAccept/onCancel/onChange) > onWillDisappear > onDidDisappear.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onWillAppear12+ | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 

Event callback when the dialog box is about to appear.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onAccept/onCancel/onChange) > onWillDisappear > onDidDisappear.

2\. You can set the callback event for changing the dialog box display effect in **onWillAppear**. The settings take effect next time the dialog box appears.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onWillDisappear12+ | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | No | Yes | 

Event callback when the dialog box is about to disappear.

**NOTE**

1\. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onAccept/onCancel/onChange) > onWillDisappear > onDidDisappear.

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
| markToday19+ | boolean | No | Yes | 

Whether to highlight the current system date.

\- **true**: Highlight the current system date.

\- **false**: Do not highlight the current system date.

Default value: **false**.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/2wOcJzT7TTaM8ngjKvQ21w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B8D3E38B414DA0C6C522A06A962669372D3AA242A6785B2DE6F437CC2E2DF0F)

When the application window is resized, the width of the dialog box is continuously compressed. If the window width is reduced below a certain threshold, the content of the dialog box may not be fully visible. To ensure that the content of the **CalendarPickerDialog** component is fully displayed, the minimum window width required is 386 vp.

#### Example

## Example 1: Setting the Background

This example demonstrates how to set the calendar picker dialog box's background using **backgroundColor**, **backgroundBlurStyle**, and **shadow** in [CalendarDialogOptions](#calendardialogoptions).

// xxx.ets
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2024-03-24');

  build() {
    Column() {
      Button('Show CalendarPicker Dialog')
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({
            selected: this.selectedDate,
            backgroundColor: Color.Gray,
            backgroundBlurStyle: BlurStyle.NONE,
            shadow: ShadowStyle.OUTER\_FLOATING\_SM,
            onAccept: (value) => {
              // Callback invoked when the OK button in the dialog box is clicked. value indicates the selected date.
              this.selectedDate = value;
              console.info('calendar onAccept:' + JSON.stringify(value));
            },
            onCancel: () => {
              // Callback invoked when the cancel button in the dialog box is clicked.
              console.info('calendar onCancel');
            },
            onChange: (value) => {
              // Callback invoked when the selection in the picker changes the selected date. value indicates the selected date.
              console.info('calendar onChange:' + JSON.stringify(value));
            },
            onDidAppear: () => {
              console.info('calendar onDidAppear');
            },
            onDidDisappear: () => {
              console.info('calendar onDidDisappear');
            },
            onWillAppear: () => {
              console.info('calendar onWillAppear');
            },
            onWillDisappear: () => {
              console.info('calendar onWillDisappear');
            }
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/zUlUIo1tSFaV9C4hqSS1KQ/en-us_image_0000002568685635.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0348813ED6D1489D8859850816E4627106FCCE51CB071410374EC203D57EB23)

## Example 2: Customizing the Button Style

This example shows how to customize the calendar picker dialog box's buttons by configuring **acceptButtonStyle** and **cancelButtonStyle** in [CalendarDialogOptions](#calendardialogoptions). This functionality is supported since API version 12.

// xxx.ets
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date();

  build() {
    Column() {
      Button('Show CalendarPicker Dialog')
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({
            selected: this.selectedDate,
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
            onAccept: (value) => {
              this.selectedDate = value;
              console.info('calendar onAccept:' + JSON.stringify(value));
            }
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/AEzcEqkPR_eR-3XifVUgAQ/en-us_image_0000002568765645.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0550303A7C182D96721ECB7F47D192A2A31FEF04BF51140E3F1BBD04FA834A29)

## Example 3: Configuring a Dialog Box in the Hover State

This example demonstrates how to set the layout area of a dialog box when the device is in semi-folded mode. This functionality is supported since API version 14.

@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2024-04-23');

  build() {
    Column() {
      Button('Show CalendarPicker Dialog')
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({
            selected: this.selectedDate,
            onAccept: (value) => {
              console.info('calendar onAccept:' + JSON.stringify(value));
            },
            onCancel: () => {
              console.info('calendar onCancel');
            },
            onChange: (value) => {
              console.info('calendar onChange:' + JSON.stringify(value));
            },
            onDidAppear: () => {
              console.info('calendar onDidAppear');
            },
            onDidDisappear: () => {
              console.info('calendar onDidDisappear');
            },
            onWillAppear: () => {
              console.info('calendar onWillAppear');
            },
            onWillDisappear: () => {
              console.info('calendar onWillDisappear');
            },
            enableHoverMode: true,
            hoverModeArea: HoverModeAreaType.TOP\_SCREEN,
          });
        })
    }.width('100%')
  }
}

## Example 4: Setting the Background Style for the Selected Date

This example demonstrates how to customize the background style of the selected date using **hintRadius** in [CalendarOptions](../../buttons-and-selections/calendarpicker/document.md#calendaroptions). This functionality is supported since API version 10.

// xxx.ets
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2024-04-23');

  build() {
    Column() {
      Button('Show CalendarPicker Dialog')
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({
            selected: this.selectedDate,
            hintRadius: 1,
            onAccept: (value) => {
              this.selectedDate = value;
              console.info('calendar onAccept:' + JSON.stringify(value));
            }
          });
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/DVMSjmItRoiB9EqUtUCfTA/en-us_image_0000002537765920.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062247Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19ED1C5B7A80708978A810215CCD4F53C74D9DCED0EFC3D8100DD23E04DAEBF6)

## Example 5: Setting Start and End Dates

This example demonstrates how to set the start and end dates for the calendar picker dialog box using **start** and **end** in [CalendarOptions](../../buttons-and-selections/calendarpicker/document.md#calendaroptions). This functionality is supported since API version 18.

// xxx.ets
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2025-01-01');
  private startDate: Date = new Date('2024-01-10');
  private endDate: Date = new Date('2025-01-10');

  build() {
    Column() {
      Text('Calendar date picker').fontSize(30)
      Button('Show CalendarPicker Dialog')
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({
            start: this.startDate,
            end: this.endDate,
            selected: this.selectedDate,
          });
        })
    }.width('100%').margin({ top: 350 })
  }
}

## Example 6: Highlighting the Current Date and Configuring Disabled Date Ranges

This example demonstrates how to keep the current system date highlighted in the calendar picker dialog box using the **markToday** property in [CalendarDialogOptions](#calendardialogoptions) and set disabled date ranges using the **disabledDateRange** property in [CalendarOptions](../../buttons-and-selections/calendarpicker/document.md#calendaroptions). This functionality is supported since API version 19.

// xxx.ets
@Entry
@Component
struct CalendarPickerExample {
  private disabledDateRange: DateRange\[\] = \[
    { start: new Date('2025-01-01'), end: new Date('2025-01-02') },
    { start: new Date('2025-01-09'), end: new Date('2025-01-10') },
    { start: new Date('2025-01-15'), end: new Date('2025-01-16') },
    { start: new Date('2025-01-19'), end: new Date('2025-01-19') },
    { start: new Date('2025-01-22'), end: new Date('2025-01-25') }
  \];

  build() {
    Column() {
      Button("Show CalendarPicker Dialog")
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({ markToday: true, disabledDateRange: this.disabledDateRange });
        })
    }.width('100%').margin({ top: 350 })
  }
}

## Example 7: Customizing the Background Blur Effect

This example demonstrates how to customize the background blur effect by configuring [backgroundBlurStyleOptions](#calendardialogoptions). This functionality is supported since API version 19.

@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2025-08-05');

  build() {
    Stack({ alignContent: Alignment.Top }) {
      // Replace $r('app.media.bg') with the image resource file you use.
      Image($r('app.media.bg'))
      Column() {
        Button('Show CalendarPicker Dialog')
          .margin(20)
          .onClick(() => {
            CalendarPickerDialog.show({
              selected: this.selectedDate,
              hintRadius: 1,
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

## Example 8: Customizing the Background Effect

This example demonstrates how to customize the background effect by configuring [backgroundEffect](#calendardialogoptions). This functionality is supported since API version 19.

@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2025-08-05');

  build() {
    Stack({ alignContent: Alignment.Top }) {
      // Replace $r('app.media.bg') with the image resource file you use.
      Image($r('app.media.bg'))
      Column() {
        Button('Show CalendarPicker Dialog')
          .margin(20)
          .onClick(() => {
            CalendarPickerDialog.show({
              selected: this.selectedDate,
              hintRadius: 1,
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
