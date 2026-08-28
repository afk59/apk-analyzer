# Using AVScreenCaptureRecorder to Record Screens and Write Them to Files (ArkTS)

Screen capture is mainly used to record the main screen.

You can call the ArkTS APIs of the [AVScreenCaptureRecorder](../../../about-this-kit/document.md#avscreencapture) module to record the screen and collect audio and video source data output by the device and microphone. You can call the APIs to obtain audio and video files and transfer the files to other modules for playback or processing. In this way, screen content can be shared in the form of files.

The AVScreenCaptureRecorder, Window, and Graphics modules together implement the entire video capture process.

The full-screen capture process involves creating an AVScreenCaptureRecorder instance, configuring audio and video capture parameters, starting and stopping screen capture, and releasing resources.

If you are in a call when screen capture starts or a call is coming during screen capture, screen capture automatically stops, and the **SCREENCAPTURE\_STATE\_STOPPED\_BY\_CALL** status is reported.

This topic describes how to use the AVScreenCaptureRecorder APIs to carry out one-time screen capture. For details about the API reference, see [AVScreenCaptureRecorder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avscreencapturerecorder).

If microphone data collection is configured, configure the permission ohos.permission.MICROPHONE and request a continuous task. For details, see [Requesting User Authorization](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md) and [Continuous Task](../../../../../application-framework/background-tasks-kit/continuous-task-arkts/document.md).

#### Applying for Permission

Before your development, configure the following permissions for your application.

-   To use the microphone, request the ohos.permission.MICROPHONE permission. For details about how to request user authorization, see [Requesting User Authorization](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).
-   To read images or videos, preferentially use the media library [Picker for access](../../../../media-library-kit/selecting-media-assets-using-picker/document.md).
-   To save images or videos, preferentially use the [security component for storage](../../../../media-library-kit/saving-media-assets/document.md).
-   Starting from API version 22, when you perform screen capture for an application on a PC/2-in-1 device, you can request the ohos.permission.TIMEOUT\_SCREENOFF\_DISABLE\_LOCK permission to maintain capture even when the screen is off but not locked. For details about the configuration, [Declaring Permissions](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).
-   Starting from API version 22, when you perform screen capture for an application on a PC/2-in-1 device, you can request the ohos.permission.CUSTOM\_SCREEN\_RECORDING permission to prevent the privacy protection pop-up from being displayed during screen capture. For details about how to request the permission, see [Requesting Restricted Permissions](../../../../../system/security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/V1y7SuqdRaOFgblNXGsoeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062042Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=146281C089C08A4C10F08C29C64A1CF2F6D7BE2BCF20F7F9C96ABE3AD7D4EE15)
    
    To clone, back up, or synchronize images and videos in users' public directory, request the ohos.permission.READ\_IMAGEVIDEO and ohos.permission.WRITE\_IMAGEVIDEO permissions for reading and writing audio files. For details, see [Requesting Restricted Permissions](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md), which can be used only after being approved by AppGallery Connect (AGC). To prevent the application release request from being rejected, you are advised to use alternative solutions such as Pickers and components preferentially. Restricted permissions are granted only when the [related conditions are met](../../../../../system/security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md#ohospermissionread_imagevideo)..
    

#### How to Develop

After an AVScreenCaptureRecorder instance is created, different APIs can be called to switch the AVScreenCaptureRecorder to different states and trigger the required behavior. If an API is called when the AVScreenCaptureRecorder is not in the given state, the system may throw an exception or generate other undefined behavior. Therefore, you are advised to check the AVScreenCaptureRecorder state before triggering state transition.

1.  Add the header files.
    
    import { common } from '@kit.AbilityKit';
    import { media } from '@kit.MediaKit';
    import { fileIo as fs } from '@kit.CoreFileKit';
    
2.  Create the member variable **screenCapture** of the **AVScreenCaptureRecorder** type.
    
    // Declare a member variable of the AVScreenCaptureRecorder type.
    private screenCapture?: media.AVScreenCaptureRecorder;
    // Create an AVScreenCaptureRecorder instance and assign a value to the member variable screenCapture.
    this.screenCapture = await media.createAVScreenCaptureRecorder();
    
3.  Set callback functions for the member variable **screenCapture** to listen for state changes and errors.
    
    this.screenCapture.on('stateChange', async (infoType: media.AVScreenCaptureStateCode) => {
      switch (infoType) {
            case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_STARTED:
                console.info("Callback invoked when screen capture starts");
                break;
            case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_CANCELED:
                this.screenCapture?.release();
                this.screenCapture = undefined;
                console.info("Screen capture is not allowed.");
                break;
            case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_STOPPED\_BY\_USER:
                this.screenCapture?.release();
                this.screenCapture = undefined;
                console.info("Touch the button in the screen capture capsule to stop screen capture. Underlying capture will stop.");
                break;
            case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_INTERRUPTED\_BY\_OTHER:
                console.info("Screen capture stops due to other interruptions. Underlying capture will stop.");
                break;
            case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_STOPPED\_BY\_CALL:
                console.info("Screen capture stops due to incoming calls. Underlying capture will stop.");
                break;
            case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_MIC\_UNAVAILABLE:
                console.info("The screen capture microphone is unavailable.");
                break;
            case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_MIC\_MUTED\_BY\_USER:
                console.info("The screen capture microphone is muted by the user.");
                break;
            case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_MIC\_UNMUTED\_BY\_USER:
                console.info("The screen capture microphone is unmuted by the user.");
                break;
            case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_ENTER\_PRIVATE\_SCENE:
                // Currently, you can directly register a listener from the system to enter the privacy scenario.
                console.info("Screen capture enters the privacy scenario.");
                break;
            case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_EXIT\_PRIVATE\_SCENE:
                console.info("Screen capture exits the privacy scenario.");
                break;
            case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_STOPPED\_BY\_USER\_SWITCHES:
                console.info("Underlying capture will stop after the user account is changed.");
                break;
            default:
                break;
        }
    })
    this.screenCapture.on('error', (err) => {
        console.error(\`Handle exceptions, code is ${err.code}, message is ${err.message}.\`);
    })
    
4.  Set screen capture parameters.
    
    ​After creating the screenCapture instance, you can set the parameters required for screen capture.
    
    ​Parameters **videoBitrate**, **audioSampleRate**, **audioChannelCount**, **audioBitrate**, **preset**, and **displayId** are optional, with default values provided in the code snippet below. The audio streams of the microphone and system sound share a set of audio parameters: **audioSampleRate**, **audioChannelCount**, and **audioBitrate**.
    
    You can create, read, and write a file descriptor by referring to the sample code in [Accessing Application Files](../../../../../application-framework/core-file-kit/application-files/application-file-access-and-management/accessing-application-files-arkts/document.md) to obtain the value of the **fd** parameter. The **getFileFd()** API provided in the example below is for reference only.
    
    If **displayId** is set to the extended display ID of a 2-in-1 device, a dialog box for screen capture selection can be opened. Users can select the screen to capture in the dialog box, and the recorded content will match the user's choices.
    
    const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let filePath: string = context.filesDir + '/screenCapture.mp4';
    let captureFile: fs.File = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
    if (!captureFile) {
      console.error("Handle exceptions.");
      return;
    }
    
    captureConfig: media.AVScreenCaptureRecordConfig = {
        // Set the width and height as required.
        frameWidth: 768,
        frameHeight: 1280,
        // Create, read, and write a file descriptor by referring to the sample code in Accessing Application Files.
        fd: captureFile.fd,
        // Optional parameters and their default values
        videoBitrate: 10000000,
        audioSampleRate: 48000,
        audioChannelCount: 2,
        audioBitrate: 96000,
        displayId: 0,
        preset: media.AVScreenCaptureRecordPreset.SCREEN\_RECORD\_PRESET\_H264\_AAC\_MP4
    };
    
5.  Call [init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avscreencapturerecorder#init12) to initialize **screenCapture** based on the preconfigured screen recording parameters.
    
    await this.screenCapture.init(this.captureConfig);
    
6.  Set the windows that will be skipped during screen capture, by entering the subwindow IDs and main window IDs. For details, see [Window API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-i#windowproperties).
    
    let windowIDs = \[57, 86\];
    await this.screenCapture.skipPrivacyMode(windowIDs);
    
7.  Call [startRecording](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avscreencapturerecorder#startrecording12) to start screen capture and use a listener to monitor state change events.
    
    await this.screenCapture.startRecording();
    
8.  Stop screen capture.
    
    -   After the user taps the stop button in the screen capture capsule to stop screen capture, the **screenCapture** instance triggers the **SCREENCAPTURE\_STATE\_STOPPED\_BY\_USER** callback to notify the application that screen capture has been stopped. You do not need to call the [stopRecording](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avscreencapturerecorder#stoprecording12) method.
        
    -   The application proactively calls [stopRecording](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avscreencapturerecorder#stoprecording12) to stop screen capture.
        
        await this.screenCapture.stopRecording();
        
9.  Call [release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avscreencapturerecorder#release12) to release the instance.
    
    await this.screenCapture.release();
    

#### Complete Sample Code

The following is the complete sample code for capturing a screen and saving the screen data captured to a file using **AVScreenCaptureRecorder**.

import { media } from '@kit.MediaKit';
import { fileIo as fs } from '@kit.CoreFileKit';

export class AVScreenCaptureDemo {
  private screenCapture?: media.AVScreenCaptureRecorder;
  private captureFile: fs.File | undefined = undefined;
  private captureConfig: media.AVScreenCaptureRecordConfig | undefined = undefined;

  private openFile(context: Context): void {
    const path: string = context.filesDir + '/screenCapture.mp4'; // File sandbox path. The file name extension must match the encapsulation format.
    this.captureFile = fs.openSync(path, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
  }

  private closeFile(): void {
    if (!this.captureFile) {
      return;
    }
    fs.closeSync(this.captureFile);
  }

  private setConfig(): void {
    if (!this.captureFile) {
      return;
    }
    this.captureConfig = {
        // Set the width and height as required.
        frameWidth: 768,
        frameHeight: 1280,
        // Create, read, and write a file descriptor by referring to the sample code in Accessing Application Files.
        fd: this.captureFile.fd,
        // Optional parameters and their default values
        videoBitrate: 10000000,
        audioSampleRate: 48000,
        audioChannelCount: 2,
        audioBitrate: 96000,
        displayId: 0,
        preset: media.AVScreenCaptureRecordPreset.SCREEN\_RECORD\_PRESET\_H264\_AAC\_MP4
      };
  }

  // Register the screenCapture callback function.
  private registerScreenCaptureCallback(): void {
    this.screenCapture?.on('stateChange', async (infoType: media.AVScreenCaptureStateCode) => {
      switch (infoType) {
        case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_STARTED:
          console.info("Callback invoked when screen capture starts");
          break;
        case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_CANCELED:
          this.screenCapture?.release();
          this.screenCapture = undefined;
          console.info("Screen capture is not allowed.");
          break;
        case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_STOPPED\_BY\_USER:
          this.screenCapture?.release();
          this.screenCapture = undefined;
          console.info("Touch the button in the screen capture capsule to stop screen capture. Underlying capture will stop.");
          break;
        case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_INTERRUPTED\_BY\_OTHER:
          console.info("Screen capture stops due to other interruptions. Underlying capture will stop.");
          break;
        case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_STOPPED\_BY\_CALL:
          console.info("Screen capture stops due to incoming calls. Underlying capture will stop.");
          break;
        case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_MIC\_UNAVAILABLE:
          console.info("The screen capture microphone is unavailable.");
          break;
        case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_MIC\_MUTED\_BY\_USER:
          console.info("The screen capture microphone is muted by the user.");
          break;
        case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_MIC\_UNMUTED\_BY\_USER:
          console.info("The screen capture microphone is unmuted by the user.");
          break;
        case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_ENTER\_PRIVATE\_SCENE:
          // Currently, you can directly register a listener from the system to enter the privacy scenario.
          console.info("Screen capture enters the privacy scenario.");
          break;
        case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_EXIT\_PRIVATE\_SCENE:
          console.info("Screen capture exits the privacy scenario.");
          break;
        case media.AVScreenCaptureStateCode.SCREENCAPTURE\_STATE\_STOPPED\_BY\_USER\_SWITCHES:
          console.info("Underlying capture will stop after the user account is changed.");
          break;
        default:
          break;
      }
    })
    this.screenCapture?.on('error', (err) => {
      console.error(\`Handle exceptions, code is ${err.code}, message is ${err.message}.\`);
    })
  }

  // Unregister the screenCapture callback function.
  private unRegisterScreenCaptureCallback(): void {
    this.screenCapture?.off('stateChange');
    this.screenCapture?.off('error');
  }

  // Call startRecording to start screen capture. To stop screen capture, click the stop button in the screen capture capsule.
  async startRecording(context: Context): Promise<void> {
    this.screenCapture = await media.createAVScreenCaptureRecorder();
    if (!this.screenCapture) {
      // failed.
      return;
    }
    this.openFile(context);
    if (!this.captureFile) {
      console.error("Handle exceptions.");
      return;
    }
    this.setConfig();
    await this.screenCapture?.init(this.captureConfig);

    this.registerScreenCaptureCallback();
    // Exempt privacy windows.
    let windowIDs = \[57, 86\];
    await this.screenCapture?.skipPrivacyMode(windowIDs);

    await this.screenCapture?.startRecording();
  }

  // Proactively call stopRecording to stop screen capture.
  async stopRecording(): Promise<void> {
    if (!this.screenCapture) {
      // Error.
      this.closeFile();
      return;
    }

    await this.screenCapture?.stopRecording();
    this.unRegisterScreenCaptureCallback();
    // Call release() to release the instance.
    await this.screenCapture?.release();

    // Close the created screen recording file.
    this.closeFile();
  }
}
