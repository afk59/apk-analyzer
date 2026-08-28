# @ohos.InputMethodExtensionAbility (InputMethodExtensionAbility)

The **InputMethodExtensionAbility** module provides APIs for developing input methods and managing the lifecycle of input method extensions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/CFMwjTc2RMW3omy946sy_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D56F935ADD0A997475F4092F8EC561FBA95EFF1D926A30578E02194FF8542380)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in the stage model.

#### Modules to Import

import { InputMethodExtensionAbility } from '@kit.IMEKit';

#### InputMethodExtensionAbility

Defines the **InputMethodExtensionAbility** class.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

#### \[h2\]Properties

Context of the **InputMethodExtensionAbility**.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context | [InputMethodExtensionContext](../ohos-inputmethodextensioncontext-inputmethodextensioncontext/document.md) | No | No | Context of the **InputMethodExtension**, which is inherited from **ExtensionContext**. |

#### \[h2\]onCreate

onCreate(want: Want): void

Called when the **InputMethodExtensionAbility** is started to implement initialization.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Information related to the **InputMethodExtensionAbility**, including the ability name and bundle name. |

**Example**

import { InputMethodExtensionAbility } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';

class InputMethodExt extends InputMethodExtensionAbility {
  onCreate(want: Want): void {
    console.info('onCreate, want:' + want.abilityName);
  }
}

#### \[h2\]onDestroy

onDestroy(): void

Called when this **InputMethodExtensionAbility** is destroyed to clear resources.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Example**

import { InputMethodExtensionAbility } from '@kit.IMEKit';

class InputMethodExt extends InputMethodExtensionAbility {
  onDestroy(): void {
    console.info('onDestroy');
  }
}
