# Crown Event

A crown event is an event triggered when the crown of a wearable device is rotated. Event dispatch relies on component focus, and you can customize event handling through [focus events](../../interaction-response-events/focus-event/document.md)d.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/62T4iN_lRGm93xxbsb47rw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=242F6D0F8211987175C35B5FD7D88D5856B9DBB5652027AFEBAD5EE1240096C8)

-   The initial APIs of this module are supported since API version 18. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   Manual rotation of the crown will trigger the default interaction logic. For example, rotating the crown causes the scrollbar to scroll in the direction of the rotation.
    
-   A component must have focus to receive crown events. Focus control can be managed using [focusable](../../../universal-attributes/interaction-properties/focus-control/document.md#focusable), [defaultFocus](../../../universal-attributes/interaction-properties/focus-control/document.md#defaultfocus9), and [focusOnTouch](../../../universal-attributes/interaction-properties/focus-control/document.md#focusontouch9).
    
-   This event is only supported on wearable devices.
    
-   By default, the following components support crown events: [Slider](../../../buttons-and-selections/slider/document.md), [DatePicker](../../../buttons-and-selections/datepicker/document.md), [TextPicker](../../../buttons-and-selections/textpicker/document.md), [TimePicker](../../../buttons-and-selections/timepicker/document.md), [Scroll](../../../scroll-and-swipe/scroll/document.md), [List](../../../scroll-and-swipe/list/document.md), [Grid](../../../scroll-and-swipe/grid/document.md), [WaterFlow](../../../scroll-and-swipe/waterflow/document.md), [ArcList](../../../scroll-and-swipe/arclist/document.md), [Refresh](../../../scroll-and-swipe/refresh/document.md), and [ArcSwiper](../../../scroll-and-swipe/arcswiper/document.md).
    

#### onDigitalCrown

onDigitalCrown(handler: Optional<Callback<CrownEvent>>): T

Called when the crown is rotated while the component has focus.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/1FtupVZuSqiErLqarzQmew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99BB71237334121A75B9847B482DC927FC5DED89D62F5C5AA67DF9EEC86CA542)

This API cannot be called within [attributeModifier](../../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | Optional<Callback<[CrownEvent](#crownevent)\>> | Yes | [CrownEvent](#crownevent) object. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### CrownEvent

Defines a data structure for the crown event received by a component. It includes the timestamp, angular velocity, rotation angle, crown action, and event propagation disabling.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| timestamp | number | No | No | Timestamp. |
| angularVelocity | number | No | No | Angular velocity in degrees per second (°/s). |
| degree | number | No | No | 
Relative rotation angle.

Unit: degrees

Value range: \[-360, 360\]

 |
| action | [CrownAction](../../../common-definitions/enums/document.md#crownaction18) | No | No | Crown action. |
| stopPropagation | Callback<void> | No | No | Disables [event bubbling](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-interaction-basic-principles#event-bubbling) propagation. |

#### Example

This example demonstrates how to register a crown event on a component and receive event data.

// xxx.ets
@Entry
@Component
struct CityList {
  @State message: string = "onDigitalCrown";

  build() {
    Column() {
      Row() {
        Stack() {
          Text(this.message)
            .fontSize(20)
            .fontColor(Color.White)
            .backgroundColor("#262626")
            .textAlign(TextAlign.Center)
            .focusable(true)
            .focusOnTouch(true)
            .defaultFocus(true)
            .borderWidth(2)
            .width(223)
            .height(223)
            .borderRadius(110)
            .onDigitalCrown((event: CrownEvent) => {
              event.stopPropagation();
              this.message = "CrownEvent\\n\\n" + JSON.stringify(event);
              console.info(\`action: ${event.action}, angularVelocity: ${event.angularVelocity}, degree: ${event.degree}, timestamp: ${event.timestamp}\`);
            })
        }.width("100%").height("100%")
      }.width("100%").height("100%")
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/PWMHoE81Sda0h83GNMzOKw/en-us_image_0000002568764501.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B4777A2682C3C8E569363BA288D9D240835A5A52F46234C2973E5FAA32C462D)
