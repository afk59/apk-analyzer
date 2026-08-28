# Moving Photos (ArkTS)

The camera framework provides the capability of taking moving photos. With this capability, users can take a moving photo in one-click mode, in a way similar to taking an ordinary photo.

To develop the moving photo feature, perform the following steps:

-   Configure the mandatory capabilities required for camera application development by following the instructions provided in [Requesting Camera Development Permissions](../../requesting-camera-development-permissions/document.md), [Camera Device Management](../../mandatory-capabilities-for-camera-application-development-arkts/camera-device-management-arkts/document.md), [Device Input Management](../../mandatory-capabilities-for-camera-application-development-arkts/device-input-management-arkts/document.md), and [Camera Session Management](../../mandatory-capabilities-for-camera-application-development-arkts/camera-session-management-arkts/document.md).
-   Check whether the device supports taking moving photos.
-   Enable the capability of taking moving photos (if supported).
-   Listen for the photo callback function and save the photo to the media library. For details, see [Accessing and Managing Moving Photos](../../../media-library-kit/moving-photos/accessing-and-managing-moving-photos/document.md).

#### How to Develop

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera) for the API reference.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/N13rksQeTQ6g0xFV2WXRAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=694BC0FB41EC0E00CB81E50912A037FDAB5BAC5FB046314CD7D826333EECFED3)

The permission ohos.permission.MICROPHONE is required for taking moving photos. For details about how to apply for and verify the permission, see [Requesting Camera Development Permissions](../../requesting-camera-development-permissions/document.md). Otherwise, there is no sound when a photo is being taken.

1.  Import dependencies. Specifically, import the camera, image, and mediaLibrary modules.
    
    import { camera } from '@kit.CameraKit';
    import { photoAccessHelper } from '@kit.MediaLibraryKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Determine the photo output stream.
    
    You can use the **photoProfiles** property of [CameraOutputCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-i#cameraoutputcapability) to obtain the photo output streams supported by the device and use [createPhotoOutput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#createphotooutput11) to create a photo output stream.
    
    function getPhotoOutput(cameraManager: camera.CameraManager,
      cameraOutputCapability: camera.CameraOutputCapability): camera.PhotoOutput | undefined {
      if (!cameraOutputCapability || !cameraOutputCapability.photoProfiles) {
        return;
      }
      let photoProfilesArray: Array<camera.Profile> = cameraOutputCapability.photoProfiles;
      if (!photoProfilesArray || photoProfilesArray.length === 0) {
        console.error("photoProfilesArray is null or \[\]");
        return;
      }
      let photoOutput: camera.PhotoOutput | undefined = undefined;
      try {
        photoOutput = cameraManager.createPhotoOutput(photoProfilesArray\[0\]);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`Failed to createPhotoOutput. error: ${err}\`);
      }
      return photoOutput;
    }
    
3.  Check whether the device supports taking moving photos.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/DmWRVgewRQ-jzQ1kdlkONA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDD7E05EDE221E9A2C1AFDB214572E370F276CC8D92D038F2D704C45E3130E16)
    
    Before the check, you must configure, commit, and start a session. For details, see [Camera Session Management](../../mandatory-capabilities-for-camera-application-development-arkts/camera-session-management-arkts/document.md).
    
    function isMovingPhotoSupported(photoOutput: camera.PhotoOutput): boolean {
      let isSupported: boolean = false;
      try {
        isSupported = photoOutput.isMovingPhotoSupported();
      } catch (error) {
        // If the operation fails, error.code is returned and processed.
        let err = error as BusinessError;
        console.error(\`The isMovingPhotoSupported call failed. error code: ${err.code}\`);
      }
      return isSupported;
    }
    
4.  Enable the capability of taking moving photos.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/Ahv5qDp4SBCR7nl_7QnnVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=195AB016790717580E34BA1073078598ACE7FF2FDDC33E326677145B85280B9F)
    
    Before enabling the capability of taking moving photos, you must enable [deferred photo delivery](../deferred-photo-delivery-arkts/document.md).
    
    function enableMovingPhoto(photoOutput: camera.PhotoOutput): void {
      try {
        photoOutput.enableMovingPhoto(true);
      } catch (error) {
        // If the operation fails, error.code is returned and processed.
        let err = error as BusinessError;
       console.error(\`The enableMovingPhoto call failed. error code: ${err.code}\`);
      }
    }
    
5.  Trigger photo capture. This procedure is the same as that in the common photo capture mode. For details, see [Photo Capture](../photo-capture-arkts/document.md).
    

#### Status Listening

During camera application development, you can listen for the output stream status of moving photos by registering the **'photoAsset'** event. This event can be registered when a PhotoOutput instance is created.

function getPhotoAccessHelper(context: Context): photoAccessHelper.PhotoAccessHelper {
  let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  return phAccessHelper;
}

async function mediaLibSavePhoto(photoAsset: photoAccessHelper.PhotoAsset,
  phAccessHelper: photoAccessHelper.PhotoAccessHelper): Promise<void> {
  try {
    let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(photoAsset);
    assetChangeRequest.saveCameraPhoto();
    await phAccessHelper.applyChanges(assetChangeRequest);
    console.info('apply saveCameraPhoto successfully');
  } catch (err) {
    console.error(\`apply saveCameraPhoto failed with error: ${err.code}, ${err.message}\`);
  }
}

function onPhotoOutputPhotoAssetAvailable(photoOutput: camera.PhotoOutput, context: Context): void {
  photoOutput.on('photoAssetAvailable', (err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset): void => {
    if (err) {
      console.error(\`photoAssetAvailable error: ${err}.\`);
      return;
    }
    console.info('photoOutPutCallBack photoAssetAvailable');
    // Call the mediaLibrary flush API to save the first-phase images and moving photos.
    mediaLibSavePhoto(photoAsset, getPhotoAccessHelper(context));
  });
}
