# Function Search Solution

#### Solution Overview

Starting from version 5.1.0(18), the function search solution has been introduced, enabling quick navigation to in-app functional pages. You can integrate your in-app functions by declaring them in the declaration file of Intents Kit and implementing necessary intent calls. This allows users to directly find these functions through Celia Search, with a single tap launching the app and navigating straight to the desired function page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/fpK9KUM3Rz-7OsEUkiW4xg/en-us_image_0000002402161801.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062127Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A3D88F7ACBD8B2B26C71E1F2C9008A8C48AB922132EB67166A310F6F4FCC4FB6 "Click to enlarge")

**Intent name: JumpFunctionPage (device-side foreground intent call)**

| 
**Category**

 | 

**Parameter**

 | 

**Mandatory**

 | 

**Description**

 | 

**Type**

 | 

**Value Example**

 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 

**Input**

 | 

pageId

 | 

Yes

 | 

ID of a specific function, which you can define as needed.

 | 

string

 | 

1, 2, 3...

 |
| 

**Output**

 | 

code

 | 

Yes

 | 

Result code of an intent call.

 | 

number

 | 

**0**: successful

Others: failed (Negotiate with Huawei in advance. Customization is not supported.)

 |
| 

result

 | 

Yes

 | 

Data returned after an intent call. If there is no data, an empty record will be returned.

 | 

Record<string, Object>

 | 

{
  message: 'Intent execute success'
}

 |

#### Intent Declaration

Edit the **insight\_intent.json** file to register the intent. The **insight\_intent.json** file must be placed in the **src/main/resources/base/profile/insight\_intent.json** directory of any module. Only one **insight\_intent.json** file can exist in the entire project.

{
    "insightIntents": \[
       {
            "intentName": "JumpFunctionPage",   // Intent name.
            "domain": "ToolsDomain",
            "intentVersion": "1.0.1", // Intent version.
         // Entry to the intent call logic.
            "srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
            "uiAbility": {
            // Ability that the intent belongs to.
            "ability": "EntryAbility",
        // **UIAbility** supports only the foreground execution mode.
            "executeMode": \[
                "foreground"
            \]
            },
            "inputParams": \[{ // Some intents allow for parameter customization, with the overall format referencing JSON-Schema.
                "properties": { // Describe the parameter list. You can add other description nodes at the same level.
                    "pageId": { // ID of a specific function.
                        "type": "string", // Parameter type.
                        "enum": \[ 
                            {
                                "value": "1", // Value of the function ID.
                                "displayName": "Find route", // Function name, displayed in Celia Search.
                                "keywords": \[
                                    "Plan route"
                                \], // Alias of the function name, which is used for indexing and filtering. At most five aliases can be set.
                                "displayDescription": "Find routes to a destination.", // Function description, displayed in Celia Search.
                                "icon": "https://abc.xx" // Function icon, displayed in Celia Search.
                            },
                            {
                                "value": "2", // Value of the function ID.
                                "displayName": "Scan", // Function name, displayed in Celia Search.
                                "keywords": \[
                                    "Scan QR code"
                                \], // Alias of the function name, which is used for indexing and filtering.
                                "displayDescription": "Scan QR codes.", // Function description, displayed in Celia Search.
                                "icon": "https://abc.xx" // Function icon, displayed in Celia Search.
                            }
                        \]
                    }
                }
            }\]
        }
    \]
}

#### Device-Side Foreground Intent Call

Implement **InsightIntentExecutor** yourself and implement the capability of opening the landing page in the corresponding callback.

The procedure is as follows:

1.  Extend **InsightIntentExecutor**.
2.  Override the corresponding method. For example, to open a foreground page, override the **onExecuteInUIAbilityForegroundMode** method.
3.  Identify the intent for jumping to a function page based on the intent name (**JumpFunctionPage**) and pass the intent parameters (**param**) in the corresponding method to open the target landing page.

import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
/\*\*
 \* Intent call example. \*/
export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
  private static readonly JUMP\_FUNCTION\_PAGE = 'JumpFunctionPage';
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
      case InsightIntentExecutorImpl.JUMP\_FUNCTION\_PAGE:
        return this.jumpFunctionPage(param, pageLoader);
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
   \* Implement the function of redirecting to the target page.
   \*
   \* @param param Intent parameters.
   \* @param pageLoader Window.
   \*/
  private jumpFunctionPage(param: Record<string, Object>, pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
    return new Promise((resolve, reject) => {
      let pageId: string = param?.pageId as string;
      pageLoader.loadContent('pages/'+ pageId)
        .then(() => {
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
