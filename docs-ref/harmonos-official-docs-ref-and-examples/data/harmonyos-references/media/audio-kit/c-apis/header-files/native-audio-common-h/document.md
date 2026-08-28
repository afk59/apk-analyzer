# native\_audio\_common.h

#### Overview

The file declares the common basic audio data structs.

It defines the types of the common return values of audio interfaces.

**File to include**: <ohaudio/native\_audio\_common.h>

**Library**: libohaudio.so

**System capability**: SystemCapability.Multimedia.Audio.Core

**Since**: 12

**Related module**: [OHAudio](../../modules/ohaudio/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioCommon\_Result](#oh_audiocommon_result) | OH\_AudioCommon\_Result | Enumerates the audio operation results. |
| [OH\_AudioScene](#oh_audioscene) | OH\_AudioScene | Enumerates the audio scenes. |
| [OH\_AudioRingerMode](#oh_audioringermode) | OH\_AudioRingerMode | Enumerates the ringer mode. |

#### Enum Description

#### \[h2\]OH\_AudioCommon\_Result

enum OH\_AudioCommon\_Result

**Description**

Enumerates the audio operation results.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| AUDIOCOMMON\_RESULT\_SUCCESS = 0 | Operation successful. |
| AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM = 6800101 | Incorrect parameter. |
| AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY = 6800102 | No memory. |
| AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE = 6800103 | Invalid state. |
| AUDIOCOMMON\_RESULT\_ERROR\_UNSUPPORTED = 6800104 | Unsupported operation. |
| AUDIOCOMMON\_RESULT\_ERROR\_TIMEOUT = 6800105 | Operation timeout. |
| AUDIOCOMMON\_RESULT\_ERROR\_STREAM\_LIMIT = 6800201 | Reached the maximum number of audio streams allowed. |
| AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM = 6800301 | System error. |

#### \[h2\]OH\_AudioScene

enum OH\_AudioScene

**Description**

Enumerates the audio scenes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| AUDIO\_SCENE\_DEFAULT = 0 | Default audio scene. |
| AUDIO\_SCENE\_RINGING = 1 | Ringing scene. |
| AUDIO\_SCENE\_PHONE\_CALL = 2 | Phone call scene. |
| AUDIO\_SCENE\_VOICE\_CHAT = 3 | Voice chat scene. |

#### \[h2\]OH\_AudioRingerMode

enum OH\_AudioRingerMode

**Description**

Enumerates the ringer mode.

**Device behavior difference**: If this API is set to the vibration mode on a device without a vibration component, no vibration effect is generated.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| AUDIO\_RINGER\_MODE\_SILENT = 0 | Silent mode. |
| AUDIO\_RINGER\_MODE\_VIBRATE = 1 | Vibration mode. |
| AUDIO\_RINGER\_MODE\_NORMAL = 2 | Normal mode. |
