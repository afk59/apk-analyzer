# Enums

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/WGeS3Qk9SKCHg5e51Xk-yg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91E6325FFF6C4628793AB352DD5D1A29F2D12CF37DE903C8414E1E422EAAF9A9)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### AudioVolumeType

Enumerates the audio volume types.

**System capability**: SystemCapability.Multimedia.Audio.Volume

| Name | Value | Description |
| :-- | :-- | :-- |
| VOICE\_CALL8+ | 0 | Audio stream for voice calls. |
| RINGTONE | 2 | Audio stream for ringtones. |
| MEDIA | 3 | Audio stream for media purpose. |
| ALARM10+ | 4 | Audio stream for alarming. |
| ACCESSIBILITY10+ | 5 | Audio stream for accessibility. |
| VOICE\_ASSISTANT8+ | 9 | Audio stream for voice assistant. |

#### InterruptMode9+

Enumerates the audio interruption modes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Audio.Interrupt

| Name | Value | Description |
| :-- | :-- | :-- |
| SHARE\_MODE | 0 | Shared mode. |
| INDEPENDENT\_MODE | 1 | Independent mode. |

#### DeviceFlag

Enumerates the audio device flags.

**System capability**: SystemCapability.Multimedia.Audio.Device

| Name | Value | Description |
| :-- | :-- | :-- |
| OUTPUT\_DEVICES\_FLAG | 1 | Output device. |
| INPUT\_DEVICES\_FLAG | 2 | Input device. |
| ALL\_DEVICES\_FLAG | 3 | All devices. |

#### DeviceUsage12+

Enumerates the audio device types by usage.

**System capability**: SystemCapability.Multimedia.Audio.Device

| Name | Value | Description |
| :-- | :-- | :-- |
| MEDIA\_OUTPUT\_DEVICES | 1 | Media output device. |
| MEDIA\_INPUT\_DEVICES | 2 | Media input device. |
| ALL\_MEDIA\_DEVICES | 3 | All media devices. |
| CALL\_OUTPUT\_DEVICES | 4 | Call output device. |
| CALL\_INPUT\_DEVICES | 8 | Call input device. |
| ALL\_CALL\_DEVICES | 12 | All call devices. |

#### DeviceRole

Enumerates the device roles.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Audio.Device

| Name | Value | Description |
| :-- | :-- | :-- |
| INPUT\_DEVICE | 1 | Input role. |
| OUTPUT\_DEVICE | 2 | Output role. |

#### DeviceType

Enumerates the device types.

**System capability**: SystemCapability.Multimedia.Audio.Device

| Name | Value | Description |
| :-- | :-- | :-- |
| INVALID | 0 | 
Invalid device.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| EARPIECE | 1 | 

Earpiece.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SPEAKER | 2 | 

Speaker.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| WIRED\_HEADSET | 3 | 

Wired headset with a microphone.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| WIRED\_HEADPHONES | 4 | 

Wired headset without a microphone.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BLUETOOTH\_SCO | 7 | 

Bluetooth device using Synchronous Connection Oriented (SCO) links.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BLUETOOTH\_A2DP | 8 | 

Bluetooth device using Advanced Audio Distribution Profile (A2DP) links.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| MIC | 15 | 

Microphone.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| USB\_HEADSET | 22 | 

USB Type-C headset.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| DISPLAY\_PORT12+ | 23 | 

Display port (DP), which is used to connect to external devices.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| REMOTE\_CAST12+ | 24 | 

Remote cast device.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| USB\_DEVICE18+ | 25 | USB device (excluding USB headsets). |
| HDMI19+ | 27 | HDMI device (such as HDMI, ARC, and eARC). |
| LINE\_DIGITAL19+ | 28 | Wired digital device (such as S/PDIF) |
| REMOTE\_DAUDIO18+ | 29 | 

Distributed device.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| HEARING\_AID20+ | 30 | Hearing aid device. |
| NEARLINK20+ | 31 | NearLink device. |
| SYSTEM\_PRIVATE22+ | 200 | System private device. (This device is a private device within the system, and applications can ignore it.) |
| DEFAULT9+ | 1000 | 

Default device type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### BluetoothAndNearlinkPreferredRecordCategory21+

