# CommonEventData

Describes the data of a common event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/ue-FwYl-RM2qjfnG4zVJ_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062357Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4ACF2B770411DE80D45E8BD23B6B938C4E18C83DC0AB78F0A1A826E3E2BE5644)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Properties

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| event | string | No | No | Name of the common event that is being received. |
| bundleName | string | No | Yes | Bundle name. The default value is an empty string. |
| code | number | No | Yes | Common event data received by the subscriber. The value of this field is the same as that of the **code** field in [CommonEventPublishData](../commoneventpublishdata/document.md) when the publisher uses [commonEventManager.publish](../../ohos-commoneventmanager-common-event/document.md#commoneventmanagerpublish-1) to publish a common event. The default value is **0**. |
| data | string | No | Yes | Common event data received by the subscriber. The value of this field is the same as that of the **data** field in [CommonEventPublishData](../commoneventpublishdata/document.md) when the publisher uses [commonEventManager.publish](../../ohos-commoneventmanager-common-event/document.md#commoneventmanagerpublish-1) to publish a common event. |
| parameters | {\[key: string\]: any} | No | Yes | Additional information about the common event received by the subscriber. The value of this field is the same as that of the **parameters** field in [CommonEventPublishData](../commoneventpublishdata/document.md) when the publisher uses [commonEventManager.publish](../../ohos-commoneventmanager-common-event/document.md#commoneventmanagerpublish-1) to publish a common event. |
