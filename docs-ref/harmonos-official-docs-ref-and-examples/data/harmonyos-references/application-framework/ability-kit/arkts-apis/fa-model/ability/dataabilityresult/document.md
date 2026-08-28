# DataAbilityResult

The module defines the operation result on DataAbilities. When you call [executeBatch](../../../dependent-elements-and-definitions/ability/dataabilityhelper/document.md#dataabilityhelperexecutebatch) to operate the database, the operation result is returned through the DataAbilityResult object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/z3UtTma6TE2QLc8ffBBccw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF2399F9103E1CAF3DE80C3096A748A2B6CC5FD76EEA6B74F17AB4107272ABBB)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the FA model.

#### Modules to Import

import ability from '@ohos.ability.ability';

#### Attributes

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uri | string | No | Yes | URI of the DataAbility. Example: 'dataability:///com.example.xxx.xxxx'. |
| count | number | No | Yes | Number of rows affected by the operation. |

**Example**

import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import rdb from '@ohos.data.rdb';
import { BusinessError } from '@ohos.base';

// Perform database operations in batches.
function executeBatchOperation() {
    let dataAbilityUri = ('dataability:///com.example.myapplication.TestDataAbility');
    let DAHelper: ability.DataAbilityHelper;
    DAHelper = featureAbility.acquireDataAbilityHelper(dataAbilityUri);

    let valueBucket: rdb.ValuesBucket = {
        'name': 'DataAbilityHelperTest',
        'age': 24,
        'salary': 2024.20,
    };
    let predicateBackReferences = new Map<number, number>()
    predicateBackReferences.set(1, 1)

    let operations: Array<ability.DataAbilityOperation> = \[
        {
            uri: dataAbilityUri,
            type: featureAbility.DataAbilityOperationType.TYPE\_INSERT,
            valuesBucket: valueBucket,
            expectedCount: 1,
            predicatesBackReferences: predicateBackReferences,
            interrupted: true,
        },
        {
            uri: dataAbilityUri,
            type: featureAbility.DataAbilityOperationType.TYPE\_INSERT,
            valuesBucket: valueBucket,
            expectedCount: 1,
            predicatesBackReferences: predicateBackReferences,
            interrupted: true,
        }
    \];
    try {
        DAHelper.executeBatch(dataAbilityUri, operations).then((data) => {
            for (let i = 0; i < data.length; i++) {
                let dataAbilityResult: ability.DataAbilityResult = data\[i\];
                console.info(\`dataAbilityResult.uri: ${dataAbilityResult.uri}\`);
                console.info(\`dataAbilityResult.count: ${dataAbilityResult.count}\`);
            }
        }).catch((err: BusinessError) => {
            console.error(\`executeBatch error: ${JSON.stringify(err)}\`);
        });
    } catch (err) {
        console.error(\`executeBatch error: ${JSON.stringify(err as BusinessError)}\`);
    }
}
