# WantAgentInfo

The module defines the information required for triggering the WantAgent.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/nBpBAwJTQL-OegVPtapMBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062211Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ECE177877470A1DB9F11B88DCEC58EC8D32792CFFE5F7306F77DF0559DA9B1DA)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { wantAgent as abilityWantAgent } from '@kit.AbilityKit';

#### WantAgentInfo

Defines the information required for triggering a WantAgent object. The information can be used as an input parameter in [getWantAgent](../../../both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md#wantagentgetwantagent) to obtain a specified WantAgent object.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| wants | Array<[Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md)\> | No | No | 
Array of all Want objects. Currently, only one Want is supported. The array is reserved for future capability expansion. If multiple values are passed in, only the first member in the array is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| operationType(deprecated) | [wantAgent.OperationType](../../../apis-no-longer-maintained/ohos-wantagent-wantagent-module/document.md#operationtype) | No | Yes | 

Operation type.

This attribute is supported since API version 7 and deprecated since API version 11. You are advised to use actionType11+ instead.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| actionType11+ | [abilityWantAgent.OperationType](../../../both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md#operationtype) | No | Yes | 

Operation type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| requestCode | number | No | No | 

Custom request code, which is used to identify the operation to execute.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| wantAgentFlags(deprecated) | Array<[wantAgent.WantAgentFlags](../../../apis-no-longer-maintained/ohos-wantagent-wantagent-module/document.md#wantagentflags)\> | No | Yes | 

Array of flags for using the WantAgent object.

This attribute is supported since API version 7 and deprecated since API version 11. You are advised to use actionFlags11+ instead.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| actionFlags11+ | Array<[abilityWantAgent.WantAgentFlags](../../../both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md#wantagentflags)\> | No | Yes | 

Array of flags for using the WantAgent object.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| extraInfo | { \[key: string\]: any } | No | Yes | 

Extra information.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| extraInfos11+ | Record<string, Object> | No | Yes | 

Extra information. You are advised to use this property to replace **extraInfo**. When this property is set, **extraInfo** does not take effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
