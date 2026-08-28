# ContinuationResult

The ContinuationResult module describes the device information returned by the continuation management entry.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/MzexytJgSjaVB9Dg_HSOBQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DD106517B4DFCAF13B6CA5B59752D1AAA02594024D23EF0AD3A9AAE2B7C68CB)

The initial APIs of this module have been supported since API version 8 and deprecated since API version 22. You are advised to use the APIs in [Distributed Device Management](../../../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md) instead.

The APIs of this module can be used only in the stage model.

#### ContinuationResult(deprecated)

Describes the device information returned by the continuation management entry after [on](../../ohos-continuation-continuationmanager-continuation-collaboration-management/document.md#continuationmanagerondeviceselecteddeprecated) is called.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/kTXJzJAhTqKo7dutCrPtTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7ED7454E14DD17F585557E276E0BA26D478F54C1D32DA2599B552E74FFC3B6A8)

This API has been deprecated since API version 22. You are advised to use [devicebasicinfo](../../../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#devicebasicinfo) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.DistributedAbilityManager

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | string | No | No | Device ID. |
| type | string | No | No | Device type. |
| name | string | No | No | Device name. |
