# netHandover (Network Handover)

This module provides network handover capabilities. When the network signal is weak and the device initiates a network handover (such as from Wi-Fi to cellular or between primary and secondary SIM cards), the device will notify your app upon the start and end of the handover. Then your app can re-establish the link accordingly and swiftly restore services, providing users with a smooth, fast, and low-latency network experience.

**Start version**: 5.0.0(12)

#### Module Import

import { netHandover } from '@kit.NetworkBoostKit';

#### netHandover.on( 'handoverChange')

on(type: 'handoverChange', callback: Callback<HandoverInfo>): void

Subscribes to network handover information.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Communication.NetworkBoost.Core

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

type

 | 

string

 | 

Yes

 | 

Event type. The value is always **handoverChange**, indicating network handover events.

 |
| 

callback

 | 

Callback<[HandoverInfo](#section5777123521219)\>

 | 

Yes

 | 

Callback function, which returns the details about the start and end of a network handover.

 |

**Error codes**:

All error codes relevant to this kit are universal error codes. For details, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

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

401

 | 

Parameter check failed.

 |
| 

801

 | 

The device does not support this API.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { netHandover } from '@kit.NetworkBoostKit';
try {
  netHandover.on('handoverChange', (info: netHandover.HandoverInfo) => {
    if (info.handoverStart) {
      // Callback for the start of network handover. Adjust the data transmission policy based on the suggestion in **HandoverStart**.
      console.info('handover start');
    } else if (info.handoverComplete) {
      // Callback for the end of network handover. Adjust the network rate and re-establish the link based on the suggestion in **HandoverComplete**.
      console.info('handover complete');
    }
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### netHandover.off( 'handoverChange')

off(type: 'handoverChange', callback?: Callback<HandoverInfo>): void

Unsubscribes from network handover information.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Communication.NetworkBoost.Core

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

type

 | 

string

 | 

Yes

 | 

Event type. The value is always **handoverChange**, indicating network handover events.

 |
| 

callback

 | 

Callback<[HandoverInfo](#section5777123521219)\>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions are unregistered.

 |

**Error codes**:

All error codes relevant to this kit are universal error codes. For details, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

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

401

 | 

Parameter check failed.

 |
| 

801

 | 

The device does not support this API.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { netHandover } from '@kit.NetworkBoostKit';
try {
  netHandover.off('handoverChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### netHandover.setHandoverMode

setHandoverMode(mode: HandoverMode): void

Defines the network handover mode. Your app can call the relevant API to change the network handover mode between delegation mode and proactive mode. The default mode is delegation. If the setting fails, the API will throw an exception.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Communication.NetworkBoost.Core

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

mode

 | 

[HandoverMode](#section85513341136)

 | 

Yes

 | 

Network handover mode that the app needs to notify the device of.

 |

**Error codes**:

All error codes relevant to this kit are universal error codes. For details, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

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

401

 | 

Parameter check failed.

 |
| 

801

 | 

The device does not support this API.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { netHandover } from '@kit.NetworkBoostKit';
try {
  // Set the mode to proactive mode, making the app to initiate handovers by itself.
  let mode: netHandover.HandoverMode = netHandover.HandoverMode.DISCRETION;
  netHandover.setHandoverMode(mode);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### netHandover.getMultiPathQuotaStats

getMultiPathQuotaStats(): MultiPathQuota

Obtains the quota information of multi-network concurrency, including the used and remaining quotas.

**Required permission**: ohos.permission.LINKTURBO

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 6.0.0(20)

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[MultiPathQuota](#section168911430203320)

 | 

Multi-network concurrency quota information of an app.

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

Internal processing error. For example, the internal state machine is faulty.

 |
| 

1013600002

 | 

System processing error. For example, inter-process communication (IPC) fails or the network management service fails to be started.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { netHandover } from '@kit.NetworkBoostKit';
try {
  let multiquota : netHandover.MultiPathQuota = netHandover.getMultiPathQuotaStats();
  console.info('getMultiPathQuotaStats multiPathQuota.used.count is:' + multiquota.used.count)
  console.info('getMultiPathQuotaStats multiPathQuota.used.duration is:' + multiquota.used.duration)
  console.info('getMultiPathQuotaStats multiPathQuota.remaining.count is:' + multiquota.remaining.count)
  console.info('getMultiPathQuotaStats multiPathQuota.remaining.durationis:' + multiquota.remaining.duration)
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### netHandover.requestMultiPath

requestMultiPath(callback: Callback<MultiPathRequestResult>): void

Initiates a multi-network concurrency request.

**Required permission**: ohos.permission.LINKTURBO

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

callback

 | 

Callback<[MultiPathRequestResult](#section1578014618195)\>

 | 

Yes

 | 

Callback used to return the multi-network concurrency initiation result.

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
| 

1013620000

 | 

Multi-network concurrency is not enabled.

 |
| 

1013620001

 | 

Multi-network concurrency has been activated or is being activated.

 |
| 

1013620002

 | 

The number of multi-network concurrency requests has reached the upper limit.

 |
| 

1013620003

 | 

Multi-network concurrency cannot be initiated due to power consumption restrictions.

 |
| 

1013620004

 | 

The quota is exhausted.

 |
| 

1013620005

 | 

A multi-network concurrency scenario conflict occurs.

 |
| 

1013620006

 | 

Multi-network concurrency is initiated too frequently.

 |
| 

1013620007

 | 

No path other than the current connected path is available for muti-network concurrency.

 |
| 

1013620008

 | 

The data traffic quota of the device is insufficient.

 |
| 

1013620009

 | 

Multi-network concurrency is not supported.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { netHandover } from '@kit.NetworkBoostKit';
try {
  netHandover.requestMultiPath((data: netHandover.MultiPathRequestResult) => {
   console.info(\` requestMultiPath result:\` + JSON.stringify(data));
  });
 } catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### netHandover.releaseMultiPath

releaseMultiPath(): void

Releases multi-network concurrency.

**Required permission**: ohos.permission.LINKTURBO

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 6.0.0(20)

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
| 

1013620100

 | 

Multi-network concurrency is activated by an app different from the one that initiates the release request.

 |
| 

1013620101

 | 

Multi-network concurrency is not activated.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { netHandover } from '@kit.NetworkBoostKit';
try {
  netHandover.releaseMultiPath();
 } catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### netHandover.on('multiPathStateChange')

on(type: 'multiPathStateChange', callback: Callback<MultiPathStateInfo>): void

Subscribes to the multi-network concurrency status change events.

**Required permission**: ohos.permission.LINKTURBO

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

type

 | 

string

 | 

Yes

 | 

Event type. The value is always **multiPathStateChange**, indicating multi-network concurrency status change events.

 |
| 

callback

 | 

Callback<[MultiPathStateInfo](#section166554717569)\>

 | 

Yes

 | 

Callback function, which is used to return multi-network concurrency status change information.

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
import { netHandover } from '@kit.NetworkBoostKit';
try {
  netHandover.on('multiPathStateChange', (data: netHandover.MultiPathStateInfo) => {
    // Callback information processing.
    console.info("on multiPathStateChange: " + JSON.stringify(data));
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### netHandover.off('multiPathStateChange')

off(type: 'multiPathStateChange', callback?: Callback<MultiPathStateInfo>): void

Unsubscribes from multi-network concurrency status change events.

**Required permission**: ohos.permission.LINKTURBO

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

type

 | 

string

 | 

Yes

 | 

Event type. The value is always **multiPathStateChange**, indicating multi-network concurrency status change events.

 |
| 

callback

 | 

Callback<[MultiPathStateInfo](#section166554717569)\>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions are unregistered.

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

Internal processing error. For example, the internal state machine is faulty.

 |
| 

1013600002

 | 

System processing error. For example, IPC fails or the network management service fails to be started.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { netHandover } from '@kit.NetworkBoostKit';
try {
  netHandover.off('multiPathStateChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### netHandover.on('multiPathRecommendation')

on(type: 'multiPathRecommendation', callback: Callback<MultiPathRecommendationInfo>): void

Subscribe to changes on multi-network suggestions provided by the device.

**Required permission**: ohos.permission.LINKTURBO

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

type

 | 

string

 | 

Yes

 | 

Event type. The value is always **multiPathRecommendation**, indicating multi-network suggestion change events.

 |
| 

callback

 | 

Callback<[MultiPathRecommendationInfo](#section1557733015378)\>

 | 

Yes

 | 

Callback function, which is used to return multi-network suggestion change information.

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
import { netHandover } from '@kit.NetworkBoostKit';
try {
  netHandover.on('multiPathRecommendation', (data: netHandover.MultiPathRecommendationInfo) => {
    // Callback information processing.
    console.info("on multiPathRecommendation: " + JSON.stringify(data));
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### netHandover.off('multiPathRecommendation')

off(type: 'multiPathRecommendation', callback?: Callback<MultiPathRecommendationInfo>): void

Unsubscribes from changes on multi-network concurrency suggestions provided by the device.

**Required permission**: ohos.permission.LINKTURBO

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

type

 | 

string

 | 

Yes

 | 

Event type. The value is always **multiPathRecommendation**, indicating multi-network suggestion change events.

 |
| 

callback

 | 

Callback<[MultiPathRecommendationInfo](#section1557733015378)\>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not passed, all callback functions are unregistered.

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
import { netHandover } from '@kit.NetworkBoostKit';
try {
  netHandover.off('multiPathRecommendation');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### HandoverInfo

Defines the network handover information to be returned.

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 5.0.0(12)

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

handoverStart

 | 

[HandoverStart](#section1593261915415)

 | 

Yes

 | 

Yes

 | 

Information indicating that network handover starts.

 |
| 

handoverComplete

 | 

[HandoverComplete](#section16119482176)

 | 

Yes

 | 

Yes

 | 

Information indicating that network handover ends.

 |

#### HandoverStart

Defines the information about the start of network handover.

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 5.0.0(12)

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

expires

 | 

number

 | 

No

 | 

No

 | 

Timeout interval of the entire network handover process, in seconds. The value can be any positive integer or 0.

 |
| 

dataSpeedAction

 | 

[DataSpeedAction](#section136319552227)

 | 

No

 | 

No

 | 

Packet transmission policy of the link before handover.

 |

#### HandoverComplete

Defines the information about the end of network handover.

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 5.0.0(12)

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

result

 | 

[ErrorResult](#section1823191782614)

 | 

No

 | 

No

 | 

Network handover result.

 |
| 

handoverContinue

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether there will be a subsequent **HandoverComplete** message. The options are as follows:

**true**: There will be more links to be activated and a subsequent **HandoverComplete** message will be sent when multiple target networks exist.

**false**: This is already the last **HandoverComplete** message and the handover process ends.

 |
| 

oldPathLifetime

 | 

number

 | 

No

 | 

No

 | 

Remaining lifetime of the original link, in seconds. The value can be any positive integer or 0.

 |
| 

oldDataSpeedAction

 | 

[DataSpeedAction](#section136319552227)

 | 

No

 | 

No

 | 

Packet transmission policy of the link before handover.

 |
| 

pathTypeChanged

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether the types of the old and new links are different. The value **true** indicates yes (for example, between Wi-Fi and cellular network), and **false** indicates no.

 |
| 

newNetHandle

 | 

[connection.NetHandle](../../../network-kit/arkts-apis/ohos-net-connection-network-connection-management/document.md#nethandle)

 | 

No

 | 

Yes

 | 

Network handling information of the link after handover.

 |
| 

reEstAction

 | 

[ReEstAction](#section575241112914)

 | 

No

 | 

No

 | 

Link re-establishment type.

 |
| 

newDataSpeedAction

 | 

[DataSpeedAction](#section136319552227)

 | 

No

 | 

No

 | 

Packet transmission policy of the link after handover.

 |

#### DataSpeedAction

Recommended packet transmission rate.

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 5.0.0(12)

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

dataSpeedSimpleAction

 | 

[netQuality.DataSpeedSimpleAction](../netquality-network-quality/document.md#section23982281626)

 | 

No

 | 

No

 | 

Suggested packet transmission policy.

 |
| 

linkUpBandwidth

 | 

[netQuality.RateBps](../netquality-network-quality/document.md#section786722592713)

 | 

No

 | 

No

 | 

Uplink bandwidth of the link before handover.

 |
| 

linkDownBandwidth

 | 

[netQuality.RateBps](../netquality-network-quality/document.md#section786722592713)

 | 

No

 | 

No

 | 

Downlink bandwidth of the link before handover.

 |

#### MultiPathStateInfo

Defines multi-network concurrency status information.

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

multiPathState

 | 

[MultiPathState](#section1635319535411)

 | 

No

 | 

No

 | 

Multi-network concurrency status.

 |
| 

cause

 | 

[MultiPathChangeCause](#section155215540412)

 | 

No

 | 

No

 | 

Reason for a multi-network concurrency status change.

 |
| 

netHandle

 | 

[connection.NetHandle](../../../network-kit/arkts-apis/ohos-net-connection-network-connection-management/document.md#nethandle)

 | 

No

 | 

No

 | 

Network handle of the multi-network concurrency.

 |
| 

pathState

 | 

[PathState](#section6391255134310)

 | 

No

 | 

No

 | 

Status of the data path other than the default path in multi-network concurrency.

 |
| 

pathType

 | 

[netQuality.PathType](../netquality-network-quality/document.md#section45141941132511)

 | 

No

 | 

No

 | 

Type of the data path other than the default path in multi-network concurrency.

 |

#### MultiPathRecommendationInfo

Defines multi-network concurrency suggestion information.

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

action

 | 

[MultiPathAction](#section186801623193513)

 | 

No

 | 

No

 | 

Multi-network concurrency action that is suggested.

 |

#### MultiPathQuota

Defines the quota usage information for multi-network concurrency.

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

used

 | 

[MultiPathQuotaInfo](#section1338164523216)

 | 

Yes

 | 

No

 | 

Used quota information.

 |
| 

remaining

 | 

[MultiPathQuotaInfo](#section1338164523216)

 | 

Yes

 | 

No

 | 

Remaining quota information.

 |

#### MultiPathQuotaInfo

Defines multi-network concurrency quota information.

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

count

 | 

number

 | 

No

 | 

No

 | 

Number of quota sessions.

 |
| 

duration

 | 

number

 | 

No

 | 

No

 | 

Quota duration, in seconds.

 |

#### MultiPathRequestResult

Defines the multi-network concurrency request result.

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

result

 | 

[MultiPathErrorResult](#section1689645144117)

 | 

No

 | 

No

 | 

Multi-network concurrency request result.

 |

#### MultiPathAction

Defines the enumeration of suggested multi-network concurrency actions.

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

MULTIPATH\_ACTION\_REQUEST

 | 

0

 | 

Initiate a multi-network concurrency request.

 |
| 

MULTIPATH\_ACTION\_RELEASE

 | 

1

 | 

Release multi-network concurrency.

 |

#### MultiPathErrorResult

Defines the enumeration of the multi-network concurrency initiation result.

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

MULTIPATH\_ERROR\_NONE

 | 

0

 | 

Multi-network concurrency initiated successfully.

 |
| 

MULTIPATH\_ERROR\_NETWORK\_REFUSED

 | 

1

 | 

Multi-network concurrency rejected.

 |
| 

MULTIPATH\_ERROR\_TIMEOUT

 | 

2

 | 

Multi-network concurrency times out.

 |
| 

MULTIPATH\_ERROR\_LOCAL

 | 

3

 | 

Multi-network concurrency is released locally when it is being initiated. For example, multi-network concurrency conditions are no longer met due to cellular data switch being turned off or other events during the startup.

 |

#### MultiPathState

Defines multi-network concurrency status values.

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

MULTIPATH\_IDLE

 | 

0

 | 

Multi-network concurrency is available.

 |
| 

MULTIPATH\_CREATING

 | 

1

 | 

Multi-network concurrency is being initiated.

 |
| 

MULTIPATH\_CREATED

 | 

2

 | 

Multi-network concurrency has been initiated.

 |
| 

MULTIPATH\_RELEASING

 | 

3

 | 

Multi-network concurrency is being released.

 |

#### PathState

Defines the status values of the data path other than the default path in multi-network concurrency.

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

PATH\_IDLE

 | 

0

 | 

A path in multi-network concurrency is idle.

 |
| 

PATH\_CONNECTED

 | 

1

 | 

A path in multi-network concurrency is set up.

 |
| 

PATH\_SUSPENDED

 | 

2

 | 

A path in multi-network concurrency is suspended.

 |

#### MultiPathChangeCause

Defines the enumeration of the reasons why multi-network concurrency status changes.

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

MULTIPATH\_CHANGE\_CAUSE\_REQUEST\_NORMAL

 | 

0

 | 

A multi-network concurrency request is normally initiated.

 |
| 

MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_NORMAL

 | 

50

 | 

Multi-network concurrency is normally released.

 |
| 

MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_NETWORK

 | 

51

 | 

Multi-network concurrency is released due to poor network conditions.

 |
| 

MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_USER\_REFUSED

 | 

52

 | 

Multi-network concurrency is released as the user turns off a relevant switch.

 |
| 

MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_NO\_QUOTA

 | 

53

 | 

Multi-network concurrency is released due to quota exhaustion.

 |
| 

MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_POWER\_CONSUMPTION

 | 

54

 | 

Multi-network concurrency is released due to power consumption factors.

 |
| 

MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_INSUFFICIENT\_TRAFFIC

 | 

55

 | 

Multi-network concurrency is released due to traffic consumption factors.

 |
| 

MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_CONFLICT

 | 

56

 | 

Multi-network concurrency is released due to scenario conflicts.

 |
| 

MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_FUSING

 | 

57

 | 

Multi-network concurrency is released by the device after an app improperly uses multi-network concurrency, for example, keeping multi-network concurrency on for a long time.

 |
| 

MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_DEFAULT

 | 

99

 | 

Multi-network concurrency is released due to network status changes of the device.

 |
| 

MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_ENTER

 | 

100

 | 

Multi-network concurrency is suspended. In this case, it is not released, but data transmission is actually suspended.

 |
| 

MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_LEAVE

 | 

101

 | 

Multi-network concurrency leaves the suspended state.

 |
| 

MULTIPATH\_CHANGE\_CAUSE\_CONN\_PROPERTIES\_UPDATE

 | 

102

 | 

Link attributes are updated for multi-network concurrency. For example, the IP address changes.

 |

#### HandoverMode

Defines the enumeration of the network handover mode.

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 5.0.0(12)

| 
Parameter

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DELEGATION

 | 

0

 | 

Delegation mode, indicating that the device initiates network handover. This mode is used by default if the app does not call the **setHandoverMode** API.

 |
| 

DISCRETION

 | 

1

 | 

Proactive mode, indicating that the app initiates network handover. An app can call this API to forbid the device to initiate network handover. However, in some cases, for example, when the app is switched to the background, the device may still initiate network handover even if the API is called.

 |

#### ReEstAction

Defines the enumeration of the link re-establishment type.

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 5.0.0(12)

| 
Parameter

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DEFAULT

 | 

0

 | 

The app needs to re-establish the link to the same remote IP address.

 |
| 

QUERY\_DNS

 | 

1

 | 

The link type changes, for example, between Wi-Fi and cellular network, or the carrier information of the link changes.

 |
| 

CHANGE\_REMOTE\_IP

 | 

2

 | 

The app needs to re-establish the link to a different IP address.

 |
| 

CHANGE\_IP\_VERSION

 | 

3

 | 

The app needs to re-establish the link by changing the IP address type, for example, between IPv4 and IPv6.

 |
| 

NO\_EST

 | 

4

 | 

The app needs to request network resources through the original data link, without the need to re-establish the link.

 |

#### ErrorResult

Defines the enumeration of the network handover result.

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 5.0.0(12)

| 
Parameter

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

ERROR\_NONE

 | 

0

 | 

The network handover is successful.

 |
| 

ERROR\_HANDOVER\_TIMEOUT

 | 

1

 | 

The network handover timed out.

 |
| 

ERROR\_NEW\_PATH\_ACTIVATION\_FAILED

 | 

2

 | 

The new link failed to be activated.

 |
| 

ERROR\_ABORT

 | 

3

 | 

Network handover was canceled.

 |
