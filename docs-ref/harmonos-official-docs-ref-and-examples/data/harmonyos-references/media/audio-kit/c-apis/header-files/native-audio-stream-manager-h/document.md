# native\_audio\_stream\_manager.h

#### Overview

The file declares the functions related to an audio stream manager.

You can call the functions to create an audio stream manager and set and manage audio streams.

**File to include**: <ohaudio/native\_audio\_stream\_manager.h>

**Library**: libohaudio.so

**System capability**: SystemCapability.Multimedia.Audio.Core

**Since**: 19

**Related module**: [OHAudio](../../modules/ohaudio/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioStreamManager](../../structs/oh-audiostreammanager/document.md) | OH\_AudioStreamManager | Describes an audio stream manager, which is used for audio stream management. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result OH\_AudioManager\_GetAudioStreamManager(OH\_AudioStreamManager \*\*streamManager)](#oh_audiomanager_getaudiostreammanager) | Obtains the handle to the audio stream manager. |
| [OH\_AudioCommon\_Result OH\_AudioStreamManager\_GetDirectPlaybackSupport(OH\_AudioStreamManager \*audioStreamManager, OH\_AudioStreamInfo \*streamInfo, OH\_AudioStream\_Usage usage, OH\_AudioStream\_DirectPlaybackMode \*directPlaybackMode)](#oh_audiostreammanager_getdirectplaybacksupport) | Obtains the direct playback mode supported by an audio stream. |
| [OH\_AudioCommon\_Result OH\_AudioStreamManager\_IsAcousticEchoCancelerSupported(OH\_AudioStreamManager \*streamManager, OH\_AudioStream\_SourceType sourceType, bool \*supported)](#oh_audiostreammanager_isacousticechocancelersupported) | Checks whether the audio stream of the specified source type supports acoustic echo cancellation. |
| [bool OH\_AudioStreamManager\_IsFastPlaybackSupported(OH\_AudioStreamManager \*streamManager, OH\_AudioStreamInfo \*streamInfo, OH\_AudioStream\_Usage usage)](#oh_audiostreammanager_isfastplaybacksupported) | Checks whether the current device supports low-latency playback for the specified audio stream information and usage scenario. |
| [bool OH\_AudioStreamManager\_IsFastRecordingSupported(OH\_AudioStreamManager \*streamManager, OH\_AudioStreamInfo \*streamInfo, OH\_AudioStream\_SourceType source)](#oh_audiostreammanager_isfastrecordingsupported) | Checks whether the current device supports low-latency recording for the specified audio stream information and usage scenario. |
| [bool OH\_AudioStreamManager\_IsIntelligentNoiseReductionEnabledForCurrentDevice(OH\_AudioStreamManager \*streamManager, OH\_AudioStream\_SourceType source)](#oh_audiostreammanager_isintelligentnoisereductionenabledforcurrentdevice) | Checks whether the intelligent noise reduction feature is enabled for the audio stream of the specified source type. |

#### Function Description

#### \[h2\]OH\_AudioManager\_GetAudioStreamManager()

OH\_AudioCommon\_Result OH\_AudioManager\_GetAudioStreamManager(OH\_AudioStreamManager \*\*streamManager)

**Description**

Obtains the handle to the audio stream manager.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamManager](../../structs/oh-audiostreammanager/document.md) \*\*streamManager | Double pointer to the audio stream manager. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS = 0**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM = 6800301**: The system status is incorrect.

 |

#### \[h2\]OH\_AudioStreamManager\_GetDirectPlaybackSupport()

OH\_AudioCommon\_Result OH\_AudioStreamManager\_GetDirectPlaybackSupport(OH\_AudioStreamManager \*audioStreamManager, OH\_AudioStreamInfo \*streamInfo, OH\_AudioStream\_Usage usage, OH\_AudioStream\_DirectPlaybackMode \*directPlaybackMode)

**Description**

Obtains the direct playback mode supported by an audio stream.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamManager](../../structs/oh-audiostreammanager/document.md) \*audioStreamManager | Handle to the audio stream manager. The handle is obtained by calling [OH\_AudioManager\_GetAudioStreamManager](#oh_audiomanager_getaudiostreammanager). |
| [OH\_AudioStreamInfo](../../structs/oh-audiostreaminfo/document.md) \*streamInfo | Pointer to the audio stream information. |
| [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage) usage | Usage scenario of the audio stream. |
| [OH\_AudioStream\_DirectPlaybackMode](../native-audiostream-base-h/document.md#oh_audiostream_directplaybackmode) \*directPlaybackMode | Pointer to [OH\_AudioStream\_DirectPlaybackMode](../native-audiostream-base-h/document.md#oh_audiostream_directplaybackmode), which is used to receive the direct playback mode supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS = 0**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM = 6800101**:

1\. The **audioStreamManager** parameter is nullptr.

2\. The **streamInfo** parameter is nullptr.

3\. The **usage** parameter is invalid.

4\. The **directPlaybackMode** parameter is nullptr.

 |

#### \[h2\]OH\_AudioStreamManager\_IsAcousticEchoCancelerSupported()

OH\_AudioCommon\_Result OH\_AudioStreamManager\_IsAcousticEchoCancelerSupported(OH\_AudioStreamManager \*streamManager, OH\_AudioStream\_SourceType sourceType, bool \*supported)

**Description**

Checks whether the audio stream of the specified source type supports acoustic echo cancellation.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamManager](../../structs/oh-audiostreammanager/document.md) \*streamManager | Handle to the audio stream manager. The handle is obtained by calling [OH\_AudioManager\_GetAudioStreamManager](#oh_audiomanager_getaudiostreammanager). |
| [OH\_AudioStream\_SourceType](../native-audiostream-base-h/document.md#oh_audiostream_sourcetype) sourceType | Usage scenario ([OH\_AudioStream\_SourceType](../native-audiostream-base-h/document.md#oh_audiostream_sourcetype)) of the audio input stream. |
| bool \*supported | Pointer to the result for the support of acoustic echo cancellation. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS = 0**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM = 6800101**:

1\. The **audioStreamManager** parameter is nullptr.

2\. The **sourceType** parameter is invalid.

3\. The **supported** parameter is nullptr.

 |

#### \[h2\]OH\_AudioStreamManager\_IsFastPlaybackSupported()

bool OH\_AudioStreamManager\_IsFastPlaybackSupported(OH\_AudioStreamManager \*streamManager, OH\_AudioStreamInfo \*streamInfo, OH\_AudioStream\_Usage usage)

**Description**

Checks whether the current device supports low-latency playback for the specified audio stream information and usage scenario.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamManager](../../structs/oh-audiostreammanager/document.md) \*streamManager | Handle to the audio stream manager. The handle is obtained by calling [OH\_AudioManager\_GetAudioStreamManager](#oh_audiomanager_getaudiostreammanager). |
| [OH\_AudioStreamInfo](../../structs/oh-audiostreaminfo/document.md) \*streamInfo | Pointer to the audio stream information. |
| [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage) usage | Usage scenario of the audio stream. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for the support of low-latency playback. **true** if supported, **false** otherwise. |

#### \[h2\]OH\_AudioStreamManager\_IsFastRecordingSupported()

bool OH\_AudioStreamManager\_IsFastRecordingSupported(OH\_AudioStreamManager \*streamManager, OH\_AudioStreamInfo \*streamInfo, OH\_AudioStream\_SourceType source)

**Description**

Checks whether the current device supports low-latency recording for the specified audio stream information and usage scenario.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamManager](../../structs/oh-audiostreammanager/document.md) \*streamManager | Handle to the audio stream manager. The handle is obtained by calling [OH\_AudioManager\_GetAudioStreamManager](#oh_audiomanager_getaudiostreammanager). |
| [OH\_AudioStreamInfo](../../structs/oh-audiostreaminfo/document.md) \*streamInfo | Pointer to the audio stream information. |
| [OH\_AudioStream\_SourceType](../native-audiostream-base-h/document.md#oh_audiostream_sourcetype) source | Usage scenario of the audio stream. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for the support of low-latency recording. **true** if supported, **false** otherwise. |

#### \[h2\]OH\_AudioStreamManager\_IsIntelligentNoiseReductionEnabledForCurrentDevice()

bool OH\_AudioStreamManager\_IsIntelligentNoiseReductionEnabledForCurrentDevice(OH\_AudioStreamManager \*streamManager, OH\_AudioStream\_SourceType source)

**Description**

Checks whether the intelligent noise reduction feature is enabled for the audio stream of the specified source type.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamManager](../../structs/oh-audiostreammanager/document.md) \*streamManager | Handle to the audio stream manager. which is obtained by calling [OH\_AudioManager\_GetAudioStreamManager](#oh_audiomanager_getaudiostreammanager). |
| [OH\_AudioStream\_SourceType](../native-audiostream-base-h/document.md#oh_audiostream_sourcetype) source | Audio stream usage scenario determined based on the audio device and pipe type. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for whether the intelligent noise reduction feature is enabled. **true** if enabled, and **false** otherwise. |
