# netQuality (Network Quality)

This module provides capabilities including real-time network quality assessment, network scenario identification, and weak signal prediction. These capabilities enable your app to dynamically adjust cache, bit rate, frame rate, and resolution policies, ensuring a seamless experience even in challenging network environments. Your app can also call the transmission quality feedback API to report the network quality, so as to trigger network acceleration.

**Start version**: 5.0.0(12)

#### Module Import

import { netQuality } from '@kit.NetworkBoostKit';

#### netQuality.on( 'netQosChange')

on(type: 'netQosChange', callback: Callback<Array<NetworkQos>>): void

Subscribes to network quality information.

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

Event type. The value is always **netQosChange**, indicating network quality change events.

 |
| 

callback

 | 

Callback<Array<[NetworkQos](#section5777123521219)\>>

 | 

Yes

 | 

Callback function, which is used to return network QoS change details.

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

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
import { netQuality } from '@kit.NetworkBoostKit';
try {
  netQuality.on('netQosChange', (list: Array<netQuality.NetworkQos>) => {
    if (list.length > 0) {
      list.forEach((qos) => {
        // Callback information processing.
        console.info(\`Succeeded receive netQosChange info\`);
      });
    }
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### netQuality.off( 'netQosChange')

off(type: 'netQosChange', callback?: Callback<Array<NetworkQos>>): void

Unsubscribes from network quality information.

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

Event type. The value is always **netQosChange**, indicating connection state change events.

 |
| 

callback

 | 

Callback<Array<[NetworkQos](#section5777123521219)\>>

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
import { netQuality } from '@kit.NetworkBoostKit';
try {
  netQuality.off('netQosChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### netQuality.on( 'netSceneChange')

on(type: 'netSceneChange', callback: Callback<Array<NetworkScene>>): void

Subscribes to network scenario information.

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

Event type. The value is always **netSceneChange**, indicating network scenario change events.

 |
| 

callback

 | 

Callback<Array<[NetworkScene](#section19886656145619)\>>

 | 

Yes

 | 

Callback function, which is used to return network scenario change details.

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
import { netQuality } from '@kit.NetworkBoostKit';
try {
  netQuality.on('netSceneChange', (list: Array<netQuality.NetworkScene>) => {
    if (list.length > 0) {
      list.forEach((scene) => {
        // Callback information processing.
        console.info(\`Succeeded receive netSceneChange info\`);
        if (scene.weakSignalPrediction) {
          // Weak signal prediction processing.
        }
      });
    }
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### netQuality.off( 'netSceneChange')

off(type: 'netSceneChange', callback?: Callback<Array<NetworkScene>>): void

Unsubscribes from network scenario information.

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

Event type. The value is always **netSceneChange**, indicating network scenario change events.

 |
| 

callback

 | 

Callback<Array<[NetworkScene](#section19886656145619)\>>

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
import { netQuality } from '@kit.NetworkBoostKit';
try {
  netQuality.off('netSceneChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### netQuality.reportQoe

reportQoe(appQoe: AppQoe): void

Reports app data transmission quality. If the reporting fails, the API will throw an exception.

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

appQoe

 | 

[AppQoe](#section25523227370)

 | 

Yes

 | 

Transmission quality data to be reported.

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
import { netQuality } from '@kit.NetworkBoostKit';
try {
  let serviceType: netQuality.ServiceType = 'shortVideo';
  let qoeType: netQuality.BadQoeCause = 'serverErr';
  let appQoe: netQuality.AppQoe = {
    serviceType,
    qoeType
  };
  netQuality.reportQoe(appQoe);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### AppQoe

Defines app data transmission quality information.

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

serviceType

 | 

[ServiceType](#section18954312204111)

 | 

No

 | 

No

 | 

Service type of the app.

 |
| 

qoeType

 | 

[QoeType](#section819973417438)

 | 

No

 | 

No

 | 

Network quality data type of the app.

 |

#### NetworkQos

Defines network quality data that is returned.

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

pathType

 | 

[PathType](#section45141941132511)

 | 

No

 | 

No

 | 

Type of the data path for which the network quality data needs to be returned.

 |
| 

linkUpBandwidth

 | 

[RateBps](#section786722592713)

 | 

No

 | 

No

 | 

Uplink bandwidth, in bit/s.

 |
| 

linkDownBandwidth

 | 

[RateBps](#section786722592713)

 | 

No

 | 

No

 | 

Downlink bandwidth, in bit/s.

 |
| 

linkUpRate

 | 

[RateBps](#section786722592713)

 | 

No

 | 

No

 | 

Uplink rate, in bit/s.

 |
| 

linkDownRate

 | 

[RateBps](#section786722592713)

 | 

No

 | 

No

 | 

Downlink rate, in bit/s.

 |
| 

rttMs

 | 

number

 | 

No

 | 

No

 | 

RTT, which indicates the average RTT of all uplink and downlink TCP data packets on the data path corresponding to **pathType** in a statistical period, in milliseconds.

If no response to a certain TCP request is received within the statistical period, the RTT of that request will not be included for calculating the average RTT. The value is any positive number.

 |
| 

linkUpBufferDelayMs

 | 

number

 | 

No

 | 

No

 | 

Uplink air interface buffer delay. The value is any positive number.

 |
| 

linkUpBufferCongestionPercent

 | 

number

 | 

No

 | 

Yes

 | 

Percentage of the uplink air interface buffer delay to the total buffering time. The value range is \[0, 100\].

 |

#### PathType

Defines the enumeration for the data path type.

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

CELLULAR\_PRIMARY

 | 

0

 | 

Primary SIM card.

 |
| 

CELLULAR\_SECONDARY

 | 

1

 | 

Secondary SIM card.

 |
| 

WIFI\_PRIMARY

 | 

2

 | 

Primary Wi-Fi.

 |
| 

WIFI\_SECONDARY

 | 

3

 | 

Secondary Wi-Fi.

 |

#### RateBps

type RateBps = number

Defines an abstract representation of the network bandwidth or rate.

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

Number. The value is any positive number in bit/s.

 |

#### ServiceType

type ServiceType = 'default' | 'background' | 'realtimeVoice' | 'realtimeVideo' | 'callSignaling' | 'realtimeGame' | 'normalGame' | 'shortVideo' | 'longVideo' | 'livestreamingAnchor' | 'livestreamingWatcher' | 'download' | 'upload' | 'browser' | 'transaction' | 'shopping' | 'detection' | 'cloudService' | 'voiceConference' | 'videoConference' | 'audio' | 'navigation' | 'seckillService' | 'login'

Defines the options of the app service type.

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'default'

 | 

Default service type, which is represented by the fixed character string **'default'**.

 |
| 

'background'

 | 

Background service, which is represented by the fixed character string **'background'**.

 |
| 

'realtimeVoice'

 | 

Real-time voice service, which is represented by the fixed character string **'realtimeVoice'**.

 |
| 

'realtimeVideo'

 | 

Real-time video service, which is represented by the fixed character string **'realtimeVideo'**.

 |
| 

'callSignaling'

 | 

Voice signaling service, which is represented by the fixed character string **'callSignaling'**.

 |
| 

'realtimeGame'

 | 

Real-time game service, which is represented by the fixed character string **'realtimeGame'**.

 |
| 

'normalGame'

 | 

Common game service, which is represented by the fixed character string **'normalGame'**.

 |
| 

'shortVideo'

 | 

Short video service, which is represented by the fixed character string **'shortVideo'**.

 |
| 

'longVideo'

 | 

Long video service, which is represented by the fixed character string **'longVideo'**.

 |
| 

'livestreamingAnchor'

 | 

Live streamer service, which is represented by the fixed character string **'livestreamingAnchor'**.

 |
| 

'livestreamingWatcher'

 | 

Live streaming viewer service, which is represented by the fixed character string **'livestreamingWatcher'**.

 |
| 

'download'

 | 

Download service, which is represented by the fixed character string **'download'**.

 |
| 

'upload'

 | 

Upload service, which is represented by the fixed character string **'upload'**.

 |
| 

'browser'

 | 

Web page browsing service, which is represented by the fixed character string **'browser'**.

 |
| 

'transaction'

 | 

Transaction payment or code scanning service, which is represented by the fixed character string **'transaction'**. This service type is supported since API version 20.

 |
| 

'shopping'

 | 

Shopping service, which is represented by the fixed character string **'shopping'**. This service type is supported since API version 20.

 |
| 

'detection'

 | 

Detection service, which is represented by the fixed character string **'detection'**. This service type is supported since API version 20.

 |
| 

'cloudService'

 | 

Cloud service/cloud game, which is represented by the fixed character string **'cloudService'**. This service type is supported since API version 20.

 |
| 

'voiceConference'

 | 

Voice conference service, which is represented by the fixed character string **'voiceConference'**. This service type is supported since API version 20.

 |
| 

'videoConference'

 | 

Video conference service, which is represented by the fixed character string **'videoConference'**. This service type is supported since API version 20.

 |
| 

'audio'

 | 

Audio (such as music) service, which is represented by the fixed character string **'audio'**. This service type is supported since API version 20.

 |
| 

'navigation'

 | 

Navigation and location service, which is represented by the fixed character string **'navigation'**. This service type is supported since API version 20.

 |
| 

'seckillService'

 | 

Seckill service, such as ticket snatching, flash sale, order grabbing, and red envelope claiming, which is represented by the fixed character string **'seckillService'**. This service type is supported since API version 20.

 |
| 

'login'

 | 

Login (including one-tap login) service, which is represented by the fixed character string **'login'**. This service type is supported since API version 20.

 |

#### QoeType

type QoeType = 'good' | BadQoeCause

Defines the options of the network quality data type of the app.

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'good'

 | 

Good network quality, which is represented by the fixed character string **'good'**.

 |
| 

[BadQoeCause](#section327672810449)

 | 

Bad network quality.

 |

#### BadQoeCause

type BadQoeCause = 'unknown' | 'serverErr' | 'noData' | 'packetLost' | 'packetOutOfOrder' | 'highJitter' | 'highLatency'

Defines the cause options of bad network quality of the app.

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'unknown'

 | 

Unknown cause, which is represented by the fixed character string **'unknown'**.

 |
| 

'serverErr'

 | 

Server error, which is represented by the fixed character string **'serverErr'**.

 |
| 

'noData'

 | 

No data, which is represented by the fixed character string **'noData'**.

 |
| 

'packetLost'

 | 

Packet loss, which is represented by the fixed character string **'packetLost'**.

 |
| 

'packetOutOfOrder'

 | 

Packets out of order, which is represented by the fixed character string **'packetOutOfOrder'**.

 |
| 

'highJitter'

 | 

High jitter, which is represented by the fixed character string **'highJitter'**.

 |
| 

'highLatency'

 | 

High latency, which is represented by the fixed character string **'highLatency'**.

 |

#### Network Rate/Bandwidth Level

Defines multiple constants that represent different network bandwidth or rate levels.

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 5.0.0(12)

| 
Parameter

 | 

Type

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

BPS

 | 

number

 | 

1

 | 

1 bit/s.

 |
| 

KBPS

 | 

number

 | 

1000

 | 

1 kbit/s.

 |
| 

MBPS

 | 

number

 | 

1000000

 | 

1 Mbit/s.

 |
| 

GBPS

 | 

number

 | 

1000000000

 | 

1 Gbit/s.

 |
| 

TBPS

 | 

number

 | 

1000000000000

 | 

1 Tbit/s.

 |

#### NetworkScene

Defines the network scenario change information that is returned.

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

pathType

 | 

[PathType](#section45141941132511)

 | 

No

 | 

No

 | 

Type of the data path for which the network scenario data needs to be returned.

 |
| 

scene

 | 

[Scene](#section18341052913)

 | 

No

 | 

No

 | 

Scenario status.

 |
| 

recommendedAction

 | 

[RecommendedAction](#section1272138831)

 | 

No

 | 

No

 | 

Recommended data transmission policy.

 |
| 

weakSignalPrediction

 | 

[WeakSignalPrediction](#section1593261915415)

 | 

No

 | 

Yes

 | 

Weak signal prediction information.

 |

#### WeakSignalPrediction

Defines the weak signal prediction information.

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

isLastPredictionValid

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether the latest weak signal prediction is still valid. The options are **true** (yes) and **false** (no). When the value is **false**, the **startTime** and **duration** parameters do not take effect.

 |
| 

startTime

 | 

number

 | 

No

 | 

No

 | 

Predicted duration before the signal becomes weak, in seconds. The value is 0 or a positive number.

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

Estimated duration of the weak signal, in seconds. The value is a positive number. If the value is 0, the prediction result is invalid.

 |

#### Scene

type Scene = 'normal' | 'congestion' | 'frequentHandover' | 'weakSignal'

Defines the options of the network scenario type.

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'normal'

 | 

Normal scenario, which is represented by the fixed character string **'normal'**.

 |
| 

'congestion'

 | 

Congestion scenario, which is represented by the fixed character string **'congestion'**.

 |
| 

'frequentHandover'

 | 

Frequent cell handover scenario, which is represented by the fixed character string **'frequentHandover'**.

 |
| 

'weakSignal'

 | 

Weak signal scenario, which is represented by the fixed character string **'weakSignal'**.

 |

#### DataSpeedSimpleAction

type DataSpeedSimpleAction = 'suspendData' | 'decreaseData' | 'increaseData' | 'keepData'

Defines the options of the suggested packet transmission policy.

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'suspendData'

 | 

Stop transmitting packets, which is represented by the fixed character string **'suspendData'**.

 |
| 

'decreaseData'

 | 

Decrease the packet transmission rate, which is represented by the fixed character string **'decreaseData'**.

 |
| 

'increaseData'

 | 

Increase the packet transmission rate, which is represented by the fixed character string **'increaseData'**.

 |
| 

'keepData'

 | 

Keep the current packet transmission rate, which is represented by the fixed character string **'keepData'**.

 |

#### RecommendedAction

type RecommendedAction = 'doCaching' | DataSpeedSimpleAction

Defines the options of the suggested data transmission policy.

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 5.0.0(12)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'doCaching'

 | 

Caching data, which is represented by the fixed character string **'doCaching'**.

 |
| 

[DataSpeedSimpleAction](#section23982281626)

 | 

Suggested packet transmission policy.

 |
