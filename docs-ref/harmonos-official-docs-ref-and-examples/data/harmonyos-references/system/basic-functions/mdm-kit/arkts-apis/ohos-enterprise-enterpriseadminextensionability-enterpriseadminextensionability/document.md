# @ohos.enterprise.EnterpriseAdminExtensionAbility (EnterpriseAdminExtensionAbility)

This module provides the [EnterpriseAdminExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-term#enterpriseadminextensionability).

To have the capabilities provided by this module, for example, to receive a notification when a device administrator application is enabled or disabled, you need to create an **EnterpriseAdminExtensionAbility** instance for the device administrator application and overload related APIs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/XKP_16OfTjGLMoTTnCQ_cQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062406Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D3657B4229E8A58F94EEFDAB515E8245D105385CF26CB8FC01C7E983C3E3797)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module can be used only in the stage model.
    

#### Modules to Import

import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

#### EnterpriseAdminExtensionAbility.onAdminEnabled

onAdminEnabled(): void

Called when the device administrator application is enabled by the enterprise administrator or employee. Upon receiving the event notification from the system, the device administrator application can set initialization policies in this callback.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Example**

import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onAdminEnabled() {
  }
};

#### EnterpriseAdminExtensionAbility.onAdminDisabled

onAdminDisabled(): void

Called when the device administrator application is disabled by the enterprise administrator or employee. Upon receiving the event notification from the system, the device administrator application can use this callback to notify the enterprise administrator that the device is no longer under management.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Example**

import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onAdminDisabled() {
  }
};

#### EnterpriseAdminExtensionAbility.onBundleAdded

onBundleAdded(bundleName: string): void

