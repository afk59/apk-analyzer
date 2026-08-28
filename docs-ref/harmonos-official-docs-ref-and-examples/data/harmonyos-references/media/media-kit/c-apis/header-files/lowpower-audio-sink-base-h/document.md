# lowpower\_audio\_sink\_base.h

#### Overview

The file declares the structs and enums of the LowPowerAudioSink.

**File to include**: <multimedia/player\_framework/lowpower\_audio\_sink\_base.h>

**Library**: liblowpower\_avsink.so

**System capability**: SystemCapability.Multimedia.Media.LowPowerAVSink

**Since**: 20

**Related module**: [LowPowerAudioSink](../../modules/lowpoweraudiosink/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md) | OH\_LowPowerAudioSink | Describes the declaration for the LowPowerAudioSink. |
| [OH\_LowPowerAudioSinkCallback](../../structs/oh-lowpoweraudiosinkcallback/document.md) | OH\_LowPowerAudioSinkCallback | 
Contains a set of callback function pointers for the LowPowerAudioSink.

To ensure the normal running of the LowPowerAudioSink, you must register the instance of this struct with the [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md) instance and process the information reported by the callback functions.

 |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_LowPowerAudioSink\_OnError)(OH\_LowPowerAudioSink\* sink, OH\_AVErrCode errCode, const char\* errorMsg, void\* userData)](#oh_lowpoweraudiosink_onerror) | OH\_LowPowerAudioSink\_OnError | Called when an error occurs in the LowPowerAudioSink. |
| [typedef void (\*OH\_LowPowerAudioSink\_OnPositionUpdated)(OH\_LowPowerAudioSink\* sink, int64\_t currentPosition, void\* userData)](#oh_lowpoweraudiosink_onpositionupdated) | OH\_LowPowerAudioSink\_OnPositionUpdated | Called when the playback position is updated in the LowPowerAudioSink. |
| [typedef void (\*OH\_LowPowerAudioSink\_OnDataNeeded)(OH\_LowPowerAudioSink\* sink, OH\_AVSamplesBuffer\* samples, void\* userData)](#oh_lowpoweraudiosink_ondataneeded) | OH\_LowPowerAudioSink\_OnDataNeeded | Called when the LowPowerAudioSink needs more data. |
| [typedef void (\*OH\_LowPowerAudioSink\_OnInterrupted)(OH\_LowPowerAudioSink\* sink, OH\_AudioInterrupt\_ForceType type, OH\_AudioInterrupt\_Hint hint, void\* userData)](#oh_lowpoweraudiosink_oninterrupted) | OH\_LowPowerAudioSink\_OnInterrupted | Called when the audio focus is interrupted in the LowPowerAudioSink. |
| [typedef void (\*OH\_LowPowerAudioSink\_OnDeviceChanged)(OH\_LowPowerAudioSink\* sink, OH\_AudioStream\_DeviceChangeReason reason, void\* userData)](#oh_lowpoweraudiosink_ondevicechanged) | OH\_LowPowerAudioSink\_OnDeviceChanged | Called when the audio device changes in the LowPowerAudioSink. |
| [typedef void (\*OH\_LowPowerAudioSink\_OnEos)(OH\_LowPowerAudioSink\* sink, void\* userData)](#oh_lowpoweraudiosink_oneos) | OH\_LowPowerAudioSink\_OnEos | Called when the playback is complete in the LowPowerAudioSink. This callback is included in [OH\_LowPowerAudioSinkCallback](../../structs/oh-lowpoweraudiosinkcallback/document.md). |

#### Function Description

#### \[h2\]OH\_LowPowerAudioSink\_OnError()

typedef void (\*OH\_LowPowerAudioSink\_OnError)(OH\_LowPowerAudioSink\* sink,OH\_AVErrCode errCode,const char\* errorMsg,void\* userData)

**Description**

Called when an error occurs in the LowPowerAudioSink.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) errCode | Error code reported when an error occurs. |
| const char\* errorMsg | Pointer to an error message. |
| void\* userData | Pointer to user-defined data. |

#### \[h2\]OH\_LowPowerAudioSink\_OnPositionUpdated()

typedef void (\*OH\_LowPowerAudioSink\_OnPositionUpdated)(OH\_LowPowerAudioSink\* sink,int64\_t currentPosition,void\* userData)

**Description**

Called when the playback position is updated in the LowPowerAudioSink.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |
| int64\_t currentPosition | Current playback position. |
| void\* userData | Pointer to user-defined data. |

#### \[h2\]OH\_LowPowerAudioSink\_OnDataNeeded()

typedef void (\*OH\_LowPowerAudioSink\_OnDataNeeded)(OH\_LowPowerAudioSink\* sink,OH\_AVSamplesBuffer\* samples,void\* userData)

**Description**

Called when the LowPowerAudioSink needs more data.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |
| [OH\_AVSamplesBuffer](../../structs/oh-avsamplesbuffer/document.md)\* samples | Pointer to the AVSamplesBuffer instance to be written. |
| void\* userData | Pointer to user-defined data. |

#### \[h2\]OH\_LowPowerAudioSink\_OnInterrupted()

typedef void (\*OH\_LowPowerAudioSink\_OnInterrupted)(OH\_LowPowerAudioSink\* sink,OH\_AudioInterrupt\_ForceType type,OH\_AudioInterrupt\_Hint hint,void\* userData)

**Description**

Called when the audio focus is interrupted in the LowPowerAudioSink.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |
| [OH\_AudioInterrupt\_ForceType](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiointerrupt_forcetype) type | Type of force that causes the audio interruption. |
| [OH\_AudioInterrupt\_Hint](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiointerrupt_hint) hint | Hint provided along with audio interruption. |
| void\* userData | Pointer to user-defined data. |

#### \[h2\]OH\_LowPowerAudioSink\_OnDeviceChanged()

typedef void (\*OH\_LowPowerAudioSink\_OnDeviceChanged)(OH\_LowPowerAudioSink\* sink,OH\_AudioStream\_DeviceChangeReason reason,void\* userData)

**Description**

Called when the audio device changes in the LowPowerAudioSink.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |
| [OH\_AudioStream\_DeviceChangeReason](../../../../audio-kit/c-apis/header-files/native-audiostream-base-h/document.md#oh_audiostream_devicechangereason) reason | Reason for the output device changes. |
| void\* userData | Pointer to user-defined data. |

#### \[h2\]OH\_LowPowerAudioSink\_OnEos()

typedef void (\*OH\_LowPowerAudioSink\_OnEos)(OH\_LowPowerAudioSink\* sink, void\* userData)

**Description**

Called when the playback is complete in the LowPowerAudioSink. This callback is included in [OH\_LowPowerAudioSinkCallback](../../structs/oh-lowpoweraudiosinkcallback/document.md).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_LowPowerAudioSink](../../structs/oh-lowpoweraudiosink/document.md)\* sink | Pointer to an OH\_LowPowerAudioSink instance. |
| void\* userData | Pointer to user-defined data. |
