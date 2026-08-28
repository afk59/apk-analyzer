# lowpower\_avsink\_base.h

#### Overview

The file declares the basic dependencies for OH\_LowPowerAudioSink and OH\_LowPowerVideoSink.

**File to include**: <multimedia/player\_framework/lowpower\_avsink\_base.h>

**Library**: liblowpower\_avsink.so

**System capability**: SystemCapability.Multimedia.Media.LowPowerAVSink

**Since**: 20

**Related module**: [AVSinkBase](../../modules/avsinkbase/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVSamplesBuffer](../../structs/oh-avsamplesbuffer/document.md) | OH\_AVSamplesBuffer | Describes the input data of the LowPowerAVSink. After receiving the DataNeeded callback, the application must pack data into an OH\_AVSamplesBuffer instance and pass it to the corresponding lowpower\_avsink. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_AVErrCode OH\_AVSamplesBuffer\_AppendOneBuffer(OH\_AVSamplesBuffer \*samplesBuffer, OH\_AVBuffer \*avBuffer)](#oh_avsamplesbuffer_appendonebuffer) | Appends data from an OH\_AVBuffer instance to an OH\_AVSamplesBuffer instance. |
| [int32\_t OH\_AVSamplesBuffer\_GetRemainedCapacity(OH\_AVSamplesBuffer \*samplesBuffer)](#oh_avsamplesbuffer_getremainedcapacity) | Obtains the remaining capacity available in an OH\_AVSamplesBuffer instance. |
| [OH\_LowPowerAVSink\_Capability \*OH\_LowPowerAVSink\_GetCapability()](#oh_lowpoweravsink_getcapability) | 
Obtains the capability of the low-power player. It mainly helps you find out what the low-power player can do, including the media formats and features it supports.

When you call this function, you can learn about the device's capabilities in audio and video processing. For example, you can find out which encoding and decoding formats are supported, as well as the range of bit rates that the device can handle.

 |

#### Function Description

#### \[h2\]OH\_AVSamplesBuffer\_AppendOneBuffer()

OH\_AVErrCode OH\_AVSamplesBuffer\_AppendOneBuffer(OH\_AVSamplesBuffer \*samplesBuffer, OH\_AVBuffer \*avBuffer)

**Description**

Appends data from an OH\_AVBuffer instance to an OH\_AVSamplesBuffer instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSamplesBuffer](../../structs/oh-avsamplesbuffer/document.md) \*samplesBuffer | Pointer to an OH\_AVSamplesBuffer instance. |
| [OH\_AVBuffer](../../../../avcodec-kit/c-apis/structs/oh-avbuffer/document.md) \*avBuffer | Pointer to an OH\_AVBuffer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: An input parameter is nullptr or invalid.

**AV\_ERR\_NO\_MEMORY**: The framePacketBuffer does not have sufficient remaining capacity to append an OH\_AVBuffer.

**AV\_ERR\_UNKNOWN**: An unknown error occurs.

 |

#### \[h2\]OH\_AVSamplesBuffer\_GetRemainedCapacity()

int32\_t OH\_AVSamplesBuffer\_GetRemainedCapacity(OH\_AVSamplesBuffer \*samplesBuffer)

**Description**

Obtains the remaining capacity available in an OH\_AVSamplesBuffer instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSamplesBuffer](../../structs/oh-avsamplesbuffer/document.md) \*samplesBuffer | Pointer to an OH\_AVSamplesBuffer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Remaining capacity available in the OH\_AVSamplesBuffer instance, in bytes. If **sampleBuffer** or data pointer is nullptr or invalid, **3** is returned. |

#### \[h2\]OH\_LowPowerAVSink\_GetCapability()

OH\_LowPowerAVSink\_Capability \*OH\_LowPowerAVSink\_GetCapability()

**Description**

Obtains the capability of the low-power player. It mainly helps you find out what the low-power player can do, including the media formats and features it supports.

When you call this function, you can learn about the device's capabilities in audio and video processing. For example, you can find out which encoding and decoding formats are supported, as well as the range of bit rates that the device can handle.

**Since**: 21

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_LowPowerAVSink\_Capability \* | 
**OH\_LowPowerAVSink\_Capability**: The low-power player is supported.

**nullptr**: The low-power player is not supported or the capability fails to be obtained.

 |
