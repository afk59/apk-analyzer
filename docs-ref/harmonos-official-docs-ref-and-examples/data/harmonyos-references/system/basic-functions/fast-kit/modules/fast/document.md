# FAST

#### Overview

Fast Algorithms Supported by Theory (FAST) Kit provides algorithm acceleration APIs to optimize metrics such as app startup time, loading speed, and response latency.

**Start version**: 6.0.2(22)

#### Summary

This section describes the files, structs, macro definitions, type definitions, enumerations, and functions of FAST Kit.

#### \[h2\]Files

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[fast\_ads\_segment\_map.h](../../header-files-and-structs/header-files/fast-ads-segment-map-h/document.md)

 | 

Defines data structures and functions related to a Segment Map.

 |
| 

[fast\_common\_def.h](../../header-files-and-structs/header-files/fast-common-def-h/document.md)

 | 

Defines common types in FAST Kit, such as error code.

 |
| 

[fast\_solver\_rect\_partition.h](../../header-files-and-structs/header-files/fast-solver-rect-partition-h/document.md)

 | 

Defines data structures and functions related to the Rectangular Partition Solver.

 |

#### \[h2\]Structs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [FAST\_Rect](../../header-files-and-structs/structs/fast-rect/document.md)

 | 

Defines the data structure of a rectangle.

 |

#### \[h2\]Type Definitions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef enum [FAST\_SegmentMapQueryType](#ga8ef2e816f027493a63bd4e82876f233f) [FAST\_SegmentMapQueryType](#ga7be8db1fe5677bb8732d73ff6d09b6f8)

 | 

Defines the query types supported by a Segment Map.

 |
| 

