# OH\_AVCodecCallback

typedef struct OH\_AVCodecCallback {...} OH\_AVCodecCallback

#### Overview

The struct defines all the asynchronous callback function pointers of an OH\_AVCodec instance. To ensure the normal running of OH\_AVCodec, you must register the instance of this struct with the OH\_AVCodec instance and process the information reported by the callback function.

For details about the development guide, see step 4 in surface mode or step 3 in buffer mode in [Video Encoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-encoding).

**Since**: 11

**Related module**: [CodecBase](../../modules/codecbase/document.md)

**Header file**: [native\_avcodec\_base.h](../../header-files/native-avcodec-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [OH\_AVCodecOnError](../../header-files/native-avcodec-base-h/document.md#oh_avcodeconerror) onError | Callback used to report a codec operation error. |
| [OH\_AVCodecOnStreamChanged](../../header-files/native-avcodec-base-h/document.md#oh_avcodeconstreamchanged) onStreamChanged | Callback used to report a codec stream change. |
| [OH\_AVCodecOnNeedInputBuffer](../../header-files/native-avcodec-base-h/document.md#oh_avcodeconneedinputbuffer) onNeedInputBuffer | Callback used to report input data required. |
| [OH\_AVCodecOnNewOutputBuffer](../../header-files/native-avcodec-base-h/document.md#oh_avcodeconnewoutputbuffer) onNewOutputBuffer | Callback used to report output data generated. |
