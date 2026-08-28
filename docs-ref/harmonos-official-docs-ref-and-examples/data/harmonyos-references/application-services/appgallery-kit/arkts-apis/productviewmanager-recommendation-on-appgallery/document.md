# productViewManager (Recommendation on AppGallery)

This module provides the capabilities to display the details page of an app or atomic service and to add an app shortcut to the home screen.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/mXKr4BEORs-zeNCxMH5fyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03B676A38E6855FC3323347505B153AB32021F416DE3650EF0A23900D72C0B25)

Exceptions need to be captured when an API is called.

**Start version**: 4.1.0(11)

#### Modules to Import

import { productViewManager } from '@kit.AppGalleryKit';

#### ProductViewCallback

Input parameters to receive the status change during the loading of an app details page.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.Recommendations

**Start version**: 4.1.0(11)

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

onError

 | 

[ErrorCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback)

 | 

No

 | 

Yes

 | 

Callback function to receive the error code generated when an app details page fails to be loaded.

-   **1011**: Failed to launch the app or switch it to the foreground.
-   **1012**: Failed to switch the app to the background.
-   **1013**: Destruction failed.

 |
| 

onAppear

 | 

Callback<void>

 | 

No

 | 

Yes

 | 

Callback function, which will be called when the app details page is successfully displayed.

NOTE:

**Start version**: 5.0.2(14)

 |
| 

onDisappear

 | 

Callback<void>

 | 

No

 | 

Yes

 | 

Callback function, which will be called when the app details page is successfully closed.

NOTE:

**Start version**: 5.0.2(14)

 |

#### ServiceViewCallback

Input parameters to receive the status change during the loading of the page for adding an atomic service widget to the home screen.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.Recommendations

**Start version**: 4.1.0(11)

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

onReceive

 | 

