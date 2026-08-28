# avtranscoder.h

#### Overview

The file declares the native APIs provided by the AVTranscoder. You can use the APIs to transcode a source video file into a new video file.

**File to include**: <multimedia/player\_framework/avtranscoder.h>

**Library**: libavtranscoder.so

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Related module**: [AVTranscoder](../../modules/avtranscoder/document.md)

**Sample**: [AVPlayerNDKVideo](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVPlayer/AVPlayerNDK)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder\_Config \*OH\_AVTranscoderConfig\_Create()](#oh_avtranscoderconfig_create) | Creates an instance of the transcoding configuration parameters. |
| [OH\_AVErrCode OH\_AVTranscoderConfig\_Release(OH\_AVTranscoder\_Config\* config)](#oh_avtranscoderconfig_release) | 
Releases the resources of the transcoding configuration parameters.

After a successful call, the instance specified by **config** is released and set to nullptr.

 |
| [OH\_AVErrCode OH\_AVTranscoderConfig\_SetSrcFD(OH\_AVTranscoder\_Config \*config, int32\_t srcFd, int64\_t srcOffset, int64\_t length)](#oh_avtranscoderconfig_setsrcfd) | 

Sets the file descriptor of the source video for transcoding.

This function must be called before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare).

 |
| [OH\_AVErrCode OH\_AVTranscoderConfig\_SetDstFD(OH\_AVTranscoder\_Config \*config, int32\_t dstFd)](#oh_avtranscoderconfig_setdstfd) | 

Sets the file descriptor of the output video for transcoding.

This function must be called before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare).

 |
| [OH\_AVErrCode OH\_AVTranscoderConfig\_SetDstVideoType(OH\_AVTranscoder\_Config \*config, const char \*mimeType)](#oh_avtranscoderconfig_setdstvideotype) | 

Sets the encoding format of the output video for transcoding.

Currently, only AVC and HEVC are supported. If the source video is in HEVC format, the default value is **HEVC**. Otherwise, the default value is **AVC**.

This function must be called before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare).

 |
| [OH\_AVErrCode OH\_AVTranscoderConfig\_SetDstAudioType(OH\_AVTranscoder\_Config \*config, const char \*mimeType)](#oh_avtranscoderconfig_setdstaudiotype) | 

Sets the encoding format of the output audio for transcoding.

Currently, only AAC is supported. If this parameter is not set, AAC is used by default.

This function must be called before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare).

 |
| [OH\_AVErrCode OH\_AVTranscoderConfig\_SetDstFileType(OH\_AVTranscoder\_Config \*config, OH\_AVOutputFormat mimeType)](#oh_avtranscoderconfig_setdstfiletype) | 

Sets the container format of the output video file for transcoding.

Currently, only MP4 is supported.

This function must be called before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare).

 |
| [OH\_AVErrCode OH\_AVTranscoderConfig\_SetDstAudioBitrate(OH\_AVTranscoder\_Config \*config, int32\_t bitrate)](#oh_avtranscoderconfig_setdstaudiobitrate) | 

Sets the bit rate of the output audio for transcoding.

This function must be called before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare).

 |
| [OH\_AVErrCode OH\_AVTranscoderConfig\_SetDstVideoBitrate(OH\_AVTranscoder\_Config \*config, int32\_t bitrate)](#oh_avtranscoderconfig_setdstvideobitrate) | 

Sets the bit rate of the output video for transcoding.

This function must be called before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare).

 |
| [OH\_AVErrCode OH\_AVTranscoderConfig\_SetDstVideoResolution(OH\_AVTranscoder\_Config \*config, int32\_t width, int32\_t height)](#oh_avtranscoderconfig_setdstvideoresolution) | 

Sets the resolution of the output video for transcoding, in px, where **width** is the width of the output video frame and **height** is the height of the output video frame.

This function must be called before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare).

 |
| [OH\_AVErrCode OH\_AVTranscoderConfig\_EnableBFrame(OH\_AVTranscoder\_Config \*config, bool enabled)](#oh_avtranscoderconfig_enablebframe) | 

Enables B-frame encoding for the output video during transcoding.

For details about the constraints on B-frame video encoding, see [Constraints in B-Frame Video Encoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-encoding-b-frame#constraints).

If the current environment does not meet these constraints, B-frames will be skipped, and encoding will proceed as if B-frame video encoding were not enabled.

 |
| [OH\_AVTranscoder \*OH\_AVTranscoder\_Create(void)](#oh_avtranscoder_create) | Creates an AVTranscoder instance. |
| [OH\_AVErrCode OH\_AVTranscoder\_Prepare(OH\_AVTranscoder \*transcoder, OH\_AVTranscoder\_Config \*config)](#oh_avtranscoder_prepare) | 

Sets the parameters for video transcoding and prepares for transcoding.

This function must be called before [OH\_AVTranscoder\_Start](#oh_avtranscoder_start). Upon a successful call to this function, the AVTranscoder enters the AVTRANSCODER\_PREPARED state.

 |
| [OH\_AVErrCode OH\_AVTranscoder\_Start(OH\_AVTranscoder \*transcoder)](#oh_avtranscoder_start) | 

Starts transcoding.

This function must be called after a successful call to [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare). Upon a successful call to this function, the AVTranscoder enters the AVTRANSCODER\_STARTED state.

 |
| [OH\_AVErrCode OH\_AVTranscoder\_Pause(OH\_AVTranscoder \*transcoder)](#oh_avtranscoder_pause) | 

Pauses transcoding.

This function must be called when the AVTranscoder is in the AVTRANSCODER\_STARTED state. Upon a successful call to this function, the AVTranscoder enters the AVTRANSCODER\_PAUSED state.

 |
| [OH\_AVErrCode OH\_AVTranscoder\_Resume(OH\_AVTranscoder \*transcoder)](#oh_avtranscoder_resume) | 

Resumes transcoding.

This function must be called when the AVTranscoder is in the AVTRANSCODER\_PAUSED state. Upon a successful call to this function, the AVTranscoder enters the AVTRANSCODER\_STARTED state again.

 |
| [OH\_AVErrCode OH\_AVTranscoder\_Cancel(OH\_AVTranscoder \*transcoder)](#oh_avtranscoder_cancel) | 

Cancels transcoding.

This function must be called when the AVTranscoder is in the AVTRANSCODER\_STARTED or AVTRANSCODER\_PAUSED state. Upon a successful call to this function, the AVTranscoder enters the AVTRANSCODER\_CANCELLED state.

 |
| [OH\_AVErrCode OH\_AVTranscoder\_Release(OH\_AVTranscoder \*transcoder)](#oh_avtranscoder_release) | Releases an AVTranscoder instance. |
| [OH\_AVErrCode OH\_AVTranscoder\_SetStateCallback(OH\_AVTranscoder \*transcoder, OH\_AVTranscoder\_OnStateChange callback, void \*userData)](#oh_avtranscoder_setstatecallback) | 

Registers a callback for transcoding state change events.

This callback is invoked when the state of the transcoding process changes.

An application can subscribe to only one transcoding state change event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

The callback must be registered before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare) is called.

 |
| [OH\_AVErrCode OH\_AVTranscoder\_SetErrorCallback(OH\_AVTranscoder \*transcoder, OH\_AVTranscoder\_OnError callback, void \*userData)](#oh_avtranscoder_seterrorcallback) | 

Registers a callback for transcoding error events.

This callback is invoked when an error occurs during the transcoding process.

If this event is reported, call [OH\_AVTranscoder\_Release](#oh_avtranscoder_release) to exit the transcoding.

An application can subscribe to only one transcoding error event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

The callback must be registered before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare) is called.

 |
| [OH\_AVErrCode OH\_AVTranscoder\_SetProgressUpdateCallback(OH\_AVTranscoder \*transcoder, OH\_AVTranscoder\_OnProgressUpdate callback, void \*userData)](#oh_avtranscoder_setprogressupdatecallback) | 

Registers a callback for transcoding progress update events.

This callback is invoked when the progress of the transcoding process is updated.

An application can subscribe to only one transcoding error event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

The callback must be registered before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare) is called.

 |

#### Function Description

#### \[h2\]OH\_AVTranscoderConfig\_Create()

OH\_AVTranscoder\_Config \*OH\_AVTranscoderConfig\_Create()

**Description**

Creates an instance of the transcoding configuration parameters.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVTranscoder\_Config](../../structs/oh-avtranscoder-config/document.md) \* | Pointer to the OH\_AVTranscoder\_Config instance created. If the operation fails, nullptr is returned. |

#### \[h2\]OH\_AVTranscoderConfig\_Release()

OH\_AVErrCode OH\_AVTranscoderConfig\_Release(OH\_AVTranscoder\_Config\* config)

**Description**

Releases the resources of the transcoding configuration parameters.

After a successful call, the instance specified by **config** is released and set to nullptr.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder\_Config](../../structs/oh-avtranscoder-config/document.md)\* config | Pointer to an OH\_AVTranscoder\_Config instance, which is created by running [OH\_AVTranscoderConfig\_Create](#oh_avtranscoderconfig_create). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The release operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **config** is nullptr.

 |

#### \[h2\]OH\_AVTranscoderConfig\_SetSrcFD()

OH\_AVErrCode OH\_AVTranscoderConfig\_SetSrcFD(OH\_AVTranscoder\_Config \*config, int32\_t srcFd, int64\_t srcOffset, int64\_t length)

**Description**

Sets the file descriptor of the source video for transcoding.

This function must be called before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare).

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder\_Config](../../structs/oh-avtranscoder-config/document.md) \*config | Pointer to an OH\_AVTranscoder\_Config instance, which is created by running [OH\_AVTranscoderConfig\_Create](#oh_avtranscoderconfig_create). |
| int32\_t srcFd | File descriptor of the source video. |
| int64\_t srcOffset | Offset of the source video in the file descriptor, in bytes. |
| int64\_t length | Size of the source video, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The setting is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **config** is nullptr, or the parameters related to the source video file are incorrect.

 |

#### \[h2\]OH\_AVTranscoderConfig\_SetDstFD()

OH\_AVErrCode OH\_AVTranscoderConfig\_SetDstFD(OH\_AVTranscoder\_Config \*config, int32\_t dstFd)

**Description**

Sets the file descriptor of the output video for transcoding.

This function must be called before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare).

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder\_Config](../../structs/oh-avtranscoder-config/document.md) \*config | Pointer to an OH\_AVTranscoder\_Config instance, which is created by running [OH\_AVTranscoderConfig\_Create](#oh_avtranscoderconfig_create). |
| int32\_t dstFd | File descriptor of the output video. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The setting is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **config** is nullptr, or the output video file descriptor is invalid.

 |

#### \[h2\]OH\_AVTranscoderConfig\_SetDstVideoType()

OH\_AVErrCode OH\_AVTranscoderConfig\_SetDstVideoType(OH\_AVTranscoder\_Config \*config, const char \*mimeType)

**Description**

Sets the encoding format of the output video for transcoding.

Currently, only AVC and HEVC are supported. If the source video is in HEVC format, the default value is **HEVC**. Otherwise, the default value is **AVC**.

This function must be called before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare).

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder\_Config](../../structs/oh-avtranscoder-config/document.md) \*config | Pointer to an OH\_AVTranscoder\_Config instance, which is created by running [OH\_AVTranscoderConfig\_Create](#oh_avtranscoderconfig_create). |
| const char \*mimeType | Pointer to the encoding format of the output video. For details, see [native\_avcodec\_base.h](../../../../avcodec-kit/c-apis/header-files/native-avcodec-base-h/document.md#variables). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The setting is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **config** is nullptr, or the value of **mimeType** is not allowed.

 |

#### \[h2\]OH\_AVTranscoderConfig\_SetDstAudioType()

OH\_AVErrCode OH\_AVTranscoderConfig\_SetDstAudioType(OH\_AVTranscoder\_Config \*config, const char \*mimeType)

**Description**

Sets the encoding format of the output audio for transcoding.

Currently, only AAC is supported. If this parameter is not set, AAC is used by default.

This function must be called before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare).

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder\_Config](../../structs/oh-avtranscoder-config/document.md) \*config | Pointer to an OH\_AVTranscoder\_Config instance, which is created by running [OH\_AVTranscoderConfig\_Create](#oh_avtranscoderconfig_create). |
| const char \*mimeType | Pointer to the encoding format of the output audio. For details, see [native\_avcodec\_base.h](../../../../avcodec-kit/c-apis/header-files/native-avcodec-base-h/document.md#variables). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The setting is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **config** is nullptr, or the value of **mimeType** is not allowed.

 |

#### \[h2\]OH\_AVTranscoderConfig\_SetDstFileType()

OH\_AVErrCode OH\_AVTranscoderConfig\_SetDstFileType(OH\_AVTranscoder\_Config \*config, OH\_AVOutputFormat mimeType)

**Description**

Sets the container format of the output video file for transcoding.

Currently, only MP4 is supported.

This function must be called before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare).

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder\_Config](../../structs/oh-avtranscoder-config/document.md) \*config | Pointer to an OH\_AVTranscoder\_Config instance, which is created by running [OH\_AVTranscoderConfig\_Create](#oh_avtranscoderconfig_create). |
| [OH\_AVOutputFormat](../../../../avcodec-kit/c-apis/header-files/native-avcodec-base-h/document.md#oh_avoutputformat) mimeType | Container format of the output video. For details, see [native\_avcodec\_base.h](../../../../avcodec-kit/c-apis/header-files/native-avcodec-base-h/document.md#variables). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The setting is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **config** is nullptr, or the value of **mimeType** is invalid.

 |

#### \[h2\]OH\_AVTranscoderConfig\_SetDstAudioBitrate()

OH\_AVErrCode OH\_AVTranscoderConfig\_SetDstAudioBitrate(OH\_AVTranscoder\_Config \*config, int32\_t bitrate)

**Description**

Sets the bit rate of the output audio for transcoding.

This function must be called before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare).

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder\_Config](../../structs/oh-avtranscoder-config/document.md) \*config | Pointer to an OH\_AVTranscoder\_Config instance, which is created by running [OH\_AVTranscoderConfig\_Create](#oh_avtranscoderconfig_create). |
| int32\_t bitrate | Bit rate of the output audio, in bit/s. The value range is \[1, 500000\]. The default value is 48 kbit/s. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The setting is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **config** is nullptr, or the value of **bitrate** is invalid.

 |

#### \[h2\]OH\_AVTranscoderConfig\_SetDstVideoBitrate()

OH\_AVErrCode OH\_AVTranscoderConfig\_SetDstVideoBitrate(OH\_AVTranscoder\_Config \*config, int32\_t bitrate)

**Description**

Sets the bit rate of the output video for transcoding.

This function must be called before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare).

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder\_Config](../../structs/oh-avtranscoder-config/document.md) \*config | Pointer to an OH\_AVTranscoder\_Config instance, which is created by running [OH\_AVTranscoderConfig\_Create](#oh_avtranscoderconfig_create). |
| int32\_t bitrate | 
Bit rate of the output video, in bit/s. The default bit rate is set according to the resolution of the output video.

For the resolution range \[240p, 480p\], the default bit rate is 1 Mbit/s.

For the resolution range (480p, 720p\], the default bit rate is 2 Mbit/s.

For the resolution range (240p, 1080p\], the default bit rate is 4 Mbit/s.

For the resolution 1080p or above, the default bit rate is 8 Mbit/s.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The setting is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **config** is nullptr, or the value of **bitrate** is invalid.

 |

#### \[h2\]OH\_AVTranscoderConfig\_SetDstVideoResolution()

OH\_AVErrCode OH\_AVTranscoderConfig\_SetDstVideoResolution(OH\_AVTranscoder\_Config \*config, int32\_t width, int32\_t height)

**Description**

Sets the resolution of the output video for transcoding, in px, where **width** is the width of the output video frame and **height** is the height of the output video frame.

This function must be called before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare).

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder\_Config](../../structs/oh-avtranscoder-config/document.md) \*config | Pointer to an OH\_AVTranscoder\_Config instance, which is created by running [OH\_AVTranscoderConfig\_Create](#oh_avtranscoderconfig_create). |
| int32\_t width | Width of the output video frame. The value range is \[240, 3840\]. The default value is the width of the source video frame. |
| int32\_t height | Height of the output video frame. The value range is \[240, 2160\]. The default value is the height of the source video frame. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The setting is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **config** is nullptr, or the value of **width** or **height** is invalid.

 |

#### \[h2\]OH\_AVTranscoderConfig\_EnableBFrame()

OH\_AVErrCode OH\_AVTranscoderConfig\_EnableBFrame(OH\_AVTranscoder\_Config \*config, bool enabled)

**Description**

Enables B-frame encoding for the output video during transcoding.

For details about the constraints on B-frame video encoding, see [Constraints in B-Frame Video Encoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-encoding-b-frame#constraints).

If the current environment does not meet these constraints, B-frames will be skipped, and encoding will proceed as if B-frame video encoding were not enabled.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder\_Config](../../structs/oh-avtranscoder-config/document.md) \*config | Pointer to an OH\_AVTranscoder\_Config instance, which is created by running [OH\_AVTranscoderConfig\_Create](#oh_avtranscoderconfig_create). |
| bool enabled | Whether to enable B-frame encoding. The values include **true** (yes) and **false** (no). The default value is **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The setting is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **config** is nullptr.

 |

#### \[h2\]OH\_AVTranscoder\_Create()

OH\_AVTranscoder \*OH\_AVTranscoder\_Create(void)

**Description**

Creates an AVTranscoder instance.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVTranscoder](../../structs/oh-avtranscoder/document.md) \* | Pointer to the OH\_AVTranscoder instance created. If the operation fails, nullptr is returned. |

#### \[h2\]OH\_AVTranscoder\_Prepare()

OH\_AVErrCode OH\_AVTranscoder\_Prepare(OH\_AVTranscoder \*transcoder, OH\_AVTranscoder\_Config \*config)

**Description**

Sets the parameters for video transcoding and prepares for transcoding.

This function must be called before [OH\_AVTranscoder\_Start](#oh_avtranscoder_start). Upon a successful call to this function, the AVTranscoder enters the AVTRANSCODER\_PREPARED state.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder](../../structs/oh-avtranscoder/document.md) \*transcoder | Pointer to an OH\_AVTranscoder instance, which is created by running [OH\_AVTranscoder\_Create](#oh_avtranscoder_create). |
| [OH\_AVTranscoder\_Config](../../structs/oh-avtranscoder-config/document.md) \*config | 
Pointer to an OH\_AVTranscoder\_Config instance,

which is created by running [OH\_AVTranscoderConfig\_Create](#oh_avtranscoderconfig_create).

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The video transcoding parameters are set successfully, and the AVTranscoder enters the AVTRANSCODER\_PREPARED state.

**AV\_ERR\_INVALID\_VAL**: The input parameter **transcoder** is nullptr, or the Prepare operation fails.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The Prepare operation is not allowed in the current state, or the format is not supported.

**AV\_ERR\_IO**: An I/O access error occurs.

**AV\_ERR\_SERVICE\_DIED**: The media service is stopped.

 |

#### \[h2\]OH\_AVTranscoder\_Start()

OH\_AVErrCode OH\_AVTranscoder\_Start(OH\_AVTranscoder \*transcoder)

**Description**

Starts transcoding.

This function must be called after a successful call to [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare). Upon a successful call to this function, the AVTranscoder enters the AVTRANSCODER\_STARTED state.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder](../../structs/oh-avtranscoder/document.md) \*transcoder | Pointer to an OH\_AVTranscoder instance, which is created by running [OH\_AVTranscoder\_Create](#oh_avtranscoder_create). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: Transcoding starts successfully, and the AVTranscoder enters the AVTRANSCODER\_STARTED state.

**AV\_ERR\_INVALID\_VAL**: The input parameter **transcoder** is nullptr, or the Start operation fails.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The Start operation is not allowed in the current state.

**AV\_ERR\_IO**: An I/O access error occurs.

**AV\_ERR\_SERVICE\_DIED**: The media service is stopped.

 |

#### \[h2\]OH\_AVTranscoder\_Pause()

OH\_AVErrCode OH\_AVTranscoder\_Pause(OH\_AVTranscoder \*transcoder)

**Description**

Pauses transcoding.

This function must be called when the AVTranscoder is in the AVTRANSCODER\_STARTED state. Upon a successful call to this function, the AVTranscoder enters the AVTRANSCODER\_PAUSED state.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder](../../structs/oh-avtranscoder/document.md) \*transcoder | Pointer to an OH\_AVTranscoder instance, which is created by running [OH\_AVTranscoder\_Create](#oh_avtranscoder_create). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: Transcoding is paused successfully, and the AVTranscoder enters the AVTRANSCODER\_PAUSED state.

**AV\_ERR\_INVALID\_VAL**: The input parameter **transcoder** is nullptr, or the Pause operation fails.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The Pause operation is not allowed in the current state.

**AV\_ERR\_IO**: An I/O access error occurs.

**AV\_ERR\_SERVICE\_DIED**: The media service is stopped.

 |

#### \[h2\]OH\_AVTranscoder\_Resume()

OH\_AVErrCode OH\_AVTranscoder\_Resume(OH\_AVTranscoder \*transcoder)

**Description**

Resumes transcoding.

This function must be called when the AVTranscoder is in the AVTRANSCODER\_PAUSED state. Upon a successful call to this function, the AVTranscoder enters the AVTRANSCODER\_STARTED state again.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder](../../structs/oh-avtranscoder/document.md) \*transcoder | Pointer to an OH\_AVTranscoder instance, which is created by running [OH\_AVTranscoder\_Create](#oh_avtranscoder_create). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: Transcoding is resumed successfully, and the AVTranscoder enters the AVTRANSCODER\_STARTED state.

**AV\_ERR\_INVALID\_VAL**: The input parameter **transcoder** is nullptr, or the Resume operation fails.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The Resume operation is not allowed in the current state.

**AV\_ERR\_IO**: An I/O access error occurs.

**AV\_ERR\_SERVICE\_DIED**: The media service is stopped.

 |

#### \[h2\]OH\_AVTranscoder\_Cancel()

OH\_AVErrCode OH\_AVTranscoder\_Cancel(OH\_AVTranscoder \*transcoder)

**Description**

Cancels transcoding.

This function must be called when the AVTranscoder is in the AVTRANSCODER\_STARTED or AVTRANSCODER\_PAUSED state. Upon a successful call to this function, the AVTranscoder enters the AVTRANSCODER\_CANCELLED state.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder](../../structs/oh-avtranscoder/document.md) \*transcoder | Pointer to an OH\_AVTranscoder instance, which is created by running [OH\_AVTranscoder\_Create](#oh_avtranscoder_create). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: Transcoding is canceled successfully, and the AVTranscoder enters the AVTRANSCODER\_CANCELLED state.

**AV\_ERR\_INVALID\_VAL**: The input parameter **transcoder** is nullptr, or the Cancel operation fails.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The Cancel operation is not allowed in the current state.

**AV\_ERR\_IO**: An I/O access error occurs.

**AV\_ERR\_SERVICE\_DIED**: The media service is stopped.

 |

#### \[h2\]OH\_AVTranscoder\_Release()

OH\_AVErrCode OH\_AVTranscoder\_Release(OH\_AVTranscoder \*transcoder)

**Description**

Releases an AVTranscoder instance.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder](../../structs/oh-avtranscoder/document.md) \*transcoder | Pointer to an OH\_AVTranscoder instance, which is created by running [OH\_AVTranscoder\_Create](#oh_avtranscoder_create). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
AV\_ERR\_OK: The AVTranscoder instance is successfully released.

**AV\_ERR\_INVALID\_VAL**: The input parameter **transcoder** is nullptr, or the Release operation fails.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The Release operation is not allowed in the current state.

**AV\_ERR\_IO**: An I/O access error occurs.

**AV\_ERR\_SERVICE\_DIED**: The media service is stopped.

 |

#### \[h2\]OH\_AVTranscoder\_SetStateCallback()

OH\_AVErrCode OH\_AVTranscoder\_SetStateCallback(OH\_AVTranscoder \*transcoder, OH\_AVTranscoder\_OnStateChange callback, void \*userData)

**Description**

Registers a callback for transcoding state change events.

This callback is invoked when the state of the transcoding process changes.

An application can subscribe to only one transcoding state change event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

The callback must be registered before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare) is called.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder](../../structs/oh-avtranscoder/document.md) \*transcoder | Pointer to an OH\_AVTranscoder instance, which is created by running [OH\_AVTranscoder\_Create](#oh_avtranscoder_create). |
| [OH\_AVTranscoder\_OnStateChange](../avtranscoder-base-h/document.md#oh_avtranscoder_onstatechange) callback | Callback invoked when the state of the transcoding process changes. For details, see [OH\_AVTranscoder\_OnStateChange](../avtranscoder-base-h/document.md#oh_avtranscoder_onstatechange). |
| void \*userData | Pointer to user-defined data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The registration is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **transcoder** or **callback** is nullptr.

 |

#### \[h2\]OH\_AVTranscoder\_SetErrorCallback()

OH\_AVErrCode OH\_AVTranscoder\_SetErrorCallback(OH\_AVTranscoder \*transcoder, OH\_AVTranscoder\_OnError callback, void \*userData)

**Description**

Registers a callback for transcoding error events.

This callback is invoked when an error occurs during the transcoding process.

If this event is reported, call [OH\_AVTranscoder\_Release](#oh_avtranscoder_release) to exit the transcoding.

An application can subscribe to only one transcoding error event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

The callback must be registered before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare) is called.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder](../../structs/oh-avtranscoder/document.md) \*transcoder | Pointer to an OH\_AVTranscoder instance, which is created by running [OH\_AVTranscoder\_Create](#oh_avtranscoder_create). |
| [OH\_AVTranscoder\_OnError](../avtranscoder-base-h/document.md#oh_avtranscoder_onerror) callback | Callback invoked when an error occurs during the transcoding process. For details, see [OH\_AVTranscoder\_OnError](../avtranscoder-base-h/document.md#oh_avtranscoder_onerror). |
| void \*userData | Pointer to user-defined data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The registration is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **transcoder** or **callback** is nullptr.

 |

#### \[h2\]OH\_AVTranscoder\_SetProgressUpdateCallback()

OH\_AVErrCode OH\_AVTranscoder\_SetProgressUpdateCallback(OH\_AVTranscoder \*transcoder, OH\_AVTranscoder\_OnProgressUpdate callback, void \*userData)

**Description**

Registers a callback for transcoding progress update events.

This callback is invoked when the progress of the transcoding process is updated.

An application can subscribe to only one transcoding error event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

The callback must be registered before [OH\_AVTranscoder\_Prepare](#oh_avtranscoder_prepare) is called.

**System capability**: SystemCapability.Multimedia.Media.AVTranscoder

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVTranscoder](../../structs/oh-avtranscoder/document.md) \*transcoder | Pointer to an OH\_AVTranscoder instance, which is created by running [OH\_AVTranscoder\_Create](#oh_avtranscoder_create). |
| [OH\_AVTranscoder\_OnProgressUpdate](../avtranscoder-base-h/document.md#oh_avtranscoder_onprogressupdate) callback | Callback invoked when the progress of the transcoding process is updated. For details, see [OH\_AVTranscoder\_OnProgressUpdate](../avtranscoder-base-h/document.md#oh_avtranscoder_onprogressupdate). |
| void \*userData | Pointer to user-defined data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The registration is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **transcoder** or **callback** is nullptr.

 |
