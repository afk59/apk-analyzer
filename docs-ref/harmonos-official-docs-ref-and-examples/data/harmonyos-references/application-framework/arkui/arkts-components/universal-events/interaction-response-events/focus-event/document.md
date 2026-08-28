# Focus Event

A focus event is triggered when the page focus moves between components. It can be used to process related logic within the component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/TbxFIhkfTBKmCjTTPr5Shg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08E8E6EA52479788CADE5131943740DADB0711588BD74CC9913D35DFD98D6E7E)

-   The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   Sequential keyboard navigation is not supported for nested scrollable components.
    
-   Components that have default interaction logic, such as [Button](../../../buttons-and-selections/button/document.md) and [TextInput](../../../text-and-input/textinput/document.md), are focusable by default. Other components, such as [Text](../../../text-and-input/text/document.md) and [Image](../../../images-and-videos/image/document.md), are not focusable by default. Only focusable components can trigger a focus event. To enable a component to be focusable, set its [focusable](../../../universal-attributes/interaction-properties/focus-control/document.md#focusable) attribute to **true**.
    
-   Container components that can gain focus, such as [Stack](../../../rows-columns-and-stacking/stack/document.md) and [Row](../../../rows-columns-and-stacking/row/document.md), are not focusable if they do not have any focusable child components. When configured with an **onClick** event or a single-finger tap gesture, the component implicitly becomes focusable if the **focusable** attribute is not explicitly set.
    
-   For details about focus development and component focusability, see [Implementing Focus Support](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event).
    

#### onFocus

onFocus(event: () => void): T

Triggered when the current component obtains focus.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback function of **onFocus**, indicating that the component has gained focus. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onBlur

onBlur(event:() => void): T

Triggered when the current component loses focus.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback function of **onBlur**, which indicates that the component has lost focus. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Example

This example demonstrates how components gain and lose focus. The colors of the buttons change when they gain or lose focus.

// xxx.ets
@Entry
@Component
struct FocusEventExample {
  @State oneButtonColor: string = '#0066FF'
  @State twoButtonColor: string = '#87CEFA'
  @State threeButtonColor: string = '#90EE90'

  build() {
    Column({ space: 20 }) {
      // Activate the focus by pressing \*\*Tab\*\* on an external keyboard and navigate it among the three buttons using the up/down arrow keys. The focused button receives a color highlight, which disappears when focus moves away.
      Button('First Button')
        .backgroundColor(this.oneButtonColor)
        .width(260)
        .height(70)
        .fontColor(Color.Black)
        .focusable(true)
        .onFocus(() => {
          this.oneButtonColor = '#FFFFFF'
        })
        .onBlur(() => {
          this.oneButtonColor = '#0066FF'
        })
      Button('Second Button')
        .backgroundColor(this.twoButtonColor)
        .width(260)
        .height(70)
        .fontColor(Color.Black)
        .focusable(true)
        .onFocus(() => {
          this.twoButtonColor = '#FFFFFF'
        })
        .onBlur(() => {
          this.twoButtonColor = '#87CEFA'
        })
      Button('Third Button')
        .backgroundColor(this.threeButtonColor)
        .width(260)
        .height(70)
        .fontColor(Color.Black)
        .focusable(true)
        .onFocus(() => {
          this.threeButtonColor = '#FFFFFF'
        })
        .onBlur(() => {
          this.threeButtonColor = '#90EE90'
        })
    }.width('100%').margin({ top: 20 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/zuxMjPUDTn2Gk6tNtO1JDw/en-us_image_0000002568765107.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDD45AC13D1149EF3599CA739EEC4C6C4099B0469FF19A04F58FE591943D4756)
