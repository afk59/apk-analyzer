# @ohos.app.ability.kioskManager (Kiosk Mode Management)

The KioskManager module provides APIs to manage kiosk mode, including entering and exiting kiosk mode.

Kiosk mode is a dedicated device lockdown mode that ensures the device UI serves only specific interaction scenarios. In this mode, device usage is confined to predetermined applications. A typical example is a bank ATM, where users can only interact with the ATM software and cannot exit it or access any other functions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/C2T9G3BlS0mlOtAq92rIJQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062208Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=010069BD2E6232AC6648B05585AAEC2C7CE680FA2B7A50C864975AAFFCBB88F5)

-   The initial APIs of this module are supported since API version 20. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in the stage model.
-   The APIs of this module are available only to applications that have been configured to support Kiosk mode via [setAllowedKioskApps](../../../../../system/basic-functions/mdm-kit/arkts-apis/ohos-enterprise-applicationmanager-application-management/document.md#applicationmanagersetallowedkioskapps20).

#### Modules to Import

import { kioskManager } from '@kit.AbilityKit';

#### kioskManager.enterKioskMode

enterKioskMode(context: UIAbilityContext): Promise<void>

Enters kiosk mode. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called only on phones, PC/2-in-1 devices, and tablets. On other devices, it returns the error code 801.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [UIAbilityContext](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md) | Yes | Context of the UIAbility that needs to enter kiosk mode. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 16000050 | Failed to connect to the system service. |
| 16000110 | The current application is not in Kiosk app list and cannot enter Kiosk mode. |
| 16000111 | The system is already in Kiosk mode and cannot enter Kiosk mode again. |
| 16000113 | Current ability is not in foreground. |

**Example**

import { common, kioskManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private uiAbilityContext: common.UIAbilityContext | undefined =
    this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Column() {
      Button('enterKioskMode').margin({ top: 30 })
        .onClick(() => {
          kioskManager.enterKioskMode(this.uiAbilityContext)
            .then(() => {
              hilog.info(0x0000, 'testTag', '%{public}s', 'enterKioskMode success');
            })
            .catch((error: BusinessError) => {
              hilog.error(0x0000, 'testTag', '%{public}s', \`enterKioskMode failed:${JSON.stringify(error)}\`);
            });
        })
    }
    .height('100%')
    .width('100%')
  }
}

#### kioskManager.exitKioskMode

exitKioskMode(context: UIAbilityContext): Promise<void>

Exits kiosk mode. This API uses a promise to return the result.

This API takes effect only for applications that have entered kiosk mode.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called only on phones, PC/2-in-1 devices, and tablets. On other devices, it returns the error code 801.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [UIAbilityContext](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md) | Yes | Context of the UIAbility that needs to exit kiosk mode. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 16000050 | Failed to connect to the system service. |
| 16000110 | The current application is not in Kiosk app list and cannot enter Kiosk mode. |
| 16000112 | The current application is not in Kiosk mode and cannot exit Kiosk mode. |

**Example**

import { common, kioskManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private uiAbilityContext: common.UIAbilityContext | undefined =
    this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Column() {
      Button('exitKioskMode').margin({ top: 10 })
        .onClick(() => {
          kioskManager.exitKioskMode(this.uiAbilityContext)
            .then(() => {
              hilog.info(0x0000, 'testTag', '%{public}s', 'exitKioskMode success');
            })
            .catch((error: BusinessError) => {
              hilog.error(0x0000, 'testTag', '%{public}s', \`exitKioskMode failed:${JSON.stringify(error)}\`);
            });
        })
    }
    .height('100%')
    .width('100%')
  }
}

#### KioskStatus

type KioskStatus = \_KioskStatus

Defines the kiosk status information, including whether the system is in kiosk mode and the information about the application in kiosk mode.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Type | Description |
| :-- | :-- |
| [\_KioskStatus](../../dependent-elements-and-definitions/application/kioskstatus-kiosk-status-information/document.md#kioskstatus) | Kiosk status information, including whether the system is in kiosk mode and the information about the application in kiosk mode. |
