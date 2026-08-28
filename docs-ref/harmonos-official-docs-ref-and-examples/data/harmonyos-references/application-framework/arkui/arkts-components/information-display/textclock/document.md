# TextClock

The **TextClock** component displays the current system time in text format for different time zones. The time is accurate to seconds.

When the component is invisible, the time change stops. The visible status of a component is processed based on [onVisibleAreaChange](../../universal-events/component-change-events/visible-area-change-event/document.md#onvisibleareachange). If the visible threshold **ratios** is greater than 0, the component is visible.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/hC_HDRraQgGKkldCN5Vh7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C30FA675986D2A2B9242B1365702A77E482B734D31FC43DA90B9C351E270F96)

This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

TextClock(options?: TextClockOptions)

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TextClockOptions](#textclockoptions18) | No | Options of the text clock. |

#### TextClockOptions18+

Options used to build the **TextClock** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/EaBjebp5R7qut19bd008lA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD34395D659C5E4CEA81D11AC16CBB86758514014A17492557A6A1D8663A5763)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| timeZoneOffset8+ | number | No | Yes | 
Time zone offset.

The value range is \[-14, 12\], indicating UTC+12 to UTC-12. A negative value indicates Eastern Standard Time, and a positive value indicates Western Standard Time. For example, **\-8** indicates UTC+8. If the value is a floating point number within the value range, it is rounded off, with the decimal portion discarded.

For countries or regions crossing the International Date Line, use -13 (UTC+13) and -14 (UTC+14) to ensure time consistency across the country or region. If the set value is not within the valid range, the time zone offset of the current system will be used.

Default value: time zone offset of the current system

The value is not rounded when it is a floating point number in the { 9.5, 3.5, -3.5, -4.5, -5.5, -5.75, -6.5, -9.5, -10.5, -12.75 } set.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| controller8+ | [TextClockController](#textclockcontroller) | No | Yes | 

Controller to control the status of the **<TextClock>** component.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]format

format(value: ResourceStr)

Sets the time format, for example, **yyyy/MM/dd** or **yyyy-MM-dd**.

**y**: year (yyyy indicates the complete year, and yy indicates the last two digits of the year.)

**M**: month (To display 01 for January, use **MM** instead.)

**d**: day (To display 01 for the first day, use **dd** instead.)

**E**: day of week (To display the full name, use **EEEE**; to display the abbreviation, use **E**, **EE**, or **EEE**.)

H: hour (24-hour format); h: hour (12-hour format)

**m**: minute

**s**: second

SS: centisecond (If the number of S characters in the format is less than 3, all are treated as centiseconds.)

SSS: millisecond (If the number of S characters in the format is greater than or equal to 3, all are treated as milliseconds.)

**a**: morning/afternoon (This parameter does not take effect when the hour part is set to **H**.)

Date separators: year, month, day, slash (/), hyphen (-), and period (.) (Custom separator styles are allowed. Letters cannot be used as separators, while Chinese characters can be treated as separators.)

The parts of the date can be used alone or combined with each other as needed. The time can be updated as frequent as once per second. As such, whenever possible, avoid setting the centisecond and millisecond parts separately.

When an invalid letter is set, the letter is ignored. If all letters in **format** are invalid, the display format follows the system's language and hour format settings.

If **format** is an empty string ("") or **undefined**, the default value is used.

Default value outside of widgets: 12-hour format: aa hh:mm:ss; 24-hour format: HH:mm:ss.

Default value in widgets: 12-hour format: hh:mm, 24-hour format: HH:mm.

When used in widgets, the minimum time unit is minute. In this case, if the format contains seconds or centiseconds, the default value will be used.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 
Time format to set.

The Resource type is supported since API version 20.

 |

The following table shows how different settings of **format** work out.

| Input Format | Display Effect |
| :-- | :-- |
| EEEE, M, d, yyyy | Saturday, February 4, 2023 |
| MMM d, yyyy | February 4, 2023 |
| EEEE, M, d | Saturday, February 4 |
| MMM dd | February 4 |
| MM/dd/yyyy | 02/04/2023 |
| EEEE MM dd | Saturday February 04 |
| yyyy | 2023 |
| yy | 23 |
| MM | February |
| M | February |
| dd (complete date) | 04 |
| d | 4 |
| EEEE (full name) | Saturday |
| E, EE, EEE (abbreviation) | Sat |
| MMM d, yyyy | February 4, 2023 |
| yyyy/M/d | 2023/2/4 |
| yyyy-M-d | 2023-2-4 |
| yyyy.M.d | 2023.2.4 |
| HH:mm:ss | 17:00:04 |
| aa hh:mm:ss | 5:00:04 AM |
| hh:mm:ss | 5:00:04 |
| HH:mm | 17:00 |
| aa hh:mm | 5:00 AM |
| hh:mm | 5:00 |
| mm:ss | 00:04 |
| mm:ss.SS | 00:04.91 |
| mm:ss.SSS | 00:04.536 |
| hh:mm:ss aa | 5:00:04 AM |
| HH | 17 |

