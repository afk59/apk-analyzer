# Low-Latency Audio Monitoring

Low-latency audio monitoring is supported since API version 20.

AudioLoopback is an audio monitoring tool that delivers audio to headphones with reduced latency in real time, enabling users to hear their own voice or other relevant sounds immediately.

It is commonly used in karaoke applications, where the recorded vocals and background music are sent to the headphones in real time. This allows users to adjust their performance based on the feedback, enhancing their experience.

When audio loopback is enabled, the system creates a low-latency renderer and capturer to implement low-latency in-ear monitoring. The audio captured is routed back to the renderer through an internal path. The renderer follows the audio focus strategy for [STREAM\_USAGE\_MUSIC](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#streamusage), whereas the capturer follows the strategy for [SOURCE\_TYPE\_MIC](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#sourcetype8).

The system automatically chooses the input and output devices. If these devices do not support low latency, audio loopback does not work. If another audio stream takes over the audio focus or if the input or output device changes to the one that does not support low latency, the system disables audio loopback automatically.

#### Prerequisites

-   Currently, low-latency audio monitoring is only supported through wired headphones, where audio is captured and played back via the wired headphones.
    
-   Low-power renderers and low-latency renderers cannot be used concurrently in API version 20. To enable a renderer, you are advised to use [STREAM\_USAGE\_UNKNOWN](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#streamusage). If [STREAM\_USAGE\_MUSIC](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#streamusage) is used, the system creates a normal renderer.
    

#### Development Guidelines

Using AudioLoopback for audio monitoring involves querying the monitoring capability with [isAudioLoopbackSupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiostreammanager#isaudioloopbacksupported20), creating an AudioLoopback instance, setting the volume, listening for status changes, and enabling/disabling audio loopback. This guide walks you through the process of enabling audio monitoring using AudioLoopback, with a focus on how to use AudioLoopback for audio monitoring. You are advised to read this in conjunction with the [AudioLoopback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audioloopback) API documentation.

The following figure shows the status changes of **AudioLoopback**. After an instance is created, you can call the corresponding method to enter the specified state to implement the corresponding behavior.

If an API is called when the AudioLoopback is not in the given state, the system may throw an exception or generate other undefined behavior. Therefore, you are advised to check the AudioLoopback state before triggering state transition.

**AudioLoopback status changes**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/ZCcHVUkdQOmHHP7uD1jrfA/en-us_image_0000002537765154.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9F7D768C827A44C550F1E2D060B5CCC438E88E0A5D26E24626235F1B02EF5FD)

The [on('statusChange')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audioloopback#onstatuschange20) API can be used to listen for **AudioLoopback** status changes. For details about the value and description of each status, see [AudioLoopbackStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#audioloopbackstatus20).

## How to Develop

1.  Query the audio monitoring capability and create an AudioLoopback instance. For details about the AudioLoopback mode, see [AudioLoopbackMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#audioloopbackmode20).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/ws5oMPEHQMKHLxsU02uo_Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC2720CE5B724989859196ACA452EAE8409A91576A0D2A8572BB11A144638A59)
    
    You must request the ohos.permission.MICROPHONE permission for audio monitoring. For details, see [Requesting User Authorization](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).
    
    import { audio } from '@kit.AudioKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    let mode: audio.AudioLoopbackMode = audio.AudioLoopbackMode.HARDWARE;
    let audioLoopback: audio.AudioLoopback;
    let isSupported = audio.getAudioManager().getStreamManager().isAudioLoopbackSupported(mode);
    if (isSupported) {
      audio.createAudioLoopback(mode).then((loopback) => {
        audioLoopback = loopback;
        console.info('Succeeded in creating audio loopback.');
      }).catch((err: BusinessError) => {
        console.error(\`Failed to create audio loopback. Code: ${err.code}, message: ${err.message}\`);
      });
    }
    
2.  Call [getStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audioloopback#getstatus20) to obtain the current audio loopback status.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/C6s3hs0CQGGIVWYkWZN9zQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BBFC1002B0F25B512EB3E9D7569C166BFBE3FA34F9AEA155700EAA2C391346E5)
    
    The audio loopback status is affected by factors such as audio focus, low-latency control, and capturer and renderer devices.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    audioLoopback.getStatus().then((status: audio.AudioLoopbackStatus) => {
      console.info(\`Succeeded in getting status, status is ${status}.\`);
    }).catch((err: BusinessError) => {
      console.error(\`Failed to get status. Code: ${err.code}, message: ${err.message}\`);
    });
    
3.  Call [setVolume](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audioloopback#setvolume20) to set the audio loopback volume.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/VeO0GCBtSpSUPd62VdBO5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AAAD3A9EC237A0E3642C4DEE45252B7FF90127B5F9586D4AB4A92341807180AF)
    
    -   Setting the volume before enabling audio loopback will take effect after successful activation of audio loopback.
    -   Setting the volume after enabling audio loopback will take effect immediately.
    -   If the volume is not set before enabling audio loopback, the default volume of 0.5 is used upon activation of audio loopback.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    audioLoopback.setVolume(0.5).then(() => {
      console.info('Succeeded in setting volume.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to set volume. Code: ${err.code}, message: ${err.message}\`);
    });
    
4.  Starting from API version 21, [setReverbPreset](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audioloopback#setreverbpreset21) method can be called to set the reverb mode of audio loopback.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/YzvYiHB4RJykGVeUqz1kjg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37B18C1141AD32310FBACB68F48E84163A5A4073EC387D600FDC631DE1372F07)
    
    -   If you set the reverb mode before enabling loopback, the setting takes effect after audio loopback is successfully enabled.
    -   If you set the reverb mode after enabling loopback, the setting takes effect immediately.
    -   If you do not set the reverb mode before enabling loopback, the default mode [THEATER](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#audioloopbackreverbpreset21) is used upon activation of audio loopback.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    try {
        audioLoopback.setReverbPreset(audio.AudioLoopbackReverbPreset.THEATER);
    } catch (err) {
        console.error(\`Failed to set reverb preset. Code: ${err.code}, message: ${err.message}\`);
    }
    
5.  Starting from API version 21, [getReverbPreset](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audioloopback#getreverbpreset21) can be called to query the reverb mode of the current audio loopback.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/hNyWFPUORE-iXXXEnWs1iQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=447E9E01D8989314F524010B8122EFB5DBF84BBE51F958DE7746066140DB7459)
    
    If no reverb mode has been set, the default mode [THEATER](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#audioloopbackreverbpreset21) is returned.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    try {
      let reverbPreset = audioLoopback.getReverbPreset();
    } catch (err) {
      console.error(\`Failed to get reverb preset. Code: ${err.code}, message: ${err.message}\`);
    }
    
6.  Starting from API version 21, [setEqualizerPreset](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audioloopback#setequalizerpreset21) can be called to set the equalizer type of audio loopback.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/wxnfM7mJSeSLyy7RU9bahg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CA9F7B644830C86832011AAFB16046A3309DFA88020C789AE910099BD950272)
    
    -   If you set the equalizer type before enabling loopback, the setting takes effect after audio loopback is successfully enabled.
    -   If you set the equalizer type after enabling loopback, the setting takes effect immediately.
    -   If you do not set the equalizer type before enabling loopback, the default mode [FULL](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#audioloopbackequalizerpreset21) is used upon activation of audio loopback.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    try {
      audioLoopback.setEqualizerPreset(audio.AudioLoopbackEqualizerPreset.FULL);
    } catch (err) {
      console.error(\`Failed to set equalizer preset. Code: ${err.code}, message: ${err.message}\`);
    }
    
7.  Starting from API version 21, [getEqualizerPreset](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audioloopback#getequalizerpreset21) can be called to query the equalizer type of the current audio loopback.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/kcqpLJkdS5WFPS_seU2niA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA39BC802F4BCC2C477AEC0F831F1FF996ED2BCBC2742B8996776F8BDE8B7CAE)
    
    If no equalizer type has been set, the default mode [FULL](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#audioloopbackequalizerpreset21) is returned.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    try {
      let reverbPreset = audioLoopback.getEqualizerPreset();
    } catch (err) {
      console.error(\`Failed to get equalizer preset. Code: ${err.code}, message: ${err.message}\`);
    }
    
8.  Call [enable](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audioloopback#enable20) to enable or disable audio loopback.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    audioLoopback.enable(true).then((isSuccess) => {
      if (isSuccess) {
        console.info('Succeeded in using enable function.');
      } else {
        console.error('Failed to use enable function.');
      }
    }).catch((err: BusinessError) => {
      console.error(\`Failed to use enable function. code: ${err.code}, message: ${err.message}\`);
    });
    
    audioLoopback.enable(false).then((isSuccess) => {
      if (isSuccess) {
        console.info('Succeeded in using enable function.');
      } else {
        console.error('Failed to use enable function.');
      }
    }).catch((err: BusinessError) => {
      console.error(\`Failed to use enable function. code: ${err.code}, message: ${err.message}\`);
    });
    

## Complete Sample Code

The following example demonstrates how to use AudioLoopback to enable low-latency audio monitoring:

import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

const TAG = 'AudioLoopbackDemo';

let mode: audio.AudioLoopbackMode = audio.AudioLoopbackMode.HARDWARE;
let audioLoopback: audio.AudioLoopback | undefined = undefined;
let currentReverbPreset: audio.AudioLoopbackReverbPreset = audio.AudioLoopbackReverbPreset.THEATER;
let currentEqualizerPreset: audio.AudioLoopbackEqualizerPreset = audio.AudioLoopbackEqualizerPreset.FULL;

let statusChangeCallback = (status: audio.AudioLoopbackStatus) => {
  if (status == audio.AudioLoopbackStatus.UNAVAILABLE\_DEVICE) {
    console.info('Audio loopback status is: UNAVAILABLE\_DEVICE');
  } else if (status == audio.AudioLoopbackStatus.UNAVAILABLE\_SCENE) {
    console.info('Audio loopback status is: UNAVAILABLE\_SCENE');
  } else if (status == audio.AudioLoopbackStatus.AVAILABLE\_IDLE) {
    console.info('Audio loopback status is: AVAILABLE\_IDLE');
  } else if (status == audio.AudioLoopbackStatus.AVAILABLE\_RUNNING) {
    console.info('Audio loopback status is: AVAILABLE\_RUNNING');
  }
};

// Query the capability and create an instance.
function init() {
  let isSupported = audio.getAudioManager().getStreamManager().isAudioLoopbackSupported(mode);
  if (isSupported) {
    audio.createAudioLoopback(mode).then((loopback) => {
      console.info('Succeeded in creating audio loopback.');
      audioLoopback = loopback;
    }).catch((err: BusinessError) => {
      console.error(\`Failed to create audio loopback. Code: ${err.code}, message: ${err.message}\`);
    });
  } else {
    console.error('Audio loopback is unsupported.');
  }
}

// Set the volume for audio loopback.
async function setVolume(volume: number) {
  if (audioLoopback !== undefined) {
    try {
      await audioLoopback.setVolume(volume);
      console.info('Succeeded in setting volume.');
    } catch (err) {
      console.error(\`Failed to set volume. Code: ${err.code}, message: ${err.message}\`);
    }
  } else {
    console.error('Audio loopback not created.');
  }
}

// Set the reverb mode for audio loopback.
async function setReverbPreset(preset: audio.AudioLoopbackReverbPreset) {
  if (audioLoopback !== undefined) {
    try {
      audioLoopback.setReverbPreset(preset);
      console.info('Succeeded in setting reverb preset.');
      currentReverbPreset = audioLoopback.getReverbPreset(); // Obtain the current reverb mode to prevent setting failures.
    } catch (err) {
      console.error(\`Failed to set reverb preset. Code: ${err.code}, message: ${err.message}\`);
    }
  } else {
    console.error('Audio loopback not created.');
  }
}

// Set the equalizer type for audio loopback.
async function setEqualizerPreset(preset: audio.AudioLoopbackEqualizerPreset) {
  if (audioLoopback !== undefined) {
    try {
      audioLoopback.setEqualizerPreset(preset);
      console.info('Succeeded in setting equalizer preset.');
      currentEqualizerPreset = audioLoopback.getEqualizerPreset(); // Obtain the current equalizer type to prevent setting failures.
    } catch (err) {
      console.error(\`Failed to set equalizer preset. Code: ${err.code}, message: ${err.message}\`);
    }
  } else {
    console.error('Audio loopback not created.');
  }
}

// Set a listener and enable audio loopback.
async function enable() {
  if (audioLoopback !== undefined) {
    try {
      let status = await audioLoopback.getStatus();
      if (status == audio.AudioLoopbackStatus.AVAILABLE\_IDLE) {
        // Register a listener.
        audioLoopback.on('statusChange', statusChangeCallback);
        // Enable audio loopback.
        let success = await audioLoopback.enable(true);
        if (success) {
          console.info('Succeeded in using enable function.');
        } else {
          status = await audioLoopback.getStatus();
          statusChangeCallback(status);
        }
      } else {
        statusChangeCallback(status);
      }
    } catch (err) {
      console.error(\`Failed to use enable function. code: ${err.code}, message: ${err.message}\`);
    }
  } else {
    console.error('Audio loopback not created.');
  }
}

// Disable audio loopback and unregister the listener.
async function disable() {
  if (audioLoopback !== undefined) {
    try {
      let status = await audioLoopback.getStatus();
      if (status == audio.AudioLoopbackStatus.AVAILABLE\_RUNNING) {
        // Disable audio loopback.
        let success = await audioLoopback.enable(false);
        if (success) {
          console.info('Succeeded in using enable function.');
          // Unregister the listener.
          audioLoopback.off('statusChange', statusChangeCallback);
        } else {
          status = await audioLoopback.getStatus();
          statusChangeCallback(status);
        }
      } else {
        statusChangeCallback(status);
      }
    } catch (err) {
      console.error(\`Failed to use enable function. code: ${err.code}, message: ${err.message}\`);
    }
  } else {
    console.error('Audio loopback not created.');
  }
}

## Sample of Low-Latency Audio Loopback

For details, see [Enabling Low-Latency Audio Loopback Using AudioLoopback](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/Audio).
