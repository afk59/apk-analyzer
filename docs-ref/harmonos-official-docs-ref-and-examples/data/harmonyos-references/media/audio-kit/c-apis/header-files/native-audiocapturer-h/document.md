# native\_audiocapturer.h

#### Overview

The file declares the functions related to an audio capturer.

**File to include**: <ohaudio/native\_audiocapturer.h>

**Library**: libohaudio.so

**System capability**: SystemCapability.Multimedia.Audio.Core

**Since**: 10

**Related module**: [OHAudio](../../modules/ohaudio/document.md)

#### Summary

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_Release(OH\_AudioCapturer\* capturer)](#oh_audiocapturer_release) | \- | Releases an audio capturer. |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_Start(OH\_AudioCapturer\* capturer)](#oh_audiocapturer_start) | \- | Starts an audio capturer to start capturing audio data. |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_Pause(OH\_AudioCapturer\* capturer)](#oh_audiocapturer_pause) | \- | Pauses an audio capturer. You are advised to use the pause function if you need to resume audio recording later. |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_Stop(OH\_AudioCapturer\* capturer)](#oh_audiocapturer_stop) | \- | Stops an audio capturer, ceasing the input audio stream. You are advised to use the stop function if you need to terminate recording completely. |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_Flush(OH\_AudioCapturer\* capturer)](#oh_audiocapturer_flush) | \- | Flushes audio data captured by an audio capturer. |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetCurrentState(OH\_AudioCapturer\* capturer, OH\_AudioStream\_State\* state)](#oh_audiocapturer_getcurrentstate) | \- | Obtains the state of an audio capturer. |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetLatencyMode(OH\_AudioCapturer\* capturer, OH\_AudioStream\_LatencyMode\* latencyMode)](#oh_audiocapturer_getlatencymode) | \- | Obtains the latency mode of an audio capturer. |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetStreamId(OH\_AudioCapturer\* capturer, uint32\_t\* streamId)](#oh_audiocapturer_getstreamid) | \- | Obtains the stream ID of an audio capturer. |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetSamplingRate(OH\_AudioCapturer\* capturer, int32\_t\* rate)](#oh_audiocapturer_getsamplingrate) | \- | Obtains the sampling rate of an audio capturer. |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetChannelCount(OH\_AudioCapturer\* capturer, int32\_t\* channelCount)](#oh_audiocapturer_getchannelcount) | \- | Obtains the number of channels for an audio capturer. |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetSampleFormat(OH\_AudioCapturer\* capturer, OH\_AudioStream\_SampleFormat\* sampleFormat)](#oh_audiocapturer_getsampleformat) | \- | Obtains the sampling format of an audio capturer. |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetEncodingType(OH\_AudioCapturer\* capturer, OH\_AudioStream\_EncodingType\* encodingType)](#oh_audiocapturer_getencodingtype) | \- | Obtains the encoding type of an audio capturer. |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetCapturerInfo(OH\_AudioCapturer\* capturer, OH\_AudioStream\_SourceType\* sourceType)](#oh_audiocapturer_getcapturerinfo) | \- | Obtains the usage scenario of an audio capturer. |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetFrameSizeInCallback(OH\_AudioCapturer\* capturer, int32\_t\* frameSize)](#oh_audiocapturer_getframesizeincallback) | \- | Obtains the frame size in the callback. The frame size is the fixed length of the buffer returned by each callback. |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetTimestamp(OH\_AudioCapturer\* capturer, clockid\_t clockId,int64\_t\* framePosition, int64\_t\* timestamp)](#oh_audiocapturer_gettimestamp) | \- | 
Obtains the information about the input audio stream timestamp and the current data frame position.

This function obtains the actual recording position (specified by **framePosition**) of the audio channel and the timestamp when recording to that position (specified by **timestamp**, in nanoseconds).

 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetFramesRead(OH\_AudioCapturer\* capturer, int64\_t\* frames)](#oh_audiocapturer_getframesread) | \- | Obtains the number of frames that have been read since the stream was created. |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetOverflowCount(OH\_AudioCapturer\* capturer, uint32\_t\* count)](#oh_audiocapturer_getoverflowcount) | \- | Obtains the number of overloaded audio streams of an audio capturer. |
| [typedef void (\*OH\_AudioCapturer\_OnReadDataCallback)(OH\_AudioCapturer\* capturer, void\* userData, void\* audioData, int32\_t audioDataSize)](#oh_audiocapturer_onreaddatacallback) | OH\_AudioCapturer\_OnReadDataCallback | Defines the callback used to read audio data. |
| [typedef void (\*OH\_AudioCapturer\_OnDeviceChangeCallback)(OH\_AudioCapturer\* capturer, void\* userData, OH\_AudioDeviceDescriptorArray\* deviceArray)](#oh_audiocapturer_ondevicechangecallback) | OH\_AudioCapturer\_OnDeviceChangeCallback | Defines the callback for audio capturer device change events. |
| [typedef void (\*OH\_AudioCapturer\_OnInterruptCallback)(OH\_AudioCapturer\* capturer, void\* userData, OH\_AudioInterrupt\_ForceType type, OH\_AudioInterrupt\_Hint hint)](#oh_audiocapturer_oninterruptcallback) | OH\_AudioCapturer\_OnInterruptCallback | Defines the callback for interruption events of an audio capturer. |
| [typedef void (\*OH\_AudioCapturer\_OnErrorCallback)(OH\_AudioCapturer\* capturer, void\* userData, OH\_AudioStream\_Result error)](#oh_audiocapturer_onerrorcallback) | OH\_AudioCapturer\_OnErrorCallback | Defines the callback for error events of an audio capturer. |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetFastStatus(OH\_AudioCapturer\* capturer, OH\_AudioStream\_FastStatus\* status)](#oh_audiocapturer_getfaststatus) | \- | Obtains the running status of an audio capturer to determine whether it is running in low-latency mode. |
| [typedef void (\*OH\_AudioCapturer\_OnFastStatusChange)(OH\_AudioCapturer\* capturer, void\* userData, OH\_AudioStream\_FastStatus status)](#oh_audiocapturer_onfaststatuschange) | OH\_AudioCapturer\_OnFastStatusChange | Defines a callback function for low-latency status changes during audio recording. |

#### Function Description

#### \[h2\]OH\_AudioCapturer\_Release()

OH\_AudioStream\_Result OH\_AudioCapturer\_Release(OH\_AudioCapturer\* capturer)

**Description**

Releases an audio capturer.

**Required permissions**: ohos.permission.MICROPHONE

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **capturer** parameter is nullptr.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

 |

#### \[h2\]OH\_AudioCapturer\_Start()

OH\_AudioStream\_Result OH\_AudioCapturer\_Start(OH\_AudioCapturer\* capturer)

**Description**

Starts an audio capturer to start capturing audio data.

**Required permissions**: ohos.permission.MICROPHONE

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **capturer** parameter is nullptr.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

 |

#### \[h2\]OH\_AudioCapturer\_Pause()

OH\_AudioStream\_Result OH\_AudioCapturer\_Pause(OH\_AudioCapturer\* capturer)

**Description**

Pauses an audio capturer. You are advised to use the pause function if you need to resume audio recording later.

**Required permissions**: ohos.permission.MICROPHONE

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **capturer** parameter is nullptr.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

 |

#### \[h2\]OH\_AudioCapturer\_Stop()

OH\_AudioStream\_Result OH\_AudioCapturer\_Stop(OH\_AudioCapturer\* capturer)

**Description**

Stops an audio capturer, ceasing the input audio stream. You are advised to use the stop function if you need to terminate recording completely.

**Required permissions**: ohos.permission.MICROPHONE

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **capturer** parameter is nullptr.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

 |

#### \[h2\]OH\_AudioCapturer\_Flush()

OH\_AudioStream\_Result OH\_AudioCapturer\_Flush(OH\_AudioCapturer\* capturer)

**Description**

Flushes audio data captured by an audio capturer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **capturer** parameter is nullptr.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

 |

#### \[h2\]OH\_AudioCapturer\_GetCurrentState()

OH\_AudioStream\_Result OH\_AudioCapturer\_GetCurrentState(OH\_AudioCapturer\* capturer, OH\_AudioStream\_State\* state)

**Description**

Obtains the state of an audio capturer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| [OH\_AudioStream\_State](../native-audiostream-base-h/document.md#oh_audiostream_state)\* state | Pointer to a variable used to receive the state. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **capturer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioCapturer\_GetLatencyMode()

OH\_AudioStream\_Result OH\_AudioCapturer\_GetLatencyMode(OH\_AudioCapturer\* capturer,OH\_AudioStream\_LatencyMode\* latencyMode)

**Description**

Obtains the latency mode of an audio capturer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| [OH\_AudioStream\_LatencyMode](../native-audiostream-base-h/document.md#oh_audiostream_latencymode)\* latencyMode | Pointer to a variable used to receive the latency mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **capturer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioCapturer\_GetStreamId()

OH\_AudioStream\_Result OH\_AudioCapturer\_GetStreamId(OH\_AudioCapturer\* capturer, uint32\_t\* streamId)

**Description**

Obtains the stream ID of an audio capturer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| uint32\_t\* streamId | Pointer to a variable used to receive the stream ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **capturer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioCapturer\_GetSamplingRate()

OH\_AudioStream\_Result OH\_AudioCapturer\_GetSamplingRate(OH\_AudioCapturer\* capturer, int32\_t\* rate)

**Description**

Obtains the sampling rate of an audio capturer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| int32\_t\* rate | Pointer to a variable used to receive the sampling rate. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **capturer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioCapturer\_GetChannelCount()

OH\_AudioStream\_Result OH\_AudioCapturer\_GetChannelCount(OH\_AudioCapturer\* capturer, int32\_t\* channelCount)

**Description**

Obtains the number of channels for an audio capturer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| int32\_t\* channelCount | Pointer to a variable used to receive the channel count. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **capturer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioCapturer\_GetSampleFormat()

OH\_AudioStream\_Result OH\_AudioCapturer\_GetSampleFormat(OH\_AudioCapturer\* capturer,OH\_AudioStream\_SampleFormat\* sampleFormat)

**Description**

Obtains the sampling format of an audio capturer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| [OH\_AudioStream\_SampleFormat](../native-audiostream-base-h/document.md#oh_audiostream_sampleformat)\* sampleFormat | Pointer to a variable used to receive the sampling format. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **capturer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioCapturer\_GetEncodingType()

OH\_AudioStream\_Result OH\_AudioCapturer\_GetEncodingType(OH\_AudioCapturer\* capturer,OH\_AudioStream\_EncodingType\* encodingType)

**Description**

Obtains the encoding type of an audio capturer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| [OH\_AudioStream\_EncodingType](../native-audiostream-base-h/document.md#oh_audiostream_encodingtype)\* encodingType | Pointer to a variable used to receive the encoding type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **capturer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioCapturer\_GetCapturerInfo()

OH\_AudioStream\_Result OH\_AudioCapturer\_GetCapturerInfo(OH\_AudioCapturer\* capturer,OH\_AudioStream\_SourceType\* sourceType)

**Description**

Obtains the usage scenario of an audio capturer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| [OH\_AudioStream\_SourceType](../native-audiostream-base-h/document.md#oh_audiostream_sourcetype)\* sourceType | Pointer to a variable used to receive the usage scenario. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **capturer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioCapturer\_GetFrameSizeInCallback()

OH\_AudioStream\_Result OH\_AudioCapturer\_GetFrameSizeInCallback(OH\_AudioCapturer\* capturer,int32\_t\* frameSize)

**Description**

Obtains the frame size in the callback. The frame size is the fixed length of the buffer returned by each callback.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| int32\_t\* frameSize | Pointer to a variable used to receive the frame size. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **capturer** parameter is nullptr.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

 |

#### \[h2\]OH\_AudioCapturer\_GetTimestamp()

OH\_AudioStream\_Result OH\_AudioCapturer\_GetTimestamp(OH\_AudioCapturer\* capturer, clockid\_t clockId,int64\_t\* framePosition, int64\_t\* timestamp)

**Description**

Obtains the information about the input audio stream timestamp and the current data frame position.

This function obtains the actual recording position (specified by **framePosition**) of the audio channel and the timestamp when recording to that position (specified by **timestamp**, in nanoseconds).

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| clockid\_t clockId | Clock identifier. Use **CLOCK\_MONOTONIC**. |
| int64\_t\* framePosition | Pointer to a variable used to receive the position information. |
| int64\_t\* timestamp | Pointer to a variable used to receive the timestamp. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **capturer** parameter is nullptr.

2\. The **clockId** parameter is invalid.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

 |

#### \[h2\]OH\_AudioCapturer\_GetFramesRead()

OH\_AudioStream\_Result OH\_AudioCapturer\_GetFramesRead(OH\_AudioCapturer\* capturer, int64\_t\* frames)

**Description**

Obtains the number of frames that have been read since the stream was created.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| int64\_t\* frames | Pointer to a variable used to receive the frame count. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **capturer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioCapturer\_GetOverflowCount()

OH\_AudioStream\_Result OH\_AudioCapturer\_GetOverflowCount(OH\_AudioCapturer\* capturer, uint32\_t\* count)

**Description**

Obtains the number of overloaded audio streams of an audio capturer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| uint32\_t\* count | Pointer to a variable used to receive the number of overloaded audio streams. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **capturer** parameter is nullptr.

 |

#### \[h2\]OH\_AudioCapturer\_OnReadDataCallback()

typedef void (\*OH\_AudioCapturer\_OnReadDataCallback)(OH\_AudioCapturer\* capturer, void\* userData, void\* audioData,int32\_t audioDataSize)

**Description**

Defines the callback used to read audio data.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| void\* userData | Pointer to the data storage region customized by an application, allowing the application to transfer data to itself. |
| void\* audioData | Pointer to the captured data storage area, which is used by the application to read captured data. |
| int32\_t audioDataSize | Length of the captured data. |

#### \[h2\]OH\_AudioCapturer\_OnDeviceChangeCallback()

typedef void (\*OH\_AudioCapturer\_OnDeviceChangeCallback)(OH\_AudioCapturer\* capturer, void\* userData,OH\_AudioDeviceDescriptorArray\* deviceArray)

**Description**

Defines the callback for audio capturer device change events.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| void\* userData | Pointer to the data storage area customized by the application. |
| [OH\_AudioDeviceDescriptorArray](../../structs/oh-audiodevicedescriptorarray/document.md)\* deviceArray | Pointer to the audio device descriptors in the array. |

#### \[h2\]OH\_AudioCapturer\_OnInterruptCallback()

typedef void (\*OH\_AudioCapturer\_OnInterruptCallback)(OH\_AudioCapturer\* capturer, void\* userData,OH\_AudioInterrupt\_ForceType type, OH\_AudioInterrupt\_Hint hint)

**Description**

Defines the callback for interruption events of an audio capturer.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| void\* userData | Pointer to the data storage area customized by the application. |
| [OH\_AudioInterrupt\_ForceType](../native-audiostream-base-h/document.md#oh_audiointerrupt_forcetype) type | Type of force that causes audio interruption. |
| [OH\_AudioInterrupt\_Hint](../native-audiostream-base-h/document.md#oh_audiointerrupt_hint) hint | Hint provided along with audio interruption. |

#### \[h2\]OH\_AudioCapturer\_OnErrorCallback()

typedef void (\*OH\_AudioCapturer\_OnErrorCallback)(OH\_AudioCapturer\* capturer, void\* userData,OH\_AudioStream\_Result error)

**Description**

Defines the callback for error events of an audio capturer.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| void\* userData | Pointer to the data storage area customized by the application. |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) error | Audio capturer error. |

#### \[h2\]OH\_AudioCapturer\_GetFastStatus()

OH\_AudioStream\_Result OH\_AudioCapturer\_GetFastStatus(OH\_AudioCapturer\* capturer,OH\_AudioStream\_FastStatus\* status)

**Description**

Obtains the running status of an audio capturer to determine whether it is running in low-latency mode.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| [OH\_AudioStream\_FastStatus](../native-audiostream-base-h/document.md#oh_audiostream_faststatus)\* status | Pointer to the running status. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **capturer** parameter is nullptr.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The function is called in an incorrect state.

 |

#### \[h2\]OH\_AudioCapturer\_OnFastStatusChange()

typedef void (\*OH\_AudioCapturer\_OnFastStatusChange)(OH\_AudioCapturer\* capturer,void\* userData,OH\_AudioStream\_FastStatus status)

**Description**

Defines a callback function for low-latency status changes during audio recording.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| void\* userData | Pointer to the data storage area customized by the application. |
| [OH\_AudioStream\_FastStatus](../native-audiostream-base-h/document.md#oh_audiostream_faststatus) status | Low-latency status. |
