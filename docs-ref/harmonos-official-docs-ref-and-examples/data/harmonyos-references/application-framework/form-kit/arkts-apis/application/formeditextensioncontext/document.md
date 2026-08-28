# FormEditExtensionContext

**FormEditExtensionContext**, inherited from [UIExtensionContext](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md), is the context of [FormEditExtensionAbility](../../ohos-app-form-formeditextensionability-formeditextensionability/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/k7NabiKbTb6Z3yPPJdlG-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C65DDB666BA19D780D2571E6F52EF7258476305F889E24DDED44620D1796D93B)

-   The initial APIs of this module are supported since API version 18. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module can be used only in the stage model.
    

#### Modules to Import

import { FormEditExtensionAbility } from '@kit.FormKit';

#### FormEditExtensionContext

You can use **FormEditExtensionContext** to access specific **FormEditExtensionAbility** resources.

#### \[h2\]startSecondPage

startSecondPage(want: Want): Promise<[AbilityResult](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/ability/abilityresult/document.md)\>

Starts the widget provider page to be edited. This API uses a promise to return the result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Information about the editing page that needs to be started by the home screen of a third-party application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AbilityResult](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/ability/abilityresult/document.md)\> | Promise used to return the ability result. |

**Error codes**

For details about the error codes, see [Form Error Codes](../../../error-codes/widget-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 202 | The application is not a system application. |
| 16500050 | An IPC connection error happened. |
| 16501000 | An internal functional error occurred. |
| 16500100 | Failed to obtain the configuration information. |

**Example**

import { FormEditExtensionAbility } from '@kit.FormKit';
import { UIExtensionContentSession, Want } from '@kit.AbilityKit';

const TAG: string = '\[testTag\] ExampleFormEditExtensionAbility'

export default class ExampleFormEditAbility extends FormEditExtensionAbility {
  abilityName: string = 'FormEditSecPageAbility'

  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    try {
      this.context.startSecondPage({
        bundleName: 'com.example.formEditDemo',
        parameters: {
          "secPageAbilityName": this.abilityName
        }

      }).then(data => {
        console.info(TAG, \`startSecondPage result want: ${data.resultCode}\`)
      });
    } catch (e) {
      console.error(TAG, \`startSecondPage failed, code: ${e.code}, message: ${e.message}\`)
      return
    }
  }
}
