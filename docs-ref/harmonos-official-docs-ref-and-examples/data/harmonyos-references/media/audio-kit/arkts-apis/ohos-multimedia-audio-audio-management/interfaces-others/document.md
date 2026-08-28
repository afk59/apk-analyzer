# Interfaces (Others)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/-TIMbRelSQmiZP7qUPXtyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A9334DC8A862C164E7E75DAA4E666F6FD6E0FF7F821F7016ADFDEAB82304DBA)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### AudioStreamInfo8+

Describes audio stream information.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| samplingRate | [AudioSamplingRate](../enums/document.md#audiosamplingrate8) | No | No | Audio sampling rate. |
| channels | [AudioChannel](../enums/document.md#audiochannel8) | No | No | Number of audio channels. |
| sampleFormat | [AudioSampleFormat](../enums/document.md#audiosampleformat8) | No | No | Audio sample format. |
| encodingType | [AudioEncodingType](../enums/document.md#audioencodingtype8) | No | No | Audio encoding type. |
| channelLayout11+ | [AudioChannelLayout](../enums/document.md#audiochannellayout11) | No | Yes | Audio channel layout. The default value is **0x0**. |

#### AudioRendererInfo8+

Describes audio renderer information.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| content(deprecated) | [ContentType](../enums/document.md#contenttypedeprecated) | No | Yes | 
Audio content type.

**System capability**: SystemCapability.Multimedia.Audio.Core

This parameter is mandatory in API versions 8 and 9 and optional since API version 10. The default value is **CONTENT\_TYPE\_UNKNOWN**.

This parameter is supported since API version 8 and deprecated since API version 10. You are advised to use **usage** instead.

 |
| usage | [StreamUsage](../enums/document.md#streamusage) | No | No | 

Audio stream usage.

**System capability**: SystemCapability.Multimedia.Audio.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| rendererFlags | number | No | No | 

Flags that control the renderer behavior.

Set this parameter to **0**.

**System capability**: SystemCapability.Multimedia.Audio.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| volumeMode19+ | [AudioVolumeMode](../enums/document.md#audiovolumemode19) | No | Yes | 

Audio volume mode. The default value is **SYSTEM\_GLOBAL**.

**System capability**: SystemCapability.Multimedia.Audio.Volume

 |

#### AudioRendererOptions8+

Describes audio renderer configurations.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| streamInfo | [AudioStreamInfo](#audiostreaminfo8) | No | No | 
Audio stream information.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

 |
| rendererInfo | [AudioRendererInfo](#audiorendererinfo8) | No | No | 

Audio renderer information.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

 |
| privacyType10+ | [AudioPrivacyType](../enums/document.md#audioprivacytype10) | No | Yes | 

Whether the audio stream can be recorded by other applications. The default value is **0**.

**System capability**: SystemCapability.Multimedia.Audio.PlaybackCapture

 |

#### InterruptEvent9+

Describes the interruption event received by the application when the audio is interrupted.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| eventType | [InterruptType](../enums/document.md#interrupttype) | No | No | Whether the audio interruption has started or ended. |
| forceType | [InterruptForceType](../enums/document.md#interruptforcetype9) | No | No | Whether the audio interruption is forcibly taken by the system or taken by an application. |
| hintType | [InterruptHint](../enums/document.md#interrupthint) | No | No | Hint provided along the interruption to provide information related to the interruption event. |

#### DeviceBlockStatusInfo13+

Describes the audio device blocked status and device information.

**System capability**: SystemCapability.Multimedia.Audio.Device

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| blockStatus | [DeviceBlockStatus](../enums/document.md#deviceblockstatus13) | No | No | Blocked status of the audio device. |
| devices | [AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors) | No | No | Device information. |

#### AudioSessionStrategy12+

Describes an audio session strategy.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| concurrencyMode | [AudioConcurrencyMode](../enums/document.md#audioconcurrencymode12) | No | No | Audio concurrency mode. |

#### AudioSessionDeactivatedEvent12+

Describes the event indicating that an audio session is deactivated.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| reason | [AudioSessionDeactivatedReason](../enums/document.md#audiosessiondeactivatedreason12) | No | No | Reason for deactivating an audio session. |

#### AudioSessionStateChangedEvent20+

Describes the event indicating that the audio session state changes.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| stateChangeHint | [AudioSessionStateChangeHint](../enums/document.md#audiosessionstatechangehint20) | No | No | Hint for the audio session state change. |

#### AudioRendererChangeInfo9+

Describes the audio renderer change event.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| streamId | number | Yes | No | Unique ID of an audio stream. |
| rendererInfo | [AudioRendererInfo](#audiorendererinfo8) | Yes | No | Audio renderer information. |
| deviceDescriptors | [AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors) | Yes | No | Audio device description. |

#### AudioCapturerChangeInfo9+

Describes the audio capturer change event.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| streamId | number | Yes | No | Unique ID of an audio stream. |
| capturerInfo | [AudioCapturerInfo](#audiocapturerinfo8) | Yes | No | Audio capturer information. |
| deviceDescriptors | [AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors) | Yes | No | Audio device information. |
| muted11+ | boolean | Yes | Yes | Whether the audio capturer is muted. **true** if muted, **false** otherwise. |

#### AudioDeviceDescriptor

Describes an audio device.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceRole | [DeviceRole](../enums/document.md#devicerole) | Yes | No | 
Device role.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| deviceType | [DeviceType](../enums/document.md#devicetype) | Yes | No | 

Device type.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| id9+ | number | Yes | No | 

Unique device ID.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| name9+ | string | Yes | No | 

Device name.

For a Bluetooth device, you must request the ohos.permission.USE\_BLUETOOTH permission.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| address9+ | string | Yes | No | 

Static MAC address of the device.

For a Bluetooth device, you must request the ohos.permission.USE\_BLUETOOTH permission.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| sampleRates9+ | Array<number> | Yes | No | 

Supported sampling rates.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| channelCounts9+ | Array<number> | Yes | No | 

Number of channels supported.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| channelMasks9+ | Array<number> | Yes | No | 

Supported channel masks.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| displayName10+ | string | Yes | No | 

Display name of the device.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| encodingTypes11+ | Array<[AudioEncodingType](../enums/document.md#audioencodingtype8)\> | Yes | Yes | 

Supported encoding types.

**System capability**: SystemCapability.Multimedia.Audio.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| spatializationSupported18+ | boolean | Yes | Yes | 

Whether the device supports spatial audio rendering. **true** if supported, **false** otherwise.

**System capability**: SystemCapability.Multimedia.Audio.Spatialization

 |
| model22+ | string | Yes | Yes | 

Model of the device.

**System capability**: SystemCapability.Multimedia.Audio.Device

 |
| capabilities22+ | Array<[AudioStreamInfo](#audiostreaminfo8)\> | Yes | Yes | 

Audio stream capabilities supported by the device.

**System capability**: SystemCapability.Multimedia.Audio.Device

 |

#### VolumeEvent9+

Describes the event received by the application when the volume is changed.

**System capability**: SystemCapability.Multimedia.Audio.Volume

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](../enums/document.md#audiovolumetype) | No | No | Audio volume type. |
| volume | number | No | No | Volume to set. The value range can be obtained by calling **getMinVolume** and **getMaxVolume**. |
| updateUi | boolean | No | No | Whether to show the volume change in UI. **true** to show, **false** otherwise. |
| volumeMode19+ | [AudioVolumeMode](../enums/document.md#audiovolumemode19) | No | Yes | Audio volume mode. The default value is **SYSTEM\_GLOBAL**. |

#### MicStateChangeEvent9+

Describes the event received by the application when the microphone mute status is changed.

**System capability**: SystemCapability.Multimedia.Audio.Device

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| mute | boolean | No | No | Mute status of the microphone **true** if muted, **false** otherwise. |

#### StreamVolumeEvent20+

Describes the event received by the application when the audio stream volume is changed.

**System capability**: SystemCapability.Multimedia.Audio.Volume

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| streamUsage | [StreamUsage](../enums/document.md#streamusage) | No | No | Audio stream for which the volume changes. |
| volume | number | No | No | Volume. |
| updateUi | boolean | No | No | Whether to show the volume change in UI. **true** to show, **false** otherwise. |

#### DeviceChangeAction

Describes the device connection status and device information.

**System capability**: SystemCapability.Multimedia.Audio.Device

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [DeviceChangeType](../enums/document.md#devicechangetype) | No | No | Device connection status. |
| deviceDescriptors | [AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors) | No | No | Device information. |

#### AudioStreamDeviceChangeInfo11+

Describes the event received by the application when the audio stream device is changed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Audio.Device

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| devices | [AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors) | No | No | Device information. |
| changeReason | [AudioStreamDeviceChangeReason](../enums/document.md#audiostreamdevicechangereason11) | No | No | Reason for the device change. |

#### CurrentOutputDeviceChangedEvent20+

Describes the event indicating that the output device changes.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| devices | [AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors) | No | No | Device information. |
| changeReason | [AudioStreamDeviceChangeReason](../enums/document.md#audiostreamdevicechangereason11) | No | No | Reason for the device change. |
| recommendedAction | [OutputDeviceChangeRecommendedAction](../enums/document.md#outputdevicechangerecommendedaction20) | No | No | Recommended action after the device change. |

#### CurrentInputDeviceChangedEvent21+

Describes the event indicating that the input device changes.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| devices | [AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors) | No | No | Device information. |
| changeReason | [AudioStreamDeviceChangeReason](../enums/document.md#audiostreamdevicechangereason11) | No | No | Reason for the device change. |

#### AudioTimestampInfo19+

Describes the information about the audio stream timestamp and the current data frame position.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| framePos | number | Yes | No | Position of the current data frame for playback or recording. |
| timestamp | number | Yes | No | Timestamp corresponding to the current data frame position during playback or recording. |

#### AudioCapturerInfo8+

Describes audio capturer information.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| source | [SourceType](../enums/document.md#sourcetype8) | No | No | Audio source type. |
| capturerFlags | number | No | No | 
Flags that control the capturer behavior.

Set this parameter to **0**.

 |

#### AudioCapturerOptions8+

Describes audio capturer configurations.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| streamInfo | [AudioStreamInfo](#audiostreaminfo8) | No | No | 
Audio stream information.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

 |
| capturerInfo | [AudioCapturerInfo](#audiocapturerinfo8) | No | No | 

Audio capturer information.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

 |
| playbackCaptureConfig(deprecated) | [AudioPlaybackCaptureConfig](#audioplaybackcaptureconfigdeprecated) | No | Yes | 

Configuration for capturing played audio.

**System capability**: SystemCapability.Multimedia.Audio.PlaybackCapture

This API is supported since API version 10 and deprecated since API version 12. You are advised to use [AVScreenCapture](../../../../media-kit/c-apis/modules/avscreencapture/document.md) instead.

 |

#### AudioInterrupt(deprecated)

Describes input parameters of audio interruption events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/gRlgenEQRmGy2Ps6zWNY3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=370C40687270A44CEE5A2FC4FA3894080AECBDDD3907923256BC438BDDE6324D)

This API is supported since API version 7 and deprecated since API version 9. No substitute is provided.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| streamUsage | [StreamUsage](../enums/document.md#streamusage) | No | No | Audio stream usage. |
| contentType | [ContentType](../enums/document.md#contenttypedeprecated) | No | No | Audio content type. |
| pauseWhenDucked | boolean | No | No | Whether audio playback can be paused during an audio interruption. **true** if audio playback can be paused, **false** otherwise. |

#### CaptureFilterOptions(deprecated)

Defines the options for filtering the played audio streams to be recorded.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/CzOQEU3OQzOFxDFxjGX0qA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A7CF9A76988C3B7C94A3476670E26397536EADD1124103D7FFCC06B0762ACF9B)

This API is supported since API version 10 and deprecated since API version 12. You are advised to use [AVScreenCapture](../../../../media-kit/c-apis/modules/avscreencapture/document.md) instead.

**System capability**: SystemCapability.Multimedia.Audio.PlaybackCapture

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| usages | Array<[StreamUsage](../enums/document.md#streamusage)\> | No | No | 
**StreamUsage** of the audio stream to be recorded. You can specify zero or more stream usages. If the array is empty, the audio stream for which **StreamUsage** is **STREAM\_USAGE\_MUSIC**, **STREAM\_USAGE\_MOVIE**, **STREAM\_USAGE\_GAME**, or **STREAM\_USAGE\_AUDIOBOOK** is recorded by default.

In API version 10, **CaptureFilterOptions** supports **StreamUsage.STREAM\_USAGE\_VOICE\_COMMUNICATION**, and therefore the ohos.permission.CAPTURE\_VOICE\_DOWNLINK\_AUDIO permission is required. Only system applications can request this permission.

Since API version 11, **CaptureFilterOptions** does not support **StreamUsage.STREAM\_USAGE\_VOICE\_COMMUNICATION**. Therefore, no permission is required for calling this API.

 |

#### AudioPlaybackCaptureConfig(deprecated)

Defines the configuration for capturing played audio.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/yy03bKJBTHm04RzriFyJTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D09470CE010683D0F5D2A96DAFB16B1DD7A34F0541230D185D68BD0F4CB5E9F)

This API is supported since API version 10 and deprecated since API version 12. You are advised to use [AVScreenCapture](../../../../media-kit/c-apis/modules/avscreencapture/document.md) instead.

**System capability**: SystemCapability.Multimedia.Audio.PlaybackCapture

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| filterOptions | [CaptureFilterOptions](#capturefilteroptionsdeprecated) | No | No | Options for filtering the played audio streams to be recorded. |

#### InterruptAction(deprecated)

Describes the callback invoked for audio interruption or focus gain events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/t8-LOld1S6ORESvvPNdVdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD508B1CDB758097CB856D1A5B063725C62690E9FD4BE465CB9B6170BFE509A1)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [InterruptEvent](#interruptevent9) instead.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| actionType | [InterruptActionType](../enums/document.md#interruptactiontypedeprecated) | No | No | Returned event type. The value **TYPE\_ACTIVATED** means the focus gain event, and **TYPE\_INTERRUPT** means the audio interruption event. |
| type | [InterruptType](../enums/document.md#interrupttype) | No | Yes | Type of the audio interruption event. |
| hint | [InterruptHint](../enums/document.md#interrupthint) | No | Yes | Hint provided along with the audio interruption event. |
| activated | boolean | No | Yes | Whether the focus is gained or released. **true** if the focus is gained or released, **false** if the focus fails to be gained or released. |
