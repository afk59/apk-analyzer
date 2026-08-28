# Types

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/eo78dkk3SZigkgRYlV3j4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF79209F16354E7BD8482D7F502F4583A3598271C20484DADF080C91FE8593DA)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### AudioRendererChangeInfoArray9+

type AudioRendererChangeInfoArray = Array<Readonly<AudioRendererChangeInfo>>

Defines an AudioRendererChangeInfo array, which is read-only.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

| Type | Description |
| :-- | :-- |
| Array<Readonly<AudioRendererChangeInfo>> | An [AudioRendererChangeInfo](../interfaces-others/document.md#audiorendererchangeinfo9) array, which is read-only. |

#### AudioCapturerChangeInfoArray9+

type AudioCapturerChangeInfoArray = Array<Readonly<AudioCapturerChangeInfo>>

Defines an AudioCapturerChangeInfo array, which is read-only.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

| Type | Description |
| :-- | :-- |
| Array<Readonly<AudioCapturerChangeInfo>> | An [AudioCapturerChangeInfo](../interfaces-others/document.md#audiocapturerchangeinfo9) array, which is read-only. |

#### AudioEffectInfoArray10+

type AudioEffectInfoArray = Array<Readonly<AudioEffectMode>>

Defines an array that contains the audio effect mode corresponding to a specific audio content type (specified by **ContentType**) and audio stream usage (specified by **StreamUsage**). The [AudioEffectMode](../enums/document.md#audioeffectmode10) array is read-only.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

| Type | Description |
| :-- | :-- |
| Array<Readonly<AudioEffectMode>> | Defines an array that contains the audio effect mode corresponding to a specific audio content type (specified by **ContentType**) and audio stream usage (specified by **StreamUsage**). The [AudioEffectMode](../enums/document.md#audioeffectmode10) array is read-only. |

#### AudioDeviceDescriptors

type AudioDeviceDescriptors = Array<Readonly<AudioDeviceDescriptor>>

Defines an [AudioDeviceDescriptor](../interfaces-others/document.md#audiodevicedescriptor) array, which is read-only.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Audio.Device

| Type | Description |
| :-- | :-- |
| Array<Readonly<AudioDeviceDescriptor>> | Defines an [AudioDeviceDescriptor](../interfaces-others/document.md#audiodevicedescriptor) array, which is read-only. |

#### AudioRendererWriteDataCallback12+

type AudioRendererWriteDataCallback = (data: ArrayBuffer) => AudioDataCallbackResult | void

Defines the callback function used to write data to the audio renderer. Once the callback function finishes its execution, the audio service queues the data pointed to by **data** for playback. Therefore, do not change the data outside the callback. It is crucial to fill **data** with the exact length of data designated for playback; otherwise, noises may occur during playback.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | ArrayBuffer | Yes | Data to be written to the buffer. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioDataCallbackResult](../enums/document.md#audiodatacallbackresult12) | void | If **void** or **AudioDataCallbackResult.VALID** is returned, the data is valid and the audio data is played. If **AudioDataCallbackResult.INVALID** is returned, the data is invalid and the audio data is not played. |
