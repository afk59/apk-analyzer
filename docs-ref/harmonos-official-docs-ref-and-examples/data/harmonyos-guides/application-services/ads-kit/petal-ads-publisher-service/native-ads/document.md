# Native Ads

#### Use Cases

Native ads can be images or videos, which are less disruptive and fit seamlessly into the surrounding content to match your custom app design.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/gSJrfm68Q7C70QtpTRVN1w/en-us_image_0000002305180804.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA2AEBC47FE80AF2377C27F6718E68669A0F4C3461A62D63FE9AEA28B24E0FFB)

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
| 

[AdComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-adcomponent)({ads: advertising.Advertisement\[\], displayOptions: advertising.AdDisplayOptions, interactionListener: advertising.AdInteractionListener, @BuilderParam adRenderer?: () => void, @Prop rollPlayState?: number})

 | 

Displays ads. It uses **AdDisplayOptions** for setting ad display parameters and **AdInteractionListener** for tracking the ad interaction status.

**Note**: To ensure that ads can be correctly displayed, this API must be used together with the ad request API.

 |

#### Recommended AdComponent Width and Height

| 
Style

 | 

Recommended Width and Height

 |
| :-- | :-- |
| 

In-feed native ad/Native masonry layout

 | 

**width**: The width should match that of the news feed content.

**height**: You do not need to set this parameter.

 |
| 

Native card ad

 | 

**width**: 312 vp

**height**: 284 vp

 |

#### Development Procedure

## Requesting an Ad

1.  Import required modules.
    
    import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';
    import { advertising, identifier } from '@kit.AdsKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Obtain the OAID.
    
    To push ads to users more precisely, add the **oaid** attribute to [AdRequestParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#adrequestparams).
    
    Follow the [description](../../oaid-service/document.md) to obtain the OAID.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/llA0P-wcSiaS73j5MULwdw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75D46A0CF76CD8E9E60A900D4B9E85489658DCE73F3644F5A53529C9FB677872)
    
    When using the test ad unit provided in the following example, you must obtain the OAID.
    
