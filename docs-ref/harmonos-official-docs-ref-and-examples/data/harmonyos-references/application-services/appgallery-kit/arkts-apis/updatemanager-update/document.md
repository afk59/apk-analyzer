# updateManager (Update)

This module provides the new version detection and update functions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/kfnmuYY5TWapsWPAA2fPMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73233B8424BB39C80277693B649B37372217FD5AEFDA7D0875CB1E2E8A1D62CE)

Exceptions need to be captured when an API is called.

**Start version**: 5.0.0(12)

#### Modules to Import

import { updateManager } from '@kit.AppGalleryKit';

#### UpdateAvailableCode

Enumerated detection result codes.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.AppGalleryService.Distribution.Update

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

LATER\_VERSION\_NOT\_EXIST

 | 

0

 | 

No new version exists.

 |
| 

LATER\_VERSION\_EXIST

 | 

1

 | 

A new version exists.

 |

#### ShowUpdateResultCode

Enumerated result codes of displaying an update pop-up.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.Update

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SHOW\_DIALOG\_SUCCESS

 | 

0

 | 

An update pop-up is successfully displayed.

 |
| 

SHOW\_DIALOG\_FAILURE

 | 

1

 | 

Failed to display an update pop-up.

 |

#### CheckUpdateResult

Result of calling the API that checks whether an update is available.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.AppGalleryService.Distribution.Update

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

updateAvailable

 | 

