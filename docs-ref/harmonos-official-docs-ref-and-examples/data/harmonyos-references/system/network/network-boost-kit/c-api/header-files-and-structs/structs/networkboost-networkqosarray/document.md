# NetworkBoost\_NetworkQosArray

#### Overview

Defines network quality change details.

**Start version**: 5.1.0(18)

**Related module**: [NetworkBoost](../../../modules/networkboost/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Variable

 | 

Description

 |
| :-- | :-- |
| 

uint32\_t [pathNum](#a7881dde170513e4e1eb2f6030d224837)

 | 

Number of paths in network quality information. The value range is \[1, 4\].

 |
| 

[NetworkBoost\_NetworkQos](../networkboost-networkqos/document.md) [networkQos](#a85ba381b3f959459d2a832ab2b5e13ff) \[[NETBOOST\_MAX\_PATH\_NUM](../../../modules/networkboost/document.md#ga7668e89aac2dea1d584a9ccacea33614)\]

 | 

Network quality information of multiple paths. Each record indicates the network quality information of a specific path. The value range is \[0, pathNum-1\].

 |

#### Member Variable Description

#### \[h2\]networkQos

[NetworkBoost\_NetworkQos](../networkboost-networkqos/document.md) NetworkBoost\_NetworkQosArray::networkQos\[[NETBOOST\_MAX\_PATH\_NUM](../../../modules/networkboost/document.md#ga7668e89aac2dea1d584a9ccacea33614)\]

**Description**

Network quality information of multiple paths. Each record indicates the network quality information of a specific path. The value range is \[0, pathNum-1\].

#### \[h2\]pathNum

uint32\_t NetworkBoost\_NetworkQosArray::pathNum

**Description**

Number of paths in network quality information. The value range is \[1, 4\].
