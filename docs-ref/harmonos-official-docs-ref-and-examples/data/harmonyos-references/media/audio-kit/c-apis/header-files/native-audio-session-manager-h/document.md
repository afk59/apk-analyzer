# native\_audio\_session\_manager.h

#### Overview

The file declares the functions related to an audio session manager.

You can call the functions to create an audio session manager, activate or deactivate an audio session, check whether an audio session is activated, and listen for audio session deactivation events.

**File to include**: <ohaudio/native\_audio\_session\_manager.h>

**Library**: libohaudio.so

**System capability**: SystemCapability.Multimedia.Audio.Core

**Since**: 12

**Related module**: [OHAudio](../../modules/ohaudio/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioSession\_Strategy](../../structs/oh-audiosession-strategy/document.md) | OH\_AudioSession\_Strategy | Describes the audio session strategy. |
| [OH\_AudioSession\_DeactivatedEvent](../../structs/oh-audiosession-deactivatedevent/document.md) | OH\_AudioSession\_DeactivatedEvent | Describes the event indicating that an audio session is deactivated. |
| [OH\_AudioSession\_StateChangedEvent](../../structs/oh-audiosession-statechangedevent/document.md) | OH\_AudioSession\_StateChangedEvent | Describes the event indicating that the audio session state changes. |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) | OH\_AudioSessionManager | Describes an audio session manager, which is used to manage audio sessions. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioSession\_ConcurrencyMode](#oh_audiosession_concurrencymode) | OH\_AudioSession\_ConcurrencyMode | Enumerates the audio concurrency modes. |
| [OH\_AudioSession\_Scene](#oh_audiosession_scene) | OH\_AudioSession\_Scene | Enumerates the audio session scenes. |
| [OH\_AudioSession\_StateChangeHint](#oh_audiosession_statechangehint) | OH\_AudioSession\_StateChangeHint | Enumerates the hints for audio session state changes. |
| [OH\_AudioSession\_OutputDeviceChangeRecommendedAction](#oh_audiosession_outputdevicechangerecommendedaction) | OH\_AudioSession\_OutputDeviceChangeRecommendedAction | Enumerates the recommended actions to take after an output device changes. |
| [OH\_AudioSession\_DeactivatedReason](#oh_audiosession_deactivatedreason) | OH\_AudioSession\_DeactivatedReason | Enumerates the reasons for deactivating an audio session. |
| [OH\_AudioSession\_BluetoothAndNearlinkPreferredRecordCategory](#oh_audiosession_bluetoothandnearlinkpreferredrecordcategory) | OH\_AudioSession\_BluetoothAndNearlinkPreferredRecordCategory | Enumerates the preferred device categories available for recording with Bluetooth or NearLink. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_AudioSession\_StateChangedCallback)(OH\_AudioSession\_StateChangedEvent event)](#oh_audiosession_statechangedcallback) | OH\_AudioSession\_StateChangedCallback | Defines a function pointer to the callback used to listen for audio session state change events. |
| [typedef void (\*OH\_AudioSession\_AvailableDeviceChangedCallback)(OH\_AudioDevice\_ChangeType type, OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray)](#oh_audiosession_availabledevicechangedcallback) | OH\_AudioSession\_AvailableDeviceChangedCallback | Defines a pointer to the callback that returns the changed audio device descriptor (possibly multiple descriptors). |
| [typedef void (\*OH\_AudioSession\_CurrentInputDeviceChangedCallback)(OH\_AudioDeviceDescriptorArray \*devices, OH\_AudioStream\_DeviceChangeReason changeReason)](#oh_audiosession_currentinputdevicechangedcallback) | OH\_AudioSession\_CurrentInputDeviceChangedCallback | Defines a function pointer to the callback used to listen for the current input device change events. |
| [typedef void (\*OH\_AudioSession\_CurrentOutputDeviceChangedCallback)(OH\_AudioDeviceDescriptorArray \*devices, OH\_AudioStream\_DeviceChangeReason changeReason, OH\_AudioSession\_OutputDeviceChangeRecommendedAction recommendedAction)](#oh_audiosession_currentoutputdevicechangedcallback) | OH\_AudioSession\_CurrentOutputDeviceChangedCallback | Defines a function pointer to the callback used to listen for the current output device change events. |
| [typedef int32\_t (\*OH\_AudioSession\_DeactivatedCallback)(OH\_AudioSession\_DeactivatedEvent event)](#oh_audiosession_deactivatedcallback) | OH\_AudioSession\_DeactivatedCallback | Defines a function pointer to the callback used to listen for audio session deactivation events. |
| [OH\_AudioCommon\_Result OH\_AudioManager\_GetAudioSessionManager(OH\_AudioSessionManager \*\*audioSessionManager)](#oh_audiomanager_getaudiosessionmanager) | \- | Obtains an OH\_AudioSessionManager instance. Before using the features related to the audio session manager, you must obtain an OH\_AudioSessionManager instance. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_ActivateAudioSession(OH\_AudioSessionManager \*audioSessionManager, const OH\_AudioSession\_Strategy \*strategy)](#oh_audiosessionmanager_activateaudiosession) | \- | Activates an audio session. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_DeactivateAudioSession(OH\_AudioSessionManager \*audioSessionManager)](#oh_audiosessionmanager_deactivateaudiosession) | \- | Deactivates an audio session. |
| [bool OH\_AudioSessionManager\_IsAudioSessionActivated(OH\_AudioSessionManager \*audioSessionManager)](#oh_audiosessionmanager_isaudiosessionactivated) | \- | Checks whether an audio session is activated. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_RegisterSessionDeactivatedCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_DeactivatedCallback callback)](#oh_audiosessionmanager_registersessiondeactivatedcallback) | \- | Registers a callback to listen for audio session deactivation events. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_UnregisterSessionDeactivatedCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_DeactivatedCallback callback)](#oh_audiosessionmanager_unregistersessiondeactivatedcallback) | \- | Unregisters the callback used to listen for audio session deactivation events. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_SetScene(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_Scene scene)](#oh_audiosessionmanager_setscene) | \- | Sets an audio session scene. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_RegisterStateChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_StateChangedCallback callback)](#oh_audiosessionmanager_registerstatechangecallback) | \- | Registers a callback to listen for audio session state change events. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_UnregisterStateChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_StateChangedCallback callback)](#oh_audiosessionmanager_unregisterstatechangecallback) | \- | Unregisters the callback used to listen for audio session state change events. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_SetDefaultOutputDevice(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDevice\_Type deviceType)](#oh_audiosessionmanager_setdefaultoutputdevice) | \- | Sets the default audio output device. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_GetDefaultOutputDevice(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDevice\_Type \*deviceType)](#oh_audiosessionmanager_getdefaultoutputdevice) | \- | Obtains the default audio output device set by calling [OH\_AudioSessionManager\_SetDefaultOutputDevice](#oh_audiosessionmanager_setdefaultoutputdevice). |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_ReleaseDevices(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray)](#oh_audiosessionmanager_releasedevices) | \- | Releases audio devices available for an audio routing manager. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_RegisterCurrentOutputDeviceChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_CurrentOutputDeviceChangedCallback callback)](#oh_audiosessionmanager_registercurrentoutputdevicechangecallback) | \- | Registers a callback to listen for the current output device change events. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_UnregisterCurrentOutputDeviceChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_CurrentOutputDeviceChangedCallback callback)](#oh_audiosessionmanager_unregistercurrentoutputdevicechangecallback) | \- | Unregisters the callback used to listen for the current output device change events. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_GetAvailableDevices(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDevice\_Usage deviceUsage, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)](#oh_audiosessionmanager_getavailabledevices) | \- | Obtains the available audio devices. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_RegisterAvailableDevicesChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDevice\_Usage deviceUsage, OH\_AudioSession\_AvailableDeviceChangedCallback callback)](#oh_audiosessionmanager_registeravailabledeviceschangecallback) | \- | Registers a callback to listen for available device change events. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_UnregisterAvailableDevicesChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_AvailableDeviceChangedCallback callback)](#oh_audiosessionmanager_unregisteravailabledeviceschangecallback) | \- | Unregisters the callback used to listen for available device change events. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_SelectMediaInputDevice(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDeviceDescriptor \*deviceDescriptor)](#oh_audiosessionmanager_selectmediainputdevice) | \- | 
Selects a media input device. This function is not suitable for call recording, meaning it does not apply to situations where [SourceType](../native-audiostream-base-h/document.md#oh_audiostream_sourcetype) is **SOURCE\_TYPE\_VOICE\_COMMUNICATION**.

When there is a concurrent recording stream with higher priority, the actual input device used by the application may differ from the one selected.

Applications can call [OH\_AudioSessionManager\_RegisterCurrentInputDeviceChangeCallback](#oh_audiosessionmanager_registercurrentinputdevicechangecallback) to register a callback to listen for the actual input device.

 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_GetSelectedMediaInputDevice(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDeviceDescriptor \*\*audioDeviceDescriptor)](#oh_audiosessionmanager_getselectedmediainputdevice) | \- | Obtains the media input device set by calling [OH\_AudioSessionManager\_SelectMediaInputDevice](#oh_audiosessionmanager_selectmediainputdevice). |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_SetBluetoothAndNearlinkPreferredRecordCategory(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_BluetoothAndNearlinkPreferredRecordCategory category)](#oh_audiosessionmanager_setbluetoothandnearlinkpreferredrecordcategory) | \- | 

Sets the preferred device category for recording with Bluetooth or NearLink. Applications can set this category before connecting to Bluetooth or NearLink devices, and the system prioritizes using the device for recording when the device is connected.

When there is a concurrent recording stream with higher priority, the actual input device used by the application may differ from the set preferred device.

Applications can call [OH\_AudioSessionManager\_RegisterCurrentInputDeviceChangeCallback](#oh_audiosessionmanager_registercurrentinputdevicechangecallback) to register a callback to listen for the actual input device.

 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_GetBluetoothAndNearlinkPreferredRecordCategory(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_BluetoothAndNearlinkPreferredRecordCategory \*category)](#oh_audiosessionmanager_getbluetoothandnearlinkpreferredrecordcategory) | \- | Obtains the preferred device category for recording with Bluetooth or NearLink. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_RegisterCurrentInputDeviceChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_CurrentInputDeviceChangedCallback callback)](#oh_audiosessionmanager_registercurrentinputdevicechangecallback) | \- | Registers a callback to listen for input device changes of an audio session manager. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_UnregisterCurrentInputDeviceChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_CurrentInputDeviceChangedCallback callback)](#oh_audiosessionmanager_unregistercurrentinputdevicechangecallback) | \- | Unregisters the callback used to listen for input device changes of an audio session manager. |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_ReleaseDevice(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDeviceDescriptor \*audioDeviceDescriptor)](#oh_audiosessionmanager_releasedevice) | \- | Releases an audio device for an audio session manager. |

#### Enum Description

#### \[h2\]OH\_AudioSession\_ConcurrencyMode

enum OH\_AudioSession\_ConcurrencyMode

**Description**

Enumerates the audio concurrency modes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| CONCURRENCY\_DEFAULT = 0 | Uses the system strategy by default. |
| CONCURRENCY\_MIX\_WITH\_OTHERS = 1 | Mixes audio with other applications that are playing audio. |
| CONCURRENCY\_DUCK\_OTHERS = 2 | Lowers the volume of the application that is currently playing the audio. |
| CONCURRENCY\_PAUSE\_OTHERS = 3 | Pauses the application that is currently playing the audio. |

#### \[h2\]OH\_AudioSession\_Scene

enum OH\_AudioSession\_Scene

**Description**

Enumerates the audio session scenes.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| AUDIO\_SESSION\_SCENE\_MEDIA = 0 | Media audio session. |
| AUDIO\_SESSION\_SCENE\_GAME = 1 | Game audio session. |
| AUDIO\_SESSION\_SCENE\_VOICE\_COMMUNICATION = 2 | VoIP voice call audio session. |

#### \[h2\]OH\_AudioSession\_StateChangeHint

enum OH\_AudioSession\_StateChangeHint

**Description**

Enumerates the hints for audio session state changes.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_RESUME = 0 | A hint is displayed, indicating that the audio session is resuming. The application can proactively trigger operations such as rendering. |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_PAUSE = 1 | A hint is displayed, indicating that the audio session is paused and the audio focus is lost temporarily. When focus is regained, the AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_RESUME event is received. |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_STOP = 2 | A hint is displayed, indicating that the audio session is stopped and the audio focus is lost permanently. |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_TIME\_OUT\_STOP = 3 | A hint is displayed, indicating that the audio session is stopped by the system due to no activity, and the audio focus is lost. |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_DUCK = 4 | A hint is displayed, indicating that audio ducking starts and the audio is played at a lower volume. |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_UNDUCK = 5 | A hint is displayed, indicating that audio ducking ends and the audio is played at the normal volume. |

#### \[h2\]OH\_AudioSession\_OutputDeviceChangeRecommendedAction

enum OH\_AudioSession\_OutputDeviceChangeRecommendedAction

**Description**

Enumerates the recommended actions to take after an output device changes.

Common scenario example: switching between a headset and a loudspeaker device. Upon switching from the loudspeaker device to the headset upon wearing, the system suggests continuing playback and prompts that the application does not need to pause. Upon transitioning from the headset to the loudspeaker device upon removal, the system suggests suspending playback.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| DEVICE\_CHANGE\_RECOMMEND\_TO\_CONTINUE = 0 | Suggests continuing playback. (This event serves as a playback maintenance indication, informing the application that audio playback does not need to stop during this device change. However, it must not be used as a criterion for triggering audio playback.) |
| DEVICE\_CHANGE\_RECOMMEND\_TO\_STOP = 1 | Suggests stopping playback. |

#### \[h2\]OH\_AudioSession\_DeactivatedReason

enum OH\_AudioSession\_DeactivatedReason

**Description**

Enumerates the reasons for deactivating an audio session.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| DEACTIVATED\_LOWER\_PRIORITY = 0 | The application focus is preempted. |
| DEACTIVATED\_TIMEOUT = 1 | The application times out after the stream is stopped. |

#### \[h2\]OH\_AudioSession\_BluetoothAndNearlinkPreferredRecordCategory

enum OH\_AudioSession\_BluetoothAndNearlinkPreferredRecordCategory

**Description**

Enumerates the preferred device categories available for recording with Bluetooth or NearLink.

**Since**: 21

| Enum Item | Description |
| :-- | :-- |
| PREFERRED\_NONE = 0 | No specific device preference. |
| PREFERRED\_DEFAULT = 1 | Prefers using Bluetooth or Nearlink devices for recording; whether to use low-latency or high-quality recording depends on the system. |
| PREFERRED\_LOW\_LATENCY = 2 | Prefers using Bluetooth or NearLink devices in low-latency mode for recording. |
| PREFERRED\_HIGH\_QUALITY = 3 | Prefers using Bluetooth or NearLink devices in high-quality mode for recording. |

#### Function Description

#### \[h2\]OH\_AudioSession\_StateChangedCallback()

typedef void (\*OH\_AudioSession\_StateChangedCallback)(OH\_AudioSession\_StateChangedEvent event)

**Description**

Defines a function pointer to the callback used to listen for audio session state change events.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSession\_StateChangedEvent](../../structs/oh-audiosession-statechangedevent/document.md) event | Event indicating that the audio session state changes. |

#### \[h2\]OH\_AudioSession\_AvailableDeviceChangedCallback()

typedef void (\*OH\_AudioSession\_AvailableDeviceChangedCallback)(OH\_AudioDevice\_ChangeType type, OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray)

**Description**

Defines a pointer to the callback that returns the changed audio device descriptor (possibly multiple descriptors).

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioDevice\_ChangeType](../native-audio-device-base-h/document.md#oh_audiodevice_changetype) type | Device connection status, which can be connected or disconnected. |
| [OH\_AudioDeviceDescriptorArray](../../structs/oh-audiodevicedescriptorarray/document.md) \*audioDeviceDescriptorArray | 
Pointer to the audio device descriptors in the array.

If the pointer is no longer needed, use [OH\_AudioSessionManager\_ReleaseDevices](#oh_audiosessionmanager_releasedevices) to release it.

 |

#### \[h2\]OH\_AudioSession\_CurrentInputDeviceChangedCallback()

typedef void (\*OH\_AudioSession\_CurrentInputDeviceChangedCallback)(OH\_AudioDeviceDescriptorArray \*devices, OH\_AudioStream\_DeviceChangeReason changeReason)

**Description**

Defines a function pointer to the callback used to listen for the current input device change events.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioDeviceDescriptorArray](../../structs/oh-audiodevicedescriptorarray/document.md) \*devices | 
Pointer to the audio device descriptors in the array.

If the pointer is no longer needed, use [OH\_AudioSessionManager\_ReleaseDevices](#oh_audiosessionmanager_releasedevices) to release it.

 |
| [OH\_AudioStream\_DeviceChangeReason](../native-audiostream-base-h/document.md#oh_audiostream_devicechangereason) changeReason | Reason for the device change. |

#### \[h2\]OH\_AudioSession\_CurrentOutputDeviceChangedCallback()

typedef void (\*OH\_AudioSession\_CurrentOutputDeviceChangedCallback)(OH\_AudioDeviceDescriptorArray \*devices, OH\_AudioStream\_DeviceChangeReason changeReason, OH\_AudioSession\_OutputDeviceChangeRecommendedAction recommendedAction)

**Description**

Defines a function pointer to the callback used to listen for the current output device change events.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioDeviceDescriptorArray](../../structs/oh-audiodevicedescriptorarray/document.md) \*devices | Pointer to the audio device descriptors in the array. For details, see [OH\_AudioDeviceDescriptorArray](../../structs/oh-audiodevicedescriptorarray/document.md). Do not release the pointer to the audioDeviceDescriptorArray struct separately. Instead, call [OH\_AudioSessionManager\_ReleaseDevices](#oh_audiosessionmanager_releasedevices) to release the DeviceDescriptor array. |
| [OH\_AudioStream\_DeviceChangeReason](../native-audiostream-base-h/document.md#oh_audiostream_devicechangereason) changeReason | Pointer to [OH\_AudioStream\_DeviceChangeReason](../native-audiostream-base-h/document.md#oh_audiostream_devicechangereason), which is used to receive the device change reason. |
| [OH\_AudioSession\_OutputDeviceChangeRecommendedAction](#oh_audiosession_outputdevicechangerecommendedaction) recommendedAction | Pointer to [OH\_AudioSession\_OutputDeviceChangeRecommendedAction](#oh_audiosession_outputdevicechangerecommendedaction), which is used to receive the recommended action to take after the device change. |

#### \[h2\]OH\_AudioSession\_DeactivatedCallback()

typedef int32\_t (\*OH\_AudioSession\_DeactivatedCallback)(OH\_AudioSession\_DeactivatedEvent event)

**Description**

Defines a function pointer to the callback used to listen for audio session deactivation events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSession\_DeactivatedEvent](../../structs/oh-audiosession-deactivatedevent/document.md) event | Event indicating that an audio session is deactivated. |

#### \[h2\]OH\_AudioManager\_GetAudioSessionManager()

OH\_AudioCommon\_Result OH\_AudioManager\_GetAudioSessionManager(OH\_AudioSessionManager \*\*audioSessionManager)

**Description**

Obtains an OH\_AudioSessionManager instance. Before using the features related to the audio session manager, you must obtain an OH\_AudioSessionManager instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*\*audioSessionManager | Double pointer to the OH\_AudioSessionManager instance obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: System error.

 |

#### \[h2\]OH\_AudioSessionManager\_ActivateAudioSession()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_ActivateAudioSession(OH\_AudioSessionManager \*audioSessionManager, const OH\_AudioSession\_Strategy \*strategy)

**Description**

Activates an audio session.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| const [OH\_AudioSession\_Strategy](../../structs/oh-audiosession-strategy/document.md) \*strategy | Pointer to an audio session strategy, which is an [OH\_AudioSession\_Strategy](../../structs/oh-audiosession-strategy/document.md) struct. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
One of the following return values:

**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **strategy** parameter is invalid.

**AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE**: Invalid state.

 |

#### \[h2\]OH\_AudioSessionManager\_DeactivateAudioSession()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_DeactivateAudioSession(OH\_AudioSessionManager \*audioSessionManager)

**Description**

Deactivates an audio session.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**: The **audioSessionManager** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE**: Invalid state.

 |

#### \[h2\]OH\_AudioSessionManager\_IsAudioSessionActivated()

bool OH\_AudioSessionManager\_IsAudioSessionActivated(OH\_AudioSessionManager \*audioSessionManager)

**Description**

Checks whether an audio session is activated.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for whether the audio session is activated. **true** if activated, **false** otherwise. |

#### \[h2\]OH\_AudioSessionManager\_RegisterSessionDeactivatedCallback()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_RegisterSessionDeactivatedCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_DeactivatedCallback callback)

**Description**

Registers a callback to listen for audio session deactivation events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioSession\_DeactivatedCallback](#oh_audiosession_deactivatedcallback) callback | Callback used to receive the audio session deactivation event. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **callback** parameter is nullptr.

 |

#### \[h2\]OH\_AudioSessionManager\_UnregisterSessionDeactivatedCallback()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_UnregisterSessionDeactivatedCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_DeactivatedCallback callback)

**Description**

Unregisters the callback used to listen for audio session deactivation events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioSession\_DeactivatedCallback](#oh_audiosession_deactivatedcallback) callback | Callback used to receive the audio session deactivation event. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **callback** parameter is nullptr.

 |

#### \[h2\]OH\_AudioSessionManager\_SetScene()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_SetScene(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_Scene scene)

**Description**

Sets an audio session scene.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioSession\_Scene](#oh_audiosession_scene) scene | Pointer to an audio session scene to be set by calling [OH\_AudioSession\_Scene](#oh_audiosession_scene). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **scene** parameter is set to a value outside the valid enumeration range.

**AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE**: The setting is not allowed in the current system state, for example, when the audio session is not ready.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system error occurs, such as an abnormal exit of a system service.

 |

#### \[h2\]OH\_AudioSessionManager\_RegisterStateChangeCallback()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_RegisterStateChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_StateChangedCallback callback)

**Description**

Registers a callback to listen for audio session state change events.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioSession\_StateChangedCallback](#oh_audiosession_statechangedcallback) callback | Callback used to receive the audio session state change event. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **callback** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY**: Memory allocation fails.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system error occurs, such as an abnormal exit of a system service.

 |

#### \[h2\]OH\_AudioSessionManager\_UnregisterStateChangeCallback()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_UnregisterStateChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_StateChangedCallback callback)

**Description**

Unregisters the callback used to listen for audio session state change events.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioSession\_StateChangedCallback](#oh_audiosession_statechangedcallback) callback | Callback used to receive the audio session state change event. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **callback** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system error occurs, such as an abnormal exit of a system service.

 |

#### \[h2\]OH\_AudioSessionManager\_SetDefaultOutputDevice()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_SetDefaultOutputDevice(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDevice\_Type deviceType)

**Description**

Sets the default audio output device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/Is5spB2FRqGn6WRTe-4Hlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062419Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95FBEB036A4406F87CD34FEB93D41FE7867D77D0ED2C8CBF887CD86E1AEDF501)

-   This API is applicable to the following scenarios: If [OH\_AudioSession\_Scene](#oh_audiosession_scene) is set to VoIP, this API takes effect immediately after the audio session is activated. If [OH\_AudioSession\_Scene](#oh_audiosession_scene) is set to non-VoIP, this API does not take effect when the audio session is activated. It takes effect only when [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage) of the started playback is a voice message, VoIP voice call, or VoIP video call. Supported devices include the earpiece, speaker, and system default device.
-   This API can be called at any time after an [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) instance is created. The system records the device set by the application. However, the setting takes effect only after the AudioSession is activated. When the application starts playback, if an external device such as a Bluetooth or wired headset is connected, the system preferentially uses the external device to play sound. Otherwise, the system uses this default device to play sound.

**Device behavior difference**: If the default audio output device is set to earpiece on a device without an earpiece, the speaker will still be used for audio output.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioDevice\_Type](../native-audio-device-base-h/document.md#oh_audiodevice_type) deviceType | 
Device type. For details about the available options, see [OH\_AudioDevice\_Type](../native-audio-device-base-h/document.md#oh_audiodevice_type). The device types that can be set are as follows:

**AUDIO\_DEVICE\_TYPE\_EARPIECE**: earpiece.

**AUDIO\_DEVICE\_TYPE\_SPEAKER**: speaker.

**AUDIO\_DEVICE\_TYPE\_DEFAULT**: system default device.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The deviceType parameter is out of the OH\_AudioDevice\_Type range.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system error occurs, such as an abnormal exit of a system service.

 |

#### \[h2\]OH\_AudioSessionManager\_GetDefaultOutputDevice()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_GetDefaultOutputDevice(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDevice\_Type \*deviceType)

**Description**

Obtains the default audio output device set by [OH\_AudioSessionManager\_SetDefaultOutputDevice](#oh_audiosessionmanager_setdefaultoutputdevice).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioDevice\_Type](../native-audio-device-base-h/document.md#oh_audiodevice_type) \*deviceType | 
Pointer to the device type. For details about the available options, see [OH\_AudioDevice\_Type](../native-audio-device-base-h/document.md#oh_audiodevice_type). The returned device types are as follows:

**AUDIO\_DEVICE\_TYPE\_EARPIECE**: earpiece.

**AUDIO\_DEVICE\_TYPE\_SPEAKER**: speaker.

**AUDIO\_DEVICE\_TYPE\_DEFAULT**: system default device.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **deviceType** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE**: The default device type cannot be obtained in the current system state, for example, when the audio session is not ready.

 |

#### \[h2\]OH\_AudioSessionManager\_ReleaseDevices()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_ReleaseDevices(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray)

**Description**

Releases audio devices available for an audio routing manager.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioDeviceDescriptorArray](../../structs/oh-audiodevicedescriptorarray/document.md) \*audioDeviceDescriptorArray | Pointer to the audio device descriptors in the array to be released. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **audioDeviceDescriptorArray** parameter is nullptr.

 |

#### \[h2\]OH\_AudioSessionManager\_RegisterCurrentOutputDeviceChangeCallback()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_RegisterCurrentOutputDeviceChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_CurrentOutputDeviceChangedCallback callback)

**Description**

Registers a callback to listen for the current output device change events.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioSession\_CurrentOutputDeviceChangedCallback](#oh_audiosession_currentoutputdevicechangedcallback) callback | Callback used to return the audio device change information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **callback** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY**: Memory allocation fails.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system error occurs, such as an abnormal exit of a system service.

 |

#### \[h2\]OH\_AudioSessionManager\_UnregisterCurrentOutputDeviceChangeCallback()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_UnregisterCurrentOutputDeviceChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_CurrentOutputDeviceChangedCallback callback)

**Description**

Unregisters the callback used to listen for the current output device change events.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioSession\_CurrentOutputDeviceChangedCallback](#oh_audiosession_currentoutputdevicechangedcallback) callback | Callback used to return the audio device change information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **callback** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system error occurs, such as an abnormal exit of a system service.

 |

#### \[h2\]OH\_AudioSessionManager\_GetAvailableDevices()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_GetAvailableDevices(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDevice\_Usage deviceUsage, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)

**Description**

Obtains the available audio devices.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioDevice\_Usage](../native-audio-device-base-h/document.md#oh_audiodevice_usage) deviceUsage | Type of audio device. |
| [OH\_AudioDeviceDescriptorArray](../../structs/oh-audiodevicedescriptorarray/document.md) \*\*audioDeviceDescriptorArray | 
Pointer to the audio device descriptors in the array.

If the pointer is no longer needed, use [OH\_AudioSessionManager\_ReleaseDevices](#oh_audiosessionmanager_releasedevices) to release it.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **deviceUsage** parameter is invalid.

3\. The **audioDeviceDescriptorArray** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system error occurs, such as an abnormal exit of a system service.

 |

#### \[h2\]OH\_AudioSessionManager\_RegisterAvailableDevicesChangeCallback()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_RegisterAvailableDevicesChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDevice\_Usage deviceUsage, OH\_AudioSession\_AvailableDeviceChangedCallback callback)

**Description**

Registers a callback to listen for available device change events.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioDevice\_Usage](../native-audio-device-base-h/document.md#oh_audiodevice_usage) deviceUsage | Type of audio device. |
| [OH\_AudioSession\_AvailableDeviceChangedCallback](#oh_audiosession_availabledevicechangedcallback) callback | Callback used to return the available audio device change information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **deviceUsage** parameter is set to an invalid value.

3\. The **callback** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system error occurs, such as an abnormal exit of a system service.

 |

#### \[h2\]OH\_AudioSessionManager\_UnregisterAvailableDevicesChangeCallback()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_UnregisterAvailableDevicesChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_AvailableDeviceChangedCallback callback)

**Description**

Unregisters the callback used to listen for available device change events.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioSession\_AvailableDeviceChangedCallback](#oh_audiosession_availabledevicechangedcallback) callback | Callback used to return the available audio device change information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **callback** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system error occurs, such as an abnormal exit of a system service.

 |

#### \[h2\]OH\_AudioSessionManager\_SelectMediaInputDevice()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_SelectMediaInputDevice(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDeviceDescriptor \*deviceDescriptor)

**Description**

Selects a media input device. This function is not suitable for call recording, meaning it does not apply to situations where [SourceType](../native-audiostream-base-h/document.md#oh_audiostream_sourcetype) is **SOURCE\_TYPE\_VOICE\_COMMUNICATION**.

When there is a concurrent recording stream with higher priority, the actual input device used by the application may differ from the one selected.

Applications can call [OH\_AudioSessionManager\_RegisterCurrentInputDeviceChangeCallback](#oh_audiosessionmanager_registercurrentinputdevicechangecallback) to register a callback to listen for the actual input device.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioDeviceDescriptor](../../structs/oh-audiodevicedescriptor/document.md) \*deviceDescriptor | 
Pointer to the target device, which must be in the array returned by [OH\_AudioSessionManager\_GetAvailableDevices](#oh_audiosessionmanager_getavailabledevices).

If nullptr is passed, the system clears the previous setting.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**: The **audioSessionManager** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system error occurs, such as an abnormal exit of a system service.

 |

#### \[h2\]OH\_AudioSessionManager\_GetSelectedMediaInputDevice()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_GetSelectedMediaInputDevice(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDeviceDescriptor \*\*audioDeviceDescriptor)

**Description**

Obtains the media input device set by calling [OH\_AudioSessionManager\_SelectMediaInputDevice](#oh_audiosessionmanager_selectmediainputdevice).

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioDeviceDescriptor](../../structs/oh-audiodevicedescriptor/document.md) \*\*audioDeviceDescriptor | 
Media device set by [OH\_AudioSessionManager\_SelectMediaInputDevice](#oh_audiosessionmanager_selectmediainputdevice). If no device has been specified, the device of the type AUDIO\_DEVICE\_TYPE\_INVALID is returned.

Use [OH\_AudioSessionManager\_ReleaseDevice](#oh_audiosessionmanager_releasedevice) to release the audioDeviceDescriptor pointer if the pointer is no longer needed.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **audioDeviceDescriptor** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system error occurs, such as an abnormal exit of a system service.

 |

#### \[h2\]OH\_AudioSessionManager\_SetBluetoothAndNearlinkPreferredRecordCategory()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_SetBluetoothAndNearlinkPreferredRecordCategory(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_BluetoothAndNearlinkPreferredRecordCategory category)

**Description**

Sets the preferred device category for recording with Bluetooth or NearLink. Applications can set this category before connecting to Bluetooth or NearLink devices, and the system prioritizes using the device for recording when the device is connected.

When there is a concurrent recording stream with higher priority, the actual input device used by the application may differ from the set preferred device.

Applications can call [OH\_AudioSessionManager\_RegisterCurrentInputDeviceChangeCallback](#oh_audiosessionmanager_registercurrentinputdevicechangecallback) to register a callback to listen for the actual input device.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioSession\_BluetoothAndNearlinkPreferredRecordCategory](#oh_audiosession_bluetoothandnearlinkpreferredrecordcategory) category | Preferred device category for recording with Bluetooth or NearLink. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **category** parameter is incorrect.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system error occurs, such as an abnormal exit of a system service.

 |

#### \[h2\]OH\_AudioSessionManager\_GetBluetoothAndNearlinkPreferredRecordCategory()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_GetBluetoothAndNearlinkPreferredRecordCategory(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_BluetoothAndNearlinkPreferredRecordCategory \*category)

**Description**

Obtains the preferred device category for recording with Bluetooth or NearLink.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioSession\_BluetoothAndNearlinkPreferredRecordCategory](#oh_audiosession_bluetoothandnearlinkpreferredrecordcategory) \*category | Pointer to the preferred device category for recording with Bluetooth or NearLink. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **category** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system error occurs, such as an abnormal exit of a system service.

 |

#### \[h2\]OH\_AudioSessionManager\_RegisterCurrentInputDeviceChangeCallback()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_RegisterCurrentInputDeviceChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_CurrentInputDeviceChangedCallback callback)

**Description**

Registers a callback to listen for input device changes of an audio session manager.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioSession\_CurrentInputDeviceChangedCallback](#oh_audiosession_currentinputdevicechangedcallback) callback | Callback used to return the input audio device change information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **callback** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY**: The memory is insufficient.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system error occurs, such as an abnormal exit of a system service.

 |

#### \[h2\]OH\_AudioSessionManager\_UnregisterCurrentInputDeviceChangeCallback()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_UnregisterCurrentInputDeviceChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_CurrentInputDeviceChangedCallback callback)

**Description**

Unregisters the callback used to listen for input device changes of an audio session manager.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioSession\_CurrentInputDeviceChangedCallback](#oh_audiosession_currentinputdevicechangedcallback) callback | Callback used to return the input audio device change information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **callback** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system error occurs, such as an abnormal exit of a system service.

 |

#### \[h2\]OH\_AudioSessionManager\_ReleaseDevice()

OH\_AudioCommon\_Result OH\_AudioSessionManager\_ReleaseDevice(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDeviceDescriptor \*audioDeviceDescriptor)

**Description**

Releases an audio device for an audio session manager.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSessionManager](../../structs/oh-audiosessionmanager/document.md) \*audioSessionManager | Pointer to an audio session manager instance, which is created by calling [OH\_AudioManager\_GetAudioSessionManager](#oh_audiomanager_getaudiosessionmanager). |
| [OH\_AudioDeviceDescriptor](../../structs/oh-audiodevicedescriptor/document.md) \*audioDeviceDescriptor | Pointer to the audio device descriptor to be released. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioSessionManager** parameter is nullptr.

2\. The **audioDeviceDescriptor** parameter is nullptr.

 |
