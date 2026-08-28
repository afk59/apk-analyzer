# Tooltip Control

You can bind a floating tooltip to a component. The tooltip automatically appears when a pointer hovers over the component and disappears when the pointer moves away.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/qCjduI45Q-aFdXZfmrB_ew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D87281F403A82720E668DEAAA736C1139EEFD16E2FC6B838E908C0F76AAA18A1)

-   This feature is supported since API version 19. Updates will be marked with a superscript to indicate their earliest API version.
    
-   Currently, this feature supports only external mouse devices, styluses, and touchpads as pointers.
    

#### bindTips

bindTips(message: TipsMessageType, options?: TipsOptions): T

Binds a tooltip to the component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/L9rtO_vWQYGY7wLBOnArOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3B50085CD651AD04C9A32052F2069D42A73C7F9B2ED0730E1D4DF5C22708671)

If the universal attribute [enable](../../interaction-properties/enable-disable-control/document.md#enabled) of the component bound to **bindTips** is set to **false**, a floating tooltip can still be displayed.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| message | [TipsMessageType](#tipsmessagetype) | Yes | Content of the tooltip message. |
| options | [TipsOptions](#tipsoptions) | No | 
Parameters of the tooltip.

Default value:

{

appearingTime: 700,

disappearingTime: 300,

appearingTimeWithContinuousOperation: 300,

disappearingTimeWithContinuousOperation: 0, enableArrow: true,

arrowPointPosition: ArrowPointPosition.CENTER,

arrowWidth: 16,arrowHeight: 8,

showAtAnchor: TipsAnchorType.TARGET

}

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### TipsOptions

Defines the parameters of the tooltip.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| appearingTime | number | No | Yes | 
Delay before the tooltip appears. The maximum delay is 4000 ms. Values exceeding 4000 ms are capped at 4000 ms.

Default value: **700**.

Unit: ms.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| disappearingTime | number | No | Yes | 

Delay before the tooltip disappears. The maximum delay is 4000 ms. Values exceeding 4000 ms are capped at 4000 ms.

Default value: **300**.

Unit: ms.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| appearingTimeWithContinuousOperation | number | No | Yes | 

Delay before the tooltip appears when multiple tooltips are displayed consecutively. The maximum delay is 4000 ms. Values exceeding 4000 ms are capped at 4000 ms.

Default value: **300**.

Unit: ms.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| disappearingTimeWithContinuousOperation | number | No | Yes | 

Delay before the tooltip disappears when multiple tooltips are displayed consecutively. The maximum delay is 4000 ms. Values exceeding 4000 ms are capped at 4000 ms.

Default value: **0**.

Unit: ms.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| enableArrow | boolean | No | Yes | 

Whether to display the tooltip arrow.

Default value: **true**.

**true**: yes. **false**: no.

**NOTE**

If the available space on the screen is insufficient, the tooltip will cover part of the component and the arrow will not be displayed.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| arrowPointPosition | [ArrowPointPosition](../../../common-definitions/enums/document.md#arrowpointposition11) | No | Yes | 

Position of the tooltip arrow relative to its parent component. Available positions are **Start**, **Center**, and **End**, in both vertical and horizontal directions. These positions are within the parent component area and do not exceed its boundaries or cover rounded corners.

Default value: **ArrowPointPosition.CENTER**.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| arrowWidth | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Width of the tooltip arrow. If the set width exceeds the length of the edge minus twice the tooltip's corner radius, the arrow is not drawn.

Default value: **16**.

Unit: vp.

**NOTE**

Percentage values are not supported.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| arrowHeight | [Dimension](../../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Height of the tooltip arrow.

Default value: **8**.

Unit: vp.

**NOTE**

Percentage values are not supported.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| showAtAnchor20+ | [TipsAnchorType](../../../common-definitions/enums/document.md#tipsanchortype20) | No | Yes | 

Anchor type of the tooltip

Default value: **TipsAnchorType.TARGET**.

**NOTE**

If the anchor type of the tooltip is **TipsAnchorType.CURSOR**, the tooltip does not display an arrow.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### TipsMessageType

type TipsMessageType = ResourceStr | StyledString

Provides information about the tooltip.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [ResourceStr](../../../common-definitions/basic-types/document.md#resourcestr) | Type used to represent the types that can be used by input parameters of the string type. |
| [StyledString](../../../text-and-input/styled-string/document.md#styledstring) | Styled string. |

#### Example

You can preview how this component looks on a real device, but not in DevEco Studio Previewer.

## Example 1: Binding a Tooltip

This example shows how to bind a tooltip to a button using **bindTips**.

// xxx.ets
@Entry
@Component
struct TipsExample {
  build() {
    Flex({ direction: FlexDirection.Column }) {
      Button('Hover Tips')
        .bindTips("Tips", {
          appearingTime: 700,
          disappearingTime: 300,
          appearingTimeWithContinuousOperation: 300,
          disappearingTimeWithContinuousOperation: 0,
          enableArrow: true,
        })
        .position({ x: 100, y: 250 })
    }.width('100%').padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/p65OKbm3QMe0ATJUD4aTEQ/en-us_image_0000002537925402.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75CF2A4ED9217FACB6DD9BBF2B9356CB869EEBD92F551AA01D69ADC7E865DBC3)

## Example 2: Displaying and Hiding Multiple Tooltips

This example demonstrates how to configure multiple tooltips to appear and disappear in sequence using **bindTips**.

// xxx.ets

@Entry
@Component
struct TipsExample {
  build() {
    Flex({ direction: FlexDirection.Column }) {
      Button('Hover Tips')
        .bindTips("Tips", {
          appearingTime: 700,
          disappearingTime: 300,
          appearingTimeWithContinuousOperation: 300,
          disappearingTimeWithContinuousOperation: 0,
          enableArrow: true,
        })
        .position({ x: 100, y: 250 })

      Button('Hover Tips')
        .bindTips("Tips", {
          appearingTime: 700,
          disappearingTime: 300,
          appearingTimeWithContinuousOperation: 300,
          disappearingTimeWithContinuousOperation: 0,
          enableArrow: true,
        })
        .position({ x: 100, y: 350 })

    }.width('100%').padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/QRKIhRdHSk2nfsUGDace5w/en-us_image_0000002568685179.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4879CE47F94E60372EECA50F6827754EC82E753117DCA5BC0278559A81CC3A6A)
