# Rewarded Ads

#### Use Cases

Rewarded ads are full-screen video ads that allow users to view in exchange for in-app rewards.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/ao0DRZxcS4anA2rAnglu2w/en-us_image_0000002305180788.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CAC592D106D8D11DE2BAE9E8180884CD0C490F280A30454A614EFCD36ADFA563)

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
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/Bn-N7_guQQaK7ve_WMW4rg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC1EDC1AE310C4493A69C58BF1D05887CF6CE5B9C00FC3AFDAA411258CEEDC74)
    
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
    
    Type of the requested ad. The value is **7** for rewarded ads.
    
     |
    | 
    
    adId
    
     | 
    
    string
    
     | 
    
    Yes
    
     | 
    
    Ad unit ID.
    
    -   For ad debugging purposes, you can use the test ad unit ID **testx9dtjwj8hp**.
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
          // Called when an ad request fails.
          onAdLoadFailure: (errorCode: number, errorMsg: string) => {
            hilog.error(0x0000, 'testTag', \`Failed to load ad. Code is ${errorCode}, message is ${errorMsg}\`);
          },
          // Called upon ad request success.
          onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
            hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
            // ...
          }
        };
        // Ad request parameters.
        const adRequestParams: advertising.AdRequestParams = {
        // **'testx9dtjwj8hp'** is a dedicated test ad unit ID. Before releasing your app, replace the test ad unit ID with the formal one.
          adId: 'testx9dtjwj8hp',
          // Rewarded ad.
          adType: 7,
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
    
    Subscribe to the **com.huawei.hms.pps.action.PPS\_REWARD\_STATUS\_CHANGED** event to track changes on the rewarded ad page and receive reward information.
    
    After subscribing to the common event, you can obtain the status changes of the rewarded ad page and the reward information from **parameters** of [CommonEventData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-commonevent-commoneventdata).
    
    -   Use **reward\_ad\_status** as the key to obtain the status changes of the rewarded ad page. The following table lists the involved page status changes.
        
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
        
        onAdReward
        
         | 
        
        A user earns a reward from the ad.
        
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
        
    -   Use **reward\_ad\_data** as the key to obtain the reward information, including:
        -   **rewardType**: name of the reward item.
        -   **rewardAmount**: quantity of the reward item.
    
    The sample code is as follows:
    
    const KEY\_REWARD\_DATA = 'reward\_ad\_data';
    const KEY\_REWARD\_STATUS = 'reward\_ad\_status';
    
    export class RewardAdStatusHandler {
      // Used to save the created subscriber object for subsequent subscription and unsubscription.
      private subscriber: commonEventManager.CommonEventSubscriber | null = null;
    
      // Subscription method, which must be called each time before an ad is displayed.
      public registerPPSReceiver(): void {
        if (this.subscriber) {
          this.unRegisterPPSReceiver();
        }
        // Subscriber information.
        const subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
          events: \['com.huawei.hms.pps.action.PPS\_REWARD\_STATUS\_CHANGED'\],
          // Setting **publisherBundleName** to **com.huawei.hms.adsservice** indicates that the subscriber only accepts and processes events from this specific package.
          // If **publisherBundleName** is not explicitly declared, the subscriber may receive forged events from other package names, resulting in security issues or misleading.
          publisherBundleName: 'com.huawei.hms.adsservice'
        };
        // Callback for subscriber creation.
        commonEventManager.createSubscriber(subscribeInfo, (err: BusinessError, commonEventSubscriber:
          commonEventManager.CommonEventSubscriber) => {
          if (err) {
            hilog.error(0x0000, 'testTag', \`Failed to create subscriber. Code is ${err.code}, message is ${err.message}\`);
            return;
          }
          hilog.info(0x0000, 'testTag', 'Succeeded in creating subscriber');
          this.subscriber = commonEventSubscriber;
          // Callback for common event subscription.
          commonEventManager.subscribe(this.subscriber, (err: BusinessError, commonEventSubscriber:
            commonEventManager.CommonEventData) => {
            if (err) {
              hilog.error(0x0000, 'testTag', \`Failed to subscribe. Code is ${err.code}, message is ${err.message}\`);
            } else {
              hilog.info(0x0000, 'testTag', 'Succeeded in subscribing data');
              const status: string = commonEventSubscriber?.parameters?.\[KEY\_REWARD\_STATUS\];
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
                case 'onAdReward':
                  const rewardData: Record<string, string | number> = commonEventSubscriber?.parameters?.\[KEY\_REWARD\_DATA\];
                  const rewardType: string = rewardData?.rewardType as string;
                  const rewardAmount: number = rewardData?.rewardAmount as number;
                  hilog.info(0x0000, 'testTag', \`Status is onAdReward. Type is ${rewardType}, Amount is ${rewardAmount}\`);
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
    import { RewardAdStatusHandler } from './RewardAdStatusHandler';
    
2.  Display the ad.
    
    Call the [showAd](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-advertising#showad) method to display an ad. The **ads** parameter indicates the ad information returned from the [ad request](#section1392312617269). Before displaying an ad, register a listener defined in [event subscription](#section395845163219).
    
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
          // Called when an ad request fails.
          onAdLoadFailure: (errorCode: number, errorMsg: string) => {
            hilog.error(0x0000, 'testTag', \`Failed to load ad. Code is ${errorCode}, message is ${errorMsg}\`);
          },
          // Called upon ad request success.
          onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
            hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
            try {
          // Register a rewarded ad status listener.
              new RewardAdStatusHandler().registerPPSReceiver();
          // Ad display parameters, which can be set based on the project requirements.
              const adDisplayOptions: advertising.AdDisplayOptions = {
          // Whether to mute the ad.
                mute: true,
                // ...
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
    

#### Validating Server-Side Verification Callbacks for Rewarded Ads

A server-side verification callback is a URL request, with specified query parameters, sent by Petal Ads to notify a media server that a user needs to be rewarded for interacting with a rewarded video ad. This mechanism provides an effective way for protection against spoofing.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/aBo1FJg-TOqrl3n7CxSpNQ/en-us_image_0000002339339833.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB0F6C709A01090704B18E744598BBC115AAF140F3ACC778888DF32C0BEE5362)

## What You Need to Know About Rewarding a User

-   You need to balance user experience and reward verification when deciding the time to reward a user. There may be delays if you use server-side callbacks. You are advised to reward the user immediately using a client-side callback and verify all rewards when receiving server-side callbacks. This approach ensures the validity of granted rewards while providing a good user experience.
-   For some apps where reward validity is critically important, delays in granting rewards are acceptable. If this also applies to your app, you are advised to reward users when receiving server-side verification callbacks.

## Validating Server-Side Verification Callbacks

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/XtjDKikBSeyKPbh3SoI_kA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2236829DBE6F5832B0BE591D248B0B74F6B87AA257D26B3F3823C4D92B35214C)

The callback will be received over 12 hours after your app has been released on AppGallery.

1.  Configure reward information for a rewarded ad.
    
    Sign in to [Petal Publisher Center](https://developer.huawei.com/consumer/en/service/ads/publisher/html/index.html?lang=en), go to **My apps**, click **Add ad unit**, select **Rewarded**, and click **Next**. On the page that is displayed, set the reward type and quantity, click **Advanced settings**, and set the server-side verification URL, as shown in the following figure.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/VT8tYqJlSBeLYRyXrXg_FQ/en-us_image_0000002305340528.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4DA41DD63BEEEE7CABD8501687B16A6204EBE3A87A1AFFE11D3FC6E5DA72580)
    
2.  (Optional) Set **customData** and **userId**.
    
    You can set **customData** and **userId** before [displaying an ad in step 2](#section16597193515555). The sample code is as follows:
    
    import { advertising } from '@kit.AdsKit';
    
    // Ad display parameters, which can be set based on the project requirements.
    const adDisplayOptions: advertising.AdDisplayOptions = {
          // Whether to mute the ad.
      mute: true,
          // Set custom data.
      customData: 'CUSTOM\_DATA',
      // Set a custom user ID.
      userId: '1234567'
    };
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/BtsFeLZVTUKUnfhDCtHLAw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D7A62CA5D9CDD399F851A7676916A39BA8720F0B2FD6C30D04D73886D971A30)
    
    If **customData** and **userId** are not set, reward grant events can still be reported, but the two parameters will not be present in the server-side callback. If you want to set **customData** and **userId**, set them before showing the ad and ensure that the URL-encoded values of both parameters do not exceed 1024 characters. Failing to meet these requirements can affect the server-side verification.
    
3.  Obtain the content to be verified.
    
    After a user watches a rewarded ad, the Petal Ads server sends the parameters to be verified as well as **keyId** and **sign** to the [verification URL in step 1](#section77672242539), for example, **https://www.example.com/feedback**. Request example:
    
    {
        "adId" : "testx9dtjwj8hp",
        "data" : "CUSTOM\_DATA",
        "keyId" : "12345678",
        "rewardAmount" : "10",
        "rewardName" : "Gold coin",
        "sign" : "OA33u6mypnhE4hbmF32N/ibYi1uXt72nDDyYMwjDI6JXVVFKePZYo4F7Fuk2MaG......",
        "uniqueId" : "3361626337333932313435313430373438383561376265636130393939313166",
        "userId" : "1234567"
    }
    
    The following table describes the parameters.
    
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
    
    adId
    
     | 
    
    String
    
     | 
    
    Yes
    
     | 
    
    ID of a rewarded video ad unit.
    
     |
    | 
    
    data
    
     | 
    
    String
    
     | 
    
    No
    
     | 
    
    Custom data string.
    
     |
    | 
    
    keyId
    
     | 
    
    String
    
     | 
    
    Yes
    
     | 
    
    Key used to verify callbacks.
    
     |
    | 
    
    rewardAmount
    
     | 
    
    String
    
     | 
    
    No
    
     | 
    
    Reward quantity.
    
     |
    | 
    
    rewardName
    
     | 
    
    String
    
     | 
    
    No
    
     | 
    
    Reward content.
    
     |
    | 
    
    sign
    
     | 
    
    String
    
     | 
    
    Yes
    
     | 
    
    Callback signature.
    
     |
    | 
    
    uniqueId
    
     | 
    
    String
    
     | 
    
    Yes
    
     | 
    
    Hexadecimal identifier generated for each reward grant event.
    
     |
    | 
    
    userId
    
     | 
    
    String
    
     | 
    
    No
    
     | 
    
    User ID.
    
     |
    
4.  Encapsulate the content to be verified.
    
    The format of content to be verified (excluding **sign** and **keyId**) is as follows:
    
    adId={adId}&data={data}&rewardAmount={rewardAmount}&rewardName={rewardName}&uniqueId={uniqueId}&userId={userId}
    
    In the format, parameter values are enclosed in {} and the parameter sequence cannot be changed. If a parameter is null or left empty, do not add it to the URL. Then, use SHA-256 to calculate a hash value for **paramContentData**. The sample code is as follows:
    
    String adId = request.getParameter("adId");
    String data = request.getParameter("data");
    // ...
    String userId = request.getParameter("userId");
    String param = "adId=" + adId + "&data=" + data + "&rewardAmount=" + rewardAmount + "&rewardName=" + rewardName + "&uniqueId=" + uniqueId + "&userId=" + userId;
    // The value of **sha256Value** is all lowercase.
    String sha256Value = Sha256Util.digest(param);
    byte\[\] paramContentData = sha256Value.getBytes(Charset.forName("UTF-8"));
    
    You can calculate the hash value by referring to the following utility class:
    
    public static String digest(String message) {
        if (TextUtils.isEmpty(message)) {
            return "";
        }
        byte\[\] content = message.getBytes(StandardCharsets.UTF\_8);
        return bytesToHexString(digest(content));
    }
    
    public static byte\[\] digest(byte\[\] data) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            return md.digest(data);
        } catch (NoSuchAlgorithmException e) {
            LOGGER.error("sha256 NoSuchAlgorithmException");
        }
        return new byte\[\]{};
    }
    
    public static String bytesToHexString(byte\[\] bytes) {
        if (null == bytes) {
            return "";
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < bytes.length; i++) {
            String hex = Integer.toHexString(0xFF & bytes\[i\]);
            if (hex.length() == 1) {
                sb.append('0');
            }
            sb.append(hex);
        }
        return sb.toString();
    }
    
5.  Obtain the public key list.
    
    a. Sign in to [Petal Publisher Center](https://developer.huawei.com/consumer/en/service/ads/publisher/html/index.html?lang=zh) and click **Account** to view your account information.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/hbyyXC2OQdyfIpLddU6XnQ/en-us_image_0000002305180796.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=959ADE28DA55F4AE1AF6D168E203B639AB511B6206BB5342AFBEF6BABB28C97E)
    
    Click **Obtain key**. In the dialog box that is displayed, obtain the publisher ID and key.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/etsNfUBrS2yrqOtfEsJixg/en-us_image_0000002339220017.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062057Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C43B5ED773E42DFB71E74206C54CD59093CA2ABC01994EC900ED50699448AFA7)
    
    b. Use the API URL of the site to which the release location of your app belongs, to obtain the public key list. The API URLs of different sites are as follows:
    
    -   Chinese mainland: https://ppscrowd-drcn.op.hicloud.com/action-lib-track/publickeys
    
    Use the key to encrypt the body using HMAC-SHA256 to obtain a signature, set the signature to **Authorization**, and set the publisher ID and **Authorization** to the header. The sample code is as follows:
    
    String data = "";
    String url = "https://ppscrowd-dre.op.dbankcloud.com/action-lib-track/publickeys";
    String authorization = "Digest validTime=\\"{0}\\", response=\\"{1}\\"";
    // Publisher ID.
    String userId = "YOUR\_PUBLISHER\_ID"; 
    // Key.
    String key = "YOUR\_KEY"; 
    
    HttpClient httpclient = HttpClients.createDefault();
    HttpGet request = new HttpGet();
    try {
        // Use the key to encrypt the body using HMAC-SHA256 to obtain a signature and set the signature to **Authorization**.
        String validTime = String.valueOf(System.currentTimeMillis());
        String body = validTime + ":/publickeys";
        byte\[\] keyBytes = Base64.decodeBase64(key);
        byte\[\] bodyBytes = body.getBytes(Charsets.UTF\_8);
    
        Mac mac = Mac.getInstance("HmacSHA256");
        SecretKey secretKey = new SecretKeySpec(keyBytes, "HmacSHA256");
        mac.init(secretKey);
        byte\[\] signatureBytes = mac.doFinal(bodyBytes);
    
        String signature = (signatureBytes == null) ? null : Hex.encodeHexString(signatureBytes);
        authorization = MessageFormat.format(authorization, validTime, signature);
        // Set the publisher ID and **Authorization** to the header.
        request.setURI(new URI(url));
        request.setHeader("userId", userId);
        request.setHeader("Authorization", authorization);
        HttpResponse response = httpclient.execute(request);
        data = EntityUtils.toString(response.getEntity());
    } catch (Exception e) {
        System.out.println(e.getMessage());
    }
    
    The data message body is returned (**publicKey** has been anonymized):
    
    {    
        "keys": \[       
            {          
                "keyId":"12345678",          
                "publicKey":"LS0tLS1\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*"       
            },      
            {          
                "keyId": "22345678",                               
                "publicKey":"LS0tLS1\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*"       
            }     
        \]
    }
    
    Response structure:
    
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
    
    keys
    
     | 
    
    List<key>
    
     | 
    
    Yes
    
     | 
    
    Public key list.
    
     |
    
    -   **key** structure:
    
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
    
    keyId
    
     | 
    
    String
    
     | 
    
    Yes
    
     | 
    
    Key ID.
    
     |
    | 
    
    publicKey
    
     | 
    
    String
    
     | 
    
    Yes
    
     | 
    
    Public key.
    
     |
    
6.  Perform verification.
    
    a. Use **keyId** to find the Base64-encoded public key from the public key list.
    
    b. Use **paramContentData**, **publicKey**, **sign**, and **SHA256withRSA** as input parameters to perform verification.
    
    The sample code is as follows:
    
    public static boolean verify(byte\[\] data, String publicKey, String sign, String signatureAlgorithm) {
        try {
            byte\[\] keyBytes = base64Decode(publicKey);
            X509EncodedKeySpec keySpec = new X509EncodedKeySpec(keyBytes);
            KeyFactory keyFactory = KeyFactory.getInstance("RSA");
            PublicKey publicK = keyFactory.generatePublic(keySpec);
            Signature signature = Signature.getInstance(signatureAlgorithm);
            signature.initVerify(publicK);
            signature.update(data);
            return signature.verify(base64Decode(sign));
        } catch (InvalidKeyException | SignatureException | UnsupportedEncodingException | InvalidKeySpecException | NoSuchAlgorithmException e) {
            return false;
        }
    }
    
    private static byte\[\] base64Decode(String encoded) throws UnsupportedEncodingException {
        return Base64.decodeBase64(encoded.getBytes("UTF-8"));
    }
