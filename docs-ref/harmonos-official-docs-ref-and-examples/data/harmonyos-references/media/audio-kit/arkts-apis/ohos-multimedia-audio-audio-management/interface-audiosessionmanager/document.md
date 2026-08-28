# Interface (AudioSessionManager)

This interface implements audio session management.

Before calling any API in AudioSessionManager, you must use [getSessionManager](../interface-audiomanager/document.md#getsessionmanager12) to obtain an AudioSessionManager instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/6tFKmVWWQzi5800XeEsKGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=419AEC35089F16AA95037174293DFB634FFA010C605783E148A40A8211288B36)

-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 12.

#### Modules to Import

import { audio } from '@kit.AudioKit';

#### activateAudioSession12+

activateAudioSession(strategy: AudioSessionStrategy): Promise<void>

Activates an audio session. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strategy | [AudioSessionStrategy](../interfaces-others/document.md#audiosessionstrategy12) | Yes | Audio session strategy. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters unspecified. 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |
| 6800301 | System error. Returned by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let strategy: audio.AudioSessionStrategy = {
  concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY\_MIX\_WITH\_OTHERS
};

audioSessionManager.activateAudioSession(strategy).then(() => {
  console.info('activateAudioSession SUCCESS');
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### deactivateAudioSession12+

deactivateAudioSession(): Promise<void>

Deactivates this audio session. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800301 | System error. Returned by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioSessionManager.deactivateAudioSession().then(() => {
  console.info('deactivateAudioSession SUCCESS');
}).catch((err: BusinessError) => {
  console.error(\`ERROR: ${err}\`);
});

#### isAudioSessionActivated12+

isAudioSessionActivated(): boolean

Checks whether this audio session is activated.

**System capability**: SystemCapability.Multimedia.Audio.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the audio session is activated. **true** if activated, **false** otherwise. |

**Example**

let isActivated = audioSessionManager.isAudioSessionActivated();

#### on('audioSessionDeactivated')12+

on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void

Subscribes to the audio session deactivation event, which is triggered when an audio session is deactivated. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'audioSessionDeactivated'** is triggered when the audio session is deactivated. |
| callback | Callback<[AudioSessionDeactivatedEvent](../interfaces-others/document.md#audiosessiondeactivatedevent12)\> | Yes | Callback used to return the reason why the audio session is deactivated. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters unspecified. 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

audioSessionManager.on('audioSessionDeactivated',
  (audioSessionDeactivatedEvent: audio.AudioSessionDeactivatedEvent) => {
  console.info(\`reason of audioSessionDeactivated: ${audioSessionDeactivatedEvent.reason} \`);
});

#### off('audioSessionDeactivated')12+

off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void

Unsubscribes from the audio session deactivation event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'audioSessionDeactivated'** is triggered when the audio session is deactivated. |
| callback | Callback<[AudioSessionDeactivatedEvent](../interfaces-others/document.md#audiosessiondeactivatedevent12)\> | No | Callback used to return the reason why the audio session is deactivated. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioSessionManager.off('audioSessionDeactivated');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let audioSessionDeactivatedCallback = (audioSessionDeactivatedEvent: audio.AudioSessionDeactivatedEvent) => {
  console.info(\`reason of audioSessionDeactivated: ${audioSessionDeactivatedEvent.reason} \`);
};

audioSessionManager.on('audioSessionDeactivated', audioSessionDeactivatedCallback);

audioSessionManager.off('audioSessionDeactivated', audioSessionDeactivatedCallback);

#### setAudioSessionScene20+

setAudioSessionScene(scene: AudioSessionScene): void

Sets an audio session scene.

**System capability**: SystemCapability.Multimedia.Audio.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scene | [AudioSessionScene](../enums/document.md#audiosessionscene20) | Yes | Audio session scene. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |
| 6800103 | Operation not permit at current state. |
| 6800301 | Audio client call audio service error, System error. |

**Example**

audioSessionManager.setAudioSessionScene(audio.AudioSessionScene.AUDIO\_SESSION\_SCENE\_MEDIA);

#### on('audioSessionStateChanged')20+

on(type: 'audioSessionStateChanged', callback: Callback<AudioSessionStateChangedEvent>): void

Subscribes to the audio session state change event, which is triggered when the audio session focus is changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'audioSessionStateChanged'** is triggered when the audio session state is changed. |
| callback | Callback<[AudioSessionStateChangedEvent](../interfaces-others/document.md#audiosessionstatechangedevent20)\> | Yes | Callback used to return the audio session change information. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |
| 6800102 | Allocate memory failed. |
| 6800301 | Audio client call audio service error, System error. |

**Example**

audioSessionManager.on('audioSessionStateChanged', (audioSessionStateChangedEvent: audio.AudioSessionStateChangedEvent) => {
  console.info(\`hint of audioSessionStateChanged: ${audioSessionStateChangedEvent.stateChangeHint} \`);
});

#### off('audioSessionStateChanged')20+

off(type: 'audioSessionStateChanged', callback?: Callback<AudioSessionStateChangedEvent>): void

Unsubscribes from the audio session state change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'audioSessionStateChanged'** is triggered when the audio session state is changed. |
| callback | Callback<[AudioSessionStateChangedEvent](../interfaces-others/document.md#audiosessionstatechangedevent20)\> | No | Callback used to return the audio session change information. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

**Example**

// Cancel all subscriptions to the event.
audioSessionManager.off('audioSessionStateChanged');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let audioSessionStateChangedCallback = (audioSessionStateChangedEvent: audio.AudioSessionStateChangedEvent) => {
  console.info(\`hint of audioSessionStateChanged: ${audioSessionStateChangedEvent.stateChangeHint} \`);
};

audioSessionManager.on('audioSessionStateChanged', audioSessionStateChangedCallback);

audioSessionManager.off('audioSessionStateChanged', audioSessionStateChangedCallback);

#### setDefaultOutputDevice20+

setDefaultOutputDevice(deviceType: DeviceType): Promise<void>

Sets the default audio output device. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/raHKlpitSSOHRAC1akl6zg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EE5FA643A6020DD2AA5546CD52FC7068ADF4D67554D34C7C08694F7C18CB910)

-   This API applies to the following scenario: When [AudioSessionScene](../enums/document.md#audiosessionscene20) is set to **VoIP**, the setting takes effect immediately after the AudioSession is activated. For non-VoIP scenarios, the setting does not take effect upon AudioSession activation. Instead, the setting applies when [StreamUsage](../enums/document.md#streamusage) for playback is voice message, VoIP voice call, or VoIP video call. Supported devices include the earpiece, speaker, and system default device.
-   This API can be called at any time after an AudioSessionManager instance is created. The system records the device set by the application. However, the setting takes effect only after the AudioSession is activated. When the application starts playing, if an external device like Bluetooth headsets or wired headsets is connected, the system prioritizes audio output through the external device. Otherwise, the system uses the device set by the application.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceType | [DeviceType](../enums/document.md#devicetype) | Yes | 
Device type.

The options are **EARPIECE**, **SPEAKER**, and **DEFAULT**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800102 | Allocate memory failed. Return by promise. |
| 6800301 | Audio client call audio service error, System error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioSessionManager.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
  console.info('setDefaultOutputDevice Success!');
}).catch((err: BusinessError) => {
  console.error(\`setDefaultOutputDevice Fail: ${err}\`);
});

#### getDefaultOutputDevice20+

getDefaultOutputDevice(): DeviceType

Obtains the default audio output device set by calling [setDefaultOutputDevice](#setdefaultoutputdevice20).

**System capability**: SystemCapability.Multimedia.Audio.Device

**Return value**

| Type | Description |
| :-- | :-- |
| DeviceType | 
Device type.

The options are **EARPIECE**, **SPEAKER**, and **DEFAULT**.

 |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |
| 6800103 | Operation not permit at current state. Return by promise. |

**Example**

let deviceType = audioSessionManager.getDefaultOutputDevice();

#### on('currentOutputDeviceChanged')20+

on(type: 'currentOutputDeviceChanged', callback: Callback<CurrentOutputDeviceChangedEvent>): void

Subscribes to the current output device change event, which is triggered when the current output device is changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'currentOutputDeviceChanged'** is triggered when the current output device is changed. |
| callback | Callback<[CurrentOutputDeviceChangedEvent](../interfaces-others/document.md#currentoutputdevicechangedevent20)\> | Yes | Callback used to return the information about the current output device. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |
| 6800102 | Allocate memory failed. |
| 6800301 | Audio client call audio service error, System error. |

**Example**

import { audio } from '@kit.AudioKit';

let currentOutputDeviceChangedCallback = (currentOutputDeviceChangedEvent: audio.CurrentOutputDeviceChangedEvent) => {
  console.info(\`reason of audioSessionStateChanged: ${currentOutputDeviceChangedEvent.changeReason} \`);
};

audioSessionManager.on('currentOutputDeviceChanged', currentOutputDeviceChangedCallback);

#### off('currentOutputDeviceChanged')20+

off(type: 'currentOutputDeviceChanged', callback?: Callback<CurrentOutputDeviceChangedEvent>): void

Unsubscribes from the current output device change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'currentOutputDeviceChanged'** is triggered when the current output device is changed. |
| callback | Callback<[CurrentOutputDeviceChangedEvent](../interfaces-others/document.md#currentoutputdevicechangedevent20)\> | No | Callback used to return the information about the current output device. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

**Example**

// Cancel all subscriptions to the event.
audioSessionManager.off('currentOutputDeviceChanged');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let currentOutputDeviceChangedCallback = (currentOutputDeviceChangedEvent: audio.CurrentOutputDeviceChangedEvent) => {
  console.info(\`reason of audioSessionStateChanged: ${currentOutputDeviceChangedEvent.changeReason} \`);
};

audioSessionManager.on('currentOutputDeviceChanged', currentOutputDeviceChangedCallback);

audioSessionManager.off('currentOutputDeviceChanged', currentOutputDeviceChangedCallback);

#### getAvailableDevices21+

getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors

Obtains the available audio devices.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceUsage | [DeviceUsage](../enums/document.md#deviceusage12) | Yes | Audio device type (classified by usage). |

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors) | Device list. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data: audio.AudioDeviceDescriptors = audioSessionManager.getAvailableDevices(audio.DeviceUsage.MEDIA\_OUTPUT\_DEVICES);
  console.info('Succeeded in doing getAvailableDevices.');
} catch (err) {
  let error = err as BusinessError;
   console.error(\`Failed to getAvailableDevices. Code: ${error.code}, message: ${error.message}\`);
}

#### on('availableDeviceChange')21+

on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void

Subscribes to the event indicating that the connection status of an available audio device is changed.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'availableDeviceChange'** is triggered when the connection status of available audio devices is changed. |
| deviceUsage | [DeviceUsage](../enums/document.md#deviceusage12) | Yes | Audio device type (classified by usage). |
| callback | Callback<[DeviceChangeAction](../interfaces-others/document.md#devicechangeaction)\> | Yes | Callback used to return the available device change details. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

**Example**

audioSessionManager.on('availableDeviceChange', audio.DeviceUsage.MEDIA\_INPUT\_DEVICES, (deviceChanged: audio.DeviceChangeAction) => {
  console.info('device change type : ' + deviceChanged.type);
  console.info('device descriptor size : ' + deviceChanged.deviceDescriptors.length);
  console.info('device change descriptor : ' + deviceChanged.deviceDescriptors\[0\].deviceRole);
  console.info('device change descriptor : ' + deviceChanged.deviceDescriptors\[0\].deviceType);
});

#### off('availableDeviceChange')21+

off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void

Unsubscribes from the event indicating that the connection status of an available audio device is changed.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'availableDeviceChange'** is triggered when the connection status of available audio devices is changed. |
| callback | Callback<[DeviceChangeAction](../interfaces-others/document.md#devicechangeaction)\> | No | Callback used to return the available device change details. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800301 | Audio client call audio service error, System error. |

**Example**

// Cancel all subscriptions to the event.
audioSessionManager.off('availableDeviceChange');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let availableDeviceChangeCallback = (deviceChanged: audio.DeviceChangeAction) => {
  console.info('device change type : ' + deviceChanged.type);
  console.info('device descriptor size : ' + deviceChanged.deviceDescriptors.length);
  console.info('device change descriptor : ' + deviceChanged.deviceDescriptors\[0\].deviceRole);
  console.info('device change descriptor : ' + deviceChanged.deviceDescriptors\[0\].deviceType);
};

audioSessionManager.on('availableDeviceChange', audio.DeviceUsage.MEDIA\_INPUT\_DEVICES, availableDeviceChangeCallback);

audioSessionManager.off('availableDeviceChange', availableDeviceChangeCallback);

#### selectMediaInputDevice21+

selectMediaInputDevice(inputAudioDevice: AudioDeviceDescriptor): Promise<void>

Selects a media input device. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/9P9eNrmaSwyk7w5fKYES-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E04D4C613C4A71612848AAD6949154FD4294BA15AC7F50E7EA272A59CC71284)

-   This API is not suitable for VoIP call recording; that is, it does not apply to scenarios where [SourceType](../enums/document.md#sourcetype8) is **SOURCE\_TYPE\_VOICE\_COMMUNICATION**.
-   Before calling this API, call [getAvailableDevices](#getavailabledevices21) to query the list of available input devices and select an input device from the list.
-   If there are recording streams of other applications with higher priorities in the system, the actual input device used will follow the input device selected by these applications.
-   Applications can listen for the [currentInputDeviceChanged](#oncurrentinputdevicechanged21) event to find out the actual input device being used.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inputAudioDevice | [AudioDeviceDescriptor](../interfaces-others/document.md#audiodevicedescriptor) | Yes | Media input device. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed, for example, the selected device does not exist. |
| 6800301 | Audio client call audio service error, System error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data: audio.AudioDeviceDescriptors = audioSessionManager.getAvailableDevices(audio.DeviceUsage.MEDIA\_OUTPUT\_DEVICES);
  console.info('Succeeded in doing getAvailableDevices.');

  if (data\[0\]) {
    audioSessionManager.selectMediaInputDevice(data\[0\]).then(() => {
      console.info('Succeeded in doing selectMediaInputDevice.');
    }).catch((selectErr: BusinessError) => {
      console.error(\`Failed to selectMediaInputDevice. Code: ${selectErr.code}, message: ${selectErr.message}\`);
    });
  }
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to getAvailableDevices. Code: ${error.code}, message: ${error.message}\`);
}

#### getSelectedMediaInputDevice21+

getSelectedMediaInputDevice(): AudioDeviceDescriptor

Obtains the media input device set by calling [selectMediaInputDevice](#selectmediainputdevice21). If no device has been specified, the device with **deviceType** set to **INVALID** is returned.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioDeviceDescriptor](../interfaces-others/document.md#audiodevicedescriptor) | Media input device. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800301 | Audio client call audio service error, System error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let device: audio.AudioDeviceDescriptor = audioSessionManager.getSelectedMediaInputDevice();
  console.info('Succeeded in doing getSelectedMediaInputDevice.');
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to getSelectedMediaInputDevice. Code: ${error.code}, message: ${error.message}\`);
}

#### clearSelectedMediaInputDevice21+

clearSelectedMediaInputDevice(): Promise<void>

Clears the media input device set by calling [selectMediaInputDevice](#selectmediainputdevice21). This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800301 | Audio client call audio service error, System error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioSessionManager.clearSelectedMediaInputDevice().then(() => {
  console.info('Succeeded in doing clearSelectedMediaInputDevice.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to clearSelectedMediaInputDevice. Code: ${err.code}, message: ${err.message}\`);
});

#### setBluetoothAndNearlinkPreferredRecordCategory21+

setBluetoothAndNearlinkPreferredRecordCategory(category: BluetoothAndNearlinkPreferredRecordCategory): Promise<void>

Sets the preferred device category for recording with Bluetooth or NearLink. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/rpNoP2_BRBySJ4ETiybRHA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D6089498EA3FF0C920548CA45DB6483EB50BA4D41C5BFD7528ABED4D38903E9)

-   Applications can set this category before connecting to Bluetooth or NearLink devices, and the system prioritizes using the device for recording when the device is connected.
-   If there are recording streams of other applications with higher priorities in the system, the actual input device used will follow the input device selected by these applications.
-   Applications can listen for the [currentInputDeviceChanged](#oncurrentinputdevicechanged21) event to find out the actual input device being used.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| category | [BluetoothAndNearlinkPreferredRecordCategory](../enums/document.md#bluetoothandnearlinkpreferredrecordcategory21) | Yes | Preferred device category for recording with Bluetooth or NearLink. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const category = audio.BluetoothAndNearlinkPreferredRecordCategory.PREFERRED\_LOW\_LATENCY;
audioSessionManager.setBluetoothAndNearlinkPreferredRecordCategory(category).then(() => {
  console.info('Succeeded in doing setBluetoothAndNearlinkPreferredRecordCategory.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to setBluetoothAndNearlinkPreferredRecordCategory. Code: ${err.code}, message: ${err.message}\`);
});

#### getBluetoothAndNearlinkPreferredRecordCategory21+

getBluetoothAndNearlinkPreferredRecordCategory(): BluetoothAndNearlinkPreferredRecordCategory

Obtains the preferred device category for recording with Bluetooth or NearLink, which is set by calling [setBluetoothAndNearlinkPreferredRecordCategory](#setbluetoothandnearlinkpreferredrecordcategory21).

**System capability**: SystemCapability.Multimedia.Audio.Device

**Return value**

| Type | Description |
| :-- | :-- |
| [BluetoothAndNearlinkPreferredRecordCategory](../enums/document.md#bluetoothandnearlinkpreferredrecordcategory21) | Preferred device category for recording with Bluetooth or NearLink. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800301 | Audio client call audio service error, System error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let category: audio.BluetoothAndNearlinkPreferredRecordCategory = audioSessionManager.getBluetoothAndNearlinkPreferredRecordCategory();
  console.info('Succeeded in doing getBluetoothAndNearlinkPreferredRecordCategory.');
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to getBluetoothAndNearlinkPreferredRecordCategory. Code: ${error.code}, message: ${error.message}\`);
}

#### on('currentInputDeviceChanged')21+

on(type: 'currentInputDeviceChanged', callback: Callback<CurrentInputDeviceChangedEvent>): void

Subscribes to the current input device change event, which is triggered when the current input device is changed.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'currentInputDeviceChanged'** is triggered when the current input device is changed. |
| callback | Callback<[CurrentInputDeviceChangedEvent](../interfaces-others/document.md#currentinputdevicechangedevent21)\> | Yes | Callback used to return the information about the current input device. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

**Example**

import { audio } from '@kit.AudioKit';

let currentInputDeviceChangedCallback = (currentInputDeviceChangedEvent: audio.CurrentInputDeviceChangedEvent) => {
  console.info(\`reason of currentInputDeviceChanged: ${currentInputDeviceChangedEvent.changeReason} \`);
};

audioSessionManager.on('currentInputDeviceChanged', currentInputDeviceChangedCallback);

#### off('currentInputDeviceChanged')21+

off(type: 'currentInputDeviceChanged', callback?: Callback<CurrentInputDeviceChangedEvent>): void

Unsubscribes from the current input device change event.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'currentInputDeviceChanged'** is triggered when the current input device is changed. |
| callback | Callback<[CurrentInputDeviceChangedEvent](../interfaces-others/document.md#currentinputdevicechangedevent21)\> | No | Callback used to return the information about the current input device. |

**Error codes**

For details about the error codes, see [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6800301 | Audio client call audio service error, System error. |

**Example**

// Cancel all subscriptions to the event.
audioSessionManager.off('currentInputDeviceChanged');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let currentInputDeviceChangedCallback = (currentInputDeviceChangedEvent: audio.CurrentInputDeviceChangedEvent) => {
  console.info(\`reason of currentInputDeviceChanged: ${currentInputDeviceChangedEvent.changeReason} \`);
};

audioSessionManager.on('currentInputDeviceChanged', currentInputDeviceChangedCallback);

audioSessionManager.off('currentInputDeviceChanged', currentInputDeviceChangedCallback);
