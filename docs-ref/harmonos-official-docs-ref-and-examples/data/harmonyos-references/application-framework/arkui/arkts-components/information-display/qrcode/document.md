# QRCode

The **QRCode** component is used to display a QR code.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/fDa6A0avTO2CpDn4xcMCTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1327FE4BD2E58C918BFB27F3D8210193E6B078D7F5DAD3349879ADD408FE2EA9)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

The pixel count of the **QRCode** component is subject to the content. If the component size is not large enough, the content may fail to be displayed. In this case, you need to resize the component.

#### Child Components

Not supported

#### APIs

QRCode(value: ResourceStr)

Creates a **QRCode** component. The displayed QR code can be scanned to obtain the encoded string information.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 
Content of the QR code. A maximum of 512 characters are supported. If this limit is exceeded, the first 512 characters are used.

The Resource type is supported since API version 20.

**NOTE**

If this parameter is set to **null**, it is equivalent to passing the string **"null"**. If it is set to **undefined**, it is equivalent to passing the string **"undefined"**. Passing an empty string will result in an invalid QR code.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]color

color(value: ResourceColor)

Sets the color of the QR code.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
QR code color. The default value is **'#ff000000'** and does not change with the system color mode.

 |

#### \[h2\]backgroundColor

backgroundColor(value: ResourceColor)

Sets the background color of the QR code.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Background color of the QR code.

Default value: **Color.White**

Since API version 11, the default value is **'#ffffffff'** and does not change with the system color mode.

 |

#### \[h2\]contentOpacity11+

contentOpacity(value: number | Resource)

Sets the opacity of the QR code content. The minimum value is 0, and the maximum value is 1.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Opacity of the QR code content.

Default value: **1**

Value range: \[0, 1\]. If the value is out of the range, the default value is used.

 |

#### Events

Among the universal events, the [click event](../../universal-events/interaction-response-events/click-event/document.md), [touch event](../../universal-events/basic-input-events/touch-event/document.md), and [show/hide event](../../universal-events/component-change-events/show-hide-event/document.md) are supported.

#### Example

## Example 1: Setting the Color, Background Color, and Opacity

This example demonstrates the basic usage of the **QRCode** component. It sets the QR code color using the [color](#color) attribute, the background color using the [backgroundColor](#backgroundcolor) attribute, and the opacity using the [contentOpacity](#contentopacity11) attribute.

// xxx.ets
@Entry
@Component
struct QRCodeExample {
  private value: string = 'hello world';

  build() {
    Column({ space: 5 }) {
      Text('normal').fontSize(9).width('90%').fontColor(0xCCCCCC).fontSize(30)
      QRCode(this.value).width(140).height(140)

      // Set the color of the QR code.
      Text('color').fontSize(9).width('90%').fontColor(0xCCCCCC).fontSize(30)
      QRCode(this.value).color(0xF7CE00).width(140).height(140)

      // Set the background color of the QR code.
      Text('backgroundColor').fontSize(9).width('90%').fontColor(0xCCCCCC).fontSize(30)
      QRCode(this.value).width(140).height(140).backgroundColor(Color.Orange)

      // Set the opacity of QR code content.
      Text('contentOpacity').fontSize(9).width('90%').fontColor(0xCCCCCC).fontSize(30)
      QRCode(this.value).width(140).height(140).color(Color.Black).contentOpacity(0.1)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/B7rL5AUlQTGLowKaI5AQOg/en-us_image_0000002537765792.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB88119C43DC36D9E0D3933BD67239837C6C942A4E551F7799DF656F1C528B9B)

## Example 2: Setting the Background Color to Transparent

This example shows how to set the QR code background color to transparent using the [backgroundColor](#backgroundcolor) attribute, allowing the QR code content to blend with the background.

// xxx.ets
@Entry
@Component
struct QRCodeExample {
  private value: string = 'hello world';

  build() {
    Column({ space: 5 }) {
      RelativeContainer() {
        // Replace $r('app.media.ocean') with the image resource file you use.
        Image($r('app.media.ocean'))
        // Set the QR code background color to transparent.
        QRCode(this.value).width(200).height(200).backgroundColor('#00ffffff')
      }.width(200).height(200)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/XTn2jdrOSZ6WxEMHLGyWpQ/en-us_image_0000002537925732.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B16AB0744C19D6A1F8FDC78239EA59C40477F190CC036E0FA54FC4938BD0AF0)
