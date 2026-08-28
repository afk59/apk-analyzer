# SplitLayout

**SplitLayout** is a component that enables you to divide the available space vertically into separate sections, each of which can contain solely text or a combination of text and images.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/wM90rsL9S0G5N0rcO3o7Mg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F661795CD889E840C1498EEF93CB71C1DE46DEA8CA7EB4A8A37BC3D8F0B464F)

This component is supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { SplitLayout } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### SplitLayout

SplitLayout({mainImage: Resource, primaryText: string, secondaryText?: string, tertiaryText?: string, container: () => void })

**Decorator**: @Component

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| mainImage | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | @State | Image. |
| primaryText | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | @Prop | Title. |
| secondaryText | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Prop | Subtitle. |
| tertiaryText | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | @Prop | Auxiliary text. |
| container | () => void | Yes | @BuilderParam | Container in the component. |

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

This example demonstrates how to use **SplitLayout** to achieve a page layout that is both adaptable and responsive.

import { SplitLayout } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State demoImage: Resource = $r("app.media.background");

  build() {
    Column() {
      SplitLayout({
        mainImage: this.demoImage,
        primaryText:'New music recommendation',
        secondaryText: 'Get a playlist tailored to your taste;',
        tertiaryText: 'Updated every day',
      }) {
        Text('Example: Components can be added to a blank area container.')
          .margin({ top: 36 })
      }
    }
    .justifyContent(FlexAlign.SpaceBetween)
    .height('100%')
    .width('100%')
  }
}

Layout less than or equal to 600 vp

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/mA__10hYQ2e8pWPnvYQJpg/en-us_image_0000002537765992.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7EA519D06262E412A8EEB8BDE0BFE6D96544CE3F3559EEFA49D69501E4D71F0)

Layout greater than 600 vp and less than or equal to 840 vp

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/wAJoEvXJT4eOg3zOHO5pYQ/en-us_image_0000002537925932.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B55BA088C9CAF2A906EBA1431A5EEE2AD3C241214ED116F4228FC16C8930E1BE)

Layout greater than 840 vp

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/J8wTMNZvS9qJXv_UIRkRmg/en-us_image_0000002568685709.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CE94F1D2CC131DA17D76BB2B4911219459FADA16B315F240052B8DCEE83F5A8)
