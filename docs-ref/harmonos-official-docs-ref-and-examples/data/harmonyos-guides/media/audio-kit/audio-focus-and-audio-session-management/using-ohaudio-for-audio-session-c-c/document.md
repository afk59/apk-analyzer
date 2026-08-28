# Using OHAudio for Audio Session (C/C++)

In the scenario where multiple audio streams are concurrently playing, the system has preset a [default audio focus strategy](../introduction-to-audio-focus/document.md#audio-focus-strategy) for unified audio focus management of all streams (including playback and recording).

An application can use an audio session provided by the audio session manager to actively manage the audio focus. Specifically, it can customize an audio focus strategy and determine the timing for releasing the audio focus, thereby meeting its specific service needs.

This document mainly introduces the usage and precautions of the AudioSession-related C APIs. For more information about audio focus and audio sessions, see [Introduction to Audio Focus](../introduction-to-audio-focus/document.md) and [Audio Session Management](../audio-session-management/document.md).

#### Prerequisites

To use the audio session manager provided by OHAudio, add the corresponding header file.

## Linking the Dynamic Library in the CMake Script

target\_link\_libraries(sample PUBLIC libohaudio.so)

## Adding a Header File

Include the [native\_audio\_session\_manager.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-session-manager-h) header file so that the application can use the functions related to audio playback.

#include <ohaudio/native\_audio\_session\_manager.h>

#### Obtaining an Audio Session Manager

Create an [OH\_AudioSessionManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio-oh-audiosessionmanager) instance. Before using any APIs of OH\_AudioSessionManager, you must use [OH\_AudioManager\_GetAudioSessionManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-session-manager-h#oh_audiomanager_getaudiosessionmanager) to obtain an OH\_AudioSessionManager instance.

OH\_AudioSessionManager \*audioSessionManager;
OH\_AudioManager\_GetAudioSessionManager(&audioSessionManager);

#### Activating an Audio Session

Call [OH\_AudioSessionManager\_ActivateAudioSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-session-manager-h#oh_audiosessionmanager_activateaudiosession) to activate an audio session.

During the activation, specify an [audio session strategy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio-oh-audiosession-strategy). The strategy contains the [OH\_AudioSession\_ConcurrencyMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-session-manager-h#oh_audiosession_concurrencymode) parameter, which is used to declare the audio concurrency strategy.

OH\_AudioSession\_Strategy strategy = {CONCURRENCY\_MIX\_WITH\_OTHERS};

OH\_AudioSessionManager\_ActivateAudioSession(audioSessionManager, &strategy);

#### Checking Whether an Audio Session Is Activated

Call [OH\_AudioSessionManager\_IsAudioSessionActivated](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-session-manager-h#oh_audiosessionmanager_isaudiosessionactivated) to check whether an audio session is activated.

bool isActivated = OH\_AudioSessionManager\_IsAudioSessionActivated(audioSessionManager);

#### Deactivating an Audio Session

Call [OH\_AudioSessionManager\_DeactivateAudioSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-session-manager-h#oh_audiosessionmanager_deactivateaudiosession) to deactivate an audio session.

OH\_AudioSessionManager\_DeactivateAudioSession(audioSessionManager);

#### Listening for Audio Session Deactivation Events

When using the audio session, you are advised to listen for the [OH\_AudioSession\_DeactivatedEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio-oh-audiosession-deactivatedevent) event.

When an audio session is deactivated (not proactively), the application receives [OH\_AudioSession\_DeactivatedEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio-oh-audiosession-deactivatedevent), which contains [OH\_AudioSession\_DeactivatedReason](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-session-manager-h#oh_audiosession_deactivatedreason).

Upon this event, the application can perform operations based on service requirements, for example, releasing resources or reactivating the audio session.

## Defining a Callback

int32\_t MyAudioSessionDeactivatedCallback(OH\_AudioSession\_DeactivatedEvent event)
{
  switch(event.reason) {
    case DEACTIVATED\_LOWER\_PRIORITY:
      // The application focus is preempted.
      return 0;
    case DEACTIVATED\_TIMEOUT:
      // A timeout error occurs.
      return 0;
  }
}

## Registering a Callback to Listen for Audio Session Deactivation Events

Call [OH\_AudioSessionManager\_RegisterSessionDeactivatedCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-session-manager-h#oh_audiosessionmanager_registersessiondeactivatedcallback) to register a callback to listen for audio session deactivation events.

OH\_AudioSessionManager\_RegisterSessionDeactivatedCallback(audioSessionManager, MyAudioSessionDeactivatedCallback);

## Unregistering the Callback Used to Listen for Audio Session Deactivation Events

Call [OH\_AudioSessionManager\_UnregisterSessionDeactivatedCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-session-manager-h#oh_audiosessionmanager_unregistersessiondeactivatedcallback) to cancel listening for audio session deactivation events.

OH\_AudioSessionManager\_UnregisterSessionDeactivatedCallback(audioSessionManager, MyAudioSessionDeactivatedCallback);

**Below is a comprehensive example of creating, activating, and listening for an audio session:**

Refer to the sample code below to complete the process of creating, activating, and listening of an audio session.

#include <cstdint>
#include "ohaudio/native\_audio\_session\_manager.h"

int32\_t MyAudioSessionDeactivatedCallback(OH\_AudioSession\_DeactivatedEvent event)
{
  switch(event.reason) {
    case DEACTIVATED\_LOWER\_PRIORITY:
      // The application focus is preempted.
      return 0;
    case DEACTIVATED\_TIMEOUT:
      // A timeout error occurs.
      return 0;
  }
}

OH\_AudioSessionManager \*audioSessionManager;

// Create an audio session manager.
OH\_AudioCommon\_Result resultManager = OH\_AudioManager\_GetAudioSessionManager(&audioSessionManager);

OH\_AudioSession\_Strategy strategy = {CONCURRENCY\_MIX\_WITH\_OTHERS};

// Set an audio concurrency mode and activate an audio session.
OH\_AudioCommon\_Result resultActivate = OH\_AudioSessionManager\_ActivateAudioSession(audioSessionManager, &strategy);

// Check whether the audio session is activated.
bool isActivated = OH\_AudioSessionManager\_IsAudioSessionActivated(audioSessionManager);

// Listen for audio session deactivation events.
OH\_AudioCommon\_Result resultRegister = OH\_AudioSessionManager\_RegisterSessionDeactivatedCallback(audioSessionManager, MyAudioSessionDeactivatedCallback);

// After the audio session is activated, the application can perform operations such as playing, pausing, stopping, and releasing audio streams.

// Cancel listening for audio session deactivation events.
OH\_AudioCommon\_Result resultUnregister = OH\_AudioSessionManager\_UnregisterSessionDeactivatedCallback(audioSessionManager, MyAudioSessionDeactivatedCallback);

// Deactivate the audio session.
OH\_AudioCommon\_Result resultDeactivate = OH\_AudioSessionManager\_DeactivateAudioSession(audioSessionManager);

#### Requesting Focus by Setting Audio Session Scene Parameters

The application requests focus using an audio session. Call [OH\_AudioSessionManager\_SetScene](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-session-manager-h#oh_audiosessionmanager_setscene) to set the scene parameters, and then call [OH\_AudioSessionManager\_ActivateAudioSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-session-manager-h#oh_audiosessionmanager_activateaudiosession) to activate the audio session.

OH\_AudioSessionManager\_SetScene(audioSessionManager, AUDIO\_SESSION\_SCENE\_MEDIA);

OH\_AudioSession\_Strategy strategy = {CONCURRENCY\_MIX\_WITH\_OTHERS};

OH\_AudioSessionManager\_ActivateAudioSession(audioSessionManager, &strategy);

#### Listening for Audio Session Focus State Change events

Listen for audio session focus state changes through [OH\_AudioSession\_StateChangedEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio-oh-audiosession-statechangedevent).

**Below is a comprehensive example of requesting focus for an audio session and listening for focus change events:**

OH\_AudioSessionManager \*audioSessionManager;

// Create an audio session manager.
OH\_AudioCommon\_Result resultManager = OH\_AudioManager\_GetAudioSessionManager(&audioSessionManager);

void AudioSessionStateChangedCallback(OH\_AudioSession\_StateChangedEvent event)
{
  switch(event.stateChangeHint) {
    case AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_PAUSE:
      // The system has paused the audio stream (focus is temporarily lost). To ensure state consistency, the application needs to switch to the audio paused state.
      // Temporarily losing focus: When other audio streams release focus, the application will receive a resume event and can resume playback.
      break;
    case AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_RESUME:
      // The system has resumed the audio session.
      break;
    case AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_STOP:
      // The system has stopped the audio stream (focus is permanently lost). To ensure state consistency, the application should switch to the audio paused state.
      // Permanently losing focus: No audio focus event will be received. The user must manually trigger the operation to resume playback.
      break;
    case AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_TIME\_OUT\_STOP:
      // The system has stopped the audio session (permanently losing focus) due to inactivity. The application should switch to the audio paused state.
      // Permanently losing focus: No audio focus event will be received. The user must manually trigger the operation to resume playback.
      break;
    case AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_DUCK:
      // The system has ducked the volume down (to 20% of the normal volume by default).
      break;
    case AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_UNDUCK:
      // The system has restored the audio volume to normal.
      break;
    default:
      break;
  }
}

OH\_AudioCommon\_Result result = OH\_AudioSessionManager\_RegisterStateChangeCallback(audioSessionManager, AudioSessionStateChangedCallback);

// In this example, AUDIO\_SESSION\_SCENE\_MEDIA is selected. You can change the session scene as needed.
OH\_AudioSessionManager\_SetScene(audioSessionManager, AUDIO\_SESSION\_SCENE\_MEDIA);

// In this example, CONCURRENCY\_MIX\_WITH\_OTHERS is selected. You can change the strategy as needed.
OH\_AudioSession\_Strategy strategy = {CONCURRENCY\_MIX\_WITH\_OTHERS};

result = OH\_AudioSessionManager\_ActivateAudioSession(audioSessionManager, &strategy);

// Start multiple audio renderers or other audio playback as needed.

result = OH\_AudioSessionManager\_DeactivateAudioSession(audioSessionManager);

result = OH\_AudioSessionManager\_UnregisterStateChangeCallback(audioSessionManager, AudioSessionStateChangedCallback);
