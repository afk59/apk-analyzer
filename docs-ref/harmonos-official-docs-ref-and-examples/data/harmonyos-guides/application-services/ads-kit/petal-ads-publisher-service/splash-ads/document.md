# Splash Ads

#### Use Cases

Splash ads are displayed immediately after an app is launched, even before the home screen of the app is displayed. You need to design a default slogan image for the app in advance, and ensure that the default slogan image is displayed before a splash ad is loaded, enhancing user experience.

Splash ads come in two forms: full-screen and half-screen. Full-screen splash ads take up the entire page, while half-screen splash ads are designed to fit custom layouts of the media UI, rendering the ad, icon, and copyright information accordingly. Typically, it is suggested to position the icon and copyright information beneath the ad.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/yQgaN2o6QpaZgrqU0s-O3w/en-us_image_0000002305340520.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0FE26A635B20F308DD6DE27355EBF8F44CB044827C93C14AE70FE04F81ADF9AD)

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

[AdComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-adcomponent)({ads: advertising.Advertisement\[\], displayOptions: advertising.AdDisplayOptions, interactionListener: advertising.AdInteractionListener, @BuilderParam adRenderer?: () => void, @Prop rollPlayState?: number})

 | 

Displays ads. It uses **AdDisplayOptions** for setting ad display parameters and **AdInteractionListener** for tracking the ad interaction status.

**Note**: To ensure that ads can be correctly displayed, this API must be used together with the ad request API.

 |

#### Development Procedure

## Requesting an Ad

1.  Import required modules.
    
    import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';
    import { advertising, identifier } from '@kit.AdsKit';
    import { router, window } from '@kit.ArkUI';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Obtain the OAID.
    
    To push ads to users more precisely, add the **oaid** attribute to [AdRequestParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#adrequestparams).
    
    Follow the [description](../../oaid-service/document.md) to obtain the OAID.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/dLwaAbNyTi6K1DM0ebBLcw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=990D58F7F87EF8939F8C34F6B2944A0BF8A416AC2A89EFEB99BF0C9BE7859329)
    
    When using the test ad unit provided in the following example, you must obtain the OAID.
    
