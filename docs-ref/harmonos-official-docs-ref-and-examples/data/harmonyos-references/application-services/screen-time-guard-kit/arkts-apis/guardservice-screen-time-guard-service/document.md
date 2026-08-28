# GuardService (Screen Time Guard Service)

This module provides guard service APIs of Screen Time Guard Kit, including app authorization APIs, screen time control APIs, and app access restriction APIs.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

**Start version**: 6.0.0(20)

#### Module Import

import { guardService } from '@kit.ScreenTimeGuardKit';

#### GuardServiceErrorCode

Enumerates the error codes related to **GuardService** of Screen Time Guard Kit.

**Model restriction**: This enumeration can be used only in the stage model.

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

INTERNAL\_ERROR

 | 

[1019000001](../arkts-api-error-codes/document.md#section146742215461)

 | 

Internal error.

 |
| 

USER\_NOT\_AUTHORIZED

 | 

[1019000002](../arkts-api-error-codes/document.md#section20689133216551)

 | 

The user has not authorized the app to access this API.

 |
| 

USER\_CANCELED

 | 

[1019000003](../arkts-api-error-codes/document.md#section133431336165512)

 | 

The user canceled the operation.

 |
| 

STRATEGIES\_EXCEED\_LIMIT

 | 

[1019000004](../arkts-api-error-codes/document.md#section53113406554)

 | 

The number of strategies exceeds the upper limit.

 |
| 

STRATEGY\_NAME\_ALREADY\_EXIST

 | 

[1019000005](../arkts-api-error-codes/document.md#section166061643165510)

 | 

Duplicate strategy name.

 |
| 

NONEXISTENT\_STRATEGY

 | 

[1019000006](../arkts-api-error-codes/document.md#section15125164745520)

 | 

The strategy does not exist.

 |
| 

STRATEGY\_ALREADY\_EXECUTED

 | 

[1019000007](../arkts-api-error-codes/document.md#section1826085035513)

 | 

The strategy is executed repeatedly.

 |
| 

STRATEGY\_NOT\_STARTED

 | 

[1019000008](../arkts-api-error-codes/document.md#section730515419559)

 | 

The strategy is not being executed.

 |
| 

INVALID\_PARAM

 | 

[1019000009](../arkts-api-error-codes/document.md#section28550355113)

 | 

Invalid parameter.

**Start version**: 6.0.2(22)

 |

#### requestUserAuth

requestUserAuth(context: common.UIAbilityContext): Promise<void>

Requests user authorization to access guard service APIs of Screen Time Guard Kit. This API returns the result asynchronously through a promise.

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

[common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

**UIAbility** context.

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

**Promise** object. No result is returned.

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

Capability not supported. function requestUserAuth can not work correctly due to limited device capabilities.

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

**Example**:

import { common } from '@kit.AbilityKit';
import { guardService } from '@kit.ScreenTimeGuardKit';

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button("TestRequestUserAuth")
        .onClick(async () => {
          guardService.requestUserAuth(this.getUIContext().getHostContext() as common.UIAbilityContext)
            .then(() => {
              console.info('requestUserAuth invoke success');
            })
        })
    }
  }
}

#### revokeUserAuth

revokeUserAuth(): Promise<void>

Revokes user authorization to access guard service APIs of Screen Time Guard Kit. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Required permission**: ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 6.0.0(20)

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

**Promise** object. No result is returned.

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

Capability not supported. function revokeUserAuth can not work correctly due to limited device capabilities.

 |
| 

1019000001

 | 

Internal error.

 |

**Example**:

import { guardService } from '@kit.ScreenTimeGuardKit';

async function testRevokeUserAuth() {
  await guardService.revokeUserAuth()
    .then(() => {
      console.info('revokeUserAuth invoke success.');
    })
}

#### getUserAuthStatus

getUserAuthStatus(): Promise<AuthStatus>

Obtains the user authorization state. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Required permission**: ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AuthStatus](#section92636497495)\>

 | 

Promise object. The initial state before user authorization is granted is **AUTH\_INIT**, the state after user authorization is granted is **AUTH\_GRANTED**, and the state after user authorization is rejected is **AUTH\_DENIED**.

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

Capability not supported. function getUserAuthStatus can not work correctly due to limited device capabilities.

 |
| 

1019000001

 | 

Internal error.

 |

**Example**:

import { guardService } from '@kit.ScreenTimeGuardKit';

async function testGetUserAuthStatus() {
  guardService.getUserAuthStatus()
    .then((status) => {
      const statusToMsg = \['AUTH\_INIT', 'AUTH\_GRANTED', 'AUTH\_DENIED'\];
      console.info('getUserAuthStatus invoke success. ' + statusToMsg\[status + 1\]);
    })
}

#### AuthStatus

Enumerates the user authorization states.

**Model restriction**: This enumeration can be used only in the stage model.

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

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

AUTH\_INIT

 | 

\-1

 | 

Initial state.

 |
| 

AUTH\_GRANTED

 | 

0

 | 

User authorization is granted.

 |
| 

AUTH\_DENIED

 | 

1

 | 

The authorization request is rejected.

 |

#### AppInfo

App token information.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

appTokens

 | 

string\[\]

 | 

No

 | 

No

 | 

App token array.

A maximum number of 100 tokens are allowed in the array.

CAUTION:

1.  If there are invalid tokens in the token array, only those valid tokens will be taken for display and use.
2.  This array can be an empty array, meaning no app is blocklisted or trustlisted. This is a normal scenario.

 |

#### addGuardStrategy

addGuardStrategy(guardStrategy: GuardStrategy): Promise<void>

Adds a screen time guard strategy. This API returns the result asynchronously through a promise.

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

guardStrategy

 | 

[GuardStrategy](#section188761911193713)

 | 

Yes

 | 

Guard strategy.

CAUTION:

A maximum of 50 guard strategies can be added.

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

**Promise** object. No result is returned.

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

Capability not supported. function addGuardStrategy can not work correctly due to limited device capabilities.

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

1019000004

 | 

The number of strategies exceeds the upper limit.

 |
| 

1019000005

 | 

The strategy name is already existed.

 |

**Example**:

import { guardService } from '@kit.ScreenTimeGuardKit';

async function testAddGuardStrategy() {
  const time: guardService.TimeStrategy = {
    type: guardService.TimeStrategyType.START\_END\_TIME\_TYPE,
    startTime: "08:00",
    endTime: "19:00",
    repeat: \[1,2,3\]
  }
  const info: guardService.AppInfo = {
    appTokens: \[\] // You can call startAppPicker to obtain the app token.
  }
  const strategy: guardService.GuardStrategy = {
    name: "TestStrategy",
    timeStrategy: time,
    appInfo: info,
    appRestrictionType: guardService.RestrictionType.BLOCKLIST\_TYPE
  }
  guardService.addGuardStrategy(strategy)
    .then(() => {
      console.info('addGuardStrategy invoke success.');
    })
}

#### GuardStrategy

Guard strategy object.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

name

 | 

string

 | 

No

 | 

No

 | 

Strategy name. The value can contain a maximum of 64 characters, and only letters, digits, and underscores (\_) are supported.

 |
| 

timeStrategy

 | 

[TimeStrategy](#section7640121574612)

 | 

No

 | 

No

 | 

Screen time guard strategy.

 |
| 

appInfo

 | 

[AppInfo](#section76401996131)

 | 

No

 | 

No

 | 

App information.

 |
| 

appRestrictionType

 | 

[RestrictionType](#section119174813532)

 | 

No

 | 

No

 | 

Restriction type.

 |

#### TimeStrategy

Screen time guard strategy object.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

**Start version**: 6.0.0(20)

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

[TimeStrategyType](#section133401616145119)

 | 

No

 | 

No

 | 

Screen time guard strategy type.

 |
| 

startTime

 | 

string

 | 

No

 | 

Yes

 | 

Start time, in HH:mm format. The value ranges from 00:00 to 23:59.

CAUTION:

This parameter is mandatory when **type** is set to **START\_END\_TIME\_TYPE**.

 |
| 

endTime

 | 

string

 | 

No

 | 

Yes

 | 

End time, in HH:mm format. The value ranges from 00:00 to 23:59.

CAUTION:

This parameter is mandatory when **type** is set to **START\_END\_TIME\_TYPE**.

NOTE:

1\. If the end time is earlier than the start time, this means the time period crosses into the next day.

2\. **startTime** and **endTime** cannot be the same.

 |
| 

totalDuration

 | 

number

 | 

No

 | 

Yes

 | 

Total duration, in minutes. The value ranges from 0 to 1440.

CAUTION:

This parameter is mandatory when **type** is set to **TOTAL\_DURATION\_TYPE**.

 |
| 

repeat

 | 

number\[\]

 | 

No

 | 

Yes

 | 

Repeated execution days. The value ranges from 1 to 7, indicating Monday to Sunday.

If an empty array is passed, the strategy is executed only once.

CAUTION:

This parameter takes effect only when **type** is set to **START\_END\_TIME\_TYPE**.

 |

#### TimeStrategyType

Enumerates the time strategy types.

**Model restriction**: This enumeration can be used only in the stage model.

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

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

START\_END\_TIME\_TYPE

 | 

1

 | 

Start and end time strategy type, indicating that the strategy takes effect within the specified start time and end time. If this strategy type is used, to call the [TimeStrategy](#section7640121574612) API, **startTime** and **endTime** are mandatory, while **totalDuration** is optional.

 |
| 

TOTAL\_DURATION\_TYPE

 | 

2

 | 

Total duration strategy type, indicating the strategy's overall active period, which begins counting after a successful call to the [startGuardStrategy](#section18918313999) API. If this strategy type is used, to call the [TimeStrategy](#section7640121574612) API, **startTime** and **endTime** are optional, while **totalDuration** is mandatory.

 |
| 

INCLUSIVE\_DURATION\_TYPE

 | 

3

 | 

Shared duration strategy type, indicating that all apps associated with the strategy share the same duration quota. After the quota is exceeded, all apps will be subject to time restrictions. The duration begins after a successful call to the [startGuardStrategy](#section18918313999) API. If this strategy type is used, to call the [TimeStrategy](#section7640121574612) API, **startTime** and **endTime** are optional, **totalDuration** is mandatory, and **RestrictionType** must be set to **TRUSTLIST\_TYPE**.

**Start version**: 6.0.2(22)

 |

#### RestrictionType

Enumerates the restriction types.

**Model restriction**: This enumeration can be used only in the stage model.

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

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

TRUSTLIST\_TYPE

 | 

1

 | 

The restrictions are based on the trustlist.

 |
| 

BLOCKLIST\_TYPE

 | 

2

 | 

The restrictions are based on the blocklist.

 |

#### updateGuardStrategy

updateGuardStrategy(strategyName: string, guardStrategy: GuardStrategy): Promise<void>

Updates a screen time guard strategy. This API returns the result asynchronously through a promise.

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

strategyName

 | 

string

 | 

Yes

 | 

Name of the screen time guard strategy to be updated. The value can contain a maximum of 64 characters, and only letters, digits, and underscores (\_) are supported.

 |
| 

guardStrategy

 | 

[GuardStrategy](#section188761911193713)

 | 

Yes

 | 

New screen time guard strategy.

CAUTION:

If you want to change the strategy name, pass the new name to the **name** attribute of **guardStrategy**. The new name cannot be an existing name. Otherwise, error code 401 will be returned.

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

**Promise** object. No result is returned.

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

Capability not supported. function updateGuardStrategy can not work correctly due to limited device capabilities.

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

1019000006

 | 

Nonexistent strategy.

 |

**Example**:

import { guardService } from '@kit.ScreenTimeGuardKit';

async function testUpdateGuardService() {
  const time: guardService.TimeStrategy = {
    type: guardService.TimeStrategyType.START\_END\_TIME\_TYPE,
    startTime: "08:00",
    endTime: "19:00",
    repeat: \[1,2,3,4,5\]
  }
  const info: guardService.AppInfo = {
    appTokens: \[\] // You can call startAppPicker to obtain the app token.
  }
  const strategy: guardService.GuardStrategy = {
    name: "TestStrategyChanged",
    timeStrategy: time,
    appInfo: info,
    appRestrictionType: guardService.RestrictionType.BLOCKLIST\_TYPE
  }
  // You need to add the TestStrategy strategy via addGuardStrategy in advance.
  guardService.updateGuardStrategy("TestStrategy", strategy)
    .then(() => {
      console.info('updateGuardStrategy invoke success.');
    })
}

#### queryGuardStrategies

queryGuardStrategies(): Promise<GuardStrategy\[\]>

Queries all guard strategies of an app. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Required permission**: ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[GuardStrategy\[\]](#section188761911193713)\>

 | 

**Promise** object. **GuardStrategy\[\]** is returned, which is an array of all guard strategies under the app.

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

Capability not supported. function queryGuardStrategies can not work correctly due to limited device capabilities.

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

**Example**:

import { guardService } from '@kit.ScreenTimeGuardKit';

async function testQueryGuardStrategies() {
  guardService.queryGuardStrategies()
    .then((guardStrategy: guardService.GuardStrategy\[\]) => {
      console.info('queryGuardStrategies invoke success, GuardStrategies: ' + guardStrategy);
    })
}

#### removeGuardStrategy

removeGuardStrategy(strategyName: string): Promise<void>

Deletes guard strategies. This API returns the result asynchronously through a promise.

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

strategyName

 | 

string

 | 

Yes

 | 

Screen time guard strategy name. The value can contain a maximum of 64 characters, and only letters, digits, and underscores (\_) are supported.

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

**Promise** object. No result is returned.

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

Capability not supported. function removeGuardStrategy can not work correctly due to limited device capabilities.

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

1019000006

 | 

Nonexistent strategy.

 |

**Example**:

import { guardService } from '@kit.ScreenTimeGuardKit';

async function testRemoveGuardStrategy() {
  await guardService.removeGuardStrategy("TestStrategy")
    .then(() => {
      console.info('removeGuardStrategy invoke success');
    })
}

#### startGuardStrategy

startGuardStrategy(strategyName: string): Promise<void>

Immediately starts the guard strategy specified by a strategy name. This API returns the result asynchronously through a promise.

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

strategyName

 | 

string

 | 

Yes

 | 

Screen time guard strategy name. The value can contain a maximum of 64 characters, and only letters, digits, and underscores (\_) are supported.

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

**Promise** object. No result is returned.

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

Capability not supported. function startGuardStrategy can not work correctly due to limited device capabilities.

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

1019000006

 | 

Nonexistent strategy.

 |
| 

1019000007

 | 

The strategy is already being executed.

 |

**Example**:

import { guardService } from '@kit.ScreenTimeGuardKit';

async function testStartGuardStrategy() {
  guardService.startGuardStrategy("TestStrategy")
    .then(() => {
      console.info('startGuardStrategy invoke success');
    })
}

#### stopGuardStrategy

stopGuardStrategy(strategyName: string): Promise<void>

Immediately stops the guard strategy specified by a strategy name. This API returns the result asynchronously through a promise.

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

strategyName

 | 

string

 | 

Yes

 | 

Screen time guard strategy name. The value can contain a maximum of 64 characters, and only letters, digits, and underscores (\_) are supported.

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

**Promise** object. No result is returned.

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

Capability not supported. function stopGuardStrategy can not work correctly due to limited device capabilities.

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

1019000006

 | 

Nonexistent strategy.

 |
| 

1019000008

 | 

This strategy has not been started yet.

 |

**Example**:

import { guardService } from '@kit.ScreenTimeGuardKit';

async function testStopGuardStrategy() {
  guardService.stopGuardStrategy("TestStrategy")
    .then(() => {
      console.info('stopGuardStrategy invoke success');
    })
}

#### setAppsRestriction

setAppsRestriction(appInfo: AppInfo, restrictionType: RestrictionType): Promise<void>

Adds access restrictions for apps based on the app token array and restriction type (trustlist or blocklist). This API returns the result asynchronously through a promise.

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

appInfo

 | 

[AppInfo](#section76401996131)

 | 

Yes

 | 

A token array of the selected apps.

 |
| 

restrictionType

 | 

[RestrictionType](#section119174813532)

 | 

Yes

 | 

Restriction type.

**TRUSTLIST\_TYPE** indicates that access to apps outside **appInfo** is restricted, and **BLOCKLIST\_TYPE** indicates that access to apps in **appInfo** is restricted.

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

**Promise** object. No result is returned.

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

Capability not supported. function setAppsRestriction can not work correctly due to limited device capabilities.

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

**Example**:

import { guardService } from '@kit.ScreenTimeGuardKit';

async function testSetAppsRestriction() {
  let selectedTokens: string\[\] = \[\]; // You can call startAppPicker to obtain the app token.
  let appInfo: guardService.AppInfo = { appTokens: selectedTokens };
  let restrictionType: guardService.RestrictionType = guardService.RestrictionType.BLOCKLIST\_TYPE;
  guardService.setAppsRestriction(appInfo, restrictionType)
    .then(() => {
      console.info('setAppsRestriction invoke success');
    });
}

#### releaseAppsRestriction

releaseAppsRestriction(appInfo: AppInfo, restrictionType: RestrictionType): Promise<void>

Removes access restrictions for apps based on the app token array and restriction type (trustlist or blocklist). This API returns the result asynchronously through a promise.

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

appInfo

 | 

[AppInfo](#section76401996131)

 | 

Yes

 | 

A token array of the selected apps.

 |
| 

restrictionType

 | 

[RestrictionType](#section119174813532)

 | 

Yes

 | 

Restriction type.

**TRUSTLIST\_TYPE** indicates that access to apps outside **appInfo** is restricted, and **BLOCKLIST\_TYPE** indicates that access to apps in **appInfo** is restricted.

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

**Promise** object. No result is returned.

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

Capability not supported. function releaseAppsRestriction can not work correctly due to limited device capabilities.

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

**Example**:

import { guardService } from '@kit.ScreenTimeGuardKit';

async function testReleaseAppsRestriction() {
  let selectedTokens: string\[\] = \[\]; // You can call startAppPicker to obtain the app token.
  let appInfo: guardService.AppInfo = { appTokens: selectedTokens };
  let restrictionType: guardService.RestrictionType = guardService.RestrictionType.BLOCKLIST\_TYPE;
  guardService.releaseAppsRestriction(appInfo, restrictionType)
    .then(() => {
      console.info('releaseAppsRestriction invoke success');
    });
}
