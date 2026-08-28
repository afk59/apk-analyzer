# HDR Vivid Camera Recording (ArkTS)

In HarmonyOS, you can call APIs to capture HDR Vivid videos featuring more refined layers and enhanced light and shadow details, thereby improving visual quality and offering superior visual effects.

This section outlines comprehensive development steps for HDR Vivid video recording. For more information on developing HDR Vivid, see [Using HDR Vivid in Media Applications](../../../using-hdr-vivid-in-media-applications/document.md).

Before referring to the sample code, you are advised to read [Device Input Management](../../mandatory-capabilities-for-camera-application-development-arkts/device-input-management-arkts/document.md), [Camera Session Management](../../mandatory-capabilities-for-camera-application-development-arkts/camera-session-management-arkts/document.md), [Video Recording](../video-recording-arkts/document.md), and other related topics in [Camera Development (ArkTS)](../../mandatory-capabilities-for-camera-application-development-arkts/camera-device-management-arkts/document.md).

#### How to Develop

1.  Import the APIs.
    
    import { camera } from '@kit.CameraKit';
    import { colorSpaceManager } from '@kit.ArkGraphics2D';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { media } from '@kit.MediaKit';
    import { common } from '@kit.AbilityKit';
    import { photoAccessHelper } from '@kit.MediaLibraryKit';
    import { fileIo as fs } from '@kit.CoreFileKit';
    
