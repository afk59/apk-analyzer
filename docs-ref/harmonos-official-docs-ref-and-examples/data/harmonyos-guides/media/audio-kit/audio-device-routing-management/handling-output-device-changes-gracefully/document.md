# Handling Output Device Changes Gracefully

You can listen for audio output device changes and implement appropriate responses. For example, if the output device disconnects during music playback, the application should pause playback immediately to avoid disrupting the user.

You can use [on('outputDeviceChangeWithInfo')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#onoutputdevicechangewithinfo11) of **AudioRenderer** or [on('currentOutputDeviceChanged')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#oncurrentoutputdevicechanged20) of **AudioSessionManager** to listen for changes in the audio output device and the associated reason. When the audio output device is changed due to the online/offline status change, forcible user selection, device preemption, or device selection strategy change, the system uses this API to notify the application of the change, including the audio output device information and change reason.

#### Audio Output Device Information

The audio device change information returned by [on('outputDeviceChangeWithInfo')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#onoutputdevicechangewithinfo11) of **AudioRenderer** or [on('currentOutputDeviceChanged')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#oncurrentoutputdevicechanged20) of **AudioSessionManager** contains the audio output device information, delivered as an array. Typically, this array contains information about only one device. For details, please refer to [AudioDeviceDescriptors](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-t#audiodevicedescriptors) (device information list).

#### Device Change Reason

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/XDZg3Fs3T6CIBms2vEuPRw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64C8C4E2CB42B26B15DFA5C81F78A3CE45F2E554648D3199286B3AEE09C5DAF7)

The system sends [AudioStreamDeviceChangeReason](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#audiostreamdevicechangereason11) to the application in any of the following cases:

-   **REASON\_NEW\_DEVICE\_AVAILABLE**: A new device is available.
    
    **Trigger conditions**:
    
    Typical Bluetooth devices (such as headsets, smart glasses, speakers, and telematics devices) are connected; Bluetooth devices that support wear detection (such as headsets and smart glasses) are put on; wired devices (such as 3.5mm headsets, Type-C headsets, USB headsets, and USB speakers) are plugged in; distributed devices are brought online.
    
-   **REASON\_OLD\_DEVICE\_UNAVAILABLE**: The old device is unavailable.
    
    When this reason is reported, the application should consider pausing audio playback.
    
    **Trigger conditions**:
    
    Typical Bluetooth devices (such as headsets, smart glasses, speakers, and telematics devices) are disconnected; Bluetooth devices that support wear detection (such as headsets and smart glasses) are taken off; wired devices (such as 3.5mm headsets, Type-C headsets, USB headsets, and USB speakers) are unplugged; distributed devices are brought offline.
    
    The handling suggestions for typical service scenarios are as follows:
    
    -   Gaming scenario: Do not pause audio playback.
    -   Audiobook scenario: Pause audio playback.
    -   Music scenario: Pause audio playback.
    -   Video scenario: Pause audio playback.
-   **REASON\_OVERRODE**: The user forcibly selects a device.
    
    **Trigger conditions**:
    
    The user selects another audio output device from the UI, and selects to answer a cellular or VoIP call from the peripheral.
    
-   **REASON\_UNKNOWN**: Unknown reason.
    

#### Example

## AudioRenderer Sample

import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioRenderer: audio.AudioRenderer | undefined = undefined;
let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE\_RATE\_48000, // Sampling rate.
  channels: audio.AudioChannel.CHANNEL\_2, // Channel.
  sampleFormat: audio.AudioSampleFormat.SAMPLE\_FORMAT\_S16LE, // Sampling format.
  encodingType: audio.AudioEncodingType.ENCODING\_TYPE\_RAW // Encoding format.
};
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM\_USAGE\_MUSIC, // Audio stream usage type: music. Set this parameter based on the service scenario.
  rendererFlags: 0 // AudioRenderer flag.
};
let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: audioRendererInfo
};

