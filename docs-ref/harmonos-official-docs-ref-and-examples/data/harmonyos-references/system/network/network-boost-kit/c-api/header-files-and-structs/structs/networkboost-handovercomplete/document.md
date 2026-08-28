# NetworkBoost\_HandoverComplete

#### Overview

Defines the information about the end of network handover.

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

[NetworkBoost\_ErrorResult](../../../modules/networkboost/document.md#ga98419dae6f140b89cac79821f9cbbc9d) [result](#a940df802a9744d5ea6f1c1c4e4460371)

 | 

Network handover result.

 |
| 

bool [handoverContinue](#a0bf437c3ed4b6a4677cc33ede5e98e32)

 | 

Indicates whether to wait for the **HandoverComplete** message. If there are more than two paths, multiple **HandoverComplete** messages may be received.

**true**: There will be more links to be activated and a subsequent **HandoverComplete** message will be sent when multiple target networks exist.

**false**: This is already the last **HandoverComplete** message and the handover process ends.

 |
| 

uint32\_t [oldPathLifetime](#a4b9a08e22f33ca1f09c30f3ca3b01425)

 | 

Remaining lifetime of the old link, in seconds. The value can be any positive integer or 0.

 |
| 

[NetworkBoost\_DataSpeedAction](../networkboost-dataspeedaction/document.md) [oldDataSpeedAction](#ae0dfbb93116a17a8df951ab5ee40b437)

 | 

Packet transmission policy of the link before handover.

 |
| 

bool [pathTypeChanged](#a610d963e22ad2c6151dc5c3f1770a42b)

 | 

Indicates whether the types of the old and new links are different. The value **true** indicates yes (for example, between Wi-Fi and cellular network), and **false** indicates no.

 |
| 

[NetworkBoost\_NetHandle](../networkboost-nethandle/document.md) [newNetHandle](#a9de97d7518d5b5da314053ae4b4df8a3)

 | 

Network handling information of the link after handover.

 |
| 

[NetworkBoost\_ReEstAction](../../../modules/networkboost/document.md#ga99d4ae084f2d5e3744231152e58e51aa) [reEstAction](#a29c0a1d7ce857c5e3bfb5e775344250b)

 | 

Link re-establishment type.

 |
| 

[NetworkBoost\_DataSpeedAction](../networkboost-dataspeedaction/document.md) [newDataSpeedAction](#a5588fe3f833622f5eb81d34cc6fcbe5f)

 | 

Packet transmission policy of the link after handover.

 |

#### Member Variable Description

#### \[h2\]handoverContinue

bool NetworkBoost\_HandoverComplete::handoverContinue

**Description**

Indicates whether to wait for the HandoverComplete message. If there are more than two paths, multiple HandoverComplete messages may be received.

**true**: There will be more links to be activated and a subsequent **HandoverComplete** message will be sent when multiple target networks exist.

**false**: This is already the last **HandoverComplete** message and the handover process ends.

#### \[h2\]newDataSpeedAction

[NetworkBoost\_DataSpeedAction](../networkboost-dataspeedaction/document.md) NetworkBoost\_HandoverComplete::newDataSpeedAction

**Description**

Packet transmission policy of the link after handover.

#### \[h2\]newNetHandle

[NetworkBoost\_NetHandle](../networkboost-nethandle/document.md) NetworkBoost\_HandoverComplete::newNetHandle

**Description**

Network handling information of the link after handover.

#### \[h2\]oldDataSpeedAction

[NetworkBoost\_DataSpeedAction](../networkboost-dataspeedaction/document.md) NetworkBoost\_HandoverComplete::oldDataSpeedAction

**Description**

Packet transmission policy of the link before handover.

#### \[h2\]oldPathLifetime

uint32\_t NetworkBoost\_HandoverComplete::oldPathLifetime

**Description**

Remaining lifetime of the old link, in seconds. The value can be any positive integer or 0.

#### \[h2\]pathTypeChanged

bool NetworkBoost\_HandoverComplete::pathTypeChanged

**Description**

Indicates whether the types of the old and new links are different. The value **true** indicates yes (for example, between Wi-Fi and cellular network), and **false** indicates no.

#### \[h2\]reEstAction

[NetworkBoost\_ReEstAction](../../../modules/networkboost/document.md#ga99d4ae084f2d5e3744231152e58e51aa) NetworkBoost\_HandoverComplete::reEstAction

**Description**

Link re-establishment type.

#### \[h2\]result

[NetworkBoost\_ErrorResult](../../../modules/networkboost/document.md#ga98419dae6f140b89cac79821f9cbbc9d) NetworkBoost\_HandoverComplete::result

**Description**

Defines the network handover result.
