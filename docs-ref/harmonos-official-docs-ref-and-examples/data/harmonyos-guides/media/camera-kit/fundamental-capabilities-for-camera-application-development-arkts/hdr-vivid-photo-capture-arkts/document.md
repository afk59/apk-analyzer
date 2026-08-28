# HDR Vivid Photo Capture (ArkTS)

In HarmonyOS, you can call APIs to capture HDR Vivid photos featuring more refined layers and enhanced light and shadow details, thereby improving visual quality and offering superior visual effects.

This section outlines comprehensive development steps for HDR Vivid photo capture. For more information on developing HDR Vivid, see [Using HDR Vivid in Media Applications](../../../using-hdr-vivid-in-media-applications/document.md).

Before referring to the sample code, you are advised to read [Device Input Management](../../mandatory-capabilities-for-camera-application-development-arkts/device-input-management-arkts/document.md), [Camera Session Management](../../mandatory-capabilities-for-camera-application-development-arkts/camera-session-management-arkts/document.md), and [Photo Capture](../photo-capture-arkts/document.md), and other related topics in [Camera Development (ArkTS)](../../mandatory-capabilities-for-camera-application-development-arkts/camera-device-management-arkts/document.md).

#### How to Develop

1.  Import the APIs.
    
    import { camera } from '@kit.CameraKit';
    import { colorSpaceManager } from '@kit.ArkGraphics2D';
    import { image } from '@kit.ImageKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { fileIo as fs } from '@kit.CoreFileKit';
    import { photoAccessHelper } from '@kit.MediaLibraryKit';
    
