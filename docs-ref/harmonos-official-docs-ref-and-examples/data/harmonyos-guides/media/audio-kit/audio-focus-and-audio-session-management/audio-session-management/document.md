# Audio Session Management

For scenarios involving concurrent playback of multiple audio streams, the system has preset a default [Audio Focus Strategy](../introduction-to-audio-focus/document.md#audio-focus-strategy), which enforces unified focus management for all audio streams (including playback and recording).

When the default focus strategy provided by the system fails to meet the application's requirements, the application can use the APIs provided by audio session management to manage the focus of audio streams within the application, customize the focus strategy for audio streams, and adjust the timing of releasing focus for audio streams to meet specific needs. All sample codes in this document are in ArkTS. If you need to develop with OHAudio, refer to [Using OHAudio for Audio Session (C/C++)](../using-ohaudio-for-audio-session-c-c/document.md).

Using audio session-related APIs enables the following functions:

-   When the system's default focus strategy cannot meet the application's current needs, the application can [modify the focus strategy using AudioSession](#modifying-the-focus-strategy-using-audiosession) to adapt a focus strategy suitable for itself.
    
    Typical scenario: When an application plays short videos, it interrupts background music. The application expects the background music to resume automatically after its own audio stream stops. This scenario requires the application to activate an **AudioSession** before starting the audio stream and deactivate it after the audio stream stops.
    
-   When an application needs to start multiple audio streams in a service process and ensure the integrity of the entire process, the application can [apply for a focus strategy using AudioSession](#applying-for-a-focus-strategy-using-audiosession) to adapt a focus strategy suitable for its service scenario.
    
    Typical scenario: When an application plays multiple audio files continuously, it does not want other interrupted background audio to resume automatically during the gaps between audio playback, and expects to maintain the continuity of audio focus throughout the playback process. This scenario requires the application to activate an **AudioSession** before the start of the entire playback process and deactivate it after the entire playback process ends).
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/FGKB0k1jS4W8xYynNyq4iA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=154CE751608002446528923B35C1CFEABF26E224A4C58A0C981F9EA62B855046)

-   The priority of audio concurrency policies is: **STOP** > **PAUSE** > **DUCK** > **PLAYBOTH**. If the specified audio session strategy has a higher priority than the default concurrency strategy, the specified audio session strategy will not take effect.
-   The application must ensure that the audio session is activated before starting audio playback or recording; otherwise, the custom focus strategy of the audio session will not take effect. If the application uses asynchronous APIs, special attention must be paid to the timing of asynchronous operations.

#### Obtaining an Audio Session Manager

Before using the APIs of **AudioSessionManager**, you need to obtain a singleton **AudioSessionManager** object through [getSessionManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiomanager#getsessionmanager12).

For development with OHAudio, see [Obtaining an Audio Session Manager](../using-ohaudio-for-audio-session-c-c/document.md#obtaining-an-audio-session-manager).

import { audio } from '@kit.AudioKit';

let audioManager = audio.getAudioManager();
let audioSessionManager: audio.AudioSessionManager = audioManager.getSessionManager();

#### Audio Session Strategy

Before activating an audio session, you must first specify an [audio session strategy (AudioSessionStrategy)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-i#audiosessionstrategy12) by setting an [audio concurrency mode (AudioConcurrencyMode)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#audioconcurrencymode12).

For development with OHAudio, see [OH\_AudioSession\_Strategy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio-oh-audiosession-strategy).

The preset audio concurrency modes are as follows:

-   **CONCURRENCY\_DEFAULT**: default [audio focus strategy](../introduction-to-audio-focus/document.md#audio-focus-strategy) of the system.
    
-   **CONCURRENCY\_MIX\_WITH\_OTHERS**: concurrent playback with other audio streams.
    
    **Typical scenarios:**
    
    -   When an application plays music, it is interrupted by subsequent music or video playback. The application expects its own audio stream to be concurrent with the subsequent music or video. This scenario requires the application to activate an **AudioSession** before starting the audio stream).
        
    -   When an application records audio, it interrupts background music or video playback. The application expects its own audio stream to be concurrent with the background music or video. This scenario requires the application to activate an **AudioSession** before starting the audio stream.
        
-   **CONCURRENCY\_DUCK\_OTHERS**: concurrent with other audio streams and reduces the volume of other audio streams.
    
    **Typical scenario**: When an application plays game sound effects, it is concurrent with background music playback. The application expects to lower the volume of the background music when its own audio stream is concurrent with it (this scenario requires the application to activate an **AudioSession** before starting the audio stream).
    
-   **CONCURRENCY\_PAUSE\_OTHERS**: pauses other audio streams and notifies them to resume after releasing the focus.
    
    **Typical scenario**: When an application plays short videos, it interrupts background music. The application expects the background music to resume automatically after its own audio stream stops. This scenario requires the application to activate an **AudioSession** before starting the audio stream and deactivate it after the audio stream stops.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/kdXvfARhQ7ufakGXQA483g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=498C25D19C0B5733EACB3CEC3A74D390245F871A9BCF60802A2DEADDBBB5E36E)

-   When an application uses the above modes through **AudioSession**, the system will try to meet its focus strategy but cannot guarantee fulfillment in all scenarios.
-   The **CONCURRENCY\_MIX\_WITH\_OTHERS** mode takes effect both when the application applies for focus and when other applications apply for focus subsequently. The **CONCURRENCY\_DUCK\_OTHERS** and **CONCURRENCY\_PAUSE\_OTHERS** modes only take effect when the application applies for focus; when other applications apply for focus subsequently, the concurrency mode of the other applications is followed first.

#### Modifying the Focus Strategy Using AudioSession

When the system's default focus strategy cannot meet the application's current needs, the application can modify the focus strategy by specifying an [Audio Session Strategy](#audio-session-strategy) and then activating an **AudioSession**.

After the **AudioSession** is successfully activated, new audio streams started by the application will follow the modified focus strategy.

When the focus strategy is modified using **AudioSession**, the **AudioSession** does not hold the focus. The focus is still held by each individual audio stream.

For development with OHAudio, see [Using OHAudio for Audio Session (C/C++)](../using-ohaudio-for-audio-session-c-c/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/6GdY_1g0RlOyfzr4mmz6QQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60CC5ED031F9A8398812BEE36C9F63983CED30DF75DEE330D77D7FDCC20D3234)

When an **AudioSession** is deactivated due to timeout, audio streams whose volume was lowered (duck) by it will trigger an unduck operation, and audio streams that were paused by it will trigger a stop operation.

## AudioSession Deactivation Event

During the use of **AudioSession**, it is recommended that the application listen to the **AudioSessionDeactivatedEvent**. When the **AudioSession** is deactivated (not actively), the application will receive this event notification. The application can take corresponding actions according to its service needs, such as releasing relevant resources or reactivating the **AudioSession**.

The **AudioSessionDeactivatedEvent** contains the parameter **AudioSessionDeactivatedReason**, which indicates the reason for the deactivation of the **AudioSession**. There are two main reasons:

1.  **DEACTIVATED\_LOWER\_PRIORITY**: When all focus held by the audio streams of the application is preempted by other applications, the **AudioSession** is deactivated at the same time.
    
2.  **DEACTIVATED\_TIMEOUT**: If the **AudioSession** is in the activated state but there are no running audio streams in the application, the **AudioSession** will be deactivated due to timeout after a specified period of time.
    

## How to Develop

1.  Specify the audio session strategy (**AudioSessionStrategy**) and activate an **AudioSession**.
    
    Call [activateAudioSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#activateaudiosession12) to activate an **AudioSession**.
    
    Specify the [audio session strategy](#audio-session-strategy) when activating the **AudioSession**. The strategy contains the **concurrencyMode** parameter, which is of the [AudioConcurrencyMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#audioconcurrencymode12) type and is used to declare the audio concurrency strategy.
    
    import { audio } from '@kit.AudioKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    let strategy: audio.AudioSessionStrategy = {
      concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY\_MIX\_WITH\_OTHERS
    };
    
    audioSessionManager.activateAudioSession(strategy).then(() => {
      console.info('Succeeded in activating audio session.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to activate audio session. Code: ${err.code}, message: ${err.message}\`);
    });
    
2.  (Optional) Check whether the audio session is activated.
    
    Call [isAudioSessionActivated](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#isaudiosessionactivated12) to check whether an audio session is activated.
    
    let isActivated = audioSessionManager.isAudioSessionActivated();
    
3.  (Optional) Listen for the audio session deactivation event.
    
    Call [on('audioSessionDeactivated')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#onaudiosessiondeactivated12) to listen for the [AudioSessionDeactivatedEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-i#audiosessiondeactivatedevent12) event.
    
    When an audio session is deactivated (not proactively), the application receives [AudioSessionDeactivatedEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-i#audiosessiondeactivatedevent12), which contains [AudioSessionDeactivatedReason](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#audiosessiondeactivatedreason12).
    
    Upon this event, the application can perform operations based on service requirements, for example, releasing resources or reactivating the audio session.
    
    Call [off('audioSessionDeactivated')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#offaudiosessiondeactivated12) to cancel listening for **AudioSessionDeactivatedEvent**.
    
    import { audio } from '@kit.AudioKit';
    
    audioSessionManager.on('audioSessionDeactivated', (audioSessionDeactivatedEvent: audio.AudioSessionDeactivatedEvent) => {
      console.info(\`Succeeded in using on function. AudioSessionDeactivatedEvent: ${JSON.stringify(audioSessionDeactivatedEvent)}\`);
    });
    
4.  Deactivate the **AudioSession**.
    
    Call [deactivateAudioSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#deactivateaudiosession12) to deactivate an audio session.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/hQ8TCxyMQ4Oykxw6VUSEyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84EB239F4B618E77B03C8CD68E9A91C984A2E0610D5790E1C61A8031F19D3BBF)
    
    After the **AudioSession** is deactivated, new audio streams started by the application will follow the default focus strategy.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    audioSessionManager.deactivateAudioSession().then(() => {
      console.info('Succeeded in deactivating audio session.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to deactivate audio session. Code: ${err.code}, message: ${err.message}\`);
    });
    

## Sample Code

The following shows the sample code for modifying the focus strategy using **AudioSession**.

import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioManager = audio.getAudioManager();
// Create an audio session manager.
let audioSessionManager: audio.AudioSessionManager = audioManager.getSessionManager();
// Set the audio concurrency mode.
let strategy: audio.AudioSessionStrategy = {
  concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY\_MIX\_WITH\_OTHERS
};

// Activate an audio session.
audioSessionManager.activateAudioSession(strategy).then(() => {
  console.info('Succeeded in activating audio session.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to activate audio session. Code: ${err.code}, message: ${err.message}\`);
});

// Check whether the audio session is activated.
let isActivated = audioSessionManager.isAudioSessionActivated();

// Listen for audio session deactivation events.
audioSessionManager.on('audioSessionDeactivated', (audioSessionDeactivatedEvent: audio.AudioSessionDeactivatedEvent) => {
  console.info(\`Succeeded in using on function. AudioSessionDeactivatedEvent: ${JSON.stringify(audioSessionDeactivatedEvent)}\`);
});

if (isActivated) {
  // After the audio session is activated, the application can perform operations such as playing, pausing, stopping, and releasing audio streams.
}

// Cancel listening for audio session deactivation events.
audioSessionManager.off('audioSessionDeactivated');

// Deactivate the audio session.
audioSessionManager.deactivateAudioSession().then(() => {
  console.info('Succeeded in deactivating audio session.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to deactivate audio session. Code: ${err.code}, message: ${err.message}\`);
});

#### Applying for a Focus Strategy Using AudioSession

When an application needs to start multiple audio streams and ensure the continuity of the process, it can apply for focus through an **AudioSession** to ensure the continuity of playback of multiple audio streams.

During the activation of **AudioSession**, the system applies for the corresponding audio focus based on the [audio session scene](#audio-session-scene) selected by the application, and the **AudioSession** will hold the focus. Subsequent playback streams started by the application through **AudioRenderer** will no longer apply for audio focus.

For development with OHAudio, see [Using OHAudio for Audio Session (C/C++)](../using-ohaudio-for-audio-session-c-c/document.md).

Typical usage scenarios are as follows:

-   When sliding to play multiple short videos, frequent application and release of focus by multiple audio streams may cause audio leakage. Applying for focus once through **AudioSession** can avoid frequent application and release of focus during the playback of multiple audio streams, thereby preventing audio leakage.
-   In VoIP call scenarios, it may be necessary to start a ringtone stream, a recording stream, and a playback stream. These audio streams have different focus priorities, and some audio streams may be interrupted by audio streams of other applications. To maintain a continuous user experience, you can use **AudioSession** to request focus and avoid interruptions to the audio streams.
-   The application uses the SDK of the player to play audio streams and does not hold the **AudioRenderer** object, but expects to listen for focus changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/t3tDYnhsR1yYC36Jqg2hNg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BCAF37A89AC301DAAF5E02BDC727548E39A7CF011E06EEF684C51F9C04ED6790)

-   The focus applied for through **AudioSession** is at the application level. If the application contains different modules, the modules must coordinate with each other to avoid situations where one module applies for focus using **AudioSession**, causing audio streams of another module to be controlled by the focus of **AudioSession** and producing unintended effects.
-   Applying for focus through **AudioSession** is only valid for playback streams, and invalid for recording streams and some playback audio streams (such as **STREAM\_USAGE\_ALARM**, **STREAM\_USAGE\_NOTIFICATION**, and **STREAM\_USAGE\_ACCESSIBILITY**).
-   If the **AudioSessionScene** is dynamically modified during the activation of the **AudioSession**, **activateAudioSession** must be called again to take effect.
-   After the focus is applied for through **AudioSession**, the focus is held by the **AudioSession**. Once the current playback of the application ends, the application needs to actively deactivate the **AudioSession** to release the focus. This prevents the focus from being held abnormally after the playback stream stops.

## Audio Session Scene

When you use **AudioSession** to apply for a focus strategy, the system provides three audio session scenes. Before activating the **AudioSession**, you need to set the corresponding audio session scene through [setAudioSessionScene](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#setaudiosessionscene20). When the **AudioSession** is activated subsequently, the system will apply for the corresponding audio focus according to the audio session scene selected by the application.

| Name | Value | Description |
| :-- | :-- | :-- |
| AUDIO\_SESSION\_SCENE\_MEDIA | 0 | Media audio session. |
| AUDIO\_SESSION\_SCENE\_GAME | 1 | Game audio session. |
| AUDIO\_SESSION\_SCENE\_VOICE\_COMMUNICATION | 2 | VoIP voice call audio session. |

## Listening for AudioSession Focus State Change Events

The focus applied for through **AudioSession** is equivalent to that applied for through **AudioRenderer**.

The application can call [on('audioSessionStateChanged')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#onaudiosessionstatechanged20) to listen for focus state changes of the **AudioSession**. To maintain state consistency between the application and the system, the application should listen for the **AudioSession** focus state events and make necessary responses when the focus changes.

[on('audioSessionStateChanged')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#onaudiosessionstatechanged20) contains information about the [AudioSession deactivation event](#audiosession-deactivation-event). When [applying for a focus strategy using AudioSession](#applying-for-a-focus-strategy-using-audiosession), you do not need to listen for the **AudioSessionDeactivatedEvent**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/qsko96bWTsO4W8-7ZjLOJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BD95785BC4A6421F2DCA7F88E9FE7B12208370155F3792F97D0CF6591FD801F)

If the application registers a listener for focus events of **AudioRenderer** at the same time, note the following:

1.  The application will receive callbacks ([InterruptEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-i#interruptevent9)) for both **AudioSession** focus state changes and **AudioRenderer** focus changes. Handle these callbacks as needed.
2.  If the focus of the **AudioSession** is paused, only the **AudioSession** will receive the focus resume event when it is resumed, and the **AudioRenderer** will not receive the focus resume event.

## How to Develop

1.  Specify the **AudioSessionScene** and **AudioSessionStrategy**, and activate an **AudioSession**.
    
    The application requests focus using an audio session. Call [setAudioSessionScene](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#setaudiosessionscene20) to set the scene parameters, and then call [activateAudioSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#activateaudiosession12) to activate the audio session. During the activation of **AudioSession**, the system will apply for the corresponding audio focus according to the audio session scene selected by the application.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/2bngRWpXROiGkUUJTjR-mw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A539D761895029AF0ABE57280511127EDA0F5E7B5CA2C2440FC34BB65B09B79)
    
    -   During the activation of **AudioSession**, the system will apply for the corresponding audio focus according to the audio session scene selected by the application. Subsequent playback streams started by the application through **AudioRenderer** will no longer apply for audio focus.
    -   If there are already active audio playback streams in the application before the **AudioSession** is activated, the system will release the focus held by these audio playback streams and manage it uniformly through the **AudioSession**.
    
    import { audio } from '@kit.AudioKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    audioSessionManager.setAudioSessionScene(audio.AudioSessionScene.AUDIO\_SESSION\_SCENE\_MEDIA);
    
    let strategy: audio.AudioSessionStrategy = {
      concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY\_MIX\_WITH\_OTHERS
    };
    
    audioSessionManager.activateAudioSession(strategy).then(() => {
      console.info('Succeeded in activating audio session.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to activate audio session. Code: ${err.code}, message: ${err.message}\`);
    });
    
2.  (Optional) Check whether the audio session is activated.
    
    Call [isAudioSessionActivated](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#isaudiosessionactivated12) to check whether an audio session is activated.
    
    let isActivated = audioSessionManager.isAudioSessionActivated();
    
3.  Listen for **AudioSession** focus state change events.
    
    Call [on('audioSessionStateChanged')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#onaudiosessionstatechanged20) to listen for focus state changes of the **AudioSession**.
    
    import { audio } from '@kit.AudioKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    let audioSessionStateChangedCallback = (audioSessionStateChangedEvent: audio.AudioSessionStateChangedEvent) => {
      console.info(\`hint of audioSessionStateChanged: ${audioSessionStateChangedEvent.stateChangeHint} \`);
    
      switch (audioSessionStateChangedEvent.stateChangeHint) {
        case audio.AudioSessionStateChangeHint.AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_PAUSE:
          // The system has paused the audio stream. The application should switch to the audio paused state.
          // Temporary loss of focus: The AudioSession will be deactivated and release the focus, and stop all audio streams of the application. Therefore, after the application receives the Resume callback, it needs to reactivate the AudioSession and resume the audio streams as needed.
          break;
        case audio.AudioSessionStateChangeHint.AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_RESUME:
          // The system has resumed the AudioSession.
          break;
        case audio.AudioSessionStateChangeHint.AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_STOP:
          // The system has stopped the audio stream (focus is permanently lost). To ensure state consistency, the application should switch to the audio paused state.
          // Permanent loss of focus: The AudioSession will be deactivated and release the focus, and stop all audio streams of the application. No further audio focus events will be received subsequently, and resuming playback requires active triggering by the user.
          break;
        case audio.AudioSessionStateChangeHint.AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_TIME\_OUT\_STOP:
          // The system has stopped the AudioSession (permanent loss of focus) due to inactivity. The application should switch to the audio stop state.
          // Permanently losing focus: No audio focus event will be received. The user must manually trigger the operation to resume playback.
          break;
        case audio.AudioSessionStateChangeHint.AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_DUCK:
          // The system has reduced the volume of all playing audio streams of the application (default to 20% of the normal volume).
          break;
        case audio.AudioSessionStateChangeHint.AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_UNDUCK:
          // The system has restored the volume of all playing audio streams of the application to normal.
          break;
        default:
          break;
      }
    };
    
    audioSessionManager.on('audioSessionStateChanged', audioSessionStateChangedCallback);
    
4.  Deactivate the **AudioSession**.
    
    Call [deactivateAudioSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#deactivateaudiosession12) to deactivate an audio session.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/gstYUyDVRAaBNeaw9kflgQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0512F10C7C531DA8B56577CB5DBBC74968DA7B8B780DB4C5EB7C6CA4286842F2)
    
    When the **AudioSession** is deactivated, the system releases the focus applied by the **AudioSession** and stops all audio streams being played by the application.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    audioSessionManager.deactivateAudioSession().then(() => {
      console.info('Succeeded in doing deactivateAudioSession.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to deactivateAudioSession. Code: ${err.code}, message: ${err.message}\`);
    });
    

## Sample Code

The following shows the sample code for applying for a focus strategy using **AudioSession**.

import { audio } from '@kit.AudioKit';  // Import the audio module.
import { BusinessError } from '@kit.BasicServicesKit'; // Import BusinessError.

// The application sets an audio session scenario based on the service scenario. When AudioSession is activated, the system applies for the corresponding audio focus based on the selected audio session scenario.
audioSessionManager.setAudioSessionScene(audio.AudioSessionScene.AUDIO\_SESSION\_SCENE\_MEDIA);

// Set the audio session policy.
let strategy: audio.AudioSessionStrategy = {
  concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY\_MIX\_WITH\_OTHERS;
};

// Activate the AudioSession.
audioSessionManager.activateAudioSession(strategy).then(() => {
  console.info('Succeeded in activating audio session.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to activate audio session. Code: ${err.code}, message: ${err.message}\`);
});

// Listen for AudioSession focus state change events.
let audioSessionStateChangedCallback = (audioSessionStateChangedEvent: audio.AudioSessionStateChangedEvent) => {
  console.info(\`hint of audioSessionStateChanged: ${audioSessionStateChangedEvent.stateChangeHint} \`);

  switch (audioSessionStateChangedEvent.stateChangeHint) {
    case audio.AudioSessionStateChangeHint.AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_PAUSE:
      // The system has paused the audio stream. The application should switch to the audio paused state.
      // Temporary loss of focus: The AudioSession will be deactivated and release the focus, and stop all audio streams of the application. Therefore, after the application receives the Resume callback, it needs to reactivate the AudioSession and resume the audio streams as needed.
      break;
    case audio.AudioSessionStateChangeHint.AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_RESUME:
      // The system has resumed the AudioSession.
      break;
    case audio.AudioSessionStateChangeHint.AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_STOP:
      // The system has stopped the audio stream (focus is permanently lost). To ensure state consistency, the application should switch to the audio paused state.
      // Permanent loss of focus: The AudioSession will be deactivated and release the focus, and stop all audio streams of the application. No further audio focus events will be received subsequently, and resuming playback requires active triggering by the user.
      break;
    case audio.AudioSessionStateChangeHint.AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_TIME\_OUT\_STOP:
      // The system has stopped the AudioSession (permanent loss of focus) due to inactivity. The application should switch to the audio stop state.
      // Permanently losing focus: No audio focus event will be received. The user must manually trigger the operation to resume playback.
      break;
    case audio.AudioSessionStateChangeHint.AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_DUCK:
      // The system has reduced the volume of all playing audio streams of the application (default to 20% of the normal volume).
      break;
    case audio.AudioSessionStateChangeHint.AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_UNDUCK:
      // The system has restored the volume of all playing audio streams of the application to normal.
      break;
    default:
      break;
  }
};
audioSessionManager.on('audioSessionStateChanged', audioSessionStateChangedCallback);

// Check whether the audio session is activated.
let isActivated = audioSessionManager.isAudioSessionActivated();

if (isActivated) {
  // After the audio session is activated, the application can perform operations such as playing, pausing, stopping, and releasing audio streams.
  // Start multiple audio renderers or other audio playback as needed. The audio playback streams started here no longer hold the focus. The focus is managed by the AudioSession.
  // If multiple audio streams are playing simultaneously, note the AudioSession deactivation timing (all audio playback streams of the application will be released when the AudioSession is deactivated).
}

// Stop listening for AudioSession focus state change events.
audioSessionManager.off('audioSessionStateChanged', audioSessionStateChangedCallback);

// Deactivate the AudioSession, that is, release the focus and stop all audio playback streams of the application.
audioSessionManager.deactivateAudioSession().then(() => {
  console.info('Succeeded in deactivating audio session.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to deactivate audio session. Code: ${err.code}, message: ${err.message}\`);
});
