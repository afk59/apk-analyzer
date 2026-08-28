# fast\_solver\_rect\_partition.h

#### Overview

Defines data structures and functions related to the Rectangular Partition Solver.

**File to include**: <FASTKit/fast\_solver\_rect\_partition.h>

**Library**: libfast\_solver.so

**System capability**: SystemCapability.FAST.Core

**Start version**: 6.0.2(22)

**Related module**: [FAST](../../../modules/fast/document.md)

#### Summary

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [FAST\_Rect](../../structs/fast-rect/document.md)

 | 

Defines the data structure of a rectangle. (Coordinate system: The X axis increases from left to right, and the Y axis increases from top to bottom.)

 |

#### \[h2\]Type Definitions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef struct [FAST\_Rect](../../structs/fast-rect/document.md) [FAST\_Rect](../../../modules/fast/document.md#gacb1549fff44eb0707913f3d5f92712b3)

 | 

Defines the data structure of a rectangle.

 |
| 

typedef struct [FAST\_RectPartitionConfig](../../../modules/fast/document.md#gabd3bea5600684d0638b6221f3d0eb23e) [FAST\_RectPartitionConfig](../../../modules/fast/document.md#gabd3bea5600684d0638b6221f3d0eb23e)

 | 

Defines the opaque configuration of the Rectangular Partition Solver.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

FAST\_EXPORT [FAST\_ErrorCode](../../../modules/fast/document.md#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_RectPartition\_CreateConfig](../../../modules/fast/document.md#ga051634633006a8f12665a412dc96687e) ([FAST\_RectPartitionConfig](../../../modules/fast/document.md#gabd3bea5600684d0638b6221f3d0eb23e) \*\*config)

 | 

Creates the opaque configuration of the Rectangular Partition Solver.

 |
| 

FAST\_EXPORT void [HMS\_FAST\_RectPartition\_DestroyConfig](../../../modules/fast/document.md#gae515ef39072676065cef8b9af446f2ac) ([FAST\_RectPartitionConfig](../../../modules/fast/document.md#gabd3bea5600684d0638b6221f3d0eb23e) \*config)

 | 

Destroys the opaque configuration of the Rectangular Partition Solver.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](../../../modules/fast/document.md#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_RectPartition\_SetAlgo](../../../modules/fast/document.md#gaec5519d0974e98f6fe99ab2fa50411cc) ([FAST\_RectPartitionConfig](../../../modules/fast/document.md#gabd3bea5600684d0638b6221f3d0eb23e) \*config, const char \*name)

 | 

Sets the algorithm used by the Rectangular Partition Solver. Currently, only the **SweepLineAlgo** algorithm is supported, which outputs a set of non-overlapping rectangles with a minimized count (not guaranteed to be optimal), operating at ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/zcjEvLXQQHS4yhiOIWzGuw/en-us_formulaimage_0000002500467146.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8AF0806F4DAC0F04855F149C5CD23A755A340E0C8DF3AB6B6E376774FA0FBDC "Click to enlarge") complexity.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](../../../modules/fast/document.md#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_RectPartition\_Solve](../../../modules/fast/document.md#ga9329484302723a20438eadc9e4b71609) ([FAST\_RectPartitionConfig](../../../modules/fast/document.md#gabd3bea5600684d0638b6221f3d0eb23e) \*config, size\_t size, const [FAST\_Rect](../../structs/fast-rect/document.md) \*origin, [FAST\_Rect](../../structs/fast-rect/document.md) \*result, size\_t \*resultSize)

 | 

Solves the rectangular partition problem under the specified opaque configuration. The function takes a set of non-overlapping rectangles as input and computes a rectangular partitioning scheme to generate a minimum number of rectangles that cover the same total area.

**Note**:

1\. The input must ensure that any two rectangles do not overlap (that is, any two rectangles must satisfy: ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/qun8aXSPRlOd1-IHkSlULQ/en-us_formulaimage_0000002492512170.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B83C428AAB48566E34F341F8CA6F591AAB81CCB34206AFACF78F0F0D359B6EF0 "Click to enlarge"), ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/yLfNawVyT0-tU9ALXfOBpw/en-us_formulaimage_0000002492352194.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=74B061CEE57D65A4BC1A4711318D7030F2A1E1877E57F69399B67572F566F2A5 "Click to enlarge"), ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/k_s2o-2PRReACY-IQTq0Vw/en-us_formulaimage_0000002492512172.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3571C775B72BDCF7B29CE848F609678AA3C63D2DC1D1A2BDCBCAD82E2A78E81B "Click to enlarge"), or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/739Z6Xs6TwyzoFzcxJea6A/en-us_formulaimage_0000002492352196.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57F66A4BEE39E41A5A27701D73DCF473471D10F4BD1901B400DA862301A2F5B7 "Click to enlarge")). Otherwise, the function returns **FAST\_ERROR\_CODE\_ILLEGAL\_INPUT**.

2\. The function ensures that the number of output rectangles is less than or equal to the number of input rectangles.

 |
