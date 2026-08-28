# minorsProtection (Youth Mode)

This module provides capabilities related to the youth mode provided by Account Kit, including enabling or disabling the youth mode, obtaining the youth mode status on the device, and obtaining the age group information. You can call the capabilities of this module to synchronize the device's youth mode status and change the youth mode status in your app accordingly.

**Start version**: 5.0.0(12)

#### Module Import

import { minorsProtection } from '@kit.AccountKit';

#### MinorsProtectionInfo

Information including the youth mode status and age group. Your app can enable or disable its youth mode according to the device's youth mode status and display appropriate content based on the age group information.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

minorsProtectionMode

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether the youth mode is enabled.

**true**: yes

**false**: no

 |
| 

ageGroup

 | 

[AgeGroup](#section397519409416)

 | 

No

 | 

Yes

 | 

Age group information.

NOTE:

1.  This parameter is returned only when the youth mode is enabled.
2.  If the youth mode is enabled and a child account (14 years old or below) in the Chinese mainland is signed in, the age group information may be returned as **\[0, 3)**, **\[3, 8)**, **\[8, 12)**, or **\[12, 16)**. Examples:
    1.  For a child account that is four years old, the age group information is returned as \[3, 8).
    2.  For a child account that is nine years old, the age group information is returned as \[8,12).
3.  If the youth mode is enabled and a non-child account in the Chinese mainland is signed in, the age group information may be returned as **\[0,3)**, **\[3,8)**, **\[8,12)**, **\[12,16)**, or **\[16,18)**. Examples:
    1.  If a 13-year-old temporary user account is created, the age group information is returned as \[12,16).
    2.  If a 17-year-old temporary user account is created, the age group information is returned as \[16,18).

 |

#### AgeGroup

Age group information object. You can display appropriate content based on the age group information in your app.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

lowerAge

 | 

number

 | 

No

 | 

No

 | 

Lower limit (included) of an age group.

NOTE:

The value can be **0**, **3**, **8**, **12**, or **16**.

 |
| 

upperAge

 | 

number

 | 

No

 | 

No

 | 

Upper limit (not included) of an age group.

NOTE:

The value can be **3**, **8**, **12**, **16**, or **18**.

 |

#### MinorsModeErrorCode

Enumerates error codes related to the youth mode.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**Start version**: 5.0.0(12)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

MINORS\_MODE\_NOT\_ENABLED

 | 

[1009900002](../../arkts-error-codes/document.md#section5166694516)

 | 

The youth mode is not enabled.

 |
| 

USER\_CANCELED

 | 

[1009900003](../../arkts-error-codes/document.md#section191691561188)

 | 

The user canceled the operation.

 |
| 

MINORS\_MODE\_ALREADY\_ON

 | 

[1009900005](../../arkts-error-codes/document.md#section35901828161314)

 | 

The youth mode is already enabled.

 |
| 

MINORS\_MODE\_ALREADY\_OFF

 | 

[1009900006](../../arkts-error-codes/document.md#section1451016215158)

 | 

The youth mode is already disabled.

 |
| 

UNSUPPORTED\_ACCOUNT

 | 

[1009900007](../../arkts-error-codes/document.md#section2076682413462)

 | 

The account is not supported.

 |
| 

SERVICE\_NOT\_AVAILABLE

 | 

[1009900011](../../arkts-error-codes/document.md#section13666164864818)

 | 

Service unavailable.

 |

#### supportMinorsMode

supportMinorsMode(): boolean

Checks whether the device environment supports the youth mode. This method is synchronous.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Returns a Boolean value.

**true**: youth mode supported

**false**: youth mode not supported

NOTE:

When a HUAWEI ID outside the Chinese mainland is used or the private space mode is enabled, **false** is returned. In other scenarios, **true** is returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS Error Codes](../../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1001502009](../../arkts-error-codes/document.md#section17561151616317)

 | 

Internal error.

 |

**Example**:

import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
  try {
    const supportMinorsMode: boolean = minorsProtection.supportMinorsMode();
    hilog.info(0x0000, 'testTag', \`Succeeded in getting supportMinorsMode is: ${supportMinorsMode.valueOf()}\`);
  } catch (error) {
    hilog.error(0x0000, 'testTag',
      \`Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}\`);
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the supportMinorsMode interface.');
}

#### getMinorsProtectionInfoSync

getMinorsProtectionInfoSync(): MinorsProtectionInfo

Obtains the youth mode status and age group information in synchronous mode. Your app can enable or disable its youth mode according to the device's youth mode status and display appropriate content based on the age group information.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[MinorsProtectionInfo](#section3551104714566)

 | 

[MinorsProtectionInfo](#section3551104714566) object. It is used to obtain the youth mode status and age group information.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS Error Codes](../../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1001502009](../../arkts-error-codes/document.md#section17561151616317)

 | 

Internal error.

 |

**Example**:

import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
  try {
    if (minorsProtection.supportMinorsMode()) {
      const minorsProtectionInfo: minorsProtection.MinorsProtectionInfo =
        minorsProtection.getMinorsProtectionInfoSync();
    // Obtain the youth mode status.
      const minorsProtectionMode: boolean = minorsProtectionInfo.minorsProtectionMode;
        // If your app frequently uses the youth mode status information, cache the information.
      hilog.info(0x0000, 'testTag',
        \`Succeeded in getting minorsProtectionMode is: ${minorsProtectionMode.valueOf()}\`);
    // The youth mode is enabled. Obtain the age group information.
      if (minorsProtectionMode) {
        const ageGroup: minorsProtection.AgeGroup | undefined = minorsProtectionInfo.ageGroup;
        if (ageGroup) {
          hilog.info(0x0000, 'testTag', \`Succeeded in getting lowerAge is: ${ageGroup.lowerAge}\`);
          hilog.info(0x0000, 'testTag', \`Succeeded in getting upperAge is: ${ageGroup.upperAge}\`);
          // Refresh the content based on the age group. If your app frequently uses the age group information, cache the information.
        }
      } else {
        // The youth mode is not enabled. The app should follow the youth mode status on the device to display all content without age restrictions.
      }
    } else {
      hilog.info(0x0000, 'testTag',
        'The current device environment does not support the youth mode, please check the current device environment.');
    }
  } catch (error) {
    hilog.error(0x0000, 'testTag',
      \`Failed to invoke supportMinorsMode or getMinorsProtectionInfoSync. errCode: ${error.code},
      errMessage: ${error.message}\`);
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the getMinorsProtectionInfoSync interface.');
}

#### getMinorsProtectionInfo

getMinorsProtectionInfo(): Promise<MinorsProtectionInfo>

Obtains the youth mode status and age group information. Your app can enable or disable its youth mode according to the device's youth mode status and display appropriate content based on the age group information. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[MinorsProtectionInfo](#section3551104714566)\>

 | 

[MinorsProtectionInfo](#section3551104714566) object returned through a promise. It is used to obtain the youth mode status and age group information.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS Error Codes](../../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1001502009](../../arkts-error-codes/document.md#section17561151616317)

 | 

Internal error.

 |

**Example**:

import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
  try {
    if (minorsProtection.supportMinorsMode()) {
      minorsProtection.getMinorsProtectionInfo()
        .then((minorsProtectionInfo: minorsProtection.MinorsProtectionInfo) => {
        // Obtain the youth mode status.
          const minorsProtectionMode: boolean = minorsProtectionInfo.minorsProtectionMode;
          // If your app frequently uses the youth mode status information, cache the information.
          hilog.info(0x0000, 'testTag',
            \`Succeeded in getting minorsProtectionMode is: ${minorsProtectionMode.valueOf()}\`);
        // The youth mode is enabled. Obtain the age group information.
          if (minorsProtectionMode) {
            const ageGroup: minorsProtection.AgeGroup | undefined = minorsProtectionInfo.ageGroup;
            if (ageGroup) {
              hilog.info(0x0000, 'testTag', \`Succeeded in getting lowerAge is: ${ageGroup.lowerAge}\`);
              hilog.info(0x0000, 'testTag', \`Succeeded in getting upperAge is: ${ageGroup.upperAge}\`);
              // Refresh the content based on the age group. If your app frequently uses the age group information, cache the information.
            }
          } else {
            // The youth mode is not enabled. The app should follow the youth mode status on the device to display all content without age restrictions.
          }
        })
        .catch((error: BusinessError<Object>) => {
          dealGetMinorsInfoAllError(error);
        });
    } else {
      hilog.info(0x0000, 'testTag',
        'The current device environment does not support the youth mode, please check the current device environment.');
    }
  } catch (error) {
    hilog.error(0x0000, 'testTag',
      \`Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}\`);
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the getMinorsProtectionInfo interface.');
}

function dealGetMinorsInfoAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', \`Failed to getMinorsProtectionInfo. Code: ${error.code}, message: ${error.message}\`);
}

#### verifyMinorsProtectionCredential

verifyMinorsProtectionCredential(context: common.Context): Promise<boolean>

Shows the youth mode password verification screen for the user to verify their identity when they need to adjust settings related to the youth mode. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md#context)

 | 

Yes

 | 

Context.

Contexts supported by apps: [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) and [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md). Apps cannot use [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md) in non-full-screen components such as semi-modal, pop-up, and sub-window components.

Contexts supported by atomic services: [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

Promise object. **true**: The password verification is successful. **false**: The password verification fails.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS Error Codes](../../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

 |
| 

[1001502009](../../arkts-error-codes/document.md#section17561151616317)

 | 

Internal error.

 |
| 

[1009900002](../../arkts-error-codes/document.md#section5166694516)

 | 

The minors mode is not enabled.

 |

**Example**:

import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
  try {
    if (minorsProtection.supportMinorsMode()) {
      // The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
      minorsProtection.verifyMinorsProtectionCredential(this.getUIContext().getHostContext())
        .then((result: boolean) => {
          hilog.info(0x0000, 'testTag', \`Succeeded in getting verify result is: ${result.valueOf()}\`);
        // Check whether the password verification is successful and execute the subsequent process accordingly.
        })
        .catch((error: BusinessError<Object>) => {
          dealVerifyAllError(error);
        });
    } else {
      hilog.info(0x0000, 'testTag',
        'The current device environment does not support the youth mode, please check the current device environment.');
    }
  } catch (error) {
    hilog.error(0x0000, 'testTag',
      \`Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}\`);
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the verifyMinorsProtectionCredential interface.');
}

function dealVerifyAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', \`Failed to verify. Code: ${error.code}, message: ${error.message}\`);
}

#### leadToTurnOnMinorsMode

leadToTurnOnMinorsMode(context: common.Context): Promise<void>

Provides an entry for enabling the youth mode. It is used to show a screen where the user can enable the youth mode. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md#context)

 | 

Yes

 | 

Context.

Contexts supported by apps: [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) and [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md). Apps cannot use [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md) in non-full-screen components such as semi-modal, pop-up, and sub-window components.

Contexts supported by atomic services: [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS Error Codes](../../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

 |
| 

[1001502009](../../arkts-error-codes/document.md#section17561151616317)

 | 

Internal error.

 |
| 

[1009900003](../../arkts-error-codes/document.md#section191691561188)

 | 

The user canceled the operation.

 |
| 

[1009900005](../../arkts-error-codes/document.md#section35901828161314)

 | 

The minors mode is already on.

 |
| 

[1009900007](../../arkts-error-codes/document.md#section2076682413462)

 | 

Unsupported HUAWEI ID.

 |
| 

[1009900011](../../arkts-error-codes/document.md#section13666164864818)

 | 

Service not available.

 |

**Example**:

import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
  try {
    if (minorsProtection.supportMinorsMode()) {
     // The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
      minorsProtection.leadToTurnOnMinorsMode(this.getUIContext().getHostContext())
        .then(() => {
          // The API call is complete. If a pop-up is needed, implement it here.
        })
        .catch((error: BusinessError<Object>) => {
          dealTurnOnAllError(error);
        });
    } else {
      hilog.info(0x0000, 'testTag',
        'The current device environment does not support the youth mode, please check the current device environment.');
    }
  } catch (error) {
    hilog.error(0x0000, 'testTag',
      \`Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}\`);
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the leadToTurnOnMinorsMode interface.');
}

function dealTurnOnAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', \`Failed to leadToTurnOnMinorsMode. Code: ${error.code}, message: ${error.message}\`);
}

#### leadToTurnOffMinorsMode

leadToTurnOffMinorsMode(context: common.Context): Promise<void>

Provides an entry for disabling the youth mode. It is used to show a screen where the user can disable the youth mode. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md#context)

 | 

Yes

 | 

Context.

Contexts supported by apps: [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) and [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md). Apps cannot use [UIExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiextensioncontext/document.md) in non-full-screen components such as semi-modal, pop-up, and sub-window components.

Contexts supported by atomic services: [UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS Error Codes](../../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

 |
| 

[1001502009](../../arkts-error-codes/document.md#section17561151616317)

 | 

Internal error.

 |
| 

[1009900003](../../arkts-error-codes/document.md#section191691561188)

 | 

The user canceled the operation.

 |
| 

[1009900006](../../arkts-error-codes/document.md#section1451016215158)

 | 

The minors mode is already off.

 |
| 

[1009900011](../../arkts-error-codes/document.md#section13666164864818)

 | 

Service not available.

 |

**Example**:

import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
  try {
    if (minorsProtection.supportMinorsMode()) {
     // The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
      minorsProtection.leadToTurnOffMinorsMode(this.getUIContext().getHostContext())
        .then(() => {
          // The API call is complete. If a pop-up is needed, implement it here.
        })
        .catch((error: BusinessError<Object>) => {
          dealTurnOffAllError(error);
        });
    } else {
      hilog.info(0x0000, 'testTag',
        'The current device environment does not support the youth mode, please check the current device environment.');
    }
  } catch (error) {
    hilog.error(0x0000, 'testTag',
      \`Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}\`);
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the leadToTurnOffMinorsMode interface.');
}

function dealTurnOffAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', \`Failed to leadToTurnOffMinorsMode. Code: ${error.code}, message: ${error.message}\`);
}
