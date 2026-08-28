# native\_avsession\_errors.h

#### Overview

The file declares the playback control error codes.

**File to include**: <multimedia/av\_session/native\_avsession\_errors.h>

**Library**: libohavsession.so

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Since**: 13

**Related module**: [OHAVSession](../../modules/ohavsession/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [AVSession\_ErrCode](#avsession_errcode) | AVSession\_ErrCode | Enumerates the playback control error codes. |

#### Enums

#### \[h2\]AVSession\_ErrCode

enum AVSession\_ErrCode

**Description**

Enumerates the playback control error codes.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| AV\_SESSION\_ERR\_SUCCESS = 0 | The operation is successful. |
| AV\_SESSION\_ERR\_INVALID\_PARAMETER = 401 | Parameter check fails. |
| AV\_SESSION\_ERR\_SERVICE\_EXCEPTION = 6600101 | The session server is abnormal. |
| AV\_SESSION\_ERR\_CODE\_SESSION\_NOT\_EXIST = 6600102 | The session does not exist. |
| AV\_SESSION\_ERR\_CODE\_COMMAND\_INVALID = 6600105 | The session command is invalid. |
| AV\_SESSION\_ERR\_CODE\_SESSION\_INACTIVE = 6600106 | The session is not activated. |
| AV\_SESSION\_ERR\_CODE\_MESSAGE\_OVERLOAD = 6600107 | Too many commands or messages. |
