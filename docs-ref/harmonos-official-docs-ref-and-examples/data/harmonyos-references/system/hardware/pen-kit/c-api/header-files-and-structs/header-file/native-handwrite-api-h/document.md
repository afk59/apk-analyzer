# native\_handwrite\_api.h

#### Overview

Declares the handwriting capability.

**Library:** libhandwrite\_ndk.z.so

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 6.0.0(20)

**Related module**: [HandWrite](../../../modules/handwrite/document.md)

#### Summary

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [HandWrite\_HistoricalPoint](../../structs/handwrite-historicalpoint/document.md)

 | 

Defines the structure of historical touch point information.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

enum [HandWrite\_ErrCode](../../../modules/handwrite/document.md#section2871102614149) {

E\_NO\_ERROR = 0,

E\_PARAMS = 401,

E\_INNER\_ERROR = 1010400001

}

 | 

Defines handwriting error codes.

 |

#### \[h2\]Functions

| 
Name

 | 

Function

 |
| :-- | :-- |
| 

int32\_t [HMS\_HandWrite\_GetPredictPoint](../../../modules/handwrite/document.md#section3513132112183)(const [HandWrite\_HistoricalPoint](../../structs/handwrite-historicalpoint/document.md) \*event, int32\_t size, float \*predictPointX, float \*predictPointY)

 | 

Obtains the prediction point.

 |
