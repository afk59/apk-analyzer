# ShortcutInfo

The module defines shortcut information configured in the configuration file. For the [FA model](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-terminology#fa-model), the information is configured in the [config.json](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-configuration-file-overview-fa) file. For the [stage model](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-terminology#stage-model), the information is configured in the configuration file under **resources/base/profile** in the development view.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/E6YguXqsT_mEDCeJSggd4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11203F61EED9FED22AE4CA619C79640FB02F3D93903D3711ACFD45E84CD4DDFA)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module have been deprecated since API version 9. You are advised to use [bundleManager-ShortcutInfo](../../../dependent-elements-and-definitions/bundlemanager/shortcutinfo/document.md) instead.

#### ShortcutInfo(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/7o8Pn6ypSM23uUxO8UUGYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD6298D16B8099172220D2FA178B7AD199684368FBBA8E91D8D0C3B953A97A47)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [bundleManager-ShortcutInfo](../../../dependent-elements-and-definitions/bundlemanager/shortcutinfo/document.md#shortcutinfo-1) instead.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | string | Yes | No | ID of the application to which the shortcut belongs. |
| bundleName | string | Yes | No | Name of the bundle that contains the shortcut. |
| hostAbility | string | Yes | No | Local ability information of the shortcut. |
| icon | string | Yes | No | Icon of the shortcut. |
| iconId8+ | number | Yes | No | Icon ID of the shortcut. |
| label | string | Yes | No | Name of the shortcut. |
| labelId8+ | number | Yes | No | Name ID of the shortcut. |
| disableMessage | string | Yes | No | Message displayed when the shortcut is disabled. |
| wants | Array<ShortcutWant> | Yes | No | Want list for the shortcut. |
| isStatic | boolean | Yes | Yes | Whether the shortcut is static. **true** if static, **false** otherwise. |
| isHomeShortcut | boolean | Yes | Yes | Whether the shortcut is a home shortcut. **true** if the shortcut is a home shortcut, **false** otherwise. |
| isEnabled | boolean | Yes | Yes | Whether the shortcut is enabled. **true** if enabled, **false** otherwise. |
