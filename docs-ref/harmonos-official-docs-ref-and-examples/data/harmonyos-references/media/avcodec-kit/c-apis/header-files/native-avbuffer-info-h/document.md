# native\_avbuffer\_info.h

#### Overview

The file declares the attribute definition of the media struct AVBuffer.

**File to include**: <multimedia/player\_framework/native\_avbuffer\_info.h>

**Library**: libnative\_media\_core.so

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Related module**: [Core](../../modules/core/document.md)

**Sample**: [AVCodec](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVCodecBufferAttr](../../structs/oh-avcodecbufferattr/document.md) | OH\_AVCodecBufferAttr | Describes the description information about the buffer of an OH\_AVCodec instance. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVCodecBufferFlags](#oh_avcodecbufferflags) | OH\_AVCodecBufferFlags | Enumerates the flags for the buffer of an OH\_AVCodec instance. |

#### Enum Description

#### \[h2\]OH\_AVCodecBufferFlags

enum OH\_AVCodecBufferFlags

**Description**

Enumerates the flags for the buffer of an OH\_AVCodec instance.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

| Value | Description |
| :-- | :-- |
| AVCODEC\_BUFFER\_FLAGS\_NONE = 0 | Common frame. |
| AVCODEC\_BUFFER\_FLAGS\_EOS = 1 << 0 | The buffer is an end-of-stream frame. |
| AVCODEC\_BUFFER\_FLAGS\_SYNC\_FRAME = 1 << 1 | The buffer contains key frames. |
| AVCODEC\_BUFFER\_FLAGS\_INCOMPLETE\_FRAME = 1 << 2 | The data in the buffer is only part of the frame. |
| AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA = 1 << 3 | The buffer contains codec-specific data. |
| AVCODEC\_BUFFER\_FLAGS\_DISCARD = 1 << 4 | 
The decoding process depends on the buffer, and the decoded data can be discarded.

**Since**: 12

 |
| AVCODEC\_BUFFER\_FLAGS\_DISPOSABLE = 1 << 5 | 

The buffer can be disposed directly.

**Since**: 12

 |
