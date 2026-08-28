# @ohos.app.ability.Ability (Ability Base Class)

The Ability class is the fundamental unit for application lifecycle scheduling. It is the base class of [UIAbility](../ohos-app-ability-uiability-ability-with-ui/document.md) and [ExtensionAbility](../ohos-app-ability-extensionability-extensionability-base-class/document.md), and provides callbacks for system configuration updates and memory level updates. However, you cannot inherit directly from this base class. You should opt for either [UIAbility](../ohos-app-ability-uiability-ability-with-ui/document.md) or [ExtensionAbility](../ohos-app-ability-extensionability-extensionability-base-class/document.md) based on your service needs. For details, see [Introduction to Ability Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/abilitykit-overview).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/JIY8BqKyQNikVqTrZiTKxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9343D1C200B88CFBFCE50A8BCA8896B6D8BC7E1F473FA8909A7CA122D12591A1)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { Ability } from '@kit.AbilityKit';

#### Ability Inheritance Relationship

The following figure shows the inheritance relationship of the Ability base class and its child classes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/nM8eXkBeSLaIlIrmGgoiVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CDCC02322EF3C889C65804987D59D3A8F2C7944B8574CCCD9F97A038C8AEB532)

Some ExtensionAbility components (such as [FormExtensionAbility](../../../../form-kit/arkts-apis/ohos-app-form-formextensionability-formextensionability/document.md) and [InputMethodExtensionAbility](../../../../ime-kit/arkts-apis/ohos-inputmethodextensionability-inputmethodextensionability/document.md)) do not inherit from the ExtensionAbility base class and therefore are not provided in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/7o1fHpAETlaIR83kZLfjQA/en-us_image_0000002568685025.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09DE2653120D9D8E73E088CB9BCD6615922F21CE8987F52EAEF83DD44220F162)

#### Ability.onConfigurationUpdate

onConfigurationUpdate(newConfig: Configuration): void

Called when a system environment variable changes. You can override this callback to respond to changes in the system environment variables. For example, when the system language changes, the application can perform customized processing in the callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/5XaWqIp1R_eRSx0eMgFqeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7476DFF63B3960E9F589313F4796A999A3475294F9C031AE73F4C85F006263FB)

There are certain restrictions when this callback is actually triggered. For example, if you set the application language by calling [setLanguage](../../dependent-elements-and-definitions/application/applicationcontext-application-context/document.md#applicationcontextsetlanguage11), the system does not trigger the **onConfigurationUpdate** callback even if the system language changes. For details, see [When to Use](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/subscribe-system-environment-variable-changes#when-to-use).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| newConfig | [Configuration](../../both-models-recommended/ohos-app-ability-configuration-environment-variables/document.md) | Yes | New configuration. |

**Example**

// You are not allowed to inherit from the top-level base class Ability. Therefore, the derived class UIAbility is used as an example.
import { UIAbility, Configuration } from '@kit.AbilityKit';

class MyUIAbility extends UIAbility {
  onConfigurationUpdate(config: Configuration) {
    console.info(\`onConfigurationUpdate, config: ${JSON.stringify(config)}\`);
  }
}

#### Ability.onMemoryLevel

onMemoryLevel(level: AbilityConstant.MemoryLevel): void

Called when the available memory of the entire device changes to a specified level. You can override this callback to respond to changes in the memory level, for example, releasing cached data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/uidvHpqYRPqzm5W2CJcBQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062204Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=168BDC1AFB951A076DF72CFC06E5FB7D7E5FF0C7D67503815C9AF2B551565CDC)

The **onMemoryLevel** callback runs in the main thread of the current process. If time-consuming UI component release is performed in this callback, the main thread task will be blocked. Therefore, you are not advised to release UI components in the callback.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| level | [AbilityConstant.MemoryLevel](../ohos-app-ability-abilityconstant-ability-related-constants/document.md#memorylevel) | Yes | 
Level of the available memory.

**NOTE**

The trigger conditions may differ across various devices. For example, on a standard device with 12 GB of memory:

\- When the available memory of the entire device drops to 1700 MB to 1800 MB, the **onMemoryLevel** callback of the MEMORY\_LEVEL\_MODERATE type is triggered, indicating that the available memory is moderate.

\- When the available memory of the entire device drops to 1600 MB to 1700 MB, the **onMemoryLevel** callback of the MEMORY\_LEVEL\_LOW type is triggered, indicating that the available memory is low.

\- When the available memory of the entire device drops below 1600 MB, the **onMemoryLevel** callback of the MEMORY\_LEVEL\_CRITICAL type is triggered, indicating that the available memory is critically low.

 |

**Example**

// You are not allowed to inherit from the top-level base class Ability. Therefore, the derived class UIAbility is used as an example.
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

class MyUIAbility extends UIAbility {
  onMemoryLevel(level: AbilityConstant.MemoryLevel) {
    console.info(\`onMemoryLevel, level: ${JSON.stringify(level)}\`);
  }
}
