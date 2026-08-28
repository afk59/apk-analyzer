# TimePicker

**TimePicker** is a component that allows users to select a time from the given range through scrolling.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/YkUxdg9sRm-Q4oq4OUhOgg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC0E9065E76029C539B6A392F9FA40EBE64779A701CE57554D920677F0E6BCD1)

-   This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   Avoid changing component attributes during animation processes.
    
-   The maximum number of rows that can be displayed varies by screen orientation: In portrait mode, the default number of rows is 5. In landscape mode, the number of rows depends on the system configuration. If no system configuration is set, the default is 3 rows. To check the specific system configuration value for landscape mode, use **$r('sys.float.ohos\_id\_picker\_show\_count\_landscape')**.
    

#### Child Components

Not supported

#### APIs

TimePicker(options?: TimePickerOptions)

Creates a time picker, which uses the 24-hour time format by default.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TimePickerOptions](#timepickeroptions) | No | Parameters of the time picker. |

#### TimePickerOptions

Describes the parameters of the time picker.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| selected | Date | No | Yes | 
Time of the selected item.

Default value: current system time

Since API version 10, this parameter supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| format11+ | [TimePickerFormat](#timepickerformat11) | No | Yes | 

Time format.

Default value: **TimePickerFormat.HOUR\_MINUTE**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| start18+ | Date | No | Yes | 

Start time of the time picker.

Default value: **Date(0, 0, 0, 0, 0, 0)**

**NOTE**

1\. Only the hour and minute values take effect.

2\. If **start** is set and is not the default value, **loop** does not take effect.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| end18+ | Date | No | Yes | 

End time of the time picker.

Default value: **Date(0, 0, 0, 23, 59, 59)**.

**NOTE**

1\. Only the hour and minute values take effect.

2\. If **end** is set and is not the default value, **loop** does not take effect.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

Property modifications made to **TimePickerOptions** during the **TimePicker** scrolling process may not take effect.

The **Date** object is used to handle dates and time. It can be used in the following ways:

**Method 1**: new Date ()

Obtains the current system date and time.

**Method 2**: new Date(value: number | string)

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | Yes | 
Date format.

**number**: number of milliseconds since 00:00:00 on January 1, 1970.

**string**: date string in formats such as 2025-02 2025-02-20 08:00:00 or 2025-02 2025-02-20T08:00:00.

 |

**Method 3**: new Date(year: number, monthIndex: number, date?: number, hours?: number, minutes?: number, seconds?: number, ms?: number)

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| year | number | Yes | Year, for example, **2025**. |
| monthIndex | number | Yes | Month index, for example, **2** for March. |
| date | number | No | Date, for example, **10** (if **hours** is set, **date** cannot be omitted). |
| hours | number | No | Hour, for example, **15** (if **minutes** is set, **hours** cannot be omitted). |
| minutes | number | No | Minute, for example, **20** (if **seconds** is set, **minutes** cannot be omitted). |
| seconds | number | No | Second, for example, **20** (if **ms** is set, **seconds** cannot be omitted). |
| ms | number | No | Millisecond, for example, **10**. |

**Handling in the case of date configuration exceptions**

| Exception | Result |
| :-- | :-- |
| The start time is later than the end time. | Both start time and end time are set to their default values. |
| The selected time is earlier than the start time. | The selected time is set to the start time. |
| The selected time is later than the end time. | The selected time is set to the end time. |
| The start time is later than the current system time, and the selected time is not set. | The selected time is set to the start time. |
| The end time is earlier than the current system time, and the selected time is not set. | The selected time is set to the end time. |
| The time format is invalid, such as **'01:61:61'**. | The default value is used. |

#### TimePickerFormat11+

Enumerates time display formats of the time picker.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| HOUR\_MINUTE | 0 | Time format displaying hours and minutes. |
| HOUR\_MINUTE\_SECOND | 1 | Time format displaying hours, minutes, and seconds. |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]useMilitaryTime

useMilitaryTime(value: boolean)

Sets whether the time is displayed in 24-hour format. If this attribute is not set, the time is displayed in the system time format by default.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to display the time in 24-hour format or 12-hour format.

\- **true**: 24-hour format.

\- **false**: 12-hour format.

 |

#### \[h2\]useMilitaryTime18+

useMilitaryTime(isMilitaryTime: Optional<boolean>)

Whether the displayed time is in 24-hour format. If this API is not called to set the time format, the system setting is used by default. Compared with [useMilitaryTime](#usemilitarytime), this API supports the **undefined** type for the **isMilitaryTime** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isMilitaryTime | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to display the time in 24-hour format or 12-hour format.

\- **true**: 24-hour format.

\- **false**: 12-hour format.

When the value of isMilitaryTime is undefined, the system setting is used.

 |

#### \[h2\]disappearTextStyle10+

disappearTextStyle(value: PickerTextStyle)

Sets the text color, font size, and font weight of edge items (the second item above or below the selected item).

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/jPuEwvwQScWbZiyPlzjU3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D473FD4B105520842A8C2EA0AB622F4FA008D04F9EAB3670917A4C6FDE75701)

Edge items only appear when there are at least two visible items above or below the selected item. If insufficient items are available, no edge items will be styled.

#### \[h2\]disappearTextStyle18+

disappearTextStyle(style: Optional<PickerTextStyle>)

Sets the text color, font size, and font weight of edge items (the second item above or below the selected item). Compared with [disappearTextStyle10+](#disappeartextstyle10), this API supports the **undefined** type for the **style** parameter.

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/7q8ESu3kS_q4V-QxhPiw9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD6192AB22D2551A7C572A4E7AEC004965F5D6A45E7CDBA6AB7F172B647D8D3B)

Edge items only appear when there are at least two visible items above or below the selected item. If insufficient items are available, no edge items will be styled.

#### \[h2\]textStyle10+

textStyle(value: PickerTextStyle)

Text color, font size, and font weight of candidate items (the first item immediately above or below the selected item).

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/qR6-NO28TBm02BrQpy1xrQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D488825C36EBEEF5677AECA6471AFAC13F29C5387C31FA684FF28186C061DAA)

