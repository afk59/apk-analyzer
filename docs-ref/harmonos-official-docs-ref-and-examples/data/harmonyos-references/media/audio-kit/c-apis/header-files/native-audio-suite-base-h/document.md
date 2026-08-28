# native\_audio\_suite\_base.h

#### Overview

The file declares the basic data structs used in audio creation.

**File to include**: <ohaudiosuite/native\_audio\_suite\_base.h>

**Library**: libohaudiosuite.so

**System capability**: SystemCapability.Multimedia.Audio.SuiteEngine

**Since**: 22

**Related module**: [OHAudioSuite](../../modules/ohaudiosuite/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioFormat](../../structs/oh-audioformat/document.md) | OH\_AudioFormat | Describes the audio stream information, which is used to describe the basic audio format, required for audio creation. |
| [OH\_AudioDataArray](../../structs/oh-audiodataarray/document.md) | OH\_AudioDataArray | Describes the input data for the multi-output rendering interface. It is used to obtain processed audio data when multiple output effect nodes are present in the pipeline. |
| [OH\_EqualizerFrequencyBandGains](../../structs/oh-equalizerfrequencybandgains/document.md) | OH\_EqualizerFrequencyBandGains | Describes the configuration parameters for the equalizer effect node used in audio creation. |
| [OH\_AudioSuiteEngineStruct](../../structs/oh-audiosuiteenginestruct/document.md) | OH\_AudioSuiteEngine | Describes the audio creation engine, which is used to manage audio creation pipelines. |
| [OH\_AudioSuitePipelineStruct](../../structs/oh-audiosuitepipelinestruct/document.md) | OH\_AudioSuitePipeline | Describes the audio creation pipeline, which is used to manage audio creation nodes. |
| [OH\_AudioNodeStruct](../../structs/oh-audionodestruct/document.md) | OH\_AudioNode | Describes a node for audio creation, which is used to represent instances of audio creation nodes. |
| [OH\_AudioNodeBuilderStruct](../../structs/oh-audionodebuilderstruct/document.md) | OH\_AudioNodeBuilder | Describes a builder for nodes used in audio creation. It allows you to create an [OH\_AudioNode](../../structs/oh-audionodestruct/document.md) object, define the data formats for input and output nodes, and configures the callback interface for input nodes. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioNode\_Type](#oh_audionode_type) | OH\_AudioNode\_Type | Enumerates the types of audio creation nodes. |
| [OH\_AudioSuite\_PipelineWorkMode](#oh_audiosuite_pipelineworkmode) | OH\_AudioSuite\_PipelineWorkMode | Enumerates the working modes of the audio creation pipeline. |
| [OH\_AudioSuite\_PipelineState](#oh_audiosuite_pipelinestate) | OH\_AudioSuite\_PipelineState | Enumerates the operational states of the audio creation pipeline. |
| [OH\_AudioSuite\_Result](#oh_audiosuite_result) | OH\_AudioSuite\_Result | Enumerates the error codes for audio creation. |
| [OH\_Audio\_SampleFormat](#oh_audio_sampleformat) | OH\_Audio\_SampleFormat | Enumerates the bit depth of audio streams in an audio creation node. |
| [OH\_Audio\_EncodingType](#oh_audio_encodingtype) | OH\_Audio\_EncodingType | Enumerates the encoding types of audio streams. |
| [OH\_Audio\_SampleRate](#oh_audio_samplerate) | OH\_Audio\_SampleRate | Enumerates the sample rates of audio streams. |
| [OH\_SoundFieldType](#oh_soundfieldtype) | OH\_SoundFieldType | Enumerates the effect modes of sound field effect nodes used for audio creation. |
| [OH\_EnvironmentType](#oh_environmenttype) | OH\_EnvironmentType | Enumerates the types of environment effect nodes used for audio creation. |
| [OH\_VoiceBeautifierType](#oh_voicebeautifiertype) | OH\_VoiceBeautifierType | Enumerates the types of voice beautifier effect nodes used for audio creation. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| EQUALIZER\_BAND\_NUM (10) | 
Number of equalizer bands, defined as 10.

**Since**: 22

 |

#### \[h2\]Variables

| Name | Description |
| :-- | :-- |
| const [OH\_EqualizerFrequencyBandGains](../../structs/oh-equalizerfrequencybandgains/document.md) OH\_EQUALIZER\_PARAM\_DEFAULT | 
Default equalizer band gain settings.

Band gains: {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}.

**Since**: 22

 |
| const [OH\_EqualizerFrequencyBandGains](../../structs/oh-equalizerfrequencybandgains/document.md) OH\_EQUALIZER\_PARAM\_BALLADS | 

Built-in ballad effect for the equalizer node.

Band gains: {3, 5, 2, -4, 1, 2, -3, 1, 4, 5}.

**Since**: 22

 |
| const [OH\_EqualizerFrequencyBandGains](../../structs/oh-equalizerfrequencybandgains/document.md) OH\_EQUALIZER\_PARAM\_CHINESE\_STYLE | 

Built-in Chinese style effect for the equalizer node.

Band gains: {0, 0, 2, 0, 0, 4, 4, 2, 2, 5}.

**Since**: 22

 |
| const [OH\_EqualizerFrequencyBandGains](../../structs/oh-equalizerfrequencybandgains/document.md) OH\_EQUALIZER\_PARAM\_CLASSICAL | 

Built-in classical effect for the equalizer node.

Band gains: {2, 3, 2, 1, 0, 0, -5, -5, -5, -6}.

**Since**: 22

 |
| const [OH\_EqualizerFrequencyBandGains](../../structs/oh-equalizerfrequencybandgains/document.md) OH\_EQUALIZER\_PARAM\_DANCE\_MUSIC | 

Built-in dance music effect for the equalizer node.

Band gains: {4, 3, 2, -3, 0, 0, 5, 4, 2, 0}.

**Since**: 22

 |
| const [OH\_EqualizerFrequencyBandGains](../../structs/oh-equalizerfrequencybandgains/document.md) OH\_EQUALIZER\_PARAM\_JAZZ | 

Built-in jazz effect for the equalizer node.

Band gains: {2, 0, 2, 3, 6, 5, -1, 3, 4, 4}.

**Since**: 22

 |
| const [OH\_EqualizerFrequencyBandGains](../../structs/oh-equalizerfrequencybandgains/document.md) OH\_EQUALIZER\_PARAM\_POP | 

Built-in pop effect for the equalizer node.

Band gains: {5, 2, 1, -1, -5, -5, -2, 1, 2, 4}.

**Since**: 22

 |
| const [OH\_EqualizerFrequencyBandGains](../../structs/oh-equalizerfrequencybandgains/document.md) OH\_EQUALIZER\_PARAM\_RB | 

Built-in R&B effect for the equalizer node.

Band gains: {1, 4, 5, 3, -2, -2, 2, 3, 5, 5}.

**Since**: 22

 |
| const [OH\_EqualizerFrequencyBandGains](../../structs/oh-equalizerfrequencybandgains/document.md) OH\_EQUALIZER\_PARAM\_ROCK | 

Built-in rock effect for the equalizer node.

Band gains: {6, 4, 4, 2, 0, 1, 3, 3, 5, 4}.

**Since**: 22

 |

#### Enum Description

#### \[h2\]OH\_AudioNode\_Type

enum OH\_AudioNode\_Type

**Description**

Enumerates the types of audio creation nodes.

**Since**: 22

| Value | Description |
| :-- | :-- |
| INPUT\_NODE\_TYPE\_DEFAULT = 1 | Input node that supports obtaining audio data from applications. |
| OUTPUT\_NODE\_TYPE\_DEFAULT = 101 | Output node that supports providing audio data to applications. |
| EFFECT\_NODE\_TYPE\_EQUALIZER = 201 | 
Equalizer effect node. The output audio format of the equalizer effect node is as follows:

Sample rate: 48000 Hz

Sample format: [OH\_Audio\_SampleFormat](#oh_audio_sampleformat).AUDIO\_SAMPLE\_S16LE

Channel count: 2

 |
| EFFECT\_NODE\_TYPE\_NOISE\_REDUCTION = 202 | 

Noise reduction effect node. The output audio format of the noise reduction effect node is as follows:

Sample rate: 16000 Hz

Sample format: [OH\_Audio\_SampleFormat](#oh_audio_sampleformat).AUDIO\_SAMPLE\_S16LE

Channel count: 1

 |
| EFFECT\_NODE\_TYPE\_SOUND\_FIELD = 203 | 

Sound field effect node. The sound field effect node supports the sound field types enumerated in [OH\_SoundFieldType](#oh_soundfieldtype).

The output audio format of the sound field effect node is as follows:

Sample rate: 48000 Hz

Sample format: [OH\_Audio\_SampleFormat](#oh_audio_sampleformat).AUDIO\_SAMPLE\_S16LE

Channel count: 2

 |
| EFFECT\_MULTII\_OUTPUT\_NODE\_TYPE\_AUDIO\_SEPARATION = 204 | 

Source separation effect node. The source separation effect node can only be connected to an output node.

The output audio format of the source separation effect node is as follows:

Sample rate: 48000 Hz

Sample format: [OH\_Audio\_SampleFormat](#oh_audio_sampleformat).AUDIO\_SAMPLE\_F32LE

Channel count: 4 (first 2 channels for vocals, last 2 for accompaniment)

 |
| EFFECT\_NODE\_TYPE\_VOICE\_BEAUTIFIER = 205 | 

Voice beautification effect node. The voice beautification effect node supports the voice beautification types enumerated in [OH\_VoiceBeautifierType](#oh_voicebeautifiertype).

The output audio format of the voice beautification effect node is as follows:

Sample rate: 48000 Hz

Sample format: [OH\_Audio\_SampleFormat](#oh_audio_sampleformat).AUDIO\_SAMPLE\_S16LE

Channel count: 2

 |
| EFFECT\_NODE\_TYPE\_ENVIRONMENT\_EFFECT = 206 | 

Environment effect node. The output audio format of the environment effect node is as follows:

Sample rate: 48000 Hz

Sample format: [OH\_Audio\_SampleFormat](#oh_audio_sampleformat).AUDIO\_SAMPLE\_S16LE

Channel count: 2

 |
| EFFECT\_NODE\_TYPE\_AUDIO\_MIXER = 207 | 

Audio mixer effect node. The output audio format of the audio mixer effect node is as follows:

Sample rate: [OH\_Audio\_SampleRate](#oh_audio_samplerate)

Sample format: [OH\_Audio\_SampleFormat](#oh_audio_sampleformat).AUDIO\_SAMPLE\_F32LE

Channel count: 2

 |

#### \[h2\]OH\_AudioSuite\_PipelineWorkMode

enum OH\_AudioSuite\_PipelineWorkMode

**Description**

Enumerates the working modes of the audio creation pipeline.

**Since**: 22

| Value | Description |
| :-- | :-- |
| AUDIOSUITE\_PIPELINE\_EDIT\_MODE = 1 | Edit mode. In this mode, the pipeline can create various effect nodes for audio processing. |
| AUDIOSUITE\_PIPELINE\_REALTIME\_MODE = 2 | 
Real-time rendering mode. In this mode, processed audio is played in real time during audio processing.

Only equalizer effect processing is supported in this mode.

 |

#### \[h2\]OH\_AudioSuite\_PipelineState

enum OH\_AudioSuite\_PipelineState

**Description**

Enumerates the operational states of the audio creation pipeline.

**Since**: 22

| Value | Description |
| :-- | :-- |
| AUDIOSUITE\_PIPELINE\_STOPPED = 1 | The pipeline is stopped. |
| AUDIOSUITE\_PIPELINE\_RUNNING = 2 | The pipeline is running. |

#### \[h2\]OH\_AudioSuite\_Result

enum OH\_AudioSuite\_Result

**Description**

Enumerates the error codes for audio creation.

**Since**: 22

| Value | Description |
| :-- | :-- |
| AUDIOSUITE\_SUCCESS = 0 | The call is successful. |
| AUDIOSUITE\_ERROR\_INVALID\_PARAM = 1 | Invalid input parameters. |
| AUDIOSUITE\_ERROR\_INVALID\_STATE = 2 | Invalid state. |
| AUDIOSUITE\_ERROR\_SYSTEM = 3 | General system error. |
| AUDIOSUITE\_ERROR\_UNSUPPORTED\_FORMAT = 4 | Unsupported audio format, such as unsupported encoding type or sample format. |
| AUDIOSUITE\_ERROR\_ENGINE\_NOT\_EXIST = 5 | The engine does not exist. |
| AUDIOSUITE\_ERROR\_PIPELINE\_NOT\_EXIST = 6 | The pipeline does not exist. |
| AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST = 7 | The node does not exist. |
| AUDIOSUITE\_ERROR\_UNSUPPORTED\_CONNECT = 8 | Nodes do not support connection. |
| AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION = 9 | Unsupported operation. For example, the audio format cannot be set for effect nodes. |
| AUDIOSUITE\_ERROR\_CREATED\_EXCEED\_SYSTEM\_LIMITS = 10 | 
The number of pipelines or nodes created reaches the upper limit. Specifically:

An engine supports the creation of up to 10 pipelines, with a maximum of 1 dedicated to real-time rendering. Each pipeline can have up to 5 input nodes, 1 output node, 3 mixer nodes, 1 audio separation node, and up to 5 other effect nodes.

 |
| AUDIOSUITE\_ERROR\_REQUIRED\_PARAMETERS\_MISSING = 11 | Mandatory parameters are missing. For example, the callback function is not set for the input node, or the audio format is not set for the output node. |
| AUDIOSUITE\_ERROR\_TIMEOUT = 12 | Operation timed out. |
| AUDIOSUITE\_ERROR\_MEMORY\_ALLOC\_FAILED = 13 | Memory allocation failed. |

#### \[h2\]OH\_Audio\_SampleFormat

enum OH\_Audio\_SampleFormat

**Description**

Enumerates the bit depth of audio streams in an audio creation node.

**Since**: 22

| Value | Description |
| :-- | :-- |
| AUDIO\_SAMPLE\_U8 = 0 | Unsigned 8-bit. |
| AUDIO\_SAMPLE\_S16LE = 1 | Short 16-bit little-endian. |
| AUDIO\_SAMPLE\_S24LE = 2 | Short 24-bit little-endian. |
| AUDIO\_SAMPLE\_S32LE = 3 | Short 32-bit little-endian. |
| AUDIO\_SAMPLE\_F32LE = 4 | Float 32-bit little-endian. |

#### \[h2\]OH\_Audio\_EncodingType

enum OH\_Audio\_EncodingType

**Description**

Enumerates the encoding types of audio streams.

**Since**: 22

| Value | Description |
| :-- | :-- |
| AUDIO\_ENCODING\_TYPE\_RAW = 0 | PCM encoding. |

#### \[h2\]OH\_Audio\_SampleRate

enum OH\_Audio\_SampleRate

**Description**

Enumerates the sample rates of audio streams.

**Since**: 22

| Value | Description |
| :-- | :-- |
| SAMPLE\_RATE\_8000 = 8000 | Sample rate of 8 kHz. |
| SAMPLE\_RATE\_11025 = 11025 | Sample rate of 11.025 kHz. |
| SAMPLE\_RATE\_12000 = 12000 | Sample rate of 12 kHz. |
| SAMPLE\_RATE\_16000 = 16000 | Sample rate of 16 kHz. |
| SAMPLE\_RATE\_22050 = 22050 | Sample rate of 22.05 kHz. |
| SAMPLE\_RATE\_24000 = 24000 | Sample rate of 24 kHz. |
| SAMPLE\_RATE\_32000 = 32000 | Sample rate of 32 kHz. |
| SAMPLE\_RATE\_44100 = 44100 | Sample rate 44.1 kHz. |
| SAMPLE\_RATE\_48000 = 48000 | Sample rate of 48 kHz. |
| SAMPLE\_RATE\_64000 = 64000 | Sample rate of 64 kHz. |
| SAMPLE\_RATE\_88200 = 88200 | Sample rate of 88.2 kHz. |
| SAMPLE\_RATE\_96000 = 96000 | Sample rate of 96 kHz. |
| SAMPLE\_RATE\_176400 = 176400 | Sample rate of 176.4 kHz. |
| SAMPLE\_RATE\_192000 = 192000 | Sample rate of 192 kHz. |

#### \[h2\]OH\_SoundFieldType

enum OH\_SoundFieldType

**Description**

Enumerates the effect modes of sound field effect nodes used for audio creation.

**Since**: 22

| Value | Description |
| :-- | :-- |
| SOUND\_FIELD\_FRONT\_FACING = 1 | Front-facing sound field effect. |
| SOUND\_FIELD\_GRAND = 2 | Grand sound field effect. |
| SOUND\_FIELD\_NEAR = 3 | Near-listening sound field effect. |
| SOUND\_FIELD\_WIDE = 4 | Wide sound field effect. |

#### \[h2\]OH\_EnvironmentType

enum OH\_EnvironmentType

**Description**

Enumerates the types of environment effect nodes used for audio creation.

**Since**: 22

| Value | Description |
| :-- | :-- |
| ENVIRONMENT\_TYPE\_BROADCAST = 1 | Broadcast environment effect. |
| ENVIRONMENT\_TYPE\_EARPIECE = 2 | Earpiece environment effect. |
| ENVIRONMENT\_TYPE\_UNDERWATER = 3 | Underwater environment effect. |
| ENVIRONMENT\_TYPE\_GRAMOPHONE = 4 | Gramophone environment effect. |

#### \[h2\]OH\_VoiceBeautifierType

enum OH\_VoiceBeautifierType

**Description**

Enumerates the types of voice beautifier effect nodes used for audio creation.

**Since**: 22

| Value | Description |
| :-- | :-- |
| VOICE\_BEAUTIFIER\_TYPE\_CLEAR = 1 | Clear voice beautifier effect. |
| VOICE\_BEAUTIFIER\_TYPE\_THEATRE = 2 | Theatre voice beautifier effect. |
| VOICE\_BEAUTIFIER\_TYPE\_CD = 3 | CD-quality voice beautifier effect. |
| VOICE\_BEAUTIFIER\_TYPE\_RECORDING\_STUDIO = 4 | Recording studio voice beautifier effect. |
