# Component-Level Pixel Rounding

Component-level pixel rounding allows you to enable or disable system pixel rounding for individual components by simply setting the **pixelRound** attribute.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/RqqqXV_9SjOODWtkGAaduQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1911F12F5BB99C4BEE0192C73A583DF5915629652C7B5EFA0D4762A4EBBF6462)

The initial APIs of this module are supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.

#### pixelRound

pixelRound(value: PixelRoundPolicy): T

Sets the pixel rounding policy for the current component in the specified direction. If a direction is not set, the pixels are rounded to the nearest whole number in that direction.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/3c-NiLjEQb2I0b0lhM6eYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A012BD8AD48EAA2DFBDAE05C9553706D1E65B4AB14CCFAB68A9CA1D467B9844)

-   In API version 11, this API uses half-pixel alignment (that is, 0-0.25 rounds to 0, 0.25-0.75 rounds to 0.5, 0.75-1.0 rounds to 1). Since API version 12, this API rounds pixels to the nearest integers and allows you to disable pixel rounding for individual components.
    
-   This API can be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.
    

In normal calculations, the vertical direction (top and bottom) correspond to the component height, and the horizontal direction (the starting direction of mirroring is considered "left") correspond to the component width. For ease of description, these two sets of directions are referred to as top-left and bottom-right.

-   Calculate the top-left coordinates of the current component: offset of the top-left corner relative to the parent container.
-   Calculate the bottom-right coordinates of the current component: offset of the top-left corner relative to the parent container plus the size of the component itself.
-   Recalculate the size of the current component: bottom-right corner rounded value minus the top-left corner rounded value.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [PixelRoundPolicy](#pixelroundpolicy) | Yes | 
Rounding policy for the bounds of the component.

**NOTE**

This attribute is applicable in scenarios where artifacts occur due to floating-point drawing. The rounding result is related not only to the component's width and height but also to its position. Even if the component's width and height are set to be the same, due to different floating-point positions described, the final width and height of the component may also be different after rounding.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### PixelRoundPolicy

Enumerates the directions of pixel rounding at the component level.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start | [PixelRoundCalcPolicy](../../../common-definitions/enums/document.md#pixelroundcalcpolicy11) | No | Yes | 
Rounding alignment for the component's start edge.

Invalid values are rounded using the round‑half‑up rule.

 |
| top | [PixelRoundCalcPolicy](../../../common-definitions/enums/document.md#pixelroundcalcpolicy11) | No | Yes | 

Rounding alignment for the component's top edge.

Invalid values are rounded using the round-half-up rule.

 |
| end | [PixelRoundCalcPolicy](../../../common-definitions/enums/document.md#pixelroundcalcpolicy11) | No | Yes | 

Rounding alignment for the component's end edge.

Invalid values are rounded using the round-half-up rule.

 |
| bottom | [PixelRoundCalcPolicy](../../../common-definitions/enums/document.md#pixelroundcalcpolicy11) | No | Yes | 

Rounding alignment for the component's bottom edge.

Invalid values are rounded using the round-half-up rule.

 |

#### FAQs

| Issue | Solution |
| :-- | :-- |
| When a child component is intended to fully fill its parent container, a 1px gap appears due to inconsistent rounding behaviors (the parent container rounds up, while the child component rounds down) of offset and size values. | 
1\. Use the ceil rounding method for the child component in the direction where the gap appears.

2\. Disable pixel rounding for both parent and child components.

 |
| When a **List** component is configured with dividers set, the dividers may disappear under specific cases. | 

1\. Set a 2 px space on the **List** component.

2\. Disable pixel rounding on the corresponding components.

 |
| Overlapping occurs on specific devices. | 

1\. Set a 2 px space on the **List** component.

2\. Disable pixel rounding on the component.

3\. Obtain the DPI value of the device through media query APIs and implement customized adaptation.

 |
| When a component is rendered with an animation, there is a slight flicker. | Disable pixel rounding on the corresponding components. |
| The layout within a container is compact, and the sizes of child components are inconsistent. | Disable pixel rounding on the corresponding components. |

#### Example

This example shows how to use **pixelRound** to guide layout adjustments when there is a 1 px gap in the parent component.

@Entry
@Component
struct PixelRoundExample {
    @State curWidth : number = 300;

    build() {
        Column() {
            Button(){
                Text(this.curWidth.toString())
            }
            .onClick(() => {
                this.curWidth += 0.1;
            })
            .height(200)
            .width(200)
            .backgroundColor('rgb(213, 213, 213)')

            Blank().height(20)

            Row() {
                Row() {
                }
                .width('100%')
                .height('100%')
                .backgroundColor(Color.Yellow)
                .pixelRound({
                    start : PixelRoundCalcPolicy.NO\_FORCE\_ROUND,
                    end : PixelRoundCalcPolicy.NO\_FORCE\_ROUND,
                })
            }
            .width(this.curWidth.toString() + 'px')
            .height('300.6px')
            .backgroundColor(Color.Red)
            .pixelRound({
                start : PixelRoundCalcPolicy.NO\_FORCE\_ROUND,
                end : PixelRoundCalcPolicy.NO\_FORCE\_ROUND,
            })
        }
        .width("100%")
        .height('100%')
        .backgroundColor('#ffe5e5e5')
    }
}

In this example, when pixel rounding is initially disabled (that is, the **pixelRound** attribute is not set on the parent and child components), the component appearance is normal. You can increase the width of the parent component by clicking the button. The initial width is set at 301.2 px to provide a baseline for observing visual changes. As you increase the width, you may notice that at certain widths, a 1 px gap appears on the right side of the parent component. You can modify the example code to perform similar tests in the vertical dimension to see whether a similar issue occurs when the height of the components is changed.

**Figure 1** Layout with pixelRound

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/1CWMxyTyQ6uSmH2l13OJ5A/en-us_image_0000002568765139.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D65E641F623452AC7896BB9FE28597698393EBFAD7DCCDCDEF855541F36C5C7D)

**Figure 2** Layout without pixelRound

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/1g5YkJ1FSfyEOD5jxy1rvw/en-us_image_0000002537765414.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D012A5EEA07DCF24956AD72360ADE929E40C70E592A46F3BFA70A8210A4E0595)
