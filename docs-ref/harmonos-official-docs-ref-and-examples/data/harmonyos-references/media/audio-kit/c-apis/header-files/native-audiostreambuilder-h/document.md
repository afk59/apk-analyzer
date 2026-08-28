# native\_audiostreambuilder.h

#### Overview

The file declares the functions related to an audio stream builder.

You can use the functions to create and destroy an audio stream builder, set audio stream attributes, and set callbacks.

**File to include**: <ohaudio/native\_audiostreambuilder.h>

**Library**: libohaudio.so

**System capability**: SystemCapability.Multimedia.Audio.Core

**Since**: 10

**Related module**: [OHAudio](../../modules/ohaudio/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_Create(OH\_AudioStreamBuilder\*\* builder, OH\_AudioStream\_Type type)](#oh_audiostreambuilder_create) | 
Creates an audio stream builder, which can be an audio renderer or capturer.

You need to call [OH\_AudioStreamBuilder\_Destroy](#oh_audiostreambuilder_destroy) to destroy the builder when it is no longer required.

 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_Destroy(OH\_AudioStreamBuilder\* builder)](#oh_audiostreambuilder_destroy) | 

Destroys an audio stream builder.

You need to call this function to destroy the builder when it is no longer required.

 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetSamplingRate(OH\_AudioStreamBuilder\* builder, int32\_t rate)](#oh_audiostreambuilder_setsamplingrate) | Sets the sampling rate of an audio stream. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetChannelCount(OH\_AudioStreamBuilder\* builder, int32\_t channelCount)](#oh_audiostreambuilder_setchannelcount) | Sets the number of channels for an audio stream. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetSampleFormat(OH\_AudioStreamBuilder\* builder, OH\_AudioStream\_SampleFormat format)](#oh_audiostreambuilder_setsampleformat) | Sets the sampling format of an audio stream. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetEncodingType(OH\_AudioStreamBuilder\* builder, OH\_AudioStream\_EncodingType encodingType)](#oh_audiostreambuilder_setencodingtype) | Sets the encoding type of an audio stream. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetLatencyMode(OH\_AudioStreamBuilder\* builder, OH\_AudioStream\_LatencyMode latencyMode)](#oh_audiostreambuilder_setlatencymode) | Sets the latency mode of an audio stream. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetChannelLayout(OH\_AudioStreamBuilder\* builder, OH\_AudioChannelLayout channelLayout)](#oh_audiostreambuilder_setchannellayout) | Sets the channel layout for an audio stream. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererInfo(OH\_AudioStreamBuilder\* builder, OH\_AudioStream\_Usage usage)](#oh_audiostreambuilder_setrendererinfo) | Sets the usage scenario of an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetVolumeMode(OH\_AudioStreamBuilder\* builder, OH\_AudioStream\_VolumeMode volumeMode)](#oh_audiostreambuilder_setvolumemode) | Sets the volume mode for an audio stream. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerInfo(OH\_AudioStreamBuilder\* builder, OH\_AudioStream\_SourceType sourceType)](#oh_audiostreambuilder_setcapturerinfo) | Sets the usage scenario of an audio capturer. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\_Callbacks callbacks, void\* userData)](#oh_audiostreambuilder_setrenderercallback) | Sets callbacks for an audio renderer. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererOutputDeviceChangeCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\_OutputDeviceChangeCallback callback, void\* userData)](#oh_audiostreambuilder_setrendereroutputdevicechangecallback) | Sets the callback for audio renderer device change events. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererPrivacy(OH\_AudioStreamBuilder\* builder, OH\_AudioStream\_PrivacyType privacy)](#oh_audiostreambuilder_setrendererprivacy) | Sets the privacy type for the audio stream being played. The privacy type specifies whether the audio stream can be recorded by other applications. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioCapturer\_Callbacks callbacks, void\* userData)](#oh_audiostreambuilder_setcapturercallback) | Sets callbacks for an audio capturer. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetWriteDataWithMetadataCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\_WriteDataWithMetadataCallback callback, void\* userData)](#oh_audiostreambuilder_setwritedatawithmetadatacallback) | Sets the callback used to write both audio data and metadata. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_GenerateRenderer(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\*\* audioRenderer)](#oh_audiostreambuilder_generaterenderer) | Creates an audio renderer instance. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_GenerateCapturer(OH\_AudioStreamBuilder\* builder, OH\_AudioCapturer\*\* audioCapturer)](#oh_audiostreambuilder_generatecapturer) | Creates an audio capturer instance. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetFrameSizeInCallback(OH\_AudioStreamBuilder\* builder, int32\_t frameSize)](#oh_audiostreambuilder_setframesizeincallback) | Sets the frame size for each callback during playback. The frame size must be at least equal to the size of the data processed by the audio hardware at a time and less than half of the internal buffer capacity. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererInterruptMode(OH\_AudioStreamBuilder\* builder, OH\_AudioInterrupt\_Mode mode)](#oh_audiostreambuilder_setrendererinterruptmode) | Sets the interrupt mode of the stream client. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererWriteDataCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\_OnWriteDataCallback callback, void\* userData)](#oh_audiostreambuilder_setrendererwritedatacallback) | 

Sets the callback used to write audio data.

This function is similar to [OH\_AudioStreamBuilder\_SetRendererCallback](#oh_audiostreambuilder_setrenderercallback). If both the functions are used, only the last callback takes effect.

 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererWriteDataCallbackAdvanced(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\_OnWriteDataCallbackAdvanced callback, void\* userData)](#oh_audiostreambuilder_setrendererwritedatacallbackadvanced) | 

Sets the callback used to write audio data.

This function is similar to [OH\_AudioStreamBuilder\_SetRendererWriteDataCallback](#oh_audiostreambuilder_setrendererwritedatacallback).

If both the functions are used, only the last callback takes effect.

Unlike **OH\_AudioStreamBuilder\_SetRendererWriteDataCallback**, **OH\_AudioStreamBuilder\_SetRendererWriteDataCallbackAdvanced** allows an application to pass variable-length audio data and notify the system of the length of the data written.

 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererInterruptCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\_OnInterruptCallback callback, void\* userData)](#oh_audiostreambuilder_setrendererinterruptcallback) | 

Sets the callback for interruption events of an audio renderer.

This function is similar to [OH\_AudioStreamBuilder\_SetRendererCallback](#oh_audiostreambuilder_setrenderercallback). If both the functions are used, only the last callback takes effect.

 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererErrorCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\_OnErrorCallback callback, void\* userData)](#oh_audiostreambuilder_setrenderererrorcallback) | 

Sets the callback for error events of an audio renderer.

This function is similar to [OH\_AudioStreamBuilder\_SetRendererCallback](#oh_audiostreambuilder_setrenderercallback). If both the functions are used, only the last callback takes effect.

 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerReadDataCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioCapturer\_OnReadDataCallback callback, void\* userData)](#oh_audiostreambuilder_setcapturerreaddatacallback) | 

Sets the callback used to read data for an audio capturer.

This function is similar to [OH\_AudioStreamBuilder\_SetCapturerCallback](#oh_audiostreambuilder_setcapturercallback). If both the functions are used, only the last callback takes effect.

 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerDeviceChangeCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioCapturer\_OnDeviceChangeCallback callback, void\* userData)](#oh_audiostreambuilder_setcapturerdevicechangecallback) | 

Sets the callback for audio capturer device change events.

This function is similar to [OH\_AudioStreamBuilder\_SetCapturerCallback](#oh_audiostreambuilder_setcapturercallback). If both the functions are used, only the last callback takes effect.

 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerInterruptCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioCapturer\_OnInterruptCallback callback, void\* userData)](#oh_audiostreambuilder_setcapturerinterruptcallback) | 

Sets the callback for interruption events of an audio capturer.

This function is similar to [OH\_AudioStreamBuilder\_SetCapturerCallback](#oh_audiostreambuilder_setcapturercallback). If both the functions are used, only the last callback takes effect.

 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerErrorCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioCapturer\_OnErrorCallback callback, void\* userData)](#oh_audiostreambuilder_setcapturererrorcallback) | 

Sets the callback for error events of an audio capturer.

This function is similar to [OH\_AudioStreamBuilder\_SetCapturerCallback](#oh_audiostreambuilder_setcapturercallback). If both the functions are used, only the last callback takes effect.

 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerWillMuteWhenInterrupted(OH\_AudioStreamBuilder\* builder, bool muteWhenInterrupted)](#oh_audiostreambuilder_setcapturerwillmutewheninterrupted) | Sets whether to mute the audio input stream when an audio interruption occurs. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererFastStatusChangeCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\_OnFastStatusChange callback, void\* userData)](#oh_audiostreambuilder_setrendererfaststatuschangecallback) | Sets a callback for low-latency status changes during audio playback. |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerFastStatusChangeCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioCapturer\_OnFastStatusChange callback, void\* userData)](#oh_audiostreambuilder_setcapturerfaststatuschangecallback) | Sets a callback for low-latency status changes during audio recording. |

#### Function Description

#### \[h2\]OH\_AudioStreamBuilder\_Create()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_Create(OH\_AudioStreamBuilder\*\* builder, OH\_AudioStream\_Type type)

**Description**

Creates an audio stream builder, which can be an audio renderer or capturer.

You need to call [OH\_AudioStreamBuilder\_Destroy](#oh_audiostreambuilder_destroy) to destroy the builder when it is no longer required.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\*\* builder | Double pointer to the audio stream builder created. |
| [OH\_AudioStream\_Type](../native-audiostream-base-h/document.md#oh_audiostream_type) type | Type of the audio stream builder, which can be AUDIOSTREAM\_TYPE\_RENDERER or AUDIOSTREAM\_TYPE\_CAPTURER. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | **AUDIOSTREAM\_SUCCESS**: The function is executed successfully. |

#### \[h2\]OH\_AudioStreamBuilder\_Destroy()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_Destroy(OH\_AudioStreamBuilder\* builder)

**Description**

Destroys an audio stream builder.

You need to call this function to destroy the builder when it is no longer required.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **builder** parameter is nullptr.

**AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**: The execution status is abnormal.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetSamplingRate()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetSamplingRate(OH\_AudioStreamBuilder\* builder, int32\_t rate)

**Description**

Sets the sampling rate of an audio stream.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| int32\_t rate | Sampling rate. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **builder** parameter is nullptr.

2\. The **rate** parameter is invalid.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetChannelCount()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetChannelCount(OH\_AudioStreamBuilder\* builder, int32\_t channelCount)

**Description**

Sets the number of channels for an audio stream.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| int32\_t channelCount | Number of channels. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **builder** parameter is nullptr.

2\. The **channelCount** parameter is invalid.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetSampleFormat()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetSampleFormat(OH\_AudioStreamBuilder\* builder,OH\_AudioStream\_SampleFormat format)

**Description**

Sets the sampling format of an audio stream.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioStream\_SampleFormat](../native-audiostream-base-h/document.md#oh_audiostream_sampleformat) format | Sampling format. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **builder** parameter is nullptr.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetEncodingType()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetEncodingType(OH\_AudioStreamBuilder\* builder,OH\_AudioStream\_EncodingType encodingType)

**Description**

Sets the encoding type of an audio stream.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioStream\_EncodingType](../native-audiostream-base-h/document.md#oh_audiostream_encodingtype) encodingType | Encoding type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **builder** parameter is nullptr.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetLatencyMode()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetLatencyMode(OH\_AudioStreamBuilder\* builder,OH\_AudioStream\_LatencyMode latencyMode)

**Description**

Sets the latency mode of an audio stream.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioStream\_LatencyMode](../native-audiostream-base-h/document.md#oh_audiostream_latencymode) latencyMode | Latency mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **builder** parameter is nullptr.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetChannelLayout()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetChannelLayout(OH\_AudioStreamBuilder\* builder,OH\_AudioChannelLayout channelLayout)

**Description**

Sets the channel layout for an audio stream.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioChannelLayout](../../../../avcodec-kit/c-apis/header-files/native-audio-channel-layout-h/document.md#oh_audiochannellayout) channelLayout | Channel layout. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **builder** parameter is nullptr.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetRendererInfo()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererInfo(OH\_AudioStreamBuilder\* builder,OH\_AudioStream\_Usage usage)

**Description**

Sets the usage scenario of an audio renderer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage) usage | Usage scenario of the audio renderer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **builder** parameter is nullptr.

2\. The **usage** parameter is invalid.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetVolumeMode()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetVolumeMode(OH\_AudioStreamBuilder\* builder,OH\_AudioStream\_VolumeMode volumeMode)

**Description**

Sets the volume mode for an audio stream.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioStream\_VolumeMode](../native-audiostream-base-h/document.md#oh_audiostream_volumemode) volumeMode | Volume mode of the audio stream. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **builder** parameter is nullptr.

2\. The **volumeMode** parameter is invalid.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetCapturerInfo()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerInfo(OH\_AudioStreamBuilder\* builder,OH\_AudioStream\_SourceType sourceType)

**Description**

Sets the usage scenario of an audio capturer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioStream\_SourceType](../native-audiostream-base-h/document.md#oh_audiostream_sourcetype) sourceType | Usage scenario of the audio capturer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **builder** parameter is nullptr.

2\. The **sourceType** parameter is invalid.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetRendererCallback()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererCallback(OH\_AudioStreamBuilder\* builder,OH\_AudioRenderer\_Callbacks callbacks, void\* userData)

**Description**

Sets callbacks for an audio renderer.

**Since**: 10

**Deprecated from**: 20

**Substitute**

Use the following APIs for substitute:

[OH\_AudioStreamBuilder\_SetRendererWriteDataCallback](#oh_audiostreambuilder_setrendererwritedatacallback), [OH\_AudioStreamBuilder\_SetRendererInterruptCallback](#oh_audiostreambuilder_setrendererinterruptcallback), [OH\_AudioStreamBuilder\_SetRendererOutputDeviceChangeCallback](#oh_audiostreambuilder_setrendereroutputdevicechangecallback), and [OH\_AudioStreamBuilder\_SetRendererErrorCallback](#oh_audiostreambuilder_setrenderererrorcallback)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioRenderer\_Callbacks](../../structs/oh-audiorenderer-callbacks-struct/document.md) callbacks | Callbacks that will be used to process events related to audio output streams. |
| void\* userData | Pointer to the application data passed through the callbacks. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **builder** parameter is nullptr.

2\. The **StreamType** parameter is invalid.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetRendererOutputDeviceChangeCallback()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererOutputDeviceChangeCallback(OH\_AudioStreamBuilder\* builder,OH\_AudioRenderer\_OutputDeviceChangeCallback callback, void\* userData)

**Description**

Sets the callback for audio renderer device change events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioRenderer\_OutputDeviceChangeCallback](../native-audiostream-base-h/document.md#oh_audiorenderer_outputdevicechangecallback) callback | Callback that will be used to process events related to audio renderer device changes. |
| void\* userData | Pointer to the application data passed through the callbacks. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **builder** parameter is nullptr.

2\. The **StreamType** parameter is invalid.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetRendererPrivacy()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererPrivacy(OH\_AudioStreamBuilder\* builder,OH\_AudioStream\_PrivacyType privacy)

**Description**

Sets the privacy type for the audio stream being played. The privacy type specifies whether the audio stream can be recorded by other applications.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioStream\_PrivacyType](../native-audiostream-base-h/document.md#oh_audiostream_privacytype) privacy | Privacy type, which specifies whether the audio stream can be recorded by other applications. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **builder** parameter is nullptr.

2\. The **StreamType** parameter is invalid.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetCapturerCallback()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerCallback(OH\_AudioStreamBuilder\* builder,OH\_AudioCapturer\_Callbacks callbacks, void\* userData)

**Description**

Sets callbacks for an audio capturer.

**Since**: 10

**Deprecated from**: 20

**Substitute**

Use the following APIs for substitute:

[OH\_AudioStreamBuilder\_SetCapturerReadDataCallback](#oh_audiostreambuilder_setcapturerreaddatacallback), [OH\_AudioStreamBuilder\_SetCapturerDeviceChangeCallback](#oh_audiostreambuilder_setcapturerdevicechangecallback), [OH\_AudioStreamBuilder\_SetCapturerInterruptCallback](#oh_audiostreambuilder_setcapturerinterruptcallback), and [OH\_AudioStreamBuilder\_SetCapturerErrorCallback](#oh_audiostreambuilder_setcapturererrorcallback)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioCapturer\_Callbacks](../../structs/oh-audiocapturer-callbacks-struct/document.md) callbacks | Callbacks that will be used to process events related to audio input streams. |
| void\* userData | Pointer to the application data passed through the callbacks. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **builder** parameter is nullptr.

2\. The **StreamType** parameter is invalid.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetWriteDataWithMetadataCallback()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetWriteDataWithMetadataCallback(OH\_AudioStreamBuilder\* builder,OH\_AudioRenderer\_WriteDataWithMetadataCallback callback, void\* userData)

**Description**

Sets the callback used to write both audio data and metadata.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioRenderer\_WriteDataWithMetadataCallback](../native-audiostream-base-h/document.md#oh_audiorenderer_writedatawithmetadatacallback) callback | Callback used to write both audio data and metadata. |
| void\* userData | Pointer to the application data passed through the callbacks. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **builder** parameter is nullptr.

2\. The **StreamType** parameter is invalid.

 |

#### \[h2\]OH\_AudioStreamBuilder\_GenerateRenderer()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_GenerateRenderer(OH\_AudioStreamBuilder\* builder,OH\_AudioRenderer\*\* audioRenderer)

**Description**

Creates an audio renderer instance.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioRenderer](../../structs/oh-audiorendererstruct/document.md)\*\* audioRenderer | Double pointer to the audio renderer instance created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **builder** parameter is nullptr.

2\. The **StreamType** parameter is invalid.

3\. The OHAudioRenderer instance fails to be created.

 |

#### \[h2\]OH\_AudioStreamBuilder\_GenerateCapturer()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_GenerateCapturer(OH\_AudioStreamBuilder\* builder,OH\_AudioCapturer\*\* audioCapturer)

**Description**

Creates an audio capturer instance.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioCapturer](../../structs/oh-audiocapturerstruct/document.md)\*\* audioCapturer | Double pointer to the audio capturer instance created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **builder** parameter is nullptr.

2\. The **StreamType** parameter is invalid.

3\. The OHAudioCapturer instance fails to be created.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetFrameSizeInCallback()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetFrameSizeInCallback(OH\_AudioStreamBuilder\* builder,int32\_t frameSize)

**Description**

Sets the frame size for each callback during playback. The frame size must be at least equal to the size of the data processed by the audio hardware at a time and less than half of the internal buffer capacity.

In the case of low-latency playback, **frameSize** can be set to the frame length corresponding to the audio that lasts for 5 ms, 10 ms, 15 ms, or 20 ms.

In the case of common playback, **frameSize** can be set to the frame length corresponding to the audio that lasts for 20 ms to 100 ms. For example, if the sampling rate is 48000 Hz, the frame length of 20 ms audio data is calculated as follows: frameSize = 48000 x 0.02, that is, 960 sampling points.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| int32\_t frameSize | Frame size. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: The **builder** parameter is nullptr.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetRendererInterruptMode()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererInterruptMode(OH\_AudioStreamBuilder\* builder,OH\_AudioInterrupt\_Mode mode)

**Description**

Sets the interrupt mode of the stream client.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioInterrupt\_Mode](../native-audiostream-base-h/document.md#oh_audiointerrupt_mode) mode | Audio interruption mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **builder** parameter is nullptr.

2\. The **mode** parameter is invalid.

3\. The **StreamType** parameter is invalid.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetRendererWriteDataCallback()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererWriteDataCallback(OH\_AudioStreamBuilder\* builder,OH\_AudioRenderer\_OnWriteDataCallback callback, void\* userData)

**Description**

Sets the callback used to write audio data.

This function is similar to [OH\_AudioStreamBuilder\_SetRendererCallback](#oh_audiostreambuilder_setrenderercallback). If both the functions are used, only the last callback takes effect.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioRenderer\_OnWriteDataCallback](../native-audiostream-base-h/document.md#oh_audiorenderer_onwritedatacallback) callback | Callback to be used to write audio data. |
| void\* userData | Pointer to the application data passed through the callbacks. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**:

1\. The **builder** parameter is nullptr.

2\. The **StreamType** parameter is invalid.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetRendererWriteDataCallbackAdvanced()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererWriteDataCallbackAdvanced(OH\_AudioStreamBuilder\* builder,OH\_AudioRenderer\_OnWriteDataCallbackAdvanced callback, void\* userData)

**Description**

Sets the callback used to write audio data.

This function is similar to [OH\_AudioStreamBuilder\_SetRendererWriteDataCallback](#oh_audiostreambuilder_setrendererwritedatacallback).

If both the functions are used, only the last callback takes effect.

Unlike **OH\_AudioStreamBuilder\_SetRendererWriteDataCallback**, **OH\_AudioStreamBuilder\_SetRendererWriteDataCallbackAdvanced** allows an application to pass variable-length audio data and notify the system of the length of the data written.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioRenderer\_OnWriteDataCallbackAdvanced](../native-audiorenderer-h/document.md#oh_audiorenderer_onwritedatacallbackadvanced) callback | Callback to be used to write audio data. |
| void\* userData | Pointer to the application data passed through the callbacks. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: An input parameter is invalid. For example, the **builder** parameter is nullptr.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetRendererInterruptCallback()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererInterruptCallback(OH\_AudioStreamBuilder\* builder,OH\_AudioRenderer\_OnInterruptCallback callback, void\* userData)

**Description**

Sets the callback for interruption events of an audio renderer.

This function is similar to [OH\_AudioStreamBuilder\_SetRendererCallback](#oh_audiostreambuilder_setrenderercallback). If both the functions are used, only the last callback takes effect.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioRenderer\_OnInterruptCallback](../native-audiorenderer-h/document.md#oh_audiorenderer_oninterruptcallback) callback | Callback used to receive interruption events. |
| void\* userData | Pointer to the application data struct that will be passed to the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: A parameter is invalid. For example, the **builder** parameter is nullptr.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetRendererErrorCallback()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererErrorCallback(OH\_AudioStreamBuilder\* builder,OH\_AudioRenderer\_OnErrorCallback callback, void\* userData)

**Description**

Sets the callback for error events of an audio renderer.

This function is similar to [OH\_AudioStreamBuilder\_SetRendererCallback](#oh_audiostreambuilder_setrenderercallback). If both the functions are used, only the last callback takes effect.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioRenderer\_OnErrorCallback](../native-audiorenderer-h/document.md#oh_audiorenderer_onerrorcallback) callback | Callback used to receive error events. |
| void\* userData | Pointer to the application data struct that will be passed to the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: A parameter is invalid. For example, the **builder** parameter is nullptr.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetCapturerReadDataCallback()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerReadDataCallback(OH\_AudioStreamBuilder\* builder,OH\_AudioCapturer\_OnReadDataCallback callback, void\* userData)

**Description**

Sets the callback used to read data for an audio capturer.

This function is similar to [OH\_AudioStreamBuilder\_SetCapturerCallback](#oh_audiostreambuilder_setcapturercallback). If both the functions are used, only the last callback takes effect.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioCapturer\_OnReadDataCallback](../native-audiocapturer-h/document.md#oh_audiocapturer_onreaddatacallback) callback | Callback used to receive data read events. |
| void\* userData | Pointer to the application data struct that will be passed to the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: A parameter is invalid. For example, the **builder** parameter is nullptr.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetCapturerDeviceChangeCallback()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerDeviceChangeCallback(OH\_AudioStreamBuilder\* builder,OH\_AudioCapturer\_OnDeviceChangeCallback callback, void\* userData)

**Description**

Sets the callback for audio capturer device change events.

This function is similar to [OH\_AudioStreamBuilder\_SetCapturerCallback](#oh_audiostreambuilder_setcapturercallback). If both the functions are used, only the last callback takes effect.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioCapturer\_OnDeviceChangeCallback](../native-audiocapturer-h/document.md#oh_audiocapturer_ondevicechangecallback) callback | Callback used to receive device change events. |
| void\* userData | Pointer to the application data struct that will be passed to the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: A parameter is invalid. For example, the **builder** parameter is nullptr.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetCapturerInterruptCallback()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerInterruptCallback(OH\_AudioStreamBuilder\* builder,OH\_AudioCapturer\_OnInterruptCallback callback, void\* userData)

**Description**

Sets the callback for interruption events of an audio capturer.

This function is similar to [OH\_AudioStreamBuilder\_SetCapturerCallback](#oh_audiostreambuilder_setcapturercallback). If both the functions are used, only the last callback takes effect.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioCapturer\_OnInterruptCallback](../native-audiocapturer-h/document.md#oh_audiocapturer_oninterruptcallback) callback | Callback used to receive interruption events. |
| void\* userData | Pointer to the application data struct that will be passed to the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: A parameter is invalid. For example, the **builder** parameter is nullptr.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetCapturerErrorCallback()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerErrorCallback(OH\_AudioStreamBuilder\* builder,OH\_AudioCapturer\_OnErrorCallback callback, void\* userData)

**Description**

Sets the callback for error events of an audio capturer.

This function is similar to [OH\_AudioStreamBuilder\_SetCapturerCallback](#oh_audiostreambuilder_setcapturercallback). If both the functions are used, only the last callback takes effect.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioCapturer\_OnErrorCallback](../native-audiocapturer-h/document.md#oh_audiocapturer_onerrorcallback) callback | Callback used to receive error events. |
| void\* userData | Pointer to the application data struct that will be passed to the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: A parameter is invalid. For example, the **builder** parameter is nullptr.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetCapturerWillMuteWhenInterrupted()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerWillMuteWhenInterrupted(OH\_AudioStreamBuilder\* builder,bool muteWhenInterrupted)

**Description**

Sets whether to mute the audio input stream when an audio interruption occurs.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| bool muteWhenInterrupted | Whether to mute the audio stream when an audio interruption occurs. **true** to mute, **false** otherwise (default interruption mode used). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: A parameter is invalid. For example, the **builder** parameter is nullptr.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetRendererFastStatusChangeCallback()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererFastStatusChangeCallback(OH\_AudioStreamBuilder\* builder,OH\_AudioRenderer\_OnFastStatusChange callback, void\* userData)

**Description**

Sets a callback for low-latency status changes during audio playback.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioRenderer\_OnFastStatusChange](../native-audiorenderer-h/document.md#oh_audiorenderer_onfaststatuschange) callback | Callback invoked for low-latency status changes during audio playback. |
| void\* userData | Pointer to the application data struct that will be passed to the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: A parameter is invalid. For example, the **builder** parameter is nullptr.

 |

#### \[h2\]OH\_AudioStreamBuilder\_SetCapturerFastStatusChangeCallback()

OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerFastStatusChangeCallback(OH\_AudioStreamBuilder\* builder,OH\_AudioCapturer\_OnFastStatusChange callback, void\* userData)

**Description**

Sets a callback for low-latency status changes during audio recording.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioStreamBuilder](../../structs/oh-audiostreambuilderstruct/document.md)\* builder | Pointer to an audio stream builder instance, which is created by calling [OH\_AudioStreamBuilder\_Create](#oh_audiostreambuilder_create). |
| [OH\_AudioCapturer\_OnFastStatusChange](../native-audiocapturer-h/document.md#oh_audiocapturer_onfaststatuschange) callback | Callback invoked for low-latency status changes during audio recording. |
| void\* userData | Pointer to the application data struct that will be passed to the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioStream\_Result](../native-audiostream-base-h/document.md#oh_audiostream_result) | 
**AUDIOSTREAM\_SUCCESS**: The function is executed successfully.

**AUDIOSTREAM\_ERROR\_INVALID\_PARAM**: A parameter is invalid. For example, the **builder** parameter is nullptr.

 |
