# Selecting the Appropriate Audio Stream Types

[Audio stream](../about-this-kit/document.md#introduction-to-audio-streams) types are crucial for determining the mode of audio playback and recording. For audio playback streams, the stream type is determined by [StreamUsage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#streamusage). For audio recording streams, the stream type is determined by [SourceType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#sourcetype8). These types pose a significant impact on volume control, audio focus management, and input/output device selection.

To ensure that the audio behavior meets expectations and delivers a superior user experience, you need to select an appropriate audio stream type based on the use cases and requirements.

This topic describes [typical audio stream types and their use cases](#typical-audio-stream-types-and-use-cases) and [their effects on audio services](#effects-of-audio-stream-types-on-audio-services). It also describes how to [set the audio stream type](#setting-the-audio-stream-type) when you use different methods to implement audio playback and recording.

#### Typical Audio Stream Types and Use Cases

## Stream Types for Audio Playback

The following table describes the typical stream types used for audio playback. The type is specified by [StreamUsage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#streamusage).

| Stream Type | Use Case |
| :-- | :-- |
| STREAM\_USAGE\_MUSIC | Music playback and other media scenarios, for example, using [SoundPool](../../media-kit/media-development-arkts/playback/using-soundpool-to-play-short-sounds-arkts/document.md) to play short sounds. |
| STREAM\_USAGE\_MOVIE | Playing various video content such as short videos, movies, and TV series. |
| STREAM\_USAGE\_AUDIOBOOK | Playing audiobooks, news, and podcasts. |
| STREAM\_USAGE\_GAME | In-game background scores and character dubbing, ensuring uninterrupted background music. It is recommended that you use **STREAM\_USAGE\_VOICE\_COMMUNICATION** for in-game voice. |
| STREAM\_USAGE\_NAVIGATION | Voice broadcast in navigation scenarios. |
| STREAM\_USAGE\_VOICE\_MESSAGE | Playing voice short messages. |
| STREAM\_USAGE\_VOICE\_COMMUNICATION | VoIP voice calls. |
| STREAM\_USAGE\_ALARM | Playing alarms. |
| STREAM\_USAGE\_RINGTONE | Playing ringtones for VoIP calls. |
| STREAM\_USAGE\_NOTIFICATION | Playing notification tones and prompt tones. |

## Stream Types for Audio Recording

The following table describes the typical stream types used for audio recording. The type is specified by [SourceType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#sourcetype8).

| Stream Type | Use Case |
| :-- | :-- |
| SOURCE\_TYPE\_MIC | Common audio recording. |
| SOURCE\_TYPE\_VOICE\_RECOGNITION9+ | Voice recognition. |
| SOURCE\_TYPE\_PLAYBACK\_CAPTURE | 
(Deprecated in API version 12) Recording raw audio data sent by other applications to the system for playback.

Audio Kit does not provide APIs for internal recording. You can use [AVScreenCapture](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avscreencapture) to perform internal recording.

 |
| SOURCE\_TYPE\_VOICE\_COMMUNICATION | VoIP voice calls. |
| SOURCE\_TYPE\_VOICE\_MESSAGE | Recording voice short messages. |
| SOURCE\_TYPE\_CAMCORDER13+ | Camera recording. |
| SOURCE\_TYPE\_UNPROCESSED14+ | Obtaining pure audio data captured by the microphone (without any system processing). |
| SOURCE\_TYPE\_LIVE20+ | Live streaming. This source type provides system echo cancellation capabilities on supported devices. |

#### Effects of Audio Stream Types on Audio Services

Different stream types affect user experience in volume control and system performance in adjusting the audio focus and selecting input/output devices. In addition, the system configures corresponding optimization processing strategies for the captured audio data based on the recording stream type. Therefore, the recording stream type affects the audio recording quality. For example, using **SOURCE\_TYPE\_MIC** instead of **SOURCE\_TYPE\_VOICE\_COMMUNICATION** in a VoIP call scenario may disable noise reduction and ambient sound elimination optimizations, leading to a poor VoIP call experience. You are advised to select the appropriate audio stream type based on the service scenario.

## Volume Control

The audio playback stream type (specified by [StreamUsage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#streamusage)) determines the volume type (specified by [AudioVolumeType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype)) to which the audio stream belongs. Each volume type (such as **MEDIA**, **RINGTONE**, **ALARM**, and **VOICE\_CALL**) has an independent volume value, which can be adjusted independently on the UI.

The table below lists the mappings between the typical audio playback stream types and volume types.

| Stream Type | Volume Type |
| :-- | :-- |
| MUSIC, MOVIE, AUDIOBOOK, GAME | MEDIA |
| RINGTONE, NOTIFICATION | RINGTONE |
| VOICE\_COMMUNICATION | VOICE\_CALL |
| ALARM | ALARM |

## Adjusting the Audio Focus

The audio stream type plays a key role in audio focus management. Different types of audio streams have different default priorities and processing modes for the audio focus.

When an application starts audio playback or recording, the system automatically applies for focus based on the audio stream type. This may interrupt or duck other audio streams. For details about the audio focus, see [Introduction to Audio Focus](../audio-focus-and-audio-session-management/introduction-to-audio-focus/document.md).

This section describes only how the typical audio stream types affect the audio focus. For details about other types, see [Default Focus Strategies](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-audio-focus-management#section17923135513547).

-   When a Navigation stream starts playing, the Music stream that is playing will be ducked. After the Navigation stream ends, the volume of the Music stream will be restored.
    
-   When a Movie stream starts playing, the Music stream that is playing will be stopped. When the Movie stream ends, the Music stream will not be automatically resumed, and the corresponding application will not receive any resume notification.
    
-   When a VoiceCommunication stream starts, the Music stream that is playing will be paused. When the VoiceCommunication stream ends, the music application will receive a notification to resume the playback.
    
-   The Music stream and Game stream can be mixed and played concurrently without affecting each other.
    
-   When a VoiceMessage stream starts, the Music stream that is playing will be paused. When the VoiceMessage stream ends, the music application will receive a notification to resume the playback.
    

## Selecting Input/Output Devices

The system selects an input/output device based on the audio stream type.

The following lists the input/output devices selected for the typical audio stream types.

-   For a MUSIC stream, the default output device is a speaker.
    
-   For a VoiceCommunication stream, the default input device is a microphone, and the default output device is an earpiece.
    
-   For an Alarm stream, the default output device is a speaker. If a Bluetooth headset is connected before an ALARM stream is played, the audio is output from both the speaker and Bluetooth headset.
    

If the default input/output devices do not meet service requirements, you can call related APIs to change the devices. When [using AudioRenderer to develop audio playback (ArkTs)](../audio-playback/using-audiorenderer-for-audio-playback-arkts/document.md), you can call [setDefaultOutputDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#setdefaultoutputdevice12) to set the default sound device.

#### Setting the Audio Stream Type

The application can implement audio playback or recording by using a plurality of methods. Therefore, manners of setting the audio stream type are also different.

Common methods for setting the audio playback stream type are as follows:

-   **[Using AudioRenderer for Audio Playback (ArkTs)](../audio-playback/using-audiorenderer-for-audio-playback-arkts/document.md):**
    
    Pass [StreamUsage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#streamusage) in [createAudioRenderer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-f#audiocreateaudiorenderer8) to specify the stream type.
    
    The **options** parameter in **createAudioRenderer** is of the **AudioRendererOptions** type and contains the **AudioRendererInfo** struct, in which **AudioRendererInfo.usage** specifies the stream type.
    
-   **[(Recommended) Using OHAudio for Audio Playback (C/C++)](../audio-playback/recommended-using-ohaudio-for-audio-playback-c-c/document.md):**
    
    Pass [OH\_AudioStream\_Usage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_usage) in [OH\_AudioStreamBuilder\_SetRendererInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setrendererinfo) to specify the stream type.
    
-   **[Using AVPlayer to Play Audio (ArkTS)](../../media-kit/media-development-arkts/playback/using-avplayer-to-play-audio-arkts/document.md):**
    
    Set the **audioRendererInfo** [property](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avplayer#properties) of the AVPlayer. **AVPlayer.audioRendererInfo** is of the **audio.AudioRendererInfo** type. You can use **AudioRendererInfo.usage** to specify [StreamUsage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#streamusage).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/9GkSAQtVQ2aIBua4QfIfag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BCD0BA4F5BD6A9E2E4148B4A9AD2BA9E8C2126659430C7E344F26E715FAF3D6B)
    
    The **audioRendererInfo** property of the AVPlayer can be set only in the initialized state.
    
    If the application does not set this property, the AVPlayer performs default processing. If the media source contains videos, the default value of **usage** is **STREAM\_USAGE\_MOVIE**. Otherwise, the default value of **usage** is **STREAM\_USAGE\_MUSIC**.
    
-   **[Using AVPlayer to Play Audio (C/C++)](../../media-kit/media-development-c-c/playback/using-avplayer-to-play-audio-c-c/document.md):**
    
    Pass [OH\_AudioStream\_Usage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_usage) in [OH\_AVPlayer\_SetAudioRendererInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setaudiorendererinfo) to specify the stream type.
    
-   **[Using SoundPool to Play Short Sounds (ArkTS)](../../media-kit/media-development-arkts/playback/using-soundpool-to-play-short-sounds-arkts/document.md):**
    
    Pass [StreamUsage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#streamusage) in [createSoundPool](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-f#mediacreatesoundpool10) to specify the stream type.
    

Common methods for setting the audio recording stream type are as follows:

-   **[Using AudioCapturer for Audio Recording (ArkTs)](../audio-recording/using-audiocapturer-for-audio-recording-arkts/document.md):**
    
    Pass [SourceType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#sourcetype8) in [createAudioCapturer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-f#audiocreateaudiocapturer8) to specify the stream type.
    
    The **options** parameter in **createAudioCapturer** is of the **AudioCapturerOptions** type and contains **AudioCapturerInfo**, in which **AudioCapturerInfo.source** specifies the source type.
    
-   **[(Recommended) Using OHAudio for Audio Recording (C/C++)](../audio-recording/recommended-using-ohaudio-for-audio-recording-c-c/document.md):**
    
    Pass [OH\_AudioStream\_SourceType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_sourcetype) in [OH\_AudioStreamBuilder\_SetCapturerInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setcapturerinfo) to specify the stream type.
    
-   **[Using AVRecorder to Record Audio (ArkTS)](../../media-kit/media-development-arkts/recording/using-avrecorder-to-record-audio-arkts/document.md):**
    
    Pass [AudioSourceType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-e#audiosourcetype9) in [AVRecorder.prepare](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#prepare9-1) to specify the stream type.
    
    The **config** parameter in **AVRecorder.prepare** is of the **AVRecorderConfig** type, in which **AVRecorderConfig.audioSourceType** specifies the audio source type.
