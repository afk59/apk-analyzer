# NetworkBoost\_SceneDesc

#### Overview

Defines the description information of a service scenario.

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

[NetworkBoost\_ServiceType](../../../modules/networkboost/document.md#gaabe242932bb115198d2f27c0deedb0f5) [scene](#section159871228122717)

 | 

Service scenario type.

 |
| 

[NetworkBoost\_SceneEvent](../../../modules/networkboost/document.md#section9626183119507) [sceneEvent](#section2054235172714)

 | 

Service scenario event.

 |
| 

uint32\_t [startTime](#section1047652018448)

 | 

Predicted duration before the **sceneEvent** is triggered, in seconds.

-   **0**: The **sceneEvent** event occurs immediately. The default value is **0**.
-   Value greater than 0: Predicted duration before the **sceneEvent** is triggered.

 |
| 

uint32\_t [duration](#section1047620200441)

 | 

Predicted duration of the service scenario, in seconds. The value **0** indicates an unknown duration, which ends when the **SceneEvent** ends. You can set this variable based on the actual service scenario.

Example of a service scenario: A seckill promotion of an app begins in 10 seconds, which will last for 20 seconds. In this case, you can pass **seckillService** for **scene**, and set **sceneEvent** to **SCENE\_EVENT\_ENTER**, **startTime** to **10**, and **duration** to **20**.

 |

#### Member Variable Description

#### scene

NetworkBoost\_ServiceType NetworkBoost\_SceneDesc::scene

**Description**

Service scenario type.

#### sceneEvent

NetworkBoost\_SceneEvent NetworkBoost\_SceneDesc::sceneEvent

**Description**

Service scenario event.

#### startTime

uint32\_t NetworkBoost\_SceneDesc::startTime

**Description**

Predicted duration before the **sceneEvent** is triggered, in seconds.

#### duration

uint32\_t NetworkBoost\_SceneDesc::duration

**Description**

Predicted duration of the service scenario, in seconds.
