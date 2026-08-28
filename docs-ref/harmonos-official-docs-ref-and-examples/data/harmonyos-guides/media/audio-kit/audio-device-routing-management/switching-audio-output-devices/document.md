# Switching Audio Output Devices

When an application outputs audio, the system selects the corresponding output device ([STREAM\_USAGE\_MUSIC](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#streamusage): speaker; [STREAM\_USAGE\_VOICE\_COMMUNICATION](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#streamusage): receiver) based on the audio stream type. If the default output device does not meet the application requirements, the application can use **AVCastPicker** or **setDefaultOutputDevice** to switch the audio output device.

#### Switching Output Devices for Media Applications

Applications can use the [AVCastPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-multimedia-avcastpicker#avcastpicker) component to switch the output device for media applications.

#### Switching Output Devices for Call Applications

## Switching External Devices

A call-type application can [use the call device switching component](../../../avsession-kit/distributed-avsession/using-the-call-device-switching-component/document.md) to switch the routing of external output devices.

## Switching Built-in Devices

If no external device is connected, in voice call scenarios, the system uses the earpiece for audio output by default. In other scenarios, the system defaults to using the speaker. If an external device is connected, the system defaults to using the external device for audio output.

To cancel the default output device set by calling **setDefaultOutputDevice**, you can set the parameter to **audio.DeviceType.DEFAULT**, which returns the audio output device selection to the system.

1.  Starting from API version 12, applications can use [setDefaultOutputDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#setdefaultoutputdevice12) of AudioRenderer to switch between the earpiece and speaker routing. Before calling this API, you need to obtain an [AudioRenderer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-f#audiocreateaudiorenderer8) instance.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/nuYPsPFMRtq9CNBN_jhAJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2680969A5092214B00C318788C9577D0840B33C68830BAB84E1DEE6ADF4843E6)
    
    -   AudioRenderer operates at the stream level. Therefore, the default audio output device set via this API take effect only for the current stream.
    -   This API has a lower priority than [setDefaultOutputDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#setdefaultoutputdevice20) of AudioSessionManager. If [setDefaultOutputDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#setdefaultoutputdevice20) of AudioSessionManager has been used to set the default audio output device, the settings made via this API does not take effect.
    
    import { audio } from '@kit.AudioKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    // Set the default output device to the device speaker.
    audioRenderer.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
      console.info('Succeeded in setting default output device.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to set default output device. Code: ${err.code}, message: ${err.message}\`);
    });
    
    // Set the default output device to the system's default output device (i.e., cancel the default device set by the application and let the system select the device).
    audioRenderer.setDefaultOutputDevice(audio.DeviceType.DEFAULT).then(() => {
      console.info('Succeeded in setting default output device.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to set default output device. Code: ${err.code}, message: ${err.message}\`);
    });
    
2.  Starting from API version 20, applications can use [setDefaultOutputDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager#setdefaultoutputdevice20) of AudioSessionManager to switch between the earpiece and speaker routing.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/u_isUaWLSo2KCqn7lpgtQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D70BB71BF850C5C59A9409C37BD092BB73F10F13524264F9B49572716F362189)
    
    AudioSessionManager operates at the application level. Therefore, calling this API to set the default audio output device takes effect for all applicable audio streams within the current application and overrides the default audio output device settings made via [setDefaultOutputDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#setdefaultoutputdevice12) of AudioRenderer.
    
    import { audio } from '@kit.AudioKit';  // Import the audio module.
    import { BusinessError } from '@kit.BasicServicesKit';
    
    let audioManager = audio.getAudioManager();  // Create an AudioManager instance.
    
    let audioSessionManager = audioManager.getSessionManager();  // Call an API of AudioManager to create an AudioSessionManager instance.
    
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
    
    // Set the default output device to the earpiece.
    audioSessionManager.setDefaultOutputDevice(audio.DeviceType.EARPIECE).then(() => {
      console.info('Succeeded in setting default output device.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to set default output device. Code: ${err.code}, message: ${err.message}\`);
    });
    
    // Set the default output device to the system's default output device (i.e., cancel the default device set by the application and let the system select the device).
    audioSessionManager.setDefaultOutputDevice(audio.DeviceType.DEFAULT).then(() => {
      console.info('Succeeded in setting default output device.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to set default output device. Code: ${err.code}, message: ${err.message}\`);
    });
