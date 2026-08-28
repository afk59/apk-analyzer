# DataAbilityOperation

The module defines the operation on DataAbilities. It can be used as an input parameter of [executeBatch](../../../dependent-elements-and-definitions/ability/dataabilityhelper/document.md#dataabilityhelperexecutebatch) to specify the database operation information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/QKYYn38PQxOcus51VJQ_NA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=693DB3BBEDCBDF68A52D07A0B7F40A7CA3B74CCB1A97D8E6AB7890332569BDBE)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the FA model.

#### Modules to Import

import ability from '@ohos.ability.ability';

#### Attributes

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

| Name | Template | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uri | string | No | No | URI of the DataAbility. Example: 'dataability:///com.example.xxx.xxxx'. |
| type | [featureAbility.DataAbilityOperationType](../../ohos-ability-featureability-featureability-module/document.md#dataabilityoperationtype7) | No | No | Operation type. |
| valuesBucket | [rdb.ValuesBucket](../../../../../arkdata/arkts-apis/ohos-data-relationalstore-rdb-store/types/document.md#valuesbucket) | No | Yes | Data value to set. |
| valueBackReferences | [rdb.ValuesBucket](../../../../../arkdata/arkts-apis/ohos-data-relationalstore-rdb-store/types/document.md#valuesbucket) | No | Yes | ValuesBucket object that contains a set of key-value pairs. |
| predicates | [dataAbility.DataAbilityPredicates](../../../../../arkdata/arkts-apis/ohos-data-dataability-dataability-predicates/document.md#dataabilitypredicates) | No | Yes | Predicates to set. If no predicate is set, all data records are displayed. |
| predicatesBackReferences | Map<number, number> | No | Yes | Back references of the predicates. |
| interrupted | boolean | No | Yes | Whether batch operations can be interrupted. **true** if batch operations can be interrupted, **false** otherwise. |
| expectedCount | number | No | Yes | Expected number of rows to be updated or deleted. |
