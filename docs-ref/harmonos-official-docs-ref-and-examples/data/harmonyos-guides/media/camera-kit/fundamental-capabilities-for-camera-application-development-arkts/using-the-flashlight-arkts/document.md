# Using the Flashlight (ArkTS)

To use the flashlight mode, you manipulate your device to turn on the flashlight, which then stays on persistently.

When you use the flashlight mode with a camera application, the following situations may occur:

-   When the rear camera is used and [FlashMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-e#flashmode) is set to off, the flashlight cannot be turned on.
-   When the front camera is used, the flashlight can be turned on and remains steady on.
-   When you switch from the front camera to the rear camera, the flashlight will be automatically turned off if it was turned on previously.

#### How to Develop

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera) for the API reference.

1.  Import the camera module, which provides camera-related properties and methods.
    
    import { camera } from '@kit.CameraKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call [isTorchSupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#istorchsupported11) in [CameraManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager) to check whether the current device supports the flashlight.
    
    function isTorchSupported(cameraManager: camera.CameraManager) : boolean {
      let torchSupport: boolean = false;
      try {
        torchSupport = cameraManager.isTorchSupported();
      } catch (error) {
        let err = error as BusinessError;
        console.error('Failed to torch. errorCode = ' + err.code);
      }
      console.info('Returned with the torch support status:' + torchSupport);
      return torchSupport;
    }
    
3.  Call [isTorchModeSupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#istorchmodesupported11) in [CameraManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager) to check whether a specific [TorchMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-e#torchmode11) is supported.
    
    function isTorchModeSupported(cameraManager: camera.CameraManager, torchMode: camera.TorchMode) : boolean {
      let isTorchModeSupport: boolean = false;
      try {
        isTorchModeSupport = cameraManager.isTorchModeSupported(torchMode);
      } catch (error) {
        let err = error as BusinessError;
        console.error('Failed to set the torch mode. errorCode = ' + err.code);
      }
      return isTorchModeSupport;
    }
    
4.  Call [setTorchMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#settorchmode11) in [CameraManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager) to set the flashlight mode, and then [getTorchMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#gettorchmode11) in [CameraManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager) to obtain the flashlight mode in use.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/_bw3XSFXRnmGSnreqb3zeQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7243DD4D1A47681F2AFD4674B5B12CE4745D54B534828F113358C2C344F659C2)
    
    Before using [getTorchMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#gettorchmode11), register a listener for the flashlight status. For details, see [Status Listening](#status-listening).
    
    function setTorchModeSupported(cameraManager: camera.CameraManager, torchMode: camera.TorchMode) : void {
      cameraManager.setTorchMode(torchMode);
      let isTorchMode = cameraManager.getTorchMode();
      console.info(\`Returned with the torch mode supported mode: ${isTorchMode}\`);
    }
    

#### Status Listening

During camera application development, you can listen for the flashlight status, including on, off, unavailable, and available.

Register the **'torchStatusChange'** event and return the listening result through a callback, which carries the **TorchStatusInfo** parameter. For details about the parameter, see [TorchStatusInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-i#torchstatusinfo11).

function onTorchStatusChange(cameraManager: camera.CameraManager): void {
  cameraManager.on('torchStatusChange', (err: BusinessError, torchStatusInfo: camera.TorchStatusInfo) => {
    if (err !== undefined && err.code !== 0) {
      console.error(\`Callback Error, errorCode: ${err.code}\`);
      return;
    }
    console.info(\`onTorchStatusChange, isTorchAvailable: ${torchStatusInfo.isTorchAvailable}, isTorchActive: ${torchStatusInfo.
      isTorchActive}, level: ${torchStatusInfo.torchLevel}\`);
  });
}