Callback<[ServiceViewReceiveData](#section530571318012)\>

 | 

No

 | 

Yes

 | 

Callback function that returns the result after a user adds the atomic service widget to the home screen by tapping a button on the loaded page.

 |
| 

onError

 | 

[ErrorCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback)

 | 

No

 | 

Yes

 | 

Callback function to receive the error code generated when the page for adding an atomic service widget to the home screen fails to be loaded.

-   **1011**: Failed to launch the atomic service or switch it to the foreground.
-   **1012**: Failed to switch the atomic service to the background.
-   **1013**: Destruction failed.

 |
| 

onAppear

 | 

Callback<void>

 | 

No

 | 

Yes

 | 

Callback function, which will be called when the page for adding an atomic service widget to the home screen is successfully displayed.

NOTE:

**Start version**: 5.0.2(14)

 |
| 

onDisappear

 | 

Callback<void>

 | 

No

 | 

Yes

 | 

Callback function, which will be called when the page for adding an atomic service widget to the home screen is successfully closed.

NOTE:

**Start version**: 5.0.2(14)

 |

#### ServiceViewReceiveData

Callback data about adding an atomic service widget to the home screen.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.Recommendations

**Start version**: 4.1.0(11)

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

result

 | 

[ReceiveDataResult](#section1690663817619)

 | 

Yes

 | 

No

 | 

Result of adding an atomic service widget to the home screen.

 |
| 

msg

 | 

string

 | 

Yes

 | 

No

 | 

Result description of adding an atomic service widget to the home screen.

 |
| 

formInfo

 | 

{\[key: string\]: Object;}

 | 

Yes

 | 

No

 | 

Data about the atomic service widget added to the home screen. The following attributes are mandatory:

-   **bundleName**: package name of the atomic service.
-   **name**: widget name.
-   **abilityName**: ability name.
-   **moduleName**: name of a module in the atomic service.
-   **defaultDimension**: widget dimensions.

 |

#### ReceiveDataResult

Enumerated result codes of adding an atomic service widget to the home screen.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.Recommendations

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SUCCESS

 | 

1000

 | 

Successful.

 |
| 

FAILURE

 | 

1001

 | 

Failed.

 |
| 

EXCEPTION

 | 

1002

 | 

An exception occurred.

 |

#### CheckShortcutResult

Shortcut verification result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.Recommendations

**Start version**: 5.0.2(14)

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

tid

 | 

string

 | 

No

 | 

Yes

 | 

Transaction ID generated based on the app shortcut information. If the shortcut information changes, a new **tid** will be generated each time. Otherwise, the existing **tid** and the remaining time before expiration (specified by **expired**) will be returned.

 |
| 

expired

 | 

number

 | 

No

 | 

Yes

 | 

Remaining time before transaction ID expiration, in milliseconds.

 |
| 

code

 | 

number

 | 

No

 | 

No

 | 

Verification result code. Value **0** indicates that the verification is successful. For details about the failure cause, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

 |
| 

limit

 | 

number

 | 

No

 | 

Yes

 | 

Number of shortcuts that can be added for an app.

 |

#### SKExposure

Registers ad impression data of the attribution source.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.Recommendations

**Start version**: 5.0.2(14)

**Parameters**:

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

adTechId

 | 

string

 | 

No

 | 

No

 | 

Attribution role ID of a distribution platform. This identifier specifies the distribution platform to which the marketing task of the registered attribution source belongs.

This ID is assigned by the app attribution service when a distribution platform [registers an attribution role](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/store-attribution-register#section11218192952612) on the cloud platform of the app attribution service. It has a fixed length of eight characters.

 |
| 

campaignId

 | 

string

 | 

No

 | 

No

 | 

Marketing task ID, which is the ID of the marketing task corresponding to the registered attribution source. The value contains a maximum of six characters.

 |
| 

destinationId

 | 

string

 | 

No

 | 

No

 | 

ID of the app released on AppGallery. The value contains a maximum of 64 characters.

NOTE:

For details about how to obtain your app ID, please refer to [Viewing App Basic Information](https://developer.huawei.com/consumer/en/doc/app/agc-help-appinfo-0000001100014694).

 |
| 

mmpIds

 | 

string\[\]

 | 

No

 | 

Yes

 | 

Attribution role ID of the attribution monitoring platform used in the current ad delivery task. A maximum of two IDs can be configured. Each ID contains eight characters.

If the caller passes the attribution monitoring platform ID, the app attribution service will post back the attribution result to the attribution monitoring platform. Without this ID, the attribution monitoring platform cannot receive the attribution result.

 |
| 

serviceTag

 | 

string

 | 

No

 | 

Yes

 | 

Business information that a distribution platform focuses on, such as creatives and assets. The value should not exceed 32 characters.

The app attribution service will add this parameter to a trustlist (for details, please contact Huawei operations staff) and open it to the distribution platform.

 |
| 

nonce

 | 

string

 | 

No

 | 

No

 | 

Random number without hyphens (-), used for signature calculations. The value of **nonce** is unique for each ad request and has a fixed length of 32 characters.

For the same **adTechId**, a single **nonce** can be used to register the attribution source information of up to five impressions and five clicks.

 |
| 

timestamp

 | 

number

 | 

No

 | 

No

 | 

Unix timestamp in milliseconds, representing the time when the ad is requested, that is, the time when the ad is delivered. Attribution source registration requires that the value not deviate from the current time by more than 10 minutes.

 |
| 

signature

 | 

string

 | 

No

 | 

No

 | 

Signature. A distribution platform or media app generates a signature based on the ad information and [attribution source signature calculation rules](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/appgallery-attribution-appendix-triger#section4208115642013). The value contains a maximum of 800 characters.

 |

**Example**:

import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { productViewManager } from '@kit.AppGalleryKit';

const TAG: string = 'LoadProduct';

@Entry
@Component
struct LoadProduct {
  build() {
    Column() {
      Button("load\_product")
        .onClick(() => {
          try {
            const exposureData: productViewManager.SKExposure = {
              adTechId: '20\*\*\*\*e8',
              campaignId: '123456',
              destinationId: '10\*\*\*\*\*\*',
              mmpIds: \['2f\*\*\*\*5', '2f7\*\*\*5'\],
              serviceTag: '123\*\*\*2',
              nonce: '123\*\*\*2',
              timestamp: 1705536488,
              signature: 'MEQCIEQlmZ\*\*\*\*zKBSE8QnhLTIHZZZ\*\*\*\*ZpRqRxHss65Ko\*\*\*\*JgJKjdrWdkL\*\*\*\*juEx2RmFS7da\*\*\*\*ZRVZ8RyMyUXg=='
            };

            const request: Want = {
              parameters: {
                bundleName: 'com.huawei.hmsapp.books',
                skExposure: exposureData
              }
            };
            productViewManager.loadProduct(this.getUIContext().getHostContext() as common.UIAbilityContext, request, {
              onError: (error: BusinessError) => {
                hilog.error(0, TAG, \`loadProduct onError.code is ${error.code}, message is ${error.message}\`);
              }
            });
          } catch (err) {
            hilog.error(0, TAG, \`loadProduct failed.code is ${err.code}, message is ${err.message}\`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

#### productViewManager.loadProduct

loadProduct(context: common.UIAbilityContext, want: Want, callback?: ProductViewCallback): void

Displays an app details page for users to download the app. This API returns the result through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.Recommendations

**Start version**: 4.1.0(11)

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
| 

want

 | 

[Want](../../../../application-framework/ability-kit/arkts-apis/apis-no-longer-maintained/ability/want/document.md)

 | 

Yes

 | 

Request parameters for displaying an app details page. **parameters** is a mandatory attribute and a structure.

This structure contains two attributes:

-   **bundleName**: name of the app package whose details page needs to be displayed. This attribute is mandatory.
-   **skExposure**: ad impression data passed to register an attribution source. For details, see the sample code.

 |
| 

callback

 | 

[ProductViewCallback](#section1744815172418)

 | 

No

 | 

Input parameter to receive the status change during the loading of an app details page. If this parameter is not specified, the error code cannot be obtained when the app details page fails to be loaded.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

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

**Example**:

import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { productViewManager } from '@kit.AppGalleryKit';

const TAG: string = 'LoadProduct';

@Entry
@Component
struct LoadProduct {
  build() {
    Column() {
      Button("load\_product")
        .onClick(() => {
          try {
            const request: Want = {
              parameters: {
                // Enter the name of the app package to be loaded, for example, **com.huawei.hmsapp.appgallery**.
                bundleName: 'com.xxx'
              }
            };
            productViewManager.loadProduct(this.getUIContext().getHostContext() as common.UIAbilityContext, request, {
              onError: (error: BusinessError) => {
                hilog.error(0, TAG, \`loadProduct onError.code is ${error.code}, message is ${error.message}\`);
              },
              onAppear: () => {
                hilog.info(0, TAG, \`loadProduct onAppear.\`);
              },
              onDisappear: () => {
                hilog.info(0, TAG, \`loadProduct onDisappear.\`);
              }
            });
          } catch (err) {
            hilog.error(0, TAG, \`loadProduct failed.code is ${err.code}, message is ${err.message}\`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

#### productViewManager.loadService

loadService(context: common.UIAbilityContext, want: Want, callback?: ServiceViewCallback): void

Displays an atomic service details page for users to add the atomic service widget to the home screen. This API returns the result through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.Recommendations

**Start version**: 4.1.0(11)

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
| 

want

 | 

[Want](../../../../application-framework/ability-kit/arkts-apis/apis-no-longer-maintained/ability/want/document.md)

 | 

Yes

 | 

Request parameter for loading an atomic service details page. The **uri** parameter is mandatory. Set it to a link for users to add the atomic service widget to the home screen. For details, see the sample code.

NOTE:

For details about how to obtain the link for users to add the atomic service widget to the home screen, please click [here](https://developer.huawei.com/consumer/en/doc/atomic-guides/atomic-applinking).

 |
| 

callback

 | 

[ServiceViewCallback](#section428319231351)

 | 

No

 | 

Input parameters to receive the status change during the loading of an atomic service details page. If this parameter is not specified, no error code is returned when the atomic service details page fails to be loaded. In addition, when the atomic service details page is successfully loaded, the result of adding the atomic service widget to the home screen cannot be obtained.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

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

**Example**:

import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { productViewManager } from '@kit.AppGalleryKit';

const TAG: string = 'LoadService';

@Entry
@Component
struct LoadService {

  build() {
    Column() {
      Button("load\_service")
        .onClick(() => {
          try {
            const request: Want = {
              // Enter the link for users to add an atomic service widget to the home screen.
              uri: 'store://appgallery.huawei.com/oper/addhome?referrer=xxxx&id=xxxx&installType=xxxx&s=xxxx'
            };
            productViewManager.loadService(this.getUIContext().getHostContext() as common.UIAbilityContext, request, {
              onReceive: (data: productViewManager.ServiceViewReceiveData) => {
                hilog.info(0, TAG, \`Succeeded in loading Service onReceive.result is ${data.result}, msg is ${data.msg}\`);
              },
              onError: (error: BusinessError) => {
                hilog.error(0, TAG, \`loadService onError.code is ${error.code}, message is ${error.message}\`)
              },
              onAppear: () => {
                hilog.info(0, TAG, \`loadService onAppear.\`);
              },
              onDisappear: () => {
                hilog.info(0, TAG, \`loadService onDisappear.\`);
              }
            });
          } catch (err) {
            hilog.error(0, TAG, \`loadService failed.code is ${err.code}, message is ${err.message}\`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

#### productViewManager.checkPinShortcutPermitted

checkPinShortcutPermitted(context: common.UIAbilityContext, shortcutId: string, want: Want, labelResName: string, iconResName: string): Promise<CheckShortcutResult>

Checks whether a shortcut can be added to the home screen by verifying with static resources and returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.Recommendations

**Start version**: 5.0.2(14)

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
| 

shortcutId

 | 

string

 | 

Yes

 | 

ID of the shortcut. The value is a string with a maximum of 63 bytes.

 |
| 

want

 | 

[Want](../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md)

 | 

Yes

 | 

Want information of the target displayed after the shortcut is tapped.

 |
| 

labelResName

 | 

string

 | 

Yes

 | 

Label resource index name of the shortcut displayed on the home screen.

 |
| 

iconResName

 | 

string

 | 

Yes

 | 

Icon resource index name of the shortcut displayed on the home screen.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[CheckShortcutResult](#section1548317391199)\>

 | 

Shortcut verification result returned through a promise.

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

1006620001

 | 

System internal error.

 |
| 

1006620002

 | 

Request to service error.

 |
| 

1006620003

 | 

Shortcut id already exists.

 |
| 

1006620004

 | 

The number of shortcuts has reached the maximum.

 |
| 

1006620005

 | 

Shortcut verification failed.

 |

**Example**:

import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { productViewManager } from '@kit.AppGalleryKit';

const TAG: string = 'CheckPinShortcutPermitted';

@Entry
@Component
struct CheckPinShortcutPermitted {

  build() {
    Column() {
      Button("checkPinShortcutPermitted")
        .onClick(() => {
          try {
            const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
            const shortcutId = "id\_test1"; // Corresponds to **shortcutId** configured in the **shortcuts** tag, for example, **"shortcutId": "id\_test1"**.
            const labelResName = "shortcut"; // Corresponds to the label resource index name configured in the **shortcuts** tag, for example, **"label": "$string:shortcut"**.
            const iconResName = "aa\_icon"; // Corresponds to the icon resource index name configured in the **shortcuts** tag, for example, **"icon": "$media:aa\_icon"**.
            const want: Want = {
              bundleName: "com.example.appgallery.kit.demo",
              moduleName: "entry",
              abilityName: "EntryAbility",
              parameters: {
                testKey: "testValue"
              }
            };
            let checkShortcutResult: productViewManager.CheckShortcutResult;
            productViewManager.checkPinShortcutPermitted(uiContext, shortcutId, want, labelResName, iconResName)
              .then((result: productViewManager.CheckShortcutResult) => {
                hilog.info(0x0001, TAG, \`checkPinShortcutPermitted success result is ${JSON.stringify(result)}\`);
                checkShortcutResult = result;
              }).catch((error: BusinessError) => {
              hilog.error(0x0001, TAG, \`checkPinShortcutPermitted error. code is ${error.code}, message is ${error.message}\`);
            })
          } catch (err) {
            hilog.error(0x0001, TAG, \`checkPinShortcutPermitted failed, code is ${err.code}, message is ${err.message}\`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

#### productViewManager.checkPinShortcutPermitted

checkPinShortcutPermitted(context: common.UIAbilityContext, shortcutId: string, want: Want, label: string, foregroundIcon: string, backgroundIcon: string): Promise<CheckShortcutResult>

Checks whether a shortcut can be added to the home screen by verifying with custom resources and returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.Recommendations

**Start version**: 5.0.2(14)

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

Context.

 |
| 

shortcutId

 | 

string

 | 

Yes

 | 

ID of the shortcut. The value is a string with a maximum of 63 bytes.

 |
| 

want

 | 

[Want](../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md)

 | 

Yes

 | 

Want information of the target displayed after the shortcut is tapped.

 |
| 

label

 | 

string

 | 

Yes

 | 

Text of the shortcut name displayed on the home screen. The length cannot exceed 255 characters.

 |
| 

foregroundIcon

 | 

string

 | 

Yes

 | 

Sandbox address for the icon of the shortcut displayed on the home screen. The icon must be in PNG or WebP format and should not exceed 100 KB.

 |
| 

backgroundIcon

 | 

string

 | 

Yes

 | 

Reserved field. Currently, only an empty string can be passed.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[CheckShortcutResult](#section1548317391199)\>

 | 

Shortcut verification result returned through a promise.

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

1006620001

 | 

System internal error.

 |
| 

1006620002

 | 

Request to service error.

 |
| 

1006620003

 | 

Shortcut id already exists.

 |
| 

1006620004

 | 

The number of shortcuts has reached the maximum.

 |
| 

1006620005

 | 

Shortcut verification failed.

 |

**Example**:

import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { productViewManager } from '@kit.AppGalleryKit';

const TAG: string = 'CheckPinShortcutPermitted';

@Entry
@Component
struct CheckPinShortcutPermitted {

  build() {
    Column() {
      Button("checkPinShortcutPermitted")
        .onClick(() => {
          try {
            const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
            const shortcutId = \`shortcutId\_1\`;
            const want: Want = {
              bundleName: "com.example.appgallery.kit.demo",
              moduleName: "entry",
              abilityName: "EntryAbility",
              parameters: {
                testKey: "testValue"
              }
            }
            const label = "shortcut";
            const foregroundIcon = uiContext.filesDir + "/icon.png";
            const backgroundIcon = "";
            let checkShortcutResult: productViewManager.CheckShortcutResult;
            productViewManager.checkPinShortcutPermitted(uiContext, shortcutId, want, label, foregroundIcon, backgroundIcon)
              .then((result: productViewManager.CheckShortcutResult) => {
                hilog.info(0x0001, TAG, \`checkPinShortcutPermitted success result is ${JSON.stringify(result)}\`);
                checkShortcutResult = result;
              }).catch((error: BusinessError) => {
              hilog.error(0x0001, TAG, \`checkPinShortcutPermitted error. code is ${error.code}, message is ${error.message}\`);
            })
          } catch (err) {
            hilog.error(0x0001, TAG, \`checkPinShortcutPermitted failed, code is ${err.code}, message is ${err.message}\`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

#### productViewManager.requestNewPinShortcut

requestNewPinShortcut(context: common.UIAbilityContext, tid: string): Promise<void>

Adds a shortcut to the home screen and returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AppGalleryService.Distribution.Recommendations

**Start version**: 5.0.2(14)

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

Context.

 |
| 

tid

 | 

string

 | 

Yes

 | 

**tid** returned by the shortcut verification result represented by [CheckShortcutResult](#section1548317391199).

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

1006620001

 | 

System internal error.

 |
| 

1006620003

 | 

Shortcut id already exists.

 |
| 

1006620004

 | 

The number of shortcuts has reached the maximum.

 |
| 

1006620005

 | 

Shortcut verification failed.

 |
| 

1006620006

 | 

The shortcut is not verified or has expired.

 |
| 

1006620007

 | 

User refused to add shortcut.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { productViewManager } from '@kit.AppGalleryKit';

const TAG: string = 'RequestNewPinShortcut';

@Entry
@Component
struct RequestNewPinShortcut {

  build() {
    Column() {
      Button("RequestNewPinShortcut")
        .onClick(() => {
          try {
            const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
            const tid = 'xxx'; // Obtain the value through the **checkPinShortcutPermitted** API.
            productViewManager.requestNewPinShortcut(uiContext, tid)
              .then(() => {
                hilog.info(0x0001, TAG, \`requestNewPinShortcut success.\`);
              }).catch((error: BusinessError) => {
              hilog.error(0x0001, TAG, \`requestNewPinShortcut error. code is ${error.code}, message is ${error.message}\`);
            })
          } catch (err) {
            hilog.error(0x0001, TAG, \`requestNewPinShortcut failed, code is ${err.code}, message is ${err.message}\`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
