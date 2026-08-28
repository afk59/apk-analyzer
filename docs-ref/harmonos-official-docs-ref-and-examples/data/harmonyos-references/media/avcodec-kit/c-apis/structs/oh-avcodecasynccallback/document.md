# OH\_AVCodecAsyncCallback

typedef struct OH\_AVCodecAsyncCallback {...} OH\_AVCodecAsyncCallback

#### Overview

The struct defines all the asynchronous callback function pointers of an OH\_AVCodec instance. To ensure the normal running of OH\_AVCodec, you must register the instance of this struct with the OH\_AVCodec instance and process the information reported by the callback function.

**Since**: 9

**Deprecated from**: 11

**Substitute**: [OH\_AVCodecCallback](../oh-avcodeccallback/document.md)

**Related module**: [CodecBase](../../modules/codecbase/document.md)

**Header file**: [native\_avcodec\_base.h](../../header-files/native-avcodec-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [OH\_AVCodecOnError](../../header-files/native-avcodec-base-h/document.md#oh_avcodeconerror) onError | Callback used to report a codec operation error. |
| [OH\_AVCodecOnStreamChanged](../../header-files/native-avcodec-base-h/document.md#oh_avcodeconstreamchanged) onStreamChanged | Callback used to report a codec stream change. |
| [OH\_AVCodecOnNeedInputData](../../header-files/native-avcodec-base-h/document.md#oh_avcodeconneedinputdata) onNeedInputData | Callback used to report input data required. |
| [OH\_AVCodecOnNewOutputData](../../header-files/native-avcodec-base-h/document.md#oh_avcodeconnewoutputdata) onNeedOutputData | Callback used to report output data generated. |
