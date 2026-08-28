# avplayer.h

#### Overview

The **avplayer.h** file declares the AVPlayer APIs. You can use the native AVPlayer APIs to play a media asset.

**File to include**: <multimedia/player\_framework/avplayer.h>

**Library**: libavplayer.so

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Related module**: [AVPlayer](../../modules/avplayer/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [MediaKeySession](../../structs/mediakeysession/document.md) | MediaKeySession | Describes the media key session. |
| [DRM\_MediaKeySystemInfo](../../structs/drm-mediakeysysteminfo/document.md) | DRM\_MediaKeySystemInfo | Describes the media key system information. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*Player\_MediaKeySystemInfoCallback)(OH\_AVPlayer player, DRM\_MediaKeySystemInfo mediaKeySystemInfo)](#player_mediakeysysteminfocallback) | Player\_MediaKeySystemInfoCallback | Called when media key system information of the AVPlayer is updated. |
| [OH\_AVPlayer \*OH\_AVPlayer\_Create(void)](#oh_avplayer_create) | \- | 
Creates an OH\_AVPlayer instance.

You are advised to create a maximum of 16 AVPlayer instances for an application in both audio and video playback scenarios.

 |
| [OH\_AVErrCode OH\_AVPlayer\_SetURLSource(OH\_AVPlayer \*player, const char \*url)](#oh_avplayer_seturlsource) | \- | Sets the HTTP URL of a media source to be played by an AVPlayer. |
| [OH\_AVErrCode OH\_AVPlayer\_SetFDSource(OH\_AVPlayer \*player, int32\_t fd, int64\_t offset, int64\_t size)](#oh_avplayer_setfdsource) | \- | Sets the file descriptor of a media source to be played by an AVPlayer. |
| [OH\_AVErrCode OH\_AVPlayer\_SetDataSource(OH\_AVPlayer player, OH\_AVDataSourceExt datasrc, void\* userData)](#oh_avplayer_setdatasource) | \- | Sets the media source of the AVPlayer. The data of this media source is provided by the application. |
| [OH\_AVErrCode OH\_AVPlayer\_Prepare(OH\_AVPlayer \*player)](#oh_avplayer_prepare) | \- | 

Prepares the playback environment and buffers media data.

This function must be called after **SetSource**.

 |
| [OH\_AVErrCode OH\_AVPlayer\_Play(OH\_AVPlayer \*player)](#oh_avplayer_play) | \- | 

Starts playback.

This function must be called after [OH\_AVPlayer\_Prepare](#oh_avplayer_prepare).

In other words, you can call this function when the AVPlayer is in the prepared state.

 |
| [OH\_AVErrCode OH\_AVPlayer\_Pause(OH\_AVPlayer \*player)](#oh_avplayer_pause) | \- | Pauses playback. |
| [OH\_AVErrCode OH\_AVPlayer\_Stop(OH\_AVPlayer \*player)](#oh_avplayer_stop) | \- | Stops playback. |
| [OH\_AVErrCode OH\_AVPlayer\_Reset(OH\_AVPlayer \*player)](#oh_avplayer_reset) | \- | 

Restores the AVPlayer to the initial state.

After the function is called, you can call **SetSource** to set the media source to play, and then call [OH\_AVPlayer\_Prepare](#oh_avplayer_prepare) and [OH\_AVPlayer\_Play](#oh_avplayer_play) in sequence.

 |
| [OH\_AVErrCode OH\_AVPlayer\_Release(OH\_AVPlayer \*player)](#oh_avplayer_release) | \- | 

Asynchronously releases an OH\_AVPlayer instance.

The asynchronous function improves performance, but cannot ensure that the surface buffer of the playback window is released. You must ensure the lifecycle of the playback window.

 |
| [OH\_AVErrCode OH\_AVPlayer\_ReleaseSync(OH\_AVPlayer \*player)](#oh_avplayer_releasesync) | \- | 

Synchronously releases an OH\_AVPlayer instance.

The synchronous function ensures that the display buffer of the playback window is released, with a long time. Therefore, you need to design an asynchronous mechanism.

 |
| [OH\_AVErrCode OH\_AVPlayer\_SetVolume(OH\_AVPlayer \*player, float leftVolume, float rightVolume)](#oh_avplayer_setvolume) | \- | 

Sets the volume for an AVPlayer.

This function can be used when the AVPlayer is in the playing or paused state. The value **0** means that the AVPlayer is muted, and **1** means that the original volume is used.

 |
| [OH\_AVErrCode OH\_AVPlayer\_SetLoudnessGain(OH\_AVPlayer \*player, float loudnessGain)](#oh_avplayer_setloudnessgain) | \- | 

Sets the loudness of the AVPlayer. This function can be called when the AVPlayer is in the prepared, playing, paused, completed, or stopped state.

The default loudness gain is 0.0 dB. The **usage** parameter of the AVPlayer stream must be [OH\_AudioStream\_Usage](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MUSIC,

[OH\_AudioStream\_Usage](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MOVIE, or [OH\_AudioStream\_Usage](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_AUDIOBOOK.

The latency mode of the audio renderer must be [OH\_AudioStream\_LatencyMode](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiostream_latencymode).AUDIOSTREAM\_LATENCY\_MODE\_NORMAL.

If the audio is played through the high-resolution pipeline, this operation is not supported.

 |
| [OH\_AVErrCode OH\_AVPlayer\_Seek(OH\_AVPlayer \*player, int32\_t mSeconds, AVPlayerSeekMode mode)](#oh_avplayer_seek) | \- | 

Seeks to a playback position.

This function can be used when the AVPlayer is in the playing or paused state.

 |
| [OH\_AVErrCode OH\_AVPlayer\_GetCurrentTime(OH\_AVPlayer \*player, int32\_t \*currentTime)](#oh_avplayer_getcurrenttime) | \- | Obtains the playback position, in milliseconds. |
| [OH\_AVErrCode OH\_AVPlayer\_GetVideoWidth(OH\_AVPlayer \*player, int32\_t \*videoWidth)](#oh_avplayer_getvideowidth) | \- | Obtains the video width. |
| [OH\_AVErrCode OH\_AVPlayer\_GetVideoHeight(OH\_AVPlayer \*player, int32\_t \*videoHeight)](#oh_avplayer_getvideoheight) | \- | Obtains the video height. |
| [OH\_AVErrCode OH\_AVPlayer\_SetPlaybackSpeed(OH\_AVPlayer \*player, AVPlaybackSpeed speed)](#oh_avplayer_setplaybackspeed) | \- | Sets the playback speed of the AVPlayer. For details about the playback speed, see [AVPlaybackSpeed](../avplayer-base-h/document.md#avplaybackspeed). |
| [OH\_AVErrCode OH\_AVPlayer\_SetPlaybackRate(OH\_AVPlayer \*player, float rate)](#oh_avplayer_setplaybackrate) | \- | 

Sets the playback rate of an AVPlayer within the valid range.

The supported states are prepared, playing, paused, and completed.

 |
| [OH\_AVErrCode OH\_AVPlayer\_GetPlaybackSpeed(OH\_AVPlayer \*player, AVPlaybackSpeed \*speed)](#oh_avplayer_getplaybackspeed) | \- | Obtains the playback speed of an AVPlayer. |
| [OH\_AVErrCode OH\_AVPlayer\_SetAudioRendererInfo(OH\_AVPlayer \*player, OH\_AudioStream\_Usage streamUsage)](#oh_avplayer_setaudiorendererinfo) | \- | Sets the audio stream type for an AVPlayer. |
| [OH\_AVErrCode OH\_AVPlayer\_SetVolumeMode(OH\_AVPlayer \*player, OH\_AudioStream\_VolumeMode volumeMode)](#oh_avplayer_setvolumemode) | \- | Sets the audio volume mode for an AVPlayer. |
| [OH\_AVErrCode OH\_AVPlayer\_SetAudioInterruptMode(OH\_AVPlayer \*player, OH\_AudioInterrupt\_Mode interruptMode)](#oh_avplayer_setaudiointerruptmode) | \- | Sets the audio interruption mode for an AVPlayer. |
| [OH\_AVErrCode OH\_AVPlayer\_SetAudioEffectMode(OH\_AVPlayer \*player, OH\_AudioStream\_AudioEffectMode effectMode)](#oh_avplayer_setaudioeffectmode) | \- | Sets the audio effect mode for an AVPlayer. |
| [OH\_AVErrCode OH\_AVPlayer\_SelectBitRate(OH\_AVPlayer \*player, uint32\_t bitRate)](#oh_avplayer_selectbitrate) | \- | 

Sets the bit rate used by an HLS player. This function is valid only for HLS network streams.

By default, the AVPlayer selects a proper bit rate and speed based on the network connection.

You can set a bit rate available in the valid bit rates reported in **INFO\_TYPE\_BITRATE\_COLLECT**. The AVPlayer selects a bit rate that is lower than and closest to the specified bit rate. When ready, you can query the selected bit rate.

 |
| [OH\_AVErrCode OH\_AVPlayer\_SetVideoSurface(OH\_AVPlayer \*player, OHNativeWindow \*window)](#oh_avplayer_setvideosurface) | \- | 

Sets a playback window.

This function must be called after **SetSource** and before **Prepare**.

 |
| [OH\_AVErrCode OH\_AVPlayer\_GetDuration(OH\_AVPlayer \*player, int32\_t \*duration)](#oh_avplayer_getduration) | \- | Obtains the total duration of a media file, in milliseconds. |
| [OH\_AVErrCode OH\_AVPlayer\_GetState(OH\_AVPlayer \*player, AVPlayerState \*state)](#oh_avplayer_getstate) | \- | Obtains the AVPlayer state. |
| [bool OH\_AVPlayer\_IsPlaying(OH\_AVPlayer \*player)](#oh_avplayer_isplaying) | \- | Checks whether an AVPlayer is playing. |
| [bool OH\_AVPlayer\_IsLooping(OH\_AVPlayer \*player)](#oh_avplayer_islooping) | \- | Checks whether an AVPlayer is looping. |
| [OH\_AVErrCode OH\_AVPlayer\_SetLooping(OH\_AVPlayer \*player, bool loop)](#oh_avplayer_setlooping) | \- | Enables loop playback. |
| [OH\_AVErrCode OH\_AVPlayer\_SetPlayerCallback(OH\_AVPlayer \*player, AVPlayerCallback callback)](#oh_avplayer_setplayercallback) | \- | 

Sets an AVPlayer callback.

The callbacks [OH\_AVPlayerOnInfo](../avplayer-base-h/document.md#oh_avplayeroninfo) and [OH\_AVPlayerOnError](../avplayer-base-h/document.md#oh_avplayeronerror) set by using this function can transfer limited information. In addition, it is inconvenient for the application to distinguish between multiple AVPlayer instances.

Starting from API version 12, [OH\_AVPlayer\_SetOnInfoCallback](#oh_avplayer_setoninfocallback) and [OH\_AVPlayer\_SetOnErrorCallback](#oh_avplayer_setonerrorcallback) are provided to set the callbacks [OH\_AVPlayerOnInfoCallback](../avplayer-base-h/document.md#oh_avplayeroninfocallback) and [OH\_AVPlayerOnErrorCallback](../avplayer-base-h/document.md#oh_avplayeronerrorcallback), respectively.

 |
| [OH\_AVErrCode OH\_AVPlayer\_SelectTrack(OH\_AVPlayer \*player, int32\_t index)](#oh_avplayer_selecttrack) | \- | 

Selects an audio or subtitle track.

By default, the first audio track with data is played, and the subtitle track is not played.

After the setting takes effect, the original track becomes invalid. Set the subtitle track to the prepared, playing, paused, or completed state, and set the audio track to the prepared state.

 |
| [OH\_AVErrCode OH\_AVPlayer\_DeselectTrack(OH\_AVPlayer \*player, int32\_t index)](#oh_avplayer_deselecttrack) | \- | Deselects an audio or subtitle track. |
| [OH\_AVErrCode OH\_AVPlayer\_GetCurrentTrack(OH\_AVPlayer \*player, int32\_t trackType, int32\_t \*index)](#oh_avplayer_getcurrenttrack) | \- | Obtains the currently valid track. You can set the track to the prepared, playing, paused, or completed state. |
| [OH\_AVErrCode OH\_AVPlayer\_SetMediaKeySystemInfoCallback(OH\_AVPlayer \*player, Player\_MediaKeySystemInfoCallback callback)](#oh_avplayer_setmediakeysysteminfocallback) | \- | Sets a callback to return the media key system information for an AVPlayer. |
| [OH\_AVErrCode OH\_AVPlayer\_GetMediaKeySystemInfo(OH\_AVPlayer \*player, DRM\_MediaKeySystemInfo \*mediaKeySystemInfo)](#oh_avplayer_getmediakeysysteminfo) | \- | Obtains the media key system information to create a media key session. |
| [OH\_AVErrCode OH\_AVPlayer\_SetDecryptionConfig(OH\_AVPlayer \*player, MediaKeySession \*mediaKeySession, bool secureVideoPath)](#oh_avplayer_setdecryptionconfig) | \- | Sets the decryption information. |
| [OH\_AVErrCode OH\_AVPlayer\_SetOnInfoCallback(OH\_AVPlayer \*player, OH\_AVPlayerOnInfoCallback callback, void \*userData)](#oh_avplayer_setoninfocallback) | \- | Sets a callback for the event indicating that the AVPlayer receives a message. |
| [OH\_AVErrCode OH\_AVPlayer\_SetOnErrorCallback(OH\_AVPlayer \*player, OH\_AVPlayerOnErrorCallback callback, void \*userData)](#oh_avplayer_setonerrorcallback) | \- | Sets a callback for the event indicating that an error occurs in the AVPlayer. |
| [OH\_AVFormat \*OH\_AVPlayer\_GetMediaDescription(OH\_AVPlayer \*player)](#oh_avplayer_getmediadescription) | \- | 

Obtains the media source information for the AVPlayer. This function can be called when the playback resource is configured and the AVPlayer is in the initialized, prepared, playing, paused, completed, or stopped state.

You must manually release the returned OH\_AVFormat pointer object when it is no longer needed.

 |
| [OH\_AVFormat \*OH\_AVPlayer\_GetTrackDescription(OH\_AVPlayer \*player, uint32\_t index)](#oh_avplayer_gettrackdescription) | \- | 

Obtains the media source track information for the AVPlayer by index. This function can be called when the playback resource is configured and the AVPlayer is in the initialized, prepared, playing, paused, completed, or stopped state.

You must manually release the returned OH\_AVFormat pointer object when it is no longer needed.

 |

#### Function Description

#### \[h2\]Player\_MediaKeySystemInfoCallback()

typedef void (\*Player\_MediaKeySystemInfoCallback)(OH\_AVPlayer \*player, DRM\_MediaKeySystemInfo\* mediaKeySystemInfo)

**Description**

Called when media key system information of the AVPlayer is updated.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| [DRM\_MediaKeySystemInfo](../../structs/drm-mediakeysysteminfo/document.md)\* mediaKeySystemInfo | Pointer to the media key system information. |

#### \[h2\]OH\_AVPlayer\_Create()

OH\_AVPlayer \*OH\_AVPlayer\_Create(void)

**Description**

Creates an OH\_AVPlayer instance.

You are advised to create a maximum of 16 AVPlayer instances for an application in both audio and video playback scenarios.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \* | 
Pointer to the OH\_AVPlayer instance created if the operation is successful; nullptr otherwise.

The possible causes of an operation failure are as follows:

1\. The execution of **PlayerFactory::CreatePlayer** fails.

2\. The execution of **new PlayerObject** fails.

 |

#### \[h2\]OH\_AVPlayer\_SetURLSource()

OH\_AVErrCode OH\_AVPlayer\_SetURLSource(OH\_AVPlayer \*player, const char \*url)

**Description**

Sets the HTTP URL of a media source to be played by an AVPlayer.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| const char \*url | URL of the media source. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The setting is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, the input parameter **url** is null, or the execution of **player SetUrlSource** fails.

 |

#### \[h2\]OH\_AVPlayer\_SetFDSource()

OH\_AVErrCode OH\_AVPlayer\_SetFDSource(OH\_AVPlayer \*player, int32\_t fd, int64\_t offset, int64\_t size)

**Description**

Sets the file descriptor of a media source to be played by an AVPlayer.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| int32\_t fd | File descriptor of the media source. |
| int64\_t offset | Offset of the media source in the file descriptor. |
| int64\_t size | Size of the media source. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The file descriptor is set successfully.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player SetFdSource** fails.

 |

#### \[h2\]OH\_AVPlayer\_SetDataSource()

OH\_AVErrCode OH\_AVPlayer\_SetDataSource(OH\_AVPlayer \*player, OH\_AVDataSourceExt\* datasrc, void\* userData)

**Description**

Sets the media source of the AVPlayer. The data of this media source is provided by the application.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 21

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| OH\_AVDataSourceExt\* datasrc | Pointer to custom media data. |
| void\* userData | Pointer to the handle, which is used in the callback. If **userData** is empty, the AVPlayer does not support multi-instance playback. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AVErrCode | 
**AV\_ERR\_OK**: The setting is successful.

**AV\_ERR\_INVALID\_VAL**: The **player** or **datasrc** parameter is nullptr.

 |

#### \[h2\]OH\_AVPlayer\_Prepare()

OH\_AVErrCode OH\_AVPlayer\_Prepare(OH\_AVPlayer \*player)

**Description**

Prepares the playback environment and buffers media data.

This function must be called after **SetSource**.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player Prepare** fails.

 |

#### \[h2\]OH\_AVPlayer\_Play()

OH\_AVErrCode OH\_AVPlayer\_Play(OH\_AVPlayer \*player)

**Description**

Starts playback.

This function must be called after [OH\_AVPlayer\_Prepare](#oh_avplayer_prepare).

In other words, you can call this function when the AVPlayer is in the prepared state.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player Play** fails.

 |

#### \[h2\]OH\_AVPlayer\_Pause()

OH\_AVErrCode OH\_AVPlayer\_Pause(OH\_AVPlayer \*player)

**Description**

Pauses playback.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player Pause** fails.

 |

#### \[h2\]OH\_AVPlayer\_Stop()

OH\_AVErrCode OH\_AVPlayer\_Stop(OH\_AVPlayer \*player)

**Description**

Stops playback.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player Stop** fails.

 |

#### \[h2\]OH\_AVPlayer\_Reset()

OH\_AVErrCode OH\_AVPlayer\_Reset(OH\_AVPlayer \*player)

**Description**

Restores the AVPlayer to the initial state.

After the function is called, you can call **SetSource** to set the media source to play, and then call [OH\_AVPlayer\_Prepare](#oh_avplayer_prepare) and [OH\_AVPlayer\_Play](#oh_avplayer_play) in sequence.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player Reset** fails.

 |

#### \[h2\]OH\_AVPlayer\_Release()

OH\_AVErrCode OH\_AVPlayer\_Release(OH\_AVPlayer \*player)

**Description**

Asynchronously releases an OH\_AVPlayer instance.

The asynchronous function improves performance, but cannot ensure that the surface buffer of the playback window is released. You must ensure the lifecycle of the playback window.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player Release** fails.

 |

#### \[h2\]OH\_AVPlayer\_ReleaseSync()

OH\_AVErrCode OH\_AVPlayer\_ReleaseSync(OH\_AVPlayer \*player)

**Description**

Synchronously releases an OH\_AVPlayer instance.

The synchronous function ensures that the display buffer of the playback window is released, with a long time. Therefore, you need to design an asynchronous mechanism.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player ReleaseSync** fails.

 |

#### \[h2\]OH\_AVPlayer\_SetVolume()

OH\_AVErrCode OH\_AVPlayer\_SetVolume(OH\_AVPlayer \*player, float leftVolume, float rightVolume)

**Description**

Sets the volume for an AVPlayer.

This function can be used when the AVPlayer is in the playing or paused state. The value **0** means that the AVPlayer is muted, and **1** means that the original volume is used.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| float leftVolume | Target volume of the left channel. |
| float rightVolume | Target volume of the right channel. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The volume is set successfully.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player SetVolume** fails.

 |

#### \[h2\]OH\_AVPlayer\_SetLoudnessGain()

OH\_AVErrCode OH\_AVPlayer\_SetLoudnessGain(OH\_AVPlayer \*player, float loudnessGain)

**Description**

Sets the loudness of the AVPlayer. This function can be called when the AVPlayer is in the prepared, playing, paused, completed, or stopped state.

The default loudness gain is 0.0 dB. The **usage** parameter of the AVPlayer stream must be [OH\_AudioStream\_Usage](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MUSIC,

[OH\_AudioStream\_Usage](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MOVIE, or [OH\_AudioStream\_Usage](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_AUDIOBOOK.

The latency mode of the audio renderer must be [OH\_AudioStream\_LatencyMode](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiostream_latencymode).AUDIOSTREAM\_LATENCY\_MODE\_NORMAL.

If the audio is played through the high-resolution pipeline, this operation is not supported.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 21

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| float loudnessGain | Loudness, in the range \[-90.0, 24.0\], in dB. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The loudness is set successfully.

**AV\_ERR\_INVALID\_VAL**: The **player** parameter is nullptr, or the **loudnessGain** parameter is invalid.

**AV\_ERR\_INVALID\_STATE**: The function is called in an abnormal state, or the **usage** parameter of **audioRendererInfo** is not one of the following:

[OH\_AudioStream\_Usage](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MUSIC,

[OH\_AudioStream\_Usage](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MOVIE,

and [OH\_AudioStream\_Usage](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_AUDIOBOOKs.

**AV\_ERR\_SERVICE\_DIED**: A system error occurs.

 |

#### \[h2\]OH\_AVPlayer\_Seek()

OH\_AVErrCode OH\_AVPlayer\_Seek(OH\_AVPlayer \*player, int32\_t mSeconds, AVPlayerSeekMode mode)

**Description**

Seeks to a playback position.

This function can be used when the AVPlayer is in the playing or paused state.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| int32\_t mSeconds | Position to seek to, in ms. |
| [AVPlayerSeekMode](../avplayer-base-h/document.md#avplayerseekmode) mode | Seek mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player Seek** fails.

 |

#### \[h2\]OH\_AVPlayer\_GetCurrentTime()

OH\_AVErrCode OH\_AVPlayer\_GetCurrentTime(OH\_AVPlayer \*player, int32\_t \*currentTime)

**Description**

Obtains the playback position, in milliseconds.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| int32\_t \*currentTime | Pointer to the playback position. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The playback position is obtained.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player GetCurrentTime** fails.

 |

#### \[h2\]OH\_AVPlayer\_GetVideoWidth()

OH\_AVErrCode OH\_AVPlayer\_GetVideoWidth(OH\_AVPlayer \*player, int32\_t \*videoWidth)

**Description**

Obtains the video width.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| int32\_t \*videoWidth | Pointer to the video width. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The video width is obtained.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr.

 |

#### \[h2\]OH\_AVPlayer\_GetVideoHeight()

OH\_AVErrCode OH\_AVPlayer\_GetVideoHeight(OH\_AVPlayer \*player, int32\_t \*videoHeight)

**Description**

Obtains the video height.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| int32\_t \*videoHeight | Pointer to the video height. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The video height is obtained.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr.

 |

#### \[h2\]OH\_AVPlayer\_SetPlaybackSpeed()

OH\_AVErrCode OH\_AVPlayer\_SetPlaybackSpeed(OH\_AVPlayer \*player, AVPlaybackSpeed speed)

**Description**

Sets the playback speed of the AVPlayer. For details about the playback speed, see [AVPlaybackSpeed](../avplayer-base-h/document.md#avplaybackspeed).

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| [AVPlaybackSpeed](../avplayer-base-h/document.md#avplaybackspeed) speed | Playback speed. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The playback speed is set successfully.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr.

 |

#### \[h2\]OH\_AVPlayer\_SetPlaybackRate()

OH\_AVErrCode OH\_AVPlayer\_SetPlaybackRate(OH\_AVPlayer \*player, float rate)

**Description**

Sets the playback rate of an AVPlayer within the valid range.

The supported states are prepared, playing, paused, and completed.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| float rate | Playback rate. The value ranges from 0.125 to 4. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The playback speed is set successfully.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The function is called when the AVPlayer is not in the allowed state, or it is called during live streaming.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or **rate** is out of range.

 |

#### \[h2\]OH\_AVPlayer\_GetPlaybackSpeed()

OH\_AVErrCode OH\_AVPlayer\_GetPlaybackSpeed(OH\_AVPlayer \*player, AVPlaybackSpeed \*speed)

**Description**

Obtains the playback speed of an AVPlayer.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| [AVPlaybackSpeed](../avplayer-base-h/document.md#avplaybackspeed) \*speed | Pointer to the playback speed. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The playback rate is obtained.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player GetPlaybackSpeed** fails.

 |

#### \[h2\]OH\_AVPlayer\_SetAudioRendererInfo()

OH\_AVErrCode OH\_AVPlayer\_SetAudioRendererInfo(OH\_AVPlayer \*player, OH\_AudioStream\_Usage streamUsage)

**Description**

Sets the audio stream type for an AVPlayer.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| [OH\_AudioStream\_Usage](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiostream_usage) streamUsage | Audio stream type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The audio stream type is set successfully.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr or **streamUsage** is invalid.

 |

#### \[h2\]OH\_AVPlayer\_SetVolumeMode()

OH\_AVErrCode OH\_AVPlayer\_SetVolumeMode(OH\_AVPlayer \*player, OH\_AudioStream\_VolumeMode volumeMode)

**Description**

Sets the audio volume mode for an AVPlayer.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 19

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| [OH\_AudioStream\_VolumeMode](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiostream_volumemode) volumeMode | Volume mode of the audio stream. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The audio volume mode is set successfully.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr or **volumeMode** is invalid.

**AV\_ERR\_INVALID\_STATE**: The function is called in an invalid state. It must be in the prepared state.

**AV\_ERR\_SERVICE\_DIED**: A system error occurs.

 |

#### \[h2\]OH\_AVPlayer\_SetAudioInterruptMode()

OH\_AVErrCode OH\_AVPlayer\_SetAudioInterruptMode(OH\_AVPlayer \*player, OH\_AudioInterrupt\_Mode interruptMode)

**Description**

Sets the audio interruption mode for an AVPlayer.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| [OH\_AudioInterrupt\_Mode](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiointerrupt_mode) interruptMode | Audio interruption mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The audio interruption mode is set successfully.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr or **interruptMode** is invalid.

 |

#### \[h2\]OH\_AVPlayer\_SetAudioEffectMode()

OH\_AVErrCode OH\_AVPlayer\_SetAudioEffectMode(OH\_AVPlayer \*player, OH\_AudioStream\_AudioEffectMode effectMode)

**Description**

Sets the audio effect mode for an AVPlayer.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| [OH\_AudioStream\_AudioEffectMode](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiostream_audioeffectmode) effectMode | Audio effect mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The audio effect mode is set successfully.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr or **effectMode** is invalid.

 |

#### \[h2\]OH\_AVPlayer\_SelectBitRate()

OH\_AVErrCode OH\_AVPlayer\_SelectBitRate(OH\_AVPlayer \*player, uint32\_t bitRate)

**Description**

Sets the bit rate used by an HLS player. This function is valid only for HLS network streams.

By default, the AVPlayer selects a proper bit rate and speed based on the network connection.

You can set a bit rate available in the valid bit rates reported in **INFO\_TYPE\_BITRATE\_COLLECT**. The AVPlayer selects a bit rate that is lower than and closest to the specified bit rate. When ready, you can query the selected bit rate.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| uint32\_t bitRate | Bit rate, in kbit/s. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The bit rate is set successfully.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player SelectBitRate** fails.

 |

#### \[h2\]OH\_AVPlayer\_SetVideoSurface()

OH\_AVErrCode OH\_AVPlayer\_SetVideoSurface(OH\_AVPlayer \*player, OHNativeWindow \*window)

**Description**

Sets a playback window.

This function must be called after **SetSource** and before **Prepare**.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| OHNativeWindow \*window | Pointer to the OHNativeWindow instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The playback window is set successfully.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** or **window** is nullptr, or the execution of **player SetVideoSurface** fails.

 |

#### \[h2\]OH\_AVPlayer\_GetDuration()

OH\_AVErrCode OH\_AVPlayer\_GetDuration(OH\_AVPlayer \*player, int32\_t \*duration)

**Description**

Obtains the total duration of a media file, in milliseconds.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| int32\_t \*duration | Pointer to the total duration. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The total duration is obtained.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player GetDuration** fails.

 |

#### \[h2\]OH\_AVPlayer\_GetState()

OH\_AVErrCode OH\_AVPlayer\_GetState(OH\_AVPlayer \*player, AVPlayerState \*state)

**Description**

Obtains the AVPlayer state.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| [AVPlayerState](../avplayer-base-h/document.md#avplayerstate) \*state | Pointer to the state of the AVPlayer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The AVPlayer state is obtained.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player GetState** fails.

 |

#### \[h2\]OH\_AVPlayer\_IsPlaying()

bool OH\_AVPlayer\_IsPlaying(OH\_AVPlayer \*player)

**Description**

Checks whether an AVPlayer is playing.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for whether the AVPlayer is playing. **true** if yes, **false** if the AVPlayer is not playing or the input parameter **player** is nullptr. |

#### \[h2\]OH\_AVPlayer\_IsLooping()

bool OH\_AVPlayer\_IsLooping(OH\_AVPlayer \*player)

**Description**

Checks whether an AVPlayer is looping.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for whether the AVPlayer is looping. **true** if yes, **false** if the AVPlayer is not looping or the input parameter **player** is nullptr. |

#### \[h2\]OH\_AVPlayer\_SetLooping()

OH\_AVErrCode OH\_AVPlayer\_SetLooping(OH\_AVPlayer \*player, bool loop)

**Description**

Enables loop playback.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| bool loop | Whether to enable loop playback. **true** to play in a loop, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: Loop playback is enabled.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player SetLooping** fails.

 |

#### \[h2\]OH\_AVPlayer\_SetPlayerCallback()

OH\_AVErrCode OH\_AVPlayer\_SetPlayerCallback(OH\_AVPlayer \*player, AVPlayerCallback callback)

**Description**

Sets an AVPlayer callback.

The callbacks [OH\_AVPlayerOnInfo](../avplayer-base-h/document.md#oh_avplayeroninfo) and [OH\_AVPlayerOnError](../avplayer-base-h/document.md#oh_avplayeronerror) set by using this function can transfer limited information. In addition, it is inconvenient for the application to distinguish between multiple AVPlayer instances.

Starting from API version 12, [OH\_AVPlayer\_SetOnInfoCallback](#oh_avplayer_setoninfocallback) and [OH\_AVPlayer\_SetOnErrorCallback](#oh_avplayer_setonerrorcallback) are provided to set the callbacks [OH\_AVPlayerOnInfoCallback](../avplayer-base-h/document.md#oh_avplayeroninfocallback) and [OH\_AVPlayerOnErrorCallback](../avplayer-base-h/document.md#oh_avplayeronerrorcallback), respectively.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Deprecated from**: 12

**Substitute**: [OH\_AVPlayer\_SetOnInfoCallback](#oh_avplayer_setoninfocallback) and [OH\_AVPlayer\_SetOnErrorCallback](#oh_avplayer_setonerrorcallback)

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| [AVPlayerCallback](../../structs/avplayercallback/document.md) callback | Callback used to return the result. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The callback is set successfully.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, the input parameter **callback.onInfo** or **onError** is null, or the execution of **player SetPlayerCallback** fails.

 |

#### \[h2\]OH\_AVPlayer\_SelectTrack()

OH\_AVErrCode OH\_AVPlayer\_SelectTrack(OH\_AVPlayer \*player, int32\_t index)

**Description**

Selects an audio or subtitle track.

By default, the first audio track with data is played, and the subtitle track is not played.

After the setting takes effect, the original track becomes invalid. Set the subtitle track to the prepared, playing, paused, or completed state, and set the audio track to the prepared state.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| int32\_t index | Index of the track. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player SelectTrack** fails.

 |

#### \[h2\]OH\_AVPlayer\_DeselectTrack()

OH\_AVErrCode OH\_AVPlayer\_DeselectTrack(OH\_AVPlayer \*player, int32\_t index)

**Description**

Deselects an audio or subtitle track.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| int32\_t index | Index of the track. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player DeselectTrack** fails.

 |

#### \[h2\]OH\_AVPlayer\_GetCurrentTrack()

OH\_AVErrCode OH\_AVPlayer\_GetCurrentTrack(OH\_AVPlayer \*player, int32\_t trackType, int32\_t \*index)

**Description**

Obtains the currently valid track. You can set the track to the prepared, playing, paused, or completed state.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| int32\_t trackType | Media type. The value **0** means audio and **1** means video. |
| int32\_t \*index | Pointer to the index of the track. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The track is obtained.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **player GetCurrentTrack** fails.

 |

#### \[h2\]OH\_AVPlayer\_SetMediaKeySystemInfoCallback()

OH\_AVErrCode OH\_AVPlayer\_SetMediaKeySystemInfoCallback(OH\_AVPlayer \*player, Player\_MediaKeySystemInfoCallback callback)

**Description**

Sets a callback to return the media key system information for an AVPlayer.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| [Player\_MediaKeySystemInfoCallback](#player_mediakeysysteminfocallback) callback | Callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** or **callback** is a null pointer, or the execution of **player SetDrmSystemInfoCallback**

**SetDrmSystemInfoCallback** or **SetDrmSystemInfoCallback** fails.

 |

#### \[h2\]OH\_AVPlayer\_GetMediaKeySystemInfo()

OH\_AVErrCode OH\_AVPlayer\_GetMediaKeySystemInfo(OH\_AVPlayer \*player, DRM\_MediaKeySystemInfo \*mediaKeySystemInfo)

**Description**

Obtains the media key system information to create a media key session.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| [DRM\_MediaKeySystemInfo](../../structs/drm-mediakeysysteminfo/document.md) \*mediaKeySystemInfo | Pointer to the media key system information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the memory is insufficient.

 |

#### \[h2\]OH\_AVPlayer\_SetDecryptionConfig()

OH\_AVErrCode OH\_AVPlayer\_SetDecryptionConfig(OH\_AVPlayer \*player, MediaKeySession \*mediaKeySession, bool secureVideoPath)

**Description**

Sets the decryption information.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| [MediaKeySession](../../structs/mediakeysession/document.md) \*mediaKeySession | Pointer to the media key session with the decryption feature. |
| bool secureVideoPath | Whether a secure decoder is required. **true** if required, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr, or the execution of **SetDecryptionConfig** fails.

 |

#### \[h2\]OH\_AVPlayer\_SetOnInfoCallback()

OH\_AVErrCode OH\_AVPlayer\_SetOnInfoCallback(OH\_AVPlayer \*player, OH\_AVPlayerOnInfoCallback callback, void \*userData)

**Description**

Sets a callback for the event indicating that the AVPlayer receives a message.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| [OH\_AVPlayerOnInfoCallback](../avplayer-base-h/document.md#oh_avplayeroninfocallback) callback | Pointer to the callback. If nullptr is passed in, the listening for AVPlayer messages is canceled. |
| void \*userData | Pointer to the instance set by the caller. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_NO\_MEMORY**: Memory allocation fails.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr or the function fails to be executed.

 |

#### \[h2\]OH\_AVPlayer\_SetOnErrorCallback()

OH\_AVErrCode OH\_AVPlayer\_SetOnErrorCallback(OH\_AVPlayer \*player, OH\_AVPlayerOnErrorCallback callback, void \*userData)

**Description**

Sets a callback for the event indicating that an error occurs in the AVPlayer.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| [OH\_AVPlayerOnErrorCallback](../avplayer-base-h/document.md#oh_avplayeronerrorcallback) callback | Pointer to the callback. If nullptr is passed in, the listening for AVPlayer errors is canceled. |
| void \*userData | Pointer to the instance set by the caller. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_NO\_MEMORY**: Memory allocation fails.

**AV\_ERR\_INVALID\_VAL**: The input parameter **player** is nullptr or the function fails to be executed.

 |

#### \[h2\]OH\_AVPlayer\_GetMediaDescription()

OH\_AVFormat \*OH\_AVPlayer\_GetMediaDescription(OH\_AVPlayer \*player)

**Description**

Obtains the media source information for the AVPlayer. This function can be called when the playback resource is configured and the AVPlayer is in the initialized, prepared, playing, paused, completed, or stopped state.

You must manually release the returned OH\_AVFormat pointer object when it is no longer needed.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVFormat](../../structs/oh-avformat/document.md) \* | 
Media source information obtained. If the operation fails, nullptr is returned.

Possible cause:

1\. The **player** pointer is invalid.

2\. The playback resource is invalid.

 |

#### \[h2\]OH\_AVPlayer\_GetTrackDescription()

OH\_AVFormat \*OH\_AVPlayer\_GetTrackDescription(OH\_AVPlayer \*player, uint32\_t index)

**Description**

Obtains the media source track information for the AVPlayer by index. This function can be called when the playback resource is configured and the AVPlayer is in the initialized, prepared, playing, paused, completed, or stopped state.

You must manually release the returned OH\_AVFormat pointer object when it is no longer needed.

**System capability**: SystemCapability.Multimedia.Media.AVPlayer

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVPlayer](../../structs/oh-avplayer/document.md) \*player | Pointer to the OH\_AVPlayer instance. |
| uint32\_t index | Index of the track. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVFormat](../../structs/oh-avformat/document.md) \* | 
Track information obtained. If the operation fails, nullptr is returned.

Possible cause:

1\. The **player** pointer is invalid.

2\. The playback resource is invalid.

3\. The track index is out of the range for the playback source file array.

 |
