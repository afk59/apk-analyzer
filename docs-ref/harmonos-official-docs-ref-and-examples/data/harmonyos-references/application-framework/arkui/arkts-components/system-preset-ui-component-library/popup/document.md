# Popup

The **Popup** component is used to display popups in a specific style.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/uY9ihg_zQMKJx8_bl-kiXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EB426DA09AFFB3753B23D5BF1464BB49AD16F59245B1EA17AA33E30D89BE5562)

-   This component is supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.
-   Use this component with the custom popup features in [popup control](../../universal-attributes/dialog-box-control/popup-control/document.md) for best results.

#### Modules to Import

import { Popup, PopupOptions, PopupTextOptions, PopupButtonOptions, PopupIconOptions } from '@kit.ArkUI';

#### Child Components

Not supported

#### Popup

Popup(options: PopupOptions): void

**Decorator**: @Builder

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [PopupOptions](#popupoptions) | Yes | Parameters of the popup. |

#### PopupOptions

Defines the style parameters of the popup.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| icon | [PopupIconOptions](#popupiconoptions) | No | Yes | 
Icon of the popup.

**NOTE**

The icon is not displayed when **width** and **height** are set to an invalid value or **0**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| title | [PopupTextOptions](#popuptextoptions) | No | Yes | 

Title of the popup.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| message | [PopupTextOptions](#popuptextoptions) | No | No | 

Content of the popup.

**NOTE**

**fontWeight** is not available for **messages**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| showClose | boolean | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 

Whether to show the close button.

**true**: Show the close button. **false**: Do not show the close button.

**Resource**: Show the corresponding icon.

Default value: **true**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onClose | () => void | No | Yes | 

Callback for the popup close button.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| buttons | \[[PopupButtonOptions](#popupbuttonoptions)?,[PopupButtonOptions](#popupbuttonoptions)?\] | No | Yes | 

Buttons of the popup. A maximum of two buttons can be set.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| direction12+ | [Direction](../../common-definitions/enums/document.md#direction) | No | Yes | 

Layout direction.

Default value: **Direction.Auto**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| maxWidth18+ | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Maximum width of the popup. This API allows the popup to display with a custom width.

**NOTE**

1\. When using resource references, ensure that the parameter type matches the attribute method type.

2\. **maxWidth** accepts numeric values (both floating-point and integer values), such as **$r('app.float.maxWidth')** and **$r('app.integer.maxWidth')**.

3\. When the type is Resource, values default to px units if no unit is explicitly specified.

Default value: **400vp**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### PopupTextOptions

Provides text style settings.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| text | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | Text content. |
| fontSize | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 
Text font size.

Default value: **$r('sys.float.ohos\_id\_text\_size\_body2')**

The string value must be convertible to a number (for example, **'10'**) or include a length unit (for example, **'10px'**); percentage-based strings are not supported.

Value range of number values: (0, +∞)

 |
| fontColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Text font color.

Default value: **$r('sys.color.ohos\_id\_color\_text\_secondary')**

 |
| fontWeight | number | [FontWeight](../../common-definitions/enums/document.md#fontweight) | string | No | Yes | 

Text font weight.

For the number type, the value ranges from 100 to 900, at an interval of 100. A larger value indicates a heavier font weight. The default value is **400**.

For the string type, only strings of the number type are supported, for example, **"400"**, **"bold"**, **"bolder"**, **"lighter"**, **"regular"**, and **"medium"**, which correspond to the enumerated values in **FontWeight**.

Default value: **FontWeight.Regular**

 |

#### PopupButtonOptions

Defines the button attributes and events.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| text | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | Text of the button. |
| action | () => void | No | Yes | Click callback of the button. |
| fontSize | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 
Font size of the button text.

Default value: **$r('sys.float.ohos\_id\_text\_size\_button2')**

The string value must be convertible to a number (for example, **'10'**) or include a length unit (for example, **'10px'**); percentage-based strings are not supported.

Invalid values are handled as default values.

 |
| fontColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Font color of the button text.

Default value: **$r('sys.color.ohos\_id\_color\_text\_primary\_activated')**

 |

#### PopupIconOptions

Defines the icon options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| image | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | Icon content. |
| width | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 
Icon width.

Default value: **32VP**

 |
| height | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Icon height.

Default value: **32VP**

 |
| fillColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | Icon fill color. This property applies only to an SVG image. |
| borderRadius | [Length](../../common-definitions/basic-types/document.md#length) | [BorderRadiuses](../../common-definitions/basic-types/document.md#borderradiuses9) | No | Yes | 

Rounded corner of the icon.

Default value: **$r('sys.float.ohos\_id\_corner\_radius\_default\_s')**

 |

#### Example

## Example 1: Setting the Popup Style

This example demonstrates how to customize the style of a popup by configuring **PopupIconOptions**, **PopupTextOptions**, and **PopupButtonOptions**.

// xxx.ets
import { Popup, PopupTextOptions, PopupButtonOptions, PopupIconOptions } from '@kit.ArkUI';

@Entry
@Component
struct PopupExample {
  build() {
    Row() {
      // Define a popup.
      Popup({
        // Set the icon through PopupIconOptions.
        icon: {
          // Replace $r('app.media.icon') with the image resource file you use.
          image: $r('app.media.icon'),
          width: 32,
          height: 32,
          fillColor: Color.White,
          borderRadius: 16
        } as PopupIconOptions,
        // Set the text through PopupTextOptions.
        title: {
          text: 'This is a popup with PopupOptions',
          fontSize: 20,
          fontColor: Color.Black,
          fontWeight: FontWeight.Normal
        } as PopupTextOptions,
        // Set the text through PopupTextOptions.
        message: {
          text: 'This is the message',
          fontSize: 15,
          fontColor: Color.Black
        } as PopupTextOptions,
        showClose: false,
        onClose: () => {
          console.info('close Button click');
        },
        // Set the button through PopupButtonOptions.
        buttons: \[{
          text: 'confirm',
          action: () => {
            console.info('confirm button click');
          },
          fontSize: 15,
          fontColor: Color.Black,
        },
          {
            text: 'cancel',
            action: () => {
              console.info('cancel button click');
            },
            fontSize: 15,
            fontColor: Color.Black
          },\] as \[PopupButtonOptions?, PopupButtonOptions?\]
      })
    }
    .width(300)
    .height(200)
    .borderWidth(2)
    .justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/4Hni6rXxRnCLtjJGWytPXQ/en-us_image_0000002537925922.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5ED114D7D38AE3A13ECD4D419B8320D9D29A4D759E28996BC0AE6530ED290B8A)

## Example 2: Implementing a Mirrored Layout

This example shows how to implement a mirrored layout for a popup by configuring **direction**.

// xxx.ets
import { Popup, PopupTextOptions, PopupButtonOptions, PopupIconOptions } from '@kit.ArkUI';

@Entry
@Component
struct PopupPage {
  @State currentDirection: Direction = Direction.Rtl;

  build() {
    Column() {
      // Define a popup.
      Popup({
        // Set the icon through PopupIconOptions.
        direction: this.currentDirection,
        icon: {
          // Replace $r('app.media.icon') with the image resource file you use.
          image: $r('app.media.icon'),
          width: 32,
          height: 32,
          fillColor: Color.White,
          borderRadius: 16,
        } as PopupIconOptions,
        // Set the text through PopupTextOptions.
        title: {
          text: 'This is a popup with PopupOptions',
          fontSize: 20,
          fontColor: Color.Black,
          fontWeight: FontWeight.Normal,

        } as PopupTextOptions,
        // Set the text through PopupTextOptions.
        message: {
          text: 'This is the message',
          fontSize: 15,
          fontColor: Color.Black,
        } as PopupTextOptions,
        showClose: true,
        onClose: () => {
          console.info('close Button click');
        },
        // Set the button through PopupButtonOptions.
        buttons: \[{
          text: 'confirm',
          action: () => {
            console.info('confirm button click');
          },
          fontSize: 15,
          fontColor: Color.Black,

        },
          {
            text: 'cancel',
            action: () => {
              console.info('cancel button click');
            },
            fontSize: 15,
            fontColor: Color.Black,
          },\] as \[PopupButtonOptions?, PopupButtonOptions?\],
      })

    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/QFOArYaGRr6bjHjExHKU6Q/en-us_image_0000002568685699.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97B8EDC9358D669876B45ACD50A03C71F1A5B2BB7FD372B3348CD2BCB7A11559)

## Example 3: Setting the Custom Width

This example demonstrates how to set the custom width for a popup using **maxWidth**.

// xxx.ets
import { Popup, PopupTextOptions, PopupButtonOptions, PopupIconOptions } from '@kit.ArkUI';

@Entry
@Component
struct PopupPage {
  @State currentDirection: Direction = Direction.Rtl;

  build() {
    Row() {
      // Define a popup.
      Popup({
        // Set the custom width.
        maxWidth: '50%',
        // Set the icon through PopupIconOptions.
        icon: {
          // Replace $r('app.media.startIcon') with the image resource file you use.
          image: $r('app.media.startIcon'),
          width: 32,
          height: 32,
          fillColor: Color.White,
          borderRadius: 16,
        } as PopupIconOptions,
        // Set the text through PopupTextOptions.
        message: {
          text: 'This is the message. This is the message. This is the message. This is the message.',
          fontSize: 15,
          fontColor: Color.Black
        } as PopupTextOptions,
        showClose: false,
        onClose: () => {
          console.info('close Button click');
        },
        // Set the button through PopupButtonOptions.
        buttons: \[{
          text: 'OK',
          action: () => {
            console.info('confirm button click');
          },
          fontSize: 15,
          fontColor: Color.Black,
        },
          {
            text: 'Cancel',
            action: () => {
              console.info('cancel button click');
            },
            fontSize: 15,
            fontColor: Color.Black
          },\] as \[PopupButtonOptions?, PopupButtonOptions?\]
      })
    }
    .width(400)
    .height(200)
    .borderWidth(2)
    .justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/glRIaC9ZR0KeKadEA9g4RA/en-us_image_0000002568765709.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02D2A983CB16453B75F446B3504B376EB470497AEEE859A10802EB1D1A576A28)