3.  Request an ad from one ad unit.
    
    Create an **AdLoader** object, use the [loadAd](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#loadad) method of **AdLoader** to request the ad, and use [AdLoadListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#adloadlistener) to track the ad loading status. When you test splash ads, a test ad unit is needed to obtain and test the splash ads. The sample code offers test ad units for two types of slash ads: one for half-screen image ads with the ID **testq6zq98hecj**, and the other for full-screen video ads with the ID **testd7c5cewoj6**. These test ad unit IDs are for debugging purposes only and are not intended for ad monetization.
    
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
    
    Type of the requested ad. The value is **1** for splash ads.
    
     |
    | 
    
    adId
    
     | 
    
    string
    
     | 
    
    Yes
    
     | 
    
    Ad unit ID.
    
    -   For ad debugging purposes, you can use the test ad unit IDs: **testq6zq98hecj** (half-screen image ads) and **testd7c5cewoj6** (full-screen video ads).
    -   For official ad delivery, you need to apply for a formal ad unit ID. Before app release, go to [Petal Ads Publisher Service](https://developer.huawei.com/consumer/en/monetize), click **Start now**, and sign in to [Petal Publisher Center](https://developer.huawei.com/consumer/en/service/ads/publisher/html/index.html?lang=en) to apply for an ad unit. For details, please click [here](https://developer.huawei.com/consumer/en/doc/monetize/addunit-0000001051321846).
    
     |
    | 
    
    adCount
    
     | 
    
    number
    
     | 
    
    No
    
     | 
    
    Ad quantity.
    
     |
    | 
    
    orientation
    
     | 
    
    number
    
     | 
    
    No
    
     | 
    
    Screen orientation of the ad requested by the app. **1**: portrait mode; **0**: landscape mode. If this parameter is not set, the default value **1** will be used. Currently, no landscape-mode splash ad creatives are available. Therefore, if the orientation is set to landscape, no splash ad will be displayed. If the app is configured to always display in landscape mode, but **orientation** is not set or is set to **1**, the display effect will be affected.
    
     |
    
    | 
    Response Parameter
    
     | 
    
    Type
    
     | 
    
    Description
    
     |
    | :-- | :-- | :-- |
    | 
    
    isFullScreen
    
     | 
    
    boolean
    
     | 
    
    Indicates whether the returned ad is in full-screen mode. The value **true** indicates a full-screen ad, and **false** indicates a half-screen ad.
    
     |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/76vo8Pv8SSGzZp-UhUvsnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86C73F99F2A4580D6D08B3DA4406D55E6746EE6E66204739A9CF0588035BA48E)
    
    1\. If no ad is requested within the specified period, the app automatically jumps to the default home screen.
    
    2\. For a better splash ad effect, you are advised to set the screen orientation to portrait before requesting ads.
    
    @Entry
    @Component
    struct Index {
      @State ad: advertising.Advertisement | undefined = undefined;
      // ...
      private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      // Whether the request times out.
      private isTimeOut: boolean = false;
      // Timeout interval, in milliseconds. You can change the value as required.
      private timeOutDuration: number = 1000;
      // Timeout index.
      private timeOutIndex: number = -1;
    
      aboutToAppear(): void {
        // Enable the full-screen immersive mode.
        this.setWindowLayoutFullScreen(true);
        // Set the screen to portrait.
        this.setWindowPreferredOrientation(window.Orientation.PORTRAIT);
        // Call **loadAd** to load an ad.
        // ...
      }
    
      aboutToDisappear(): void {
        // Disable the full-screen mode. Set the mode based on your needs.
        this.setWindowLayoutFullScreen(false);
        // Set screen orientation to the default value. You can change the value based on your needs.
        this.setWindowPreferredOrientation(window.Orientation.UNSPECIFIED);
      }
    
      private async setWindowLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void> {
        try {
          const win: window.Window = await window.getLastWindow(this.context);
          await win.setWindowLayoutFullScreen(isLayoutFullScreen);
        } catch (e) {
          hilog.error(0x0000, 'testTag', \`Failed to set window layout. Code is ${e.code}, message is ${e.message}\`);
        }
      }
    
      private async setWindowPreferredOrientation(orientation: Orientation): Promise<void> {
        try {
          const win: window.Window = await window.getLastWindow(this.context);
          await win.setPreferredOrientation(orientation);
        } catch (e) {
          hilog.error(0x0000, 'testTag', \`Failed to set preferred orientation. Code is ${e.code}, message is ${e.message}\`);
        }
      }
    
      build() {
        // ...
      }
    
      // ...
      private async loadAd(adId: string): Promise<void> {
        // Ad request parameters.
        const adRequestParams: advertising.AdRequestParams = {
          // Ad unit ID.
          adId: adId,
          // Splash ad.
          adType: 1,
          // Number of requested ads.
          adCount: 1,
          // OAID.
          oaid: await requestOAID(this.context)
        };
        // Ad request callback listener.
        const adLoadListener: advertising.AdLoadListener = {
          onAdLoadFailure: (errorCode: number, errorMsg: string) => {
            hilog.error(0x0000, 'testTag', \`Failed to load ad. Code is ${errorCode}, message is ${errorMsg}\`);
          },
          onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
            clearTimeout(this.timeOutIndex);
            if (this.isTimeOut) {
              return;
            }
            hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
            this.ad = ads\[0\];
          }
        };
        // Ad configuration parameters, which can be set based on the project requirements.
        const adOptions: advertising.AdOptions = {};
        // Create an **AdLoader** ad object.
        const adLoader: advertising.AdLoader = new advertising.AdLoader(this.context);
        // Start the timeout timer.
        this.timeOutHandler();
        try {
          // Call the API for requesting ads.
          adLoader.loadAd(adRequestParams, adOptions, adLoadListener);
        } catch (e) {
          hilog.error(0x0000, 'testTag', \`Failed to load ad. Code is ${e.code}, message is ${e.message}\`);
        }
      }
    
      private timeOutHandler(): void {
        this.isTimeOut = false;
      // Timeout handling.
        this.timeOutIndex = setTimeout(() => {
          this.isTimeOut = true;
          this.routeToHome();
          hilog.error(0x0000, 'testTag', 'Load ad time out');
        }, this.timeOutDuration);
      }
    
      private routeToHome(): void {
        // You can change the target page for redirection that is triggered after a timeout, based on the project requirements.
        this.getUIContext().getRouter().replaceUrl({ url: 'pages/Index' }, router.RouterMode.Single)
          .catch((e: BusinessError) => {
            hilog.error(0x0000, 'testTag', \`Failed to route to home. Code is ${e.code}, message is ${e.message}\`);
          });
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
    

## Displaying an Ad

1.  Import required modules.
    
    import { AdComponent, advertising } from '@kit.AdsKit';
    import { router } from '@kit.ArkUI';
    import { BusinessError } from '@kit.BasicServicesKit';
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
    
    This callback is triggered when the ad countdown ends, a user taps the skip button, or an ad is returned from the background. In these cases, the app should navigate to the home page.
    
    The callback status contains the specific reason for closing the ads. For details, please refer to the [data description](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#onstatuschanged).
    
     |
    | 
    
    onAdFail
    
     | 
    
    An ad fails to be loaded.
    
     | 
    
    This callback is triggered when an ad fails to be displayed. In this case, the app should navigate to its home screen.
    
     |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/Iwz3ZE7NR72E6z_FjCk9sA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97D4DECCD2CBBD43D700D9B0C1787D3A33EE1535D45558CDDA865F2D6FFCCF50)
    
    1\. The default slogan image needs to be displayed before an ad is requested.
    
    2\. The app determines whether to display a full-screen or half-screen ad based on the **isFullScreen** parameter obtained from the requested ad.
    
    3\. Currently, only vertical ads can be displayed.
    
    @Entry
    @Component
    struct Index {
      @State ad: advertising.Advertisement | undefined = undefined;
      // Ad display parameters.
      private adDisplayOptions: advertising.AdDisplayOptions = {
        // Whether to mute the ad.
        mute: true
      };
      // ...
    
      build() {
        RelativeContainer() {
          // Display the custom slogan image.
          Image($r('app.media.slogan'))
            .width('100%')
            .height('100%')
            .zIndex(0)
          // Display the custom icon, app name, and copyright information.
          Column() {
            Row() {
              Image($r('app.media.video'))
                .width(24)
                .height(24)
                .margin(8)
              Text($r('app.string.video'))
                .fontColor('#1A1A1A')
                .fontSize(16)
            }
            .margin({ bottom: 8 })
    
            Column() {
              Text($r('app.string.copyright'))
                .fontColor('#1A1A1A')
                .fontSize(9)
            }
          }
          .zIndex(1)
          .alignRules({ bottom: { anchor: '\_\_container\_\_', align: VerticalAlign.Bottom } })
          .width('100%')
          .height('13%')
    
          if (this.ad) {
            if (this.ad.isFullScreen) {
              // Full-screen splash ad.
              this.splashFullScreen()
            } else {
              // Half-screen splash ad.
              this.splashHalfScreen()
            }
          }
        }
        .width('100%')
        .height('100%')
      }
    
      /\*\*
       \* Half-screen splash ad.
       \*/
      @Builder
      private splashHalfScreen() {
        AdComponent({
          ads: \[this.ad!\],
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
                  this.routeToHome();
                  break;
                case 'onAdFail':
                  hilog.error(0x0000, 'testTag', 'Status is onAdFail');
                  this.routeToHome();
                  break;
              }
            }
          }
        })
          .zIndex(1)
          .width('100%')
          .height('87%')
          // Custom component animation.
          .transition(TransitionEffect.OPACITY.animation({ duration: 1000, curve: Curve.Friction}))
          .alignRules({ top: { anchor: '\_\_container\_\_', align: VerticalAlign.Top } })
      }
    
      /\*\*
       \* Full-screen splash ad.
       \*/
      @Builder
      private splashFullScreen() {
        AdComponent({
          ads: \[this.ad!\],
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
                  this.routeToHome();
                  break;
                case 'onAdFail':
                  hilog.error(0x0000, 'testTag', 'Status is onAdFail');
                  this.routeToHome();
                  break;
              }
            }
          }
        })
          .zIndex(1)
          .width('100%')
          .height('100%')
      }
      // ...
    
      private routeToHome(): void {
        // You can change the target page for redirection that is triggered after a timeout, based on the project requirements.
        this.getUIContext().getRouter().replaceUrl({ url: 'pages/Index' }, router.RouterMode.Single)
          .catch((e: BusinessError) => {
            hilog.error(0x0000, 'testTag', \`Failed to route to home. Code is ${e.code}, message is ${e.message}\`);
          });
      }
    }
    
    // ...
