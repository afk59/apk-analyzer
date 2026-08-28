# StartAbilityParameter

The module defines the parameters for starting an ability. The parameters can be used as input parameters in [startAbility](../../ohos-ability-featureability-featureability-module/document.md#featureabilitystartability) to start the specified ability.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/hbQVv4raTw6wP9mDOEAICA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31793C0FEF75501706CB591CC384DC21608492E6A74F757F38807D02ADB79508)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the FA model.

#### Modules to Import

import ability from '@ohos.ability.ability';

#### Attributes

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | No | No | Want information about the target ability. |
| abilityStartSetting | { \[key: string\]: any } | No | Yes | Special attribute of the target ability. This attribute can be passed in the call. |
| abilityStartSettings11+ | Record<string, Object> | No | Yes | Special attribute of the target ability. This attribute can be passed in the call. You are advised to use this attribute to replace **abilityStartSetting**. When this attribute is set, **abilityStartSetting** does not take effect. |

**Example**

import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import Want from '@ohos.app.ability.Want';

let want: Want = {
    bundleName: 'com.example.abilityStartSettingApp2',
    abilityName: 'com.example.abilityStartSettingApp.EntryAbility',
};

let startAbilityParameter: ability.StartAbilityParameter = {
    want : want,
    abilityStartSettings : {
        abilityBounds : \[100,200,300,400\],
        windowMode :
        featureAbility.AbilityWindowConfiguration.WINDOW\_MODE\_UNDEFINED,
        displayId : 1,
    }
};

try {
    featureAbility.startAbility(startAbilityParameter, (error, data) => {
        if (error && error.code !== 0) {
            console.error(\`startAbility fail, error: ${JSON.stringify(error)}\`);
        } else {
            console.info(\`startAbility success, data: ${JSON.stringify(data)}\`);
        }
    });
} catch(error) {
    console.error(\`startAbility error: ${JSON.stringify(error)}\`);
}
