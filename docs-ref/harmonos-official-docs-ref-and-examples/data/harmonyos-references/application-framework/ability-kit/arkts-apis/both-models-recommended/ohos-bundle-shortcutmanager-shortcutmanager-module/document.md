# @ohos.bundle.shortcutManager (shortcutManager Module)

The module provides APIs to manage [shortcuts](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/typical-scenario-configuration), including whether to display shortcuts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/pBTCHrmbSPq48UlVdJOEDg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062208Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32F6499722BFD31983C60B1E19FDD2E0B99F7FFB159B23C75ED3824EA820189E)

The initial APIs of this module are supported since API version 20. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { shortcutManager } from '@kit.AbilityKit';

#### shortcutManager.setShortcutVisibleForSelf

setShortcutVisibleForSelf(id: string, visible: boolean) : Promise<void>

Sets whether to display the specified shortcut for the current application. This API uses a promise to return the result.

**System capability**: SystemCapability.BundleManager.BundleFramework.Launcher

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Shortcut ID, which is the value of the **shortcutId** field under the **shortcuts** tag in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file. The value is a string of up to 63 bytes. |
| visible | boolean | Yes | Whether to display the shortcut. **true** to display, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Bundle Error Codes](../../../error-codes/bundle-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17700070 | The specified shortcut id is illegal. |

**Example**

import { shortcutManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Replace it with the shortcutId field under the shortcuts tag of the module.json5 file.
shortcutManager.setShortcutVisibleForSelf("shortcut\_id", false)
  .then(() => {
    console.info('setShortcutVisibleForSelf success');
  }).catch((err: BusinessError) => {
  console.error(\`setShortcutVisibleForSelf errData is errCode:${err.code}  message:${err.message}\`);
});

#### shortcutManager.getAllShortcutInfoForSelf

getAllShortcutInfoForSelf(): Promise<Array<ShortcutInfo>>

Obtains all the shortcut information defined in the [configuration](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#shortcuts) file of the current application. This API uses a promise to return the result.

**System capability**: SystemCapability.BundleManager.BundleFramework.Launcher

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[ShortcutInfo](../../dependent-elements-and-definitions/bundlemanager/shortcutinfo/document.md)\>> | Promise that returns all the shortcut information defined in the configuration file. |

**Example**

import { shortcutManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

shortcutManager.getAllShortcutInfoForSelf()
  .then((data: shortcutManager.ShortcutInfo\[\]) => {
    console.info('getAllShortcutInfoForSelf shortcut data is' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
  console.error(\`getAllShortcutInfoForSelf errData is errCode:${err.code}  message:${err.message}\`);
});

#### ShortcutInfo

type ShortcutInfo = \_ShortcutInfo

Defines the shortcut information defined in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#shortcuts) file of the application.

**System capability**: SystemCapability.BundleManager.BundleFramework.Launcher

| Type | Description |
| :-- | :-- |
| [\_ShortcutInfo](../../dependent-elements-and-definitions/bundlemanager/shortcutinfo/document.md#shortcutinfo-1) | Shortcut information defined in the configuration file. |

#### ShortcutWant

type ShortcutWant = \_ShortcutWant

Defines the target [wants](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#wants) defined in the shortcut configuration.

**System capability**: SystemCapability.BundleManager.BundleFramework.Launcher

| Type | Description |
| :-- | :-- |
| [\_ShortcutWant](../../dependent-elements-and-definitions/bundlemanager/shortcutinfo/document.md#shortcutwant) | Target [wants](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#wants) defined in the shortcut configuration. |

#### ParameterItem

type ParameterItem = \_ParameterItem

Defines the custom data in the shortcut configuration.

**System capability**: SystemCapability.BundleManager.BundleFramework.Launcher

| Type | Description |
| :-- | :-- |
| [\_ParameterItem](../../dependent-elements-and-definitions/bundlemanager/shortcutinfo/document.md#parameteritem) | Custom data in the shortcut configuration. |
