# avrecorder\_base.h

#### Overview

The file declares the struct and enums used by the AVRecorder.

**File to include**: <multimedia/player\_framework/avrecorder\_base.h>

**Library**: libavrecorder.so

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Related module**: [AVRecorder](../../modules/avrecorder/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVRecorder\_Profile](../../structs/oh-avrecorder-profile/document.md) | OH\_AVRecorder\_Profile | Describes the parameters used for audio and video recording. |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) | OH\_AVRecorder | Describes an initialized AVRecorder. |
| [OH\_AVRecorder\_Location](../../structs/oh-avrecorder-location/document.md) | OH\_AVRecorder\_Location | Describes the geographical location information about a media asset. |
| [OH\_AVRecorder\_MetadataTemplate](../../structs/oh-avrecorder-metadatatemplate/document.md) | OH\_AVRecorder\_MetadataTemplate | Describes the basic template of metadata. |
| [OH\_AVRecorder\_Metadata](../../structs/oh-avrecorder-metadata/document.md) | OH\_AVRecorder\_Metadata | Describes the metadata. |
| [OH\_AVRecorder\_Config](../../structs/oh-avrecorder-config/document.md) | OH\_AVRecorder\_Config | Describes the AVRecorder configuration. |
| [OH\_AVRecorder\_Range](../../structs/oh-avrecorder-range/document.md) | OH\_AVRecorder\_Range | Describes the range. |
| [OH\_AVRecorder\_EncoderInfo](../../structs/oh-avrecorder-encoderinfo/document.md) | OH\_AVRecorder\_EncoderInfo | Describes the encoder information. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVRecorder\_AudioSourceType](#oh_avrecorder_audiosourcetype) | OH\_AVRecorder\_AudioSourceType | Enumerates the audio source types of the AVRecorder. |
| [OH\_AVRecorder\_VideoSourceType](#oh_avrecorder_videosourcetype) | OH\_AVRecorder\_VideoSourceType | Enumerates the video source types of the AVRecorder. |
| [OH\_AVRecorder\_CodecMimeType](#oh_avrecorder_codecmimetype) | OH\_AVRecorder\_CodecMimeType | Enumerates the MIME types of the encoder. |
| [OH\_AVRecorder\_ContainerFormatType](#oh_avrecorder_containerformattype) | OH\_AVRecorder\_ContainerFormatType | Enumerates the Container Format Types (CFTs). |
| [OH\_AVRecorder\_State](#oh_avrecorder_state) | OH\_AVRecorder\_State | Enumerates the AVRecorder states. |
| [OH\_AVRecorder\_StateChangeReason](#oh_avrecorder_statechangereason) | OH\_AVRecorder\_StateChangeReason | Enumerates the reasons for AVRecorder state changes. |
| [OH\_AVRecorder\_FileGenerationMode](#oh_avrecorder_filegenerationmode) | OH\_AVRecorder\_FileGenerationMode | Enumerates the modes available for creating a recording file. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_AVRecorder\_OnStateChange)(OH\_AVRecorder \*recorder, OH\_AVRecorder\_State state, OH\_AVRecorder\_StateChangeReason reason, void \*userData)](#oh_avrecorder_onstatechange) | OH\_AVRecorder\_OnStateChange | Called when the AVRecorder state changes. |
| [typedef void (\*OH\_AVRecorder\_OnError)(OH\_AVRecorder \*recorder, int32\_t errorCode, const char \*errorMsg, void \*userData)](#oh_avrecorder_onerror) | OH\_AVRecorder\_OnError | Called when an error occurs during recording. |
| [typedef void (\*OH\_AVRecorder\_OnUri)(OH\_AVRecorder \*recorder, OH\_MediaAsset \*asset, void \*userData)](#oh_avrecorder_onuri) | OH\_AVRecorder\_OnUri | Called when the recording is in [OH\_AVRecorder\_FileGenerationMode](#oh_avrecorder_filegenerationmode).AVRECORDER\_AUTO\_CREATE\_CAMERA\_SCENE mode. |

#### Enum Description

#### \[h2\]OH\_AVRecorder\_AudioSourceType

enum OH\_AVRecorder\_AudioSourceType

**Description**

Enumerates the audio source types of the AVRecorder.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| AVRECORDER\_DEFAULT = 0 | Default audio source. |
| AVRECORDER\_MIC = 1 | Microphone audio source. |
| AVRECORDER\_VOICE\_RECOGNITION = 2 | Audio source in speech recognition scenarios. |
| AVRECORDER\_VOICE\_COMMUNICATION = 7 | Voice communication source. |
| AVRECORDER\_VOICE\_MESSAGE = 10 | Voice message source. |
| AVRECORDER\_CAMCORDER = 13 | Audio source in camera recording scenarios. |

#### \[h2\]OH\_AVRecorder\_VideoSourceType

enum OH\_AVRecorder\_VideoSourceType

**Description**

Enumerates the video source types of the AVRecorder.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| AVRECORDER\_SURFACE\_YUV = 0 | Raw data surface. |
| AVRECORDER\_SURFACE\_ES = 1 | ES data surface. |

#### \[h2\]OH\_AVRecorder\_CodecMimeType

enum OH\_AVRecorder\_CodecMimeType

**Description**

Enumerates the MIME types of the encoder.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| AVRECORDER\_VIDEO\_AVC = 2 | MIME type of the H.264 encoder. |
| AVRECORDER\_AUDIO\_AAC = 3 | MIME type of the AAC encoder. |
| AVRECORDER\_AUDIO\_MP3 = 4 | MIME type of the MP3 encoder. |
| AVRECORDER\_AUDIO\_G711MU = 5 | MIME type of the G711-mulaw encoder. |
| AVRECORDER\_VIDEO\_MPEG4 = 6 | MIME type of the MPEG4 encoder. |
| AVRECORDER\_VIDEO\_HEVC = 8 | MIME type of the H.265 encoder. |
| AVRECORDER\_AUDIO\_AMR\_NB = 9 | MIME type of the AMR-NB codec. |
| AVRECORDER\_AUDIO\_AMR\_WB = 10 | MIME type of the AMR-WB codec. |

#### \[h2\]OH\_AVRecorder\_ContainerFormatType

enum OH\_AVRecorder\_ContainerFormatType

**Description**

Enumerates the Container Format Types (CFTs).

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| AVRECORDER\_CFT\_MPEG\_4 = 2 | Video container format mp4. |
| AVRECORDER\_CFT\_MPEG\_4A = 6 | Audio container format m4a. |
| AVRECORDER\_CFT\_AMR = 8 | Audio container format amr. |
| AVRECORDER\_CFT\_MP3 = 9 | Audio container format mp3. |
| AVRECORDER\_CFT\_WAV = 10 | Audio container format wav. |
| AVRECORDER\_CFT\_AAC = 11 | 
Audio container format aac (with ADTS header).

**Since**: 20

 |

#### \[h2\]OH\_AVRecorder\_State

enum OH\_AVRecorder\_State

**Description**

Enumerates the AVRecorder states.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| AVRECORDER\_IDLE = 0 | Idle. In this state, you can call [OH\_AVRecorder\_Prepare](../avrecorder-h/document.md#oh_avrecorder_prepare) to set recording parameters, and the AVRecorder transitions to the AVRECORDER\_PREPARED state. |
| AVRECORDER\_PREPARED = 1 | Prepared. After the parameters are set, you can call [OH\_AVRecorder\_Start](../avrecorder-h/document.md#oh_avrecorder_start) to start recording, and the AVRecorder transitions to the AVRECORDER\_STARTED state. |
| AVRECORDER\_STARTED = 2 | 
Started. Recording is in progress. In this case, you can call [OH\_AVRecorder\_Pause](../avrecorder-h/document.md#oh_avrecorder_pause) to pause recording, and the AVRecorder transitions to the AVRECORDER\_PAUSED state.

You can also call [OH\_AVRecorder\_Stop](../avrecorder-h/document.md#oh_avrecorder_stop) to stop recording, and the AVRecorder transitions to the AVRECORDER\_STOPPED state.

 |
| AVRECORDER\_PAUSED = 3 | 

Paused. In this state, you can call [OH\_AVRecorder\_Resume](../avrecorder-h/document.md#oh_avrecorder_resume) to resume recording, and the AVRecorder transitions to the AVRECORDER\_STARTED state.

You can also call [OH\_AVRecorder\_Stop](../avrecorder-h/document.md#oh_avrecorder_stop) to stop recording, and the AVRecorder transitions to the AVRECORDER\_STOPPED state.

 |
| AVRECORDER\_STOPPED = 4 | Stopped. In this state, you can call [OH\_AVRecorder\_Prepare](../avrecorder-h/document.md#oh_avrecorder_prepare) to set recording parameters, and the AVRecorder transitions to the AVRECORDER\_PREPARED state again. |
| AVRECORDER\_RELEASED = 5 | Released. The recording resources are released. No operation can be performed at this time. In any other state, you can call [OH\_AVRecorder\_Release](../avrecorder-h/document.md#oh_avrecorder_release) to transition to the AVRECORDER\_RELEASED state. |
| AVRECORDER\_ERROR = 6 | 

Error state. The AVRecorder transitions to this state when an irreversible error occurs in the instance.

In this state, the [OH\_AVRecorder\_OnError](#oh_avrecorder_onerror) event is reported, with the detailed error cause.

You should call [OH\_AVRecorder\_Reset](../avrecorder-h/document.md#oh_avrecorder_reset) to reset the AVRecorder instance or call [OH\_AVRecorder\_Release](../avrecorder-h/document.md#oh_avrecorder_release) to release resources.

 |

#### \[h2\]OH\_AVRecorder\_StateChangeReason

enum OH\_AVRecorder\_StateChangeReason

**Description**

Enumerates the reasons for AVRecorder state changes.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| AVRECORDER\_USER = 0 | The state change is caused by user operations. |
| AVRECORDER\_BACKGROUND = 1 | The state change is caused by background operations. |

#### \[h2\]OH\_AVRecorder\_FileGenerationMode

enum OH\_AVRecorder\_FileGenerationMode

**Description**

Enumerates the modes available for creating a recording file.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| AVRECORDER\_APP\_CREATE = 0 | The application creates a media file in the sandbox. |
| AVRECORDER\_AUTO\_CREATE\_CAMERA\_SCENE = 1 | The system creates a media file. This value is valid only in camera recording scenarios. |

#### Function Description

#### \[h2\]OH\_AVRecorder\_OnStateChange()

typedef void (\*OH\_AVRecorder\_OnStateChange)(OH\_AVRecorder \*recorder,OH\_AVRecorder\_State state, OH\_AVRecorder\_StateChangeReason reason, void \*userData)

**Description**

Called when the AVRecorder state changes.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |
| [OH\_AVRecorder\_State](#oh_avrecorder_state) state | AVRecorder state. |
| [OH\_AVRecorder\_StateChangeReason](#oh_avrecorder_statechangereason) reason | Reason for the AVRecorder state change. |
| void \*userData | Pointer to user-defined data. |

#### \[h2\]OH\_AVRecorder\_OnError()

typedef void (\*OH\_AVRecorder\_OnError)(OH\_AVRecorder \*recorder, int32\_t errorCode, const char \*errorMsg,void \*userData)

**Description**

Called when an error occurs during recording.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |
| int32\_t errorCode | Error code. For details, see [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode). |
| const char \*errorMsg | Pointer to the error message. |
| void \*userData | Pointer to user-defined data. |

#### \[h2\]OH\_AVRecorder\_OnUri()

typedef void (\*OH\_AVRecorder\_OnUri)(OH\_AVRecorder \*recorder, OH\_MediaAsset \*asset, void \*userData)

**Description**

Called when the recording is in [OH\_AVRecorder\_FileGenerationMode](#oh_avrecorder_filegenerationmode).AVRECORDER\_AUTO\_CREATE\_CAMERA\_SCENE mode.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |
| [OH\_MediaAsset](../../../../media-library-kit/c-apis/structs/oh-mediaasset/document.md) \*asset | Pointer to the OH\_MediaAsset instance. |
| void \*userData | Pointer to user-defined data. |