3.  Request an ad.
    
    To request an ad, you must create an **AdLoader** object.
    
    -   To request an ad from one ad unit, use the [loadAd](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#loadad) method of **AdLoader** to request the ad, and use [AdLoadListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#adloadlistener) to track the ad loading status.
    -   To request ads from multiple ad units, use the [loadAdWithMultiSlots](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#loadadwithmultislots) method of **AdLoader** to request the ads, and use [MultiSlotsAdLoadListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#multislotsadloadlistener) to track the ad loading status.
    
    The following table describes the key parameters for requesting an ad.
    
    | 
    Parameter
    
     | 
    
    Type
    
     | 
    
    Mandatory
    
     | 
    
    Description
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    adType
    
     | 
    
    number
    
     | 
    
    Yes
    
     | 
    
    Type of the requested ad. The value is **3** for native ads.
    
     |
    | 
    
    adId
    
     | 
    
    string
    
     | 
    
    Yes
    
     | 
    
    Ad unit ID.
    
    -   For ad debugging purposes, use the following test ad unit IDs: **testy63txaom86** (native video ads), **testu7m3hc4gvm** (native large image ads), **testb65czjivt9** (native small image ads), and **testr6w14o0hqz** (native three-image ads).
    -   For official ad delivery, you need to apply for a formal ad unit ID. Before app release, go to [Petal Ads Publisher Service](https://developer.huawei.com/consumer/en/monetize), click **Start now**, and sign in to [Petal Publisher Center](https://developer.huawei.com/consumer/en/service/ads/publisher/html/index.html?lang=en) to apply for an ad unit. For details, please click [here](https://developer.huawei.com/consumer/en/doc/monetize/addunit-0000001051321846).
    
     |
    | 
    
    oaid
    
     | 
    
    string
    
     | 
    
    No
    
     | 
    
    OAID, which is used to precisely push ads. If this parameter is left empty, personalized ads cannot be obtained.
    
     |
    
    The following sample code shows how to request ads from multiple ad units:
    
    @Entry
    @Component
    struct Index {
      @State ads: advertising.Advertisement\[\] = \[\];
      // ...
      private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    
      aboutToAppear(): void {
        // Call **loadAd** to load an ad.
        // ...
      }
    
      private async loadAd(...adIds: string\[\]): Promise<void> {
        // Ad request parameters.
        const adRequestParamsArray: advertising.AdRequestParams\[\] = \[\];
        const oaid: string | undefined = await requestOAID(this.context);
        for (const adId of adIds) {
          adRequestParamsArray.push({
            // Ad unit ID.
            adId: adId,
            // Native ad.
            adType: 3,
            // This is an extended parameter for native ads, specifying whether to directly return the ad without waiting for the download of all ad assets.
            enableDirectReturnVideoAd: true,
            // OAID.
            oaid: oaid
          });
        }
        // Ad configuration parameters, which can be set based on the project requirements.
        const adOptions: advertising.AdOptions = {};
        // Ad request callback listener.
        const multiSlotsAdLoaderListener: advertising.MultiSlotsAdLoadListener = {
          onAdLoadFailure: (errorCode: number, errorMsg: string) => {
            hilog.error(0x0000, 'testTag', \`Failed to load multiSlots ad. Code is ${errorCode}, message is ${errorMsg}\`);
          },
          onAdLoadSuccess: (ads: Map<string, Array<advertising.Advertisement>>) => {
            hilog.info(0x0000, 'testTag', 'Succeeded in loading multiSlots ad');
            const returnAds: advertising.Advertisement\[\] = \[\];
            ads.forEach((adsArray) => returnAds.push(...adsArray));
            this.ads = returnAds;
          }
        };
        // Create an **AdLoader** ad object.
        const adLoader: advertising.AdLoader = new advertising.AdLoader(this.context);
        try {
          // Call the API for requesting ads.
          adLoader.loadAdWithMultiSlots(adRequestParamsArray, adOptions, multiSlotsAdLoaderListener);
        } catch (e) {
          hilog.error(0x0000, 'testTag', \`Failed to load multiSlots ad. Code is ${e.code}, message is ${e.message}\`);
        }
      }
    
      build() {
        // ...
      }
    
      // ...
    }
    
    async function requestOAID(context: Context): Promise<string | undefined> {
      // Request **Activity tracking for this app** from users.
      let isPermissionGranted: boolean = false;
      try {
        const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
        const result: PermissionRequestResult =
          await atManager.requestPermissionsFromUser(context, \['ohos.permission.APP\_TRACKING\_CONSENT'\]);
        isPermissionGranted = result.authResults\[0\] === abilityAccessCtrl.GrantStatus.PERMISSION\_GRANTED;
      } catch (err) {
        hilog.error(0x0000, 'testTag', \`Failed to request permission. Code is ${err.code}, message is ${err.message}\`);
      }
      if (isPermissionGranted) {
        hilog.info(0x0000, 'testTag', 'Succeeded in requesting permission');
        try {
          const oaid = await identifier.getOAID();
          hilog.info(0x0000, 'testTag', 'Succeeded in getting OAID');
          return oaid;
        } catch (err) {
          hilog.error(0x0000, 'testTag', \`Failed to get OAID. Code is ${err.code}, message is ${err.message}\`);
        }
      } else {
        hilog.error(0x0000, 'testTag', 'Failed to request permission. User rejected');
      }
      return undefined;
    }
    

## Displaying an Ad

1.  Import required modules.
    
    import { AdComponent, advertising } from '@kit.AdsKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Display the ad.
    
    When an ad is displayed, use [AdInteractionListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#adinteractionlistener) to listen for ad status callbacks. The following table describes the details.
    
    | 
    Callback Status
    
     | 
    
    Description
    
     | 
    
    Suggestion
    
     |
    | :-- | :-- | :-- |
    | 
    
    onAdOpen
    
     | 
    
    An ad is opened.
    
     | 
    
    \-
    
     |
    | 
    
    onAdClick
    
     | 
    
    An ad is clicked.
    
     | 
    
    \-
    
     |
    | 
    
    onAdClose
    
     | 
    
    An ad is closed.
    
     | 
    
    This callback is triggered when a user provides negative feedback or closes an ad. Hide the ad component in this case.
    
    The callback status contains the specific reason for closing the ads. For details, please refer to the [data description](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#onstatuschanged).
    
     |
    | 
    
    onAdFail
    
     | 
    
    An ad fails to be loaded.
    
     | 
    
    This callback is triggered when an ad fails to be displayed. Hide the ad component in this case.
    
     |
    
    In the in-feed native ad scenario, the height of the [AdComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-adcomponent) component does not need to be explicitly set. [AdComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-adcomponent) will automatically adjust the height to adapt to the content to be displayed.
    
    The sample code is as follows:
    
    @Entry
    @Component
    struct Index {
      @State ads: advertising.Advertisement\[\] = \[\];
      @State visibilityState: Visibility = Visibility.Visible;
      // ...
    
      build() {
        Column() {
          if (this.ads.length > 0) {
            this.inFeedNativeAd(this.ads\[0\])
            // ...
          }
        }
        .width('100%')
        .height('100%')
      }
    
      @Builder
      inFeedNativeAd(ad: advertising.Advertisement): void {
        Row() {
          AdComponent({
            ads: \[ad\],
            // Ad display parameters, which can be set based on the project requirements.
            displayOptions: {
              // Whether to mute the ad.
              mute: true
            },
            interactionListener: {
              onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
                switch (status) {
                  case 'onAdOpen':
                    hilog.info(0x0000, 'testTag', 'Status is onAdOpen');
                    break;
                  case 'onAdClick':
                    hilog.info(0x0000, 'testTag', 'Status is onAdClick');
                    break;
                  case 'onAdClose':
                    hilog.info(0x0000, 'testTag', 'Status is onAdClose');
                    this.visibilityState = Visibility.None;
                    break;
                  case 'onAdFail':
                    hilog.error(0x0000, 'testTag', 'Status is onAdFail');
                    this.visibilityState = Visibility.None;
                    break;
                }
              }
            }
          })
          // For in-feed native ads, you are not advised to set the height. It is recommended that you set the width to 100% to fill the parent container.
            .width('100%')
        }
        .width('100%')
        .padding({ left: 16, right: 16 })
        .visibility(this.visibilityState)
      }
    
      // ...
    }
    
    The native card ad has fixed dimensions of 312 vp x 284 vp, and [AdComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-adcomponent) can be centered within the display.
    
    The sample code is as follows:
    
    @Entry
    @Component
    struct Index {
      @State ads: advertising.Advertisement\[\] = \[\];
      @State visibilityState: Visibility = Visibility.Visible;
      // ...
    
      build() {
        Column() {
          if (this.ads.length > 0) {
            // ...
            this.nativeCardAd(this.ads\[0\])
          }
        }
        .width('100%')
        .height('100%')
      }
    
      // ...
    
      @Builder
      nativeCardAd(ad: advertising.Advertisement): void {
        Row() {
          AdComponent({
            ads: \[ad\],
            // Ad display parameters, which can be set based on the project requirements.
            displayOptions: {
              // Whether to mute the ad.
              mute: true
            },
            interactionListener: {
              onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
                switch (status) {
                  case 'onAdOpen':
                    hilog.info(0x0000, 'testTag', 'Status is onAdOpen');
                    break;
                  case 'onAdClick':
                    hilog.info(0x0000, 'testTag', 'Status is onAdClick');
                    break;
                  case 'onAdClose':
                    hilog.info(0x0000, 'testTag', 'Status is onAdClose');
                    this.visibilityState = Visibility.None;
                    break;
                  case 'onAdFail':
                    hilog.info(0x0000, 'testTag', 'Status is onAdFail');
                    this.visibilityState = Visibility.None;
                    break;
                }
              }
            }
          })
          // For native card ads, the width and height are fixed (312 vp x 284 vp).
            .width(312)
            .height(284)
        }
        .width('100%')
        // The ad cannot fill the parent container due to the fixed dimensions, so it is centered within the layout.
        .justifyContent(FlexAlign.Center)
        .visibility(this.visibilityState)
      }
    }
