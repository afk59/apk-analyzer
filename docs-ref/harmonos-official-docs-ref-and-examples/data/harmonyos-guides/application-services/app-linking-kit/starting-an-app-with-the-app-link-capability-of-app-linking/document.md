# Starting an App with the App Link Capability of App Linking

#### Use Case

With the app link capability of App Linking, the system directs users to specific content in the target app based on the passed URI (HTTPS link). Unlike Deep Linking, App Linking allows users to smoothly access the content regardless of whether they have installed the target app.

For example, once you have integrated the scan-to-access service by using the app link capability of App Linking, users can scan the QR code or barcode of your app through system-level scanning entry points such as the scan button on the control panel. This takes them directly to the corresponding service page of your app, providing a seamless, one-step experience.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/64EqE4PTTi2VcX8jUU55gw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1A21B164013FC4BE1D9F24F505160615C153E7C9F438A9FBCFC51D229B94873)

This capability applies only to HarmonyOS apps with API version 12 or later. If you are developing an atomic service, please refer to [Using App Linking for Atomic Service Redirection](https://developer.huawei.com/consumer/en/doc/atomic-guides/atomic-applinking).

#### Mechanism

-   App Linking adopts domain name verification, which is unavailable in Deep Linking. This helps identify valid apps, making links more secure and reliable.
-   App Linking ensures that an HTTPS address can be used to access both the in-app content and its web version. If the app is installed, the app is preferentially opened to present the content. If the app is not installed, a web page is opened to present the content in a browser.

#### Restrictions

Phones, PCs/2-in-1 devices, and tablets are supported. In 5.1.1(19) and later versions, this service is also available on TVs.

#### Prerequisites

You have [enabled App Linking](../getting-started/enabling-app-linking/document.md).

#### Development Process

| 
Party

 | 

Procedure

 |
| :-- | :-- |
| 

Target app

 | 

Cloud-side development

 | 

[Enable App Linking](../getting-started/enabling-app-linking/document.md).

 |
| 

Cloud-side development

 | 

[Associate your app on your website](#en-us_topic_0000002415444457_section6903241628).

 |
| 

Cloud-side development

 | 

[Create an associated website domain name for your app in AppGallery Connect](#en-us_topic_0000002415444457_section1101111611317).

 |
| 

App-side development

 | 

[Configure the associated website domain name in the module.json5 file](#en-us_topic_0000002415444457_section13808113610362).

 |
| 

App-side development

 | 

[Process the passed link](#en-us_topic_0000002415444457_section1620481746).

 |
| 

Front-end development

 | 

Develop the HTML5 web page corresponding to the passed link. If the app is not installed, this web page will be displayed when the link is tapped.

NOTE:

This document focuses on the development of HarmonyOS apps and will not detail web page development.

 |
| 

Caller app

 | 

App-side development

 | 

Open the target app through the [UIAbilityContext.openLink() API](#en-us_topic_0000002415444457_section15392826124511) or [system browser/ArkWeb](#en-us_topic_0000002415444457_section3736124874513).

 |

#### Configuring the App Link Capability for the Target App

## Associating Your App on Your Website

Perform the following operations on the domain name server (DNS) of your website. When you [create an associated website domain name for your app in AppGallery Connect](#en-us_topic_0000002415444457_section1101111611317), AppGallery Connect will use the following file to identify apps belonging to the domain name, making the links more secure and reliable.

1.  Create the domain name configuration file **applinking.json**. The file content is as follows:
    
    {
     "applinking": {
       "apps": \[
         {
           "appIdentifier": "_1234567_"
         }
       \]
     }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/1DGxoG3dRZGYxAzmjzZ_8Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E012E7F74C74BB44339DAC79B4FB9A3EA518F03DED945F9C9599453830023FC8)
    
    -   **appIdentifier** is the app ID generated during app creation. For details about how to obtain the app ID, please refer to [Viewing App Information](https://developer.huawei.com/consumer/en/doc/app/agc-help-view-app-info-0000002282674569).
    -   A domain name can be associated with multiple apps if you add multiple **appIdentifier** elements to the **apps** list. Each **appIdentifier** element corresponds to an app.
    
2.  Place the **applinking.json** configuration file in the following directory on the DNS: **https://**_domain.name_**/.well-known/applinking.json**.
    
    For example, if the domain name of your server is **www.example.com**, place the **applinking.json** file in the following directory:
    
    **https://www.example.com/.well-known/applinking.json**
    

## Creating an Associated Website Domain Name for Your App in AppGallery Connect

To use the app link capability of HarmonyOS, you need to create an associated website domain name for your HarmonyOS app. If a user has your HarmonyOS app installed, tapping a link under your domain name will automatically open the relevant page in the app.

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Development and services**.
2.  Click the project to which your HarmonyOS app belongs.
3.  In the navigation tree on the left, choose **Grow** > **App Linking**, click the **App links (applicable to API 12 or later)** tab, and click **New**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/WHbQPUD-TIqmKcBWHHi8VA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F56C636958F76CF03D25FFFAF5DF3665A43E190B88645036613C01B068A7D1F0)
    
    -   Since you are developing a HarmonyOS app, you only need to pay attention to the **App links (applicable to API 12 or later)** tab. Other tabs are applicable to other systems.
    -   If the **App links (applicable to API 12 or later)** tab is not displayed, click **Custom configuration** on the right and select the tab.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/w_lJ6QeWTyGVa5X-38xKLw/en-us_image_0000002453978601.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7165FC4CF769440FC4EC048C6B7898932B10D0849D0EE0DE6EA81A49572C10D7)
    
4.  Enter the domain name of [your website with which the app is associated](#en-us_topic_0000002415444457_section6903241628), for example, **https://www.example.com**. An exact domain name without special characters shall be used.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/8uTmqOKGTLaY9yb-BMFW6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=944A3FB1246D2738FEE3190ADC9A6EC2A8EB9EAED0BFCE1C67818742E6E4C2AC)
    
    Do not add a slash (/) to the end of the domain name. For example, **https://www.example.com/** is not supported.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/1ErK9zBoSVCqE5iVBQFlJA/en-us_image_0000002505731392.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B95268BAA239FEC03B62FE82487CE1A744A029DCC891552FE00A8FABEF9529AA)
    
5.  After the setting is complete, click **Release**. AppGallery Connect will check whether the apps contained in the configuration file of the website domain name overlap with the apps in the project.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/wN1O-U5pTcSUlj9uJA9RPw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E064741104E33218A9FA6F28DA7704C2773573EC43D287DCCC63B48312EB2DD6)
    
    After an app link is released, AppGallery Connect will obtain the configuration file from the DNS every 24 hours and check whether the file contains any apps in the project.
    
    For example, if you create an app link at 17:21 on April 7, AppGallery Connect may obtain the new configuration file from the DNS at 17:30 on April 8, check whether the file contains any apps in the project, and update the release status.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/Y_qv0V2zSNWPj_aPjQSg7A/en-us_image_0000002537651141.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4BBE6EBE33900BF337C2CFE9CC8E4373B42EF8EF5212D6983C5F163D2D39F03)
    
    -   If the configuration file of the domain name contains any app in the project, the release is successful. You can click **View** to view the information about the apps associated with the domain name.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/9OQMxV9lRxO5GEH2AMvn0Q/en-us_image_0000002420532798.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DAB1FE8B0B46F409BF7546E9AA3A7F1915A5E62B54F3C51962D1210401DBCA5F)
        
    -   If the verification is in progress, the status is **Publishing**.
    -   If the configuration file does not contain any app in the project, the release fails. You can click **View** to check the release failure cause.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/-potdy-aS7eL5E7oh_DIxA/en-us_image_0000002454091917.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB2201F20183CE37DD7512CC40F4CF65B45EDCE3B58E954A7E944500E4DC960B)
        
    

## Configuring the Associated Domain Name in the module.json5 File

Configure the following information in the [module.json5 file](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) of your app to declare the domain name associated with the app and enable domain name verification.

-   The **entities** list must contain **entity.system.browsable**.
-   The **actions** list must contain **ohos.want.action.viewData**.
-   The **uris** list must contain an element whose **scheme** is **https** and **host** is the associated domain name. The optional attributes include **path**, **pathStartWith**, and **pathRegex**. For details, please refer to [Description of uris](../../../application-framework/ability-kit/stage-model-development/inter-application-redirection/starting-a-specified-application/application-link-description/document.md#description-of-uris).
-   **domainVerify** must be set to **true**, indicating that domain name verification is enabled.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/Xq1fFz4dSQqlVO9tpyTNnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C415CA21243DF71E8BB9502D11D633967987F869BA7BE0000E77AB00A41052A7)

By default, the **skills** section contains a **skill** object, which is used to mark the app entry. The app redirection link cannot be configured in the **skill** object. Instead, you need to create an independent **skill** object.

If multiple redirection scenarios are involved, create different **skill** objects in the **skills** section. Otherwise, the configuration cannot take effect.

For example, the configuration below declares that the app is associated with the domain name **www.example.com**.

{
  "module": {
    "abilities": \[
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "icon": "$media:icon",
        "label": "$string:EntryAbility\_label",
        // Set **exported** to **true**. If **exported** is set to **false**, only authorized system apps can start the target app.
        "exported": true,
        "startWindowIcon": "$media:icon",
        "startWindowBackground": "$color:start\_window\_background",
        "skills": \[
          {
            "entities": \[
              "entity.system.home"
            \],
            "actions": \[
              // Since version 5.1.1(19), **actions** must be set to **ohos.want.action.home**. For version 5.1.0(18) and earlier, **actions** should be set to **action.system.home**.
              "ohos.want.action.home"
            \]
          },
          {
            "entities": \[
              // **entities** must contain **entity.system.browsable**.
              "entity.system.browsable"
            \],
            "actions": \[
              // **actions** must contain **ohos.want.action.viewData**.
              "ohos.want.action.viewData"
            \],
            "uris": \[
              {
                // **scheme** must be set to **https**.
                "scheme": "https",
                // **host** must be set to the associated domain name.
                "host": "www.example.com",
                // **path** is optional, which indicates the directory on the DNS, such as **path1** in **www.example.com/path1**.
                // If the app supports only specific paths, provide those paths here to prevent unsupported paths from triggering the app.
                "path": "path1"
              }
            \],
            // **domainVerify** must be set to **true**.
           "domainVerify": true
          }
          // If other redirection capabilities are involved, such as push message– and NFC-based redirection, add a **skill** object to prevent conflicts with App Linking.
        \]
      }
    \]
  }
}

## Processing the Passed Link

Add the following code to the **onCreate()** or **onNewWant()** lifecycle callback of the app's ability (for example, **EntryAbility**) to process the passed link.

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { url } from '@kit.ArkTS';
export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // Obtain the passed link information from **want**.
    // For example, the passed URL is **https://www.example.com/programs?action=showall**.
    let uri = want?.uri;
    if (uri) {
      // Parse the **query** parameter from the link. You can perform subsequent processing based on your service requirements.
      try {
        let urlObject = url.URL.parseURL(want?.uri);
        let action = urlObject.params.get('action');
        // For example, if **action** is set to **showall**, all programs are displayed.
        if (action === "showall"){
          // ...
        }
        // ...
      } catch (error) {
        hilog.error(0x0000, 'testTag', \`Failed to parse url.\`);
      }
    }
  }
}

To start a specified **UIAbility** page component based on link parameters, please refer to [Starting a Specified Page of UIAbility](../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/starting-uiability-within-the-same-application/document.md#starting-a-specified-page-of-uiability).

## Verifying the App Startup Effect

1.  [Manually sign](../../../coding-and-debugging/configuring-a-debug-signature/document.md#section297715173233) your app.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/_RA2Pv-dSUGLfYM1hY04Xg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FF89A10A9A033700988B4F63460EA525B4CFA40ECBE671560FCBAE0FEAC3461)
    
    Do not use the automatic signing function of DevEco Studio. Otherwise, the app cannot be started.
    
2.  Compile, package, and install the app on the debugging device.
3.  Use the app link capability of App Linking to start the app from the caller app. For details, please refer to [Implementing App Redirection from the Caller App](#en-us_topic_0000002415444457_section93961521541).

#### Implementing App Redirection from the Caller App

## Starting the App by Calling the UIAbilityContext.openLink() API

The caller app passes the link of the target app through the [UIAbilityContext.openLink()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#openlink12) API to start the target app.

The **UIAbilityContext.openLink()** API provides two methods for starting the target app.

-   Method 1: Open the app only in App Linking mode.
    
    In this method, **appLinkingOnly** is set to **true**. If an app is matched, that app is directly opened. If no app matches, an exception is thrown.
    
    This method applies to scenarios where you have implemented exception handling for target app launch failure. For example, if the caller app integrates ArkWeb, the link can be opened through ArkWeb if the target app is unavailable.
    
-   Method 2: Preferentially open the app in App Linking mode.
    
    In this method, **appLinkingOnly** is set to **false** or not set. If an app is matched, that app is directly opened. If no app matches, the system attempts to access the app content in a browser.
    
    This method applies to scenarios where you have not implemented exception handling for target app launch failure. If the target app is unavailable, the link is opened through the system browser.
    

This section describes method 1, in order to check whether the App Linking configuration is correct. The following is an example.

1.  Add the **GlobalContext.ets** file to the **entry/src/main/ets/common** directory to initialize and obtain the app context.
    
    import { common } from '@kit.AbilityKit';
    
    export class GlobalContext {
      private static context: common.UIAbilityContext;
    
      public static initContext(context: common.UIAbilityContext): void {
        GlobalContext.context = context;
      }
    
      public static getContext(): common.UIAbilityContext {
        return GlobalContext.context;
      }
    }
    
2.  Import **GlobalContext** to the **entry/src/main/ets/entryability/EntryAbility.ets** file and use **GlobalContext.initContext(this.context)** in the **onCreate** method to initialize the global app context.
3.  In the **entry/src/main/ets/pages/Index.ets** file, call the [UIAbilityContext.openLink()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#openlink12) API to open the app.
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { GlobalContext } from '../common/GlobalContext';
    
    @Entry
    @Component
    struct Index {
      build() {
        Button('start link', { type: ButtonType.Capsule, stateEffect: true })
          .width('87%')
          .height('5%')
          .margin({ bottom: '12vp' })
          .onClick(() => {
            let context = GlobalContext.getContext();
            let link: string = "https://www.example.com/programs?action=showall";
            // Open the app only in App Linking mode.
            context.openLink(link, { appLinkingOnly: true })
              .then(() => {
                hilog.info(0x0000, 'testTag', \`Succeeded in opening link.\`);
              })
              .catch((error: BusinessError) => {
                hilog.error(0x0000, 'testTag', \`Failed to open link, code: ${error.code}, message: ${error.message}\`);
              })
          })
      }
    }
    

## Starting the App Through the System Browser or ArkWeb

ArkWeb deeply integrates App Linking. When a user taps a link in the system browser or on an embedded web page in an app that integrates ArkWeb, the system preferentially starts the target matched app through App Linking, and displays the corresponding content in the app. However, there are certain restrictions:

1.  If the domain name of the web page that the user browses is the same as that of the link tapped, the system will open the link in the system browser or the ArkWeb component to maintain a consistent browsing experience.
2.  If the domain name of the web page is different from that of the link (for example, one is **example.com** while the other is **app.example.com**), the system will preferentially start the target app using App Linking and display the corresponding content in the app.

#### FAQs

## What should I do if the value of **skills** in the **module.json5** file of the app is incorrect?

Check whether the domain name of the app in the **host** field is the same as that created in AppGallery Connect.

## What should I do if the server of my website is incorrectly configured?

Follow the instructions below:

1.  Check the JSON configuration file of the server and ensure that the value of **appIdentifier** is correct.
2.  Check whether the **applinking.json** file is stored in the correct directory (**.well-known**). Use a browser or other ways to access the JSON file at **https://_your.domain.name_/.well-known/applinking.json** and ensure that the file is accessible.

## What should I do if the system has not completed domain name verification?

Follow the instructions below:

1.  After installing the app on the device, wait at least 20 seconds to ensure that the system completes domain name verification.
2.  If the network is disconnected or weak, the domain name verification may fail, and the system will verify the domain name again within 24 hours.

## How do I check whether domain name verification is successful?

To view the app domain name verification result, click **Terminal** in DevEco Studio and run the following command to query the result:

**hdc shell hidumper -s AppDomainVerifyManager**

If the verification is successful, you will see the **success** message like the output below.

BundleName:
  appIdentifier:123456789
   domain verify status:
    https://www.example.com:success

-   If the **client-error** message is displayed, troubleshoot as follows:
    1.  Check whether the value of **appIdentifier** in the returned message is the same as the app ID in AppGallery Connect.
    2.  Check whether the domain name configured in AppGallery Connect is successfully released.
-   If the **http\_unknown** message is displayed, make sure that the device has access to the Internet, and reinstall the app.
-   If other messages are displayed, seek [technical support](https://developer.huawei.com/consumer/en/support/feedback/#/).

## What should I do if I cannot use App Linking to open a pre-installed app when I start my device for the first time?

The system verifies the domain name of a pre-installed app within 20 minutes after the device is started for the first time. If the device cannot access the Internet in this period, the domain name verification may fail. In this case, restart your device or try again after 24 hours. The system will verify the domain name of the pre-installed app again after you restart the device or after 24 hours.

## What should I do if the content is not updated in a timely manner when I access the content delivery network (CDN)?

The CDN cache duration is 10 minutes. Wait for a while and access the CDN again.

## How are apps and domain names mapped?

They are in a many-to-many relationship. An app can be associated with multiple domain names, and a domain name can be associated with multiple apps.

## If a domain name is associated with multiple apps, which app will be started by the domain name?

You can configure the **applinking.json** file to associate a domain name with multiple apps. If the **uris** field in the **module.json5** file of each app is set to the same value, the system displays a pop-up for users to select the app to start. You can also use the **path** field to distinguish the apps to start. For example, use **https://www.example.com/path1** to start target app 1 and use **https://www.example.com/path2** to start target app 2.

## What should I do if an error message indicating that the download source **JSON** file is denied and the security policy needs to be verified is displayed during app link configuration based on App Linking?

The domain name configuration file should be placed in the designated directory on the DNS:

**https://**_domain.name_**/.well-known/applinking.json**

For example, if the domain name of your server is **www.example.com**, place the **applinking.json** file in the following directory:

**https://www.example.com/.well-known/applinking.json**
