# NetworkBoost\_HandoverStart

#### Overview

Defines the information about the start of network handover.

**Start version**: 5.1.0(18)

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

uint32\_t [expires](#a405fb82f10e067f1dacd91e1eac02725)

 | 

Timeout interval of the entire network handover process, in seconds. The value can be any positive integer or 0.

 |
| 

[NetworkBoost\_DataSpeedAction](../networkboost-dataspeedaction/document.md) [dataSpeedAction](#a9ef2e94bd85d1dbe00f1a0021c4fc7b5)

 | 

Packet transmission policy of the link before handover.

 |

#### Member Variable Description

#### \[h2\]dataSpeedAction

[NetworkBoost\_DataSpeedAction](../networkboost-dataspeedaction/document.md) NetworkBoost\_HandoverStart::dataSpeedAction

**Description**

Packet transmission policy of the link before handover.

#### \[h2\]expires

uint32\_t NetworkBoost\_HandoverStart::expires

**Description**

Timeout interval of the entire network handover process, in seconds. The value can be any positive integer or 0.
