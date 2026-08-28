# HandWrite\_HistoricalPoint

#### Overview

Defines the structure of historical touch point information.

**System capability**: SystemCapability.Stylus.HandWrite

**Start version**: 6.0.0(20)

**Related module**: [HandWrite](../../../modules/handwrite/document.md)

**Header file**: [native\_handwrite\_api.h](../../header-file/native-handwrite-api-h/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

float [x](#section20387061661)

 | 

X coordinate of the historical touch point, relative to the left edge of the touched element, in pixels.

 |
| 

float [y](#section72219335715)

 | 

Y coordinate of the historical touch point, relative to the top edge of the touched element, in pixels.

 |
| 

int64\_t [timeStamp](#section12061557279)

 | 

Timestamp of the current historical touch point, in nanoseconds.

 |
| 

float [force](#section3181185590)

 | 

Pressure value of the current historical touch point.

 |

#### Member Variable Description

#### \[h2\]x

float HandWrite\_HistoricalPoint::x

**Description**

X coordinate of the historical touch point, relative to the left edge of the touched element.

#### \[h2\]y

float HandWrite\_HistoricalPoint::y

**Description**

Y coordinate of the historical touch point, relative to the top edge of the touched element.

#### \[h2\]timeStamp

int64\_t HandWrite\_HistoricalPoint::timeStamp

**Description**

Timestamp of the current historical touch point, in nanoseconds.

#### \[h2\]force

float HandWrite\_HistoricalPoint::force

**Description**

Pressure value of the current historical touch point.
