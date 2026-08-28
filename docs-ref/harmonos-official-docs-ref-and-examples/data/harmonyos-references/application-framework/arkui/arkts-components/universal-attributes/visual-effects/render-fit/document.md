# Render Fit

The **renderFit** attribute sets how the final state of a component's content is rendered during its width and height animation process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/0Pq5h_nCTCWJSjsiCiyGOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0AC9614806D8DAACAF874F18970DF1C0685571939EF214439B7B14EF59CEF683)

The initial APIs of this module are supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### renderFit

renderFit(fitMode: RenderFit): T

Sets how the final state of the component's content is rendered during its width and height animation process. If it is not set via this API, the content size at the end of the animation is maintained, and the content always remains top-left aligned with the component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fitMode | [RenderFit](../../../common-definitions/enums/document.md#renderfit10) | Yes | Sets how the final state of the component's content is rendered during its width and height animation process. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### renderFit18+

renderFit(fitMode: Optional<RenderFit>): T

Sets how the final state of the component's content is rendered during its width and height animation process. If it is not set via this API, the content size at the end of the animation is maintained, and the content always remains top-left aligned with the component. Compared to [renderFit](#renderfit), this API supports the **undefined** type for the **fitMode** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fitMode | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[RenderFit](../../../common-definitions/enums/document.md#renderfit10)\> | Yes | 
Sets how the final state of the component's content is rendered during its width and height animation process.

If **fitMode** is set to **undefined**, the default value is used, which is equivalent to **RenderFit.TOP\_LEFT**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/Uf7qOENTS3SsdnZpQ0HkTA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE0D8A82ED7497A9A36399B1C15E5EB8FD10681E8A49D2FD136D6B79253BDBA2)

For the [XComponent](../../../rendering-drawing/xcomponent/document.md) component of the TEXTURE or SURFACE type, if the **renderFit** attribute is not set, it defaults to **RenderFit.RESIZE\_FILL**.

For the [XComponent](../../../rendering-drawing/xcomponent/document.md) component of the SURFACE type with an opaque black background color: In versions earlier than API version 18, the **renderFit** attribute only supports **RenderFit.RESIZE\_FILL**; since API version 18, the **renderFit** attribute supports all its available enum values.

For the **XComponent** component created using the [ArkUI NDK API](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ndk-access-the-arkts-page), the [getAttribute](../../../../c-api/structs/arkui-nativenodeapi-1/document.md#getattribute) function is not supported for obtaining the **renderFit** attribute value.

#### Example

This example demonstrates how to set different content fill modes for a component during width and height animations through the **renderFit** attribute.

// xxx.ets
@Entry
@Component
struct RenderFitExample {
  @State width1: number = 100;
  @State height1: number = 30;
  flag: boolean = true;

  build() {
    Column() {
      Text("Hello")
        .width(this.width1)
        .height(this.height1)
        .borderWidth(1)
        .textAlign(TextAlign.Start)
        .renderFit(RenderFit.LEFT)// The component's content stays at the final size and always aligned with the left of the component.
        .margin(20)

      Text("Hello")
        .width(this.width1)
        .height(this.height1)
        .textAlign(TextAlign.Center)
        .borderWidth(1)
        .renderFit(RenderFit.CENTER)// The component's content stays at the final size and always aligned with the center of the component.
        .margin(20)

      Button("animate")
        .onClick(() => {
          this.getUIContext()?.animateTo({ curve: Curve.Ease }, () => {
            if (this.flag) {
              this.width1 = 150;
              this.height1 = 50;
            } else {
              this.width1 = 100;
              this.height1 = 30;
            }
            this.flag = !this.flag;
          })
        })
    }.width("100%").height("100%").alignItems(HorizontalAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/7kvwpmUVTQGrmbwUcHo-KA/en-us_image_0000002568685153.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E9C8315D12A9C1ECA9783452BCF057E59050B574CBBE821C3197CF2544FB4FA)
