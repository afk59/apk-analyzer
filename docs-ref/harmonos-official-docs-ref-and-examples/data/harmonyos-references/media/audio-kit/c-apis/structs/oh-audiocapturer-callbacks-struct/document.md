# OH\_AudioCapturer\_Callbacks\_Struct

typedef struct OH\_AudioCapturer\_Callbacks\_Struct {...} OH\_AudioCapturer\_Callbacks

#### Overview

The struct defines a pointer to the callback functions related to an audio capturer.

To avoid unexpected behavior, ensure that every member variable of the struct is initialized by a custom callback method or a null pointer when setting the audio callback functions. For details, see [Using OHAudio for Audio Recording (C/C++)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/using-ohaudio-for-recording).

**Since**: 10

**Deprecated from**: 20

**Substitute**

Use the following callback types for substitute:

[OH\_AudioCapturer\_OnReadDataCallback](../../header-files/native-audiocapturer-h/document.md#oh_audiocapturer_onreaddatacallback), [OH\_AudioCapturer\_OnDeviceChangeCallback](../../header-files/native-audiocapturer-h/document.md#oh_audiocapturer_ondevicechangecallback), [OH\_AudioCapturer\_OnInterruptCallback](../../header-files/native-audiocapturer-h/document.md#oh_audiocapturer_oninterruptcallback), and [OH\_AudioCapturer\_OnErrorCallback](../../header-files/native-audiocapturer-h/document.md#oh_audiocapturer_onerrorcallback)

**Related module**: [OHAudio](../../modules/ohaudio/document.md)

**Header file**: [native\_audiostream\_base.h](../../header-files/native-audiostream-base-h/document.md)

#### Summary

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [int32\_t (\*OH\_AudioCapturer\_OnReadData)(OH\_AudioCapturer\* capturer,void\* userData,void\* buffer,int32\_t length)](#oh_audiocapturer_onreaddata) | Defines a function pointer to the callback function used to read audio data. |
| [int32\_t (\*OH\_AudioCapturer\_OnStreamEvent)(OH\_AudioCapturer\* capturer,void\* userData,OH\_AudioStream\_Event event)](#oh_audiocapturer_onstreamevent) | Defines a function pointer to the callback function used to process audio recording stream events. |
| [int32\_t (\*OH\_AudioCapturer\_OnInterruptEvent)(OH\_AudioCapturer\* capturer,void\* userData,OH\_AudioInterrupt\_ForceType type,OH\_AudioInterrupt\_Hint hint)](#oh_audiocapturer_oninterruptevent) | Defines a function pointer to the callback function used to process audio recording interruption events. |
| [int32\_t (\*OH\_AudioCapturer\_OnError)(OH\_AudioCapturer\* capturer, void\* userData, OH\_AudioStream\_Result error)](#oh_audiocapturer_onerror) | Defines a function pointer to the callback function used to process audio recording errors. |

#### Member Function Description

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/ZXrd0maISF2K-kecuRrxoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062420Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8EAC1FB527A90529D751D6F1308E8C80583CBDF2437DADD600A9D5400118AE78)

No enumerated values are defined as the return values of the following callbacks. In the current version, no processing specific to the return value is provided. To support expansion in later versions, the default value **0** is used.

#### \[h2\]OH\_AudioCapturer\_OnReadData()

int32\_t (\*OH\_AudioCapturer\_OnReadData)(OH\_AudioCapturer\* capturer,void\* userData,void\* buffer,int32\_t length)

**Description**

Defines a function pointer to the callback function used to read audio data.

The callback function is used only to read audio data. Do not call AudioCapturer APIs in it.

**Since**: 10

**Deprecated from**: 20

**Substitute**: [OH\_AudioCapturer\_OnReadDataCallback](../../header-files/native-audiocapturer-h/document.md#oh_audiocapturer_onreaddatacallback)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../../header-files/native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| void\* userData | Pointer to the data storage area customized by the application. |
| void\* buffer | Pointer to the captured data storage area, which is used by the application to read captured data. |
| int32\_t length | Length of the buffer. |

#### \[h2\]OH\_AudioCapturer\_OnStreamEvent()

int32\_t (\*OH\_AudioCapturer\_OnStreamEvent)(OH\_AudioCapturer\* capturer,void\* userData,OH\_AudioStream\_Event event)

**Description**

Defines a function pointer to the callback function used to process audio recording stream events.

**Since**: 10

**Deprecated from**: 20

**Substitute**: [OH\_AudioCapturer\_OnDeviceChangeCallback](../../header-files/native-audiocapturer-h/document.md#oh_audiocapturer_ondevicechangecallback)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../../header-files/native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| void\* userData | Pointer to the data storage area customized by the application. |
| [OH\_AudioStream\_Event](../../header-files/native-audiostream-base-h/document.md#oh_audiostream_event) event | Audio event. |

#### \[h2\]OH\_AudioCapturer\_OnInterruptEvent()

int32\_t (\*OH\_AudioCapturer\_OnInterruptEvent)(OH\_AudioCapturer\* capturer,void\* userData,OH\_AudioInterrupt\_ForceType type,OH\_AudioInterrupt\_Hint hint)

**Description**

Defines a function pointer to the callback function used to process audio recording interruption events.

**Since**: 10

**Deprecated from**: 20

**Substitute**: [OH\_AudioCapturer\_OnInterruptCallback](../../header-files/native-audiocapturer-h/document.md#oh_audiocapturer_oninterruptcallback)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../../header-files/native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| void\* userData | Pointer to the data storage area customized by the application. |
| [OH\_AudioInterrupt\_ForceType](../../header-files/native-audiostream-base-h/document.md#oh_audiointerrupt_forcetype) type | Type of force that causes audio interruption. |
| [OH\_AudioInterrupt\_Hint](../../header-files/native-audiostream-base-h/document.md#oh_audiointerrupt_hint) hint | Hint provided along with audio interruption. |

#### \[h2\]OH\_AudioCapturer\_OnError()

int32\_t (\*OH\_AudioCapturer\_OnError)(OH\_AudioCapturer\* capturer, void\* userData, OH\_AudioStream\_Result error)

**Description**

Defines a function pointer to the callback function used to process audio recording errors.

**Since**: 10

**Deprecated from**: 20

**Substitute**: [OH\_AudioCapturer\_OnErrorCallback](../../header-files/native-audiocapturer-h/document.md#oh_audiocapturer_onerrorcallback)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioCapturer](../oh-audiocapturerstruct/document.md)\* capturer | Pointer to an audio capturer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateCapturer](../../header-files/native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generatecapturer). |
| void\* userData | Pointer to the data storage area customized by the application. |
| [OH\_AudioStream\_Result](../../header-files/native-audiostream-base-h/document.md#oh_audiostream_result) error | Audio recording error result, which may be **AUDIOSTREAM\_ERROR\_INVALID\_PARAM**, **AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**, or **AUDIOSTREAM\_ERROR\_SYSTEM**. |
