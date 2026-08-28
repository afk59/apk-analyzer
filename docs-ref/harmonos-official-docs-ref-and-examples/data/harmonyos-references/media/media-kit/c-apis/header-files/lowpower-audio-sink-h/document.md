# lowpower\_audio\_sink.h

#### Overview

The file declares the native APIs provided by the OH\_LowPowerAudioSink instance. You can use the APIs to implement low-power audio playback.

**File to include**: <multimedia/player\_framework/lowpower\_audio\_sink.h>

**Library**: liblowpower\_avsink.so

**System capability**: SystemCapability.Multimedia.Media.LowPowerAVSink

**Since**: 20

**Related module**: [LowPowerAudioSink](../../modules/lowpoweraudiosink/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink\* OH\_LowPowerAudioSink\_CreateByMime(const char\* mime)](#oh_lowpoweraudiosink_createbymime) | Creates an OH\_LowPowerAudioSink instance. |
| [OH\_AVErrCode OH\_LowPowerAudioSink\_Configure(OH\_LowPowerAudioSink\* sink, const OH\_AVFormat\* format)](#oh_lowpoweraudiosink_configure) | Configures an OH\_LowPowerAudioSink instance. This function must be called before [OH\_LowPowerAudioSink\_Prepare](#oh_lowpoweraudiosink_prepare). |
| [OH\_AVErrCode OH\_LowPowerAudioSink\_SetParameter(OH\_LowPowerAudioSink\* sink, const OH\_AVFormat\* format)](#oh_lowpoweraudiosink_setparameter) | Sets parameters for an OH\_LowPowerAudioSink instance. The parameters can be dynamically set after [OH\_LowPowerAudioSink\_Prepare](#oh_lowpoweraudiosink_prepare). |
| [OH\_AVErrCode OH\_LowPowerAudioSink\_GetParameter(OH\_LowPowerAudioSink\* sink, OH\_AVFormat\* format)](#oh_lowpoweraudiosink_getparameter) | Obtains the parameters of an OH\_LowPowerAudioSink instance. |
| [OH\_AVErrCode OH\_LowPowerAudioSink\_Prepare(OH\_LowPowerAudioSink\* sink)](#oh_lowpoweraudiosink_prepare) | 
Prepares an OH\_LowPowerAudioSink instance for decoding and rendering. This function must be called after [OH\_LowPowerAudioSink\_Configure](#oh_lowpoweraudiosink_configure).

Before calling this function, you must call [OH\_LowPowerVideoSink\_SetSyncAudioSink](../lowpower-video-sink-h/document.md#oh_lowpowervideosink_setsyncaudiosink) of the LowPowerVideoSink.

 |
| [OH\_AVErrCode OH\_LowPowerAudioSink\_Start(OH\_LowPowerAudioSink\* sink)](#oh_lowpoweraudiosink_start) | 

Starts an OH\_LowPowerAudioSink instance. This function must be called after a successful call to [OH\_LowPowerAudioSink\_Prepare](#oh_lowpoweraudiosink_prepare).

After successful startup, the OH\_LowPowerAudioSink instance starts reporting the [OH\_LowPowerAudioSink\_OnDataNeeded](../lowpower-audio-sink-base-h/document.md#oh_lowpoweraudiosink_ondataneeded) event.

 |
| [OH\_AVErrCode OH\_LowPowerAudioSink\_Pause(OH\_LowPowerAudioSink\* sink)](#oh_lowpoweraudiosink_pause) | 

Pauses an OH\_LowPowerAudioSink instance. This function must be called after [OH\_LowPowerAudioSink\_Start](#oh_lowpoweraudiosink_start) or [OH\_LowPowerAudioSink\_Resume](#oh_lowpoweraudiosink_resume).

After successful pause, the OH\_LowPowerAudioSink instance stops reporting the [OH\_LowPowerAudioSink\_OnDataNeeded](../lowpower-audio-sink-base-h/document.md#oh_lowpoweraudiosink_ondataneeded) event.

 |
| [OH\_AVErrCode OH\_LowPowerAudioSink\_Resume(OH\_LowPowerAudioSink\* sink)](#oh_lowpoweraudiosink_resume) | 

Resumes an OH\_LowPowerAudioSink instance. This function must be called after [OH\_LowPowerAudioSink\_Pause](#oh_lowpoweraudiosink_pause).

After successful resumption, the OH\_LowPowerAudioSink instance resumes reporting the [OH\_LowPowerAudioSink\_OnDataNeeded](../lowpower-audio-sink-base-h/document.md#oh_lowpoweraudiosink_ondataneeded) event.

 |
| [OH\_AVErrCode OH\_LowPowerAudioSink\_Flush(OH\_LowPowerAudioSink\* sink)](#oh_lowpoweraudiosink_flush) | 

Clears all input and output data from the decoders and render buffers of an OH\_LowPowerAudioSink instance.

You are not advised to call this function after [OH\_LowPowerAudioSink\_Start](#oh_lowpoweraudiosink_start) or [OH\_LowPowerAudioSink\_Resume](#oh_lowpoweraudiosink_resume).

Note that if the decoder has previously received data, you must input the codec data again.

 |
| [OH\_AVErrCode OH\_LowPowerAudioSink\_Stop(OH\_LowPowerAudioSink\* sink)](#oh_lowpoweraudiosink_stop) | Stops an OH\_LowPowerAudioSink instance. |
| [OH\_AVErrCode OH\_LowPowerAudioSink\_Reset(OH\_LowPowerAudioSink\* sink)](#oh_lowpoweraudiosink_reset) | 

Resets an OH\_LowPowerAudioSink instance.

To reuse the instance, you must call [OH\_LowPowerAudioSink\_Configure](#oh_lowpoweraudiosink_configure) to configure the instance again.

 |
| [OH\_AVErrCode OH\_LowPowerAudioSink\_Destroy(OH\_LowPowerAudioSink\* sink)](#oh_lowpoweraudiosink_destroy) | Clears internal resources of an OH\_LowPowerAudioSink instance and destroys the instance. You only need to call the function once. |
| [OH\_AVErrCode OH\_LowPowerAudioSink\_SetVolume(OH\_LowPowerAudioSink\* sink, const float volume)](#oh_lowpoweraudiosink_setvolume) | Sets the rendering volume for an OH\_LowPowerAudioSink instance. |
| [OH\_AVErrCode OH\_LowPowerAudioSink\_SetLoudnessGain(OH\_LowPowerAudioSink\* sink, float loudnessGain)](#oh_lowpoweraudiosink_setloudnessgain) | Sets the loudness gain for an OH\_LowPowerAudioSink instance. |
| [OH\_AVErrCode OH\_LowPowerAudioSink\_SetPlaybackSpeed(OH\_LowPowerAudioSink\* sink, const float speed)](#oh_lowpoweraudiosink_setplaybackspeed) | Sets the audio rendering speed for an OH\_LowPowerAudioSink instance. |
| [OH\_AVErrCode OH\_LowPowerAudioSink\_ReturnSamples(OH\_LowPowerAudioSink\* sink, OH\_AVSamplesBuffer\* samples)](#oh_lowpoweraudiosink_returnsamples) | Provides a buffer to an OH\_LowPowerAudioSink instance for procesing. |
| [OH\_AVErrCode OH\_LowPowerAudioSink\_RegisterCallback(OH\_LowPowerAudioSink\* sink, OH\_LowPowerAudioSinkCallback\* callback)](#oh_lowpoweraudiosink_registercallback) | Registers a callback for an OH\_LowPowerAudioSink instance. |
| [OH\_LowPowerAudioSinkCallback\* OH\_LowPowerAudioSinkCallback\_Create(void)](#oh_lowpoweraudiosinkcallback_create) | Creates an OH\_LowPowerAudioSinkCallback instance. |
| [OH\_AVErrCode OH\_LowPowerAudioSinkCallback\_Destroy(OH\_LowPowerAudioSinkCallback\* callback)](#oh_lowpoweraudiosinkcallback_destroy) | Destroys an OH\_LowPowerAudioSinkCallback instance. |
| [OH\_AVErrCode OH\_LowPowerAudioSinkCallback\_SetPositionUpdateListener(OH\_LowPowerAudioSinkCallback\* callback, OH\_LowPowerAudioSink\_OnPositionUpdated onPositionUpdated, void\* userData)](#oh_lowpoweraudiosinkcallback_setpositionupdatelistener) | Sets a progress update listener for an OH\_LowPowerAudioSinkCallback instance. |
| [OH\_AVErrCode OH\_LowPowerAudioSinkCallback\_SetDataNeededListener(OH\_LowPowerAudioSinkCallback\* callback, OH\_LowPowerAudioSink\_OnDataNeeded onDataNeeded, void\* userData)](#oh_lowpoweraudiosinkcallback_setdataneededlistener) | Sets a data needed listener for an OH\_LowPowerAudioSinkCallback instance. |
| [OH\_AVErrCode OH\_LowPowerAudioSinkCallback\_SetErrorListener(OH\_LowPowerAudioSinkCallback\* callback, OH\_LowPowerAudioSink\_OnError onError, void\* userData)](#oh_lowpoweraudiosinkcallback_seterrorlistener) | Sets an error listener for an OH\_LowPowerAudioSinkCallback instance. |
| [OH\_AVErrCode OH\_LowPowerAudioSinkCallback\_SetInterruptListener(OH\_LowPowerAudioSinkCallback\* callback, OH\_LowPowerAudioSink\_OnInterrupted onInterrupted, void\* userData)](#oh_lowpoweraudiosinkcallback_setinterruptlistener) | Sets an audio focus interruption listener for an OH\_LowPowerAudioSinkCallback instance. |
| [OH\_AVErrCode OH\_LowPowerAudioSinkCallback\_SetDeviceChangeListener(OH\_LowPowerAudioSinkCallback\* callback, OH\_LowPowerAudioSink\_OnDeviceChanged onDeviceChanged, void\* userData)](#oh_lowpoweraudiosinkcallback_setdevicechangelistener) | Sets an audio device change listener for an OH\_LowPowerAudioSinkCallback instance. |
| [OH\_AVErrCode OH\_LowPowerAudioSinkCallback\_SetEosListener(OH\_LowPowerAudioSinkCallback callback, OH\_LowPowerAudioSink\_OnEos onEos, void userData)](#oh_lowpoweraudiosinkcallback_seteoslistener) | Sets an end-of-stream listener for an OH\_LowPowerAudioSinkCallback instance. |

#### Function Description

#### \[h2\]OH\_LowPowerAudioSink\_CreateByMime()

OH\_LowPowerAudioSink\* OH\_LowPowerAudioSink\_CreateByMime(const char\* mime)

**Description**

Creates an OH\_LowPowerAudioSink instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* mime | Pointer to the MIME type of the audio decoder. For details about the available options, see [AVCODEC\_MIME\_TYPE](../../../../avcodec-kit/c-apis/header-files/native-avcodec-base-h/document.md#variables). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* | Pointer to the OH\_LowPowerAudioSink instance created. If the operation fails, nullptr is returned. |

#### \[h2\]OH\_LowPowerAudioSink\_Configure()

OH\_AVErrCode OH\_LowPowerAudioSink\_Configure(OH\_LowPowerAudioSink\* sink, const OH\_AVFormat\* format)

**Description**

Configures an OH\_LowPowerAudioSink instance. This function must be called before [OH\_LowPowerAudioSink\_Prepare](#oh_lowpoweraudiosink_prepare).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |
| const [OH\_AVFormat](../../../../avcodec-kit/c-apis/structs/oh-avformat/document.md)\* format | Pointer to an OH\_AVFormat instance, which describes the parameters to be configured for the OH\_LowPowerAudioSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_UNSUPPORT**: The format is not supported.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSink\_SetParameter()

OH\_AVErrCode OH\_LowPowerAudioSink\_SetParameter(OH\_LowPowerAudioSink\* sink, const OH\_AVFormat\* format)

**Description**

Sets parameters for an OH\_LowPowerAudioSink instance. The parameters can be dynamically set after [OH\_LowPowerAudioSink\_Prepare](#oh_lowpoweraudiosink_prepare).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |
| const [OH\_AVFormat](../../../../avcodec-kit/c-apis/structs/oh-avformat/document.md)\* format | Pointer to an OH\_AVFormat instance, which describes the parameters configured for an OH\_LowPowerAudioSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_UNSUPPORT**: The format is not supported.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSink\_GetParameter()

OH\_AVErrCode OH\_LowPowerAudioSink\_GetParameter(OH\_LowPowerAudioSink\* sink, OH\_AVFormat\* format)

**Description**

Obtains the parameters of an OH\_LowPowerAudioSink instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |
| [OH\_AVFormat](../../../../avcodec-kit/c-apis/structs/oh-avformat/document.md)\* format | Pointer to an OH\_AVFormat instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSink\_Prepare()

OH\_AVErrCode OH\_LowPowerAudioSink\_Prepare(OH\_LowPowerAudioSink\* sink)

**Description**

Prepares an OH\_LowPowerAudioSink instance for decoding and rendering. This function must be called after [OH\_LowPowerAudioSink\_Configure](#oh_lowpoweraudiosink_configure).

Before calling this function, you must call [OH\_LowPowerVideoSink\_SetSyncAudioSink](../lowpower-video-sink-h/document.md#oh_lowpowervideosink_setsyncaudiosink) of the LowPowerVideoSink.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_UNSUPPORT**: The format is not supported.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSink\_Start()

OH\_AVErrCode OH\_LowPowerAudioSink\_Start(OH\_LowPowerAudioSink\* sink)

**Description**

Starts an OH\_LowPowerAudioSink instance. This function must be called after a successful call to [OH\_LowPowerAudioSink\_Prepare](#oh_lowpoweraudiosink_prepare).

After successful startup, the OH\_LowPowerAudioSink instance starts reporting the [OH\_LowPowerAudioSink\_OnDataNeeded](../lowpower-audio-sink-base-h/document.md#oh_lowpoweraudiosink_ondataneeded) event.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_UNSUPPORT**: The format is not supported.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSink\_Pause()

OH\_AVErrCode OH\_LowPowerAudioSink\_Pause(OH\_LowPowerAudioSink\* sink)

**Description**

Pauses an OH\_LowPowerAudioSink instance. This function must be called after [OH\_LowPowerAudioSink\_Start](#oh_lowpoweraudiosink_start) or [OH\_LowPowerAudioSink\_Resume](#oh_lowpoweraudiosink_resume).

After successful pause, the OH\_LowPowerAudioSink instance stops reporting the [OH\_LowPowerAudioSink\_OnDataNeeded](../lowpower-audio-sink-base-h/document.md#oh_lowpoweraudiosink_ondataneeded) event.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSink\_Resume()

OH\_AVErrCode OH\_LowPowerAudioSink\_Resume(OH\_LowPowerAudioSink\* sink)

**Description**

Resumes an OH\_LowPowerAudioSink instance. This function must be called after [OH\_LowPowerAudioSink\_Pause](#oh_lowpoweraudiosink_pause).

After successful resumption, the OH\_LowPowerAudioSink instance resumes reporting the [OH\_LowPowerAudioSink\_OnDataNeeded](../lowpower-audio-sink-base-h/document.md#oh_lowpoweraudiosink_ondataneeded) event.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSink\_Flush()

OH\_AVErrCode OH\_LowPowerAudioSink\_Flush(OH\_LowPowerAudioSink\* sink)

**Description**

Clears all input and output data from the decoders and render buffers of an OH\_LowPowerAudioSink instance.

You are not advised to call this function after [OH\_LowPowerAudioSink\_Start](#oh_lowpoweraudiosink_start) or [OH\_LowPowerAudioSink\_Resume](#oh_lowpoweraudiosink_resume).

Note that if the decoder has previously received data, you must input the codec data again.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSink\_Stop()

OH\_AVErrCode OH\_LowPowerAudioSink\_Stop(OH\_LowPowerAudioSink\* sink)

**Description**

Stops an OH\_LowPowerAudioSink instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSink\_Reset()

OH\_AVErrCode OH\_LowPowerAudioSink\_Reset(OH\_LowPowerAudioSink\* sink)

**Description**

Resets an OH\_LowPowerAudioSink instance.

To reuse the instance, you must call [OH\_LowPowerAudioSink\_Configure](#oh_lowpoweraudiosink_configure) to configure the instance again.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSink\_Destroy()

OH\_AVErrCode OH\_LowPowerAudioSink\_Destroy(OH\_LowPowerAudioSink\* sink)

**Description**

Clears internal resources of an OH\_LowPowerAudioSink instance and destroys the instance. You only need to call the function once.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSink\_SetVolume()

OH\_AVErrCode OH\_LowPowerAudioSink\_SetVolume(OH\_LowPowerAudioSink\* sink, const float volume)

**Description**

Sets the rendering volume for an OH\_LowPowerAudioSink instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |
| const float volume | Rendering volume, in the range of \[0.0, 1.0\]. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSink\_SetLoudnessGain()

OH\_AVErrCode OH\_LowPowerAudioSink\_SetLoudnessGain(OH\_LowPowerAudioSink\* sink, float loudnessGain)

**Description**

Sets the loudness gain for an OH\_LowPowerAudioSink instance.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |
| float loudnessGain | Loudness gain, in the range \[-90.0, 24.0\]. The default value is 0.0 dB. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

 |

#### \[h2\]OH\_LowPowerAudioSink\_SetPlaybackSpeed()

OH\_AVErrCode OH\_LowPowerAudioSink\_SetPlaybackSpeed(OH\_LowPowerAudioSink\* sink, const float speed)

**Description**

Sets the audio rendering speed for an OH\_LowPowerAudioSink instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |
| const float speed | Audio rendering speed, in the range \[0.25, 4.0\]. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSink\_ReturnSamples()

OH\_AVErrCode OH\_LowPowerAudioSink\_ReturnSamples(OH\_LowPowerAudioSink\* sink, OH\_AVSamplesBuffer\* samples)

**Description**

Provides a buffer to an OH\_LowPowerAudioSink instance for procesing.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |
| [OH\_AVSamplesBuffer](../../structs/oh-avsamplesbuffer/document.md)\* samples | Pointer to the OH\_AVSamplesBuffer instance to be provided. Batch input of samples is supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSink\_RegisterCallback()

OH\_AVErrCode OH\_LowPowerAudioSink\_RegisterCallback(OH\_LowPowerAudioSink\* sink, OH\_LowPowerAudioSinkCallback\* callback)

**Description**

Registers a callback for an OH\_LowPowerAudioSink instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |
| [OH\_LowPowerAudioSinkCallback](../../structs/oh-lowpoweraudiosinkcallback/document.md)\* callback | Pointer to an OH\_LowPowerAudioSinkCallback instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSinkCallback\_Create()

OH\_LowPowerAudioSinkCallback\* OH\_LowPowerAudioSinkCallback\_Create(void)

**Description**

Creates an OH\_LowPowerAudioSinkCallback instance.

**Since**: 20

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSinkCallback](../../structs/oh-lowpoweraudiosinkcallback/document.md)\* | Pointer to the OH\_LowPowerAudioSinkCallback instance created. If the memory is insufficient, nullptr is returned. |

#### \[h2\]OH\_LowPowerAudioSinkCallback\_Destroy()

OH\_AVErrCode OH\_LowPowerAudioSinkCallback\_Destroy(OH\_LowPowerAudioSinkCallback\* callback)

**Description**

Destroys an OH\_LowPowerAudioSinkCallback instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSinkCallback](../../structs/oh-lowpoweraudiosinkcallback/document.md)\* callback | Pointer to an OH\_LowPowerAudioSinkCallback instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

 |

#### \[h2\]OH\_LowPowerAudioSinkCallback\_SetPositionUpdateListener()

OH\_AVErrCode OH\_LowPowerAudioSinkCallback\_SetPositionUpdateListener(OH\_LowPowerAudioSinkCallback\* callback, OH\_LowPowerAudioSink\_OnPositionUpdated onPositionUpdated, void\* userData)

**Description**

Sets a progress update listener for an OH\_LowPowerAudioSinkCallback instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSinkCallback](../../structs/oh-lowpoweraudiosinkcallback/document.md)\* callback | Pointer to an OH\_LowPowerAudioSinkCallback instance. |
| [OH\_LowPowerAudioSink\_OnPositionUpdated](../lowpower-audio-sink-base-h/document.md#oh_lowpoweraudiosink_onpositionupdated) onPositionUpdated | OH\_LowPowerAudioSink\_OnPositionUpdated, which is invoked when the playback position is updated in the OH\_LowPowerAudioSink instance. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSinkCallback\_SetDataNeededListener()

OH\_AVErrCode OH\_LowPowerAudioSinkCallback\_SetDataNeededListener(OH\_LowPowerAudioSinkCallback\* callback, OH\_LowPowerAudioSink\_OnDataNeeded onDataNeeded, void\* userData)

**Description**

Sets a data needed listener for an OH\_LowPowerAudioSinkCallback instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSinkCallback](../../structs/oh-lowpoweraudiosinkcallback/document.md)\* callback | Pointer to an OH\_LowPowerAudioSinkCallback instance. |
| [OH\_LowPowerAudioSink\_OnDataNeeded](../lowpower-audio-sink-base-h/document.md#oh_lowpoweraudiosink_ondataneeded) onDataNeeded | OH\_LowPowerAudioSink\_OnDataNeeded, which is invoked when the OH\_LowPowerAudioSink instance needs more data. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSinkCallback\_SetErrorListener()

OH\_AVErrCode OH\_LowPowerAudioSinkCallback\_SetErrorListener(OH\_LowPowerAudioSinkCallback\* callback, OH\_LowPowerAudioSink\_OnError onError, void\* userData)

**Description**

Sets an error listener for an OH\_LowPowerAudioSinkCallback instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSinkCallback](../../structs/oh-lowpoweraudiosinkcallback/document.md)\* callback | Pointer to an OH\_LowPowerAudioSinkCallback instance. |
| [OH\_LowPowerAudioSink\_OnError](../lowpower-audio-sink-base-h/document.md#oh_lowpoweraudiosink_onerror) onError | OH\_LowPowerAudioSink\_OnError, which is invoked when an error occurs in the OH\_LowPowerAudioSink instance. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSinkCallback\_SetInterruptListener()

OH\_AVErrCode OH\_LowPowerAudioSinkCallback\_SetInterruptListener(OH\_LowPowerAudioSinkCallback\* callback, OH\_LowPowerAudioSink\_OnInterrupted onInterrupted, void\* userData)

**Description**

Sets an audio focus interruption listener for an OH\_LowPowerAudioSinkCallback instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSinkCallback](../../structs/oh-lowpoweraudiosinkcallback/document.md)\* callback | Pointer to an OH\_LowPowerAudioSinkCallback instance. |
| [OH\_LowPowerAudioSink\_OnInterrupted](../lowpower-audio-sink-base-h/document.md#oh_lowpoweraudiosink_oninterrupted) onInterrupted | OH\_LowPowerAudioSink\_OnInterrupted, which is invoked when the audio focus is interrupted in the OH\_LowPowerAudioSink instance. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSinkCallback\_SetDeviceChangeListener()

OH\_AVErrCode OH\_LowPowerAudioSinkCallback\_SetDeviceChangeListener(OH\_LowPowerAudioSinkCallback\* callback, OH\_LowPowerAudioSink\_OnDeviceChanged onDeviceChanged, void\* userData)

**Description**

Sets an audio device change listener for an OH\_LowPowerAudioSinkCallback instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSinkCallback](../../structs/oh-lowpoweraudiosinkcallback/document.md)\* callback | Pointer to an OH\_LowPowerAudioSinkCallback instance. |
| [OH\_LowPowerAudioSink\_OnDeviceChanged](../lowpower-audio-sink-base-h/document.md#oh_lowpoweraudiosink_ondevicechanged) onDeviceChanged | OH\_LowPowerAudioSink\_OnDeviceChanged, which is invoked when the audio device changes in the OH\_LowPowerAudioSink instance. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerAudioSinkCallback\_SetEosListener()

OH\_AVErrCode OH\_LowPowerAudioSinkCallback\_SetEosListener(OH\_LowPowerAudioSinkCallback \*callback, OH\_LowPowerAudioSink\_OnEos onEos, void\* userData)

**Description**

Sets an end-of-stream listener for an OH\_LowPowerAudioSinkCallback instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSinkCallback](../../structs/oh-lowpoweraudiosinkcallback/document.md) \*callback | Pointer to an OH\_LowPowerAudioSinkCallback instance. |
| [OH\_LowPowerAudioSink\_OnEos](../lowpower-audio-sink-base-h/document.md#oh_lowpoweraudiosink_oneos) onEos | OH\_LowPowerAudioSink\_OnEos, which is invoked when playback is complete in the OH\_LowPowerAudioSink instance. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |
