# native\_avmuxer.h

#### Overview

The file declares the native APIs used for audio and video multiplexing.

**File to include**: <multimedia/player\_framework/native\_avmuxer.h>

**Library**: libnative\_media\_avmuxer.so

**System capability**: SystemCapability.Multimedia.Media.Muxer

**Since**: 10

**Related module**: [AVMuxer](../../modules/avmuxer/document.md)

**Sample**: [AVCodec](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVMuxer](../../structs/oh-avmuxer/document.md) | OH\_AVMuxer | Describes a native object for the muxer interface. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_AVMuxer \*OH\_AVMuxer\_Create(int32\_t fd, OH\_AVOutputFormat format)](#oh_avmuxer_create) | Creates an OH\_AVMuxer instance by using the file descriptor and container format. |
| [OH\_AVErrCode OH\_AVMuxer\_SetRotation(OH\_AVMuxer \*muxer, int32\_t rotation)](#oh_avmuxer_setrotation) | Sets the rotation angle (clockwise), which must be 0, 90, 180, or 270, of an output video. This function must be called before [OH\_AVMuxer\_Start](#oh_avmuxer_start). |
| [OH\_AVErrCode OH\_AVMuxer\_SetFormat(OH\_AVMuxer \*muxer, OH\_AVFormat \*format)](#oh_avmuxer_setformat) | 
Sets format data to the muxer.

Starting from API version 14, setting the creation time via **OH\_MD\_KEY\_CREATION\_TIME** is supported. If the setting fails, check whether the value of **OH\_MD\_KEY\_CREATION\_TIME** complies with the ISO 8601 standard and whether the UTC time is used.

Starting from API version 20, the following operations are supported:

\- Setting the file description via **OH\_MD\_KEY\_COMMENT**. If the setting fails, check whether **OH\_MD\_KEY\_COMMENT** is a string within the range \[1, 256\].

\- Setting the position of the MP4 moov via **OH\_MD\_KEY\_ENABLE\_MOOV\_FRONT**. If **OH\_MD\_KEY\_ENABLE\_MOOV\_FRONT** is set to **0**, moov is placed at the end. If it is set to **1**, moov is placed at the front. By default, moov is placed at the end.

 |
| [OH\_AVErrCode OH\_AVMuxer\_AddTrack(OH\_AVMuxer \*muxer, int32\_t \*trackIndex, OH\_AVFormat \*trackFormat)](#oh_avmuxer_addtrack) | Adds an audio or video track to a muxer. Each time this function is called, an audio or video track is added to the muxer. This function must be called before [OH\_AVMuxer\_Start](#oh_avmuxer_start). |
| [OH\_AVErrCode OH\_AVMuxer\_Start(OH\_AVMuxer \*muxer)](#oh_avmuxer_start) | Starts a muxer. This function must be called after [OH\_AVMuxer\_AddTrack](#oh_avmuxer_addtrack) and before [OH\_AVMuxer\_WriteSample](#oh_avmuxer_writesample). |
| [OH\_AVErrCode OH\_AVMuxer\_WriteSample(OH\_AVMuxer \*muxer, uint32\_t trackIndex, OH\_AVMemory \*sample, OH\_AVCodecBufferAttr info)](#oh_avmuxer_writesample) | Writes a sample to a muxer. This function must be called after [OH\_AVMuxer\_Start](#oh_avmuxer_start) and before [OH\_AVMuxer\_Stop](#oh_avmuxer_stop). The caller must write the sample to the correct audio or video track based on the timing in **info**. |
| [OH\_AVErrCode OH\_AVMuxer\_WriteSampleBuffer(OH\_AVMuxer \*muxer, uint32\_t trackIndex, const OH\_AVBuffer \*sample)](#oh_avmuxer_writesamplebuffer) | Writes a sample to a muxer. This function must be called after [OH\_AVMuxer\_Start](#oh_avmuxer_start) and before [OH\_AVMuxer\_Stop](#oh_avmuxer_stop). The caller must write the sample to the correct audio or video track based on the timing in **sample**. |
| [OH\_AVErrCode OH\_AVMuxer\_Stop(OH\_AVMuxer \*muxer)](#oh_avmuxer_stop) | Stops a muxer. Once the muxer is stopped, it cannot be restarted. |
| [OH\_AVErrCode OH\_AVMuxer\_Destroy(OH\_AVMuxer \*muxer)](#oh_avmuxer_destroy) | 

Clears internal resources and destroys an OH\_AVMuxer instance.

Do not repeatedly destroy the instance. Otherwise, the program may crash.

 |

#### Function Description

#### \[h2\]OH\_AVMuxer\_Create()

OH\_AVMuxer \*OH\_AVMuxer\_Create(int32\_t fd, OH\_AVOutputFormat format)

**Description**

Creates an OH\_AVMuxer instance by using the file descriptor and container format.

**System capability**: SystemCapability.Multimedia.Media.Muxer

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t fd | File descriptor (FD). You must open the file in read/write mode (O\_RDWR) and close the file after using it. |
| [OH\_AVOutputFormat](../native-avcodec-base-h/document.md#oh_avoutputformat) format | Format of the multiplexed output file. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVMuxer](../../structs/oh-avmuxer/document.md) \* | Pointer to the **OH\_AVMuxer** instance created. You must call [OH\_AVMuxer\_Destroy](#oh_avmuxer_destroy) to destroy the instance when it is no longer needed. |

#### \[h2\]OH\_AVMuxer\_SetRotation()

OH\_AVErrCode OH\_AVMuxer\_SetRotation(OH\_AVMuxer \*muxer, int32\_t rotation)

**Description**

Sets the rotation angle (clockwise), which must be 0, 90, 180, or 270, of an output video. This function must be called before [OH\_AVMuxer\_Start](#oh_avmuxer_start).

**System capability**: SystemCapability.Multimedia.Media.Muxer

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMuxer](../../structs/oh-avmuxer/document.md) \*muxer | Pointer to an OH\_AVMuxer instance. |
| int32\_t rotation | Angle to set. The value must be 0, 90, 180, or 270. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The muxer pointer is null or the value of **rotation** is invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The function is called out of sequence.

 |

#### \[h2\]OH\_AVMuxer\_SetFormat()

OH\_AVErrCode OH\_AVMuxer\_SetFormat(OH\_AVMuxer \*muxer, OH\_AVFormat \*format)

**Description**

Sets format data to the muxer.

Starting from API version 14, setting the creation time via **OH\_MD\_KEY\_CREATION\_TIME** is supported. If the setting fails, check whether the value of **OH\_MD\_KEY\_CREATION\_TIME** complies with the ISO 8601 standard and whether the UTC time is used.

Starting from API version 20, the following operations are supported:

-   Setting the file description via **OH\_MD\_KEY\_COMMENT**. If the setting fails, check whether **OH\_MD\_KEY\_COMMENT** is a string within the range \[1, 256\].
-   Setting the position of the MP4 moov via **OH\_MD\_KEY\_ENABLE\_MOOV\_FRONT**. If **OH\_MD\_KEY\_ENABLE\_MOOV\_FRONT** is set to **0**, moov is placed at the end. If it is set to **1**, moov is placed at the front. By default, moov is placed at the end.

**System capability**: SystemCapability.Multimedia.Media.Muxer

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMuxer](../../structs/oh-avmuxer/document.md) \*muxer | Pointer to an OH\_AVMuxer instance. |
| [OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. It is a file-level metadata set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The **format** parameter is correctly set.

**AV\_ERR\_INVALID\_VAL**: The muxer pointer is null or the value of **format** is invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The function is called out of sequence.

 |

#### \[h2\]OH\_AVMuxer\_AddTrack()

OH\_AVErrCode OH\_AVMuxer\_AddTrack(OH\_AVMuxer \*muxer, int32\_t \*trackIndex, OH\_AVFormat \*trackFormat)

**Description**

Adds an audio or video track to a muxer. Each time this function is called, an audio or video track is added to the muxer. This function must be called before [OH\_AVMuxer\_Start](#oh_avmuxer_start).

**System capability**: SystemCapability.Multimedia.Media.Muxer

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMuxer](../../structs/oh-avmuxer/document.md) \*muxer | Pointer to an OH\_AVMuxer instance. |
| int32\_t \*trackIndex | Pointer to the index of the media track. The index will be used in the [OH\_AVMuxer\_WriteSample](#oh_avmuxer_writesample) function. If the media track is added, the index value is greater than or equal to 0; otherwise, the value is less than 0. |
| [OH\_AVFormat](../../structs/oh-avformat/document.md) \*trackFormat | Pointer to an OH\_AVFormat instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The muxer pointer is null, or the track index or track format is invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The function is called out of sequence.

**AV\_ERR\_UNSUPPORT**: The MIME type is not supported.

**AV\_ERR\_NO\_MEMORY**: Memory allocation fails.

**AV\_ERR\_UNKNOWN**: An unknown error occurs.

 |

#### \[h2\]OH\_AVMuxer\_Start()

OH\_AVErrCode OH\_AVMuxer\_Start(OH\_AVMuxer \*muxer)

**Description**

Starts a muxer. This function must be called after [OH\_AVMuxer\_AddTrack](#oh_avmuxer_addtrack) and before [OH\_AVMuxer\_WriteSample](#oh_avmuxer_writesample).

**System capability**: SystemCapability.Multimedia.Media.Muxer

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMuxer](../../structs/oh-avmuxer/document.md) \*muxer | Pointer to an OH\_AVMuxer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The muxer pointer is null.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The function is called out of sequence.

**AV\_ERR\_UNKNOWN**: An unknown error occurs.

 |

#### \[h2\]OH\_AVMuxer\_WriteSample()

OH\_AVErrCode OH\_AVMuxer\_WriteSample(OH\_AVMuxer \*muxer, uint32\_t trackIndex, OH\_AVMemory \*sample, OH\_AVCodecBufferAttr info)

**Description**

Writes a sample to a muxer. This function must be called after [OH\_AVMuxer\_Start](#oh_avmuxer_start) and before [OH\_AVMuxer\_Stop](#oh_avmuxer_stop). The caller must write the sample to the correct audio or video track based on the timing in **info**.

**System capability**: SystemCapability.Multimedia.Media.Muxer

**Since**: 10

**Deprecated from**: 11

**Substitute**: [OH\_AVMuxer\_WriteSampleBuffer](#oh_avmuxer_writesamplebuffer)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMuxer](../../structs/oh-avmuxer/document.md) \*muxer | Pointer to an OH\_AVMuxer instance. |
| uint32\_t trackIndex | Index of the audio or video track corresponding to the data. |
| [OH\_AVMemory](../../structs/oh-avmemory/document.md) \*sample | Pointer to the data obtained after encoding or demultiplexing. |
| [OH\_AVCodecBufferAttr](../../structs/oh-avcodecbufferattr/document.md) info | Sample description. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The muxer pointer is null, or the track index, sample, or info is invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The function is called out of sequence.

**AV\_ERR\_NO\_MEMORY**: Memory allocation fails.

**AV\_ERR\_UNKNOWN**: An unknown error occurs.

 |

#### \[h2\]OH\_AVMuxer\_WriteSampleBuffer()

OH\_AVErrCode OH\_AVMuxer\_WriteSampleBuffer(OH\_AVMuxer \*muxer, uint32\_t trackIndex, const OH\_AVBuffer \*sample)

**Description**

Writes a sample to a muxer. This function must be called after [OH\_AVMuxer\_Start](#oh_avmuxer_start) and before [OH\_AVMuxer\_Stop](#oh_avmuxer_stop). The caller must write the sample to the correct audio or video track based on the timing in **sample**.

**System capability**: SystemCapability.Multimedia.Media.Muxer

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMuxer](../../structs/oh-avmuxer/document.md) \*muxer | Pointer to an OH\_AVMuxer instance. |
| uint32\_t trackIndex | Index of the audio or video track corresponding to the data. |
| const [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) \*sample | Pointer to the data and properties obtained after encoding or demultiplexing. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The muxer pointer is null, or the track index or sample is invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The function is called out of sequence.

**AV\_ERR\_NO\_MEMORY**: Memory allocation fails.

**AV\_ERR\_UNKNOWN**: An unknown error occurs.

 |

#### \[h2\]OH\_AVMuxer\_Stop()

OH\_AVErrCode OH\_AVMuxer\_Stop(OH\_AVMuxer \*muxer)

**Description**

Stops a muxer. Once the muxer is stopped, it cannot be restarted.

**System capability**: SystemCapability.Multimedia.Media.Muxer

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMuxer](../../structs/oh-avmuxer/document.md) \*muxer | Pointer to an OH\_AVMuxer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The muxer pointer is null.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The function is called out of sequence.

 |

#### \[h2\]OH\_AVMuxer\_Destroy()

OH\_AVErrCode OH\_AVMuxer\_Destroy(OH\_AVMuxer \*muxer)

**Description**

Clears internal resources and destroys an OH\_AVMuxer instance.

Do not repeatedly destroy the instance. Otherwise, the program may crash.

**System capability**: SystemCapability.Multimedia.Media.Muxer

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMuxer](../../structs/oh-avmuxer/document.md) \*muxer | Pointer to an OH\_AVMuxer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The muxer pointer is null.

 |
