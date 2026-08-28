# OH\_NativeVSync\_ExpectedRateRange

typedef struct {...} OH\_NativeVSync\_ExpectedRateRange

#### Overview

Provides the expected frame rate range.

**Since**: 20

**Related module**: [NativeVsync](../../modules/nativevsync/document.md)

**Header file**: [native\_vsync.h](../../header-files/native-vsync-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t min | Minimum frame rate. |
| int32\_t max | Maximum frame rate. |
| int32\_t expected | Expected frame rate. |

#### \[h2\]Member Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_NativeVSync\_FrameCallback)(long long timestamp, void \*data)](#oh_nativevsync_framecallback) | OH\_NativeVSync\_FrameCallback() | 
Defines the pointer to a VSync callback function.

**Since**: 9

**System capability**: SystemCapability.Graphic.Graphic2D.NativeVsync

 |

#### Member Function Description

#### \[h2\]OH\_NativeVSync\_FrameCallback()

typedef void (\*OH\_NativeVSync\_FrameCallback)(long long timestamp, void \*data)

**Item**

Defines the pointer to a VSync callback function.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeVsync

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| long long timestamp | System timestamp obtained by VSync using **CLOCK\_MONOTONIC**, in nanoseconds. |
| void \*data | Pointer to user-defined data. |
