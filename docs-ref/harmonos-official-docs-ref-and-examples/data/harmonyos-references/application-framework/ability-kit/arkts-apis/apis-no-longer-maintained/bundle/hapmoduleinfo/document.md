# HapModuleInfo

The HapModuleInfo module provides information about an HAP module. Unless otherwise specified, the information is obtained through [bundle.getBundleInfo](../../ohos-bundle-bundle-module/document.md#bundlegetbundleinfodeprecated).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/Z2TycLQfQVeTMyoKebsoAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE4BCB0D87B50593EA5E49321149E38C16739CE020EE0BC6A221019C59818793)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module have been deprecated since API version 9. You are advised to use [bundleManager-HapModuleInfo](../../../dependent-elements-and-definitions/bundlemanager/hapmoduleinfo/document.md) instead.

#### HapModuleInfo(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/hBqHHKMyTj6fShBOAltBrg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F0AE86458F8D04408F10C3FF796B814E4807D44C56EBA34FB94AC90EF29DAB9)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [bundleManager-HapModuleInfo](../../../dependent-elements-and-definitions/bundlemanager/hapmoduleinfo/document.md#hapmoduleinfo-1) instead.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | Yes | No | Module name. |
| description | string | Yes | No | Module description. |
| descriptionId | number | Yes | No | Module description ID. |
| icon | string | Yes | No | Module icon. |
| label | string | Yes | No | Module label. |
| labelId | number | Yes | No | Module label ID. |
| iconId | number | Yes | No | Module icon ID. |
| backgroundImg | string | Yes | No | Module background image. |
| supportedModes | number | Yes | No | Running modes supported by the module. |
| reqCapabilities | Array<string> | Yes | No | Capabilities required for module running. |
| deviceTypes | Array<string> | Yes | No | Device types supported by the module. |
| abilityInfo | Array<[AbilityInfo](../abilityinfo/document.md)\> | Yes | No | Ability information. |
| moduleName | string | Yes | No | Module name. |
| mainAbilityName | string | Yes | No | Name of the main ability. |
| installationFree | boolean | Yes | No | Whether installation-free is supported. **true** if supported, **false** otherwise. |
