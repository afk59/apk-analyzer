# TriggerInfo

The module defines the information required for triggering the WantAgent. The information is used as an input parameter of [trigger](../../../both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md#wantagenttrigger).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/Ii0WKdFySam3qI_V6xVA2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062211Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D9817ED690387984BA96760704F467EAAE8EA8AAA9239428AE7BF9E82D4DD89)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { wantAgent } from '@kit.AbilityKit';

#### Properties

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| code | number | No | No | Common event code. This field is valid only when [OperationType](../../../both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md#operationtype) of the WantAgent instance is **'SEND\_COMMON\_EVENT'**. The meaning of this field is the same as that of the **code** field set in [CommonEventPublishData](../../../../../../system/basic-functions/basic-services-kit/arkts-apis/process-and-thread-communication/commonevent/commoneventpublishdata/document.md#properties) when the publisher uses [commonEventManager.publish](../../../../../../system/basic-functions/basic-services-kit/arkts-apis/process-and-thread-communication/ohos-commoneventmanager-common-event/document.md#commoneventmanagerpublish-1) to publish common events. |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | No | Yes | Carrier for information transfer between objects (application components). |
| permission | string | No | Yes | Permission required for a subscriber to receive the common event. This field is valid only when [OperationType](../../../both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md#operationtype) of the WantAgent instance is **'SEND\_COMMON\_EVENT'**. |
| extraInfo | { \[key: string\]: any } | No | Yes | Extra information. |
| extraInfos11+ | Record<string, Object> | No | Yes | Extra information. You are advised to use this property to replace **extraInfo**. When this property is set, **extraInfo** does not take effect. |
