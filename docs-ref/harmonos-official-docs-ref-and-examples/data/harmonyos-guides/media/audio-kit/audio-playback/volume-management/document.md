# Volume Management

This module provides capabilities for managing playback volume, covering system volume, application volume, and audio stream volume.

The system volume is managed globally by HarmonyOS and applies to all applications and devices. HarmonyOS categorizes audio into various stream types, each with its own independent system volume control.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/akTMSL4-S9G_YwML3vf6KA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E22089B8A469F50380192291C2AB7D65EB73D9D37E208E25987BCEBCE91E4011)

The system volume can be adjusted using physical volume buttons or through the system settings screen. On the system settings screen, users can individually adjust the volume levels for each type of system volume.

The following lists the common stream types and their corresponding system volumes.

-   Media volume: used for media playback such as music, videos, and games.
-   Call volume: used for voice calls.
-   Ringtone volume: used for incoming call ringtones.
-   Alarm volume: used for alarm notifications.

The application volume is a type of volume control provided by HarmonyOS for third-party applications to manage the volume of all audio streams within that application. Once set, all audio streams initiated by the application will use this volume level by default. In addition, applications with the system application permission can adjust the volume of specific applications by using their UIDs.

The audio stream volume is a volume setting controlled independently by an application and affects only the output volume of the specified audio stream within that application. For example, a media player can control its playback volume independently without affecting the system volume or other types of stream volumes within the application.

The following describes the relationship between the system volume, application volume, and audio stream volume.

-   Hierarchy: The system volume is global, whereas the application volume and audio stream volume are local.
    
    The adjustment range for the application volume and audio stream volume is limited by the system volume. For example, if the system media volume is set to 50% and the application volume is set to 100%, the final output volume of the application can only reach 50%.
    
    The audio stream volume provides more precise control over the application volume. Third-party applications that have set an application volume can further fine-tune the volume of specific audio streams using the audio stream volume.
    
-   Synergy: The final output volume of an application is determined collectively by the system volume, application volume, and audio stream volume. For example, if the system media volume is set to 50%, the application volume is set to 50%, and the application sets the audio stream volume for media audio to 100%, the final output volume of that audio stream will be 25%.
    

HarmonyOS achieves precise volume control for applications through the coordinated use of the system volume, app volume, and audio stream volume.

#### System Volume

The API for managing the system volume is provided by **AudioVolumeManager**. Before using this API, you must call [getVolumeManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiomanager#getvolumemanager9) to obtain an **AudioVolumeManager** instance.

Currently, AudioVolumeManager can be used to obtain volume information and listen for volume changes. It cannot be used to adjust the system volume. If you want to adjust the system volume, follow the instructions provided in [Adjusting the System Volume Using the Volume Panel](#adjusting-the-system-volume-using-the-volume-panel).

import { audio } from '@kit.AudioKit';

let audioManager = audio.getAudioManager();
let audioVolumeManager = audioManager.getVolumeManager();

## Obtaining Volume Information

Call [AudioVolumeManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager) to obtain the volume of a specified audio stream.

The example code is as follows:

import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the volume of a stream.
audioVolumeManager.getVolumeByStream(audio.StreamUsage.STREAM\_USAGE\_MUSIC);

// Obtain the minimum volume of a stream.
audioVolumeManager.getMinVolumeByStream(audio.StreamUsage.STREAM\_USAGE\_MUSIC);

// Obtain the maximum volume of a stream.
audioVolumeManager.getMaxVolumeByStream(audio.StreamUsage.STREAM\_USAGE\_MUSIC);

## Listening for System Volume Changes

You can set an event to listen for system volume changes.

import { audio } from '@kit.AudioKit';

audioVolumeManager.on('streamVolumeChange', audio.StreamUsage.STREAM\_USAGE\_MUSIC, (streamVolumeEvent: audio.StreamVolumeEvent) => {
  console.info(\`Succeeded in using on function. StreamVolumeEvent: ${JSON.stringify(streamVolumeEvent)}\`);
});

## Adjusting the System Volume Using the Volume Panel

An application cannot directly adjust the system volume. However, it can invoke the system volume panel for users to adjust the volume. When the user adjusts the volume, a volume prompt UI is displayed to explicitly notify the user that the system volume changes.

To achieve this, you can use the ArkTS component **AVVolumePanel** in your application. For details, see the [AVVolumePanel Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-multimedia-avvolumepanel).

#### Application Volume

The API for managing the application volume is provided by **AudioVolumeManager**. Before using this API, you must call [getVolumeManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiomanager#getvolumemanager9) to obtain an **AudioVolumeManager** instance.

When [volume mode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#audiovolumemode19) is set to **APP\_INDIVIDUAL**, you can set and query the application volume by calling the APIs in the following sample.

## Adjusting the Application Volume

import { audio } from '@kit.AudioKit';

let audioManager = audio.getAudioManager();
let audioVolumeManager = audioManager.getVolumeManager();

// Set the volume (ranging from 0 to 100) for the application.
audioVolumeManager.setAppVolumePercentage(20).then(() => {
  console.info('Succeeded in setting app volume percentage.');
});

// Query the application volume.
audioVolumeManager.getAppVolumePercentage().then((value: number) => {
  console.info(\`Succeeded in getting app volume percentage, app volume is ${value}.\`);
});

// Subscribe to the application volume change event. For the same event, if the callback parameter passed to the off API is the same as that passed to the on API, the off API cancels the subscription registered with the specified callback parameter.
let appVolumeChangeCallback = (volumeEvent: audio.VolumeEvent) => {
  console.info(\`Succeeded in using on or off function. VolumeEvent: ${JSON.stringify(volumeEvent)}\`);
};
audioVolumeManager.on('appVolumeChange', appVolumeChangeCallback);
audioVolumeManager.off('appVolumeChange', appVolumeChangeCallback);

#### Audio Stream Volume

The **setVolume()** API in both the **AVPlayer** and **AudioRenderer** classes can be used to set the audio stream volume. The code snippet below uses the API in the [AVPlayer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-f#mediacreateavplayer9) class:

let volume = 1.0;  // Specified volume. The value range is \[0.00-1.00\]. The value 1 indicates the maximum volume.
avPlayer.setVolume(volume);

Call [setVolume](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#setvolume9) and [getVolume](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#getvolume12) of [AudioRenderer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-f#audiocreateaudiorenderer8) to set and obtain the volume of the audio stream, respectively.

The example code is as follows:

import { BusinessError } from '@kit.BasicServicesKit';

// Set the volume for the audio stream.
audioRenderer.setVolume(0.5).then(() => {  // The volume range is \[0.0-1.0\].
  console.info('Succeeded in setting volume.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to set volume. Code: ${err.code}, message: ${err.message}\`);
});

// Obtain the volume of the audio stream.
try {
  let value: number = audioRenderer.getVolume();
  console.info(\`Succeeded in getting volume, volume is ${value}.\`);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`Failed to get volume. Code: ${error.code}, message: ${error.message}\`);
}
