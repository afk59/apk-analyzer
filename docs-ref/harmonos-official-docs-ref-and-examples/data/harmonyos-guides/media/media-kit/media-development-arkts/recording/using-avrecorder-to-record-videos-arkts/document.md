# Using AVRecorder to Record Videos (ArkTS)

You can use the [AVRecorder](../../../about-this-kit/document.md#avrecorder) to develop the video recording service. The AVRecorder supports audio capture, audio encoding, video encoding, audio encapsulation, and video encapsulation. It is applicable to simple video recording scenarios and can be used to generate local video files directly.

In this topic, you will learn how to use the AVRecorder to complete the process of starting, pausing, resuming, and stopping video recording.

During application development, you can use the **state** property of AVRecorder to obtain its current state or use [on('stateChange')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#onstatechange9) to listen for state change events. During development, you must strictly comply with the state machine requirements. For example, you can call the [pause](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#pause9-1) API only in the **started** state and call the [resume](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#resume9-1) API only in the **paused** state.

**Figure 1** Recording state transition

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/2zcZlZrHQziWq2a66GQvJg/en-us_image_0000002537765190.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062042Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2D6CCE2B259F95FC40ED13FE35D4C9357575DC1FA4C895BF3E611BBCF244D44)

For details about the states, see [AVRecorderState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-t#avrecorderstate9).

#### Requesting Permissions

Before your development, configure the following permissions for your application.

-   To use the microphone, request the ohos.permission.MICROPHONE permission. For details about how to request user authorization, see [Requesting User Authorization](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).
-   To use the camera for photo capture, request the ohos.permission.CAMERA permission. For details about how to request user authorization, see [Requesting User Authorization](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).
-   To read images or videos from Gallery, preferentially use the media library [Picker for access](../../../../media-library-kit/selecting-media-assets-using-picker/document.md).
-   To save images or videos to Gallery, preferentially use the [security component for storage](../../../../media-library-kit/saving-media-assets/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/1o68gYrgRyKPHL8t5EOJ_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062042Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9255DB7788876C8D8E9F6381D14C60286AB54B9DD03B0EC3EE74F5F508B7C95)

To clone, back up, or synchronize images and videos in users' public directory, request the ohos.permission.READ\_IMAGEVIDEO and ohos.permission.WRITE\_IMAGEVIDEO permissions for reading and writing audio files. For details, see [Requesting Restricted Permissions](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md), which can be used only after being approved by AppGallery Connect (AGC). To prevent the application release request from being rejected, you are advised to use alternative solutions such as Pickers and components preferentially. Restricted permissions are granted only when the [related conditions are met](../../../../../system/security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md#ohospermissionread_imagevideo)..

#### How to Develop

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/74Q3pCVIRjqS4Zbj-aSH9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062042Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84947625A70F4CFD3F418958C288858790148BCC2A10EAB8BF5DD48736EF66E2)

The AVRecorder only processes video data. To complete video recording, it must work with the video data collection module, which transfers the captured video data to the AVRecorder for data processing through the surface. Currently, the mainstream data collection module is the camera module. For details about the implementation, see [Video Recording](../../../../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/video-recording-arkts/document.md).

For details about how to create and save a file, see [Accessing Application Files](../../../../../application-framework/core-file-kit/application-files/application-file-access-and-management/accessing-application-files-arkts/document.md). By default, files are saved in the sandbox path of the application. To save them to Gallery, use the [security components](../../../../media-library-kit/saving-media-assets/document.md).

Read [AVRecorder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder) for the API reference.

1.  Create an AVRecorder instance. The AVRecorder is in the **idle** state.
    
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
    
    import { media } from '@kit.MediaKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    // Callback function for state changes.
    this.avRecorder?.on('stateChange', (state: media.AVRecorderState, reason: media.StateChangeReason) => {
      console.info(\`AVRecorder state is changed to ${state}, reason: ${reason}\`);
    });
    // Callback function for errors.
    this.avRecorder?.on('error', (error: BusinessError) => {
      console.error(\`Error occurred in avRecorder, error code: ${error.code}, message: ${error.message}\`);
    });
    
3.  Set video recording parameters and call [prepare](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#prepare9-1) to enter the **prepared** state.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/1GEv1vlRQ4itoN_3xjwQEA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062042Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D99AE56B898B61BF931888BDFB726540093A6D0D8E03DA3E3B76EF086D74734A)
    
    Pay attention to the following when configuring parameters:
    
    -   Before parameter configuration, ensure that you have gained the required permissions. For details, see [Requesting Permissions](#requesting-permissions).
        
    -   In pure video recording scenarios, set only video-related parameters in **avConfig** of **prepare()**.
        
        If audio-related parameters are configured, the system regards it as audio and video recording.
        
    -   The [recording specifications](../../../about-this-kit/document.md#supported-formats) in use must be those supported. The video bit rate, resolution, and frame rate are subject to the ranges supported by the hardware device.
        
    -   The recording output URL (URL in **avConfig** in the sample code) must be in the format of fd://xx (where xx indicates a file descriptor). You must call [ohos.file.fs of Core File Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs) to implement access to the application file. For details, see [Accessing Application Files](../../../../../application-framework/core-file-kit/application-files/application-file-access-and-management/accessing-application-files-arkts/document.md).
        
    -   For details about the video file encapsulation format (**fileFormat**) and video encoding format (**videoCodec**) configured in the sample code, see [AVRecorderProfile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-i#avrecorderprofile9).
        
    
    import { media } from '@kit.MediaKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { fileIo as fs } from '@kit.CoreFileKit';
    
    let avProfile: media.AVRecorderProfile = {
      fileFormat: media.ContainerFormatType.CFT\_MPEG\_4, // Video file encapsulation format.
      videoBitrate: 200000, // Video bit rate.
      videoCodec: media.CodecMimeType.VIDEO\_AVC, // Video file encoding format.
      videoFrameWidth: 640, // Video frame width.
      videoFrameHeight: 480, // Video frame height.
      videoFrameRate: 30 // Video frame rate
    };
    
    let videoMetaData: media.AVMetadata = {
      videoOrientation: '0' // Video rotation angle. The default value is 0, indicating that the video is not rotated. The value can be 0, 90, 180, or 270.
    };
    
    const context: Context = this.getUIContext().getHostContext()!; // Refer to Accessing Application Files.
    let filePath: string = context.filesDir + '/example.mp4';
    let videoFile: fs.File = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
    let fileFd: number = videoFile.fd; // Obtain the file FD.
    
    let avConfig: media.AVRecorderConfig = {
      videoSourceType: media.VideoSourceType.VIDEO\_SOURCE\_TYPE\_SURFACE\_YUV, // Video source type. YUV and ES are supported.
      profile: avProfile,
      url: 'fd://' + fileFd.toString(), // Create, read, and write a video file by referring to the sample code in Application File Access and Management.
      metadata: videoMetaData
    };
    
    try {
      await this.avRecorder?.prepare(avConfig);
      console.info('Succeeded in preparing avRecorder');
    } catch (err) {
      let error: BusinessError = err as BusinessError;
      console.error(\`Failed to prepare avRecorder, error code: ${error.code}, message: ${error.message}\`);
    }
    
4.  Obtain the surface ID required for video recording.
    
    Call [getInputSurface](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#getinputsurface9-1). The surface ID in the return value is passed to the video data input source module. Camera is a commonly used video data input source, as shown in the sample code.
    
    The video data collection module obtains the surface based on the surface ID and transmits video data to the AVRecorder through the surface. Then the AVRecorder processes the video data.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    this.avRecorder?.getInputSurface().then((surfaceId: string) => {
      console.info('Succeeded in getting input surface');
    }, (error: BusinessError) => {
      console.error(\`Failed to get input surface, error code: ${error.code}, message: ${error.message}\`);
    });
    
5.  Initialize the video data input source. This step is performed in the video data collection module. For the camera module, you need to create a Camera instance, obtain the camera list, create a camera input stream, and create a video output stream. For details, see [Video Recording](../../../../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/video-recording-arkts/document.md).
    
6.  Start recording. Start the input source to input video data, for example, by calling **camera.VideoOutput.start** of the camera module. Call [start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#start9-1). The AVRecorder enters the **started** state.
    
7.  Call [pause](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#pause9-1) to pause the recording. The AVRecorder enters the **paused** state, and the input source stops inputting data. For example, the camera module calls **camera.VideoOutput.stop** to stop the input of camera video data.
    
8.  Call [resume](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#resume9-1) to resume recording. The AVRecorder enters the **started** state again.
    
9.  Call [stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#stop9-1) to stop recording. The AVRecorder enters the **stopped** state and the camera stops recording.
    
10.  Call [reset](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#reset9-1) to reset resources. The AVRecorder enters the **idle** state and recording parameters can be configured again.
     
11.  Call [release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#release9-1) to release the instance. The AVRecorder enters the **released** state, exits recording, and releases resources related to the video data input source, such as camera resources.
     

#### Complete Sample Code

Refer to the sample code below to complete the process of starting, pausing, resuming, and stopping recording.

import { common } from '@kit.AbilityKit';
import { camera } from '@kit.CameraKit';
import { media } from '@kit.MediaKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs, fileUri } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function videoRecording(context: common.Context): Promise<void> {
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

  // Set recording parameters to complete the preparations.
  let avProfile: media.AVRecorderProfile = {
    fileFormat: media.ContainerFormatType.CFT\_MPEG\_4, // Video file encapsulation format.
    videoBitrate: 100000, // Video bit rate.
    videoCodec: media.CodecMimeType.VIDEO\_AVC, // Video file encoding format.
    videoFrameWidth: 640, // Video frame width.
    videoFrameHeight: 480, // Video frame height.
    videoFrameRate: 30 // Video frame rate
  };
  let videoMetaData: media.AVMetadata = {
    videoOrientation: '0' // Video rotation angle. The default value is 0, indicating that the video is not rotated. The value can be 0, 90, 180, or 270.
  };
  let avConfig: media.AVRecorderConfig = {
    videoSourceType: media.VideoSourceType.VIDEO\_SOURCE\_TYPE\_SURFACE\_YUV, // Video source type. YUV and ES are supported.
    profile: avProfile,
    url: 'fd://35', // Create, read, and write a file by referring to the sample code in Application File Access and Management.
    metadata: videoMetaData
  };

  // Create a file and set avConfig.url.
  let filePath: string = ''; // File path.
  let videoFile: fs.File | undefined = undefined;
  try {
    filePath = context.filesDir + '/example.mp4'; // File sandbox path. The file name extension must match the encapsulation format.
    videoFile = fs.openSync(filePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE); // Open the file.
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to open file, error code: ${err.code}, message: ${err.message}\`);
  }
  if (videoFile !== undefined) {
    avConfig.url = 'fd://' + videoFile.fd; // Update the URL.
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

  // Complete camera-related preparations.
  let cameraManager: camera.CameraManager = camera.getCameraManager(context);
  let videoOutSurfaceId: string = await avRecorder.getInputSurface();
  await prepareCamera(cameraManager, videoOutSurfaceId);

  // Start recording.
  try {
    if (avRecorder.state === 'prepared') { // start() can be called only when the AVRecorder is in the prepared state.
      await startCameraOutput(); // Start camera stream output.
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
      await stopCameraOutput(); // Stop the camera stream output.
    }
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to pause avRecorder, error code: ${err.code}, message: ${err.message}\`);
  }

  // Resume recording.
  try {
    if (avRecorder.state === 'paused') { // resume() can be called only when the AVRecorder is in the paused state.
      await startCameraOutput(); // Start camera stream output.
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
      await stopCameraOutput(); // Stop the camera stream output.
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
    if (videoFile !== undefined) {
      await fs.close(videoFile.fd);
    }
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to close fd, error code: ${err.code}, message: ${err.message}\`);
  }

  // Release the camera instance.
  await releaseCamera();
  
  // The security component saves the media asset to Gallery.
  let phAccessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);

  // Ensure that the asset specified by uriPath exists.
  let uriPath: string = fileUri.getUriFromPath(filePath); // Obtain the file URI, which is used by the security component when saving the file to Gallery.
  let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
    photoAccessHelper.MediaAssetChangeRequest.createVideoAssetRequest(context, uriPath);
  await phAccessHelper.applyChanges(assetChangeRequest);
}

// Complete camera-related preparations.
async function prepareCamera(cameraManager: camera.CameraManager, videoOutSurfaceId: string) {
  // For details on the implementation, see the camera document.
}

// Start the camera stream output.
async function startCameraOutput() {
  // Call start of the VideoOutput class to start video output.
}

// Stop the camera stream output.
async function stopCameraOutput() {
  // Call stop of the VideoOutput class to stop video output.
}

// Release the camera instance.
async function releaseCamera() {
  // Release the instances created during camera preparation.
}
