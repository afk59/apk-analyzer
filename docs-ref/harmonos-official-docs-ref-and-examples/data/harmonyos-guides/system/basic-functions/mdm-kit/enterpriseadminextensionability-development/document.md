# EnterpriseAdminExtensionAbility Development

#### Introduction

**EnterpriseAdminExtensionAbility** is an essential component for device administrator applications. When developing an MDM device administrator application, you need to create an **EnterpriseAdminExtensionAbility** instance and implement MDM service logic in this instance. **EnterpriseAdminExtensionAbility** implements notifications of system management status changes and defines the callbacks to be invoked when a device administrator application is enabled or disabled or an application is installed or uninstalled.

#### Available APIs

The following lists the APIs used in this example. For details about more APIs and their usage, see [@ohos.enterprise.EnterpriseAdminExtensionAbility (EnterpriseAdminExtensionAbility)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-enterpriseadminextensionability).

| API | Description |
| :-- | :-- |
| [onAdminEnabled(): void](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-enterpriseadminextensionability#enterpriseadminextensionabilityonadminenabled) | Called when a device administrator application is enabled. |
| [onAdminDisabled(): void](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-enterpriseadminextensionability#enterpriseadminextensionabilityonadmindisabled) | Called when a device administrator application is disabled. |
| [onBundleAdded(bundleName: string): void](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-enterpriseadminextensionability#enterpriseadminextensionabilityonbundleadded) | Called when an application is installed. |
| [onBundleRemoved(bundleName: string): void](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-enterpriseadminextensionability#enterpriseadminextensionabilityonbundleremoved) | Called when an application is uninstalled. |

#### How to Develop

Create a project. The project structure is as follows.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/RbKML9ZXT3Cm53ewQpl8XQ/en-us_image_0000002568684821.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E3EFDC8A3A1E4B9C8C024F4CEC12D66CDA2444E897D3D8B81DA6122A1057EE2)

Create an **ExtensionAbility** of the **EnterpriseAdmin** type, that is, an **EnterpriseAdminExtensionAbility** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/tCiQt6rEQsSnD8MawuNTGA/en-us_image_0000002568764831.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F7E20477BEB9B2A7C045B0897D6C1D320EA878AFFDC36A2B79757F24846E772)

Open the **EnterpriseAdminAbility.ets** file, import the **EnterpriseAdminExtensionAbility** module, enable it to inherit from the **EnterpriseAdminExtensionAbility** module, and define callbacks, such as **onAdminEnabled()** and **onAdminDisabled()**. When the device administrator application is enabled or disabled, the callback will be invoked to receive notifications.

import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';
// ···

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
// ···

  // Callback to be invoked when the device administrator application is enabled. Initialization policy can be set in this callback.
  onAdminEnabled() {
    console.info('onAdminEnabled');
    // ···
  }

  // Callback to be invoked when the device administrator application is disabled. This callback can be used to notify the enterprise administrator application that the device is no longer under management.
  onAdminDisabled() {
    console.info('onAdminDisabled');
    // ···
  }

  // Callback to be invoked when an application is installed. This callback can be used to report events.
  onBundleAdded(bundleName: string) {
    console.info('EnterpriseAdminAbility onBundleAdded bundleName:' + bundleName);
  }

  // Callback to be invoked when an application is uninstalled. This callback can be used to report events.
  onBundleRemoved(bundleName: string) {
    console.info('EnterpriseAdminAbility onBundleRemoved bundleName' + bundleName);
  }
};

In the [module.json5](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) file of the project module, register **EnterpriseAdminAbility** as **ExtensionAbility**, and set **type** to **enterpriseAdmin** and **srcEntry** to the code path of the **ExtensionAbility** component.

"extensionAbilities": \[
  {
    "name": "EnterpriseAdminAbility",
    "type": "enterpriseAdmin",
    "exported": true,
    "srcEntry": "./ets/enterpriseadminability/EnterpriseAdminAbility.ets"
  }
\],
