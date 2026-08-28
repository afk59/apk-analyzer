# Standalone Game Sign-in

A standalone game is a game in which data is stored locally and no server connection is required.

After integrating the basic game service, a standalone game allows users to quickly sign in with a HUAWEI ID. The basic game service also provides HUAWEI ID identity verification and anti-addiction for minors for standalone games.

#### Preparations

## Creating a Game

To release a game on AppGallery, you need to create a game app in AppGallery Connect. For details, please refer to [Creating a HarmonyOS App](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-app-0000002247955506). Relevant parameters need to be set as follows:

-   **App type**: Select **HarmonyOS app**.
-   **Level-1 app category**: Select **Game**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/EywrDfhsREuRbNwU9uNGXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=035A5992365103885835F451893F421D4EB5BC5418C8A75B22AC26DDF8DB7D68)

It is recommended that the name of the game package for official release not contain words such as **test** and **dev**.

## Applying for Identity Verification by the National Press and Publication Administration

According to the _Notice by the National Press and Publication Administration of Further Imposing Strict Administrative Measures to Prevent Minors from Becoming Addicted to Online Games_, all game publishing and operating enterprises were required to complete interconnection with the [online game anti-addiction identity verification system](https://wlc.nppa.gov.cn/fcm_company/index.html#/login?redirect=/) before June 1, 2021, with **bizID** (game record filing identification code) obtained. A game's **bizID** needs to be configured in AppGallery Connect for Huawei to connect to the National Press and Publication Administration's identity verification system and enable mandatory identity verification. No additional development is required from developers.

## Generating a Signing Certificate

The signature information, including the digital certificate and profile, can ensure the integrity of your game.

-   Debugging phase: [Sign your app manually](../../../../../coding-and-debugging/configuring-a-debug-signature/document.md#section297715173233), [request a debug certificate](https://developer.huawei.com/consumer/en/doc/app/agc-help-debug-cert-0000002283256797), and [request a debug profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-debug-profile-0000002248181278).
-   Release phase: [Sign your app manually](../../../../../coding-and-debugging/configuring-a-debug-signature/document.md#section297715173233), [request a release certificate](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-cert-0000002283336729), and [request a release profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-profile-0000002248341090).

## Configuring a Signing Certificate Fingerprint

AppGallery Connect automatically generates a public key for the certificate and calculates the SHA-256 fingerprint. You need to obtain and configure the SHA-256 fingerprint in AppGallery Connect. Each game can have a maximum of four signing certificate fingerprints. For details, please refer to [Configuring a Public Key Fingerprint](https://developer.huawei.com/consumer/en/doc/app/agc-help-cert-fingerprint-0000002278002933).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/WwxIVvIXQOqWP4KcZtUqXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCC20C2EC31D74CADE7C288B98A12D3297EB54BE25B5FC16825A010ABE07D9B7)

Add the fingerprint of the debug certificate in the debugging phase and add the fingerprint of the release certificate in the release phase.

## Configuring the App ID and Client ID

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), choose **Development and services**, select your project and game, and obtain the app ID and client ID under **App information**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/XwKcHBTzQrW1CvZ_snHIbw/en-us_image_0000002517704709.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FBEF55484CBDE339EF1B0ABF9EBA966AD8A211731A985DADDDE95ED245BB1D8E)
    
2.  In the **module.json5** file of the **entry** module in the project, add **metadata**, configure **client\_id** and **app\_id** in **metadata**, and add **requestPermissions** to configure the network permission. The sample code is as follows:
    
    "module": {
      "name": "entry",
      "type": "xxx",
      "description": "xxxx",
      "mainElement": "xxxx",
      "deviceTypes": \[\],
      "pages": "xxxx",
      "abilities": \[\],
      "metadata": \[ // Configure the following information:
        {
          "name": "client\_id",
          "value": "xxxxxx" // Set it to the client ID obtained in the preceding step.
        },
        {
          "name": "app\_id",
          "value": "xxxxxx" // Set it to the app ID obtained in the preceding step.
        }
      \],
      "requestPermissions": \[ // Configure the network permission.
        {
          "name": "ohos.permission.INTERNET"
        }
      \]
    }
    

## Configuring the App ID Mapping

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), choose **Development and services**, select your project and game, choose **Build** > **Game Service** from the navigation pane on the left, and click **New Configuration**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/t5DEjSB5T82CSK0sWqU49Q/en-us_image_0000002523641337.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9DD6B2F8D952847EDA88CF01F5707948E33CAB4050508454FDFE0EBFCEEEA74F)
    
