# Skill

The module defines a skill object. Such an object can be obtained through [bundleManager.getBundleInfoForSelf](../../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundleinfoforself), with at least **GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE**, **GET\_BUNDLE\_INFO\_WITH\_ABILITY**, and **GET\_BUNDLE\_INFO\_WITH\_SKILL** passed in to **bundleFlags**. (The skill information is contained in [BundleInfo](../bundleinfo/document.md) -> [HapModuleInfo](../hapmoduleinfo/document.md) -> [AbilityInfo](../abilityinfo/document.md) or [ExtensionAbilityInfo](../extensionabilityinfo/document.md).)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/fh1URTtlS0mKQjYmPKQBZg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062211Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=38AD3EB6E1D5AB68465E3B9C2B579D8E0AAA9FCEA7C6F7CDFA30D5AE92D77602)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { bundleManager } from '@kit.AbilityKit';

#### Skill

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| actions | Array<string> | Yes | No | [Actions](../../../apis-no-longer-maintained/ohos-ability-wantconstant-wantconstant/document.md#action) received by the skill. |
| entities | Array<string> | Yes | No | [Entities](../../../apis-no-longer-maintained/ohos-ability-wantconstant-wantconstant/document.md#entity) received by the skill. |
| uris | Array<SkillUri> | Yes | No | URIs that match Want. |
| domainVerify | boolean | Yes | No | DomainVerify value received by the skill. This parameter exists only in **AbilityInfo** and specifies whether domain name verification is enabled. **true** if enabled, **false** otherwise. |

#### SkillUri

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| scheme | string | Yes | No | Scheme of the URI, such as HTTP, HTTPS, file, and FTP. |
| host | string | Yes | No | Host address of the URI. This parameter takes effect only when **scheme** is specified. |
| port | number | Yes | No | Port number of the URI. This parameter takes effect only when both **scheme** and **host** are specified. |
| path | string | Yes | No | Path of the URI. This parameter takes effect only when both **scheme** and **host** are specified. |
| pathStartWith | string | Yes | No | Prefix of the path of the URI. This parameter takes effect only when both **scheme** and **host** are specified. |
| pathRegex | string | Yes | No | Regular expression of the path of the URI. This parameter takes effect only when both **scheme** and **host** are specified. |
| type | string | Yes | No | Data type that matches the want. The value complies with the Multipurpose Internet Mail Extensions (MIME) and [UniformDataType](../../../../../arkdata/arkts-apis/ohos-data-uniformtypedescriptor-uniform-data-definition-and-description/document.md) type specifications. |
| utd | string | Yes | No | Standard data type of the URI that matches Want. This parameter applies to sharing scenarios. |
| maxFileSupported | number | Yes | No | Maximum number of files of a specified type that can be received or opened at a time. The value must be an integer greater than or equal to 0. |
| linkFeature | string | Yes | No | [Feature type](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-uri-config#description-of-linkfeature) provided by the URI. It is used to implement redirection between applications and exists only in **AbilityInfo**. |
