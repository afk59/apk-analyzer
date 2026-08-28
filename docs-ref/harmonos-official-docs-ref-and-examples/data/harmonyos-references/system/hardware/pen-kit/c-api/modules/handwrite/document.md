# HandWrite

#### Overview

Provides the handwriting capability.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 6.0.0(20)

#### Summary

#### \[h2\]Files

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[native\_handwrite\_api.h](../../header-files-and-structs/header-file/native-handwrite-api-h/document.md)

 | 

Declares the handwriting capability.

 |

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [HandWrite\_HistoricalPoint](../../header-files-and-structs/structs/handwrite-historicalpoint/document.md)

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

enum [HandWrite\_ErrCode](#section2871102614149) {

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

int32\_t [HMS\_HandWrite\_GetPredictPoint](#section3513132112183)(const [HandWrite\_HistoricalPoint](../../header-files-and-structs/structs/handwrite-historicalpoint/document.md)\* event,

int32\_t size, float \*predictPointX, float \*predictPointY)

 | 

Obtains the prediction point.

 |

#### Enumeration Type Description

#### \[h2\]HandWrite\_ErrCode

enum HandWrite\_ErrCode

**Description**

Defines handwriting error codes.

**Start version**: 6.0.0(20)

| 
Enumeration

 | 

Description

 |
| :-- | :-- |
| 

E\_NO\_ERROR

 | 

The execution is successful.

 |
| 

E\_PARAMS

 | 

Input parameter is invalid.

 |
| 

E\_INNER\_ERROR

 | 

Internal system error. Related resources fail to be loaded.

 |

#### Function Description

#### \[h2\]HMS\_HandWrite\_GetPredictPoint()

int32\_t [HMS\_HandWrite\_GetPredictPoint](#section3513132112183)(const [HandWrite\_HistoricalPoint](../../header-files-and-structs/structs/handwrite-historicalpoint/document.md)\* event,
    int32\_t size, float \*predictPointX, float \*predictPointY)

**Description**

Obtains the prediction point.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

event

 | 

The input historical point.

 |
| 

size

 | 

Number of historical points.

 |
| 

predictPointX

 | 

X coordinate of the prediction point.

 |
| 

predictPointY

 | 

Y coordinate of the prediction point.

 |

**Return**: HandWrite\_ErrCode:

E\_NO\_ERROR 0 - The execution is successful.

E\_PARAMS 401 - The input parameter is invalid.

E\_INNER\_ERROR 1010400001 - Internal system error. Related resources fail to be loaded.