Enumerates the preferred device categories available for recording with Bluetooth or NearLink.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| PREFERRED\_NONE | 0 | No specific device preference. |
| PREFERRED\_DEFAULT | 1 | Prefers using Bluetooth or NearLink devices for recording; whether to use low-latency or high-quality recording depends on the system. |
| PREFERRED\_LOW\_LATENCY | 2 | Prefers using Bluetooth or NearLink devices in low-latency mode for recording. |
| PREFERRED\_HIGH\_QUALITY | 3 | Prefers using Bluetooth or NearLink devices in high-quality mode for recording. |

#### CommunicationDeviceType9+

Enumerates the device types used for communication.

**System capability**: SystemCapability.Multimedia.Audio.Communication

| Name | Value | Description |
| :-- | :-- | :-- |
| SPEAKER | 2 | Speaker. |

#### AudioRingMode

Enumerates the audio ring modes.

**System capability**: SystemCapability.Multimedia.Audio.Communication

| Name | Value | Description |
| :-- | :-- | :-- |
| RINGER\_MODE\_SILENT | 0 | Silent mode. |
| RINGER\_MODE\_VIBRATE | 1 | Vibration mode. |
| RINGER\_MODE\_NORMAL | 2 | Normal mode. |

#### AudioSampleFormat8+

Enumerates the audio sample formats.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SAMPLE\_FORMAT\_INVALID | \-1 | Invalid format. |
| SAMPLE\_FORMAT\_U8 | 0 | Unsigned 8-bit integer. |
| SAMPLE\_FORMAT\_S16LE | 1 | Signed 16-bit integer, little endian. |
| SAMPLE\_FORMAT\_S24LE | 2 | 
Signed 24-bit integer, little endian.

Due to system restrictions, only some devices support this sampling format.

 |
| SAMPLE\_FORMAT\_S32LE | 3 | 

Signed 32-bit integer, little endian.

Due to system restrictions, only some devices support this sampling format.

 |
| SAMPLE\_FORMAT\_F32LE9+ | 4 | 

Signed 32-bit floating-point number, little endian.

Due to system restrictions, only some devices support this sampling format.

 |

#### AudioErrors9+

Enumerates the error codes available for audio management.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ERROR\_INVALID\_PARAM | 6800101 | Invalid parameter. |
| ERROR\_NO\_MEMORY | 6800102 | Memory allocation failure. |
| ERROR\_ILLEGAL\_STATE | 6800103 | Unsupported state. |
| ERROR\_UNSUPPORTED | 6800104 | Unsupported parameter value. |
| ERROR\_TIMEOUT | 6800105 | Processing timeout. |
| ERROR\_STREAM\_LIMIT | 6800201 | Too many audio streams. |
| ERROR\_SYSTEM | 6800301 | System error. |

#### AudioChannel8+

Enumerates the audio channels.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CHANNEL\_1 | 1 | One audio channel (mono). |
| CHANNEL\_2 | 2 | Two audio channels (stereo). |
| CHANNEL\_311+ | 3 | Three audio channels. |
| CHANNEL\_411+ | 4 | Four audio channels. |
| CHANNEL\_511+ | 5 | Five audio channels. |
| CHANNEL\_611+ | 6 | Six audio channels. |
| CHANNEL\_711+ | 7 | Seven audio channels. |
| CHANNEL\_811+ | 8 | Eight audio channels. |
| CHANNEL\_911+ | 9 | Nine audio channels. |
| CHANNEL\_1011+ | 10 | Ten audio channels. |
| CHANNEL\_1211+ | 12 | Twelve audio channels. |
| CHANNEL\_1411+ | 14 | Fourteen audio channels. |
| CHANNEL\_1611+ | 16 | Sixteen audio channels. |

#### AudioSamplingRate8+

