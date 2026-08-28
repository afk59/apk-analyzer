# OpenGTX\_NetworkInfo

#### Overview

Describes the current device network information. This struct is passed by a game app after obtaining the network information.

**Start version**: 5.0.0(12)

**Related module**: [GraphicsAccelerate](../../../modules/graphicsaccelerate/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[OpenGTX\_NetworkLatency](../opengtx-networklatency/document.md) [networkLatency](#a7630cf3cc694ba3d8ce1c7565d3c8860)

 | 

Network latency in a game. If there is no uplink or downlink latency, set this variable to the value of **total** (total latency). The total game latency is divided into five levels: 0 ms, 50 ms, 100 ms, 150 ms, and 200 ms. When the level changes, the game app notifies OpenGTX of the change.

 |
| 

char\* [networkServerIP](#a8a901843481e827a3799eb116744cf35)

 | 

Game server IP address. The value is a string of 1 to 256 characters.

 |

#### Member Variable Description

#### \[h2\]networkLatency

[OpenGTX\_NetworkLatency](../opengtx-networklatency/document.md) OpenGTX\_NetworkInfo::networkLatency

**Description**

Network latency in a game. If there is no uplink or downlink latency, set this variable to the value of **total** (total latency). The total game latency is divided into five levels: 0 ms, 50 ms, 100 ms, 150 ms, and 200 ms. When the level changes, the game app notifies OpenGTX of the change.

#### \[h2\]networkServerIP

char\* OpenGTX\_NetworkInfo::networkServerIP

**Description**

Game server IP address. The value is a string of 1 to 256 characters.