2.  In the **Adding configuration information** dialog box, set the parameters and click **Next step**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/sta385V4QGWY9tjO5XO-mQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE3F2305049679BFD7D13BC9B263E87E42042CB6C268957D7369B24E00A90F83)
    
    Ensure that the mapping between the game (in HAP format) and the game (in APK format) is correctly configured. If you select a game of an incorrect type, a dialog box will be displayed, prompting you to reselect a correct game.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/cOgkLTfLSWC_4Y_XKbHNGw/en-us_image_0000002485705812.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4139C50C77DD84B298B00DA96AEC6FD3A96941E278E26BDFBC8BF5EED0D757EB)
    
    | 
    Parameter
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    HarmonyOS 5.0 and above game
    
     | 
    
    Select the game (in HAP format) to be released.
    
     |
    | 
    
    HarmonyOS 4 and below game
    
     | 
    
    Select the corresponding game (in APK format) that has been released or is to be released.
    
     |
    
3.  In the displayed dialog box, set the parameters and click **Next step**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/PphEODyeSdqBRj3oOUVh5A/en-us_image_0000002485705816.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB33C7A044C5C371FEB3566649584CFBFC674B5B5081961ABF4AF35DB748E507)
    
4.  (Optional) Enter the callback address of your server and click **OK** to submit the app ID mapping for approval.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/UgZ5DU_jSL-SHYMJeLZ_vQ/en-us_image_0000002485545868.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86008E7EEBDC215832CE1A958E618EB66DD7128F609A9CFD3448C4A1BD30535A)
    
5.  Any exceptions (for example, the release status does not meet the requirements) will be indicated in red text in the dialog box shown below. You are advised to click **Cancel** and reconfigure the app ID mapping. If you ignore the exceptions and click **OK** to continue submitting, your app ID mapping configuration may be rejected.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/c9fASttrTIin6pzCN09ZQA/en-us_image_0000002517745779.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9639FDAB6F25089964BB4B7B902A14E0E03DF08815C37A4E9355FA3E8C10C0BE)
    
6.  After you submit your request, it will take 1–3 working days for Huawei staff to complete the review.
    
    If you want to reconfigure the app ID mapping after it has taken effect, submit a request for deleting the mapping first.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/lEKPwXb2QS287yeb2tG7dA/en-us_image_0000002485545908.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A0C827F997774F295C7EDCE419EC4841EE1852461D432092515909B136DA435)
    
    The review result of the app ID mapping configuration or deletion request will be sent to you through the interaction center or email.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/8mcK1qcmR8GeR7Cf9luhjw/en-us_image_0000002517705829.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AEDFB5F83CDDC4D9483BEF9DC41702557A8DC20B6D8696FDD04E673953075DA9)
    

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/_98NU_7XQyOCTN2XAPER_Q/en-us_image_0000002517705841.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CA2EBF496DF33824BDCA6127B0270E9C948E79B136DA28A49673404DB49DE1D)

