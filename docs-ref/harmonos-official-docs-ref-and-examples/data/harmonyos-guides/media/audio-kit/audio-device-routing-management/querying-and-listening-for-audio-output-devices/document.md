# Querying and Listening for Audio Output Devices

Applications can manage global audio output devices in either of the following ways:

-   Generally, applications can [query and listen for audio output devices using AudioRoutingManager](#querying-and-listening-for-audio-output-devices-using-audioroutingmanager).
-   Starting from API version 20, AudioSessionManager offers certain APIs for managing output devices. Applications can now [query and listen for audio output devices using AudioSession](#querying-and-listening-for-audio-output-devices-using-audiosession). This is useful for simultaneously managing audio focus and output.

#### Querying and Listening for Audio Output Devices Using AudioRoutingManager

You can use APIs to manage audio output devices, including querying audio device information and listening for connection status changes. For details about the APIs, see [AudioRoutingManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audioroutingmanager).

## Creating an AudioRoutingManager Instance

Before using AudioRoutingManager to manage audio devices, import the audio module and create an AudioManager instance.

import { audio } from '@kit.AudioKit';  // Import the audio module.

let audioManager = audio.getAudioManager();  // Create an AudioManager instance.

let audioRoutingManager = audioManager.getRoutingManager();  // Call an API of AudioManager to create an AudioRoutingManager instance.

## Supported Audio Output Device Types

The table below lists the supported output devices.

| Name | Value | Description |
| :-- | :-- | :-- |
| EARPIECE | 1 | Earpiece. |
| SPEAKER | 2 | Speaker. |
| WIRED\_HEADSET | 3 | Wired headset with a microphone. |
| WIRED\_HEADPHONES | 4 | Wired headset without microphone. |
| BLUETOOTH\_SCO | 7 | Bluetooth device using Synchronous Connection Oriented (SCO) links. |
| BLUETOOTH\_A2DP | 8 | Bluetooth device using Advanced Audio Distribution Profile (A2DP) links. |
| USB\_HEADSET | 22 | USB Type-C headset. |
| NEARLINK | 31 | NearLink device. |

## Obtaining Output Device Information

Use the [getDevices](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audioroutingmanager#getdevices9) method to obtain information about all output devices.

import { audio } from '@kit.AudioKit';

audioRoutingManager.getDevices(audio.DeviceFlag.OUTPUT\_DEVICES\_FLAG).then((data: audio.AudioDeviceDescriptors) => {
  console.info('Promise returned to indicate that the device list is obtained.');
});

## Listening for Device Connection State Changes

Set a listener to listen for changes of the device connection state. When a device is connected or disconnected, a callback is triggered.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/85P1KgZ6TFG4uYbOrQvsog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FCF6630920B0BFFD216CF5EFBB2E26F2EFFEB4E395BDD0045AF50AF300D42D8F)

The listener captures all changes in device connections. It is not recommended that the changes be used as a basis for handling automatic pausing in applications. If an application needs to manage services related to automatic pause, it should consider the [reasons behind changes in the audio stream output device](../handling-output-device-changes-gracefully/document.md#device-change-reason).

import { audio } from '@kit.AudioKit';

// Listen for connection state changes of audio devices.
audioRoutingManager.on('deviceChange', audio.DeviceFlag.OUTPUT\_DEVICES\_FLAG, (deviceChanged: audio.DeviceChangeAction) => {
  console.info(\`device change type : ${deviceChanged.type}\`);  // Device connection state change. The value 0 means that the device is connected and 1 means that the device is disconnected.
  console.info(\`device descriptor size : ${deviceChanged.deviceDescriptors.length}\`);
  console.info(\`device change descriptor : ${deviceChanged.deviceDescriptors\[0\].deviceRole}\`);  // Device role.
  console.info(\`device change descriptor : ${deviceChanged.deviceDescriptors\[0\].deviceType}\`);  // Device type.
});

// Cancel the listener for the connection state changes of audio devices.
audioRoutingManager.off('deviceChange');

## Obtaining Information About the Output Device with the Highest Priority

Use the [getPreferOutputDeviceForRendererInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audioroutingmanager#getpreferoutputdeviceforrendererinfo10) method to obtain information about the output device with the highest priority.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/qqqc2mJzTM25nQKzUBLamw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2C3A1FF2F11E3FFA1AD2C1EC6596DC962B372437DF1A8152A5AD5D1EA3723EB)

The output device with the highest priority is the device that will output audio.

import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rendererInfo: audio.AudioRendererInfo = {
    usage: audio.StreamUsage.STREAM\_USAGE\_MUSIC, // Audio stream usage type: music. Set this parameter based on the service scenario.
    rendererFlags: 0 // AudioRenderer flag.
};

async function getPreferOutputDeviceForRendererInfo() {
  audioRoutingManager.getPreferOutputDeviceForRendererInfo(rendererInfo).then((desc: audio.AudioDeviceDescriptors) => {
    console.info(\`device descriptor: ${desc}\`);
  }).catch((err: BusinessError) => {
    console.error(\`Result ERROR: ${err}\`);
  })
}

## Listening for Changes of the Output Device with the Highest Priority

import { audio } from '@kit.AudioKit';

let rendererInfo: audio.AudioRendererInfo = {
    usage: audio.StreamUsage.STREAM\_USAGE\_MUSIC, // Audio stream usage type: music. Set this parameter based on the service scenario.
    rendererFlags: 0 // AudioRenderer flag.
};

// Listen for changes of the output device with the highest priority.
audioRoutingManager.on('preferOutputDeviceChangeForRendererInfo', rendererInfo, (desc: audio.AudioDeviceDescriptors) => {
    console.info(\`device change descriptor : ${desc\[0\].deviceRole}\`);  // Device role.
    console.info(\`device change descriptor : ${desc\[0\].deviceType}\`);  // Device type.
});

// Cancel the listening for changes of the output device with the highest priority.
audioRoutingManager.off('preferOutputDeviceChangeForRendererInfo');

#### Querying and Listening for Audio Output Devices Using AudioSession

Applications using the player SDK to play audio streams do not hold an [AudioRenderer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer) object. As a result, they cannot flexibly control the selection of playback devices and listen for the device status. Starting from API version 20, AudioSession not only introduces focus management but also provides capabilities for managing audio output devices, including setting the default output device and listening for device changes. For more information, refer to the following documentation:

-   ArkTS APIs: [AudioSessionManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager)
-   C APIs: [native\_audio\_session\_manager.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-session-manager-h)

## Creating an AudioSession Instance

Before using AudioSessionManager to manage audio devices, import the module and create an AudioSessionManager instance.

import { audio } from '@kit.AudioKit';  // Import the audio module.

let audioManager = audio.getAudioManager();  // Create an AudioManager instance.

let audioSessionManager = audioManager.getSessionManager();  // Call an API of AudioManager to create an AudioSessionManager instance.

## Setting the Default Audio Output Device

Call [setDefaultOutputDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#setdefaultoutputdevice20) to set the default output device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/nbwsevv3TUegUqpG-AkY0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B309D8197F75DAFB3103A4C7670D89725F4779F6F75EEB32453ECF7B52F08751)

-   As AudioSession is an application-level setting, calling this API to set the default audio output device will override the audio output device information set by the **setDefaultOutputDevice** API of AudioRenderer.
-   To cancel the default output device set by calling **setDefaultOutputDevice**, you can set the parameter to **audio.DeviceType.DEFAULT**, which returns the device selection to the system. Otherwise, each time **activateAudioSession** is called, the default output device selected by the application takes effect.

import { BusinessError } from '@kit.BasicServicesKit';

// Set the default output device to the device speaker.
audioSessionManager.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
  console.info('setDefaultOutputDevice Success!');
}).catch((err: BusinessError) => {
  console.error(\`setDefaultOutputDevice Fail: ${err}\`);
});

// Set the default output device to the system default device, i.e., cancel the default device set by the application and hand over the device selection to the system.
audioSessionManager.setDefaultOutputDevice(audio.DeviceType.DEFAULT).then(() => {
  console.info('setDefaultOutputDevice Success!');
}).catch((err: BusinessError) => {
  console.error(\`setDefaultOutputDevice Fail: ${err}\`);
});

## Obtaining the Default Audio Output Device

Call [getDefaultOutputDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#getdefaultoutputdevice20) to obtain the default output device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/6WQXxPxURUS1y30GZgDZog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA80E85BBD404D07766A721A95E5EC053A048D7B791ED103C9A88FC1A672CFDA)

This API is used to query the output device set via [setDefaultOutputDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#setdefaultoutputdevice20).

let deviceType = audioSessionManager.getDefaultOutputDevice();
console.info('getDefaultOutputDevice Success, deviceType: ${deviceType}');

## Listening for Output Device Changes

Subscribe to [CurrentOutputDeviceChangedEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-i#currentoutputdevicechangedevent20) to listen for changes in the connection status of output devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/4x61h4M-SpKmvCtJo9X_WA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8068FA6E6E641FF68EABD0AF1F7CC4243E3C859BAD9155F013DE3B0FFDF44435)

**currentOutputDeviceChangedCallback** includes the reason for the device change and the recommended subsequent actions. Applications should handle different change reasons accordingly and continue or stop playback as recommended by the system.

import { audio } from '@kit.AudioKit';

// For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let currentOutputDeviceChangedCallback = (currentOutputDeviceChangedEvent: audio.CurrentOutputDeviceChangedEvent) => {
  console.info(\`reason of audioSessionStateChanged: ${currentOutputDeviceChangedEvent.changeReason} \`);

  switch (currentOutputDeviceChangedEvent.changeReason) {
    case audio.AudioStreamDeviceChangeReason.REASON\_OLD\_DEVICE\_UNAVAILABLE:
      // Handle the event where the old device is unavailable. If the application is in the playing state, the playback should be paused and the UX interface should be updated.
      break;
    case audio.AudioStreamDeviceChangeReason.REASON\_NEW\_DEVICE\_AVAILABLE:
      // Handle the event where a new device is available based on the application's service logic.
      break;
    case audio.AudioStreamDeviceChangeReason.REASON\_OVERRODE:
      // Handle the event where the device is overridden based on the application's service logic.
      break;
    case audio.AudioStreamDeviceChangeReason.REASON\_SESSION\_ACTIVATED:
      // Handle the event where the audio session is activated based on the application's service logic.
      break;
    case audio.AudioStreamDeviceChangeReason.REASON\_STREAM\_PRIORITY\_CHANGED:
      // Handle the event where a higher-priority audio stream triggers a device change based on the application's service logic.
      break;
    case audio.AudioStreamDeviceChangeReason.REASON\_UNKNOWN:
      // Handle the event for unknown reasons based on the application's service logic.
      break;
  }
};

audioSessionManager.on('currentOutputDeviceChanged', currentOutputDeviceChangedCallback);

audioSessionManager.off('currentOutputDeviceChanged', currentOutputDeviceChangedCallback);

// Cancel all subscriptions to the event.
audioSessionManager.off('currentOutputDeviceChanged');
