# DatePicker

**DatePicker** is a component for selecting a date through scrolling interaction.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/vU97FP5hTmGYZ4ACLUzbdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1975106E87569B8E07B1C7304A8B655E26994E0600E109AC485D126A869A3EEE)

-   This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   Avoid changing component attributes during animation processes.
    
-   The maximum number of rows that can be displayed varies by screen orientation: In portrait mode, the default number of rows is 5. In landscape mode, the number of rows depends on the system configuration. If no system configuration is set, the default is 3 rows. To check the specific system configuration value for landscape mode, use **$r('sys.float.ohos\_id\_picker\_show\_count\_landscape')**.
    

#### Child Components

Not supported

#### APIs

DatePicker(options?: DatePickerOptions)

Creates a date picker in the given date range.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [DatePickerOptions](#datepickeroptions) | No | Parameters of the date picker. |

#### DatePickerOptions

Describes the parameters of the date picker.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start | Date | No | Yes | 
Start date of the picker.

Default value: **Date('1970-1-1')**

Value range: \[Date('1900-01-31'), Date('2100-12-31')\]

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| end | Date | No | Yes | 

End date of the picker.

Default value: **Date('2100-12-31')**

Value range: \[Date('1900-01-31'), Date('2100-12-31')\]

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| selected | Date | No | Yes | 

Date of the selected item.

Default value: current system date

Value range: \[Date('1900-01-31'), Date('2100-12-31')\]

Since API version 10, this parameter supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| mode18+ | [DatePickerMode](#datepickermode18) | No | Yes | 

Date display mode.

Default value: **DatePickerMode.DATE**, which means to display three columns: year, month, and day.

In [DatePickerDialog](../../dialog-boxes/date-picker-dialog-box-datepickerdialog/document.md), when **showTime** in [DatePickerDialogOptions](../../dialog-boxes/date-picker-dialog-box-datepickerdialog/document.md#datepickerdialogoptions) is **true**, this parameter is ignored and the year, month, day columns are always shown.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/EFVtJkcvRPuJAYj7EpqsrQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A66053E756DBCBE13A3B94B7E8322EF34C470E4B8752F3485C18E7B06F75424C)

-   For details about how to use **Date**, see [TimePickerOptions](../timepicker/document.md#timepickeroptions).
    
-   Property modifications made to **DatePickerOptions** during the **DatePicker** scrolling process may not take effect.
    

**Exception description of date configuration**

| Exception | Result |
| :-- | :-- |
| The start date is later than the end date, and the selected date is not set. | The start date, end date, and selected date are set to the default values. |
| The start date is later than the end date, and the selected date is earlier than the default start date. | The start date and end date are set to the default values, and the selected date is set to the default start date. |
| The start date is later than the end date, and the selected date is later than the default end date. | The start date and end date are set to the default values, and the selected date is set to the default end date. |
| The start date is later than the end date, and the selected date is within the range of the default start date and end date. | The start date and end date are set to the default values, and the selected date is set to the specified value. |
| The selected date is earlier than the start date. | The start date is set to the selected date. |
| The selected date is later than the end date. | The end date is set to the selected date. |
| The start date is later than the current system date, and the selected date is not set. | The start date is set to the selected date. |
| The end date is earlier than the current system date, and the selected date is not set. | The end date is set to the selected date. |
| The set date is in invalid format, for example, **'1999-13-32'**. | The default value is used. |
| The start date or end date is earlier than the earliest date in the valid date range. | The start date or end date is set to the default state date. |
| The start date or end date is later than the latest date in the valid date range. | The start date or end date is set to the default end date. |
| Both the start date and end date are earlier than the earliest date in the valid date range. | The start date and end date are set to the earliest date in the valid date range. |
| Both the start date and end date are later than the latest date in the valid date range. | The start date and end date are set to the latest date in the valid date range. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/2LwjgW-TTtqzjyEL2UpZ8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B13AD6142DBC119A27343A3579BAF111534435A47F7A2A7886AF850831471333)

Handle exceptions for the start and end dates first, followed by exceptions for the selected date.

#### DatePickerMode18+

Enumerates date display modes.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DATE | 0 | Three-column display: year, month, and day. |
| YEAR\_AND\_MONTH | 1 | Two-column display: year and month. |
| MONTH\_AND\_DAY | 2 | 
Two-column display: month and day.

In this mode, the year value remains fixed.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]lunar

lunar(value: boolean)

Sets whether to display dates in lunar calendar format.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/NGLMtLQWQWi7cbOQ_xhNpw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2AB63E10F76D5C33B5573CD579E8024316A54014E9587A13BF3C2CED49D90DF)

This attribute takes effect only in Simplified Chinese and Traditional Chinese locales; it has no effect in other locales.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to display dates in lunar calendar format.

\- **true**: Display dates in lunar calendar format.

\- **false**: Do not display dates in lunar calendar format.

Default value: **false**

 |

#### \[h2\]lunar18+

lunar(isLunar: Optional<boolean>)

Sets whether to display dates in lunar calendar format. Compared to [lunar](#lunar), the **isLunar** parameter supports the **undefined** type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/ajPCpy47SMefoz4aOiN8Pg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC748B3E79D5CA16781289D933433CA3EF4BA3CDFB23EB4A067E4F053823F53B)

This attribute takes effect only in Simplified Chinese and Traditional Chinese locales; it has no effect in other locales.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isLunar | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to display dates in lunar calendar format.

\- **true**: Display dates in lunar calendar format.

\- **false**: Do not display dates in lunar calendar format.

Default value: **false**

If the value of **isLunar** is **undefined**, the default value is used.

 |

#### \[h2\]disappearTextStyle10+

disappearTextStyle(value: PickerTextStyle)

Sets the text style for edge items (the second item above or below the selected item).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [PickerTextStyle](../picker-common-apis/document.md#pickertextstyle) | Yes | 
Text color, font size, and font weight for edge items.

Default value:

{

color: '#ff182431',

font: {

size: '14fp',

weight: FontWeight.Regular

}

}

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/OgfMcilkToGY8hv6ko2plA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7EC587303427D8E827A965E5B53764630F969654A965B5F88B37FFF36426469)

Edge items only appear when there are at least two visible items above or below the selected item. If insufficient items are available, no edge items will be styled.

#### \[h2\]disappearTextStyle18+

disappearTextStyle(style: Optional<PickerTextStyle>)

Sets the text style for edge items (the second item above or below the selected item). Compared to [disappearTextStyle10+](#disappeartextstyle10), this API supports the **undefined** type for the **style** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[PickerTextStyle](../picker-common-apis/document.md#pickertextstyle)\> | Yes | 
Text color, font size, and font weight for edge items.

Default value:

{

color: '#ff182431',

font: {

size: '14fp',

weight: FontWeight.Regular

}

}

If the value of **style** is **undefined**, the default value is used.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/IGOO0GEcSL2-Cgw_zbht9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82F7DA902401A8E864A2C28F60FF894A3DC46CFCAFB39D7A28B7679F2D38EBE5)

Edge items only appear when there are at least two visible items above or below the selected item. If insufficient items are available, no edge items will be styled.

#### \[h2\]textStyle10+

textStyle(value: PickerTextStyle)

Sets the text style for candidate items (the first item immediately above or below the selected item).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [PickerTextStyle](../picker-common-apis/document.md#pickertextstyle) | Yes | 
Text color, font size, and font weight for candidate items.

Default value:

{

color: '#ff182431',

font: {

size: '16fp',

weight: FontWeight.Regular

}

}

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/JIwf7U36RueEl9jCSz_w-w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6C353B0DFD2C529F78B9DB933C6E43EBDBB86CE13ABA45852EF9A58821B0C1B)

Candidate items only appear when there is at least one visible item above or below the selected item. If insufficient items are available, no candidate items will be styled.

#### \[h2\]textStyle18+

textStyle(style: Optional<PickerTextStyle>)

Sets the text style for candidate items (the first item immediately above or below the selected item). Compared to [textStyle10+](#textstyle10), this API supports the **undefined** type for the **style** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[PickerTextStyle](../picker-common-apis/document.md#pickertextstyle)\> | Yes | 
Text color, font size, and font weight for candidate items.

Default value:

{

color: '#ff182431',

font: {

size: '16fp',

weight: FontWeight.Regular

}

}

If the value of **style** is **undefined**, the default value is used.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/-Ekx_aW5TVKpzLjtM2G_PQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=720A8F1BBB024EFF1AD196178815F84365F98160D54BDF1EA36DC7742141E94F)

Candidate items only appear when there is at least one visible item above or below the selected item. If insufficient items are available, no candidate items will be styled.

#### \[h2\]selectedTextStyle10+

selectedTextStyle(value: PickerTextStyle)

Sets the text style for the selected item.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [PickerTextStyle](../picker-common-apis/document.md#pickertextstyle) | Yes | 
Font color, font size, and font weight of the selected item.

Default value:

{

color: '#ff007dff',

font: {

size: '20fp',

weight: FontWeight.Medium

}

}

 |

#### \[h2\]selectedTextStyle18+

selectedTextStyle(style: Optional<PickerTextStyle>)

Sets the text style for the selected item. Compared to [selectedTextStyle10+](#selectedtextstyle10), this API supports the **undefined** type for the **style** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[PickerTextStyle](../picker-common-apis/document.md#pickertextstyle)\> | Yes | 
Font color, font size, and font weight of the selected item.

Default value:

{

color: '#ff007dff',

font: {

size: '20fp',

weight: FontWeight.Medium

}

}

If the value of **style** is **undefined**, the default value is used.

 |

#### \[h2\]enableHapticFeedback18+

enableHapticFeedback(enable: Optional<boolean>)

Sets whether to enable haptic feedback.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to enable haptic feedback.

\- **true**: Enable haptic feedback.

\- **false**: Disable haptic feedback.

Default value: **true**

Whether this parameter takes effect after being set to **true** depends on hardware support.

If the value of **enable** is **undefined**, the default value is used.

 |

To enable haptic feedback, you must declare the following permission under **requestPermissions** in **module** in **src/main/module.json5** of the project.

"requestPermissions": \[
   {
      "name": "ohos.permission.VIBRATE",
   }
\]

#### \[h2\]digitalCrownSensitivity18+

digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>)

Sets the sensitivity to the digital crown rotation.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sensitivity | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[CrownSensitivity](../../common-definitions/enums/document.md#crownsensitivity18)\> | Yes | 
Sensitivity to the digital crown rotation.

Default value: **CrownSensitivity.MEDIUM**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/FTsMLo_LQqWOChWuycRA1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D05FA058A960DD8EBCAAF011E61F27C143982D336AF5331D9E6263767590306)

This API is only available to circular screens on wearable devices. The component needs to obtain focus before responding to the [crown event](../../universal-events/basic-input-events/crown-event/document.md).

#### \[h2\]canLoop20+

canLoop(isLoop: Optional<boolean>)

Sets whether to enable cyclic scrolling.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isLoop | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to enable cyclic scrolling.

\- **true**: Cyclic scrolling is enabled, where the year values increment or decrement with month cycling, and month values increment or decrement with day cycling.

\- **false**: Cyclic scrolling is disabled, preventing out-of-bounds scrolling in year, month, and day columns and cross-column value synchronization.

Default value: **true**

If the value of **isLoop** is **undefined**, the default value is used.

 |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onChange(deprecated)

onChange(callback: (value: DatePickerResult) => void)

Triggered when the date picker snaps to the selected item. This event cannot be triggered by two-way bound state variables.

This API is supported since API version 8 and deprecated since API version 10. You are advised to use [onDateChange](#ondatechange10) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | (value: [DatePickerResult](#datepickerresult)) => void | Yes | Selected time. |

#### \[h2\]onDateChange10+

onDateChange(callback: Callback<Date>)

Triggered when the date picker snaps to the selected item. This event cannot be triggered by two-way bound state variables.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../../common-definitions/basic-types/document.md#callback12)<Date> | Yes | Selected date, where the year, month, and day portions are subject to the selection, the hour and minute portions are subject to the current system time, and the second portion is always **00**. |

#### \[h2\]onDateChange18+

onDateChange(callback: Optional<Callback<Date>>)

Triggered when the date picker snaps to the selected item. This event cannot be triggered by two-way bound state variables. Compared to [onDateChange10+](#ondatechange10), this API supports the **undefined** type for the **callback** parameter.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/y9L95Tp6Sqik74U0sFFaiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B2EB089D18BFF1700F4DA0C3CE554477B47A49A3D198E11A0BE15527AEDCCC6)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[Callback](../../common-definitions/basic-types/document.md#callback12)<Date>> | Yes | 
Selected date, where the year, month, and day portions are subject to the selection, the hour and minute portions are subject to the current system time, and the second portion is always **00**.

If **callback** is set to **undefined**, the callback function is not used.

 |

#### DatePickerResult

Defines the time format returned by the date picker.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| year | number | No | Yes | 
Year of the selected date.

Value range: depends on **start** and **end**. If **start** and **end** are not set, the default range is \[1970, 2100\].

 |
| month | number | No | Yes | 

Zero-based month index of the selected date. **0** indicates January, and **11** indicates December.

Value range: depends on **start** and **end**. If **start** and **end** are not set, the default range is \[0, 11\].

 |
| day | number | No | Yes | 

Day of the selected date.

Value range: depends on **start** and **end**. If **start** and **end** are not set, the default range is \[1, 31\].

 |

#### Example

## Example 1: Switching Between Gregorian and Lunar Calendars

This example implements a date picker that allows users to switch between the Gregorian (solar) calendar and the lunar calendar by clicking a button.

// xxx.ets
@Entry
@Component
struct DatePickerExample {
  @State isLunar: boolean = false;
  private selectedDate: Date = new Date('2021-08-08');

  build() {
    Column() {
      Button('Switch Calendar')
        .margin({ top: 30, bottom: 30 })
        .onClick(() => {
          this.isLunar = !this.isLunar;
        })
      DatePicker({
        start: new Date('1970-1-1'),
        end: new Date('2100-1-1'),
        selected: this.selectedDate
      })
        .lunar(this.isLunar)
        .onDateChange((value: Date) => {
          this.selectedDate = value;
          console.info('select current date is: ' + value.toString());
        })

    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/7xuQvIuJTJW5FnjGHq-FkA/en-us_image_0000002537765608.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F5063F31063674A6910B85F196A4AFCE2A789C33CB57096F250DA5D5D102646A)

## Example 2: Setting the Text Style

This example shows how to customize the text style using [disappearTextStyle](#disappeartextstyle10), [textStyle](#textstyle10), and [selectedTextStyle](#selectedtextstyle10).

// xxx.ets
@Entry
@Component
struct DatePickerExample {
  private selectedDate: Date = new Date('2021-08-08');

  build() {
    Column() {
      DatePicker({
        start: new Date('1970-1-1'),
        end: new Date('2100-1-1'),
        selected: this.selectedDate
      })
        .disappearTextStyle({ color: Color.Gray, font: { size: '16fp', weight: FontWeight.Bold } })
        .textStyle({ color: '#ff182431', font: { size: '18fp', weight: FontWeight.Normal } })
        .selectedTextStyle({ color: '#ff0000FF', font: { size: '26fp', weight: FontWeight.Regular, family: "HarmonyOS Sans", style: FontStyle.Normal } })
        .onDateChange((value: Date) => {
          this.selectedDate = value;
          console.info('select current date is: ' + value.toString());
        })

    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/keWmuKmhT1Cp2TsvImnKOw/en-us_image_0000002537925548.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CCB33FD7E24C5697E2F7D57FEAF78C7B16600C6D1B97FBE81F3612801190CD8)

## Example 3: Displaying Year and Month, or Month and Day Columns

This example demonstrates how to display year and month, or month and day columns using **mode**.

The **mode** attribute of [DatePickerOptions](#datepickeroptions) is added since API version 18.

// xxx.ets
@Entry
@Component
struct DatePickerExample {
  @State isLunar: boolean = false;
  private selectedDate: Date = new Date('2025-01-15');
  @State datePickerModeList: (DatePickerMode)\[\] = \[
    DatePickerMode.DATE,
    DatePickerMode.YEAR\_AND\_MONTH,
    DatePickerMode.MONTH\_AND\_DAY,
  \];
  @State datePickerModeIndex: number = 0;

  build() {
    Column() {
      Button('Switch Calendar')
        .margin({ top: 30, bottom: 30 })
        .onClick(() => {
          this.isLunar = !this.isLunar;
        })
      DatePicker({
        start: new Date('1970-1-1'),
        end: new Date('2100-1-1'),
        selected: this.selectedDate,
        mode:this.datePickerModeList\[this.datePickerModeIndex\]
      })
        .lunar(this.isLunar)
        .onDateChange((value: Date) => {
          this.selectedDate = value;
          console.info('select current date is: ' + value.toString());
        })

      Button('mode :' + this.datePickerModeIndex).margin({ top: 20 })
        .onClick(() => {
          this.datePickerModeIndex++;
          if(this.datePickerModeIndex >= this.datePickerModeList.length){
            this.datePickerModeIndex = 0;
          }
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/E2JO0eoSTfarMqI8yPVFsA/en-us_image_0000002568685325.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B3351B26B0FE9EFDBA7FAA30A27A32D3657B82E1D6BEFA82EFDB292D7720AD96)

## Example 4: Setting Cyclic Scrolling

This example demonstrates how to set whether to enable cyclic scrolling using [canLoop](#canloop20), available since API version 20.

// xxx.ets
@Entry
@Component
struct DatePickerExample {
  @State isLoop: boolean = true;
  selectedDate: Date = new Date("2010-1-1");

  build() {
    Column() {
      DatePicker({
        start: new Date("2000-1-1"),
        end: new Date("2100-12-31"),
        selected: this.selectedDate,
      })
        .canLoop(this.isLoop)
        .onDateChange((value: Date) => {
            console.info("DatePicker:onDateChange()" + value.toString());
        })

      Row() {
        Text('Cyclic scrolling').fontSize(20)
        Toggle({ type: ToggleType.Switch, isOn: true })
          .onChange((isOn: boolean) => {
            this.isLoop = isOn;
          })
      }.position({ x: '60%', y: '40%' })
    }.width('100%')
  }
}