Candidate items only appear when there is at least one visible item above or below the selected item. If insufficient items are available, no candidate items will be styled.

#### \[h2\]textStyle18+

textStyle(style: Optional<PickerTextStyle>)

Sets the text color, font size, and font weight of candidate items (the first item immediately above or below the selected item). Compared with [textStyle10+](#textstyle10), this API supports the **undefined** type for the **style** parameter.

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/p_0mg04OSOeT8iAtNIhPPg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=064DD5AF43B6FED4774EF269E711CD1D37935F0BB8EA78EEC9EE3D53004D9537)

Candidate items only appear when there is at least one visible item above or below the selected item. If insufficient items are available, no candidate items will be styled.

#### \[h2\]selectedTextStyle10+

selectedTextStyle(value: PickerTextStyle)

Sets the text color, font size, and font weight of the selected item.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior**: This API has no effect on wearables and works on other devices.

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

Sets the text color, font size, and font weight of the selected item. Compared with [selectedTextStyle10+](#selectedtextstyle10), this API supports the **undefined** type for the **style** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior**: This API has no effect on wearables and works on other devices.

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

#### \[h2\]loop11+

loop(value: boolean)

Sets whether to enable loop scrolling.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable loop scrolling.

\- **true**: Enable loop scrolling.

\- **false**: Disable loop scrolling.

Default value: **true**.

 |

#### \[h2\]loop18+

loop(isLoop: Optional<boolean>)

Sets whether to enable loop scrolling. Compared with [loop11+](#loop11), this API supports the **undefined** type for the **isLoop** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isLoop | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to enable loop scrolling.

\- **true**: Enable loop scrolling.

\- **false**: Disable loop scrolling.

Default value: **true**.

If the value of **isLoop** is **undefined**, the default value is used.

 |

#### \[h2\]dateTimeOptions12+

dateTimeOptions(value: DateTimeOptions)

Sets whether to display a leading zero for the hours, minutes, and seconds.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [DateTimeOptions](#datetimeoptions12) | Yes | 
Whether to display a leading zero for the hours, minutes, and seconds.

Default value:

**hour**: For the 24-hour format, the default value is **"2-digit"**, meaning the hour is displayed as a two-digit number. If the actual value is less than 10, a leading zero is added, displayed as "0X". For the 12-hour format, the default value is **"numeric"**, meaning no leading zero.

**minute**: The default value is **"2-digit"**, meaning the minute is displayed as a two-digit number. If the actual value is less than 10, a leading zero is added, displayed as "0X".

**second**: The default value is **"2-digit"**, meaning the minute is displayed as a two-digit number. If the actual value is less than 10, a leading zero is added, displayed as "0X".

If **hour**, **minute**, or **second** is set to **undefined**, the display follows the default rules.

 |

#### \[h2\]dateTimeOptions18+

dateTimeOptions(timeFormat: Optional<DateTimeOptions>)

Sets whether to display a leading zero for the hours, minutes, and seconds. Compared with [dateTimeOptions12+](#datetimeoptions12), this API supports the **undefined** type for the **timeFormat** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timeFormat | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[DateTimeOptions](#datetimeoptions12)\> | Yes | 
Whether to display a leading zero for the hours, minutes, and seconds. Currently only the configuration of the **hour**, **minute**, and **second** parameters is supported.

Default value:

**hour**: For the 24-hour format, the default value is **"2-digit"**, meaning the hour is displayed as a two-digit number. If the actual value is less than 10, a leading zero is added, displayed as "0X". For the 12-hour format, the default value is **"numeric"**, meaning no leading zero.

**minute**: The default value is **"2-digit"**, meaning the minute is displayed as a two-digit number. If the actual value is less than 10, a leading zero is added, displayed as "0X".

**second**: The default value is **"2-digit"**, meaning the minute is displayed as a two-digit number. If the actual value is less than 10, a leading zero is added, displayed as "0X".

If **hour**, **minute**, or **second** is set to **undefined**, the display follows the default rules.

 |

#### \[h2\]enableHapticFeedback12+

enableHapticFeedback(enable: boolean)

Sets whether to enable haptic feedback.

To enable haptic feedback, you must declare the following permission under **requestPermissions** in **module** in **src/main/module.json5** of the project.

"requestPermissions": \[
   {
      "name": "ohos.permission.VIBRATE",
   }
\]

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/d4_tjaVQRAGhuB-0jtD9yQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A73D9139812B238D3342ADBBA331445377ED4632921F4445F285167F8C20ECA5)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether to enable haptic feedback.

\- **true**: Enable haptic feedback.

\- **false**: Disable haptic feedback.

Default value: **true**.

Whether this parameter takes effect after being set to **true** depends on hardware support.

 |

#### \[h2\]enableHapticFeedback18+

enableHapticFeedback(enable: Optional<boolean>)

Sets whether to enable haptic feedback. Compared with [enableHapticFeedback12+](#enablehapticfeedback12), this API supports the **undefined** type for the **enable** parameter.

To enable haptic feedback, you must declare the following permission under **requestPermissions** in **module** in **src/main/module.json5** of the project.

"requestPermissions": \[
  {
    "name": "ohos.permission.VIBRATE",
  }
\]

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to enable haptic feedback.

\- **true**: Enable haptic feedback.

\- **false**: Disable haptic feedback.

Default value: **true**.

If the value of **enable** is **undefined**, the default value is used.

Whether this parameter takes effect after being set to **true** depends on hardware support.

 |

#### \[h2\]enableCascade18+

enableCascade(enabled: boolean)

Sets whether the AM/PM indicator automatically switches based on the hour value. Only takes effect when [useMilitaryTime](#usemilitarytime) is set to **false**.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | 
Sets whether the AM/PM indicator automatically switches based on the hour value. This setting only takes effect when **useMilitaryTime** is set to **false**.

\- **true**: The AM/PM indicator automatically switches based on the hour value.

\- **false**: The AM/PM indicator remains static regardless of hour changes.

Default value: **false**.

When **enabled** is set to **true**, it only takes effect if the **loop** parameter is also **true**.

 |

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/L4zHODZURWGWmo31cHs9Qw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B569F373A2035D5FB10FA4E25FB3D2C88BB3F9F64001F5E42CEFB17559EE8CD2)

This API is used for circular screens on wearables. The component needs to obtain focus before responding to the [crown event](../../universal-events/basic-input-events/crown-event/document.md).

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onChange

onChange(callback: (value: TimePickerResult ) => void)

Triggered when the time picker snaps to the selected item. This event cannot be triggered by two-way bound state variables.

This callback is triggered only after the scroll animation completes. To obtain real-time index changes, use [onEnterSelectedArea](#onenterselectedarea18) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [TimePickerResult](#timepickerresult) | Yes | Time in 24-hour format. |

#### \[h2\]onChange18+

onChange(callback: Optional<OnTimePickerChangeCallback>)

Triggered when the time options in the TimePicker rest on the selected position after scrolling. This event cannot be triggered by two-way bound state variables. Compared with [onChange](#onchange), the **callback** parameter supports the **undefined** type.

This callback is triggered only after the scroll animation completes. To obtain real-time index changes, use [onEnterSelectedArea](#onenterselectedarea18) instead.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[OnTimePickerChangeCallback](#ontimepickerchangecallback18)\> | Yes | 
Callback invoked when a time option is selected.

If **callback** is set to **undefined**, the callback function is not used.

 |

#### \[h2\]onEnterSelectedArea18+

onEnterSelectedArea(callback: Callback<TimePickerResult>)

Triggered during the scrolling of the time picker when an item enters the divider area.

Compared with the [onChange](#onchange) event, this event is triggered earlier, specifically when the scroll distance of the current column exceeds half the height of the selected item, which indicates that the item has entered the divider area. When [enableCascade](#enablecascade18) is set to **true**, using this callback is not recommended due to the interdependent relationship between the AM/PM and hour columns. This callback indicates the moment an option enters the divider area during scrolling, and only the value of the currently scrolled column will change. The values of other non-scrolled columns will remain unchanged.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/_GCqR9MFRxijgEl1I7J6eg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2ACD8B18DD360E0E1EFC41642657A0FA9BD8DF377018CE3378E83E0D2AB7BCCF)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[TimePickerResult](#timepickerresult)\> | Yes | Callback triggered during the scrolling of the time picker when an item enters the divider area. |

#### DateTimeOptions12+

type DateTimeOptions = DateTimeOptions

Defines the options for a **DateTimeOptions** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [DateTimeOptions](../../../../localization-kit/arkts-apis/ohos-intl-internationalization/document.md#datetimeoptionsdeprecated) | Options for creating the **DateTimeOptions** object. |

#### OnTimePickerChangeCallback18+

type OnTimePickerChangeCallback = (result: TimePickerResult) => void

Triggered when a time is selected.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| result | [TimePickerResult](#timepickerresult) | Yes | Time in 24-hour format. |

#### TimePickerResult

Describes a time in 24-hour format.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| hour | number | No | No | 
Hour portion of the selected time.

Value range: \[0-23\]

 |
| minute | number | No | No | 

Minute portion of the selected time.

Value range: \[0-59\]

 |
| second11+ | number | No | No | 

Second portion of the selected time.

Value range: \[0-59\]

 |

#### Example

## Example 1: Setting the Text Style

This example demonstrates how to configure [disappearTextStyle](#disappeartextstyle10), [textStyle](#textstyle10), and [selectedTextStyle](#selectedtextstyle10) to customize the text style in a time picker.

// xxx.ets
@Entry
@Component
struct TimePickerExample {
  private selectedTime: Date = new Date('2022-07-22T08:00:00');

  build() {
    TimePicker({
      selected: this.selectedTime
    })
      .disappearTextStyle({ color: '#004aaf', font: { size: 24, weight: FontWeight.Lighter } })
      .textStyle({ color: Color.Black, font: { size: 26, weight: FontWeight.Normal } })
      .selectedTextStyle({ color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } })
      .onChange((value: TimePickerResult) => {
        if (value.hour >= 0) {
          this.selectedTime.setHours(value.hour, value.minute);
          console.info('select current date is: ' + JSON.stringify(value));
        }
      })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/f90FGUl0RUyolxm3ZrIErg/en-us_image_0000002568685331.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=583A1E47CD3AB38E3D07BCBAD1F789296E915D2678FBD0886013374D85E9B879)

## Example 2: Switching Between 12-Hour and 24-Hour Formats

This example demonstrates how to switch between 12-hour and 24-hour formats using **useMilitaryTime**.

// xxx.ets
@Entry
@Component
struct TimePickerExample {
  @State isMilitaryTime: boolean = false;
  private selectedTime: Date = new Date('2022-07-22T08:00:00');

  build() {
    Column() {
      Button('Switch Time Format')
        .margin(30)
        .onClick(() => {
          this.isMilitaryTime = !this.isMilitaryTime;
        })

      TimePicker({
        selected: this.selectedTime
      })
        .useMilitaryTime(this.isMilitaryTime)
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current time is: ' + JSON.stringify(value));
          }
        })
        .onEnterSelectedArea((value: TimePickerResult) => {
            console.info('item enter selected area, time is: ' + JSON.stringify(value));
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/-dhtv6OgQbKytRwhN8EvwQ/en-us_image_0000002568765341.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B006E762050746395F9C5D78C832D87790AD08D85155C23B457C78FD2B251F5E)

## Example 3: Setting the Time Format

This example shows how to set the time format using **format** and **dateTimeOptions**.

// xxx.ets
@Entry
@Component
struct TimePickerExample {
  private selectedTime: Date = new Date('2022-07-22T08:00:00');

  build() {
    Column() {
      TimePicker({
        selected: this.selectedTime,
        format: TimePickerFormat.HOUR\_MINUTE\_SECOND
      })
        .dateTimeOptions({ hour: "numeric", minute: "2-digit", second: "2-digit" })
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current date is: ' + JSON.stringify(value));
          }
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/ac64OWJ9QgywkqW9loZhAA/en-us_image_0000002537765616.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6382F7DDC2CF9CB7F00C9CB464B898532712A2F906AA96EFF6816B5F528DF66)

## Example 4: Setting Loop Scrolling

This example demonstrates how to set whether to enable loop scrolling using [loop](#loop11).

// xxx.ets
@Entry
@Component
struct TimePickerExample {
  @State isLoop: boolean = true;
  @State selectedTime: Date = new Date('2022-07-22T12:00:00');

  build() {
    Column() {
      TimePicker({
        selected: this.selectedTime
      })
        .loop(this.isLoop)
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current date is: ' + JSON.stringify(value));
          }
        })

      Row() {
        Text('Loopable scrolling').fontSize(20)

        Toggle({ type: ToggleType.Switch, isOn: true })
          .onChange((isOn: boolean) => {
            this.isLoop = isOn;
          })
      }.position({ x: '60%', y: '40%' })

    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/r6nZ_ObwSFuitO-L25Q3pw/en-us_image_0000002537925556.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D644B22003F69B4B2BBEAE38C599DECD1DEEA68F1F1E36570E56711E9C4D382)

## Example 5: Setting the Start Time

This example demonstrates how to set the start time for the time picker.

// xxx.ets
@Entry
@Component
struct TimePickerExample {
  private selectedTime: Date = new Date('2022-07-22T08:50:00');

  build() {
    Column() {
      TimePicker({
        selected: this.selectedTime,
        format: TimePickerFormat.HOUR\_MINUTE\_SECOND,
        start: new Date('2022-07-22T08:30:00')
      })
        .dateTimeOptions({ hour: "numeric", minute: "2-digit", second: "2-digit" })
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current date is: ' + JSON.stringify(value));
          }
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/nz2FhsTLSgi4ifA5RSKFuA/en-us_image_0000002568685333.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC8E353422141912ED96FF9D7813122F91CC7F22463551D89FB59C377B108F8A)

## Example 6: Setting the End Time

This example demonstrates how to set the end time for the time picker.

// xxx.ets
@Entry
@Component
struct TimePickerExample {
  private selectedTime: Date = new Date('2022-07-22T08:50:00');

  build() {
    Column() {
      TimePicker({
        selected: this.selectedTime,
        format: TimePickerFormat.HOUR\_MINUTE\_SECOND,
        end: new Date('2022-07-22T15:20:00'),
      })
        .dateTimeOptions({ hour: "numeric", minute: "2-digit", second: "2-digit" })
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current date is: ' + JSON.stringify(value));
          }
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/GI2XveOyRPqCENPUxqJ27w/en-us_image_0000002568765343.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A624A054A8BEF5B4FC0026ADA851DFEB80FB83E06DC6FF6C60030CAF3B71C358)

## Example 7: Enabling the AM/PM Indicator to Automatically Switch Based on the Hour Value in 12-hour Format

This example demonstrates how to enable the AM/PM indicator to automatically switch based on the hour value in 12-hour format using [enableCascade](#enablecascade18) and [loop](#loop11).

The **enableCascade** API is added since API version 18.

// xxx.ets
@Entry
@Component
struct TimePickerExample {
  private selectedTime: Date = new Date('2022-07-22T08:00:00');

  build() {
    Column() {
      TimePicker({
        selected: this.selectedTime,
      })
        .enableCascade(true)
        .loop(true)
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current date is: ' + JSON.stringify(value));
          }
        })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/0jItL5YpTGqR6wbLGEFklw/en-us_image_0000002537765618.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD0731C5A37274E2017AB058ECBE6D4572921AEAAE33FFFE75EFE23A94427BDA)
