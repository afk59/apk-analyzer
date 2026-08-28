# Visual Effect

The visual effect attributes set filter effects (such as blur and pixel stretch) and non-filter effects (such as point light) for components.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/VY69r386SheorcNjGobZtg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EAE8DF566403FC0C243D83E8B485ABBF32B26B0443B0A4574377B72DB5436F22)

The initial APIs of this module are supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### visualEffect

visualEffect(effect: VisualEffect): T

Sets a visual effect that is not a filter effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/dMsGNaZ_QZOL_lnzFX_DYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC0F45170DF47DA6D7CF82B518277EDC841CD3DB063B3285A04727FEDFF5FF54)

This API can be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| effect | [VisualEffect](#visualeffect-1) | Yes | Visual effect. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### backgroundFilter

backgroundFilter(filter: Filter): T

Sets the visual effect of the background filter.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/YCFIA0oUSse1UUbJdEkhig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6CC70F3BBDF8A8CF6474132906E68FE840C87A439485D31FBD5146B8A09936DE)

This API can be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filter | [Filter](#filter) | Yes | Visual effect of the background filter. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### foregroundFilter

foregroundFilter(filter: Filter): T

Sets the visual effect of the foreground (content) filter.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/WDtEOWeCSoqDitOdu9vd_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49A7D42222A269E4FE9942C7BC9A39E583E8CFCD7DA3F988C13EA95A16496F54)

This API can be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filter | [Filter](#filter) | Yes | Visual effect of the foreground (content) filter. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### compositingFilter

compositingFilter(filter: Filter): T

Sets the visual effect of the compositing filter.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/lAJkEw-mQhiXl3XPj4vDFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC71314D422311EAB977AE62D68478FDEBBD249BA64EBFAC12CF15B333F1CC07)

This API can be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filter | [Filter](#filter) | Yes | Visual effect of the compositing filter. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Filter

type Filter = Filter

Represents a filter object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Filter](../../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-uieffect-cascading-effect/document.md#filter) | Used to apply the specified visual effect to the target component. |

#### VisualEffect

type VisualEffect = VisualEffect

Represents a visual effect configuration object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [VisualEffect](../../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-uieffect-cascading-effect/document.md#visualeffect) | Used to apply the specified visual effect to the target component. |

#### Example

This example demonstrates how to apply blur effects using **foregroundFilter**, **backgroundFilter**, and **compositingFilter**.

// xxx.ets
import { uiEffect } from '@kit.ArkGraphics2D';

@Entry
@Component
struct FilterEffectExample {
  @State filterTest1: uiEffect.Filter = uiEffect.createFilter().blur(10);
  @State filterTest2: uiEffect.Filter = uiEffect.createFilter().blur(10);
  @State filterTest3: uiEffect.Filter = uiEffect.createFilter().blur(10);

  build() {
    Column({ space: 15 }) {

      Text('foregroundFilter').fontSize(20).width('75%').fontColor('#DCDCDC')
      Text('Foreground filter')
        .width(100)
        .height(100)
        .backgroundColor('#ADD8E6')
        // Replace $r("app.media.app\_icon") with the resource file you use.
        .backgroundImage($r("app.media.app\_icon"))
        .backgroundImageSize({ width: 80, height: 80 })
        .foregroundFilter(this.filterTest1) // Set the blur effect using foregroundFilter.

      Text('backgroundFilter').fontSize(20).width('75%').fontColor('#DCDCDC')
      Text('Background filter')
        .width(100)
        .height(100)
        .backgroundColor('#ADD8E6')
        // Replace $r("app.media.app\_icon") with the resource file you use.
        .backgroundImage($r("app.media.app\_icon"))
        .backgroundImageSize({ width: 80, height: 80 })
        .backgroundFilter(this.filterTest2) // Set the blur effect using backgroundFilter.

      Text('compositingFilter').fontSize(20).width('75%').fontColor('#DCDCDC')
      Text('Compositing filter')
        .width(100)
        .height(100)
        .backgroundColor('#ADD8E6')
        // Replace $r("app.media.app\_icon") with the resource file you use.
        .backgroundImage($r("app.media.app\_icon"))
        .backgroundImageSize({ width: 80, height: 80 })
        .compositingFilter(this.filterTest3) // Set the blur effect using compositingFilter.
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/SKAuwuWJRvmsWq2QkUPnTA/en-us_image_0000002568685151.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83E3253678E5D1D6BDD77194F7F112CEB75CF55751FFDC6B060D7690C5CF5FCD)
