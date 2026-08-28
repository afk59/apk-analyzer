# @ohos.advertising.AutoAdComponent (Carousel Ad Component)

This module provides the capability of displaying carousel ads.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/It1wO3WYRbunzKfGneqsrg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A712EB233DE3199FC6C9E411FF9D885D00D3FE6099AA44D59778B8E4BE32E221)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { AutoAdComponent } from '@kit.AdsKit';

#### AutoAdComponent

AutoAdComponent({
  adParam: advertising.AdRequestParams,
  adOptions: advertising.AdOptions,
  displayOptions: advertising.AdDisplayOptions,  
  interactionListener: advertising.AdInteractionListener  
})  

**Decorator type**: @Component

**Atomic service API**: This API can be used in atomic services since API version 12.

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

adParam

 | 

advertising.[AdRequestParams](../../arkts-apis/ohos-advertising-ads-kit-framework/document.md#adrequestparams)

 | 

Yes

 | 

\-

 | 

Ad request parameters.

 |
| 

adOptions

 | 

advertising.[AdOptions](../../arkts-apis/ohos-advertising-ads-kit-framework/document.md#adoptions)

 | 

Yes

 | 

\-

 | 

Ad configuration parameters.

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

 |

**Example**:

import { advertising, AutoAdComponent } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  // Ad request parameters.
  private adRequestParams: advertising.AdRequestParams = {
    // Ad unit ID.
    adId: 'testw6vs28auh3',
    // Ad type.
    adType: 8
  };
  // Ad configuration parameters.
  private adOptions: advertising.AdOptions = {};
  // Ad display parameters.
  private adDisplayOptions: advertising.AdDisplayOptions = {
    // Interval for ad rotation, in ms. The value ranges from 30000 to 120000.
    refreshTime: 30000
  };

  build() {
    Column() {
      AutoAdComponent({
        adParam: this.adRequestParams,
        adOptions: this.adOptions,
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

Constructor used to create an **AutoAdComponent** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Advertising.Ads
