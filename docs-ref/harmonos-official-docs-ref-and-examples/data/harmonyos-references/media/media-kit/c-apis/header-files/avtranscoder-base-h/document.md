# avtranscoder\_base.h

#### Overview

The file declares the struct and enums used by the AVTranscoder.

**File to include**: <multimedia/player\_framework/avtranscoder\_base.h>

**Library**: libavtranscoder.so

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Related module**: [AVTranscoder](../../modules/avtranscoder/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVTranscoder](../../structs/oh-avtranscoder/document.md) | OH\_AVTranscoder | Initializes an AVTranscoder. |
| [OH\_AVTranscoder\_Config](../../structs/oh-avtranscoder-config/document.md) | OH\_AVTranscoder\_Config | Initializes an AVTranscoder\_Config. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVTranscoder\_State](#oh_avtranscoder_state) | OH\_AVTranscoder\_State | Enumerates the transcoding states. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_AVTranscoder\_OnStateChange)(OH\_AVTranscoder \*transcoder, OH\_AVTranscoder\_State state, void \*userData)](#oh_avtranscoder_onstatechange) | OH\_AVTranscoder\_OnStateChange | Defines a callback invoked when the state of the transcoding process changes. |
| [typedef void (\*OH\_AVTranscoder\_OnError)(OH\_AVTranscoder \*transcoder, int32\_t errorCode, const char \*errorMsg, void \*userData)](#oh_avtranscoder_onerror) | OH\_AVTranscoder\_OnError | Defines a callback invoked when an error occurs during the transcoding process. |
| [typedef void (\*OH\_AVTranscoder\_OnProgressUpdate)(OH\_AVTranscoder \*transcoder, int32\_t progress, void \*userData)](#oh_avtranscoder_onprogressupdate) | OH\_AVTranscoder\_OnProgressUpdate | Defines a callback invoked when the progress of the transcoding process is updated. |

#### Enum Description

#### \[h2\]OH\_AVTranscoder\_State

enum OH\_AVTranscoder\_State

**Description**

Enumerates the transcoding states.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| AVTRANSCODER\_PREPARED = 1 | The transcoding process is prepared and ready to start. |
| AVTRANSCODER\_STARTED = 2 | The transcoding process has started. |
| AVTRANSCODER\_PAUSED = 3 | The transcoding process is paused. |
| AVTRANSCODER\_CANCELLED = 4 | The transcoding process has been canceled. |
| AVTRANSCODER\_COMPLETED = 5 | The transcoding process is completed. |

#### Function Description

#### \[h2\]OH\_AVTranscoder\_OnStateChange()

typedef void (\*OH\_AVTranscoder\_OnStateChange)(OH\_AVTranscoder \*transcoder, OH\_AVTranscoder\_State state, void \*userData)

**Description**

Defines a callback invoked when the state of the transcoding process changes.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder](../../structs/oh-avtranscoder/document.md) \*transcoder | Pointer to an OH\_AVTranscoder instance. |
| [OH\_AVTranscoder\_State](#oh_avtranscoder_state) state | Transcoding state. For details, see [OH\_AVTranscoder\_State](#oh_avtranscoder_state). |
| void \*userData | Pointer to user-defined data. |

#### \[h2\]OH\_AVTranscoder\_OnError()

typedef void (\*OH\_AVTranscoder\_OnError)(OH\_AVTranscoder \*transcoder, int32\_t errorCode, const char \*errorMsg,void \*userData)

**Description**

Defines a callback invoked when an error occurs during the transcoding process.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder](../../structs/oh-avtranscoder/document.md) \*transcoder | Pointer to an OH\_AVTranscoder instance. |
| int32\_t errorCode | 
Error code.

**AV\_ERR\_NO\_MEMORY**: No memory. The value is **1**.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The value is **2**.

**AV\_ERR\_INVALID\_VAL**: The parameter check fails. The value is **3**.

**AV\_ERR\_IO**: I/O error. The value is **4**.

**AV\_ERR\_INVALID\_STATE**: The operation is not supported in the current state. The value is **8**.

**AV\_ERR\_UNSUPPORT**: The function is not supported. The value is **9**.

 |
| const char \*errorMsg | Pointer to the error message. |
| void \*userData | Pointer to user-defined data. |

#### \[h2\]OH\_AVTranscoder\_OnProgressUpdate()

typedef void (\*OH\_AVTranscoder\_OnProgressUpdate)(OH\_AVTranscoder \*transcoder, int32\_t progress, void \*userData)

**Description**

Defines a callback invoked when the progress of the transcoding process is updated.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder](../../structs/oh-avtranscoder/document.md) \*transcoder | Pointer to an OH\_AVTranscoder instance. |
| int32\_t progress | Transcoding progress. |
| void \*userData | Pointer to user-defined data. |
