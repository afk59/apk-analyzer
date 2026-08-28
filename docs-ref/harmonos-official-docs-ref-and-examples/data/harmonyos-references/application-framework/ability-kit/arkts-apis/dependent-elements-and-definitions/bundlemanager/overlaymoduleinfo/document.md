# OverlayModuleInfo

The module provides information about a module with the overlay feature. An application can obtain such information through [overlay.getOverlayModuleInfo](../../../both-models-recommended/ohos-bundle-overlay-overlay-module/document.md#overlaygetoverlaymoduleinfo).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/fL1ZbpE3S9-ZXtxdHa8e8Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC9F69A3EACF65E7B8522FC111289B4327F52CD5F1C6252FF08DFE90E7B8728F)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { overlay } from '@kit.AbilityKit';

#### OverlayModuleInfo

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | Yes | No | Bundle name of the application to which the module with the overlay feature belongs. |
| moduleName | string | Yes | No | Name of the module with the overlay feature. |
| targetModuleName | string | Yes | No | Name of the target module specified by the overlay feature, that is, the name of the module whose resources are to be replaced by the overlay package. |
| priority | number | Yes | No | Priority of the module with the overlay feature. The value is an integer ranging from 1 to 100. A larger value indicates a higher priority. |
| state | number | Yes | No | Whether the module with the overlay feature is [disabled](../../../both-models-recommended/ohos-bundle-overlay-overlay-module/document.md#overlaysetoverlayenabled). The value **0** means that the module with the overlay feature is disabled, and **1** means the opposite. |
