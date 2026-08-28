# native\_audiostream\_base.h

#### Overview

The file declares the basic data structure of OHAudio.

**File to include**: <ohaudio/native\_audiostream\_base.h>

**Library**: libohaudio.so

**System capability**: SystemCapability.Multimedia.Audio.Core

**Since**: 10

**Related module**: [OHAudio](../../modules/ohaudio/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioStreamInfo](../../structs/oh-audiostreaminfo/document.md) | OH\_AudioStreamInfo | Describes the audio stream information, which is used to describe the basic audio format. |
| [OH\_AudioRenderer\_Callbacks\_Struct](../../structs/oh-audiorenderer-callbacks-struct/document.md) | OH\_AudioRenderer\_Callbacks | Describes a pointer to the callbacks related to an audio renderer. (It is deprecated in API version 20.) |
| [OH\_AudioCapturer\_Callbacks\_Struct](../../structs/oh-audiocapturer-callbacks-struct/document.md) | OH\_AudioCapturer\_Callbacks | 
Describes a pointer to the callbacks related to an audio capturer.

To avoid unexpected behavior, ensure that every member variable of the struct is initialized by a custom callback method or a null pointer when setting the audio callback functions. (It is deprecated in API version 20.)

 |
| [OH\_AudioStreamBuilderStruct](../../structs/oh-audiostreambuilderstruct/document.md) | OH\_AudioStreamBuilder | Defines a struct for an audio stream builder. An audio stream builder instance is often used to create an audio stream and set its attributes. |
| [OH\_AudioRendererStruct](../../structs/oh-audiorendererstruct/document.md) | OH\_AudioRenderer | Describes an audio renderer, which is used to render audio data. |
| [OH\_AudioCapturerStruct](../../structs/oh-audiocapturerstruct/document.md) | OH\_AudioCapturer | Describes an audio capturer, which is used to capture audio data. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioStream\_Result](#oh_audiostream_result) | OH\_AudioStream\_Result | Enumerates the audio operation results. |
| [OH\_AudioStream\_Type](#oh_audiostream_type) | OH\_AudioStream\_Type | Enumerates the audio stream types. |
| [OH\_AudioStream\_SampleFormat](#oh_audiostream_sampleformat) | OH\_AudioStream\_SampleFormat | Enumerates the sampling formats of audio streams. |
| [OH\_AudioStream\_EncodingType](#oh_audiostream_encodingtype) | OH\_AudioStream\_EncodingType | Enumerates the encoding types of audio streams. |
| [OH\_AudioStream\_Usage](#oh_audiostream_usage) | OH\_AudioStream\_Usage | 
Enumerates the usage scenarios of audio streams.

Generally, it is used to describe usage scenarios of audio output streams.

 |
| [OH\_AudioStream\_LatencyMode](#oh_audiostream_latencymode) | OH\_AudioStream\_LatencyMode | Enumerates the latency modes of audio streams. |
| [OH\_AudioStream\_DirectPlaybackMode](#oh_audiostream_directplaybackmode) | OH\_AudioStream\_DirectPlaybackMode | Enumerates the direct playback modes of audio streams. |
| [OH\_AudioStream\_VolumeMode](#oh_audiostream_volumemode) | OH\_AudioStream\_VolumeMode | Enumerates the volume modes of audio streams. |
| [OH\_AudioStream\_State](#oh_audiostream_state) | OH\_AudioStream\_State | Enumerates the audio stream states. |
| [OH\_AudioStream\_SourceType](#oh_audiostream_sourcetype) | OH\_AudioStream\_SourceType | 

Enumerates the usage scenarios of audio streams.

Generally, it is used to describe usage scenarios of audio input streams.

 |
| [OH\_AudioStream\_Event](#oh_audiostream_event) | OH\_AudioStream\_Event | Enumerates the audio stream events. (It is deprecated in API version 20.) |
| [OH\_AudioInterrupt\_ForceType](#oh_audiointerrupt_forcetype) | OH\_AudioInterrupt\_ForceType | 

Enumerates the types of force that causes audio interruption.

The force type is obtained when an audio interruption event is received.

This type specifies whether the audio interruption operation is forcibly performed by the system. The operation information (such as audio pause or stop) can be obtained through [OH\_AudioInterrupt\_Hint](#oh_audiointerrupt_hint).

 |
| [OH\_AudioInterrupt\_Hint](#oh_audiointerrupt_hint) | OH\_AudioInterrupt\_Hint | 

Enumerates the hints provided along with audio interruption.

The force type is obtained when an audio interruption event is received.

The hint specifies the operation (such as audio pause or volume adjustment) to be performed on audio streams based on the focus strategy.

You can determine whether the operation is forcibly performed by the system based on [OH\_AudioInterrupt\_ForceType](#oh_audiointerrupt_forcetype).

 |
| [OH\_AudioInterrupt\_Mode](#oh_audiointerrupt_mode) | OH\_AudioInterrupt\_Mode | Enumerates the audio interruption modes. |
| [OH\_AudioStream\_AudioEffectMode](#oh_audiostream_audioeffectmode) | OH\_AudioStream\_AudioEffectMode | Enumerates the audio effect modes. |
| [OH\_AudioStream\_FastStatus](#oh_audiostream_faststatus) | OH\_AudioStream\_FastStatus | Enumerates the low-latency statuses. |
| [OH\_AudioStream\_DeviceChangeReason](#oh_audiostream_devicechangereason) | OH\_AudioStream\_DeviceChangeReason | Enumerates the reasons for audio stream device changes. |
| [OH\_AudioStream\_PrivacyType](#oh_audiostream_privacytype) | OH\_AudioStream\_PrivacyType | Enumerates the privacy types of an audio stream. The privacy type specifies whether the audio stream can be recorded by other applications. |
| [OH\_AudioData\_Callback\_Result](#oh_audiodata_callback_result) | OH\_AudioData\_Callback\_Result | Enumerates the audio data callback results. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_AudioRenderer\_OutputDeviceChangeCallback)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioStream\_DeviceChangeReason reason)](#oh_audiorenderer_outputdevicechangecallback) | OH\_AudioRenderer\_OutputDeviceChangeCallback | Defines a pointer to the callback invoked when the audio capturer device changes. |
| [typedef void (\*OH\_AudioRenderer\_OnMarkReachedCallback)(OH\_AudioRenderer\* renderer, uint32\_t samplePos, void\* userData)](#oh_audiorenderer_onmarkreachedcallback) | OH\_AudioRenderer\_OnMarkReachedCallback | Defines a pointer to the callback invoked when the mark position is reached. |
| [typedef int32\_t (\*OH\_AudioRenderer\_WriteDataWithMetadataCallback)(OH\_AudioRenderer\* renderer, void\* userData, void\* audioData, int32\_t audioDataSize, void\* metadata, int32\_t metadataSize)](#oh_audiorenderer_writedatawithmetadatacallback) | OH\_AudioRenderer\_WriteDataWithMetadataCallback | Defines a function pointer to the callback used to write audio data and metadata. |
| [typedef OH\_AudioData\_Callback\_Result (\*OH\_AudioRenderer\_OnWriteDataCallback)(OH\_AudioRenderer\* renderer, void\* userData, void\* audioData, int32\_t audioDataSize)](#oh_audiorenderer_onwritedatacallback) | OH\_AudioRenderer\_OnWriteDataCallback | 
Defines a function pointer to the callback used to write audio data.

The callback is used only to write audio data. Do not call AudioRenderer APIs in it.

The return result indicates whether the data filled in the buffer is valid. If the data is invalid, the data entered by the user will not be played.

Once the callback finishes its execution, the audio service queues the data pointed to by **audioData** for playback. Therefore, do not change the data outside the callback. It is crucial to fill **audioData** with the exact length (specified by **audioDataSize**) of data designated for playback; otherwise, noises may occur during playback.

The **audioDataSize** parameter can be set by calling [OH\_AudioStreamBuilder\_SetFrameSizeInCallback](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_setframesizeincallback).

 |

#### Enum Description

#### \[h2\]OH\_AudioStream\_Result

enum OH\_AudioStream\_Result

**Description**

Enumerates the audio operation results.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| AUDIOSTREAM\_SUCCESS = 0 | Operation successful. |
| AUDIOSTREAM\_ERROR\_INVALID\_PARAM = 1 | Invalid input parameter. |
| AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE = 2 | Invalid state. |
| AUDIOSTREAM\_ERROR\_SYSTEM = 3 | System error. |
| AUDIOSTREAM\_ERROR\_UNSUPPORTED\_FORMAT = 4 | 
Unsupported audio format, such as unsupported encoding type or sampling format.

**Since**: 19

 |

#### \[h2\]OH\_AudioStream\_Type

enum OH\_AudioStream\_Type

**Description**

Enumerates the audio stream types.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| AUDIOSTREAM\_TYPE\_RENDERER = 1 | The audio stream is an output stream. |
| AUDIOSTREAM\_TYPE\_CAPTURER = 2 | The audio stream is an input stream. |

#### \[h2\]OH\_AudioStream\_SampleFormat

enum OH\_AudioStream\_SampleFormat

**Description**

Enumerates the sampling formats of audio streams.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| AUDIOSTREAM\_SAMPLE\_U8 = 0 | Unsigned 8-bit. |
| AUDIOSTREAM\_SAMPLE\_S16LE = 1 | Short 16-bit little-endian. |
| AUDIOSTREAM\_SAMPLE\_S24LE = 2 | Short 24-bit little-endian. |
| AUDIOSTREAM\_SAMPLE\_S32LE = 3 | Short 32-bit little-endian. |
| AUDIOSTREAM\_SAMPLE\_F32LE = 4 | 
Float 32-bit little-endian.

**Since**: 17

 |

#### \[h2\]OH\_AudioStream\_EncodingType

enum OH\_AudioStream\_EncodingType

**Description**

Enumerates the encoding types of audio streams.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| AUDIOSTREAM\_ENCODING\_TYPE\_RAW = 0 | PCM encoding. |
| AUDIOSTREAM\_ENCODING\_TYPE\_AUDIOVIVID = 1 | 
Audio Vivid encoding.

**Since**: 12

 |
| AUDIOSTREAM\_ENCODING\_TYPE\_E\_AC3 = 2 | 

E\_AC3 encoding.

**Since**: 19

 |

#### \[h2\]OH\_AudioStream\_Usage

enum OH\_AudioStream\_Usage

**Description**

Enumerates the usage scenarios of audio streams.

Generally, it is used to describe usage scenarios of audio output streams.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| AUDIOSTREAM\_USAGE\_UNKNOWN = 0 | Unknown content. |
| AUDIOSTREAM\_USAGE\_MUSIC = 1 | Music. |
| AUDIOSTREAM\_USAGE\_VOICE\_COMMUNICATION = 2 | VoIP voice call. |
| AUDIOSTREAM\_USAGE\_VOICE\_ASSISTANT = 3 | Voice assistant. |
| AUDIOSTREAM\_USAGE\_ALARM = 4 | Alarming. |
| AUDIOSTREAM\_USAGE\_VOICE\_MESSAGE = 5 | Voice message. |
| AUDIOSTREAM\_USAGE\_RINGTONE = 6 | Ringtone. |
| AUDIOSTREAM\_USAGE\_NOTIFICATION = 7 | Notification. |
| AUDIOSTREAM\_USAGE\_ACCESSIBILITY = 8 | Accessibility. |
| AUDIOSTREAM\_USAGE\_MOVIE = 10 | Movie or video. |
| AUDIOSTREAM\_USAGE\_GAME = 11 | Gaming. |
| AUDIOSTREAM\_USAGE\_AUDIOBOOK = 12 | Audiobooks (including crosstalks and storytelling), news radio, and podcasts. |
| AUDIOSTREAM\_USAGE\_NAVIGATION = 13 | Navigation. |
| AUDIOSTREAM\_USAGE\_VIDEO\_COMMUNICATION = 17 | 
VoIP video call.

**Since**: 12

 |

#### \[h2\]OH\_AudioStream\_LatencyMode

enum OH\_AudioStream\_LatencyMode

**Description**

Enumerates the latency modes of audio streams.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| AUDIOSTREAM\_LATENCY\_MODE\_NORMAL = 0 | Normal latency mode. |
| AUDIOSTREAM\_LATENCY\_MODE\_FAST = 1 | Low latency mode. |

#### \[h2\]OH\_AudioStream\_DirectPlaybackMode

enum OH\_AudioStream\_DirectPlaybackMode

**Description**

Enumerates the direct playback modes of audio streams.

**Since**: 19

| Enum Item | Description |
| :-- | :-- |
| AUDIOSTREAM\_DIRECT\_PLAYBACK\_NOT\_SUPPORTED = 0 | Direct playback is not supported. |
| AUDIOSTREAM\_DIRECT\_PLAYBACK\_BITSTREAM\_SUPPORTED = 1 | Direct playback of bit streams (without decoding) is supported. |
| AUDIOSTREAM\_DIRECT\_PLAYBACK\_PCM\_SUPPORTED = 2 | Direct playback of PCM-encoded audio is supported. |

#### \[h2\]OH\_AudioStream\_VolumeMode

enum OH\_AudioStream\_VolumeMode

**Description**

Enumerates the volume modes of audio streams.

**Since**: 19

| Enum Item | Description |
| :-- | :-- |
| AUDIOSTREAM\_VOLUMEMODE\_SYSTEM\_GLOBAL = 0 | System-level volume (default mode). |
| AUDIOSTREAM\_VOLUMEMODE\_APP\_INDIVIDUAL = 1 | 
Application-level volume.

In this mode, you can set and query the application volume through the provided functions.

 |

#### \[h2\]OH\_AudioStream\_State

enum OH\_AudioStream\_State

**Description**

Enumerates the audio stream states.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| AUDIOSTREAM\_STATE\_INVALID = -1 | Invalid state. |
| AUDIOSTREAM\_STATE\_NEW = 0 | Newly created. |
| AUDIOSTREAM\_STATE\_PREPARED = 1 | Prepared. |
| AUDIOSTREAM\_STATE\_RUNNING = 2 | Running. |
| AUDIOSTREAM\_STATE\_STOPPED = 3 | Stopped. |
| AUDIOSTREAM\_STATE\_RELEASED = 4 | Released. |
| AUDIOSTREAM\_STATE\_PAUSED = 5 | Paused. |

#### \[h2\]OH\_AudioStream\_SourceType

enum OH\_AudioStream\_SourceType

**Description**

Enumerates the usage scenarios of audio streams.

Generally, it is used to describe usage scenarios of audio input streams.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| AUDIOSTREAM\_SOURCE\_TYPE\_INVALID = -1 | Invalid state. |
| AUDIOSTREAM\_SOURCE\_TYPE\_MIC = 0 | Audio recording. |
| AUDIOSTREAM\_SOURCE\_TYPE\_VOICE\_RECOGNITION = 1 | Voice recognition. |
| AUDIOSTREAM\_SOURCE\_TYPE\_PLAYBACK\_CAPTURE = 2 | 
Audio playback.

**Deprecated from**: 12

**Substitute**: [OH\_AVScreenCapture](../../../../media-kit/c-apis/structs/oh-avscreencapture/document.md)

 |
| AUDIOSTREAM\_SOURCE\_TYPE\_VOICE\_COMMUNICATION = 7 | Voice communication. |
| AUDIOSTREAM\_SOURCE\_TYPE\_VOICE\_MESSAGE = 10 | 

Voice message.

**Since**: 12

 |
| AUDIOSTREAM\_SOURCE\_TYPE\_CAMCORDER = 13 | 

Video recording.

**Since**: 13

 |
| AUDIOSTREAM\_SOURCE\_TYPE\_UNPROCESSED = 14 | 

Raw microphone recording, where the system does not perform any algorithm processing.

**Since**: 14

 |
| AUDIOSTREAM\_SOURCE\_TYPE\_LIVE = 17 | 

Live.

**Since**: 20

 |

#### \[h2\]OH\_AudioStream\_Event

enum OH\_AudioStream\_Event

**Description**

Enumerates the audio stream events.

**Since**: 10

**Deprecated from**: 20

**Substitute**: [OH\_AudioRenderer\_OutputDeviceChangeCallback](#oh_audiorenderer_outputdevicechangecallback)

| Enum Item | Description |
| :-- | :-- |
| AUDIOSTREAM\_EVENT\_ROUTING\_CHANGED = 0 | The audio route has been changed. |

#### \[h2\]OH\_AudioInterrupt\_ForceType

enum OH\_AudioInterrupt\_ForceType

**Description**

Enumerates the types of force that causes audio interruption.

The force type is obtained when an audio interruption event is received.

This type specifies whether the audio interruption operation is forcibly performed by the system. The operation information (such as audio pause or stop) can be obtained through [OH\_AudioInterrupt\_Hint](#oh_audiointerrupt_hint).

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| AUDIOSTREAM\_INTERRUPT\_FORCE = 0 | The operation is forcibly performed by the system. |
| AUDIOSTREAM\_INTERRUPT\_SHARE = 1 | The operation will not be performed by the system. [OH\_AudioInterrupt\_Hint](#oh_audiointerrupt_hint) is used to provide recommended operations for the application, and the application can determine the next processing mode. |

#### \[h2\]OH\_AudioInterrupt\_Hint

enum OH\_AudioInterrupt\_Hint

**Description**

Enumerates the hints provided along with audio interruption.

The force type is obtained when an audio interruption event is received.

The hint specifies the operation (such as audio pause or volume adjustment) to be performed on audio streams based on the focus strategy.

You can determine whether the operation is forcibly performed by the system based on [OH\_AudioInterrupt\_ForceType](#oh_audiointerrupt_forcetype).

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| AUDIOSTREAM\_INTERRUPT\_HINT\_NONE = 0 | None. |
| AUDIOSTREAM\_INTERRUPT\_HINT\_RESUME = 1 | 
A hint is displayed, indicating that the audio stream is restored. The application can proactively trigger operations related to rendering or recording.

This operation cannot be forcibly performed by the system, and the corresponding [OH\_AudioInterrupt\_ForceType](#oh_audiointerrupt_forcetype) must be **AUDIOSTREAM\_INTERRUPT\_SHARE**.

 |
| AUDIOSTREAM\_INTERRUPT\_HINT\_PAUSE = 2 | 

A hint is displayed, indicating that the audio stream is paused and the audio focus is lost temporarily.

The **AUDIOSTREAM\_INTERRUPT\_HINT\_RESUME** event will be triggered when the focus is gained.

 |
| AUDIOSTREAM\_INTERRUPT\_HINT\_STOP = 3 | A hint is displayed, indicating that the audio stream stops and the audio focus is lost. |
| AUDIOSTREAM\_INTERRUPT\_HINT\_DUCK = 4 | A hint is displayed, indicating that audio ducking starts and the audio is played at a lower volume. |
| AUDIOSTREAM\_INTERRUPT\_HINT\_UNDUCK = 5 | A hint is displayed, indicating that audio ducking ends and the audio is played at the normal volume. |
| AUDIOSTREAM\_INTERRUPT\_HINT\_MUTE = 6 | 

A hint is displayed, indicating that the audio is muted.

**Since**: 20

 |
| AUDIOSTREAM\_INTERRUPT\_HINT\_UNMUTE = 7 | 

A hint is displayed, indicating that the audio is unmuted.

**Since**: 20

 |

#### \[h2\]OH\_AudioInterrupt\_Mode

enum OH\_AudioInterrupt\_Mode

**Description**

Enumerates the audio interruption modes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| AUDIOSTREAM\_INTERRUPT\_MODE\_SHARE = 0 | Shared mode. |
| AUDIOSTREAM\_INTERRUPT\_MODE\_INDEPENDENT = 1 | Independent mode. |

#### \[h2\]OH\_AudioStream\_AudioEffectMode

enum OH\_AudioStream\_AudioEffectMode

**Description**

Enumerates the audio effect modes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| EFFECT\_NONE = 0 | No audio effect used. |
| EFFECT\_DEFAULT = 1 | Default audio effect mode. |

#### \[h2\]OH\_AudioStream\_FastStatus

enum OH\_AudioStream\_FastStatus

**Description**

Enumerates the low-latency statuses.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| AUDIOSTREAM\_FASTSTATUS\_NORMAL = 0 | Normal audio stream status. |
| AUDIOSTREAM\_FASTSTATUS\_FAST = 1 | Low-latency audio stream status. |

#### \[h2\]OH\_AudioStream\_DeviceChangeReason

enum OH\_AudioStream\_DeviceChangeReason

**Description**

Enumerates the reasons for audio stream device changes.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| REASON\_UNKNOWN = 0 | Unknown reason. |
| REASON\_NEW\_DEVICE\_AVAILABLE = 1 | A new device is available. |
| REASON\_OLD\_DEVICE\_UNAVAILABLE = 2 | The old device is unavailable. When this reason is reported, the application should consider pausing audio playback. |
| REASON\_OVERRODE = 3 | The user or system forcibly changes the device. |
| REASON\_SESSION\_ACTIVATED = 4 | 
The audio session has been activated.

**Since**: 20

 |
| REASON\_STREAM\_PRIORITY\_CHANGED = 5 | 

An audio stream with higher priority appears.

**Since**: 20

 |

#### \[h2\]OH\_AudioStream\_PrivacyType

enum OH\_AudioStream\_PrivacyType

**Description**

Enumerates the privacy types of an audio stream. The privacy type specifies whether the audio stream can be recorded by other applications.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| AUDIO\_STREAM\_PRIVACY\_TYPE\_PUBLIC = 0 | The audio stream can be recorded or screen-projected by other applications and is not privacy-related. |
| AUDIO\_STREAM\_PRIVACY\_TYPE\_PRIVATE = 1 | The audio stream cannot be recorded or screen-projected by other applications. |
| AUDIO\_STREAM\_PRIVACY\_TYPE\_SHARED = 2 | 
The audio stream can be recorded or screen-projected by other applications and is privacy-related.

For example, if the privacy policy is **PRIVACY\_TYPE\_PUBLIC**, audio streams of the [AUDIOSTREAM\_USAGE\_VOICE\_COMMUNICATION](#oh_audiostream_usage) type cannot be recorded or screen-projected by other applications. However, if the privacy policy is **PRIVACY\_TYPE\_SHARED**, these audio streams can be recorded or screen-projected by other applications.

**Since**: 21

 |

#### \[h2\]OH\_AudioData\_Callback\_Result

enum OH\_AudioData\_Callback\_Result

**Description**

Enumerates the audio data callback results.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| AUDIO\_DATA\_CALLBACK\_RESULT\_INVALID = -1 | The audio data callback result is invalid, and the audio data will not be played. |
| AUDIO\_DATA\_CALLBACK\_RESULT\_VALID = 0 | The audio data callback result is valid, and the audio data will be played. |

#### Function Description

#### \[h2\]OH\_AudioRenderer\_OutputDeviceChangeCallback()

typedef void (\*OH\_AudioRenderer\_OutputDeviceChangeCallback)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioStream\_DeviceChangeReason reason)

**Description**

Defines a pointer to the callback invoked when the audio capturer device changes.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| void\* userData | Pointer to the application data passed through the callback. |
| [OH\_AudioStream\_DeviceChangeReason](#oh_audiostream_devicechangereason) reason | Enumerates the reasons for audio stream device changes. |

#### \[h2\]OH\_AudioRenderer\_OnMarkReachedCallback()

typedef void (\*OH\_AudioRenderer\_OnMarkReachedCallback)(OH\_AudioRenderer\* renderer, uint32\_t samplePos, void\* userData)

**Description**

Defines a pointer to the callback invoked when the mark position is reached.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| uint32\_t samplePos | Mark position. |
| void\* userData | Pointer to the application data passed through the callback. |

#### \[h2\]OH\_AudioRenderer\_WriteDataWithMetadataCallback()

typedef int32\_t (\*OH\_AudioRenderer\_WriteDataWithMetadataCallback)(OH\_AudioRenderer\* renderer, void\* userData, void\* audioData, int32\_t audioDataSize, void\* metadata, int32\_t metadataSize)

**Description**

Defines a function pointer to the callback used to write audio data and metadata.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| void\* userData | Pointer to the application data passed through the callback. |
| void\* audioData | Pointer to the audio data written by the user. |
| int32\_t audioDataSize | Length of the audio data, in bytes. |
| void\* metadata | Pointer to the metadata written by the user. |
| int32\_t metadataSize | Length of the metadata, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Error code of the callback. |

#### \[h2\]OH\_AudioRenderer\_OnWriteDataCallback()

typedef OH\_AudioData\_Callback\_Result (\*OH\_AudioRenderer\_OnWriteDataCallback)(OH\_AudioRenderer\* renderer, void\* userData, void\* audioData, int32\_t audioDataSize)

**Description**

Defines a function pointer to the callback used to write audio data.

The callback is used only to write audio data. Do not call AudioRenderer APIs in it.

The return result indicates whether the data filled in the buffer is valid. If the data is invalid, the data entered by the user will not be played.

Once the callback finishes its execution, the audio service queues the data pointed to by **audioData** for playback. Therefore, do not change the data outside the callback. It is crucial to fill **audioData** with the exact length (specified by **audioDataSize**) of data designated for playback; otherwise, noises may occur during playback.

The **audioDataSize** parameter can be set by calling [OH\_AudioStreamBuilder\_SetFrameSizeInCallback](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_setframesizeincallback).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| void\* userData | Pointer to the application data passed through the callback. |
| void\* audioData | Pointer to the audio data written by the user. |
| int32\_t audioDataSize | Length of the audio data, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioData\_Callback\_Result](#oh_audiodata_callback_result) | 
**AUDIO\_DATA\_CALLBACK\_RESULT\_INVALID**: The audio data callback result is invalid, and the audio data will not be played.

**AUDIO\_DATA\_CALLBACK\_RESULT\_VALID**: The audio data callback result is valid, and the audio data will be played.

 |
