# AbilityInfo

The module provides information about an ability. Unless otherwise specified, the information is obtained through [bundle.getAbilityInfo](../../ohos-bundle-bundle-module/document.md#bundlegetabilityinfodeprecated).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/BnaGAtsATBu4hya2XjiAqw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=415021D8D858834764DA5938EDF5C3650EEA81918B6F2175A8FEC88EC9C1C3CB)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module have been deprecated since API version 9. You are advised to use [bundleManager-AbilityInfo](../../../dependent-elements-and-definitions/bundlemanager/abilityinfo/document.md) instead.

#### AbilityInfo(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/b7QP82AjTW6oh66p3aHx2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D234F9F23BFF4BD155965BC1BCD73DE84A0EE615B75E4CBB00BA9EB472C255FD)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [bundleManager-AbilityInfo](../../../dependent-elements-and-definitions/bundlemanager/abilityinfo/document.md#abilityinfo-1) instead.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | Yes | No | Bundle name. |
| name | string | Yes | No | Ability name. |
| label | string | Yes | No | Ability name visible to users. |
| description | string | Yes | No | Ability description. |
| icon | string | Yes | No | Index of the ability icon resource file. |
| descriptionId | number | Yes | No | ID of the ability description. |
| iconId | number | Yes | No | ID of the ability icon. |
| moduleName | string | Yes | No | Name of the HAP file to which the ability belongs. |
| process | string | Yes | No | Process name of the ability. |
| targetAbility | string | Yes | No | 
Target ability that the ability alias points to.

**Model restriction**: This API can be used only in the FA model.

 |
| backgroundModes | number | Yes | No | 

Background service mode of the ability.

**Model restriction**: This API can be used only in the FA model.

 |
| isVisible | boolean | Yes | No | Whether the ability can be called by other applications. **true** if the ability can be called by other applications, **false** otherwise. |
| formEnabled | boolean | Yes | No | 

Whether the ability provides the service widget capability. **true** if the ability provides the service widget capability, **false** otherwise.

**Model restriction**: This API can be used only in the FA model.

 |
| type | bundle.AbilityType | Yes | No | 

Ability type.

**Model restriction**: This API can be used only in the FA model.

 |
| orientation | [bundle.DisplayOrientation](../../ohos-bundle-bundle-module/document.md#displayorientationdeprecated) | Yes | No | Ability display orientation. |
| launchMode | [bundle.LaunchMode](../../ohos-bundle-bundle-module/document.md#launchmodedeprecated) | Yes | No | Ability launch mode. |
| permissions | Array<string> | Yes | No | 

Permissions required for other applications to call the ability.

The value is obtained by passing in GET\_ABILITY\_INFO\_WITH\_PERMISSION to [bundle.getAbilityInfo](../../ohos-bundle-bundle-module/document.md#bundlegetabilityinfodeprecated).

 |
| deviceTypes | Array<string> | Yes | No | Device types supported by the ability. |
| deviceCapabilities | Array<string> | Yes | No | Device capabilities required for the ability. |
| readPermission | string | Yes | No | 

Permission required for reading the ability data.

**Model restriction**: This API can be used only in the FA model.

 |
| writePermission | string | Yes | No | 

Permission required for writing data to the ability.

**Model restriction**: This API can be used only in the FA model.

 |
| applicationInfo | [ApplicationInfo](../applicationinfo/document.md) | Yes | No | 

Application configuration information.

The value is obtained by passing in GET\_ABILITY\_INFO\_WITH\_APPLICATION to [bundle.getAbilityInfo](../../ohos-bundle-bundle-module/document.md#bundlegetabilityinfodeprecated).

 |
| uri | string | Yes | No | 

URI of the ability.

**Model restriction**: This API can be used only in the FA model.

 |
| labelId | number | Yes | No | ID of the ability label. |
| subType | bundle.AbilitySubType | Yes | No | 

Subtype of the template that can be used by the ability.

**Model restriction**: This API can be used only in the FA model.

 |
| metaData8+ | Array<[CustomizeData](../customizedata/document.md)\> | Yes | No | 

Metadata of the ability.

The value is obtained by passing in GET\_ABILITY\_INFO\_WITH\_METADATA to [bundle.getAbilityInfo](../../ohos-bundle-bundle-module/document.md#bundlegetabilityinfodeprecated).

 |
| enabled8+ | boolean | Yes | No | Whether the ability is enabled. **true** if enabled, **false** otherwise. |