2.  Check the supported color spaces.
    
    function getSupportedColorSpaces(session: camera.PhotoSession): Array<colorSpaceManager.ColorSpace> {
      let colorSpaces: Array<colorSpaceManager.ColorSpace> = \[\];
      try {
        colorSpaces = session.getSupportedColorSpaces();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`The getSupportedColorSpaces call failed. error code: ${err.code}\`);
      }
      return colorSpaces;
     }
    
3.  Set a color space.
    
    For SDR photo capture, the color space must be **SRGB**. For HDR photo capture, the color space must be **DISPLAY\_P3**. For details, refer to [setColorSpace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-colormanagement#setcolorspace12).
    
    function setColorSpaceBeforeCommitConfig(session: camera.PhotoSession, isHdr: boolean): void {
      let colorSpace: colorSpaceManager.ColorSpace = isHdr? colorSpaceManager.ColorSpace.DISPLAY\_P3 : colorSpaceManager.ColorSpace.SRGB;
      let colorSpaces: Array<colorSpaceManager.ColorSpace> = getSupportedColorSpaces(session);
      let isSupportedColorSpaces = colorSpaces.indexOf(colorSpace) >= 0;
      if (isSupportedColorSpaces) {
        console.info(\`setColorSpace: ${colorSpace}\`);
        session.setColorSpace(colorSpace);
        let activeColorSpace:colorSpaceManager.ColorSpace = session.getActiveColorSpace();
        console.info(\`activeColorSpace: ${activeColorSpace}\`);
      } else {
        console.info(\`colorSpace: ${colorSpace} is not support\`);
      }
    }
    
4.  Implement HDR photo capture.
    
    Before committing the session configuration, perform step 3 to set the color space. Other steps are the same as those in the normal photo capture process.
    
    async function savePicture(buffer: ArrayBuffer, img: image.Image, context: Context): Promise<void> {
      let accessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
      let options: photoAccessHelper.CreateOptions = {
        title: Date.now().toString()
      };
      let photoUri: string = await accessHelper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'jpg', options);
      // To call createAsset(), the application must have the ohos.permission.READ\_IMAGEVIDEO and ohos.permission.WRITE\_IMAGEVIDEO permissions.
      let file: fs.File = fs.openSync(photoUri, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
      await fs.write(file.fd, buffer);
      fs.closeSync(file);
      img.release();
    }
    
    function setPhotoOutputCb(photoOutput: camera.PhotoOutput, context: Context): void {
      // After the callback is set, call capture() of photoOutput to transfer the photo buffer back to the callback.
      photoOutput.on('photoAvailable', (errCode: BusinessError, photo: camera.Photo): void => {
        console.info('getPhoto start');
        console.info(\`err: ${JSON.stringify(errCode)}\`);
        if (errCode || photo === undefined) {
          console.error('getPhoto failed');
          return;
        }
        let imageObj = photo.main;
        imageObj.getComponent(image.ComponentType.JPEG, (errCode: BusinessError, component: image.Component): void => {
          console.info('getComponent start');
          if (errCode || component === undefined) {
            console.error('getComponent failed');
            return;
          }
          let buffer: ArrayBuffer;
          if (component.byteBuffer) {
            buffer = component.byteBuffer;
          } else {
            console.error('byteBuffer is null');
            return;
          }
          savePicture(buffer, imageObj, context);
        });
      });
    }
    
    async function cameraHdrShootingCase(context: Context, surfaceId: string): Promise<void> {
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
      let cameraArray: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
      if (cameraArray.length <= 0) {
        console.error("cameraManager.getSupportedCameras error");
        return;
      }
    
      for (let index = 0; index < cameraArray.length; index++) {
        console.info('cameraId : ' + cameraArray\[index\].cameraId);                          // Obtain the camera ID.
        console.info('cameraPosition : ' + cameraArray\[index\].cameraPosition);              // Obtain the camera position.
        console.info('cameraType : ' + cameraArray\[index\].cameraType);                      // Obtain the camera type.
        console.info('connectionType : ' + cameraArray\[index\].connectionType);              // Obtain the camera connection type.
      }
    
      // Create a camera input stream.
      let cameraInput: camera.CameraInput | undefined = undefined;
      try {
        cameraInput = cameraManager.createCameraInput(cameraArray\[0\]);
      } catch (error) {
        let err = error as BusinessError;
        console.error('Failed to createCameraInput errorCode = ' + err.code);
      }
      if (cameraInput === undefined) {
        return;
      }
    
      // Listen for camera input errors.
      let cameraDevice: camera.CameraDevice = cameraArray\[0\];
      cameraInput.on('error', cameraDevice, (error: BusinessError) => {
        console.error(\`Camera input error code: ${error.code}\`);
      })
    
      // Open the camera.
      await cameraInput.open();
    
      // Obtain the supported modes.
      let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraArray\[0\]);
      let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL\_PHOTO) >= 0;
      if (!isSupportPhotoMode) {
        console.error('photo mode not support');
        return;
      }
      // Obtain the output streams supported by the camera.
      let cameraOutputCap: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(cameraArray\[0\], camera.SceneMode.NORMAL\_PHOTO);
      if (!cameraOutputCap) {
        console.error("cameraManager.getSupportedOutputCapability error");
        return;
      }
      console.info("outputCapability: " + JSON.stringify(cameraOutputCap));
    
      let previewProfilesArray: Array<camera.Profile> = cameraOutputCap.previewProfiles;
      if (!previewProfilesArray) {
        console.error("createOutput previewProfilesArray == null || undefined");
      }
    
      let photoProfilesArray: Array<camera.Profile> = cameraOutputCap.photoProfiles;
      if (!photoProfilesArray) {
        console.error("createOutput photoProfilesArray == null || undefined");
      }
    
      // Create a preview output stream. For details about the surfaceId parameter, see the XComponent. The preview stream uses the surface provided by the XComponent.
      let previewOutput: camera.PreviewOutput | undefined = undefined;
      try {
        previewOutput = cameraManager.createPreviewOutput(previewProfilesArray\[0\], surfaceId);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to create the PreviewOutput instance. error code: ${err.code}\`);
      }
      if (previewOutput === undefined) {
        return;
      }
      // Listen for preview output errors.
      previewOutput.on('error', (error: BusinessError) => {
        console.error(\`Preview output error code: ${error.code}\`);
      });
    
      // Create a photo output stream.
      let photoOutput: camera.PhotoOutput | undefined = undefined;
      try {
        photoOutput = cameraManager.createPhotoOutput(photoProfilesArray\[0\]);
      } catch (error) {
        let err = error as BusinessError;
        console.error('Failed to createPhotoOutput errorCode = ' + err.code);
      }
      if (photoOutput === undefined) {
        return;
      }
    
      // Call the preceding callback to save the image.
      setPhotoOutputCb(photoOutput, context);
    
      // Create a session.
      let photoSession: camera.PhotoSession | undefined = undefined;
      try {
        photoSession = cameraManager.createSession(camera.SceneMode.NORMAL\_PHOTO) as camera.PhotoSession;
      } catch (error) {
        let err = error as BusinessError;
        console.error('Failed to create the session instance. errorCode = ' + err.code);
      }
      if (photoSession === undefined) {
        return;
      }
      // Listen for session errors.
      photoSession.on('error', (error: BusinessError) => {
        console.error(\`Capture session error code: ${error.code}\`);
      });
    
      // Start configuration for the session.
      try {
        photoSession.beginConfig();
      } catch (error) {
        let err = error as BusinessError;
        console.error('Failed to beginConfig. errorCode = ' + err.code);
      }
    
      // Add the camera input stream to the session.
      try {
        photoSession.addInput(cameraInput);
      } catch (error) {
        let err = error as BusinessError;
        console.error('Failed to addInput. errorCode = ' + err.code);
      }
    
      // Add the preview output stream to the session.
      try {
        photoSession.addOutput(previewOutput);
      } catch (error) {
        let err = error as BusinessError;
        console.error('Failed to addOutput(previewOutput). errorCode = ' + err.code);
      }
    
      // Add the photo output stream to the session.
      try {
        photoSession.addOutput(photoOutput);
      } catch (error) {
        let err = error as BusinessError;
        console.error('Failed to addOutput(photoOutput). errorCode = ' + err.code);
      }
    
      // Set the color space.
      setColorSpaceBeforeCommitConfig(photoSession, true);
    
      // Commit the session configuration.
      await photoSession.commitConfig();
    
      // Start the session.
      await photoSession.start().then(() => {
        console.info('Promise returned to indicate the session start success.');
      });
    
      let photoCaptureSetting: camera.PhotoCaptureSetting = {
        quality: camera.QualityLevel.QUALITY\_LEVEL\_HIGH, // Set the photo quality to high.
        rotation: camera.ImageRotation.ROTATION\_0 // Set the rotation angle of the photo to 0.
      }
      // Use the current photo capture settings to take photos.
      photoOutput.capture(photoCaptureSetting, (err: BusinessError) => {
        if (err) {
          console.error(\`Failed to capture the photo ${err.message}\`);
          return;
        }
        console.info('Callback invoked to indicate the photo capture request success.');
      });
    
      // After the photo capture is complete, call the following APIs to close the camera and release the session. Do not release the session before the photo capture is complete.
      // Stop the session.
      await photoSession.stop();
    
      // Release the camera input stream.
      await cameraInput.close();
    
      // Release the preview output stream.
      await previewOutput.release();
    
      // Release the photo output stream.
      await photoOutput.release();
    
      // Release the session.
      await photoSession.release();
    
      // Set the session to null.
      photoSession = undefined;
    }
