# AppPicker (App Selection Page)

The AppPicker module can start the app selection page and permitted app redirect page.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

**Start version**: 6.0.0(20)

#### Module Import

import { appPicker } from '@kit.ScreenTimeGuardKit';

#### startAppPicker

startAppPicker(context: common.Context, appSelection: guardService.AppInfo): Promise<string\[\]>

Starts the **AppPicker** page in secure mode and displays the app list where the selected apps are marked. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Required permission**: ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

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

context

 | 

[common.Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

**UIAbility** context.

 |
| 

appSelection

 | 

[guardService.AppInfo](../guardservice-screen-time-guard-service/document.md#section76401996131)

 | 

Yes

 | 

Selected apps, which will appear with a checkmark on the **AppPicker** page.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string\[\]>

 | 

**Promise** object. **string\[\]** is returned, which is a token array of the selected apps.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission verification failed. The application does not have the permission required to call the API.

 |
| 

401

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

801

 | 

Capability not supported. function startAppPicker can not work correctly due to limited device capabilities.

 |
| 

1019000001

 | 

Internal error.

 |
| 

1019000002

 | 

The user has not authorized the application to access this interface.

 |
| 

1019000003

 | 

The user canceled the operation.

 |

**Example**:

import { appPicker } from '@kit.ScreenTimeGuardKit';

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button("TestStartAppPicker")
        .onClick(async () => {
          appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: \[\] })
            .then((tokens) => {
              console.info('startAppPicker invoke success' + tokens);
            })
        })
    }
  }
}

#### startAppForm

startAppForm(context: common.Context, appSelection: guardService.AppInfo, appSubTitle: string, displayTrustApp: boolean): Promise<void>

Opens the permitted app redirect page. Upon tapping an app icon, users are redirected to the app. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Required permission**: ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 6.0.2(22)

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

[common.Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

**UIAbility** context.

 |
| 

appSelection

 | 

[guardService.AppInfo](../guardservice-screen-time-guard-service/document.md#section76401996131)

 | 

Yes

 | 

Apps displayed on the permitted app redirect page.

 |
| 

appSubTitle

 | 

string

 | 

Yes

 | 

Subtitle of the permitted app redirect page. The value can contain a maximum of 200 characters.

 |
| 

displayTrustApp

 | 

boolean

 | 

Yes

 | 

Indicates whether to display apps that are unrestricted by default on the redirect page. The value **true** indicates yes and the value **false** indicates no. Currently, only Contacts is unrestricted by default.

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

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission verification failed. The application does not have the permission required to call the API.

 |
| 

801

 | 

Capability not supported. function startAppForm can not work correctly due to limited device capabilities.

 |
| 

1019000001

 | 

Internal error.

 |
| 

1019000002

 | 

The user has not authorized the application to access this interface.

 |
| 

1019000003

 | 

The user canceled the operation.

 |
| 

1019000009

 | 

Parameter error. Possible causes:1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.

 |

**Example**:

import { appPicker } from '@kit.ScreenTimeGuardKit';

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button("TestStartAppForm")
        .onClick(async () => {
          let selectedTokens: string\[\] = \[\]; // You can call startAppPicker to obtain the app token.
          appPicker.startAppForm(this.getUIContext().getHostContext(), { appTokens: selectedTokens }, "TestStartAppForm", false)
            .then(() => {
              console.info('startAppForm invoke success');
            })
        })
    }
  }
}
