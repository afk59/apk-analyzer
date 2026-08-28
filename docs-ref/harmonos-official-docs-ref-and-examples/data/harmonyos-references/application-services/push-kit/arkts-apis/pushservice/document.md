# pushService

This module provides basic capabilities of Push Kit, including obtaining and deleting push tokens, binding and unbinding accounts, receiving scenario-specific messages, registering and deregistering token updates, as well as registering and deregistering distributed message reception event listeners.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Push.PushService

**Start version**: 4.0.0(10)

#### Module Import

import { pushService } from '@kit.PushKit';

#### pushService.getToken

getToken(callback: AsyncCallback<string>): void

Obtains a push token. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**System capability**: SystemCapability.Push.PushService

**Start version**: 4.0.0(10)

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

callback

 | 

AsyncCallback<string>

 | 

Yes

 | 

Callback function. If the operation is successful, a 112-character token is obtained and **err** is **undefined**; otherwise, an error object is returned.

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

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

 |
| 

1000900001

 | 

System internal error.

 |
| 

1000900008

 | 

Failed to connect to the push service.

 |
| 

1000900009

 | 

Internal error of the push service.

 |
| 

1000900010

 | 

Illegal application identity.

 |
| 

1000900011

 | 

The network is unavailable.

 |
| 

1000900012

 | 

Push rights are not activated.

 |
| 

1000900013

 | 

Cross-location application is not allowed to obtain the token.

 |
| 

1000900014

 | 

The device does not support getting token.

 |

**Example**:

import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  pushService.getToken((err: BusinessError, data: string) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'Failed to get push token: %{public}d %{public}s', err.code, err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'Succeeded in getting push token');
    }
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to get push token: %{public}d %{public}s', e.code, e.message);
}

#### pushService.getToken

getToken(): Promise<string>

Obtains a push token. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 4.0.0(10)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string>

 | 

Token returned through a promise, which contains 112 characters.

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

1000900001

 | 

System internal error.

 |
| 

1000900008

 | 

Failed to connect to the push service.

 |
| 

1000900009

 | 

Internal error of the push service.

 |
| 

1000900010

 | 

Illegal application identity.

 |
| 

1000900011

 | 

The network is unavailable.

 |
| 

1000900012

 | 

Push rights are not activated.

 |
| 

1000900013

 | 

Cross-location application is not allowed to obtain the token.

 |
| 

1000900014

 | 

The device does not support getting token.

 |

**Example**:

import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  pushService.getToken().then((data: string) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in getting push token.');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Failed to get push token: %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to get push token: %{public}d %{public}s', e.code, e.message);
}

#### pushService.deleteToken

deleteToken(callback: AsyncCallback<void>): void

Deletes a push token. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 4.0.0(10)

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

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object.

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

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

 |
| 

1000900001

 | 

System internal error.

 |
| 

1000900008

 | 

Failed to connect to the push service.

 |
| 

1000900009

 | 

Internal error of the push service.

 |
| 

1000900010

 | 

Illegal application identity.

 |
| 

1000900011

 | 

The network is unavailable.

 |

**Example**:

import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  pushService.deleteToken((err: BusinessError) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'Failed to delete push token: %{public}d %{public}s', err.code, err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'Succeeded in deleting push token.');
    }
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to delete push token: %{public}d %{public}s', e.code, e.message);
}

#### pushService.deleteToken

deleteToken(): Promise<void>

Deletes a push token. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 4.0.0(10)

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

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1000900001

 | 

System internal error.

 |
| 

1000900008

 | 

Failed to connect to the push service.

 |
| 

1000900009

 | 

Internal error of the push service.

 |
| 

1000900010

 | 

Illegal application identity.

 |
| 

1000900011

 | 

The network is unavailable.

 |

**Example**:

