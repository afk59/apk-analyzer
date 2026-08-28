# Device Input Management (ArkTS)

Before developing a camera application, you must [request required permissions](../../requesting-camera-development-permissions/document.md).

A camera application invokes and controls a camera device to perform basic operations such as preview, photo capture, and video recording.

#### How to Develop

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera) for the API reference.

1.  Import the camera module, which provides camera-related properties and methods.
    
    import { camera } from '@kit.CameraKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/JQwwSoPzTn-3GLACpXZgHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E880618B162578E0A5B5B57018B24A38E360E3D16FECF3A50593EACB9EDFDE8A)
    
    Before any camera device input, you must complete camera management by following the instructions provided in [Camera Device Management](../camera-device-management-arkts/document.md).
    
2.  Call [createCameraInput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#createcamerainput) in [cameraManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager) to create a camera input stream.
    
    async function createInput(cameraDevice: camera.CameraDevice, cameraManager: camera.CameraManager): Promise<camera.CameraInput | undefined> {
      // Create a camera input stream.
      let cameraInput: camera.CameraInput | undefined = undefined;
      try {
        cameraInput = cameraManager.createCameraInput(cameraDevice);
      } catch (error) {
        let err = error as BusinessError;
        console.error('Failed to createCameraInput errorCode = ' + err.code);
      }
      if (cameraInput === undefined) {
        return undefined;
      }
      // Listen for camera input errors.
      cameraInput.on('error', cameraDevice, (error: BusinessError) => {
        console.error(\`Camera input error code: ${error.code}\`);
      });
      // Open the camera.
      await cameraInput.open();
      return cameraInput;
    }
    
3.  Call [getSupportedSceneModes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#getsupportedscenemodes11) to obtain the list of scene modes supported by the current camera device. The list stores all the [SceneMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-e#scenemode11) supported by the camera device.
    
    function getSupportedSceneMode(cameraDevice: camera.CameraDevice, cameraManager: camera.CameraManager): Array<camera.SceneMode> {
      // Obtain the list of scene modes supported by the camera device.
      let sceneModeArray: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraDevice);
      if (sceneModeArray != undefined && sceneModeArray.length > 0) {
        for (let index = 0; index < sceneModeArray.length; index++) {
          console.info('Camera SceneMode : ' + sceneModeArray\[index\]);
      }
        return sceneModeArray;
      } else {
          console.error("cameraManager.getSupportedSceneModes error");
          return \[\];
      }
    }
    
4.  Call [getSupportedOutputCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#getsupportedoutputcapability11) to obtain all output streams supported by the current camera device, such as preview streams, photo streams, and video streams. The supported output streams are listed in the **profile** field in [CameraOutputCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-i#cameraoutputcapability). Different types of output streams must be added based on the value of [SceneMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-e#scenemode11) specified by the camera device.
    
    async function getSupportedOutputCapability(cameraDevice: camera.CameraDevice, cameraManager: camera.CameraManager, sceneMode: camera.SceneMode): Promise<camera.CameraOutputCapability | undefined> {
       // Obtain the output stream capability supported by the camera.
       let cameraOutputCapability: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(cameraDevice, sceneMode);
       if (!cameraOutputCapability) {
         console.error("cameraManager.getSupportedOutputCapability error");
         return undefined;
       }
       console.info("outputCapability: " + JSON.stringify(cameraOutputCapability));
       // The following uses the NORMAL\_PHOTO mode as an example. You need to add the preview stream and photo stream.
       // previewProfiles is the preview output streams supported by the current camera device.
       let previewProfilesArray: Array<camera.Profile> = cameraOutputCapability.previewProfiles;
       if (!previewProfilesArray) {
         console.error("createOutput previewProfilesArray == null || undefined");
       }
       // photoProfiles is the photo output streams supported by the current camera device.
       let photoProfilesArray: Array<camera.Profile> = cameraOutputCapability.photoProfiles;
       if (!photoProfilesArray) {
         console.error("createOutput photoProfilesArray == null || undefined");
       }
       return cameraOutputCapability;
    }
