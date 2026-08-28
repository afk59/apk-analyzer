# @ohos.application.DistributedExtensionAbility (Distributed Extension)

The **DistributedExtensionAbility** module provides distributed extension capabilities and lifecycle callbacks for distributed ability creation, destruction, and connection.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/1Aq8T0PcQCOnxdlyl2Orfw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062343Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7374B2FE8D349A8B94A102923A4F360F01D1AE3074CB491866CDC4D58515BE38)

The initial APIs of this module are supported since API version 20. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { DistributedExtensionAbility} from '@kit.DistributedServiceKit';

#### DistributedExtensionAbility

#### \[h2\]Attributes

**System capability**: SystemCapability.DistributedSched.AppCollaboration

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context | DistributedExtensionContext | No | No | Context of the **DistributedExtension**. This context inherits from **ExtensionContext**. |

#### \[h2\]onCreate

onCreate(want: Want): void

Callback invoked to initialize the service logic when a **DistributedExtensionAbility** instance is created.

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want information related to the **DistributedExtensionAbility** instance, including the ability name and bundle name. |

**Example**

import { Want } from '@kit.AbilityKit';
import { DistributedExtensionAbility } from '@kit.DistributedServiceKit';

export default class DistributedExtension extends DistributedExtensionAbility {
  onCreate(want: Want) {
    console.info(\`DistributedExtension Create ok\`);
    console.info(\`DistributedExtension on Create want: ${JSON.stringify(want)}\`);
    console.info(\`DistributedExtension Create end\`);
  }
}

#### \[h2\]onCollaborate

onCollaborate(wantParam: Record <string, Object>) : AbilityConstant.CollaborateResult

Callback invoked to return the collaboration result in multi-device collaboration scenarios.

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| wantParam | Record <string, Object> | Yes | Want parameter, which supports only the key **"ohos.extra.param.key.supportCollaborateIndex"**. The key can be used to obtain the data passed by the caller and perform corresponding processing. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AbilityConstant.CollaborateResult](../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-abilityconstant-ability-related-constants/document.md#collaborateresult18) | Collaboration result, that is, whether the target application accepts the collaboration request. |

**Example**

import { abilityConnectionManager, DistributedExtensionAbility } from '@kit.DistributedServiceKit';
import { AbilityConstant } from '@kit.AbilityKit';

export default class DistributedExtension extends DistributedExtensionAbility {
  onCollaborate(wantParam: Record<string, Object>) {
    console.info(\`DistributedExtension onCollabRequest Accept to the result of Ability collaborate\`);
    let sessionId = -1;
    const collaborationValues = wantParam\["CollaborationValues"\] as abilityConnectionManager.CollaborationValues;
    if (collaborationValues == undefined) {
      return sessionId;
    }
    console.info(\`onCollab, collaborationValues: ${JSON.stringify(collaborationValues)}\`);
    return AbilityConstant.CollaborateResult.ACCEPT;
  }
}

#### \[h2\]onDestroy

onDestroy(): void

Callback invoked to clear resources when a **ServiceExtensionAbility** instance is destroyed.

**System capability**: SystemCapability.DistributedSched.AppCollaboration

**Example**

import { DistributedExtensionAbility } from '@kit.DistributedServiceKit';

export default class DistributedExtension extends DistributedExtensionAbility {
  onDestroy() {
    console.info('DistributedExtension onDestroy ok');
  }
}
