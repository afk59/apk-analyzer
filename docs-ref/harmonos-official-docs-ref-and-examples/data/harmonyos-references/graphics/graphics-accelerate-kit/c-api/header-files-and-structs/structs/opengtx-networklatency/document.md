# OpenGTX\_NetworkLatency

#### Overview

Describes the current device network latency information. This struct is passed by a game app after obtaining the network latency information.

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

int32\_t [total](#afea715723d4661c5273bcfe34636cf38)

 | 

Total latency of a game, in ms. The value range is \[0, 200\].

 |
| 

int32\_t [up](#ae67db898729d9184a7502097387d7903)

 | 

Uplink latency of a game, in ms. The value range is \[0, 200\].

 |
| 

int32\_t [down](#a583d7d2a0449ffca70f17e378637cd42)

 | 

Downlink latency of a game, in ms. The value range is \[0, 200\].

 |

#### Member Variable Description

#### \[h2\]down

int32\_t OpenGTX\_NetworkLatency::down

**Description**

Downlink latency of a game, in ms. The value range is \[0, 200\].

#### \[h2\]total

int32\_t OpenGTX\_NetworkLatency::total

**Description**

Total latency of a game, in ms. The value range is \[0, 200\].

#### \[h2\]up

int32\_t OpenGTX\_NetworkLatency::up

**Description**

Uplink latency of a game, in ms. The value range is \[0, 200\].
