# CommonEventPublishData

The **CommonEventPublishData** module provides APIs for defining common event content and attributes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/kUW0zl4IRcOjFEEDRt_YBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062357Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6FCE8D26708120C4185E5DC01DCA06FDF7EE46F411085480B72A77858D4DA038)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

If there is no restriction, any application can subscribe to common events and read related information. In this case, sensitive information should not be carried in common events. The **subscriberPermissions** and **bundleName** parameters of this module can be used to restrict the receiving scope of common events.

#### Properties

**System capability**: SystemCapability.Notification.CommonEvent

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | No | Yes | 
Bundle name of the subscriber that can receive the common event.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| code | number | No | Yes | 

Common event data transferred by the publisher. The default value is **0**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| data | string | No | Yes | 

Common event data transferred by the publisher. The data size cannot exceed 64 KB.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| subscriberPermissions | Array<string> | No | Yes | 

Permissions required for subscribers to receive the common event.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| isOrdered | boolean | No | Yes | 

Whether the common event is an ordered one. The default value is **false**.

\- **true**: This event is an ordered common event. Based on the priority set by the subscriber, the common event is preferentially sent to the subscriber with a higher priority. After the subscriber successfully receives the event, the public event is sent to the subscriber with a lower priority. Subscribers with the same priority receive common events in a random order.

\- **false**: This event is an unordered common event. Whether subscribers receive the event is not considered, and the common event which subscribers receive may not comply with the subscription sequence.

 |
| isSticky | boolean | No | Yes | 

Whether the common event is a sticky one. The default value is **false**.

\- **true**: This event is a sticky common event, which allows subscribers to receive common events that have been sent before subscription.

\- **false**: This event is not a sticky common event, which allows subscribers to receive common events sent after subscription.

Only system applications and system services are allowed to send sticky events.

**Required Permissions**: [ohos.permission.COMMONEVENT\_STICKY](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/permissions-for-all#ohospermissioncommonevent_sticky)

 |
| parameters | {\[key: string\]: any} | No | Yes | 

Additional information about the common event transferred by the publisher.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
