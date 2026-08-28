# CommonEventSubscribeInfo

The **CommonEventSubscribeInfo** module provides APIs for providing subscriber information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/yURzSXsUTxuKjVEPrKtdtA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062357Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23B50E26FF0588DCE6D2475A75233C99CC8B02E75EAC639E410F778E1F6666F8)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

After users subscribing to custom common events, any application can send potential malicious common events to subscribers. Use the **publisherPermission** and **publisherBundleName** parameters of this module to restrict the publishing scope of common events.

#### Attributes

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| events | Array<string> | No | No | Common events to subscribe to. |
| publisherPermission | string | No | Yes | Permission of the publisher. The subscriber can receive only the events from the publisher with this permission. |
| publisherDeviceId | string | No | Yes | Device ID. Use [@ohos.deviceInfo](../../../device-management/ohos-deviceinfo-device-information/document.md) to obtain the UDID as the device ID of the subscriber. Not supported currently. |
| userId | number | No | Yes | User ID. If this parameter is not specified, the default value, which is the ID of the current user, will be used. The value must be an existing user ID in the system. Use [getOsAccountLocalId](../../../account-management/ohos-account-osaccount-system-account-management/document.md#getosaccountlocalid9) to obtain the system account ID and use it as the user ID of the subscriber. |
| priority | number | No | Yes | Subscriber priority. The value ranges from –100 to +1000. If the value exceeds the upper or lower limit, the upper or lower limit is used. |
| publisherBundleName11+ | string | No | Yes | Bundle name of the publisher to subscribe to. |
