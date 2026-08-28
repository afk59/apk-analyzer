# Touch Target

You can set the touch target for components. When handling a touch event, ArkUI performs a [hit test](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-interaction-basic-principles#hit-testing) on the touch point and the component area before the event is triggered to determine the components targeted by the event. Then ArkUI dispatches the event based on the test result. This affects the dispatch of [click](../../../../universal-events/interaction-response-events/click-event/document.md), [touch](../../../../universal-events/basic-input-events/touch-event/document.md), [drag](../../../../universal-events/interaction-response-events/drag-event/document.md), [mouse](../../../../universal-events/basic-input-events/mouse-event/document.md), [axis](../../../../universal-events/basic-input-events/axis-event/document.md), [hover](../../../../universal-events/interaction-response-events/hover-event/document.md), [accessibility hover](../../../../universal-events/accessibility-related/accessibility-hover-event/document.md), and [gesture](../../../../gesture-handling/gesture-binding/gesture-binding/document.md) events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/OdU5JU8DTYCQeY0AyaK0pg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F92E9D38A4E9E9D7062799B8A8711907651ABA0E6CBB21166561E4D73E15A28F)

-   The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   When setting the touch target attributes, you need to press the finger in the touch target. If the event response conditions are met when the finger is lifted, the event is triggered. In addition, if the conditions are met before the current gesture ends, continuously triggerable events will also be activated.
    

#### responseRegion

responseRegion(value: Array<Rectangle> | Rectangle): T

Sets one or more touch targets.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Array<[Rectangle](#rectangle)\> | [Rectangle](#rectangle) | Yes | 
Touch target, including the position and size.

The default touch target is the entire component. Default value:

{

x: 0,

y: 0,

width: '100%',

height: '100%'

}

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### mouseResponseRegion10+

mouseResponseRegion(value: Array<Rectangle> | Rectangle): T

Sets one or more mouse response regions.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Array<[Rectangle](#rectangle)\> | [Rectangle](#rectangle) | Yes | 
Mouse response regions, defining the position and size.

The default touch target is the entire component. Default value:

{

x: 0,

y: 0,

width: '100%',

height: '100%'

}

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### responseRegionList22+

responseRegionList(regions: Array<ResponseRegion>): T

Sets the touch target list for the component. When this API is called, the [responseRegion](#responseregion) and [mouseResponseRegion](#mouseresponseregion10) APIs do not take effect.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| regions | Array<[ResponseRegion](#responseregion22)\> | Yes | 
Array of touch targets for the component.

Each touch target contains the input tool type, position, and size.

Default value:

\[{

tool: ResponseRegionSupportedTool.ALL,

x: LengthMetrics.vp(0),

y: LengthMetrics.vp(0),

width: LengthMetrics.percent(1),

height: LengthMetrics.percent(1)

}\]

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Rectangle

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | [Length](../../../../common-definitions/basic-types/document.md#length) | No | Yes | 
X coordinate of the touch point relative to the upper left corner of the component.

Default value: **0vp**

 |
| y | [Length](../../../../common-definitions/basic-types/document.md#length) | No | Yes | 

Y coordinate of the touch point relative to the upper left corner of the component.

Default value: **0vp**

 |
| width | [Length](../../../../common-definitions/basic-types/document.md#length) | No | Yes | 

Width of the touch target.

Default value: **'100%'**

 |
| height | [Length](../../../../common-definitions/basic-types/document.md#length) | No | Yes | 

Height of the touch target.

Default value: **'100%'**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/bmbT9vuUSuG_Tse3b_tBHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4EF9DEDBC96A8578BE1BD8933400FF9FD4C2FFB5C90190BABA745B20AA2C35F7)

-   **x** and **y** can be set to a positive or negative percentage value. Setting **x** to **'100%'** shifts the response region rightward by the component's width, while setting **x** to **'-100%'** shifts the response region leftward by the component's width. Setting **y** to **'100%'** shifts the response region downward by the component's height, while setting **y** to **'-100%'** shifts the response region upward by the component's height.
    
-   **width** and **height** can only be set to positive percentage values. When **width** is set to **'100%'**, the width of the response region is equal to that of the component. For example, if the width of a component is 100 vp, **'100%'** indicates that the width of the response region is also 100 vp. When **height** is set to **'100%'**, the height of the response region is equal to that of the component.
    
-   Percentage values are calculated relative to the component's own width and height.
    
-   When the parent component has [clip](../../../visual-effects/shape-clipping/document.md#clip12) set to **true**, child component interaction is affected by the parent component's response region. Children outside the parent component's response region won't respond to gestures or events.
    
-   **width** and **height** do not support **calc()** dynamic calculations.
    

#### ResponseRegion22+

Defines a touch target consisting of an input tool type, touch position, and size.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/P5DqY2kMQG2ap5W-PqbMjA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E892CDC297A492EFFAE58F489DC2D60BDCBB2381FBD45BC3A950CAFAE15AF288)

-   When the parent component has [clip](../../../visual-effects/shape-clipping/document.md#clip12) set to **true**, child component interaction is affected by the parent component's response region. Children outside the parent component's response region won't respond to gestures or events.
    
-   If the input tool type, touch position, and size are not configured for a touch target, default values are used.
    
-   Positive calculation results for x and y represent shifts to the right and down, respectively. Negative calculation results represent shifts to the left and up, respectively.
    
-   If the width and height are of the string type, the string must be in lowercase. Dynamic calculation with **calc()** is supported. The format of the input string for **calc()** is Width/Height scaling ratio ± Width/Height increment, where the scaling ratio is a percentage and the increment unit is px or vp. For example, in **calc(80% + 10vp)**, **80%** is the width/height scaling ratio, and **10vp** is the width/height increment. If the width and height are of the **LengthMetrics** type and the unit is percent, the width and height are calculated relative to the component's own width and height. **percent(1)** indicates 100%. If the calculation result is a negative value, the default value is used.
    

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| tool | [ResponseRegionSupportedTool](../../../../common-definitions/enums/document.md#responseregionsupportedtool22) | No | Yes | 
Type of the input tool applicable to the touch target.

Default value: **ResponseRegionSupportedTool.ALL**

 |
| x | [LengthMetrics](../../../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 

X coordinate of the touch point relative to the upper left corner of the component.

Default value: **LengthMetrics.vp(0)**

 |
| y | [LengthMetrics](../../../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 

Y coordinate of the touch point relative to the upper left corner of the component.

Default value: **LengthMetrics.vp(0)**

 |
| width | [LengthMetrics](../../../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | string | No | Yes | 

Width of the touch target.

Default value: **LengthMetrics.percent(1)**

 |
| height | [LengthMetrics](../../../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | string | No | Yes | 

Height of the touch target.

Default value: **LengthMetrics.percent(1)**

 |

#### Example

## Example 1: Setting a Touch Target via the responseRegion API

This example demonstrates how to set a touch target for a button using **responseRegion** to respond to click events.

// xxx.ets
@Entry
@Component
struct TouchTargetExample {
  @State text: string = "";

  build() {
    Column({ space: 20 }) {
      Text("{x:0,y:0,width:'50%',height:'100%'}")
      // The width of the touch target is half of that of the button. No response after touching the right part of button1.
      Button("button1")
        .responseRegion({
          x: 0,
          y: 0,
          width: '50%',
          height: '100%'
        })
        .onClick(() => {
          this.text = 'button1 clicked'
        })

      // Add multiple touch targets for a component.
      Text("\[{x:'100%',y:0,width:'50%',height:'100%'}," +
        "\\n{ x: 0, y: 0, width: '50%', height: '100%' }\]")
      Button("button2")
        .responseRegion(\[
          {
            x: '100%',
            y: 0,
            width: '50%',
            height: '100%'
          }, // The first touch target is located rightward by one button width, with its size equal to half of the button size. The touch event is triggered if the right part of button2 is clicked.
          {
            x: 0,
            y: 0,
            width: '50%',
            height: '100%'
          }// The width of the second touch target is half of the button width. The touch event is triggered if the left part of button2 is clicked.
        \])
        .onClick(() => {
          this.text = 'button2 clicked'
        })
      // The touch target is located downward by one button height, with its size equal to the button size. The touch event is triggered if the area below the button3 is clicked.
      Text("{x:0,y:'100%',width:'100%',height:'100%'}")
      Button("button3")
        .responseRegion({
          x: 0,
          y: '100%',
          width: '100%',
          height: '100%'
        })
        .onClick(() => {
          this.text = 'button3 clicked'
        })

      Text(this.text).margin({ top: 50 })
    }.width('100%').margin({ top: 10 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/QgAtXngXQ4SOWTS6IV4BSw/en-us_image_0000002537765454.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E764444DA98EAECCCE2509DE0DD1E87DDDE4DBBC97CCB5E0C414F5F4A8DA4C2C)

## Example 2: Setting a Touch Target via the responseRegionList API

This example demonstrates how to set a touch target for a button using [responseRegionList](#responseregionlist22) to respond to click events.

The **responseRegionList** API is supported since API version 22.

// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct TouchTargetExample {
  @State text: string = "";

  build() {
    Column({ space: 20 }) {
      Text("left part of button1")
      // The width of the touch target is half of that of the button. No response after touching the right part of button1.
      Button("button1")
        .responseRegionList(\[{
          x: LengthMetrics.vp(0),
          y: LengthMetrics.vp(0),
          width: LengthMetrics.percent(0.5),
          height: LengthMetrics.percent(1),
        }\])
        .onClick(() => {
          this.text = 'button1 clicked'
        })

      // Touch target 1 is located rightward by one button width, with its size equal to the entire button size. The touch event is triggered if the left part of button2 is clicked.
      // Touch target 2 is located downward by one button height, with its size equal to the entire button size. The touch event is triggered if the area below the button2 is clicked.
      Text("one button size right of button2," + "\\n one button size below button2")
      Button("button2")
        .responseRegionList(\[{
          x: LengthMetrics.percent(1),
          y: LengthMetrics.vp(0),
          width: LengthMetrics.percent(1),
          height: LengthMetrics.percent(1),
        }, {
          tool: ResponseRegionSupportedTool.MOUSE,
          x: LengthMetrics.vp(0),
          y: LengthMetrics.percent(1),
          width: 'calc(100% + 0vp)',
          height: 'calc(100% - 0px)',
        }\])
        .onClick(() => {
          this.text = 'button2 clicked'
        })

      Text(this.text).margin({ top: 50 })
    }.width('100%').margin({ top: 10 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/pv6wjRI4SH2ZufzxY4bLeQ/en-us_image_0000002537925394.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12790B6BA56950FDF4E7B88B90502D364EC9CD7E5F2C3D106E3E79A2DFF2AE85)

## Example 3: Setting the Mouse Touch Target to Respond to Click Events

This example demonstrates how to set the mouse touch target using [mouseResponseRegion](#mouseresponseregion10) to respond to click events.

// xxx.ets
@Entry
@Component
struct MouseResponseRegionExample {
  @State clickInfo: string = 'Click the touch target to trigger an event';

  build() {
    Column({ space: 30 }) {
      // Example 1: Single touch target (only the left half of the button)
      Text('Touch target: left half of the button (triggered upon a touch)')
        .fontSize(14)
      Button('Button1 (Left Half Touch Target)')
        .width(200)
        .height(60)
        // Mouse touch target: only the left half of the button (x/y relative to the component itself, width 50%)
        .mouseResponseRegion({
          // X coordinate of the touch target relative to the component (top-left corner as origin)
          x: 0,
          // Y coordinate of the touch target relative to the component
          y: 0,
          // Width of the touch target (50% of the button)
          width: '50%',
          // Height of the touch target (100% of the button)
          height: '100%'
        })
        .onClick(() => {
          this.clickInfo = 'Left half touch target of Button1 clicked';
        })
      // Example 2: Multiple touch targets (both left half of the button and area below the button)
      Text('Touch target: the left half of the button + the area below it (triggered upon a touch on either part)')
        .fontSize(14)
      Button('Button2 (Multiple Touch Targets)')
        .width(200)
        .height(60)
        // Mouse touch target: array, containing two independent touch targets
        .mouseResponseRegion(\[
          // Touch target 1: left half of the button
          {
            x: 0,
            y: 0,
            width: '50%',
            height: '100%'
          },
          // Touch target 2: area below the button (y=100% indicates the bottom of the button, and the height is 60 vp)
          {
            x: 0,
            y: '100%',
            width: '100%',
            height: 60
          }
        \])
        .onClick(() => {
          this.clickInfo = 'Any touch target of Button2 clicked';
        })
      // Example 3: Touch target outside the button (blank area to the right of the button)
      Text('Touch target: outside the right part of the button (triggered upon a touch on the blank area to the right of the button)')
        .fontSize(14)
      Button('Button3 (Right Outer Touch Target)')
        .width(200)
        .height(60)
        // Mouse touch target: area outside the right side of the button (x=100% indicates the right edge of the button)
        .mouseResponseRegion({
          // X coordinate of the touch target: right edge of the button
          x: '100%',
          y: 0,
          // Touch target width: 80 vp
          width: 80,
          height: '100%'
        })
        .onClick(() => {
          this.clickInfo = 'Right outer touch target of Button3 clicked';
        })
      // Display the click result.
      Text(this.clickInfo)
        .fontSize(16)
        .margin({ top: 20 })
    }
    .width('100%')
    .height('100%')
    // Center the display.
    .justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/3GCvLPxbTY6sOsVGL51O0g/en-us_image_0000002568685171.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7B379D40EEE3B9A12D99B0765481DA9270884C10772ACB5F374DE9FA25285A9)
