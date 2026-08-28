# Foreground Effect

You can set the foreground effect for a component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/EGQFfZpBSDan_BtKncX46A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBBF51BF7EA05D4032548966C911F43D4BA9A05EA001443A56CA79F93F58D9F0)

The initial APIs of this module are supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### foregroundEffect

foregroundEffect(options: ForegroundEffectOptions): T

Sets the foreground effect of a component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ForegroundEffectOptions](#foregroundeffectoptions12) | Yes | Foreground effect settings, including the blur radius. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### ForegroundEffectOptions12+

Describes the foreground effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| radius | number | No | No | 
Blur radius. The value range is \[0, +∞).

This parameter takes effect only within the component scope. When it is used with other APIs, the effect beyond the component scope does not apply.

 |

#### Example

This example demonstrates how to set the foreground effect using **foregroundEffect**.

// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Row() {
      // Replace $r("app.media.icon") with the image resource file you use.
      Image($r('app.media.icon'))
          .width(100)
          .height(100)
          .foregroundEffect({ radius: 20 })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

Below is how the component looks with the foreground effect applied.

**radius** indicates the blur radius. A larger value creates a more blurred effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/nR7ZBlsmQCa3kFqhnUqJww/en-us_image_0000002537925372.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=078380AD2E306B40A2810C9D1C0CC7201D44AE37C8CE8FD6CA4CA3AFD6AE7E5A)
