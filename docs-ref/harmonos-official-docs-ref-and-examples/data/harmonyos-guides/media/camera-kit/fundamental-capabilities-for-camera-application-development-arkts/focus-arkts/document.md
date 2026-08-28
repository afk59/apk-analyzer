# Focus (ArkTS)

The camera framework offers capabilities for focusing, enabling applications to configure focus modes and focus points based on specific use cases.

#### How to Develop

For details about the APIs, see [Camera API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera).

1.  Import the NDK APIs.
    
    import { camera } from '@kit.CameraKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call [isFocusModeSupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-focusquery#isfocusmodesupported11) to check whether the device supports a focus mode.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/pRVdODC_RKerdpz-GOQhfQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062039Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2C3F7A1C5DB96598E54AA9A9D115FE9D883305B8FAB1DA0BA5FD396C3B0F880)
    
    This operation must be performed after the session calls [commitConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session#commitconfig11) to complete stream configuration.
    
    function isFocusModeSupported(photoSession: camera.PhotoSession): boolean {
      let status: boolean = false;
      try {
        // Check whether the autofocus mode is supported.
        status = photoSession.isFocusModeSupported(camera.FocusMode.FOCUS\_MODE\_AUTO);
      } catch (error) {
        // If the operation fails, error.code is returned and processed.
        let err = error as BusinessError;
        console.error(\`The isFocusModeSupported call failed. error code: ${err.code}\`);
      }
      return status;
    }
    
3.  Call [setFocusMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-focus#setfocusmode11) to set the focus mode.
    
    If autofocus is used, you can call [setFocusPoint](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-focus#setfocuspoint11) to set the focus point. The camera triggers autofocus based on the focus point.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/Otio_NZATHWbrAyJJ5zJiw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062039Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0701C43D83FE5805DFBC9534AC3F004CD7C3D48C00876E4713097F3075ADAE1B)
    
    This operation must be performed after the session calls [commitConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session#commitconfig11) to complete stream configuration.
    
    function setFocusMode(photoSession: camera.PhotoSession): void {
      const focusPoint: camera.Point = {x: 1, y: 1};
      try {
        // Set the autofocus mode.
        photoSession.setFocusMode(camera.FocusMode.FOCUS\_MODE\_AUTO);
        // Set the focus point.
        photoSession.setFocusPoint(focusPoint);
      } catch (error) {
        // If the operation fails, error.code is returned and processed.
        let err = error as BusinessError;
        console.error(\`The setFocusMode and setFocusPoint call failed. error code: ${err.code}\`);
      }
    }
    

#### Status Listening

During camera application development, you can listen for camera focus status changes at any time.

Obtain the listening result by registering the callback function of [focusStateChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-photosession#onfocusstatechange11). This event is triggered only when the camera focus status changes in autofocus mode.

function onFocusStateChange(photoSession: camera.PhotoSession): void {
  photoSession.on('focusStateChange', (err: BusinessError, focusState: camera.FocusState) => {
    if (err !== undefined && err.code !== 0) {
      console.error(\`focusStateChange error code: ${err.code}\`);
      return;
    }
    console.info(\`focusStateChange focusState: ${focusState}\`);
    // To ensure user experience of the focus function, you can set the focus mode to continuous autofocus after autofocus is successful, meeting the focus requirement in a complex photographing scenario.
    if (focusState === camera.FocusState.FOCUS\_STATE\_FOCUSED) {
      photoSession.setFocusMode(camera.FocusMode.FOCUS\_MODE\_CONTINUOUS\_AUTO);
    }
  });
}
