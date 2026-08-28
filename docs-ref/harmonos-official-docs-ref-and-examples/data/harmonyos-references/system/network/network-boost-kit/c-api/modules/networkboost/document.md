# NetworkBoost

#### Overview

This kit provides APIs related to network quality assessment and network handover.

-   The network quality module provides capabilities including real-time network quality assessment, network scenario identification, and weak signal prediction. These capabilities enable your app to dynamically adjust cache, bit rate, frame rate, and resolution policies, ensuring a seamless experience even in challenging network environments. Your app can also call the transmission quality feedback API to report the network quality, so as to trigger network acceleration.
-   The network handover module provides network handover capabilities. When the network signal is weak and the device initiates a network handover (such as from Wi-Fi to cellular or between primary and secondary SIM cards), the device will notify your app upon the start and end of the handover. Then your app can re-establish the link accordingly and swiftly restore services, providing users with a smooth, fast, and low-latency network experience.
-   Multi-network concurrency refers to the system capability to establish multiple network paths through provided APIs. When an app initiates a multi-network concurrency request, the device determines the concurrency strategy based on the service scenario, applies corresponding concurrency controls, and evaluates the performance benefits accordingly. The principles for using multi-network concurrency are: app-initiated requests (with restricted permissions), system-level governance, and minimal usage.

**Start version**: 5.1.0(18)

#### Summary

#### \[h2\]Files

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[network\_boost\_handover.h](../../header-files-and-structs/header-files/network-boost-handover-h/document.md)

 | 

Declares APIs for network handover, and defines basic functions, structs, and constants.

 |
| 

[network\_boost\_quality.h](../../header-files-and-structs/header-files/network-boost-quality-h/document.md)

 | 

Declares APIs for network quality assessment, and defines basic functions, structs, and constants.

 |
| 

[network\_boost.h](../../header-files-and-structs/header-files/network-boost-h/document.md)

 | 

Declares APIs for network acceleration, and defines basic functions, structs, and constants.

 |

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [NetworkBoost\_DataSpeedAction](../../header-files-and-structs/structs/networkboost-dataspeedaction/document.md)

 | 

Defines the recommended packet transmission rate.

 |
| 

struct [NetworkBoost\_NetHandle](../../header-files-and-structs/structs/networkboost-nethandle/document.md)

 | 

Defines the network handling information.

 |
| 

struct [NetworkBoost\_HandoverStart](../../header-files-and-structs/structs/networkboost-handoverstart/document.md)

 | 

Defines the information about the start of network handover.

 |
| 

struct [NetworkBoost\_HandoverComplete](../../header-files-and-structs/structs/networkboost-handovercomplete/document.md)

 | 

Defines the information about the end of network handover.

 |
| 

struct [HMS\_NetworkBoost\_HandoverCallback](../../header-files-and-structs/structs/hms-networkboost-handovercallback/document.md)

 | 

Defines the network handover information that is returned.

 |
| 

struct [NetworkBoost\_NetworkQos](../../header-files-and-structs/structs/networkboost-networkqos/document.md)

 | 

Defines the network quality information of a single path that is returned.

 |
| 

struct [NetworkBoost\_NetworkQosArray](../../header-files-and-structs/structs/networkboost-networkqosarray/document.md)

 | 

Defines the network quality information of multiple paths that is returned.

 |
| 

struct [NetworkBoost\_WeakSignalPrediction](../../header-files-and-structs/structs/networkboost-weaksignalprediction/document.md)

 | 

Defines weak signal prediction information.

 |
| 

struct [NetworkBoost\_NetworkScene](../../header-files-and-structs/structs/networkboost-networkscene/document.md)

 | 

Defines the network scenario change information that is returned.

 |
| 

struct [NetworkBoost\_MultiPathQuotaInfo](../../header-files-and-structs/structs/networkboost-multipathquotainfo/document.md)

 | 

Defines multi-network concurrency quota information.

 |
| 

struct [NetworkBoost\_MultiPathQuota](../../header-files-and-structs/structs/networkboost-multipathquota/document.md)

 | 

Defines the quota usage information for multi-network concurrency.

 |
| 

struct [NetworkBoost\_MultiPathRequestResult](../../header-files-and-structs/structs/networkboost-multipathrequestresult/document.md)

 | 

Defines the multi-network concurrency request result.

 |
| 

struct [NetworkBoost\_MultiPathStateChange](../../header-files-and-structs/structs/networkboost-multipathstatechange/document.md)

 | 

Defines multi-network concurrency status information.

 |
| 

struct [NetworkBoost\_MultiPathRecommendation](../../header-files-and-structs/structs/networkboost-multipathrecommendation/document.md)

 | 

Defines multi-network concurrency suggestion information.

 |
| 

struct [NetworkBoost\_SceneDesc](../../header-files-and-structs/structs/networkboost-scenedesc/document.md)

 | 

Defines the description information of a service scenario.

 |

