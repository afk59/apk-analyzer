# OH\_AudioRenderer\_Callbacks\_Struct

typedef struct OH\_AudioRenderer\_Callbacks\_Struct {...} OH\_AudioRenderer\_Callbacks

#### Overview

The struct defines a pointer to the callback functions related to an audio renderer.

To avoid unexpected behavior, ensure that every member variable of the struct is initialized by a custom callback method or a null pointer when setting the audio callback functions.

For details, see [(Recommended) Using OHAudio for Audio Playback (C/C++)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/using-ohaudio-for-playback).

**Since**: 10

**Deprecated from**: 20

**Substitute**

Use the following callback types for substitute:

[OH\_AudioRenderer\_OnWriteDataCallback](../../header-files/native-audiostream-base-h/document.md#oh_audiorenderer_onwritedatacallback), [OH\_AudioRenderer\_OutputDeviceChangeCallback](../../header-files/native-audiostream-base-h/document.md#oh_audiorenderer_outputdevicechangecallback), [OH\_AudioRenderer\_OnInterruptCallback](../../header-files/native-audiorenderer-h/document.md#oh_audiorenderer_oninterruptcallback), and [OH\_AudioRenderer\_OnErrorCallback](../../header-files/native-audiorenderer-h/document.md#oh_audiorenderer_onerrorcallback)

**Related module**: [OHAudio](../../modules/ohaudio/document.md)

**Header file**: [native\_audiostream\_base.h](../../header-files/native-audiostream-base-h/document.md)

#### Summary

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [int32\_t (\*OH\_AudioRenderer\_OnWriteData)(OH\_AudioRenderer\* renderer, void\* userData, void\* buffer, int32\_t length)](#oh_audiorenderer_onwritedata) | Defines a function pointer to the callback function used to write audio data. |
| [int32\_t (\*OH\_AudioRenderer\_OnStreamEvent)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioStream\_Event event)](#oh_audiorenderer_onstreamevent) | Defines a function pointer to the callback function used to process audio playback stream events. |
| [int32\_t (\*OH\_AudioRenderer\_OnInterruptEvent)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioInterrupt\_ForceType type, OH\_AudioInterrupt\_Hint hint)](#oh_audiorenderer_oninterruptevent) | Defines a function pointer to the callback function used to process audio playback interruption events. |
| [int32\_t (\*OH\_AudioRenderer\_OnError)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioStream\_Result error)](#oh_audiorenderer_onerror) | Defines a function pointer to the callback function used to process audio playback errors. |

#### Member Function Description

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/kxah1XX7TOyL8ShnZ-Vplw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062420Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BEC692E38B8DE9988E3640A521CBD2DBA287371824355DD2E4333AD6E644828)

No enumerated values are defined as the return values of the following callbacks. In the current version, no processing specific to the return value is provided. To support expansion in later versions, the default value **0** is used.

#### \[h2\]OH\_AudioRenderer\_OnWriteData()

int32\_t (\*OH\_AudioRenderer\_OnWriteData)(OH\_AudioRenderer\* renderer, void\* userData, void\* buffer, int32\_t length)

**Description**

Defines a function pointer to the callback function used to write audio data.

The callback function is used only to write audio data. Do not call AudioRenderer APIs in it.

Once the callback function finishes its execution, the audio service queues the data pointed to by **buffer** for playback. Therefore, do not change the data outside the callback. It is crucial to fill **buffer** with the exact length (specified by **length**) of data designated for playback; otherwise, noises may occur during playback.

**Since**: 10

**Deprecated from**: 20

**Substitute**: [OH\_AudioRenderer\_OnWriteDataCallback](../../header-files/native-audiostream-base-h/document.md#oh_audiorenderer_onwritedatacallback)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../../header-files/native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| void\* userData | Pointer to the data storage area customized by the application. |
| void\* buffer | Pointer to the playback data storage area, which is used by the application to fill in playback data. |
| int32\_t length | Length of the buffer. |

#### \[h2\]OH\_AudioRenderer\_OnStreamEvent()

int32\_t (\*OH\_AudioRenderer\_OnStreamEvent)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioStream\_Event event)

**Description**

Defines a function pointer to the callback function used to process audio playback stream events.

**OH\_AudioRenderer\_OnStreamEvent** is a reserved API and does not trigger callbacks. Starting from API version 11, if you need to listen for device changes, use [OH\_AudioRenderer\_OutputDeviceChangeCallback](../../header-files/native-audiostream-base-h/document.md#oh_audiorenderer_outputdevicechangecallback) instead.

**Since**: 10

**Deprecated from**: 20

**Substitute**: [OH\_AudioRenderer\_OutputDeviceChangeCallback](../../header-files/native-audiostream-base-h/document.md#oh_audiorenderer_outputdevicechangecallback)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../../header-files/native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| void\* userData | Pointer to the data storage area customized by the application. |
| [OH\_AudioStream\_Event](../../header-files/native-audiostream-base-h/document.md#oh_audiostream_event) event | Audio event. |

#### \[h2\]OH\_AudioRenderer\_OnInterruptEvent()

int32\_t (\*OH\_AudioRenderer\_OnInterruptEvent)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioInterrupt\_ForceType type, OH\_AudioInterrupt\_Hint hint)

**Description**

Defines a function pointer to the callback function used to process audio playback interruption events.

**Since**: 10

**Deprecated from**: 20

**Substitute**: [OH\_AudioRenderer\_OnInterruptCallback](../../header-files/native-audiorenderer-h/document.md#oh_audiorenderer_oninterruptcallback)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../../header-files/native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| void\* userData | Pointer to the data storage area customized by the application. |
| [OH\_AudioInterrupt\_ForceType](../../header-files/native-audiostream-base-h/document.md#oh_audiointerrupt_forcetype) type | Type of force that causes audio interruption. |
| [OH\_AudioInterrupt\_Hint](../../header-files/native-audiostream-base-h/document.md#oh_audiointerrupt_hint) hint | Hint provided along with audio interruption. |

#### \[h2\]OH\_AudioRenderer\_OnError()

int32\_t (\*OH\_AudioRenderer\_OnError)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioStream\_Result error)

**Description**

Defines a function pointer to the callback function used to process audio playback errors.

**Since**: 10

**Deprecated from**: 20

**Substitute**: [OH\_AudioRenderer\_OnErrorCallback](../../header-files/native-audiorenderer-h/document.md#oh_audiorenderer_onerrorcallback)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRenderer](../oh-audiorendererstruct/document.md)\* renderer | Pointer to an audio renderer instance, which is created by calling [OH\_AudioStreamBuilder\_GenerateRenderer](../../header-files/native-audiostreambuilder-h/document.md#oh_audiostreambuilder_generaterenderer). |
| void\* userData | Pointer to the data storage area customized by the application. |
| [OH\_AudioStream\_Result](../../header-files/native-audiostream-base-h/document.md#oh_audiostream_result) error | Audio playback error result, which may be **AUDIOSTREAM\_ERROR\_INVALID\_PARAM**, **AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE**, or **AUDIOSTREAM\_ERROR\_SYSTEM**. |
