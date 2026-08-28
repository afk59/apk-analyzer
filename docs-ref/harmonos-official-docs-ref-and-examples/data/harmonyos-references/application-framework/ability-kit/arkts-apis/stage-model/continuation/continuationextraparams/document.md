# ContinuationExtraParams

The ContinuationExtraParams module provides the filter parameters required by the device selection module in the continuation management entry. These filter parameters can be used as an input parameter of [startContinuationDeviceManager](../../ohos-continuation-continuationmanager-continuation-collaboration-management/document.md#continuationmanagerstartcontinuationdevicemanagerdeprecated).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/3EdLgyGHQviPO1bN-ZdXKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B79142137CD57D907D4E55BC76F37CE05B349F17D4D275D90839DE03FB43370B)

The initial APIs of this module have been supported since API version 8 and deprecated since API version 22. You are advised to use the APIs in [Distributed Device Management](../../../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md) instead.

The APIs of this module can be used only in the stage model.

#### ContinuationExtraParams(deprecated)

Describes the extra parameters required by the device selection module in the continuation management entry.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/jhmWlTc1TC2nlw7sDW0RBw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6CC2DD1168151113DA16D6C31D9AF94583AF04681D761BF50ABF64B9622CDFF7)

This API has been deprecated since API version 22. You are advised to use [devicebasicinfo](../../../../../../system/network/distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#devicebasicinfo) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.DistributedAbilityManager

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceType | Array<string> | No | Yes | Device type. |
| targetBundle | string | No | Yes | Name of the target bundle. |
| description | string | No | Yes | Device filtering description. |
| filter | any | No | Yes | Device filtering parameter. |
| continuationMode | [continuationManager.ContinuationMode](../../ohos-continuation-continuationmanager-continuation-collaboration-management/document.md#continuationmodedeprecated) | No | Yes | Continuation mode. |
| authInfo | Record<string, Object> | No | Yes | Authentication information. |
