# Camera Session Management (ArkTS)

Before using the camera application for preview, photo capture, video recording, and metadata management, you must create a camera session.

You can implement the following functions in the session:

-   Configure the camera input and output streams. This is mandatory for photo capture.
    
    Configuring an input stream is to add a device input, which means that the user selects a camera for photo capture. Configuring an output stream is to select a data output mode. When your application needs to implement photo capture, configure the output streams to include a preview stream and a capture stream: the preview stream data is displayed on the [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent), while the capture stream data is saved to the photo album using the capabilities of the [ImageReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagereceiver) API.
    
-   Perform more operations on the camera device. For example, add the flash and adjust the focal length. For details about the supported configurations and APIs, see [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera).
    
-   Control session switching. The application can switch the camera mode by removing and adding output streams. For example, to switch from photo capture to video recording, the application must remove the photo output stream and add the video output stream.
    

After the session configuration is complete, the application must commit the configuration and start the session before using the camera functionalities.

#### How to Develop

1.  Import the modules.
    
    import { camera } from '@kit.CameraKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call the [createSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#createsession11) method in [cameraManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager) to create a session.
    
    // videoSession is used as an example.
    function getSession(cameraManager: camera.CameraManager): camera.VideoSession | undefined {
      let videoSession: camera.VideoSession | undefined = undefined;
      try {
        videoSession = cameraManager.createSession(camera.SceneMode.NORMAL\_VIDEO) as camera.VideoSession;
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to create the session instance. error: ${err.code}\`);
      }
      return videoSession;
    }
    
3.  Call the [beginConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session#beginconfig11) method in [VideoSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-videosession) to configure the session.
    
    function beginConfig(videoSession: camera.VideoSession): void {
      try {
        videoSession.beginConfig();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to beginConfig. error: ${err.code}\`);
      }
    }
    
4.  Configure the session. You can call [addInput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session#addinput11) and [addOutput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session#addoutput11) in **VideoSession** to add the input and output streams to the session, respectively. The code snippet below uses adding the preview stream **previewOutput** and photo stream **photoOutput** as an example to implement the photo capture and preview mode.
    
    After the configuration, call [commitConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session#commitconfig11) and [start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session#start11) in **VideoSession** in sequence to commit the configuration and start the session.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/7CVb8idUQu63KPGp7S6bWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=52CC45CB4B29182824F2430B6E0819FB227B8B193C8AB935CC7370E87D0B79BC)
    
    Before calling [addOutput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session#addoutput11) to add a camera output stream, you can call [canAddOutput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session#canaddoutput11) to check whether the camera output stream can be added to the session.
    
    For details about how to create **cameraInput**, **previewOutput**, and **photoOutput**, see [Device Input Management](../device-input-management-arkts/document.md), [Camera Preview](../../fundamental-capabilities-for-camera-application-development-arkts/preview-arkts/document.md), and [Photo Capture](../../fundamental-capabilities-for-camera-application-development-arkts/photo-capture-arkts/document.md), respectively.
    
    async function startSession(videoSession: camera.VideoSession, cameraInput: camera.CameraInput, previewOutput: camera.PreviewOutput, photoOutput: camera.PhotoOutput): Promise<void> {
      try {
        videoSession.addInput(cameraInput);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to addInput. error: ${err.code}\`);
      }
      let canAddPreviewOutput : boolean = false;
      try {
        canAddPreviewOutput = videoSession.canAddOutput(previewOutput);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to add previewOutput. error: ${err.code}\`);
      }
      if (!canAddPreviewOutput) {
        console.error(\`Failed to add preview output.\`);
        return;
      }
      try {
        videoSession.addOutput(previewOutput);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to add previewOutput. error: ${err.code}\`);
      }
      let canAddPhotoOutput : boolean = false
      try {
        canAddPhotoOutput = videoSession.canAddOutput(photoOutput);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to add photoOutput error: ${err.code}\`);
      }
      if (!canAddPhotoOutput) {
        console.error(\`Failed to add photo output.\`);
        return;
      }
      try {
        videoSession.addOutput(photoOutput);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to add photoOutput. error: ${err.code}\`);
      }
      try {
        await videoSession.commitConfig();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to commitConfig. error: ${err.code}\`);
       return;
      }
    
      try {
        await videoSession.start();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to start. error: ${err.code}\`);
      }
    }
    
5.  Control the session. You can call [stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session#stop11) in **VideoSession** to stop the current session, and call [removeOutput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session#removeoutput11) and [addOutput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session#addoutput11) to switch to another session. The code snippet below uses removing the photo stream **photoOutput** and adding the video stream **videoOutput** as an example to complete the switching from photo capture to recording.
    
    async function switchOutput(videoSession: camera.VideoSession, videoOutput: camera.VideoOutput, photoOutput: camera.PhotoOutput): Promise<void> {
      try {
        await videoSession.stop();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to stop. error: ${err.code}\`);
      }
    
      try {
        videoSession.beginConfig();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to beginConfig. error: ${err.code}\`);
      }
      // Remove the photo output stream from the session.
      try {
        videoSession.removeOutput(photoOutput);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to remove photoOutput. error: ${err.code}\`);
      }
      try {
        videoSession.canAddOutput(videoOutput);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to add videoOutput error: ${err.code}\`);
      }
      // Add the video output stream to the session.
      try {
        videoSession.addOutput(videoOutput);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to add videoOutput. error: ${err.code}\`);
      }
      try {
        await videoSession.commitConfig();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to commitConfig. error: ${err.code}\`);
      }
    
      try {
        await videoSession.start();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to start. error: ${err.code}\`);
      }
    }
