# network\_boost\_quality.h

#### Overview

Declares APIs for network quality assessment, and defines basic functions, structs, and constants.

**Library**: libnetwork\_boost.so

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 5.1.0(18)

**Related module**: [NetworkBoost](../../../modules/networkboost/document.md)

#### Summary

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [NetworkBoost\_NetworkQos](../../structs/networkboost-networkqos/document.md)

 | 

Defines network quality data that is returned.

 |
| 

struct [NetworkBoost\_NetworkQosArray](../../structs/networkboost-networkqosarray/document.md)

 | 

Defines network quality change details.

 |
| 

struct [NetworkBoost\_WeakSignalPrediction](../../structs/networkboost-weaksignalprediction/document.md)

 | 

Defines weak signal prediction information.

 |
| 

struct [NetworkBoost\_NetworkScene](../../structs/networkboost-networkscene/document.md)

 | 

Defines the network scenario change information that is returned.

 |

#### \[h2\]Macros

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[NETBOOST\_MAX\_PATH\_NUM](../../../modules/networkboost/document.md#ga7668e89aac2dea1d584a9ccacea33614) 4

 | 

Maximum number of paths for which network quality change information can be returned.

 |
| 

[NB\_BPS](../../../modules/networkboost/document.md#gabdf273f7096ba64be754f03a0da421f1) 1

 | 

1 bit/s.

 |
| 

[NB\_KBPS](../../../modules/networkboost/document.md#gab99b17bff7ea6a679f99ac7cdd1b3700) 1000

 | 

1 kbit/s.

 |
| 

[NB\_MBPS](../../../modules/networkboost/document.md#gafd7fe5b6bd12a15f1eafab390bd8a8bd) 1000000

 | 

1 Mbit/s.

 |
| 

[NB\_GBPS](../../../modules/networkboost/document.md#ga1e4efaf6c147fb7cfbd8f72083be3f82) 1000000000

 | 

1 Gbit/s.

 |
| 

[NB\_TBPS](../../../modules/networkboost/document.md#gade9c8363d332d7740b454e2920315ac5) 1000000000000

 | 

1 Tbit/s. To handle this, utilize the uint64\_t data type to prevent overflow.

 |

#### \[h2\]Types

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef enum [NetworkBoost\_RecommendedAction](../../../modules/networkboost/document.md#ga42f25be03d340c17630c3a0f9cd0d123) [NetworkBoost\_RecommendedAction](../../../modules/networkboost/document.md#ga3543e6660b965ebc071fd13d359d6a39)

 | 

Defines the enumeration of the suggested data transmission policy.

 |
| 

typedef enum [NetworkBoost\_PathType](../../../modules/networkboost/document.md#gae8474ae83c3add50ac3fa7702c089ea8) [NetworkBoost\_PathType](../../../modules/networkboost/document.md#ga45748b2a298346cbea2f1cbe573ffe72)

 | 

Defines the enumeration of the path type.

 |
| 

typedef enum [NetworkBoost\_Scene](../../../modules/networkboost/document.md#ga972c3eb36772eb1affb0cd551429547b) [NetworkBoost\_Scene](../../../modules/networkboost/document.md#ga551f8ada8a742207e5eba134765d2a0f)

 | 

Defines the enumeration of the network scenario type.

 |
| 

typedef enum [NetworkBoost\_ServiceType](../../../modules/networkboost/document.md#ga5b192f3d72de3ac083df4cf36cbc318f) [NetworkBoost\_ServiceType](../../../modules/networkboost/document.md#gaabe242932bb115198d2f27c0deedb0f5)

 | 

Defines the enumeration of the app service type.

 |
| 

typedef enum [NetworkBoost\_QoeType](../../../modules/networkboost/document.md#ga539adc59ea2ca1c7498eac3a59bc62be) [NetworkBoost\_QoeType](../../../modules/networkboost/document.md#ga152febbb6bccad7017f37457e433ba6e)

 | 

Defines the enumeration of the network quality data type of the app.

 |
| 

typedef struct [NetworkBoost\_NetworkQos](../../structs/networkboost-networkqos/document.md) [NetworkBoost\_NetworkQos](../../../modules/networkboost/document.md#ga950f78df8282426c91728728c8ca9e8e)

 | 

Defines network quality data that is returned.

 |
| 

typedef struct [NetworkBoost\_NetworkQosArray](../../structs/networkboost-networkqosarray/document.md) [NetworkBoost\_NetworkQosArray](../../../modules/networkboost/document.md#gac61cbd4df3cf59284dcbdc5860e6ef9b)

 | 

Defines network quality change details.

 |
| 

typedef struct [NetworkBoost\_WeakSignalPrediction](../../structs/networkboost-weaksignalprediction/document.md) [NetworkBoost\_WeakSignalPrediction](../../../modules/networkboost/document.md#ga2d2d1a19e06dd2746d18eb9eaa8ae8af)

 | 

Defines weak signal prediction information.

 |
| 

typedef struct [NetworkBoost\_NetworkScene](../../structs/networkboost-networkscene/document.md) [NetworkBoost\_NetworkScene](../../../modules/networkboost/document.md#ga133be4442e775aa5b062a29f6de9bfe0)

 | 

Defines the network scenario change information that is returned.

 |
| 

typedef void(\* [HMS\_NetworkBoost\_NetQosChange](../../../modules/networkboost/document.md#ga51a4f0de15c82e94eceafdc8444dd51a)) ([NetworkBoost\_NetworkQosArray](../../structs/networkboost-networkqosarray/document.md) \*networkQosArray)

 | 

Defines the network quality change callback.

 |
| 

typedef void(\* [HMS\_NetworkBoost\_NetSceneChange](../../../modules/networkboost/document.md#gab00c153ac0c6faf6066cd013ac1d97d4)) ([NetworkBoost\_NetworkScene](../../structs/networkboost-networkscene/document.md) \*networkScene)

 | 

Defines the network scenario change callback.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[NetworkBoost\_RecommendedAction](../../../modules/networkboost/document.md#ga42f25be03d340c17630c3a0f9cd0d123) {

NB\_ACTION\_DO\_CACHING = 0, NB\_ACTION\_SUSPEND\_DATA = 1, NB\_ACTION\_DECREASE\_DATA = 2, NB\_ACTION\_INCREASE\_DATA = 3,

NB\_ACTION\_KEEP\_DATA = 4

}

 | 

Defines the enumeration of the suggested data transmission policy.

 |
| 

[NetworkBoost\_PathType](../../../modules/networkboost/document.md#gae8474ae83c3add50ac3fa7702c089ea8) { NB\_PATH\_CELLULAR\_PRIMARY = 0, NB\_PATH\_CELLULAR\_SECONDARY = 1, NB\_PATH\_WIFI\_PRIMARY = 2, NB\_PATH\_WIFI\_SECONDARY = 3 }

 | 

Defines the enumeration of the path type.

 |
| 

[NetworkBoost\_Scene](../../../modules/networkboost/document.md#ga972c3eb36772eb1affb0cd551429547b) { NB\_SCENE\_NORMAL = 0, NB\_SCENE\_CONGESTION = 1, NB\_SCENE\_FREQUENT\_HANDOVER = 2, NB\_SCENE\_WEAK\_SIGNAL = 3 }

 | 

Defines the enumeration of the network scenario type.

 |
| 

[NetworkBoost\_ServiceType](../../../modules/networkboost/document.md#ga5b192f3d72de3ac083df4cf36cbc318f) {

NB\_SERVICE\_DEFAULT = 0, NB\_SERVICE\_BACKGROUND = 1, NB\_SERVICE\_REAL\_TIME\_VOICE = 2, NB\_SERVICE\_REAL\_TIME\_VIDEO = 3,

NB\_SERVICE\_CALL\_SIGNALING = 4, NB\_SERVICE\_REAL\_TIME\_GAME = 5, NB\_SERVICE\_NORMAL\_GAME = 6, NB\_SERVICE\_SHORT\_VIDEO = 7,

NB\_SERVICE\_LONG\_VIDEO = 8, NB\_SERVICE\_LIVE\_STREAMING\_ANCHOR = 9, NB\_SERVICE\_LIVE\_STREAMING\_WATCHER = 10, NB\_SERVICE\_DOWNLOAD = 11,

NB\_SERVICE\_UPLOAD = 12, NB\_SERVICE\_BROWSER = 13, NB\_SERVICE\_TRANSACTION = 14, NB\_SERVICE\_DETECTION = 15, NB\_SERVICE\_CLOUDSERVICE = 16, NB\_SERVICE\_VOICE\_CONFERENCE = 17, NB\_SERVICE\_VIDEO\_CONFERENCE = 18, NB\_SERVICE\_NAVIGATION = 19, NB\_SERVICE\_SECKILL\_SERVICE = 20, NB\_SERVICE\_LOGIN = 21, NB\_SERVICE\_AUDIO = 22, NB\_SERVICE\_SHOPPING = 23

}

 | 

Defines the enumeration of the app service type.

 |
| 

[NetworkBoost\_QoeType](../../../modules/networkboost/document.md#ga539adc59ea2ca1c7498eac3a59bc62be) {

NB\_QOE\_GOOD = 0, NB\_QOE\_BAD\_UNKNOWN = 1, NB\_QOE\_BAD\_SERVER\_ERROR = 2, NB\_QOE\_BAD\_NO\_DATA = 3,

NB\_QOE\_BAD\_PACKET\_LOST = 4, NB\_QOE\_BAD\_PACKET\_OUT\_OF\_ORDER = 5, NB\_QOE\_BAD\_HIGH\_JITTER = 6, NB\_QOE\_BAD\_HIGH\_LATENCY = 7

}

 | 

Defines the enumeration of the network quality data type of the app.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

int32\_t [HMS\_NetworkBoost\_RegisterNetQosCallback](../../../modules/networkboost/document.md#ga72cac93efbd98d448ae2d3dc7d3b3dfe) ([HMS\_NetworkBoost\_NetQosChange](../../../modules/networkboost/document.md#ga51a4f0de15c82e94eceafdc8444dd51a) callback, uint32\_t \*callbackId)

 | 

Registers the network quality information callback.

 |
| 

int32\_t [HMS\_NetworkBoost\_UnregisterNetQosCallback](../../../modules/networkboost/document.md#gae435e58413bd125a9bca06aed0b6ebfe) (uint32\_t callbackId)

 | 

Deregisters the network quality information callback.

 |
| 

int32\_t [HMS\_NetworkBoost\_RegisterNetSceneCallback](../../../modules/networkboost/document.md#ga13b998a6c6fca1a4b84dd77f547f20ea) ([HMS\_NetworkBoost\_NetSceneChange](../../../modules/networkboost/document.md#gab00c153ac0c6faf6066cd013ac1d97d4) callback, uint32\_t \*callbackId)

 | 

Registers the network scenario change callback.

 |
| 

int32\_t [HMS\_NetworkBoost\_UnregisterNetSceneCallback](../../../modules/networkboost/document.md#gad7e9989cb65b01ba52e0b8427fa3e113) (uint32\_t callbackId)

 | 

Deregisters the network scenario change callback.

 |
| 

int32\_t [HMS\_NetworkBoost\_ReportQoe](../../../modules/networkboost/document.md#ga2d62d2b3ec0536118a28175d53e0f363) ([NetworkBoost\_ServiceType](../../../modules/networkboost/document.md#ga5b192f3d72de3ac083df4cf36cbc318f) serviceType, [NetworkBoost\_QoeType](../../../modules/networkboost/document.md#ga539adc59ea2ca1c7498eac3a59bc62be) qoeType)

 | 

Sends back the app data transmission experience.

 |