[UpdateAvailableCode](#section4465197164210)

 | 

Yes

 | 

No

 | 

Check result.

 |
| 

versionName

 | 

string

 | 

Yes

 | 

Yes

 | 

Version name, for example, **1.0.0.1**.

**Start version**: 6.0.0(20)

NOTE:

This parameter is available only for atomic services.

 |
| 

versionCode

 | 

number

 | 

Yes

 | 

Yes

 | 

Version number, for example, **1001**.

**Start version**: 6.0.0(20)

NOTE:

This parameter is available only for atomic services.

 |

#### RequestErrorCode

Enumerated result codes of calling the API for detecting atomic service updates.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.AppGalleryService.Distribution.Update

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

NO\_UPGRADE

 | 

0

 | 

No latest version is available.

 |
| 

NEED\_UPGRADE

 | 

1

 | 

The latest version is available.

 |
| 

DOWNLOADED

 | 

2

 | 

Download completed.

 |

#### UpdateSessionState

Callback result from the API that detects atomic service updates.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.AppGalleryService.Distribution.Update

**Start version**: 6.0.0(20)

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

code

 | 

[RequestErrorCode](#section1713825674019)

 | 

Yes

 | 

No

 | 

Result code.

 |
| 

checkUpdateResult

 | 

[CheckUpdateResult](#section1535385414136)

 | 

Yes

 | 

Yes

 | 

Check result.

NOTE:

This parameter is not empty only when the value of **RequestErrorCode** is **NEED\_UPGRADE** or **NO\_UPGRADE**.

 |

#### updateManager.checkAppUpdate

checkAppUpdate(context: common.UIAbilityContext): Promise<CheckUpdateResult>

Checks whether there is any update. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.Update

**Device behavior differences**: For versions earlier than API version 19, this API can be called on phones, tablets, and PCs/2-in-1 devices. For other device types, the value of **updateAvailable** in **CheckUpdateResult** returned by this API is always **LATER\_VERSION\_NOT\_EXIST**, and the app update status cannot be checked. For API version 19, this API can be called on phones, tablets, PCs/2-in-1 devices, and TVs. For other device types, the value of **updateAvailable** in **CheckUpdateResult** returned by this API is always **LATER\_VERSION\_NOT\_EXIST**, and the app update status cannot be checked. For API version 20 or later, this API can be called on phones, tablets, PCs/2-in-1 devices, TVs, and wearables.

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

[common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

Context of the app that calls the API.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[CheckUpdateResult](#section1535385414136)\>

 | 

Update check result, returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1009400001

 | 

SA connect error.

 |
| 

1009400002

 | 

Request to service error.

 |
| 

1009400003

 | 

Network error.

 |
| 

1009400004

 | 

The application is not in the foreground.

 |
| 

1009400005

 | 

Not agreeing to the privacy agreement.

 |
| 

1009400006

 | 

Time limited.

 |
| 

1009400007

 | 

Other error.

 |

**Example**:

import { updateManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State message: string = 'checkAppUpdate test'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            try {
              updateManager.checkAppUpdate(this.getUIContext().getHostContext() as common.UIAbilityContext)
                .then((checkResult: updateManager.CheckUpdateResult) => {
                  hilog.info(0, 'TAG', "Succeeded in checking Result updateAvailable:" + checkResult.updateAvailable);
                }).catch((error: BusinessError) => {
                hilog.error(0, 'TAG', \`checkAppUpdate onError.code is ${error.code}, message is ${error.message}\`);
              });
            } catch (error) {
              hilog.error(0, 'TAG', \`checkAppUpdate onError.code is ${error.code}, message is ${error.message}\`);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### updateManager.showUpdateDialog

showUpdateDialog(context: common.UIAbilityContext): Promise<ShowUpdateResultCode>

Displays an update pop-up. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.Update

**Device behavior differences**: For versions earlier than API version 19, this API can be called on phones, tablets, and PCs/2-in-1 devices. For other device types, the value of **ShowUpdateResultCode** returned by this API is always **SHOW\_DIALOG\_FAILURE**, and the app update pop-up cannot be displayed. For API version 19, this API can be called on phones, tablets, PCs/2-in-1 devices, and TVs. For other device types, the value of **ShowUpdateResultCode** returned by this API is always **SHOW\_DIALOG\_FAILURE**, and the app update pop-up cannot be displayed. For API version 20 or later, this API can be called on phones, tablets, PCs/2-in-1 devices, TVs, and wearables.

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

[common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

Context of the app that calls the API.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ShowUpdateResultCode](#section194882568246)\>

 | 

Result of the user operation in the update pop-up, returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1009400001

 | 

SA connection error.

 |
| 

1009400002

 | 

Request to service error.

 |
| 

1009400004

 | 

The application is not in the foreground.

 |
| 

1009400005

 | 

Not agreeing to the privacy agreement.

 |
| 

1009400007

 | 

Other error.

 |

**Example**:

import { updateManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State message: string = 'showUpdateDialog test'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            try {
              updateManager.showUpdateDialog(this.getUIContext().getHostContext() as common.UIAbilityContext)
                .then((resultCode: updateManager.ShowUpdateResultCode) => {
                  hilog.info(0, 'TAG', "Succeeded in showing UpdateDialog resultCode:" + resultCode);
                })
                .catch((error: BusinessError) => {
                  hilog.error(0, 'TAG', \`showUpdateDialog onError.code is ${error.code}, message is ${error.message}\`);
                });
            } catch (error) {
              hilog.error(0, 'TAG', \`showUpdateDialog onError.code is ${error.code}, message is ${error.message}\`);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### updateManager.on('updateChange')

on(type: 'updateChange', callback: Callback<UpdateSessionState>, timeout?: number): void

Registers a listener for the atomic service update detection API. If an update is detected, the result will be returned through a callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/M9CAgFlWQECzHK4q-ySl9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5FCF8605E33AB8C9F1835B9340EB845E09CEC07945D4DCBE8CD2A2F22830ABC8)

For the same atomic service, this API can be called for a maximum of six times a day and only once every 30 minutes.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.AppGalleryService.Distribution.Update

**Start version**: 6.0.0(20)

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

type

 | 

string

 | 

Yes

 | 

The value is always **updateChange**.

 |
| 

callback

 | 

Callback<[UpdateSessionState](#section18222589421)\>

 | 

Yes

 | 

Callback function used to return the result.

 |
| 

timeout

 | 

number

 | 

No

 | 

Maximum listening duration supported by the registered listener, in seconds. The value is an integer less than or equal to 20. If no value is passed, the default value **20** will be used.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1009400001

 | 

SA connection error.

 |
| 

1009400002

 | 

Request to service error.

 |
| 

1009400007

 | 

Other error.

 |
| 

1009400008

 | 

The number of parameters for the on API is incorrect.

 |
| 

1009400009

 | 

The type parameter for the on API is invalid.

 |
| 

1009400010

 | 

The callback parameter for the on API is invalid.

 |
| 

1009400011

 | 

The timeout parameter for the on API is invalid.

 |

**Example**:

import { updateManager } from '@kit.AppGalleryKit';
import { abilityManager, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State message: string = 'on'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => this.callOn)
      }
      .width('100%')
    }
    .height('100%')
  }

  private callOn() {
    let callback = (state: updateManager.UpdateSessionState) => {
      if (state.code === updateManager.RequestErrorCode.NO\_UPGRADE) {
        hilog.info (0, 'TAG', \`on success, no need update\`);
        updateManager.off('updateChange');
      } else if (state.code === updateManager.RequestErrorCode.NEED\_UPGRADE) {
        hilog.info (0, 'TAG', \`on success, need update\`);
      } else if (state.code === updateManager.RequestErrorCode.DOWNLOADED) {
        hilog.info (0, 'TAG', \`on success, need update and download success\`);
        updateManager.off('updateChange');
        abilityManager.restartSelfAtomicService(this.getUIContext().getHostContext() as common.Context);
      }
    };
    try {
      updateManager.on('updateChange', callback, 20);
    } catch (error) {
      hilog.error(0, 'TAG', \`on Error.code is ${error.code}, message is ${error.message}\`);
    }
  }
}

#### updateManager.off('updateChange')

off(type: 'updateChange', callback?: Callback<UpdateSessionState>): void

Unregisters the listener for the atomic service update detection API.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.AppGalleryService.Distribution.Update

**Start version**: 6.0.0(20)

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

type

 | 

string

 | 

Yes

 | 

The value is always **updateChange**.

 |
| 

callback

 | 

Callback<[UpdateSessionState](#section18222589421)\>

 | 

No

 | 

Callback function used to return the result. If this parameter is left empty, all listeners of the current app will be canceled.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1009400001

 | 

SA connection error.

 |
| 

1009400002

 | 

Request to service error.

 |
| 

1009400007

 | 

Other error.

 |
| 

1009400012

 | 

The number of parameters for the off API is incorrect.

 |
| 

1009400013

 | 

The type parameter for the off API is invalid.

 |
| 

1009400014

 | 

The callback parameter for the off API is invalid.

 |

**Example**:

import { updateManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
try {
  // Cancel the listener.
  updateManager.off('updateChange');
} catch (error) {
  hilog.error(0, 'TAG', \`moduleInstallManager.off onError.code is ${error.code}, message is ${error.message}\`);
}
