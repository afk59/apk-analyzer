# fast\_ads\_segment\_map.h

#### Overview

Defines data structures and functions related to a Segment Map.

**File to include**: <FASTKit/fast\_ads\_segment\_map.h>

**Library**: libfast\_ads.so

**System capability**: SystemCapability.FAST.Core

**Start version**: 6.0.2(22)

**Related module**: [FAST](../../../modules/fast/document.md)

#### Summary

#### \[h2\]Type Definitions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef enum [FAST\_SegmentMapQueryType](../../../modules/fast/document.md#ga8ef2e816f027493a63bd4e82876f233f) [FAST\_SegmentMapQueryType](../../../modules/fast/document.md#ga7be8db1fe5677bb8732d73ff6d09b6f8)

 | 

Defines the query types supported by a Segment Map.

 |
| 

typedef enum [FAST\_SegmentMapUpdateType](../../../modules/fast/document.md#ga2747e3df771507eaeff23cc28f17fc76) [FAST\_SegmentMapUpdateType](../../../modules/fast/document.md#ga88bbda3d57a45b5bd34a2892013a694f)

 | 

Defines the update types supported by a Segment Map.

 |
| 

typedef struct [FAST\_SegmentMapConfig](../../../modules/fast/document.md#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) [FAST\_SegmentMapConfig](../../../modules/fast/document.md#ga752c7dc05b0f2d87f8cb4bd8bb04b34e)

 | 

Defines the opaque configuration of a Segment Map.

 |
| 

typedef void \* [FAST\_SegmentMapHandle](../../../modules/fast/document.md#ga3c42403e7c9306245dd1340f166993d9)

 | 

Defines the handle to a Segment Map.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[FAST\_SegmentMapQueryType](../../../modules/fast/document.md#ga8ef2e816f027493a63bd4e82876f233f) { [FAST\_SEGMENTMAP\_QUERY\_TYPE\_SUM](../../../modules/fast/document.md#gga8ef2e816f027493a63bd4e82876f233facf3afe794c5e32bf0400630eaba67e9c) = 0, [FAST\_SEGMENTMAP\_QUERY\_TYPE\_MIN](../../../modules/fast/document.md#gga8ef2e816f027493a63bd4e82876f233facbdea2922cd1bbed97dc788cb515a7b9) = 1, [FAST\_SEGMENTMAP\_QUERY\_TYPE\_MAX](../../../modules/fast/document.md#gga8ef2e816f027493a63bd4e82876f233fa4ad7364deefffe6a10c5aa8098670a83) = 2 }

 | 

Enumerates the query types supported by a Segment Map.

 |
| 

[FAST\_SegmentMapUpdateType](../../../modules/fast/document.md#ga2747e3df771507eaeff23cc28f17fc76) { [FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SET](../../../modules/fast/document.md#gga2747e3df771507eaeff23cc28f17fc76a6b3378fd423bad1f8ac685f386fd98a1) = 0, [FAST\_SEGMENTMAP\_UPDATE\_TYPE\_ADD](../../../modules/fast/document.md#gga2747e3df771507eaeff23cc28f17fc76a815d2af4cdaa826e15a162e4dfd4fbff) = 1, [FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SUB](../../../modules/fast/document.md#gga2747e3df771507eaeff23cc28f17fc76a14b3ed12f408fd2232fc78691bbf9647) = 2 }

 | 

Enumerates the update types supported by a Segment Map.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

FAST\_EXPORT [FAST\_ErrorCode](../../../modules/fast/document.md#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_CreateConfig](../../../modules/fast/document.md#ga3c5e1b0e64894e3a8910c06800afe560) ([FAST\_SegmentMapConfig](../../../modules/fast/document.md#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \*\*config)

 | 

Creates the opaque configuration of a Segment Map.

 |
| 

FAST\_EXPORT void [HMS\_FAST\_SegmentMap\_DestroyConfig](../../../modules/fast/document.md#ga54dc92174e74665cd52b96dd0dc99e45) ([FAST\_SegmentMapConfig](../../../modules/fast/document.md#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \*config)

 | 

Destroys the opaque configuration of a Segment Map.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](../../../modules/fast/document.md#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_SetQueryType](../../../modules/fast/document.md#ga14043280774888f1d2a34951f27415ae) ([FAST\_SegmentMapConfig](../../../modules/fast/document.md#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \*config, [FAST\_SegmentMapQueryType](../../../modules/fast/document.md#ga8ef2e816f027493a63bd4e82876f233f) type)

 | 

Sets the query type in the opaque configuration of a Segment Map.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](../../../modules/fast/document.md#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_SetUpdateType](../../../modules/fast/document.md#ga1f37b6071a0af42c8e217cc0bf2bda2a) ([FAST\_SegmentMapConfig](../../../modules/fast/document.md#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \*config, [FAST\_SegmentMapUpdateType](../../../modules/fast/document.md#ga2747e3df771507eaeff23cc28f17fc76) type)

 | 

Sets the update type in the opaque configuration of a Segment Map.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](../../../modules/fast/document.md#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_Create](../../../modules/fast/document.md#ga1e6c63ee4731e04eeac80a64246db037) ([FAST\_SegmentMapHandle](../../../modules/fast/document.md#ga3c42403e7c9306245dd1340f166993d9) \*handle, size\_t size, const int32\_t \*array, [FAST\_SegmentMapConfig](../../../modules/fast/document.md#ga752c7dc05b0f2d87f8cb4bd8bb04b34e) \*config)

 | 

Creates a Segment Map.

 |
| 

FAST\_EXPORT void [HMS\_FAST\_SegmentMap\_Destroy](../../../modules/fast/document.md#gaf24e3e9e42dbf8e6fd7092762ffdf894) ([FAST\_SegmentMapHandle](../../../modules/fast/document.md#ga3c42403e7c9306245dd1340f166993d9) handle)

 | 

Destroys a Segment Map instance and deallocates memory. Calling this function again after destruction is considered undefined behavior.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](../../../modules/fast/document.md#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_Update](../../../modules/fast/document.md#gae85d6f1561a1c4bab0c9161401db07fe) ([FAST\_SegmentMapHandle](../../../modules/fast/document.md#ga3c42403e7c9306245dd1340f166993d9) handle, size\_t left, size\_t right, int32\_t value)

 | 

Performs a range update (value assignment, addition, or subtraction) on a Segment Map based on the configuration.

 |
| 

FAST\_EXPORT [FAST\_ErrorCode](../../../modules/fast/document.md#ga0766cadc400f678a061813aedc6938ed) [HMS\_FAST\_SegmentMap\_Query](../../../modules/fast/document.md#ga13129191dae4340dccb99132f54d4055) ([FAST\_SegmentMapHandle](../../../modules/fast/document.md#ga3c42403e7c9306245dd1340f166993d9) handle, size\_t left, size\_t right, int32\_t \*result)

 | 

Performs a range query on a Segment Map to return statistics like the maximum, minimum, or sum based on the configuration.

 |
