# Integration Solution

#### Solution Overview

If you want to notify a user of an event, you can push the event content to the smart distribution platform via the cloud server of your app or atomic service. This process is known as intent sharing. The system uses smart decision making to determine the conditions for triggering a notification. When these conditions are met, an event notification widget is displayed to the user. Upon tapping the widget, the user is redirected to the app or atomic service details page to view the event details. This process is known as intent call.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/RH1hyLL7R02zVq3Qfw6UAg/en-us_image_0000002368482196.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062126Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E27B9FD21F0298555032CAAE6837751ABAC708DA1529A97511FC26A77A0F9DDE "Click to enlarge")

#### Flowchart

1.  Obtain the Service OpenID (SID) required for sharing a cloud-side event.

2.  After a user event occurs, your cloud will synchronize the event content and SID to the Intents Kit cloud.
3.  Huawei will determine the rules and time for pushing event-related notifications based on the event and scenario.
4.  The event-related notification is displayed to the user, enhancing impressions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/oh49qM0eSDaEzEo4rsSTBQ/en-us_image_0000002402121937.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062126Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42A721D5185306EB27AE23947690EC378D10E3ABCF2EDB87AB8636BB01DFB7FD "Click to enlarge")

#### Registering an Intent

Take the repayment reminder feature as an example. You need to register the **ViewRepayment** intent.

Edit the **insight\_intent.json** file to declare the intent. The **insight\_intent.json** file must be placed in the **src/main/resources/base/profile/insight\_intent.json** directory of any module. Only one **insight\_intent.json** file can exist in the entire project.

{
  // List of intents supported by your app.
  // Declare the mandatory intents contained in the plugin supported by your app. Your declaration will be verified during app release.
  "insightIntents": \[
    {
      // Intent name.
      // The name must comply with the Intents Kit specifications. Currently, only preconfigured intents for specific vertical domains are supported, while custom intents are not allowed.
      // Each intent name must be unique in an app.
      "intentName": "ViewRepayment",
      // Vertical domain to which the intent belongs.
      "domain": "BankingDomain",
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

#### Obtaining the SID

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/FWDO_tAhTneG7bYasD4VeQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062126Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=039C6A7188B205515659B6D4152CF0E642AFB04A5E55A6CC0F8AE0990654963F)

For details, please refer to [getSid](https://developer.huawei.com/consumer/en/doc/harmonyos-references/intents-arkts-api-insightintent#section76701233209) in the Intents Kit API reference.

The cloud-side event sharing credential SID is preferentially obtained from the cache. If it fails to be obtained from the cache, a new SID can be forcibly obtained from the cloud.

import { insightIntent } from '@kit.IntentsKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Pass a proper context based on the code context.
insightIntent.getSid(context, false) // Preferentially obtain the cached SID. If this parameter is set to **true**, a new SID will be forcibly obtained from the cloud.
  .then((sid: string) => {
  // The SID is successfully obtained.
    console.info('getSid succeed!');
  }).catch((error: BusinessError) => {
  // Failed to obtain the SID.
  console.error(\`getSid failed! error=${error.code} reason=${error.message}\`);
});

#### Sharing a Cloud-Side Intent

## Calling the Intent Sharing API

The app or atomic service shares the intent-related event data with Intents Kit through the [cloud-side intent sharing API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/intents-rest-api-intent-share#section105321034437) to enable event-based notifications.

## Calling the Event Revoking API

When the intent-related event data shared by the app or atomic service expires, Intents Kit needs to revoke the event data through the [cloud-side event revoking API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/intents-rest-api-revoke-event) to avoid triggering notifications that exceed the validity period.

#### Calling a Device-Side Intent

Implement **InsightIntentExecutor** yourself, and in the corresponding callback, implement the capability to open the landing page (the page displayed after users tap the recommendation widget).

The procedure is as follows:

1.  Extend **InsightIntentExecutor**.
2.  Override the corresponding method. For example, to open a foreground page, override the **onExecuteInUIAbilityForegroundMode** method.
3.  Identify the **ViewRepayment** intent based on the intent name.
4.  Pass the intent parameters (**param**) to the corresponding method and open the corresponding landing page (for example, the repayment page).
    
    import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
    import { window } from '@kit.ArkUI';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    /\*\*
     \* Intent call example. \*/
    export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
      private static readonly VIEW\_REPAYMENT = 'ViewRepayment';
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
          case InsightIntentExecutorImpl.VIEW\_REPAYMENT:
            return this.viewRepayment(param, pageLoader);
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
       \* Implement the repayment query function.
       \*
       \* @param param Intent parameters.
       \* @param pageLoader Window.
       \*/
      private viewRepayment(param: Record<string, Object>, pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
        return new Promise((resolve, reject) => {
          let para: Record<string, string> = {
            'result': JSON.stringify(param)
          };
          let localStorage: LocalStorage = new LocalStorage(para);
          // TODO Implement intent calls. The input parameter of **loadContent** is the path to the landing page for viewing repayment information, for example, **pages/Index**.
          pageLoader.loadContent('pages/Index', localStorage)
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
