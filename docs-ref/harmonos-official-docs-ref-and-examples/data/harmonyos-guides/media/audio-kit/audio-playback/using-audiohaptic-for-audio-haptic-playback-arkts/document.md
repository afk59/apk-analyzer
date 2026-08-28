# Using AudioHaptic for Audio-Haptic Playback (ArkTs)

**AudioHaptic** provides APIs for audio-haptic playback and management. It applies to scenarios where haptic feedback needs to be initiated synchronously during audio playback, for example, when there are incoming calls or messages or users are typing.

#### Development Guidelines

The entire process of audio-haptic development involves management of audio and haptic sources, configuration of an audio latency mode and audio stream usage, and creation and management of an audio-haptic player. This topic uses the process of one-time audio-haptic playback as an example to describe how to use **AudioHaptic**. Before the development, read [AudioHaptic](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-audiohaptic) for better understanding.

## Requesting Permissions

If the audio-haptic player needs to trigger vibration, check whether the application has the permission **ohos.permission.VIBRATE**.

1.  [Declare the permission](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).
2.  [Request user authorization](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).

## How to Develop

1.  Obtain an **AudioHapticManager** instance, and register the audio and haptic sources. For details about the sources supported, see [AudioHapticManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-audiohaptic#audiohapticmanager).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/TY9n94b3RYSpY0K9adAFKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A0209E88FA6F5A7EF5DC21078D9E4F99C00E73D3856E9B315C5A21735D032F0)
    
    -   You can register resources using one of the following methods:
        
        Method 1: Use the [registerSource](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-audiohaptic#registersource) API to register resources through file URIs.
        
        Method 2 (recommended): Use [registerSourceFromFd](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-audiohaptic#registersourcefromfd20) to register resources through file descriptors. This API is available from API version 20,
        
    -   A maximum of 128 resources can be registered at the same time for an application. Any attempt to register beyond this limit will fail (returning a negative resource ID). You are advised to reasonably manage the number of registered resources. For resources that are no longer used, you are advised to unregister them in a timely manner.
        
    
    import { audio, audioHaptic } from '@kit.AudioKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { common } from '@kit.AbilityKit';
    
    let audioHapticManagerInstance: audioHaptic.AudioHapticManager = audioHaptic.getAudioHapticManager();
    
    // A maximum of 128 resources can be registered at the same time for an application. Any attempt to register beyond this limit will fail (returning a negative resource ID).
    // You are advised to reasonably manage the number of registered resources. For resources that are no longer used, unregister them in a timely manner.
    
    // Method 1: Use registerSource to register sources.
    let audioUri = 'data/audioTest.wav'; // This is only an example. In actual use, replace the file with the URI of your target audio resource.
    let hapticUri = 'data/hapticTest.json'; // This is only an example. In actual use, replace the file with the URI of your target haptic resource.
    let idForUri = 0;
    
    audioHapticManagerInstance.registerSource(audioUri, hapticUri).then((value: number) => {
      console.info(\`Promise returned to indicate that the source id of the registered source ${value}.\`);
      idForUri = value;
    }).catch((err: BusinessError) => {
      console.error(\`Failed to register source ${err}\`);
    });
    
    // Method 2: Use registerSourceFromFd to register sources.
    let idForFd = 0;
    // Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    
    let audioFile = context.resourceManager.getRawFdSync('audioTest.ogg'); // This is only an example. In actual use, replace the file with the corresponding file in the rawfile directory of the application.
    let audioFd: audioHaptic.AudioHapticFileDescriptor = {
      fd: audioFile.fd,
      offset: audioFile.offset,
      length: audioFile.length,
    };
    
    let hapticFile = context.resourceManager.getRawFdSync('hapticTest.json'); // This is only an example. In actual use, replace the file with the corresponding file in the rawfile directory of the application.
    let hapticFd: audioHaptic.AudioHapticFileDescriptor = {
      fd: hapticFile.fd,
      offset: hapticFile.offset,
      length: hapticFile.length,
    };
    
    audioHapticManagerInstance.registerSourceFromFd(audioFd, hapticFd).then((value: number) => {
      console.info('Succeeded in doing registerSourceFromFd.');
      idForFd = value;
    }).catch((err: BusinessError) => {
      console.error(\`Failed to registerSourceFromFd. Code: ${err.code}, message: ${err.message}\`);
    });
    
2.  Set the parameters of an audio-haptic player. For details, see [AudioHapticManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-audiohaptic#audiohapticmanager).
    
    let latencyMode: audioHaptic.AudioLatencyMode = audioHaptic.AudioLatencyMode.AUDIO\_LATENCY\_MODE\_FAST;
    audioHapticManagerInstance.setAudioLatencyMode(idForFd, latencyMode);
    
    let usage: audio.StreamUsage = audio.StreamUsage.STREAM\_USAGE\_NOTIFICATION;
    audioHapticManagerInstance.setStreamUsage(idForFd, usage);
    
3.  Call [createPlayer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-audiohaptic#createplayer) to create an **AudioHapticPlayer** instance.
    
    let options: audioHaptic.AudioHapticPlayerOptions = {muteAudio: false, muteHaptics: false};
    let audioHapticPlayer: audioHaptic.AudioHapticPlayer | undefined = undefined;
    
    audioHapticManagerInstance.createPlayer(idForFd, options).then((value: audioHaptic.AudioHapticPlayer) => {
      console.info(\`Create the audio haptic player successfully.\`);
      audioHapticPlayer = value;
    }).catch((err: BusinessError) => {
      console.error(\`Failed to create player ${err}\`);
    });
    
4.  Call the [start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-audiohaptic#start) method to start audio playback and vibration at the same time.
    
    audioHapticPlayer.start().then(() => {
      console.info(\`Promise returned to indicate that start playing successfully.\`);
    }).catch((err: BusinessError) => {
      console.error(\`Failed to start playing. ${err}\`);
    });
    
5.  Call the [stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-audiohaptic#stop) method to stop audio playback and vibration at the same time.
    
    audioHapticPlayer.stop().then(() => {
      console.info(\`Promise returned to indicate that stop playing successfully.\`);
    }).catch((err: BusinessError) => {
      console.error(\`Failed to stop playing. ${err}\`);
    });
    
6.  Call the [release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-audiohaptic#release) method to release the **AudioHapticPlayer** instance.
    
    audioHapticPlayer.release().then(() => {
      console.info(\`Promise returned to indicate that release the audio haptic player successfully.\`);
    }).catch((err: BusinessError) => {
      console.error(\`Failed to release the audio haptic player. ${err}\`);
    });
    
7.  Call the [unregisterSource](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-audiohaptic#unregistersource) method to unregister the audio and vibration resources.
    
    // For resources that are no longer used, you are advised to unregister them in a timely manner to avoid issues such as resource leaks, exceeding the maximum allowed number of registered resources, or other such issues.
    audioHapticManagerInstance.unregisterSource(idForFd).then(() => {
      console.info(\`Promise returned to indicate that unregister source successfully\`);
    }).catch((err: BusinessError) => {
      console.error(\`Failed to unregister source ${err}\`);
    });
