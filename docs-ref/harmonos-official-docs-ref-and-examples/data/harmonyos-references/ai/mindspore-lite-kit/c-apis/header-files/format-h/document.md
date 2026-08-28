# format.h

#### Overview

Declares tensor data formats.

**File to include**: <mindspore/format.h>

**Library**: libmindspore\_lite\_ndk.so

**System capability**: SystemCapability.Ai.MindSpore

**Since**: 9

**Related module**: [MindSpore](../../modules/mindspore/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AI\_Format](#oh_ai_format) | OH\_AI\_Format | Data formats supported by MSTensor. |

#### Enum Description

#### \[h2\]OH\_AI\_Format

enum OH\_AI\_Format

**Description**

Declares data formats supported by MSTensor.

**Since**: 9

| Enum Item | Description |
| :-- | :-- |
| OH\_AI\_FORMAT\_NCHW = 0 | Tensor data is stored in the sequence of batch number N, channel C, height H, and width W. |
| OH\_AI\_FORMAT\_NHWC = 1 | Tensor data is stored in the sequence of batch number N, height H, width W, and channel C. |
| OH\_AI\_FORMAT\_NHWC4 = 2 | Tensor data is stored in the sequence of batch number N, height H, width W, and channel C. The C axis is 4-byte aligned. |
| OH\_AI\_FORMAT\_HWKC = 3 | Tensor data is stored in the sequence of height H, width W, core count K, and channel C. |
| OH\_AI\_FORMAT\_HWCK = 4 | Tensor data is stored in the sequence of height H, width W, channel C, and core count K. |
| OH\_AI\_FORMAT\_KCHW = 5 | Tensor data is stored in the sequence of core count K, channel C, height H, and width W. |
| OH\_AI\_FORMAT\_CKHW = 6 | Tensor data is stored in the sequence of channel C, core count K, height H, and width W. |
| OH\_AI\_FORMAT\_KHWC = 7 | Tensor data is stored in the sequence of core count K, height H, width W, and channel C. |
| OH\_AI\_FORMAT\_CHWK = 8 | Tensor data is stored in the sequence of channel C, height H, width W, and core count K. |
| OH\_AI\_FORMAT\_HW = 9 | Tensor data is stored in the sequence of height H and width W. |
| OH\_AI\_FORMAT\_HW4 = 10 | Tensor data is stored in the sequence of height H and width W. The W axis is 4-byte aligned. |
| OH\_AI\_FORMAT\_NC = 11 | Tensor data is stored in the sequence of batch number N and channel C. |
| OH\_AI\_FORMAT\_NC4 = 12 | Tensor data is stored in the sequence of batch number N and channel C. The C axis is 4-byte aligned. |
| OH\_AI\_FORMAT\_NC4HW4 = 13 | Tensor data is stored in the sequence of batch number N, channel C, height H, and width W. The C axis and W axis are 4-byte aligned. |
| OH\_AI\_FORMAT\_NCDHW = 15 | Tensor data is stored in the sequence of batch number N, channel C, depth D, height H, and width W. |
| OH\_AI\_FORMAT\_NWC = 16 | Tensor data is stored in the sequence of batch number N, width W, and channel C. |
| OH\_AI\_FORMAT\_NCW = 17 | Tensor data is stored in the sequence of batch number N, channel C, and width W. |
