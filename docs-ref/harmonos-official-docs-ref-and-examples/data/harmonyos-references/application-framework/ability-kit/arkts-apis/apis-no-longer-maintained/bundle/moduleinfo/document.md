# ModuleInfo

The ModuleInfo module provides module information of an application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/2XTJ3oD6TvW3Rnb5gnSz0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A60CEAE04E1722F7002575BC1B15E2B2573A771F6A7893015792E01E3CF2BF9)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module have been deprecated since API version 9. You are advised to use [bundleManager-HapModuleInfo](../../../dependent-elements-and-definitions/bundlemanager/hapmoduleinfo/document.md) instead.

#### ModuleInfo(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/eTLwI78ETNK_1me2kvQqnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062212Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC3D7634D3299676ADDEE1A45258C01D4FB193FA080960453327EBBB5CA3EF7E)

This API has been supported since API version 7 and deprecated since API version 9. You are advised to use [bundleManager-HapModuleInfo](../../../dependent-elements-and-definitions/bundlemanager/hapmoduleinfo/document.md#hapmoduleinfo-1) instead.

**System capability**: SystemCapability.BundleManager.BundleFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| moduleName | string | Yes | No | Module name. |
| moduleSourceDir | string | Yes | No | Installation directory. Do not access resource files using concatenated paths. Use [@ohos.resourceManager](../../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md) instead. |
