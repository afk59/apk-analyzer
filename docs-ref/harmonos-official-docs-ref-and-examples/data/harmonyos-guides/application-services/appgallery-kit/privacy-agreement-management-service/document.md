# Privacy Agreement Management Service

This service provides apps and atomic services that have integrated the standardized privacy statement hosting service with the ability to query privacy agreement URLs, check the privacy agreement signing status, terminate privacy agreements, and launch the standardized privacy agreement pop-up.

#### Use Cases

-   Privacy agreement URL query
    
    This function supports querying or displaying a privacy agreement within your app if your app has integrated the standardized privacy statement hosting service.
    
-   Privacy agreement signing status query
    
    If a user has not signed the privacy agreement, system permission requests will be rejected to avoid repeated, unnecessary requests before user consent. You can check the signing status to plan relevant permissions and obtain data in a compliant manner within your app or atomic service.
    
-   Terminating a privacy agreement
    
    This function is used to terminate a privacy agreement signed by a user. After termination, reopening the app will trigger the standardized privacy agreement pop-up again.
    

-   Launching the standardized privacy agreement pop-up
    
    This function is used for you to proactively launch the standardized privacy agreement pop-up if your app has integrated the standardized privacy statement hosting service.
    

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/szrfKbYjSmywnv8mKU02Ng/en-us_image_0000002371652901.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062059Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D909E662BF9802A97825F9DCC273A5A767C149D21CA6036C5050ECB1DE799100 "Click to enlarge")

## Querying Privacy Agreement URLs

1.  A user requests to query the privacy agreement URL.
2.  The app calls the **getAppPrivacyMgmtInfo** API to query the privacy agreement URL.
3.  The API returns the privacy agreement URL.
4.  The app sends the query result to the user.

## Querying the Privacy Agreement Signing Status

1.  A user requests to query the privacy agreement signing status.
2.  The app or atomic service calls the **getAppPrivacyResult** API to query the privacy agreement signing status.
3.  The API returns the privacy agreement signing status.
4.  The app or atomic service returns the result to the user.

## Terminating the Privacy Agreement

1.  A user requests to terminate the privacy agreement.
2.  The app calls the **disableService** API to terminate the privacy agreement.

## Launching the Standardized Privacy Agreement Pop-up

1.  A user requests to display the standardized privacy agreement pop-up.
2.  The app calls the **requestAppPrivacyConsent** API to launch the standardized privacy agreement pop-up.
3.  The pop-up result is returned.
4.  The standardized privacy agreement pop-up is displayed.

#### Restrictions

-   The [loadContent()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiextensioncontentsession#loadcontent) method cannot be repeatedly called to load pages in the same ability.
-   The app or atomic service needs to integrate the standardized privacy statement hosting service.
-   The privacy agreement management service is supported on phones, tablets, and PCs/2-in-1 devices. Starting from 5.1.1(19), it also supports TVs.
-   You can use the Emulator for Arm and x86 architectures to debug APIs of the privacy agreement management service by manually presetting privacy agreement URLs.

#### API Description

The privacy agreement management service provides the following APIs. For details, please refer to the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-privacymanager).

| 
API

 | 

**Description**

 |
| :-- | :-- |
| 

[getAppPrivacyMgmtInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-privacymanager#section10984155711373)(): [AppPrivacyMgmtInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-privacymanager#section1535385414136)

 | 

Queries the privacy agreement URL.

 |
| 

[getAppPrivacyResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-privacymanager#section887383520415)(): [AppPrivacyResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-privacymanager#section12860134614530)\[\]

 | 

Queries the privacy agreement signing status.

 |
| 

[disableService](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-privacymanager#section16502191111574)():void

 | 

Terminates the privacy agreement.

 |
| 

[requestAppPrivacyConsent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-privacymanager#section36372438116)(context:common.UIAbilityContext):Promise<[ConsentResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-privacymanager#section5439151165618)\>

 | 

Launches the standardized privacy agreement pop-up.

 |

#### Development Procedure

## Querying Privacy Agreement URLs

1.  Import the **privacyManager** module and related common modules.
    
    import { privacyManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Call the [getAppPrivacyMgmtInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-privacymanager#section10984155711373) API to query the privacy agreement URL.
    
    try {
      let appPrivacyManageInfo: privacyManager.AppPrivacyMgmtInfo = privacyManager.getAppPrivacyMgmtInfo();
      hilog.info(0, 'TAG', "Succeeded in getting AppPrivacyManageInfo type: " + appPrivacyManageInfo\["type"\]);
      let privacyLinkInfoArray : privacyManager.AppPrivacyLink\[\] = appPrivacyManageInfo.privacyInfo;
      hilog.info(0, 'TAG', "Succeeded in getting AppPrivacyManageInfo size = " + privacyLinkInfoArray.length);
      for (let i = 0; i < privacyLinkInfoArray.length; i++) {
        hilog.info(0, 'TAG', "Succeeded in getting AppPrivacyManageInfo type = " + privacyLinkInfoArray\[i\]\["type"\] + ", version = " + privacyLinkInfoArray\[i\]\["versionCode"\] + ", url = " + privacyLinkInfoArray\[i\]\["url"\]);
      }
    } catch (error) {
      hilog.error(0, 'TAG', "GetAppPrivacyManageInfoPublic exception code: " + error.code + ", exception message: " + error.message);
    }
    

## Querying the Privacy Agreement Signing Status

1.  Import the **privacyManager** module and related common modules.
    
    import { privacyManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Call the [getAppPrivacyResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-privacymanager#section887383520415) API to query the privacy agreement signing status.
    
    try {
      let appPrivacyResults: privacyManager.AppPrivacyResult\[\] = privacyManager.getAppPrivacyResult();
      hilog.info(0, 'TAG', "Succeeded in getting AppPrivacyResult size = " + appPrivacyResults.length);
      for (let i = 0; i < appPrivacyResults.length; i++) {
        hilog.info(0, 'TAG', "Succeeded in getting AppPrivacyResult type = " + appPrivacyResults\[i\]\["type"\] + ", version = " + appPrivacyResults\[i\]\["versionCode"\] + ", result = "+appPrivacyResults\[i\]\["result"\]);
      }
    } catch (error) {
      hilog.error(0, 'TAG', "GetAppPrivacyResultPublic exception code: " + error.code + ", exception message: " + error.message);
    }
    

## Terminating the Privacy Agreement

1.  Import the **privacyManager** module and related common modules.
    
    import { privacyManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Call the [disableService](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-privacymanager#section16502191111574) API to terminate the privacy agreement.
    
    try {
      privacyManager.disableService();
      hilog.info(0, 'TAG', "Succeeded in disabling Service success.");
    } catch (error) {
      hilog.error(0, 'TAG', "DisableService exception code: " + error.code + ", exception message: " + error.message);
    }
    

## Launching the Standardized Privacy Agreement Pop-up

1.  Import the **privacyManager** module and related common modules.
    
    import { privacyManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import type { common } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call the [requestAppPrivacyConsent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-privacymanager#section36372438116) API to launch the standardized privacy agreement pop-up.
    
    try {
      const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      privacyManager.requestAppPrivacyConsent(uiContext).then((consentResult : privacyManager.ConsentResult) => {
        let appPrivacyResults: privacyManager.AppPrivacyResult\[\] = consentResult\["results"\];
        for (let i = 0; i < appPrivacyResults.length; i++) {
          hilog.info(0, 'TAG', "GetAppPrivacyResult type = " + appPrivacyResults\[i\]\["type"\] + ", version = " + appPrivacyResults\[i\]\["versionCode"\] + ", result = " + appPrivacyResults\[i\]\["result"\] + ", signingTimeStamp = " + appPrivacyResults\[i\]\["signingTimeStamp"\]);
        }
      }).catch((error: BusinessError<Object>) => {
        hilog.error(0, 'TAG', \`requestAppPrivacyConsent failed, Code: ${error.code}, message: ${error.message}\`);
      });
    } catch (error) {
      hilog.error(0, 'TAG', "requestAppPrivacyConsent exception code: " + error.code + ", exception message: " + error.message);
    }
    

#### Common Event Indicating the Privacy Agreement Signing Result

After your app or atomic service integrates the standardized privacy statement hosting service, if a user has not agreed to the privacy agreement, a standardized privacy agreement pop-up will appear when the user launches the app or atomic service.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/GAaQgYcBR_aChTMUMAknTg/en-us_image_0000002371652905.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062059Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F6D365D8792CEB9FFF04826D829D2164010C00349004C3E2B7A1D63B9DC14EA "Click to enlarge")

When the user taps **Agree** in the pop-up, AppGallery will send a common event indicating the privacy agreement pop-up signing result. Your app can listen to this event to obtain the privacy agreement signing result.

## Event Description

| 
Event

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

[COMMON\_EVENT\_PRIVACY\_STATE\_CHANGED](https://developer.huawei.com/consumer/en/doc/harmonyos-references/commoneventmanager-definitions#common_event_privacy_state_changed11)

 | 

usual.event.PRIVACY\_STATE\_CHANGED

 | 

Common event indicating the privacy agreement signing result. The event carries the following data:

{

'resultType': privacyResultType,

'appIndex': appIndex

}

Note:

-   The options of **privacyResultType** are as follows:
    
    **1**: The user has agreed to the privacy agreement for using the full mode.
    
    **0**: The user has not agreed to the privacy agreement.
    
-   **appIndex**: twin index.

 |

The following is an example of receiving a common event (without an app twin):

import { hilog } from '@kit.PerformanceAnalysisKit';
import { commonEventManager } from '@kit.BasicServicesKit';
const TAG = 'PrivacySubscribe';

class PrivacySubscribeSample {
  private readonly eventId = 'usual.event.PRIVACY\_STATE\_CHANGED';
  // Subscriber information. Used to save the created subscriber object for subsequent subscription and unsubscription.
  private subscriber: commonEventManager.CommonEventSubscriber | undefined = undefined;
  // Event list.
  private subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
    events: \[this.eventId\]
  };

  public subscribe(): void {
    hilog.info(0, TAG, "subscribe");
    // Create a subscriber.
    commonEventManager.createSubscriber(this.subscribeInfo).then((commonEventSubscriber) => {
      hilog.info(0, TAG, "createSubscriber");
      this.subscriber = commonEventSubscriber;

      // Subscribe to the common event.
      try {
        commonEventManager.subscribe(this.subscriber, (err, data) => {
          if (err) {
            hilog.error(0, TAG, \`subscribe failed, code is ${err?.code}, message is ${err?.message}\`);
            return;
          }

          let result = JSON.parse(data?.data ?? '{}')?.resultType as number;
          if (result === 1) {
            // The user agrees to the privacy agreement.
          }
        });
      } catch (error) {
        hilog.error(0, TAG, "init createSubscriber failed, exception code: " + error.code + ", exception message: " + error.message);
      }
    });
  }
}

The following is an example of receiving a common event (with an app twin):

import { hilog } from '@kit.PerformanceAnalysisKit';
import { commonEventManager } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';

const TAG = 'PrivacyEventSubscriber';

export default class MyAbility extends UIAbility {
  onBackground() {
    let appCloneIndex = 0;
    let applicationContext = this.context.getApplicationContext();
    try {
      appCloneIndex = applicationContext.getCurrentAppCloneIndex();
    } catch (error) {
      hilog.error(0, TAG, \`getCurrentAppCloneIndex fail, exception code:\` + error.code + \`, exception message: \` + error.message);
    }
    new PrivacyEventSubscriber(appCloneIndex).subscribe();
  }
}

class PrivacyEventSubscriber {
  private appCloneIndex: number = 0;
  private readonly eventId = 'usual.event.PRIVACY\_STATE\_CHANGED';
  // Subscriber information. Used to save the created subscriber object for subsequent subscription and unsubscription.
  private subscriber: commonEventManager.CommonEventSubscriber | undefined = undefined;
  // Event list.
  private subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
    events: \[this.eventId\]
  };

  constructor(appCloneIndex: number) {
    this.appCloneIndex = appCloneIndex;
  }

  public subscribe(): void {
    hilog.info(0, TAG, "subscribe");
    // Create a subscriber.
    commonEventManager.createSubscriber(this.subscribeInfo).then((commonEventSubscriber) => {
      hilog.info(0, TAG, "createSubscriber");
      this.subscriber = commonEventSubscriber;

      // Subscribe to the common event.
      try {
        commonEventManager.subscribe(this.subscriber, (err, data) => {
          if (err) {
            hilog.error(0, TAG, \`subscribe failed, code is ${err?.code}, message is ${err?.message}\`);
            return;
          }

          let result = JSON.parse(data?.data ?? '{}')?.resultType as number;
          let appIndex = JSON.parse(data?.data ?? '{}')?.appIndex as number ?? 0;
          // The twin index passed by the common event is the same as the twin index of the current app.
          if (appIndex === this.appCloneIndex) {
            if (result === 1) {
              // The user agrees to the privacy agreement.
            }
          }
        });
      } catch (error) {
        hilog.error(0, TAG, "init createSubscriber failed, exception code: " + error.code + ", exception message: " + error.message);
      }
    });
  }
}

#### Integrating the Privacy Agreement Management Service into an Unreleased App

For apps that are not yet available on AppGallery, you can manually preset privacy agreement URLs to simulate the integration of the privacy agreement hosting and management services.

Once this information is set up, a privacy agreement pop-up will be displayed when a user opens your app. Your app can then use the functions provided by the privacy agreement management service, such as querying privacy agreement URLs, checking the privacy agreement signing status, and terminating privacy agreements.

1.  Change the build mode of the app project to [debug](../../../building-an-app/customizing-your-build/customizing-build-options/examples/document.md#section390311716277).
2.  Open the module whose **type** is **entry** in the code project, modify the **src/main/module.json5** file, and add the **module.metadata** information, which contains the following three fields with values of the string type:
    
    | 
    Field
    
     | 
    
    Description
    
     | 
    
    Mandatory
    
     |
    | :-- | :-- | :-- |
    | 
    
    appgallery\_privacy\_hosted
    
     | 
    
    Indicates whether to enable the privacy agreement pop-up. **1** indicates yes, while other values indicate no.
    
     | 
    
    Yes
    
     |
    | 
    
    appgallery\_privacy\_link\_privacy\_statement
    
     | 
    
    Privacy statement URL (HTTPS). A link specified by this URL will be displayed in the pop-up.
    
     | 
    
    Yes
    
     |
    | 
    
    appgallery\_privacy\_link\_user\_agreement
    
     | 
    
    User agreement URL (HTTPS). A link specified by this URL will be displayed in the pop-up.
    
     | 
    
    No
    
     |
    | 
    
    appgallery\_privacy\_link\_user\_agreements
    
     | 
    
    URLs of multiple user agreements (HTTPS). Links specified by these URLs will be displayed in the pop-up.
    
    The value directly references a JSON file which is stored in the **resources/rawfile** folder of the module whose type is **entry**.
    
    When there are multiple user agreement URLs, the **appgallery\_privacy\_link\_user\_agreements** field takes precedence, and the single user agreement URL configured through **appgallery\_privacy\_link\_user\_agreement** will become invalid.
    
    NOTE:
    
    **Start version**: 5.0.2(14)
    
    
    
    
    
     | 
    
    No
    
     |
    

When AppGallery is functioning properly and the network is connected, you can run the **hdc** command to install your app from a local file. Then you can test the privacy agreement pop-up and debug the privacy management service APIs using the preset privacy URLs.

The sample code is as follows:

// module.json5
{
  "module": {
    "name": "entry",
    "type": "entry",
    "description": "$string:module\_desc",
    "metadata": \[
      {
        "name": "appgallery\_privacy\_hosted",
        "value": "1"
      },
      {
        "name": "appgallery\_privacy\_link\_privacy\_statement",
        "value": "https://www.example.com/" // Must be an HTTPS URL.
      },
      {
        "name": "appgallery\_privacy\_link\_user\_agreement",
        "value": "https://www.example.com/" // Must be an HTTPS URL.
      },
      {
        "name": "appgallery\_privacy\_link\_user\_agreements",
        "value": "link\_user\_agreements.json" // Name of the JSON configuration file. For details, see the following example.
      }
    \],
    // Other content.
  }
}

The sample code in the **link\_user\_agreements.json** file is as follows:

{
    "user\_agreement\_Infos": \[
        {
            "name": "User agreement 1",       // Name of user agreement 1 to be displayed.
            "url": "https://xxxx"     // User agreement URL.
        },
        {
            "name": "User agreement 2",       // Name of user agreement 2 to be displayed.
            "url": "https://xxxx"     // User agreement URL.
        }
    \]
}
