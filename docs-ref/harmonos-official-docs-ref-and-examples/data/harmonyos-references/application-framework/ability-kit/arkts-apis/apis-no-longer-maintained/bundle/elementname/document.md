# ElementName

The module provides element name information, which can be obtained through [Context.getElementName](../../../fa-model/app/context-context-base-class-of-the-fa-model/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/Tq-0lDoLTwm-1Di_o4GsVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=999414BBBD9A258879728A4875EB8882790B41351EFC5E919A6DFCB3DC17A0EE)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module have been deprecated since API version 9. You are advised to use [bundleManager-ElementName](../../../dependent-elements-and-definitions/bundlemanager/elementname/document.md) instead.

#### ElementName(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/WIXyVr0WRBu5it0sjFzroQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9F82CA60324938A0DE745B231969F4C4EC3A5804D9B5A123C102A41F848E1C9)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [bundleManager-ElementName](../../../dependent-elements-and-definitions/bundlemanager/elementname/document.md#elementname-1) instead.

Describes the element name information, which identifies the basic information about an ability and is obtained through [Context.getElementName](../../../fa-model/app/context-context-base-class-of-the-fa-model/document.md).

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | No | Yes | Device ID. |
| bundleName | string | No | No | Bundle name. |
| abilityName | string | No | No | Ability name. |
| uri | string | No | Yes | Resource ID. |
| shortName | string | No | Yes | Short name of the ability. |