Enumerates the audio sampling rates. The sampling rates supported vary according to the device in use.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SAMPLE\_RATE\_8000 | 8000 | The sampling rate is 8000. |
| SAMPLE\_RATE\_11025 | 11025 | The sampling rate is 11025. |
| SAMPLE\_RATE\_12000 | 12000 | The sampling rate is 12000. |
| SAMPLE\_RATE\_16000 | 16000 | The sampling rate is 16000. |
| SAMPLE\_RATE\_22050 | 22050 | The sampling rate is 22050. |
| SAMPLE\_RATE\_24000 | 24000 | The sampling rate is 24000. |
| SAMPLE\_RATE\_32000 | 32000 | The sampling rate is 32000. |
| SAMPLE\_RATE\_44100 | 44100 | The sampling rate is 44100. |
| SAMPLE\_RATE\_48000 | 48000 | The sampling rate is 48000. |
| SAMPLE\_RATE\_64000 | 64000 | The sampling rate is 64000. |
| SAMPLE\_RATE\_8820012+ | 88200 | The sampling rate is 88200. |
| SAMPLE\_RATE\_96000 | 96000 | The sampling rate is 96000. |
| SAMPLE\_RATE\_17640012+ | 176400 | The sampling rate is 176400. |
| SAMPLE\_RATE\_19200012+ | 192000 | The sampling rate is 192000. |

#### AudioEncodingType8+

Enumerates the audio encoding types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ENCODING\_TYPE\_INVALID | \-1 | Invalid. |
| ENCODING\_TYPE\_RAW | 0 | PCM encoding. |

#### AudioChannelLayout11+

Enumerates the audio channel layouts of audio files.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CH\_LAYOUT\_UNKNOWN | 0x0 | Unknown. |
| CH\_LAYOUT\_MONO | 0x4 | Mono. |
| CH\_LAYOUT\_STEREO | 0x3 | Stereo. |
| CH\_LAYOUT\_STEREO\_DOWNMIX | 0x60000000 | Stereo downmix. |
| CH\_LAYOUT\_2POINT1 | 0xB | 2.1. |
| CH\_LAYOUT\_3POINT0 | 0x103 | 3.0. |
| CH\_LAYOUT\_SURROUND | 0x7 | Surround. |
| CH\_LAYOUT\_3POINT1 | 0xF | 3.1. |
| CH\_LAYOUT\_4POINT0 | 0x107 | 4.0. |
| CH\_LAYOUT\_QUAD | 0x33 | Quad. |
| CH\_LAYOUT\_QUAD\_SIDE | 0x603 | Quad side. |
| CH\_LAYOUT\_2POINT0POINT2 | 0x3000000003 | 2.0.2. |
| CH\_LAYOUT\_AMB\_ORDER1\_ACN\_N3D | 0x100000000001 | First-order FOA file in ACN\_N3D (ITU standards). |
| CH\_LAYOUT\_AMB\_ORDER1\_ACN\_SN3D | 0x100000001001 | First-order FOA file in ACN\_SN3D (ITU standards). |
| CH\_LAYOUT\_AMB\_ORDER1\_FUMA | 0x100000000101 | First-order FOA file in FUMA (ITU standards). |
| CH\_LAYOUT\_4POINT1 | 0x10F | 4.1. |
| CH\_LAYOUT\_5POINT0 | 0x607 | 5.0. |
| CH\_LAYOUT\_5POINT0\_BACK | 0x37 | 5.0 back. |
| CH\_LAYOUT\_2POINT1POINT2 | 0x300000000B | 2.1.2. |
| CH\_LAYOUT\_3POINT0POINT2 | 0x3000000007 | 3.0.2. |
| CH\_LAYOUT\_5POINT1 | 0x60F | 5.1. |
| CH\_LAYOUT\_5POINT1\_BACK | 0x3F | 5.1 back. |
| CH\_LAYOUT\_6POINT0 | 0x707 | 6.0. |
| CH\_LAYOUT\_HEXAGONAL | 0x137 | Hexagonal. |
| CH\_LAYOUT\_3POINT1POINT2 | 0x500F | 3.1.2. |
| CH\_LAYOUT\_6POINT0\_FRONT | 0x6C3 | 6.0 front. |
| CH\_LAYOUT\_6POINT1 | 0x70F | 6.1. |
| CH\_LAYOUT\_6POINT1\_BACK | 0x13F | 6.1 back. |
| CH\_LAYOUT\_6POINT1\_FRONT | 0x6CB | 6.1 front. |
| CH\_LAYOUT\_7POINT0 | 0x637 | 7.0. |
| CH\_LAYOUT\_7POINT0\_FRONT | 0x6C7 | 7.0 front. |
| CH\_LAYOUT\_7POINT1 | 0x63F | 7.1. |
| CH\_LAYOUT\_OCTAGONAL | 0x737 | Octagonal. |
| CH\_LAYOUT\_5POINT1POINT2 | 0x300000060F | 5.1.2. |
| CH\_LAYOUT\_7POINT1\_WIDE | 0x6CF | 7.1 wide. |
| CH\_LAYOUT\_7POINT1\_WIDE\_BACK | 0xFF | 7.1 wide back. |
| CH\_LAYOUT\_AMB\_ORDER2\_ACN\_N3D | 0x100000000002 | Second-order HOA file in ACN\_N3D (ITU standards). |
| CH\_LAYOUT\_AMB\_ORDER2\_ACN\_SN3D | 0x100000001002 | Second-order HOA file in ACN\_SN3D (ITU standards). |
| CH\_LAYOUT\_AMB\_ORDER2\_FUMA | 0x100000000102 | Second-order HOA file in FUMA (ITU standards). |
| CH\_LAYOUT\_5POINT1POINT4 | 0x2D60F | 5.1.4. |
| CH\_LAYOUT\_7POINT1POINT2 | 0x300000063F | 7.1.2. |
| CH\_LAYOUT\_7POINT1POINT4 | 0x2D63F | 7.1.4. |
| CH\_LAYOUT\_10POINT2 | 0x180005737 | 10.2. |
| CH\_LAYOUT\_9POINT1POINT4 | 0x18002D63F | 9.1.4. |
| CH\_LAYOUT\_9POINT1POINT6 | 0x318002D63F | 9.1.6. |
| CH\_LAYOUT\_HEXADECAGONAL | 0x18003F737 | Hexadecagonal. |
| CH\_LAYOUT\_AMB\_ORDER3\_ACN\_N3D | 0x100000000003 | Third-order HOA file in ACN\_N3D (ITU standards). |
| CH\_LAYOUT\_AMB\_ORDER3\_ACN\_SN3D | 0x100000001003 | Third-order HOA file in ACN\_SN3D (ITU standards). |
| CH\_LAYOUT\_AMB\_ORDER3\_FUMA | 0x100000000103 | Third-order HOA file in FUMA (ITU standards). |

