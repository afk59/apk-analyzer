# NetworkBoost\_MultiPathStateChange

#### Overview

Defines multi-network concurrency status information, which is used to notify about multi-network concurrency status changes after the multi-network concurrency status change event callback is registered.

**Start version**: 6.0.2(22)

**Related module**: [NetworkBoost](../../../modules/networkboost/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[NetworkBoost\_MultiPathState](../../../modules/networkboost/document.md#section12626124820456) [multiPathState](#section159871228122717)

 | 

Multi-network concurrency status.

 |
| 

[NetworkBoost\_MultiPathChangeCause](../../../modules/networkboost/document.md#section19927184203916) [changeCause](#section2054235172714)

 | 

Reason for a multi-network concurrency status change.

 |
| 

[NetworkBoost\_NetHandle](../../../modules/networkboost/document.md#ga83a1277967e95e2965b6f8dbee5945cc) [netHandle](#section18578175863714)

 | 

Network handle of the multi-network concurrency.

 |
| 

[NetworkBoost\_PathState](../../../modules/networkboost/document.md#section1774664693518) [pathState](#section135790582373)

 | 

Status of the data path other than the default path in multi-network concurrency.

 |
| 

[NetworkBoost\_PathType](../../../modules/networkboost/document.md#ga45748b2a298346cbea2f1cbe573ffe72) [pathType](#section1487115310381)

 | 

Type of the data path other than the default path in multi-network concurrency.

 |

#### Member Variable Description

#### multiPathState

NetworkBoost\_MultiPathState NetworkBoost\_MultiPathStateChange::multiPathState

**Description**

Multi-network concurrency status, including idle, establishing, established, and releasing.

#### changeCause

NetworkBoost\_MultiPathChangeCause NetworkBoost\_MultiPathStateChange::changeCause

**Description**

Reason for the multi-network concurrency status change, which is obtained when a status change occurs.

#### netHandle

NetworkBoost\_NetHandle NetworkBoost\_MultiPathStateChange::netHandle

**Description**

Network handle of the multi-network concurrency.

#### pathState

NetworkBoost\_PathState NetworkBoost\_MultiPathStateChange::pathState

**Description**

Status of the data path other than the default path in multi-network concurrency.

#### pathType

NetworkBoost\_PathType NetworkBoost\_MultiPathStateChange::pathType

**Description**

Type of the data path other than the default path in multi-network concurrency.