#### \[h2\]fontColor

fontColor(value: ResourceColor)

Sets the font color.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Font color.

Default value for wearables: '#c5ffffff'; default value for other devices: 'e6182431'

 |

#### \[h2\]fontSize

fontSize(value: Length)

Sets the font size.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | Font size. If **fontSize** is of the number type, the unit fp is used. The default font size is 16 fp. The value cannot be a percentage. |

#### \[h2\]fontStyle

fontStyle(value: FontStyle)

Sets the font style.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [FontStyle](../../common-definitions/enums/document.md#fontstyle) | Yes | 
Font style.

Default value: **FontStyle.Normal**, indicating the standard font style (non-italic)

 |

#### \[h2\]fontWeight

fontWeight(value: number | FontWeight | string)

Sets the font weight of the text. If the value is too large, the text in different fonts may be truncated.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [FontWeight](../../common-definitions/enums/document.md#fontweight) | string | Yes | 
Font width of the text. The value range of the number type is \[100, 900\]. The value interval is 100. A larger value indicates a wider font. If the value of the number type is not within the value range, the default value is **400**. For the string type, only strings that represent a number, for example, **"400"**, and the following enumerated values of **FontWeight** are supported: **"bold"**, **"bolder"**, **"lighter"**, **"regular"**, and **"medium"**.

Default value: **FontWeight.Normal**

 |

#### \[h2\]fontFamily

fontFamily(value: ResourceStr)

Sets the font family.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 
Font family. Default font: **'HarmonyOS Sans'**

The 'HarmonyOS Sans' font and [registered custom fonts](../../../arkts-api/ui/ohos-font-custom-font-registration/document.md) are supported for applications.

Only the 'HarmonyOS Sans' font is supported for widgets.

 |

#### \[h2\]textShadow11+

textShadow(value: ShadowOptions | Array<ShadowOptions>)

Sets the text shadow. It supports input parameters in an array to implement multiple text shadows. This API does not work with the **fill** attribute or coloring strategy.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ShadowOptions](../../universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | Array<[ShadowOptions](../../universal-attributes/visual-effects/image-effect/document.md#shadowoptions)\> | Yes | Font shadow of the text. |

#### \[h2\]fontFeature11+

fontFeature(value: string)

Sets the font feature, for example, monospaced digits.

Format: normal | <feature-tag-value>

Format of **<feature-tag-value>**: <string> \[ <integer> | on | off \]

There can be multiple **<feature-tag-value>** values, which are separated by commas (,).

For example, the input format for monospaced clock fonts is "ss01" on.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Font feature. |

#### \[h2\]contentModifier12+

contentModifier(modifier: ContentModifier<TextClockConfiguration>)

Creates a content modifier.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [ContentModifier<TextClockConfiguration>](#textclockconfiguration12) | Yes | 
Content modifier to apply to the text clock.

**modifier**: content modifier. You need to customize a class to implement the **ContentModifier** API.

 |

#### \[h2\]dateTimeOptions12+

dateTimeOptions(dateTimeOptions: Optional<DateTimeOptions>)

Sets whether to display a leading zero for the hour.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dateTimeOptions | Optional<[DateTimeOptions](../../../../localization-kit/arkts-apis/ohos-intl-internationalization/document.md#datetimeoptionsdeprecated)\> | Yes | 
Whether to display leading zeros in the hour. It only supports setting the **hour** parameter. When the parameter value is **{hour: "2-digit"}**, a leading zero is displayed. When the parameter value is **{hour: "numeric"}**, no leading zero is displayed.

Default value: **undefined**. By default, leading zeros are displayed in 24-hour format, but not displayed in 12-hour format.

 |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onDateChange

onDateChange(event: (value: number) => void)

Triggered when the time changes.

This event does not take effect when the component is invisible.

If the event is not used in a widget, it is triggered when the change occurs in seconds.

If the event is used in a widget, it is triggered when the change occurs in minutes.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | Unix time stamp, which is the number of seconds that have elapsed since the Unix epoch. |

#### TextClockController

Implements the controller of the **TextClock** component. You can bind the controller to the component to control its start and stop. A **TextClock** component can be bound to only one controller.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

## Objects to Import

controller: TextClockController = new TextClockController();

#### \[h2\]constructor

constructor()

A constructor used to create a **TextClockController** instance.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]start

start()

Starts the **<TextClock>** component.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]stop

stop()

Stops the **<TextClock>** component.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### TextClockConfiguration12+

You need a custom class to implement the **ContentModifier** API.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| timeZoneOffset | number | No | No | 
Time zone offset of the text clock.

The value range is \[-14, 12\], indicating UTC+12 to UTC-12. A negative value indicates Eastern Standard Time, and a positive value indicates Western Standard Time. For example, **\-8** indicates UTC+8. If the value is a floating point number within the value range, it is rounded off, with the decimal portion discarded.

 |
| started | boolean | No | No | 

Whether the text clock is started.

**true**: The text clock is started.

**false**: The text clock is disabled.

Default value: **true**

 |
| timeValue | number | No | No | Time zone offset of the text clock in seconds from UTC. |

#### Example

## Example 1: Implementing a Text Clock with Start/Stop Control

This example demonstrates the basic usage of the **TextClock** component, setting the clock display format using the [format](#format) attribute.

Clicking **"start TextClock"** triggers the callback to invoke **TextClockController** and initiate the clock. Clicking **"stop TextClock"** pauses the clock via **TextClockController**.

The example demonstrates how to continuously update **accumulateTime** content during clock updates by invoking the [TextClockController](#textclockcontroller) callback.

@Entry
@Component
struct Second {
  @State accumulateTime: number = 0;
  // Objects to import
  controller: TextClockController = new TextClockController();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('Current milliseconds is ' + this.accumulateTime)
        .fontSize(20)
      // Display the system time in 12-hour format for the UTC+8 time zone, accurate to seconds.
      TextClock({ timeZoneOffset: -8, controller: this.controller })
        .format('aa hh:mm:ss')
        .onDateChange((value: number) => {
          this.accumulateTime = value;
        })
        .margin(20)
        .fontSize(30)
      Button('start TextClock')
        .margin({ bottom: 10 })
        .onClick(() => {
          // Start the text clock.
          this.controller.start();
        })
      Button('stop TextClock')
        .onClick(() => {
          // Stop the text clock.
          this.controller.stop();
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/w_3t7iPzSGqSdU4Vk1ti3w/en-us_image_0000002568685509.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BED0518AA36275C82A3F50E0356206E8F51436BB0B768FDC3BAD7AF7211B4E84)

## Example 2: Setting the Text Shadow Style

This example shows how to set the text shadow style for the text clock using the [textShadow](#textshadow11) attribute.

@Entry
@Component
struct TextClockExample {
  @State textShadows: ShadowOptions | Array<ShadowOptions> = \[{
    radius: 10,
    color: Color.Red,
    offsetX: 10,
    offsetY: 0
  }, {
    radius: 10,
    color: Color.Black,
    offsetX: 20,
    offsetY: 0
  }, {
    radius: 10,
    color: Color.Brown,
    offsetX: 30,
    offsetY: 0
  }, {
    radius: 10,
    color: Color.Green,
    offsetX: 40,
    offsetY: 0
  }, {
    radius: 10,
    color: Color.Yellow,
    offsetX: 100,
    offsetY: 0
  }\];

  build() {
    Column({ space: 8 }) {
      TextClock().fontSize(50).textShadow(this.textShadows)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/YtO0e4d6RLaRTRYcEAyvfw/en-us_image_0000002568765519.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C964B6882BB3CB47BD2CC50329168B8BC4C85723664829D7C5A28A36AC75A4F0)

## Example 3: Configuring the Custom Content Area

This example implements the functionality of customizing the style of a text clock, creating a time picker component with a custom style: The time picker dynamically adjusts its selected value based on the text clock's timezone offset and the time zone offset in seconds from UTC, creating a clock effect; depending on whether the text clock is started, the time picker toggles between a 12-hour and a 24-hour format display.

class MyTextClockStyle implements ContentModifier<TextClockConfiguration> {
  currentTimeZoneOffset: number = new Date().getTimezoneOffset() / 60;
  title: string = '';

  constructor(title: string) {
    this.title = title;
  }

  applyContent(): WrappedBuilder<\[TextClockConfiguration\]> {
    return wrapBuilder(buildTextClock);
  }
}

@Builder
function buildTextClock(config: TextClockConfiguration) {
  Row() {
    Column() {
      Text((config.contentModifier as MyTextClockStyle).title)
        .fontSize(20)
        .margin(20)
      TimePicker({
        selected: (new Date(config.timeValue \* 1000 +
          ((config.contentModifier as MyTextClockStyle).currentTimeZoneOffset - config.timeZoneOffset) \* 60 \* 60 \*
            1000)),
        format: TimePickerFormat.HOUR\_MINUTE\_SECOND
      })
        .useMilitaryTime(!config.started)
    }
  }
}

@Entry
@Component
struct TextClockExample {
  @State accumulateTime1: number = 0;
  @State timeZoneOffset: number = -8;
  controller1: TextClockController = new TextClockController();
  controller2: TextClockController = new TextClockController();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('Current milliseconds is ' + this.accumulateTime1)
        .fontSize(20)
        .margin({ top: 20 })
      TextClock({ timeZoneOffset: this.timeZoneOffset, controller: this.controller1 })
        .format('aa hh:mm:ss')
        .onDateChange((value: number) => {
          this.accumulateTime1 = value;
        })
        .margin(20)
        .fontSize(30)
      TextClock({ timeZoneOffset: this.timeZoneOffset, controller: this.controller2 })
        .format('aa hh:mm:ss')
        .fontSize(30)
        .contentModifier(new MyTextClockStyle('ContentModifier:'))
      Button('start TextClock')
        .margin({ top: 20, bottom: 10 })
        .onClick(() => {
          // Start the text clock.
          this.controller1.start();
          this.controller2.start();
        })
      Button('stop TextClock')
        .margin({ bottom: 30 })
        .onClick(() => {
          // Stop the text clock.
          this.controller1.stop();
          this.controller2.stop();
        })

    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/JawliA64QSKk1S_SjYIGcw/en-us_image_0000002537765794.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4343A98AA81B0F118AB76E32CE928D269A78F5A129AE38B6D4736D0819896635)

## Example 4: Setting Leading Zero

This example demonstrates how to use the [dateTimeOptions](#datetimeoptions12) attribute to add or remove the leading zero for the hour field. By default, the hour field includes a leading zero in the 24-hour format, but typically does not include a leading zero in the 12-hour format.

@Entry
@Component
struct TextClockExample {
  build() {
    Column({ space: 8 }) {
      Row() {
        Text('Remove the leading zero in 24-hour format: ')
          .fontSize(20)
        TextClock()
          .fontSize(20)
          .format('HH:mm:ss')
          .dateTimeOptions({ hour: 'numeric' })
      }

      Row() {
        Text('Add the leading zero in 12-hour format: ')
          .fontSize(20)
        TextClock()
          .fontSize(20)
          .format('aa hh:mm:ss')
          .dateTimeOptions({ hour: '2-digit' })
      }
    }
    .alignItems(HorizontalAlign.Start)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/9aIIuckeRxmwISZjBfofBA/en-us_image_0000002537925734.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=413BF3E49B943C3A9BD779F46F72EFECB5E316F4A7361F6F0BF7F46E16FA011D)

## Example 5: Setting the Text Display Style

This example demonstrates how to use the [fontFeature](#fontfeature11), [fontColor](#fontcolor), [fontStyle](#fontstyle), [fontWeight](#fontweight) and [fontFamily](#fontfamily) attributes to set the text display style of the clock.

@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('fontFeature').fontColor(0xCCCCCC)
      // Set text features.
      TextClock()
        .fontFeature('\\"sinf\\" off')
      TextClock()
        .fontFeature('\\"sinf\\" on')
        .margin('10%')

      // Set the font color.
      Text('fontColor').fontColor(0xCCCCCC)
      TextClock()
        .fontColor(Color.Black)
      TextClock()
        .fontColor(Color.Blue)
        .margin('10%')

      Text('fontStyle').fontColor(0xCCCCCC)
      // Set the font style.
      TextClock()
        .fontStyle(FontStyle.Normal)
      TextClock()
        .fontStyle(FontStyle.Italic)
        .margin('10%')

      Text('fontWeight').fontColor(0xCCCCCC)
      Sets font weight.
      TextClock()
        .fontWeight(FontWeight.Normal)
      TextClock()
        .fontWeight(FontWeight.Bold)
        .margin('10%')

      Text('fontFamily').fontColor(0xCCCCCC)
      // Set the font.
      TextClock()
        .fontFamily('HarmonyOS Sans')
    }
    .width('100%')
    .height('100%')
  }
}