1.  The player starts the game.
2.  The game calls the [init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section225333655719) API to initialize Game Service Kit. After the initialization, the Huawei privacy agreement pop-up is displayed. Once the player accepts the terms, the process continues.
3.  The game calls the [unionLogin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section157848375136) API with the **showLoginDialog** parameter set to **false** and the **thirdAccountInfos** parameter set to an empty array.
4.  The game displays a welcome banner on the top of the screen. Game Service Kit returns the information to the game, including **accountName** (or **hw\_account** if HUAWEI ID sign-in is used), **accountIdentifier** (or **hw\_account** if HUAWEI ID sign-in is used), and **gamePlayerId**.
5.  Call the [verifyLocalPlayer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section15119154416715) API to check the following information about the HUAWEI ID signed in on the user's device: After the verification is successful, the player enters the game.
    1.  If the player has not completed identity verification, the [verifyLocalPlayer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section15119154416715) API displays the identity verification pop-up for the player.
    2.  If the player has completed identity verification and is identified as a minor, the [verifyLocalPlayer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section15119154416715) API will then automatically detect their game playtime. If the player signs in beyond the specified timeframe, the player will be forcibly signed out and error code [1002000006](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-error-code#section4418848101513) will be returned.

#### API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer).

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section225333655719)(context: common.UIAbilityContext, callback: AsyncCallback<void>): void

 | 

Initializes Game Service Kit using the default context. This API returns the result through a callback.

 |
| 

[unionLogin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section157848375136)(context: common.UIAbilityContext, loginParam: UnionLoginParam): Promise<UnionLoginResult>

 | 

Signs in to the game. This API returns the result through a promise.

 |
| 

[verifyLocalPlayer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section15119154416715)(context: common.UIAbilityContext, thirdUserInfo: ThirdUserInfo): Promise<void>

 | 

Verifies compliance, including the identity verification status and anti-addiction information of the HUAWEI ID signed in on the current device. This API returns the result through a promise.

 |

#### Development Procedure

## Importing Modules

Import Game Service Kit and common modules.

import { gamePlayer } from '@kit.GameServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

## Performing Initialization

Call the [init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section225333655719) API to initialize Game Service Kit.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/L2I6uoJaQZ24TmnhHnvvhA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA76348587F605A0B05A34ED035F5FDD6D63D4C2A276BF21B35DBB34E2992BAC)

-   The class calling this API must strictly inherit from **UIAbility**, and the optimal time to obtain the context is after the game UI has been successfully loaded in the **onWindowStageCreate** lifecycle method.
-   Your game can call other APIs only after successfully calling the [init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section225333655719) API. Otherwise, your game release request will be rejected.