#### \[h2\]Macros

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[NETBOOST\_MAX\_PATH\_NUM](#ga7668e89aac2dea1d584a9ccacea33614) 4

 | 

Maximum number of paths for which network quality change information can be returned.

 |
| 

[NB\_BPS](#gabdf273f7096ba64be754f03a0da421f1) 1

 | 

1 bit/s.

 |
| 

[NB\_KBPS](#gab99b17bff7ea6a679f99ac7cdd1b3700) 1000

 | 

1 kbit/s.

 |
| 

[NB\_MBPS](#gafd7fe5b6bd12a15f1eafab390bd8a8bd) 1000000

 | 

1 Mbit/s.

 |
| 

[NB\_GBPS](#ga1e4efaf6c147fb7cfbd8f72083be3f82) 1000000000

 | 

1 Gbit/s.

 |
| 

[NB\_TBPS](#gade9c8363d332d7740b454e2920315ac5) 1000000000000

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

typedef enum [NetworkBoost\_DataSpeedSimpleAction](#gae2c308911ff3569b20102600d64d460a) [NetworkBoost\_DataSpeedSimpleAction](#gac06c759288ec3617480002297aa11dab)

 | 

Defines the enumeration of the suggested packet transmission policy.

 |
| 

typedef enum [NetworkBoost\_ErrorResult](#ga98419dae6f140b89cac79821f9cbbc9d) [NetworkBoost\_ErrorResult](#ga6946f85cae25ae0ebfd5bbee9579cd08)

 | 

Defines the enumeration of the network handover result.

 |
| 

typedef enum [NetworkBoost\_ReEstAction](#ga99d4ae084f2d5e3744231152e58e51aa) [NetworkBoost\_ReEstAction](#gab5ab8d4dfd6770df9ddf344440fe39c9)

 | 

Defines the enumeration of the link re-establishment type.

 |
| 

typedef struct [NetworkBoost\_DataSpeedAction](../../header-files-and-structs/structs/networkboost-dataspeedaction/document.md) [NetworkBoost\_DataSpeedAction](#ga98032d55873b9c438e4fe7a4393b6ebb)

 | 

Defines the recommended packet transmission rate.

 |
| 

typedef struct [NetworkBoost\_NetHandle](../../header-files-and-structs/structs/networkboost-nethandle/document.md) [NetworkBoost\_NetHandle](#ga83a1277967e95e2965b6f8dbee5945cc)

 | 

Defines the network handling information.

 |
| 

typedef struct [NetworkBoost\_HandoverStart](../../header-files-and-structs/structs/networkboost-handoverstart/document.md) [NetworkBoost\_HandoverStart](#gae5e48d9919724eba0c72d4e320122ca6)

 | 

Defines the information about the start of network handover.

 |
| 

typedef struct [NetworkBoost\_HandoverComplete](../../header-files-and-structs/structs/networkboost-handovercomplete/document.md) [NetworkBoost\_HandoverComplete](#ga9490335b78db33fe8effe0674036146f)

 | 

Defines the information about the end of network handover.

 |
| 

typedef enum [NetworkBoost\_HandoverMode](#ga7911fd83a6c8af864d1c87e67d5b0cb1) [NetworkBoost\_HandoverMode](#gaf4d63e47ed8a29ad3bd4104669d80755)

 | 

Defines the enumeration of the network handover mode.

 |
| 

typedef void(\* [HMS\_NetworkBoost\_OnHandoverStart](#gaeb846c7c42199e314b95770657ed583d)) ([NetworkBoost\_HandoverStart](../../header-files-and-structs/structs/networkboost-handoverstart/document.md) \*handoverStart)

 | 

Defines the callback prototype triggered when the network handover starts.

 |
| 

typedef void(\* [HMS\_NetworkBoost\_OnHandoverComplete](#ga799fbecb09ede04fec174737425082f6)) ([NetworkBoost\_HandoverComplete](../../header-files-and-structs/structs/networkboost-handovercomplete/document.md) \*handoverComplete)

 | 

Defines the callback prototype triggered when the network handover ends.

 |
| 

typedef struct [HMS\_NetworkBoost\_HandoverCallback](../../header-files-and-structs/structs/hms-networkboost-handovercallback/document.md) [HMS\_NetworkBoost\_HandoverCallback](#ga8ce6f265f4275452f332441338e3035c)

 | 

Defines the parameters for registering a callback function to handle network handover, including start and end.

 |
| 

typedef enum [NetworkBoost\_RecommendedAction](#ga42f25be03d340c17630c3a0f9cd0d123) [NetworkBoost\_RecommendedAction](#ga3543e6660b965ebc071fd13d359d6a39)

 | 

Defines the enumeration of the suggested data transmission policy.

 |
| 

typedef enum [NetworkBoost\_PathType](#gae8474ae83c3add50ac3fa7702c089ea8) [NetworkBoost\_PathType](#ga45748b2a298346cbea2f1cbe573ffe72)

 | 

Defines the enumeration of the path type.

 |
| 

typedef enum [NetworkBoost\_Scene](#ga972c3eb36772eb1affb0cd551429547b) [NetworkBoost\_Scene](#ga551f8ada8a742207e5eba134765d2a0f)

 | 

Defines the enumeration of the network scenario type.

 |
| 

typedef enum [NetworkBoost\_ServiceType](#ga5b192f3d72de3ac083df4cf36cbc318f) [NetworkBoost\_ServiceType](#gaabe242932bb115198d2f27c0deedb0f5)

 | 

Defines the enumeration of the app service type.

 |
| 

typedef enum [NetworkBoost\_QoeType](#ga539adc59ea2ca1c7498eac3a59bc62be) [NetworkBoost\_QoeType](#ga152febbb6bccad7017f37457e433ba6e)

 | 

Defines the enumeration of the network quality data type of the app.

 |
| 

typedef struct [NetworkBoost\_NetworkQos](../../header-files-and-structs/structs/networkboost-networkqos/document.md) [NetworkBoost\_NetworkQos](#ga950f78df8282426c91728728c8ca9e8e)

 | 

Defines the network quality information of a single path that is returned.

 |
| 

typedef struct [NetworkBoost\_NetworkQosArray](../../header-files-and-structs/structs/networkboost-networkqosarray/document.md) [NetworkBoost\_NetworkQosArray](#gac61cbd4df3cf59284dcbdc5860e6ef9b)

 | 

Defines the network quality information of multiple paths that is returned.

 |
| 

typedef struct [NetworkBoost\_WeakSignalPrediction](../../header-files-and-structs/structs/networkboost-weaksignalprediction/document.md) [NetworkBoost\_WeakSignalPrediction](#ga2d2d1a19e06dd2746d18eb9eaa8ae8af)

 | 

Defines weak signal prediction information.

 |
| 

typedef struct [NetworkBoost\_NetworkScene](../../header-files-and-structs/structs/networkboost-networkscene/document.md) [NetworkBoost\_NetworkScene](#ga133be4442e775aa5b062a29f6de9bfe0)

 | 

Defines the network scenario change information that is returned.

 |
| 

typedef void(\* [HMS\_NetworkBoost\_NetQosChange](#ga51a4f0de15c82e94eceafdc8444dd51a)) ([NetworkBoost\_NetworkQosArray](../../header-files-and-structs/structs/networkboost-networkqosarray/document.md) \*networkQosArray)

 | 

Defines the callback function prototype for network quality changes.

 |
| 

typedef void(\* [HMS\_NetworkBoost\_NetSceneChange](#gab00c153ac0c6faf6066cd013ac1d97d4)) ([NetworkBoost\_NetworkScene](../../header-files-and-structs/structs/networkboost-networkscene/document.md) \*networkScene)

 | 

Defines the callback function prototype for network scenario changes.

 |
| 

typedef void (\* [HMS\_NetworkBoost\_OnMultiPathRequestResult](#section1291820306417))([NetworkBoost\_MultiPathRequestResult](../../header-files-and-structs/structs/networkboost-multipathrequestresult/document.md)\* result)

 | 

Defines the callback prototype for multi-network concurrency request results.

 |
| 

typedef void (\* [HMS\_NetworkBoost\_OnMultiPathStateChange](#section192149121805))([NetworkBoost\_MultiPathStateChange](../../header-files-and-structs/structs/networkboost-multipathstatechange/document.md)\* multiPathState)

 | 

Defines the callback prototype for multi-network concurrency status changes.

 |
| 

typedef void (\* [HMS\_NetworkBoost\_OnMultiPathRecommendation](#section198348561206))([NetworkBoost\_MultiPathRecommendation](../../header-files-and-structs/structs/networkboost-multipathrecommendation/document.md)\* recommendation)

 | 

Defines the callback prototype for multi-network concurrency suggestion changes.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[NetworkBoost\_DataSpeedSimpleAction](#gae2c308911ff3569b20102600d64d460a) { NB\_SIMPLEACTION\_SUSPEND\_DATA = 1, NB\_SIMPLEACTION\_DECREASE\_DATA = 2, NB\_SIMPLEACTION\_INCREASE\_DATA = 3, NB\_SIMPLEACTION\_KEEP\_DATA = 4 }

 | 

Defines the enumeration of the suggested packet transmission policy.

 |
| 

[NetworkBoost\_ErrorResult](#ga98419dae6f140b89cac79821f9cbbc9d) { NB\_ERROR\_NONE = 0, NB\_ERROR\_HANDOVER\_TIMEOUT = 1, NB\_ERROR\_NEW\_PATH\_ACTIVATION\_FAILED = 2, NB\_ERROR\_ABORT = 3 }

 | 

Defines the enumeration of the network handover result.

 |
| 

[NetworkBoost\_ReEstAction](#ga99d4ae084f2d5e3744231152e58e51aa) {

NB\_REEST\_DEFAULT = 0, NB\_REEST\_QUERY\_DNS = 1, NB\_REEST\_CHANGE\_REMOTE\_IP = 2, NB\_REEST\_CHANGE\_IP\_VERSION = 3,

NB\_NO\_EST = 4

}

 | 

Defines the enumeration of the link re-establishment type.

 |
| 

[NetworkBoost\_HandoverMode](#ga7911fd83a6c8af864d1c87e67d5b0cb1) { NB\_MODE\_DELEGATION = 0, NB\_MODE\_DISCRETION = 1 }

 | 

Defines the enumeration of the network handover mode.

 |
| 

[NetworkBoost\_RecommendedAction](#ga42f25be03d340c17630c3a0f9cd0d123) {

NB\_ACTION\_DO\_CACHING = 0, NB\_ACTION\_SUSPEND\_DATA = 1, NB\_ACTION\_DECREASE\_DATA = 2, NB\_ACTION\_INCREASE\_DATA = 3,

NB\_ACTION\_KEEP\_DATA = 4

}

 | 

Defines the enumeration of the suggested data transmission policy.

 |
| 

[NetworkBoost\_PathType](#gae8474ae83c3add50ac3fa7702c089ea8) { NB\_PATH\_CELLULAR\_PRIMARY = 0, NB\_PATH\_CELLULAR\_SECONDARY = 1, NB\_PATH\_WIFI\_PRIMARY = 2, NB\_PATH\_WIFI\_SECONDARY = 3 }

 | 

Defines the enumeration of the path type.

 |
| 

[NetworkBoost\_Scene](#ga972c3eb36772eb1affb0cd551429547b) { NB\_SCENE\_NORMAL = 0, NB\_SCENE\_CONGESTION = 1, NB\_SCENE\_FREQUENT\_HANDOVER = 2, NB\_SCENE\_WEAK\_SIGNAL = 3 }

 | 

Defines the enumeration of the network scenario type.

 |
| 

[NetworkBoost\_ServiceType](#ga5b192f3d72de3ac083df4cf36cbc318f) {

NB\_SERVICE\_DEFAULT = 0, NB\_SERVICE\_BACKGROUND = 1, NB\_SERVICE\_REAL\_TIME\_VOICE = 2, NB\_SERVICE\_REAL\_TIME\_VIDEO = 3,

NB\_SERVICE\_CALL\_SIGNALING = 4, NB\_SERVICE\_REAL\_TIME\_GAME = 5, NB\_SERVICE\_NORMAL\_GAME = 6, NB\_SERVICE\_SHORT\_VIDEO = 7,

NB\_SERVICE\_LONG\_VIDEO = 8, NB\_SERVICE\_LIVE\_STREAMING\_ANCHOR = 9, NB\_SERVICE\_LIVE\_STREAMING\_WATCHER = 10, NB\_SERVICE\_DOWNLOAD = 11,

NB\_SERVICE\_UPLOAD = 12, NB\_SERVICE\_BROWSER = 13, NB\_SERVICE\_BROWSER = 13, NB\_SERVICE\_TRANSACTION = 14, NB\_SERVICE\_DETECTION = 15, NB\_SERVICE\_CLOUDSERVICE = 16, NB\_SERVICE\_VOICE\_CONFERENCE = 17, NB\_SERVICE\_VIDEO\_CONFERENCE = 18, NB\_SERVICE\_NAVIGATION = 19, NB\_SERVICE\_SECKILL\_SERVICE = 20, NB\_SERVICE\_LOGIN = 21, NB\_SERVICE\_AUDIO = 22, NB\_SERVICE\_SHOPPING = 23

}

 | 

Defines the enumeration of the app service type.

 |
| 

[NetworkBoost\_QoeType](#ga539adc59ea2ca1c7498eac3a59bc62be) {

NB\_QOE\_GOOD = 0, NB\_QOE\_BAD\_UNKNOWN = 1, NB\_QOE\_BAD\_SERVER\_ERROR = 2, NB\_QOE\_BAD\_NO\_DATA = 3,

NB\_QOE\_BAD\_PACKET\_LOST = 4, NB\_QOE\_BAD\_PACKET\_OUT\_OF\_ORDER = 5, NB\_QOE\_BAD\_HIGH\_JITTER = 6, NB\_QOE\_BAD\_HIGH\_LATENCY = 7

}

 | 

Defines the enumeration of the network quality data type of the app.

 |
| 

[NetworkBoost\_PathState](#section1774664693518) {

NB\_PATH\_IDLE = 0, NB\_PATH\_CONNECTED = 1, NB\_PATH\_SUSPENDED = 2

}

 | 

Defines the enumeration for the status of a data path other than the default path in multi-network concurrency.

 |
| 

[NetworkBoost\_MultiPathErrorResult](#section129101047154112) {

NB\_MULTIPATH\_ERROR\_NONE = 0, NB\_MULTIPATH\_ERROR\_NETWORK\_REFUSED = 1, NB\_MULTIPATH\_ERROR\_TIMEOUT = 2, NB\_MULTIPATH\_ERROR\_LOCAL = 3

}

 | 

Defines the enumeration of the multi-network concurrency initiation result.

 |
| 

[NetworkBoost\_MultiPathChangeCause](#section19927184203916) {

NB\_MULTIPATH\_CAUSE\_REQUEST\_NORMAL = 0, NB\_MULTIPATH\_CAUSE\_RELEASE\_NORMAL = 50, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_NETWORK = 51, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_USER\_REFUSED = 52, NB\_MULTIPATH\_CAUSE\_RELEASE\_NO\_QUOTA = 53, NB\_MULTIPATH\_CAUSE\_RELEASE\_POWER\_CONSUMPTION = 54, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_INSUFFICIENT\_TRAFFIC = 55, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_CONFLICT = 56, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_FUSING = 57, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_DEFAULT = 99, NB\_MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_ENTER = 100, NB\_MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_LEAVE = 101, NB\_MULTIPATH\_CHANGE\_CAUSE\_CONN\_PROPERTIES\_UPDATE = 102

}

 | 

Defines the enumeration of the reasons why multi-network concurrency status changes.

 |
| 

[NetworkBoost\_MultiPathState](#section12626124820456) {

NB\_MULTIPATH\_IDLE = 0, NB\_MULTIPATH\_CREATEING = 1, NB\_MULTIPATH\_CREATED = 2, NB\_MULTIPATH\_RELEASING = 3

}

 | 

Defines the enumeration for the status of multi-network concurrency.

 |
| 

[NetworkBoost\_MultiPathAction](#section12185112974610) {

NB\_MULTIPATH\_ACTION\_REQUEST = 0, NB\_MULTIPATH\_ACTION\_RELEASE = 1

}

 | 

Defines the enumeration of suggested multi-network concurrency actions.

 |
| 

[NetworkBoost\_SceneEvent](#section9626183119507) {

NB\_SCENE\_EVENT\_ENTER = 0, NB\_SCENE\_EVENT\_UPDATE = 1, NB\_SCENE\_EVENT\_LEAVE = 2

}

 | 

Defines the enumeration of service scenario events.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

int32\_t [HMS\_NetworkBoost\_RegisterHandoverChangeCallback](#gac3d95b4bf5c8cbec5ca862130d441fce) ([HMS\_NetworkBoost\_HandoverCallback](../../header-files-and-structs/structs/hms-networkboost-handovercallback/document.md) \*callback, uint32\_t \*callbackId)

 | 

Registers the network handover callback.

 |
| 

int32\_t [HMS\_NetworkBoost\_UnregisterHandoverChangeCallback](#gaca0ae3e209bc314e808d808786d76eae) (uint32\_t callbackId)

 | 

Deregisters the network handover callback.

 |
| 

int32\_t [HMS\_NetworkBoost\_SetHandoverMode](#ga1f03a8af2bbf9de6af215df385498a7a) ([NetworkBoost\_HandoverMode](#ga7911fd83a6c8af864d1c87e67d5b0cb1) mode)

 | 

Defines the network handover mode. Your app can call the relevant API to change the network handover mode between delegation mode and proactive mode. The default mode is delegation.

 |
| 

int32\_t [HMS\_NetworkBoost\_RegisterNetQosCallback](#ga72cac93efbd98d448ae2d3dc7d3b3dfe) ([HMS\_NetworkBoost\_NetQosChange](#ga51a4f0de15c82e94eceafdc8444dd51a) callback, uint32\_t \*callbackId)

 | 

Registers the network quality change callback.

 |
| 

int32\_t [HMS\_NetworkBoost\_UnregisterNetQosCallback](#gae435e58413bd125a9bca06aed0b6ebfe) (uint32\_t callbackId)

 | 

Deregisters the network quality change callback.

 |
| 

int32\_t [HMS\_NetworkBoost\_RegisterNetSceneCallback](#ga13b998a6c6fca1a4b84dd77f547f20ea) ([HMS\_NetworkBoost\_NetSceneChange](#gab00c153ac0c6faf6066cd013ac1d97d4) callback, uint32\_t \*callbackId)

 | 

Registers the network scenario change callback.

 |
| 

int32\_t [HMS\_NetworkBoost\_UnregisterNetSceneCallback](#gad7e9989cb65b01ba52e0b8427fa3e113) (uint32\_t callbackId)

 | 

Deregisters the network scenario change callback.

 |
| 

int32\_t [HMS\_NetworkBoost\_ReportQoe](#ga2d62d2b3ec0536118a28175d53e0f363) ([NetworkBoost\_ServiceType](#ga5b192f3d72de3ac083df4cf36cbc318f) serviceType, [NetworkBoost\_QoeType](#ga539adc59ea2ca1c7498eac3a59bc62be) qoeType)

 | 

Sends back the app data transmission experience.

 |
| 

int32\_t [HMS\_NetworkBoost\_GetMultiPathQuotaStats](#section3899010125311)([NetworkBoost\_MultiPathQuota](../../header-files-and-structs/structs/networkboost-multipathquota/document.md) \*quota)

 | 

Obtains the quota information of multi-network concurrency, including the used and remaining quotas.

 |
| 

int32\_t [HMS\_NetworkBoost\_RequestMultiPath](#section13240250195914)([HMS\_NetworkBoost\_OnMultiPathRequestResult](../../header-files-and-structs/structs/networkboost-multipathrequestresult/document.md) result)

 | 

Initiates a multi-network concurrency request.

 |
| 

int32\_t [HMS\_NetworkBoost\_ReleaseMultiPath](#section58537189614)()

 | 

Releases multi-network concurrency.

 |
| 

int32\_t [HMS\_NetworkBoost\_RegisterMultiPathStateChangeCallback](#section421172813919)([HMS\_NetworkBoost\_OnMultiPathStateChange](#section192149121805) callback, uint32\_t\* callbackId)

 | 

Registers the callback triggered when a multi-network concurrency status change event occurs.

 |
| 

int32\_t [HMS\_NetworkBoost\_UnregisterMultiPathStateChangeCallback](#section52786305915)(uint32\_t callbackId)

 | 

Deregisters the callback triggered when a multi-network concurrency status change event occurs.

 |
| 

int32\_t [HMS\_NetworkBoost\_RegisterMultiPathRecommendationCallback](#section463012484123)([HMS\_NetworkBoost\_OnMultiPathRecommendation](#section198348561206) callback, uint32\_t\* callbackId)

 | 

Registers the callback triggered when the multi-network concurrency suggestion provided by the device changes.

 |
| 

int32\_t [HMS\_NetworkBoost\_UnregisterMultiPathRecommendationCallback](#section18632948201214)(uint32\_t callbackId)

 | 

Deregisters the callback triggered when the multi-network concurrency suggestion provided by the device changes.

 |
| 

int32\_t [HMS\_NetworkBoost\_SetSceneDesc](#section1441013415156)([NetworkBoost\_SceneDesc](../../header-files-and-structs/structs/networkboost-scenedesc/document.md) sceneDesc)

 | 

Sets the service scenario.

 |

#### Macro Description

#### \[h2\]NB\_BPS

#define NB\_BPS   1

**Description**

1 bit/s.

**Start version**: 5.1.0(18)

#### \[h2\]NB\_GBPS

#define NB\_GBPS   1000000000

**Description**

1 Gbit/s.

**Start version**: 5.1.0(18)

#### \[h2\]NB\_KBPS

#define NB\_KBPS   1000

**Description**

1 kbit/s.

**Start version**: 5.1.0(18)

#### \[h2\]NB\_MBPS

#define NB\_MBPS   1000000

**Description**

1 Mbit/s.

**Start version**: 5.1.0(18)

#### \[h2\]NB\_TBPS

#define NB\_TBPS   1000000000000

**Description**

1 Tbit/s. To handle this, utilize the uint64\_t data type to prevent overflow.

**Start version**: 5.1.0(18)

#### \[h2\]NETBOOST\_MAX\_PATH\_NUM

#define NETBOOST\_MAX\_PATH\_NUM   4

**Description**

Maximum length of the array of details about network quality changes.

**Start version**: 5.1.0(18)

#### Type Definition Description

#### \[h2\]HMS\_NetworkBoost\_HandoverCallback

typedef struct [HMS\_NetworkBoost\_HandoverCallback](../../header-files-and-structs/structs/hms-networkboost-handovercallback/document.md) [HMS\_NetworkBoost\_HandoverCallback](../../header-files-and-structs/structs/hms-networkboost-handovercallback/document.md)

**Description**

Defines the network handover information that is returned. Each method in the callback cannot be empty.

**Start version**: 5.1.0(18)

#### \[h2\]HMS\_NetworkBoost\_NetQosChange

typedef void(\* HMS\_NetworkBoost\_NetQosChange) ([NetworkBoost\_NetworkQosArray](../../header-files-and-structs/structs/networkboost-networkqosarray/document.md) \*networkQosArray)

**Description**

Callback function, which is used to return network quality change details.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

networkQosArray

 | 

Network quality change details.

 |

#### \[h2\]HMS\_NetworkBoost\_NetSceneChange

typedef void(\* HMS\_NetworkBoost\_NetSceneChange) ([NetworkBoost\_NetworkScene](../../header-files-and-structs/structs/networkboost-networkscene/document.md) \*networkScene)

**Description**

Callback function, which is used to return network scenario change details.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

networkScene

 | 

Network scenario change details.

 |

#### \[h2\]HMS\_NetworkBoost\_OnHandoverComplete

typedef void(\* HMS\_NetworkBoost\_OnHandoverComplete) ([NetworkBoost\_HandoverComplete](../../header-files-and-structs/structs/networkboost-handovercomplete/document.md) \*handoverComplete)

**Description**

Callback function, which returns the details about the end of a network handover.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

handoverComplete

 | 

Details about the end of network handover.

 |

#### \[h2\]HMS\_NetworkBoost\_OnHandoverStart

typedef void(\* HMS\_NetworkBoost\_OnHandoverStart) ([NetworkBoost\_HandoverStart](../../header-files-and-structs/structs/networkboost-handoverstart/document.md) \*handoverStart)

**Description**

Callback function, which returns the details about the start of a network handover.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

handoverStart

 | 

Details about the start of network handover.

 |

#### \[h2\]HMS\_NetworkBoost\_OnMultiPathRequestResult

typedef void (\*HMS\_NetworkBoost\_OnMultiPathRequestResult)(NetworkBoost\_MultiPathRequestResult\* result)

**Description**

Defines the callback prototype for multi-network concurrency request results.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

result

 | 

Result of initiating multi-network concurrency.

 |

#### \[h2\]HMS\_NetworkBoost\_OnMultiPathStateChange

typedef void (\*HMS\_NetworkBoost\_OnMultiPathStateChange)(NetworkBoost\_MultiPathStateChange\* multiPathState)

**Description**

Defines the callback prototype for multi-network concurrency status changes.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

multiPathState

 | 

Multi-network concurrency status information.

 |

#### \[h2\]HMS\_NetworkBoost\_OnMultiPathRecommendation

typedef void (\*HMS\_NetworkBoost\_OnMultiPathRecommendation)(NetworkBoost\_MultiPathRecommendation\* recommendation)

**Description**

Defines the callback prototype for multi-network concurrency suggestion information.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

recommendation

 | 

Multi-network concurrency suggestion information.

 |

#### \[h2\]NetworkBoost\_DataSpeedAction

typedef struct [NetworkBoost\_DataSpeedAction](../../header-files-and-structs/structs/networkboost-dataspeedaction/document.md) [NetworkBoost\_DataSpeedAction](../../header-files-and-structs/structs/networkboost-dataspeedaction/document.md)

**Description**

Defines the recommended packet transmission rate.

**Start version**: 5.1.0(18)

#### \[h2\]NetworkBoost\_DataSpeedSimpleAction

typedef enum [NetworkBoost\_DataSpeedSimpleAction](#gae2c308911ff3569b20102600d64d460a) [NetworkBoost\_DataSpeedSimpleAction](#gae2c308911ff3569b20102600d64d460a)

**Description**

Defines the enumeration of the suggested packet transmission policy.

**Start version**: 5.1.0(18)

#### \[h2\]NetworkBoost\_ErrorResult

typedef enum [NetworkBoost\_ErrorResult](#ga98419dae6f140b89cac79821f9cbbc9d) [NetworkBoost\_ErrorResult](#ga98419dae6f140b89cac79821f9cbbc9d)

**Description**

Defines the network handover result.

**Start version**: 5.1.0(18)

#### \[h2\]NetworkBoost\_HandoverComplete

typedef struct [NetworkBoost\_HandoverComplete](../../header-files-and-structs/structs/networkboost-handovercomplete/document.md) [NetworkBoost\_HandoverComplete](../../header-files-and-structs/structs/networkboost-handovercomplete/document.md)

**Description**

Defines the information about the end of network handover.

**Start version**: 5.1.0(18)

#### \[h2\]NetworkBoost\_HandoverMode

typedef enum [NetworkBoost\_HandoverMode](#ga7911fd83a6c8af864d1c87e67d5b0cb1) [NetworkBoost\_HandoverMode](#ga7911fd83a6c8af864d1c87e67d5b0cb1)

**Description**

Defines the enumeration of the network handover mode.

**Start version**: 5.1.0(18)

#### \[h2\]NetworkBoost\_HandoverStart

typedef struct [NetworkBoost\_HandoverStart](../../header-files-and-structs/structs/networkboost-handoverstart/document.md) [NetworkBoost\_HandoverStart](../../header-files-and-structs/structs/networkboost-handoverstart/document.md)

**Description**

Defines the information about the start of network handover.

**Start version**: 5.1.0(18)

#### \[h2\]NetworkBoost\_NetHandle

typedef struct [NetworkBoost\_NetHandle](../../header-files-and-structs/structs/networkboost-nethandle/document.md) [NetworkBoost\_NetHandle](../../header-files-and-structs/structs/networkboost-nethandle/document.md)

**Description**

Defines the handle of the data network.

**Start version**: 5.1.0(18)

#### \[h2\]NetworkBoost\_NetworkQos

typedef struct [NetworkBoost\_NetworkQos](../../header-files-and-structs/structs/networkboost-networkqos/document.md) [NetworkBoost\_NetworkQos](../../header-files-and-structs/structs/networkboost-networkqos/document.md)

**Description**

Defines the network quality information of a single path that is returned.

**Start version**: 5.1.0(18)

#### \[h2\]NetworkBoost\_NetworkQosArray

typedef struct [NetworkBoost\_NetworkQosArray](../../header-files-and-structs/structs/networkboost-networkqosarray/document.md) [NetworkBoost\_NetworkQosArray](../../header-files-and-structs/structs/networkboost-networkqosarray/document.md)

**Description**

Defines the network quality information of multiple paths that is returned.

**Start version**: 5.1.0(18)

#### \[h2\]NetworkBoost\_NetworkScene

typedef struct [NetworkBoost\_NetworkScene](../../header-files-and-structs/structs/networkboost-networkscene/document.md) [NetworkBoost\_NetworkScene](../../header-files-and-structs/structs/networkboost-networkscene/document.md)

**Description**

Defines the network scenario change information that is returned.

**Start version**: 5.1.0(18)

#### \[h2\]NetworkBoost\_PathType

typedef enum [NetworkBoost\_PathType](#gae8474ae83c3add50ac3fa7702c089ea8) [NetworkBoost\_PathType](#gae8474ae83c3add50ac3fa7702c089ea8)

**Description**

Defines the path type.

**Start version**: 5.1.0(18)

#### \[h2\]NetworkBoost\_QoeType

typedef enum [NetworkBoost\_QoeType](#ga539adc59ea2ca1c7498eac3a59bc62be) [NetworkBoost\_QoeType](#ga539adc59ea2ca1c7498eac3a59bc62be)

**Description**

Defines the enumeration of the network quality data type of the app.

**Start version**: 5.1.0(18)

#### \[h2\]NetworkBoost\_RecommendedAction

typedef enum [NetworkBoost\_RecommendedAction](#ga42f25be03d340c17630c3a0f9cd0d123) [NetworkBoost\_RecommendedAction](#ga42f25be03d340c17630c3a0f9cd0d123)

**Description**

Defines the enumeration of the recommended data transmission policy.

**Start version**: 5.1.0(18)

#### \[h2\]NetworkBoost\_ReEstAction

typedef enum [NetworkBoost\_ReEstAction](#ga99d4ae084f2d5e3744231152e58e51aa) [NetworkBoost\_ReEstAction](#ga99d4ae084f2d5e3744231152e58e51aa)

**Description**

Defines the enumeration of the link re-establishment type.

**Start version**: 5.1.0(18)

#### \[h2\]NetworkBoost\_Scene

typedef enum [NetworkBoost\_Scene](#ga972c3eb36772eb1affb0cd551429547b) [NetworkBoost\_Scene](#ga972c3eb36772eb1affb0cd551429547b)

**Description**

Defines the enumeration of the network scenario type.

**Start version**: 5.1.0(18)

#### \[h2\]NetworkBoost\_ServiceType

typedef enum [NetworkBoost\_ServiceType](#ga5b192f3d72de3ac083df4cf36cbc318f) [NetworkBoost\_ServiceType](#ga5b192f3d72de3ac083df4cf36cbc318f)

**Description**

Defines the enumeration of the app service type.

**Start version**: 5.1.0(18)

#### \[h2\]NetworkBoost\_WeakSignalPrediction

typedef struct [NetworkBoost\_WeakSignalPrediction](../../header-files-and-structs/structs/networkboost-weaksignalprediction/document.md) [NetworkBoost\_WeakSignalPrediction](../../header-files-and-structs/structs/networkboost-weaksignalprediction/document.md)

**Description**

Defines weak signal prediction information.

**Start version**: 5.1.0(18)

#### Enumeration Type Description

#### \[h2\]NetworkBoost\_DataSpeedSimpleAction

enum [NetworkBoost\_DataSpeedSimpleAction](#gae2c308911ff3569b20102600d64d460a)

**Description**

Defines the enumeration of the suggested packet transmission policy.

**Start version**: 5.1.0(18)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

NB\_SIMPLEACTION\_SUSPEND\_DATA

 | 

Stops packet sending.

 |
| 

NB\_SIMPLEACTION\_DECREASE\_DATA

 | 

Decreases the packet transmission rate.

 |
| 

NB\_SIMPLEACTION\_INCREASE\_DATA

 | 

Increases the packet transmission rate.

 |
| 

NB\_SIMPLEACTION\_KEEP\_DATA

 | 

Keeps the current packet transmission rate.

 |

#### \[h2\]NetworkBoost\_ErrorResult

enum [NetworkBoost\_ErrorResult](#ga98419dae6f140b89cac79821f9cbbc9d)

**Description**

Defines the enumeration of the network handover result.

**Start version**: 5.1.0(18)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

NB\_ERROR\_NONE

 | 

The network handover is successful.

 |
| 

NB\_ERROR\_HANDOVER\_TIMEOUT

 | 

The network handover timed out.

 |
| 

NB\_ERROR\_NEW\_PATH\_ACTIVATION\_FAILED

 | 

The new link failed to be activated.

 |
| 

NB\_ERROR\_ABORT

 | 

Network handover was canceled.

 |

#### \[h2\]NetworkBoost\_HandoverMode

enum [NetworkBoost\_HandoverMode](#ga7911fd83a6c8af864d1c87e67d5b0cb1)

**Description**

Defines the enumeration of the network handover mode.

**Start version**: 5.1.0(18)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

NB\_MODE\_DELEGATION

 | 

Delegation mode, indicating that the device initiates network handover. This is the default mode.

 |
| 

NB\_MODE\_DISCRETION

 | 

Proactive mode, indicating that the app initiates network handover. An app can call this API to forbid the device to initiate network handover. However, in some cases, for example, when the app is switched to the background, the device may still initiate network handover even if the API is called.

 |

#### \[h2\]NetworkBoost\_PathType

enum [NetworkBoost\_PathType](#gae8474ae83c3add50ac3fa7702c089ea8)

**Description**

Defines the enumeration of the data path type.

**Start version**: 5.1.0(18)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

NB\_PATH\_CELLULAR\_PRIMARY

 | 

Primary SIM card.

 |
| 

NB\_PATH\_CELLULAR\_SECONDARY

 | 

Secondary SIM card.

 |
| 

NB\_PATH\_WIFI\_PRIMARY

 | 

Primary Wi-Fi.

 |
| 

NB\_PATH\_WIFI\_SECONDARY

 | 

Secondary Wi-Fi.

 |

#### \[h2\]NetworkBoost\_QoeType

enum [NetworkBoost\_QoeType](#ga539adc59ea2ca1c7498eac3a59bc62be)

**Description**

Defines the enumeration of the network quality data type of the app.

**Start version**: 5.1.0(18)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

NB\_QOE\_GOOD

 | 

Good experience.

 |
| 

NB\_QOE\_BAD\_UNKNOWN

 | 

Poor experience: unknown cause.

 |
| 

NB\_QOE\_BAD\_SERVER\_ERROR

 | 

Poor experience: server exception.

 |
| 

NB\_QOE\_BAD\_NO\_DATA

 | 

Poor experience: no data.

 |
| 

NB\_QOE\_BAD\_PACKET\_LOST

 | 

Poor experience: packet loss.

 |
| 

NB\_QOE\_BAD\_PACKET\_OUT\_OF\_ORDER

 | 

Poor experience: packets out of order.

 |
| 

NB\_QOE\_BAD\_HIGH\_JITTER

 | 

Poor experience: high jitter.

 |
| 

NB\_QOE\_BAD\_HIGH\_LATENCY

 | 

Poor experience: high latency.

 |

#### \[h2\]NetworkBoost\_RecommendedAction

enum [NetworkBoost\_RecommendedAction](#ga42f25be03d340c17630c3a0f9cd0d123)

**Description**

Defines the enumeration of the suggested data transmission policy.

**Start version**: 5.1.0(18)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

NB\_ACTION\_DO\_CACHING

 | 

Caches data.

 |
| 

NB\_ACTION\_SUSPEND\_DATA

 | 

Stops packet sending.

 |
| 

NB\_ACTION\_DECREASE\_DATA

 | 

Decreases the packet transmission rate.

 |
| 

NB\_ACTION\_INCREASE\_DATA

 | 

Increases the packet transmission rate.

 |
| 

NB\_ACTION\_KEEP\_DATA

 | 

Keeps the current packet transmission rate.

 |

#### \[h2\]NetworkBoost\_ReEstAction

enum [NetworkBoost\_ReEstAction](#ga99d4ae084f2d5e3744231152e58e51aa)

**Description**

Defines the enumeration of the link re-establishment type.

**Start version**: 5.1.0(18)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

NB\_REEST\_DEFAULT

 | 

The app needs to re-establish the link to the same remote IP address.

 |
| 

NB\_REEST\_QUERY\_DNS

 | 

The link type changes, for example, between Wi-Fi and cellular network, or the carrier information of the link changes.

 |
| 

NB\_REEST\_CHANGE\_REMOTE\_IP

 | 

The app needs to re-establish the link to a different IP address.

 |
| 

NB\_REEST\_CHANGE\_IP\_VERSION

 | 

The app needs to re-establish the link by changing the IP address type, for example, between IPv4 and IPv6.

 |
| 

NB\_NO\_EST

 | 

The app needs to request network resources through the original data link, without the need to re-establish the link.

 |

#### \[h2\]NetworkBoost\_Scene

enum [NetworkBoost\_Scene](#ga972c3eb36772eb1affb0cd551429547b)

**Description**

Defines the enumeration of the network scenario type.

**Start version**: 5.1.0(18)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

NB\_SCENE\_NORMAL

 | 

Common network scenario.

 |
| 

NB\_SCENE\_CONGESTION

 | 

Congestion scenario.

 |
| 

NB\_SCENE\_FREQUENT\_HANDOVER

 | 

Scenario of frequent handovers between cells.

 |
| 

NB\_SCENE\_WEAK\_SIGNAL

 | 

Weak signal scenario.

 |

#### \[h2\]NetworkBoost\_ServiceType

enum [NetworkBoost\_ServiceType](#ga5b192f3d72de3ac083df4cf36cbc318f)

**Description**

Defines the enumeration of the app service type.

**Start version**: 5.1.0(18)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

NB\_SERVICE\_DEFAULT

 | 

Default service type.

 |
| 

NB\_SERVICE\_BACKGROUND

 | 

Background service.

 |
| 

NB\_SERVICE\_REAL\_TIME\_VOICE

 | 

Real-time voice.

 |
| 

NB\_SERVICE\_REAL\_TIME\_VIDEO

 | 

Real-time video.

 |
| 

NB\_SERVICE\_CALL\_SIGNALING

 | 

Voice signaling.

 |
| 

NB\_SERVICE\_REAL\_TIME\_GAME

 | 

Real-time game.

 |
| 

NB\_SERVICE\_NORMAL\_GAME

 | 

Common game.

 |
| 

NB\_SERVICE\_SHORT\_VIDEO

 | 

Short video.

 |
| 

NB\_SERVICE\_LONG\_VIDEO

 | 

Long video.

 |
| 

NB\_SERVICE\_LIVE\_STREAMING\_ANCHOR

 | 

Live streamer service.

 |
| 

NB\_SERVICE\_LIVE\_STREAMING\_WATCHER

 | 

Live streaming viewer service.

 |
| 

NB\_SERVICE\_DOWNLOAD

 | 

Download.

 |
| 

NB\_SERVICE\_UPLOAD

 | 

Upload.

 |
| 

NB\_SERVICE\_BROWSER

 | 

Page browsing.

 |
| 

NB\_SERVICE\_TRANSACTION

 | 

Transaction payment or QR code scanning.

 |
| 

NB\_SERVICE\_DETECTION

 | 

Network probing.

 |
| 

NB\_SERVICE\_CLOUDSERVICE

 | 

Cloud service/game.

 |
| 

NB\_SERVICE\_VOICE\_CONFERENCE

 | 

Voice conference.

 |
| 

NB\_SERVICE\_VIDEO\_CONFERENCE

 | 

Video conference.

 |
| 

NB\_SERVICE\_NAVIGATION

 | 

Navigation and location.

 |
| 

NB\_SERVICE\_SECKILL\_SERVICE

 | 

Seckill service, such as ticket snatching, flash sale, order grabbing, or red envelope claiming.

 |
| 

NB\_SERVICE\_LOGIN

 | 

Sign-in (including one-tap sign-in).

 |
| 

NB\_SERVICE\_AUDIO

 | 

Music/Audio service.

 |
| 

NB\_SERVICE\_SHOPPING

 | 

Shopping.

 |

#### \[h2\]NetworkBoost\_PathState

enum [NetworkBoost\_PathState](#section1774664693518)

**Description**

Defines the enumeration for the status of a data path other than the default path in multi-network concurrency.

**Start version**: 6.0.2(22)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

NB\_PATH\_IDLE

 | 

The path in multi-network concurrency is idle.

 |
| 

NB\_PATH\_CONNECTED

 | 

The path in multi-network concurrency is set up.

 |
| 

NB\_PATH\_SUSPENDED

 | 

The path in multi-network concurrency is suspended.

 |

#### \[h2\]NetworkBoost\_MultiPathChangeCause

enum [NetworkBoost\_MultiPathChangeCause](#section19927184203916)

**Description**

Defines the enumeration of the reasons why multi-network concurrency status changes.

**Start version**: 6.0.2(22)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

NB\_MULTIPATH\_CAUSE\_REQUEST\_NORMAL

 | 

A multi-network concurrency request is normally initiated.

 |
| 

NB\_MULTIPATH\_CAUSE\_RELEASE\_NORMAL

 | 

Multi-network concurrency is normally released.

 |
| 

NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_NETWORK

 | 

Multi-network concurrency is released due to poor network conditions.

 |
| 

NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_USER\_REFUSED

 | 

Multi-network concurrency is released as the user turns off a relevant switch.

 |
| 

NB\_MULTIPATH\_CAUSE\_RELEASE\_NO\_QUOTA

 | 

Multi-network concurrency is released due to quota exhaustion.

 |
| 

NB\_MULTIPATH\_CAUSE\_RELEASE\_POWER\_CONSUMPTION

 | 

Multi-network concurrency is released due to power consumption factors.

 |
| 

NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_INSUFFICIENT\_TRAFFIC

 | 

Multi-network concurrency is released due to traffic consumption factors.

 |
| 

NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_CONFLICT

 | 

Multi-network concurrency is released due to scenario conflicts.

 |
| 

NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_FUSING

 | 

Multi-network concurrency is released by the device after an app improperly uses multi-network concurrency, for example, keeping multi-network concurrency on for a long time.

 |
| 

NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_DEFAULT

 | 

Multi-network concurrency is released due to network status changes of the device.

 |
| 

NB\_MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_ENTER

 | 

Multi-network concurrency is suspended. In this case, it is not released, but data transmission is actually suspended.

 |
| 

NB\_MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_LEAVE

 | 

Multi-network concurrency leaves the suspended state.

 |
| 

NB\_MULTIPATH\_CHANGE\_CAUSE\_CONN\_PROPERTIES\_UPDATE

 | 

Link attributes are updated for multi-network concurrency. For example, the IP address changes.

 |

#### \[h2\]NetworkBoost\_MultiPathErrorResult

enum [NetworkBoost\_MultiPathErrorResult](#section129101047154112)

**Description**

Defines the enumeration of the multi-network concurrency initiation result.

**Start version**: 6.0.2(22)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

NB\_MULTIPATH\_ERROR\_NONE

 | 

Multi-network concurrency initiated successfully.

 |
| 

NB\_MULTIPATH\_ERROR\_NETWORK\_REFUSED

 | 

Multi-network concurrency rejected.

 |
| 

NB\_MULTIPATH\_ERROR\_TIMEOUT

 | 

Multi-network concurrency timed out.

 |
| 

NB\_MULTIPATH\_ERROR\_LOCAL

 | 

Multi-network concurrency is released locally when it is being initiated. For example, multi-network concurrency conditions are no longer met due to cellular data switch being turned off or other events during the startup.

 |

#### \[h2\]NetworkBoost\_MultiPathState

enum [NetworkBoost\_MultiPathState](#section12626124820456)

**Description**

Defines the enumeration for the status of multi-network concurrency.

**Start version**: 6.0.2(22)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

NB\_MULTIPATH\_IDLE

 | 

Multi-network concurrency is available.

 |
| 

NB\_MULTIPATH\_CREATEING

 | 

Multi-network concurrency is being initiated.

 |
| 

NB\_MULTIPATH\_CREATED

 | 

Multi-network concurrency has been initiated.

 |
| 

NB\_MULTIPATH\_RELEASING

 | 

Multi-network concurrency is being released.

 |

#### \[h2\]NetworkBoost\_MultiPathAction

enum [NetworkBoost\_MultiPathAction](#section12185112974610)

**Description**

Defines the enumeration of suggested multi-network concurrency actions.

**Start version**: 6.0.2(22)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

NB\_MULTIPATH\_ACTION\_REQUEST

 | 

Initiate a multi-network concurrency request.

 |
| 

NB\_MULTIPATH\_ACTION\_RELEASE

 | 

Release multi-network concurrency.

 |

#### \[h2\]NetworkBoost\_SceneEvent

enum Networ[NetworkBoost\_SceneEvent](#section9626183119507)kBoost\_SceneEvent

**Description**

Defines the enumeration of service scenario events.

**Start version**: 6.0.2(22)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

NB\_SCENE\_EVENT\_ENTER

 | 

The app enters a service scenario.

 |
| 

NB\_SCENE\_EVENT\_UPDATE

 | 

The last service scenario event information is updated.

 |
| 

NB\_SCENE\_EVENT\_LEAVE

 | 

The app leaves a service scenario.

 |

#### Function Description

#### \[h2\]HMS\_NetworkBoost\_RegisterHandoverChangeCallback()

int32\_t HMS\_NetworkBoost\_RegisterHandoverChangeCallback ([HMS\_NetworkBoost\_HandoverCallback](../../header-files-and-structs/structs/hms-networkboost-handovercallback/document.md) \* callback, uint32\_t \* callbackId )

**Description**

Registers the network handover callback.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

callback

 | 

Callback function of the network handover information.

 |
| 

callbackId

 | 

ID of the callback function, which is allocated by the system and used to deregister the callback.

 |

**Returns**:

**0**: Success.

**201**: Insufficient permission.

**401**: Parameter error.

**801**: System capability not supported.

**62100001**: Internal error.

**62100002**: System service operation failure.

**62100003**: The number of registration requests has reached the upper limit.

**Permission**:

ohos.permission.GET\_NETWORK\_INFO

#### \[h2\]HMS\_NetworkBoost\_RegisterNetQosCallback()

int32\_t HMS\_NetworkBoost\_RegisterNetQosCallback ([HMS\_NetworkBoost\_NetQosChange](#ga51a4f0de15c82e94eceafdc8444dd51a) callback, uint32\_t \* callbackId )

**Description**

Registers the network quality information callback.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

callback

 | 

Callback function, which returns the network quality data.

 |
| 

callbackId

 | 

ID of the callback function, which is allocated by the system and used to deregister the callback.

 |

**Returns**:

**0**: Success.

**201**: Insufficient permission.

**401**: Parameter error.

**801**: System capability not supported.

**62100001**: Internal error.

**62100002**: System service operation failure.

**62100003**: The number of registration requests has reached the upper limit.

**Permission**:

ohos.permission.GET\_NETWORK\_INFO

#### \[h2\]HMS\_NetworkBoost\_RegisterNetSceneCallback()

int32\_t HMS\_NetworkBoost\_RegisterNetSceneCallback ([HMS\_NetworkBoost\_NetSceneChange](#gab00c153ac0c6faf6066cd013ac1d97d4) callback, uint32\_t \* callbackId )

**Description**

Registers the network scenario change callback.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

callback

 | 

Callback function, which returns the network scenario change details.

 |
| 

callbackId

 | 

ID of the callback function, which is allocated by the system and used to deregister the callback.

 |

**Returns**:

**0**: Success.

**201**: Insufficient permission.

**401**: Parameter error.

**801**: System capability not supported.

**62100001**: Internal error.

**62100002**: System service operation failure.

**62100003**: The number of registration requests has reached the upper limit.

**Permission**:

ohos.permission.GET\_NETWORK\_INFO

#### \[h2\]HMS\_NetworkBoost\_ReportQoe()

int32\_t HMS\_NetworkBoost\_ReportQoe ([NetworkBoost\_ServiceType](#ga5b192f3d72de3ac083df4cf36cbc318f) serviceType, [NetworkBoost\_QoeType](#ga539adc59ea2ca1c7498eac3a59bc62be) qoeType )

**Description**

Sends back the app data transmission experience.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

serviceType

 | 

Service type of the app.

 |
| 

qoeType

 | 

Network experience type of the app.

 |

**Returns**:

**0**: Success.

**201**: Insufficient permission.

**401**: Parameter error.

**801**: System capability not supported.

**62100001**: Internal error.

**62100002**: System service operation failure.

**Permission**:

ohos.permission.GET\_NETWORK\_INFO

#### \[h2\]HMS\_NetworkBoost\_SetHandoverMode()

int32\_t HMS\_NetworkBoost\_SetHandoverMode ([NetworkBoost\_HandoverMode](#ga7911fd83a6c8af864d1c87e67d5b0cb1) mode)

**Description**

Changes the network handover mode.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

mode

 | 

Network handover mode.

 |

**Returns**:

**0**: Success.

**201**: Insufficient permission.

**401**: Parameter error.

**801**: System capability not supported.

**62100001**: Internal error.

**62100002**: System service operation failure.

**Permission**:

ohos.permission.GET\_NETWORK\_INFO

#### \[h2\]HMS\_NetworkBoost\_UnregisterHandoverChangeCallback()

int32\_t HMS\_NetworkBoost\_UnregisterHandoverChangeCallback (uint32\_t callbackId)

**Description**

Deregisters the network handover information callback.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

callbackId

 | 

Callback ID, which is allocated by the system when the callback is registered

 |

**Returns**:

**0**: Success.

**201**: Insufficient permission.

**401**: Parameter error.

**801**: System capability not supported.

**62100001**: Internal error.

**62100002**: System service operation failure.

**Permission**:

ohos.permission.GET\_NETWORK\_INFO

#### \[h2\]HMS\_NetworkBoost\_UnregisterNetQosCallback()

int32\_t HMS\_NetworkBoost\_UnregisterNetQosCallback (uint32\_t callbackId)

**Description**

Deregisters the network quality information callback.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

callbackId

 | 

Callback ID, which is allocated by the system when the callback is registered

 |

**Returns**:

**0**: Success.

**201**: Insufficient permission.

**401**: Parameter error.

**801**: System capability not supported.

**62100001**: Internal error.

**62100002**: System service operation failure.

**Permission**:

ohos.permission.GET\_NETWORK\_INFO

#### \[h2\]HMS\_NetworkBoost\_UnregisterNetSceneCallback()

int32\_t HMS\_NetworkBoost\_UnregisterNetSceneCallback (uint32\_t callbackId)

**Description**

Deregisters the network scenario change callback.

**Start version**: 5.1.0(18)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

callbackId

 | 

Callback ID, which is allocated by the system when the callback is registered

 |

**Returns**:

**0**: Success.

**201**: Insufficient permission.

**401**: Parameter error.

**801**: System capability not supported.

**62100001**: Internal error.

**62100002**: System service operation failure.

**Permission**:

ohos.permission.GET\_NETWORK\_INFO

#### \[h2\]HMS\_NetworkBoost\_GetMultiPathQuotaStats()

int32\_t HMS\_NetworkBoost\_GetMultiPathQuotaStats([NetworkBoost\_MultiPathQuota](../../header-files-and-structs/structs/networkboost-multipathquota/document.md)\* quota)

**Description**

Obtains the quota information of multi-network concurrency, including the used and remaining quotas.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

quota

 | 

Quota information obtained for an app.

 |

**Returns**:

**0**: Success.

**201**: Insufficient permission.

**1013600001**: Internal error.

**1013600002**: System processing error. For example, IPC fails or the network management service fails to be started.

**1013600041**: The input parameter is invalid. For example, a null pointer has been passed.

**Permission**:

ohos.permission.LINKTURBO

#### \[h2\]HMS\_NetworkBoost\_RequestMultiPath()

int32\_t HMS\_NetworkBoost\_RequestMultiPath([HMS\_NetworkBoost\_OnMultiPathRequestResult](#section1291820306417) result)

**Description**

Initiates a multi-network concurrency request.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

result

 | 

Result of initiating multi-network concurrency.

 |

**Returns**:

**0**: Success.

**201**: Insufficient permission.

**1013600001**: System processing error. For example, the internal state machine is faulty, or the internal message queue is congested.

**1013600002**: System processing error. For example, IPC fails or the network management service fails to be started.

**1013600041**: The input parameter is invalid. For example, a null pointer has been passed.

**1013620000**: Multi-network concurrency is not enabled.

**1013620001**: Multi-network concurrency has been activated or is being activated.

**1013620002**: Multi-network concurrency requests reached the upper limit.

**1013620003**: Multi-network concurrency cannot be initiated due to power consumption restrictions.

**1013620004**: Quota exhausted.

**1013620005**: A multi-network concurrency scenario conflict occurred.

**1013620006**: Multi-network concurrency is initiated too frequently.

**1013620007**: No path is available for muti-network concurrency.

**1013620008**: Insufficient data traffic quota.

**1013620009**: Multi-network concurrency is not supported.

**Permission**:

ohos.permission.LINKTURBO

#### \[h2\]HMS\_NetworkBoost\_ReleaseMultiPath()

int32\_t HMS\_NetworkBoost\_ReleaseMultiPath()

**Description**

Releases multi-network concurrency.

**Start version**: 6.0.2(22)

**Returns**:

**0**: Success.

**201**: Insufficient permission.

**1013600001**: System processing error. For example, the internal state machine is faulty, or the internal message queue is congested.

**1013600002**: System processing error. For example, IPC fails or the network management service fails to be started.

**1013620100**: Multi-network concurrency is activated by an app different from the one that initiated the release request.

**1013620101**: Multi-network concurrency is not activated.

**Permission**:

ohos.permission.LINKTURBO

#### \[h2\]HMS\_NetworkBoost\_RegisterMultiPathStateChangeCallback()

int32\_t HMS\_NetworkBoost\_RegisterMultiPathStateChangeCallback([HMS\_NetworkBoost\_OnMultiPathStateChange](#section192149121805) callback, uint32\_t\* callbackId)

**Description**

Registers the callback triggered when a multi-network concurrency status change event occurs.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

callback

 | 

Network status change callback.

 |
| 

callbackId

 | 

Callback ID, which is allocated by the system when the callback is registered.

 |

**Returns**:

**0**: Success.

**201**: Insufficient permission.

**1013600001**: System processing error. For example, the internal state machine is faulty, or the internal message queue is congested.

**1013600002**: System processing error. For example, IPC fails or the network management service fails to be started.

**1013600041**: The input parameter is invalid. For example, a null pointer has been passed.

**Permission**:

ohos.permission.LINKTURBO

#### \[h2\]HMS\_NetworkBoost\_UnregisterMultiPathStateChangeCallback()

int32\_t HMS\_NetworkBoost\_UnregisterMultiPathStateChangeCallback(uint32\_t callbackId)

**Description**

Deregisters the callback triggered when a multi-network concurrency status change event occurs.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

callbackId

 | 

Callback ID, which is allocated by the system when the callback is registered.

 |

**Returns**:

**0**: Success.

**201**: Insufficient permission.

**1013600001**: System processing error. For example, the internal state machine is faulty, or the internal message queue is congested.

**1013600002**: System processing error. For example, IPC fails or the network management service fails to be started.

**Permission**:

ohos.permission.LINKTURBO

#### \[h2\]HMS\_NetworkBoost\_RegisterMultiPathRecommendationCallback()

int32\_t HMS\_NetworkBoost\_RegisterMultiPathRecommendationCallback([HMS\_NetworkBoost\_OnMultiPathRecommendation](#section198348561206) callback, uint32\_t\* callbackId)

**Description**

Registers the callback triggered when the multi-network concurrency suggestion provided by the device changes.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

callback

 | 

Callback for multi-network concurrency suggestion changes.

 |
| 

callbackId

 | 

Callback ID, which is allocated by the system when the callback is registered.

 |

**Returns**:

**0**: Success.

**201**: Insufficient permission.

**1013600001**: System processing error. For example, the internal state machine is faulty, or the internal message queue is congested.

**1013600002**: System processing error. For example, IPC fails or the network management service fails to be started.

**1013600041**: The input parameter is invalid. For example, a null pointer has been passed.

**Permission**:

ohos.permission.LINKTURBO

#### \[h2\]HMS\_NetworkBoost\_UnregisterMultiPathRecommendationCallback()

int32\_t HMS\_NetworkBoost\_UnregisterMultiPathRecommendationCallback(uint32\_t callbackId)

**Description**

Deregisters the callback triggered when the multi-network concurrency suggestion provided by the device changes.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

callbackId

 | 

Callback ID, which is allocated by the system when the callback is registered.

 |

**Returns**:

**0**: Success.

**201**: Insufficient permission.

**1013600001**: System processing error. For example, the internal state machine is faulty, or the internal message queue is congested.

**1013600002**: System processing error. For example, IPC fails or the network management service fails to be started.

**Permission**:

ohos.permission.LINKTURBO

#### \[h2\]HMS\_NetworkBoost\_SetSceneDesc()

int32\_t HMS\_NetworkBoost\_SetSceneDesc([NetworkBoost\_SceneDesc](../../header-files-and-structs/structs/networkboost-scenedesc/document.md) sceneDesc)

**Description**

Sets the service scenario.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

sceneDesc

 | 

Description information of a service scenario.

 |

**Returns**:

**0**: Success.

**201**: Insufficient permission.

**1013600001**: System processing error. For example, the internal state machine is faulty, or the internal message queue is congested.

**1013600002**: System processing error. For example, IPC fails or the network management service fails to be started.

**Permission**:

ohos.permission.INTERNET
