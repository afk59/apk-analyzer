# avplayer\_base.h

#### Overview

The file declares the structs and enums of the AVPlayer.

**File to include**: <multimedia/player\_framework/avplayer\_base.h>

**Library**: libavplayer.so

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Related module**: [AVPlayer](../../modules/avplayer/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [AVPlayerCallback](../../structs/avplayercallback/document.md) | AVPlayerCallback | Contains the set of the [OH\_AVPlayerOnInfo](#oh_avplayeroninfo) and **OH\_AVPlayerOnInfo** callback function pointers. To ensure the normal running of OH\_AVPlayer, you must register this struct with the OH\_AVPlayer instance and process the information reported by the callback functions. |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) | OH\_AVPlayer | Describes an initialized AVPlayer. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [AVPlayerState](#avplayerstate) | AVPlayerState | Enumerates the AVPlayer states. |
| [AVPlayerSeekMode](#avplayerseekmode) | AVPlayerSeekMode | Enumerates the seek modes. |
| [AVPlaybackSpeed](#avplaybackspeed) | AVPlaybackSpeed | Enumerates the playback speeds of the AVPlayer. |
| [AVPlayerOnInfoType](#avplayeroninfotype) | AVPlayerOnInfoType | 
Enumerates the types of messages received by the AVPlayer.

The enum can be used in [OH\_AVPlayerOnInfoCallback](#oh_avplayeroninfocallback) and [OH\_AVPlayerOnInfo](#oh_avplayeroninfo) (deprecated) to indicate the type of information received by the AVPlayer.

 |
| [AVPlayerBufferingType](#avplayerbufferingtype) | AVPlayerBufferingType | Enumerates the types of buffer messages of the AVPlayer. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_AVPlayerOnInfo)(OH\_AVPlayer \*player, AVPlayerOnInfoType type, int32\_t extra)](#oh_avplayeroninfo) | OH\_AVPlayerOnInfo | Called when the AVPlayer receives a message. |
| [typedef void (\*OH\_AVPlayerOnInfoCallback)(OH\_AVPlayer \*player, AVPlayerOnInfoType type, OH\_AVFormat\* infoBody, void \*userData)](#oh_avplayeroninfocallback) | OH\_AVPlayerOnInfoCallback | Called when the AVPlayer receives a message. If this callback is successfully set, the [OH\_AVPlayerOnInfo](#oh_avplayeroninfo) function will not be invoked. |
| [typedef void (\*OH\_AVPlayerOnError)(OH\_AVPlayer \*player, int32\_t errorCode, const char \*errorMsg)](#oh_avplayeronerror) | OH\_AVPlayerOnError | Called when an error occurs in the AVPlayer. This type is available in API version 9 or later. |
| [typedef void (\*OH\_AVPlayerOnErrorCallback)(OH\_AVPlayer \*player, int32\_t errorCode, const char \*errorMsg, void \*userData)](#oh_avplayeronerrorcallback) | OH\_AVPlayerOnErrorCallback | Called when an error occurs in the AVPlayer. If this callback is successfully set, the [OH\_AVPlayerOnError](#oh_avplayeronerror) function will not be invoked. |

#### \[h2\]Variables

| Name | Description |
| :-- | :-- |
| const char \* OH\_PLAYER\_STATE | 
Pointer to the key for obtaining the AVPlayer state. The value is of the int32\_t type.

**Since**: 12

 |
| const char \* OH\_PLAYER\_STATE\_CHANGE\_REASON | 

Pointer to the key for obtaining the AVPlayer state change reason. The value is of the int32\_t type.

The value **1** means that the change is triggered by user operations, and **2** means that the change is triggered by the system.

**Since**: 12

 |
| const char \* OH\_PLAYER\_VOLUME | 

Pointer to the key for obtaining the volume. The value type is float.

**Since**: 12

 |
| const char \* OH\_PLAYER\_BITRATE\_ARRAY | 

Pointer to the key for obtaining the bit rate array. The value is of the uint8\_t byte array type. When this key is used to obtain information, you need to:

Use a pointer variable of the uint8\_t type to store the bit rate list and use a variable of the size\_t type to store the byte array length.

Then it allocates several storage spaces of the uint32\_t type to receive the bit rate integer of the uint32\_t type, which is converted from the uint8\_t byte array.

For details, see the [OH\_AVPlayerOnInfoCallback](#oh_avplayeroninfocallback) function described in the corresponding [development guide](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/using-ndk-avplayer-for-playback).

**Since**: 12

 |
| const char \* OH\_PLAYER\_AUDIO\_INTERRUPT\_TYPE | 

Pointer to the key for obtaining the audio interruption type. The value is of the int32\_t type.

**Since**: 12

 |
| const char \* OH\_PLAYER\_AUDIO\_INTERRUPT\_FORCE | 

Pointer to the key for obtaining the FORCE type of audio interruption. The value is of the int32\_t type.

**Since**: 12

 |
| const char \* OH\_PLAYER\_AUDIO\_INTERRUPT\_HINT | 

Pointer to the key for obtaining the HINT type of audio interruption. The value is of the int32\_t type.

**Since**: 12

 |
| const char \* OH\_PLAYER\_AUDIO\_DEVICE\_CHANGE\_REASON | 

Pointer to the key for obtaining the audio device change reason. The value is of the int32\_t type.

**Since**: 12

 |
| const char \* OH\_PLAYER\_BUFFERING\_TYPE | 

Pointer to the key for obtaining the type of the buffer update message. The value type is [AVPlayerBufferingType](#avplayerbufferingtype).

When this key is used to obtain information, you must use a variable of the int32\_t type to save the result and then convert the result to a value of AVPlayerBufferingType.

**Since**: 12

 |
| const char \* OH\_PLAYER\_BUFFERING\_VALUE | 

Pointer to the key for obtaining the value of the buffer update message. The value is of the int32\_t type. For details, see [AVPlayerBufferingType](#avplayerbufferingtype).

This parameter is valid only when the buffer update message type is **AVPLAYER\_BUFFERING\_PERCENT** or **AVPLAYER\_BUFFERING\_CACHED\_DURATION**.

**Since**: 12

 |
| const char \* OH\_PLAYER\_SEEK\_POSITION | 

Pointer to the key for obtaining the playback progress after the seek operation. The value is of the int32\_t type.

**Since**: 12

 |
| const char \* OH\_PLAYER\_PLAYBACK\_SPEED | 

Pointer to the key for obtaining the playback speed. The value type is [AVPlaybackSpeed](#avplaybackspeed).

When this key is used to obtain information, you must use a variable of the int32\_t type to save the result and then convert the result to a value of AVPlaybackSpeed.

**Since**: 12

 |
| const char \* OH\_PLAYER\_PLAYBACK\_RATE | 

Pointer to the key for obtaining the playback rate. The value is a floating-point number.

**Since**: 20

 |
| const char \* OH\_PLAYER\_BITRATE | 

Pointer to the key for obtaining the bit rate. The value is of the uint32\_t type.

**Since**: 12

 |
| const char \* OH\_PLAYER\_CURRENT\_POSITION | 

Pointer to the key for obtaining the playback progress information. The value is of the int32\_t type.

**Since**: 12

 |
| const char \* OH\_PLAYER\_DURATION | 

Pointer to the key for obtaining the media asset duration. The value type is int64\_t.

**Since**: 12

 |
| const char \* OH\_PLAYER\_VIDEO\_WIDTH | 

Pointer to the key for obtaining the video width. The value is of the int32\_t type.

**Since**: 12

 |
| const char \* OH\_PLAYER\_VIDEO\_HEIGHT | 

Pointer to the key for obtaining the video height. The value is of the int32\_t type.

**Since**: 12

 |
| const char \* OH\_PLAYER\_MESSAGE\_TYPE | 

Pointer to the key for obtaining the type of message received by the AVPlayer. The value is of the int32\_t type.

The value **1** means that the video frame starts to be rendered.

**Since**: 12

 |
| const char \* OH\_PLAYER\_IS\_LIVE\_STREAM | 

Pointer to the key for checking whether a media asset is live streaming. The value is of the int32\_t type.

The value **1** means live streaming.

**Since**: 12

 |
| const char \* OH\_PLAYER\_MD\_KEY\_HAS\_VIDEO | 

Pointer to the key for obtaining whether the media resource contains video tracks. The value is of the int32\_t type.

The value **1** means that the media resource contains video tracks, and the value **0** means the opposite.

**Since**: 22

 |
| const char \* OH\_PLAYER\_MD\_KEY\_HAS\_AUDIO | 

Pointer to the key for obtaining whether the media resource contains audio tracks. The value is of the int32\_t type.

The value **1** means that the media resource contains audio tracks, and the value **0** means the opposite.

**Since**: 22

 |
| const char \* OH\_PLAYER\_MD\_KEY\_HAS\_SUBTITLE | 

Pointer to the key for obtaining whether the media resource contains subtitle tracks. The value is of the int32\_t type.

The value **1** means that the media resource contains subtitle tracks, and the value **0** means the opposite.

**Since**: 22

 |
| const char \* OH\_PLAYER\_MD\_KEY\_TRACK\_INDEX | 

Pointer to the key for obtaining the track index information of a media resource. The value is of the int32\_t type.

**Since**: 22

 |

#### Enum Description

#### \[h2\]AVPlayerState

enum AVPlayerState

**Description**

Enumerates the AVPlayer states.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| AV\_IDLE = 0 | Idle. |
| AV\_INITIALIZED = 1 | Initialized. |
| AV\_PREPARED = 2 | Ready. |
| AV\_PLAYING = 3 | Playing. |
| AV\_PAUSED = 4 | Paused. |
| AV\_STOPPED = 5 | Stopped. |
| AV\_COMPLETED = 6 | Completed. |
| AV\_RELEASED = 7 | Released. |
| AV\_ERROR = 8 | Error. |

#### \[h2\]AVPlayerSeekMode

enum AVPlayerSeekMode

**Description**

Enumerates the seek modes.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| AV\_SEEK\_NEXT\_SYNC = 0 | Seeks to the next key frame at the specified position. |
| AV\_SEEK\_PREVIOUS\_SYNC | Seeks to the previous key frame at the specified position. |
| AV\_SEEK\_CLOSEST = 2 | 
Seeks to the frame closest to the specified position.

**Since**: 12

 |

#### \[h2\]AVPlaybackSpeed

enum AVPlaybackSpeed

**Description**

Enumerates the playback speeds of the AVPlayer.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| AV\_SPEED\_FORWARD\_0\_75\_X | Plays the video at 0.75 times the normal speed. |
| AV\_SPEED\_FORWARD\_1\_00\_X | Plays the video at the normal speed. |
| AV\_SPEED\_FORWARD\_1\_25\_X | Plays the video at 1.25 times the normal speed. |
| AV\_SPEED\_FORWARD\_1\_75\_X | Plays the video at 1.75 times the normal speed. |
| AV\_SPEED\_FORWARD\_2\_00\_X | Plays the video at 2.0 times the normal speed. |
| AV\_SPEED\_FORWARD\_0\_50\_X | 
Plays the video at 0.5 times the normal speed.

**Since**: 12

 |
| AV\_SPEED\_FORWARD\_1\_50\_X | 

Plays the video at 1.5 times the normal speed.

**Since**: 12

 |
| AV\_SPEED\_FORWARD\_3\_00\_X | 

Plays the video at 3.0 times the normal speed.

**Since**: 13

 |
| AV\_SPEED\_FORWARD\_0\_25\_X | 

Plays the video at 0.25 times the normal speed.

**Since**: 13

 |
| AV\_SPEED\_FORWARD\_0\_125\_X | 

Plays the video at 0.125 times the normal speed.

**Since**: 13

 |

#### \[h2\]AVPlayerOnInfoType

enum AVPlayerOnInfoType

**Description**

Enumerates the types of messages received by the AVPlayer.

The enum can be used in **OH\_AVPlayerOnInfoCallback** and **OH\_AVPlayerOnInfo** (deprecated) to indicate the type of information received by the AVPlayer.

Starting from API version 12, you are advised to use [OH\_AVPlayerOnInfoCallback](#oh_avplayeroninfocallback) instead. Different information (**infoBody**) can be obtained for different **OnInfo** types. **infoBody** contains the key-value pairs. For details, see the following enumerated value table.

If you are using API version 11 for development, use **OH\_AVPlayerOnInfo (deprecated)**. For details about the mappings used in this deprecated API, see [OH\_AVPlayerOnInfo](#oh_avplayeroninfo).

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| AV\_INFO\_TYPE\_SEEKDONE = 0 | 
Message returned when seeking to a playback position is complete.

If **key** is set to **OH\_PLAYER\_SEEK\_POSITION**, the value type is int32\_t. The system uses int32\_t to transfer the value, and the application uses int32\_t to obtain the value.

 |
| AV\_INFO\_TYPE\_SPEEDDONE = 1 | 

Message returned when the playback speed setting is complete.

If **key** is set to **OH\_PLAYER\_PLAYBACK\_SPEED**, the value is an enumerated value of [AVPlaybackSpeed](#avplaybackspeed). The system uses int32\_t to transfer the value, and the application uses int32\_t to obtain the value and forcibly converts the value to an enumerated value of [AVPlaybackSpeed](#avplaybackspeed).

 |
| AV\_INFO\_TYPE\_BITRATEDONE = 2 | 

Message returned when the bit rate setting is complete.

If **key** is set to **OH\_PLAYER\_BITRATE**, the value type is uint32\_t. The system uses int32\_t to transfer the value, and the application uses int32\_t to obtain the value and forcibly converts the value to the uint32\_t type.

 |
| AV\_INFO\_TYPE\_EOS = 3 | Message returned when the playback is complete. |
| AV\_INFO\_TYPE\_STATE\_CHANGE = 4 | 

Message returned when the AVPlayer state changes.

If **key** is set to **OH\_PLAYER\_STATE**, the value type is int32\_t. The system uses int32\_t to transfer the value, and the application uses int32\_t to obtain the value and forcibly converts the value to an enumerated value of [AVPlayerState](#avplayerstate).

If **key** is set to **OH\_PLAYER\_STATE\_CHANGE\_REASON**, the value type is int32\_t. The system uses int32\_t to transfer the value, and the application uses int32\_t to obtain the value. The value **1** means that the change is triggered by user operations, and **2** means that the change is triggered by the system.

 |
| AV\_INFO\_TYPE\_POSITION\_UPDATE = 5 | 

Message returned when the playback position changes.

If **key** is set to **OH\_PLAYER\_CURRENT\_POSITION**, the value type is int32\_t. The system uses int32\_t to transfer the value, and the application uses int32\_t to obtain the value.

 |
| AV\_INFO\_TYPE\_MESSAGE = 6 | 

Message returned when video rendering starts.

If **key** is set to **OH\_PLAYER\_MESSAGE\_TYPE**, the value type is int32\_t. The system uses int32\_t to transfer the value, and the application uses int32\_t to obtain the value. The value **1** means that video rendering starts.

 |
| AV\_INFO\_TYPE\_VOLUME\_CHANGE = 7 | 

Message returned when the playback volume changes.

If **key** is set to **OH\_PLAYER\_VOLUME**, the value type is float. The system uses float to transfer the value, and the application uses float to obtain the value. The value range is \[0.0, 1.0\].

 |
| AV\_INFO\_TYPE\_RESOLUTION\_CHANGE = 8 | 

Message returned when the video size is obtained for the first time or the video size is updated.

If **key** is set to **OH\_PLAYER\_VIDEO\_WIDTH** or **OH\_PLAYER\_VIDEO\_HEIGHT**, the value type is int32\_t. The system uses int32\_t to transfer the value, and the application uses int32\_t to obtain the value.

 |
| AV\_INFO\_TYPE\_BUFFERING\_UPDATE = 9 | 

Message returned when multi-queue buffering changes.

If **key** is set to **OH\_PLAYER\_BUFFERING\_TYPE**, the value is an enumerated value of [AVPlayerBufferingType](#avplayerbufferingtype). The system uses int32\_t to transfer the value, and the application uses int32\_t to obtain the value and forcibly converts the value to an enumerated value of [AVPlayerBufferingType](#avplayerbufferingtype).

If **key** is set to **OH\_PLAYER\_BUFFERING\_VALUE**, the value type is int32\_t. The system uses int32\_t to transfer the value, and the application uses int32\_t to obtain the value.

This value is valid when the buffer update message type is **AVPLAYER\_BUFFERING\_PERCENT** or **AVPLAYER\_BUFFERING\_CACHED\_DURATION**, which indicate the percentage of the buffer progress and the duration that the cached data can play, respectively.

 |
| AV\_INFO\_TYPE\_BITRATE\_COLLECT = 10 | 

Message returned to report the HLS video bit rates.

If **key** is set to **OH\_PLAYER\_BITRATE\_ARRAY**, the value type is uint8\_t. The application uses a pointer variable of the uint8\_t type to store the bit rate list and uses a variable of the size\_t type to store the byte array length. Then it allocates several storage spaces of the uint32\_t type to receive the bit rate integer of the uint32\_t type, which is converted from the uint8\_t byte array.

 |
| AV\_INFO\_TYPE\_INTERRUPT\_EVENT = 11 | 

Message returned when the audio focus changes.

The value type is int32\_t. The system uses int32\_t to transfer the value, and the application uses int32\_t to obtain the value.

**key** can be set to any of the following values:

**OH\_PLAYER\_AUDIO\_INTERRUPT\_TYPE**: The value **1** means that the audio interruption event starts, and **2** means that the event ends.

**OH\_PLAYER\_AUDIO\_INTERRUPT\_FORCE**: The value **0** means forcible interruption (the system changes the audio playback status), and **1** means sharing interruption (the application changes the audio playback status).

**OH\_PLAYER\_AUDIO\_INTERRUPT\_HINT**: The value **0** (NONE) means no hint; **1** (RESUME) means that the audio playback is resumed; **2** (PAUSE) means that the audio playback is paused and loses focus; **3** (STOP) means that the audio playback is stopped; **4** (DUCK) means that the audio volume is reduced; **5** (UNDUCK) means that the audio volume is restored.

 |
| AV\_INFO\_TYPE\_DURATION\_UPDATE = 12 | 

Message returned when the playback duration changes.

If **key** is set to **OH\_PLAYER\_DURATION**, the value type is int64\_t. The system uses int64\_t to transfer the value, and the application uses int64\_t to obtain the value.

 |
| AV\_INFO\_TYPE\_IS\_LIVE\_STREAM = 13 | Message returned when live streams are played. If **key** is set to **OH\_PLAYER\_IS\_LIVE\_STREAM**, the value type is int32\_t. The system uses int32\_t to transfer the value, and the application uses int32\_t to obtain the value. The value **0** means a non-live stream, and **1** means a live stream. |
| AV\_INFO\_TYPE\_TRACKCHANGE = 14 | Message returned when the track changes. **extra** is not defined in this scenario. |
| AV\_INFO\_TYPE\_TRACK\_INFO\_UPDATE = 15 | Message returned when the track information updates. **extra** is not defined in this scenario. |
| AV\_INFO\_TYPE\_SUBTITLE\_UPDATE = 16 | Message returned when the subtitle information changes. **extra** is not defined in this scenario. |
| AV\_INFO\_TYPE\_AUDIO\_OUTPUT\_DEVICE\_CHANGE = 17 | 

Message returned when the audio output device changes.

If **key** is set to **OH\_PLAYER\_AUDIO\_DEVICE\_CHANGE\_REASON**, the value type is int32\_t. The system uses int32\_t to transfer the value, and the application uses int32\_t to obtain the value.

 |
| AV\_INFO\_TYPE\_PLAYBACK\_RATE\_DONE = 18 | 

Message returned when the playback rate is applied.

If **key** is set to **OH\_PLAYER\_PLAYBACK\_RATE**, the value type is float. The system uses float to transfer the value, and the application uses float to obtain the value.

**Since**: 20

 |

#### \[h2\]AVPlayerBufferingType

enum AVPlayerBufferingType

**Description**

Enumerates the types of buffer messages of the AVPlayer.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| AVPLAYER\_BUFFERING\_START = 1 | Buffering start message. |
| AVPLAYER\_BUFFERING\_END | Buffering end message. |
| AVPLAYER\_BUFFERING\_PERCENT | Buffer execution progress, in percentage. The value is an integer in the range \[0, 100\]. |
| AVPLAYER\_BUFFERING\_CACHED\_DURATION | Duration that cached data can be played, in milliseconds. |

#### Function Description

#### \[h2\]OH\_AVPlayerOnInfo()

typedef void (\*OH\_AVPlayerOnInfo)(OH\_AVPlayer \*player, AVPlayerOnInfoType type, int32\_t extra)

**Description**

Called when the AVPlayer receives a message.

The following table lists the mappings between **type** and **extra** values.

| Value of type | Value of extra |
| :-- | :-- |
| AV\_INFO\_TYPE\_SEEKDONE | Message returned when seeking to a playback position is complete. **extra** indicates the position after the seek operation. |
| AV\_INFO\_TYPE\_SPEEDDONE | Message returned when the playback speed setting is complete. **extra** indicates the playback speed. For details about the available options, see [AVPlaybackSpeed](#avplaybackspeed). |
| AV\_INFO\_TYPE\_BITRATEDONE | Message returned when the bit rate setting is complete. **extra** indicates the bit rate. |
| AV\_INFO\_TYPE\_EOS | Message returned when the playback is complete. |
| AV\_INFO\_TYPE\_STATE\_CHANGE | Message returned when the AVPlayer state changes. **extra** indicates the new state. For details about the available options, see [AVPlayerState](#avplayerstate). |
| AV\_INFO\_TYPE\_POSITION\_UPDATE | Message returned when the playback position changes. **extra** indicates the current position. |
| AV\_INFO\_TYPE\_MESSAGE | Message returned when video rendering starts. **extra** indicates the first video frame rendered. |
| AV\_INFO\_TYPE\_VOLUME\_CHANGE | Message returned when the playback volume changes. **extra** is not defined in this scenario. |
| AV\_INFO\_TYPE\_RESOLUTION\_CHANGE | Message returned when the video size is obtained for the first time or the video size is updated. **extra** is not defined in this scenario. |
| AV\_INFO\_TYPE\_BUFFERING\_UPDATE | Message returned when multi-queue buffering changes. **extra** indicates the video duration. |
| AV\_INFO\_TYPE\_BITRATE\_COLLECT | Message returned to report the HLS video bit rates. Each bit rate has been converted into a uint8\_t byte array during the reporting. You need to forcibly convert the uint8\_t byte array into a uint32\_t integer array. |
| AV\_INFO\_TYPE\_INTERRUPT\_EVENT | Message returned when the audio focus changes. **extra** indicates the hints provided along with audio interruption. For details about the available options, see [OH\_AudioInterrupt\_Hint](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiointerrupt_hint). The application can determine whether to perform further processing based on the hint. |
| AV\_INFO\_TYPE\_DURATION\_UPDATE | Message returned when the playback duration changes. **extra** indicates the video duration. |
| AV\_INFO\_TYPE\_IS\_LIVE\_STREAM | Message returned when live streams are played. **extra** indicates whether the stream is a live stream. The value **0** means a non-live stream, and **1** means a live stream. |
| AV\_INFO\_TYPE\_TRACKCHANGE | Message returned when the track changes. **extra** is not defined in this scenario. |
| AV\_INFO\_TYPE\_TRACK\_INFO\_UPDATE | Message returned when the track information updates. **extra** is not defined in this scenario. |
| AV\_INFO\_TYPE\_SUBTITLE\_UPDATE | Message returned when the subtitle information changes. **extra** is not defined in this scenario. |
| AV\_INFO\_TYPE\_AUDIO\_OUTPUT\_DEVICE\_CHANGE | Message returned when the audio output device changes. **extra** indicates the device change reason. For details about the available options, see [OH\_AudioStream\_DeviceChangeReason](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiostream_devicechangereason). |

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Deprecated from**: 12

**Substitute**: [OH\_AVPlayerOnInfoCallback](#oh_avplayeroninfocallback)

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to an OH\_AVPlayer instance. |
| [AVPlayerOnInfoType](#avplayeroninfotype) type | Message type. For details about the available options, see [AVPlayerOnInfoType](#avplayeroninfotype). For details about the mappings between **type** and **extra** values, see the function description. |
| int32\_t extra | Other information, such as the start time and position of the media file to play. |

#### \[h2\]OH\_AVPlayerOnInfoCallback()

typedef void (\*OH\_AVPlayerOnInfoCallback)(OH\_AVPlayer \*player, AVPlayerOnInfoType type, OH\_AVFormat\* infoBody,void \*userData)

**Description**

Called when the AVPlayer receives a message. If this callback is successfully set, the **OH\_AVPlayerOnInfo** function will not be invoked.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to an OH\_AVPlayer instance. |
| [AVPlayerOnInfoType](#avplayeroninfotype) type | Message type. For details about the available options, see [AVPlayerOnInfoType](#avplayeroninfotype). |
| [OH\_AVFormat](../../../../avcodec-kit/c-apis/structs/oh-avformat/document.md)\* infoBody | Pointer to the message. The pointer is valid only in this callback. |
| void \*userData | Pointer to the instance provided by the caller when setting the callback function. |

#### \[h2\]OH\_AVPlayerOnError()

typedef void (\*OH\_AVPlayerOnError)(OH\_AVPlayer \*player, int32\_t errorCode, const char \*errorMsg)

**Description**

Called when an error occurs in the AVPlayer. This type is available in API version 9 or later.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Deprecated from**: 12

**Substitute**: [OH\_AVPlayerOnErrorCallback](#oh_avplayeronerrorcallback)

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to an OH\_AVPlayer instance. |
| int32\_t errorCode | 
Error code.

**AV\_ERR\_NO\_MEMORY**: No memory. The value is **1**.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The value is **2**.

**AV\_ERR\_INVALID\_VAL**: Invalid value. The value is **3**.

**AV\_ERR\_IO**: I/O error. The value is **4**.

**AV\_ERR\_TIMEOUT**: Timeout. The value is **5**.

**AV\_ERR\_UNKNOWN**: Unknown error. The value is **6**.

**AV\_ERR\_SERVICE\_DIED**: The service is dead. The value is **7**.

**AV\_ERR\_INVALID\_STATE**: The operation is not supported in the current state. The value is **8**.

**AV\_ERR\_UNSUPPORT**: The function is not supported. The value is **9**.

**AV\_ERR\_EXTEND\_START**: Initial value for extended error codes. The value is **100**.

 |
| const char \*errorMsg | Pointer to the error message. |

#### \[h2\]OH\_AVPlayerOnErrorCallback()

typedef void (\*OH\_AVPlayerOnErrorCallback)(OH\_AVPlayer \*player, int32\_t errorCode, const char \*errorMsg,void \*userData)

**Description**

Called when an error occurs in the AVPlayer. If this callback is successfully set, the **OH\_AVPlayerOnError** function will not be invoked.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to an OH\_AVPlayer instance. |
| int32\_t errorCode | 
Error code.

**AV\_ERR\_NO\_MEMORY**: No memory. The value is **1**.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The value is **2**.

**AV\_ERR\_INVALID\_VAL**: Invalid value. The value is **3**.

**AV\_ERR\_IO**: I/O error. For API versions 12 and 13, the value is **4**. Starting from API version 14, it corresponds to more specific error codes ranging from 5411001 to 5411011.

**AV\_ERR\_TIMEOUT**: Timeout. The value is **5**.

**AV\_ERR\_UNKNOWN**: Unknown error. The value is **6**.

**AV\_ERR\_SERVICE\_DIED**: The service is dead. The value is **7**.

**AV\_ERR\_INVALID\_STATE**: The operation is not supported in the current state. The value is **8**.

**AV\_ERR\_UNSUPPORT**: The function is not supported. The value is **9**.

**AV\_ERR\_EXTEND\_START**: Initial value for extended error codes. The value is **100**.

 |
| const char \*errorMsg | Pointer to the error message. |
| void \*userData | Pointer to the user data passed in. The same data is returned. |