#### StreamUsage

Enumerates the types of audio streams played.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| STREAM\_USAGE\_UNKNOWN | 0 | 
Unknown content.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| STREAM\_USAGE\_MEDIA(deprecated) | 1 | 

Media.

This enumerated value is supported since API version 7 and deprecated since API version 10. You are advised to use **STREAM\_USAGE\_MUSIC**, **STREAM\_USAGE\_MOVIE**, **STREAM\_USAGE\_GAME**, or **STREAM\_USAGE\_AUDIOBOOK** instead.

 |
| STREAM\_USAGE\_MUSIC10+ | 1 | 

Music.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| STREAM\_USAGE\_VOICE\_COMMUNICATION | 2 | 

VoIP voice call. (The 3A algorithm is enabled when this stream starts.)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| STREAM\_USAGE\_VOICE\_ASSISTANT9+ | 3 | 

Voice assistant.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| STREAM\_USAGE\_ALARM10+ | 4 | 

Audio stream for alarming.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| STREAM\_USAGE\_VOICE\_MESSAGE10+ | 5 | 

Voice message.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| STREAM\_USAGE\_NOTIFICATION\_RINGTONE(deprecated) | 6 | 

Notification tone.

This enumerated value is supported since API version 7 and deprecated since API version 10. You are advised to use **STREAM\_USAGE\_RINGTONE** instead.

 |
| STREAM\_USAGE\_RINGTONE10+ | 6 | 

Ringtone.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| STREAM\_USAGE\_NOTIFICATION10+ | 7 | 

Notification.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| STREAM\_USAGE\_ACCESSIBILITY10+ | 8 | 

Accessibility.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| STREAM\_USAGE\_MOVIE10+ | 10 | 

Movie or video.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| STREAM\_USAGE\_GAME10+ | 11 | 

Gaming.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| STREAM\_USAGE\_AUDIOBOOK10+ | 12 | 

Audiobooks (including crosstalks and storytelling), news radio, and podcasts.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| STREAM\_USAGE\_NAVIGATION10+ | 13 | 

Navigation.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| STREAM\_USAGE\_VIDEO\_COMMUNICATION12+ | 17 | 

VoIP video call. (The 3A algorithm is enabled when this stream starts.)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### AudioState8+

