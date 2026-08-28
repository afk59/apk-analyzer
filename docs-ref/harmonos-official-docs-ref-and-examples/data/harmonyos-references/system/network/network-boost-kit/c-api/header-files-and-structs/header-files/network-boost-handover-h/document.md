# network\_boost\_handover.h

#### Overview

Declares APIs for network handover, and defines basic functions, structs, and constants.

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

struct [NetworkBoost\_DataSpeedAction](../../structs/networkboost-dataspeedaction/document.md)

 | 

Defines the enumeration of the packet transmission policy.

 |
| 

struct [NetworkBoost\_NetHandle](../../structs/networkboost-nethandle/document.md)

 | 

Defines the handle of the data network.

 |
| 

struct [NetworkBoost\_HandoverStart](../../structs/networkboost-handoverstart/document.md)

 | 

Defines the information about the start of network handover.

 |
| 

struct [NetworkBoost\_HandoverComplete](../../structs/networkboost-handovercomplete/document.md)

 | 

Defines the information about the end of network handover.

 |
| 

struct [HMS\_NetworkBoost\_HandoverCallback](../../structs/hms-networkboost-handovercallback/document.md)

 | 

Callback function, which returns the details about the start and end of a network handover.

 |
| 

struct [NetworkBoost\_MultiPathQuotaInfo](../../structs/networkboost-multipathquotainfo/document.md)

 | 

Defines multi-network concurrency quota information.

 |
| 

struct [NetworkBoost\_MultiPathQuota](../../structs/networkboost-multipathquota/document.md)

 | 

Defines the quota usage information for multi-network concurrency.

 |
| 

struct [NetworkBoost\_MultiPathRequestResult](../../structs/networkboost-multipathrequestresult/document.md)

 | 

Defines the multi-network concurrency request result.

 |
| 

struct [NetworkBoost\_MultiPathStateChange](../../structs/networkboost-multipathstatechange/document.md)

 | 

Defines multi-network concurrency status information.

 |
| 

struct [NetworkBoost\_MultiPathRecommendation](../../structs/networkboost-multipathrecommendation/document.md)

 | 

Defines multi-network concurrency suggestion information.

 |

