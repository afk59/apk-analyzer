# Component Size Change Event

The size change event is triggered whenever the component's size changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/CFFGxyfQSieDlb1k_sUZlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CEB7CE592908058DB27D030D49DBB05958499EE02AC42B5F9482C73D6978680)

The initial APIs of this module are supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

The width and height returned by this event represent the component's post-rendering size, which may differ from the preset width and height values of the component.

#### onSizeChange

onSizeChange(event: SizeChangeCallback): T

Triggered when the component size changes due to layout updates.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/9-cUwkgGRGG10jyc3AH1SA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D65E5C760BB881C78722437F1ABA4AC7BD3D7FB1499E90388727B46AA132EBC2)

1.  This API is triggered upon layout changes. Due to calculation precision limitations, the return value may deviate slightly from the actual physical size.
    
2.  **onSizeChange** is a synchronous callback triggered during the layout process. Directly modifying state variables within **onSizeChange** may cause the changes to be included in the animation closure. Specifically, animations compare the layout state before the animation starts with the state after the animation closure is executed. If the **onSizeChange** callback is triggered synchronously during the pre-animation layout phase, the changes made in this callback will be processed as part of the animation, along with the changes in the animation closure. To avoid this issue, you can use [setTimeout](../../../../../../common-capabilities/arkts-api/timer/document.md#settimeout) or [postFrameCallback](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#postframecallback12) (with a 0 ms delay) inside **onSizeChange** to defer the UI processing logic to asynchronous execution.
    

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [SizeChangeCallback](#sizechangecallback) | Yes | Size of the component before and after the change. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### SizeChangeCallback

type SizeChangeCallback = (oldValue: SizeOptions, newValue: SizeOptions) => void

Invoked when the component size changes.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| oldValue | [SizeOptions](../../../common-definitions/basic-types/document.md#sizeoptions) | Yes | Width and height of the component before the change. |
| newValue | [SizeOptions](../../../common-definitions/basic-types/document.md#sizeoptions) | Yes | Width and height of the component after the change. |

#### Example

This example demonstrates how to set a size change event for a **Text** component. When the size of the **Text** component changes, the **onSizeChange** event is triggered, allowing you to obtain relevant parameters.

// xxx.ets
@Entry
@Component
struct AreaExample {
  @State value: string = 'Text'
  @State sizeValue: string = ''

  build() {
    Column() {
      Text(this.value)
        .backgroundColor(Color.Green)
        .margin(30)
        .fontSize(20)
        .onClick(() => {
          this.value = this.value + 'Text'
        })
        .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
          console.info(\`Ace: on size change, oldValue is ${JSON.stringify(oldValue)} value is ${JSON.stringify(newValue)}\`)
          this.sizeValue = JSON.stringify(newValue)
        })
      Text('new area is: \\n' + this.sizeValue).margin({ right: 30, left: 30 })
    }
    .width('100%').height('100%').margin({ top: 30 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/OiCulHwGRRaxl4vQtl_H4A/en-us_image_0000002568685103.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5944AC55B7A8B0EFA28F128967C60E3F3BB3FBB959C724712F22AF89CB1F3021)
