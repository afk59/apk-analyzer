# Roll Ads

#### Use Cases

Roll ads are displayed as short videos or images, before, during, or after the video content is played.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/YFgQeSR6QKuJk84SDm0KWA/en-us_image_0000002339220013.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB3B9D313DC9B1DB0C8C9E5C63ABC8E3B203553354B08A21D7153F77B8B63761)

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
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Obtain the OAID.
    
    To push ads to users more precisely, add the **oaid** attribute to [AdRequestParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#adrequestparams).
    
    Follow the [description](../../oaid-service/document.md) to obtain the OAID.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/riUUtYWMRt-LJq4TNUyZJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16613EBB30CF816E1EBCE4270345D3C396D542C91507F58AF31744673855439C)
    
    When using the test ad unit provided in the following example, you must obtain the OAID.
    
3.  Request an ad from one ad unit.
    
    Create an **AdLoader** object, use the [loadAd](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#loadad) method of **AdLoader** to request the ad, and use [AdLoadListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#adloadlistener) to track the ad loading status.
    
    To request a roll ad, set the **totalDuration** parameter in [AdOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#adoptions).
    
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
    
    Type of the requested ad. The value is **60** for roll ads.
    
     |
    | 
    
    adId
    
     | 
    
    string
    
     | 
    
    Yes
    
     | 
    
    Ad unit ID.
    
    -   For ad debugging purposes, you can use the test ad unit ID **testy3cglm3pj0**.
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
      // Ad content obtained.
      @State ads: advertising.Advertisement\[\] = \[\];
      // ...
      private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    
      aboutToAppear(): void {
        // Call **loadAd** to load an ad.
        this.loadAd();
      }
    
      // ...
    
      build() {
        // ...
      }
    
      // ...
    
      private async loadAd(): Promise<void> {
        // Ad request callback listener.
        const adLoadListener: advertising.AdLoadListener = {
          onAdLoadFailure: (errorCode: number, errorMsg: string) => {
            hilog.error(0x0000, 'testTag', \`Failed to load ad. Code is ${errorCode}, message is ${errorMsg}\`);
          },
          onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
            hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
            this.ads = ads;
          }
        };
        // Ad request parameters.
        const adRequestParams: advertising.AdRequestParams = {
          // **'testy3cglm3pj0'** is a dedicated test ad unit ID. Before releasing your app, replace the test ad unit ID with the formal one.
          adId: 'testy3cglm3pj0',
          // Roll ad.
          adType: 60,
          // Used to distinguish common requests from preload requests. **true**: asset preload request; **false**: common online request.
          isPreload: false,
          // OAID.
          oaid: await requestOAID(this.context)
        };
        // Ad configuration parameters, which can be set based on the project requirements.
        const adOptions: advertising.AdOptions = {
          // Set the roll ad display duration (mandatory for roll ads).
          totalDuration: 30
        };
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
    

## Displaying an Ad

1.  Import required modules.
    
    import { common } from '@kit.AbilityKit';
    import { AdComponent, advertising } from '@kit.AdsKit';
    import { window } from '@kit.ArkUI';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Display the ad.
    
    When an ad is displayed, use [AdInteractionListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#adinteractionlistener) to listen for ad status callbacks. The following table describes the details.
    
    | 
    Callback Status
    
     | 
    
    Description
    
     | 
    
    Extended Information
    
     | 
    
    Suggestion
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    onAdFail
    
     | 
    
    An ad fails to be loaded.
    
     | 
    
    \-
    
     | 
    
    This callback is triggered when an ad fails to be displayed. Hide the ad component and play the main video in this case.
    
     |
    | 
    
    onPortrait
    
     | 
    
    The back button is tapped when the device is in full-screen mode.
    
     | 
    
    \-
    
     | 
    
    This callback is triggered when the back button is tapped when the device is in full-screen mode. In this case, set screen orientation to portrait, and display the navigation bar, status bar, and bottom navigation bar as required, and set the ad component width and height.
    
     |
    | 
    
    onLandscape
    
     | 
    
    The full-screen button is tapped when the device is in portrait mode.
    
     | 
    
    \-
    
     | 
    
    This callback is triggered when the full-screen button is tapped when the device is in portrait mode. In this case, set screen orientation to landscape, hide the navigation bar, status bar, and bottom navigation bar as required, and set the ad component width and height.
    
     |
    | 
    
    onMediaProgress
    
     | 
    
    The ad playback progress changes.
    
     | 
    
    -   **playTime**: The value is of the number type and indicates the ad playback duration, in milliseconds.
    -   **percentage**: The value is of the number type and indicates the ad playback progress, in percentage.
    
     | 
    
    \-
    
     |
    | 
    
    onMediaStart
    
     | 
    
    An ad starts to be played.
    
     | 
    
    -   **playTime**: The value is of the number type and indicates the ad playback duration, in milliseconds.
    
     | 
    
    \-
    
     |
    | 
    
    onMediaPause
    
     | 
    
    The ad playback is paused.
    
     | 
    
    -   **playTime**: The value is of the number type and indicates the ad playback duration, in milliseconds.
    
     | 
    
    \-
    
     |
    | 
    
    onMediaStop
    
     | 
    
    The ad playback stops.
    
     | 
    
    -   **playTime**: The value is of the number type and indicates the ad playback duration, in milliseconds.
    
     | 
    
    \-
    
     |
    | 
    
    onMediaComplete
    
     | 
    
    The ad playback is complete.
    
     | 
    
    -   **playTime**: The value is of the number type and indicates the ad playback duration, in milliseconds.
    
     | 
    
    This callback is triggered upon the completion of a single ad playback. Once all ads have finished playing, hide the ad component and play the main video.
    
     |
    | 
    
    onMediaError
    
     | 
    
    An ad fails to be played.
    
     | 
    
    -   **playTime**: The value is of the number type and indicates the ad playback duration, in milliseconds. Value **\-1** indicates an exception.
    -   **errorCode**: The value is of the number type and indicates the error code ID.
    -   **errorMsg**: The value is of the string type and indicates the error message.
    
    For details about the error codes, please refer to AVPlayer.[on('error')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avplayer#onerror9).
    
     | 
    
    \-
    
     |
    | 
    
    onMediaCountdown
    
     | 
    
    The ad playback countdown is updated.
    
     | 
    
    -   **countdownTime**: The value is of the number type and indicates the countdown duration, in seconds.
    
     | 
    
    This callback is triggered when the ad countdown is updated. The countdown control needs to be drawn based on the countdown duration in the extended information.
    
     |
    | 
    
    onBackClicked
    
     | 
    
    The back button is tapped.
    
     | 
    
    \-
    
     | 
    
    This callback is triggered when the back button is tapped in non-full-screen mode or when the system is locked in full-screen mode. In this case, the atomic service should return to the previous page.
    
     |
    
    Use **AdComponent** to display a roll ad. Take a pre-roll ad as an example. After the ad is played, the main video will be played.
    
    The sample code is as follows:
    
    @Entry
    @Component
    struct Index {
      // Ad content obtained.
      @State ads: advertising.Advertisement\[\] = \[\];
      // Countdown text.
      @State countDownText: string = '';
      // Roll ad playback status.
      @State rollPlayState: number = 1;
      // Whether to play the main video.
      @State isPlayVideo: boolean = false;
      // Video aspect ratio.
      @State ratio: number = 16 / 9;
      // Ad display parameters, which can be set based on the project requirements.
      private adDisplayOptions: advertising.AdDisplayOptions = {
        // Whether to mute the ad.
        mute: true
      };
      // Number of roll ads that have been played.
      private playedAdSize: number = 0;
      // Used to render the countdown in the upper right corner.
      private countDownTxtPlaceholder: string = '%d | No ads for VIP members';
      private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    
      // ...
    
      aboutToDisappear(): void {
        // Set screen orientation to the default value. You can change the value based on the project requirements.
        void this.setWindowPreferredOrientation(window.Orientation.UNSPECIFIED).catch((error: BusinessError) => {
          hilog.info(0x0000, 'testTag',
            \`Failed to setWindowPreferredOrientation. Code is ${error.code}, message is ${error.message}\`);
        });
        // Display the navigation bar, status bar, and bottom navigation bar. You can change the value based on the project requirements.
        void this.setWindowSystemBar(\['status', 'navigation'\]).catch((error: BusinessError) => {
          hilog.info(0x0000, 'testTag',
            \`Failed to setWindowSystemBar. Code is ${error.code}, message is ${error.message}\`);
        });
      }
    
      build() {
        Stack({ alignContent: Alignment.TopEnd }) {
          if (!this.isPlayVideo && this.ads.length > 0) {
            AdComponent({
              ads: \[...this.ads\],
              rollPlayState: this.rollPlayState,
              displayOptions: this.adDisplayOptions,
              interactionListener: {
                // Ad status change callback.
                onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
                  switch (status) {
                    case 'onAdFail':
                      hilog.error(0x0000, 'testTag', 'Status is onAdFail');
                      this.isPlayVideo = true;
                      break;
                    case 'onPortrait':
                      hilog.info(0x0000, 'testTag', 'Status is onPortrait');
                      // Set the screen to portrait.
                      void this.setWindowPreferredOrientation(window.Orientation.PORTRAIT).catch((error: BusinessError) => {
                        hilog.info(0x0000, 'testTag',
                          \`Failed to setWindowPreferredOrientation. Code is ${error.code}, message is ${error.message}\`);
                      });
                      // Display the navigation bar, status bar, and bottom navigation bar.
                      void this.setWindowSystemBar(\['status', 'navigation'\]).catch((error: BusinessError) => {
                        hilog.info(0x0000, 'testTag',
                          \`Failed to setWindowSystemBar. Code is ${error.code}, message is ${error.message}\`);
                      });
                      // In portrait mode, revert to the original aspect ratio.
                      this.ratio = 16 / 9;
                      break;
                    case 'onLandscape':
                      hilog.info(0x0000, 'testTag', 'Status is onLandscape');
                      // Set the screen to landscape.
                      void this.setWindowPreferredOrientation(window.Orientation.LANDSCAPE).catch((error: BusinessError) => {
                        hilog.info(0x0000, 'testTag',
                          \`Failed to setWindowPreferredOrientation. Code is ${error.code}, message is ${error.message}\`);
                      });
                      // Hide the navigation bar, status bar, and bottom navigation bar.
                      void this.setWindowSystemBar(\[\]).catch((error: BusinessError) => {
                        hilog.info(0x0000, 'testTag',
                          \`Failed to setWindowSystemBar. Code is ${error.code}, message is ${error.message}\`);
                      });
                      // Ignore the aspect ratio in landscape mode.
                      this.ratio = -1;
                      break;
                    case 'onMediaProgress':
                      hilog.info(0x0000, 'testTag', 'Status is onMediaProgress');
                      break;
                    case 'onMediaStart':
                      hilog.info(0x0000, 'testTag', 'Status is onMediaStart');
                      break;
                    case 'onMediaPause':
                      hilog.info(0x0000, 'testTag', 'Status is onMediaPause');
                      break;
                    case 'onMediaStop':
                      hilog.info(0x0000, 'testTag', 'Status is onMediaStop');
                      break;
                    case 'onMediaComplete':
                      hilog.info(0x0000, 'testTag', 'Status is onMediaComplete');
                      // After all ads have finished playing, the main video starts to be played.
                      this.playedAdSize++;
                      if (this.playedAdSize === this.ads.length) {
                        this.isPlayVideo = true;
                      }
                      break;
                    case 'onMediaError':
                      hilog.error(0x0000, 'testTag', 'Status is onMediaError');
                      break;
                    case 'onMediaCountdown':
                      hilog.info(0x0000, 'testTag', 'Status is onMediaCountdown');
                      const parseData: Record<string, Object> = this.safeParseData(data);
                      this.countDownText = this.countDownTxtPlaceholder.replace('%d', String(parseData.countdownTime));
                      break;
                    case 'onBackClicked':
                      hilog.info(0x0000, 'testTag', 'Status is onBackClicked');
                      this.getUIContext().getRouter().back();
                      break;
                  }
                }
              }
            })
              .visibility(!this.isPlayVideo ? Visibility.Visible : Visibility.None)
              .width('100%')
              .height('100%')
    
            Text(this.countDownText)
              .fontSize(12)
              .lineHeight(12)
              .maxLines(1)
              .textAlign(TextAlign.Center)
              .fontColor(Color.White)
              .textOverflow({ overflow: TextOverflow.Ellipsis })
              .backgroundColor('#66000000')
              .border({ radius: 25 })
              .padding(8)
              .margin(16)
              .height(24)
              .onClick(() => {
                hilog.info(0x0000, 'testTag', 'OnVipClicked, do something...');
                this.isPlayVideo = true;
              })
              .visibility(this.countDownText ? Visibility.Visible : Visibility.None)
          }
    
          Video({
            // Video to be played after the ad playback is complete. Set this parameter based on the project requirements.
            src: $rawfile('videoTest.mp4'),
            // Preview image of the video to be played. Set this parameter based on the project requirements.
            previewUri: $r('app.media.video\_preview'),
            controller: new VideoController()
          })
            .visibility(this.isPlayVideo ? Visibility.Visible : Visibility.None)
            .autoPlay(this.isPlayVideo)
            .controls(false)
            .width('100%')
            .height('100%')
        }
        .width('100%')
        .height('100%')
        .aspectRatio(this.ratio)
      }
    
      private async setWindowPreferredOrientation(orientation: Orientation): Promise<void> {
        try {
          const win: window.Window = await window.getLastWindow(this.context);
          await win.setPreferredOrientation(orientation);
        } catch (e) {
          hilog.error(0x0000, 'testTag', \`Failed to set preferred orientation. Code is ${e.code}, message is ${e.message}\`);
        }
      }
    
      private async setWindowSystemBar(names: Array<'status' | 'navigation'>): Promise<void> {
        try {
          const win: window.Window = await window.getLastWindow(this.context);
          await win.setWindowSystemBarEnable(names);
        } catch (e) {
          hilog.error(0x0000, 'testTag', \`Failed to set window system bar. Code is ${e.code}, message is ${e.message}\`);
        }
      }
    
      private safeParseData(data: string): Record<string, Object> {
        try {
          if (typeof data === 'string') {
            return JSON.parse(data);
          }
          return JSON.parse(JSON.stringify(data));
        } catch (e) {
          hilog.error(0x0000, 'testTag', \`Failed to parse data. Code is ${e.code}, message is ${e.message}\`);
        }
        return {};
      }
    
      // ...
    }
