# Hyperlink

The **Hyperlink** component implements a link from a location in the component to another location.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/MlU4h545So6sPt9Y5TtOFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=864FDD5C574E807A4A78B17391328F1AE134365EC8687CDA85A011621B557BB7)

-   This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.
-   This component must be used with the system browser.

#### Required Permissions

If Internet access is required, you must apply for the **ohos.permission.INTERNET** permission. For details about how to apply for a permission, see [Declaring Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions).

#### Child Components

This component can contain the [Image](../../images-and-videos/image/document.md) child component.

#### APIs

Hyperlink(address: string | Resource, content?: string | Resource)

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| address | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | Web page to which the hyperlink is redirected. |
| content | string | [Resource](../../common-definitions/basic-types/document.md#resource) | No | 
Text displayed in the hyperlink.

**NOTE**

If this component has child components, the hyperlink text is not displayed.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]color

color(value: Color | number | string | Resource)

Sets the color of the hyperlink text.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Color](../../common-definitions/enums/document.md#color) | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Color of the hyperlink text

Default value of phone: #ff0a59f7

 |

#### Example

This example shows how to create hyperlinks with both images and text that can be clicked to navigate to a specified URL.

@Entry
@Component
struct HyperlinkExample {
  build() {
    Column() {
      Column() {
        Hyperlink('https://example.com/') {
          // Replace $r('app.media.bg') with the image resource file you use.
          Image($r('app.media.bg'))
            .width(200)
            .height(100)
        }
      }

      Column() {
        Hyperlink('https://example.com/', 'Go to the developer website') {
        }
        .color(Color.Blue)
      }
    }.width('100%').height('100%').justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/nn0YdWyzS7S_17wU3e1sgA/en-us_image_0000002537765696.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B42854F89B966B38233A33D37A3A64E074EC21ADF5C412B895F8291F51A6D59)
