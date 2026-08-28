# Querying and Listening for Audio Input Devices

You can use APIs to manage audio input devices, including querying audio input device information and listening for device connection status changes. For details about the APIs, see [AudioRoutingManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audioroutingmanager).

#### Creating an AudioRoutingManager Instance

Before using AudioRoutingManager to manage audio devices, import the audio module and create an AudioManager instance.

import { audio } from '@kit.AudioKit';  // Import the audio module.

let audioManager = audio.getAudioManager();  // Create an AudioManager instance.
let audioRoutingManager = audioManager.getRoutingManager();  // Call an API of AudioManager to create an AudioRoutingManager instance.

#### Supported Audio Input Device Types

The table below lists the supported audio input devices.

| Name | Value | Description |
| :-- | :-- | :-- |
| WIRED\_HEADSET | 3 | Wired headset with a microphone. |
| BLUETOOTH\_SCO | 7 | Bluetooth device using Synchronous Connection Oriented (SCO) links. |
| MIC | 15 | Microphone. |
| USB\_HEADSET | 22 | USB Type-C headset. |
| NEARLINK | 31 | NearLink device. |

#### Obtaining Input Device Information

Use the [getDevices](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audioroutingmanager#getdevices9) method to obtain information about all input devices.

import { audio } from '@kit.AudioKit';

audioRoutingManager.getDevices(audio.DeviceFlag.INPUT\_DEVICES\_FLAG).then((data: audio.AudioDeviceDescriptors) => {
  console.info('Promise returned to indicate that the device list is obtained.');
});

#### Listening for Device Connection State Changes

Set a listener to listen for changes of the device connection state. When a device is connected or disconnected, a callback is triggered.

import { audio } from '@kit.AudioKit';

// Listen for connection state changes of audio devices.
audioRoutingManager.on('deviceChange', audio.DeviceFlag.INPUT\_DEVICES\_FLAG, (deviceChanged: audio.DeviceChangeAction) => {
  console.info('device change type: ' + deviceChanged.type);  // Device connection state change. The value 0 means that the device is connected and 1 means that the device is disconnected.
  console.info('device descriptor size : ' + deviceChanged.deviceDescriptors.length);
  console.info('device change descriptor: ' + deviceChanged.deviceDescriptors\[0\].deviceRole);  // Device role.
  console.info('device change descriptor: ' + deviceChanged.deviceDescriptors\[0\].deviceType);  // Device type.
});

// Cancel the listener for the connection state changes of audio devices.
audioRoutingManager.off('deviceChange', (deviceChanged: audio.DeviceChangeAction) => {
  console.info('Should be no callback.');
});
