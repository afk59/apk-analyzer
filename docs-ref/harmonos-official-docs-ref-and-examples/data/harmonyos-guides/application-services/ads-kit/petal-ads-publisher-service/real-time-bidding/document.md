# Real-Time Bidding

#### Use Cases

Real-time bidding is a process where, when a user accesses an app, creating an impression opportunity, multiple demand-side platforms (DSPs) assess the value of the impression in real time based on its context and user attributes. Each DSP then submits a bid, with the highest bidder winning the impression opportunity.

#### Supported Ads

-   Native ads
-   Rewarded ads
-   Interstitial ads
-   Splash ads
-   Roll ads

#### API Description

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[loadAd](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#loadad)(adParam: AdRequestParams, adOptions: AdOptions, listener: AdLoadListener): void

 | 

Requests an ad from one ad unit. It uses **AdRequestParams** and **AdOptions** for setting ad request parameters and **AdLoadListener** for tracking the ad loading status.

 |
| 

[loadAdWithMultiSlots](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#loadadwithmultislots)(adParams: AdRequestParams\[\], adOptions: AdOptions, listener: MultiSlotsAdLoadListener): void

 | 

Requests ads from multiple ad units. It uses **AdRequestParams\[\]** and **AdOptions** for setting ad request parameters and **MultiSlotsAdLoadListener** for tracking the ad loading status.

 |

#### Development Procedure

## Adding Bidding Parameters

Add real-time bidding parameters to [AdRequestParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#adrequestparams).

The following table lists the key parameters for real-time bidding.

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

tMax

 | 

number

 | 

No

 | 

Maximum transaction timeout interval (including the network delay), in milliseconds.

 |
| 

cur

 | 

string

 | 

No

 | 

Currency supported by the bidding request. If there are multiple currencies, separate them with a comma (,). Currently, the following currencies are supported:

1.  CNY
2.  USD
3.  EUR
4.  GBP
5.  JPY

If this parameter is left empty, CNY is used by default.

 |
| 

bidFloor

 | 

number

 | 

No

 | 

Minimum bid price of the ad unit.

 |
| 

bidFloorCur

 | 

string

 | 

No

 | 

Currency used for the minimum bid price of the ad unit. If **bidFloor** is not empty, **bidFloorCur** cannot be empty, either. Currently, only one of the following five currencies is supported:

1.  CNY
2.  USD
3.  EUR
4.  GBP
5.  JPY

If this parameter is left empty, CNY is used by default.

 |
| 

bpkgName

 | 

string

 | 

No

 | 

App package names for bidding. If there are multiple package names, separate them with a comma (,).

 |

The sample code is as follows:

import { advertising } from '@kit.AdsKit';

const adRequestParams: advertising.AdRequestParams = {
  // **'testu7m3hc4gvm'** is a dedicated test ad unit ID with no bidding information. Before releasing your app, replace the test ad unit ID with the formal one.
  adId: 'testu7m3hc4gvm',
  // Ad type.
  adType: 3,
  // Maximum transaction timeout interval.
  tMax: 100,
  // Currency supported by the bidding request. If there are multiple currencies, separate them with a comma (,).
  cur: 'CNY',
  // Minimum bid price of the ad unit.
  bidFloor: 6.66,
  // Currency used for the minimum bid price of the ad unit.
  bidFloorCur: 'CNY',
  // App package names for bidding. If there are multiple package names, separate them with a comma (,).
  bpkgName: 'com.huawei.baidu,com.huawei.music'
};

## Processing the Bidding Result

After a successful ad request, process the returned real-time bidding result [Advertisement](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#advertisement).biddingInfo within the callback AdLoadListener.[onAdLoadSuccess](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#onadloadsuccess) or MultiSlotsAdLoadListener.[onAdLoadSuccess](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#onadloadsuccess).

The following table describes the real-time bidding result information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/4fW5cFjnRi-SSu1-b3zURg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8336478886C2BF479B3711823C35A9708179C23D5B25A831CD6F3C5C4FB14637)

To post back the bidding result, you need to request the Internet permission [ohos.permission.INTERNET](../../../../system/security/application-access-control/application-permission-management/application-permissions/open-system-grant-permissions/document.md#ohospermissioninternet). For details about how to request the permission, please refer to [Preparations](../../preparations/document.md).

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

price

 | 

number

 | 

Yes

 | 

Effective cost per mille (eCPM) for this ad, which represents the revenue generated for every 1000 impressions.

 |
| 

cur

 | 

string

 | 

Yes

 | 

Currency of the ad price. Supported currencies: **CNY**, **USD**, **EUR**, **GBP**, and **JPY**.

 |
| 

nurl

 | 

string

 | 

Yes

 | 

URL used by the app to post back the bidding success result.

 |
| 

lurl

 | 

string

 | 

Yes

 | 

URL used by the app to post back the bidding failure result.

 |

-   If Petal Ads wins, replace the macro in **nurl** and post back the bidding success result.
    
    The following table describes the macros.
    
    | 
    Macro
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    SECOND\_PRICE
    
     | 
    
    Highest bid price of other DSPs when Petal Ads wins. Example: **3.6**
    
     |
    | 
    
    AUCTION\_CURRENCY
    
     | 
    
    Price currency. Supported currencies: **CNY**, **USD**, **EUR**, **GBP**, and **JPY**.
    
     |
    

-   If Petal Ads loses, replace the macro in **lurl** and post back the bidding failure result.
    
    The following table describes the macros.
    
    | 
    Macro
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    AUCTION\_PRICE
    
     | 
    
    Highest bid price of other DSPs when Petal Ads loses. Example: **3.6**
    
     |
    | 
    
    AUCTION\_LOSS
    
     | 
    
    Bidding result. If the process does not reach the bidding stage, a callback is still necessary. Replace **AUCTION\_LOSS** with the specific result code.
    
    Enumeration:
    
    **102**: Bidding failed.
    
    **103**: The advertiser is filtered out because the eCPM offered is lower than the minimum.
    
    **104**: The advertiser is filtered out because the package name is forbidden.
    
    **105**: The advertiser is filtered out due to other reasons.
    
    **4005**: No response is returned due to timeout.
    
     |
    | 
    
    AUCTION\_CURRENCY
    
     | 
    
    Price currency. Supported currencies: **CNY**, **USD**, **EUR**, **GBP**, and **JPY**.
    
     |
    | 
    
    AUCTION\_APP\_PKG
    
     | 
    
    Package name of the app promoted by the winning DSP when Petal Ads loses.
    
     |
    | 
    
    AUCTION\_APP\_NAME
    
     | 
    
    Name of the app promoted by the winning DSP when Petal Ads loses.
    
     |
    | 
    
    AUCTION\_CP\_ID
    
     | 
    
    ID of the winning DSP when Petal Ads loses.
    
    **1**: Tencent Ads
    
    **2**: Pangle
    
    **3**: Baiqingteng (Baidu's ad platform)
    
    **4**: Kuaishoulianmeng (Kuaishou alliance)
    
    **5**: iQIYI
    
    **6**: Alibaba
    
    **7**: vivo
    
    **8**: OPPO
    
    **9**: Xiaomi
    
    **10**: JD
    
    **11**: Pinduoduo
    
    **100**: others
    
     |
    

The sample code is as follows:

import { advertising } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { rcp } from '@kit.RemoteCommunicationKit';

interface BiddingInfo {
  // eCPM for this ad, which represents the revenue generated for every 1000 impressions.
  price: number;

  // Currency of the ad price.
  cur: string;

  // URL used by the app to post back the bidding success result.
  nurl: string;

  // URL used by the app to post back the bidding failure result.
  lurl: string;
}

const adLoaderListener: advertising.AdLoadListener = {
  // Called when an ad request fails.
  onAdLoadFailure: (errorCode: number, errorMsg: string) => {
    hilog.error(0x0000, 'testTag', \`Failed to load ad. Code is ${errorCode}, message is ${errorMsg}\`);
  },
  // Called upon ad request success.
  onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
    // Expected minimum bid price.
    const bidFloor: number = 6;
    const biddingSuccessAds: Array<advertising.Advertisement> = \[\];
    for (const ad of ads) {
      const biddingInfo: BiddingInfo = ad.biddingInfo as BiddingInfo;
      if (!biddingInfo) {
        continue;
      }
      if (biddingInfo.cur === 'CNY' && biddingInfo.price >= bidFloor) {
        hilog.info(0x0000, 'testTag', 'Petal Ads wins.');
        if (biddingInfo.nurl) {
          const url: string = biddingInfo.nurl
            // Highest bid price of other DSPs when Petal Ads wins.
            .replace('SECOND\_PRICE', '3.6')
            // Price currency.
            .replace('AUCTION\_CURRENCY', 'CNY');
          sendBiddingResult(url);
        }
        biddingSuccessAds.push(ad);
      } else {
        hilog.info(0x0000, 'testTag', 'Petal Ads loses.');
        if (biddingInfo.lurl) {
          const url: string = biddingInfo.lurl
            // Highest bid price of other DSPs when Petal Ads loses.
            .replace('AUCTION\_PRICE', '3.6')
            // Bidding result.
            .replace('AUCTION\_LOSS', '102')
            // Price currency.
            .replace('AUCTION\_CURRENCY', 'CNY')
            // Package name of the app promoted by the winning DSP when Petal Ads loses.
            .replace('AUCTION\_APP\_PKG', 'com.huawei.music')
            // Name of the app promoted by the winning DSP when Petal Ads loses.
            .replace('AUCTION\_APP\_NAME', 'music')
            // ID of the winning DSP when Petal Ads loses.
            .replace('AUCTION\_CP\_ID', '100')
          sendBiddingResult(url);
        }
      }
    }
    // ... The logic of displaying ads is omitted.
  }
};

async function sendBiddingResult(url: string): Promise<void> {
  let session: rcp.Session | undefined = undefined;
  try {
    session = rcp.createSession();
    await session.get(url);
  } catch (e) {
    hilog.error(0x0000, 'testTag', \`Failed to send bidding result. Code is ${e.code}, message is ${e.message}\`);
  } finally {
    session?.close();
  }
}
