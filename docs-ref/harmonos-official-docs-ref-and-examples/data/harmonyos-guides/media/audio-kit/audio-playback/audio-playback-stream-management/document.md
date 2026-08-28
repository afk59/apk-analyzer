# Audio Playback Stream Management

An audio playback application must notice audio stream state changes and perform corresponding operations. For example, when detecting that an audio stream is being played or paused, the application must change the UI display of the **Play** button.

#### Reading or Listening for Audio Stream State Changes in the Application

Create an **AudioRenderer** by referring to [Using AudioRenderer for Audio Playback (ArkTs)](../using-audiorenderer-for-audio-playback-arkts/document.md) or [audio.createAudioRenderer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-f#audiocreateaudiorenderer8). Then obtain the audio stream state changes in either of the following ways.

-   Obtain the [property](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#properties) state of the **AudioRenderer**.
    
    import { audio } from '@kit.AudioKit';
    
    let audioRendererState: audio.AudioState = audioRenderer.state;
    console.info(\`Current state is: ${audioRendererState}\`);
    
-   Register **stateChange** to listen for state changes of the AudioRenderer.
    
    import { audio } from '@kit.AudioKit';
    
    audioRenderer.on('stateChange', (rendererState: audio.AudioState) => {
      console.info(\`Succeeded in using on function, state change to: ${rendererState}\`);
    });
    

The application then performs an operation, for example, changing the display of the **Play** button, by comparing the obtained state with [AudioState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-e#audiostate8).

#### Reading or Listening for Changes in All Audio Streams

If an application needs to obtain the change information about all audio streams, it can use **AudioStreamManager** to read or listen for the changes of all audio streams.

The figure below shows the call relationship of audio stream management.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/QAfvbS2HR7aT_B6oq9tyGg/en-us_image_0000002537765152.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=082512FE6309D6A57A80C36CBCF45965971DA86375220D884339B6E1B869EB45)

During application development, you must call [getStreamManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiomanager#getstreammanager9) to create an **AudioStreamManager** instance, through which you can manage audio streams.

For details about the APIs, see [AudioStreamManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiostreammanager).

#### How to Develop

1.  Create an **AudioStreamManager** instance.
    
    import { audio } from '@kit.AudioKit';
    
    let audioManager = audio.getAudioManager();
    let audioStreamManager = audioManager.getStreamManager();
    
2.  Use [on('audioRendererChange')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiostreammanager#onaudiorendererchange9) to listen for audio playback stream changes. If the application needs to receive a notification when the audio playback stream state or device changes, it can subscribe to this event.
    
    import { audio } from '@kit.AudioKit';
    
    audioStreamManager.on('audioRendererChange',  (audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
      console.info(\`Succeeded in using on function. AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}\`);
    });
    
3.  (Optional) Use [off('audioRendererChange')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiostreammanager#offaudiorendererchange9) to cancel listening for audio playback stream changes.
    
    audioStreamManager.off('audioRendererChange');
    console.info('Succeeded in using off function.');
    
4.  (Optional) Use [getCurrentAudioRendererInfoArray](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiostreammanager#getcurrentaudiorendererinfoarray9) to obtain the information about all audio playback streams. This API can be used to obtain the unique ID of the audio playback stream, audio renderer information, and audio playback device information.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/ZgPwE1x7Q9ejTsrx01tb3Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F11EB402268A30440F7EBE6F8E17397AA6618D5321A79336C70979DA1FE4489A)
    
    Before listening for state changes of all audio streams, the application must [declare the ohos.permission.USE\_BLUETOOTH permission](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md), for the device name and device address (Bluetooth related attributes) to be displayed correctly.
    
    import { audio } from '@kit.AudioKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    async function getCurrentAudioRendererInfoArray(): Promise<void> {
      await audioStreamManager.getCurrentAudioRendererInfoArray().then((audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
        console.info(\`Succeeded in getting current audio renderer info array. AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}\`);
      }).catch((err: BusinessError ) => {
        console.error(\`Failed to get current audio renderer info array. Code: ${err.code}, message: ${err.message}\`);
      });
    }
