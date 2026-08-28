# Camera Device Management (ArkTS)

Before developing a camera application, you must call camera APIs to create a camera device management instance.

#### How to Develop

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera) for the API reference.

1.  Import the camera module, which provides camera-related properties and methods.
    
    import { camera } from '@kit.CameraKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { common } from '@kit.AbilityKit';
    
2.  Call [getCameraManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-f#cameragetcameramanager) to obtain a CameraManager object.
    
    For details about how to obtain the context, see [Obtaining the Context of UIAbility](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/uiability-usage/document.md#obtaining-the-context-of-uiability).
    
    function getCameraManager(context: common.BaseContext): camera.CameraManager | undefined {
      let cameraManager: camera.CameraManager;
      try {
        cameraManager = camera.getCameraManager(context);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`getCameraManager error, errCode: ${err.code}\`);
        return undefined;
      }
      return cameraManager;
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/Oq8j227yQEC4Sq8kJwlGHA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5099C5742441178636BC267D82037A10C330B08560C05C53F4155BA6E6B53FA1)
    
    If obtaining the object fails, the camera device may be occupied or unusable. If it is occupied, wait until it is released.
    
3.  Call [getSupportedCameras](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#getsupportedcameras) in [CameraManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager) to obtain the list of cameras supported by the current device. The list stores the IDs of all cameras supported. If the list is not empty, each ID in the list can be used to create an independent camera object. If the list is empty, no camera is available for the current device and subsequent operations cannot be performed.
    
    function getCameraDevices(cameraManager: camera.CameraManager): Array<camera.CameraDevice> {
      let cameraArray: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
      if (cameraArray != undefined && cameraArray.length > 0) {
        for (let index = 0; index < cameraArray.length; index++) {
          console.info('cameraId : ' + cameraArray\[index\].cameraId);  // Obtain the camera ID.
          console.info('cameraPosition : ' + cameraArray\[index\].cameraPosition);  // Obtain the camera position.
          console.info('cameraType : ' + cameraArray\[index\].cameraType);  // Obtain the camera type.
          console.info('connectionType : ' + cameraArray\[index\].connectionType);  // Obtain the camera connection type.
        }
        return cameraArray;
      } else {
        console.error("cameraManager.getSupportedCameras error");
        return \[\];
      }
    }
    

#### Status Listening

During camera application development, you can listen for the camera status, including the appearance of a new camera, removal of a camera, and availability of a camera. The camera ID and camera status are included in the callback function. When a new camera appears, the new camera can be added to the supported camera list.

Register the **'cameraStatus'** event and return the listening result through a callback, which carries the **CameraStatusInfo** parameter. For details about the parameter, see [CameraStatusInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-i#camerastatusinfo).

function onCameraStatusChange(cameraManager: camera.CameraManager): void {
  cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
    if (err !== undefined && err.code !== 0) {
      console.error(\`Callback Error, errorCode: ${err.code}\`);
      return;
    }
    // If a camera is connected through a USB cable, the callback function returns the CAMERA\_STATUS\_APPEAR status.
    if (cameraStatusInfo.status == camera.CameraStatus.CAMERA\_STATUS\_APPEAR) {
      console.info(\`New Camera device appear.\`);
    }
    // If the USB connection of the camera is interrupted, the callback function returns the CAMERA\_STATUS\_DISAPPEAR status.
    if (cameraStatusInfo.status == camera.CameraStatus.CAMERA\_STATUS\_DISAPPEAR) {
      console.info(\`Camera device has been removed.\`);
    }
    // If the camera is closed, the callback function returns the CAMERA\_STATUS\_AVAILABLE status.
    if (cameraStatusInfo.status == camera.CameraStatus.CAMERA\_STATUS\_AVAILABLE) {
      console.info(\`Current Camera is available.\`);
    }
    // If the camera is opened or occupied, the callback function returns the CAMERA\_STATUS\_UNAVAILABLE status.
    if (cameraStatusInfo.status == camera.CameraStatus.CAMERA\_STATUS\_UNAVAILABLE) {
      console.info(\`Current Camera has been occupied.\`);
    }
    console.info(\`camera: ${cameraStatusInfo.camera.cameraId}\`);
    console.info(\`status: ${cameraStatusInfo.status}\`);
  });
}
