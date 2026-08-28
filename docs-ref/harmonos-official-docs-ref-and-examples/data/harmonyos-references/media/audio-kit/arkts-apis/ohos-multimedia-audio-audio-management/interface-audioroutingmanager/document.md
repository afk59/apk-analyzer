# Interface (AudioRoutingManager)

This interface implements audio routing management.

Before calling any API in AudioRoutingManager, you must use [getRoutingManager](../interface-audiomanager/document.md#getroutingmanager9) to obtain an AudioRoutingManager instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/ryF5wgDlRWyz_Rc8iRKd0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062417Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C52A5C7D2B8E7262994B8135FA7F8B18E7EA986E69929343A71B785F86BB180E)

-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 9.

#### Modules to Import

import { audio } from '@kit.AudioKit';

#### getDevices9+

getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void

Obtains the audio devices with a specific flag. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceFlag | [DeviceFlag](../enums/document.md#deviceflag) | Yes | Audio device flag. |
| callback | AsyncCallback<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the audio devices obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRoutingManager.getDevices(audio.DeviceFlag.OUTPUT\_DEVICES\_FLAG, (err: BusinessError, audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
  if (err) {
    console.error(\`Failed to get devices. Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`Succeeded in getting devices, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.\`);
  }
});

#### getDevices9+

getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>

Obtains the audio devices with a specific flag. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceFlag | [DeviceFlag](../enums/document.md#deviceflag) | Yes | Audio device flag. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors)\> | Promise used to return the device list. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRoutingManager.getDevices(audio.DeviceFlag.OUTPUT\_DEVICES\_FLAG).then((audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
  console.info(\`Succeeded in getting devices, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get devices. Code: ${err.code}, message: ${err.message}\`);
});

#### getDevicesSync10+

getDevicesSync(deviceFlag: DeviceFlag): AudioDeviceDescriptors

Obtains the audio devices with a specific flag. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceFlag | [DeviceFlag](../enums/document.md#deviceflag) | Yes | Audio device flag. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors) | Device list. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioDeviceDescriptors = audioRoutingManager.getDevicesSync(audio.DeviceFlag.OUTPUT\_DEVICES\_FLAG);
  console.info(\`Succeeded in getting devices, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to get devices. Code: ${error.code}, message: ${error.message}\`);
}

#### isMicBlockDetectionSupported13+

isMicBlockDetectionSupported(): Promise<boolean>

Checks whether the current device supports microphone blocking detection. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result, indicating the support for microphone blocking detection. **true** if supported, **false** otherwise. |

**Example**

audioRoutingManager.isMicBlockDetectionSupported().then((value: boolean) => {
  console.info(\`Query whether microphone block detection is supported on current device result is ${value}.\`);
});

#### on('micBlockStatusChanged')13+

on(type: 'micBlockStatusChanged', callback: Callback<DeviceBlockStatusInfo>): void

Subscribes to the microphone blocked status change event. This API uses an asynchronous callback to return the result.

Before using this API, check whether the current device supports microphone blocking detection. This event is triggered when the microphone blocked status changes during recording. Currently, this API takes effect only for the microphone on the local device.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'micBlockStatusChanged'** is triggered when the microphone blocked status is changed. |
| callback | Callback<[DeviceBlockStatusInfo](../interfaces-others/document.md#deviceblockstatusinfo13)\> | Yes | Callback used to return the microphone blocked status and device information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

// Before the subscription, check whether the current device supports detection.
audioRoutingManager.isMicBlockDetectionSupported().then((value: boolean) => {
  console.info(\`Query whether microphone block detection is supported on current device result is ${value}.\`);
  if (value) {
    audioRoutingManager.on('micBlockStatusChanged', (micBlockStatusChanged: audio.DeviceBlockStatusInfo) => {
      console.info(\`block status : ${micBlockStatusChanged.blockStatus} \`);
    });
  }
});

#### off('micBlockStatusChanged')13+

off(type: 'micBlockStatusChanged', callback?: Callback<DeviceBlockStatusInfo>): void

Unsubscribes from the microphone blocked status change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'micBlockStatusChanged'** is triggered when the microphone blocked status is changed. |
| callback | Callback<[DeviceBlockStatusInfo](../interfaces-others/document.md#deviceblockstatusinfo13)\> | No | Callback used to return the microphone blocked status and device information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioRoutingManager.off('micBlockStatusChanged');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let micBlockStatusCallback = (micBlockStatusChanged: audio.DeviceBlockStatusInfo) => {
  console.info(\`block status : ${micBlockStatusChanged.blockStatus} \`);
};

audioRoutingManager.on('micBlockStatusChanged', micBlockStatusCallback);

audioRoutingManager.off('micBlockStatusChanged', micBlockStatusCallback);

#### on('deviceChange')9+

on(type: 'deviceChange', deviceFlag: DeviceFlag, callback: Callback<DeviceChangeAction>): void

Subscribes to the event indicating that the connection status of an audio device is changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'deviceChange'** is triggered when the connection status of an audio device is changed. |
| deviceFlag | [DeviceFlag](../enums/document.md#deviceflag) | Yes | Audio device flag. |
| callback | Callback<[DeviceChangeAction](../interfaces-others/document.md#devicechangeaction)\> | Yes | Callback used to return the device change details. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

audioRoutingManager.on('deviceChange', audio.DeviceFlag.OUTPUT\_DEVICES\_FLAG, (deviceChanged: audio.DeviceChangeAction) => {
  console.info('device change type : ' + deviceChanged.type);
  console.info('device descriptor size : ' + deviceChanged.deviceDescriptors.length);
  console.info('device change descriptor : ' + deviceChanged.deviceDescriptors\[0\].deviceRole);
  console.info('device change descriptor : ' + deviceChanged.deviceDescriptors\[0\].deviceType);
});

#### off('deviceChange')9+

off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void

Unsubscribes from the event indicating that the connection status of an audio device is changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'deviceChange'** is triggered when the connection status of an audio device is changed. |
| callback | Callback<[DeviceChangeAction](../interfaces-others/document.md#devicechangeaction)\> | No | Callback used to return the device change details. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioRoutingManager.off('deviceChange');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let deviceChangeCallback = (deviceChanged: audio.DeviceChangeAction) => {
  console.info('device change type : ' + deviceChanged.type);
  console.info('device descriptor size : ' + deviceChanged.deviceDescriptors.length);
  console.info('device change descriptor : ' + deviceChanged.deviceDescriptors\[0\].deviceRole);
  console.info('device change descriptor : ' + deviceChanged.deviceDescriptors\[0\].deviceType);
};

audioRoutingManager.on('deviceChange', audio.DeviceFlag.OUTPUT\_DEVICES\_FLAG, deviceChangeCallback);

audioRoutingManager.off('deviceChange', deviceChangeCallback);

#### setCommunicationDevice9+

setCommunicationDevice(deviceType: CommunicationDeviceType, active: boolean, callback: AsyncCallback<void>): void

Sets a communication device to the active state. This API uses an asynchronous callback to return the result.

This API will be deprecated in a later version due to function design is changed. You are not advised to use it.

You are advised to use the [AVCastPicker component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/using-switch-call-devices) provided by AVSession to switch between call devices.

**System capability**: SystemCapability.Multimedia.Audio.Communication

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceType | [CommunicationDeviceType](../enums/document.md#communicationdevicetype9) | Yes | Audio device flag. |
| active | boolean | Yes | Active state to set. **true** to set the device to the active state, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRoutingManager.setCommunicationDevice(audio.CommunicationDeviceType.SPEAKER, true, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to set the active status of the device. ${err}\`);
    return;
  }
  console.info('Callback invoked to indicate that the device is set to the active status.');
});

#### getAvailableDevices12+

getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors

Obtains the available audio devices. This API returns the result synchronously.

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

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data: audio.AudioDeviceDescriptors = audioRoutingManager.getAvailableDevices(audio.DeviceUsage.MEDIA\_OUTPUT\_DEVICES);
  console.info('Succeeded in doing getAvailableDevices.');
} catch (err) {
  let error = err as BusinessError;
   console.error(\`Failed to getAvailableDevices. Code: ${error.code}, message: ${error.message}\`);
}

#### on('availableDeviceChange')12+

on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void

Subscribes to the event indicating that the connection status of an available audio device is changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'availableDeviceChange'** is triggered when the connection status of available audio devices is changed. |
| deviceUsage | [DeviceUsage](../enums/document.md#deviceusage12) | Yes | Audio device type (classified by usage). |
| callback | Callback<[DeviceChangeAction](../interfaces-others/document.md#devicechangeaction)\> | Yes | Callback used to return the device change details. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

audioRoutingManager.on('availableDeviceChange', audio.DeviceUsage.MEDIA\_OUTPUT\_DEVICES, (deviceChanged: audio.DeviceChangeAction) => {
  console.info('device change type : ' + deviceChanged.type);
  console.info('device descriptor size : ' + deviceChanged.deviceDescriptors.length);
  console.info('device change descriptor : ' + deviceChanged.deviceDescriptors\[0\].deviceRole);
  console.info('device change descriptor : ' + deviceChanged.deviceDescriptors\[0\].deviceType);
});

#### off('availableDeviceChange')12+

off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void

Unsubscribes from the event indicating that the connection status of an available audio device is changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'availableDeviceChange'** is triggered when the connection status of available audio devices is changed. |
| callback | Callback<[DeviceChangeAction](../interfaces-others/document.md#devicechangeaction)\> | No | Callback used to return the available device change details. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

// Cancel all subscriptions to the event.
audioRoutingManager.off('availableDeviceChange');

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let availableDeviceChangeCallback = (deviceChanged: audio.DeviceChangeAction) => {
  console.info('device change type : ' + deviceChanged.type);
  console.info('device descriptor size : ' + deviceChanged.deviceDescriptors.length);
  console.info('device change descriptor : ' + deviceChanged.deviceDescriptors\[0\].deviceRole);
  console.info('device change descriptor : ' + deviceChanged.deviceDescriptors\[0\].deviceType);
};

audioRoutingManager.on('availableDeviceChange', audio.DeviceUsage.MEDIA\_OUTPUT\_DEVICES, availableDeviceChangeCallback);

audioRoutingManager.off('availableDeviceChange', availableDeviceChangeCallback);

#### setCommunicationDevice9+

setCommunicationDevice(deviceType: CommunicationDeviceType, active: boolean): Promise<void>

Sets a communication device to the active state. This API uses a promise to return the result.

This API will be deprecated in a later version due to function design is changed. You are not advised to use it.

You are advised to use the [AVCastPicker component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/using-switch-call-devices) provided by AVSession to switch between call devices.

**System capability**: SystemCapability.Multimedia.Audio.Communication

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceType | [CommunicationDeviceType](../enums/document.md#communicationdevicetype9) | Yes | Active audio device type. |
| active | boolean | Yes | Active state to set. **true** to set the device to the active state, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

audioRoutingManager.setCommunicationDevice(audio.CommunicationDeviceType.SPEAKER, true).then(() => {
  console.info('Promise returned to indicate that the device is set to the active status.');
});

#### isCommunicationDeviceActive9+

isCommunicationDeviceActive(deviceType: CommunicationDeviceType, callback: AsyncCallback<boolean>): void

Checks whether a communication device is active. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Communication

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceType | [CommunicationDeviceType](../enums/document.md#communicationdevicetype9) | Yes | Active audio device type. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true** if the device is active or **false** if not active; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

audioRoutingManager.isCommunicationDeviceActive(audio.CommunicationDeviceType.SPEAKER, (err: BusinessError, value: boolean) => {
  if (err) {
    console.error(\`Failed to obtain the active status of the device. ${err}\`);
    return;
  }
  console.info('Callback invoked to indicate that the active status of the device is obtained.');
});

#### isCommunicationDeviceActive9+

isCommunicationDeviceActive(deviceType: CommunicationDeviceType): Promise<boolean>

Checks whether a communication device is active. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Communication

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceType | [CommunicationDeviceType](../enums/document.md#communicationdevicetype9) | Yes | Active audio device type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result, indicating whether the device is active. **true** if active, **false** otherwise. |

**Example**

audioRoutingManager.isCommunicationDeviceActive(audio.CommunicationDeviceType.SPEAKER).then((value: boolean) => {
  console.info(\`Promise returned to indicate that the active status of the device is obtained ${value}.\`);
});

#### isCommunicationDeviceActiveSync10+

isCommunicationDeviceActiveSync(deviceType: CommunicationDeviceType): boolean

Checks whether a communication device is active. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Communication

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceType | [CommunicationDeviceType](../enums/document.md#communicationdevicetype9) | Yes | Active audio device type. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the device is active. **true** if active, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: boolean = audioRoutingManager.isCommunicationDeviceActiveSync(audio.CommunicationDeviceType.SPEAKER);
  console.info(\`Indicate that the active status of the device is obtained ${value}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to obtain the active status of the device ${error}.\`);
}

#### getPreferOutputDeviceForRendererInfo10+

getPreferOutputDeviceForRendererInfo(rendererInfo: AudioRendererInfo, callback: AsyncCallback<AudioDeviceDescriptors>): void

Obtains the output device with the highest priority based on the audio renderer information. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rendererInfo | [AudioRendererInfo](../interfaces-others/document.md#audiorendererinfo8) | Yes | Audio renderer information. |
| callback | AsyncCallback<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the output device with the highest priority obtained; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by callback. |
| 6800301 | System error. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let rendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM\_USAGE\_MUSIC, // Audio stream usage type: music. Set this parameter based on the service scenario.
  rendererFlags: 0 // AudioRenderer flag.
};

audioRoutingManager.getPreferOutputDeviceForRendererInfo(rendererInfo, (err: BusinessError, audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
  if (err) {
    console.error(\`Failed to get prefer output device for renderer info. Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`Succeeded in getting prefer output device for renderer info, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.\`);
  }
});

#### getPreferOutputDeviceForRendererInfo10+

getPreferOutputDeviceForRendererInfo(rendererInfo: AudioRendererInfo): Promise<AudioDeviceDescriptors>

Obtains the output device with the highest priority based on the audio renderer information. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rendererInfo | [AudioRendererInfo](../interfaces-others/document.md#audiorendererinfo8) | Yes | Audio renderer information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors)\> | Promise used to return the information about the output device with the highest priority. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800301 | System error. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let rendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM\_USAGE\_MUSIC, // Audio stream usage type: music. Set this parameter based on the service scenario.
  rendererFlags: 0 // AudioRenderer flag.
};

audioRoutingManager.getPreferOutputDeviceForRendererInfo(rendererInfo).then((audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
  console.info(\`Succeeded in getting prefer output device for renderer info, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get prefer output device for renderer info. Code: ${err.code}, message: ${err.message}\`);
})

#### getPreferredOutputDeviceForRendererInfoSync10+

getPreferredOutputDeviceForRendererInfoSync(rendererInfo: AudioRendererInfo): AudioDeviceDescriptors

Obtains the output device with the highest priority based on the audio renderer information. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rendererInfo | [AudioRendererInfo](../interfaces-others/document.md#audiorendererinfo8) | Yes | Audio renderer information. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors) | Information about the output device with the highest priority. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let rendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM\_USAGE\_MUSIC, // Audio stream usage type: music. Set this parameter based on the service scenario.
  rendererFlags: 0 // AudioRenderer flag.
};

try {
  let audioDeviceDescriptors = audioRoutingManager.getPreferredOutputDeviceForRendererInfoSync(rendererInfo);
  console.info(\`Succeeded in getting prefer output device for renderer info, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to get prefer output device for renderer info. Code: ${error.code}, message: ${error.message}\`);
}

#### on('preferOutputDeviceChangeForRendererInfo')10+

on(type: 'preferOutputDeviceChangeForRendererInfo', rendererInfo: AudioRendererInfo, callback: Callback<AudioDeviceDescriptors>): void

Subscribes to the change event of the output device with the highest priority, which is triggered when the output device with the highest priority is changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'preferOutputDeviceChangeForRendererInfo'** is triggered when the output device with the highest priority is changed. |
| rendererInfo | [AudioRendererInfo](../interfaces-others/document.md#audiorendererinfo8) | Yes | Audio renderer information. |
| callback | Callback<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors)\> | Yes | Callback used to return the information about the output device with the highest priority. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

let rendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM\_USAGE\_MUSIC, // Audio stream usage type: music. Set this parameter based on the service scenario.
  rendererFlags: 0 // AudioRenderer flag.
};

audioRoutingManager.on('preferOutputDeviceChangeForRendererInfo', rendererInfo, (audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
  console.info(\`Succeeded in using on function, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.\`);
});

#### off('preferOutputDeviceChangeForRendererInfo')10+

off(type: 'preferOutputDeviceChangeForRendererInfo', callback?: Callback<AudioDeviceDescriptors>): void

Unsubscribes from the change event of the output device with the highest priority. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'preferOutputDeviceChangeForRendererInfo'** is triggered when the output device with the highest priority is changed. |
| callback | Callback<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors)\> | No | Callback used to return the information about the output device with the highest priority. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
// If multiple subscriptions are made to the same event, you can call audioRoutingManager.off('preferOutputDeviceChangeForRendererInfo'); to cancel all of them.
let preferOutputDeviceChangeForRendererInfoCallback = (audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
  console.info(\`Succeeded in using on or off function, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.\`);
};
let rendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM\_USAGE\_MUSIC, // Audio stream usage type: music. Set this parameter based on the service scenario.
  rendererFlags: 0 // AudioRenderer flag.
};

audioRoutingManager.on('preferOutputDeviceChangeForRendererInfo', rendererInfo, preferOutputDeviceChangeForRendererInfoCallback);

audioRoutingManager.off('preferOutputDeviceChangeForRendererInfo', preferOutputDeviceChangeForRendererInfoCallback);

#### getPreferredInputDeviceForCapturerInfo10+

getPreferredInputDeviceForCapturerInfo(capturerInfo: AudioCapturerInfo, callback: AsyncCallback<AudioDeviceDescriptors>): void

Obtains the input device with the highest priority based on the audio capturer information. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| capturerInfo | [AudioCapturerInfo](../interfaces-others/document.md#audiocapturerinfo8) | Yes | Audio capturer information. |
| callback | AsyncCallback<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the input device with the highest priority obtained; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by callback. |
| 6800301 | System error. Return by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let capturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE\_TYPE\_MIC, // Audio source type: microphone. Set this parameter based on the service scenario.
  capturerFlags: 0 // AudioCapturer flag.
};

audioRoutingManager.getPreferredInputDeviceForCapturerInfo(capturerInfo, (err: BusinessError, audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
  if (err) {
    console.error(\`Failed to get preferred input device for capturer info. Code: ${err.code}, message: ${err.message}\`);
  } else {
    console.info(\`Succeeded in getting preferred input device for capturer info, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.\`);
  }
});

#### getPreferredInputDeviceForCapturerInfo10+

getPreferredInputDeviceForCapturerInfo(capturerInfo: AudioCapturerInfo): Promise<AudioDeviceDescriptors>

Obtains the input device with the highest priority based on the audio capturer information. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| capturerInfo | [AudioCapturerInfo](../interfaces-others/document.md#audiocapturerinfo8) | Yes | Audio capturer information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors)\> | Promise used to return the information about the input device with the highest priority. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800301 | System error. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let capturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE\_TYPE\_MIC, // Audio source type: microphone. Set this parameter based on the service scenario.
  capturerFlags: 0 // AudioCapturer flag.
};

audioRoutingManager.getPreferredInputDeviceForCapturerInfo(capturerInfo).then((audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
  console.info(\`Succeeded in getting preferred input device for capturer info, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get preferred input device for capturer info. Code: ${err.code}, message: ${err.message}\`);
});

#### getPreferredInputDeviceForCapturerInfoSync10+

getPreferredInputDeviceForCapturerInfoSync(capturerInfo: AudioCapturerInfo): AudioDeviceDescriptors

Obtains the input device with the highest priority based on the audio capturer information. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| capturerInfo | [AudioCapturerInfo](../interfaces-others/document.md#audiocapturerinfo8) | Yes | Audio capturer information. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors) | Information about the input device with the highest priority. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let capturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE\_TYPE\_MIC, // Audio source type: microphone. Set this parameter based on the service scenario.
  capturerFlags: 0 // AudioCapturer flag.
};

try {
  let audioDeviceDescriptors = audioRoutingManager.getPreferredInputDeviceForCapturerInfoSync(capturerInfo);
  console.info(\`Succeeded in getting preferred input device for capturer info, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to get preferred input device for capturer info. Code: ${error.code}, message: ${error.message}\`);
}

#### on('preferredInputDeviceChangeForCapturerInfo')10+

on(type: 'preferredInputDeviceChangeForCapturerInfo', capturerInfo: AudioCapturerInfo, callback: Callback<AudioDeviceDescriptors>): void

Subscribes to the change event of the input device with the highest priority, which is triggered when the input device with the highest priority is changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'preferredInputDeviceChangeForCapturerInfo'** is triggered when the input device with the highest priority is changed. |
| capturerInfo | [AudioCapturerInfo](../interfaces-others/document.md#audiocapturerinfo8) | Yes | Audio capturer information. |
| callback | Callback<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors)\> | Yes | Callback used to return the information about the input device with the highest priority. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

let capturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE\_TYPE\_MIC, // Audio source type: microphone. Set this parameter based on the service scenario.
  capturerFlags: 0 // AudioCapturer flag.
};

audioRoutingManager.on('preferredInputDeviceChangeForCapturerInfo', capturerInfo, (audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
  console.info(\`Succeeded in using on function, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.\`);
});

#### off('preferredInputDeviceChangeForCapturerInfo')10+

off(type: 'preferredInputDeviceChangeForCapturerInfo', callback?: Callback<AudioDeviceDescriptors>): void

Unsubscribes from the change event of the input device with the highest priority. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Audio.Device

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The event **'preferredInputDeviceChangeForCapturerInfo'** is triggered when the input device with the highest priority is changed. |
| callback | Callback<[AudioDeviceDescriptors](../types/document.md#audiodevicedescriptors)\> | No | Callback used to return the information about the input device with the highest priority. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Audio Error Codes](../../../error-codes/audio-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**Example**

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
// If multiple subscriptions are made to the same event, you can call audioRoutingManager.off('preferredInputDeviceChangeForCapturerInfo'); to cancel all of them.
let preferredInputDeviceChangeForCapturerInfoCallback = (audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
  console.info(\`Succeeded in using on or off function, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.\`);
};
let capturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE\_TYPE\_MIC, // Audio source type: microphone. Set this parameter based on the service scenario.
  capturerFlags: 0 // AudioCapturer flag.
};

audioRoutingManager.on('preferredInputDeviceChangeForCapturerInfo', capturerInfo, preferredInputDeviceChangeForCapturerInfoCallback);

audioRoutingManager.off('preferredInputDeviceChangeForCapturerInfo', preferredInputDeviceChangeForCapturerInfoCallback);