// Create an AudioRenderer instance.
audio.createAudioRenderer(audioRendererOptions).then((data) => {
  audioRenderer = data;
  console.info('AudioFrameworkRenderLog: AudioRenderer Created : Success : Stream Type: SUCCESS');
}).catch((err: BusinessError) => {
  console.error(\`AudioFrameworkRenderLog: AudioRenderer Created : ERROR : ${err}\`);
});

if (audioRenderer) {
  // Subscribe to audio output device changes, carrying the change reason.
  (audioRenderer as audio.AudioRenderer).on('outputDeviceChangeWithInfo', async (deviceChangeInfo: audio.AudioStreamDeviceChangeInfo) => {
    switch (deviceChangeInfo.changeReason) {
      case audio.AudioStreamDeviceChangeReason.REASON\_OLD\_DEVICE\_UNAVAILABLE:
        // Respond to the device unavailability event. If the application is playing content, pause the playback and update the UX.
        // await audioRenderer.pause();
        break;
      case audio.AudioStreamDeviceChangeReason.REASON\_NEW\_DEVICE\_AVAILABLE:
        // The application responds to the device availability event based on the service status.
        break;
      case audio.AudioStreamDeviceChangeReason.REASON\_OVERRODE:
        // The application responds to the forcible device selection event based on the service status.
        break;
      case audio.AudioStreamDeviceChangeReason.REASON\_UNKNOWN:
        // The application responds to the unknown reason event based on the service status.
        break;
    }
  });
}

## AudioSessionManager sample

import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioRenderer: audio.AudioRenderer | undefined = undefined;
let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE\_RATE\_48000, // Sampling rate.
  channels: audio.AudioChannel.CHANNEL\_2, // Channel.
  sampleFormat: audio.AudioSampleFormat.SAMPLE\_FORMAT\_S16LE, // Sampling format.
  encodingType: audio.AudioEncodingType.ENCODING\_TYPE\_RAW // Encoding format.
};
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM\_USAGE\_MUSIC, // Audio stream usage type: music. Set this parameter based on the service scenario.
  rendererFlags: 0 // AudioRenderer flag.
};
let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: audioRendererInfo
};

// Create an AudioRenderer instance.
audio.createAudioRenderer(audioRendererOptions).then((data) => {
  audioRenderer = data;
  console.info('AudioFrameworkRenderLog: AudioRenderer Created : Success : Stream Type: SUCCESS');
}).catch((err: BusinessError) => {
  console.error(\`AudioFrameworkRenderLog: AudioRenderer Created : ERROR : ${err}\`);
});

if (audioRenderer) {
  try {
    let sessionManager = audio.getAudioManager().getSessionManager();
    sessionManager.activateAudioSession({ concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY\_MIX\_WITH\_OTHERS });
    // Subscribe to audio output device changes, carrying the change reason.
    sessionManager.on('currentOutputDeviceChanged', async (deviceChangeInfo: audio.CurrentOutputDeviceChangedEvent) => {
      switch (deviceChangeInfo.changeReason) {
        case audio.AudioStreamDeviceChangeReason.REASON\_OLD\_DEVICE\_UNAVAILABLE:
          // Respond to the device unavailability event. If the application is playing content, pause the playback and update the UX.
          // await audioRenderer.pause();
          console.info('REASON\_OLD\_DEVICE\_UNAVAILABLE, pause audio is recommended');
          break;
        case audio.AudioStreamDeviceChangeReason.REASON\_NEW\_DEVICE\_AVAILABLE:
          // The application responds to the device availability event based on the service status.
          break;
        case audio.AudioStreamDeviceChangeReason.REASON\_OVERRODE:
          // The application responds to the forcible device selection event based on the service status.
          break;
        case audio.AudioStreamDeviceChangeReason.REASON\_UNKNOWN:
          // The application responds to the unknown reason event based on the service status.
          break;
      }
    });
  } catch (err) {
    console.error(\`on sessionManager#currentOutputDeviceChanged fail: ${err}\`);
  }
}
