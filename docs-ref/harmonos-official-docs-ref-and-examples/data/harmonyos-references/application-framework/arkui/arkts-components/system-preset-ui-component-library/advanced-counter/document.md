# advanced.Counter

The **Counter** component enables precise numerical value adjustment.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/XN1eIuIETw-c-XYikKIAgg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDED60B1376207FED7999C34B862096E7262D3EB16EDCDB9594FCEE727C8AB42)

This component is supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.

If the **Counter** component has [universal attributes](../../universal-attributes/document.md) and [universal events](../../universal-events/document.md) configured, the compiler toolchain automatically generates an additional ****Common**** node and mounts the universal attributes and universal events on this node rather than the **Counter** component itself. As a result, the configured universal attributes and universal events may fail to take effect or behave as intended. For this reason, avoid using universal attributes and events with the **Counter** component.

#### Modules to Import

import { CounterType, CounterComponent, CounterOptions, DateData } from '@kit.ArkUI';

#### Child Components

Not supported

#### CounterComponent

CounterComponent({ options: CounterOptions })

Defines a **Counter** component instance.

**Decorator**: @Component

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| options | [CounterOptions](#counteroptions) | Yes | @Prop | Configuration parameters of the **Counter** component. |

#### CounterOptions

Defines the counter type and style.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [CounterType](#countertype) | No | No | Type of the counter. |
| direction12+ | [Direction](../../common-definitions/enums/document.md#direction) | No | Yes | 
Layout direction.

Default value: **Direction.Auto**

If the value is **undefined**, the default value is used.

 |
| numberOptions | [NumberStyleOptions](#numberstyleoptions) | No | Yes | 

Style of the list or compact counter.

Default value: list or compact counter with value 0.

If the value is **undefined**, the default value is used.

 |
| inlineOptions | [InlineStyleOptions](#inlinestyleoptions) | No | Yes | 

Parameters of the inline numeric counter.

Default value: regular inline numeric counter with value 0.

If the value is **undefined**, the default value is used.

 |
| dateOptions | [DateStyleOptions](#datestyleoptions) | No | Yes | 

Style of the inline date counter.

Default value: date counter showing 0001/01/01.

If the value is **undefined**, the default value is used.

 |

The table below lists the counter type and style mapping.

| Counter Type | Counter Style |
| :-- | :-- |
| CounterType.LIST | NumberStyleOptions |
| CounterType.COMPACT | NumberStyleOptions |
| CounterType.INLINE | InlineStyleOptions |
| CounterType.INLINE\_DATE | DateStyleOptions |

#### CounterType

Enumerates counter types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| LIST | 0 | List counter. |
| COMPACT | 1 | Compact counter. |
| INLINE | 2 | Inline numeric counter. |
| INLINE\_DATE | 3 | Inline date counter. |

#### CommonOptions

Defines common attributes and events for all counter types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| focusable | boolean | No | Yes | 
Whether the counter is focusable.

**NOTE**

This attribute only applies to list and compact counters.

Default value: **true**.

**true**: focusable. **false**: not focusable.

If the value is **undefined**, the default value is used.

 |
| step | number | No | Yes | 

Step of the counter.

Value range: an integer greater than or equal to 1.

Default value: **1**

If the value is out of the range, the default value is used.

 |
| onHoverIncrease | (isHover: boolean) => void | No | Yes | 

Callback invoked when the mouse pointer is moved over or away from the increase button of the counter.

**isHover**: whether the mouse pointer is hovering over the component. The value **true** means that the mouse pointer enters the component, and the value **false** means that the mouse pointer leaves the component.

Default value: no callback triggered.

If the value is **undefined**, the default value is used.

 |
| onHoverDecrease | (isHover: boolean) => void | No | Yes | 

Callback invoked when the mouse pointer is moved over or away from the decrease button of the counter.

**isHover**: whether the mouse pointer is hovering over the component. The value **true** means that the mouse pointer enters the component, and the value **false** means that the mouse pointer leaves the component.

Default value: no callback triggered.

If the value is **undefined**, the default value is used.

 |

#### InlineStyleOptions

Defines the inline numeric counter attributes and events.

Inherits from [CommonOptions](#commonoptions).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | number | No | Yes | 
Initial value of the counter.

Default value: **0**

Value range: \[min, max\].

When the value exceeds the allowed range, it is handled as follows: if the value is **undefined**, the default value is applied; otherwise, the maximum allowed value is used.

 |
| min | number | No | Yes | 

Minimum value of the counter.

Default value: **0**

Value range: (-∞, +∞)

If the value is **undefined**, the default value is used.

 |
| max | number | No | Yes | 

Maximum value of the counter.

Default value: **999**

Value range: (-∞, +∞)

If the value is **undefined**, the default value is used.

 |
| textWidth | number | No | Yes | 

Text width of the counter.

Default value: auto-adjusted width.

Value range: \[0, +∞)

Unit: vp.

When the value exceeds the allowed range, it is handled as follows: if the value is **undefined**, the default value is applied; otherwise, the maximum allowed value is used.

 |
| onChange | (value: number) => void | No | Yes | 

Callback invoked when the value changes. The current value is returned.

**value**: current value.

Default value: no callback triggered.

If the value is **undefined**, the default value is used.

 |

#### NumberStyleOptions

Defines the list and compact counter attributes and events.

Inherits from [InlineStyleOptions](#inlinestyleoptions).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| label | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Label of the counter.

Default value: **' '**

If the value is **undefined**, the default value is used.

 |
| onFocusIncrease | () => void | No | Yes | 

Callback invoked when the increase button of the counter gains focus.

Default value: no callback triggered.

If the value is **undefined**, the default value is used.

 |
| onFocusDecrease | () => void | No | Yes | 

Callback invoked when the decrease button of the counter gains focus.

Default value: no callback triggered.

If the value is **undefined**, the default value is used.

 |
| onBlurIncrease | () => void | No | Yes | 

Callback invoked when the increase button of the counter loses focus.

Default value: no callback triggered.

If the value is **undefined**, the default value is used.

 |
| onBlurDecrease | () => void | No | Yes | 

Callback invoked when the decrease button of the counter loses focus.

Default value: no callback triggered.

If the value is **undefined**, the default value is used.

 |

#### DateStyleOptions

Defines the inline date counter attributes and events.

Inherits from [CommonOptions](#commonoptions).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| year | number | No | Yes | 
Initial year of the counter.

Default value: **1**

Value range: \[1, 5000\]

If the value is out of the range, the default value is used.

 |
| month | number | No | Yes | 

Initial month of the counter.

Default value: **1**

Value range: \[1, 12\]

If the value is out of the range, the default value is used.

 |
| day | number | No | Yes | 

Initial day of the counter.

Default value: **1**

Value range: \[1, 31\]

If the value is out of the range, the default value is used.

 |
| onDateChange | (date: [DateData](#datedata)) => void | No | Yes | 

Callback invoked when the date changes. The current date is returned.

**date**: current date.

If the value is **undefined**, the current date value is not displayed.

 |

#### DateData

Defines date attributes, including year, month, and day.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| year | number | No | No | 
Initial year of the counter.

Default value: **1**

Value range: \[1, 5000\]

If the value is out of the range, the default value is used.

 |
| month | number | No | No | 

Initial month of the counter.

Default value: **1**

Value range: \[1, 12\]

If the value is out of the range, the default value is used.

 |
| day | number | No | No | 

Initial day of the counter.

Default value: **1**

Value range: \[1, 31\]

If the value is out of the range, the default value is used.

 |

#### \[h2\]constructor

constructor(year: number, month: number, day: number)

DateData constructor for initializing date objects.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| year | number | Yes | Initial year of the counter. |
| month | number | Yes | Initial month of the counter. |
| day | number | Yes | Initial day of the counter. |

#### \[h2\]toString

toString(): string

Returns the current date in YYYY-MM-DD format.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| string | Current date. |

#### Example

## Example 1: Implementing a List Counter

This example implements a list counter by setting **type** to **CounterType.LIST** and configuring **numberOptions**.

import { CounterType, CounterComponent } from '@kit.ArkUI';

@Entry
@Component
struct ListCounterExample {
  build() {
    Column() {
      // List counter
      CounterComponent({
        options: {
          type: CounterType.LIST,
          numberOptions: {
            label: "Price",
            min: 0,
            value: 5,
            max: 10
          }
        }
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/QUciYnRWQPS9CihATQWziw/en-us_image_0000002537925942.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D527D24B1067DE29A883F0CDE33BB34EE8DA0E17227B230CD9BD8FC53A0D4CFD)

## Example 2: Implementing a Compact Counter

This example implements a compact counter by setting **type** to **CounterType.COMPACT** and configuring **numberOptions**.

import { CounterType, CounterComponent } from '@kit.ArkUI';

@Entry
@Component
struct CompactCounterExample {
  build() {
    Column() {
      // Compact counter
      CounterComponent({
        options: {
          type: CounterType.COMPACT,
          numberOptions: {
            label: "Quantity",
            value: 10,
            min: 0,
            max: 100,
            step: 10
          }
        }
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/ZZioUu-SSVytWlEt7-Fmdw/en-us_image_0000002568685719.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5230ADE62BC0B6D1911AECEEED85E8EA11C3160001B95ED5AFB71C7EF18FCFE6)

## Example 3: Implementing an Inline Numeric Counter

This example implements an inline numeric counter by setting **type** to **CounterType.INLINE** and configuring **inlineOptions**.

import { CounterType, CounterComponent } from '@kit.ArkUI';

@Entry
@Component
struct NumberStyleExample {
  build() {
    Column() {
      // Inline numeric counter
      CounterComponent({
        options: {
          type: CounterType.INLINE,
          inlineOptions: {
            value: 100,
            min: 10,
            step: 2,
            max: 1000,
            textWidth: 100,
            onChange: (value: number) => {
              console.info('onCounterChange Counter: ' + value.toString());
            }
          }
        }
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/CjB7yhKnRlC6HOxq1kJPOA/en-us_image_0000002568765729.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80C696A5DE01B95693AE264A2B37AD85FF1891CC89250D0C6A669BCC241FF90A)

## Example 4: Implementing an Inline Date Counter

This example implements an inline date counter by setting **type** to **CounterType.INLINE\_DATE** and configuring **dateOptions**.

import { CounterType, CounterComponent, DateData } from '@kit.ArkUI';

@Entry
@Component
struct DataStyleExample {
  build() {
    Column() {
      // Inline date counter
      CounterComponent({
        options: {
          type: CounterType.INLINE\_DATE,
          dateOptions: {
            year: 2016,
            onDateChange: (date: DateData) => {
              console.info('onDateChange Date: ' + date.toString());
            }
          }
        }
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/ZPS5SaIiQAO612XMHQCE7Q/en-us_image_0000002537766004.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73913C5C66C72B829AAEE1C77E6A6D29A60F18916600142CA30309510239FBD0)

## Example 5: Implementing a Mirrored Layout

This example implements a mirrored layout for list, compact, inline numeric, and inline date counters by setting **direction**.

import { CounterType, CounterComponent, DateData } from '@kit.ArkUI';

@Entry
@Component
struct CounterPage {
  @State currentDirection: Direction = Direction.Rtl

  build() {
    Column({}) {

      // List counter
      CounterComponent({
        options: {
          direction: this.currentDirection,
          type: CounterType.LIST,
          numberOptions: {
            label: "Price",
            min: 0,
            value: 5,
            max: 10,
          }
        }
      })
        .width('80%')

      // Numeric counter
      CounterComponent({
        options: {
          direction: this.currentDirection,
          type: CounterType.COMPACT,
          numberOptions: {
            label: "Quantity",
            value: 10,
            min: 0,
            max: 100,
            step: 10
          }
        }
      }).margin({ top: 20 })

      // Inline numeric counter
      CounterComponent({
        options: {
          type: CounterType.INLINE,
          direction: this.currentDirection,
          inlineOptions: {
            value: 100,
            min: 10,
            step: 2,
            max: 1000,
            textWidth: 100,
            onChange: (value: number) => {
              console.info('onCounterChange Counter: ' + value.toString());
            }
          }
        }
      }).margin({ top: 20 })
      // Inline date counter
      CounterComponent({
        options: {
          direction: this.currentDirection,
          type: CounterType.INLINE\_DATE,
          dateOptions: {
            year: 2024,
            onDateChange: (date: DateData) => {
              console.info('onDateChange Date: ' + date.toString());
            }
          }
        }
      }).margin({ top: 20 })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/LcivKjNCTzGaOjgQpKWMKw/en-us_image_0000002537925944.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4FC40A2A9F8B62C4B6ABBF0268D354FD6D4648C78D3E63A9668EF4910290C34)
