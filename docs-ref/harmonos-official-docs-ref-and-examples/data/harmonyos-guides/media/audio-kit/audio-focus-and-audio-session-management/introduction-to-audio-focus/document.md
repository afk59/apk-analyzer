# Introduction to Audio Focus

When an application plays or records a sound, conflicts with other audio streams may occur, adversely affecting user experience. For example, when a video starts playing while music is playing in the background, users expect the music to pause to prioritize the video's audio. This is where audio focus comes into play. For applications that provide audio services, it is important to properly manage audio focus, which can significantly improve the audio experience of users.

This topic outlines the system's audio focus strategy, detailing how applications can respond to focus changes. The system also provides the [audio session management](../audio-session-management/document.md) mechanism, allowing applications to customize the focus strategy for their audio streams.

#### Audio Focus

The system has a default [audio focus strategy](#audio-focus-strategy) that manages all playback and recording audio streams based on their types and the order in which they initiate.

Applications must [request audio focus](#requesting-audio-focus) before starting playback or recording and [release it](#releasing-audio-focus) in time when the playback or recording is complete. During audio playback or recording, audio focus may be lost due to the intervention of other audio streams. In this case, applications need to [handle audio focus changes](#handling-audio-focus-changes).

To ensure a superior audio focus experience for users, applications should:

-   Before starting playback or recording, [select an appropriate audio stream type](../../selecting-the-appropriate-audio-stream-types/document.md) based on the specific use of the audio, by accurately setting [StreamUsage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#streamusage) or [SourceType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#sourcetype8).
    
-   During audio playback or recording, you need to monitor the audio focus to [handle audio focus change events](#handling-audio-focus-changes), and take corresponding measures when receiving an audio focus interruption event ([InterruptEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-i#interruptevent9)).
    
-   If an application intends to actively manage the audio focus, it can use the APIs related to [Audio Session Management](../audio-session-management/document.md) for such operations.
    

## Requesting Audio Focus

When an application starts to play or record audio, the system automatically requests audio focus for that audio stream.

For example, when an application [uses AudioRenderer for audio playback (ArkTs)](../../audio-playback/using-audiorenderer-for-audio-playback-arkts/document.md) and calls [start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#start8) of AudioRenderer, the system automatically requests audio focus for the application.

If the audio focus request is successful, the audio stream starts normally; otherwise, the audio stream fails to start.

It is recommended that the application actively monitor audio focus to [handle audio focus change events](#handling-audio-focus-changes). Once an audio focus request is denied, the application will receive an audio focus event ([InterruptEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-i#interruptevent9)).

If an application wants to request focus just once and play several audio streams in a row without being interrupted, it can use the APIs related to [Audio Session Management](../audio-session-management/document.md).

**Special scenarios:**

1.  **Short sound playback**: If the application [uses SoundPool to play short sounds (ArkTS)](../../../media-kit/media-development-arkts/playback/using-soundpool-to-play-short-sounds-arkts/document.md) and [StreamUsage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#streamusage) is set to **Music**, **Movie**, or **AudioBook**, the concurrent mode is used by default when the focus is requested, and other audios are not affected.
    
2.  **Silent playback**: If an application starts to play audio (or video) in mute mode and intends to avoid affecting other audio during the mute phase, and then seeks audio focus with a standard strategy when unmuting, it can call APIs related to the silent concurrent playback mode. For details, see:
    
    -   [setMediaMuted](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avplayer#setmediamuted12) function: [Using AVPlayer to Play Audio (ArkTS)](../../../media-kit/media-development-arkts/playback/using-avplayer-to-play-audio-arkts/document.md)
        
    -   [setSilentModeAndMixWithOthers](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#setsilentmodeandmixwithothers12) function: [Using AudioRenderer for Audio Playback (ArkTs)](../../audio-playback/using-audiorenderer-for-audio-playback-arkts/document.md)
        
    -   [OH\_AudioRenderer\_SetSilentModeAndMixWithOthers](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_setsilentmodeandmixwithothers) function: [(Recommended) Using OHAudio for Audio Playback (C/C++)](../../audio-playback/recommended-using-ohaudio-for-audio-playback-c-c/document.md)
        

## Releasing Audio Focus

When an application stops playing or recording audio, the system automatically releases audio focus for that audio stream.

For example, when an application [uses AudioRenderer for audio playback (ArkTs)](../../audio-playback/using-audiorenderer-for-audio-playback-arkts/document.md) and calls [pause](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#pause8), [stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#stop8), or [release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#release8) of AudioRenderer, the system releases audio focus for the application.

After the audio focus is released, other audio streams (for example, streams with reduced volume or paused streams) affected by the audio stream will be resumed.

If an application prefers not to release audio focus immediately when the audio stream stops, it can call the APIs related to [Audio Session Management](../audio-session-management/document.md) to delay the release.

If an application has already requested focus by activating [Audio Session Management](../audio-session-management/document.md), it needs to terminate the **AudioSession** to release the focus.

## Audio Focus Strategy

When an audio stream requests or releases audio focus, the system manages focus for all audio streams (including playback and recording) based on the audio focus strategy to determine which audio streams can run properly and which need to be interrupted or perform other operations.

The system's default audio focus strategy is determined based on the audio stream type ([StreamUsage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#streamusage) for playback streams and [SourceType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#sourcetype8) for recording streams) and the sequence in which the audio streams start.

To prevent unexpected focus changes, applications must correctly set **StreamUsage** or **SourceType** based on the usage of the audio stream before starting playback or recording. For details about the stream types, see [Selecting an Appropriate Audio Stream Type](../../selecting-the-appropriate-audio-stream-types/document.md).

Common audio focus scenarios are as follows:

-   When a Movie stream starts playing, the Music stream that is playing will be paused. When the Movie stream ends, the Music stream will not receive any resume notification.
-   When a Navigation stream starts playing, the Music stream that is playing will be ducked. When the Navigation stream ends, the volume of the Music stream will be restored.
-   A Music stream and a Game stream can be mixed and played concurrently without affecting each other.
-   When a VoiceCommunication stream starts playing, the Music stream that is playing will be paused. When the VoiceCommunication stream ends, the Music stream will receive a notification to resume the playback.
-   When a VoiceMessage stream starts playing, the Music stream that is playing will be paused. When the VoiceMessage stream ends, the Music stream will receive a notification to resume the playback.

If the default audio focus strategy cannot meet the requirements of specific scenarios, the application can leverage [Audio Session Management](../audio-session-management/document.md) to adjust the audio focus strategy adopted by the audio streams of the current application.

## Audio Focus Mode

Applications can set the focus mode (specified by [InterruptMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#interruptmode9)) to either self-manage its audio streams or allow the system to manage them uniformly.

The system provides two predefined focus modes:

-   **SHARE\_MODE**: Multiple audio streams from the same application share a single audio focus. The concurrency rules between these audio streams are determined by the application, without the use of the audio focus strategy. However, if another application needs to play audio while one of these audio streams is being played, the audio focus strategy is triggered.
    
-   **INDEPENDENT\_MODE**: Each audio stream from the application has its own audio focus, and the audio focus strategy is triggered when multiple audio streams are played concurrently.
    

Applications can select the appropriate focus mode based on their needs. By default, the system uses **SHARE\_MODE** when creating audio streams, but applications can specify a different mode if desired.

You can set the audio focus mode in one of the following ways:

-   If you [use AVPlayer for audio playback (ArkTS)](../../../media-kit/media-development-arkts/playback/using-avplayer-to-play-audio-arkts/document.md), modify the [audioInterruptMode property](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avplayer#properties) of AVPlayer to set the audio focus mode.
    
-   If you [use AVPlayer for audio playback (C/C++)](../../../media-kit/media-development-c-c/playback/using-avplayer-to-play-audio-c-c/document.md), call [OH\_AVPlayer\_SetAudioInterruptMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setaudiointerruptmode) to set the audio focus mode.
    
-   If you [use AudioRenderer for audio playback (ArkTs)](../../audio-playback/using-audiorenderer-for-audio-playback-arkts/document.md), call [setInterruptMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#setinterruptmode9) of AudioRenderer to set the audio focus mode.
    
-   If you [use OHAudio for audio playback (C/C++)](../../audio-playback/recommended-using-ohaudio-for-audio-playback-c-c/document.md), call [OH\_AudioStreamBuilder\_SetRendererInterruptMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setrendererinterruptmode) to set the audio focus mode.
    

## Handling Audio Focus Changes

If another audio stream requests focus when an application is playing or recording audio, the system handles this situation based on the [audio focus strategy](#audio-focus-strategy). If the current audio stream encounters a focus change and requires operations such as pausing, resuming, ducking, and unducking, the system performs necessary operations and notifies the application through an audio focus event (specified by [InterruptEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-i#interruptevent9)).

To maintain state consistency between the application and system and ensure a positive user experience, it is recommended that the application listen for audio focus events (specified by [InterruptEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-i#interruptevent9)) and respond appropriately to the event when focus changes.

The manners for listening for audio focus events vary according to the development modes:

-   If you [use AVPlayer for audio playback (ArkTS)](../../../media-kit/media-development-arkts/playback/using-avplayer-to-play-audio-arkts/document.md), call [on('audioInterrupt')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avplayer#onaudiointerrupt9) to listen for [InterruptEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-i#interruptevent9).
    
-   If you [use AVPlayer for audio playback (C/C++)](../../../media-kit/media-development-c-c/playback/using-avplayer-to-play-audio-c-c/document.md), call [OH\_AVPlayer\_SetOnInfoCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setoninfocallback) to listen for [OH\_AVPlayerOnInfoCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h#oh_avplayeroninfocallback).
    
-   If you [use AudioRenderer for audio playback (ArkTs)](../../audio-playback/using-audiorenderer-for-audio-playback-arkts/document.md), call [on('audioInterrupt')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#onaudiointerrupt9) to listen for [InterruptEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-i#interruptevent9).
    
-   If you [use OHAudio for audio playback (C/C++)](../../audio-playback/recommended-using-ohaudio-for-audio-playback-c-c/document.md), call [OH\_AudioStreamBuilder\_SetRendererCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setrenderercallback) to listen for audio focus events (specified by [OH\_AudioRenderer\_OnInterruptEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio-oh-audiorenderer-callbacks-struct#oh_audiorenderer_oninterruptevent)).
    
-   If you [use AudioCapturer for audio recording (ArkTs)](../../audio-recording/using-audiocapturer-for-audio-recording-arkts/document.md), call [on('audioInterrupt')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiocapturer#onaudiointerrupt10) to listen for [InterruptEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-i#interruptevent9).
    
-   If you [use OHAudio for audio recording (C/C++)](../../audio-recording/recommended-using-ohaudio-for-audio-recording-c-c/document.md), call [OH\_AudioStreamBuilder\_SetCapturerCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setcapturercallback) to listen for audio focus events (specified by [OH\_AudioCapturer\_OnInterruptEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio-oh-audiocapturer-callbacks-struct#oh_audiocapturer_oninterruptevent)).
    

When receiving an audio focus event (specified by [InterruptEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-i#interruptevent9)), applications must perform corresponding processing based on the information in the event to maintain consistency with the system state and deliver a quality audio experience to users.

In an audio focus event, applications should pay attention to two key pieces of information: **InterruptForceType** and **InterruptHint**.

-   [InterruptForceType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#interruptforcetype9):
    
    This parameter specifies whether the focus change is forcibly performed by the system.
    
    -   **INTERRUPT\_FORCE**: enforced by the system. After receiving an interruption notification, the application does not need to call any system API. It just needs to perform necessary processing, such as updating the status and UI display.
        
    -   **INTERRUPT\_SHARE**: managed by the application, which can choose to respond or ignore, without system interference.
        
    
    By default, the system preferentially uses **INTERRUPT\_FORCE**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/B1UIaZe7TlqxNY06yDMM9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79397F7D252F0633DC2F744BBE253B4B8D0E0849CA529F64355A4F3E65EF3EA7)
    
    For operations that cannot be forcibly performed by the system (for example, **INTERRUPT\_HINT\_RESUME**), **INTERRUPT\_SHARE** is used.
    
-   [InterruptHint](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#interrupthint):
    
    This parameter is used to notify the application of the audio stream status.
    
    -   **INTERRUPT\_HINT\_RESUME**: Audio playback or recording can be resumed. This is received only after a PAUSE message is received.
        
        This operation cannot be forcibly performed by the system, and the corresponding **InterruptForceType** must be **INTERRUPT\_SHARE**.
        
    -   **INTERRUPT\_HINT\_PAUSE**: The audio stream is paused and audio focus is lost temporarily. When focus is available, **INTERRUPT\_HINT\_RESUME** will be received.
        
    -   **INTERRUPT\_HINT\_STOP**: The audio stream stops and audio focus is lost.
        
    -   **INTERRUPT\_HINT\_DUCK**: The audio stream should lower its volume but continue playing, defaulting to 20% of the normal volume.
        
    -   **INTERRUPT\_HINT\_UNDUCK**: The audio stream should return to its normal volume.
        

## Typical Scenarios

The following table lists typical focus adaptation scenarios.

| Audio Type of Application A | Recommended Stream Type | Audio Type of Application B | Recommended Stream Type | Recommended User Experience | Adaptation Solution |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Music | STREAM\_USAGE\_MUSIC | Music | STREAM\_USAGE\_MUSIC | Application A stops playing the music, and the UI displays the stopped state. Application B plays the music normally. | Application A listens for audio focus events. When it receives the **INTERRUPT\_HINT\_STOP** event, it stops music playback and updates its UI. |
| Music | STREAM\_USAGE\_MUSIC | Navigation | STREAM\_USAGE\_NAVIGATION | 
The navigation is played properly, and the music volume is decreased.

After the navigation ends, the music volume is restored to normal.

 | Application A listens for audio focus events. When it receives the **INTERRUPT\_HINT\_DUCK** and **INTERRUPT\_HINT\_UNDUCK** events, it updates its UI. |
| Video | STREAM\_USAGE\_MOVIE | Alarm | STREAM\_USAGE\_ALARM | 

When the alarm rings, the video playback pauses.

When the alarm ends, the video playback resumes.

 | 

Application A listens for audio focus events. When it receives the INTERRUPT\_HINT\_PAUSE event, it pauses video playback and updates its UI.

When the alarm ends, application A receives the **INTERRUPT\_HINT\_RESUME** event and restarts the playback.

 |
| Music | STREAM\_USAGE\_MUSIC | Ringtone | STREAM\_USAGE\_RINGTONE | 

When the phone rings, the music playback pauses.

When the call is not connected or the call is connected and then ended, the music playback resumes.

 | 

Application A listens for audio focus events. When it receives the INTERRUPT\_HINT\_PAUSE event, it pauses music playback and updates its UI.

When the call ends, application A receives the **INTERRUPT\_HINT\_RESUME** event and restarts the playback.

 |
| Music | STREAM\_USAGE\_MUSIC | VoIP call | STREAM\_USAGE\_VOICE\_COMMUNICATION | 

When a call is connected, the music playback pauses.

When the call ends, the music playback resumes.

 | 

Application A listens for audio focus events.

When it receives the INTERRUPT\_HINT\_PAUSE event, it pauses music playback and updates its UI.

When the call ends, application A receives the **INTERRUPT\_HINT\_RESUME** event and restarts the playback.

 |

The following provides an example of audio focus processing.

To deliver an optimal audio experience for users, applications should perform processing based on the event content. The following [uses AudioRenderer for audio playback (ArkTs)](../../audio-playback/using-audiorenderer-for-audio-playback-arkts/document.md) as an example to describe the recommended processing methods for applications.

Before listening for audio playback focus change events, you must obtain an [AudioRenderer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-f#audiocreateaudiorenderer8) instance. If you use other APIs to develop audio playback or recording, the processing method is similar. You can compile the code based on service requirements or adjust the processing methods as needed.

import { audio } from '@kit.AudioKit';  // Import the audio module.
import { BusinessError } from '@kit.BasicServicesKit'; // Import BusinessError.

let isPlay: boolean; // An identifier specifying whether the audio stream is being played. In actual development, this parameter corresponds to the module related to the audio playback state.
let isDucked: boolean; // An identifier specifying whether to duck the volume down. In actual development, this parameter corresponds to the module related to the audio volume.
let started: boolean; // An identifier specifying whether the start operation is successful.

async function onAudioInterrupt(): Promise<void> {
  // The AudioRenderer is used as an example to describe how to develop audio playback. The audioRenderer variable is the AudioRenderer instance created for playback.
  audioRenderer.on('audioInterrupt', async(interruptEvent: audio.InterruptEvent) => {
    // When audio focus changes, the AudioRenderer receives the interruptEvent callback and performs processing based on the content in the callback.
    // 1. (Optional) The AudioRenderer reads the value of interruptEvent.forceType to see whether the system has forcibly performed the operation.
    // Note: In the default focus strategy, INTERRUPT\_HINT\_RESUME maps to the force type INTERRUPT\_SHARE, and others map to INTERRUPT\_FORCE. Therefore, the value of forceType does not need to be checked.
    // 2. (Mandatory) The AudioRenderer then reads the value of interruptEvent.hintType and performs corresponding processing.
    if (interruptEvent.forceType === audio.InterruptForceType.INTERRUPT\_FORCE) {
      // If the value of interruptEvent.forceType is INTERRUPT\_FORCE, the system has performed audio-related processing, and the application needs to update its state and make adjustments accordingly.
       switch (interruptEvent.hintType) {
        case audio.InterruptHint.INTERRUPT\_HINT\_PAUSE:
          // The system has paused the audio stream (focus is temporarily lost). To ensure state consistency, the application needs to switch to the audio paused state.
          // Temporarily losing focus: After other audio streams release focus, the current audio stream will receive the audio focus event corresponding to resume and automatically resume the playback.
          isPlay = false; // A simplified processing indicating several operations for switching the application to the audio paused state.
          break;
        case audio.InterruptHint.INTERRUPT\_HINT\_STOP:
          // The system has stopped the audio stream (focus is permanently lost). To ensure state consistency, the application needs to switch to the audio paused state.
          // Permanently losing focus: No audio focus event will be received. The user must manually trigger the operation to resume playback.
          isPlay = false; // A simplified processing indicating several operations for switching the application to the audio paused state.
          break;
        case audio.InterruptHint.INTERRUPT\_HINT\_DUCK:
          // The system has ducked the volume down (to 20% of the normal volume by default).
          isDucked = true; // A simplified processing indicating several operations for switching the application to the volume decreased state.
          break;
        case audio.InterruptHint.INTERRUPT\_HINT\_UNDUCK:
          // The system has restored the audio volume to normal.
          isDucked = false; // A simplified processing indicating several operations for switching the application to the normal volume state.
          break;
        default:
          break;
      }
    } else if (interruptEvent.forceType === audio.InterruptForceType.INTERRUPT\_SHARE) {
      // If the value of interruptEvent.forceType is INTERRUPT\_SHARE, the application can take action or ignore as required.
      switch (interruptEvent.hintType) {
        case audio.InterruptHint.INTERRUPT\_HINT\_RESUME:
          // The paused audio stream can be played. It is recommended that the application continue to play the audio stream and switch to the audio playing state.
          // If the application does not want to continue the playback, it can ignore the event.
          // To continue the playback, the application needs to call start(), and use the identifier variable started to record the execution result of start().
          await audioRenderer.start().then(() => {
            started = true; // Calling start() is successful.
          }).catch((err: BusinessError) => {
            started = false; // Calling start() fails.
          });
          // If calling start() is successful, the application needs to switch to the audio playing state.
          if (started) {
            isPlay = true; // A simplified processing indicating several operations for switching the application to the audio playing state.
          } else {
            // Resuming the audio playback fails.
          }
          break;
        default:
          break;
      }
   }
  });
}
