# OH\_AVCodecBufferAttr

typedef struct OH\_AVCodecBufferAttr {...} OH\_AVCodecBufferAttr

#### Overview

The struct describes the description information about the buffer of an OH\_AVCodec instance.

**Since**: 9

**Related module**: [Core](../../modules/core/document.md)

**Header file**: [native\_avbuffer\_info.h](../../header-files/native-avbuffer-info-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int64\_t pts | Display timestamp of the buffer, in microseconds. |
| int32\_t size | Size of data contained in the buffer, in bytes. |
| int32\_t offset | Offset of valid data in the buffer. |
| uint32\_t flags | Flags of the buffer. For details, see [OH\_AVCodecBufferFlags](../../header-files/native-avbuffer-info-h/document.md#oh_avcodecbufferflags). |
