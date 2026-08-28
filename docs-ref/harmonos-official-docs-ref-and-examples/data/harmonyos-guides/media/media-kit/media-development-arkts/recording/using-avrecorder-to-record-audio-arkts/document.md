# Using AVRecorder to Record Audio (ArkTS)

In this topic, you will learn how to use [AVRecorder](../../../about-this-kit/document.md#avrecorder) to develop audio recording functionalities including starting, pausing, resuming, and stopping recording.

During application development, you can use the **state** property of AVRecorder to obtain its current state or use [on('stateChange')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#onstatechange9) to listen for state change events. During development, you must strictly comply with the state machine requirements. For example, you can call the [pause](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#pause9-1) API only in the **started** state and call the [resume](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#resume9-1) API only in the **paused** state.

**Figure 1** Recording state transition

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/9Ypjn0t1TKiqFOSRW3An_A/en-us_image_0000002568764915.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062042Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=961C6B153F8297B0B8552E02329D9B6F27310E9B565E7786F2EDF8E374AE7661)

For details about the states, see [AVRecorderState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-t#avrecorderstate9).

#### Requesting Permissions

Before your development, configure the following permissions for your application.

-   To use the microphone, request the ohos.permission.MICROPHONE permission. For details about how to request user authorization, see [Requesting User Authorization](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).
-   To read and save audio files, preferentially use [AudioViewPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#audioviewpicker).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/5Oa9m8oyTBW7m22CbLRlrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062042Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1689CB5AB62A166A4347E93C147F02F302AFFAF368D4A450FB6E9256F901FC83)

To clone, back up, or synchronize audio files in users' public directory, request the ohos.permission.READ\_AUDIO and ohos.permission.WRITE\_AUDIO permissions for reading and writing audio files. For details, see [Requesting Restricted Permissions](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md), which can be used only after being approved by AppGallery Connect (AGC). To prevent the application release request from being rejected, you are advised to use alternative solutions such as Pickers and components preferentially. Restricted permissions are granted only when the [related conditions are met](../../../../../system/security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md#ohospermissionread_audio)..

#### Precautions for Developing Audio Recording Applications

-   If continuous recording or background recording is required, the application must request a continuous task to prevent it from being suspended. For details, see [Continuous Task](../../../../../application-framework/background-tasks-kit/continuous-task-arkts/document.md).
-   The application must start recording when it runs in the foreground. It can switch to the background after the recording is started. Recording cannot be started in the background.
-   To record audio, the application must use an appropriate recording stream type. For details, see [Selecting the Appropriate Audio Stream Types](../../../../audio-kit/selecting-the-appropriate-audio-stream-types/document.md).

#### How to Develop

Read [AVRecorder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder) for the API reference.

1.  Create an AVRecorder instance. The AVRecorder is in the **idle** state.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/zRqX8T2cSZ6qE2yvxT1znA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062042Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E714B90528A29AFBCA21A58DC63FE91D119332D96830AD119493CF975C52946)
    
    Perform the subsequent operations after the AVRecorder completes value assignment.
    
    import { media } from '@kit.MediaKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    private avRecorder: media.AVRecorder | undefined = undefined;
    
    try {
      this.avRecorder = await media.createAVRecorder();
    } catch (err) {
      let error: BusinessError = err as BusinessError;
      console.error(\`Failed to create avRecorder, error code: ${error.code}, message: ${error.message}\`);
    }
    
2.  Set the events to listen for.
    
    | Event Type | Description |
    | :-- | :-- |
    | stateChange | Mandatory; used to listen for changes of the **state** property of the AVRecorder. |
    | error | Mandatory; used to listen for AVRecorder errors. |
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    // Callback function for state changes.
    this.avRecorder?.on('stateChange', (state: media.AVRecorderState, reason: media.StateChangeReason) => {
      console.info(\`AVRecorder state is changed to ${state}, reason: ${reason}\`);
      // You can add the action to be performed after the state is switched.
    });
    
    // Callback function for errors.
    this.avRecorder?.on('error', (error) => {
      console.error(\`Error occurred in avRecorder, error code: ${error.code}, message: ${error.message}\`);
    });
    
3.  Set audio recording parameters and call [prepare](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#prepare9-1) to enter the **prepared** state.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/xPA2wPTqR8mk00Y_A69ZPw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062042Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DF37BBCACE540CEF341E293FBBDB5083FE7D70A0200053E3BF49A0CF2EACF59)
    
    Pay attention to the following when configuring parameters:
    
    -   Before parameter configuration, ensure that you have gained the required permissions. For details, see [Requesting Permissions](#requesting-permissions).
        
    -   In pure audio recording scenarios, set only audio-related parameters in **avConfig** of **prepare()**.
        
        If video recording is required, follow the instructions provided in [Video Recording Development](../using-avrecorder-to-record-videos-arkts/document.md). If video-related parameters are configured, an error will be reported in subsequent steps.
        
    -   The [recording specifications](../../../about-this-kit/document.md#supported-formats) in use must be those supported. The specific recording parameters must strictly comply with the specified [recording parameter configuration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-i#avrecorderprofile9).
        
    -   The recording output URL (URL in **avConfig** in the sample code) must be in the format of fd://xx (where xx indicates a file descriptor). You must call [ohos.file.fs of Core File Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs) to implement access to the application file. For details, see [Accessing Application Files](../../../../../application-framework/core-file-kit/application-files/application-file-access-and-management/accessing-application-files-arkts/document.md).
        
    -   For details about the audio encoding format (**audioCodec**), extended audio encoding format (**aacProfile**), and encapsulation format (**fileFormat**) configured in the example, see [AVRecorderProfile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-i#avrecorderprofile9).
        
    
    import { media } from '@kit.MediaKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { fileIo as fs } from '@kit.CoreFileKit';
    
    let avProfile: media.AVRecorderProfile = {
      audioBitrate: 112000, // Audio bit rate.
      audioChannels: 2, // Number of audio channels.
      audioCodec: media.CodecMimeType.AUDIO\_AAC, // Audio encoding format.
      aacProfile: media.AacProfile.AAC\_HE, // Extended audio encoding format.
      audioSampleRate: 48000, // Audio sampling rate.
      fileFormat: media.ContainerFormatType.CFT\_MPEG\_4A, // Encapsulation format.
    };
    
    const context: Context = this.getUIContext().getHostContext()!; // Refer to Accessing Application Files.
    let filePath: string = context.filesDir + '/example.mp3';
    let audioFile: fs.File = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
    let fileFd: number = audioFile.fd; // Obtain the file FD.
     
    let avConfig: media.AVRecorderConfig = {
      audioSourceType: media.AudioSourceType.AUDIO\_SOURCE\_TYPE\_MIC, // Audio input source. In this example, the microphone is used.
      profile: avProfile,
      url: 'fd://' + fileFd.toString(), // Obtain the file descriptor of the created audio file by referring to the sample code in Application File Access and Management.
    };
    
    try {
      await this.avRecorder?.prepare(avConfig);
      console.info('Succeeded in preparing avRecorder');
    } catch (err) {
      let error: BusinessError = err as BusinessError;
      console.error(\`Failed to prepare avRecorder, error code: ${error.code}, message: ${error.message}\`);
    }
    
4.  Call [start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#start9-1) to start recording and enter the **started** state.
    
    // Start recording.
    await this.avRecorder?.start();
    
5.  Call [pause](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#pause9-1) to pause recording and enter the **paused** state.
    
    // Pause recording.
    await this.avRecorder?.pause();
    
6.  Call [resume](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#resume9-1) to resume recording and enter the **started** state again.
    
    // Resume recording.
    await this.avRecorder?.resume();
    
7.  Call [stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#stop9-1) to stop recording and enter the **stopped** state.
    
    // Stop recording.
    await this.avRecorder?.stop();
    
8.  Call [reset](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#reset9-1) to reset resources and enter the **idle** state again. Recording parameters can be configured again.
    
    // Reset resources.
    await this.avRecorder?.reset();
    
9.  Call [release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#release9-1) to release the instance, enter the **released** state, and exit recording.
    
    // Destroy the instance.
    await this.avRecorder?.release();
    

#### Complete Sample Code

Refer to the sample code below to complete the process of starting, pausing, resuming, and stopping recording.

Before using the sample code, you need to apply for the ohos.permission.MICROPHONE microphone permission. For details about how to request user authorization, see [Requesting User Authorization](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).

import { common } from '@kit.AbilityKit';
import { media } from '@kit.MediaKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function audioRecording(context: common.Context): Promise<void> {
  // Create an AVRecorder instance named avRecorder.
  let avRecorder: media.AVRecorder | undefined = undefined;
  try {
    avRecorder = await media.createAVRecorder();
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to create avRecorder, error code: ${err.code}, message: ${err.message}\`);
    return;
  }
  
  // Set AVRecorder callback functions.
  try {
    // Callback for state changes.
    avRecorder.on('stateChange', (state: media.AVRecorderState, reason: media.StateChangeReason) => {
      console.info(\`AVRecorder state is changed to ${state}, reason: ${reason}\`);
    });
    // Callback function for errors.
    avRecorder.on('error', (error: BusinessError) => {
      console.error(\`Error occurred in avRecorder, error code: ${error.code}, message: ${error.message}\`);
    });
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to set avRecorder callback, error code: ${err.code}, message: ${err.message}\`);
  }

  let avProfile: media.AVRecorderProfile = {
    audioBitrate: 112000, // Audio bit rate.
    audioChannels: 2, // Number of audio channels.
    audioCodec: media.CodecMimeType.AUDIO\_AAC, // Audio encoding format.
    aacProfile: media.AacProfile.AAC\_HE, // Extended audio encoding format.
    audioSampleRate: 48000, // Audio sampling rate.
    fileFormat: media.ContainerFormatType.CFT\_MPEG\_4A, // Encapsulation format.
  };
  let avConfig: media.AVRecorderConfig = {
    audioSourceType: media.AudioSourceType.AUDIO\_SOURCE\_TYPE\_MIC, // Audio input source. In this example, the microphone is used.
    profile: avProfile,
    url: 'fd://35', // Create, read, and write a file by referring to the sample code in Application File Access and Management.
  };

  // Create a file and set avConfig.url.
  let audioFile: fs.File | undefined = undefined;
  try {
    let path: string = context.filesDir + '/example.mp3'; // File sandbox path. The file name extension must match the container format.
    audioFile = fs.openSync(path, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE); // Open the file.
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to open file, error code: ${err.code}, message: ${err.message}\`);
  }
  if (audioFile !== undefined) {
    avConfig.url = 'fd://' + audioFile.fd; // Update the URL.
  }
  
  // Set recording parameters to complete the preparations.
  try {
    if (avRecorder.state === 'idle' || avRecorder.state === 'stopped') { // prepare() can be called only when the AVRecorder is in the idle or stopped state.
      await avRecorder.prepare(avConfig);
    }
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to prepare avRecorder, error code: ${err.code}, message: ${err.message}\`);
  }

  // Start recording.
  try {
    if (avRecorder.state === 'prepared') { // start() can be called only when the AVRecorder is in the prepared state.
      await avRecorder.start();
    }
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to start avRecorder, error code: ${err.code}, message: ${err.message}\`);
  }

  // Pause recording.
  try {
    if (avRecorder.state === 'started') { // pause() can be called only when the AVRecorder is in the started state.
      await avRecorder.pause();
    }
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to pause avRecorder, error code: ${err.code}, message: ${err.message}\`);
  }

  // Resume recording.
  try {
    if (avRecorder.state === 'paused') { // resume() can be called only when the AVRecorder is in the paused state.
      await avRecorder.resume();
    }
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to resume avRecorder, error code: ${err.code}, message: ${err.message}\`);
  }

  // Stop recording.
  try {
    if (avRecorder.state === 'started' || avRecorder.state === 'paused') { // stop() can be called only when the AVRecorder is in the started or paused state.
      await avRecorder.stop();
    }
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to stop avRecorder, error code: ${err.code}, message: ${err.message}\`);
  }
  
  // Reset recording.
  try {
    await avRecorder.reset();
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to reset avRecorder, error code: ${err.code}, message: ${err.message}\`);
  }

  // Release the AVRecorder instance.
  try {
    await avRecorder.release();
    avRecorder = undefined;
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to release avRecorder, error code: ${err.code}, message: ${err.message}\`);
  }

  // Close the file descriptor of the recording file.
  try {
    if (audioFile !== undefined) {
      await fs.close(audioFile.fd);
    }
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to close fd, error code: ${err.code}, message: ${err.message}\`);
  }
}
