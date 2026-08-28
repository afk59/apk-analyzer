# ArcButton

The **ArcButton** component represents an arc button specifically designed for circular screens on wearables. It offers various button styles, such as emphasized, normal, and warning.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/dpjAKnekR5GQdOaEfnU4Lw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9DDEED9A8AD6BB8F87E8B8C031409E60809A576D2F053A05F43B3E297B23EF50)

This component is supported since API version 18. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import {
  ArcButton,
  ArcButtonOptions,
  ArcButtonStatus,
  ArcButtonStyleMode,
  ArcButtonPosition,
}  from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### Events

Among the universal events, the [click event](../../universal-events/interaction-response-events/click-event/document.md) and [touch event](../../universal-events/basic-input-events/touch-event/document.md) are supported.

#### ArcButton

ArcButton({ options: ArcButtonOptions })

Creates an instance of **ArcButton** with configuration parameters.

**Decorator**: @Component

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| options | [ArcButtonOptions](#arcbuttonoptions) | Yes | @Require | Text, background color, shadow, and other parameters of the **ArcButton** component. |

#### ArcButtonOptions

Defines the default or custom style parameters for the **ArcButton** component.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

## Properties

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| position | [ArcButtonPosition](#arcbuttonposition) | No | No | 
Type of the arc button.

Default value: **ArcButtonPosition.BOTTOM\_EDGE**

 |
| styleMode | [ArcButtonStyleMode](#arcbuttonstylemode) | No | No | 

Style mode for the arc button.

Default value: **ArcButtonStyleMode.EMPHASIZED\_LIGHT**

 |
| status | [ArcButtonStatus](#arcbuttonstatus) | No | No | 

Status of the arc button.

Default value: **ArcButtonStatus.NORMAL**

 |
| label | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | Text displayed on the arc button. |
| backgroundBlurStyle | [BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | No | 

Background blur style of the arc button.

Default value: **BlurStyle.NONE**

 |
| backgroundColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | No | 

Background color of the arc button.

This property takes effect only when **ArcButtonStyleMode** is set to **CUSTOM**.

Default value: **Color.Black**

 |
| shadowColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | No | 

Shadow color of the arc button.

Default value: **Color.Black**

 |
| shadowEnabled | boolean | No | No | 

Whether to enable the shadow for the arc button.

Default value: **false**

The value **true** means to enable the shadow, and **false** means the opposite.

 |
| fontSize | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | No | 

Font size of the arc button.

Default value: **19fp**

 |
| fontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | No | 

Font color of the arc button.

This property takes effect only when **ArcButtonStyleMode** is set to **CUSTOM**.

Default value: **Color.White**

 |
| pressedFontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | No | 

Font color of the arc button when pressed.

This property takes effect only when **ArcButtonStyleMode** is set to **CUSTOM**.

Default value: **Color.White**

 |
| fontStyle | [FontStyle](../../common-definitions/enums/document.md#fontstyle) | No | No | 

Font style of the arc button.

Default value: **FontStyle.Normal**

 |
| fontFamily | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | No | Font family of the arc button. |
| fontMargin | [LocalizedMargin](../../common-definitions/basic-types/document.md#localizedmargin12) | No | No | 

Margin of the arc button text.

Default value: **{ start: 24vp, top: 10vp,end: 24vp, bottom: 16vp }**

 |
| onTouch | [Callback](../../common-definitions/basic-types/document.md#voidcallback12)< [TouchEvent](../../universal-events/basic-input-events/touch-event/document.md#touchevent)\> | No | Yes | Callback triggered by touch actions on the arc button. |
| onClick | [Callback](../../common-definitions/basic-types/document.md#voidcallback12)<[ClickEvent](../../universal-events/interaction-response-events/click-event/document.md#clickevent) > | No | Yes | Callback triggered by click actions on the arc button. |

#### \[h2\]constructor

constructor(options: CommonArcButtonOptions)

A constructor used to create an **ArcButton** component.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [CommonArcButtonOptions](#commonarcbuttonoptions) | Yes | Text, background color, shadow, and other parameters of the **ArcButton** component. |

#### CommonArcButtonOptions

Defines the default or custom style parameters for the **ArcButton** component.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| position | [ArcButtonPosition](#arcbuttonposition) | No | Yes | 
Type of the arc button.

Default value: **ArcButtonPosition.BOTTOM\_EDGE**

 |
| styleMode | [ArcButtonStyleMode](#arcbuttonstylemode) | No | Yes | 

Style mode for the arc button.

Default value: **ArcButtonStyleMode.EMPHASIZED\_LIGHT**

 |
| status | [ArcButtonStatus](#arcbuttonstatus) | No | Yes | 

Status of the arc button.

Default value: **ArcButtonStatus.NORMAL**

 |
| label | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | Text displayed on the arc button. |
| backgroundBlurStyle | [BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | Yes | 

Background blur style of the arc button.

Default value: **BlurStyle.NONE**

 |
| backgroundColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Background color of the arc button.

This property takes effect only when **ArcButtonStyleMode** is set to **CUSTOM**.

Default value: **Color.Black**

 |
| shadowColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Shadow color of the arc button.

Default value: **Color.Black**

 |
| shadowEnabled | boolean | No | Yes | 

Whether to enable the shadow for the arc button.

Default value: **false**

The value **true** means to enable the shadow, and **false** means the opposite.

 |
| fontSize | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 

Font size of the arc button.

Default value: **19fp**

 |
| fontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Font color of the arc button.

This property takes effect only when **ArcButtonStyleMode** is set to **CUSTOM**.

Default value: **Color.White**

 |
| pressedFontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Font color of the arc button when pressed.

This property takes effect only when **ArcButtonStyleMode** is set to **CUSTOM**.

Default value: **Color.White**

 |
| fontStyle | [FontStyle](../../common-definitions/enums/document.md#fontstyle) | No | Yes | 

Font style of the arc button.

Default value: **FontStyle.Normal**

 |
| fontFamily | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | Font family of the arc button. |
| fontMargin | [LocalizedMargin](../../common-definitions/basic-types/document.md#localizedmargin12) | No | Yes | 

Margin of the arc button text.

Default value: **{ start: 24vp, top: 10vp,end: 24vp, bottom: 16vp }**

 |
| onTouch | [Callback](../../common-definitions/basic-types/document.md#voidcallback12)< [TouchEvent](../../universal-events/basic-input-events/touch-event/document.md#touchevent)\> | No | Yes | Callback triggered by touch actions on the arc button. |
| onClick | [Callback](../../common-definitions/basic-types/document.md#voidcallback12)<[ClickEvent](../../universal-events/interaction-response-events/click-event/document.md#clickevent) > | No | Yes | Callback triggered by click actions on the arc button. |

#### ArcButtonPosition

Enumerates the types of arc buttons that can be set for **ArcButton**.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

| Name | Value | Description |
| :-- | :-- | :-- |
| TOP\_EDGE | 0 | Upper arc button located at the top of the circular screen. |
| BOTTOM\_EDGE | 1 | Lower arc button located at the bottom of the circular screen. |

#### ArcButtonStyleMode

Enumerates the style modes that can be set for **ArcButton**.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

| Name | Value | Description |
| :-- | :-- | :-- |
| EMPHASIZED\_LIGHT | 0 | Emphasized style in light color mode. Displayed as a blue background with white text. |
| EMPHASIZED\_DARK | 1 | Warning style in dark color mode. Displayed as a red background with white text. |
| NORMAL\_LIGHT | 2 | Normal style in light color mode. Displayed as a dark blue background with blue text. |
| NORMAL\_DARK | 3 | Normal style in dark color mode. Displayed as a dark gray background with blue text. |
| CUSTOM | 4 | Custom button color and font color. |

#### ArcButtonStatus

Enumerates the states that can be set for **ArcButton**.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

| Name | Value | Description |
| :-- | :-- | :-- |
| NORMAL | 0 | Normal state. |
| PRESSED | 1 | Pressed state. |
| DISABLED | 2 | Disabled state. |

#### Example

This example shows the basic usage of the **ArcButton** component, supported since API version 18. The following is an example configuration:

**topOptions** defines an upper arc button with the button text "ButtonTop," a font size of 15 fp, and shadow enabled, in the normal state with a light-color emphasized style.

**bottomOptions** defines a bottom arc button with the button text "ButtonBottom," a font size of 15 fp, shadow enabled, in a light-color emphasized style, with a click event set for the button.

To run this sample code, wearable device support is required. In the project configuration file [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) located in the **src/main** directory, configure **wearable** under [devicetypes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#devicetypes).

// module.json5
{
  "module": {
    // ...
    "deviceTypes": \[
      "wearable",
      "phone"
    \]
    // ...
  }
}

// xxx.ets
import {
  LengthMetrics,
  LengthUnit,
  ArcButton,
  ArcButtonOptions,
  ArcButtonStatus,
  ArcButtonStyleMode,
  ArcButtonPosition,
}  from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local topOptions: ArcButtonOptions = new ArcButtonOptions({});
  @Local bottomOptions: ArcButtonOptions = new ArcButtonOptions({});

  aboutToAppear() {
    this.topOptions = new ArcButtonOptions({
      label: 'ButtonTop',
      status: ArcButtonStatus.NORMAL,
      position: ArcButtonPosition.TOP\_EDGE,
      styleMode: ArcButtonStyleMode.EMPHASIZED\_LIGHT,
      fontSize: new LengthMetrics(15, LengthUnit.FP),
      shadowEnabled: true
    })

    this.bottomOptions = new ArcButtonOptions({
      label: 'ButtonBottom',
      styleMode: ArcButtonStyleMode.EMPHASIZED\_LIGHT,
      fontSize: new LengthMetrics(15, LengthUnit.FP),
      shadowEnabled: true,
      onClick: () => {
        console.info('click from ArcButton.');
      }
    })
  }

  build() {
    Stack() {
      Stack() {
        Circle({ width: 233, height: 233 })
          .strokeWidth(0.1)
          .fill(Color.White)

        Column() {
          ArcButton({ options: this.topOptions })
          Blank()
          ArcButton({ options: this.bottomOptions })

        }.width('100%')
        .height('100%')
      }.width(233)
      .height(233)
    }.width('100%')
    .height('100%')
    .alignContent(Alignment.Center)
    .backgroundColor(Color.Gray)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/3bGjRwGTSZeb8jkohnoyJQ/en-us_image_0000002568765355.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062241Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA451F985272540A9C3905E33268428252F09CB8EAD3E69A0C4C2ADA191DB235)
