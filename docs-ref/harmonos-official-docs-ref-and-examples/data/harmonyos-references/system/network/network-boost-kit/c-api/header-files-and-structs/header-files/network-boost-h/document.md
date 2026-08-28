# network\_boost.h

#### Overview

Declares APIs for network acceleration, and defines basic functions, structs, and constants.

**Library**: libnetwork\_boost.so

**System capability**: SystemCapability.Communication.NetworkBoost.Core

**Start version**: 6.0.2(22)

**Related module**: [NetworkBoost](../../../modules/networkboost/document.md)

#### Summary

#### Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [NetworkBoost\_SceneDesc](../../structs/networkboost-scenedesc/document.md)

 | 

Defines the description information of a service scenario.

 |

#### Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [NetworkBoost\_SceneEvent](../../../modules/networkboost/document.md#section9626183119507){

SCENE\_EVENT\_ENTER = 0, SCENE\_EVENT\_UPDATE = 1, SCENE\_EVENT\_LEAVE = 2

}

 | 

Defines the enumeration of service scenario events.

 |

#### Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

int32\_t [HMS\_NetworkBoost\_SetSceneDesc](../../../modules/networkboost/document.md#section1441013415156)([NetworkBoost\_SceneDesc](../../structs/networkboost-scenedesc/document.md) sceneDesc)

 | 

Sets the service scenario.

 |
