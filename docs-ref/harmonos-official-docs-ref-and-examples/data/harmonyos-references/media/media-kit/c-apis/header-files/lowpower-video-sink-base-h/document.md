# lowpower\_video\_sink\_base.h

#### Overview

The file declares the structs and enums of the LowPowerVideoSink.

**File to include**: <multimedia/player\_framework/lowpower\_video\_sink\_base.h>

**Library**: liblowpower\_avsink.so

**System capability**: SystemCapability.Multimedia.Media.LowPowerAVSink

**Since**: 20

**Related module**: [LowPowerVideoSink](../../modules/lowpowervideosink/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md) | OH\_LowPowerVideoSink | Describes the declaration for the LowPowerVideoSink. |
| [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md) | OH\_LowPowerVideoSinkCallback | 
Contains a set of callback function pointers for the LowPowerVideoSink.

To ensure the normal running of the LowPowerVideoSink, you must register the instance of this struct with the [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md) instance and process the information reported by the callback functions.

 |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_LowPowerVideoSink\_OnDataNeeded)(OH\_LowPowerVideoSink\* sink, OH\_AVSamplesBuffer\* buffer, void \*userData)](#oh_lowpowervideosink_ondataneeded) | OH\_LowPowerVideoSink\_OnDataNeeded | Called when the LowPowerVideoSink needs more data. This callback is included in [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md). |
| [typedef void (\*OH\_LowPowerVideoSink\_OnError)(OH\_LowPowerVideoSink\* sink, OH\_AVErrCode errCode, const char\* errMsg, void\* userData)](#oh_lowpowervideosink_onerror) | OH\_LowPowerVideoSink\_OnError | Called when an error occurs in the LowPowerVideoSink. |
| [typedef void (\*OH\_LowPowerVideoSink\_OnTargetArrived)(OH\_LowPowerVideoSink\* sink, const int64\_t targetPts, const bool isTimeout, void\* userData)](#oh_lowpowervideosink_ontargetarrived) | OH\_LowPowerVideoSink\_OnTargetArrived | Called when the LowPowerVideoSink reaches the target point. This callback is included in [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md). |
| [typedef void (\*OH\_LowPowerVideoSink\_OnRenderStarted)(OH\_LowPowerVideoSink\* sink, void\* userData)](#oh_lowpowervideosink_onrenderstarted) | OH\_LowPowerVideoSink\_OnRenderStarted | Called when the LowPowerVideoSink starts rendering. This callback is included in [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md). |
| [typedef void (\*OH\_LowPowerVideoSink\_OnStreamChanged)(OH\_LowPowerVideoSink\* sink, OH\_AVFormat\* format, void\* userData)](#oh_lowpowervideosink_onstreamchanged) | OH\_LowPowerVideoSink\_OnStreamChanged | Called when the stream changes in the LowPowerVideoSink. This callback is included in [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md). |
| [typedef void (\*OH\_LowPowerVideoSink\_OnFirstFrameDecoded)(OH\_LowPowerVideoSink\* sink, void\* userData)](#oh_lowpowervideosink_onfirstframedecoded) | OH\_LowPowerVideoSink\_OnFirstFrameDecoded | Called when the first frame is successfully decoded in the LowPowerVideoSink. This callback is included in [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md). |
| [typedef void (\*OH\_LowPowerVideoSink\_OnEos)(OH\_LowPowerVideoSink\* sink, void\* userData)](#oh_lowpowervideosink_oneos) | OH\_LowPowerVideoSink\_OnEos | Called when the playback is completed in the LowPowerVideoSink. This callback is included in [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md). |

#### Function Description

#### \[h2\]OH\_LowPowerVideoSink\_OnDataNeeded()

typedef void (\*OH\_LowPowerVideoSink\_OnDataNeeded)(OH\_LowPowerVideoSink\* sink,OH\_AVSamplesBuffer\* buffer,void \*userData)

**Description**

Called when the LowPowerVideoSink needs more data. This callback is included in [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |
| [OH\_AVSamplesBuffer](../../structs/oh-avsamplesbuffer/document.md)\* buffer | Pointer to an OH\_AVSamplesBuffer instance. |
| void \*userData | Pointer to the data on which the caller depends when executing the callback. |

#### \[h2\]OH\_LowPowerVideoSink\_OnError()

typedef void (\*OH\_LowPowerVideoSink\_OnError)(OH\_LowPowerVideoSink\* sink,OH\_AVErrCode errCode,const char\* errMsg,void\* userData)

**Description**

Called when an error occurs in the LowPowerVideoSink.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) errCode | Error code returned when an error occurs during service operations. |
| const char\* errMsg | Pointer to the error message returned when an error occurs during service operations. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

#### \[h2\]OH\_LowPowerVideoSink\_OnTargetArrived()

typedef void (\*OH\_LowPowerVideoSink\_OnTargetArrived)(OH\_LowPowerVideoSink\* sink,const int64\_t targetPts,const bool isTimeout,void\* userData)

**Description**

Called when the LowPowerVideoSink reaches the target point. This callback is included in [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |
| const int64\_t targetPts | Presentation timestamp (PTS) of the target point. |
| const bool isTimeout | Whether the wait for the target point has timed out. **true** if timed out, **false** otherwise. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

#### \[h2\]OH\_LowPowerVideoSink\_OnRenderStarted()

typedef void (\*OH\_LowPowerVideoSink\_OnRenderStarted)(OH\_LowPowerVideoSink\* sink, void\* userData)

**Description**

Called when the LowPowerVideoSink starts rendering. This callback is included in [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

#### \[h2\]OH\_LowPowerVideoSink\_OnStreamChanged()

typedef void (\*OH\_LowPowerVideoSink\_OnStreamChanged)(OH\_LowPowerVideoSink\* sink, OH\_AVFormat\* format, void\* userData)

**Description**

Called when the stream changes in the LowPowerVideoSink. This callback is included in [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |
| [OH\_AVFormat](../../../../avcodec-kit/c-apis/structs/oh-avformat/document.md)\* format | Pointer to the changed parameters and their values. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

#### \[h2\]OH\_LowPowerVideoSink\_OnFirstFrameDecoded()

typedef void (\*OH\_LowPowerVideoSink\_OnFirstFrameDecoded)(OH\_LowPowerVideoSink\* sink, void\* userData)

**Description**

Called when the first frame is successfully decoded in the LowPowerVideoSink. This callback is included in [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |

#### \[h2\]OH\_LowPowerVideoSink\_OnEos()

typedef void (\*OH\_LowPowerVideoSink\_OnEos)(OH\_LowPowerVideoSink\* sink, void\* userData)

**Description**

Called when the playback is completed in the LowPowerVideoSink. This callback is included in [OH\_LowPowerVideoSinkCallback](../../structs/oh-lowpowervideosinkcallback/document.md).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerVideoSink](../../structs/oh-lowpowervideosink/document.md)\* sink | Pointer to an OH\_LowPowerVideoSink instance. |
| void\* userData | Pointer to the data on which the caller depends when executing the callback. |
