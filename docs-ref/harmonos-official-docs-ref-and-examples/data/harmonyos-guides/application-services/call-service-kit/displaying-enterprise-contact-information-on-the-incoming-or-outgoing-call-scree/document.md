# Displaying Enterprise Contact Information on the Incoming or Outgoing Call Screen

This function is available only for enterprise app developers.

#### Use Cases

When an incoming or outgoing call is made, information about contact persons who have installed an enterprise app will be displayed. This helps the user identify the caller or callee more easily, enabling a quicker response and improving internal communication efficiency.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/COp-JPquSNqw6hn5PGrBiA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=940EDAD0733EEBB0412D3F020BDA606DD13A04E67497C98B05311AB767CAEF64)

Only one contact person is displayed on the incoming/outgoing call screen or banner. If the same contact person exists in multiple apps, the apps will be sorted lexicographically by app package name, and the first result will be displayed.

#### API Description

For details, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/callservicekit-callerinfoquery-extension-ability#section1220554318191).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

onQueryCallerInfo(phoneNumber: string): Promise<CallerInfo>

 | 

Queries contact person information.

 |

#### Integration Request

Use of this API is subject to restrictions. To gain access, submit an application as follows:

Email your application to agconnect@huawei.com.

Email subject: \[_Company name_\]-Capability of displaying enterprise contact information-_Developer ID_

Email body: app user entity, app name, app ID, app package name, and use case description (specifically detailing the app's contact volume and other necessary information).

#### Replacing the Debug Profile

After the capability of displaying enterprise contact information on the incoming and outgoing call screen is granted, you need to [apply for a new debug profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-debugprofile-0000001914423102). Then, replace the debug profile in DevEco Studio with the new one.

#### Development Procedure

1.  Create a custom component of the **ExtensionAbility** type in the project and inherit from [CallerInfoQueryExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/callservicekit-callerinfoquery-extension-ability) to override the **onQueryCallerInfo** method.
    
    Note:
    
    When the **onQueryCallerInfo** method is called, the system first creates an **AbilityStage** instance for the app. Therefore, avoid adding overly complex or time-consuming logic within **AbilityStage** to prevent call timeouts.
    
    Sample code:
    
    import { CallerInfoQueryExtensionAbility, CallerInfo } from '@kit.CallServiceKit';
    
    export default class EntryCallerInfoQueryExtAbility extends CallerInfoQueryExtensionAbility {
     // During incoming or outgoing calls, the system dialer app actively calls this API to query enterprise contact information.
      onQueryCallerInfo(phoneNumber: string): Promise<CallerInfo> {
        return new Promise<CallerInfo>((resolve, reject) => {
          let isSuccess = true;
          // Implement the service logic for querying enterprise contact persons by mobile number.
          if (isSuccess) {
            // If the query is successful, return the result.
            resolve({
              contactName:"xxxx",
              employeeId:"xxxx",
              department:"xxxx",
              position:"xxxx"
            });
          } else {
            // If the query failed, return the error.
            reject("error reason");
          }
        });
      }
    }
    
2.  Register **extensionAbilities** in the app configuration file **module.json5**. For details, please refer to [module.json5 Configuration File](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md).
    
    Sample code:
    
    {
        "extensionAbilities": \[
          {
            "name": "EntryCallerInfoQueryExtAbility",
            "srcEntry": "./ets/callerinfoquery/EntryCallerInfoQueryExtAbility.ets",
            "type": "callerInfoQuery"
          }
        \]
    }
    
    -   **type** should be set to **callerInfoQuery**, indicating the extension type **CallerInfoQueryExtensionAbility**.
    -   **srcEntry** is the path to the **ExtensionAbility** component specified in the preceding step.
3.  Go to the **Phone** app on a debugging device, tap **....** in the upper-right corner, and then go to **Settings** > **Call & message identification**. Enable **Call & message identification**.
