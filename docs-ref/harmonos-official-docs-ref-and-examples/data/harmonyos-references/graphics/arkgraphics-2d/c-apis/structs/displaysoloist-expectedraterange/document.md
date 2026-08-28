# DisplaySoloist\_ExpectedRateRange

typedef struct {...} DisplaySoloist\_ExpectedRateRange

#### Overview

This struct describes the expected frame rate range.

**Since**: 12

**Related module**: [NativeDisplaySoloist](../../modules/nativedisplaysoloist/document.md)

**Header file**: [native\_display\_soloist.h](../../header-files/native-display-soloist-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t min | Minimum value of the expected frame rate range. The value range is \[0,120\]. |
| int32\_t max | Maximum value of the expected frame rate range. The value range is \[0,120\]. |
| int32\_t expected | Expected frame rate. The value range is \[0,120\]. |

#### \[h2\]Member Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_DisplaySoloist\_FrameCallback)(long long timestamp, long long targetTimestamp, void\* data)](#oh_displaysoloist_framecallback) | OH\_DisplaySoloist\_FrameCallback() | 
Defines the pointer to an OH\_DisplaySoloist callback function.

**Since**: 12

 |

#### Member Function Description

#### \[h2\]OH\_DisplaySoloist\_FrameCallback()

typedef void (\*OH\_DisplaySoloist\_FrameCallback)(long long timestamp, long long targetTimestamp, void\* data)

**Description**

Defines the pointer to an OH\_DisplaySoloist callback function.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| long long timestamp | Current frame VSync timestamp. |
| long long targetTimestamp | Expected VSync timestamp of the next frame. |
| void\* data | Pointer to user-defined data. |