typedef enum [FAST\_SegmentMapUpdateType](#ga2747e3df771507eaeff23cc28f17fc76) [FAST\_SegmentMapUpdateType](#ga88bbda3d57a45b5bd34a2892013a694f)

 | 

Defines the update types supported by a Segment Map.

 |
| 

typedef struct [FAST\_SegmentMapConfig](#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) [FAST\_SegmentMapConfig](#ga752c7dc05b0f2d87f8cb4bd8bb04b34e)

 | 

Defines the opaque configuration of a Segment Map.

 |
| 

typedef void \* [FAST\_SegmentMapHandle](#ga3c42403e7c9306245dd1340f166993d9)

 | 

Defines the handle to a Segment Map.

 |
| 

typedef enum [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) [FAST\_ErrorCode](#gac7fc20f8b5755a79929abf218a853078)

 | 

Defines the error codes of FAST Kit.

 |
| 

typedef struct [FAST\_Rect](../../header-files-and-structs/structs/fast-rect/document.md) [FAST\_Rect](#gacb1549fff44eb0707913f3d5f92712b3)

 | 

Defines the data structure of a rectangle.

 |
| 

typedef struct [FAST\_RectPartitionConfig](#gabd3bea5600684d0638b6221f3d0eb23e) [FAST\_RectPartitionConfig](#gabd3bea5600684d0638b6221f3d0eb23e)

 | 

Defines the opaque configuration of the Rectangular Partition Solver.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[FAST\_SegmentMapQueryType](#ga8ef2e816f027493a63bd4e82876f233f) { FAST\_SEGMENTMAP\_QUERY\_TYPE\_SUM = 0, FAST\_SEGMENTMAP\_QUERY\_TYPE\_MIN = 1, FAST\_SEGMENTMAP\_QUERY\_TYPE\_MAX = 2 }

 | 

Enumerates the query types supported by a Segment Map.

 |
| 

[FAST\_SegmentMapUpdateType](#ga2747e3df771507eaeff23cc28f17fc76) { FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SET = 0, FAST\_SEGMENTMAP\_UPDATE\_TYPE\_ADD = 1, FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SUB = 2 }

 | 

Enumerates the update types supported by a Segment Map.

 |
| 

[FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) {

FAST\_ERROR\_CODE\_SUCCESS = 1023100000, FAST\_ERROR\_CODE\_FAIL = 1023100001, FAST\_ERROR\_CODE\_ILLEGAL\_INPUT = 1023100002, FAST\_ERROR\_CODE\_INVALID\_PTR = 1023100003,

FAST\_ERROR\_CODE\_OOM = 1023199001

}

 | 

Enumerates the error codes of FAST Kit.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_CreateConfig](#ga3c5e1b0e64894e3a8910c06800afe560) ([FAST\_SegmentMapConfig](#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \*\*config)

 | 

Creates an opaque configuration instance for a Segment Map.

 |
| 

FAST\_EXPORT void [HMS\_FAST\_SegmentMap\_DestroyConfig](#ga54dc92174e74665cd52b96dd0dc99e45) ([FAST\_SegmentMapConfig](#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \*config)

 | 

Destroys the opaque configuration instance of a Segment Map and deallocates memory.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_SetQueryType](#ga14043280774888f1d2a34951f27415ae) ([FAST\_SegmentMapConfig](#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \*config, [FAST\_SegmentMapQueryType](#ga8ef2e816f027493a63bd4e82876f233f) type)

 | 

Sets the query type in the opaque configuration of a Segment Map.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_SetUpdateType](#ga1f37b6071a0af42c8e217cc0bf2bda2a) ([FAST\_SegmentMapConfig](#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \*config, [FAST\_SegmentMapUpdateType](#ga2747e3df771507eaeff23cc28f17fc76) type)

 | 

Sets the update type in the opaque configuration of a Segment Map.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_Create](#ga1e6c63ee4731e04eeac80a64246db037) ([FAST\_SegmentMapHandle](#ga3c42403e7c9306245dd1340f166993d9) \*handle, size\_t size, const int32\_t \*array, [FAST\_SegmentMapConfig](#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \*config)

 | 

Creates a Segment Map.

 |
| 

FAST\_EXPORT void [HMS\_FAST\_SegmentMap\_Destroy](#gaf24e3e9e42dbf8e6fd7092762ffdf894) ([FAST\_SegmentMapHandle](#ga3c42403e7c9306245dd1340f166993d9) handle)

 | 

Destroys a Segment Map instance.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_Update](#gae85d6f1561a1c4bab0c9161401db07fe) ([FAST\_SegmentMapHandle](#ga3c42403e7c9306245dd1340f166993d9) handle, size\_t left, size\_t right, int32\_t value)

 | 

Performs a range update on a Segment Map.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_Query](#ga13129191dae4340dccb99132f54d4055) ([FAST\_SegmentMapHandle](#ga3c42403e7c9306245dd1340f166993d9) handle, size\_t left, size\_t right, int32\_t \*result)

 | 

Performs a range query on a Segment Map.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_RectPartition\_CreateConfig](#ga051634633006a8f12665a412dc96687e) ([FAST\_RectPartitionConfig](#gabd3bea5600684d0638b6221f3d0eb23e) \*\*config)

 | 

Creates the opaque configuration of the Rectangular Partition Solver.

 |
| 

FAST\_EXPORT void [HMS\_FAST\_RectPartition\_DestroyConfig](#gae515ef39072676065cef8b9af446f2ac) ([FAST\_RectPartitionConfig](#gabd3bea5600684d0638b6221f3d0eb23e) \*config)

 | 

Destroys the opaque configuration of the Rectangular Partition Solver.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_RectPartition\_SetAlgo](#gaec5519d0974e98f6fe99ab2fa50411cc) ([FAST\_RectPartitionConfig](#gabd3bea5600684d0638b6221f3d0eb23e) \*config, const char \*name)

 | 

Sets the algorithm used by the Rectangular Partition Solver. Currently, only the **SweepLineAlgo** algorithm is supported, which outputs a set of non-overlapping rectangles with a minimized count (not guaranteed to be optimal), operating at ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/PieEVYVsQv6RkxCYnrNIsw/en-us_formulaimage_0000002500467256.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=63257F47673FA3A5904D145A5DBD13AEBF63F58E3D8B0B60B47599B5C979F068 "Click to enlarge") complexity.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_RectPartition\_Solve](#ga9329484302723a20438eadc9e4b71609) ([FAST\_RectPartitionConfig](#gabd3bea5600684d0638b6221f3d0eb23e) \*config, size\_t size, const [FAST\_Rect](../../header-files-and-structs/structs/fast-rect/document.md) \*origin, [FAST\_Rect](../../header-files-and-structs/structs/fast-rect/document.md) \*result, size\_t \*resultSize)

 | 

Solves the rectangular partition problem under the specified opaque configuration. The function takes a set of non-overlapping rectangles as input and computes a rectangular partitioning scheme to generate a minimum number of rectangles that cover the same total area.

**Note**:

1\. The input must ensure that any two rectangles do not overlap (that is, any two rectangles must satisfy: ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/oaGaxj2NShG9uxE4HqQFsg/en-us_formulaimage_0000002538474565.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E17B1CD6F99C874B89A4AD1CCE655D6BB71C9420DA5782AC8AB405420141B6F8 "Click to enlarge"), ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/vq34HH4lQGunWmIwkaxljw/en-us_formulaimage_0000002506834654.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2E968AB3535C12C7B90263CFBF4A4BCF2686E32B0A8A3962C7D78AA1C7DD2C3 "Click to enlarge"), ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/DJ0Qb013R_GUYy_1YcYHcg/en-us_formulaimage_0000002538474567.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBE2754F63AEB4A4A91BE0B44520A4E17204CE747FA9E6217B2724E84A47954B "Click to enlarge"), or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/0Sf01vdVRSa6OtD98pfDgw/en-us_formulaimage_0000002506834656.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F61D9295BC85468925D3458FEE3AAA4F8547E6F884A0F1542E182C6B292E580 "Click to enlarge")). Otherwise, the function returns **FAST\_ERROR\_CODE\_ILLEGAL\_INPUT**.

2\. The function can ensure that the number of output rectangles is less than or equal to the number of input rectangles.

 |

#### Type Definition Description

#### FAST\_ErrorCode

typedef enum [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed)

**Description**

Defines the error codes of FAST Kit.

**Start version**: 6.0.2(22)

#### FAST\_Rect

typedef struct [FAST\_Rect](../../header-files-and-structs/structs/fast-rect/document.md) [FAST\_Rect](../../header-files-and-structs/structs/fast-rect/document.md)

**Description**

Defines the data structure of a rectangle.

**Start version**: 6.0.2(22)

#### FAST\_RectPartitionConfig

typedef struct [FAST\_RectPartitionConfig](#gabd3bea5600684d0638b6221f3d0eb23e) [FAST\_RectPartitionConfig](#gabd3bea5600684d0638b6221f3d0eb23e)

**Description**

Defines the opaque configuration of the Rectangular Partition Solver. If no algorithm is set in the configuration, the default algorithm **SweepLineAlgo** is used.

**Start version**: 6.0.2(22)

#### FAST\_SegmentMapConfig

typedef struct [FAST\_SegmentMapConfig](#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) [FAST\_SegmentMapConfig](#ga752c7dc05b0f2d87f8cb4bd8bb04b34e)

**Description**

Defines the opaque configuration of a Segment Map.

**Start version**: 6.0.2(22)

#### FAST\_SegmentMapHandle

typedef void\* [FAST\_SegmentMapHandle](#ga3c42403e7c9306245dd1340f166993d9)

**Description**

Defines the handle to a Segment Map.

**Start version**: 6.0.2(22)

#### FAST\_SegmentMapQueryType

typedef enum [FAST\_SegmentMapQueryType](#ga8ef2e816f027493a63bd4e82876f233f) [FAST\_SegmentMapQueryType](#ga8ef2e816f027493a63bd4e82876f233f)

**Description**

Defines the range query types supported by the Segment Map data structure.

**Start version**: 6.0.2(22)

#### FAST\_SegmentMapUpdateType

typedef enum [FAST\_SegmentMapUpdateType](#ga2747e3df771507eaeff23cc28f17fc76) [FAST\_SegmentMapUpdateType](#ga2747e3df771507eaeff23cc28f17fc76)

**Description**

Defines the range update types supported by the Segment Map data structure.

**Start version**: 6.0.2(22)

#### Enumeration Description

#### FAST\_ErrorCode

enum [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed)

**Description**

Enumerates the error codes of FAST Kit.

**Start version**: 6.0.2(22)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FAST\_ERROR\_CODE\_SUCCESS = 1023100000

 | 

Successful.

 |
| 

FAST\_ERROR\_CODE\_FAIL = 1023100001

 | 

Failure.

 |
| 

FAST\_ERROR\_CODE\_ILLEGAL\_INPUT = 1023100002

 | 

Invalid input.

 |
| 

FAST\_ERROR\_CODE\_INVALID\_PTR = 1023100003

 | 

Invalid pointer (for example, **NULL**).

 |
| 

FAST\_ERROR\_CODE\_OOM = 1023199001

 | 

Memory overflow.

 |

#### FAST\_SegmentMapQueryType

enum [FAST\_SegmentMapQueryType](#ga8ef2e816f027493a63bd4e82876f233f)

**Description**

Enumerates the query types supported by a Segment Map.

This enumeration defines the range query operations that are supported by the Segment Map data structure.

**Start version**: 6.0.2(22)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FAST\_SEGMENTMAP\_QUERY\_TYPE\_SUM

 | 

Range sum query.

 |
| 

FAST\_SEGMENTMAP\_QUERY\_TYPE\_MIN

 | 

Range minimum query.

 |
| 

FAST\_SEGMENTMAP\_QUERY\_TYPE\_MAX

 | 

Range maximum query.

 |

#### FAST\_SegmentMapUpdateType

enum [FAST\_SegmentMapUpdateType](#ga2747e3df771507eaeff23cc28f17fc76)

**Description**

Enumerates the update types supported by a Segment Map.

This enumeration defines the range update operations that are supported by the Segment Map data structure.

**Start version**: 6.0.2(22)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SET

 | 

Assigns the same value to each element in a given range.

 |
| 

FAST\_SEGMENTMAP\_UPDATE\_TYPE\_ADD

 | 

Adds a same value to each element in a given range.

 |
| 

FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SUB

 | 

Subtracts a same value from each element in a given range.

 |

#### Function Description

#### HMS\_FAST\_RectPartition\_CreateConfig()

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) HMS\_FAST\_RectPartition\_CreateConfig ([FAST\_RectPartitionConfig](#gabd3bea5600684d0638b6221f3d0eb23e) \*\* config)

**Description**

Creates the opaque configuration of the Rectangular Partition Solver.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

config

 | 

Pointer to the opaque configuration [FAST\_RectPartitionConfig](#gabd3bea5600684d0638b6221f3d0eb23e) of the Rectangular Partition Solver.

 |

**Returns**:

If the operation is successful, [FAST\_ERROR\_CODE\_SUCCESS](#ga0766cadc400f678a061813aedc6938ed) is returned.

If **config** is **NULL**, [FAST\_ERROR\_CODE\_INVALID\_PTR](#ga0766cadc400f678a061813aedc6938ed) is returned.

If the memory is exhausted, [FAST\_ERROR\_CODE\_OOM](#ga0766cadc400f678a061813aedc6938ed) is returned.

#### HMS\_FAST\_RectPartition\_DestroyConfig()

FAST\_EXPORT void HMS\_FAST\_RectPartition\_DestroyConfig ([FAST\_RectPartitionConfig](#gabd3bea5600684d0638b6221f3d0eb23e) \* config)

**Description**

Destroys the opaque configuration of the Rectangular Partition Solver and deallocates memory. Accessing this opaque configuration again after destruction is considered undefined behavior.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

config

 | 

To-be-destroyed opaque configuration [FAST\_RectPartitionConfig](#gabd3bea5600684d0638b6221f3d0eb23e) of the Rectangular Partition Solver.

 |

#### HMS\_FAST\_RectPartition\_SetAlgo()

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) HMS\_FAST\_RectPartition\_SetAlgo ([FAST\_RectPartitionConfig](#gabd3bea5600684d0638b6221f3d0eb23e) \* config, const char \* name )

**Description**

Sets the algorithm used by the Rectangular Partition Solver. Currently, only the **SweepLineAlgo** algorithm is supported, which outputs a set of non-overlapping rectangles with a minimized count (not guaranteed to be optimal), operating at O(N logN) complexity.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

config

 | 

To-be-set opaque configuration [FAST\_RectPartitionConfig](#gabd3bea5600684d0638b6221f3d0eb23e) of the Rectangular Partition Solver.

 |
| 

name

 | 

Name of the algorithm used by the Rectangular Partition Solver. Currently, only the **SweepLineAlgo** algorithm is supported, which outputs a set of non-overlapping rectangles with a minimized count (not guaranteed to be optimal), operating at ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/nUtESez-T4C74AOUK1EQdQ/en-us_formulaimage_0000002532387121.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BCD454CDE1A7E5D962CD862F838F0CB804576928C7CAACAC803918C3FE6D3082 "Click to enlarge") complexity.

 |

**Returns**:

If the operation is successful, [FAST\_ERROR\_CODE\_SUCCESS](#ga0766cadc400f678a061813aedc6938ed) is returned.

If **config** or **name** is **NULL**, [FAST\_ERROR\_CODE\_INVALID\_PTR](#ga0766cadc400f678a061813aedc6938ed) is returned.

If the algorithm is not supported, [FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](#ga0766cadc400f678a061813aedc6938ed) is returned.

#### HMS\_FAST\_RectPartition\_Solve()

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) HMS\_FAST\_RectPartition\_Solve ([FAST\_RectPartitionConfig](#gabd3bea5600684d0638b6221f3d0eb23e) \* config, size\_t size, const [FAST\_Rect](../../header-files-and-structs/structs/fast-rect/document.md) \* origin, [FAST\_Rect](../../header-files-and-structs/structs/fast-rect/document.md) \* result, size\_t \* resultSize )

**Description**

Solves the rectangular partition problem under the specified opaque configuration. The **result** array must be initialized before this function is called.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

config

 | 

Opaque configuration of the Rectangular Partition Solver. If no algorithm is set in the configuration, the default algorithm **SweepLineAlgo** is used.

 |
| 

size

 | 

Number of rectangles ([FAST\_Rect](../../header-files-and-structs/structs/fast-rect/document.md)) to be partitioned.

 |
| 

origin

 | 

Array of input rectangles ([FAST\_Rect](../../header-files-and-structs/structs/fast-rect/document.md)) to be partitioned.

 |
| 

result

 | 

Array to store output rectangles ([FAST\_Rect](../../header-files-and-structs/structs/fast-rect/document.md)) after partitioning. The **result** array must be initialized before this function is called. The size of the **result** array must be the same as that of the input array. Otherwise, a memory overflow may occur.

 |
| 

resultSize

 | 

Number of rectangles ([FAST\_Rect](../../header-files-and-structs/structs/fast-rect/document.md)) after partitioning.

 |

**Returns**:

If the operation is successful, [FAST\_ERROR\_CODE\_SUCCESS](#ga0766cadc400f678a061813aedc6938ed) is returned.

If an input parameter pointer is **NULL**, [FAST\_ERROR\_CODE\_INVALID\_PTR](#ga0766cadc400f678a061813aedc6938ed) is returned.

If the input is invalid (for example, overlapping rectangles), [FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](#ga0766cadc400f678a061813aedc6938ed) is returned.

If the algorithm fails to solve the problem, [FAST\_ERROR\_CODE\_FAIL](#ga0766cadc400f678a061813aedc6938ed) is returned.

**Note**:

1.  If the **SweepLineAlgo** algorithm is used, [FAST\_ERROR\_CODE\_FAIL](#ga0766cadc400f678a061813aedc6938ed) will not be returned. This is only a preventive measure.

#### HMS\_FAST\_SegmentMap\_Create()

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) HMS\_FAST\_SegmentMap\_Create ([FAST\_SegmentMapHandle](#ga3c42403e7c9306245dd1340f166993d9) \* handle, size\_t size, const int32\_t \* array, [FAST\_SegmentMapConfig](#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \* config )

**Description**

Creates a Segment Map.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

handle

 | 

Pointer to the Segment Map handle [FAST\_SegmentMapHandle](#ga3c42403e7c9306245dd1340f166993d9).

 |
| 

size

 | 

Size (number of elements) of the underlying array.

 |
| 

array

 | 

(Optional) Underlying array for initializing a Segment Map. If the value is **NULL**, all elements in the Segment Map are initialized to **0**. Otherwise, the array size must be the same as that specified by the **size** parameter.

 |
| 

config

 | 

Opaque configuration [FAST\_SegmentMapConfig](#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) of a Segment Map. If this parameter is set to **NULL** or not set, the default query type is [FAST\_SEGMENTMAP\_QUERY\_TYPE\_SUM](#ga8ef2e816f027493a63bd4e82876f233f) and update type is [FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SET](#ga2747e3df771507eaeff23cc28f17fc76).

 |

**Returns**:

If the operation is successful, [FAST\_ERROR\_CODE\_SUCCESS](#ga0766cadc400f678a061813aedc6938ed) is returned.

If **config** or **handle** is **NULL**, [FAST\_ERROR\_CODE\_INVALID\_PTR](#ga0766cadc400f678a061813aedc6938ed) is returned.

If the memory is exhausted, [FAST\_ERROR\_CODE\_OOM](#ga0766cadc400f678a061813aedc6938ed) is returned.

#### HMS\_FAST\_SegmentMap\_CreateConfig()

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) HMS\_FAST\_SegmentMap\_CreateConfig ([FAST\_SegmentMapConfig](#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \*\* config)

**Description**

Creates the opaque configuration of a Segment Map.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

config

 | 

Pointer to the opaque configuration [FAST\_SegmentMapConfig](#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) of a Segment Map.

 |

**Returns**:

If the operation is successful, [FAST\_ERROR\_CODE\_SUCCESS](#ga0766cadc400f678a061813aedc6938ed) is returned.

If **config** is **NULL**, [FAST\_ERROR\_CODE\_INVALID\_PTR](#ga0766cadc400f678a061813aedc6938ed) is returned.

If the memory is exhausted, [FAST\_ERROR\_CODE\_OOM](#ga0766cadc400f678a061813aedc6938ed) is returned.

#### HMS\_FAST\_SegmentMap\_Destroy()

FAST\_EXPORT void HMS\_FAST\_SegmentMap\_Destroy ([FAST\_SegmentMapHandle](#ga3c42403e7c9306245dd1340f166993d9) handle)

**Description**

Destroys a Segment Map instance.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

handle

 | 

Handle [FAST\_SegmentMapHandle](#ga3c42403e7c9306245dd1340f166993d9) to the Segment Map to be destroyed.

 |

#### HMS\_FAST\_SegmentMap\_DestroyConfig()

FAST\_EXPORT void HMS\_FAST\_SegmentMap\_DestroyConfig ([FAST\_SegmentMapConfig](#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \* config)

**Description**

Destroys the opaque configuration of a Segment Map.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

config

 | 

To-be-destroyed opaque configuration [FAST\_SegmentMapConfig](#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) of a Segment Map.

 |

#### HMS\_FAST\_SegmentMap\_Query()

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) HMS\_FAST\_SegmentMap\_Query ([FAST\_SegmentMapHandle](#ga3c42403e7c9306245dd1340f166993d9) handle, size\_t left, size\_t right, int32\_t \* result )

**Description**

Performs a range query on a Segment Map.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

handle

 | 

Handle to a Segment Map.

 |
| 

left

 | 

Left endpoint (included) of a range, which is left-closed and right-open.

 |
| 

right

 | 

Right endpoint (excluded) of a range, which is left-closed and right-open.

 |
| 

result

 | 

Range query result.

 |

**Returns**:

If the operation is successful, [FAST\_ERROR\_CODE\_SUCCESS](#ga0766cadc400f678a061813aedc6938ed) is returned.

If **handle** is **NULL**, [FAST\_ERROR\_CODE\_INVALID\_PTR](#ga0766cadc400f678a061813aedc6938ed) is returned.

If the input is invalid (for example, the left endpoint is greater than or equal to the right endpoint), [FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](#ga0766cadc400f678a061813aedc6938ed) is returned.

#### HMS\_FAST\_SegmentMap\_SetQueryType()

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) HMS\_FAST\_SegmentMap\_SetQueryType ([FAST\_SegmentMapConfig](#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \* config, [FAST\_SegmentMapQueryType](#ga8ef2e816f027493a63bd4e82876f233f) type )

**Description**

Sets the query type in the opaque configuration of a Segment Map.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

config

 | 

To-be-modified opaque configuration of a Segment Map.

 |
| 

type

 | 

Query type.

 |

**Returns**:

If the operation is successful, [FAST\_ERROR\_CODE\_SUCCESS](#ga0766cadc400f678a061813aedc6938ed) is returned.

If **config** is **NULL**, [FAST\_ERROR\_CODE\_INVALID\_PTR](#ga0766cadc400f678a061813aedc6938ed) is returned.

#### HMS\_FAST\_SegmentMap\_SetUpdateType()

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) HMS\_FAST\_SegmentMap\_SetUpdateType ([FAST\_SegmentMapConfig](#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \* config, [FAST\_SegmentMapUpdateType](#ga2747e3df771507eaeff23cc28f17fc76) type )

**Description**

Sets the update type in the opaque configuration of a Segment Map.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

config

 | 

To-be-modified opaque configuration of a Segment Map.

 |
| 

type

 | 

Update type.

 |

**Returns**:

If the operation is successful, [FAST\_ERROR\_CODE\_SUCCESS](#ga0766cadc400f678a061813aedc6938ed) is returned.

If **config** is **NULL**, [FAST\_ERROR\_CODE\_INVALID\_PTR](#ga0766cadc400f678a061813aedc6938ed) is returned.

#### HMS\_FAST\_SegmentMap\_Update()

FAST\_EXPORT [FAST\_ErrorCode](#ga0766cadc400f678a061813aedc6938ed) HMS\_FAST\_SegmentMap\_Update ([FAST\_SegmentMapHandle](#ga3c42403e7c9306245dd1340f166993d9) handle, size\_t left, size\_t right, int32\_t value )

**Description**

Performs a range update on a Segment Map.

**Start version**: 6.0.2(22)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

handle

 | 

Handle to a Segment Map.

 |
| 

left

 | 

Left endpoint (included) of a range, which is left-closed and right-open.

 |
| 

right

 | 

Right endpoint (excluded) of a range, which is left-closed and right-open.

 |
| 

value

 | 

New value.

 |

**Returns**:

If the operation is successful, [FAST\_ERROR\_CODE\_SUCCESS](#ga0766cadc400f678a061813aedc6938ed) is returned.

If **handle** is **NULL**, [FAST\_ERROR\_CODE\_INVALID\_PTR](#ga0766cadc400f678a061813aedc6938ed) is returned.

If the input is invalid (for example, the left endpoint is greater than or equal to the right endpoint), [FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](#ga0766cadc400f678a061813aedc6938ed) is returned.
