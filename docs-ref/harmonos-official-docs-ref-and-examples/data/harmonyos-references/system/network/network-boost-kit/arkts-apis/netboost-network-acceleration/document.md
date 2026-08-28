# netBoost (Network Acceleration)

**Start version**: 6.0.0(20)

#### Module Import

import { netBoost } from '@kit.NetworkBoostKit';

#### netBoost.setSceneDesc

setSceneDesc(sceneDesc : SceneDesc): void

Sets the service scenario.

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetworkBoost.Core

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

sceneDesc

 | 

[SceneDesc](#section5777123521219)

 | 

Yes

 | 

Description information of a service scenario.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Description

 |
| :-- | :-- |
| 

201

 | 

Permission verification failed.

 |
| 

1013600001

 | 

System processing error. For example, the internal state machine is faulty, or the internal message queue is congested.

 |
| 

1013600002

 | 

System processing error. For example, IPC fails or the network management service fails to be started.

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
import { netBoost } from '@kit.NetworkBoostKit';
try {
  let sceneDesc : netBoost.SceneDesc = {
    scene : 'realtimeVoice',
    sceneEvent : netBoost.SceneEvent.SCENE\_EVENT\_ENTER
  }
  netBoost.setSceneDesc(sceneDesc);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### SceneDesc

Defines the description information of a service scenario.

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 6.0.0(20)

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

scene

 | 

[netQuality.ServiceType](../netquality-network-quality/document.md#section18954312204111)

 | 

No

 | 

No

 | 

Service scenario type.

 |
| 

sceneEvent

 | 

[SceneEvent](#section1278885681816)

 | 

No

 | 

No

 | 

Service scenario event.

 |
| 

startTime

 | 

number

 | 

No

 | 

Yes

 | 

Predicted duration before the **sceneEvent** is triggered, in seconds.

-   **0**: The **sceneEvent** event occurs immediately. The default value is **0**.
-   Value greater than 0: Predicted duration before the **sceneEvent** is triggered.

 |
| 

duration

 | 

number

 | 

No

 | 

Yes

 | 

Predicted duration of the **SceneEvent**, in seconds. The value **0** indicates an unknown duration, which ends when the **SceneEvent** ends.

For example, if an app is about to enter a seckill scenario in 10 seconds and the scenario is expected to last for 20 seconds, the **scene** can be set to **seckillService**, **sceneEvent** to **SCENE\_EVENT\_ENTER**, **startTime** to **10**, and **duration** to **20**. You can set these fields based on the actual service scenario.

 |

#### SceneEvent

Defines the enumeration of service scenario events.

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 6.0.0(20)

| 
Parameter

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SCENE\_EVENT\_ENTER

 | 

0

 | 

The app enters a service scenario.

 |
| 

SCENE\_EVENT\_UPDATE

 | 

1

 | 

The last service scenario event information is updated.

 |
| 

SCENE\_EVENT\_LEAVE

 | 

2

 | 

The app leaves a service scenario.

 |
