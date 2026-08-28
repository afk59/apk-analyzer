# native\_avscreen\_capture\_errors.h

#### Overview

The file declares the error codes generated during screen capture.

**File to include**: <multimedia/player\_framework/native\_avscreen\_capture\_errors.h>

**Library**: libnative\_avscreen\_capture.so

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Related module**: [AVScreenCapture](../../modules/avscreencapture/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](#oh_avscreen_capture_errcode) | OH\_AVSCREEN\_CAPTURE\_ErrCode | Defines an enum for the error codes generated during screen capture. |

#### Enum Description

#### \[h2\]OH\_AVSCREEN\_CAPTURE\_ErrCode

enum OH\_AVSCREEN\_CAPTURE\_ErrCode

**Description**

Enumerates the error codes generated during screen capture.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

| Enum | Description |
| :-- | :-- |
| AV\_SCREEN\_CAPTURE\_ERR\_BASE = 0 | Basic value returned when an API call error occurs. |
| AV\_SCREEN\_CAPTURE\_ERR\_OK = AV\_SCREEN\_CAPTURE\_ERR\_BASE | Operation successful. |
| AV\_SCREEN\_CAPTURE\_ERR\_NO\_MEMORY = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 1 | Insufficient memory. |
| AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 2 | Operation not allowed. |
| AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 3 | Invalid parameter. |
| AV\_SCREEN\_CAPTURE\_ERR\_IO = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 4 | Abnormal input and output streams. |
| AV\_SCREEN\_CAPTURE\_ERR\_TIMEOUT = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 5 | Network timeout. |
| AV\_SCREEN\_CAPTURE\_ERR\_UNKNOWN = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 6 | Unknown error. |
| AV\_SCREEN\_CAPTURE\_ERR\_SERVICE\_DIED = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 7 | Media service terminated. |
| AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_STATE = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 8 | Unsupported operation in this state. |
| AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 9 | Unsupported interface. |
| AV\_SCREEN\_CAPTURE\_ERR\_EXTEND\_START = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 100 | Unexpected error. |