2.  Obtain the configuration items for preview and video recording.
    
    The output format of HDR video recording must be set to **CAMERA\_FORMAT\_YCRCB\_P010**. For details, refer to [setColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-colormanagement#setcolorspace12).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/ZSpeP83QTT6nPZCQxH7kMA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062039Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB99ED394E0AC473A1CF1DCC670DF10CB85E2337E0981B6BAB0F058054D26CD1)
    
    The preview stream and video output stream must have the same aspect ratio of the resolution. For example, if the aspect ratio of the surface in the **XComponent** is 1920:1080 (which is equal to 16:9), then the aspect ratio of the resolution of the preview stream must also be 16:9. This means that the resolution can be 640:360, 960:540, 1920:1080, or the like.
    
    function getPreviewProfile(previewProfiles: Array<camera.Profile>, size: camera.Size): undefined | camera.Profile {
      let previewProfile: undefined | camera.Profile = previewProfiles.find((profile: camera.Profile) => {
        return profile.format === camera.CameraFormat.CAMERA\_FORMAT\_YCRCB\_P010 &&
          profile.size.width === size.width && profile.size.height == size.height
      });
      return previewProfile;
    }
    
    function getVideoProfile(videoProfiles: Array<camera.VideoProfile>, size: camera.Size): undefined | camera.VideoProfile {
      let videoProfile: undefined | camera.VideoProfile = videoProfiles.find((profile: camera.VideoProfile) => {
        return profile.format === camera.CameraFormat.CAMERA\_FORMAT\_YCRCB\_P010 &&
          profile.size.width === size.width && profile.size.height == size.height
      });
      return videoProfile;
    }
    
3.  Check whether a video stabilization mode is supported.
    
    To perform HDR video recording, video stabilization must be supported.
    
    function isVideoStabilizationModeSupported(session: camera.VideoSession, mode: camera.VideoStabilizationMode): boolean {
      let isSupported: boolean = false;
      try {
        isSupported = session.isVideoStabilizationModeSupported(mode);
      } catch (error) {
        // If the operation fails, error.code is returned and processed.
        let err = error as BusinessError;
        console.error(\`The isVideoStabilizationModeSupported call failed. error code: ${err.code}\`);
      }
      return isSupported;
    }
    
4.  Set the video stabilization mode.
    
    function setVideoStabilizationMode(session: camera.VideoSession): void {
      let mode: camera.VideoStabilizationMode = camera.VideoStabilizationMode.AUTO;
      // Check whether a video stabilization mode is supported.
      let isSupported: boolean = isVideoStabilizationModeSupported(session, mode);
      if (isSupported) {
        console.info(\`setVideoStabilizationMode: ${mode}\`);
        // Set the video stabilization mode.
        try {
          session.setVideoStabilizationMode(mode);
        } catch (error) {
          // If the operation fails, error.code is returned and processed.
          let err = error as BusinessError;
          console.error(\`setVideoStabilizationMode call failed. error code: ${err.code}\`);
        }
        let activeVideoStabilizationMode = session.getActiveVideoStabilizationMode();
        console.info(\`activeVideoStabilizationMode: ${activeVideoStabilizationMode}\`);
      } else {
        console.info(\`videoStabilizationMode: ${mode} is not support\`);
      }
    }
    
5.  Check the supported color spaces.
    
    function getSupportedColorSpaces(session: camera.VideoSession): Array<colorSpaceManager.ColorSpace> {
      let colorSpaces: Array<colorSpaceManager.ColorSpace> = \[\];
      try {
        colorSpaces = session.getSupportedColorSpaces();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`The getSupportedColorSpaces call failed. error code: ${err.code}\`);
      }
      return colorSpaces;
    }
    
6.  Set a color space.
    
    For SDR video recording, the color space must be **BT709\_LIMIT**. For HDR video recording, the color space must be **BT2020\_HLG\_LIMIT**. For details, refer to [setColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-colormanagement#setcolorspace12). You are advised to call [setColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-colormanagement#setcolorspace12) before submitting session configurations.
    
    function setColorSpaceBeforeCommitConfig(session: camera.VideoSession, isHdr: boolean): void {
      let colorSpace: colorSpaceManager.ColorSpace = isHdr? colorSpaceManager.ColorSpace.BT2020\_HLG\_LIMIT : colorSpaceManager.ColorSpace.BT709\_LIMIT;
      let colorSpaces: Array<colorSpaceManager.ColorSpace> = session.getSupportedColorSpaces();
      let isSupportedColorSpaces = colorSpaces.indexOf(colorSpace) >= 0;
      if (isSupportedColorSpaces) {
        console.info(\`setColorSpace: ${colorSpace}\`);
        try {
          session.setColorSpace(colorSpace);
        } catch (error) {
          // If the operation fails, error.code is returned and processed.
          let err = error as BusinessError;
          console.error(\`setColorSpace call failed. error code: ${err.code}\`);
        }
        let activeColorSpace:colorSpaceManager.ColorSpace = session.getActiveColorSpace();
        console.info(\`activeColorSpace: ${activeColorSpace}\`);
      } else {
        console.info(\`colorSpace: ${colorSpace} is not support\`);
      }
    }
    
7.  Implement HDR video recording.
    
    Before creating the preview output and video output streams, perform step 2 to obtain the configuration items. Before committing the session configuration, perform step 6 to set a color space. After committing the session configuration, perform step 4 to set a video stabilization mode. Other steps are the same as those in the normal recording process.
    
    async function cameraHdrRecordingCase(context: common.Context, surfaceId: string): Promise<void> {
      // Create a CameraManager object.
      let cameraManager: camera.CameraManager = camera.getCameraManager(context);
      if (!cameraManager) {
        console.error("camera.getCameraManager error");
        return;
      }
    
      // Listen for camera status changes.
      cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
        if (err !== undefined && err.code !== 0) {
          console.error('cameraStatus with errorCode = ' + err.code);
          return;
        }
        console.info(\`camera : ${cameraStatusInfo.camera.cameraId}\`);
        console.info(\`status: ${cameraStatusInfo.status}\`);
      });
    
      // Obtain the camera list.
      let cameraArray: Array<camera.CameraDevice> = \[\];
      try {
        cameraArray = cameraManager.getSupportedCameras();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`getSupportedCameras call failed. error code: ${err.code}\`);
      }
    
      if (cameraArray.length <= 0) {
        console.error("cameraManager.getSupportedCameras error");
        return;
      }
    
      // Obtain the supported modes.
      let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraArray\[0\]);
      let isSupportVideoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL\_VIDEO) >= 0;
      if (!isSupportVideoMode) {
        console.error('video mode not support');
        return;
      }
    
      // Obtain the output streams supported by the camera.
      let cameraOutputCap: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(cameraArray\[0\], camera.SceneMode.NORMAL\_VIDEO);
      if (!cameraOutputCap) {
        console.error("cameraManager.getSupportedOutputCapability error")
        return;
      }
      console.info("outputCapability: " + JSON.stringify(cameraOutputCap));
    
      let previewProfilesArray: Array<camera.Profile> = cameraOutputCap.previewProfiles;
      if (!previewProfilesArray) {
        console.error("createOutput previewProfilesArray == null || undefined");
        return;
      }
    
      let videoProfilesArray: Array<camera.VideoProfile> = cameraOutputCap.videoProfiles;
      if (!videoProfilesArray) {
        console.error("createOutput videoProfilesArray == null || undefined");
        return;
      }
      // The width and height of videoProfile must be the same as those of AVRecorderProfile.
      let videoSize: camera.Size = {
        width: 640,
        height: 480
      }
      let previewProfile: undefined | camera.Profile = getPreviewProfile(previewProfilesArray, videoSize);
      if (!previewProfile) {
        console.error('previewProfile is not found');
        return;
      }
      let videoProfile: undefined | camera.VideoProfile = getVideoProfile(videoProfilesArray, videoSize);
      if (!videoProfile) {
        console.error('videoProfile is not found');
        return;
      }
      // Configure the parameters based on those supported by the hardware device.
      let aVRecorderProfile: media.AVRecorderProfile = {
        audioBitrate: 48000,
        audioChannels: 2,
        audioCodec: media.CodecMimeType.AUDIO\_AAC,
        audioSampleRate: 48000,
        fileFormat: media.ContainerFormatType.CFT\_MPEG\_4,
        videoBitrate: 2000000,
        videoCodec: media.CodecMimeType.VIDEO\_HEVC,
        videoFrameWidth: videoSize.width,
        videoFrameHeight: videoSize.height,
        videoFrameRate: 30,
        isHdr: true
      };
      let options: photoAccessHelper.CreateOptions = {
        title: Date.now().toString()
      };
      let accessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
      let videoUri: string = await accessHelper.createAsset(photoAccessHelper.PhotoType.VIDEO, 'mp4', options);
      let file: fs.File = fs.openSync(videoUri, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
      let aVRecorderConfig: media.AVRecorderConfig = {
        audioSourceType: media.AudioSourceType.AUDIO\_SOURCE\_TYPE\_MIC,
        videoSourceType: media.VideoSourceType.VIDEO\_SOURCE\_TYPE\_SURFACE\_YUV,
        profile: aVRecorderProfile,
        url: \`fd://${file.fd.toString()}\`, // Before passing in a file descriptor to this parameter, the file must be created by the caller and granted with the read and write permissions. Example value: fd://45--file:///data/media/01.mp4.
        rotation: 0, // The value can be 0, 90, 180, or 270. If any other value is used, prepare() reports an error.
        location: { latitude: 30, longitude: 130 }
      };
    
      let avRecorder: media.AVRecorder | undefined = undefined;
      try {
        avRecorder = await media.createAVRecorder();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`createAVRecorder call failed. error code: ${err.code}\`);
      }
    
      if (avRecorder === undefined) {
        return;
      }
    
      try {
        await avRecorder.prepare(aVRecorderConfig);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`prepare call failed. error code: ${err.code}\`);
      }
    
      let videoSurfaceId: string | undefined = undefined; // The surfaceID is passed in to the camera API to create a VideoOutput instance.
      try {
        videoSurfaceId = await avRecorder.getInputSurface();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`getInputSurface call failed. error code: ${err.code}\`);
      }
      if (videoSurfaceId === undefined) {
        return;
      }
      // Create a VideoOutput instance.
      let videoOutput: camera.VideoOutput | undefined = undefined;
      try {
        videoOutput = cameraManager.createVideoOutput(videoProfile, videoSurfaceId);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to create the videoOutput instance. error: ${JSON.stringify(err)}\`);
      }
      if (videoOutput === undefined) {
        return;
      }
      // Listen for video output errors.
      videoOutput.on('error', (error: BusinessError) => {
        console.error(\`Preview output error code: ${error.code}\`);
      });
    
      // Create a session.
      let videoSession: camera.VideoSession | undefined = undefined;
      try {
        videoSession = cameraManager.createSession(camera.SceneMode.NORMAL\_VIDEO) as camera.VideoSession;
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to create the session instance. error: ${JSON.stringify(err)}\`);
      }
      if (videoSession === undefined) {
        return;
      }
      // Listen for session errors.
      videoSession.on('error', (error: BusinessError) => {
        console.error(\`Video session error code: ${error.code}\`);
      });
    
      // Start configuration for the session.
      try {
        videoSession.beginConfig();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to beginConfig. error: ${JSON.stringify(err)}\`);
      }
    
      // Create a camera input stream.
      let cameraInput: camera.CameraInput | undefined = undefined;
      try {
        cameraInput = cameraManager.createCameraInput(cameraArray\[0\]);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to createCameraInput. error: ${JSON.stringify(err)}\`);
      }
      if (cameraInput === undefined) {
        return;
      }
      // Listen for camera input errors.
      let cameraDevice: camera.CameraDevice = cameraArray\[0\];
      cameraInput.on('error', cameraDevice, (error: BusinessError) => {
        console.error(\`Camera input error code: ${error.code}\`);
      });
    
      // Open the camera.
      try {
        await cameraInput.open();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to open cameraInput. error: ${JSON.stringify(err)}\`);
      }
    
      // Add the camera input stream to the session.
      try {
        videoSession.addInput(cameraInput);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to add cameraInput. error: ${JSON.stringify(err)}\`);
      }
    
      // Create a preview output stream. For details about the surfaceId parameter, see the XComponent. The preview stream is the surface provided by the XComponent.
      let previewOutput: camera.PreviewOutput | undefined = undefined;
      try {
        previewOutput = cameraManager.createPreviewOutput(previewProfile, surfaceId);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to create the PreviewOutput instance. error: ${JSON.stringify(err)}\`);
      }
    
      if (previewOutput === undefined) {
        return;
      }
      // Add the preview output stream to the session.
      try {
        videoSession.addOutput(previewOutput);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to add previewOutput. error: ${JSON.stringify(err)}\`);
      }
    
      // Add the video output stream to the session.
      try {
        videoSession.addOutput(videoOutput);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to add videoOutput. error: ${JSON.stringify(err)}\`);
      }
    
        // Set the color space.
      setColorSpaceBeforeCommitConfig(videoSession, true);
    
      // Commit the session configuration.
      try {
        await videoSession.commitConfig();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`videoSession commitConfig error: ${JSON.stringify(err)}\`);
      }
    
      // Set the video stabilization mode.
      setVideoStabilizationMode(videoSession);
    
      // Start the session.
      try {
        await videoSession.start();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`videoSession start error: ${JSON.stringify(err)}\`);
      }
    
      // Start the video output stream.
      videoOutput.start((err: BusinessError) => {
        if (err) {
          console.error(\`Failed to start the video output. error: ${JSON.stringify(err)}\`);
          return;
        }
        console.info('Callback invoked to indicate the video output start success.');
      });
    
      // Start video recording.
      try {
        await avRecorder.start();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`avRecorder start error: ${JSON.stringify(err)}\`);
      }
    
      // Stop the video output stream.
      videoOutput.stop((err: BusinessError) => {
        if (err) {
          console.error(\`Failed to stop the video output. error: ${JSON.stringify(err)}\`);
          return;
        }
        console.info('Callback invoked to indicate the video output stop success.');
      });
    
      // Stop video recording.
      try {
        await avRecorder.stop();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`avRecorder stop error: ${JSON.stringify(err)}\`);
      }
    
      // Stop the session.
      await videoSession.stop();
    
      // Close the file.
      fs.closeSync(file);
    
      // Release the camera input stream.
      await cameraInput.close();
    
      // Release the preview output stream.
      await previewOutput.release();
    
      // Release the video output stream.
      await videoOutput.release();
    
      // Release the session.
      await videoSession.release();
    
      // Set the session to null.
      videoSession = undefined;
    }
