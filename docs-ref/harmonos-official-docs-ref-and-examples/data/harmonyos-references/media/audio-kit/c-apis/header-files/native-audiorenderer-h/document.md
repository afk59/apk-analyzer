# native\_audiorenderer.h

#### Overview

The file declares the functions related to an audio renderer.

**File to include**: <ohaudio/native\_audiorenderer.h>

**Library**: libohaudio.so

**System capability**: SystemCapability.Multimedia.Audio.Core

**Since**: 10

**Related module**: [OHAudio](../../modules/ohaudio/document.md)

#### Summary

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_Release(OH\_AudioRenderer\* renderer)](#oh_audiorenderer_release) | \- | Releases an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_Start(OH\_AudioRenderer\* renderer)](#oh_audiorenderer_start) | \- | Starts an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_Pause(OH\_AudioRenderer\* renderer)](#oh_audiorenderer_pause) | \- | Pauses an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_Stop(OH\_AudioRenderer\* renderer)](#oh_audiorenderer_stop) | \- | Stops an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_Flush(OH\_AudioRenderer\* renderer)](#oh_audiorenderer_flush) | \- | Clears audio data in the buffer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetCurrentState(OH\_AudioRenderer\* renderer, OH\_AudioStream\_State\* state)](#oh_audiorenderer_getcurrentstate) | \- | Obtains the state of an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetSamplingRate(OH\_AudioRenderer\* renderer, int32\_t\* rate)](#oh_audiorenderer_getsamplingrate) | \- | Obtains the sampling rate of an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetStreamId(OH\_AudioRenderer\* renderer, uint32\_t\* streamId)](#oh_audiorenderer_getstreamid) | \- | Obtains the stream ID of an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetChannelCount(OH\_AudioRenderer\* renderer, int32\_t\* channelCount)](#oh_audiorenderer_getchannelcount) | \- | Obtains the number of channels for an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetSampleFormat(OH\_AudioRenderer\* renderer, OH\_AudioStream\_SampleFormat\* sampleFormat)](#oh_audiorenderer_getsampleformat) | \- | Obtains the sampling format of an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetLatencyMode(OH\_AudioRenderer\* renderer, OH\_AudioStream\_LatencyMode\* latencyMode)](#oh_audiorenderer_getlatencymode) | \- | Obtains the latency mode of an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetRendererInfo(OH\_AudioRenderer\* renderer, OH\_AudioStream\_Usage\* usage)](#oh_audiorenderer_getrendererinfo) | \- | Obtains the usage type of an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetEncodingType(OH\_AudioRenderer\* renderer, OH\_AudioStream\_EncodingType\* encodingType)](#oh_audiorenderer_getencodingtype) | \- | Obtains the encoding type of an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetFramesWritten(OH\_AudioRenderer\* renderer, int64\_t\* frames)](#oh_audiorenderer_getframeswritten) | \- | Obtains the number of frames that have been written since the stream was created. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetTimestamp(OH\_AudioRenderer\* renderer, clockid\_t clockId, int64\_t\* framePosition, int64\_t\* timestamp)](#oh_audiorenderer_gettimestamp) | \- | 
Obtains the timestamp and position information of an output audio stream.

This function obtains the actual playback position (specified by **framePosition**) of the audio channel and the timestamp when playing to that position (specified by **timestamp**, in nanoseconds).

When you switch devices or resume playback after a pause, the playback position and timestamp retrieved via this function will temporarily stay in the state they were in before the switch or pause, since the playback channel requires a moment to stabilize.

 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetAudioTimestampInfo(OH\_AudioRenderer\* renderer, int64\_t\* framePosition, int64\_t\* timestamp)](#oh_audiorenderer_getaudiotimestampinfo) | \- | 

Obtains the timestamp and position information of an output audio stream. It adapts to the speed adjustment interface.

This information is commonly used for audio and video synchronization.

 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetFrameSizeInCallback(OH\_AudioRenderer\* renderer, int32\_t\* frameSize)](#oh_audiorenderer_getframesizeincallback) | \- | Obtains the frame size in the callback. The frame size is the fixed length of the buffer returned by each callback. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetSpeed(OH\_AudioRenderer\* renderer, float\* speed)](#oh_audiorenderer_getspeed) | \- | Obtains the rate of an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_SetSpeed(OH\_AudioRenderer\* renderer, float speed)](#oh_audiorenderer_setspeed) | \- | Sets the rate for an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_SetMarkPosition(OH\_AudioRenderer\* renderer, uint32\_t samplePos, OH\_AudioRenderer\_OnMarkReachedCallback callback, void\* userData)](#oh_audiorenderer_setmarkposition) | \- | Sets the mark position for an audio renderer. When this function is called, the mark position that has been set will be overwritten. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_CancelMark(OH\_AudioRenderer\* renderer)](#oh_audiorenderer_cancelmark) | \- | Cancels the mark set by [OH\_AudioRenderer\_SetMarkPosition](#oh_audiorenderer_setmarkposition). |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_SetVolume(OH\_AudioRenderer\* renderer, float volume)](#oh_audiorenderer_setvolume) | \- | Sets the volume for an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_SetVolumeWithRamp(OH\_AudioRenderer\* renderer, float volume, int32\_t durationMs)](#oh_audiorenderer_setvolumewithramp) | \- | Sets the volume with a ramp within the specified duration for an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetVolume(OH\_AudioRenderer\* renderer, float\* volume)](#oh_audiorenderer_getvolume) | \- | Obtains the volume of an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetUnderflowCount(OH\_AudioRenderer\* renderer, uint32\_t\* count)](#oh_audiorenderer_getunderflowcount) | \- | Obtains the number of underloaded audio streams of an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetChannelLayout(OH\_AudioRenderer\* renderer, OH\_AudioChannelLayout\* channelLayout)](#oh_audiorenderer_getchannellayout) | \- | Obtains the channel layout of an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetEffectMode(OH\_AudioRenderer\* renderer, OH\_AudioStream\_AudioEffectMode\* effectMode)](#oh_audiorenderer_geteffectmode) | \- | Obtains the effect mode of an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_SetEffectMode(OH\_AudioRenderer\* renderer, OH\_AudioStream\_AudioEffectMode effectMode)](#oh_audiorenderer_seteffectmode) | \- | Sets the effect mode for an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetRendererPrivacy(OH\_AudioRenderer\* renderer, OH\_AudioStream\_PrivacyType\* privacy)](#oh_audiorenderer_getrendererprivacy) | \- | Checks whether the audio stream being played can be recorded by other applications. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_SetSilentModeAndMixWithOthers(OH\_AudioRenderer\* renderer, bool on)](#oh_audiorenderer_setsilentmodeandmixwithothers) | \- | 

Sets the silent mode in concurrent playback for an audio renderer.

If the silent mode in concurrent playback is enabled, the system mutes the audio stream and does not interrupt other audio streams. If the silent mode in concurrent playback is disabled, the audio stream can gain focus based on the system focus strategy.

 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetSilentModeAndMixWithOthers(OH\_AudioRenderer\* renderer, bool\* on)](#oh_audiorenderer_getsilentmodeandmixwithothers) | \- | Checks whether the silent mode in concurrent playback is enabled for an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_SetDefaultOutputDevice(OH\_AudioRenderer\* renderer, OH\_AudioDevice\_Type deviceType)](#oh_audiorenderer_setdefaultoutputdevice) | \- | 

Sets the default built-in audio output device.

This function applies only to the scenario where [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage) is set to voice messages, VoIP voice calls, and VoIP video calls and the available device types are the receiver, speaker, and system default device.

This function can be called at any time after an AudioRenderer instance is created. The system records the default built-in audio output device set by the application. When the application is started, if an external device such as a Bluetooth or wired headset is connected, the system preferentially uses the external device to play sound. Otherwise, the system uses this default device to play sound.

 |
| [typedef void (\*OH\_AudioRenderer\_OnInterruptCallback)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioInterrupt\_ForceType type, OH\_AudioInterrupt\_Hint hint)](#oh_audiorenderer_oninterruptcallback) | OH\_AudioRenderer\_OnInterruptCallback | Defines the callback for interruption events of an audio renderer. |
| [typedef void (\*OH\_AudioRenderer\_OnErrorCallback)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioStream\_Result error)](#oh_audiorenderer_onerrorcallback) | OH\_AudioRenderer\_OnErrorCallback | Defines the callback for error events of an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetFastStatus(OH\_AudioRenderer\* renderer, OH\_AudioStream\_FastStatus\* status)](#oh_audiorenderer_getfaststatus) | \- | Obtains the running status of an audio renderer to determine whether it is running in low-latency mode. |
| [typedef void (\*OH\_AudioRenderer\_OnFastStatusChange)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioStream\_FastStatus status)](#oh_audiorenderer_onfaststatuschange) | OH\_AudioRenderer\_OnFastStatusChange | Defines a callback function for low-latency status changes during audio playback. |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_SetLoudnessGain(OH\_AudioRenderer\* renderer, float loudnessGain)](#oh_audiorenderer_setloudnessgain) | \- | 

Sets the loudness of audio playback. The default loudness value is 0.0 dB. The audio stream playback type must be one of the following: Music: [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MUSIC

Movies or videos: [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MUSIC

Audiobooks (including books, crosstalk, and storytelling), listening to news, podcasts, and others: [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_AUDIOBOOK

The latency mode of the audio stream must be [OH\_AudioStream\_LatencyMode](../native-audiostream-base-h/document.md#oh_audiostream_latencymode).AUDIOSTREAM\_LATENCY\_MODE\_NORMAL.

Loudness settings are not supported for high-definition audio channels.

Due to the buffer between the audio framework and hardware, there may be a delay in the actual effect of loudness adjustment. The delay duration depends on the buffer length.

You are advised to set the loudness before starting playback of different audio streams to achieve the optimal balance effect.

 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetLoudnessGain(OH\_AudioRenderer\* renderer, float\* loudnessGain)](#oh_audiorenderer_getloudnessgain) | \- | Obtains the loudness of audio playback. |
| [typedef int32\_t (\*OH\_AudioRenderer\_OnWriteDataCallbackAdvanced)(OH\_AudioRenderer\* renderer, void\* userData, void\* audioData, int32\_t audioDataSize)](#oh_audiorenderer_onwritedatacallbackadvanced) | OH\_AudioRenderer\_OnWriteDataCallbackAdvanced | 

Defines a function pointer to the callback used to write audio data. Unlike **OH\_AudioRenderer\_OnWriteDataCallback**, this function allows the application to fill data of the length ranging \[0, audioDataSize\].

Here, **audioDataSize** refers to the length of the callback buffer. The caller notifies the system of the length of the data written through the return value.

If the return value is 0, the callback thread sleeps for a period of time.

Otherwise, the system may immediately initiate the next callback.

 |

#### Function Description

#### \[h2\]OH\_AudioRenderer\_Release()

OH\_AudioStream\_Result OH\_AudioRenderer\_Release(OH\_AudioRenderer\* renderer)

**Description**

Releases an audio renderer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

 |

#### \[h2\]OH\_AudioRenderer\_Start()

OH\_AudioStream\_Result OH\_AudioRenderer\_Start(OH\_AudioRenderer\* renderer)

**Description**

Starts an audio renderer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

 |

#### \[h2\]OH\_AudioRenderer\_Pause()

OH\_AudioStream\_Result OH\_AudioRenderer\_Pause(OH\_AudioRenderer\* renderer)

**Description**

Pauses an audio renderer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

 |

#### \[h2\]OH\_AudioRenderer\_Stop()

OH\_AudioStream\_Result OH\_AudioRenderer\_Stop(OH\_AudioRenderer\* renderer)

**Description**

Stops an audio renderer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

 |

#### \[h2\]OH\_AudioRenderer\_Flush()

OH\_AudioStream\_Result OH\_AudioRenderer\_Flush(OH\_AudioRenderer\* renderer)

**Description**

Clears audio data in the buffer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

 |

#### \[h2\]OH\_AudioRenderer\_GetCurrentState()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetCurrentState(OH\_AudioRenderer\* renderer,OH\_AudioStream\_State\* state)

**Description**

Obtains the state of an audio renderer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| [OH\_AudioStream\_State](../native-audiostream-base-h/document.md#oh_audiostream_state)\* state | Pointer to a variable used to receive the state. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_GetSamplingRate()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetSamplingRate(OH\_AudioRenderer\* renderer, int32\_t\* rate)

**Description**

Obtains the sampling rate of an audio renderer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| int32\_t\* rate | Pointer to a variable used to receive the sampling rate. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_GetStreamId()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetStreamId(OH\_AudioRenderer\* renderer, uint32\_t\* streamId)

**Description**

Obtains the stream ID of an audio renderer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| uint32\_t\* streamId | Pointer to a variable used to receive the stream ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_GetChannelCount()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetChannelCount(OH\_AudioRenderer\* renderer, int32\_t\* channelCount)

**Description**

Obtains the number of channels for an audio renderer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| int32\_t\* channelCount | Pointer to a variable used to receive the channel count. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_GetSampleFormat()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetSampleFormat(OH\_AudioRenderer\* renderer,OH\_AudioStream\_SampleFormat\* sampleFormat)

**Description**

Obtains the sampling format of an audio renderer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| [OH\_AudioStream\_SampleFormat](../native-audiostream-base-h/document.md#oh_audiostream_sampleformat)\* sampleFormat | Pointer to a variable used to receive the sampling format. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_GetLatencyMode()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetLatencyMode(OH\_AudioRenderer\* renderer,OH\_AudioStream\_LatencyMode\* latencyMode)

**Description**

Obtains the latency mode of an audio renderer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| [OH\_AudioStream\_LatencyMode](../native-audiostream-base-h/document.md#oh_audiostream_latencymode)\* latencyMode | Pointer to a variable used to receive the latency mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_GetRendererInfo()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetRendererInfo(OH\_AudioRenderer\* renderer,OH\_AudioStream\_Usage\* usage)

**Description**

Obtains the usage type of an audio renderer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage)\* usage | Pointer to a variable used to receive the usage type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_GetEncodingType()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetEncodingType(OH\_AudioRenderer\* renderer,OH\_AudioStream\_EncodingType\* encodingType)

**Description**

Obtains the encoding type of an audio renderer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| [OH\_AudioStream\_EncodingType](../native-audiostream-base-h/document.md#oh_audiostream_encodingtype)\* encodingType | Pointer to a variable used to receive the encoding type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_GetFramesWritten()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetFramesWritten(OH\_AudioRenderer\* renderer, int64\_t\* frames)

**Description**

Obtains the number of frames that have been written since the stream was created.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| int64\_t\* frames | Pointer to a variable used to receive the frame count. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_GetTimestamp()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetTimestamp(OH\_AudioRenderer\* renderer, clockid\_t clockId,int64\_t\* framePosition, int64\_t\* timestamp)

**Description**

Obtains the timestamp and position information of an output audio stream.

This function obtains the actual playback position (specified by **framePosition**) of the audio channel and the timestamp when playing to that position (specified by **timestamp**, in nanoseconds).

When you switch devices or resume playback after a pause, the playback position and timestamp retrieved via this function will temporarily stay in the state they were in before the switch or pause, since the playback channel requires a moment to stabilize.

This function is used to implement audio and video synchronization. It is recommended that the function be called once every minute (at least every 200 ms). Frequent calls may increase power consumption. Therefore, do not frequently query the timestamp when the audio-visual synchronization effect can be ensured.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| clockid\_t clockId | Clock identifier. Use **CLOCK\_MONOTONIC**. |
| int64\_t\* framePosition | Pointer to a variable used to receive the position information. |
| int64\_t\* timestamp | Pointer to a variable used to receive the timestamp. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **renderer** parameter is nullptr.

2\. The **clockId** parameter is set to an invalid value.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

 |

#### \[h2\]OH\_AudioRenderer\_GetAudioTimestampInfo()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetAudioTimestampInfo(OH\_AudioRenderer\* renderer,int64\_t\* framePosition, int64\_t\* timestamp)

**Description**

Obtains the timestamp and position information of an output audio stream. It adapts to the speed adjustment interface.

This information is commonly used for audio and video synchronization.

Note that when the actual playback position (**framePosition**) is 0, the timestamp remains fixed until the stream begins to play. The playback position is also reset when **Flush** is called.

Additionally, changes in the audio stream route, such as switching devices or output types, will reset the playback position, whereas the timestamp keeps increasing. You are advised to call this function to obtain the corresponding value only when the actual playback position and timestamp are stable. This function adapts to the speed adjustment interface. For example, if the playback speed is set to 2x, the rate at which the playback position increases is also twice the normal speed.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| int64\_t\* framePosition | Pointer to a variable used to receive the position information. |
| int64\_t\* timestamp | Pointer to a variable used to receive the timestamp. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **renderer** parameter is nullptr.

2\. The **framePosition** or **timestamp** parameter is nullptr.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The current stream status is invalid.

**AUDIOSTREAM\_ERROR\_SYSTEM**:

1\. The system process breaks down or is blocked.

2\. An internal system error occurs.

 |

#### \[h2\]OH\_AudioRenderer\_GetFrameSizeInCallback()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetFrameSizeInCallback(OH\_AudioRenderer\* renderer, int32\_t\* frameSize)

**Description**

Obtains the frame size in the callback. The frame size is the fixed length of the buffer returned by each callback.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| int32\_t\* frameSize | Pointer to a variable used to receive the frame size. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_GetSpeed()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetSpeed(OH\_AudioRenderer\* renderer, float\* speed)

**Description**

Obtains the rate of an audio renderer.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| float\* speed | Pointer to the variable that receives the playback rate. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_SetSpeed()

OH\_AudioStream\_Result OH\_AudioRenderer\_SetSpeed(OH\_AudioRenderer\* renderer, float speed)

**Description**

Sets the rate for an audio renderer.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| float speed | Playback rate, which ranges from 0.25 to 4.0. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_SetMarkPosition()

OH\_AudioStream\_Result OH\_AudioRenderer\_SetMarkPosition(OH\_AudioRenderer\* renderer, uint32\_t samplePos,OH\_AudioRenderer\_OnMarkReachedCallback callback, void\* userData)

**Description**

Sets the mark position for an audio renderer. When this function is called, the mark position that has been set will be overwritten.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| uint32\_t samplePos | Mark position. |
| [OH\_AudioRenderer\_OnMarkReachedCallback](../native-audiostream-base-h/document.md#oh_audiorenderer_onmarkreachedcallback) callback | Callback invoked when the target mark position is reached. |
| void\* userData | Pointer to the application data passed through the callbacks. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **renderer** parameter is nullptr.

2\. The **samplePos** parameter is set to an invalid value.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

**AUDIOSTREAM\_ERROR\_SYSTEM**: A system error occurs.

 |

#### \[h2\]OH\_AudioRenderer\_CancelMark()

OH\_AudioStream\_Result OH\_AudioRenderer\_CancelMark(OH\_AudioRenderer\* renderer)

**Description**

Cancels the mark set by [OH\_AudioRenderer\_SetMarkPosition](#oh_audiorenderer_setmarkposition).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_SetVolume()

OH\_AudioStream\_Result OH\_AudioRenderer\_SetVolume(OH\_AudioRenderer\* renderer, float volume)

**Description**

Sets the volume for an audio renderer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| float volume | Target volume, in the range of \[0.0, 1.0\]. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **renderer** parameter is nullptr.

2\. The **volume** parameter is set to an invalid value.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

**AUDIOSTREAM\_ERROR\_SYSTEM**: A system error occurs.

 |

#### \[h2\]OH\_AudioRenderer\_SetVolumeWithRamp()

OH\_AudioStream\_Result OH\_AudioRenderer\_SetVolumeWithRamp(OH\_AudioRenderer\* renderer, float volume, int32\_t durationMs)

**Description**

Sets the volume with a ramp within the specified duration for an audio renderer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| float volume | Target volume, in the range of \[0.0, 1.0\]. |
| int32\_t durationMs | Duration, in milliseconds. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **renderer** parameter is nullptr.

2\. The **volume** parameter is set to an invalid value.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

**AUDIOSTREAM\_ERROR\_SYSTEM**: A system error occurs.

 |

#### \[h2\]OH\_AudioRenderer\_GetVolume()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetVolume(OH\_AudioRenderer\* renderer, float\* volume)

**Description**

Obtains the volume of an audio renderer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| float\* volume | Pointer to the audio volume. The audio volume is in the range of \[0.0, 1.0\]. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **renderer** parameter is nullptr.

2\. The **volume** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_GetUnderflowCount()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetUnderflowCount(OH\_AudioRenderer\* renderer, uint32\_t\* count)

**Description**

Obtains the number of underloaded audio streams of an audio renderer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| uint32\_t\* count | Pointer to a variable used to receive the number of underloaded audio streams. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **renderer** parameter is nullptr.

2\. The **count** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_GetChannelLayout()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetChannelLayout(OH\_AudioRenderer\* renderer,OH\_AudioChannelLayout\* channelLayout)

**Description**

Obtains the channel layout of an audio renderer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| [OH\_AudioChannelLayout](../../../../avcodec-kit/c-apis/header-files/native-audio-channel-layout-h/document.md#oh_audiochannellayout)\* channelLayout | Pointer to a variable used to receive the channel layout. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_GetEffectMode()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetEffectMode(OH\_AudioRenderer\* renderer,OH\_AudioStream\_AudioEffectMode\* effectMode)

**Description**

Obtains the effect mode of an audio renderer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| [OH\_AudioStream\_AudioEffectMode](../native-audiostream-base-h/document.md#oh_audiostream_audioeffectmode)\* effectMode | Pointer to a variable used to receive the effect mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_SetEffectMode()

OH\_AudioStream\_Result OH\_AudioRenderer\_SetEffectMode(OH\_AudioRenderer\* renderer,OH\_AudioStream\_AudioEffectMode effectMode)

**Description**

Sets the effect mode for an audio renderer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| [OH\_AudioStream\_AudioEffectMode](../native-audiostream-base-h/document.md#oh_audiostream_audioeffectmode) effectMode | Effect mode to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_GetRendererPrivacy()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetRendererPrivacy(OH\_AudioRenderer\* renderer,OH\_AudioStream\_PrivacyType\* privacy)

**Description**

Checks whether the audio stream being played can be recorded by other applications.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| [OH\_AudioStream\_PrivacyType](../native-audiostream-base-h/document.md#oh_audiostream_privacytype)\* privacy | Pointer to the privacy type, which specifies whether the audio stream being played can be recorded by other applications. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_SetSilentModeAndMixWithOthers()

OH\_AudioStream\_Result OH\_AudioRenderer\_SetSilentModeAndMixWithOthers(OH\_AudioRenderer\* renderer, bool on)

**Description**

Sets the silent mode in concurrent playback for an audio renderer.

If the silent mode in concurrent playback is enabled, the system mutes the audio stream and does not interrupt other audio streams. If the silent mode in concurrent playback is disabled, the audio stream can gain focus based on the system focus strategy.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| bool on | 
Status of the silent mode in concurrent playback.

The value **true** means that the audio stream being played is muted and the playback of other audio streams is not interrupted.

The value **false** means that the audio stream being played is unmuted and can gain focus based on the system focus strategy.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_GetSilentModeAndMixWithOthers()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetSilentModeAndMixWithOthers(OH\_AudioRenderer\* renderer, bool\* on)

**Description**

Checks whether the silent mode in concurrent playback is enabled for an audio renderer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| bool\* on | Whether the silent mode in concurrent playback is enabled. **true** if enabled, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_SetDefaultOutputDevice()

OH\_AudioStream\_Result OH\_AudioRenderer\_SetDefaultOutputDevice(OH\_AudioRenderer\* renderer, OH\_AudioDevice\_Type deviceType)

**Description**

Sets the default built-in audio output device.

This function applies only to the scenario where [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage) is set to voice messages, VoIP voice calls, and VoIP video calls and the available device types are the receiver, speaker, and system default device.

This function can be called at any time after an AudioRenderer instance is created. The system records the default built-in audio output device set by the application. When the application starts playback, if an external device such as a Bluetooth or wired headset is connected, the system preferentially uses the external device to play sound. Otherwise, the system uses this default device to play sound.

**Device behavior difference**: If the default audio output device is set to earpiece on a device without an earpiece, the speaker will still be used for audio output.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| [OH\_AudioDevice\_Type](../native-audio-device-base-h/document.md#oh_audiodevice_type) deviceType | 
Device type. For details about the available options, see [OH\_AudioDevice\_Type](../native-audio-device-base-h/document.md#oh_audiodevice_type). The device types that can be set are as follows:

**AUDIO\_DEVICE\_TYPE\_EARPIECE**: receiver.

**AUDIO\_DEVICE\_TYPE\_SPEAKER**: speaker.

**AUDIO\_DEVICE\_TYPE\_DEFAULT**: system default device.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **renderer** parameter is nullptr.

2\. The **deviceType** parameter is set to an invalid value.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

**AUDIOSTREAM\_ERROR\_SYSTEM**: A system error occurs.

 |

#### \[h2\]OH\_AudioRenderer\_OnInterruptCallback()

typedef void (\*OH\_AudioRenderer\_OnInterruptCallback)(OH\_AudioRenderer\* renderer, void\* userData,OH\_AudioInterrupt\_ForceType type, OH\_AudioInterrupt\_Hint hint)

**Description**

Defines the callback for interruption events of an audio renderer.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| void\* userData | Pointer to the data storage area customized by the application. |
| [OH\_AudioInterrupt\_ForceType](../native-audiostream-base-h/document.md#oh_audiointerrupt_forcetype) type | Type of force that causes audio interruption. |
| [OH\_AudioInterrupt\_Hint](../native-audiostream-base-h/document.md#oh_audiointerrupt_hint) hint | Hint provided along with audio interruption. |

#### \[h2\]OH\_AudioRenderer\_OnErrorCallback()

typedef void (\*OH\_AudioRenderer\_OnErrorCallback)(OH\_AudioRenderer\* renderer, void\* userData,OH\_AudioStream\_Result error)

**Description**

Defines the callback for error events of an audio renderer.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| void\* userData | Pointer to the data storage area customized by the application. |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) error | Audio renderer error. |

#### \[h2\]OH\_AudioRenderer\_GetFastStatus()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetFastStatus(OH\_AudioRenderer\* renderer,OH\_AudioStream\_FastStatus\* status)

**Description**

Obtains the running status of an audio renderer to determine whether it is running in low-latency mode.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| [OH\_AudioStream\_FastStatus](../native-audiostream-base-h/document.md#oh_audiostream_faststatus)\* status | Pointer to the running status. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **renderer** parameter is nullptr.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The function is called in an incorrect state.

 |

#### \[h2\]OH\_AudioRenderer\_OnFastStatusChange()

typedef void (\*OH\_AudioRenderer\_OnFastStatusChange)(OH\_AudioRenderer\* renderer,void\* userData,OH\_AudioStream\_FastStatus status)

**Description**

Defines a callback function for low-latency status changes during audio playback.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| void\* userData | Pointer to the data storage area customized by the application. |
| [OH\_AudioStream\_FastStatus](../native-audiostream-base-h/document.md#oh_audiostream_faststatus) status | Low-latency status. |

#### \[h2\]OH\_AudioRenderer\_SetLoudnessGain()

OH\_AudioStream\_Result OH\_AudioRenderer\_SetLoudnessGain(OH\_AudioRenderer\* renderer, float loudnessGain)

**Description**

Sets the loudness of audio playback. The default loudness value is 0.0 dB. The audio stream playback type must be one of the following: Music: [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MUSIC

Movies or videos: [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MUSIC

Audiobooks (including books, crosstalk, and storytelling), listening to news, podcasts, and others: [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_AUDIOBOOK

The latency mode of the audio stream must be [OH\_AudioStream\_LatencyMode](../native-audiostream-base-h/document.md#oh_audiostream_latencymode).AUDIOSTREAM\_LATENCY\_MODE\_NORMAL.

Loudness settings are not supported for high-definition audio channels.

Due to the buffer between the audio framework and hardware, there may be a delay in the actual effect of loudness adjustment. The delay duration depends on the buffer length.

You are advised to set the loudness before starting playback of different audio streams to achieve the optimal balance effect.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| float loudnessGain | Loudness, in the range \[-90.0, 24.0\], in dB. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **renderer** parameter is nullptr, or audio streams do not support setting the loudness.

2\. The **loudnessGain** parameter is not within the allowed range.

 |

#### \[h2\]OH\_AudioRenderer\_GetLoudnessGain()

OH\_AudioStream\_Result OH\_AudioRenderer\_GetLoudnessGain(OH\_AudioRenderer\* renderer, float\* loudnessGain)

**Description**

Obtains the loudness of audio playback.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| float\* loudnessGain | Pointer to the variable that receives the loudness. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **renderer** parameter is nullptr.

2\. The **loudnessGain** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRenderer\_OnWriteDataCallbackAdvanced()

typedef int32\_t (\*OH\_AudioRenderer\_OnWriteDataCallbackAdvanced)(OH\_AudioRenderer\* renderer, void\* userData, void\* audioData, int32\_t audioDataSize)

**Description**

Defines a function pointer to the callback used to write audio data. Unlike **OH\_AudioRenderer\_OnWriteDataCallback**, this function allows the application to fill data of the length ranging \[0, audioDataSize\].

Here, **audioDataSize** refers to the length of the callback buffer. The caller notifies the system of the length of the data written through the return value.

If the return value is 0, the callback thread sleeps for a period of time.

Otherwise, the system may immediately initiate the next callback.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\* renderer | Pointer to the instance for which the callback occurs. |
| void\* userData | Pointer to the application data passed through the callbacks. |
| void\* audioData | Pointer to the audio data to be filled by the application. |
| int32\_t audioDataSize | Length of the audio data, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Actual length of valid audio data filled by the application. The return value must be in the range of \[0, audioDataSize\].

If the return value is less than 0, the system adjusts it to 0. If the return value is greater than **audioDataSize**, the system adjusts it to **audioDataSize**.

Note that the return value must be an integer multiple of the size of a single sampling point.

For example, for audio data in stereo s16 format, it must be an integer multiple of 4 (2 \* 16 / 8).

Failure to do so may result in playback noise.

 |
