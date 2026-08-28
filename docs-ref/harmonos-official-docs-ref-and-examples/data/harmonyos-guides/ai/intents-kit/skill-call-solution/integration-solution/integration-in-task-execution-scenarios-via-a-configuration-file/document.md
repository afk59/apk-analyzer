# Integration in Task Execution Scenarios via a Configuration File

#### Solution Overview

You need to register intents and implement intent calls based on their definitions. When users interact with Celia Chat using natural language input, Celia Chat interprets the semantics, converts them into intent calls (including intent parameters), and executes them to provide an interactive experience.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/Sa1mJlU9RD6rTcuwMH-gig/en-us_image_0000002368482180.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062127Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7CD0EC43E215FEAE3EE300955A088CA77BC335176890B19CC44753B0CFFD45A "Click to enlarge")

#### Intent Declaration

Take the travel tips search feature as an example. You need to register the **ViewTravelGuides** intent first.

Edit the **insight\_intent.json** file to register the intent. The **insight\_intent.json** file must be placed in the **src/main/resources/base/profile/insight\_intent.json** directory of any module. Only one **insight\_intent.json** file can exist in the entire project.

{
  // List of intents supported by your app.
  // Declare the mandatory intents contained in the plugin supported by your app. Your declaration will be verified during app release.
  "insightIntents": \[
    {
      // Intent name.
      // The name must comply with the Intents Kit specifications. Currently, only preconfigured intents for specific vertical domains are supported, while custom intents are not allowed.
      // Each intent name must be unique in an app.
      "intentName": "ViewTravelGuides",
      // Vertical domain to which an intent belongs.
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
      },
 "uiExtension": {// Declaration required when a windowed UI is provided for intent execution.
        "ability": "insightIntentUIExtensionAbility",// Name of the ability where the API that calls the intent is located.
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
              message: 'Intent execute success'
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

#### Device-Side Foreground Intent Call with a Windowed UI

Implement **InsightIntentExecutor** yourself, and in the corresponding callback, implement the capability to load content for display on the windowed UI.

The procedure is as follows:

1.  Extend **InsightIntentExecutor**.
2.  Override the corresponding method. For example, to open a foreground windowed UI, override the **onExecuteInUIExtensionAbility** method.
3.  Identify the intent via its name (**LoadBluetoothCard**), call the extension intent, pass the intent parameters (**param**) to the relevant method, and open the corresponding windowed UI (such as the Bluetooth windowed UI).

import { insightIntent, InsightIntentExecutor, UIExtensionContentSession } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
/\*\*
 \* Intent call example. \*/
export default class IntentExecutorImpl extends InsightIntentExecutor {
  private static readonly TAG: string = 'IntentExecutorImpl';
  private static readonly LOAD\_BLUETOOTH\_CARD: string = 'LoadBluetoothCard';
  /\*\*
   \* Override the method to execute the foreground UI extension intent.
   \*
   \* @param name Intent name.
   \* @param param Intent parameters.
   \* @param pageLoader Window.
   \* @returns Intent call result.
   \*/
  async onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>,
    pageLoader: UIExtensionContentSession):
    Promise<insightIntent.ExecuteResult> {
    console.info(IntentExecutorImpl.TAG, \`onExecuteInUIExtensionAbility\`);
    switch (name) {
      case IntentExecutorImpl.LOAD\_BLUETOOTH\_CARD:
        console.info(IntentExecutorImpl.TAG, \`onExecuteInUIAbilityForegroundMode::ForegroundUiAbility intent\`);
        return this.openLoadBluetoothCard(pageLoader);
      default:
        console.info(IntentExecutorImpl.TAG, \`onExecuteInUIAbilityForegroundMode::invalid intent\`);
        break;
    }
    let result: insightIntent.ExecuteResult = {
      code: -1,
      result: {
        message: 'onExecuteInUIExtensionAbility failed'
      }
    };
    return result;
  }
  /\*\*
   \* Execute the **LoadBluetoothCard** intent.
   \*
   \* @param pageLoader Session object for content loading.
   \* @returns Execution result.
   \*/
  private async openLoadBluetoothCard(pageLoader: UIExtensionContentSession): Promise<insightIntent.ExecuteResult> {
    pageLoader.loadContent('pages/UiExtensionPage');
    let result: insightIntent.ExecuteResult = {
      code: 0,
      result: {
        message: 'intent execute success'
      }
    }
    return result;
  }
}
