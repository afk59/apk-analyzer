# NotificationCommonDef

Describes the bundle information of an application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/EEWPjmm2S7qX2Dp38rXInA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=509EB017D84D8BE1FA2CD904AE110311C321CEB0D9F3EBCC2AAB0D9DDF286FA0)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### BundleOption

Describes the **BundleOption** information, that is, the bundle information of an application.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundle | string | No | No | Application name. |
| uid | number | No | Yes | UID of the application, which is obtained from [ApplicationInfo](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/applicationinfo/document.md#applicationinfo-1). The default value is **0**. |

#### GrantedBundleInfo22+

Describes the authorized bundle information.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | No | No | Bundle name of the application. |
| appIndex | number | Yes | No | Index of an application clone, which takes effect only for application clones. The value is obtained from the **appIndex** of [ApplicationInfo](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/applicationinfo/document.md#applicationinfo-1). |
| appName | string | Yes | Yes | Application name, which is obtained from the **label** of [ApplicationInfo](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/applicationinfo/document.md#applicationinfo-1). |
