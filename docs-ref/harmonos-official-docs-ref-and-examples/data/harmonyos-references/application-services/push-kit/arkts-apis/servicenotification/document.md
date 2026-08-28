# serviceNotification

This module provides basic service notification capabilities, including requesting authorization on notification subscription.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Push.PushService

**Start version**: 4.1.0(11)

#### Module Import

import { serviceNotification } from '@kit.PushKit';

#### serviceNotification.requestSubscribeNotification

requestSubscribeNotification(context: Context, entityIds: Array<string>, callback: AsyncCallback<RequestResult>): void

Requests authorization on notification subscription. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This API is supported on phones, tablets, and PCs/2-in-1 devices. On other devices, it returns error code 1000900017.

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

[Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) of the UI for requesting authorization on notification subscription.

NOTICE:

The context supports only **UIAbilityContext**.

 |
| 

entityIds

 | 

Array<string>

 | 

Yes

 | 

Template ID list.

 |
| 

callback

 | 

AsyncCallback<[RequestResult](#section185441313151716)\>

 | 

Yes

 | 

Callback function. If the operation is successful, **err** is **undefined** and **data** is the subscription authorization result. Otherwise, **err** is an error object.

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

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

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

1000900017

 | 

The device does not support current operation.

 |
| 

1000900018

 | 

Number of calls exceeded.

 |
| 

1000900019

 | 

Illegal entity id.

 |
| 

1000900020

 | 

App token is empty.

 |
| 

1000900021

 | 

App is not available or not registered.

 |
| 

1000900022

 | 

Notification switch off.

 |
| 

1000900023

 | 

Number of entity ids exceed the upper limit.

 |
| 

1000900024

 | 

Failed to display subscription UI.

 |
| 

1000900025

 | 

No rights to access entity id.

 |
| 

1000900026

 | 

Illegal entity type.

 |

**Example**:

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { serviceNotification } from '@kit.PushKit';
import { BusinessError } from '@kit.BasicServicesKit';
const DOMAIN = 0x0000;
export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
    try {
  // Replace **entityIds** with the IDs of the templates to be subscribed to.
      const entityIds = \['entityId1', 'entityId2', 'entityId3'\];
      serviceNotification.requestSubscribeNotification(this.context, entityIds, (err, data) => {
        if (err) {
          hilog.error(0x0000, 'testTag', 'Failed to request subscribe notification: %{public}d %{public}s', err.code,
            err.message);
        } else {
          hilog.info(0x0000, 'testTag', 'Succeeded in requesting subscribe notification: %{public}s',
            JSON.stringify(data.entityResult));
        }
      });
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, 'testTag', 'Failed to request subscribe notification: %{public}d %{public}s', e.code,
        e.message);
    }
  }
}

#### serviceNotification.requestSubscribeNotification

requestSubscribeNotification(context: Context, entityIds: Array<string>, type?: SubscribeNotificationType): Promise<RequestResult>

Requests authorization on notification subscription. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 1000900017.

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

[Context](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) of the UI for requesting authorization on notification subscription.

NOTICE:

The context supports only **UIAbilityContext**.

 |
| 

entityIds

 | 

Array<string>

 | 

Yes

 | 

ID list of templates to be subscribed to.

 |
| 

type

 | 

[SubscribeNotificationType](#section3556183619491)

 | 

No

 | 

Subscription type. The default value is **SUBSCRIBE\_WITH\_TOKEN**.

NOTE:

Start version: 5.0.0(12).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[RequestResult](#section185441313151716)\>

 | 

Subscription authorization result, which is returned through a promise.

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

1000900011

 | 

The network is unavailable.

 |
| 

1000900017

 | 

The device does not support current operation.

 |
| 

1000900018

 | 

Number of calls exceeded.

 |
| 

1000900019

 | 

Illegal entity id.

 |
| 

1000900020

 | 

App token is empty.

 |
| 

1000900021

 | 

App is not available or not registered.

 |
| 

1000900022

 | 

Notification switch off.

 |
| 

1000900023

 | 

Number of entity ids exceed the upper limit.

 |
| 

1000900024

 | 

Failed to display subscription UI.

 |
| 

1000900025

 | 

No rights to access entity id.

 |
| 

1000900026

 | 

Illegal entity type.

 |
| 

1000900030

 | 

The user has not logged in with HUAWEI ID.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/SjDv3BmwQ06HjHc0OAsn1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062517Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDFED249F5CEB04EC8284D60ACCBDBAC3B9BA5E64BF3B638922A348BC450F302)

Error code 1000900030 is involved only when the API is used in an atomic service.

Error code 1000900011 may be caused by disabled network access of Push Kit. You can go to **Settings** > **Mobile network** > **Data usage** > **Network access** on the phone, and check whether network access is disabled for Push Kit.

**Example**:

import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { serviceNotification } from '@kit.PushKit';
import { BusinessError } from '@kit.BasicServicesKit';
const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
    try {
  // Replace **entityIds** with the IDs of the templates to be subscribed to.
      const entityIds = \['entityId1', 'entityId2', 'entityId3'\];
      let type: serviceNotification.SubscribeNotificationType =
        serviceNotification.SubscribeNotificationType.SUBSCRIBE\_WITH\_HUAWEI\_ID;
      serviceNotification.requestSubscribeNotification(this.context, entityIds, type).then((data) => {
        hilog.info(0x0000, 'testTag', 'Succeeded in requesting subscribe notification: %{public}s',
          JSON.stringify(data.entityResult));
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', 'Failed to request subscribe notification: %{public}d %{public}s', err.code,
          err.message);
      });
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, 'testTag', 'Failed to request subscribe notification: %{public}d %{public}s', e.code,
        e.message);
    }
  }
}

#### RequestResult

Authorization result of a subscription.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices.

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

entityResult

 | 

Array<[EntityResult](#section63339171710)\>

 | 

Yes

 | 

No

 | 

Subscription authorization result.

 |

#### EntityResult

Authorization result for each template in a single subscription.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices.

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

entityId

 | 

string

 | 

Yes

 | 

No

 | 

Template ID.

 |
| 

resultCode

 | 

[ResultCode](#section5698135841715)

 | 

Yes

 | 

No

 | 

Subscription authorization result code.

 |

#### ResultCode

Enumerated values of subscription authorization results.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This enumeration is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices.

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

ACCEPTED

 | 

0

 | 

A template is accepted.

 |
| 

REJECTED

 | 

1

 | 

A template is rejected.

 |
| 

FILTERED

 | 

2

 | 

A template is filtered out.

 |
| 

BANNED

 | 

3

 | 

A template is banned.

 |
| 

UNKNOWN

 | 

\-1

 | 

Unknown error.

 |

#### SubscribeNotificationType

Enumerated values of subscription types.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: This enumeration is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices.

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

SUBSCRIBE\_WITH\_TOKEN

 | 

0

 | 

Subscription based on a push token. **Only apps support push token-based subscription.**

 |
