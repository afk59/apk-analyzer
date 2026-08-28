# AREngine\_ARSemanticDenseCubeData

#### Overview

Cube data of a high-precision geometric reconstruction object.

This struct is used as the input to the [HMS\_AREngine\_ARSemanticDense\_AcquireCubeData](../../../modules/ar-engine/document.md#section7554459949) API.

**Start version**: 6.0.0(20)

**Related module**: [AR Engine](../../../modules/ar-engine/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

int32\_t [id](#a8fd160424c15bc17d2860f26b1f67d3f)

 | 

ID of the current cube.

 |
| 

int32\_t [vertexSize](#a60bbc989bbfdd3ea9f45d9eafe7e8e35)

 | 

Vertex size of the current cube.

 |
| 

float\* [vertexData](#section3737714246)

 | 

Vertex data of the current cube.

The data includes all eight vertices, which are indexed from the rear face in a counterclockwise order.

 |
| 

float [confidence](#section139458299242)

 | 

Confidence of the current cube.

 |
| 

AREngine\_ARSemanticPlaneLabel [label](#section86565446916)

 | 

Semantic label of the current cube.

For details, please refer to [AREngine\_ARSemanticPlaneLabel](../../../modules/ar-engine/document.md#gafbb6b69fefdc417ba6437ce2fe587cb1).

 |

#### Struct Member Variable Description

#### \[h2\]id

int32\_t AREngine\_ARSemanticDenseCubeData::id

**Description**

ID of the current cube.

#### \[h2\]vertexSize

int32\_t AREngine\_ARSemanticDenseCubeData::vertexSize

**Description**

Vertex size of the current cube.

#### \[h2\]vertexData

float\* AREngine\_ARSemanticDenseCubeData::vertexData

**Description**

Vertex data of the current cube.

#### \[h2\]confidence

float AREngine\_ARSemanticDenseCubeData::confidence

**Description**

Confidence of the current cube.

#### \[h2\]label

AREngine\_ARSemanticPlaneLabel AREngine\_ARSemanticDenseCubeData::label

**Description**

Semantic label of the current cube.