Called when applications are installed. The application bundle name is included. You should register the **MANAGED\_EVENT\_BUNDLE\_ADDED** event through [adminManager.subscribeManagedEventSync](../ohos-enterprise-adminmanager-administrator-permission-management/document.md#adminmanagersubscribemanagedeventsync). The enterprise administrator application can subscribe to application installation events. When an application is installed on an enterprise device, the device administrator application reports the event in this callback to notify the enterprise administrator.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name of the application installed. |

**Example**

import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onBundleAdded(bundleName: string) {
    console.info(\`Succeeded in calling onBundleAdded callback, added bundle name : ${bundleName}\`);
  }
};

#### EnterpriseAdminExtensionAbility.onBundleAdded14+

onBundleAdded(bundleName: string, accountId: number): void

Called when applications are installed. The application bundle name and account ID are included. You should register the **MANAGED\_EVENT\_BUNDLE\_ADDED** event through [adminManager.subscribeManagedEventSync](../ohos-enterprise-adminmanager-administrator-permission-management/document.md#adminmanagersubscribemanagedeventsync). The enterprise administrator application can subscribe to application installation events. When an application is installed on an enterprise device, the device administrator application reports the event in this callback to notify the enterprise administrator.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name of the application installed. |
| accountId | number | Yes | Account ID of the application installed. |

**Example**

import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  // Since there is another callback method with the same name onBundleAdded(bundleName: string) that lacks the accountId parameter, accountId must be marked as optional in actual invocations. Please refer to the sample code for the proper syntax. Removing the question mark (?) following accountId will cause a compilation error.
  onBundleAdded(bundleName: string, accountId?: number) {
    console.info(\`Succeeded in calling onBundleAdded callback, added bundle name : ${bundleName}, accountId: ${accountId}\`);
  }
};

#### EnterpriseAdminExtensionAbility.onBundleRemoved

onBundleRemoved(bundleName: string): void

Called when applications are uninstalled. The application bundle name is included. You should register the **MANAGED\_EVENT\_BUNDLE\_REMOVED** event through [adminManager.subscribeManagedEventSync](../ohos-enterprise-adminmanager-administrator-permission-management/document.md#adminmanagersubscribemanagedeventsync). The enterprise administrator application can subscribe to application uninstallation events. When an application is uninstalled from an enterprise device, the device administrator application reports the event in this callback to notify the enterprise administrator.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name of the application uninstalled. |

**Example**

import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onBundleRemoved(bundleName: string) {
    console.info(\`Succeeded in calling onBundleRemoved callback, removed bundle name : ${bundleName}\`);
  }
};

#### EnterpriseAdminExtensionAbility.onBundleRemoved14+

onBundleRemoved(bundleName: string, accountId: number): void

Called when applications are uninstalled. The application bundle name and account ID are included. You should register the **MANAGED\_EVENT\_BUNDLE\_REMOVED** event through [adminManager.subscribeManagedEventSync](../ohos-enterprise-adminmanager-administrator-permission-management/document.md#adminmanagersubscribemanagedeventsync). The enterprise administrator application can subscribe to application uninstallation events. When an application is uninstalled from an enterprise device, the device administrator application reports the event in this callback to notify the enterprise administrator.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name of the application uninstalled. |
| accountId | number | Yes | Account ID of the application uninstalled. |

**Example**

import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  // Since there is another callback method with the same name onBundleRemoved(bundleName: string) that lacks the accountId parameter, accountId must be marked as optional in actual invocations. Please refer to the sample code for the proper syntax. Removing the question mark (?) following accountId will cause a compilation error.
  onBundleRemoved(bundleName: string, accountId?: number) {
    console.info(\`Succeeded in calling onBundleRemoved callback, removed bundle name : ${bundleName}, accountId: ${accountId}\`);
  }
};

#### EnterpriseAdminExtensionAbility.onAppStart

onAppStart(bundleName: string): void

Called when an application is started. You should register the **MANAGED\_EVENT\_APP\_START** event through [adminManager.subscribeManagedEventSync](../ohos-enterprise-adminmanager-administrator-permission-management/document.md#adminmanagersubscribemanagedeventsync). The enterprise administrator application can subscribe to application start events. When an application is started on an enterprise device, the device administrator application reports the event in this callback to notify the enterprise administrator.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name of the application started. |

**Example**

import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onAppStart(bundleName: string) {
    console.info(\`Succeeded in calling onAppStart callback, started bundle name : ${bundleName}\`);
  }
};

#### EnterpriseAdminExtensionAbility.onAppStop

onAppStop(bundleName: string): void

Called when an application is stopped. You should register the **MANAGED\_EVENT\_APP\_STOP** event through [adminManager.subscribeManagedEventSync](../ohos-enterprise-adminmanager-administrator-permission-management/document.md#adminmanagersubscribemanagedeventsync). The enterprise administrator application can subscribe to application stop events. When an application is stopped on an enterprise device, the device administrator application reports the event in this callback to notify the enterprise administrator.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name of the application stopped. |

**Example**

import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onAppStop(bundleName: string) {
    console.info(\`Succeeded in calling onAppStop callback, stopped bundle name : ${bundleName}\`);
  }
};

#### EnterpriseAdminExtensionAbility.onSystemUpdate

onSystemUpdate(systemUpdateInfo: systemManager.SystemUpdateInfo): void

Called to report a system update event. You should register the **MANAGED\_EVENT\_SYSTEM\_UPDATE** event through [adminManager.subscribeManagedEventSync](../ohos-enterprise-adminmanager-administrator-permission-management/document.md#adminmanagersubscribemanagedeventsync). The enterprise administrator application can subscribe to application update events. When an application is updated on an enterprise device, the device administrator application reports the event in this callback to notify the enterprise administrator.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| systemUpdateInfo | [systemManager.SystemUpdateInfo](../ohos-enterprise-systemmanager-system-management/document.md#systemupdateinfo) | Yes | Information about the version update. |

**Example**

import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';
import { systemManager } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onSystemUpdate(systemUpdateInfo: systemManager.SystemUpdateInfo) {
    console.info(\`Succeeded in calling onSystemUpdate callback, version name  : ${systemUpdateInfo.versionName}\`);
  }
};

#### EnterpriseAdminExtensionAbility.onStart

onStart(): void

Called when EnterpriseAdminExtensionAbility starts.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Example**

import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onStart() {
    console.info(\`Succeeded in calling onStart callback.\`);
  }
};

#### EnterpriseAdminExtensionAbility.onAccountAdded18+

onAccountAdded(accountId: number): void

Called when a system account is added. You should register the **MANAGED\_EVENT\_ACCOUNT\_ADDED** event through [adminManager.subscribeManagedEventSync](../ohos-enterprise-adminmanager-administrator-permission-management/document.md#adminmanagersubscribemanagedeventsync). The enterprise administrator application can subscribe to system account add events. When a system account is added to an enterprise device, the device administrator application reports the event in this callback to notify the enterprise administrator.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| accountId | number | Yes | Account ID added. |

**Example**

import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onAccountAdded(accountId: number) {
    console.info(\`Succeeded in calling onAccountAdded callback, added accountId: ${accountId}\`);
  }
};

#### EnterpriseAdminExtensionAbility.onAccountSwitched18+

onAccountSwitched(accountId: number): void

Called when the system account is switched. You should register the **MANAGED\_EVENT\_ACCOUNT\_SWITCHED** event through [adminManager.subscribeManagedEventSync](../ohos-enterprise-adminmanager-administrator-permission-management/document.md#adminmanagersubscribemanagedeventsync). The enterprise administrator application can subscribe to system account switch events. When a system account is switched, the device administrator application reports the event in this callback to notify the enterprise administrator.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| accountId | number | Yes | Account ID switched. |

**Example**

import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onAccountSwitched(accountId: number) {
    console.info(\`Succeeded in calling onAccountSwitched callback, switched accountId: ${accountId}\`);
  }
};

#### EnterpriseAdminExtensionAbility.onAccountRemoved18+

onAccountRemoved(accountId: number): void

Called when the system account is removed. You should register the **MANAGED\_EVENT\_ACCOUNT\_REMOVED** event through [adminManager.subscribeManagedEventSync](../ohos-enterprise-adminmanager-administrator-permission-management/document.md#adminmanagersubscribemanagedeventsync). The enterprise administrator application can subscribe to system account removal events. When a system account is removed, the device administrator application reports the event in this callback to notify the enterprise administrator.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| accountId | number | Yes | Account ID removed. |

**Example**

import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onAccountRemoved(accountId: number) {
    console.info(\`Succeeded in calling onAccountRemoved callback, removed accountId: ${accountId}\`);
  }
};

#### EnterpriseAdminExtensionAbility.onKioskModeEntering20+

onKioskModeEntering(bundleName: string, accountId: number): void

Called when an application enters the kiosk mode. This callback contains the application bundle name and account ID.

Kiosk mode is a system-level runtime mode that restricts a device to a single application or a set of applications. It controls the lock screen, status bar, gestures, and key features to prevent users from launching other applications or performing other operations on the device.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name of the application that enters the kiosk mode. |
| accountId | number | Yes | Account ID of the application that enters the kiosk mode. |

**Example**

import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onKioskModeEntering(bundleName: string, accountId: number): void {
    console.info(\`Succeeded in calling onKioskModeEntering callback, bundleName:${bundleName}, accountId:${accountId}\`);
  }
};

#### EnterpriseAdminExtensionAbility.onKioskModeExiting20+

onKioskModeExiting(bundleName: string, accountId: number): void

Called when an application exits the kiosk mode. This callback contains the application bundle name and account ID.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name of the application that exits the kiosk mode. |
| accountId | number | Yes | Account ID of the application that exits the kiosk mode. |

**Example**

import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onKioskModeExiting(bundleName: string, accountId: number): void {
    console.info(\`Succeeded in calling onKioskModeExiting callback, bundleName:${bundleName}, accountId:${accountId}\`);
  }
};

#### EnterpriseAdminExtensionAbility.onMarketAppInstallResult22+

onMarketAppInstallResult(bundleName: string, result: common.InstallationResult): void

Called when an application is installed via the [bundleManager.installMarketApps](../ohos-enterprise-bundlemanager-bundle-management/document.md#bundlemanagerinstallmarketapps22) API. This callback contains the application bundle name and installation result.

**System capability**: SystemCapability.Customization.EnterpriseDeviceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Application bundle name on AppGallery. |
| result | [common.InstallationResult](../ohos-enterprise-common-common-module/document.md#installationresult) | Yes | Installation result. |

**Example**

import { EnterpriseAdminExtensionAbility, common } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onMarketAppInstallResult(bundleName: string, result: common.InstallationResult): void {
    console.info(\`Succeeded in calling onMarketAppInstallResult callback, bundleName:${bundleName}, result:${result}\`);
  }
};
