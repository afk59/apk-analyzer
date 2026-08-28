# ExtensionContext

ExtensionContext provides the context environment for an [ExtensionAbility](../../../stage-model/ohos-app-ability-extensionability-extensionability-base-class/document.md). It inherits from [Context](../context-context-base-class-of-the-stage-model/document.md#context).

This module provides APIs for accessing resources of a specific [ExtensionAbility](../../../stage-model/ohos-app-ability-extensionability-extensionability-base-class/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/aBQHpJiDQvirA8myKu390w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062209Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77DEA7C5F77317C68357DE2053512DF7549756C0C4D175C3D39E451FFC9C274A)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in the stage model.

#### Modules to Import

import { common } from '@kit.AbilityKit';

#### Attributes

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| currentHapModuleInfo | [HapModuleInfo](../../bundlemanager/hapmoduleinfo/document.md) | No | No | Information about the HAP file. |
| config | [Configuration](../../../both-models-recommended/ohos-app-ability-configuration-environment-variables/document.md) | No | No | Module configuration information. |
| extensionAbilityInfo | [ExtensionAbilityInfo](../../bundlemanager/extensionabilityinfo/document.md) | No | No | [ExtensionAbility](../../../stage-model/ohos-app-ability-extensionability-extensionability-base-class/document.md) information. |

#### When to Use

ExtensionContext provides information about an ExtensionAbility, module, and HAP file. You can use the information based on service requirements.

**Example**

Obtain the context of a [FormExtensionAbility](../../../../../form-kit/arkts-apis/ohos-app-form-formextensionability-formextensionability/document.md) and query information such as its HAP file.

import { FormExtensionAbility, formBindingData } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onAddForm(want: Want) {
    console.info(\`FormExtensionAbility onAddForm, want: ${want.abilityName}\`);
    let extensionContext = this.context;
    let hapInfo = extensionContext.currentHapModuleInfo;
    console.info(\`HAP name is: ${hapInfo.name}\`);
    let dataObj1: Record<string, string> = {
      'temperature': '11c',
      'time': '11:00'
    };
    let obj1: formBindingData.FormBindingData = formBindingData.createFormBindingData(dataObj1);
    return obj1;
  }
};