import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  pushService.deleteToken().then(() => {
    hilog.info(0x0000, 'testTag', 'Succeeded in deleting push token.');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Failed to delete push token: %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to delete push token: %{public}d %{public}s', e.code, e.message);
}

#### pushService.bindAppProfileId

bindAppProfileId(appProfileType: pushCommon.AppProfileType, appProfileId: string, callback: AsyncCallback<void>): void

Binds the anonymous identifier of an app account. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 4.0.0(10)

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

appProfileType

 | 

pushCommon.[AppProfileType](../pushcommon/document.md#section411410371767)

 | 

Yes

 | 

Bound account type, which can be HUAWEI ID or an account in the app's own account system.

 |
| 

appProfileId

 | 

string

 | 

Yes

 | 

Anonymous identifier of an account. The value cannot be an empty string. You are not advised to use the actual account ID as **appProfileId**. Generate an anonymous identifier that can uniquely map to the account ID. There is no restriction on the generation algorithm. The value contains a maximum of 64 characters.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object.

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

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

 |
| 

1000900001

 | 

System internal error.

 |
| 

1000900008

 | 

Failed to connect to the push service.

 |
| 

1000900009

 | 

Internal error of the push service.

 |
| 

1000900010

 | 

Illegal application identity.

 |
| 

1000900015

 | 

The number of bound profile-app relationships exceeds the maximum.

 |
| 

1000900016

 | 

The os distributed account is not logged in.

 |

**Example**:

import { pushService, pushCommon } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Define the profileId to be bound.
const profileId: string = '1\*\*\*\*9';
try {
  pushService.bindAppProfileId(pushCommon.AppProfileType.PROFILE\_TYPE\_APPLICATION\_ACCOUNT, profileId, (err: BusinessError) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'Failed to bind app profile id: %{public}d %{public}s', err.code, err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'Succeeded in binding app profile id.');
    }
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to bind app profile id: %{public}d %{public}s', e.code, e.message);
}

#### pushService.bindAppProfileId

bindAppProfileId(appProfileType: pushCommon.AppProfileType, appProfileId: string): Promise<void>

Binds the anonymous identifier of an app account. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 4.0.0(10)

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

appProfileType

 | 

pushCommon.[AppProfileType](../pushcommon/document.md#section411410371767)

 | 

Yes

 | 

Bound account type, which can be HUAWEI ID or an account in the app's own account system.

 |
| 

appProfileId

 | 

string

 | 

Yes

 | 

Anonymous identifier of an account. The value cannot be an empty string. You are not advised to use the actual account ID as **appProfileId**. Generate an anonymous identifier that can uniquely map to the account ID. There is no restriction on the generation algorithm. The value contains a maximum of 64 characters.

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

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

 |
| 

1000900001

 | 

System internal error.

 |
| 

1000900008

 | 

Failed to connect to the push service.

 |
| 

1000900009

 | 

Internal error of the push service.

 |
| 

1000900010

 | 

Illegal application identity.

 |
| 

1000900015

 | 

The number of bound profile-app relationships exceeds the maximum.

 |
| 

1000900016

 | 

The os distributed account is not logged in.

 |

**Example**:

import { pushService, pushCommon } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Define the profileId to be bound.
const profileId = '1\*\*\*\*9';
try {
  // Bind the app account.
  pushService.bindAppProfileId(pushCommon.AppProfileType.PROFILE\_TYPE\_APPLICATION\_ACCOUNT, profileId).then(() => {
    hilog.info(0x0000, 'testTag', 'Succeeded in binding app profile id.');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Failed to bind app profile id: %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to bind app profile id: %{public}d %{public}s', e.code, e.message);
}

#### pushService.unbindAppProfileId

unbindAppProfileId(appProfileId: string, callback: AsyncCallback<void>): void

Unbinds the anonymous identifier of an app account. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 4.0.0(10)

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

appProfileId

 | 

string

 | 

Yes

 | 

Anonymous identifier of an account. Set this parameter to the value of **appProfileId** specified in the [bindAppProfileId](#section20575105524912)() call. The value contains a maximum of 64 characters.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object.

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

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

 |
| 

1000900001

 | 

System internal error.

 |
| 

1000900008

 | 

Failed to connect to the push service.

 |
| 

1000900009

 | 

Internal error of the push service.

 |
| 

1000900010

 | 

Illegal application identity.

 |

**Example**:

import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Define the profileId to be unbound.
const profileId: string = '1\*\*\*\*9';
try {
  pushService.unbindAppProfileId(profileId, (err: BusinessError) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'Failed to unbind app profile id: %{public}d %{public}s', err.code, err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'Succeeded in unbinding app profile id.');
    }
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to unbind app profile id: %{public}d %{public}s', e.code, e.message);
}

#### pushService.unbindAppProfileId

unbindAppProfileId(appProfileId: string): Promise<void>

Unbinds the anonymous identifier of an app account. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 4.0.0(10)

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

appProfileId

 | 

string

 | 

Yes

 | 

Anonymous identifier of an account. Set this parameter to the value of **appProfileId** specified in the [bindAppProfileId](#section20575105524912)() call. The value contains a maximum of 64 characters.

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

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

 |
| 

1000900001

 | 

System internal error.

 |
| 

1000900008

 | 

Failed to connect to the push service.

 |
| 

1000900009

 | 

Internal error of the push service.

 |
| 

1000900010

 | 

Illegal application identity.

 |

**Example**:

import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Define the profileId to be unbound.
const profileId: string = '1\*\*\*\*9';
try {
  pushService.unbindAppProfileId(profileId).then(() => {
    hilog.info(0x0000, 'testTag', 'Succeeded in unbinding app profile id.');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Failed to unbind app profile id: %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to unbind app profile id: %{public}d %{public}s', e.code, e.message);
}

#### pushService.PushType

type PushType = 'DEFAULT' |'IM' | 'VoIP' | 'BACKGROUND' | 'EMERGENCY'

Scenario-specific message type. The options are listed in the following table.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 5.0.2(14)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'DEFAULT'

 | 

Notification message.

 |
| 

'IM'

 | 

Text-to-speech message.

 |
| 

'VoIP'

 | 

In-app call message.

 |
| 

'BACKGROUND'

 | 

Background message.

 |
| 

'EMERGENCY'

 | 

Emergency event message.

 |

#### pushService.receiveMessage

receiveMessage(pushType: PushType, ability: Ability, onMessage: Callback<pushCommon.PushPayload>): void

Receives scenario-specific messages from Push Kit.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 4.0.0(10)

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

pushType

 | 

[PushType](#section5507492425)

 | 

Yes

 | 

Scenario-specific message type.

NOTE:

-   **EMERGENCY** in **pushService.PushType**: This option is provided since API version 5.0.0(12). It is used only for special scenarios such as earthquake disasters.
-   **DEFAULT** in **pushService.PushType**: This option is provided since API version 5.0.2(14). For details about the API call sample code, please refer to step 3 in [Processing Notification Messages When the App is Running in the Foreground](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-send-alert#section99251359545).
-   **IM**: text-to-speech message. For details about the API call sample code, please refer to step 3 in [Development Procedure](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-send-extend-noti#section7799156112814).
-   **VoIP**: in-app call message
    
    For details about the API call sample code, please refer to step 2 in [Development Procedure](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-voip#section41452724812).
    
-   **BACKGROUND**: background message
    
    For details about the API call sample code, please refer to step 5 in [Development Procedure](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/push-background#section8986919144115).
    

 |
| 

ability

 | 

[Ability](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-ability-ability-base-class/document.md)

 | 

Yes

 | 

UIAbility.

 |
| 

onMessage

 | 

Callback<pushCommon.[PushPayload](../pushcommon/document.md#section16335431712)\>

 | 

Yes

 | 

Callback function, which returns the scenario-specific message data.

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

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

 |
| 

1000900001

 | 

System internal error.

 |
| 

1000900005

 | 

Messages of the same push type cannot be received repeatedly.

 |

**Example**:

import { UIAbility } from '@kit.AbilityKit';
import { pushService, pushCommon } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// You do not need to add a UIAbility. You can call the API in the **onCreate** method of the original UIAbility. Here, **PushMessageAbility** is used as an example.
export default class PushMessageAbility extends UIAbility {
  // The **onCreate()** API returns the result synchronously and does not support asynchronous callback.
  onCreate(): void {
    try {
      // The **receiveMessage()** method cannot be called immediately after an asynchronous method, as this may affect message reception.
      // Register the BACKGROUND scenario-specific message.
      pushService.receiveMessage('BACKGROUND', this, (data: pushCommon.PushPayload) => {
        // Process the message. You are advised to add a try-catch block for the callback.
        try {
          hilog.info(0x0000, 'testTag', 'Receive background message : %{public}s', JSON.stringify(data));
        } catch (e) {
          let errRes: BusinessError = e as BusinessError;
          hilog.error(0x0000, 'testTag', 'Failed to process data: %{public}d %{public}s', errRes.code, errRes.message);
        }
      });
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, 'testTag', 'Failed to receive message: %{public}d %{public}s', e.code, e.message);
    }
  }
}

#### pushService.on('tokenUpdate')

on(type: 'tokenUpdate', ability: Ability, callback: Callback<string>): void

Registers token update events. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This API is supported on wearables, but does not work on other devices.

**Start version**: 5.1.0(18)

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

Event type. The value is fixed at **'tokenUpdate'**, indicating the token update event.

 |
| 

ability

 | 

[Ability](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-ability-ability-base-class/document.md)

 | 

Yes

 | 

UIAbility, an app component that provides the UI.

 |
| 

callback

 | 

Callback<string>

 | 

Yes

 | 

Callback used to return the token update data. The token length is 112 characters.

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

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

 |
| 

1000900001

 | 

System internal error.

 |

**Example**:

import { UIAbility } from '@kit.AbilityKit';
import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// You do not need to add a UIAbility. You can call the API in the **onCreate** method of the original UIAbility. Here, **PushMessageAbility** is used as an example.
export default class PushMessageAbility extends UIAbility {
  onCreate(): void {
    const callBack = (data: string) => {
      try {
        hilog.info(0x0000, 'testTag', 'update token: %{public}s', data);
      } catch (e) {
        let err: BusinessError = e as BusinessError;
        hilog.error(0x0000, 'testTag', 'Failed to update data: %{public}d %{public}s', err.code, err.message);
      }
    }

    try {
      // Callback for token update event registration.
      pushService.on('tokenUpdate', this, callBack);
      hilog.info(0x0000, 'testTag', 'Register on success');
    } catch (e) {
      let err: BusinessError = e as BusinessError;
      hilog.error(0x0000, 'testTag', 'Register on error: %{public}d %{public}s', err.code, err.message);
    }
  }
}

#### pushService.off('tokenUpdate')

off(type: 'tokenUpdate', callback?: Callback<string>): void

Deregisters token update events. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This API is supported on wearables, but does not work on other devices.

**Start version**: 5.1.0(18)

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

Event type. The value is fixed at **'tokenUpdate'**, indicating the token update event.

 |
| 

callback

 | 

Callback<string>

 | 

No

 | 

Callback for deregistering the tokenUpdate event listener.

Note: If no callback is passed during the deregistration, all callbacks under the tokenUpdate event are deregistered.

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

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

 |
| 

1000900001

 | 

System internal error.

 |

**Example**:

import { UIAbility } from '@kit.AbilityKit';
import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// You do not need to add a UIAbility. You can call the API in the **onDestroy** method of the original UIAbility. Here, **PushMessageAbility** is used as an example.
export default class PushMessageAbility extends UIAbility {
  onDestroy(): void {
    try {
      // Callback for token update event deregistration.
      pushService.off('tokenUpdate');
      hilog.info(0x0000, 'testTag', 'Register off success');
    } catch (e) {
      let err: BusinessError = e as BusinessError;
      hilog.error(0x0000, 'testTag', 'Register off error: %{public}d %{public}s', err.code, err.message);
    }
  }
}

#### pushService.on('distributedMessageReceive')

on(type: 'distributedMessageReceive', callee: Callee, callback: DistributedMessageCallback): void

Registers a distributed message reception event listener. This API returns the result asynchronously through a callback. An app needs to register with the **onCreate()** method of the UIAbility, and can be registered only once. The action corresponding to the UIAbility is **action.ohos.push.distribute.listener**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/RJt-9AfbR2a5tHA1B6uFGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062517Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26C5493FC8CA923C80744592330F3DE46324D8B0BA22C6E2FD57AA5281FE4FA9)

If calling the scenario-specific message reception API ([pushService.receiveMessage](#section125883044911)) and registering the distributed message reception event listener are implemented in the same UIAbility, the **action.ohos.push.distribute.listener** and **action.ohos.push.listener** must be defined in the same **actions** array. In other cases, define the two listeners in **actions** of their respective UIAbility.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

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

Event to be listened. The value is fixed at **'distributedMessageReceive'**, indicating the distributed message reception event.

 |
| 

callee

 | 

[Callee](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md#callee)

 | 

Yes

 | 

Implements callbacks for [caller](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md#caller) notification registration and deregistration. The parameter value is obtained from the UIAbility.

 |
| 

callback

 | 

[DistributedMessageCallback](#section411410371767)

 | 

Yes

 | 

Callback for registering the distributed message reception event listener. The callback is executed asynchronously after a distributed message is received.

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

1000900031

 | 

The same type of callback can be registered only once.

 |
| 

1000900001

 | 

System internal error.

 |

**Example**:

import { UIAbility } from '@kit.AbilityKit';
import { pushService, pushCommon } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class PushMessageAbility extends UIAbility {
  private callback: pushService.DistributedMessageCallback = async (data:  pushCommon.PushPayload) => {
    let resultCode = pushService.ResultCode.SUCCESS;
    try {
      hilog.info(0x0000, 'testTag', 'Distribute message: %{public}s', JSON.stringify(data));
      // Process service logic, for example, publish data to wearables.
    } catch (e) {
      resultCode = pushService.ResultCode.FAILED;
      let errRes: BusinessError = e as BusinessError;
      hilog.error(0x0000, 'testTag', 'Failed to receive distribute data: %{public}d %{public}s', errRes.code, errRes.message);
    }
    // Return the execution result after the processing is complete.
    return { resultCode };
  };

  onCreate(): void {
    try {
      // Register a distributeMessageReceive event listener.
      pushService.on('distributedMessageReceive', this.callee, this.callback);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, 'testTag', 'Register on error: %{public}d %{public}s', e.code, e.message);
    }
  }
}

#### pushService.off('distributedMessageReceive')

off(type: 'distributedMessageReceive', callback?: DistributedMessageCallback): void

Deregisters a distributed message reception event listener. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

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

Event that is listened. The value is fixed at **'distributedMessageReceive'**, indicating the distributed message reception event.

 |
| 

callback

 | 

[DistributedMessageCallback](#section411410371767)

 | 

No

 | 

Callback for deregistering the distributedMessageReceive event listener. After the deregistration, the app cannot receive distributed messages through the callback.

Note: If no callback is passed during the deregistration, all callbacks under the distributedMessageReceive event are deregistered.

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

1000900001

 | 

System internal error.

 |

**Example**:

import { UIAbility } from '@kit.AbilityKit';
import { pushCommon, pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class PushMessageAbility extends UIAbility {
  private callback: pushService.DistributedMessageCallback = async (data:  pushCommon.PushPayload) => {
    let resultCode = pushService.ResultCode.SUCCESS;
    try {
      hilog.info(0x0000, 'testTag', 'Distribute message: %{public}s', JSON.stringify(data));
      // Process service logic, for example, publish data to wearables.
    } catch (e) {
      resultCode = pushService.ResultCode.FAILED;
      let errRes: BusinessError = e as BusinessError;
      hilog.error(0x0000, 'testTag', 'Failed to receive distribute data: %{public}d %{public}s', errRes.code, errRes.message);
    }
    // Return the execution result after the processing is complete.
    return { resultCode };
  };

  onDestroy(): void {
    try {
      // Deregister the distributedMessageReceive event listener.
      pushService.off('distributedMessageReceive', this.callback);
      hilog.info(0x0000, 'testTag', 'Register off success');
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, 'testTag', 'Register off error: %{public}d %{public}s', e.code, e.message);
    }
  }
}

#### DistributedMessageCallback

type DistributedMessageCallback = (PushPayload: pushCommon.PushPayload) => Promise<DistributedMessageResult>

Callback function used in the distributed message reception event.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

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

PushPayload

 | 

pushCommon.[PushPayload](../pushcommon/document.md#section16335431712)

 | 

Yes

 | 

Defines the distributed message data parameters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<DistributedMessageResult>

 | 

[DistributedMessageResult](#section015518411017) object returned through a promise.

 |

#### DistributedMessageResult

Defines the callback type used in the distributedMessageReceive event.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Parameter

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

resultCode

 | 

[ResultCode](#section016942713918)

 | 

No

 | 

No

 | 

Callback execution result, which is of the enumeration type. For details, please refer to [ResultCode](#section016942713918).

 |

#### ResultCode

Enumerates the execution results of [DistributedMessageCallback](#section411410371767).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This enumeration is supported on phones and tablets, but does not work on other devices.

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

SUCCESS

 | 

0

 | 

The execution is successful.

 |
| 

FAILED

 | 

1

 | 

The execution fails.

 |