onWindowStageCreate(windowStage: window.WindowStage) {
  windowStage.loadContent("pages/index", (err, data) => {
    try {
      gamePlayer.init(this.context,()=>{
        hilog.info(0x0000, 'testTag', \`Succeeded in initializing.\`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', \`Failed to init. Code: ${err.code}, message: ${err.message}\`);
    }
  });
}

After the initialization, the Huawei privacy agreement pop-up is displayed. After the player signs the agreement, the process continues.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/2WpWUBAfTV2vcgGI87L7gg/en-us_image_0000002517745911.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE302140557F71A6CC12B4BC23C77A6DD80779D21A56C29CB65443CD0AC70EBE "Click to enlarge")

Once the player signs the privacy agreement, the privacy agreement pop-up will not be displayed again for games they sign in with that HUAWEI ID.

## Signing in to the Game

Call the [unionLogin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section157848375136) API to sign in to the game.

let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
let request: gamePlayer.UnionLoginParam = {
  showLoginDialog: false, // Indicates whether to display the multi-provider sign-in panel. The value **true** indicates that the panel will be forcibly displayed. The value **false** indicates that the player's last sign-in method will be used and the panel will not be displayed. However, the panel will always be displayed for first-time sign-ins or after a reinstallation.
  thirdAccountInfos: \[\] // For standalone games, pass an empty array.
};
try {
  gamePlayer.unionLogin(context, request).then((result: gamePlayer.UnionLoginResult) => {
    hilog.info(0x0000, 'testTag', \`Succeeded in logging in: ${result?.accountName}\`);
  }).catch((error: BusinessError) => {
    hilog.error(0x0000, 'testTag', \`Failed to login. Code: ${error.code}, message: ${error.message}\`);
  });
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', \`Failed to login. Code: ${err.code}, message: ${err.message}\`);
}

After the player completes the sign-in process, a welcome banner is displayed on the top of the game, and information such as **accountName** (or **hw\_account** if HUAWEI ID sign-in is used) and **gamePlayerId** is returned to the game.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/PkZQaVljRyKqDnSkweqGOw/en-us_image_0000002517745933.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AE7D1ED0F3E76288A520E25D2F0E88420902D1BBAC8D081742DBFADFC07809A "Click to enlarge")

## Performing Compliance Verification

Call the [verifyLocalPlayer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section15119154416715) API to verify the identity verification status and minor anti-addiction information of the HUAWEI ID signed in on the current device. After successful verification, the player enters the game.

let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
let request: gamePlayer.ThirdUserInfo = {
  thirdOpenId: '' // Leave this parameter empty for standalone games.
};
try {
  gamePlayer.verifyLocalPlayer(context, request).then(() => {
    hilog.info(0x0000, 'testTag', \`Succeeded in verifying.\`);
  }).catch((error: BusinessError) => {
    hilog.error(0x0000, 'testTag', \`Failed to verify. Code: ${error.code}, message: ${error.message}\`);
  });
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', \`Failed to verify. Code: ${err.code}, message: ${err.message}\`);
}

For HUAWEI IDs, the basic game service provides identity verification and anti-addiction for minors, and IAP Kit provides payment compliance control (for example, payment limits for minors).

| 
Compliance Verification

 | 

Verification Item

 | 

National Regulation

 | 

Solution

 |
| :-- | :-- | :-- | :-- |
| 

HUAWEI ID identity verification

 | 

Check whether the HUAWEI ID signed in on the device has completed identity verification.

 | 

In accordance with relevant laws and regulations, all online game players must register and sign in with valid and authentic identity information.

 | 

When a player signs in with a HUAWEI ID that has not completed identity verification, the basic game service will display a pop-up prompting them to complete the process. If the player cancels identity verification, error code [1002000004](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-error-code#section206921217496) is returned.

 |
| 

Anti-addiction for minors

 | 

Check whether a HUAWEI ID that has completed identity verification and is identified as belonging to a minor signs in to the game within the permitted time period.

 | 

In accordance with the latest regulations of the National Press and Publication Administration, all online game enterprises can provide minors with only 1 hour of online gaming services from 20:00 to 21:00 on Fridays, Saturdays, Sundays, and statutory holidays. No online game services can be provided to minors in any form in other time periods.

 | 

-   If a HUAWEI ID that has completed identity verification and is identified as belonging to a minor signs in during the permitted time period, the basic game service displays a pop-up at 21:00, informing the player that their game time has ended. The player will then be forcibly signed out, and error code [1002000006](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-error-code#section4418848101513) will be returned.
-   If a HUAWEI ID that has completed identity verification and is identified as belonging to a minor signs in beyond the permitted time period, the basic game service displays a pop-up, informing the player that they are not allowed to play. The player will then be forcibly signed out, and error code [1002000006](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-error-code#section4418848101513) will be returned.

 |
| 

Payment limits for minors

 | 

Check whether a HUAWEI ID that has completed identity verification and is identified as belonging to a minor is subject to a payment limit.

 | 

In accordance with the latest regulations of the National Press and Publication Administration, online game companies are prohibited from offering paid game services to users under the age of 8. For paid game services provided by the same online game company: users aged 8–15 are limited to a top-up amount of CNY50 per transaction and CNY200 per month in total; users aged 16–17 are limited to a top-up amount of CNY100 per transaction and CNY400 per month in total.

 | 

If a HUAWEI ID that has completed identity verification and is identified as belonging to a minor reaches the in-game payment limit, IAP Kit will display a pop-up, indicating that the spending restriction has been reached.

When a user uses Huawei IAP, Huawei will automatically enforce payment limit controls according to the requirements of the National Press and Publication Administration. No action is required from you in this case.

 |
