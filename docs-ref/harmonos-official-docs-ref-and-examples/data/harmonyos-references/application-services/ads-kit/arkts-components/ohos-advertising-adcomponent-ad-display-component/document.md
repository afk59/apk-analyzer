# @ohos.advertising.AdComponent (Ad Display Component)

This module provides the capability of displaying ads, including native, roll, and splash ads.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/CvOGKATJT8-Cb26M1t8GFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CEDF86D01E73856F4613FA5B0FAE4A4D1081AC13AE2D8F4E32FA910FABE2102E)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { AdComponent } from '@kit.AdsKit';

#### AdComponent

AdComponent({
  ads: advertising.Advertisement\[\], 
  displayOptions: advertising.AdDisplayOptions,
  interactionListener: advertising.AdInteractionListener,
  @BuilderParam adRenderer?: () => void,   
  @Prop rollPlayState?: number
})

**Decorator type**: @Component

**System capability**: SystemCapability.Advertising.Ads

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Decorator Type**

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

ads

 | 

advertising.[Advertisement](../../arkts-apis/ohos-advertising-ads-kit-framework/document.md#advertisement)\[\]

 | 

Yes

 | 

\-

 | 

Array of ad objects.

**Note**: For ads other than roll ads, only the first data record in the array will be displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| 

displayOptions

 | 

advertising.[AdDisplayOptions](../../arkts-apis/ohos-advertising-ads-kit-framework/document.md#addisplayoptions)

 | 

Yes

 | 

\-

 | 

Ad display parameters.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| 

interactionListener

 | 

advertising.[AdInteractionListener](../../arkts-apis/ohos-advertising-ads-kit-framework/document.md#adinteractionlistener)

 | 

Yes

 | 

\-

 | 

Ad status change callback.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| 

adRenderer12+

 | 

() => void

 | 

No

 | 

@BuilderParam

 | 

Self-rendered ad format. The use of self-rendered ad formats in your app is restricted. For details, please [consult customer service](https://developer.huawei.com/consumer/en/doc/monetize/support-0000001061434261).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| 

rollPlayState15+

 | 

number

 | 

No

 | 

@Prop

 | 

Roll ad playback status provided for your app. Value **1** indicates playing and value **2** (default value) indicates paused. Other values are invalid and cannot change the original playback status. For the roll ad display page, this parameter must be associated with an attribute decorated with **@State** in the parent ArkTS struct that contains **AdComponent**. For details, please refer to the [sample code](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ads-publisher-service-roll#section4281165885118).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/FKKSUxXFT6K9cCq334M0PQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F112AE702BFC101B8871F33C5CB6001D7B3880D8FBDE68E429CFE6929981D9E3)

To ensure that ads can be correctly displayed, this API must be used together with the ad request API.

**Example**:

import { AdComponent, advertising } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  // Ad content obtained.
  private ads: advertising.Advertisement\[\] = \[\];
  // Ad display parameters.
  private adDisplayOptions: advertising.AdDisplayOptions = {};

  build() {
    Column() {
      AdComponent({
        ads: this.ads,
        displayOptions: this.adDisplayOptions,
        interactionListener: {
          onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
            switch (status) {
              case 'onAdOpen':
                hilog.info(0x0000, 'testTag', 'onAdOpen');
                break;
              case 'onAdClick':
                hilog.info(0x0000, 'testTag', 'onAdClick');
                break;
              case 'onAdClose':
                hilog.info(0x0000, 'testTag', 'onAdClose');
                break;
            }
          }
        }
      })
        .width('100%')
        .height('100%')
    }
    .width('100%')
    .height('100%')
  }
}

#### \[h2\]build

build(): void

Constructor used to create an **AdComponent** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads
