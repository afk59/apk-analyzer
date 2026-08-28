# native\_avdemuxer.h

#### Overview

The file declares the APIs for parsing audio and video media data.

**File to include**: <multimedia/player\_framework/native\_avdemuxer.h>

**Library**: libnative\_media\_avdemuxer.so

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 10

**Related module**: [AVDemuxer](../../modules/avdemuxer/document.md)

**Sample**: [AVCodec](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVDemuxer](../../structs/oh-avdemuxer/document.md) | OH\_AVDemuxer | Describes a native object for the OH\_AVDemuxer interface. |
| [DRM\_MediaKeySystemInfo](../../structs/drm-mediakeysysteminfo/document.md) | DRM\_MediaKeySystemInfo | Describes a native object for the DRM\_MediaKeySystemInfo API. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*DRM\_MediaKeySystemInfoCallback)(DRM\_MediaKeySystemInfo\* mediaKeySystemInfo)](#drm_mediakeysysteminfocallback) | DRM\_MediaKeySystemInfoCallback | 
Defines a pointer to the callback function for DRM\_MediaKeySystemInfo. No demuxer instance is returned. This callback function applies to the scenario where a single demuxer instance is used.

You need to call [OH\_AVDemuxer\_SetMediaKeySystemInfoCallback](#oh_avdemuxer_setmediakeysysteminfocallback) to set the callback function as a callback.

 |
| [typedef void (\*Demuxer\_MediaKeySystemInfoCallback)(OH\_AVDemuxer \*demuxer, DRM\_MediaKeySystemInfo \*mediaKeySystemInfo)](#demuxer_mediakeysysteminfocallback) | Demuxer\_MediaKeySystemInfoCallback | 

Defines a pointer to the callback function for **DRM\_MediaKeySystemInfo**. A demuxer instance is returned. This callback function applies to the scenario where multiple demuxer instances are used.

You need to call [OH\_AVDemuxer\_SetDemuxerMediaKeySystemInfoCallback](#oh_avdemuxer_setdemuxermediakeysysteminfocallback) to set the callback function as a callback. This callback function is recommended.

 |
| [OH\_AVDemuxer \*OH\_AVDemuxer\_CreateWithSource(OH\_AVSource \*source)](#oh_avdemuxer_createwithsource) | \- | 

Creates an OH\_AVDemuxer instance based on a source instance.

For details about how to create, destroy, and use a source instance, see [OH\_AVSource](../../modules/avsource/document.md).

 |
| [OH\_AVErrCode OH\_AVDemuxer\_Destroy(OH\_AVDemuxer \*demuxer)](#oh_avdemuxer_destroy) | \- | 

Destroys an OH\_AVDemuxer instance and clears internal resources. An instance can be destroyed only once.

The destroyed instance cannot be used until it is re-created. You are advised to set the pointer to NULL after the instance is destroyed.

 |
| [OH\_AVErrCode OH\_AVDemuxer\_SelectTrackByID(OH\_AVDemuxer \*demuxer, uint32\_t trackIndex)](#oh_avdemuxer_selecttrackbyid) | \- | 

Selects a track from which the demuxer reads sample data.

You can select multiple tracks by calling this API multiple times, with a different track index passed in each time.

When [OH\_AVDemuxer\_ReadSample](#oh_avdemuxer_readsample) is called, only the data in the selected track is read. If the same track is selected multiple times, **AV\_ERR\_OK** is returned and the API call takes effect only once.

 |
| [OH\_AVErrCode OH\_AVDemuxer\_UnselectTrackByID(OH\_AVDemuxer \*demuxer, uint32\_t trackIndex)](#oh_avdemuxer_unselecttrackbyid) | \- | 

Deselects a track. The demuxer no longer reads sample data from a track after it is deselected.

You can deselect multiple tracks by calling this API multiple times, with a different track index passed in each time.

If the same track is deselected multiple times, **AV\_ERR\_OK** is returned and the API call takes effect only once.

 |
| [OH\_AVErrCode OH\_AVDemuxer\_ReadSample(OH\_AVDemuxer \*demuxer, uint32\_t trackIndex, OH\_AVMemory \*sample, OH\_AVCodecBufferAttr \*info)](#oh_avdemuxer_readsample) | \- | 

Reads the sample and related information from the specified track.

You must select a track before reading the sample. After this API is called, the demuxer automatically proceeds to the next frame.

 |
| [OH\_AVErrCode OH\_AVDemuxer\_ReadSampleBuffer(OH\_AVDemuxer \*demuxer, uint32\_t trackIndex, OH\_AVBuffer \*sample)](#oh_avdemuxer_readsamplebuffer) | \- | 

Reads the sample and related information from the specified track.

You must select a track before reading the sample. After this API is called, the demuxer automatically proceeds to the next frame.

 |
| [OH\_AVErrCode OH\_AVDemuxer\_SeekToTime(OH\_AVDemuxer \*demuxer, int64\_t millisecond, OH\_AVSeekMode mode)](#oh_avdemuxer_seektotime) | \- | Seeks to the specified time for all the selected tracks based on a seek mode. |
| [OH\_AVErrCode OH\_AVDemuxer\_SetMediaKeySystemInfoCallback(OH\_AVDemuxer \*demuxer, DRM\_MediaKeySystemInfoCallback callback)](#oh_avdemuxer_setmediakeysysteminfocallback) | \- | Sets a callback for obtaining the media key system information. |
| [OH\_AVErrCode OH\_AVDemuxer\_SetDemuxerMediaKeySystemInfoCallback(OH\_AVDemuxer \*demuxer, Demuxer\_MediaKeySystemInfoCallback callback)](#oh_avdemuxer_setdemuxermediakeysysteminfocallback) | \- | Sets a callback for obtaining the media key system information. |
| [OH\_AVErrCode OH\_AVDemuxer\_GetMediaKeySystemInfo(OH\_AVDemuxer \*demuxer, DRM\_MediaKeySystemInfo \*mediaKeySystemInfo)](#oh_avdemuxer_getmediakeysysteminfo) | \- | Obtains the media key system information. The media key system information can be obtained only after [Demuxer\_MediaKeySystemInfoCallback](#demuxer_mediakeysysteminfocallback) or [DRM\_MediaKeySystemInfoCallback](#drm_mediakeysysteminfocallback) is successfully invoked. |

#### Function Description

#### \[h2\]DRM\_MediaKeySystemInfoCallback()

typedef void (\*DRM\_MediaKeySystemInfoCallback)(DRM\_MediaKeySystemInfo\* mediaKeySystemInfo)

**Description**

Defines a pointer to the callback function for DRM\_MediaKeySystemInfo. No demuxer instance is returned. This callback function applies to the scenario where a single demuxer instance is used.

You need to call [OH\_AVDemuxer\_SetMediaKeySystemInfoCallback](#oh_avdemuxer_setmediakeysysteminfocallback) to set the callback function as a callback.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 11

**Deprecated from**: 14

**Substitute**: [Demuxer\_MediaKeySystemInfoCallback](#demuxer_mediakeysysteminfocallback)

#### \[h2\]Demuxer\_MediaKeySystemInfoCallback()

typedef void (\*Demuxer\_MediaKeySystemInfoCallback)(OH\_AVDemuxer \*demuxer, DRM\_MediaKeySystemInfo \*mediaKeySystemInfo)

**Description**

Defines a pointer to the callback function for **DRM\_MediaKeySystemInfo**. A demuxer instance is returned. This callback function applies to the scenario where multiple demuxer instances are used.

You need to call [OH\_AVDemuxer\_SetDemuxerMediaKeySystemInfoCallback](#oh_avdemuxer_setdemuxermediakeysysteminfocallback) to set the callback function as a callback. This callback function is recommended.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 12

#### \[h2\]OH\_AVDemuxer\_CreateWithSource()

OH\_AVDemuxer \*OH\_AVDemuxer\_CreateWithSource(OH\_AVSource \*source)

**Description**

Creates an OH\_AVDemuxer instance based on a source instance.

For details about how to create, destroy, and use a source instance, see [OH\_AVSource](../../modules/avsource/document.md).

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSource](../../structs/oh-avsource/document.md) \*source | Pointer to an OH\_AVSource instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVDemuxer](../../structs/oh-avdemuxer/document.md) \* | 
Pointer to an OH\_AVDemuxer instance.

If the operation fails, NULL is returned.

The possible causes of an operation failure are as follows:

1\. The value of **source** is invalid (either nullptr or a pointer to a non-OH\_AVSource instance).

2\. The value of **source** does not point to an OH\_AVSource instance.

 |

#### \[h2\]OH\_AVDemuxer\_Destroy()

OH\_AVErrCode OH\_AVDemuxer\_Destroy(OH\_AVDemuxer \*demuxer)

**Description**

Destroys an OH\_AVDemuxer instance and clears internal resources. An instance can be destroyed only once.

The destroyed instance cannot be used until it is re-created. You are advised to set the pointer to NULL after the instance is destroyed.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVDemuxer](../../structs/oh-avdemuxer/document.md) \*demuxer | Pointer to an OH\_AVDemuxer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The value of **demuxer** is nullptr or does not point to a demuxer instance.

 |

#### \[h2\]OH\_AVDemuxer\_SelectTrackByID()

OH\_AVErrCode OH\_AVDemuxer\_SelectTrackByID(OH\_AVDemuxer \*demuxer, uint32\_t trackIndex)

**Description**

Selects a track from which the demuxer reads sample data.

You can select multiple tracks by calling this API multiple times, with a different track index passed in each time.

When [OH\_AVDemuxer\_ReadSample](#oh_avdemuxer_readsample) is called, only the data in the selected track is read. If the same track is selected multiple times, **AV\_ERR\_OK** is returned and the API call takes effect only once.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVDemuxer](../../structs/oh-avdemuxer/document.md) \*demuxer | Pointer to an OH\_AVDemuxer instance. |
| uint32\_t trackIndex | Index of the track. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**:

1\. The value of **demuxer** is nullptr or does not point to a demuxer instance.

2\. The track index is out of range.

3\. Track reading is not supported.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The demuxer is not correctly initialized.

 |

#### \[h2\]OH\_AVDemuxer\_UnselectTrackByID()

OH\_AVErrCode OH\_AVDemuxer\_UnselectTrackByID(OH\_AVDemuxer \*demuxer, uint32\_t trackIndex)

**Description**

Deselects a track. The demuxer no longer reads sample data from a track after it is deselected.

You can deselect multiple tracks by calling this API multiple times, with a different track index passed in each time.

If the same track is deselected multiple times, **AV\_ERR\_OK** is returned and the API call takes effect only once.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVDemuxer](../../structs/oh-avdemuxer/document.md) \*demuxer | Pointer to an OH\_AVDemuxer instance. |
| uint32\_t trackIndex | Index of the track. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The value of **demuxer** is nullptr or does not point to a demuxer instance.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The demuxer is not correctly initialized.

 |

#### \[h2\]OH\_AVDemuxer\_ReadSample()

OH\_AVErrCode OH\_AVDemuxer\_ReadSample(OH\_AVDemuxer \*demuxer, uint32\_t trackIndex, OH\_AVMemory \*sample, OH\_AVCodecBufferAttr \*info)

**Description**

Reads the sample and related information from the specified track.

You must select a track before reading the sample. After this API is called, the demuxer automatically proceeds to the next frame.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 10

**Deprecated from**: 11

**Substitute**: [OH\_AVDemuxer\_ReadSampleBuffer](#oh_avdemuxer_readsamplebuffer)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVDemuxer](../../structs/oh-avdemuxer/document.md) \*demuxer | Pointer to an OH\_AVDemuxer instance. |
| uint32\_t trackIndex | Index of the track from which the compressed frame is to be read. |
| [OH\_AVMemory](../../structs/oh-avmemory/document.md) \*sample | Pointer to the OH\_AVMemory instance for storing the compressed frame data. |
| [OH\_AVCodecBufferAttr](../../structs/oh-avcodecbufferattr/document.md) \*info | Pointer to the OH\_AVCodecBufferAttr instance for storing the compressed frame information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**:

1\. The value of **demuxer** is nullptr or does not point to a demuxer instance.

2\. The track index is out of range.

3\. Track reading is not supported.

4\. The value of **sample** is null.

5\. The value of **info** is null.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**:

1\. The track with the specified index is not selected.

2\. The demuxer is not correctly initialized.

**AV\_ERR\_NO\_MEMORY**: The sample capacity is insufficient to store all frame data.

**AV\_ERR\_UNKNOWN**: Failed to read or parse the frame from the file.

 |

#### \[h2\]OH\_AVDemuxer\_ReadSampleBuffer()

OH\_AVErrCode OH\_AVDemuxer\_ReadSampleBuffer(OH\_AVDemuxer \*demuxer, uint32\_t trackIndex, OH\_AVBuffer \*sample)

**Description**

Reads the sample and related information from the specified track.

You can use [OH\_AVDemuxer\_SelectTrackByID](#oh_avdemuxer_selecttrackbyid) to select a track before reading the sample. After this API is called, the demuxer automatically proceeds to the next frame.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVDemuxer](../../structs/oh-avdemuxer/document.md) \*demuxer | Pointer to an OH\_AVDemuxer instance. |
| uint32\_t trackIndex | Index of the track from which the compressed frame is to be read. |
| OH\_AVBuffer \*sample | Pointer to the OH\_AVBuffer instance for storing the compressed frame data and related information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**:

1\. The value of **demuxer** is nullptr or does not point to a demuxer instance.

2\. The value of **sample** is nullptr.

3\. The track index is out of range.

4\. The value of **sample** is null.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**:

1\. The track with the specified index is not selected.

2\. The demuxer is not correctly initialized.

**AV\_ERR\_NO\_MEMORY**: The sample capacity is insufficient to store all frame data.

**AV\_ERR\_UNKNOWN**: Failed to read or parse the frame from the file.

 |

#### \[h2\]OH\_AVDemuxer\_SeekToTime()

OH\_AVErrCode OH\_AVDemuxer\_SeekToTime(OH\_AVDemuxer \*demuxer, int64\_t millisecond, OH\_AVSeekMode mode)

**Description**

Seeks to the specified time for all the selected tracks based on a seek mode.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVDemuxer](../../structs/oh-avdemuxer/document.md) \*demuxer | Pointer to an OH\_AVDemuxer instance. |
| int64\_t millisecond | Time to seek to, in milliseconds. The timestamp is relative to the start position of the file. |
| [OH\_AVSeekMode](../native-avcodec-base-h/document.md#oh_avseekmode) mode | Seek mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**:

1\. The value of **demuxer** is nullptr or does not point to a demuxer instance.

2\. The value of **millisecond** is out of range.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**:

1\. The track with the specified index is not selected.

2\. The demuxer is not correctly initialized.

3\. The seek operation cannot be performed on the resource.

**AV\_ERR\_UNKNOWN**:

1\. The seek operation fails.

2\. **OH\_AVSeekMode** is set to **SEEK\_MODE\_NEXT\_SYNC** and there is no I-frame following the specified position.

 |

#### \[h2\]OH\_AVDemuxer\_SetMediaKeySystemInfoCallback()

OH\_AVErrCode OH\_AVDemuxer\_SetMediaKeySystemInfoCallback(OH\_AVDemuxer \*demuxer, DRM\_MediaKeySystemInfoCallback callback)

**Description**

Sets a callback for obtaining the media key system information.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 11

**Deprecated from**: 14

**Substitute**: [OH\_AVDemuxer\_SetDemuxerMediaKeySystemInfoCallback](#oh_avdemuxer_setdemuxermediakeysysteminfocallback)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVDemuxer](../../structs/oh-avdemuxer/document.md) \*demuxer | Pointer to an OH\_AVDemuxer instance. |
| [DRM\_MediaKeySystemInfoCallback](#drm_mediakeysysteminfocallback) callback | Callback function. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The demuxer is not correctly initialized.

**AV\_ERR\_INVALID\_VAL**: The value of **demuxer** is nullptr or does not point to a demuxer instance.

 |

#### \[h2\]OH\_AVDemuxer\_SetDemuxerMediaKeySystemInfoCallback()

OH\_AVErrCode OH\_AVDemuxer\_SetDemuxerMediaKeySystemInfoCallback(OH\_AVDemuxer \*demuxer, Demuxer\_MediaKeySystemInfoCallback callback)

**Description**

Sets a callback for obtaining the media key system information.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVDemuxer](../../structs/oh-avdemuxer/document.md) \*demuxer | Pointer to an OH\_AVDemuxer instance. |
| [Demuxer\_MediaKeySystemInfoCallback](#demuxer_mediakeysysteminfocallback) callback | Callback function. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The demuxer is not correctly initialized.

**AV\_ERR\_INVALID\_VAL**: The value of **demuxer** is nullptr or does not point to a demuxer instance.

 |

#### \[h2\]OH\_AVDemuxer\_GetMediaKeySystemInfo()

OH\_AVErrCode OH\_AVDemuxer\_GetMediaKeySystemInfo(OH\_AVDemuxer \*demuxer, DRM\_MediaKeySystemInfo \*mediaKeySystemInfo)

**Description**

Obtains the media key system information. The media key system information can be obtained only after [Demuxer\_MediaKeySystemInfoCallback](#demuxer_mediakeysysteminfocallback) or [DRM\_MediaKeySystemInfoCallback](#drm_mediakeysysteminfocallback) is successfully invoked.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVDemuxer](../../structs/oh-avdemuxer/document.md) \*demuxer | Pointer to an OH\_AVDemuxer instance. |
| [DRM\_MediaKeySystemInfo](../../structs/drm-mediakeysysteminfo/document.md) \*mediaKeySystemInfo | Pointer to the media key system information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The demuxer engine is not initialized or fails to be initialized.

**AV\_ERR\_INVALID\_VAL**:

1\. The value of **demuxer** is nullptr or does not point to a demuxer instance.

2\. The value of **mediaKeySystemInfo** is nullptr.

 |
