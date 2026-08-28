# Banner Ads

#### Use Cases

A banner ad is a rectangular image displayed at the top, middle, or bottom of an in-app page. It automatically refreshes at an interval.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/A9uYSKHuRcCqPD6R2tKIVw/en-us_image_0000002305340512.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE0B3317EE7D29F1A8D3825D431CB26E666891267E02B1D71B269791B9C6EE05)

#### API Description

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[AutoAdComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-autoadcomponent)({adParam: advertising.AdRequestParams, adOptions: advertising.AdOptions, displayOptions: advertising.AdDisplayOptions, interactionListener: advertising.AdInteractionListener})

 | 

Displays ads. It uses **AdRequestParams** and **AdOptions** for setting ad request parameters, **AdDisplayOptions** for configuring ad display parameters, and **AdInteractionListener** for tracking the ad interaction status.

 |

#### Development Procedure

1.  Import required modules.
    
    import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';
    import { advertising, AutoAdComponent, identifier } from '@kit.AdsKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Obtain the OAID.
    
    To push ads to users more precisely, add the **oaid** attribute to [AdRequestParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#adrequestparams) to improve the ad push precision and fill rate.
    
    Follow the [description](../../oaid-service/document.md) to obtain the OAID.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/GPTkkPM-RQKFRFb58M5zJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DABC5292FD68F66B12A6275E400880A57E3DA5B757CCE5FC8FB113091FE86B7)
    
    When using the test ad unit provided in the following example, you must obtain the OAID.
    
3.  Request and display an ad.
    
    Use **AutoAdComponent** to request and show a banner ad.
    
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
    
    Type of the requested ad. The value is **8** for banner ads.
    
     |
    | 
    
    adId
    
     | 
    
    string
    
     | 
    
    Yes
    
     | 
    
    Ad unit ID.
    
    -   For ad debugging purposes, you can use the test ad unit ID **testw6vs28auh3**.
    -   For official ad delivery, you need to apply for a formal ad unit ID. Before app release, go to [Petal Ads Publisher Service](https://developer.huawei.com/consumer/en/monetize), click **Start now**, and sign in to [Petal Publisher Center](https://developer.huawei.com/consumer/en/service/ads/publisher/html/index.html?lang=en) to apply for an ad unit. For details, please click [here](https://developer.huawei.com/consumer/en/doc/monetize/addunit-0000001051321846).
    
     |
    | 
    
    adWidth
    
     | 
    
    number
    
     | 
    
    Yes
    
     | 
    
    Ad unit width, in vp. Two dimensions are supported: 360 x 57 or 360 x 144.
    
     |
    | 
    
    adHeight
    
     | 
    
    number
    
     | 
    
    Yes
    
     | 
    
    Ad unit height, in vp. Two dimensions are supported: 360 x 57 or 360 x 144.
    
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
    
    The following table describes the key parameters for displaying an ad.
    
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
    
    refreshTime
    
     | 
    
    number
    
     | 
    
    No
    
     | 
    
    Interval for displaying the banner ad in carousel mode, in ms. The value ranges from 30000 to 120000.
    
    If this parameter is left empty or set to a non-numeric value or a number less than or equal to 0, the banner ad will not be displayed in carousel mode. If this parameter is set to a number less than 30000, the value **30000** will be used. If this parameter is set to a number greater than 120000, the value **120000** will be used.
    
     |
    
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
    
    This callback is triggered when a user closes an ad. Hide the ad component in this case.
    
    The callback status contains the specific reason for closing the ads. For details, please refer to the [data description](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#onstatuschanged).
    
     |
    | 
    
    onAdLoad
    
     | 
    
    An ad is successfully loaded.
    
     | 
    
    \-
    
     |
    | 
    
    onAdFail
    
     | 
    
    An ad fails to be loaded.
    
     | 
    
    This callback is triggered when an ad fails to load. Hide the ad component in this case.
    
     |
    
    The sample code is as follows:
    
    @Entry
    @Component
    struct Index {
      @State visibilityState: Visibility = Visibility.None;
      // Ad request parameters.
      private adRequestParams: advertising.AdRequestParams = {
        // **'testw6vs28auh3'** is a dedicated test ad unit ID. Before releasing your app, replace the test ad unit ID with the formal one.
        adId: 'testw6vs28auh3',
        // Banner ad.
        adType: 8,
        // Ad unit width.
        adWidth: 360,
        // Ad unit height.
        adHeight: 57
      };
      // Ad configuration parameters, which can be set based on the project requirements.
      private adOptions: advertising.AdOptions = {};
      // Ad display parameters, which can be set based on the project requirements.
      private adDisplayOptions: advertising.AdDisplayOptions = {
        // Interval for displaying an ad in carousel mode, in ms. The value ranges from 30000 to 120000.
        refreshTime: 30000
      };
      private ratio: number = 1;
      private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    
      async aboutToAppear(): Promise<void> {
        // OAID.
        this.adRequestParams.oaid = await requestOAID(this.context);
        this.visibilityState = Visibility.Visible;
        if (this.adRequestParams.adWidth && this.adRequestParams.adHeight) {
          this.ratio = this.adRequestParams.adWidth / this.adRequestParams.adHeight;
        }
      }
    
      build() {
        Stack({ alignContent: Alignment.Bottom }) {
          Row() {
            AutoAdComponent({
              adParam: this.adRequestParams,
              adOptions: this.adOptions,
              displayOptions: this.adDisplayOptions,
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
                    case 'onAdLoad':
                      hilog.info(0x0000, 'testTag', 'Status is onAdLoad');
                      break;
                    case 'onAdFail':
                      hilog.error(0x0000, 'testTag', 'Status is onAdFail');
                      this.visibilityState = Visibility.None;
                      break;
                  }
                }
              }
            })
          }
          .width('100%')
          .aspectRatio(this.ratio)
          .visibility(this.visibilityState)
        }
        .width('100%')
        .height('100%')
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
