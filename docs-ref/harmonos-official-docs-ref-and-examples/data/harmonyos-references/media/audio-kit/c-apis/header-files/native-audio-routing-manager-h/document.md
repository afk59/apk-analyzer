# native\_audio\_routing\_manager.h

#### Overview

The file declares the functions related to an audio routing manager.

You can use the functions to create an audio routing manager, register and deregister a callback to listen for device connection status changes, and release devices.

**File to include**: <ohaudio/native\_audio\_routing\_manager.h>

**Library**: libohaudio.so

**System capability**: SystemCapability.Multimedia.Audio.Core

**Since**: 12

**Related module**: [OHAudio](../../modules/ohaudio/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioRoutingManager](../../structs/oh-audioroutingmanager/document.md) | OH\_AudioRoutingManager | Describes an audio routing manager, which is used for audio routing management. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef int32\_t (\*OH\_AudioRoutingManager\_OnDeviceChangedCallback)(OH\_AudioDevice\_ChangeType type, OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray)](#oh_audioroutingmanager_ondevicechangedcallback) | OH\_AudioRoutingManager\_OnDeviceChangedCallback | Defines a pointer to the callback that returns the changed audio device descriptor (possibly multiple descriptors). |
| [OH\_AudioCommon\_Result OH\_AudioManager\_GetAudioRoutingManager(OH\_AudioRoutingManager \*\*audioRoutingManager)](#oh_audiomanager_getaudioroutingmanager) | \- | Obtains the handle to an audio routing manager. The handle should be set as the first parameter in the routing-related functions. |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_GetDevices(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioDevice\_Flag deviceFlag, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)](#oh_audioroutingmanager_getdevices) | \- | Obtains available devices based on the device flag. |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_GetAvailableDevices(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioDevice\_Usage deviceUsage, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)](#oh_audioroutingmanager_getavailabledevices) | \- | Obtains the available audio devices. |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_GetPreferredOutputDevice(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioStream\_Usage streamUsage, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)](#oh_audioroutingmanager_getpreferredoutputdevice) | \- | Obtains the output device with the highest priority based on the usage scenario of an audio output stream. |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_GetPreferredInputDevice(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioStream\_SourceType sourceType, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)](#oh_audioroutingmanager_getpreferredinputdevice) | \- | Obtains the input device with the highest priority based on the usage scenario of an audio input stream. |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_RegisterDeviceChangeCallback(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioDevice\_Flag deviceFlag, OH\_AudioRoutingManager\_OnDeviceChangedCallback callback)](#oh_audioroutingmanager_registerdevicechangecallback) | \- | Registers a callback to listen for device changes of an audio routing manager. |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_UnregisterDeviceChangeCallback(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioRoutingManager\_OnDeviceChangedCallback callback)](#oh_audioroutingmanager_unregisterdevicechangecallback) | \- | Unregisters the callback used to listen for device changes of an audio routing manager. |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_ReleaseDevices(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray)](#oh_audioroutingmanager_releasedevices) | \- | Releases audio devices available for an audio routing manager. |
| [typedef void (\*OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback)(OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray, OH\_AudioDevice\_BlockStatus status, void \*userData)](#oh_audioroutingmanager_ondeviceblockstatuscallback) | OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback | Defines a pointer to the callback that returns the blocked status of one or more audio devices. |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_IsMicBlockDetectionSupported(OH\_AudioRoutingManager \*audioRoutingManager, bool \*supported)](#oh_audioroutingmanager_ismicblockdetectionsupported) | \- | Checks whether the current device supports microphone blocking detection. |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_SetMicBlockStatusCallback(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback callback, void \*userData)](#oh_audioroutingmanager_setmicblockstatuscallback) | \- | 
Sets a callback function to be invoked when the microphone's blocked status is changed.

Before using this function, check whether the current device supports microphone blocking detection. The application receives a callback only when the microphone is used for recording and the microphone's blocked status changes. Currently, this function takes effect only for the microphone on the local device.

 |

#### Function Description

#### \[h2\]OH\_AudioRoutingManager\_OnDeviceChangedCallback()

typedef int32\_t (\*OH\_AudioRoutingManager\_OnDeviceChangedCallback)(OH\_AudioDevice\_ChangeType type, OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray
)

**Description**

Defines a pointer to the callback that returns the changed audio device descriptor (possibly multiple descriptors).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioDevice\_ChangeType](../native-audio-device-base-h/document.md#oh_audiodevice_changetype) type | Device connection status, which is [OH\_AudioDevice\_ChangeType](../native-audio-device-base-h/document.md#oh_audiodevice_changetype). The status can be either connected or disconnected. |
| [OH\_AudioDeviceDescriptorArray](../../structs/oh-audiodevicedescriptorarray/document.md) \*audioDeviceDescriptorArray | Pointer to the audio device descriptors in the array. For details, see [OH\_AudioDeviceDescriptorArray](../../structs/oh-audiodevicedescriptorarray/document.md). Do not release the pointer to the audioDeviceDescriptorArray struct separately. Instead, call [OH\_AudioRoutingManager\_ReleaseDevices](#oh_audioroutingmanager_releasedevices) to release the DeviceDescriptor array. |

#### \[h2\]OH\_AudioManager\_GetAudioRoutingManager()

OH\_AudioCommon\_Result OH\_AudioManager\_GetAudioRoutingManager(OH\_AudioRoutingManager \*\*audioRoutingManager)

**Description**

Obtains the handle to an audio routing manager. The handle should be set as the first parameter in the routing-related functions.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRoutingManager](../../structs/oh-audioroutingmanager/document.md) \*\*audioRoutingManager | Handle to the audio routing manager, which is obtained by calling [OH\_AudioManager\_GetAudioRoutingManager](#oh_audiomanager_getaudioroutingmanager). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | **AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully. |

#### \[h2\]OH\_AudioRoutingManager\_GetDevices()

OH\_AudioCommon\_Result OH\_AudioRoutingManager\_GetDevices(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioDevice\_Flag deviceFlag, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)

**Description**

Obtains available devices based on the device flag.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRoutingManager](../../structs/oh-audioroutingmanager/document.md) \*audioRoutingManager | Handle to the audio routing manager, which is obtained by calling [OH\_AudioManager\_GetAudioRoutingManager](#oh_audiomanager_getaudioroutingmanager). |
| [OH\_AudioDevice\_Flag](../native-audio-device-base-h/document.md#oh_audiodevice_flag) deviceFlag | Device flag, which is used to filter the target device. |
| [OH\_AudioDeviceDescriptorArray](../../structs/oh-audiodevicedescriptorarray/document.md) \*\*audioDeviceDescriptorArray | Double pointer to the audio device descriptors in the array. Do not release the pointer to the audioDeviceDescriptorArray struct separately. Instead, call [OH\_AudioRoutingManager\_ReleaseDevices](#oh_audioroutingmanager_releasedevices) to release the DeviceDescriptor array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioRoutingManager** parameter is nullptr.

2\. The **deviceFlag** parameter is set to an invalid value.

3\. The **audioDeviceDescriptorArray** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY**: The memory is insufficient.

 |

#### \[h2\]OH\_AudioRoutingManager\_GetAvailableDevices()

OH\_AudioCommon\_Result OH\_AudioRoutingManager\_GetAvailableDevices(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioDevice\_Usage deviceUsage, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)

**Description**

Obtains the available audio devices.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRoutingManager](../../structs/oh-audioroutingmanager/document.md) \*audioRoutingManager | Handle to the audio routing manager, which is obtained by calling [OH\_AudioManager\_GetAudioRoutingManager](#oh_audiomanager_getaudioroutingmanager). |
| [OH\_AudioDevice\_Usage](../native-audio-device-base-h/document.md#oh_audiodevice_usage) deviceUsage | Usage scenario of the audio device. For details about the available options, see [OH\_AudioDevice\_Usage](../native-audio-device-base-h/document.md#oh_audiodevice_usage). |
| [OH\_AudioDeviceDescriptorArray](../../structs/oh-audiodevicedescriptorarray/document.md) \*\*audioDeviceDescriptorArray | Double pointer to the audio device descriptors in the array. Do not release the pointer to the audioDeviceDescriptorArray struct separately. Instead, call [OH\_AudioRoutingManager\_ReleaseDevices](#oh_audioroutingmanager_releasedevices) to release the DeviceDescriptor array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioRoutingManager** parameter is nullptr.

2\. The **deviceUsage** parameter is invalid.

3\. The **audioDeviceDescriptorArray** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY**: The memory is insufficient.

 |

#### \[h2\]OH\_AudioRoutingManager\_GetPreferredOutputDevice()

OH\_AudioCommon\_Result OH\_AudioRoutingManager\_GetPreferredOutputDevice(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioStream\_Usage streamUsage, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)

**Description**

Obtains the output device with the highest priority based on the usage scenario of an audio output stream.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRoutingManager](../../structs/oh-audioroutingmanager/document.md) \*audioRoutingManager | Handle to the audio routing manager, which is obtained by calling [OH\_AudioManager\_GetAudioRoutingManager](#oh_audiomanager_getaudioroutingmanager). |
| [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage) streamUsage | Usage scenario of the audio output stream. For details about the available options, see [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage). |
| [OH\_AudioDeviceDescriptorArray](../../structs/oh-audiodevicedescriptorarray/document.md) \*\*audioDeviceDescriptorArray | Double pointer to the audio device descriptors in the array. Do not release the pointer to the audioDeviceDescriptorArray struct separately. Instead, call [OH\_AudioRoutingManager\_ReleaseDevices](#oh_audioroutingmanager_releasedevices) to release the DeviceDescriptor array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioRoutingManager** parameter is nullptr.

2\. The **streamUsage** parameter is invalid.

3\. The **audioDeviceDescriptorArray** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY**: The memory is insufficient.

 |

#### \[h2\]OH\_AudioRoutingManager\_GetPreferredInputDevice()

OH\_AudioCommon\_Result OH\_AudioRoutingManager\_GetPreferredInputDevice(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioStream\_SourceType sourceType, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)

**Description**

Obtains the input device with the highest priority based on the usage scenario of an audio input stream.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRoutingManager](../../structs/oh-audioroutingmanager/document.md) \*audioRoutingManager | Handle to the audio routing manager, which is obtained by calling [OH\_AudioManager\_GetAudioRoutingManager](#oh_audiomanager_getaudioroutingmanager). |
| [OH\_AudioStream\_SourceType](../native-audiostream-base-h/document.md#oh_audiostream_sourcetype) sourceType | Usage scenario of the audio input stream. For details about the available options, see [OH\_AudioStream\_SourceType](../native-audiostream-base-h/document.md#oh_audiostream_sourcetype). |
| [OH\_AudioDeviceDescriptorArray](../../structs/oh-audiodevicedescriptorarray/document.md) \*\*audioDeviceDescriptorArray | Double pointer to the audio device descriptors in the array. Do not release the pointer to the audioDeviceDescriptorArray struct separately. Instead, call [OH\_AudioRoutingManager\_ReleaseDevices](#oh_audioroutingmanager_releasedevices) to release the DeviceDescriptor array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioRoutingManager** parameter is nullptr.

2\. The **sourceType** parameter is invalid.

3\. The **audioDeviceDescriptorArray** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY**: The memory is insufficient.

 |

#### \[h2\]OH\_AudioRoutingManager\_RegisterDeviceChangeCallback()

OH\_AudioCommon\_Result OH\_AudioRoutingManager\_RegisterDeviceChangeCallback(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioDevice\_Flag deviceFlag, OH\_AudioRoutingManager\_OnDeviceChangedCallback callback)

**Description**

Registers a callback to listen for device changes of an audio routing manager.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRoutingManager](../../structs/oh-audioroutingmanager/document.md) \*audioRoutingManager | Handle to the audio routing manager, which is obtained by calling [OH\_AudioManager\_GetAudioRoutingManager](#oh_audiomanager_getaudioroutingmanager). |
| [OH\_AudioDevice\_Flag](../native-audio-device-base-h/document.md#oh_audiodevice_flag) deviceFlag | Device flag. |
| [OH\_AudioRoutingManager\_OnDeviceChangedCallback](#oh_audioroutingmanager_ondevicechangedcallback) callback | Callback function used to return the changed audio device descriptor. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioRoutingManager** parameter is nullptr.

2\. The **deviceFlag** parameter is set to an invalid value.

3\. The **callback** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRoutingManager\_UnregisterDeviceChangeCallback()

OH\_AudioCommon\_Result OH\_AudioRoutingManager\_UnregisterDeviceChangeCallback(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioRoutingManager\_OnDeviceChangedCallback callback)

**Description**

Unregisters the callback used to listen for device changes of an audio routing manager.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRoutingManager](../../structs/oh-audioroutingmanager/document.md) \*audioRoutingManager | Handle to the audio routing manager, which is obtained by calling [OH\_AudioManager\_GetAudioRoutingManager](#oh_audiomanager_getaudioroutingmanager). |
| [OH\_AudioRoutingManager\_OnDeviceChangedCallback](#oh_audioroutingmanager_ondevicechangedcallback) callback | Callback function used to return the changed audio device descriptor. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioRoutingManager** parameter is nullptr.

2\. The **callback** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRoutingManager\_ReleaseDevices()

OH\_AudioCommon\_Result OH\_AudioRoutingManager\_ReleaseDevices(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray)

**Description**

Releases audio devices available for an audio routing manager.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRoutingManager](../../structs/oh-audioroutingmanager/document.md) \*audioRoutingManager | Handle to the audio routing manager, which is obtained by calling [OH\_AudioManager\_GetAudioRoutingManager](#oh_audiomanager_getaudioroutingmanager). |
| [OH\_AudioDeviceDescriptorArray](../../structs/oh-audiodevicedescriptorarray/document.md) \*audioDeviceDescriptorArray | Pointer to the array of audio devices, which are obtained by calling [OH\_AudioRoutingManager\_GetDevices](#oh_audioroutingmanager_getdevices). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioRoutingManager** parameter is nullptr.

2\. The **audioDeviceDescriptorArray** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback()

typedef void (\*OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback)(OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray, OH\_AudioDevice\_BlockStatus status, void \*userData)

**Description**

Defines a pointer to the callback that returns the blocked status of one or more audio devices.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioDeviceDescriptorArray](../../structs/oh-audiodevicedescriptorarray/document.md) \*audioDeviceDescriptorArray | Pointer to the array of audio devices, which are obtained by calling [OH\_AudioRoutingManager\_GetDevices](#oh_audioroutingmanager_getdevices). Do not release the pointer to the **audioDeviceDescriptorArray** struct separately. Instead, call [OH\_AudioRoutingManager\_ReleaseDevices](#oh_audioroutingmanager_releasedevices) to release the **DeviceDescriptor** array. |
| [OH\_AudioDevice\_BlockStatus](../native-audio-device-base-h/document.md#oh_audiodevice_blockstatus) status | Blocked status of the audio device. |
| void \*userData | Pointer to user data. |

#### \[h2\]OH\_AudioRoutingManager\_IsMicBlockDetectionSupported()

OH\_AudioCommon\_Result OH\_AudioRoutingManager\_IsMicBlockDetectionSupported(OH\_AudioRoutingManager \*audioRoutingManager, bool \*supported)

**Description**

Checks whether the current device supports microphone blocking detection.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRoutingManager](../../structs/oh-audioroutingmanager/document.md) \*audioRoutingManager | Handle to the audio routing manager, which is obtained by calling [OH\_AudioManager\_GetAudioRoutingManager](#oh_audiomanager_getaudioroutingmanager). |
| bool \*supported | Check result for the support of microphone blocking detection. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioRoutingManager** parameter is nullptr.

2\. The **supported** parameter is nullptr.

 |

#### \[h2\]OH\_AudioRoutingManager\_SetMicBlockStatusCallback()

OH\_AudioCommon\_Result OH\_AudioRoutingManager\_SetMicBlockStatusCallback(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback callback, void \*userData)

**Description**

Sets a callback function to be invoked when the microphone's blocked status is changed.

Before using this function, check whether the current device supports microphone blocking detection. The application receives a callback only when the microphone is used for recording and the microphone's blocked status changes. Currently, this function takes effect only for the microphone on the local device.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioRoutingManager](../../structs/oh-audioroutingmanager/document.md) \*audioRoutingManager | Handle to the audio routing manager, which is obtained by calling [OH\_AudioManager\_GetAudioRoutingManager](#oh_audiomanager_getaudioroutingmanager). |
| [OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback](#oh_audioroutingmanager_ondeviceblockstatuscallback) callback | Pointer to the [OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback](#oh_audioroutingmanager_ondeviceblockstatuscallback) callback, which is used to return the blocked status. |
| void \*userData | Pointer to user data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioRoutingManager** parameter is nullptr.

2\. The **callback** parameter is nullptr.

 |
