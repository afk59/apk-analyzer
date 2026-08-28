# lowpower\_video\_sink.h

#### Overview

The file declares the native APIs provided by the LowPowerVideoSink. You can use the APIs to implement low-power video playback.

**File to include**: <multimedia/player\_framework/lowpower\_video\_sink.h>

**Library**: liblowpower\_avsink.so

**System capability**: SystemCapability.Multimedia.Media.LowPowerAVSink

**Since**: 20

**Related module**: [LowPowerVideoSink](../../modules/lowpowervideosink/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink\* OH\_LowPowerVideoSink\_CreateByMime(const char\* mime)](#oh_lowpowervideosink_createbymime) | Creates an OH\_LowPowerVideoSink instance. |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_Configure(OH\_LowPowerVideoSink\* sink, const OH\_AVFormat\* format)](#oh_lowpowervideosink_configure) | Configures an OH\_LowPowerVideoSink instance. This function must be called before [OH\_LowPowerVideoSink\_Prepare](#oh_lowpowervideosink_prepare). |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_SetParameter(OH\_LowPowerVideoSink\* sink, const OH\_AVFormat\* format)](#oh_lowpowervideosink_setparameter) | Sets parameters for an OH\_LowPowerVideoSink instance. The parameters can be dynamically set after [OH\_LowPowerVideoSink\_Prepare](#oh_lowpowervideosink_prepare). |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_GetParameter(OH\_LowPowerVideoSink\* sink, OH\_AVFormat\* format)](#oh_lowpowervideosink_getparameter) | Obtains the parameters of an OH\_LowPowerVideoSink instance. |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_SetVideoSurface(OH\_LowPowerVideoSink\* sink, const OHNativeWindow\* surface)](#oh_lowpowervideosink_setvideosurface) | Sets the rendering window for an OH\_LowPowerVideoSink instance. This function must be called before [OH\_LowPowerVideoSink\_Prepare](#oh_lowpowervideosink_prepare). |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_Prepare(OH\_LowPowerVideoSink\* sink)](#oh_lowpowervideosink_prepare) | Prepares an OH\_LowPowerVideoSink instance for decoding and rendering. This function must be called after [OH\_LowPowerVideoSink\_SetSyncAudioSink](#oh_lowpowervideosink_setsyncaudiosink). |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_StartDecoder(OH\_LowPowerVideoSink\* sink)](#oh_lowpowervideosink_startdecoder) | 
Starts an OH\_LowPowerVideoSink instance for decoding. This function must be called after [OH\_LowPowerVideoSink\_Prepare](#oh_lowpowervideosink_prepare) or if no video is playing, after [OH\_LowPowerVideoSink\_SetTargetStartFrame](#oh_lowpowervideosink_settargetstartframe).

After successful startup, the OH\_LowPowerVideoSink instance starts reporting the [OH\_LowPowerVideoSink\_OnDataNeeded](../lowpower-video-sink-base-h/document.md#oh_lowpowervideosink_ondataneeded) event.

 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_RenderFirstFrame(OH\_LowPowerVideoSink\* sink)](#oh_lowpowervideosink_renderfirstframe) | Renders the first frame decoded by an OH\_LowPowerVideoSink instance. This function must be called after [OH\_LowPowerVideoSink\_StartDecoder](#oh_lowpowervideosink_startdecoder). |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_StartRenderer(OH\_LowPowerVideoSink\* sink)](#oh_lowpowervideosink_startrenderer) | Starts an OH\_LowPowerVideoSink instance for rendering. This function must be called after [OH\_LowPowerVideoSink\_StartDecoder](#oh_lowpowervideosink_startdecoder). |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_Pause(OH\_LowPowerVideoSink\* sink)](#oh_lowpowervideosink_pause) | 

Pauses an OH\_LowPowerVideoSink instance. This function must be called after [OH\_LowPowerVideoSink\_StartRenderer](#oh_lowpowervideosink_startrenderer) or [OH\_LowPowerVideoSink\_Resume](#oh_lowpowervideosink_resume).

After successful pause, the OH\_LowPowerVideoSink instance stops reporting the [OH\_LowPowerVideoSink\_OnDataNeeded](../lowpower-video-sink-base-h/document.md#oh_lowpowervideosink_ondataneeded) event.

 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_Resume(OH\_LowPowerVideoSink\* sink)](#oh_lowpowervideosink_resume) | 

Resumes an OH\_LowPowerVideoSink instance. This function must be called after[OH\_LowPowerVideoSink\_Pause](#oh_lowpowervideosink_pause).

After successful resumption, the OH\_LowPowerVideoSink instance resumes reporting the [OH\_LowPowerVideoSink\_OnDataNeeded](../lowpower-video-sink-base-h/document.md#oh_lowpowervideosink_ondataneeded) event.

 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_Flush(OH\_LowPowerVideoSink\* sink)](#oh_lowpowervideosink_flush) | 

Clears all input and output data from the decoders and render buffers of an OH\_LowPowerVideoSink instance.

You are not advised to call this function after [OH\_LowPowerVideoSink\_StartRenderer](#oh_lowpowervideosink_startrenderer) or [OH\_LowPowerVideoSink\_Resume](#oh_lowpowervideosink_resume).

Note that if the decoder has previously received data, you must input the codec data again.

 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_Stop(OH\_LowPowerVideoSink\* sink)](#oh_lowpowervideosink_stop) | Stops an OH\_LowPowerVideoSink instance. |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_Reset(OH\_LowPowerVideoSink\* sink)](#oh_lowpowervideosink_reset) | 

Resets an OH\_LowPowerVideoSink instance.

To reuse the instance, you must call [OH\_LowPowerVideoSink\_Configure](#oh_lowpowervideosink_configure) to configure the instance again.

 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_Destroy(OH\_LowPowerVideoSink\* sink)](#oh_lowpowervideosink_destroy) | Clears internal resources of an OH\_LowPowerVideoSink instance and destroys the instance. You only need to call the function once. |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_SetSyncAudioSink(OH\_LowPowerVideoSink\* videoSink, OH\_LowPowerAudioSink\* audioSink)](#oh_lowpowervideosink_setsyncaudiosink) | Sets an OH\_LowPowerAudioSink instance for audio-video synchronization in an OH\_LowPowerVideoSink instance. |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_SetTargetStartFrame(OH\_LowPowerVideoSink\* sink, const int64\_t framePts, OH\_LowPowerVideoSink\_OnTargetArrived onTargetArrived, const int64\_t timeoutMs, void\* userData)](#oh_lowpowervideosink_settargetstartframe) | Sets the target rendering frame for an OH\_LowPowerVideoSink instance. |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_SetPlaybackSpeed(OH\_LowPowerVideoSink\* sink, const float speed)](#oh_lowpowervideosink_setplaybackspeed) | Sets the playback speed for an OH\_LowPowerVideoSink instance. |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_ReturnSamples(OH\_LowPowerVideoSink\* sink, OH\_AVSamplesBuffer\* samples)](#oh_lowpowervideosink_returnsamples) | Provides a buffer to an OH\_LowPowerVideoSink instance for procesing. |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_GetLatestPts(OH\_LowPowerVideoSink \*sink, int64\_t \*pts)](#oh_lowpowervideosink_getlatestpts) | Obtains the Presentation Timestamp (PTS) of the video that is playing. |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_RegisterCallback(OH\_LowPowerVideoSink\* sink, OH\_LowPowerVideoSinkCallback\* callback)](#oh_lowpowervideosink_registercallback) | Registers a callback for an OH\_LowPowerVideoSink instance. |
| [OH\_LowPowerVideoSinkCallback\* OH\_LowPowerVideoSinkCallback\_Create(void)](#oh_lowpowervideosinkcallback_create) | Creates an OH\_LowPowerVideoSinkCallback instance. |
| [OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_Destroy(OH\_LowPowerVideoSinkCallback\* callback)](#oh_lowpowervideosinkcallback_destroy) | Destroys an OH\_LowPowerVideoSinkCallback instance. |
| [OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetDataNeededListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnDataNeeded onDataNeeded, void\* userData)](#oh_lowpowervideosinkcallback_setdataneededlistener) | Sets a data needed listener for an OH\_LowPowerVideoSinkCallback instance. |
| [OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetErrorListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnError onError, void\* userData)](#oh_lowpowervideosinkcallback_seterrorlistener) | Sets an error listener for an OH\_LowPowerVideoSinkCallback instance. |
| [OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetRenderStartListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnRenderStarted onRenderStarted, void\* userData)](#oh_lowpowervideosinkcallback_setrenderstartlistener) | Sets a render start listener for an OH\_LowPowerVideoSinkCallback instance. |
| [OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetStreamChangedListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnStreamChanged onStreamChanged, void\* userData)](#oh_lowpowervideosinkcallback_setstreamchangedlistener) | Sets a stream change listener for an OH\_LowPowerVideoSinkCallback instance. |
| [OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetFirstFrameDecodedListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnFirstFrameDecoded onFirstFrameDecoded, void\* userData)](#oh_lowpowervideosinkcallback_setfirstframedecodedlistener) | Sets a first-frame ready listener for an OH\_LowPowerVideoSinkCallback instance. |
| [OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetEosListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnEos onEos, void\* userData)](#oh_lowpowervideosinkcallback_seteoslistener) | Sets an end-of-stream listener for an OH\_LowPowerVideoSinkCallback instance. |

#### Function Description

#### \[h2\]OH\_LowPowerVideoSink\_CreateByMime()

OH\_LowPowerVideoSink\* OH\_LowPowerVideoSink\_CreateByMime(const char\* mime)

**Description**

Creates an OH\_LowPowerVideoSink instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* mime | Pointer to the MIME type of the video decoder. For details about the available options, see [AVCODEC\_MIME\_TYPE](../../../../avcodec-kit/c-apis/header-files/native-avcodec-base-h/document.md#variables). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* | Pointer to the OH\_LowPowerVideoSink instance created. If the operation fails, nullptr is returned. |

#### \[h2\]OH\_LowPowerVideoSink\_Configure()

OH\_AVErrCode OH\_LowPowerVideoSink\_Configure(OH\_LowPowerVideoSink\* sink, const OH\_AVFormat\* format)

**Description**

Configures an OH\_LowPowerVideoSink instance. This function must be called before [OH\_LowPowerVideoSink\_Prepare](#oh_lowpowervideosink_prepare).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |
| const [OH\_AVFormat](../../../../avcodec-kit/c-apis/structs/oh-avformat/document.md)\* format | Pointer to an OH\_AVFormat instance, which describes the parameters to be configured for the OH\_LowPowerVideoSink instance. |

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

#### \[h2\]OH\_LowPowerVideoSink\_SetParameter()

OH\_AVErrCode OH\_LowPowerVideoSink\_SetParameter(OH\_LowPowerVideoSink\* sink, const OH\_AVFormat\* format)

**Description**

Sets parameters for an OH\_LowPowerVideoSink instance. The parameters can be dynamically set after [OH\_LowPowerVideoSink\_Prepare](#oh_lowpowervideosink_prepare).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |
| const [OH\_AVFormat](../../../../avcodec-kit/c-apis/structs/oh-avformat/document.md)\* format | Pointer to an OH\_AVFormat instance, which describes the parameters to be configured for the OH\_LowPowerVideoSink instance. |

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

#### \[h2\]OH\_LowPowerVideoSink\_GetParameter()

OH\_AVErrCode OH\_LowPowerVideoSink\_GetParameter(OH\_LowPowerVideoSink\* sink, OH\_AVFormat\* format)

**Description**

Obtains the parameters of an OH\_LowPowerVideoSink instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |
| [OH\_AVFormat](../../../../avcodec-kit/c-apis/structs/oh-avformat/document.md)\* format | Pointer to an OH\_AVFormat instance, which describes the parameters configured for an OH\_LowPowerVideoSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSink\_SetVideoSurface()

OH\_AVErrCode OH\_LowPowerVideoSink\_SetVideoSurface(OH\_LowPowerVideoSink\* sink, const OHNativeWindow\* surface)

**Description**

Sets the rendering window for an OH\_LowPowerVideoSink instance. This function must be called before [OH\_LowPowerVideoSink\_Prepare](#oh_lowpowervideosink_prepare).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |
| const [OHNativeWindow](../../../../avcodec-kit/c-apis/structs/nativewindow/document.md)\* surface | Pointer to the OHNativeWindow instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSink\_Prepare()

OH\_AVErrCode OH\_LowPowerVideoSink\_Prepare(OH\_LowPowerVideoSink\* sink)

**Description**

Prepares an OH\_LowPowerVideoSink instance for decoding and rendering. This function must be called after [OH\_LowPowerVideoSink\_SetSyncAudioSink](#oh_lowpowervideosink_setsyncaudiosink).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |

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

#### \[h2\]OH\_LowPowerVideoSink\_StartDecoder()

OH\_AVErrCode OH\_LowPowerVideoSink\_StartDecoder(OH\_LowPowerVideoSink\* sink)

**Description**

Starts an OH\_LowPowerVideoSink instance for decoding. This function must be called after [OH\_LowPowerVideoSink\_Prepare](#oh_lowpowervideosink_prepare) or if no video is playing, after [OH\_LowPowerVideoSink\_SetTargetStartFrame](#oh_lowpowervideosink_settargetstartframe).

After successful startup, the OH\_LowPowerVideoSink instance starts reporting the [OH\_LowPowerVideoSink\_OnDataNeeded](../lowpower-video-sink-base-h/document.md#oh_lowpowervideosink_ondataneeded) event.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |

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

#### \[h2\]OH\_LowPowerVideoSink\_RenderFirstFrame()

OH\_AVErrCode OH\_LowPowerVideoSink\_RenderFirstFrame(OH\_LowPowerVideoSink\* sink)

**Description**

Renders the first frame decoded by an OH\_LowPowerVideoSink instance. This function must be called after [OH\_LowPowerVideoSink\_StartDecoder](#oh_lowpowervideosink_startdecoder).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSink\_StartRenderer()

OH\_AVErrCode OH\_LowPowerVideoSink\_StartRenderer(OH\_LowPowerVideoSink\* sink)

**Description**

Starts an OH\_LowPowerVideoSink instance for rendering. This function must be called after [OH\_LowPowerVideoSink\_StartDecoder](#oh_lowpowervideosink_startdecoder).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |

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

#### \[h2\]OH\_LowPowerVideoSink\_Pause()

OH\_AVErrCode OH\_LowPowerVideoSink\_Pause(OH\_LowPowerVideoSink\* sink)

**Description**

Pauses an OH\_LowPowerVideoSink instance. This function must be called after [OH\_LowPowerVideoSink\_StartRenderer](#oh_lowpowervideosink_startrenderer) or [OH\_LowPowerVideoSink\_Resume](#oh_lowpowervideosink_resume).

After successful pause, the OH\_LowPowerVideoSink instance stops reporting the [OH\_LowPowerVideoSink\_OnDataNeeded](../lowpower-video-sink-base-h/document.md#oh_lowpowervideosink_ondataneeded) event.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSink\_Resume()

OH\_AVErrCode OH\_LowPowerVideoSink\_Resume(OH\_LowPowerVideoSink\* sink)

**Description**

Resumes an OH\_LowPowerVideoSink instance. This function must be called after[OH\_LowPowerVideoSink\_Pause](#oh_lowpowervideosink_pause).

After successful resumption, the OH\_LowPowerVideoSink instance resumes reporting the [OH\_LowPowerVideoSink\_OnDataNeeded](../lowpower-video-sink-base-h/document.md#oh_lowpowervideosink_ondataneeded) event.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSink\_Flush()

OH\_AVErrCode OH\_LowPowerVideoSink\_Flush(OH\_LowPowerVideoSink\* sink)

**Description**

Clears all input and output data from the decoders and render buffers of an OH\_LowPowerVideoSink instance.

You are not advised to call this function after [OH\_LowPowerVideoSink\_StartRenderer](#oh_lowpowervideosink_startrenderer) or [OH\_LowPowerVideoSink\_Resume](#oh_lowpowervideosink_resume).

Note that if the decoder has previously received data, you must input the codec data again.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSink\_Stop()

OH\_AVErrCode OH\_LowPowerVideoSink\_Stop(OH\_LowPowerVideoSink\* sink)

**Description**

Stops an OH\_LowPowerVideoSink instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSink\_Reset()

OH\_AVErrCode OH\_LowPowerVideoSink\_Reset(OH\_LowPowerVideoSink\* sink)

**Description**

Resets an OH\_LowPowerVideoSink instance.

To reuse the instance, you must call [OH\_LowPowerVideoSink\_Configure](#oh_lowpowervideosink_configure) to configure the instance again.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSink\_Destroy()

OH\_AVErrCode OH\_LowPowerVideoSink\_Destroy(OH\_LowPowerVideoSink\* sink)

**Description**

Clears internal resources of an OH\_LowPowerVideoSink instance and destroys the instance. You only need to call the function once.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSink\_SetSyncAudioSink()

OH\_AVErrCode OH\_LowPowerVideoSink\_SetSyncAudioSink(OH\_LowPowerVideoSink\* videoSink, OH\_LowPowerAudioSink\* audioSink)

**Description**

Sets an OH\_LowPowerAudioSink instance for audio-video synchronization in an OH\_LowPowerVideoSink instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* videoSink | Pointer to an OH\_LowPowerVideoSink instance. |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* audioSink | Pointer to an OH\_LowPowerAudioSink instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSink\_SetTargetStartFrame()

OH\_AVErrCode OH\_LowPowerVideoSink\_SetTargetStartFrame(OH\_LowPowerVideoSink\* sink, const int64\_t framePts, OH\_LowPowerVideoSink\_OnTargetArrived onTargetArrived, const int64\_t timeoutMs, void\* userData)

**Description**

Sets the target rendering frame for an OH\_LowPowerVideoSink instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |
| const int64\_t framePts | Presentation timestamp (PTS) of the target video frame to render. |
| [OH\_LowPowerVideoSink\_OnTargetArrived](../lowpower-video-sink-base-h/document.md#oh_lowpowervideosink_ontargetarrived) onTargetArrived | OH\_LowPowerVideoSink\_OnTargetArrived, which is invoked when the target frame is rendered. |
| const int64\_t timeoutMs | Time wait for the first frame to finish rendering. If the first frame does not finish rendering within the specified time, the OH\_LowPowerVideoSink\_OnTargetArrived callback is directly invoked. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSink\_SetPlaybackSpeed()

OH\_AVErrCode OH\_LowPowerVideoSink\_SetPlaybackSpeed(OH\_LowPowerVideoSink\* sink, const float speed)

**Description**

Sets the playback speed for an OH\_LowPowerVideoSink instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |
| const float speed | Playback speed, in the range \[0.1, 4.0\]. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSink\_ReturnSamples()

OH\_AVErrCode OH\_LowPowerVideoSink\_ReturnSamples(OH\_LowPowerVideoSink\* sink, OH\_AVSamplesBuffer\* samples)

**Description**

Provides a buffer to an OH\_LowPowerVideoSink instance for procesing.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |
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

#### \[h2\]OH\_LowPowerVideoSink\_GetLatestPts()

OH\_AVErrCode OH\_LowPowerVideoSink\_GetLatestPts(OH\_LowPowerVideoSink \*sink, int64\_t \*pts)

**Description**

Obtains the Presentation Timestamp (PTS) of the video that is playing.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md) \*sink | Pointer to an OH\_LowPowerVideoSink instance. |
| int64\_t \*pts | Pointer to the PTS of the video. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSink\_RegisterCallback()

OH\_AVErrCode OH\_LowPowerVideoSink\_RegisterCallback(OH\_LowPowerVideoSink\* sink, OH\_LowPowerVideoSinkCallback\* callback)

**Description**

Registers a callback for an OH\_LowPowerVideoSink instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |
| [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md)\* callback | Pointer to an OH\_LowPowerVideoSinkCallback instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_SERVICE\_DIED**: The media server is destroyed.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSinkCallback\_Create()

OH\_LowPowerVideoSinkCallback\* OH\_LowPowerVideoSinkCallback\_Create(void)

**Description**

Creates an OH\_LowPowerVideoSinkCallback instance.

**Since**: 20

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md)\* | Pointer to the OH\_LowPowerVideoSinkCallback instance created. If the memory is insufficient, nullptr is returned. |

#### \[h2\]OH\_LowPowerVideoSinkCallback\_Destroy()

OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_Destroy(OH\_LowPowerVideoSinkCallback\* callback)

**Description**

Destroys an OH\_LowPowerVideoSinkCallback instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md)\* callback | Pointer to an OH\_LowPowerVideoSinkCallback instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

 |

#### \[h2\]OH\_LowPowerVideoSinkCallback\_SetDataNeededListener()

OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetDataNeededListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnDataNeeded onDataNeeded, void\* userData)

**Description**

Sets a data needed listener for an OH\_LowPowerVideoSinkCallback instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md)\* callback | Pointer to an OH\_LowPowerVideoSinkCallback instance. |
| [OH\_LowPowerVideoSink\_OnDataNeeded](../lowpower-video-sink-base-h/document.md#oh_lowpowervideosink_ondataneeded) onDataNeeded | OH\_LowPowerVideoSink\_OnDataNeeded, which is invoked when the OH\_LowPowerVideoSink instance needs more data. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSinkCallback\_SetErrorListener()

OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetErrorListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnError onError, void\* userData)

**Description**

Sets an error listener for an OH\_LowPowerVideoSinkCallback instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md)\* callback | Pointer to an OH\_LowPowerVideoSinkCallback instance. |
| [OH\_LowPowerVideoSink\_OnError](../lowpower-video-sink-base-h/document.md#oh_lowpowervideosink_onerror) onError | OH\_LowPowerVideoSink\_OnError, which is invoked when an error occurs in the OH\_LowPowerVideoSink instance. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSinkCallback\_SetRenderStartListener()

OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetRenderStartListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnRenderStarted onRenderStarted, void\* userData)

**Description**

Sets a render start listener for an OH\_LowPowerVideoSinkCallback instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md)\* callback | Pointer to an OH\_LowPowerVideoSinkCallback instance. |
| [OH\_LowPowerVideoSink\_OnRenderStarted](../lowpower-video-sink-base-h/document.md#oh_lowpowervideosink_onrenderstarted) onRenderStarted | OH\_LowPowerVideoSink\_OnRenderStarted, which is invoked when rendering starts in the OH\_LowPowerVideoSink instance. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSinkCallback\_SetStreamChangedListener()

OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetStreamChangedListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnStreamChanged onStreamChanged, void\* userData)

**Description**

Sets a stream change listener for an OH\_LowPowerVideoSinkCallback instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md)\* callback | Pointer to an OH\_LowPowerVideoSinkCallback instance. |
| [OH\_LowPowerVideoSink\_OnStreamChanged](../lowpower-video-sink-base-h/document.md#oh_lowpowervideosink_onstreamchanged) onStreamChanged | OH\_LowPowerVideoSink\_OnStreamChanged, which is invoked when the stream changes in the OH\_LowPowerVideoSink instance. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSinkCallback\_SetFirstFrameDecodedListener()

OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetFirstFrameDecodedListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnFirstFrameDecoded onFirstFrameDecoded, void\* userData)

**Description**

Sets a first-frame ready listener for an OH\_LowPowerVideoSinkCallback instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md)\* callback | Pointer to an OH\_LowPowerVideoSinkCallback instance. |
| [OH\_LowPowerVideoSink\_OnFirstFrameDecoded](../lowpower-video-sink-base-h/document.md#oh_lowpowervideosink_onfirstframedecoded) onFirstFrameDecoded | OH\_LowPowerVideoSink\_OnFirstFrameReady, which is invoked when the first frame is ready in the OH\_LowPowerVideoSink instance. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |

#### \[h2\]OH\_LowPowerVideoSinkCallback\_SetEosListener()

OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetEosListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnEos onEos, void\* userData)

**Description**

Sets an end-of-stream listener for an OH\_LowPowerVideoSinkCallback instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md)\* callback | Pointer to an OH\_LowPowerVideoSinkCallback instance. |
| [OH\_LowPowerVideoSink\_OnEos](../lowpower-video-sink-base-h/document.md#oh_lowpowervideosink_oneos) onEos | OH\_LowPowerVideoSink\_OnEos, which is invoked when playback is complete in the OH\_LowPowerVideoSink instance. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not supported.

 |
