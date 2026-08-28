# TextTimer

The **TextTimer** component displays timing information and is controlled in text format.

The time updates stop when the component is invisible. The component's visibility is determined by the value of **ratios** in the [onVisibleAreaChange](../../universal-events/component-change-events/visible-area-change-event/document.md#onvisibleareachange) event callback: If the value is greater than 0, the component is visible.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/NMOjDFZmS1yJ10REMwHyig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8AE122256450447578226B371F3C6E5BFB9E11F60CE7D13A77C5676A49C4C3DB)

This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

TextTimer(options?: TextTimerOptions)

**Widget capability**: Since API version 10, this API is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TextTimerOptions](#texttimeroptions) | No | Parameters of the **TextTimer** component. |

#### TextTimerOptions

Options used to build the TextTimer component.

**Widget capability**: Since API version 10, this API is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isCountDown | boolean | No | Yes | 
Countdown switch.

**true**: The timer counts down (for example, from 30 seconds to 0 seconds).

**false**: The timer counts up (for example, from 0 seconds to 30 seconds).

Default value: **false**

 |
| count | number | No | Yes | 

Timer duration, in milliseconds. It is effective only when **isCountDown** is **true**. The maximum value is 86400000 ms (24 hours). If 0 < **count** < 86400000, **count** is the initial value of the timer. Otherwise, the default value is used as the initial value.

Default value: **60000**

 |
| controller | [TextTimerController](#texttimercontroller) | No | Yes | **TextTimer** controller. |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]format

format(value: string)

Sets the custom format. The value must contain at least one of the following keywords: **HH**, mm, **ss**, and **SS**. If the date format is yy, MM, or dd, the default value is used.

The timer update frequency is in the minimum unit of format. For example, if format is set to HH:mm, the update frequency is one minute.

**Widget capability**: Since API version 10, this API is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | 
Custom date display format.

Default value: **'HH:mm:ss.SS'**

 |

#### \[h2\]fontColor

fontColor(value: ResourceColor)

Sets the font color.

**Widget capability**: Since API version 10, this API is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Font color.

The default value on wearable devices is '#c5ffffff', indicating that the text is displayed in white.

Default value on other devices: '#e6182431', which is displayed in black.

 |

#### \[h2\]fontSize

fontSize(value: Length)

Sets the font size.

**Widget capability**: Since API version 10, this API is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | Font size. If **fontSize** is of the number type, the unit fp is used. The default font size is 16 fp. The value cannot be a percentage. |

#### \[h2\]fontStyle

fontStyle(value: FontStyle)

Sets the font style.

**Widget capability**: Since API version 10, this API is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [FontStyle](../../common-definitions/enums/document.md#fontstyle) | Yes | 
Font style, for example, italic.

Default value: **FontStyle.Normal**

 |

#### \[h2\]fontWeight

fontWeight(value: number | FontWeight | ResourceStr)

Font weight of the text. If the value is too large, the text in different fonts may be truncated.

**Widget capability**: Since API version 10, this API is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [FontWeight](../../common-definitions/enums/document.md#fontweight) | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 
Font width of the text. The value range of the number type is \[100, 900\]. The value interval is 100. A larger value indicates a wider font. If the value of the number type is not within the value range, the default value is 400. The \[ResourceStr\] (ts-types.md#resourcestr) type supports only the string of the number type, for example, 400, bold, bolder, lighter, regular, and medium, corresponds to the corresponding enumerated values in FontWeight.

Default value: **FontWeight.Normal**

The Resource type is supported since API version 20.

 |

#### \[h2\]fontFamily

fontFamily(value: ResourceStr)

Sets the font family.

**Widget capability**: Since API version 10, this API is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 
Font family. The default font is **'HarmonyOS Sans'**.

The 'HarmonyOS Sans' font and [registered custom fonts](../../../arkts-api/ui/ohos-font-custom-font-registration/document.md) are supported for applications.

Only the 'HarmonyOS Sans' font is supported for widgets.

 |

#### \[h2\]textShadow11+

textShadow(value: ShadowOptions | Array<ShadowOptions>)

Sets the text shadow. It supports input parameters in an array to implement multiple text shadows. This API does not work with the **fill** attribute or coloring strategy.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/wTxuld0ZRmmBQORnYvjxcw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83796DD93D698E33FE2A842AF270ABA690B13ED9BAB19DB489716EFB86EFD7B7)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ShadowOptions](../../universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | Array<[ShadowOptions](../../universal-attributes/visual-effects/image-effect/document.md#shadowoptions)\> | Yes | Parameters of the text shadow effect, including the color, blur radius, and offset. |

#### \[h2\]contentModifier12+

contentModifier(modifier: ContentModifier<TextTimerConfiguration>)

Creates a content modifier.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [ContentModifier](../../universal-attributes/modifiers-and-custom-property/content-modifier/document.md#contentmodifiert)[<TextTimerConfiguration>](#texttimerconfiguration12) | Yes | 
Content modifier to apply to the **TextTimer** component.

**modifier**: content modifier. You need a custom class to implement the **ContentModifier** API.

 |

#### Events

#### \[h2\]onTimer

onTimer(event: (utc: number, elapsedTime: number) => void)

This event is triggered when the time text changes. This event is not triggered when the screen is locked or the application is running in the background.

When the high-precision [format](#format) (SSS or SS) is set, the callback interval may fluctuate.

**Widget capability**: Since API version 10, this API is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| utc | number | Yes | Linux timestamp, which is the amount of time that has elapsed since January 1, 1970, in the minimum unit of the format. |
| elapsedTime | number | Yes | Elapsed time of the timer, in the minimum unit of the format. |

#### TextTimerController

Implements a controller for controlling the **TextTimer** component. A **TextTimer** component can only be bound to one controller, and the relevant commands can only be called after the component has been created. A **TextTimerController** can control only the last **TextTimer** component bound to it.

**Widget capability**: Since API version 10, this API is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

## Objects to Import

textTimerController: TextTimerController = new TextTimerController();

#### \[h2\]constructor

constructor()

A constructor used to create a **TextTimerController** object.

**Widget capability**: Since API version 10, this API is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]start

start()

Starts the timer.

**Widget capability**: Since API version 10, this API is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]pause

pause()

Pauses the timer.

**Widget capability**: Since API version 10, this API is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]reset

reset()

Resets the timer.

**Widget capability**: Since API version 10, this API is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### TextTimerConfiguration12+

Defines the configuration of the TextTimer used by the ContentModifier API.

You need a custom class to implement the **ContentModifier** API.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| count | number | No | No | 
Timer duration, in milliseconds. It is effective only when **isCountDown** is **true**. The maximum value is 86400000 ms (24 hours). If the value is between 0 and 86,400,000, it is used as the initial countdown time. Otherwise, the default value is used as the initial countdown time.

Default value: **60000**

 |
| isCountDown | boolean | No | No | 

Whether the timer is a countdown.

true: The timer starts to count down, for example, from 30s to 0s. false: The timer starts to count up, for example, from 0s to 30s.

Default value: **false**

 |
| started | boolean | No | No | 

Whether the timer has already started.

true: The timer has started. false: The timer has not started.

Default value: **false**

 |
| elapsedTime | number | No | No | Elapsed time of the timer, in the minimum unit of the format. |

#### Example

## Example 1: Implementing a Text Timer with Start, Pause, and Reset Buttons

This example demonstrates the basic usage of the **TextTimer** component, setting the timer display format using the [format](#format) attribute.

Users can start, pause, and reset the timer by clicking the **start**, **pause**, and **reset** buttons.

// xxx.ets
@Entry
@Component
struct TextTimerExample {
  textTimerController: TextTimerController = new TextTimerController();
  @State format: string = 'mm:ss.SS';

  build() {
    Column() {
      TextTimer({ isCountDown: true, count: 30000, controller: this.textTimerController })
        .format(this.format)
        .fontColor(Color.Black)
        .fontSize(50)
        .onTimer((utc: number, elapsedTime: number) => {
          console.info('textTimer notCountDown utc is: ' + utc + ', elapsedTime: ' + elapsedTime)
        })
      Row() {
        Button('start').onClick(() => {
          this.textTimerController.start();
        })
        Button('pause').onClick(() => {
          this.textTimerController.pause();
        })
        Button('reset').onClick(() => {
          this.textTimerController.reset();
        })
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/uDP47gfxQAi5ASvZbkSfVw/en-us_image_0000002568685511.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6999C6BDB644B1D762B3F550102C9841537B7A632401926302E4F10058340BEC)

## Example 2: Setting the Text Shadow Style

In this example, the [textShadow](#textshadow11) property is used to set the text shadow style of the timer.

// xxx.ets
@Entry
@Component
struct TextTimerExample {
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
      TextTimer().fontSize(50).textShadow(this.textShadows)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/EnU8DJdtQZyNhmMg8dEEPg/en-us_image_0000002568765521.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B68345457BE45ED5F8A2443C55E72D9409D9C17CF3B1FDFA5FAC7E102E9FA0A6)

## Example 3: Configuring the Custom Content Area

This example showcases two simple **TextTimer** components set against a light gray background. Once the timers are activated, they display the time progression in real-time. When the countdown timer starts, the background turns black; when the count-up timer starts, the background turns gray.

// xxx.ets
class MyTextTimerModifier implements ContentModifier<TextTimerConfiguration> {
  constructor() {
  }

  applyContent(): WrappedBuilder<\[TextTimerConfiguration\]> {
    return wrapBuilder(buildTextTimer);
  }
}

@Builder
function buildTextTimer(config: TextTimerConfiguration) {
  Column() {
    Stack({ alignContent: Alignment.Center }) {
      Circle({ width: 150, height: 150 })
        .fill(config.started ? (config.isCountDown ? 0xFF232323 : 0xFF717171) : 0xFF929292)
      Column() {
        Text (config.isCountDown ? ' Countdown' : 'Counting up') .fontColor(Color.White)
        Text(
          (config.isCountDown ? ' Remaining' : 'Has passed') + (config.isCountDown ?
            (Math.max(config.count / 1000 - config.elapsedTime / 100, 0)).toFixed(1) + '/' +
            (config.count / 1000).toFixed(0)
            : ((config.elapsedTime / 100).toFixed(0))
          ) + '')
        ).fontColor(Color.White)
      }
    }
  }
}

@Entry
@Component
struct Index {
  @State count: number = 10000;
  @State myTimerModifier: MyTextTimerModifier = new MyTextTimerModifier();
  countDownTextTimerController: TextTimerController = new TextTimerController();
  countUpTextTimerController: TextTimerController = new TextTimerController();

  build() {
    Row() {
      Column() {
        TextTimer({ isCountDown: true, count: this.count, controller: this.countDownTextTimerController })
          .contentModifier(this.myTimerModifier)
          .onTimer((utc: number, elapsedTime: number) => {
            console.info('textTimer onTimer utc is: ' + utc + ', elapsedTime: ' + elapsedTime);
          })
          .margin(10)
        TextTimer({ isCountDown: false, controller: this.countUpTextTimerController })
          .contentModifier(this.myTimerModifier)
          .onTimer((utc: number, elapsedTime: number) => {
            console.info('textTimer onTimer utc is: ' + utc + ', elapsedTime: ' + elapsedTime);
          })
        Row() {
          Button('start').onClick(() => {
            this.countDownTextTimerController.start();
            this.countUpTextTimerController.start();
          }).margin(10)
          Button('pause').onClick(() => {
            this.countDownTextTimerController.pause();
            this.countUpTextTimerController.pause();
          }).margin(10)
          Button('reset').onClick(() => {
            this.countDownTextTimerController.reset();
            this.countUpTextTimerController.reset();
          }).margin(10)
        }.margin(20)
      }.width('100%')
    }.height('100%')
  }
}

## Example 4: Enabling the Timer to Start Immediately After Creation

This example demonstrates how to start the **TextTimer** immediately after it is created.

// xxx.ets
@Entry
@Component
struct TextTimerStart {
  textTimerController: TextTimerController = new TextTimerController();
  @State format: string = 'mm:ss.SS';

  build() {
    Column() {
      Scroll()
        .height('20%')
      TextTimer({ isCountDown: true, count: 30000, controller: this.textTimerController })
        .format(this.format)
        .fontColor(Color.Black)
        .fontSize(50)
        .onTimer((utc: number, elapsedTime: number) => {
          console.info('textTimer notCountDown utc is: ' + utc + ', elapsedTime: ' + elapsedTime)
        })
        .onAppear(() => {
          this.textTimerController.start();
        })
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/uIdIEHIURtWrpdqjyTUAeQ/en-us_image_0000002537765796.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4AF7896C54C2000625C2D4783776004E8AFB96E6E66E145C4150DCF1ABB9FA9)

## Example 5: Setting the Text Style

This example uses the [fontColor](#fontcolor), [fontSize](#fontsize), [fontStyle](#fontstyle), [fontWeight](#fontweight) and [fontFamily](#fontfamily) attributes to display text in different styles.

// xxx.ets
@Entry
@Component
struct demo {
  textTimerController: TextTimerController = new TextTimerController();
  @State format: string = 'HH:mm:ss.SS';
  @State countValue: number = 5025678;

  build() {
    Column({ space: 10 }) {
      Text ('Set the font color').fontColor(0xCCCCCC)
      TextTimer({ isCountDown: true, count: this.countValue, controller: this.textTimerController })
        .fontColor(Color.Blue)
      TextTimer({ isCountDown: true, count: this.countValue, controller: this.textTimerController })
        .fontColor(Color.Gray)

      Text ('Set the font size').fontColor(0xCCCCCC)
      TextTimer({ isCountDown: true, count: this.countValue, controller: this.textTimerController })
        .fontSize(10)
      TextTimer({ isCountDown: true, count: this.countValue, controller: this.textTimerController })
        .fontSize(30)

      Text ('Set the font style').fontColor(0xCCCCCC)
      TextTimer({ isCountDown: true, count: this.countValue, controller: this.textTimerController })
        .fontStyle(FontStyle.Normal)
      TextTimer({ isCountDown: true, count: this.countValue, controller: this.textTimerController })
        .fontStyle(FontStyle.Italic)

      Text ('Set the font weight').fontColor(0xCCCCCC)
      TextTimer({ isCountDown: true, count: this.countValue, controller: this.textTimerController })
        .fontWeight(FontWeight.Lighter)
      TextTimer({ isCountDown: true, count: this.countValue, controller: this.textTimerController })
        .fontWeight(FontWeight.Bolder)

      Text ('Set the font family').fontColor(0xCCCCCC)
      TextTimer({ isCountDown: true, count: this.countValue, controller: this.textTimerController })
        .fontFamily('HMOS Color Emoji')
      TextTimer({ isCountDown: true, count: this.countValue, controller: this.textTimerController })
        .fontFamily('HarmonyOS Sans')
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
