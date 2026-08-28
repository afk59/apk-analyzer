# Managing Microphone Mute State

The microphone is used to record audio data. To deliver an optimal recording effect, you are advised to query the microphone state before starting recording and listen for state changes during recording.

If the user mutes the microphone during audio recording, the recording process is normal, the size of the recorded file increases with the recording duration, but the data volume written into the file is 0.

Volume adjustment is not supported during recording.

#### How to Develop

The **AudioVolumeGroupManager** class provides APIs for managing the microphone state. For details, see [AudioVolumeGroupManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiovolumegroupmanager).

1.  Create an audioVolumeGroupManager object.
    
    import { audio } from '@kit.AudioKit';
    
    let audioVolumeGroupManager: audio.AudioVolumeGroupManager;
    
    // Create an audioVolumeGroupManager object.
    async function loadVolumeGroupManager() {
      const groupid = audio.DEFAULT\_VOLUME\_GROUP\_ID;
      audioVolumeGroupManager = await audio.getAudioManager().getVolumeManager().getVolumeGroupManager(groupid);
      console.info('audioVolumeGroupManager create success.');
    }
    
2.  Call [on('micStateChange')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiovolumegroupmanager#onmicstatechange9) to listen for microphone state changes. When the microphone mute state changes, the application will be notified of the change.
    
    Currently, in scenarios where multiple [AudioManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiomanager) instances are used in a single process, this subscription API only takes effect for the last instance. Subscriptions for other instances will be overwritten (even if the last instance has no active subscription). For this reason, you are advised to use a single **AudioManager** instance for development.
    
    // Listen for microphone state changes.
    async function on() {
      audioVolumeGroupManager.on('micStateChange', (micStateChange: audio.MicStateChangeEvent) => {
        console.info(\`Current microphone status is: ${micStateChange.mute} \`);
      });
    }
    
3.  Call [isMicrophoneMute](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiovolumegroupmanager#ismicrophonemute9) to check whether the microphone is muted. If the return value is **true**, the microphone is muted; otherwise, the microphone is not muted.
    
    // Check whether the microphone is muted.
    async function isMicrophoneMute() {
      await audioVolumeGroupManager.isMicrophoneMute().then((value: boolean) => {
        console.info(\`isMicrophoneMute is: ${value}.\`);
      });
    }