#### \[h2\]Types

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef enum [NetworkBoost\_DataSpeedSimpleAction](../../../modules/networkboost/document.md#gae2c308911ff3569b20102600d64d460a) [NetworkBoost\_DataSpeedSimpleAction](../../../modules/networkboost/document.md#gac06c759288ec3617480002297aa11dab)

 | 

Defines the enumeration of the simple suggested packet transmission policy.

 |
| 

typedef enum [NetworkBoost\_ErrorResult](../../../modules/networkboost/document.md#ga98419dae6f140b89cac79821f9cbbc9d) [NetworkBoost\_ErrorResult](../../../modules/networkboost/document.md#ga6946f85cae25ae0ebfd5bbee9579cd08)

 | 

Defines the enumeration of the network handover result.

 |
| 

typedef enum [NetworkBoost\_ReEstAction](../../../modules/networkboost/document.md#ga99d4ae084f2d5e3744231152e58e51aa) [NetworkBoost\_ReEstAction](../../../modules/networkboost/document.md#gab5ab8d4dfd6770df9ddf344440fe39c9)

 | 

Defines the enumeration of the link re-establishment type.

 |
| 

typedef struct [NetworkBoost\_DataSpeedAction](../../structs/networkboost-dataspeedaction/document.md) [NetworkBoost\_DataSpeedAction](../../../modules/networkboost/document.md#ga98032d55873b9c438e4fe7a4393b6ebb)

 | 

Defines the recommended packet transmission rate.

 |
| 

typedef struct [NetworkBoost\_NetHandle](../../structs/networkboost-nethandle/document.md) [NetworkBoost\_NetHandle](../../../modules/networkboost/document.md#ga83a1277967e95e2965b6f8dbee5945cc)

 | 

Defines the handle of the data network.

 |
| 

typedef struct [NetworkBoost\_HandoverStart](../../structs/networkboost-handoverstart/document.md) [NetworkBoost\_HandoverStart](../../../modules/networkboost/document.md#gae5e48d9919724eba0c72d4e320122ca6)

 | 

Defines the information about the start of network handover.

 |
| 

typedef struct [NetworkBoost\_HandoverComplete](../../structs/networkboost-handovercomplete/document.md) [NetworkBoost\_HandoverComplete](../../../modules/networkboost/document.md#ga9490335b78db33fe8effe0674036146f)

 | 

Defines the information about the end of network handover.

 |
| 

typedef enum [NetworkBoost\_HandoverMode](../../../modules/networkboost/document.md#ga7911fd83a6c8af864d1c87e67d5b0cb1) [NetworkBoost\_HandoverMode](../../../modules/networkboost/document.md#gaf4d63e47ed8a29ad3bd4104669d80755)

 | 

Defines the enumeration of the network handover mode.

 |
| 

typedef void(\* [HMS\_NetworkBoost\_OnHandoverStart](../../../modules/networkboost/document.md#gaeb846c7c42199e314b95770657ed583d)) ([NetworkBoost\_HandoverStart](../../structs/networkboost-handoverstart/document.md) \*handoverStart)

 | 

Defines the callback prototype triggered when the network handover starts.

 |
| 

typedef void(\* [HMS\_NetworkBoost\_OnHandoverComplete](../../../modules/networkboost/document.md#ga799fbecb09ede04fec174737425082f6)) ([NetworkBoost\_HandoverComplete](../../structs/networkboost-handovercomplete/document.md) \*handoverComplete)

 | 

Defines the callback prototype triggered when the network handover ends.

 |
| 

typedef struct [HMS\_NetworkBoost\_HandoverCallback](../../structs/hms-networkboost-handovercallback/document.md) [HMS\_NetworkBoost\_HandoverCallback](../../../modules/networkboost/document.md#ga8ce6f265f4275452f332441338e3035c)

 | 

Callback function, which returns the details about the start and end of a network handover.

 |
| 

typedef void ([HMS\_NetworkBoost\_OnMultiPathRequestResult](../../../modules/networkboost/document.md#section1291820306417))([NetworkBoost\_MultiPathRequestResult](../../structs/networkboost-multipathrequestresult/document.md)\* result)

 | 

Defines the callback prototype for multi-network concurrency request results.

 |
| 

typedef void ([HMS\_NetworkBoost\_OnMultiPathStateChange](../../../modules/networkboost/document.md#section192149121805))([NetworkBoost\_MultiPathStateChange](../../structs/networkboost-multipathstatechange/document.md)\* multiPathState)

 | 

Defines the callback prototype for multi-network concurrency status changes.

 |
| 

typedef void ([HMS\_NetworkBoost\_OnMultiPathRecommendation](../../../modules/networkboost/document.md#section198348561206))([NetworkBoost\_MultiPathRecommendation](../../structs/networkboost-multipathrecommendation/document.md)\* recommendation)

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

[NetworkBoost\_DataSpeedSimpleAction](../../../modules/networkboost/document.md#gae2c308911ff3569b20102600d64d460a) { NB\_SIMPLEACTION\_SUSPEND\_DATA = 1, NB\_SIMPLEACTION\_DECREASE\_DATA = 2, NB\_SIMPLEACTION\_INCREASE\_DATA = 3, NB\_SIMPLEACTION\_KEEP\_DATA = 4 }

 | 

Defines the enumeration of the simple suggested packet transmission policy.

 |
| 

[NetworkBoost\_ErrorResult](../../../modules/networkboost/document.md#ga98419dae6f140b89cac79821f9cbbc9d) { NB\_ERROR\_NONE = 0, NB\_ERROR\_HANDOVER\_TIMEOUT = 1, NB\_ERROR\_NEW\_PATH\_ACTIVATION\_FAILED = 2, NB\_ERROR\_ABORT = 3 }

 | 

Defines the enumeration of the network handover result.

 |
| 

[NetworkBoost\_ReEstAction](../../../modules/networkboost/document.md#ga99d4ae084f2d5e3744231152e58e51aa) {

NB\_REEST\_DEFAULT = 0, NB\_REEST\_QUERY\_DNS = 1, NB\_REEST\_CHANGE\_REMOTE\_IP = 2, NB\_REEST\_CHANGE\_IP\_VERSION = 3,

NB\_NO\_EST = 4

}

 | 

Defines the enumeration of the link re-establishment type.

 |
| 

[NetworkBoost\_HandoverMode](../../../modules/networkboost/document.md#ga7911fd83a6c8af864d1c87e67d5b0cb1) { NB\_MODE\_DELEGATION = 0, NB\_MODE\_DISCRETION = 1 }

 | 

Defines the enumeration of the network handover mode.

 |
| 

[NetworkBoost\_PathState](../../../modules/networkboost/document.md#section1774664693518){

NB\_PATH\_IDLE = 0, NB\_PATH\_CONNECTED = 1, NB\_PATH\_SUSPENDED = 2

}

 | 

Defines the enumeration for the status of a data path other than the default path in multi-network concurrency.

 |
| 

[NetworkBoost\_MultiPathErrorResult](../../../modules/networkboost/document.md#section129101047154112){

NB\_MULTIPATH\_ERROR\_NONE = 0, NB\_MULTIPATH\_ERROR\_NETWORK\_REFUSED = 1, NB\_MULTIPATH\_ERROR\_TIMEOUT = 2, NB\_MULTIPATH\_ERROR\_LOCAL = 3

}

 | 

Defines the enumeration of the multi-network concurrency initiation result.

 |
| 

[NetworkBoost\_MultiPathChangeCause](../../../modules/networkboost/document.md#section19927184203916){

NB\_MULTIPATH\_CAUSE\_REQUEST\_NORMAL = 0, NB\_MULTIPATH\_CAUSE\_RELEASE\_NORMAL = 50, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_NETWORK = 51, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_USER\_REFUSED = 52, NB\_MULTIPATH\_CAUSE\_RELEASE\_NO\_QUOTA = 53, NB\_MULTIPATH\_CAUSE\_RELEASE\_POWER\_CONSUMPTION = 54, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_INSUFFICIENT\_TRAFFIC = 55, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_CONFLICT = 56, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_FUSING = 57, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_DEFAULT = 99, NB\_MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_ENTER = 100, NB\_MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_LEAVE = 101, NB\_MULTIPATH\_CHANGE\_CAUSE\_CONN\_PROPERTIES\_UPDATE = 102

}

 | 

Defines the enumeration of the reasons why multi-network concurrency status changes.

 |
| 

[NetworkBoost\_MultiPathState](../../../modules/networkboost/document.md#section12626124820456){

NB\_MULTIPATH\_IDLE = 0, NB\_MULTIPATH\_CREATEING = 1, NB\_MULTIPATH\_CREATED = 2, NB\_MULTIPATH\_RELEASING = 3

}

 | 

Defines the enumeration for the status of multi-network concurrency.

 |
| 

[NetworkBoost\_MultiPathAction](../../../modules/networkboost/document.md#section12185112974610){

NB\_MULTIPATH\_ACTION\_REQUEST = 0, NB\_MULTIPATH\_ACTION\_RELEASE = 1

}

 | 

Defines the enumeration of suggested multi-network concurrency actions.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

int32\_t [HMS\_NetworkBoost\_RegisterHandoverChangeCallback](../../../modules/networkboost/document.md#gac3d95b4bf5c8cbec5ca862130d441fce) ([HMS\_NetworkBoost\_HandoverCallback](../../structs/hms-networkboost-handovercallback/document.md) \*callback, uint32\_t \*callbackId)

 | 

Registers the network handover callback.

 |
| 

int32\_t [HMS\_NetworkBoost\_UnregisterHandoverChangeCallback](../../../modules/networkboost/document.md#gaca0ae3e209bc314e808d808786d76eae) (uint32\_t callbackId)

 | 

Deregisters the network handover callback.

 |
| 

int32\_t [HMS\_NetworkBoost\_SetHandoverMode](../../../modules/networkboost/document.md#ga1f03a8af2bbf9de6af215df385498a7a) ([NetworkBoost\_HandoverMode](../../../modules/networkboost/document.md#ga7911fd83a6c8af864d1c87e67d5b0cb1) mode)

 | 

Defines the network handover mode. Your app can call the relevant API to change the network handover mode between delegation mode and proactive mode. The default mode is delegation. If the setting fails, the API will throw an exception.

 |
| 

int32\_t [HMS\_NetworkBoost\_GetMultiPathQuotaStats](../../../modules/networkboost/document.md#section3899010125311)([NetworkBoost\_MultiPathQuota](../../structs/networkboost-multipathquota/document.md) \*quota)

 | 

Obtains the quota information of multi-network concurrency, including the used and remaining quotas.

 |
| 

int32\_t [HMS\_NetworkBoost\_RequestMultiPath](../../../modules/networkboost/document.md#section13240250195914)([HMS\_NetworkBoost\_OnMultiPathRequestResult](../../structs/networkboost-multipathrequestresult/document.md) result, uint32\_t \*requestId)

 | 

Initiates a multi-network concurrency request.

 |
| 

int32\_t [HMS\_NetworkBoost\_ReleaseMultiPath](../../../modules/networkboost/document.md#section58537189614)(uint32\_t requestId)

 | 

Releases multi-network concurrency.

 |
| 

int32\_t [HMS\_NetworkBoost\_RegisterMultiPathStateChangeCallback](../../../modules/networkboost/document.md#section421172813919)([HMS\_NetworkBoost\_OnMultiPathStateChange](../../../modules/networkboost/document.md#section192149121805)callback, uint32\_t \*callbackId)

 | 

Registers the callback triggered when a multi-network concurrency status change event occurs.

 |
| 

int32\_t [HMS\_NetworkBoost\_UnregisterMultiPathStateChangeCallback](../../../modules/networkboost/document.md#section52786305915)(uint32\_t callbackId)

 | 

Deregisters the callback triggered when a multi-network concurrency status change event occurs.

 |
| 

int32\_t [HMS\_NetworkBoost\_RegisterMultiPathRecommendationCallback](../../../modules/networkboost/document.md#section463012484123)([HMS\_NetworkBoost\_OnMultiPathRecommendation](../../../modules/networkboost/document.md#section198348561206)callback, uint32\_t \*callbackId)

 | 

Registers the callback triggered when the multi-network concurrency suggestion provided by the device changes.

 |
| 

int32\_t [HMS\_NetworkBoost\_UnregisterMultiPathRecommendationCallback](../../../modules/networkboost/document.md#section18632948201214)(uint32\_t callbackId)

 | 

Deregisters the callback triggered when the multi-network concurrency suggestion provided by the device changes.

 |
