# CalendarPicker

The **CalendarPicker** component provides a drop-down calendar for users to select a date.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/dPUftji6TgmBcWrSSaKd9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5310C1AE551081405B54846B17EFEF67ED231F16B496E2D9F346CB752C34666F)

This component is supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

CalendarPicker(options?: CalendarOptions)

Creates a calendar picker.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [CalendarOptions](#calendaroptions) | No | Parameters of the calendar picker. |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]edgeAlign

edgeAlign(alignType: CalendarAlign, offset?: Offset)

Sets how the picker is aligned with the entry component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| alignType | [CalendarAlign](#calendaralign) | Yes | 
Alignment type.

Default value: **CalendarAlign.END**

 |
| offset | [Offset](../../common-definitions/basic-types/document.md#offset) | No | 

Offset of the picker relative to the entry component after alignment based on the specified alignment type.

Default value: **{dx: 0, dy: 0}**

 |

#### \[h2\]edgeAlign18+

edgeAlign(alignType: Optional<CalendarAlign>, offset?: Offset)

Sets how the picker is aligned with the entry component. Compared with [edgeAlign](#edgealign), this API supports the **undefined** type for the **alignType** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| alignType | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[CalendarAlign](#calendaralign)\> | Yes | 
Alignment type.

Default value: **CalendarAlign.END**

If the value of **alignType** is **undefined**, the default value is used.

 |
| offset | [Offset](../../common-definitions/basic-types/document.md#offset) | No | 

Offset of the picker relative to the entry component after alignment based on the specified alignment type.

Default value: **{dx: 0, dy: 0}**

 |

#### \[h2\]textStyle

textStyle(value: PickerTextStyle)

Sets the font color, font size, and font weight in the entry area.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [PickerTextStyle](../picker-common-apis/document.md#pickertextstyle) | Yes | 
Font color, font size, and font weight in the entry area.

Default value:

{

color: '#ff182431',

font: {

size: '16fp',

weight: FontWeight.Regular

}

}

 |

#### \[h2\]textStyle18+

textStyle(style: Optional<PickerTextStyle>)

Sets the font color, font size, and font weight in the entry area. Compared with [textStyle](#textstyle), this API supports the **undefined** type for the **style** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[PickerTextStyle](../picker-common-apis/document.md#pickertextstyle)\> | Yes | 
Font color, font size, and font weight in the entry area.

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

#### \[h2\]markToday19+

markToday(enabled: boolean)

Sets whether to highlight the current system date.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | 
Whether to highlight the current system date.

\- **true**: Highlight the current system date.

\- **false**: Do not highlight the current system date.

Default value: **false**

 |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onChange

onChange(callback: Callback<Date>)

Triggered when a date is selected. This event cannot be triggered by two-way bound state variables.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../../common-definitions/basic-types/document.md#callback12)<Date> | Yes | Selected date value. |

#### \[h2\]onChange18+

onChange(callback: Optional<Callback<Date>>)

Triggered when a date is selected. This event cannot be triggered by two-way bound state variables. Compared with [onChange](#onchange), this API supports the **undefined** type for the **callback** parameter.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/knO10QD_Rne4mkXn8kkovg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3743005BC6FE855710BF6F0DD52E3E397B3D5FDD3D7184F60095A8FA651184C9)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[Callback](../../common-definitions/basic-types/document.md#callback12)<Date>> | Yes | 
Selected date value.

If **callback** is set to **undefined**, the callback function is not used.

 |

#### CalendarOptions

Describes the parameters of the calendar picker.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| hintRadius | number | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 
Style of the background of the selected state.

Value range: \[0.0, 16.0\]

Unit: vp.

Default value: **16.0** (the background is a circle).

**NOTE**

If the value is **0.0**, the background is a right-angled rectangle. If the value is in the (0.0, 16.0) range, the background is a rounded rectangle. If the value is a negative number or greater than 16.0, the default value **16.0** is used, which means the background is a circle.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| selected | Date | No | Yes | 

Date of the selected item. If the value is not set or does not comply with the date format specifications, the default value will be used.

Default value: current system date

Value range: \[Date('0001-01-01'), Date('5000-12-31')\]

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| start18+ | Date | No | Yes | 

Start date.

Default value: **Date('0001-01-01')**

Value range: \[Date('0001-01-01'), Date('5000-12-31')\]

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| end18+ | Date | No | Yes | 

End date.

Default value: **Date('5000-12-31')**

Value range: \[Date('0001-01-01'), Date('5000-12-31')\]

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| disabledDateRange19+ | [DateRange](../picker-common-apis/document.md#daterange19)\[\] | No | Yes | 

Disabled date range.

**NOTE**

1\. If the start date or end date within a date range is invalid or is not set, the entire date range does not take effect.

2\. If the end date is earlier than the start date within a date range, the entire date range does not take effect.

3\. When users select a date and adjust it with the up or down arrow keys, the system skips over all dates in the disabled date range.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |

**Rules for setting start and end**

| Scenario | Description |
| :-- | :-- |
| The start date is later than the end date. | Both start and end dates are invalid, and the selected date is the default value. |
| The selected date is earlier than the start date. | The selected date is set as the start date. |
| The selected date is later than the end date. | The selected date is set as the end date. |
| The start date is later than the current system date, and the selected date is not set. | The selected date is set as the start date. |
| The end date is earlier than the current system date, and the selected date is not set. | The selected date is set as the end date. |
| The set date is in invalid format, for example, **'1999-13-32'**. | The start or end date setting is invalid, and the selected date is the default value. |

#### CalendarAlign

Enumerates alignment types.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Value | Description |
| :-- | :-- | :-- |
| START | 0 | Left-aligned with the entry component. |
| CENTER | 1 | Center-aligned with the entry component. |
| END | 2 | Right-aligned with the entry component. |

#### Example

## Example 1: Implementing a Calendar Picker

This example uses **calendarPicker** to implement the **CalendarPicker** component and provides a drop-down calendar.

// xxx.ets
@Entry
@Component
struct CalendarPickerExample {
  private selectedDate: Date = new Date('2024-03-05');

  build() {
    Column() {
      Column() {
        CalendarPicker({ hintRadius: 10, selected: this.selectedDate })
          .edgeAlign(CalendarAlign.END)
          .textStyle({ color: "#ff182431", font: { size: 20, weight: FontWeight.Normal } })
          .margin(10)
          .onChange((value) => {
            console.info(\`CalendarPicker onChange: ${value.toString()}\`);
          })
      }.alignItems(HorizontalAlign.End).width("100%")

      Text('Calendar picker').fontSize(30)
    }.width('100%').margin({ top: 350 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/UxXYhTFMSJanRWYPZCaniA/en-us_image_0000002568765333.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47CEECC57D5273E21FFB45B03FB7F8A4EBF4729B9F8BEA74E34C3DF06792AE34)

## Example 2: Setting Start and End Dates

This example demonstrates how to set the start and end dates for the calendar picker using **start** and **end**.

Since API version 18, the **start** and **end** attributes are added to [CalendarOptions](#calendaroptions).

// xxx.ets
@Entry
@Component
struct CalendarPickerExample {
  private selectedDate: Date = new Date('2025-01-15');
  private startDate: Date = new Date('2025-01-05');
  private endDate: Date = new Date('2025-01-25');

  build() {
    Column() {
      Column() {
        CalendarPicker({ hintRadius: 10, selected: this.selectedDate, start: this.startDate, end: this.endDate })
          .edgeAlign(CalendarAlign.END)
          .textStyle({ color: "#ff182431", font: { size: 20, weight: FontWeight.Normal } })
          .margin(10)
          .onChange((value) => {
            console.info(\`CalendarPicker onChange: ${value.toString()}\`);
          })
      }.alignItems(HorizontalAlign.End).width("100%")
    }.width('100%').margin({ top: 350 })
  }
}

## Example 3: Highlighting the Current System Date and Disabling a Specific Date Range

This example shows how to highlight the current system date using **markToday** and disable a specific date range using **disabledDateRange**.

Since API version 19, the [markToday](#marktoday19) API is added, and the **disabledDateRange** attribute is added to [CalendarOptions](#calendaroptions).

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
      CalendarPicker({ disabledDateRange: this.disabledDateRange })
        .margin(10)
        .markToday(true)
        .onChange((value) => {
          console.info(\`CalendarPicker onChange: ${value.toString()}\`);
        })
    }.alignItems(HorizontalAlign.End).width('100%')
  }
}