Enumerates the audio states.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| STATE\_INVALID | \-1 | Invalid state. |
| STATE\_NEW | 0 | Creating instance state. |
| STATE\_PREPARED | 1 | Prepared. |
| STATE\_RUNNING | 2 | Running. |
| STATE\_STOPPED | 3 | Stopped. |
| STATE\_RELEASED | 4 | Released. |
| STATE\_PAUSED | 5 | Paused. |

#### AudioEffectMode10+

Enumerates the audio effect modes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

| Name | Value | Description |
| :-- | :-- | :-- |
| EFFECT\_NONE | 0 | The audio effect is disabled. |
| EFFECT\_DEFAULT | 1 | The default audio effect is used. |

#### AudioRendererRate8+

Enumerates the audio renderer rates.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

| Name | Value | Description |
| :-- | :-- | :-- |
| RENDER\_RATE\_NORMAL | 0 | Normal rate. |
| RENDER\_RATE\_DOUBLE | 1 | Double rate. |
| RENDER\_RATE\_HALF | 2 | 0.5x rate. |

#### InterruptType

Enumerates the audio interruption types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

| Name | Value | Description |
| :-- | :-- | :-- |
| INTERRUPT\_TYPE\_BEGIN | 1 | Audio interruption started. |
| INTERRUPT\_TYPE\_END | 2 | Audio interruption ended. |

#### InterruptForceType9+

Enumerates the types of force that causes audio interruption.

