# @ohos.app.ability.CompletionHandler (Application Launch Result Handler)

**CompletionHandler** is an optional parameter of [StartOptions](../ohos-app-ability-startoptions-optional-parameters-of-startability/document.md#startoptions) and [OpenLinkOptions](../ohos-app-ability-openlinkoptions-optional-parameters-of-openlink/document.md#openlinkoptions). It is used to process the result of an application launch request.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/snTk32JrSnKAMlcYR67TpQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062205Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A3D7CD459A6AF554FD02239BDE5EB9BAFF244A723286C199B1A7B647D6BAF089)

-   The initial APIs of this module are supported since API version 20. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module can be used only in the stage model.
    

#### Constraints

Currently, this module can be used in the following APIs:

-   [startAbility](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startability-2)
    
-   [startAbilityForResult](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startabilityforresult-2)
    
-   [openLink](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#openlink12)
    

#### Modules to Import

import { CompletionHandler } from '@kit.AbilityKit';

#### CompletionHandler

CompletionHandler provides two callback functions, [onRequestSuccess](#onrequestsuccess) and [onRequestFailure](#onrequestfailure), to handle the results of successful and failed application launch requests, respectively.

#### \[h2\]onRequestSuccess

onRequestSuccess(elementName: ElementName, message: string): void

Called when the application is successfully launched.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| elementName | [ElementName](../../dependent-elements-and-definitions/bundlemanager/elementname/document.md) | Yes | **ElementName** information used to identify the target application. Typically, **ElementName** includes only **abilityName** and **bundleName**. The presence of **moduleName** and **deviceId** depends on whether the caller provides them. **shortName** and **uri** are empty. |
| message | string | Yes | 
Message displayed when the application is successfully launched. This message is in JSON format, as follows:

{

"errMsg": "Succeeded."

}

 |

**Example**

See [Usage of CompletionHandler](#usage-of-completionhandler).

#### \[h2\]onRequestFailure

onRequestFailure(elementName: ElementName, message: string): void

Called when the application fails to be launched.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| elementName | [ElementName](../../dependent-elements-and-definitions/bundlemanager/elementname/document.md) | Yes | 
**ElementName** information used to identify the target application.

\- Typically, **ElementName** includes only **abilityName** and **bundleName**. The presence of **moduleName** and **deviceId** depends on whether the caller provides them. **shortName** and **uri** are empty.

\- **ElementName** information cannot be obtained if the implicit startup fails.

 |
| message | string | Yes | 

Message displayed when the application fails to be launched. This message is in JSON format, as follows:

{

"errMsg": "xxx"

}

The value of xxx is described as follows:

Failed to call <api-name>: An error occurs when calling the API. <api-name> is the specific API name, for example, **startAbility**.

User refused redirection: The user has closed the application redirection dialog box.

User closed the implicit startup picker: The user has closed the dialog box for selecting an application for implicit startup.

User closed the app clone picker: The user has closed the dialog box for selecting a cloned application.

Free installation failed: The free installation fails.

 |

**Example**

See [Usage of CompletionHandler](#usage-of-completionhandler).

## Usage of CompletionHandler

import { UIAbility, Want, StartOptions, CompletionHandler, bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };

    let completionHandler: CompletionHandler = {
      onRequestSuccess: (elementName: bundleManager.ElementName, message: string): void => {
        console.info(\`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start succeeded: ${message}\`);
      },
      onRequestFailure: (elementName: bundleManager.ElementName, message: string): void => {
        console.error(\`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start failed: ${message}\`);
      }
    };

    let options: StartOptions = {
      completionHandler: completionHandler
    };

    try {
      this.context.startAbility(want, options, (err: BusinessError) => {
        if (err.code) {
          // Process service logic errors.
          console.error(\`startAbility failed, code is ${err.code}, message is ${err.message}\`);
          return;
        }
        // Carry out normal service processing.
        console.info('startAbility succeed');
      });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`startAbility failed, code is ${code}, message is ${message}\`);
    }
  }
}
