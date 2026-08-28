# OpenGTX\_GameSceneInfo

#### Overview

Describes the game scene information. This struct is passed by a game app after obtaining the scene information.

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

[OpenGTX\_SceneID](../../../modules/graphicsaccelerate/document.md#gad7e5d2d235183dc0c6549331d6bc2932) [sceneID](#aebbf4e9b7189fe91c035c5f883c0aa17)

 | 

Game scene type.

 |
| 

char\* [description](#ad16ededcd444a4183f46987c55a98ff4)

 | 

Game scene description. The value is a string of 0 to 256 characters.

 |
| 

int32\_t [recommendFPS](#a1187bcfe8f07e6e974a2c7690c78af65)

 | 

Recommended frame rate for the current scene. The value range is 0 and \[30, [targetFPS](../opengtx-configdescription/document.md#a97b1fac259c0724de14f964712c85cae)\]. If this variable is set to **0**, the value does not take effect.

 |
| 

int32\_t [minFPS](#a9d6a81921f08d4a6e6e8e122f5c8ace7)

 | 

Expected minimum frame rate for the current scene. The value range is 0 and \[30, [targetFPS](../opengtx-configdescription/document.md#a97b1fac259c0724de14f964712c85cae)\]. If this variable is set to **0**, the value does not take effect.

 |
| 

int32\_t [maxFPS](#a854d149c4c4e0b6953800592f96b312b)

 | 

Expected maximum frame rate for the current scene. The value range is 0 and \[30, [targetFPS](../opengtx-configdescription/document.md#a97b1fac259c0724de14f964712c85cae)\]. If this variable is set to **0**, the value does not take effect.

 |
| 

[OpenGTX\_ResolutionValue](../opengtx-resolutionvalue/document.md) [resolutionCurValue](#ad91afb9f2d7a372969002871e184a4ca)

 | 

Resolution of the current scene. The value ranges from 360p to 8K.

 |

#### Member Variable Description

#### \[h2\]description

char\* OpenGTX\_GameSceneInfo::description

**Description**

Game scene description. The value is a string of 0 to 256 characters.

#### \[h2\]maxFPS

int32\_t OpenGTX\_GameSceneInfo::maxFPS

**Description**

Expected maximum frame rate for the current scene. The value range is 0 and \[30, [targetFPS](../opengtx-configdescription/document.md#a97b1fac259c0724de14f964712c85cae)\]. If this variable is set to **0**, the value does not take effect.

#### \[h2\]minFPS

int32\_t OpenGTX\_GameSceneInfo::minFPS

**Description**

Expected minimum frame rate for the current scene. The value range is 0 and \[30, [targetFPS](../opengtx-configdescription/document.md#a97b1fac259c0724de14f964712c85cae)\]. If this variable is set to **0**, the value does not take effect.

#### \[h2\]recommendFPS

int32\_t OpenGTX\_GameSceneInfo::recommendFPS

**Description**

Recommended frame rate for the current scene. The value range is 0 and \[30, [targetFPS](../opengtx-configdescription/document.md#a97b1fac259c0724de14f964712c85cae)\]. If this variable is set to **0**, the value does not take effect.

#### \[h2\]resolutionCurValue

[OpenGTX\_ResolutionValue](../opengtx-resolutionvalue/document.md) OpenGTX\_GameSceneInfo::resolutionCurValue

**Description**

Resolution of the current scene. The value ranges from 360p to 8K.

#### \[h2\]sceneID

[OpenGTX\_SceneID](../../../modules/graphicsaccelerate/document.md#gad7e5d2d235183dc0c6549331d6bc2932) OpenGTX\_GameSceneInfo::sceneID

**Description**

Game scene type.
