# AREngine\_ARSemanticDensePointData

#### Overview

Dense point cloud data of a high-precision geometric reconstruction object.

This struct is used as the input to the [HMS\_AREngine\_ARSemanticDense\_AcquirePointData](../../../modules/ar-engine/document.md#section288942515910) API.

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

ID of the current point.

 |
| 

float [x](#a60bbc989bbfdd3ea9f45d9eafe7e8e35)

 | 

X coordinate of the current point.

 |
| 

float [y](#section3737714246)

 | 

Y coordinate of the current point.

 |
| 

float [z](#section1948521711242)

 | 

Z coordinate of the current point.

 |
| 

int32\_t [r](#section168088181247)

 | 

R component of the current point's color (in RGBA format).

 |
| 

int32\_t [g](#section13605141942412)

 | 

G component of the current point's color (in RGBA format).

 |
| 

int32\_t [b](#section173378203245)

 | 

B component of the current point's color (in RGBA format).

 |
| 

int32\_t [a](#section216215292248)

 | 

A component of the current point's color (in RGBA format).

 |
| 

float [confidence](#section139458299242)

 | 

Confidence of the current point.

 |

#### Struct Member Variable Description

#### \[h2\]id

int32\_t AREngine\_ARSemanticDensePointData::id

**Description**

ID of the current point.

#### \[h2\]x

float AREngine\_ARSemanticDensePointData::x

**Description**

X coordinate of the current point.

#### \[h2\]y

float AREngine\_ARSemanticDensePointData::y

**Description**

Y coordinate of the current point.

#### \[h2\]z

float AREngine\_ARSemanticDensePointData::z

**Description**

Z coordinate of the current point.

#### \[h2\]r

int32\_t AREngine\_ARSemanticDensePointData::r

**Description**

R component of the current point's color (in RGBA format).

#### \[h2\]g

int32\_t AREngine\_ARSemanticDensePointData::g

**Description**

G component of the current point's color (in RGBA format).

#### \[h2\]b

int32\_t AREngine\_ARSemanticDensePointData::b

**Description**

B component of the current point's color (in RGBA format).

#### \[h2\]a

int32\_t AREngine\_ARSemanticDensePointData::a

**Description**

A component of the current point's color (in RGBA format).

#### \[h2\]confidence

float AREngine\_ARSemanticDensePointData::confidence

**Description**

Confidence of the current point.
