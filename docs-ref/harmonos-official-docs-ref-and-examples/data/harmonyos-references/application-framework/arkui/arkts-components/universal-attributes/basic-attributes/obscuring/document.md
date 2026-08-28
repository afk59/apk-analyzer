# Obscuring

When needed, you can obscure content of a component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/55iKY1VlSY2pAmGL3pszRw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B1C1B847FE92395B73158C0A4A7A7E8E9B516A3D7AD26885077B21BA39EA0CA)

The initial APIs of this module are supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### obscured

obscured(reasons: Array<ObscuredReasons>): T

Sets how the component content is obscured.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| reasons | Array<[ObscuredReasons](../../../common-definitions/enums/document.md#obscuredreasons10)\> | Yes | 
How the component content is obscured.

Default value: **\[\]**

This API is only available for the [Image](../../../images-and-videos/image/document.md) and [Text](../../../text-and-input/text/document.md) components.

**NOTE**

To obscure an image when it is being loaded, you must set the width and height of the **Image** component.

Obscuring is not available for **Text** components that have child components or have any [styled string](../../../text-and-input/styled-string/document.md) configured.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Example

This example demonstrates how to obscure the content of **Text** and **Image** components using the **obscured** API.

// xxx.ets
@Entry
@Component
struct ObscuredExample {
  build() {
    Row() {
      Column() {
        Text('Text not set obscured attribute').fontSize(10).fontColor(Color.Black)
        Text('This is an example for text obscured attribute.')
          .fontSize(30)
          .width('600px')
          .fontColor(Color.Black)
          .border({ width: 1 })
        Text('Image not set obscured attribute').fontSize(10).fontColor(Color.Black)
        // Replace $r('app.media.icon') with the image resource file you use.
        Image($r('app.media.icon'))
          .width('200px')
          .height('200px')
        Text('Text set obscured attribute').fontSize(10).fontColor(Color.Black)
        Text('This is an example for text obscured attribute.')
          .fontSize(30)
          .width('600px')
          .fontColor(Color.Black)
          .border({ width: 1 })
          .obscured(\[ObscuredReasons.PLACEHOLDER\])
        Text('Image set obscured attribute').fontSize(10).fontColor(Color.Black)
        // Replace $r('app.media.icon') with the image resource file you use.
        Image($r('app.media.icon'))
          .width('200px')
          .height('200px')
          .obscured(\[ObscuredReasons.PLACEHOLDER\])
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/yatffIZ2Scq4CN3D4yMNIQ/en-us_image_0000002568685115.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5ECD3561D3A790904694D8F873FED81D61EEB07496A972315139044B249F306)