The force type is obtained when an [InterruptEvent](../interfaces-others/document.md#interruptevent9) is received.

This type specifies whether audio interruption is forcibly performed by the system. The operation information (such as audio pause or stop) can be obtained through [InterruptHint](#interrupthint). For details about the audio interruption policy, see [Introduction to Audio Focus](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/audio-playback-concurrency).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

| Name | Value | Description |
| :-- | :-- | :-- |
| INTERRUPT\_FORCE | 0 | The operation is forcibly performed by the system. |
| INTERRUPT\_SHARE | 1 | The operation will not be performed by the system. [InterruptHint](#interrupthint) is used to provide recommended operations for the application, and the application can determine the next processing mode. |

#### InterruptHint

Enumerates the hints provided along with audio interruption.

The hint is obtained when an [InterruptEvent](../interfaces-others/document.md#interruptevent9) is received.

The hint specifies the operation (such as audio pause or volume adjustment) to be performed on audio streams based on the focus strategy.

You can determine whether the operation is forcibly performed by the system based on [InterruptForceType](#interruptforcetype9) in **InterruptEvent**. For details, see [Introduction to Audio Focus](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/audio-playback-concurrency).

**System capability**: SystemCapability.Multimedia.Audio.Renderer

| Name | Value | Description |
| :-- | :-- | :-- |
| INTERRUPT\_HINT\_NONE8+ | 0 | 
None.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| INTERRUPT\_HINT\_RESUME | 1 | 

A hint is displayed, indicating that the audio stream is restored. The application can proactively trigger operations related to rendering or recording.

This operation cannot be forcibly performed by the system, and the corresponding [InterruptForceType](#interruptforcetype9) must be **INTERRUPT\_SHARE**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| INTERRUPT\_HINT\_PAUSE | 2 | 

A hint is displayed, indicating that the audio stream is paused and the audio focus is lost temporarily.

When the audio focus is available, the **INTERRUPT\_HINT\_RESUME** event is received.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| INTERRUPT\_HINT\_STOP | 3 | 

A hint is displayed, indicating that the audio stream stops and the audio focus is lost.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| INTERRUPT\_HINT\_DUCK | 4 | 

A hint is displayed, indicating that audio ducking starts and the audio is played at a lower volume.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| INTERRUPT\_HINT\_UNDUCK8+ | 5 | 

A hint is displayed, indicating that audio ducking ends and the audio is played at the normal volume.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| INTERRUPT\_HINT\_MUTE20+ | 6 | A hint is displayed, indicating that the audio is muted. |
| INTERRUPT\_HINT\_UNMUTE20+ | 7 | A hint is displayed, indicating that the audio is unmuted. |

#### AudioVolumeMode19+

Enumerates the audio volume modes.

**System capability**: SystemCapability.Multimedia.Audio.Volume

| Name | Value | Description |
| :-- | :-- | :-- |
| SYSTEM\_GLOBAL | 0 | System-level volume (default mode). |
| APP\_INDIVIDUAL | 1 | Application-level volume. |

#### AudioPrivacyType10+

Enumerates whether an audio stream can be recorded by other applications.

**System capability**: SystemCapability.Multimedia.Audio.PlaybackCapture

| Name | Value | Description |
| :-- | :-- | :-- |
| PRIVACY\_TYPE\_PUBLIC | 0 | The audio stream can be recorded or screen-projected by other applications and is not privacy-related. |
| PRIVACY\_TYPE\_PRIVATE | 1 | The audio stream cannot be recorded or screen-projected by other applications. |
| PRIVACY\_TYPE\_SHARED21+ | 2 | 
The audio stream can be recorded or screen-projected by other applications and is privacy-related.

For example, if the privacy policy is **PRIVACY\_TYPE\_PUBLIC**, audio streams of the [STREAM\_USAGE\_VOICE\_COMMUNICATION](#streamusage) type cannot be recorded or screen-projected by other applications.

However, if the privacy policy is **PRIVACY\_TYPE\_SHARED**, these audio streams can be recorded or screen-projected by other applications.

 |

#### ChannelBlendMode11+

Enumerates the audio channel blending modes.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| MODE\_DEFAULT | 0 | No channel mixing. |
| MODE\_BLEND\_LR | 1 | Blends the left and right channels together. |
| MODE\_ALL\_LEFT | 2 | Copies the left channel and applies it to both the left and right channels. |
| MODE\_ALL\_RIGHT | 3 | Copies the right channel and applies it to both the left and right channels. |

#### AudioStreamDeviceChangeReason11+

Enumerates the reasons for audio stream device changes.

**System capability**: SystemCapability.Multimedia.Audio.Device

| Name | Value | Description |
| :-- | :-- | :-- |
| REASON\_UNKNOWN | 0 | 
Unknown reason.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| REASON\_NEW\_DEVICE\_AVAILABLE | 1 | 

A new device is available.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| REASON\_OLD\_DEVICE\_UNAVAILABLE | 2 | 

The old device is unavailable. When this reason is reported, consider pausing audio playback.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| REASON\_OVERRODE | 3 | 

Forcibly selected.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| REASON\_SESSION\_ACTIVATED20+ | 4 | The audio session has been activated. |
| REASON\_STREAM\_PRIORITY\_CHANGED20+ | 5 | An audio stream with higher priority appears. |

#### OutputDeviceChangeRecommendedAction20+

Enumerates the recommended actions to take after an output device changes.

Common scenario example: switching between a headset and a loudspeaker device. Upon switching from the loudspeaker device to the headset upon wearing, the system suggests continuing playback and prompts that the application does not need to pause. Upon transitioning from the headset to the loudspeaker device upon removal, the system suggests suspending playback.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| DEVICE\_CHANGE\_RECOMMEND\_TO\_CONTINUE | 0 | Suggests continuing playback. (This event serves as a playback maintenance indication, informing the application that audio playback does not need to stop during this device change. However, it must not be used as a criterion for triggering audio playback.) |
| DEVICE\_CHANGE\_RECOMMEND\_TO\_STOP | 1 | Suggests stopping playback. |

#### DeviceChangeType

Enumerates the device connection statuses.

**System capability**: SystemCapability.Multimedia.Audio.Device

| Name | Value | Description |
| :-- | :-- | :-- |
| CONNECT | 0 | Connected. |
| DISCONNECT | 1 | Disconnected. |

#### DeviceBlockStatus13+

Enumerates the blocked statuses of audio devices.

**System capability**: SystemCapability.Multimedia.Audio.Device

| Name | Value | Description |
| :-- | :-- | :-- |
| UNBLOCKED | 0 | The audio device is not blocked. |
| BLOCKED | 1 | The audio device is blocked. |

#### SourceType8+

Enumerates the types of audio streams captured.

| Name | Value | Description |
| :-- | :-- | :-- |
| SOURCE\_TYPE\_INVALID | \-1 | 
Invalid audio source.

**System capability**: SystemCapability.Multimedia.Audio.Core

 |
| SOURCE\_TYPE\_MIC | 0 | 

Mic source.

**System capability**: SystemCapability.Multimedia.Audio.Core

 |
| SOURCE\_TYPE\_VOICE\_RECOGNITION9+ | 1 | 

Voice recognition source.

**System capability**: SystemCapability.Multimedia.Audio.Core

 |
| SOURCE\_TYPE\_PLAYBACK\_CAPTURE(deprecated) | 2 | 

Internal audio recording source.

**System capability**: SystemCapability.Multimedia.Audio.PlaybackCapture

This API is supported since API version 10 and deprecated since API version 12. You are advised to use [AVScreenCapture](../../../../media-kit/c-apis/modules/avscreencapture/document.md) instead.

 |
| SOURCE\_TYPE\_VOICE\_COMMUNICATION | 7 | 

Voice communication source. (The 3A algorithm is not enabled if recording is started independently. It is enabled when the AudioRenderer of the [STREAM\_USAGE\_VOICE\_COMMUNICATION](#streamusage) or [STREAM\_USAGE\_VIDEO\_COMMUNICATION](#streamusage) type is also used to start playback.)

**System capability**: SystemCapability.Multimedia.Audio.Core

 |
| SOURCE\_TYPE\_VOICE\_MESSAGE12+ | 10 | 

Voice message source.

**System capability**: SystemCapability.Multimedia.Audio.Core

 |
| SOURCE\_TYPE\_CAMCORDER13+ | 13 | 

Video recording source.

**System capability**: SystemCapability.Multimedia.Audio.Core

 |
| SOURCE\_TYPE\_UNPROCESSED14+ | 14 | 

Audio source for raw microphone recording, where the system does not perform any algorithm processing.

**System capability**: SystemCapability.Multimedia.Audio.Core

 |
| SOURCE\_TYPE\_LIVE20+ | 17 | 

Audio source in live streaming scenarios. This source type provides system echo cancellation capabilities on supported devices.

**System capability**: SystemCapability.Multimedia.Audio.Core

 |

#### AudioScene8+

Enumerates the audio scenes.

**System capability**: SystemCapability.Multimedia.Audio.Communication

| Name | Value | Description |
| :-- | :-- | :-- |
| AUDIO\_SCENE\_DEFAULT | 0 | Default audio scene. |
| AUDIO\_SCENE\_RINGING12+ | 1 | Normal mode. |
| AUDIO\_SCENE\_PHONE\_CALL12+ | 2 | Phone call scene. |
| AUDIO\_SCENE\_VOICE\_CHAT | 3 | Voice chat scene. |

#### AudioConcurrencyMode12+

Enumerates the audio concurrency modes.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CONCURRENCY\_DEFAULT | 0 | Uses the system strategy by default. |
| CONCURRENCY\_MIX\_WITH\_OTHERS | 1 | Mixes with other audio streams. |
| CONCURRENCY\_DUCK\_OTHERS | 2 | Ducks other audio streams. |
| CONCURRENCY\_PAUSE\_OTHERS | 3 | Pauses other audio streams. |

#### AudioSessionDeactivatedReason12+

Enumerates the reasons for deactivating an audio session.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| DEACTIVATED\_LOWER\_PRIORITY | 0 | The application focus is preempted. |
| DEACTIVATED\_TIMEOUT | 1 | The audio session times out. |

#### AudioSessionScene20+

Enumerates the audio session scenes.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| AUDIO\_SESSION\_SCENE\_MEDIA | 0 | Media audio session. |
| AUDIO\_SESSION\_SCENE\_GAME | 1 | Game audio session. |
| AUDIO\_SESSION\_SCENE\_VOICE\_COMMUNICATION | 2 | VoIP voice call audio session. |

#### AudioSessionStateChangeHint20+

Enumerates the hints for audio session state changes.

The hint is obtained when an [AudioSessionStateChangedEvent](../interfaces-others/document.md#audiosessionstatechangedevent20) is received.

The hint specifies the action (such as audio pause or volume adjustment) to take on the audio session based on the focus strategy.

For details, see [Audio Session Management](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/audio-session-management).

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_RESUME | 0 | A hint is displayed, indicating that the audio session is resuming. The application can proactively trigger operations such as rendering. |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_PAUSE | 1 | A hint is displayed, indicating that the audio session is paused and the audio focus is lost temporarily. When focus is regained, the AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_RESUME event is received. |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_STOP | 2 | A hint is displayed, indicating that the audio session is stopped and the audio focus is lost permanently. |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_TIME\_OUT\_STOP | 3 | A hint is displayed, indicating that the audio session is stopped by the system due to no activity, and the audio focus is lost. |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_DUCK | 4 | A hint is displayed, indicating that audio ducking starts and the audio is played at a lower volume. |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_UNDUCK | 5 | A hint is displayed, indicating that audio ducking ends and the audio is played at the normal volume. |

#### AudioDataCallbackResult12+

Enumerates the audio data callback results.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| INVALID | \-1 | The callback data is invalid. |
| VALID | 0 | The callback data is valid. |

#### ContentType(deprecated)

Enumerates the audio content types.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/eAcnckMiSvWEcejJ4I3Omg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48A9CFD0D406A621BE8C7C0ADF101CD37D9DC89348BF03BD5D1CE91CEB144AA9)

This API is supported since API version 7 and deprecated since API version 10. You are advised to use [StreamUsage](#streamusage) instead.

**System capability**: SystemCapability.Multimedia.Audio.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CONTENT\_TYPE\_UNKNOWN | 0 | Unknown content. |
| CONTENT\_TYPE\_SPEECH | 1 | Speech. |
| CONTENT\_TYPE\_MUSIC | 2 | Music. |
| CONTENT\_TYPE\_MOVIE | 3 | Movie. |
| CONTENT\_TYPE\_SONIFICATION | 4 | Notification tone. |
| CONTENT\_TYPE\_RINGTONE8+ | 5 | Ringtone. |

#### ActiveDeviceType(deprecated)

Enumerates the active device types.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/A5pY4b54TEuBmNR-9s53RA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2012DA0B698884BEBD77082DFF0AC8F16B38A96F502558187F81978AD9FAE2E)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [CommunicationDeviceType](#communicationdevicetype9) instead.

**System capability**: SystemCapability.Multimedia.Audio.Device

| Name | Value | Description |
| :-- | :-- | :-- |
| SPEAKER | 2 | Speaker. |
| BLUETOOTH\_SCO | 7 | Bluetooth device using Synchronous Connection Oriented (SCO) links. |

#### InterruptActionType(deprecated)

Enumerates the returned event types for audio interruption events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/jRPgn72IQn2Rgdbct5ygTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7469278F90E0FAC9104AA710F1C75DDFB17CF0DC61BD3826E02FAFA1EF5B64EF)

This API is supported since API version 7 and deprecated since API version 9. No substitute is provided.

**System capability**: SystemCapability.Multimedia.Audio.Renderer

| Name | Value | Description |
| :-- | :-- | :-- |
| TYPE\_ACTIVATED | 0 | Focus gain event. |
| TYPE\_INTERRUPT | 1 | Audio interruption event. |

#### AudioLoopbackMode20+

Enumerates the audio loopback modes.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

| Name | Value | Description |
| :-- | :-- | :-- |
| HARDWARE | 0 | Hardware loopback. |

#### AudioLoopbackStatus20+

Enumerates the audio loopback statuses.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

| Name | Value | Description |
| :-- | :-- | :-- |
| UNAVAILABLE\_DEVICE | \-2 | Loopback is unavailable due to issues with the input or output device (for example, changes in the audio output device). |
| UNAVAILABLE\_SCENE | \-1 | Loopback is unavailable due to restrictions in the audio scene (for example, audio focus or low-latency management). |
| AVAILABLE\_IDLE | 0 | Loopback is available but currently idle. |
| AVAILABLE\_RUNNING | 1 | Loopback is actively running. |

#### AudioLoopbackReverbPreset21+

Enumerates the reverb modes of audio loopback.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

| Name | Value | Description |
| :-- | :-- | :-- |
| ORIGINAL | 1 | Maintains the original reverb without enhancement. |
| KTV | 2 | Provides a Karaoke-style reverb effect. |
| THEATER | 3 | Provides a theater-style reverb effect (default). |
| CONCERT | 4 | Provides a concert-style reverb effect. |

#### AudioLoopbackEqualizerPreset21+

Enumerates the equalizer types of audio loopback.

**System capability**: SystemCapability.Multimedia.Audio.Capturer

| Name | Value | Description |
| :-- | :-- | :-- |
| FLAT | 1 | Maintains the original sound without equalization. |
| FULL | 2 | Enhances the fullness of vocals (default). |
| BRIGHT | 3 | Enhances the brightness of vocals. |
