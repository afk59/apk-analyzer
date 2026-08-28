# Interstitial Ads

#### Use Cases

Interstitial ads appear in either full or half screen when an app is launched, paused, or closed. They are cleverly timed to not disrupt the user's regular interaction with the app. Due to their large size, they offer excellent visibility and exposure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/mxkyXXFkTSmJqnHOb2038g/en-us_image_0000002530433001.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE9A3914FA081E88F29712F11B6B3814BA8C04A8FDA945ED12CA73CC08042E9B)

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

[showAd](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#showad)(ad: Advertisement, options: AdDisplayOptions, context?: common.UIAbilityContext): void

 | 

Displays ads. It uses **AdDisplayOptions** to set ad display parameters.

**Note**: To ensure that ads can be correctly displayed, this API must be used together with the ad request API.

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
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/X_0IHAV3TD6-FmaD0l1sQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADB1CC81885C4B4283D045183C8AB8AC1B981ED4B109D127E320232CC5ABCB5A)
    
    When using the test ad unit provided in the following example, you must obtain the OAID.
    
3.  Request an ad from one ad unit.
    
    Create an **AdLoader** object, use the [loadAd](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#loadad) method of **AdLoader** to request the ad, and use [AdLoadListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#adloadlistener) to track the ad loading status.
    
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
    
    Type of the requested ad. The value is **12** for interstitial ads.
    
     |
    | 
    
    adId
    
     | 
    
    string
    
     | 
    
    Yes
    
     | 
    
    Ad unit ID.
    
    -   For ad debugging purposes, you can use the test ad unit ID **testb4znbuh3n2**.
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
    
    The sample code is as follows:
    
    @Entry
    @Component
    struct Index {
      private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    
      build() {
        Column() {
          Button('LoadAd')
            .onClick(() => {
              this.loadAd();
            })
        }
        .width('100%')
        .height('100%')
        .justifyContent(FlexAlign.Center)
      }
    
      private async loadAd(): Promise<void> {
        // Ad request callback listener.
        const adLoadListener: advertising.AdLoadListener = {
          onAdLoadFailure: (errorCode: number, errorMsg: string) => {
            hilog.error(0x0000, 'testTag', \`Failed to load ad. Code is ${errorCode}, message is ${errorMsg}\`);
          },
          onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
            hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
            // ...
          }
        };
        // Ad request parameters.
        const adRequestParams: advertising.AdRequestParams = {
          // **'testb4znbuh3n2'** is a dedicated test ad unit ID. Before releasing your app, replace the test ad unit ID with the formal one.
          adId: 'testb4znbuh3n2',
          // Interstitial ad.
          adType: 12,
          // OAID.
          oaid: await requestOAID(this.context)
        };
        // Ad configuration parameters, which can be set based on the project requirements.
        const adOptions: advertising.AdOptions = {};
        // Create an **AdLoader** ad object.
        const adLoader: advertising.AdLoader = new advertising.AdLoader(this.context);
        try {
          // Call the API for requesting ads.
          adLoader.loadAd(adRequestParams, adOptions, adLoadListener);
        } catch (e) {
          hilog.error(0x0000, 'testTag', \`Failed to load ad. Code is ${e.code}, message is ${e.message}\`);
        }
      }
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
    

## Subscribing to an Event

1.  Import required modules.
    
    import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Subscribe to an event.
    
    Subscribe to the **com.huawei.hms.pps.action.PPS\_INTERSTITIAL\_STATUS\_CHANGED** event to track changes on the interstitial ad page.
    
    After subscribing to the common event, you can obtain the status changes of the interstitial ad page from **parameters** of [CommonEventData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-commonevent-commoneventdata) using **interstitial\_ad\_status** as the key.
    
    The following table describes the involved page status changes.
    
    | 
    Page Change Status
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    onAdOpen
    
     | 
    
    An ad is opened.
    
     |
    | 
    
    onAdClick
    
     | 
    
    An ad is clicked.
    
     |
    | 
    
    onAdClose
    
     | 
    
    An ad is closed.
    
     |
    | 
    
    onVideoPlayBegin
    
     | 
    
    The ad video playback starts.
    
     |
    | 
    
    onVideoPlayEnd
    
     | 
    
    The ad video playback ends.
    
     |
    
    The sample code is as follows:
    
    const KEY\_INTERSTITIAL\_STATUS = 'interstitial\_ad\_status';
    
    export class InterstitialAdStatusHandler {
      // Used to save the created subscriber object for subsequent subscription and unsubscription.
      private subscriber: commonEventManager.CommonEventSubscriber | null = null;
    
      // Subscription method, which must be called each time before an ad is displayed.
      public registerPPSReceiver(): void {
        if (this.subscriber) {
          this.unRegisterPPSReceiver();
        }
        // Subscriber information.
        const subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
          events: \['com.huawei.hms.pps.action.PPS\_INTERSTITIAL\_STATUS\_CHANGED'\],
          // Setting **publisherBundleName** to **com.huawei.hms.adsservice** indicates that the subscriber only accepts and processes events from this specific package.
          // If **publisherBundleName** is not explicitly declared, the subscriber may receive forged events from other package names, resulting in security issues or misleading.
          publisherBundleName: 'com.huawei.hms.adsservice'
        };
        // Callback for subscriber creation.
        commonEventManager.createSubscriber(subscribeInfo,
          (err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
            if (err) {
              hilog.error(0x0000, 'testTag', \`Failed to create subscriber. Code is ${err.code}, message is ${err.message}\`);
              return;
            }
            hilog.info(0x0000, 'testTag', 'Succeeded in creating subscriber');
            this.subscriber = commonEventSubscriber;
            // Callback for common event subscription.
            commonEventManager.subscribe(this.subscriber,
              (err: BusinessError, commonEventData: commonEventManager.CommonEventData) => {
                if (err) {
                  hilog.error(0x0000, 'testTag', \`Failed to subscribe. Code is ${err.code}, message is ${err.message}\`);
                } else {
                  // The subscriber receives the common event.
                  hilog.info(0x0000, 'testTag', 'Succeeded in subscribing data');
                  // Obtain the status change of the interstitial ad page.
                  const status: string = commonEventData?.parameters?.\[KEY\_INTERSTITIAL\_STATUS\];
                  switch (status) {
                    case 'onAdOpen':
                      hilog.info(0x0000, 'testTag', 'Status is onAdOpen');
                      break;
                    case 'onAdClick':
                      hilog.info(0x0000, 'testTag', 'Status is onAdClick');
                      break;
                    case 'onAdClose':
                      hilog.info(0x0000, 'testTag', 'Status is onAdClose');
                      this.unRegisterPPSReceiver();
                      break;
                    case 'onVideoPlayBegin':
                      hilog.info(0x0000, 'testTag', 'Status is onVideoPlayBegin');
                      break;
                    case 'onVideoPlayEnd':
                      hilog.info(0x0000, 'testTag', 'Status is onVideoPlayEnd');
                      break;
                    default:
                      break;
                  }
                }
              });
          });
      }
    
      // Cancel the subscription.
      public unRegisterPPSReceiver(): void {
        commonEventManager.unsubscribe(this.subscriber, (err: BusinessError) => {
          if (err) {
            hilog.error(0x0000, 'testTag', \`Failed to unsubscribe. Code is ${err.code}, message is ${err.message}\`);
          } else {
            hilog.info(0x0000, 'testTag', 'Succeeded in unsubscribing');
            this.subscriber = null;
          }
        });
      }
    }
    

## Displaying an Ad

1.  Import required modules.
    
    import { common } from '@kit.AbilityKit';
    import { advertising } from '@kit.AdsKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    // File created during event subscription
    import { InterstitialAdStatusHandler } from './InterstitialAdStatusHandler';
    
2.  Display the ad.
    
    Call the [showAd](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#showad) method to display an ad. The **ads** parameter indicates the ad information returned from the [ad request](#section0237145185117). Before displaying an ad, register a listener defined in [event subscription](#section14755121210539).
    
    The sample code is as follows:
    
    @Entry
    @Component
    struct Index {
      private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    
      build() {
        // ...
      }
    
      private async loadAd(): Promise<void> {
        // Ad request callback listener.
        const adLoadListener: advertising.AdLoadListener = {
          onAdLoadFailure: (errorCode: number, errorMsg: string) => {
            hilog.error(0x0000, 'testTag', \`Failed to load ad. Code is ${errorCode}, message is ${errorMsg}\`);
          },
          onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
            hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
            try {
          // Register an interstitial ad status listener.
              new InterstitialAdStatusHandler().registerPPSReceiver();
          // Ad display parameters, which can be set based on the project requirements.
              const adDisplayOptions: advertising.AdDisplayOptions = {
          // Whether to mute the ad.
                mute: true
              };
          // Here, **ads\[0\]** refers to the first ad that has been obtained. You can choose the ad to display based on the project requirements.
              advertising.showAd(ads\[0\], adDisplayOptions, this.context);
            } catch (e) {
              hilog.error(0x0000, 'testTag', \`Failed to show ad. Code is ${e.code}, message is ${e.message}\`);
            }
          }
        };
        // ...
      }
    }
