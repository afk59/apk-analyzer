# Integration Solution

#### Solution Overview

The location-based recommendation capability enables you your app or atomic service to share location data and related recommendation content via the cloud. Together with real-time locations, device statuses, and behavioral tags, the system makes smart decisions to deliver content through Celia Suggestions, better meeting user needs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/TXR-oGG5QIumQnU1krMqfw/en-us_image_0000002402121921.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062127Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC73535C8BAE2178B59E9C2CE278A3B3AFDD756E60530DED073551EA7BD376DE "Click to enlarge")

#### Requesting the Proximity-based Service Permission

The proximity-based service is a core capability in Huawei's hardware-software synergy solution. It enables merchants to reach more HarmonyOS users and deliver highly targeted, high-quality services.

#### Intent Declaration

Take the travel tips search feature as an example. You need to register the **ViewTravelGuides** intent first.

Edit the **insight\_intent.json** file to declare the intent. The **insight\_intent.json** file must be placed in the **src/main/resources/base/profile/insight\_intent.json** directory of any module. Only one **insight\_intent.json** file can exist in the entire project.

{
  // List of intents supported by your app.
  // Declare the mandatory intents contained in the plugin supported by your app. Your declaration will be verified during app release.
  "insightIntents": \[
    {
      // Intent name.
      // The name must comply with the Intents Kit specifications. Currently, only preconfigured intents for specific vertical domains are supported, while custom intents are not allowed.
      // Each intent name must be unique in an app.
      "intentName": "ViewTravelGuides",
      // Vertical domain to which the intent belongs.
      "domain": "TravelDomain",
      // Intent version number.
      // When a plugin references an intent, the intent version number will be verified. The intent can be called only when the version number is the same as that defined by the plugin.
      "intentVersion": "1.0.1",
      // Entry to the intent call logic.
      "srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
      "uiAbility": {
        // Ability that the intent belongs to.
        "ability": "EntryAbility",
        // **UIAbility** supports two execution modes: foreground and background.
        "executeMode": \[
          "background",
          "foreground"
        \]
      }
    }
  \]
}

#### Device-Side Foreground Intent Call

Implement **InsightIntentExecutor** yourself, and in the corresponding callback, implement the capability to open the landing page (for example, the travel tips page displayed after a user taps a recommendation widget).

The procedure is as follows:

1.  Extend **InsightIntentExecutor**.
2.  Override the corresponding method. For example, to open a foreground page, override the **onExecuteInUIAbilityForegroundMode** method.
3.  Identify the intent via its name (for example, **ViewTravelGuides**), pass the intent parameters (**param**) to the corresponding method, and open the corresponding landing page (for example, the travel tips page displayed after a user taps a recommendation widget).

import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
/\*\*
 \* Intent call example. \*/
export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
  private static readonly VIEW\_TRAVEL\_GUIDES = 'ViewTravelGuides';
  /\*\*
   \* Override the method to execute the intent in the foreground **UIAbility**.
   \*
   \* @param name Intent name.
   \* @param param Intent parameters.
   \* @param pageLoader Window.
   \* @returns Intent call result.
   \*/
  onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage):
    Promise<insightIntent.ExecuteResult> {
    // Dispatch processing logic based on the intent name. You can implement page redirection as needed.
    switch (name) {
      case InsightIntentExecutorImpl.VIEW\_TRAVEL\_GUIDES:
        return this.viewTravelGuides(param, pageLoader);
      default:
        break;
    }
    return Promise.resolve({
      code: -1,
      result: {
        message: 'unknown intent'
      }
    } as insightIntent.ExecuteResult)
  }
  /\*\*
   \* Implement the function of viewing travel tips.
   \*
   \* @param param Intent parameters.
   \* @param pageLoader Window.
   \*/
  private viewTravelGuides(param: Record<string, Object>, pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
    return new Promise((resolve, reject) => {
      // TODO Implement an intent call. The input parameter of **loadContent** is the path to the landing page for viewing travel tips, for example, **pages/TravelGuidePage**.
      pageLoader.loadContent('pages/TravelGuidePage')
        .then(() => {
          let entityId: string = (param.items as Array<object>)?.\[0\]?.\['entityId'\];
          // TODO If the intent is successfully called, log content will be displayed here.
          resolve({
            code: 0,
            result: {
              message: 'Intent execute succeed'
            }
          });
        })
        .catch((err: BusinessError) => {
          // TODO Handle the failure if the intent fails to be called.
          resolve({
            code: -1,
            result: {
              message: 'Intent execute failed'
            }
          })
        });
    })
  }
}
